#!/bin/env slides

# OpenBSD, pledge(), and unveil()

_By Bruce Hill_

```
            _.-|-/\-._     
         \-'          '-.    
        /    /\    /\    \/          _____                 ____   _____ _____  
      \/  <    .  >  ./.  \/        / ___ \               |  _ \ / ____|  __ \ 
  _   /  <         > /___\ |.      / /  / /___  ___  ____ | |_) | (___ | |  | |
.< \ /  <     /\    > ( #) |#)    / /  / / __ \/ _ \/ __ \|  _ < \___ \| |  | |
  | |    <       /\   -.   __\   / /__/ / /_/ /  __/ / / /| |_) |____) | |__| |
   \   <  <   V      > )./_._(\  \_____/ .___/\___/_/ /_/ |____/|_____/|_____/ 
  .)/\   <  <  .-     /  \_'_) )-..   /_/                                    
      \  <   ./  /  > >       /._./
      /\   <  '-' >    >    /   
        '-._ < v    >   _.-'
          / '-.______.-' \
                 \/
```

(Puffy the OpenBSD mascot)

---------------------------------

# OpenBSD

- BSD = Berkeley Software Distribution
  - Also known as "Berkeley Unix"
  - MacOS is based on BSD

```demo
sxiv -sf -f os-family-tree.png
```

- Kinda like Linux, but cooler!
  - Better security
  - Simpler design
  - ...but maybe worse for personal computing
  - But great for web servers!
- My website runs on OpenBSD!

----------------------------------

# Linux Analogy

The BSD Family:

- **FreeBSD:** the _Ubuntu_ of the BSD family
  - Relatively user-friendly
  - Good for desktops
- **NetBSD:** the _Linux Mint_ of the BSD family
  - Very portable
  - Good for low-resource machines
- **OpenBSD:** the _Arch/Qubes_ of the BSD family
  - Great documentation (manpages)
  - **High emphasis on security**

--------------------------------------

# OpenBSD

- Probably more secure than any OS you've ever used
  - Maybe Qubes is a contender? Debatable.
- Really excellent code quality
  - Great learning resource
- Ports collection for package management
  - Very cool, but out of scope for today
- Numerous security improvements exported to other platforms:
  - OpenSSH
  - `strlcpy()`
  - `arc4random()`
- Some security improvements that **should** be exported:
  - `unveil()`
  - `pledge()`

-------------------------------------

# Tangent: Release Artwork

![sxiv -sf -f](openbsd-7.6.jpg)

-------------------------------------

# Tangent: Release Artwork

