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
status: draft
---

# Saving Compile Settings

## Fast answer

Save compile settings when you have a repeatable export workflow that should not be rebuilt manually each time.

## Why this matters


Compile settings are valuable because they encode decisions.

A useful compile setup might include:

- chosen output type
- selected format
- Section Layout assignments
- metadata behavior
- footnote/comment behavior
- replacement rules
- page settings
- compatibility settings

Saving settings turns an export into a repeatable production process.


## Core workflow


Recommended approach:

1. Start from a built-in Compile Format.
2. Test output.
3. Duplicate or save a custom version before major edits.
4. Name the format by purpose.
5. Keep one format per output need.

Useful names:

```text
Submission - Word - Double Spaced
Proof Copy - PDF - Wide Margins
Ebook - EPUB - Retail Draft
Archive - Plain Text
```


## Common mistakes


### Editing the original without knowing it

Always duplicate before heavy customization.

### Names that do not describe purpose

“Custom Format 2” becomes useless later.

### Saving too early

Do not save a format before you know it works.

### One format for everything

Separate outputs need separate compile settings.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Storage logic

A custom format may be project-specific or reusable depending on how it is saved. For a book workflow, decide whether the format belongs only to the current project or should be available to future projects.

## Version naming

For serious projects, consider names like:

```text
Novel Submission v01
Novel Submission v02 - No Comments
Paperback Proof v03 - Chapter Numbers Fixed
```

## Minimum useful saved set

A strong project usually benefits from at least three saved compile formats:

- manuscript submission
- proofreading PDF
- ebook test


## Related pages

- [Using Compile Formats](06-using-compile-formats.md)
- [Using the Compile Format Designer](09-using-the-compile-format-designer.md)
- [Compile Options](26-compile-options.md)
