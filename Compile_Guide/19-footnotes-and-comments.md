---
title: Footnotes & Comments
slug: footnotes-and-comments
part: Compiling
sequence: 19
tags:
  - compile
  - footnotes
  - comments
  - editing
difficulty: intermediate
status: complete
---

# Footnotes & Comments

## Fast answer

This area controls whether notes and comments appear in compiled output and how they are represented.

## Why this matters


Footnotes and comments have different editorial meanings.

Footnotes/endnotes may be part of the published work.

Comments are usually internal editorial material.

Compile needs explicit instructions for each.


## Core workflow


Basic workflow:

1. Decide whether comments should be included.
2. Decide whether footnotes should be footnotes or endnotes.
3. Check whether notes are inline or inspector-based.
4. Choose output behavior in Compile.
5. Compile a short test.
6. Inspect in target output application.

For editorial submissions, comments may be useful.

For final publication, comments are usually removed.


## Common mistakes


### Accidentally exporting comments

This is a common professional mistake.

### Losing footnotes

Output format and compatibility settings can change note behavior.

### Confusing comments with footnotes

They are separate systems.

### Not checking the final file

Always open the exported document externally.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Endnote placement

Some workflows use an endnote placement placeholder:

```text
<$--ENDNOTES-->
```

This tells Compile where endnotes should appear.

## Linked comments

Some workflows use:

```text
<$--COMMENTS-->
```

Use this only when the chosen output behavior and file type support it.

## Editorial rule

Before final export, run a dedicated notes check:

- intentional footnotes remain
- comments removed
- annotations removed
- endnote position verified


## Related pages

- [Compile Options](26-compile-options.md)
- [Compatibility](21-compatibility.md)
- [Contents Settings](22-contents-settings.md)
