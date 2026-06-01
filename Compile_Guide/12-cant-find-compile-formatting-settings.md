---
title: Can't find Compile Formatting Settings?
slug: cant-find-compile-formatting-settings
part: Compiling
sequence: 12
tags:
  - compile
  - troubleshooting
  - formatting
difficulty: intermediate
status: complete
---

# Can't find Compile Formatting Settings?

## Fast answer

If formatting settings seem missing, you are probably looking at the project-level Compile screen instead of editing a Compile Format or Section Layout.

## Why this matters


Scrivener separates project-level compile choices from format-level formatting rules.

Project-level choices include:

- what to compile
- metadata for this export
- some options
- Section Layout assignments

Format-level choices include:

- Section Layout formatting
- title options
- separators
- style mappings
- transformations
- compatibility behavior

Many formatting controls live inside the Compile Format Designer.


## Core workflow


Diagnostic workflow:

1. Confirm the current output type.
2. Confirm the selected Compile Format.
3. Check Section Layout assignment.
4. Find the layout responsible for the wrong output.
5. Edit a copy of the Compile Format.
6. Locate that Section Layout inside the designer.
7. Change one formatting setting.
8. Compile a test.


## Common mistakes


### Looking for old-version settings

Scrivener 3 changed the Compile model substantially.

### Editing project settings instead of format settings

Project Settings affects Section Types. Compile Format Designer affects layout formatting.

### Not knowing which layout is active

Find the Section Type of the problem document, then see which layout it uses.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Fast diagnosis

If the problem is:

| Problem | Likely location |
|---|---|
| wrong documents included | Contents |
| wrong heading style | Section Layout assignment or layout design |
| missing title | Section Layout title/text settings |
| wrong page break | Section Layout or Separators/Page Settings |
| wrong author/title | Metadata Settings |
| comments showing | Footnotes & Comments / Compile Options |
| styles wrong | Compile Styles / Compatibility |


## Related pages

- [Using the Compile Format Designer](09-using-the-compile-format-designer.md)
- [Section Layouts](11-section-layouts.md)
- [Contents Settings](22-contents-settings.md)
