---
title: Can't find Compile Formatting Settings?
slug: cant-find-compile-formatting-settings
part: Compiling
sequence: 12
tags:
  - compile
  - troubleshooting
  - formatting
difficulty: intermediate
---

# Can't find Compile Formatting Settings?

## Fast answer

If formatting settings seem missing, you are probably looking at the project-level Compile screen instead of the Compile Format Designer. Most formatting controls live inside the Format Designer, not in the main Compile panel.

## The split that confuses people

Scrivener separates project-level compile choices from format-level formatting rules.

**Project-level (main Compile panel):**

- what to compile (Contents)
- metadata for this export
- Section Layout assignments
- some options

**Format-level (Compile Format Designer):**

- Section Layout formatting (font, spacing, indent, page break)
- title prefix and suffix
- separator behavior
- style mappings
- transformations
- compatibility behavior

If you are looking for a formatting setting and cannot find it in the main Compile panel, it is in the Format Designer.

## How to get there

1. In the Compile panel, identify the Compile Format being used.
2. Right-click the format and choose Edit Format (or double-click it).
3. This opens the Compile Format Designer.
4. Find the Section Layout responsible for the problem document.
5. Edit that layout's settings.
6. Compile a test.

## Fast diagnosis table

| Problem | Where to look |
|---|---|
| Wrong documents included | Contents Settings |
| Wrong heading style | Section Layout assignment or layout design in Format Designer |
| Missing heading | Section Layout title/text settings |
| Wrong page break | Section Layout New Page setting or Separators |
| Wrong author or title | Metadata Settings |
| Comments showing in output | Footnotes & Comments, Compile Options |
| Styles wrong | Compile Styles, Compatibility |
| Spacing wrong | Section Layout paragraph settings |

## Common mistakes

**Looking for Scrivener 2 settings.** Scrivener 3 redesigned Compile. The old hierarchy-based checkboxes are gone. Section Types and Section Layouts replaced them.

**Editing Project Settings instead of Format Designer.** Project Settings controls Section Type definitions. The Format Designer controls how those types are formatted.

## Related pages

- [Using the Compile Format Designer](09-using-the-compile-format-designer.md)
- [Section Layouts](11-section-layouts.md)
- [Contents Settings](22-contents-settings.md)
- [Compile Troubleshooting](00-compile-troubleshooting.md)
