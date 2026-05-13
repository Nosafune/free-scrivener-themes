from __future__ import annotations

import argparse
import json
import math
import shutil
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PySide6.QtCore import QSettings
from PySide6.QtGui import QColor


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "source" / "nosafune_seed_palettes.json"
TEMPLATE_BUNDLE = ROOT / "themes" / "obsidian_vault_amber.scrtheme"
OUTPUT_DIR = ROOT / "themes"


@dataclass(frozen=True)
class ThemeSeed:
    theme_id: str
    display_name: str
    output_suffix: str
    profile: str
    page_background: str
    body_text: str
    secondary_text: str
    accent_text: str
    ornament_color: str
    header_footer_color: str
    chapter_title_color: str
    scene_break_color: str
    default_scene_break_glyph: str


@dataclass(frozen=True)
class DerivedPalette:
    window_bg: str
    editor_bg: str
    panel_bg: str
    panel_bg_strong: str
    tooltip_bg: str
    text_primary: str
    text_muted: str
    text_disabled: str
    text_bright: str
    accent_primary: str
    accent_soft: str
    divider: str
    selection_bg: str
    selection_text: str
    focus_ring: str
    title_text: str
    title_bg: str
    button_bg: str
    button_text: str
    link_visited: str
    light: str
    midlight: str
    mid: str
    dark: str
    shadow: str
    revision_1: str
    revision_2: str
    revision_3: str
    revision_4: str
    revision_5: str
    snapshot_deleted: str
    snapshot_new: str
    snapshot_bg: str
    progress_start: str
    progress_midway: str
    progress_end: str
    progress_overflow: str


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    hex_value = value.strip().lstrip("#")
    if len(hex_value) != 6:
        raise ValueError(f"Invalid hex color: {value!r}")
    return tuple(int(hex_value[index : index + 2], 16) for index in (0, 2, 4))


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def clamp_channel(value: float) -> int:
    return max(0, min(255, int(round(value))))


def mix(a: str, b: str, amount: float) -> str:
    ar, ag, ab = hex_to_rgb(a)
    br, bg, bb = hex_to_rgb(b)
    return rgb_to_hex(
        (
            clamp_channel(ar + (br - ar) * amount),
            clamp_channel(ag + (bg - ag) * amount),
            clamp_channel(ab + (bb - ab) * amount),
        )
    )


def luminance(hex_value: str) -> float:
    def channel(value: int) -> float:
        channel_value = value / 255
        if channel_value <= 0.03928:
            return channel_value / 12.92
        return ((channel_value + 0.055) / 1.055) ** 2.4

    r, g, b = hex_to_rgb(hex_value)
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(a: str, b: str) -> float:
    lum_a = luminance(a)
    lum_b = luminance(b)
    high = max(lum_a, lum_b)
    low = min(lum_a, lum_b)
    return (high + 0.05) / (low + 0.05)


def best_contrast(candidates: Iterable[str], background: str) -> str:
    best = None
    best_ratio = -1.0
    for candidate in candidates:
        ratio = contrast_ratio(candidate, background)
        if ratio > best_ratio:
            best = candidate
            best_ratio = ratio
    if best is None:
        raise ValueError("No candidates provided")
    return best


def best_text_on(background: str, preferred: str | None = None) -> str:
    candidates = [c for c in [preferred, "#FFFDF7", "#111111"] if c]
    return best_contrast(candidates, background)


def adjust_toward(base: str, toward: str, background: str, minimum_ratio: float) -> str:
    if contrast_ratio(base, background) >= minimum_ratio:
        return base

    low = 0.0
    high = 1.0
    best = base
    for _ in range(32):
        amount = (low + high) / 2
        candidate = mix(base, toward, amount)
        ratio = contrast_ratio(candidate, background)
        if ratio >= minimum_ratio:
            best = candidate
            high = amount
        else:
            low = amount
    return best


def adjust_away(base: str, background: str, target_ratio: float, toward: str) -> str:
    current = contrast_ratio(base, background)
    if math.isclose(current, target_ratio, abs_tol=0.05):
        return base
    if current < target_ratio:
        return adjust_toward(base, toward, background, target_ratio)

    low = 0.0
    high = 1.0
    best = base
    for _ in range(32):
        amount = (low + high) / 2
        candidate = mix(base, background, amount)
        ratio = contrast_ratio(candidate, background)
        if ratio <= target_ratio:
            best = candidate
            high = amount
        else:
            low = amount
    return best


