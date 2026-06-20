#!/usr/bin/env python3
"""Convert Telephone paper PDFs into project-aware Markdown full text.

This wrapper reuses the PDF extraction helpers from 4-SpatialAgent-Survey while
keeping Telephone-specific outputs and citation metadata under assets/papers.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[3]
RESEARCH_ROOT = ROOT.parent
SURVEY_SRC = RESEARCH_ROOT / "4-SpatialAgent-Survey" / "spatial-agent-survey" / "src"
if str(SURVEY_SRC) not in sys.path:
    sys.path.insert(0, str(SURVEY_SRC))

from spatial_agent_survey.pdf import extract_abstract_from_text, extract_pdf, render_fulltext_markdown


PAPERS_DIR = ROOT / "assets" / "papers"
METADATA_DIR = PAPERS_DIR / "metadata"
FULLTEXT_DIR = PAPERS_DIR / "fulltext"
CITATION_SOURCES = METADATA_DIR / "citation_sources.json"
FULLTEXT_MANIFEST = METADATA_DIR / "fulltext_manifest.json"
FULLTEXT_SUMMARY = METADATA_DIR / "fulltext_summary.md"

CORE_INDEXES = [
    11,  # Generative Agents
    2,   # Simulating Rumor Spreading in Social Networks using LLM Agents
    20,  # Multiagent Debate
    4,   # Debate Helps Supervise Unreliable Experts
    29,  # TruthfulQA
    32,  # Semantic Entropy
    37,  # Internal State / lying
    39,  # Cannot self-correct
    42,  # MemoryBank
    43,  # MemGPT
    44,  # Reflexion
    50,  # LLM misinformation propagation
    53,  # Science of fake news
    54,  # Rumor Cascades
    61,  # Belief Echoes
    9,   # AI models collapse
    10,  # Artificial Hivemind
    68,  # Curse of Recursion
    69,  # Self-Consuming Models Go MAD
    71,  # LAAC
]


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_citations() -> list[dict]:
    rows = read_json(CITATION_SOURCES)
    return sorted(rows, key=lambda row: row["index"])


def parse_indexes(raw: str) -> list[int]:
    indexes: list[int] = []
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        indexes.append(int(part))
    return indexes


def category_from_pdf_path(pdf_path: Path) -> str:
    try:
        relative = pdf_path.relative_to(PAPERS_DIR / "pdf")
    except ValueError:
        return "99_uncategorized"
    return relative.parts[0] if len(relative.parts) > 1 else "99_uncategorized"


def fulltext_paths(pdf_path: Path) -> tuple[Path, Path]:
    category = category_from_pdf_path(pdf_path)
    out_dir = FULLTEXT_DIR / category
    return out_dir / f"{pdf_path.stem}.fulltext.md", out_dir / f"{pdf_path.stem}.meta.json"


def quality_flags(row: dict, text_char_count: int, page_count: int, abstract: str) -> list[str]:
    flags: list[str] = []
    if row.get("status") != "ok":
        flags.append(f"extract_status:{row.get('status')}")
    if text_char_count < 1000:
        flags.append("very_short_text")
    elif text_char_count < 5000:
        flags.append("short_text")
    if page_count and text_char_count / page_count < 700:
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
    return flags


def citation_block(citation: dict, abstract: str, flags: list[str]) -> str:
    lines = [
        "---",
        f"telephone_index: {citation['index']}",
        f"title: {json.dumps(citation['title'], ensure_ascii=False)}",
        f"category: {category_from_pdf_path(ROOT / citation['pdf_path']) if citation.get('pdf_path') else ''}",
        f"venue: {json.dumps(citation.get('venue') or '', ensure_ascii=False)}",
        f"year: {citation.get('year') or ''}",
        f"doi: {citation.get('doi') or ''}",
        f"arxiv_id: {citation.get('arxiv_id') or ''}",
        f"preferred_source_type: {citation.get('preferred_source_type') or ''}",
        f"publisher_url: {citation.get('publisher_url') or ''}",
        f"quality_flags: {json.dumps(flags, ensure_ascii=False)}",
        "---",
        "",
        "# Citation Context",
        "",
        f"- Telephone index: {citation['index']}",
        f"- Preferred source: {citation.get('venue') or 'unresolved'}",
        f"- DOI: {citation.get('doi') or 'none'}",
        f"- arXiv: {citation.get('arxiv_id') or 'none'}",
        f"- PDF: `{citation.get('pdf_path') or ''}`",
        "",
        "## Extracted Abstract",
        "",
        abstract or "[abstract not detected]",
        "",
    ]
    return "\n".join(lines)


def convert_one(citation: dict, overwrite: bool = False, max_pages: int | None = None) -> dict:
    pdf_rel = citation.get("pdf_path")
    result_row = {
        "index": citation["index"],
        "title": citation["title"],
        "status": "missing_pdf",
        "conversion_action": "not_run",
        "pdf_path": pdf_rel,
        "fulltext_path": None,
        "meta_path": None,
        "text_char_count": 0,
        "page_count": 0,
        "quality_flags": [],
        "error": "",
    }
    if not pdf_rel:
        result_row["error"] = "No local PDF path in citation_sources.json."
        return result_row

    pdf_path = ROOT / pdf_rel
    if not pdf_path.exists():
        result_row["error"] = f"PDF not found: {pdf_rel}"
        return result_row

    markdown_path, meta_path = fulltext_paths(pdf_path)
    if not overwrite and markdown_path.exists() and meta_path.exists():
        try:
            meta = read_json(meta_path)
            result_row.update({
                "status": meta.get("status") or "ok",
                "conversion_action": "skipped_existing",
                "fulltext_path": str(markdown_path.relative_to(ROOT)),
                "meta_path": str(meta_path.relative_to(ROOT)),
                "text_char_count": meta.get("text_char_count", 0),
                "page_count": meta.get("page_count", 0),
                "quality_flags": meta.get("telephone_quality_flags", []),
            })
            return result_row
        except Exception:
            pass

    try:
        extraction = extract_pdf(pdf_path, max_pages=max_pages)
        abstract = extract_abstract_from_text(extraction.text)
        flags = quality_flags(extraction.to_meta_dict(), extraction.text_char_count, extraction.page_count, abstract)
        markdown = citation_block(citation, abstract, flags) + render_fulltext_markdown(extraction)
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_path.write_text(markdown, encoding="utf-8")

        meta = extraction.to_meta_dict()
        meta.update({
            "telephone_index": citation["index"],
            "telephone_title": citation["title"],
            "telephone_category": category_from_pdf_path(pdf_path),
            "telephone_citation": citation,
            "telephone_abstract": abstract,
            "telephone_quality_flags": flags,
        })
        write_json(meta_path, meta)
        result_row.update({
            "status": extraction.status,
            "conversion_action": "converted",
            "fulltext_path": str(markdown_path.relative_to(ROOT)),
            "meta_path": str(meta_path.relative_to(ROOT)),
            "text_char_count": extraction.text_char_count,
            "page_count": extraction.page_count,
            "quality_flags": flags,
        })
        return result_row
    except Exception as exc:  # noqa: BLE001
        result_row["status"] = "failed"
        result_row["error"] = f"{exc.__class__.__name__}: {exc}"
        return result_row


def write_summary(rows: list[dict], selection_label: str) -> None:
    converted = sum(1 for row in rows if row["status"] in {"ok", "outline_only", "skipped_existing"})
    failed = len(rows) - converted
    lines = [
        "# Fulltext Conversion Summary",
        "",
        f"Updated: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
        f"Selection: {selection_label}",
        f"Total selected: {len(rows)}",
        f"Converted or existing: {converted}",
        f"Missing or failed: {failed}",
        "",
        "| # | Title | Status | Action | Chars | Pages | Flags | Fulltext |",
        "|---|---|---|---|---:|---:|---|---|",
    ]
    for row in rows:
        flags = ", ".join(row.get("quality_flags") or [])
        fulltext = f"`{row['fulltext_path']}`" if row.get("fulltext_path") else ""
        title = row["title"].replace("|", "\\|")
        lines.append(
            f"| {row['index']} | {title} | {row['status']} | {row.get('conversion_action') or ''} | "
            f"{row.get('text_char_count') or 0} | {row.get('page_count') or 0} | {flags} | {fulltext} |"
        )
    FULLTEXT_SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")


def select_rows(citations: list[dict], args: argparse.Namespace) -> tuple[list[dict], str]:
    if args.all:
        return [row for row in citations if row.get("pdf_path")], "all local PDFs"
    if args.indexes:
        wanted = set(parse_indexes(args.indexes))
        return [row for row in citations if row["index"] in wanted], f"indexes {args.indexes}"
    wanted = set(CORE_INDEXES)
    return [row for row in citations if row["index"] in wanted], "core-first batch"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="convert all local PDFs")
    parser.add_argument("--indexes", default="", help="comma-separated citation indexes to convert")
    parser.add_argument("--overwrite", action="store_true", help="overwrite existing fulltext outputs")
    parser.add_argument("--max-pages", type=int, default=None, help="optional page limit for testing")
    args = parser.parse_args()

    citations = load_citations()
    selected, label = select_rows(citations, args)
    if not selected:
        raise SystemExit("No matching local PDFs selected.")

    rows = []
    for citation in selected:
        row = convert_one(citation, overwrite=args.overwrite, max_pages=args.max_pages)
        print(
            f"[{row['status']}/{row.get('conversion_action')}] {row['index']:02d} {row['title']} "
            f"chars={row.get('text_char_count') or 0} flags={','.join(row.get('quality_flags') or [])}",
            flush=True,
        )
        rows.append(row)

    write_json(FULLTEXT_MANIFEST, rows)
    write_summary(rows, label)
    print(f"Wrote {FULLTEXT_MANIFEST}")
    print(f"Wrote {FULLTEXT_SUMMARY}")
    return 0 if all(row["status"] != "failed" for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
