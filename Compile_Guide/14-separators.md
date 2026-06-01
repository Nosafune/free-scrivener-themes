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
---

# Separators

## Fast answer

Separators control what appears between compiled Binder items: nothing, a blank line, a page break, a symbol, or custom text.

## Why separators matter

Scrivener projects are modular -- a novel might be 80 separate Binder documents. When Compile assembles them into one output file, it needs rules for what goes between each item.

Separators answer: What goes between Scene A and Scene B? What goes between Chapter Two and Chapter Three?

## Common separator values

```
No separator
Single return
Empty line
Page break
#
***
Custom text or symbol
```

## Separator decision table

| Boundary | Common separator |
|---|---|
| Part to Chapter | page break |
| Chapter to first Scene | no separator (chapter heading is the break) |
| Scene to Scene | scene break symbol or empty line |
| Front matter items | page break |
| Appendix entries | page break or heading separator |
| Micro-fragments | no separator |

## How separators are configured

Separators are set in two places:

- **Section Layout settings:** each layout can define its own separator before and after
- **Separators pane in the Format Designer:** global overrides for between-item behavior

Check both locations if separator output looks wrong.

## Testing tip

Create three consecutive scenes and compile them. If the separator result looks wrong for three scenes, it will look wrong everywhere. Isolate the problem on a small test before troubleshooting the full manuscript.

## Common mistakes

**Using separators to fix structure problems.** If chapters and scenes are assigned incorrectly, separator output becomes chaotic. Fix the structure and assignment first.

**Using manual scene break symbols in every document.** Let Compile insert consistent separators from the Section Layout or Separators settings. Manual symbols create inconsistency and are hard to change globally.

**Forgetting ebook behavior.** Page breaks and separators behave differently in reflowable ebook formats. Test EPUB output separately from PDF output.

## Related pages

- [Section Layouts](11-section-layouts.md)
- [Give a paragraph some room](13-give-a-paragraph-some-room.md)
- [Page Settings](20-page-settings.md)
