---
title: Deep dive into Compile
slug: deep-dive-into-compile
part: Compiling
sequence: 1
tags:
  - compile
  - workflow
  - section-types
  - section-layouts
difficulty: beginner
---

# Deep dive into Compile

## Fast answer

Compile is Scrivener's export engine. It collects selected Binder items, applies Section Type and Section Layout rules, and produces an external document.

## Why this matters

Compile looks intimidating because it touches almost every other Scrivener system: Binder hierarchy, Section Types, Section Layouts, Compile Formats, metadata, styles, placeholders, replacements, footnotes, and output-specific settings.

The key insight is that Compile is not one tool -- it is a pipeline. Understanding which stage controls what makes every problem easier to locate.

## The correct mental model

```
Project structure     is the input.
Section Types         identify what each Binder item is.
Section Layouts       define how each type appears in output.
Compile Format        holds the layouts and format-level rules.
Contents Settings     control which items are included.
Output file           is the result.
```

## The core pipeline

```
Choose output type
  |
Choose Compile Format
  |
Choose Contents
  |
Assign Section Layouts to Section Types
  |
Review metadata and options
  |
Compile test output
  |
Adjust one setting at a time
```

## The most common mistake

Opening the Compile Format Designer before confirming Section Types and Contents. This creates confusion because the wrong documents are being formatted, or the wrong type is assigned -- neither of which the Designer can fix.

Always confirm what is included and what type each item is before touching format settings.

## Editor formatting vs compile formatting

Your editor appearance does not control output appearance. Compile Formats and Section Layouts override editor formatting. Write in any font and size you prefer -- it will not appear in the output unless you compile As-Is.

## Beginner strategy

1. Use a built-in format first. Do not customize immediately.
2. Check Contents. Confirm only intended documents are included.
3. Check Section Types. Confirm each item is labeled correctly.
4. Assign Section Layouts and run a test compile to Word or PDF.
5. Inspect the output file externally. Adjust from there.

## Advanced strategy

Build separate compile presets for each output you produce regularly:

- editor submission (Word, double-spaced, standard manuscript)
- proofing PDF (wide margins, comfortable reading)
- ebook (EPUB 3 with cover and metadata)
- plain text archive
- beta reader packet (selected chapters)

## Related pages

- [Compile Roadmap](00-compile-roadmap.md)
- [Using Compile Formats](06-using-compile-formats.md)
- [Section Layouts](11-section-layouts.md)
- [Assigning Section Layouts to Section Types](07-assigning-section-layouts-to-section-types.md)
- [Contents Settings](22-contents-settings.md)
