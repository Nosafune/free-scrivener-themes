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
---

# Statistics & Tables

## Fast answer

Statistics are inserted via placeholders that resolve at compile time. Tables require special attention because output formats handle them very differently.

## Statistics placeholders

These resolve during compile, not while you are writing:

```
<$wc>          total word count
<$wc100>       word count rounded to nearest 100
<$cc>          character count
<$doccount>    number of compiled documents
<$draftTarget> project draft target
```

Place statistics in front matter, title pages, or metadata fields where they will be useful to the reader or publisher.

## Table workflow

1. Create simple tables where possible (avoid excessive nesting and merged cells).
2. Compile a test with the table included.
3. Open the output in the target application.
4. Inspect column widths, line breaks, and cell content.
5. For ebooks, test on multiple readers.

## Table format survival rules

- Keep column count low.
- Avoid very long cell text.
- Avoid merged cells where possible.
- Test in the final output format before assuming the table is usable.
- For print-only complex tables, consider an image instead of a live table.

## Format risk by output type

| Format | Table risk |
|---|---|
| Word | Generally reliable |
| PDF | Generally reliable |
| EPUB | High -- reflowable layout breaks wide fixed tables |
| Plain text | Tables are stripped entirely |

## Common mistakes

**Complex tables in ebooks.** Wide fixed-column tables almost always break in reflowable EPUB output. Simplify or use an image.

**Assuming statistics update in the Editor.** `<$wc>` counts compiled words at export time. It does not match the live Editor word count unless the compile includes the same documents.

**Not testing in the target app.** A table that looks fine in Scrivener's preview may reflow badly in Word or break entirely in an ebook reader.

## Related pages

- [Using Placeholders](04-using-placeholders.md)
- [Compatibility](21-compatibility.md)
- [Page Settings](20-page-settings.md)
