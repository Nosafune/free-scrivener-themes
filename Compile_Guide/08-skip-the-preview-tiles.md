---
title: Skip the preview tiles
slug: skip-the-preview-tiles
part: Compiling
sequence: 8
tags:
  - compile
  - preview
  - section-layouts
difficulty: intermediate
---

# Skip the preview tiles

## Fast answer

Preview tiles show approximate layout behavior, not the finished manuscript. Use them for orientation, then move to a real test compile for any serious verification.

## What preview tiles are good for

- Choosing between title-only vs title-and-text layouts
- Identifying whether a page break is present
- Comparing heading styles at a glance
- Picking a starting point when you are unsure which layout family to use

## What preview tiles cannot show you

Preview tiles use sample text, not your project's actual content. They cannot accurately show:

- Placeholder behavior
- Footnote and endnote rendering
- Page headers and footers
- Ebook navigation
- Replacements
- Custom metadata
- Compatibility settings
- How your specific Binder titles will appear as headings

For any of these, compile a real test.

## Recommended approach

1. Scan preview tiles for broad layout behavior.
2. Select the closest-looking layout.
3. Assign it.
4. Compile a short sample (one chapter with a scene or two).
5. Open the output file externally and evaluate.
6. Return to preview tiles only if you need to switch layout families entirely.

Do not spend time fine-tuning in preview. The real output is the only ground truth.

## Common mistakes

**Expecting exact output.** Preview tiles are illustrative, not predictive.

**Spending too long comparing tiles.** Choose a likely layout and test. Iteration on real output is faster than deliberation in preview.

**Ignoring actual document settings.** Metadata, replacement rules, and footnote behavior are invisible in preview and very visible in output.

## Related pages

- [Assigning Section Layouts to Section Types](07-assigning-section-layouts-to-section-types.md)
- [Section Layouts](11-section-layouts.md)
- [Deep dive into Compile](01-deep-dive-into-compile.md)
