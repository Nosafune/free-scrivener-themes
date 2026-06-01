---
title: Text Layout & Document Title Links
slug: text-layout-and-document-title-links
part: Compiling
sequence: 16
tags:
  - compile
  - titles
  - links
  - layout
difficulty: intermediate
status: complete
---

# Text Layout & Document Title Links

## Fast answer

Text layout controls how document text and titles are assembled; document title links can support cross-references and navigation-oriented output.

## Why this matters


Compiled output is not just document text pasted together.

Compile can use:

- Binder titles
- document text
- generated titles
- linked titles
- title prefixes
- title suffixes
- cross-reference placeholders
- internal links

This is especially important for nonfiction, textbooks, reference works, and ebooks.


## Core workflow


Basic workflow:

1. Decide whether Binder titles should appear.
2. Decide whether titles should be generated, literal, or omitted.
3. Check Section Layout title settings.
4. Check title prefix/suffix fields.
5. Test internal document links.
6. Verify output in the target format.

Examples:

```text
Chapter <$t>
<$title>
```

```text
Appendix <$R>: <$title>
```

```text
See Chapter <$n#chapter:installing-themes>
```


## Common mistakes


### Treating Binder titles as only organizational

Binder titles can become compiled headings.

### Duplicate titles

Repeated Binder titles can confuse navigation and references.

### Broken links

Internal links must point to the intended documents.

### Output format assumptions

Some link behaviors vary by output type.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Title strategy

For a clean project, decide early:

| Binder title role | Strategy |
|---|---|
| organizational only | do not include title in layout |
| printed heading | include title in layout |
| auto-numbered heading | combine title with numbering placeholder |
| ebook navigation | use meaningful titles |

## Document title links

For reference-heavy projects, title links can support:

- cross-references
- page references
- figure references
- appendix navigation
- ebook internal navigation


## Related pages

- [Section Layouts](11-section-layouts.md)
- [Automatic Numbering](03-automatic-numbering.md)
- [Using Placeholders](04-using-placeholders.md)
