---
title: Project Replacements
slug: project-replacements
part: Compiling
sequence: 27
tags:
  - compile
  - replacements
  - project
  - workflow
difficulty: intermediate
status: complete
---

# Project Replacements

## Fast answer

Project Replacements perform project-specific compile-time substitutions, useful for edition logic, placeholder simplification, and cleanup.

## Why this matters


Project Replacements are transformations scoped to the project.

They let you keep the manuscript source stable while changing output.

Use them for:

- readable placeholder aliases
- edition-specific text
- symbol replacement
- cleanup tokens
- formatting-sensitive substitutions
- names that differ by version


## Core workflow


Basic workflow:

1. Identify the source text to replace.
2. Decide the compiled output.
3. Add the replacement rule.
4. Keep it narrow.
5. Compile a short test.
6. Search output for false positives.
7. Document the replacement.

Example:

| Draft token | Replacement |
|---|---|
| `{{PROJECT_TITLE}}` | `<$projecttitle>` |
| `{{CHAPTER_NUMBER}}` | `<$t:chapter>` |
| `[[REMOVE_FOR_FINAL]]` | empty |


## Common mistakes


### Replacing ordinary words

Never replace common prose unless you fully understand the consequences.

### Using invisible rules

Document every replacement.

### Forgetting different compile formats

A replacement needed for ebook may not be wanted for print.

### No false-positive test

Search the output after compiling.


## Practical test

Compile a small sample before compiling the full manuscript. Use one chapter, one scene, one front matter item, and one item that uses the setting being tested.

## Troubleshooting lens

When output looks wrong, ask:

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?


## Replacement governance

For serious projects, maintain a replacement log:

| Token | Replacement | Used in format | Purpose |
|---|---|---|---|
| `{{CHAPTER_NUMBER}}` | `<$t:chapter>` | All | readable placeholder |
| `[[BETA_NOTE]]` | empty | Final | remove beta-only notes |
| `--` | em dash | Print | typography cleanup |

## Best practice

Use unusual token syntax for replacement sources:

```text
{{LIKE_THIS}}
[[OR_THIS]]
```

Do not use words that might appear naturally in prose.


## Related pages

- [Transformations & Replacements](17-transformations-and-replacements.md)
- [Using Placeholders](04-using-placeholders.md)
- [Compile Options](26-compile-options.md)
