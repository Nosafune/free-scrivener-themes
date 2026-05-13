---
title: Metadata Settings
slug: metadata-settings
part: Compiling
sequence: 25
tags:
  - compile
  - metadata
  - placeholders
  - ebook
difficulty: intermediate
status: draft
---

# Metadata Settings

## Fast answer

Metadata Settings define project-level information used in compiled output, especially title, author, description, and ebook metadata.

## Why this matters


Metadata is not decorative. It can become visible in output.

Metadata may feed:

- title page
- headers
- footers
- ebook metadata
- project placeholders
- catalog information
- author fields
- description fields

A wrong metadata field can make the exported book look wrong even if the manuscript is correct.


## Core workflow


Basic workflow:

1. Open Compile.
2. Find Metadata settings.
3. Set title.
4. Set author.
5. Set abbreviated title if needed.
6. Set ebook description if exporting ebook.
7. Compile title page/header test.
8. Verify output externally.

Common placeholders relying on metadata:

```text
<$projecttitle>
<$projectname>
<$abbr_title>
<$author>
<$surname>
<$forename>
```


## Common mistakes


### Renaming the project file only

The compiled title may come from Compile metadata, not just the file name.

### Forgetting ebook description

Ebook metadata matters for distribution and testing.

### Inconsistent author fields

Title page, headers, and metadata should agree.

### Not testing placeholders

Metadata placeholders must be checked in output.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Metadata consistency checklist

- [ ] project title
- [ ] abbreviated title
- [ ] author name
- [ ] contributor names
- [ ] ebook description
- [ ] copyright/front matter consistency
- [ ] series info if relevant
- [ ] language if relevant
- [ ] title page placeholders
- [ ] headers/footers

## Common failure

The project file is renamed, but `<$projecttitle>` still outputs an older title because the Compile metadata pane was not updated.


## Related pages

- [Using Placeholders](04-using-placeholders.md)
- [List of all Placeholders](05-list-of-all-placeholders.md)
- [Page Settings](20-page-settings.md)
