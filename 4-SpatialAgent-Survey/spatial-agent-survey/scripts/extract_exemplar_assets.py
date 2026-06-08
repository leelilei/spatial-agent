#!/usr/bin/env python3
"""Extract figure-design reference assets from local survey exemplar PDFs."""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Iterable

try:
    import fitz
except ModuleNotFoundError as exc:  # pragma: no cover - environment check
    raise SystemExit("PyMuPDF is required. Install with: python3 -m pip install --user pymupdf") from exc

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ModuleNotFoundError as exc:  # pragma: no cover - environment check
    raise SystemExit("Pillow is required. Install with: python3 -m pip install --user pillow") from exc


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent
DEFAULT_LIBRARY_DIR = REPO_ROOT / "assets" / "survey_paper" / "pdfs" / "review_library"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "assets" / "survey_paper" / "exemplar_assets"

PRESETS = {
    "figure-redraw": ["01", "05", "07", "11", "12", "13", "14", "15"],
}

FIGURE_MAP = [
    {
        "target": "Figure 1",
        "purpose": "Corpus and evidence-role diagram",
        "references": ["13", "15"],
        "inspect": "Conceptual role separation, evidence-map framing, and scoping-review charting logic.",
    },
    {
        "target": "Figure 2",
        "purpose": "PRISMA-ScR screening and evidence-map stabilization flow",
        "references": ["11", "12", "14"],
        "inspect": "PRISMA flow hierarchy, count placement, and separation of screening from synthesis.",
    },
    {
        "target": "Figure 3",
        "purpose": "L0-L5 agent-accessible spatial representation taxonomy",
        "references": ["01", "07"],
        "inspect": "Taxonomy overview composition and cross-scale / methodology hierarchy diagrams.",
    },
    {
        "target": "Figure 4",
        "purpose": "Representation distribution by core layer",
        "references": ["13"],
        "inspect": "Distribution / bubble / conceptual-analysis plots with compact count presentation.",
    },
    {
        "target": "Figure 5",
        "purpose": "Local adjacency versus global configuration worked example",
        "references": ["01"],
        "inspect": "Spatial-scale explanatory visuals; final graph logic remains original to this survey.",
    },
    {
        "target": "Figure 6",
        "purpose": "Research agenda map",
        "references": ["05", "07"],
        "inspect": "Agenda / challenge maps and future-work organization in LLM-agent surveys.",
    },
]

CAPTION_RE = re.compile(
    r"(?is)\b(?P<kind>fig(?:ure)?\.?|table)\s*(?P<label>[0-9]+(?:\.[0-9]+)?[A-Za-z]?)\b"
)


@dataclass
class CaptionHit:
    page: int
    kind: str
    label: str
    caption: str
    bbox: list[float]


@dataclass
class EmbeddedImageHit:
    page: int
    xref: int
    width: int
    height: int
    colorspace: int
    output: str


@dataclass
class FigureAssetHit:
    page: int
    kind: str
    label: str
    caption: str
    image: str
    metadata: str
    crop_bbox: list[float]


@dataclass
class ExemplarResult:
    source_pdf: str
    output_dir: str
    extracted_at_utc: str
    page_count: int
    rendered_pages: list[int] = field(default_factory=list)
    captions: list[CaptionHit] = field(default_factory=list)
    embedded_images: list[EmbeddedImageHit] = field(default_factory=list)
    figure_assets: list[FigureAssetHit] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def compact_text(text: str, limit: int = 650) -> str:
    compact = re.sub(r"\s+", " ", normalize_text(text)).strip()
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3].rstrip() + "..."


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def output_slug(pdf_path: Path) -> str:
    return pdf_path.stem


def paper_id(pdf_path: Path) -> str:
    match = re.match(r"^([0-9]{2})_", pdf_path.name)
    return match.group(1) if match else pdf_path.stem


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_").lower()
    return slug or "item"


def filename_text_from_caption(caption: CaptionHit) -> str:
    text = re.sub(
        rf"(?is)^\s*(?:fig(?:ure)?\.?|table)\s*{re.escape(caption.label)}\s*[:.\-]?\s*",
        "",
        caption.caption,
    )
    slug = safe_slug(text)
    return slug[:150].strip("_") or f"page_{caption.page:03d}"


