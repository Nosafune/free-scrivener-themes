# Free Scrivener Themes

Windows Scrivener 3.x theme collection and small compiler.

## Preview Screenshots

Preview renders generated from the current seed palettes.
Regenerate them with:

```powershell
python scripts/render_theme_previews.py
```

### Mani Katti

![Mani Katti preview](assets/readme-previews/mani_katti.png)

### Salva la Reina

![Salva la Reina preview](assets/readme-previews/salva_la_reina.png)

### Majima No Aniki

![Majima No Aniki preview](assets/readme-previews/majima.png)

## What Is Here

- `themes/obsidian_vault_amber.scrtheme`
- `themes/obsidian_vault_warm.scrtheme`
- `themes/mani_katti.scrtheme`
- `themes/salva_la_reina.scrtheme`
- `themes/majima.scrtheme`

The first two are the legacy template/reference bundles already in this repo.
The Nosafune-seeded themes are generated from the compiler pipeline.

## Build

Rebuild the generated themes with:

```powershell
python scripts/scrivener_theme_compiler.py build
```

Verify the generated bundles with:

```powershell
python scripts/scrivener_theme_compiler.py verify
```

Rebuild and verify in one pass:

```powershell
python scripts/scrivener_theme_compiler.py build --verify
```

Build-time dependency:
- Python 3
- `PySide6`

## Install

Download any `.scrtheme` file from `themes/`, then import it in Scrivener via:

`Window > Themes > Import Themes`

## Source Palette Contract

The generated themes use Nosafune seed palettes with these fields:

- `page_background`
- `body_text`
- `secondary_text`
- `accent_text`
- `ornament_color`
- `header_footer_color`
- `chapter_title_color`
- `scene_break_color`

The compiler expands those seed values into the extra UI roles Scrivener needs.
