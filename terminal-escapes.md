#!/bin/env slides

# Demystifying Terminal Escapes

*by Bruce Hill*

--------------------------------

Have you ever wondered how Vim and other
command-line programs manage to do cool
stuff with your terminal?

Like drawing all over the place without
cluttering your command line history?

--------------------------------

Well, it's not magic, and you can do it too!

-------------------------------

There are three main topics I'll cover:

1. Printing terminal escape sequences
2. Getting and setting terminal information

-------------------------------

Most terminal emulators that you use
(iTerm, alacritty, GNOME terminal, etc)
are emulating old-school physical terminals
like the VT100:

```demo
firefox --new-window https://en.wikipedia.org/wiki/VT100
```

-------------------------------

The way that terminals used to work is that
you would send bytes from a computer over
a wire to a terminal (the termination point
of the signal).

## Commonly Sent

- Text to print
- Escape sequences

-------------------------------

# Escape Sequences

In order to do stuff like move the cursor
around, clear the screen, etc. you could
send an escape sequence to the terminal.

One common escape sequence you might know
is the newline `\n` and carriage return `\r`
escapes. These moved the carriage on a
teletype to the next line or back to the
start of a line.

```demo
term
```

-------------------------------

# Operating System Commands

More advanced escape sequences like
**Operating System Commands** let you
do more fancy stuff like moving the
cursor position to an arbitrary X/Y
position or setting the text color.

The magic **Operating System Command** is two bytes:

```
\033[
```

Also known as `\x1B[` or `\e[`.

```
\033[
```

It tells the terminal that the next
thing that follows isn't text to print
but is a command that needs to run.

-------------------------------

Here are some fun operating system commands:

```demo
ansi | less -R
```

*You can run these yourself with just a print statement!*

-------------------------------

Here's what's actually getting sent to the terminal:

```demo
ansi | less
```

-------------------------------

# Alternate Screens

One of the most important operating system commands
is toggling the alternate screen on and off:

```
Alternate screen on:
\033[?1049h

Alternate screen off:
\033[?1049l
```

This is what lets you run a terminal program
that doesn't spam the scrollback log!

-------------------------------

# Getting and Setting Info

In C, there are some functions that let you
get information about the terminal

-------------------------------

## tcgetattr/tcsetattr

Useful for reading one keypress at a time!

```c
int tcgetattr(int fd, struct termios *termios_p);
int tcsetattr(int fd, int optional_actions,
              const struct termios *termios_p);
void cfmakeraw(struct termios *termios_p);
```

```demo
man tcsetattr
```

-------------------------------

## ioctl

Useful for getting terminal width/height!

```c
int ioctl(int fd, int op, ...);
```

```demo
man ioctl
```

-------------------------------

# BTUI

I wrote a library called **BTUI**
to do the bare minimum of this stuff:

```demo
firefox --new-window https://github.com/bruce-hill/btui
```

(I really don't like ncurses, it's very bloated and unwieldy)


-------------------------------

# slides

This presentation is made using the BTUI library
and its Python bindings.

Thanks to Michael Rees for the idea
to make a terminal slide presenter!

```demo
firefox --new-window https://github.com/bruce-hill/slides
```

-------------------------------

# Goodbye!

Thanks for your time!
I'm **Bruce Hill** if you want to find me on zulip.

-------------------------------

# Bonus Demo 1: Conway's Game of Life

```demo
conway
```

-------------------------------

# Bonus Demo 2: Double Pendulum

```demo
2pend
```

-------------------------------

# Bonus Demo 3: Space Invaders

```demo
cd ~/software/btui/Python/invaders
./invaders.py
```

-------------------------------

# Bonus Demo 4: Alternate Character Set

```demo
alternate-character-set | less -r
```