def is_dark(hex_value: str) -> bool:
    return luminance(hex_value) < 0.45


def choose_divider(seed: ThemeSeed, palette_bg: str, dark_theme: bool) -> str:
    if contrast_ratio(seed.ornament_color, palette_bg) >= 3.0:
        divider = seed.ornament_color
    elif contrast_ratio(seed.secondary_text, palette_bg) >= 2.85:
        divider = seed.secondary_text
    else:
        divider = seed.accent_text
    target_ratio = 3.35 if dark_theme else 3.0
    if contrast_ratio(divider, palette_bg) > target_ratio + 0.75:
        divider = adjust_away(divider, palette_bg, target_ratio, "#FFFFFF" if dark_theme else "#000000")
    elif contrast_ratio(divider, palette_bg) < target_ratio:
        divider = adjust_toward(divider, "#FFFFFF" if dark_theme else "#000000", palette_bg, target_ratio)
    return divider


def derive_palette(seed: ThemeSeed) -> DerivedPalette:
    window_bg = seed.page_background
    dark_theme = is_dark(window_bg)
    text_primary = adjust_toward(
        seed.body_text,
        "#FFFDF7" if dark_theme else "#111111",
        window_bg,
        7.0,
    )
    text_muted = adjust_toward(
        seed.secondary_text,
        "#FFFDF7" if dark_theme else "#111111",
        window_bg,
        4.25,
    )
    accent_base = seed.accent_text
    accent_primary = adjust_toward(
        accent_base,
        "#FFF8EE" if dark_theme else "#111111",
        window_bg,
        4.5,
    )
    accent_soft = mix(accent_primary, window_bg, 0.42 if dark_theme else 0.28)
    divider = choose_divider(seed, window_bg, dark_theme)
    panel_bg = mix(window_bg, text_primary, 0.08 if dark_theme else 0.05)
    panel_bg_strong = mix(window_bg, text_primary, 0.14 if dark_theme else 0.09)
    editor_bg = mix(window_bg, panel_bg, 0.06 if dark_theme else 0.03)
    tooltip_bg = mix(panel_bg_strong, window_bg, 0.08 if dark_theme else 0.05)
    selection_bg = accent_primary
    selection_text = best_text_on(selection_bg, text_primary)
    focus_ring = mix(accent_primary, selection_bg, 0.12)
    title_text = adjust_toward(
        best_contrast([seed.chapter_title_color, accent_primary, seed.header_footer_color], window_bg),
        "#FFFDF7" if dark_theme else "#111111",
        window_bg,
        4.75,
    )
    title_bg = mix(panel_bg_strong, accent_soft, 0.10 if dark_theme else 0.07)
    button_bg = panel_bg_strong
    button_text = best_text_on(button_bg, text_primary)
    link_visited = mix(accent_primary, divider, 0.45)
    text_bright = best_text_on(window_bg, None)
    text_disabled = mix(text_primary, window_bg, 0.56 if dark_theme else 0.48)

    light = mix(button_bg, text_primary, 0.20 if dark_theme else 0.14)
    midlight = mix(button_bg, text_primary, 0.10 if dark_theme else 0.08)
    mid = mix(button_bg, window_bg, 0.15 if dark_theme else 0.12)
    dark = mix(window_bg, "#000000", 0.18 if dark_theme else 0.28)
    shadow = mix(window_bg, "#000000", 0.40 if dark_theme else 0.52)

    snapshot_deleted = mix("#C65D4A", window_bg, 0.18 if dark_theme else 0.06)
    snapshot_new = mix("#2F9E5D", window_bg, 0.18 if dark_theme else 0.06)
    snapshot_bg = panel_bg
    progress_start = mix(accent_primary, window_bg, 0.12)
    progress_midway = mix(progress_start, divider, 0.35)
    progress_end = title_text
    progress_overflow = snapshot_deleted

    revision_1 = accent_primary
    revision_2 = mix(accent_primary, accent_soft, 0.40)
    revision_3 = title_text
    revision_4 = mix(divider, text_muted, 0.35)
    revision_5 = mix(accent_soft, divider, 0.45)

    return DerivedPalette(
        window_bg=window_bg,
        editor_bg=editor_bg,
        panel_bg=panel_bg,
        panel_bg_strong=panel_bg_strong,
        tooltip_bg=tooltip_bg,
        text_primary=text_primary,
        text_muted=text_muted,
        text_disabled=text_disabled,
        text_bright=text_bright,
        accent_primary=accent_primary,
        accent_soft=accent_soft,
        divider=divider,
        selection_bg=selection_bg,
        selection_text=selection_text,
        focus_ring=focus_ring,
        title_text=title_text,
        title_bg=title_bg,
        button_bg=button_bg,
        button_text=button_text,
        link_visited=link_visited,
        light=light,
        midlight=midlight,
        mid=mid,
        dark=dark,
        shadow=shadow,
        revision_1=revision_1,
        revision_2=revision_2,
        revision_3=revision_3,
        revision_4=revision_4,
        revision_5=revision_5,
        snapshot_deleted=snapshot_deleted,
        snapshot_new=snapshot_new,
        snapshot_bg=snapshot_bg,
        progress_start=progress_start,
        progress_midway=progress_midway,
        progress_end=progress_end,
        progress_overflow=progress_overflow,
    )