[Every OS release has artwork and music made by the community](https://www.openbsd.org/artwork.html)

Every six months since 1996!

-------------------------------------

# Defense in Depth

OpenBSD operates on the assumption that users
**will** write and run software with bugs.

**What happens next will amaze you!**

When a program starts, it has some idea of what the
expected behavior will be.

- Which files or directories it needs to access
- Which system calls will be needed
- What _kind of thing_ the program is doing

The idea is to **pre-commit** to only doing those things.

If a program has a bug that allows for unintended behavior,
**OpenBSD will limit the fallout of that bug.**

----------------------------------

# Unveil

```c
int unveil(const char *path, const char *permissions)
```

When a program starts, it can restrict itself
to certain parts of the filesystem with `unveil()`

- Limit which files and directories the program can see
- Change whether the program has read/write/execute permissions on files

This is **enforced by the OS** and it will cause
system calls like `open()` to return error values as
if those files didn't exist or didn't have those
permissions.

Unveil is **additive** so once you call it, it
closes off access to all files on the filesystem
except the ones you _add_ access to.

```demo
less unveil.txt
```

----------------------------------

# Chroot Jail Comparison

`unveil()` is similar to `chroot`, but much, much
easier to use.

**Chroot:**

- Run a program in a fake (restricted) filesystem
- Only include copies of stuff you want
- Run your program so it thinks that is the whole filesystem
- Annoying to set up
- Requires copying files

**Unveil:**

- Selectively mask off parts of the existing filesystem
- Easy to add a few function calls or wrap a program
- Don't need to copy any files
- Can easily do read-only or write-only access

----------------------------------

# Using unveil()

`unveil()` is a drop-in security measure that can make
a program more secure _without invasive changes._

You _just_ have to add a call to `unveil()` to the
top of your program and any program that correctly
handles non-existent files works as you would hope.

```python
def buggy_write_to_tempfile(filename: str, contents: str):
    with open("/tmp/" + filename, "w") as f:
        f.write(contents)

# Uh oh!
buggy_write_to_tempfile("../etc/passwd", "Oh no")
```

Let's make it secure:

```python
import openbsd
openbsd.unveil("/tmp", "rw")

# Now this is safe(r)!
buggy_write_to_tempfile("../etc/passwd", "Oh no")
```

Now we can't read or write any file outside of `/tmp`!

----------------------------------

# Pledge

```c
int pledge(const char *promises, const char *execpromises)
```

`pledge()` lets you restrict which **system calls**
the current program is allowed to make (and which
ones any child processes can make).

Some interesting permissions:

- `stdio`: do standard I/O operations like reading `stdin` and printing to `stdout`
- `rpath`: perform **read-only** operations on the filesystem (e.g. `cat`)
- `wpath`: perform **write-only** operations on the filesystem (e.g. a logger)
- `inet`: do networking stuff like access the internet
- `exec`: execute other programs
- `unveil`: call `unveil()` to allow access to more files **(!!!)**

```demo
less pledge.txt
```

----------------------------------

# Pledge Case Study: Echo

The `echo` program in the OpenBSD codebase
(slightly modified)

```c
int main(int argc, char *argv[]) {
    if (pledge("stdio", NULL) == -1)
        err(1, "pledge");

    while (*argv) {
        (void)fputs(*argv, stdout);
        if (*++argv)
            putchar(' ');
    }
    putchar('\n');

    return 0;
}
```

Even if there were a bug in this program, it is
_near impossible_ for the program to do anything other
than read `stdin` and print to `stdout`!

----------------------------------

# Pledge Narrowing: cat

Another useful technique is to start with maximum
permissions and gradually drop permissions as you go.

Here's a [simplified](https://github.com/openbsd/src/blob/master/bin/cat/cat.c) version of `cat`:

```c
int main(int argc, char *argv[]) {
        pledge("stdio rpath", NULL);

        FILE *f = argc == 1 ? stdout : fopen(argv[1], "r");

        // Don't need FS read permissions anymore
        pledge("stdio", NULL);

        char buf[100];
        size_t just_read;
        while ((just_read=fread(buf, 1, sizeof(buf), f)) > 0)
                fwrite(buf, 1, just_read, stdout);

        fclose(f);
        return 0;
}
```

**💀 BAD PRACTICE: not checking return values 💀**

----------------------------------

# Combined pledge/unveil Example

From `fsck.c`, which checks the filesystem:

```c
if (unveil("/dev", "rw") == -1)
    err(1, "unveil /dev");
if (unveil("/etc/fstab", "r") == -1)
    err(1, "unveil %s", _PATH_FSTAB);
if (unveil("/sbin", "x") == -1)
    err(1, "unveil /sbin");
if (pledge("stdio rpath wpath disklabel proc exec", NULL) == -1)
    err(1, "pledge");
```

It can:

1. Read and write to `/dev`
2. Read `/etc/fstab`
3. Run programs in `/sbin`
4. Do I/O, filesystem stuff, and run programs from `/sbin`

It cannot:

1. Access password files
2. Read from user's home directory
3. Write files anywhere besides `/dev`
4. Connect to the internet
5. Kill other processes
6. **Change my `pledge()`/`unveil()` permissions further (!!!)**

----------------------------------
# Case Study: Firefox

>Firefox on OpenBSD is secured with pledge(2) and unveil(2)
>to limit the system calls and filesystem access that each
>of Firefox's process types (main, content, remote data decoder,
>audio decoder, socket and GPU) is permitted.
>**By default, only ~/Downloads and /tmp can be written to**
>when downloading files, or when viewing local files
>as file:// URLs.

Even if there are bugs in a massive program like Firefox,
the scope of the damage an attacker could do is limited!

----------------------------------

# Conclusion

I hope you think these security tools are as cool as I do!

OpenBSD is a really great OS to run on a web server where
you care a lot about security!

Most of the built-in software that ships with the OS makes
good use of `pledge()` and `unveil()` to give you better
security!

Try it yourself sometime! It's mostly familiar to Mac/Linux
users, but with a few galaxy brain ideas.

----------------------------------

# The End

_Thanks for your time!_

----------------------------------

# Footnote 1: Code Quality

Compare OpenBSD's implementation of `true`:

![OpenBSD - true.c](openbsd-true.c)

With the GNU Coure Utilities implementation used in Linux:

![GNU Core Utilities - true.c](coreutils-true.c)

----------------------------------

# Footnote 2: Code Quality

OpenBSD comes with `doas`, which is under 500 lines of code:

```
*******************************************************************************
Language                     files          blank        comment           code
*******************************************************************************
C                                1             55             19            424
*******************************************************************************
```

The `sudo` that comes with Linux is nearly a quarter million lines of code!

```
*******************************************************************************
Language                     files          blank        comment           code
*******************************************************************************
C                              468         18,038         28,119        132,203
PO File                         74         30,350         48,907         78,866
Bourne Shell                    94          8,868          6,387         51,341
m4                              24           1336            607         14,761
...
*******************************************************************************
SUM:                           717         59,673         85,426        284,387
*******************************************************************************
```

[More lines of code = more risk of vulnerabilities](https://www.alibabacloud.com/help/en/ecs/vulnerability-announcement-or-linux-sudo-permission-vulnerability)

