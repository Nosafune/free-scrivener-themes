---
title: Skip the preview tiles
slug: skip-the-preview-tiles
part: Compiling
sequence: 8
tags:
  - compile
  - preview
  - section-layouts
difficulty: intermediate
status: complete
---

# Skip the preview tiles

## Fast answer

Preview tiles are useful for orientation, but advanced troubleshooting should focus on Section Type assignment, Section Layout assignment, and actual test output.

## Why this matters


Compile previews show approximate layout behavior, not the full finished manuscript.

They are useful for:

- choosing among layout options
- identifying page break behavior
- seeing whether titles are included
- comparing layout families

They are not a substitute for compiling a test output.


## Core workflow


Use preview tiles like this:

1. Scan for broad layout behavior.
2. Select the closest layout.
3. Assign it.
4. Compile a short sample.
5. Evaluate the real output.
6. Return to preview only if assignment was clearly wrong.

For technical troubleshooting, trust real compiled output over preview.


## Common mistakes


### Expecting exact output

Preview tiles use sample text and may not show project-specific behavior.

### Ignoring actual document settings

A tile cannot fully show metadata, replacement, footnote, or output-specific effects.

### Spending too long in previews

Choose a likely layout and test.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## When preview tiles are enough

They are usually enough for:

- choosing title-only vs title-and-text
- deciding whether a page break is present
- identifying section text layouts
- comparing heading styles

## When preview tiles are not enough

Compile a real test when checking:

- placeholders
- footnotes
- page headers
- ebook navigation
- replacements
- custom metadata
- compatibility settings


## Related pages

- [Assigning Section Layouts to Section Types](07-assigning-section-layouts-to-section-types.md)
- [Section Layouts](11-section-layouts.md)
- [Deep dive into Compile](01-deep-dive-into-compile.md)
