---
title: Tomo Deep Dive
author: Bruce Hill
---

# Quick Introduction

Tomo is the programming language I've been working on since 2020. It first
started as a pandemic hobby project, but it's grown a lot since then. Tomo is a
statically typed, garbage-collected, imperative language that cross-compiles to
C, with a focus on safety, simplicity, and speed. Roughly speaking, it's in the
same ballpark as Go, but with many safety and convenience features that Go
lacks, as well as easy interoperability with C code.

A Tomo program looks something like this:

```tomo
func greeting(name:Text, add_exclamation:Bool -> Text)
    message := "hello $name"
    capitalized := " ".join([
        w.title() for w in message.split_any(" ")
    ])
    if add_exclamation
        capitalized ++= "!!!"
    return capitalized

func main(name:Text, shout=no)
    to_say := greeting(name, add_exclamation=shout)
    say(to_say)
```

# The Tomo Compiler Pipeline

The compiler for Tomo is mainly written in C, and between the compiler and the
standard library, there are about 20,481 lines of C code split across 77 files.

At a high level, each Tomo program is transpiled into a C header file and a C
source file. Then, a C compiler (such as GCC) is used to compile that file into
an object file and link it against the Tomo standard library to produce a final
binary, which can be executed. Additionally, the compiler auto-generates code to
do command line argument parsing for the `main()` function, so that code is
generated, compiled, and linked in as well. The process looks something like
this:

```
  +----------+  transpile   +------------+  generate arg parser   
  | foo.tm.h | <----------- |   foo.tm   | -------------
  +----------+              +------------+              |
    |    |                    | transpile               |
    |    |                    v                         |
    |    |                  +------------+              |
    |    |                  |  foo.tm.c  |         +--------------------+
    |    |                  +------------+         | main() entry point |
    |    |                    |                    +--------------------+
    |    |          compile   v                         |
    |    |                  +------------+              |
    |    +----------------->|  foo.tm.o  |              |
    |                       +------------+              |
    |                         | link                    |
    |                         v                         |
    |          compile      +------------+  compile     |
    +---------------------> |    foo     | <------------+
                            +------------+
```

This process also extends to Tomo files that import other Tomo files. When
multiple files are involved in compilation, the compiler will lazily compile all
downstream dependencies as needed, in parallel. Compilation follows these rules:

 1) Header files are a dependency for many parts of the process, so it's
    good to transpile them as early as possible.
 2) Once all the header files are available, the C source files are
    compiled into their object files in parallel. This is by far the
    slowest part of compilation (invoking the C compiler), so it benefits
    the most from parallelization.
 3) After all object files are compiled, the last step is to link them
    all together (fast and simple).

To satisfy these requirements as efficiently as possible, the approach taken
below is to first transpile all header files sequentially (this could be
parallelized, but is faster than the overhead of forking new processes), then
fork a new process for each dependency to transpile and compile it to an object
file. Then, wait for all child processes to finish and link the resulting object
files together.

\newpage

## Phase 1 (sequential transpilation):

```
          +--------+       +--------+
          | foo.tm |       | baz.tm |
          +--------+       +--------+
              |              |   | 
              +--------------+   |
              |                  |
              v                  v
         +----------+      +----------+
         | foo.tm.h |      | baz.tm.h |
         +----------+      +----------+
```

## Phase 2 (parallel transpilation/compilation):

```
 ################################    ################################
 #           Process 1          #    #           Process 2          #
 #   +--------+   +----------+  #    #  +----------+   +--------+   #
 #   | foo.tm |   | foo.tm.h |  #    #  | baz.tm.h |   | baz.tm |   #
 #   +--------+   | baz.tm.h |  #    #  +----------+   +--------+   #
 #       |        +----+-----+  #    #         |           |        #
 #       v             |        #    #         |           v        #
 #  +----------+       |        #    #         |      +----------+  #
 #  | foo.tm.c |       |        #    #         |      | baz.tm.c |  #
 #  +----------+       |        #    #         |      +----------+  #
 #       |             |        #    #         |        |           #
 #       +------+------+        #    #         +--------+           #
 #              |               #    #                  |           #
 #              v               #    #                  v           #
 #        +----------+          #    #            +----------+      #
 #        | foo.tm.o |          #    #            | baz.tm.o |      #
 #        +----------+          #    #            +----------+      #
 ################################    ################################
```

## Phase 3 (linking a shared object file library):

```
   +----------+      +----------+
   | foo.tm.o |      | baz.tm.o |
   +----------+      +----------+
        |                 |
        +--------+--------+
                 |
                 v
           +-----------+
           | libfoo.so |
           +-----------+
```

## Phase 3 (linking an executable):

```
   +----------+      +----------+   +--------+  +--------+
   | foo.tm.o |      | baz.tm.o |   | foo.tm |  | baz.tm |
   +----------+      +----------+   +--------+  +--------+
        |                 |              |          |
        +--------+--------+              +----+-----+
                 | link                       | Figure out command line args
                 v                            v
              +-----+    compile   +-------------------------+
              | foo |<-------------| main() function for exe |
              +-----+              +----------+--------------+
                                   | foo.tm.h |
                                   +----------+
                                   | baz.tm.h |
                                   +----------+
```

# Lazy Compilation

The compilation model used for Tomo not only splits compilation into separate,
parallel compilation units, but it also handles lazy recompilation lazily using
an approach similar to Make. A file is considered stale if any of its
dependencies have been modified more recently than it has. Under this approach,
each Tomo source file is scanned to check for which files it depends upon,
rather than having a separate build configuration file. Each object file depends
on the transpiled C header and source files, and the C header and source files
depend on the Tomo source file, as well as its dependencies. The upshot of this
approach is that if only one file in the dependency tree is modified, only that
file and its dependants need to be recompiled, rather than recompiling the
entire project. For larger projects, this drastically speeds up incremental
recompilation.

# Rationale and Alternatives

One of the goals of Tomo was to bring some of the best elements of C into a
modern language that cares about safety. One of C's strengths is the ability to
split a large project into separate compilation units. Some hobby (or even
professional) programming languages take the simpler approach of lumping an
entire project into a single compilation unit and compiling everything in one
big pass. This approach makes building a compiler simpler (you can just treat
multiple files as one big file), but it means that you end up with dramatically
worse compilation times--firstly because you must always recompile the entire
project, secondly because it's much harder to parallelize compilation without
cleanly defined separate compilation units, and thirdly because optimization
times tend to blow up when giving the optimizer an arbitrarily large program.
Since one of my goals with Tomo is to provide a better language experience than
existing programming languages, I opted to take the harder route to provide a
much snappier user experience that will provide a competitive advantage for the
language and hopefully win over users!
