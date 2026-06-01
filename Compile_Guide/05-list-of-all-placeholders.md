---
title: List of all Placeholders
slug: list-of-all-placeholders
part: Compiling
sequence: 5
tags:
  - compile
  - placeholders
  - reference
difficulty: advanced
status: complete
---

# List of all Placeholders

## Fast answer

This is the placeholder reference for Scrivener 3 compile. Placeholders are compile-time tokens — Scrivener replaces them with project data, numbering, dates, or metadata during export.

## Why this matters


A placeholder reference is useful only if you can find what you need quickly. This page groups placeholders by practical purpose rather than alphabetically.


## Core workflow


Use this reference in three passes:

1. Find the category.
2. Copy the placeholder exactly.
3. Test it in the intended output format.

Important: before publication, verify this list against **Help → List of All Placeholders** in the exact Scrivener version being documented.


## Common mistakes


### Treating this as universal across every output format

Some placeholders are format-specific.

### Forgetting syntax

Placeholders must be typed exactly.

### Using document variables in headers/footers

Not every placeholder works in every location.

### Not escaping literal placeholders

Use a backslash when writing about placeholders instead of executing them.




## Template placeholders

| Placeholder | Use |
|---|---|
| `<$template_firstName>` | User first name from Contacts/account data |
| `<$template_lastName>` | User surname/last name |
| `<$template_fullName>` | User full name |
| `<$template_initial>` | First initial |
| `<$template_street>` | Street |
| `<$template_city>` | City/town |
| `<$template_state>` | State/county |
| `<$template_ZIP>` | ZIP/postcode |
| `<$template_country>` | Country |
| `<$template_phoneNumber>` | Phone number |
| `<$template_email>` | Email address |
| `<$template_projectName>` | Project title from project file name |

## Scriptwriting placeholder

| Placeholder | Use |
|---|---|
| `<$mediaPlaybackTime>` | Current playback time from media in the other editor |
| `<$mediaPlaybackTime:HH:mm:ss>` | Current playback time with custom format |

## Page numbers

| Placeholder | Use |
|---|---|
| `<$p>` | Current page number in header/footer; can also resolve linked document page numbers where possible |
| `<$p-r>` | Lowercase Roman page number |
| `<$P-R>` | Uppercase Roman page number |
| `<$pagecount>` | Page count in headers/footers |

## Headers and footers

| Placeholder | Use |
|---|---|
| `<$pageGroupTitle>` | Title of the document after the relevant page break |
| `<$pageGroupParentTitle>` | Parent title of the document after the relevant page break |

## Comments, footnotes, and layout

| Placeholder | Use |
|---|---|
| `<$--ENDNOTES-->` | Endnote placement marker |
| `<$--COMMENTS-->` | Linked comment placement marker |
| `<$BLANK_PAGE>` | Leaves the page blank |

## Document variables

| Placeholder | Use |
|---|---|
| `<$title>` | Current document title |
| `<$levelN_title>` | Title at outline level N |
| `<$levelN_title_no_spaces>` | Level title with spaces removed |
| `<$docTarget>` | Document target |
| `<$custom:FieldName>` | Custom metadata value |
| `<$htmlref>` | Ebook HTML reference for linked document |

## Current date and time

| Placeholder | Use |
|---|---|
| `<$date>` | Current date, short format |
| `<$date:HH:mm:ss>` | Custom date/time format |
| `<$shortdate>` | Short date |
| `<$mediumdate>` | Medium date |
| `<$longdate>` | Long date |
| `<$fulldate>` | Full date |
| `<$time>` / `<$shorttime>` | Short time |
| `<$mediumtime>` | Medium time |
| `<$longtime>` | Long time |
| `<$fulltime>` | Full time |
| `<$year>` | Current year |
| `<$shortnumericalmonth>` | Month as 1 or 2 digits |
| `<$numericalmonth>` | Month as 2 digits |
| `<$shortmonth>` | Abbreviated month name |
| `<$month>` / `<$longmonth>` | Full month name |
| `<$day>` / `<$shortday>` | Day of month |
| `<$longday>` | Day of month, two digits |
| `<$shortweekday>` | Abbreviated weekday |
| `<$weekday>` / `<$longweekday>` | Full weekday |

