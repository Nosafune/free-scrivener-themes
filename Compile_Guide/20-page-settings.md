---
title: Page Settings
slug: page-settings
part: Compiling
sequence: 20
tags:
  - compile
  - page-settings
  - pdf
  - print
difficulty: intermediate
status: draft
---

# Page Settings

## Fast answer

Page Settings control page-level output behavior such as size, margins, headers, footers, and pagination where the output format supports fixed pages.

## Why this matters


Page settings matter most for fixed-page outputs.

Examples:

- Print
- PDF
- Word/RTF manuscript exports

They matter less or differently for reflowable ebooks.


## Core workflow


Basic workflow:

1. Choose fixed-page output.
2. Set page size.
3. Set margins.
4. Configure headers and footers.
5. Configure page numbering.
6. Test front matter and first chapter.
7. Inspect final PDF or Word output.

Common header/footer placeholders:

```text
<$p>
<$pagecount>
<$projecttitle>
<$author>
<$pageGroupTitle>
```


## Common mistakes


### Applying PDF assumptions to EPUB

Ebooks do not have fixed page layout.

### Wrong page size

Letter and A4 differences matter.

### Header/footer on front matter

Front matter may need different numbering or no numbering.

### Forgetting outside/inside margins

Print layouts may need mirrored margins.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Page setup testing

Always test:

- title page
- first front matter page
- first chapter page
- ordinary body page
- final page
- appendix page if present

## Fixed-page vs reflowable thinking

Fixed-page formats ask:

```text
Where does this sit on the page?
```

Reflowable formats ask:

```text
What is this content semantically?
```


## Related pages

- [Compatibility](21-compatibility.md)
- [Using Placeholders](04-using-placeholders.md)
- [Give a paragraph some room](13-give-a-paragraph-some-room.md)
