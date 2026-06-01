---
title: Compile Styles
slug: compile-styles
part: Compiling
sequence: 15
tags:
  - compile
  - styles
  - formatting
difficulty: intermediate
---

# Compile Styles

## Fast answer

Compile Styles determine how styled text from the Editor is preserved, transformed, or reformatted during export.

## Why styles matter at compile time

Styles describe meaning. A paragraph tagged "Block Quote" carries semantic information that Compile can act on consistently -- changing font, indentation, or output-format treatment in one place rather than hunting through the manuscript.

Manual formatting (direct bold, random indents, hand-typed font changes) gives Compile nothing semantic to work with. It either gets stripped or passes through unchanged, depending on the format.

## Where Compile Styles fit

A Section Layout defines the baseline formatting for body text. Compile Styles define exceptions within that body text:

```
Body text formatting  ->  Section Layout
Block Quote           ->  Compile Style (exception)
Verse                 ->  Compile Style (exception)
Caption               ->  Compile Style (exception)
```

## Workflow

1. Use styles in the editor only for text that needs special treatment.
2. Confirm which styles exist in the project (Format > Styles).
3. Open Compile Styles settings in the Format Designer.
4. For each style: preserve it, rename it, reformat it, or strip it.
5. Test in the target output.

## Good style names

Name styles for what they mean, not what they look like:

| Bad | Good |
|---|---|
| Blue 14pt | Block Quote |
| Indented Thing | Letter |
| Looks Nice | Epigraph |

Semantic names survive format changes. Appearance-based names become meaningless when you change output formats.

## Common mistakes

**Styling ordinary body text.** Body text usually does not need a style. Over-styling makes Compile Styles harder to manage.

**Confusing Editor styles with Section Layouts.** Styles affect text inside documents. Section Layouts affect entire Binder items. They are separate systems that work together.

**Manual formatting instead of styles.** Manual formatting is invisible to Compile Styles and hard to control globally.

**Not checking output app behavior.** Word, PDF, and EPUB handle styles differently. Test in each target format.

## Related pages

- [Section Layouts](11-section-layouts.md)
- [Compatibility](21-compatibility.md)
- [Transformations & Replacements](17-transformations-and-replacements.md)
