---
title: Compile Troubleshooting
slug: compile-troubleshooting
part: Compiling
tags:
  - compile
  - troubleshooting
  - reference
difficulty: intermediate
---

# Compile Troubleshooting

Use this page when the output is wrong but the cause is unclear.

## Headings are wrong

Check:

1. Is the Binder item assigned the correct Section Type?
2. Is that Section Type assigned to the intended Section Layout?
3. Does the selected Compile Format contain the layout you expect?
4. Are you editing the correct format copy?
5. Did you compile to the same output type you tested?

## Chapter numbers are wrong

Check:

1. Is the numbering placeholder in the Section Layout prefix/suffix/title?
2. Is it using the correct stream?
3. Does numbering need to restart?
4. Are front matter documents accidentally consuming numbering?
5. Are chapter headings and scene text assigned to different layouts?

## Text spacing is wrong

Check:

1. Section Layout formatting
2. paragraph spacing before/after
3. line spacing
4. first-line indent
5. separators
6. whether text is compiled As-Is

## Comments appeared in the output

Check:

1. Footnotes & Comments settings
2. Compile Options
3. whether comments are inline annotations or inspector comments
4. whether the selected output format supports the chosen behavior

## Footnotes are missing

Check:

1. Footnotes & Comments settings
2. Compatibility settings
3. output format
4. whether notes are inline or inspector footnotes
5. whether the target file type supports the expected note behavior

## The wrong documents exported

Check:

1. Contents Settings
2. Include checkboxes
3. selected compile group
4. selected collection
5. Binder selection
6. front/back matter inclusion

## Styles did not survive

Check:

1. Compile Styles
2. Compatibility settings
3. output format
4. whether styles are mapped or stripped
5. whether the target app supports the exported style behavior

## Ebook output has navigation problems

Check:

1. Section Types
2. Section Layouts
3. title generation
4. ToC settings
5. ebook metadata
6. whether front matter is included correctly
7. whether headings are produced as actual headings

## Best debugging rule

Change one compile variable at a time.

If you change the Compile Format, Section Layout assignment, Contents, and Replacements all at once, the failure becomes harder to locate.