def figure_asset_stem(caption: CaptionHit, duplicate_index: int) -> str:
    base = f"{caption.kind}{safe_slug(caption.label)}_{filename_text_from_caption(caption)}"
    if duplicate_index > 1:
        base = f"{base}_p{caption.page:03d}_{duplicate_index}"
    return base


def rect_to_list(rect: fitz.Rect) -> list[float]:
    return [round(float(rect.x0), 2), round(float(rect.y0), 2), round(float(rect.x1), 2), round(float(rect.y1), 2)]


def resolve_pdf_paths(args: argparse.Namespace) -> list[Path]:
    library_dir = args.library_dir
    pdfs = sorted(library_dir.glob("*.pdf"))
    if args.all:
        return pdfs

    ids = list(args.ids or [])
    if args.preset:
        ids.extend(PRESETS[args.preset])
    if not ids:
        ids.extend(PRESETS["figure-redraw"])

    selected: list[Path] = []
    missing: list[str] = []
    for item in ids:
        item_path = Path(item)
        if item_path.exists() and item_path.suffix.lower() == ".pdf":
            selected.append(item_path.resolve())
            continue
        candidates = [pdf for pdf in pdfs if pdf.name.startswith(f"{item}_") or pdf.stem == item]
        if candidates:
            selected.extend(candidates)
        else:
            missing.append(item)

    if missing:
        raise SystemExit(f"No review-library PDF matched: {', '.join(missing)}")

    deduped: list[Path] = []
    seen: set[Path] = set()
    for path in selected:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        deduped.append(resolved)
    return sorted(deduped)


def extract_page_texts(doc: fitz.Document, max_pages: int | None) -> list[str]:
    page_count = len(doc) if max_pages is None else min(len(doc), max_pages)
    texts: list[str] = []
    for page_index in range(page_count):
        page = doc.load_page(page_index)
        texts.append(normalize_text(page.get_text("text") or ""))
    return texts


def find_caption_hits(doc: fitz.Document, max_pages: int | None) -> list[CaptionHit]:
    hits: list[CaptionHit] = []
    page_count = len(doc) if max_pages is None else min(len(doc), max_pages)
    for page_index in range(page_count):
        page = doc.load_page(page_index)
        blocks = page.get_text("blocks") or []
        for block in sorted(blocks, key=lambda item: (item[1], item[0])):
            x0, y0, x1, y1, text = block[:5]
            normalized = compact_text(str(text))
            if not normalized:
                continue
            match = CAPTION_RE.search(normalized)
            if not match:
                continue
            prefix = normalized[: match.start()].strip()
            # Keep caption-like blocks, not ordinary body references such as "shown in Figure 2".
            if prefix and re.search(r"[A-Za-z]", prefix):
                continue
            kind_raw = match.group("kind").lower()
            kind = "figure" if kind_raw.startswith("fig") else "table"
            hits.append(
                CaptionHit(
                    page=page_index + 1,
                    kind=kind,
                    label=match.group("label"),
                    caption=normalized,
                    bbox=[round(float(v), 2) for v in (x0, y0, x1, y1)],
                )
            )
    return hits


def select_render_pages(
    *,
    mode: str,
    page_count: int,
    captions: list[CaptionHit],
    max_rendered_pages: int,
) -> list[int]:
    if mode == "none":
        return []
    if mode == "all":
        pages = list(range(1, page_count + 1))
    else:
        pages = sorted({1, *[caption.page for caption in captions]})
        if len(pages) == 1 and not captions:
            pages = list(range(1, min(page_count, 3) + 1))
    return pages[:max_rendered_pages]


def render_pages(doc: fitz.Document, pages: Iterable[int], out_dir: Path, dpi: int, overwrite: bool) -> list[int]:
    pages_dir = out_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)
    zoom = dpi / 72.0
    matrix = fitz.Matrix(zoom, zoom)
    rendered: list[int] = []
    for page_number in pages:
        page_path = pages_dir / f"page_{page_number:03d}.png"
        if page_path.exists() and not overwrite:
            rendered.append(page_number)
            continue
        page = doc.load_page(page_number - 1)
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        pix.save(page_path)
        rendered.append(page_number)
    return rendered


