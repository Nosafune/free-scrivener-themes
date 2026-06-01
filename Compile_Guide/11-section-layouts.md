---
title: Section Layouts
slug: section-layouts
part: Compiling
sequence: 11
tags:
  - compile
  - section-layouts
  - formatting
difficulty: intermediate
---

# Section Layouts

## Fast answer

Section Layouts are formatting recipes inside a Compile Format. They define how Binder items assigned to them appear in compiled output.

## What a Section Layout controls

- Whether the Binder title appears as a heading
- Whether the document text is included
- Title prefix and suffix (where numbering placeholders go)
- Whether the item starts on a new page
- Separator behavior before and after
- Paragraph formatting (font, size, spacing, indent)
- How styles are treated
- Whether editor formatting is preserved (As-Is)

## How they work

Section Layouts live inside a Compile Format. You assign them to Section Types in the Compile dialog. The result:

```
Section Type: Chapter Heading
Section Layout: Chapter Number and Title
  -> prints "Chapter Three" on a new page

Section Type: Scene
Section Layout: Section Text
  -> prints document text with no heading, after a separator
```

## Layout design checklist

For each Section Layout, decide:

- Does it print the Binder title as a heading?
- Does it print the document body text?
- Does it add automatic numbering?
- Does it start on a new page?
- Does it preserve editor formatting (As-Is), or override it?
- Does it need different behavior for ebook vs print?

## High-value layout types

- Part title (new page, large heading, no body text)
- Chapter title with page break
- Chapter title plus body text (for short chapter-per-document structures)
- Scene text only (no heading, continues from separator)
- Appendix heading
- Front matter As-Is
- Back matter As-Is

## Common mistakes

**Choosing layouts by name only.** Two layouts with similar names can have completely different page break or title behavior. Preview and test.

**Editing the layout when the assignment is wrong.** Confirm which layout is actually assigned before editing anything.

**Expecting one layout to handle everything.** Parts, chapters, scenes, and appendices all typically need different layouts.

**Forgetting title vs text inclusion.** A layout may include the Binder title, the document text, both, or neither. Check this explicitly.

## Related pages

- [Assigning Section Layouts to Section Types](07-assigning-section-layouts-to-section-types.md)
- [Using Compile Formats](06-using-compile-formats.md)
- [Automatic Numbering](03-automatic-numbering.md)
- [Using the Compile Format Designer](09-using-the-compile-format-designer.md)
