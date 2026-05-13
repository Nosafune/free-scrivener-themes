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
status: draft
---

# Transformations & Replacements

## Fast answer

Transformations and Replacements modify text during compile without permanently changing the draft.

## Why this matters


This is one of Compile’s most useful advanced capabilities.

It allows export-specific changes while preserving the manuscript source.

Examples:

- convert smart quotes
- change ellipses behavior
- replace placeholder-friendly shorthand
- remove draft markers
- change edition-specific terminology
- convert symbols
- adjust formatting conventions


## Core workflow


Basic workflow:

1. Identify text that should change only at export.
2. Add a replacement rule.
3. Keep replacement scope narrow.
4. Compile a short test.
5. Search the output for false positives.
6. Document the rule.

Example:

| Draft text | Compiled text |
|---|---|
| `CHAPTER_NUMBER` | `<$t:chapter>` |
| `[DRAFT_ONLY]` | empty string |
| `--` | em dash |


## Common mistakes


### Broad replacements

Replacing common words can damage the manuscript.

### No test search

Always search compiled output for unexpected replacements.

### Using replacements as a substitute for revision

Replacements are output tools, not a writing-quality fix.

### Forgetting order

Multiple replacement rules may interact.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## High-value replacement use cases

### Placeholder readability

Draft:

```text
PART_NUMBER
```

Compile replacement:

```text
<$t:part>
```

### Edition-specific text

Draft:

```text
[[EDITION_NOTE]]
```

Ebook replacement:

```text
Available in the expanded edition.
```

Print replacement:

```text

```

### Cleanup

Remove internal drafting tokens:

```text
[CHECK]
[TODO]
[DRAFT]
```

Do this carefully. Search first.


## Related pages

- [Project Replacements](27-project-replacements.md)
- [Using Placeholders](04-using-placeholders.md)
- [Compile Options](26-compile-options.md)
