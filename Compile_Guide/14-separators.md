---
title: Separators
slug: separators
part: Compiling
sequence: 14
tags:
  - compile
  - separators
  - formatting
difficulty: intermediate
status: draft
---

# Separators

## Fast answer

Separators control what appears between compiled Binder items: nothing, a blank line, a page break, a symbol, or custom text.

## Why this matters


Separators are critical because Scrivener projects are modular.

When many small documents become one output file, Compile needs to know how to join them.

Separators answer:

```text
What goes between these two compiled items?
```

Examples:

- page break before a chapter
- blank line between sections
- scene break symbol
- no separator between fragments
- custom divider


## Core workflow


Basic workflow:

1. Identify the boundary being controlled.
2. Determine the relevant Section Layouts or compile settings.
3. Choose separator behavior.
4. Test with adjacent documents.
5. Test with empty or title-only documents.
6. Test with chapter transitions and scene transitions.

Common separators:

```text
No separator
Single return
Empty line
Page break
#
***
Custom text
```


## Common mistakes


### Using separators to fix structure problems

If chapters and scenes are assigned incorrectly, separators become chaotic.

### Inconsistent scene documents

Some scenes may have titles, some may not.

### Using manual scene break symbols everywhere

Let Compile insert consistent separators when possible.

### Forgetting ebook behavior

Page breaks and separators behave differently in reflowable formats.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Separator decision table

| Boundary | Common separator |
|---|---|
| Part to Chapter | page break |
| Chapter to Scene | page break or no extra separator |
| Scene to Scene | scene break symbol or blank line |
| Front matter items | page break |
| Appendix entries | page break or heading separator |
| Micro-fragments | no separator |

## Testing tip

Create three consecutive scenes:

```text
Scene A
Scene B
Scene C
```

Compile them with your separator rule. If the result looks wrong here, it will look wrong everywhere.


## Related pages

- [Section Layouts](11-section-layouts.md)
- [Give a paragraph some room](13-give-a-paragraph-some-room.md)
- [Page Settings](20-page-settings.md)
