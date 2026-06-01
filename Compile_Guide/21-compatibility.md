---
title: Compatibility
slug: compatibility
part: Compiling
sequence: 21
tags:
  - compile
  - compatibility
  - export
  - file-types
difficulty: intermediate
---

# Compatibility

## Fast answer

Compatibility settings handle output-format limitations and conversion behavior between Scrivener and external formats. Every output format has constraints -- Compatibility lets you manage them.

## Why this matters

The same manuscript behaves differently in Word, PDF, EPUB, RTF, and plain text. Scrivener must translate its internal document model into another file model, and that translation is imperfect for complex content.

Compatibility settings give you control over how that translation happens for features like styles, footnotes, tables, images, and special characters.

## Representative test sample

Before finalizing any output format, compile a short sample that includes:

- a heading
- normal body text
- styled text (block quote or similar)
- a footnote
- a comment
- an image
- a table
- an internal link

Open the result in the real target application. Problems that do not appear in Scrivener's preview will appear here.

## Format risk table

| Feature | Risk |
|---|---|
| Footnotes | Behavior varies significantly by output |
| Comments | May be omitted, transformed, or appear unexpectedly |
| Tables | Fragile in reflowable ebooks |
| Images | Size and anchoring vary by format |
| Page numbers | Meaningless in reflowable ebooks |
| Styles | May map differently across output types |
| Internal links | Format-dependent; test in each output |
| Headers/footers | Fixed-page formats only |

## Fixed-page vs reflowable

Fixed-page formats (PDF, Word, Print) ask: **Where does this sit on the page?**

Reflowable formats (EPUB) ask: **What is this content semantically?**

These are fundamentally different questions. Settings that make sense for one are often meaningless or counterproductive for the other.

## Common mistakes

**Assuming all file types preserve all features.** They do not. Complex formatting that works in Word may be stripped or broken in EPUB.

**Testing only inside Scrivener.** Scrivener's preview does not show how the output will render in external applications. Always open the file externally.

**Overusing complex formatting.** Simpler formatting survives conversion better across all output types.

## Related pages

- [Select File Types for Compile Formats](10-select-file-types-for-compile-formats.md)
- [Footnotes & Comments](19-footnotes-and-comments.md)
- [Compile Styles](15-compile-styles.md)