def extract_embedded_images(
    doc: fitz.Document,
    out_dir: Path,
    *,
    min_width: int,
    min_height: int,
    overwrite: bool,
) -> list[EmbeddedImageHit]:
    images_dir = out_dir / "images"
    images_dir.mkdir(parents=True, exist_ok=True)
    hits: list[EmbeddedImageHit] = []
    seen_xrefs: set[int] = set()
    for page_index in range(len(doc)):
        page = doc.load_page(page_index)
        for image_index, image_info in enumerate(page.get_images(full=True), start=1):
            xref = int(image_info[0])
            if xref in seen_xrefs:
                continue
            seen_xrefs.add(xref)
            try:
                extracted = doc.extract_image(xref)
            except Exception:
                continue
            width = int(extracted.get("width", 0))
            height = int(extracted.get("height", 0))
            if width < min_width or height < min_height:
                continue
            ext = str(extracted.get("ext") or "png").lower()
            image_path = images_dir / f"image_p{page_index + 1:03d}_{image_index:02d}_xref{xref}.{ext}"
            if overwrite or not image_path.exists():
                image_path.write_bytes(extracted["image"])
            hits.append(
                EmbeddedImageHit(
                    page=page_index + 1,
                    xref=xref,
                    width=width,
                    height=height,
                    colorspace=int(extracted.get("colorspace", 0)),
                    output=str(image_path.relative_to(out_dir)),
                )
            )
    return hits


def page_graphic_rects(page: fitz.Page) -> list[fitz.Rect]:
    rects: list[fitz.Rect] = []
    seen: set[tuple[float, float, float, float]] = set()
    for image_info in page.get_images(full=True):
        xref = int(image_info[0])
        try:
            image_rects = page.get_image_rects(xref)
        except Exception:
            image_rects = []
        for rect in image_rects:
            key = tuple(round(float(v), 2) for v in (rect.x0, rect.y0, rect.x1, rect.y1))
            if key in seen:
                continue
            seen.add(key)
            rects.append(fitz.Rect(rect))
    try:
        drawings = page.get_drawings()
    except Exception:
        drawings = []
    for drawing in drawings:
        rect = drawing.get("rect")
        if rect is None:
            continue
        rect = fitz.Rect(rect)
        if rect.is_empty or rect.width < 8 or rect.height < 8:
            continue
        key = tuple(round(float(v), 2) for v in (rect.x0, rect.y0, rect.x1, rect.y1))
        if key in seen:
            continue
        seen.add(key)
        rects.append(rect)
    return rects


def page_text_rects(page: fitz.Page, caption: CaptionHit) -> list[fitz.Rect]:
    caption_rect = fitz.Rect(caption.bbox)
    rects: list[fitz.Rect] = []
    for block in page.get_text("blocks") or []:
        x0, y0, x1, y1, text = block[:5]
        text = compact_text(str(text), limit=160)
        if not text:
            continue
        rect = fitz.Rect(float(x0), float(y0), float(x1), float(y1))
        if rect.intersects(caption_rect):
            continue
        rects.append(rect)
    return rects


def union_rect(rects: Iterable[fitz.Rect]) -> fitz.Rect | None:
    iterator = iter(rects)
    try:
        combined = fitz.Rect(next(iterator))
    except StopIteration:
        return None
    for rect in iterator:
        combined |= rect
    return combined


def expanded_rect(rect: fitz.Rect, margin: float, page_rect: fitz.Rect) -> fitz.Rect:
    expanded = fitz.Rect(rect.x0 - margin, rect.y0 - margin, rect.x1 + margin, rect.y1 + margin)
    return expanded & page_rect


def horizontally_related(a: fitz.Rect, b: fitz.Rect, margin: float = 36) -> bool:
    expanded = fitz.Rect(b.x0 - margin, b.y0, b.x1 + margin, b.y1)
    return a.x0 <= expanded.x1 and a.x1 >= expanded.x0


