---
title: Automatic Numbering
slug: automatic-numbering
part: Compiling
sequence: 3
tags:
  - compile
  - numbering
  - placeholders
  - chapters
difficulty: intermediate
status: draft
---

# Automatic Numbering

## Fast answer

Automatic numbering uses placeholders so Scrivener can generate chapter, part, figure, table, or hierarchical numbers at compile time.

## Why this matters


Manual numbering is fragile.

If you type chapter numbers yourself, every structural change creates cleanup work. Automatic numbering lets Scrivener calculate numbers during compile, after the project has been assembled.

This matters for:

- chapter numbers
- part numbers
- appendix numbers
- figure numbers
- table numbers
- legal/technical outlines
- hierarchical structures


## Core workflow


Basic pattern:

```text
Chapter <$t>
```

Possible compiled result:

```text
Chapter One
```

A numeric chapter heading might use:

```text
Chapter <$n>
```

For independent numbering streams, name the stream:

```text
Part <$t:part>
Chapter <$t:chapter>
Figure <$n:figure>
Table <$n:table>
```

Use named streams when different categories need independent numbering.


## Common mistakes


### Manual numbering

Manual numbering breaks when you rearrange chapters.

### Using one stream for everything

Parts, chapters, figures, and tables usually need separate streams.

### Forgetting front matter

Front matter can accidentally consume numbering if placeholders appear there.

### Not testing after rearranging

Reordering Binder items can affect numbering.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Restarting numbering

Use restart placeholders when a stream must begin again.

Examples:

```text
<$rst>
<$rst_n>
<$rst_chapter>
```

## Hierarchical numbering

Hierarchical numbering is useful for technical work:

```text
<$hn>
<$ahn>
<$aon>
```

This can produce outline-style numbers such as:

```text
2
2.1
2.1.3
```

## Figure and table references

For robust figure/table references, use named streams and keywords:

```text
Figure <$n:figure:mapA>
See Figure <$n#figure:mapA>.
```

The first placeholder generates the number. The second refers back to it without incrementing.


## Related pages

- [Using Placeholders](04-using-placeholders.md)
- [List of all Placeholders](05-list-of-all-placeholders.md)
- [Transformations & Replacements](17-transformations-and-replacements.md)
