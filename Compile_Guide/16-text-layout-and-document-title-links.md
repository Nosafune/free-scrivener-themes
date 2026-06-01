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
---

# Text Layout & Document Title Links

## Fast answer

Text layout controls how document text and titles are assembled in output. Document title links support cross-references and navigation in ebook and reference work output.

## What compiled output can include

Compiled output is not just document text pasted end to end. For each Binder item, Compile can include:

- the Binder title as a heading
- a generated title (from a prefix/suffix template)
- document body text
- auto-numbered title elements
- cross-reference placeholders
- internal links

The Section Layout controls which of these appear, and in what order.

## Title generation examples

Plain Binder title: `<$title>`

Numbered chapter title: `Chapter <$t>` followed by `<$title>`

Appendix with Roman numeral: `Appendix <$R>: <$title>`

Cross-reference by number: `See Chapter <$n#chapter:setup>`

## Title strategy

Decide early how Binder titles will function in your project:

| Binder title role | Section Layout setting |
|---|---|
| Organizational only | Do not include title in output |
| Printed heading | Include title in layout |
| Auto-numbered heading | Combine title with numbering placeholder |
| Ebook navigation | Use meaningful, unique titles |

## Document title links for reference works

For nonfiction, textbooks, or ebook-heavy projects, document title links can support:

- internal cross-references (See Chapter 4)
- figure and table references
- appendix navigation
- EPUB internal navigation

Use `<$n#stream:keyword>` to reference a numbered item without incrementing the count.

## Common mistakes

**Treating Binder titles as organizational only.** They can and often should become compiled headings. Review whether titles are set to appear in the Section Layout.

**Duplicate Binder titles.** Repeated titles confuse navigation (especially in ebooks) and make cross-references ambiguous.

**Assuming link behavior is the same across formats.** Internal link behavior varies between PDF, Word, and EPUB. Test in each target format.

## Related pages

- [Section Layouts](11-section-layouts.md)
- [Automatic Numbering](03-automatic-numbering.md)
- [Using Placeholders](04-using-placeholders.md)
