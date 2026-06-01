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
---

# Page Settings

## Fast answer

Page Settings control page size, margins, headers, footers, and pagination for fixed-page outputs (PDF, Word, Print). They do not apply to reflowable ebooks.

## When page settings matter

Page settings are relevant for PDF, Print, and Word/RTF manuscript exports. They are not relevant -- or behave differently -- for EPUB and plain text.

## Core settings

**Page size:** Letter (8.5 x 11 in) is standard in North America. A4 is standard in most other countries. Paperback trim sizes vary (common: 5.06 x 7.81 in, 5.5 x 8.5 in, 6 x 9 in).

**Margins:** Standard manuscript: 1 inch all sides. Print books: inside margin (gutter) should be wider than outside margin, especially for longer books.

**Headers and footers:** Typical manuscript header: Author / Title / Page. Footer: usually empty or page number only.

## Common header/footer placeholders

```
<$p>                 page number
<$pagecount>         total pages
<$projecttitle>      project title
<$author>            author name
<$abbr_title>        abbreviated title
<$pageGroupTitle>    current chapter title
```

## Front matter behavior

Front matter often needs different page numbering:

- title page: no page number
- copyright, dedication: Roman numerals (i, ii, iii)
- main text: Arabic numerals starting at 1

Configure this in the Section Layout settings for front matter items and in the page settings pane.

## Common mistakes

**Applying PDF assumptions to EPUB.** Ebooks are reflowable. Page layout settings mean nothing in a reflowable context.

**Wrong page size for the printer.** Letter and A4 differ. Always confirm page size matches your print target.

**Headers or footers on the title page.** The title page almost never has a running header. Configure the title page Section Layout to suppress headers and footers.

**Forgetting mirrored margins for print.** Print layouts need the inside margin (binding side) wider than the outside. Enable mirrored margins in Page Settings for print output.

## Related pages

- [Compatibility](21-compatibility.md)
- [Using Placeholders](04-using-placeholders.md)
- [Give a paragraph some room](13-give-a-paragraph-some-room.md)
