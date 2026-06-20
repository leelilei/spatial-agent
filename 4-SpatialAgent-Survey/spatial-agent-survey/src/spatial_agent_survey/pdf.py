"""PDF extraction helpers for the survey workflow."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import json
import re
from pathlib import Path
from typing import Any

try:
    import pdfplumber
except ModuleNotFoundError:  # pragma: no cover - optional runtime dependency
    pdfplumber = None

try:
    from pypdf import PdfReader
except ModuleNotFoundError:  # pragma: no cover - optional runtime dependency
    try:
        from PyPDF2 import PdfReader  # type: ignore[assignment]
    except ModuleNotFoundError:  # pragma: no cover - optional runtime dependency
        PdfReader = None  # type: ignore[assignment]


DEFAULT_TEXT_EXTRACTION_BACKEND = "pdfplumber"
MARKDOWN_SUFFIX = ".fulltext.md"
META_SUFFIX = ".meta.json"
PDFPLUMBER_TEXT_KWARGS = {"x_tolerance": 1, "y_tolerance": 3}


@dataclass
class PdfOutlineItem:
    """A flattened outline entry with indentation level."""

    title: str
    level: int
    page_number: int | None = None


@dataclass
class PdfExtractionResult:
    """Normalized PDF extraction result."""

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
        """Serialize to the JSON sidecar format."""

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


def _normalize_text(text: str) -> str:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = _strip_pdf_boilerplate(normalized)
    normalized = re.sub(r"(?<=\w)-\n(?=\w)", "", normalized)
    normalized = re.sub(r"[ \t]+\n", "\n", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def _strip_pdf_boilerplate(text: str) -> str:
    """Remove common publisher permission footers that pollute extracted text."""

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
    return re.sub(r"\s+", " ", _normalize_text(text)).strip()


def _split_keywords(raw_keywords: str) -> list[str]:
    if not raw_keywords:
        return []
    return [part.strip() for part in raw_keywords.split(",") if part.strip()]


def _first_non_empty(*values: str | None) -> str:
    for value in values:
        if value and str(value).strip():
            return str(value).strip()
    return ""


def _get_metadata_field(metadata: Any, key: str) -> str:
    if not metadata:
        return ""
    try:
        value = metadata.get(key)
    except AttributeError:
        value = None
    return str(value).strip() if value else ""


def _extract_outline(reader: Any) -> list[PdfOutlineItem]:
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


def _extract_text_with_pdfplumber(pdf_path: Path, max_pages: int | None = None) -> tuple[str, list[str]]:
    warnings: list[str] = []
    if pdfplumber is None:
        return "", ["pdfplumber is not installed"]

    page_texts: list[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages if max_pages is None else pdf.pages[:max_pages]
        for index, page in enumerate(pages, start=1):
            try:
                page_text = _extract_pdfplumber_page_text(page)
            except Exception as exc:
                warnings.append(f"page {index}: pdfplumber extraction failed: {exc}")
                page_text = ""
            page_text = _normalize_text(page_text)
            if page_text:
                page_texts.append(page_text)

    return "\n\n".join(page_texts).strip(), warnings


def _extract_pdfplumber_page_text(page: Any) -> str:
    """Extract one page, preserving left-column then right-column order when detected."""

    if _looks_like_two_column_page(page):
        return _extract_two_column_page_text(page)
    return page.extract_text(**PDFPLUMBER_TEXT_KWARGS) or ""


def _looks_like_two_column_page(page: Any) -> bool:
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


def _extract_two_column_page_text(page: Any) -> str:
    width = float(page.width)
    height = float(page.height)
    mid_x = width / 2
    gutter_width = max(18.0, width * 0.03)
    column_start_y = _first_page_column_start_y(page)
    page_texts: list[str] = []
    if column_start_y > 0:
        top_text = page.crop((0, 0, width, column_start_y)).extract_text(**PDFPLUMBER_TEXT_KWARGS) or ""
        top_text = _normalize_text(top_text)
        if top_text:
            page_texts.append(top_text)

    bboxes = [
        (0, column_start_y, mid_x - gutter_width / 2, height),
        (mid_x + gutter_width / 2, column_start_y, width, height),
    ]
    column_texts: list[str] = []
    for bbox in bboxes:
        text = page.crop(bbox).extract_text(**PDFPLUMBER_TEXT_KWARGS) or ""
        text = _normalize_text(text)
        if text:
            column_texts.append(text)
    if column_texts:
        page_texts.append("\n\n".join(column_texts))
    return "\n\n".join(page_texts)


def _first_page_column_start_y(page: Any) -> float:
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


def _extract_text_with_pypdf(pdf_path: Path, max_pages: int | None = None) -> tuple[str, list[str]]:
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
        except Exception as exc:
            warnings.append(f"page {index}: pypdf extraction failed: {exc}")
            page_text = ""
        page_text = _normalize_text(page_text)
        if page_text:
            page_texts.append(page_text)
    return "\n\n".join(page_texts).strip(), warnings


def extract_pdf(pdf_path: str | Path, *, max_pages: int | None = None) -> PdfExtractionResult:
    """Extract text, metadata, and outline from a PDF."""

    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(path)

    extract_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    if PdfReader is None and pdfplumber is None:
        raise RuntimeError("No supported PDF extraction backend is installed")

    reader = PdfReader(str(path)) if PdfReader is not None else None
    metadata = reader.metadata if reader is not None else {}

    warnings: list[str] = []
    text = ""
    backend = DEFAULT_TEXT_EXTRACTION_BACKEND

    if pdfplumber is not None:
        text, warnings = _extract_text_with_pdfplumber(path, max_pages=max_pages)
    if not text:
        backend = "pypdf"
        fallback_text, fallback_warnings = _extract_text_with_pypdf(path, max_pages=max_pages)
        warnings.extend(fallback_warnings)
        text = fallback_text

    outline = _extract_outline(reader) if reader is not None else []
    status = "ok" if text else "outline_only" if outline else "failed"

    result = PdfExtractionResult(
        source_pdf=path,
        extractor_backend=backend,
        extract_time=extract_time,
        title=_first_non_empty(_get_metadata_field(metadata, "/Title"), outline[0].title if outline else ""),
        author=_get_metadata_field(metadata, "/Author"),
        doi=_get_metadata_field(metadata, "/doi"),
        keywords=_split_keywords(_get_metadata_field(metadata, "/Keywords")),
        subject=_get_metadata_field(metadata, "/Subject"),
        page_count=len(reader.pages) if reader is not None else 0,
        outline=outline,
        text=text,
        text_char_count=len(text),
        status=status,
        warnings=warnings,
    )
    return result


def render_fulltext_markdown(result: PdfExtractionResult) -> str:
    """Render a full-text Markdown artifact."""

    lines = [f"Title: {result.title or result.source_pdf.stem}", "", f"Source PDF: {result.source_pdf}", ""]
    lines.extend(
        [
            "Extraction:",
            f"- backend: {result.extractor_backend}",
            f"- extracted_at_utc: {result.extract_time}",
            f"- page_count: {result.page_count}",
            f"- status: {result.status}",
            f"- text_char_count: {result.text_char_count}",
            "",
            "Metadata:",
            f"- author: {result.author or 'unknown'}",
            f"- doi: {result.doi or 'unknown'}",
            f"- keywords: {', '.join(result.keywords) if result.keywords else 'unknown'}",
            f"- subject: {result.subject or 'unknown'}",
            "",
            "Outline:",
        ]
    )

    if result.outline:
        for item in result.outline:
            indent = "  " * item.level
            if item.page_number is not None:
                lines.append(f"{indent}- {item.title} (page {item.page_number})")
            else:
                lines.append(f"{indent}- {item.title}")
    else:
        lines.append("- none")

    if result.warnings:
        lines.extend(["", "Warnings:"])
        for warning in result.warnings:
            lines.append(f"- {warning}")

    lines.extend(["", "Markdown Content:", ""])
    lines.append(result.text or "[no extractable text]")
    lines.append("")
    return "\n".join(lines)


def write_fulltext_outputs(
    result: PdfExtractionResult,
    *,
    output_dir: str | Path | None = None,
    emit_meta: bool = True,
) -> tuple[Path, Path | None]:
    """Write Markdown and JSON sidecar outputs for one extracted PDF."""

    target_dir = Path(output_dir) if output_dir is not None else result.source_pdf.parent
    target_dir.mkdir(parents=True, exist_ok=True)
    stem = result.source_pdf.stem

    markdown_path = target_dir / f"{stem}{MARKDOWN_SUFFIX}"
    markdown_path.write_text(render_fulltext_markdown(result), encoding="utf-8")

    meta_path: Path | None = None
    if emit_meta:
        meta_path = target_dir / f"{stem}{META_SUFFIX}"
        meta_path.write_text(
            json.dumps(result.to_meta_dict(), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    return markdown_path, meta_path


def extract_pdf_abstract(pdf_path: str | Path, max_pages: int = 2) -> str:
    """Extract an abstract-like snippet from the first pages of a PDF."""

    result = extract_pdf(pdf_path, max_pages=max_pages)
    return extract_abstract_from_text(result.text)


def extract_abstract_from_text(text: str) -> str:
    """Heuristically recover the abstract section from extracted text."""

    normalized = _normalize_text(text)
    if not normalized:
        return ""

    after_abstract = _slice_after_abstract_label(normalized)
    abstract = _slice_until_section_boundary(after_abstract) if after_abstract else ""
    if not abstract:
        abstract = _slice_until_section_boundary(_fallback_preamble_abstract(normalized))
    return flatten_text(abstract)


def _slice_after_abstract_label(text: str) -> str:
    match = re.search(r"(?is)\babstract\b\s*[:\n ]*", text)
    if not match:
        return ""
    return text[match.end():].strip()


def _slice_until_section_boundary(text: str) -> str:
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


def _fallback_preamble_abstract(text: str) -> str:
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
