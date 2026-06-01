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
---

# Footnotes & Comments

## Fast answer

Footnotes and comments are separate systems with separate compile behaviors. Set each intentionally before any serious export.

## The difference

**Footnotes/endnotes** are typically part of the published work: citations, clarifications, academic notes.

**Comments** (inspector comments and inline annotations) are typically internal editorial material: notes to yourself, questions for collaborators, revision flags.

Compile needs explicit instructions for each.

## Footnotes/endnotes workflow

1. Decide: footnotes or endnotes?
2. Decide: are these inline notes or inspector notes? (They are stored differently in Scrivener.)
3. Open Footnotes & Comments in the Compile panel or Format Designer.
4. Set the behavior for each note type.
5. Compile a test with at least one note.
6. Open the output file externally and confirm note rendering.

Endnote placement uses this placeholder in the document where you want them to appear:

```
<$--ENDNOTES-->
```

## Comments workflow

Comments almost never belong in a final export. Before any serious compile:

1. Decide whether comments are intentional (editorial pass) or should be removed (final output).
2. Check Footnotes & Comments settings.
3. Check Compile Options.
4. Compile a test.
5. Search the output file for comment text to confirm removal.

## Output format notes

| Output | Footnotes | Comments |
|---|---|---|
| Word | Yes, full support | Yes, shown as track-changes style |
| PDF | Yes, printed | Generally not shown |
| EPUB | Varies by reader | Generally not supported |
| Plain text | Stripped or inline | Stripped or inline |

## Common mistakes

**Accidentally exporting comments to a reader or editor.** This is a common professional mistake. Always run a post-compile search on sensitive exports.

**Losing footnotes by switching output format.** Note behavior can change when you switch Compile For. Test every output type independently.

**Confusing comments with footnotes.** They are stored separately and configured separately. Checking one does not affect the other.

## Editorial rule

Before final export, run a dedicated notes check:

- intentional footnotes remain
- comments removed
- annotations removed
- endnote placement confirmed

## Related pages

- [Compile Options](26-compile-options.md)
- [Compatibility](21-compatibility.md)
- [Contents Settings](22-contents-settings.md)
