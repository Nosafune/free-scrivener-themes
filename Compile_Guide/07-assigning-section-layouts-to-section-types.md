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
---

# Assigning Section Layouts to Section Types

## Fast answer

This is the central Compile step: match what each Binder item is (Section Type) to how that kind of item should look in the output (Section Layout).

## Why this matters

Section Types and Section Layouts are the heart of Scrivener 3 Compile.

- Section Types answer: **What is this Binder item?**
- Section Layouts answer: **How should this type appear when exported?**

The assignment step connects those two answers. Every compile problem that is not a Contents problem is usually an assignment problem.

## How to assign

1. Open Compile.
2. Choose output type and Compile Format.
3. Click Assign Section Layouts.
4. Select a Section Type on the left.
5. Choose the layout that should apply.
6. Repeat for each Section Type that appears in your project.
7. Compile a small test.
8. Inspect headings, text, numbering, and page breaks.

## Example mapping

| Section Type | Section Layout |
|---|---|
| Part Heading | Numbered Part Title |
| Chapter Heading | Chapter Title with Page Break |
| Scene | Section Text |
| Appendix | Appendix Heading |
| Front Matter | As-Is |

## Best diagnostic question

When something compiles wrong, ask:

> Which Section Type did this Binder item have, and which Section Layout was assigned to that type?

That question solves most compile confusion.

## Common mistakes

**Assigning based on layout names alone.** Preview the layout before choosing. The name may not fully describe the behavior.

**Forgetting to assign a used type.** If a type is used in the Binder and has no layout assigned, it will compile with no formatting applied.

**Mistaking Binder level for Section Type.** Binder hierarchy can auto-assign default types, but Section Type is what Compile actually uses. Verify assignments explicitly.

**Not using the assignment preview.** The assignment dialog highlights which Binder items are affected by each type. Use this to confirm you are targeting the right documents.

## Related pages

- [Section Layouts](11-section-layouts.md)
- [Deep dive into Compile](01-deep-dive-into-compile.md)
- [Using Compile Formats](06-using-compile-formats.md)
- [Contents Settings](22-contents-settings.md)