def load_seeds() -> list[ThemeSeed]:
    payload = json.loads(SOURCE_FILE.read_text(encoding="utf-8"))
    return [ThemeSeed(**item) for item in payload]


def seed_style(seed: ThemeSeed) -> str:
    return "Dark" if is_dark(seed.page_background) else "Light"


def update_manifest(xml_text: str, theme: ThemeSeed, output_stem: str, style: str) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        "<ScrivenerThemes>\n"
        f'    <ScrivenerTheme name="{theme.display_name}" style="{style}">\n'
        f"        <qtstylesheet>{output_stem}.qss</qtstylesheet>\n"
        f"        <palette>{output_stem}.pal</palette>\n"
        f'        <preferences load="Colors">{output_stem}.prefs</preferences>\n'
        "    </ScrivenerTheme>\n"
        "</ScrivenerThemes>\n"
    )


def qsettings_path_key(key: str) -> str:
    return key.replace("\\", "/")


def set_color(settings: QSettings, key: str, value: str) -> None:
    settings.setValue(qsettings_path_key(key), QColor(value))


def update_prefs(prefs_path: Path, theme: ThemeSeed, palette: DerivedPalette) -> None:
    settings = QSettings(str(prefs_path), QSettings.Format.IniFormat)

    color_map = {
        "Appearance\\Colors\\BinderBackground": palette.panel_bg,
        "Appearance\\Colors\\BookmarksBackground": palette.panel_bg_strong,
        "Appearance\\Colors\\CommentsAreaBackgroundColorMainWindow": palette.panel_bg,
        "Appearance\\Colors\\CommentsAreaBackgroundColorQuickReference": palette.panel_bg_strong,
        "Appearance\\Colors\\CorkboardBackground": palette.editor_bg,
        "Appearance\\Colors\\DocumentNotesBackground": palette.panel_bg_strong,
        "Appearance\\Colors\\FifthRevision": palette.revision_5,
        "Appearance\\Colors\\FirstRevision": palette.revision_1,
        "Appearance\\Colors\\FourthRevision": palette.revision_4,
        "Appearance\\Colors\\FreeformBackground": palette.editor_bg,
        "Appearance\\Colors\\LabelViewBackground": palette.editor_bg,
        "Appearance\\Colors\\OutlinerBackground": palette.panel_bg,
        "Appearance\\Colors\\OutlinerFolderTitlesTextColor": palette.text_primary,
        "Appearance\\Colors\\OutlinerGridColor": palette.divider,
        "Appearance\\Colors\\OutlinerGroupTitlesTextColor": palette.title_text,
        "Appearance\\Colors\\OutlinerSynopsesTextColor": palette.text_muted,
        "Appearance\\Colors\\RecentSearchResultsBackground": palette.panel_bg_strong,
        "Appearance\\Colors\\ScratchPadBackground": palette.panel_bg,
        "Appearance\\Colors\\ScratchPadText": palette.text_primary,
        "Appearance\\Colors\\ScriveningsTitlesBackgroundColor": palette.title_bg,
        "Appearance\\Colors\\ScriveningsTitlesColor": palette.title_text,
        "Appearance\\Colors\\SecondRevision": palette.revision_2,
        "Appearance\\Colors\\SnapshotDeletedText": palette.snapshot_deleted,
        "Appearance\\Colors\\SnapshotNewText": palette.snapshot_new,
        "Appearance\\Colors\\SnapshotTextBackground": palette.snapshot_bg,
        "Appearance\\Colors\\TargetProgressEndColor": palette.progress_end,
        "Appearance\\Colors\\TargetProgressMidwayColor": palette.progress_midway,
        "Appearance\\Colors\\TargetProgressOverflowColor": palette.progress_overflow,
        "Appearance\\Colors\\TargetProgressStartColor": palette.progress_start,
        "Appearance\\Colors\\ThirdRevision": palette.revision_3,
    }

    for key, value in color_map.items():
        set_color(settings, key, value)

    settings.setValue("Appearance/CollectionsBackgroundDarkness", 80 if is_dark(theme.page_background) else 30)
    settings.setValue("Appearance/InlineFootnotesFont", "Sitka Text,12,-1,2,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/MainFormatbarHeightPx", 30)
    settings.setValue("Appearance/MainFormatbarIconHeightPx", 18)
    settings.setValue("Appearance/MainToolbarHeightPx", 36)
    settings.setValue("Appearance/MainToolbarIconHeightPx", 20)
    settings.setValue("Appearance/OutlinerRemoveBoldFromTitlesWithoutSynopsisWhenSynopsesAreVisible", True)
    settings.setValue("Appearance/OutlinerRowSpacingTitlesOnlyPts", 6)
    settings.setValue("Appearance/OutlinerRowSpacingWithSynopsesPts", 10)
    settings.setValue("Appearance/OutlinerShowHorGridLines", True)
    settings.setValue("Appearance/OutlinerShowHorGridLinesOnlyInFixedRowHeights", True)
    settings.setValue("Appearance/OutlinerShowVerGridLines", False)
    settings.setValue("Appearance/OutlinerUseBoldForDocGroupTitles", False)
    settings.setValue("Appearance/OutlinerUseBoldForFolderTitles", True)
    settings.setValue("Appearance/OutlinerUseOtherFontForTitlesWhenSynopsesAreHidden", True)
    settings.setValue("Appearance/ScriveningsCenterTitles", True)
    settings.setValue("Appearance/ScriveningsDoNotShowSeparatorsAboveTitles", True)
    settings.setValue("Appearance/ScriveningsMinimumFontSize", 14)
    settings.setValue("Appearance/ScriveningsReduceFontSizePerLevelBy", 4)
    settings.setValue("Appearance/ScriveningsSeparator", "EmptyLine")
    settings.setValue("Appearance/ScriveningsSeparatorStyle", "DashedLine")
    settings.setValue("Appearance/ScriveningsSeparatorStyleScriptwriting", "DashedLine")
    settings.setValue("Appearance/ScriveningsTitlesFont", "Sitka Heading,32,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/ScriveningsUnderlineTitles", False)
    settings.setValue("Appearance/ScriveningsUseTitlesBackgroundColor", False)
    settings.setValue("Appearance/ShowImageDocumentsAsCorkboardPhotos", True)
    settings.setValue("Appearance/ShowIndexCardShadowsInCorkboard", False)
    settings.setValue("Appearance/ShowIndexCardTextLines", False)
    settings.setValue("Appearance/SpellingUnderlineStyle", 7)
    settings.setValue("Appearance/TargetProgressSmoothColors", False)
    settings.setValue("Appearance/alternateOutlinerRowColor", False)
    settings.setValue("Appearance/binderFont3", "Segoe UI,9,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/centerEditorInFixedWidthMode", True)
    settings.setValue("Appearance/centerPagesInPageViewMode", True)
    settings.setValue("Appearance/copyholderZoomPercent", 100)
    settings.setValue("Appearance/defaultEditorWidth", 550)
    settings.setValue("Appearance/documentNotesFont3", "Sitka Small,10,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/documentNotesZoomPercent", 100)
    settings.setValue("Appearance/editorZoomPercent", 100)
    settings.setValue("Appearance/hideMarkupItems", 58)
    settings.setValue("Appearance/highlightCurrentLineInCompositionMode", False)
    settings.setValue("Appearance/highlightCurrentLineInQuickReference", False)
    settings.setValue("Appearance/inspectorCommentsFont3", "Sitka Small,10,-1,2,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/inspectorFootnotesFont3", "Sitka Small,10,-1,2,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/labelTintOpacity", 128)
    settings.setValue("Appearance/mainEditorInspectorNotesAsLinks", True)
    settings.setValue("Appearance/mainEditorScrollBarsNextToTextInFixedWidthMode", False)
    settings.setValue("Appearance/mainEditorUnderlineLinks", True)
    settings.setValue("Appearance/outlinerFont3", "Segoe UI,10,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/outlinerSynopsesFont3", "Segoe UI,10,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/outlinerTitlesFont3", "Segoe UI,11,-1,5,600,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/pageSpacingPt", 20)
    settings.setValue("Appearance/pageViewSizeBasedOnProjectOrCompile", 0)
    settings.setValue("Appearance/projectNotesFont3", "Sitka Small,10,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/projectNotesZoomPercent", 100)
    settings.setValue("Appearance/reloadLastSelectedZoom", True)
    settings.setValue("Appearance/scratchPadFont3", "Sitka Small,10,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/scrivenerGuiFont3", "Segoe UI,9,-1,5,400,0,0,0,0,0,0,0,0,0,0,1")
    settings.setValue("Appearance/showBinderCurrentEditorDocIndicator", True)
    settings.setValue("Appearance/showPageViewMarginGuides", False)
    settings.setValue("Appearance/showProgressBarsInQuickSearchToolbar", True)
    settings.setValue("Appearance/snapshotsZoomPercent", 100)
    settings.setValue("Appearance/useFixedWidthEditor", True)

    settings.sync()
    if settings.status() != QSettings.Status.NoError:
        raise RuntimeError(f"Could not save preferences file: {prefs_path}")


