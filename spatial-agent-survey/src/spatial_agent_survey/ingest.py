"""Ingestion and deduplication helpers for raw paper search results."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from .schemas import PaperRecord


def read_jsonl(path: Path) -> List[Dict]:
    rows: List[Dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def write_csv(
    path: Path,
    rows: Sequence[Dict],
    fieldnames: Sequence[str],
    *,
    encoding: str = "utf-8",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding=encoding, newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "untitled"


def _normalize_authors(raw_value: object) -> List[str]:
    if raw_value is None:
        return []
    if isinstance(raw_value, list):
        return [str(item).strip() for item in raw_value if str(item).strip()]
    text = str(raw_value).strip()
    if not text:
        return []
    if ";" in text:
        parts = text.split(";")
    elif "," in text:
        parts = text.split(",")
    else:
        parts = [text]
    return [part.strip() for part in parts if part.strip()]


def reconstruct_openalex_abstract(inverted_index: Dict | None) -> str:
    """Rebuild plain-text abstract from OpenAlex inverted index payload."""

    if not inverted_index:
        return ""

    token_positions: List[tuple[int, str]] = []
    for token, positions in inverted_index.items():
        for position in positions or []:
            try:
                token_positions.append((int(position), str(token)))
            except (TypeError, ValueError):
                continue

    if not token_positions:
        return ""

    ordered_tokens = [token for _, token in sorted(token_positions, key=lambda item: item[0])]
    return " ".join(ordered_tokens).strip()


def openalex_result_to_raw_record(
    raw: Dict,
    *,
    query_family: str,
    search_variant: str,
    search_batch: str,
) -> Dict[str, object]:
    """Convert one OpenAlex work result into repo raw-search JSONL shape."""

    primary_location = raw.get("primary_location") or {}
    source = primary_location.get("source") or {}
    ids = raw.get("ids") or {}

    venue = (
        source.get("display_name")
        or primary_location.get("raw_source_name")
        or raw.get("host_venue", {}).get("display_name")
        or ""
    )
    url = (
        primary_location.get("landing_page_url")
        or primary_location.get("pdf_url")
        or raw.get("doi")
        or ids.get("openalex")
        or ""
    )
    authors = []
    for authorship in raw.get("authorships") or []:
        author = authorship.get("author") or {}
        display_name = str(author.get("display_name") or "").strip()
        if display_name:
            authors.append(display_name)

    return {
        "title": str(raw.get("title") or raw.get("display_name") or "").strip(),
        "abstract": reconstruct_openalex_abstract(raw.get("abstract_inverted_index")),
        "year": raw.get("publication_year"),
        "venue": str(venue).strip(),
        "url": str(url).strip(),
        "doi": str(raw.get("doi") or ids.get("doi") or "").replace("https://doi.org/", "").strip(),
        "authors": authors,
        "query_family": query_family,
        "search_variant": search_variant,
        "search_source": "openalex",
        "search_batch": search_batch,
        "openalex_id": str(ids.get("openalex") or raw.get("id") or "").strip(),
        "openalex_type": str(raw.get("type") or "").strip(),
        "cited_by_count": raw.get("cited_by_count", 0),
    }


def make_paper_id(title: str, year: int | None = None, doi: str = "", url: str = "") -> str:
    if doi:
        digest = hashlib.md5(doi.lower().encode("utf-8")).hexdigest()[:10]
        return f"doi-{digest}"
    if url:
        digest = hashlib.md5(url.lower().encode("utf-8")).hexdigest()[:10]
        return f"url-{digest}"
    slug = _slugify(title)
    suffix = str(year) if year else "na"
    return f"{slug}-{suffix}"


def normalize_raw_record(raw: Dict, source_family: str) -> PaperRecord:
    title = (
        raw.get("title")
        or raw.get("paperTitle")
        or raw.get("name")
        or raw.get("paper_title")
        or ""
    )
    abstract = raw.get("abstract") or raw.get("summary") or raw.get("snippet") or ""
    year = raw.get("year") or raw.get("publication_year") or raw.get("pub_year")
    venue = raw.get("venue") or raw.get("journal") or raw.get("conference") or ""
    url = raw.get("url") or raw.get("link") or raw.get("paper_url") or ""
    doi = raw.get("doi") or raw.get("DOI") or ""
    authors = _normalize_authors(raw.get("authors") or raw.get("author"))
    parsed_year = None
    if year not in (None, ""):
        try:
            parsed_year = int(year)
        except (TypeError, ValueError):
            parsed_year = None
    paper_id = make_paper_id(title=title, year=parsed_year, doi=doi, url=url)
    return PaperRecord(
        paper_id=paper_id,
        title=title,
        abstract=str(abstract).strip(),
        year=parsed_year,
        venue=str(venue).strip(),
        url=str(url).strip(),
        doi=str(doi).strip(),
        authors=authors,
        source_families=[source_family],
    )


def ingest_search_results(raw_dir: Path) -> List[PaperRecord]:
    papers: List[PaperRecord] = []
    if not raw_dir.exists():
        return papers
    for path in sorted(raw_dir.rglob("*.jsonl")):
        source_family = path.stem
        for raw_row in read_jsonl(path):
            papers.append(normalize_raw_record(raw_row, source_family=source_family))
    return papers


def dedupe_papers(papers: Iterable[PaperRecord]) -> Tuple[List[PaperRecord], List[Dict[str, str]]]:
    deduped: Dict[str, PaperRecord] = {}
    duplicates: List[Dict[str, str]] = []
    for paper in papers:
        key = paper.doi.lower() or paper.url.lower() or f"{paper.title.lower()}::{paper.year}"
        if key in deduped:
            existing = deduped[key]
            merged_sources = sorted(set(existing.source_families + paper.source_families))
            existing.source_families = merged_sources
            duplicates.append(
                {
                    "kept_paper_id": existing.paper_id,
                    "duplicate_paper_id": paper.paper_id,
                    "reason": "doi/url/title-year",
                }
            )
            continue
        deduped[key] = paper
    return list(deduped.values()), duplicates


def papers_to_rows(papers: Iterable[PaperRecord]) -> List[Dict]:
    rows: List[Dict] = []
    for paper in papers:
        row = paper.model_dump()
        row["authors"] = "; ".join(row["authors"])
        row["source_families"] = "; ".join(row["source_families"])
        if row.get("final_status") is not None:
            row["final_status"] = row["final_status"].value
        if row.get("corpus_tier") is not None:
            row["corpus_tier"] = row["corpus_tier"].value
        if row.get("core_layer") is not None:
            row["core_layer"] = row["core_layer"].value
        if row.get("exclusion_reason") is not None:
            row["exclusion_reason"] = row["exclusion_reason"].value
        rows.append(row)
    return rows
