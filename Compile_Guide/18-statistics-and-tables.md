---
title: Statistics & Tables
slug: statistics-and-tables
part: Compiling
sequence: 18
tags:
  - compile
  - statistics
  - tables
  - placeholders
difficulty: intermediate
status: draft
---

# Statistics & Tables

## Fast answer

Statistics and tables require special attention because output formats handle counts, table structure, and layout differently.

## Why this matters


Statistics in Compile may include word count, character count, document count, or project targets through placeholders.

Tables are more fragile because they depend heavily on output format.

This topic matters most for:

- nonfiction
- academic work
- technical documentation
- reports
- books with figures/tables
- appendices


## Core workflow


Statistics workflow:

1. Decide whether statistics belong in the compiled output.
2. Use placeholders such as `<$wc>` or `<$doccount>`.
3. Place them in front matter, title page, or metadata as needed.
4. Compile and verify.

Table workflow:

1. Create simple tables where possible.
2. Avoid excessive nesting.
3. Test in target output.
4. Inspect column widths and line breaks.
5. For ebooks, test on multiple readers.


## Common mistakes


### Complex tables in ebooks

Reflowable ebooks are bad at wide fixed tables.

### Assuming counts update in the Editor

Statistics placeholders resolve during compile.

### Overdesigning tables

Simpler tables survive export better.

### Ignoring target format

A table that works in Word may fail in EPUB.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Useful statistics placeholders

```text
<$wc>
<$wc100>
<$cc>
<$doccount>
<$draftTarget>
<$sessionTarget>
```

## Table survival rules

- keep columns few
- avoid very long cell text
- avoid merged cells where possible
- test in the final output format
- consider images for complex fixed tables in print-only outputs


## Related pages

- [Using Placeholders](04-using-placeholders.md)
- [Compatibility](21-compatibility.md)
- [Page Settings](20-page-settings.md)