def infer_caption_crop(
    page: fitz.Page,
    caption: CaptionHit,
    *,
    search_window: float,
    margin: float,
) -> tuple[fitz.Rect, fitz.Rect]:
    page_rect = page.rect
    caption_rect = fitz.Rect(caption.bbox)
    graphics = page_graphic_rects(page)
    texts = page_text_rects(page, caption)

    if caption.kind == "table":
        primary = [
            rect
            for rect in [*graphics, *texts]
            if rect.y0 >= caption_rect.y1 - 4
            and rect.y0 <= caption_rect.y1 + search_window
            and horizontally_related(rect, caption_rect, margin=72)
        ]
        content = union_rect(primary)
        if content is None:
            content = fitz.Rect(54, caption_rect.y1 + 6, page_rect.width - 54, min(page_rect.height - 54, caption_rect.y1 + search_window))
        with_caption = content | caption_rect
        return expanded_rect(content, margin, page_rect), expanded_rect(with_caption, margin, page_rect)

    above_graphics = [
        rect
        for rect in graphics
        if rect.y1 <= caption_rect.y0 + 6
        and rect.y1 >= caption_rect.y0 - search_window
        and horizontally_related(rect, caption_rect, margin=96)
    ]
    below_graphics = [
        rect
        for rect in graphics
        if rect.y0 >= caption_rect.y1 - 6
        and rect.y0 <= caption_rect.y1 + search_window
        and horizontally_related(rect, caption_rect, margin=96)
    ]

    above_content = union_rect(above_graphics)
    below_content = union_rect(below_graphics)

    def area(rect: fitz.Rect | None) -> float:
        return 0.0 if rect is None else max(0.0, rect.width) * max(0.0, rect.height)

    use_below = below_content is not None and area(below_content) > max(800.0, area(above_content) * 1.15)
    content = below_content if use_below else above_content

    if content is not None:
        # Add labels or legends that are text objects but visually belong to the figure.
        if use_below:
            related_texts = [
                rect
                for rect in texts
                if rect.y0 >= caption_rect.y1 - 6
                and rect.y1 <= content.y1 + 12
                and horizontally_related(rect, content, margin=48)
            ]
        else:
            related_texts = [
                rect
                for rect in texts
                if rect.y1 <= caption_rect.y0 + 6
                and rect.y0 >= content.y0 - 12
                and horizontally_related(rect, content, margin=48)
            ]
        content = union_rect([content, *related_texts]) or content
    else:
        nearby_texts = [
            rect
            for rect in texts
            if (
                rect.y1 <= caption_rect.y0 + 6
                and rect.y1 >= caption_rect.y0 - search_window
                or rect.y0 >= caption_rect.y1 - 6
                and rect.y0 <= caption_rect.y1 + search_window
            )
            and horizontally_related(rect, caption_rect, margin=96)
        ]
        content = union_rect(nearby_texts)

    if content is None:
        content = fitz.Rect(54, max(36, caption_rect.y0 - min(search_window, 300)), page_rect.width - 54, caption_rect.y0 - 4)

    if use_below:
        content = fitz.Rect(content.x0, max(content.y0, caption_rect.y1 + 4), content.x1, content.y1)
        if content.height < 24:
            content = fitz.Rect(54, caption_rect.y1 + 4, page_rect.width - 54, min(page_rect.height - 36, caption_rect.y1 + min(search_window, 300)))
    else:
        # Caption-below figures should not include the caption in the clean figure crop.
        content = fitz.Rect(content.x0, content.y0, content.x1, min(content.y1, caption_rect.y0 - 4))
        if content.height < 24:
            content = fitz.Rect(54, max(36, caption_rect.y0 - min(search_window, 240)), page_rect.width - 54, caption_rect.y0 - 4)

    with_caption = content | caption_rect
    return expanded_rect(content, margin, page_rect), expanded_rect(with_caption, margin, page_rect)


def render_clip(page: fitz.Page, rect: fitz.Rect, output_path: Path, *, dpi: int, overwrite: bool) -> None:
    if output_path.exists() and not overwrite:
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    zoom = dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=rect, alpha=False)
    pix.save(output_path)


