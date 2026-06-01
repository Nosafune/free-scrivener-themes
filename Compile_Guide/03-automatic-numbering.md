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
---

# Automatic Numbering

## Fast answer

Automatic numbering uses placeholders so Scrivener generates chapter, part, figure, or table numbers at compile time rather than requiring manual typing.

## Why this matters

Manual chapter numbers break every time you add, remove, or reorder a chapter. Automatic numbering lets Scrivener calculate numbers during compile, after the project is fully assembled. You never renumber by hand.

## Basic patterns

Arabic numeral: `Chapter <$n>`

Title-case word: `Chapter <$t>` -- compiles to: One, Two, Three, ...

Uppercase Roman: `Part <$R>`

## Named streams

When different categories need independent numbering, use named streams:

```
Part <$t:part>
Chapter <$t:chapter>
Figure <$n:figure>
Table <$n:table>
```

Each stream counts independently. Part Two, Chapter Seven, and Figure 3 can coexist correctly.

## Restarting numbering

Use restart placeholders when a stream must begin again:

```
<$rst_chapter>
```

Place the restart placeholder in the Section Layout for the document that should trigger the reset -- for example, the opening scene after a Part divider.

## Hierarchical numbering

For technical or academic work:

```
<$hn>     ->  2, 2.1, 2.1.3
<$ahn>    ->  B, B.1, B.1.3
<$aon>    ->  2, 2.a, 2.a.i
```

## Cross-references

To create a numbered label and refer back to it without incrementing:

```
Figure <$n:figure:mapA>       <- generates and assigns the number
See Figure <$n#figure:mapA>.  <- refers to the same number
```

## Common mistakes

**Typing numbers manually.** They break on every structural change.

**Using one stream for everything.** Parts, chapters, figures, and tables need separate streams.

**Front matter consuming the stream.** If a placeholder appears in a front matter document, it increments the counter. Use different streams or exclude front matter from compile.

**Not testing after reordering.** Restructuring the Binder changes numbering. Always run a test compile after reorganizing.

## Related pages

- [Using Placeholders](04-using-placeholders.md)
- [List of all Placeholders](05-list-of-all-placeholders.md)
- [Transformations & Replacements](17-transformations-and-replacements.md)
