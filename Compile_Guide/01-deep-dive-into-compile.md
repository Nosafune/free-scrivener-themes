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
status: complete
---

# Deep dive into Compile

## Fast answer

Compile is Scrivener’s export engine. It gathers selected Binder items, applies Section Type and Section Layout rules, then produces an external document.

## Why this matters


Compile looks intimidating because it sits at the intersection of almost every other Scrivener system.

It can use:

- Binder hierarchy
- Section Types
- Section Layouts
- Compile Formats
- metadata
- styles
- placeholders
- replacements
- front matter
- back matter
- comments
- footnotes
- output-specific settings

The mistake is thinking Compile is one tool. It is a pipeline.


## Core workflow


Use this basic pipeline:

```text
Choose output type
  ↓
Choose Compile Format
  ↓
Choose Contents
  ↓
Assign Section Layouts
  ↓
Review metadata/options
  ↓
Compile test output
  ↓
Adjust format or assignment
```

A practical first compile should avoid custom formatting. Choose a built-in format, confirm the right documents are included, and inspect the output. Only then edit the format.


## Common mistakes


### Editing too soon

Users often open the Format Designer before confirming Section Types and Contents. That creates confusion.

### Confusing Section Types and Section Layouts

Section Types identify what documents are. Section Layouts define how those document types are formatted.

### Expecting Editor formatting to equal output formatting

Compile may override Editor formatting depending on the selected format and layout.

### Testing on a whole manuscript

Compile small first. A short test reveals problems faster.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## The correct mental model

```text
Project structure is input.
Compile Format is formatting logic.
Section Layout assignment is the bridge.
Output file is the result.
```

## Beginner-safe strategy

1. Use built-in formats first.
2. Do not edit the format immediately.
3. Assign layouts carefully.
4. Compile to Word or PDF for inspection.
5. Save a custom format only after the result is close.

## Advanced strategy

Build separate compile presets for:

- editor submission
- proofing PDF
- personal print copy
- ebook
- outline export
- beta reader copy
- plain text archive

Each output can use the same manuscript with different compile rules.


## Related pages

- [Using Compile Formats](06-using-compile-formats.md)
- [Section Layouts](11-section-layouts.md)
- [Assigning Section Layouts to Section Types](07-assigning-section-layouts-to-section-types.md)
- [Contents Settings](22-contents-settings.md)