def write_caption_markdown(pdf_path: Path, out_dir: Path, asset: FigureAssetHit, caption: CaptionHit) -> Path:
    path = out_dir / asset.metadata
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {asset.kind.title()} {asset.label}",
        "",
        f"Source PDF: `{pdf_path}`",
        f"Page: `{caption.page}`",
        "",
        "Caption:",
        "",
        asset.caption,
        "",
        "Assets:",
        "",
        f"- Image: `{asset.image}`",
        f"- Crop bbox: `{asset.crop_bbox}`",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def extract_caption_assets(
    doc: fitz.Document,
    pdf_path: Path,
    out_dir: Path,
    captions: list[CaptionHit],
    *,
    dpi: int,
    search_window: float,
    margin: float,
    overwrite: bool,
) -> list[FigureAssetHit]:
    assets: list[FigureAssetHit] = []
    counters: dict[tuple[str, str], int] = {}
    for caption in captions:
        page = doc.load_page(caption.page - 1)
        crop_rect, _with_caption_rect = infer_caption_crop(
            page,
            caption,
            search_window=search_window,
            margin=margin,
        )
        key = (caption.kind, caption.label)
        counters[key] = counters.get(key, 0) + 1
        stem = figure_asset_stem(caption, counters[key])
        image = Path("figures") / f"{stem}.png"
        metadata = Path("figures") / f"{stem}.md"

        render_clip(page, crop_rect, out_dir / image, dpi=dpi, overwrite=overwrite)

        asset = FigureAssetHit(
            page=caption.page,
            kind=caption.kind,
            label=caption.label,
            caption=caption.caption,
            image=str(image),
            metadata=str(metadata),
            crop_bbox=rect_to_list(crop_rect),
        )
        write_caption_markdown(pdf_path, out_dir, asset, caption)
        assets.append(asset)
    return assets


def write_text_markdown(pdf_path: Path, out_dir: Path, page_texts: list[str]) -> Path:
    lines = [
        f"# {pdf_path.stem}",
        "",
        f"Source PDF: `{pdf_path}`",
        "",
        "Extraction backend: `PyMuPDF`",
        "",
    ]
    for index, text in enumerate(page_texts, start=1):
        lines.extend([f"## Page {index}", "", text or "[no extractable text]", ""])
    text_path = out_dir / "text.md"
    text_path.write_text("\n".join(lines), encoding="utf-8")
    return text_path


def write_figure_index(pdf_path: Path, out_dir: Path, result: ExemplarResult) -> Path:
    asset_by_key: dict[tuple[int, str, str, str], FigureAssetHit] = {}
    for asset in result.figure_assets:
        asset_by_key[(asset.page, asset.kind, asset.label, asset.caption)] = asset

    lines = [
        f"# Figure/Table Index: {pdf_path.stem}",
        "",
        f"Source PDF: `{pdf_path}`",
        "",
        "## Caption Hits",
        "",
        "| page | kind | label | caption | image | metadata | rendered page |",
        "|---:|---|---|---|---|---|---|",
    ]
    if result.captions:
        rendered_set = set(result.rendered_pages)
        for hit in result.captions:
            rendered = f"pages/page_{hit.page:03d}.png" if hit.page in rendered_set else ""
            asset = asset_by_key.get((hit.page, hit.kind, hit.label, hit.caption))
            image = f"`{asset.image}`" if asset else ""
            metadata = f"`{asset.metadata}`" if asset else ""
            lines.append(
                "| "
                + " | ".join(
                    [
                        str(hit.page),
                        hit.kind,
                        hit.label,
                        markdown_escape(hit.caption),
                        image,
                        metadata,
                        rendered,
                    ]
                )
                + " |"
            )
    else:
        lines.append("|  |  |  | no figure/table caption hits found |  |  |  |")

    lines.extend(
        [
            "",
            "## Embedded Images",
            "",
            "| page | size | output |",
            "|---:|---:|---|",
        ]
    )
    if result.embedded_images:
        for image in result.embedded_images:
            lines.append(f"| {image.page} | {image.width}x{image.height} | `{image.output}` |")
    else:
        lines.append("|  |  | no embedded images above threshold |")

    index_path = out_dir / "figure_index.md"
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return index_path


