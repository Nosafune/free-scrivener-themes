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
status: draft
---

# Section Layouts

## Fast answer

Section Layouts are formatting recipes inside a Compile Format. They define how Binder items assigned to them will appear in the compiled output.

## Why this matters


Section Layouts control output behavior at the Binder-item level.

They can control:

- title inclusion
- text inclusion
- title prefixes
- title suffixes
- numbering
- page breaks
- separators
- paragraph formatting
- heading treatment
- style handling

They are not the same as Editor styles.


## Core workflow


Use Section Layouts by assigning them to Section Types.

Example:

```text
Section Type: Chapter Heading
Section Layout: Chapter Number and Title

Section Type: Scene
Section Layout: Section Text
```

A layout can include:

```text
Chapter <$t>
<$title>
```

or simply compile the text without a title.


## Common mistakes


### Choosing layouts by name only

Preview and test them.

### Editing the layout when assignment is wrong

First confirm assignment.

### Expecting one layout to do everything

Different document types usually need different layouts.

### Forgetting title/text inclusion

A layout may include the Binder title, the document text, both, or neither.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Layout design checklist

For each Section Layout, decide:

- Does it print the Binder title?
- Does it print the document text?
- Does it add automatic numbering?
- Does it start on a new page?
- Does it add a separator before or after?
- Does it preserve Editor formatting?
- Does it override paragraph formatting?
- Does it need different behavior for ebook vs print?

## High-value layout types

- Part title
- Chapter title
- Chapter title + text
- Scene text
- Appendix heading
- Front matter As-Is
- Back matter As-Is


## Related pages

- [Assigning Section Layouts to Section Types](07-assigning-section-layouts-to-section-types.md)
- [Using Compile Formats](06-using-compile-formats.md)
- [Automatic Numbering](03-automatic-numbering.md)