def update_palette(pal_path: Path, theme: ThemeSeed, palette: DerivedPalette) -> None:
    family = {
        "Base": palette.editor_bg,
        "AlternateBase": palette.panel_bg,
        "Window": palette.window_bg,
        "ToolTipBase": palette.tooltip_bg,
        "Button": palette.button_bg,
        "Highlight": palette.selection_bg,
        "WindowText": palette.text_primary,
        "Text": palette.text_primary,
        "BrightText": palette.text_bright,
        "ButtonText": palette.button_text,
        "HighlightedText": palette.selection_text,
        "ToolTipText": palette.text_primary,
        "PlaceholderText": palette.text_disabled,
        "Link": palette.accent_primary,
        "LinkVisited": palette.link_visited,
        "Light": palette.light,
        "Midlight": palette.midlight,
        "Mid": palette.mid,
        "Dark": palette.dark,
        "Shadow": palette.shadow,
        "WindowText:Disabled": palette.text_disabled,
        "Text:Disabled": palette.text_disabled,
        "ButtonText:Disabled": palette.text_disabled,
        "Highlight:Disabled": palette.divider,
    }

    lines = pal_path.read_text(encoding="utf-8").splitlines()
    rewritten: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("//"):
            rewritten.append(line)
            continue

        if "(" not in line or ")" not in line:
            rewritten.append(line)
            continue

        name = line.split("(", 1)[0].strip()
        if name in family:
            r, g, b = hex_to_rgb(family[name])
            comment = line.split("//", 1)[1] if "//" in line else ""
            rewritten.append(f"{name}({r},{g},{b})" + (f" //{comment}" if comment else ""))
        else:
            rewritten.append(line)

    pal_path.write_text("\n".join(rewritten) + "\n", encoding="utf-8")