def write_contact_sheet(out_dir: Path, rendered_pages: list[int], *, max_items: int) -> Path | None:
    page_paths = [out_dir / "pages" / f"page_{page:03d}.png" for page in rendered_pages]
    page_paths = [path for path in page_paths if path.exists()][:max_items]
    if not page_paths:
        return None

    thumb_size = (320, 420)
    label_height = 34
    columns = 4
    rows = (len(page_paths) + columns - 1) // columns
    margin = 24
    gap = 18
    width = margin * 2 + columns * thumb_size[0] + (columns - 1) * gap
    height = margin * 2 + rows * (thumb_size[1] + label_height) + (rows - 1) * gap
    sheet = Image.new("RGB", (width, height), "#f8f8f5")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for idx, path in enumerate(page_paths):
        row, col = divmod(idx, columns)
        x = margin + col * (thumb_size[0] + gap)
        y = margin + row * (thumb_size[1] + label_height + gap)
        with Image.open(path) as img:
            img = ImageOps.contain(img.convert("RGB"), thumb_size, method=Image.Resampling.LANCZOS)
            canvas = Image.new("RGB", thumb_size, "white")
            paste_x = (thumb_size[0] - img.width) // 2
            paste_y = (thumb_size[1] - img.height) // 2
            canvas.paste(img, (paste_x, paste_y))
            sheet.paste(canvas, (x, y))
        draw.rectangle([x, y, x + thumb_size[0], y + thumb_size[1]], outline="#333333", width=1)
        draw.text((x, y + thumb_size[1] + 8), path.stem, fill="#222222", font=font)

    sheet_path = out_dir / "contact_sheet.png"
    sheet.save(sheet_path)
    return sheet_path


