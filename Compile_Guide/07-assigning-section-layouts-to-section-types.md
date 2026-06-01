---
title: Assigning Section Layouts to Section Types
slug: assigning-section-layouts-to-section-types
part: Compiling
sequence: 7
tags:
  - compile
  - section-types
  - section-layouts
  - workflow
difficulty: beginner
status: complete
---

# Assigning Section Layouts to Section Types

## Fast answer

This is the central Compile step: match what each Binder item is to how that kind of item should look in the output.

## Why this matters


Section Types and Section Layouts are the heart of Scrivener 3 Compile.

Section Types answer:

```text
What is this Binder item?
```

Section Layouts answer:

```text
How should this type of item look when exported?
```

The assignment step connects those two ideas.


## Core workflow


Basic workflow:

1. Open Compile.
2. Choose output type and Compile Format.
3. Click **Assign Section Layouts**.
4. Select a Section Type on the left.
5. Choose the layout that should apply.
6. Repeat for each used Section Type.
7. Compile a small test.
8. Inspect headings, text, numbering, and breaks.

Example mapping:

| Section Type | Section Layout |
|---|---|
| Part Heading | Numbered Part Title |
| Chapter Heading | Chapter Title with Page Break |
| Scene | Section Text |
| Appendix | Appendix Heading |
| Front Matter | As-Is |


## Common mistakes


### Assigning based on names only

Preview the layout. The name may not fully describe behavior.

### Forgetting unused Section Types

Unused types do not matter. Used types do.

### Mistaking Binder level for Section Type

Binder level can assign defaults, but Section Type is what Compile uses directly.

### Not checking highlighted items

Use the assignment preview/highlighting to verify which Binder items are affected.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Best diagnostic question

When something compiles wrong, ask:

```text
Which Section Type did this Binder item have, and which Section Layout was assigned to that type?
```

That question solves most Compile confusion.

## Good teaching example

Use a toy project with:

```text
Manuscript
├── Title Page
├── Chapter One
│   ├── Scene 1
│   └── Scene 2
└── Appendix
```

Assign each item a type, then compile it three different ways.


## Related pages

- [Section Layouts](11-section-layouts.md)
- [Deep dive into Compile](01-deep-dive-into-compile.md)
- [Using Compile Formats](06-using-compile-formats.md)
- [Contents Settings](22-contents-settings.md)
