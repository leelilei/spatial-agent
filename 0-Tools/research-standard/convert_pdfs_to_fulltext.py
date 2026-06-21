#!/usr/bin/env python3
"""Convert research-project PDFs into Markdown fulltext artifacts.

Standard project layout:

    assets/papers/pdf/**/*.pdf      -> source PDFs
    assets/papers/fulltext/**/*.md  -> extracted Markdown
    assets/papers/metadata/         -> manifest and summary

The tool also accepts a legacy `assets/papers/pdfs` source directory for projects
that were created before the standard settled on `pdf`.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import pdfplumber
except ModuleNotFoundError:  # pragma: no cover - dependency check path
    pdfplumber = None

try:
    from pypdf import PdfReader
except ModuleNotFoundError:  # pragma: no cover - dependency check path
    try:
        from PyPDF2 import PdfReader  # type: ignore[assignment]
    except ModuleNotFoundError:  # pragma: no cover - dependency check path
        PdfReader = None  # type: ignore[assignment]


PDFPLUMBER_TEXT_KWARGS = {"x_tolerance": 1, "y_tolerance": 3}
MARKDOWN_SUFFIX = ".fulltext.md"
META_SUFFIX = ".meta.json"


@dataclass
class PdfOutlineItem:
    title: str
    level: int
    page_number: int | None = None


@dataclass
class PdfExtractionResult:
    source_pdf: Path
    extractor_backend: str
    extract_time: str
    title: str = ""
    author: str = ""
    doi: str = ""
    keywords: list[str] = field(default_factory=list)
    subject: str = ""
    page_count: int = 0
    outline: list[PdfOutlineItem] = field(default_factory=list)
    text: str = ""
    text_char_count: int = 0
    status: str = "ok"
    warnings: list[str] = field(default_factory=list)

    def to_meta_dict(self) -> dict[str, Any]:
        return {
            "source_pdf": str(self.source_pdf),
            "extractor_backend": self.extractor_backend,
            "extract_time": self.extract_time,
            "title": self.title,
            "author": self.author,
            "doi": self.doi,
            "keywords": self.keywords,
            "subject": self.subject,
            "page_count": self.page_count,
            "outline": [asdict(item) for item in self.outline],
            "text_char_count": self.text_char_count,
            "status": self.status,
            "warnings": self.warnings,
        }


def normalize_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = strip_pdf_boilerplate(normalized)
    normalized = re.sub(r"(?<=\w)-\n(?=\w)", "", normalized)
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def strip_pdf_boilerplate(text: str) -> str:
    """Remove common publisher footers that pollute extracted text."""

    cleaned_lines: list[str] = []
    skipping_permission_block = False
    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()
        starts_permission_block = lower.startswith("permission to make digital")
        standalone_boilerplate = (
            lower.startswith("for all other uses")
            or lower.startswith("acm isbn")
            or lower.startswith("https://doi.org/")
            or lower.startswith("http://dx.doi.org/")
            or "copyright held by" in lower
        )

        if starts_permission_block:
            skipping_permission_block = True
            continue
        if skipping_permission_block:
            if not stripped:
                skipping_permission_block = False
            continue
        if standalone_boilerplate:
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def flatten_text(text: str) -> str:
    return re.sub(r"\s+", " ", normalize_text(text)).strip()


def first_non_empty(*values: str | None) -> str:
    for value in values:
        if value and str(value).strip():
            return str(value).strip()
    return ""


def metadata_field(metadata: Any, key: str) -> str:
    if not metadata:
        return ""
    try:
        value = metadata.get(key)
    except AttributeError:
        value = None
    return str(value).strip() if value else ""


def split_keywords(raw_keywords: str) -> list[str]:
    if not raw_keywords:
        return []
    return [part.strip() for part in raw_keywords.split(",") if part.strip()]


def extract_outline(reader: Any) -> list[PdfOutlineItem]:
    raw_outline = getattr(reader, "outline", []) or []
    outline: list[PdfOutlineItem] = []

    def walk(items: list[Any], level: int) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item, level + 1)
                continue
            title = getattr(item, "title", None) or str(item)
            title = title.strip()
            if not title:
                continue
            page_number = None
            try:
                page_number = reader.get_destination_page_number(item) + 1
            except Exception:
                page_number = None
            outline.append(PdfOutlineItem(title=title, level=level, page_number=page_number))

    walk(raw_outline, 0)
    return outline


def looks_like_two_column_page(page: Any) -> bool:
    try:
        words = page.extract_words(**PDFPLUMBER_TEXT_KWARGS) or []
    except Exception:
        return False
    if len(words) < 120:
        return False

    width = float(page.width)
    height = float(page.height)
    mid_x = width / 2
    gutter_width = max(36.0, width * 0.06)
    top_cutoff = height * 0.12
    bottom_cutoff = height * 0.92
    left_words = right_words = gutter_words = 0

    for word in words:
        top = float(word["top"])
        if top < top_cutoff or top > bottom_cutoff:
            continue
        center_x = (float(word["x0"]) + float(word["x1"])) / 2
        if center_x < mid_x - gutter_width / 2:
            left_words += 1
        elif center_x > mid_x + gutter_width / 2:
            right_words += 1
        else:
            gutter_words += 1

    body_words = left_words + right_words + gutter_words
    if body_words < 100:
        return False
    if min(left_words, right_words) < body_words * 0.25:
        return False
    return gutter_words / body_words < 0.08


def first_page_column_start_y(page: Any) -> float:
    if getattr(page, "page_number", None) != 1:
        return 0.0
    try:
        words = page.extract_words(**PDFPLUMBER_TEXT_KWARGS) or []
    except Exception:
        return 0.0
    for word in words:
        if str(word.get("text", "")).strip().lower().rstrip(":") == "abstract":
            return max(0.0, float(word["top"]) - 2.0)
    return 0.0


def extract_two_column_page_text(page: Any) -> str:
    width = float(page.width)
    height = float(page.height)
    mid_x = width / 2
    gutter_width = max(18.0, width * 0.03)
    column_start_y = first_page_column_start_y(page)
    page_texts: list[str] = []
    if column_start_y > 0:
        top_text = page.crop((0, 0, width, column_start_y)).extract_text(**PDFPLUMBER_TEXT_KWARGS) or ""
        top_text = normalize_text(top_text)
        if top_text:
            page_texts.append(top_text)

    bboxes = [
        (0, column_start_y, mid_x - gutter_width / 2, height),
        (mid_x + gutter_width / 2, column_start_y, width, height),
    ]
    column_texts: list[str] = []
    for bbox in bboxes:
        text = page.crop(bbox).extract_text(**PDFPLUMBER_TEXT_KWARGS) or ""
        text = normalize_text(text)
        if text:
            column_texts.append(text)
    if column_texts:
        page_texts.append("\n\n".join(column_texts))
    return "\n\n".join(page_texts)


def extract_pdfplumber_page_text(page: Any) -> str:
    if looks_like_two_column_page(page):
        return extract_two_column_page_text(page)
    return page.extract_text(**PDFPLUMBER_TEXT_KWARGS) or ""


def extract_text_with_pdfplumber(pdf_path: Path, max_pages: int | None = None) -> tuple[str, list[str]]:
    warnings: list[str] = []
    if pdfplumber is None:
        return "", ["pdfplumber is not installed"]

    page_texts: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages if max_pages is None else pdf.pages[:max_pages]
        for index, page in enumerate(pages, start=1):
            try:
                page_text = extract_pdfplumber_page_text(page)
            except Exception as exc:  # noqa: BLE001
                warnings.append(f"page {index}: pdfplumber extraction failed: {exc}")
                page_text = ""
            page_text = normalize_text(page_text)
            if page_text:
                page_texts.append(page_text)
    return "\n\n".join(page_texts).strip(), warnings


def extract_text_with_pypdf(pdf_path: Path, max_pages: int | None = None) -> tuple[str, list[str]]:
    warnings: list[str] = []
    if PdfReader is None:
        return "", ["pypdf/PyPDF2 is not installed"]

    reader = PdfReader(str(pdf_path))
    page_texts: list[str] = []
    pages = reader.pages if max_pages is None else reader.pages[:max_pages]
    for index, page in enumerate(pages, start=1):
        try:
            page_text = page.extract_text() or ""
        except TypeError:
            page_text = page.extract_text() or ""
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"page {index}: pypdf extraction failed: {exc}")
            page_text = ""
        page_text = normalize_text(page_text)
        if page_text:
            page_texts.append(page_text)
    return "\n\n".join(page_texts).strip(), warnings


def extract_pdf(pdf_path: Path, max_pages: int | None = None) -> PdfExtractionResult:
    if PdfReader is None and pdfplumber is None:
        raise RuntimeError(
            "No supported PDF extraction backend is installed. Install pdfplumber and pypdf."
        )

    reader = PdfReader(str(pdf_path)) if PdfReader is not None else None
    metadata = reader.metadata if reader is not None else {}
    extract_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    warnings: list[str] = []
    text = ""
    backend = "pdfplumber"
    if pdfplumber is not None:
        text, warnings = extract_text_with_pdfplumber(pdf_path, max_pages=max_pages)
    if not text:
        backend = "pypdf"
        fallback_text, fallback_warnings = extract_text_with_pypdf(pdf_path, max_pages=max_pages)
        warnings.extend(fallback_warnings)
        text = fallback_text

    outline = extract_outline(reader) if reader is not None else []
    status = "ok" if text else "outline_only" if outline else "failed"

    return PdfExtractionResult(
        source_pdf=pdf_path,
        extractor_backend=backend,
        extract_time=extract_time,
        title=first_non_empty(metadata_field(metadata, "/Title"), outline[0].title if outline else ""),
        author=metadata_field(metadata, "/Author"),
        doi=metadata_field(metadata, "/doi"),
        keywords=split_keywords(metadata_field(metadata, "/Keywords")),
        subject=metadata_field(metadata, "/Subject"),
        page_count=len(reader.pages) if reader is not None else 0,
        outline=outline,
        text=text,
        text_char_count=len(text),
        status=status,
        warnings=warnings,
    )


def extract_abstract_from_text(text: str) -> str:
    normalized = normalize_text(text)
    if not normalized:
        return ""

    after_abstract = slice_after_abstract_label(normalized)
    abstract = slice_until_section_boundary(after_abstract) if after_abstract else ""
    if not abstract:
        abstract = slice_until_section_boundary(fallback_preamble_abstract(normalized))
    return flatten_text(abstract)


def slice_after_abstract_label(text: str) -> str:
    match = re.search(r"(?is)\babstract\b\s*[:\n ]*", text)
    if not match:
        return ""
    return text[match.end():].strip()


def slice_until_section_boundary(text: str) -> str:
    boundary_patterns = [
        r"(?is)\n\s*keywords?\b",
        r"(?is)\n\s*index terms\b",
        r"(?is)\n\s*ccs concepts\b",
        r"(?is)\n\s*acm reference format\b",
        r"(?is)\n\s*1\s*\.?\s*introduction\b",
        r"(?is)\n\s*1\.1\b",
        r"(?is)\n\s*figure\s*1\b",
    ]
    end = len(text)
    for pattern in boundary_patterns:
        match = re.search(pattern, text)
        if match:
            end = min(end, match.start())
    return text[:end].strip()


def fallback_preamble_abstract(text: str) -> str:
    first_page = text.split("\n\n", 1)[0] if "\n\n" in text else text
    intro_match = re.search(r"(?is)\n\s*1\s*\.?\s*introduction\b", first_page)
    figure_match = re.search(r"(?is)\n\s*figure\s*1\b", first_page)
    cutoffs = [match.start() for match in (intro_match, figure_match) if match]
    preamble = first_page[: min(cutoffs)] if cutoffs else first_page
    lines = [line.strip() for line in preamble.splitlines() if line.strip()]
    candidate_lines = [line for line in lines if len(line) >= 120]
    if not candidate_lines:
        candidate_lines = [line for line in lines if len(line) >= 80]
    return "\n".join(candidate_lines).strip()


def quality_flags(result: PdfExtractionResult, abstract: str) -> list[str]:
    flags: list[str] = []
    if result.status != "ok":
        flags.append(f"extract_status:{result.status}")
    if result.text_char_count < 1000:
        flags.append("very_short_text")
    elif result.text_char_count < 5000:
        flags.append("short_text")
    if result.page_count and result.text_char_count / result.page_count < 700:
        flags.append("low_chars_per_page")
    if not abstract:
        flags.append("abstract_not_detected")
    elif (
        len(abstract) > 2500
        or "Permission to make digital" in abstract
        or "Copyright" in abstract
        or "ACM ISBN" in abstract
        or re.search(r"\b[A-Z]{2,}\s*[’']\d{2},", abstract)
    ):
        flags.append("abstract_may_include_layout_noise")
    if result.warnings:
        flags.append("has_warnings")
    return flags


def display_path(path: Path, project_root: Path) -> str:
    try:
        return str(path.relative_to(project_root))
    except ValueError:
        return str(path)


def render_markdown(result: PdfExtractionResult, project_root: Path, source_relative: Path, flags: list[str]) -> str:
    abstract = extract_abstract_from_text(result.text)
    lines = [
        "---",
        f"title: {json.dumps(result.title or result.source_pdf.stem, ensure_ascii=False)}",
        f"source_pdf: {json.dumps(str(source_relative), ensure_ascii=False)}",
        f"extractor_backend: {result.extractor_backend}",
        f"extracted_at_utc: {result.extract_time}",
        f"page_count: {result.page_count}",
        f"status: {result.status}",
        f"text_char_count: {result.text_char_count}",
        f"quality_flags: {json.dumps(flags, ensure_ascii=False)}",
        "---",
        "",
        "# PDF Fulltext",
        "",
        f"- Source PDF: `{display_path(result.source_pdf, project_root)}`",
        f"- Backend: {result.extractor_backend}",
        f"- Extracted at UTC: {result.extract_time}",
        f"- Page count: {result.page_count}",
        f"- Status: {result.status}",
        f"- Text chars: {result.text_char_count}",
        f"- Quality flags: {', '.join(flags) if flags else 'none'}",
        "",
        "## Metadata",
        "",
        f"- Title: {result.title or result.source_pdf.stem}",
        f"- Author: {result.author or 'unknown'}",
        f"- DOI: {result.doi or 'unknown'}",
        f"- Keywords: {', '.join(result.keywords) if result.keywords else 'unknown'}",
        f"- Subject: {result.subject or 'unknown'}",
        "",
        "## Extracted Abstract",
        "",
        abstract or "[abstract not detected]",
        "",
        "## Outline",
        "",
    ]
    if result.outline:
        for item in result.outline:
            indent = "  " * item.level
            suffix = f" (page {item.page_number})" if item.page_number is not None else ""
            lines.append(f"{indent}- {item.title}{suffix}")
    else:
        lines.append("- none")

    if result.warnings:
        lines.extend(["", "## Warnings", ""])
        for warning in result.warnings:
            lines.append(f"- {warning}")

    lines.extend(["", "## Markdown Content", "", result.text or "[no extractable text]", ""])
    return "\n".join(lines)


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_project_path(project_root: Path, raw: str) -> Path:
    path = Path(raw).expanduser()
    if path.is_absolute():
        return path.resolve()
    return (project_root / path).resolve()


def default_pdf_dir(project_root: Path) -> Path:
    standard = project_root / "assets" / "papers" / "pdf"
    legacy = project_root / "assets" / "papers" / "pdfs"
    if standard.exists() or not legacy.exists():
        return standard
    return legacy


def output_paths(pdf_path: Path, pdf_dir: Path, fulltext_dir: Path) -> tuple[Path, Path, Path]:
    relative = pdf_path.relative_to(pdf_dir)
    relative_md = relative.with_suffix(MARKDOWN_SUFFIX)
    relative_meta = relative.with_suffix(META_SUFFIX)
    return relative, fulltext_dir / relative_md, fulltext_dir / relative_meta


def collect_pdfs(pdf_dir: Path, include: str | None, limit: int | None) -> list[Path]:
    if not pdf_dir.exists():
        raise FileNotFoundError(f"PDF directory not found: {pdf_dir}")
    pattern = re.compile(include, re.IGNORECASE) if include else None
    pdfs = sorted(path for path in pdf_dir.rglob("*.pdf") if path.is_file())
    if pattern is not None:
        pdfs = [path for path in pdfs if pattern.search(str(path))]
    if limit is not None:
        pdfs = pdfs[:limit]
    return pdfs


def convert_one(
    pdf_path: Path,
    *,
    project_root: Path,
    pdf_dir: Path,
    fulltext_dir: Path,
    overwrite: bool,
    max_pages: int | None,
) -> dict[str, Any]:
    relative_pdf, markdown_path, meta_path = output_paths(pdf_path, pdf_dir, fulltext_dir)
    row: dict[str, Any] = {
        "source_pdf": display_path(pdf_path, project_root),
        "relative_pdf": str(relative_pdf),
        "fulltext_path": display_path(markdown_path, project_root),
        "meta_path": display_path(meta_path, project_root),
        "status": "not_run",
        "action": "not_run",
        "text_char_count": 0,
        "page_count": 0,
        "quality_flags": [],
        "error": "",
    }

    if not overwrite and markdown_path.exists() and meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8-sig"))
            row.update(
                {
                    "status": meta.get("status") or "ok",
                    "action": "skipped_existing",
                    "text_char_count": meta.get("text_char_count", 0),
                    "page_count": meta.get("page_count", 0),
                    "quality_flags": meta.get("quality_flags", []),
                }
            )
            return row
        except Exception:
            pass

    try:
        result = extract_pdf(pdf_path, max_pages=max_pages)
        abstract = extract_abstract_from_text(result.text)
        flags = quality_flags(result, abstract)
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(
            render_markdown(result, project_root, relative_pdf, flags),
            encoding="utf-8",
        )
        meta = result.to_meta_dict()
        meta.update(
            {
                "project_root": str(project_root),
                "relative_pdf": str(relative_pdf),
                "fulltext_path": display_path(markdown_path, project_root),
                "quality_flags": flags,
                "abstract": abstract,
            }
        )
        write_json(meta_path, meta)
        row.update(
            {
                "status": result.status,
                "action": "converted",
                "text_char_count": result.text_char_count,
                "page_count": result.page_count,
                "quality_flags": flags,
            }
        )
    except Exception as exc:  # noqa: BLE001
        row.update({"status": "failed", "action": "failed", "error": f"{exc.__class__.__name__}: {exc}"})
    return row


def write_summary(path: Path, rows: list[dict[str, Any]], pdf_dir: Path, fulltext_dir: Path) -> None:
    ok_statuses = {"ok", "outline_only"}
    converted_or_existing = sum(
        1 for row in rows if row["status"] in ok_statuses and row["action"] in {"converted", "skipped_existing"}
    )
    failed = sum(1 for row in rows if row["status"] == "failed")
    lines = [
        "# Fulltext Conversion Summary",
        "",
        f"Updated: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
        f"PDF directory: `{pdf_dir}`",
        f"Fulltext directory: `{fulltext_dir}`",
        f"Total selected: {len(rows)}",
        f"Converted or existing: {converted_or_existing}",
        f"Failed: {failed}",
        "",
        "| Source PDF | Status | Action | Chars | Pages | Flags | Fulltext |",
        "|---|---|---|---:|---:|---|---|",
    ]
    for row in rows:
        flags = ", ".join(row.get("quality_flags") or [])
        source_pdf = str(row.get("relative_pdf") or row.get("source_pdf") or "").replace("|", "\\|")
        fulltext = f"`{row['fulltext_path']}`" if row.get("fulltext_path") else ""
        lines.append(
            f"| `{source_pdf}` | {row.get('status') or ''} | {row.get('action') or ''} | "
            f"{row.get('text_char_count') or 0} | {row.get('page_count') or 0} | {flags} | {fulltext} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a standard research project's archived PDFs to Markdown fulltext."
    )
    parser.add_argument("project_root", help="Research project root, e.g. D:/0-Research/6-city")
    parser.add_argument(
        "--pdf-dir",
        default="",
        help="PDF directory relative to project root. Default: assets/papers/pdf, with assets/papers/pdfs fallback.",
    )
    parser.add_argument(
        "--fulltext-dir",
        default="assets/papers/fulltext",
        help="Fulltext output directory relative to project root.",
    )
    parser.add_argument(
        "--metadata-dir",
        default="assets/papers/metadata",
        help="Manifest and summary output directory relative to project root.",
    )
    parser.add_argument("--include", default="", help="Regex filter matched against PDF paths.")
    parser.add_argument("--limit", type=int, default=None, help="Convert only the first N matching PDFs.")
    parser.add_argument("--max-pages", type=int, default=None, help="Optional page limit for smoke tests.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing fulltext and meta files.")
    parser.add_argument("--dry-run", action="store_true", help="List selected PDFs without writing outputs.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    project_root = Path(args.project_root).expanduser().resolve()
    if not project_root.exists():
        sys.stderr.write(f"Project root not found: {project_root}\n")
        return 2

    pdf_dir = resolve_project_path(project_root, args.pdf_dir) if args.pdf_dir else default_pdf_dir(project_root)
    fulltext_dir = resolve_project_path(project_root, args.fulltext_dir)
    metadata_dir = resolve_project_path(project_root, args.metadata_dir)

    if pdfplumber is None and PdfReader is None:
        sys.stderr.write("Missing PDF dependencies. Install with: python -m pip install pdfplumber pypdf\n")
        return 2

    try:
        pdfs = collect_pdfs(pdf_dir, args.include or None, args.limit)
    except FileNotFoundError as exc:
        sys.stderr.write(f"{exc}\n")
        return 2

    if not pdfs:
        sys.stderr.write(f"No PDFs found in {pdf_dir}\n")
        return 1

    if args.dry_run:
        for pdf in pdfs:
            print(display_path(pdf, project_root))
        print(f"Selected {len(pdfs)} PDF(s) from {pdf_dir}")
        return 0

    rows: list[dict[str, Any]] = []
    for pdf in pdfs:
        row = convert_one(
            pdf,
            project_root=project_root,
            pdf_dir=pdf_dir,
            fulltext_dir=fulltext_dir,
            overwrite=args.overwrite,
            max_pages=args.max_pages,
        )
        flags = ",".join(row.get("quality_flags") or [])
        print(
            f"[{row['status']}/{row['action']}] {display_path(pdf, project_root)} "
            f"chars={row.get('text_char_count') or 0} flags={flags}",
            flush=True,
        )
        rows.append(row)

    manifest_path = metadata_dir / "fulltext_manifest.json"
    summary_path = metadata_dir / "fulltext_summary.md"
    write_json(manifest_path, rows)
    write_summary(summary_path, rows, pdf_dir, fulltext_dir)
    print(f"Wrote {manifest_path}")
    print(f"Wrote {summary_path}")
    return 0 if all(row["status"] != "failed" for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())