def write_meta(out_dir: Path, result: ExemplarResult) -> Path:
    meta_path = out_dir / "meta.json"
    meta_path.write_text(json.dumps(asdict(result), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return meta_path


def clean_flat_figure_dir(out_dir: Path, overwrite: bool) -> None:
    figures_dir = out_dir / "figures"
    if overwrite and figures_dir.exists():
        shutil.rmtree(figures_dir)
    figures_dir.mkdir(parents=True, exist_ok=True)


def extract_one(pdf_path: Path, args: argparse.Namespace) -> ExemplarResult:
    out_dir = args.output_dir / output_slug(pdf_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    clean_flat_figure_dir(out_dir, args.overwrite)

    doc = fitz.open(pdf_path)
    try:
        page_texts = extract_page_texts(doc, args.max_text_pages)
        captions = find_caption_hits(doc, args.max_text_pages)
        render_page_numbers = select_render_pages(
            mode=args.render_pages,
            page_count=len(doc),
            captions=captions,
            max_rendered_pages=args.max_rendered_pages,
        )
        rendered_pages = render_pages(
            doc,
            render_page_numbers,
            out_dir,
            dpi=args.page_dpi,
            overwrite=args.overwrite,
        )
        embedded_images = extract_embedded_images(
            doc,
            out_dir,
            min_width=args.min_image_width,
            min_height=args.min_image_height,
            overwrite=args.overwrite,
        )
        figure_assets = extract_caption_assets(
            doc,
            pdf_path,
            out_dir,
            captions,
            dpi=args.figure_dpi,
            search_window=args.figure_search_window,
            margin=args.figure_crop_margin,
            overwrite=args.overwrite,
        )
        result = ExemplarResult(
            source_pdf=str(pdf_path),
            output_dir=str(out_dir),
            extracted_at_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
            page_count=len(doc),
            rendered_pages=rendered_pages,
            captions=captions,
            embedded_images=embedded_images,
            figure_assets=figure_assets,
        )
        if args.render_pages != "all" and len(rendered_pages) < len(doc):
            result.warnings.append(
                f"render_pages={args.render_pages}; rendered {len(rendered_pages)} of {len(doc)} pages"
            )
        write_text_markdown(pdf_path, out_dir, page_texts)
        write_meta(out_dir, result)
        write_figure_index(pdf_path, out_dir, result)
        write_contact_sheet(out_dir, rendered_pages, max_items=args.contact_sheet_max)
        return result
    finally:
        doc.close()


def write_root_readme(output_dir: Path, results: list[ExemplarResult], command: str) -> None:
    lines = [
        "# Exemplar Assets",
        "",
        "Generated reference package for figure redesign prompts.",
        "",
        f"Generated at UTC: `{datetime.now(timezone.utc).replace(microsecond=0).isoformat()}`",
        "",
        "Command:",
        "",
        f"```bash\n{command}\n```",
        "",
        "## Processed Papers",
        "",
        "| id | paper | pages | rendered pages | captions | figure assets | embedded images | folder |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for result in results:
        pdf_path = Path(result.source_pdf)
        folder = Path(result.output_dir).name
        lines.append(
            f"| {paper_id(pdf_path)} | `{pdf_path.name}` | {result.page_count} | "
            f"{len(result.rendered_pages)} | {len(result.captions)} | {len(result.figure_assets)} | "
            f"{len(result.embedded_images)} | "
            f"`{folder}/` |"
        )
    lines.extend(
        [
            "",
            "Each folder contains:",
            "",
            "- `text.md`: page-level extracted text.",
            "- `meta.json`: extraction metadata and counts.",
            "- `figure_index.md`: figure/table caption hits and embedded image inventory.",
            "- `figures/`: flat caption-level crops and same-name Markdown metadata, for example `figure1_multiple_scale_spatial_intelligence_in_real_world.png`.",
            "- `pages/`: rendered reference pages selected by the extraction mode.",
            "- `images/`: embedded raster images above the size threshold.",
            "- `contact_sheet.png`: quick visual overview of rendered pages.",
            "",
        ]
    )
    (output_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def write_target_figure_reference_map(output_dir: Path, results: list[ExemplarResult]) -> None:
    id_to_folder = {paper_id(Path(result.source_pdf)): Path(result.output_dir).name for result in results}
    lines = [
        "# Target Figure Reference Map",
        "",
        "Use this map before writing GPT-Image prompts. It links each target survey figure to local exemplar assets.",
        "",
        "| target | purpose | reference assets | what to inspect |",
        "|---|---|---|---|",
    ]
    for row in FIGURE_MAP:
        refs = []
        for ref_id in row["references"]:
            folder = id_to_folder.get(ref_id)
            if folder:
                refs.append(f"`{folder}/figure_index.md`; `{folder}/figures/`; `{folder}/contact_sheet.png`")
            else:
                refs.append(f"`{ref_id}` not extracted")
        lines.append(
            "| "
            + " | ".join(
                [
                    row["target"],
                    markdown_escape(row["purpose"]),
                    "<br>".join(refs),
                    markdown_escape(row["inspect"]),
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "Prompt rule: describe the target figure's purpose, reader takeaway, mandatory data, and claim boundaries first. Let the image model choose composition using the exemplar assets as visual references.",
            "",
        ]
    )
    (output_dir / "target_figure_reference_map.md").write_text("\n".join(lines), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ids", nargs="*", help="Review-library numeric IDs or explicit PDF paths.")
    parser.add_argument("--preset", choices=sorted(PRESETS), default=None)
    parser.add_argument("--all", action="store_true", help="Process all review-library PDFs.")
    parser.add_argument("--library-dir", type=Path, default=DEFAULT_LIBRARY_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--render-pages", choices=["figure", "all", "none"], default="figure")
    parser.add_argument("--max-rendered-pages", type=int, default=40)
    parser.add_argument("--max-text-pages", type=int, default=None)
    parser.add_argument("--page-dpi", type=int, default=160)
    parser.add_argument("--figure-dpi", type=int, default=220)
    parser.add_argument("--figure-search-window", type=float, default=420)
    parser.add_argument("--figure-crop-margin", type=float, default=8)
    parser.add_argument("--min-image-width", type=int, default=240)
    parser.add_argument("--min-image-height", type=int, default=160)
    parser.add_argument("--contact-sheet-max", type=int, default=32)
    parser.add_argument("--overwrite", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    pdf_paths = resolve_pdf_paths(args)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    results: list[ExemplarResult] = []
    for pdf_path in pdf_paths:
        result = extract_one(pdf_path, args)
        results.append(result)
        print(
            f"[ok] {pdf_path.name}: pages={result.page_count}, "
            f"rendered={len(result.rendered_pages)}, captions={len(result.captions)}, "
            f"figure_assets={len(result.figure_assets)}, images={len(result.embedded_images)}"
        )

    write_root_readme(args.output_dir, results, " ".join([Path(sys.argv[0]).name, *sys.argv[1:]]))
    write_target_figure_reference_map(args.output_dir, results)
    print(f"[done] wrote exemplar assets to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