def rename_bundle_entries(bundle_dir: Path, output_stem: str) -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for file in bundle_dir.iterdir():
        if file.is_file() and file.suffix in {".xml", ".qss", ".pal", ".prefs"}:
            target = bundle_dir / f"{output_stem}{file.suffix}"
            file.rename(target)
            mapping[file.suffix] = target
    return mapping


def compile_theme(seed: ThemeSeed) -> Path:
    palette = derive_palette(seed)
    output_stem = seed.output_suffix
    output_path = OUTPUT_DIR / f"{output_stem}.scrtheme"
    style = seed_style(seed)

    with tempfile.TemporaryDirectory(prefix=f"scrivener-theme-{output_stem}-") as temp_dir_name:
        temp_dir = Path(temp_dir_name)
        extracted_dir = temp_dir / "template"
        extracted_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(TEMPLATE_BUNDLE, "r") as archive:
            archive.extractall(extracted_dir)

        renamed = rename_bundle_entries(extracted_dir, output_stem)
        if {".xml", ".qss", ".pal", ".prefs"} - renamed.keys():
            raise RuntimeError(f"Template bundle missing expected files: {TEMPLATE_BUNDLE}")

        xml_path = renamed[".xml"]
        qss_path = renamed[".qss"]
        pal_path = renamed[".pal"]
        prefs_path = renamed[".prefs"]

        xml_path.write_text(update_manifest(xml_path.read_text(encoding="utf-8"), seed, output_stem, style), encoding="utf-8")
        update_palette(pal_path, seed, palette)
        update_prefs(prefs_path, seed, palette)

        if output_path.exists():
            output_path.unlink()

        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in [xml_path, qss_path, pal_path, prefs_path]:
                archive.write(path, arcname=path.name)

    return output_path


