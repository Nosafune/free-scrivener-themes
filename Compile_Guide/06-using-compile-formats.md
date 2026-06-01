---
title: Using Compile Formats
slug: using-compile-formats
part: Compiling
sequence: 6
tags:
  - compile
  - formats
  - export
difficulty: intermediate
---

# Using Compile Formats

## Fast answer

A Compile Format is a reusable export design that holds Section Layouts and format-level rules. Selecting one determines what layout options are available and how the output is shaped.

## Why this matters

Compile Formats are the containers that hold export presentation. They control available layouts, typography rules, title formatting, separator behavior, page behavior, style handling, transformations, and output-specific settings.

Changing the Compile Format changes what choices are available to you. A format built for print PDF is not the same as one built for EPUB.

## Basic workflow

1. Open Compile.
2. Choose the output type from Compile For.
3. Select a Compile Format from the format list.
4. Review the preview tiles.
5. Assign Section Layouts.
6. Compile a test.
7. Duplicate and edit the format only if the test reveals something the built-in cannot handle.

Use built-in formats as starting points. Customize only after you see what the default produces.

## Format decision table

| Need | Start with |
|---|---|
| Agent or editor submission | Manuscript-style format |
| Print proof | PDF or print format |
| Ebook | EPUB format |
| Plain text archive | Plain Text or MultiMarkdown-friendly format |
| Outline export | Outline-focused compile setup |

## Naming pattern

```
[Project] - [Output] - [Purpose] - [Version]
```

Examples:

```
Novel - DOCX - Submission - v01
Nonfiction - PDF - Proof - v03
Series Bible - TXT - Archive
```

## Common mistakes

**Assuming all formats work for all outputs.** Compile Formats can be output-specific. Switching Compile For can change which formats appear.

**Editing before assigning layouts.** Often the layout assignment alone fixes the problem without any format editing.

**Using one format for multiple purposes.** A submission manuscript and an ebook need different formats. Separate them from the start.

## Related pages

- [Saving Compile Settings](02-saving-compile-settings.md)
- [Using the Compile Format Designer](09-using-the-compile-format-designer.md)
- [Select File Types for Compile Formats](10-select-file-types-for-compile-formats.md)
