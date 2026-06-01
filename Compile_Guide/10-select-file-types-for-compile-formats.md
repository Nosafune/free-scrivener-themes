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
status: complete
---

# Select File Types for Compile Formats

## Fast answer

Compile Formats are filtered by output file type, so choose the intended output before judging which formats are available.

## Why this matters


The output format affects the available compile formats and the behavior of individual settings.

A format meant for PDF may not make sense for EPUB. A plain text export cannot preserve all formatting. A Word export may handle styles differently than a PDF export.

The first decision is always:

```text
What are we compiling for?
```


## Core workflow


Basic workflow:

1. Open Compile.
2. Choose **Compile For**.
3. Review the format list.
4. Select the closest format.
5. Assign layouts.
6. Test output in the target application.

Examples:

| Output goal | Compile For |
|---|---|
| editor manuscript | Microsoft Word or RTF |
| print proof | PDF or Print |
| ebook | EPUB/Kindle |
| archive | Plain Text |
| markdown pipeline | MultiMarkdown/Plain Text route if used |

> **Note:** Scrivener 3 exports EPUB 3 (the current standard). Amazon KDP now prefers EPUB 3 over the older .mobi format for new uploads.

## Common mistakes


### Selecting format before file type

Changing file type can change available formats.

### Expecting PDF behavior in EPUB

Ebooks are reflowable; page-specific behavior often does not apply.

### Expecting rich formatting in plain text

Plain text output cannot preserve many visual settings.

### Not opening output externally

Always inspect the result in the program or device readers will use.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Output-type reality check

| Feature | Word | PDF | EPUB | Plain Text |
|---|---:|---:|---:|---:|
| page numbers | yes | yes | limited/not fixed | no |
| fixed margins | yes | yes | no | no |
| live styles | yes | no/limited | CSS-like | no |
| ebook metadata | no | no | yes | no |
| reflowable layout | no | no | yes | no |
| comments/footnotes | yes | yes/limited | varies | limited |


## Related pages

- [Using Compile Formats](06-using-compile-formats.md)
- [Compatibility](21-compatibility.md)
- [Page Settings](20-page-settings.md)
