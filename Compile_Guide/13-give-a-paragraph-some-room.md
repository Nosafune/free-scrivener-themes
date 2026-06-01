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
---

# Give a paragraph some room

## Fast answer

Paragraph spacing in compiled output is controlled by Section Layout formatting rules, not by what the Editor looks like. Fix spacing problems in the layout, not in the manuscript.

## Why the Editor does not help here

Compile Formats override editor paragraph formatting. A document that looks well-spaced in the Editor can come out cramped or over-spaced in output because the Section Layout's paragraph settings take precedence.

This is by design: it lets you write in whatever spacing is comfortable and still produce professional output. But it means you cannot fix a spacing problem by editing the manuscript.

## Where to fix it

1. Identify the Section Type of the affected document.
2. Find its assigned Section Layout.
3. Open the Compile Format Designer.
4. Navigate to that Section Layout's formatting.
5. Adjust: space before paragraph, space after paragraph, line spacing, first-line indent.
6. Compile a short test.
7. Inspect: first paragraph after heading, normal body paragraph, paragraph after separator.

## First-paragraph rules

Many manuscript formats suppress first-line indent on the paragraph immediately after a chapter heading or scene separator. If your first paragraphs look inconsistent, check whether the Section Layout has first-paragraph-override settings.

## Common mistakes

**Using empty paragraphs for spacing.** Blank lines are fragile and behave differently across output formats. Use paragraph spacing rules in the layout instead.

**Fixing spacing in the editor.** Compile will override it.

**Not checking ebook output separately.** Reflowable ebooks use CSS-like spacing behavior, which may differ from your print layout. Test each output format independently.

## Related pages

- [Section Layouts](11-section-layouts.md)
- [Compile Styles](15-compile-styles.md)
- [Separators](14-separators.md)
- [Page Settings](20-page-settings.md)
