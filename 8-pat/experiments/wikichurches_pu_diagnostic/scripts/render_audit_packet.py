#!/usr/bin/env python3
"""Render blinded HTML index and sealed official-box overlays."""

from __future__ import annotations

import argparse
import csv
import html
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--parts", type=Path, required=True)
    parser.add_argument("--image-dir", type=Path, required=True)
    parser.add_argument("--blinded-html", type=Path, required=True)
    parser.add_argument("--overlay-dir", type=Path, required=True)
    args = parser.parse_args()

    rows = list(csv.DictReader(args.manifest.open()))
    payload = json.loads(args.parts.read_text())
    meta = payload["meta"]
    official = payload["annotations"]
    args.overlay_dir.mkdir(parents=True, exist_ok=True)
    args.blinded_html.parent.mkdir(parents=True, exist_ok=True)
    font = ImageFont.load_default(size=18)

    cards: list[str] = []
    for row in rows:
        audit_id = row["audit_id"]
        filename = row["image_filename"]
        image_path = args.image_dir / f"{audit_id}.jpg"
        if not image_path.exists():
            raise FileNotFoundError(image_path)

        cards.append(
            (
                '<article class="card">'
                f"<h2>{html.escape(audit_id)}</h2>"
                f"<p>{html.escape(row['assigned_style'])} · "
                f"{html.escape(row['sample_type'])}</p>"
                f'<a href="images/{html.escape(image_path.name)}" target="_blank">'
                f'<img src="images/{html.escape(image_path.name)}" '
                f'alt="{html.escape(audit_id)}"></a>'
                "</article>"
            )
        )

        with Image.open(image_path) as source:
            image = source.convert("RGB")
        draw = ImageDraw.Draw(image)
        width, height = image.size
        for group in official[filename]["bbox_groups"]:
            for element in group["elements"]:
                x1 = max(0, min(width - 1, round(element["left"] * width)))
                y1 = max(0, min(height - 1, round(element["top"] * height)))
                x2 = max(
                    x1 + 1,
                    min(
                        width,
                        round((element["left"] + element["width"]) * width),
                    ),
                )
                y2 = max(
                    y1 + 1,
                    min(
                        height,
                        round((element["top"] + element["height"]) * height),
                    ),
                )
                label = meta[element["label"]]["name"]
                draw.rectangle((x1, y1, x2, y2), outline=(255, 48, 48), width=4)
                text_box = draw.textbbox((x1, y1), label, font=font)
                label_width = text_box[2] - text_box[0] + 8
                label_height = text_box[3] - text_box[1] + 6
                label_top = y1
                label_bottom = min(height, label_top + label_height)
                draw.rectangle(
                    (
                        x1,
                        label_top,
                        min(width, x1 + label_width),
                        label_bottom,
                    ),
                    fill=(255, 48, 48),
                )
                draw.text(
                    (x1 + 4, label_top + 2),
                    label,
                    fill=(255, 255, 255),
                    font=font,
                )
        image.save(args.overlay_dir / f"{audit_id}_official.jpg", quality=94)

    document = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>WikiChurches 50-image blind audit</title>
<style>
body {{ margin: 0; font-family: -apple-system, BlinkMacSystemFont, sans-serif;
       background: #f5f3ee; color: #171717; }}
header {{ position: sticky; top: 0; z-index: 2; padding: 18px 28px;
          background: rgba(245,243,238,.94); border-bottom: 1px solid #d7d1c5; }}
h1 {{ margin: 0 0 6px; font-size: 24px; }}
header p, .card p {{ margin: 0; color: #655f56; }}
main {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(340px,1fr));
        gap: 18px; padding: 22px; }}
.card {{ background: white; border: 1px solid #ddd7cd; border-radius: 12px;
         padding: 14px; box-shadow: 0 2px 8px rgba(30,20,10,.05); }}
.card h2 {{ display: inline; margin: 0 10px 8px 0; font-size: 18px; }}
.card p {{ display: inline; font-size: 14px; }}
.card img {{ display: block; margin-top: 12px; width: 100%; height: 340px;
             object-fit: contain; background: #111; border-radius: 7px; }}
</style>
</head>
<body>
<header>
<h1>WikiChurches 局部构件盲审</h1>
<p>50 张；点击图片打开 1920 px 审计版本。禁止查看 sealed 目录。</p>
</header>
<main>{''.join(cards)}</main>
</body>
</html>
"""
    args.blinded_html.write_text(document)


if __name__ == "__main__":
    main()
