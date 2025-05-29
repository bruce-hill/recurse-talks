#!/bin/env slides

# The Awk Talk

_Bruce Hill_
(RC Spring 1 2025)

---

# What Is

`awk` is a command line program, but also a programming
language for doing stuff with streams of lines of text.

---
 
# Awk Structure

An awk program is a series of short programs
with an optional condition, followed by an 
optional action.

```
program <- statement+
statement <- condition action / condition / action
condition <- "/"regex"/" / expression
action <- "{" code "}" 
```

---

# Patterns

A common condition is a pattern match that
succeeds on lines that match the pattern.

For example, `awk '/foo[0-9]/'` will print lines
that match the regex `foo[0-9]`

The default action if you don't specify anything
is **print the line**

---

# Actions

If you want to do something other than just printing the
line, you can specify an action in curly braces.

One of the most common things to do is print different
_fields_ from a line. This can be done with `$1`, `$2`, etc.
(`$0` is the whole line).

For example, if you wanted to see a list of the owners of
all the files in `/tmp` you could do:

```bash
ls -l /tmp | awk '{print $3}'
```

---

# Field Separators

Awk also lets you specify different field separators besides
whitespace (e.g. commas).

```
awk -F ',' '{print $2}'
```

---

# Some Neat Conditions

Here are some helpful conditions:

- `BEGIN`: runs before the first line
- `END`: runs after the last line
- `NR==100`: runs on a specific line number 

You can imagine how awk can be easily used to replace `head`
and `tail`: `awk 'NR<=10'`

---

# Handy awk Tricks

Awk is very loosey goosey about types.
There are basically two types: associative arrays and
strings.

Strings do numbery stuff and all variables can be used
without initializing.

Here's a simple example:

```
awk '/foo/{count+=1} END{print count}'
```

(Count the lines matching `/foo/`)

---

# Associative Arrays

These are basically a one-stop-shop for arrays and dicts.

You can also use associative arrays without initializing:

```demo
tr ' ' '\n' < raven.txt | \
awk '
/./{count[$0]+=1}
END{
  asorti(count);
  for(w in count)
    print count[w], w
}' | head -10

ask
```

---

# Conclusion

Awk is pretty cool and it's a full programming language.
Next time you have a command line task to solve, consider
reaching for awk.

But if you get to the point where you are investigating
how to store a large awk program in a file, you've maybe
gone too far down the rabbit hole.
