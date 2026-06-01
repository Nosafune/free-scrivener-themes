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
---

# Using the Compile Format Designer

## Fast answer

The Compile Format Designer is where you edit the internals of a Compile Format after layout assignment alone is not enough. Use it only after confirming that assignment, Contents, and Section Types are correct.

## What the Format Designer controls

- Section Layout definitions (what each layout actually does)
- Title prefix and suffix options
- Separator behavior
- Style mappings
- Transformations
- Page settings (margins, headers, footers)
- Compatibility options
- File-type-specific behavior

## Safe workflow

1. Start from a working built-in format.
2. Duplicate it. Name the copy clearly.
3. Change one setting.
4. Compile a short test.
5. Record what you changed and what happened.
6. Repeat.

Do not change five settings at once. When something breaks, you will not know which change caused it.

## What to edit and where

| Problem | Location in Designer |
|---|---|
| Heading is wrong font or size | Section Layouts > that layout > formatting |
| Page break missing before chapter | Section Layouts > that layout > New Page |
| Chapter number not appearing | Section Layouts > that layout > Title Options |
| Scene separator wrong | Separators pane |
| Style not coming through | Styles pane |
| Footer content wrong | Page Settings pane |
| Word comments surviving | Compatibility pane |

## Recommended test project

Create a small project containing front matter, a Part, a Chapter with two Scenes, and back matter. Include one footnote, one comment, one styled paragraph, one image, and one placeholder. This gives you a controlled lab for testing any Designer change.

## Common mistakes

**Editing the wrong format.** Confirm the format name in the Designer title bar matches the one selected in the Compile panel.

**No test project.** Changes look different on a 300-page novel vs a 5-page test. Start small.

**Confusing project settings with format settings.** Section Types are in Project Settings. Section Layout formatting is in the Format Designer. They are separate.

**Not duplicating first.** A copied format is your rollback point.

## Related pages

- [Using Compile Formats](06-using-compile-formats.md)
- [Saving Compile Settings](02-saving-compile-settings.md)
- [Section Layouts](11-section-layouts.md)
- [Compile Styles](15-compile-styles.md)