def verify_bundle(bundle_path: Path, expected_stem: str) -> None:
    with zipfile.ZipFile(bundle_path, "r") as archive:
        names = sorted(archive.namelist())
        expected = sorted(
            [
                f"{expected_stem}.xml",
                f"{expected_stem}.qss",
                f"{expected_stem}.pal",
                f"{expected_stem}.prefs",
            ]
        )
        if names != expected:
            raise RuntimeError(f"{bundle_path.name}: expected {expected}, got {names}")

        xml_text = archive.read(f"{expected_stem}.xml").decode("utf-8")
        if f'<ScrivenerTheme name="' not in xml_text:
            raise RuntimeError(f"{bundle_path.name}: missing ScrivenerTheme root")
        if f"<qtstylesheet>{expected_stem}.qss</qtstylesheet>" not in xml_text:
            raise RuntimeError(f"{bundle_path.name}: stylesheet name mismatch")
        if f"<palette>{expected_stem}.pal</palette>" not in xml_text:
            raise RuntimeError(f"{bundle_path.name}: palette name mismatch")
        if f"<preferences load=\"Colors\">{expected_stem}.prefs</preferences>" not in xml_text:
            raise RuntimeError(f"{bundle_path.name}: prefs name mismatch")


def verify_seed(seed: ThemeSeed) -> None:
    required = [
        seed.page_background,
        seed.body_text,
        seed.secondary_text,
        seed.accent_text,
        seed.ornament_color,
        seed.header_footer_color,
        seed.chapter_title_color,
        seed.scene_break_color,
    ]
    for field in required:
        if not isinstance(field, str) or not field.startswith("#") or len(field) != 7:
            raise ValueError(f"{seed.theme_id}: invalid seed color {field!r}")

    palette = derive_palette(seed)
    checks = [
        ("text", palette.text_primary, seed.page_background, 7.0),
        ("muted", palette.text_muted, seed.page_background, 4.25),
        ("selection", palette.selection_text, palette.selection_bg, 4.5),
        ("divider", palette.divider, seed.page_background, 2.75),
    ]
    for label, color, background, minimum in checks:
        ratio = contrast_ratio(color, background)
        if ratio < minimum:
            raise RuntimeError(f"{seed.theme_id}: {label} contrast too low ({ratio:.2f} < {minimum:.2f})")


def build() -> list[Path]:
    seeds = load_seeds()
    outputs: list[Path] = []
    for seed in seeds:
        verify_seed(seed)
        outputs.append(compile_theme(seed))
    return outputs


def verify() -> None:
    seeds = load_seeds()
    for seed in seeds:
        verify_seed(seed)
        verify_bundle(OUTPUT_DIR / f"{seed.output_suffix}.scrtheme", seed.output_suffix)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compile Nosafune seed palettes into Scrivener themes.")
    parser.add_argument("command", choices=["build", "verify"], help="Build or verify the Scrivener themes.")
    parser.add_argument("--verify", action="store_true", help="Run verification after build.")
    args = parser.parse_args()

    if args.command == "build":
        outputs = build()
        for output in outputs:
            print(f"built {output.name}")
        if args.verify:
            verify()
            print("verified")
    elif args.command == "verify":
        verify()
        print("verified")


if __name__ == "__main__":
    main()
