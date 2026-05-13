from __future__ import annotations

import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from scrivener_theme_compiler import derive_palette, load_seeds  # noqa: E402


OUTPUT_DIR = ROOT / "assets" / "readme-previews"
WIDTH = 1440
HEIGHT = 900


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        (r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf"),
        (r"C:\Windows\Fonts\seguisb.ttf" if bold else r"C:\Windows\Fonts\seguisym.ttf"),
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def hex_rgba(hex_color: str, alpha: int = 255) -> tuple[int, int, int, int]:
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4)) + (alpha,)


def is_dark(hex_color: str) -> bool:
    value = hex_color.lstrip("#")
    r, g, b = (int(value[i : i + 2], 16) for i in (0, 2, 4))
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) < 140


def measure(draw: ImageDraw.ImageDraw, font, text: str) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def rounded_panel(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int] | None = None,
    radius: int = 18,
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=2 if outline else 0)


def shadow_panel(
    base: Image.Image,
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    fill: tuple[int, int, int, int],
    shadow: tuple[int, int, int, int],
    radius: int = 18,
) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle((x0 + 8, y0 + 10, x1 + 8, y1 + 10), radius=radius, fill=shadow)
    rounded_panel(draw, box, fill, outline=None, radius=radius)


def draw_wrapped_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font,
    fill: tuple[int, int, int, int],
    max_width: int,
    line_spacing: int = 9,
) -> int:
    x, y = xy
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split()
        current = ""
        for word in words:
            test = word if not current else f"{current} {word}"
            width, _ = measure(draw, font, test)
            if width <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)

    line_height = measure(draw, font, "Ag")[1]
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += line_height + line_spacing
    return y


