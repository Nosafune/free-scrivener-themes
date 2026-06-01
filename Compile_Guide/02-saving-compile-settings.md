---
title: Saving Compile Settings
slug: saving-compile-settings
part: Compiling
sequence: 2
tags:
  - compile
  - settings
  - formats
  - workflow
difficulty: intermediate
---

# Saving Compile Settings

## Fast answer

Save compile settings as named Compile Formats so you can repeat a complex export without rebuilding it each time.

## Why this matters

A useful compile setup encodes many decisions: output type, section layout assignments, metadata behavior, footnote and comment rules, replacement logic, page settings, and compatibility options. Saving that configuration means you can reuse it for every draft pass, revision, or edition without losing your settings.

Without saved formats, every export requires rebuilding these choices -- which introduces inconsistency and wastes time.

## How to save a format

**Project-specific format:** Right-click a Compile Format in the left panel, choose Save to Project Formats. Available only in this project.

**Shared format:** Right-click, choose Save to My Formats. Available in all future projects.

**Before editing:** Duplicate first. Right-click a built-in format and choose Duplicate. Work from the copy so the original is preserved.

## Naming convention

A format name should tell you exactly what it does and when to use it:

```
Novel - DOCX - Submission - v01
Novel - DOCX - Submission - No Comments
Nonfiction - PDF - Proof - Wide Margins
Series Bible - TXT - Archive
Ebook - EPUB - Retail Draft
```

## Minimum useful saved set

A serious project benefits from at least three saved formats:

- manuscript submission (Word, double-spaced, clean of comments)
- proofing PDF (comfortable margins, legible)
- ebook (EPUB 3, cover and metadata configured)

## Common mistakes

**Editing the original without duplicating first.** Built-in formats can be damaged and are not easily restored.

**Saving before testing.** Save a format after you know it produces correct output, not before.

**One format for everything.** Submission manuscripts and ebooks need different settings. Trying to make one format serve both creates conflicts you cannot resolve cleanly.

## Related pages

- [Using Compile Formats](06-using-compile-formats.md)
- [Using the Compile Format Designer](09-using-the-compile-format-designer.md)
- [Compile Options](26-compile-options.md)
