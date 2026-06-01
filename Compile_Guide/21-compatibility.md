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
status: complete
---

# Compatibility

## Fast answer

Compatibility settings handle output-specific limitations and conversion behavior between Scrivener and external formats.

## Why this matters


Every output format has constraints.

Compatibility settings matter because the same manuscript can behave differently in:

- Word
- PDF
- EPUB
- RTF
- plain text
- print
- Markdown/MultiMarkdown workflows

Compile must translate Scrivener’s internal document model into another file model.


## Core workflow


Basic workflow:

1. Choose output format.
2. Compile a short representative sample.
3. Open the output externally.
4. Check styles, footnotes, tables, images, links, and special characters.
5. Adjust compatibility settings if needed.
6. Re-test.

Representative sample should include:

- heading
- body text
- styled text
- footnote
- comment
- image
- table
- internal link


## Common mistakes


### Assuming all file types preserve all features

They do not.

### Testing only inside Scrivener

External inspection is required.

### Ignoring reader/device differences

Ebooks especially require real testing.

### Overusing complex formatting

Simpler formatting survives conversion better.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Format risk table

| Feature | Risk |
|---|---|
| footnotes | varies by output |
| comments | may be omitted or transformed |
| tables | fragile in ebooks |
| images | size and anchoring vary |
| page numbers | meaningless in reflowable ebooks |
| styles | may map differently |
| internal links | format-dependent |
| headers/footers | fixed-page formats only |

## Best practice

Create a compatibility test document and compile it after any major format change.


## Related pages

- [Select File Types for Compile Formats](10-select-file-types-for-compile-formats.md)
- [Footnotes & Comments](19-footnotes-and-comments.md)
- [Compile Styles](15-compile-styles.md)
