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
status: draft
---

# Using Placeholders

## Fast answer

Placeholders are compile-time tokens. Scrivener replaces them with project data, document data, numbering, dates, page numbers, or inserted content during export.

## Why this matters


Placeholders make reusable output possible.

Instead of typing fixed values everywhere, you can insert a token and let Compile resolve it.

Examples:

```text
<$projecttitle>
<$author>
<$date>
<$p>
<$wc>
<$n>
```

This is especially useful in:

- title pages
- headers
- footers
- chapter headings
- figure captions
- tables
- front matter
- ebook metadata


## Core workflow


Recommended workflow:

1. Decide what value should be generated at compile time.
2. Choose the appropriate placeholder.
3. Place it in text, layout prefix/suffix, header/footer, or metadata field.
4. Compile a small test.
5. Inspect the replacement.
6. Escape the placeholder if you want it to print literally.

To print a placeholder literally, use a backslash:

```text
\<$date>
```


## Common mistakes


### Using placeholders everywhere

Placeholders are powerful but can make text harder to read.

### Forgetting context limits

Some placeholders work only in headers/footers, ebook output, script settings, or compile settings.

### Typing placeholders incorrectly

Small syntax errors prevent replacement.

### Not testing output

Placeholder behavior must be tested in the target output format.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Readability trick

Use Project Replacements to make placeholders easier to read while drafting.

Example draft text:

```text
CHAPTER_NUMBER
```

Compile replacement:

```text
<$t:chapter>
```

This keeps the manuscript readable while still generating automatic output.

## Common high-value placeholders

```text
<$projecttitle>
<$author>
<$date>
<$p>
<$pagecount>
<$wc>
<$n>
<$t>
<$custom:FieldName>
```


## Related pages

- [List of all Placeholders](05-list-of-all-placeholders.md)
- [Automatic Numbering](03-automatic-numbering.md)
- [Project Replacements](27-project-replacements.md)
- [Metadata Settings](25-metadata-settings.md)