## User and project information

| Placeholder | Use |
|---|---|
| `<$surname>` / `<$lastname>` | User surname |
| `<$forename>` / `<$firstname>` | User first name |
| `<$initial>` | User initial |
| `<$author>` / `<$name>` / `<$fullname>` / `<$username>` | User full name |
| `<$compilegroup>` | Name of the current compile group |
| `<$draftname>` | Draft folder title |
| `<$projecttitle>` / `<$projectname>` | Project title/name from Compile metadata |
| `<$abbr_projecttitle>` / `<$abbr_projectname>` / `<$abbr_title>` | Abbreviated project title/name |

## Statistics

| Placeholder | Use |
|---|---|
| `<$wc>` | Total word count |
| `<$wc50>` | Word count rounded to nearest 50 |
| `<$wc100>` | Word count rounded to nearest 100 |
| `<$wc500>` | Word count rounded to nearest 500 |
| `<$wc1000>` | Word count rounded to nearest 1000 |
| `<$cc>` | Character count |
| `<$cc50>` | Character count rounded to nearest 50 |
| `<$cc100>` | Character count rounded to nearest 100 |
| `<$cc500>` | Character count rounded to nearest 500 |
| `<$cc1000>` | Character count rounded to nearest 1000 |
| `<$doccount>` | Number of compiled documents |
| `<$draftTarget>` | Project draft target |
| `<$sessionTarget>` | Project session target |

## Auto-numbering

| Placeholder | Use |
|---|---|
| `<$n>` | Arabic numerals: 1, 2, 3 |
| `<$sn>` | Sub-numbering stream |
| `<$np>` | Page-resetting number, PDF/print only |
| `<$r>` | Lowercase Roman numerals |
| `<$R>` | Uppercase Roman numerals |
| `<$l>` | Lowercase alphabetical numbering |
| `<$L>` | Uppercase alphabetical numbering |
| `<$w>` | Lowercase word numbers |
| `<$t>` | Title-case word numbers |
| `<$W>` | Uppercase word numbers |
| `<$hn>` | Hierarchical numbering |
| `<$ahn>` | Alphabetical hierarchical numbering |
| `<$aon>` | Alphanumeric outline numbering |
| `<$hn_0>` | Hierarchical numbering starting at zero |
| `<$hn_levelN>` | Hierarchical numbering starting at level N |
| `<$rst>` | Restart numbering |
| `<$rst_X>` | Restart a specific stream |
| `<$n:name>` | Named Arabic numbering stream |
| `<$t:name>` | Named title-case word numbering stream |
| `<$n:name:keyword>` | Numbered reference with keyword |
| `<$n#name:keyword>` | Reference an existing named number |

## Images and inserted text

| Placeholder | Use |
|---|---|
| `<$img:imgName>` | Insert an image document by name |
| `<$img:imgPath>` | Insert an image by file path |
| `<$img:imgNameOrPath;w=x;h=y>` | Insert image with width/height |
| `<$img:Img Doc;ebook=50%>` | Ebook percentage width |
| `<$include>` | Include linked document text |
| `<$include:textNameOrPath>` | Include project or external document text |

## Ebook and miscellaneous

| Placeholder | Use |
|---|---|
| `<$toc>` | Ebook table of contents placeholder |
| `<$ebook_start>` | Kindle start location marker |
| `<$nav_start>` / `<$nav_end>` | EPUB3 navigation block markers |
| `<$char_name>` | Scriptwriting continued-dialogue character name marker |


## Related pages

- [Using Placeholders](04-using-placeholders.md)
- [Automatic Numbering](03-automatic-numbering.md)
- [Metadata Settings](25-metadata-settings.md)
- [Project Replacements](27-project-replacements.md)
