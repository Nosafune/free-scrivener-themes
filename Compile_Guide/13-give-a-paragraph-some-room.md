---
title: Give a paragraph some room
slug: give-a-paragraph-some-room
part: Compiling
sequence: 13
tags:
  - compile
  - paragraphs
  - spacing
  - formatting
difficulty: intermediate
status: draft
---

# Give a paragraph some room

## Fast answer

Paragraph spacing in Compile is controlled by layout formatting, paragraph settings, and sometimes style behavior.

## Why this matters


Paragraph spacing is one of the most common output surprises.

The Editor may look acceptable, but the compiled result can change because Compile may override paragraph formatting.

This matters for:

- chapter openings
- scene breaks
- title spacing
- block quotes
- front matter
- manuscript submissions
- print layout


## Core workflow


Basic spacing workflow:

1. Identify the affected Section Type.
2. Identify its assigned Section Layout.
3. Open the layout formatting settings.
4. Adjust paragraph spacing before/after.
5. Check line spacing.
6. Check first-line indent.
7. Compile a short test.
8. Inspect in target output format.

Test with at least:

- first paragraph after a heading
- normal paragraph
- paragraph after a separator
- styled paragraph if styles are used


## Common mistakes


### Using empty paragraphs for spacing

Blank lines are fragile and can behave differently across outputs.

### Fixing spacing in the Editor only

Compile may override it.

### Forgetting first paragraph rules

Many manuscript formats suppress first-line indent after headings or separators.

### Not checking ebook output separately

Ebook spacing depends on reflowable layout behavior.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Better spacing strategy

Use layout rules for structural spacing.

Use styles only for semantically special paragraphs such as:

- block quotes
- verse
- letters
- excerpts
- captions

Avoid manual blank-line spacing except for intentional manuscript content.


## Related pages

- [Section Layouts](11-section-layouts.md)
- [Compile Styles](15-compile-styles.md)
- [Separators](14-separators.md)
- [Page Settings](20-page-settings.md)
