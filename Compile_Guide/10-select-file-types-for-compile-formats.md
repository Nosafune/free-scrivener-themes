---
title: Select File Types for Compile Formats
slug: select-file-types-for-compile-formats
part: Compiling
sequence: 10
tags:
  - compile
  - file-types
  - export
difficulty: intermediate
---

# Select File Types for Compile Formats

## Fast answer

Choose the output file type first (Compile For), then select a Compile Format. The available formats and relevant settings both change depending on what you are outputting.

## Why order matters

Changing the output type can change which Compile Formats appear in the list and which settings are available. A format built for PDF may not make sense for EPUB. A plain text export cannot preserve formatting that a Word export handles cleanly.

The first question is always: **What are we compiling for?**

## Output type reference

| Output goal | Compile For |
|---|---|
| Agent or editor manuscript | Microsoft Word (.docx) or RTF |
| Print proof or final PDF | PDF |
| Ebook | EPUB 3 |
| Archive or conversion pipeline | Plain Text |
| Technical or Markdown workflow | MultiMarkdown or plain text route |

> **Note:** Scrivener 3 exports EPUB 3, the current ebook standard. Amazon KDP now accepts and prefers EPUB 3 over the older .mobi format for new uploads.

## What each format can and cannot do

| Feature | Word | PDF | EPUB | Plain Text |
|---|---|---|---|---|
| Page numbers | yes | yes | no (reflowable) | no |
| Fixed margins | yes | yes | no | no |
| Live styles | yes | limited | CSS-like | no |
| Ebook metadata | no | no | yes | no |
| Reflowable layout | no | no | yes | no |
| Comments/footnotes | yes | partial | varies | limited |

## Common mistakes

**Selecting a format before setting the output type.** Switching Compile For can reset available format options. Set the output type first.

**Expecting PDF behavior in EPUB.** Ebooks are reflowable. Page-specific behavior does not apply.

**Not opening the output externally.** Always inspect the result in the program or device readers will use. Scrivener's preview is not a substitute for Word, Adobe Reader, or a real ebook reader.

## Related pages

- [Using Compile Formats](06-using-compile-formats.md)
- [Compatibility](21-compatibility.md)
- [Page Settings](20-page-settings.md)