def render_preview(seed, output_path: Path) -> None:
    palette = derive_palette(seed)
    image = Image.new("RGBA", (WIDTH, HEIGHT), hex_rgba(palette.window_bg))
    draw = ImageDraw.Draw(image)

    title_font = load_font(34, bold=True)
    section_font = load_font(18, bold=True)
    body_font = load_font(20)
    small_font = load_font(16)
    mono_font = load_font(15)

    top_fill = hex_rgba(palette.panel_bg_strong, 245)
    panel_fill = hex_rgba(palette.panel_bg, 242)
    editor_fill = hex_rgba(palette.editor_bg, 242)
    shadow = hex_rgba(palette.dark, 90)

    # Top chrome
    rounded_panel(draw, (24, 20, WIDTH - 24, 96), top_fill, outline=hex_rgba(palette.divider, 160), radius=22)
    draw.text((52, 39), seed.display_name, font=title_font, fill=hex_rgba(palette.title_text))
    draw.text((680, 40), "Scrivener 3.x preview", font=small_font, fill=hex_rgba(palette.text_muted))

    for i, label in enumerate(["Binder", "Editor", "Inspector"]):
        x = 980 + (i * 126)
        rounded_panel(
            draw,
            (x, 34, x + 110, 72),
            hex_rgba(palette.accent_soft, 185 if i == 1 else 120),
            outline=hex_rgba(palette.divider, 120),
            radius=16,
        )
        tw, th = measure(draw, small_font, label)
        draw.text((x + (110 - tw) // 2, 44), label, font=small_font, fill=hex_rgba(palette.text_primary))

    # Side panels
    shadow_panel(image, draw, (24, 122, 274, 808), panel_fill, shadow, radius=22)
    shadow_panel(image, draw, (282, 122, 1118, 808), editor_fill, shadow, radius=22)
    shadow_panel(image, draw, (1126, 122, 1416, 808), panel_fill, shadow, radius=22)

    # Binder list
    draw.text((48, 148), "Binder", font=section_font, fill=hex_rgba(seed.header_footer_color))
    binder_items = [
        ("Overview", False),
        ("Chapter I", True),
        ("Scene 1", False),
        ("Scene 2", False),
        ("Scene 3", False),
        ("Notes", False),
    ]
    y = 190
    for label, selected in binder_items:
        if selected:
            rounded_panel(draw, (40, y - 8, 258, y + 32), hex_rgba(palette.selection_bg, 220), outline=None, radius=12)
            fill = hex_rgba(palette.selection_text)
        else:
            fill = hex_rgba(palette.text_primary)
        draw.text((54, y), label, font=body_font, fill=fill)
        y += 48

    draw.text((48, 486), "Project notes", font=section_font, fill=hex_rgba(seed.header_footer_color))
    draw_wrapped_text(
        draw,
        (48, 522),
        "Compact, quiet, and readable. The UI keeps the writing surface calm while accents stay visible.",
        small_font,
        hex_rgba(palette.text_muted),
        198,
        line_spacing=6,
    )

    # Editor
    draw.text((314, 148), "Scene 1: The corridor with the green lamp", font=section_font, fill=hex_rgba(palette.title_text))
    draw.text((314, 182), "Draft text with selections, links, and title treatment visible in the theme.", font=small_font, fill=hex_rgba(palette.text_muted))
    draw.line((314, 216, 1088, 216), fill=hex_rgba(palette.divider), width=2)

    body = (
        "The first line is the opening beat. "
        "A selected phrase shows the accent clearly, while body text remains calm and readable. "
        "A link is visible without becoming neon. "
        "The whole point is a writing surface that does not fight the page."
    )
    draw_wrapped_text(
        draw,
        (314, 246),
        body,
        body_font,
        hex_rgba(palette.text_primary),
        730,
        line_spacing=12,
    )

    select_box = (520, 338, 1012, 378)
    rounded_panel(draw, select_box, hex_rgba(palette.selection_bg, 224), outline=None, radius=12)
    draw.text((536, 344), "Selected sentence: current thought stands out cleanly.", font=body_font, fill=hex_rgba(palette.selection_text))

    editor_followup = (
        "Muted metadata stays present but quiet. "
        "Section headers, separators, and footnotes all keep enough contrast to be useful."
    )
    draw_wrapped_text(
        draw,
        (314, 410),
        editor_followup,
        body_font,
        hex_rgba(palette.text_primary),
        730,
        line_spacing=12,
    )

    draw.text((314, 572), "Link example", font=section_font, fill=hex_rgba(palette.accent_primary))
    draw.text((446, 572), "chapter_ref", font=section_font, fill=hex_rgba(palette.accent_soft))
    draw.line((314, 602, 1040, 602), fill=hex_rgba(palette.divider, 200), width=1)

    # Inspector
    draw.text((1150, 148), "Inspector", font=section_font, fill=hex_rgba(seed.header_footer_color))
    inspector_blocks = [
        ("Synopsis", "A short summary stays visible without taking over the page."),
        ("Notes", "Muted text, clean spacing, and a stable hierarchy."),
        ("Snapshots", "Revision accents remain distinct and restrained."),
    ]
    iy = 190
    for header, text in inspector_blocks:
        rounded_panel(draw, (1144, iy, 1398, iy + 120), hex_rgba(palette.panel_bg_strong, 220), outline=hex_rgba(palette.divider, 110), radius=16)
        draw.text((1162, iy + 16), header, font=section_font, fill=hex_rgba(palette.title_text))
        draw_wrapped_text(draw, (1162, iy + 48), text, small_font, hex_rgba(palette.text_muted), 214, line_spacing=5)
        iy += 138

    # Palette strip
    strip_y = 660
    draw.text((314, strip_y), "Core roles", font=section_font, fill=hex_rgba(seed.header_footer_color))
    roles = [
        ("bg", palette.window_bg),
        ("text", palette.text_primary),
        ("accent", palette.accent_primary),
        ("divider", palette.divider),
        ("select", palette.selection_bg),
        ("muted", palette.text_muted),
    ]
    rx = 406
    for label, color in roles:
        rounded_panel(draw, (rx, strip_y - 2, rx + 108, strip_y + 58), hex_rgba(color), outline=hex_rgba(palette.divider, 130), radius=12)
        tw, _ = measure(draw, mono_font, label)
        draw.text((rx + (108 - tw) // 2, strip_y + 66), label, font=mono_font, fill=hex_rgba(palette.text_muted))
        rx += 124

    # Footer
    rounded_panel(draw, (24, 834, WIDTH - 24, 876), hex_rgba(palette.panel_bg_strong, 245), outline=hex_rgba(palette.divider, 150), radius=16)
    draw.text((50, 845), f"Generated from Nosafune seed palette: {seed.output_suffix}", font=small_font, fill=hex_rgba(palette.text_muted))
    draw.text(
        (WIDTH - 250, 845),
        f"{'Dark' if is_dark(seed.page_background) else 'Light'} family",
        font=small_font,
        fill=hex_rgba(palette.text_muted),
    )

    image.save(output_path)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    seeds = {seed.output_suffix: seed for seed in load_seeds()}
    for output_suffix in ["mani_katti", "salva_la_reina", "majima"]:
        render_preview(seeds[output_suffix], OUTPUT_DIR / f"{output_suffix}.png")
        print(f"rendered {output_suffix}.png")


if __name__ == "__main__":
    main()
