---
title: Compile Troubleshooting
slug: compile-troubleshooting
part: Compiling
tags:
  - compile
  - troubleshooting
  - reference
difficulty: intermediate
---

# Compile Troubleshooting

Use this page when output is wrong but the cause is unclear.

## The best first question

When something compiles wrong, ask:

> Which Section Type does this Binder item have, and which Section Layout is assigned to that type?

That question resolves the majority of compile problems.

## The debugging rule

Change one compile variable at a time. If you change the Compile Format, Section Layout assignment, Contents, and Replacements simultaneously, the failure is impossible to isolate. One change. One test compile. Repeat.

## The five-question checklist

1. Is the correct material included?
2. Is the correct Section Type assigned?
3. Is the correct Section Layout assigned?
4. Is the selected Compile Format the one being edited?
5. Is the output format capable of showing the thing you expect?

---

## Headings are wrong

1. Is the Binder item assigned the correct Section Type?
2. Is that Section Type assigned to the intended Section Layout?
3. Does the selected Compile Format contain the layout you expect?
4. Are you editing a copy of the format, not the original?
5. Did you compile to the same output type you checked the preview for?

## Chapter numbers are wrong

1. Is the numbering placeholder in the Section Layout prefix, suffix, or title field?
2. Is it using the correct stream name?
3. Does numbering need to restart at some point?
4. Are front matter documents accidentally consuming the numbering stream?
5. Are chapter headings and scene text assigned to different layouts?

## Text spacing is wrong

1. Check Section Layout paragraph formatting: spacing before/after and line spacing.
2. Check first-line indent settings.
3. Check separator settings.
4. Check whether the affected text is compiled As-Is.

## Comments appeared in the output

1. Check Footnotes & Comments settings.
2. Check Compile Options.
3. Are these inline annotations or inspector comments? They may behave differently.
4. Does the output format support the chosen comment behavior?

## Footnotes are missing

1. Check Footnotes & Comments settings.
2. Check Compatibility settings.
3. Confirm the output format supports the note type you are using.
4. Are the notes inline or inspector-based? Confirm which type is configured.

## The wrong documents exported

1. Check Contents Settings and the compile group.
2. Check Include checkboxes on individual documents.
3. Check front matter and back matter inclusion settings.
4. Are you compiling a Binder selection by accident?

## Styles did not survive

1. Check Compile Styles settings.
2. Check Compatibility settings.
3. Confirm the output format supports the style behavior you expect.
4. Are styles mapped or stripped in the current format?

## Ebook navigation is broken

1. Check Section Types on all items.
2. Check Section Layout title generation -- headings must be generated as actual headings for EPUB navigation to work.
3. Check ToC settings and ebook metadata.
4. Is front matter included in the right place with the right start location?

## Related pages

- [Compile Roadmap](00-compile-roadmap.md)
- [Compile Preflight Checklists](00-compile-preflight-checklists.md)
- [Can't find Compile Formatting Settings?](12-cant-find-compile-formatting-settings.md)
