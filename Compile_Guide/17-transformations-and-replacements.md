---
title: Transformations & Replacements
slug: transformations-and-replacements
part: Compiling
sequence: 17
tags:
  - compile
  - replacements
  - transformations
  - editing
difficulty: intermediate
---

# Transformations & Replacements

## Fast answer

Transformations and Replacements modify text during compile without permanently changing the draft. They fire at export time and affect only the output file.

## Why this is useful

This is one of Compile's most practical advanced capabilities. It lets you keep the manuscript source clean while producing export-specific changes:

- convert smart quotes to straight quotes (or vice versa)
- replace readable draft shorthand with actual placeholders
- remove draft markers before sending to a reader
- change edition-specific terminology between print and ebook
- convert symbols or special characters

The source manuscript is never touched.

## Transformations vs Replacements

**Transformations** are built-in automatic conversions: smart quote style, ellipsis handling, dash conversion, whitespace cleanup. They apply globally based on checkboxes.

**Replacements** are custom rules you write: find this text, output that text. They are more powerful and more targeted.

## Replacement examples

| Draft text | Compiled output |
|---|---|
| CHAPTER_NUMBER | `<$t:chapter>` |
| [DRAFT_ONLY] | (empty string) |
| -- | em dash |

## Replacement workflow

1. Identify text that should change only at export.
2. Add a replacement rule (Compile Format Designer > Replacements).
3. Keep the source text narrow and distinctive.
4. Compile a short test.
5. Search the output for false positives.
6. Document the rule for future reference.

## Good replacement token design

Use unusual syntax that will not appear in normal prose:

```
{{LIKE_THIS}}
[[OR_THIS]]
```

Avoid replacing common words. Replacing "the" is not safe.

## Multiple replacements and ordering

Replacement rules apply in the order listed. If one replacement produces text that a later replacement would also match, the rules interact. Check ordering carefully when using multiple replacements.

## Common mistakes

**Broad source text.** Replacing a common word can damage large sections of the manuscript.

**No post-compile search.** Always search the compiled output for unexpected replacements before sending.

**Using replacements as a substitute for revision.** Replacements are output tools, not writing quality fixes.

## Related pages

- [Project Replacements](27-project-replacements.md)
- [Using Placeholders](04-using-placeholders.md)
- [Compile Options](26-compile-options.md)
