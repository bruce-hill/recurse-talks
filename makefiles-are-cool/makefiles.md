#!/bin/env slides

# Makefiles Are Cool

_By Bruce Hill_


--------------------------

# First Experiences with Makefiles Suck

![sxiv -sf -f](bosch.jpg)

- Some college course gave you this thing that magically
  makes your code compile.
- Some open source project has an autogenerate script that
  makes a 20,000 line makefile.
- Configuration options are often poorly documented.
- Just run `make` and pray it works.

--------------------------

# Actually Make Is Good

- Really useful for small projects
- Not just compiling C code
- Anything where files are used to make other files

--------------------------

# What Even Is Make?

![](tinybrain.png)

`make` is a command you run to compile stuff.

--------------------------

# What Even Is Make?

![](brain.png)

`make` is a bunch of similar programs (most commonly GNU)
that look at files and determines which files need to be
rebuilt and how.

--------------------------

# What Even Is Make?

![](bigbrain.png)

`make` is a domain specific programming language
and interpreter for expressing dependency trees
and production rule systems.

--------------------------

# What Even Is Make?

![](galaxybrain.png)

`make` is a lightweight way to have files turn
into other files lazily using simple rules.

--------------------------

# Makefiles

When you run `make`, it looks for a file called
`Makefile` or `makefile` with a set of rules.

Each rule has the format:

```make
output: input1 input2 input3...
    how to build...
```

The body of the rule is a _shell script_

**The rule will only run if any of the input files has
been modified more recently than the output file!**

----------------------------

# Simple Example

```make
sorted_names.txt: names.txt
    sort names.txt > sorted_names.txt
```

If you ever modify `names.txt`, you can run
`make sorted_names.txt` to create the sorted names file.

If you don't want to retype the filename, you can use
the variables `$<` (input files), `$@` (output file),
and `$^` (first input file):

```make
sorted_names.txt: names.txt
    sort $< > $@
```

-----------------------------

# Another Example

Run a python script to draw an image:

```make
graph.png: plot_graph.py graph_module.py
    python3 $^
```

This will re-run if either `plot_graph.py` or
`graph_module.py` is edited.

----------------------------

# Dependency Trees

Rules can form dependency trees:

```make
graph.png: plot_graph.py data.csv
    python3 plot_graph.py data.csv

data.csv: raw_data.bin
    convert_bin_to_csv raw_data.bin
```

Running `make graph.png` will first make sure that
`plot_graph.py` and `data.csv` are up-to-date,
then make sure that `graph.png` is up-to-date.

Rules are **lazy**, so if you edit `plot_graph.py`, but
don't touch `raw_data.bin`, then running `make graph.png`
won't run `convert_bin_to_csv` because it's not necessary.

----------------------------

# Phony Rules

Sometimes you have a rule that doesn't actually have
a file ouput.

You can use `.PHONY` to tell `make` to not bother looking
for a file with that name.

Most commonly used for `all`, `clean`, and `install`:

```make
.PHONY all clean install

all: sorted_names.txt graph.png

clean:
    rm sorted_names.txt graph.png

install: sorted_names.txt graph.png
    cp $< /etc/cool-files/
```

**Note 1:** a rule with no body just means "I need these
files to be built using their rules, but I don't do anything
in particular"

**Note 2:** when you run just `make` with no arguments, it
runs the _first_ rule in the file, which is usually `all`

----------------------------

# Pattern Rules

If you put a `%` in the name, you can do reusable pattern
rules that work for different filenames.

## Turn Markdown Files into PDFs

```make
%.pdf: %.md
    pandoc $< -o $@
```

## Compile C Code

```make
%.o: %.c %.h
    cc -c $^ -o $@
```

-----------------------------

# Defining Variables

You can define variables that are reused in different
rules like this:

```make
O=-O2
CFLAGS=-Wall -Werror $O

all: program

program: main.c foo.o baz.o
    cc $CFLAGS $< -o $@

%.o: %.c %.h
    cc $CFLAGS -c $^ -o $@
```

When running `make` you can override these variables if you
want to:

```bash
make O=-O1 CFLAGS='-Weverything -Werror' all
```

**Warning:** changing the variables does not change file
modification times, so `make` won't know stuff needs to
be rebuilt with different flags.

--------------------------------

# My Website

I use a makefile to build my website and blog:

- `pandoc` to make HTML files from markdown files.
- A janky bash script to make an RSS feed from my blogposts.
- `gzip` to compress my CSS files.
- `rsync` PHONY rule to send files to my server.

![](website_makefile.make)

--------------------------------

# Not Covered

There's a bunch of stuff not covered in the talk:

- Platform-dependent variables
- Pattern matching variables (get all the files of a type)
- Built-in rules (you can run `make` even without a makefile)
- Silent commands with `@`
- [Read the docs](https://www.gnu.org/software/make/manual/html_node/index.html)
- You can use pandoc to make a website
- You can use pandoc to make manpages for programs
- You can use pandoc for anything
- Please don't make scripts to autogenerate 10K+ line makefiles

-------------------------------

# The End

Thanks! Hope you try using simple
Makefiles for your own projects!
