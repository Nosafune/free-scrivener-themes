---
title: Using the Compile Format Designer
slug: using-the-compile-format-designer
part: Compiling
sequence: 9
tags:
  - compile
  - format-designer
  - advanced
difficulty: advanced
status: complete
---

# Using the Compile Format Designer

## Fast answer

The Compile Format Designer is where you edit the internals of a Compile Format after layout assignment is not enough.

## Why this matters


The Format Designer is the advanced area.

Use it to control:

- Section Layout definitions
- title options
- separators
- style behavior
- transformations
- page settings
- compatibility
- file-type-specific behavior

It is powerful because it edits the formatting recipe itself.


## Core workflow


Safe workflow:

1. Start from a working built-in format.
2. Duplicate the format.
3. Rename the copy clearly.
4. Change one setting.
5. Compile a short test.
6. Record what changed.
7. Repeat.

Do not edit five settings at once.


## Common mistakes


### Editing the wrong format

Make sure the selected format is the one being modified.

### No test project

Use a small sample project to test designer settings.

### Confusing project options with format options

Some Compile settings are project-level; others live inside the format.

### Not duplicating first

A copied format gives you a safe rollback point.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Recommended testing project

Create a tiny project with:

```text
Front Matter
Manuscript
  Part
    Chapter
      Scene
      Scene
Back Matter
```

Add:

- one footnote
- one comment
- one styled heading
- one image
- one table
- one placeholder
- one custom metadata field

This gives you a controlled test lab for Compile Format Designer changes.


## Related pages

- [Using Compile Formats](06-using-compile-formats.md)
- [Saving Compile Settings](02-saving-compile-settings.md)
- [Section Layouts](11-section-layouts.md)
- [Compile Styles](15-compile-styles.md)
