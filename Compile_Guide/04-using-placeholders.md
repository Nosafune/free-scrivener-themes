---
title: Using Placeholders
slug: using-placeholders
part: Compiling
sequence: 4
tags:
  - compile
  - placeholders
  - metadata
  - numbering
difficulty: intermediate
---

# Using Placeholders

## Fast answer

Placeholders are compile-time tokens. Scrivener replaces them during export with project data, document data, numbering, dates, page numbers, or inserted content.

## Why this matters

Placeholders make output reusable. Instead of typing fixed values, you insert a token and let Compile resolve it at export time. The same manuscript produces a correctly titled title page, correctly numbered chapters, and correct author headers for any draft -- without editing the text.

## Where placeholders work

Placeholders can appear in:

- document text
- Section Layout prefix and suffix fields
- Section Layout title fields
- header and footer fields
- metadata fields
- replacement rules

Not every placeholder works in every location. Some are headers/footers only. Some are ebook-only. Test in the intended output.

## Common high-value placeholders

```
<$projecttitle>   project title from Compile metadata
<$author>         author name from Compile metadata
<$date>           current date at compile time
<$p>              current page number (headers/footers only)
<$pagecount>      total page count (headers/footers only)
<$wc>             total word count
<$n>              auto-number, Arabic (1, 2, 3)
<$t>              auto-number, title-case word (One, Two, Three)
<$custom:Name>    custom metadata field value
```

## Escaping placeholders

To print a placeholder literally, prefix it with a backslash: `\<$date>`

Scrivener will output the literal text `<$date>` without replacing it.

## Readability trick

Use Project Replacements to keep drafts readable while generating correct output.

Draft text: `CHAPTER_NUMBER`

Compile Replacement: `CHAPTER_NUMBER  ->  <$t:chapter>`

The manuscript stays readable during writing. The replacement fires at compile time.

## Common mistakes

**Using placeholders in the wrong location.** Check the full list to confirm which locations each placeholder supports.

**Typing placeholders incorrectly.** A single wrong character prevents replacement. Copy from Help > List of All Placeholders inside Scrivener.

**Not testing in the target format.** Placeholder behavior can differ between PDF, Word, and EPUB output. Always inspect a test compile externally.

## Related pages

- [List of all Placeholders](05-list-of-all-placeholders.md)
- [Automatic Numbering](03-automatic-numbering.md)
- [Project Replacements](27-project-replacements.md)
- [Metadata Settings](25-metadata-settings.md)
