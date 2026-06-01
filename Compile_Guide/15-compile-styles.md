---
title: Compile Styles
slug: compile-styles
part: Compiling
sequence: 15
tags:
  - compile
  - styles
  - formatting
difficulty: intermediate
status: complete
---

# Compile Styles

## Fast answer

Compile Styles determine how styled text from the Editor is preserved, transformed, or reformatted during export.

## Why this matters


Styles are safer than manual formatting because they describe meaning.

A paragraph styled as Block Quote can be treated consistently at compile time. A paragraph manually indented with random spacing is harder to control.

Compile Styles matter for:

- block quotes
- headings
- captions
- verse
- letters
- code blocks
- callouts
- front matter
- nonfiction elements


## Core workflow


Recommended workflow:

1. Use styles only for text that needs special treatment.
2. Avoid styling ordinary body text unnecessarily.
3. Confirm which styles exist in the project.
4. Open Compile Styles settings.
5. Decide whether each style is preserved, renamed, or reformatted.
6. Test in the target output.

Example style set:

```text
Block Quote
Caption
Epigraph
Letter
Verse
Code
```


## Common mistakes


### Styling everything

Body text often does not need a style.

### Confusing Editor Styles with Section Layouts

Styles affect text inside documents. Section Layouts affect Binder items.

### Manual formatting instead of styles

Manual formatting is harder to control globally.

### Not checking output app behavior

Word, PDF, and EPUB handle styles differently.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Style discipline

Use styles for semantic exceptions, not decoration.

Bad style names:

```text
Blue 14pt
Indented Thing
Looks Nice
```

Good style names:

```text
Block Quote
Caption
Poem
Letter
Sidebar
```

## Compile interaction

A Section Layout may define body text formatting while Compile Styles define exceptions within that body text.


## Related pages

- [Section Layouts](11-section-layouts.md)
- [Compatibility](21-compatibility.md)
- [Transformations & Replacements](17-transformations-and-replacements.md)
