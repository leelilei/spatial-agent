#!/usr/bin/env python3
"""Backfill missing Phase 1 abstracts from external metadata and local proxies."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote
from urllib.request import Request, urlopen

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent

HTTP_HEADERS = {"User-Agent": "Mozilla/5.0 Codex Phase1 Abstract Backfill"}
DEFAULT_TIMEOUT = 10
DEFAULT_WORKERS = 6

PLACEHOLDER_ZH_SUMMARY = (
    "当前未获取到英文摘要；现阶段仅能依据题名与分层做初步判断，需补全文或外部元数据后再进一步复核。"
)

PROXY_SUMMARIES = {
    "Space is the Machine: A Configurational Theory of Architecture": (
        "This book develops a configurational theory of architecture, arguing that space is "
        "not a neutral container but an active structure that shapes movement, encounter, "
        "visibility, and urban life. It systematizes analytic methods for describing spatial "
        "layouts in buildings and cities and connects these configurational properties to "
        "social effects such as movement economies, co-presence, and the organization of built form."
    ),
}


@dataclass(frozen=True)
class LookupRecord:
    record_id: str
    title: str
    doi: str
    url: str
    venue: str


@dataclass
class Resolution:
    abstract: str
    source: str
    status: str
    note: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidate-pool",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_candidate_pool_2026-04-13.csv",
    )
    parser.add_argument(
        "--papers-master",
        type=Path,
        default=REPO_ROOT / "spatial-agent-survey" / "data" / "processed" / "papers_master_phase1_2026-04-13.csv",
    )
    parser.add_argument(
        "--papers-master-raw",
        type=Path,
        default=REPO_ROOT / "spatial-agent-survey" / "data" / "processed" / "papers_master_raw_phase1_2026-04-13.csv",
    )
    parser.add_argument(
        "--manual-review",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_2026-04-13.csv",
    )
    parser.add_argument(
        "--translation-input",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_translation_input_2026-04-13.json",
    )
    parser.add_argument(
        "--abstract-rereview",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_abstract_rereview_round1_2026-04-13.csv",
    )
    parser.add_argument(
        "--fresh-abstracts",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_fresh_targeted_l4_tilt_abstracts_2026-04-28.csv",
    )
    parser.add_argument(
        "--fresh-disposition",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_fresh_targeted_l4_tilt_abstract_disposition_2026-04-28.csv",
    )
    parser.add_argument(
        "--report-csv",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_missing_abstract_backfill_2026-04-28.csv",
    )
    parser.add_argument(
        "--report-md",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_missing_abstract_backfill_2026-04-28.md",
    )
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    return parser.parse_args()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        return list(reader.fieldnames or []), rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def normalize_doi(value: str) -> str:
    doi = str(value or "").strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if doi.lower().startswith(prefix):
            doi = doi[len(prefix) :]
            break
    return doi.strip().lower()


def normalize_title(value: str) -> str:
    text = html.unescape(str(value or "").lower())
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^a-z0-9 ]+", "", text)
    return text.strip()


def clean_text(value: str) -> str:
    text = html.unescape(str(value or ""))
    text = text.replace("&#13;", " ").replace("\r", "\n").replace("\u00a0", " ")
    text = re.sub(r"-\s*\n\s*", "", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" ?\n ?", "\n", text)
    return text.strip()


def flatten_text(value: str) -> str:
    return re.sub(r"\s+", " ", clean_text(value)).strip()


def strip_tags(value: str) -> str:
    return flatten_text(re.sub(r"<[^>]+>", " ", str(value or "")))


def is_usable_abstract(value: str) -> bool:
    text = flatten_text(value)
    if len(text) < 80:
        return False
    lowered = text.lower()
    if lowered.startswith("cambridge core -") or lowered.startswith("space is the machine"):
        return False
    return True


def fetch_text(url: str, timeout: int) -> str:
    request = Request(url, headers=HTTP_HEADERS)
    with urlopen(request, timeout=timeout) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="replace")


def reconstruct_openalex_abstract(inverted_index: dict[str, list[int]] | None) -> str:
    if not inverted_index:
        return ""
    positions: dict[int, str] = {}
    for token, indexes in inverted_index.items():
        for index in indexes:
            positions[index] = token
    return " ".join(positions[index] for index in sorted(positions))


def parse_meta_abstract(html_text: str) -> tuple[str, str]:
    for match in re.finditer(r"<meta\s+([^>]+)>", html_text, flags=re.I):
        attrs = dict(
            (key.lower(), html.unescape(value))
            for key, value in re.findall(r'([\w:-]+)\s*=\s*["\']([^"\']*)["\']', match.group(1))
        )
        key = (attrs.get("name") or attrs.get("property") or "").lower()
        if key in {
            "citation_abstract",
            "dc.description",
            "dcterms.abstract",
            "eprints.abstract",
            "description",
            "og:description",
            "twitter:description",
        }:
            content = strip_tags(attrs.get("content", ""))
            if is_usable_abstract(content):
                return content, f"meta:{key}"

    for match in re.finditer(
        r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
        html_text,
        flags=re.I | re.S,
    ):
        raw = match.group(1).strip()
        try:
            payload = json.loads(raw)
        except Exception:
            continue
        objects = payload if isinstance(payload, list) else [payload]
        for item in objects:
            if not isinstance(item, dict):
                continue
            description = strip_tags(str(item.get("description") or ""))
            if is_usable_abstract(description):
                return description, "jsonld:description"

    patterns = [
        (r'<blockquote[^>]*class=["\'][^"\']*abstract[^"\']*["\'][^>]*>(.*?)</blockquote>', "html:blockquote_abstract"),
        (r'<div[^>]*class=["\'][^"\']*acl-abstract[^"\']*["\'][^>]*>(.*?)</div>', "html:acl_abstract"),
        (r'<section[^>]*class=["\'][^"\']*abstract[^"\']*["\'][^>]*>(.*?)</section>', "html:section_abstract"),
        (r'<div[^>]*id=["\'][^"\']*abstract[^"\']*["\'][^>]*>(.*?)</div>', "html:div_id_abstract"),
    ]
    for pattern, source in patterns:
        match = re.search(pattern, html_text, flags=re.I | re.S)
        if not match:
            continue
        text = strip_tags(match.group(1))
        text = re.sub(r"^Abstract\s*", "", text, flags=re.I)
        if is_usable_abstract(text):
            return text, source

    return "", ""


class AbstractResolver:
    def __init__(self, timeout: int) -> None:
        self.timeout = timeout
        self.cache: dict[tuple[str, str, str], Resolution] = {}
        self.lock = threading.Lock()

    def resolve(self, record: LookupRecord) -> Resolution:
        cache_key = (normalize_title(record.title), normalize_doi(record.doi), record.url.strip())
        with self.lock:
            cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        resolution = self._resolve_uncached(record)
        with self.lock:
            self.cache[cache_key] = resolution
        return resolution

    def _resolve_uncached(self, record: LookupRecord) -> Resolution:
        for method in (
            self._from_openalex_by_doi,
            self._from_crossref,
            self._from_openalex_by_title,
            self._from_page_meta,
            self._from_proxy_summary,
        ):
            resolution = method(record)
            if resolution is not None:
                return resolution
        return Resolution("", "", "unresolved", "No usable abstract found.")

    def _from_openalex_by_doi(self, record: LookupRecord) -> Resolution | None:
        doi = normalize_doi(record.doi)
        if not doi:
            return None
        url = f"https://api.openalex.org/works?filter=doi:{quote(doi)}&per-page=1"
        try:
            payload = json.loads(fetch_text(url, self.timeout))
        except Exception:
            return None
        for result in payload.get("results", []):
            abstract = reconstruct_openalex_abstract(result.get("abstract_inverted_index"))
            if is_usable_abstract(abstract):
                return Resolution(flatten_text(abstract), "openalex_doi", "resolved")
        return None

    def _from_crossref(self, record: LookupRecord) -> Resolution | None:
        doi = normalize_doi(record.doi)
        if not doi:
            return None
        url = f"https://api.crossref.org/works/{quote(doi)}"
        try:
            payload = json.loads(fetch_text(url, self.timeout))
        except Exception:
            return None
        abstract = strip_tags(str((payload.get("message") or {}).get("abstract") or ""))
        if is_usable_abstract(abstract):
            return Resolution(abstract, "crossref", "resolved")
        return None

    def _from_openalex_by_title(self, record: LookupRecord) -> Resolution | None:
        title = record.title.strip()
        if not title:
            return None
        expected = normalize_title(title)
        url = f"https://api.openalex.org/works?search={quote(title)}&per-page=5"
        try:
            payload = json.loads(fetch_text(url, self.timeout))
        except Exception:
            return None
        doi = normalize_doi(record.doi)
        for result in payload.get("results", []):
            result_title = normalize_title(result.get("display_name") or result.get("title") or "")
            result_doi = normalize_doi((((result.get("ids") or {}).get("doi")) or result.get("doi") or ""))
            if expected and result_title != expected and doi and result_doi != doi:
                continue
            if expected and result_title != expected and not doi:
                continue
            abstract = reconstruct_openalex_abstract(result.get("abstract_inverted_index"))
            if is_usable_abstract(abstract):
                return Resolution(flatten_text(abstract), "openalex_title", "resolved")
        return None

    def _from_page_meta(self, record: LookupRecord) -> Resolution | None:
        candidates: list[tuple[str, str]] = []
        if record.url.strip():
            candidates.append((record.url.strip(), "url"))
        doi = normalize_doi(record.doi)
        if doi:
            candidates.append((f"https://doi.org/{doi}", "doi_landing"))

        seen: set[str] = set()
        for candidate, _kind in candidates:
            if candidate in seen:
                continue
            seen.add(candidate)
            try:
                html_text = fetch_text(candidate, self.timeout)
            except Exception:
                continue
            abstract, source = parse_meta_abstract(html_text)
            if abstract:
                return Resolution(abstract, source, "resolved")
        return None

    def _from_proxy_summary(self, record: LookupRecord) -> Resolution | None:
        proxy = PROXY_SUMMARIES.get(record.title.strip())
        if not proxy:
            return None
        return Resolution(flatten_text(proxy), "proxy_local_summary", "proxy")


def build_lookup_records(rows: list[dict[str, str]], key_field: str) -> dict[str, LookupRecord]:
    records: dict[str, LookupRecord] = {}
    for row in rows:
        key = str(row.get(key_field) or "").strip()
        if not key:
            continue
        records[key] = LookupRecord(
            record_id=key,
            title=str(row.get("title") or "").strip(),
            doi=str(row.get("doi") or "").strip(),
            url=str(row.get("url") or "").strip(),
            venue=str(row.get("venue") or "").strip(),
        )
    return records


def resolve_missing(
    rows: list[dict[str, str]],
    key_field: str,
    resolver: AbstractResolver,
    workers: int,
) -> dict[str, Resolution]:
    lookup_records = build_lookup_records(rows, key_field)
    missing = [record for record in lookup_records.values() if not str(next(row for row in rows if str(row.get(key_field) or "").strip() == record.record_id).get("abstract") or "").strip()]
    resolutions: dict[str, Resolution] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {executor.submit(resolver.resolve, record): record for record in missing}
        for future in as_completed(future_map):
            record = future_map[future]
            try:
                resolutions[record.record_id] = future.result()
            except Exception as exc:
                resolutions[record.record_id] = Resolution("", "", "error", str(exc))
    return resolutions


def apply_candidate_backfill(
    rows: list[dict[str, str]],
    key_field: str,
    resolutions: dict[str, Resolution],
) -> int:
    updated = 0
    for row in rows:
        key = str(row.get(key_field) or "").strip()
        if not key:
            continue
        if str(row.get("abstract") or "").strip():
            continue
        resolution = resolutions.get(key)
        if not resolution or not resolution.abstract:
            continue
        row["abstract"] = resolution.abstract
        updated += 1
    return updated


def apply_review_sheet_sync(
    rows: list[dict[str, str]],
    candidate_abstracts: dict[str, str],
    candidate_sources: dict[str, str],
) -> int:
    updated = 0
    for row in rows:
        paper_id = str(row.get("paper_id") or "").strip()
        abstract = candidate_abstracts.get(paper_id, "")
        if not abstract:
            continue
        current = str(row.get("abstract") or "").strip()
        if current == abstract and str(row.get("abstract_source") or "").strip():
            continue
        row["abstract"] = abstract
        if "abstract_source" in row:
            row["abstract_source"] = candidate_sources.get(paper_id, "candidate_pool")
        updated += 1
    return updated


def apply_translation_input_sync(
    payload: list[dict[str, Any]],
    candidate_abstracts: dict[str, str],
) -> int:
    updated = 0
    for item in payload:
        paper_id = str(item.get("paper_id") or "").strip()
        abstract = candidate_abstracts.get(paper_id, "")
        if not abstract:
            continue
        current = str(item.get("abstract") or "").strip()
        if current == abstract:
            continue
        item["abstract"] = abstract
        updated += 1
    return updated


def update_fresh_abstract_status(rows: list[dict[str, str]], resolutions: dict[str, Resolution]) -> int:
    updated = 0
    for row in rows:
        key = str(row.get("fresh_id") or "").strip()
        if not key:
            continue
        resolution = resolutions.get(key)
        if not resolution or not resolution.abstract:
            continue
        if not str(row.get("abstract") or "").strip():
            row["abstract"] = resolution.abstract
            updated += 1
        if "abstract_status" in row:
            row["abstract_status"] = "abstract_available"
    return updated


def build_candidate_maps(rows: list[dict[str, str]]) -> tuple[dict[str, str], dict[str, str]]:
    abstract_map: dict[str, str] = {}
    source_map: dict[str, str] = {}
    for row in rows:
        key = str(row.get("paper_id") or "").strip()
        abstract = str(row.get("abstract") or "").strip()
        if key and abstract:
            abstract_map[key] = abstract
    return abstract_map, source_map


def write_report_csv(
    path: Path,
    records: dict[str, LookupRecord],
    resolutions: dict[str, Resolution],
    group: str,
    write_header: bool,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "w" if write_header else "a"
    with path.open(mode, encoding="utf-8", newline="") as handle:
        fieldnames = ["group", "record_id", "title", "venue", "doi", "url", "status", "source", "note"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        for record_id in sorted(records):
            record = records[record_id]
            resolution = resolutions.get(record_id, Resolution("", "", "missing", ""))
            writer.writerow(
                {
                    "group": group,
                    "record_id": record.record_id,
                    "title": record.title,
                    "venue": record.venue,
                    "doi": record.doi,
                    "url": record.url,
                    "status": resolution.status,
                    "source": resolution.source,
                    "note": resolution.note,
                }
            )


def write_report_md(
    path: Path,
    candidate_before: int,
    candidate_after: int,
    fresh_before: int,
    fresh_after: int,
    candidate_resolutions: dict[str, Resolution],
    fresh_resolutions: dict[str, Resolution],
    candidate_records: dict[str, LookupRecord],
    fresh_records: dict[str, LookupRecord],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    candidate_counter = Counter(res.status for res in candidate_resolutions.values())
    fresh_counter = Counter(res.status for res in fresh_resolutions.values())
    candidate_unresolved = [candidate_records[key].title for key, res in candidate_resolutions.items() if not res.abstract]
    fresh_unresolved = [fresh_records[key].title for key, res in fresh_resolutions.items() if not res.abstract]

    lines = [
        "# Phase 1 Missing Abstract Backfill",
        "",
        "Date: 2026-04-28",
        "",
        "## Candidate Pool",
        "",
        f"- Missing before: `{candidate_before}`",
        f"- Missing after: `{candidate_after}`",
        f"- Resolution breakdown: `{dict(candidate_counter)}`",
        "",
        "## Fresh L4 Screen",
        "",
        f"- Missing before: `{fresh_before}`",
        f"- Missing after: `{fresh_after}`",
        f"- Resolution breakdown: `{dict(fresh_counter)}`",
        "",
        "## Remaining Unresolved",
        "",
    ]

    if not candidate_unresolved and not fresh_unresolved:
        lines.append("- None.")
    else:
        for title in candidate_unresolved:
            lines.append(f"- candidate_pool: {title}")
        for title in fresh_unresolved:
            lines.append(f"- fresh_l4: {title}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def count_missing(rows: list[dict[str, str]]) -> int:
    return sum(1 for row in rows if not str(row.get("abstract") or "").strip())


def main() -> int:
    args = parse_args()

    candidate_fields, candidate_rows = read_csv(args.candidate_pool)
    papers_master_fields, papers_master_rows = read_csv(args.papers_master)
    papers_master_raw_fields, papers_master_raw_rows = read_csv(args.papers_master_raw)
    manual_fields, manual_rows = read_csv(args.manual_review)
    rereview_fields, rereview_rows = read_csv(args.abstract_rereview)
    fresh_fields, fresh_rows = read_csv(args.fresh_abstracts)
    fresh_disposition_fields, fresh_disposition_rows = read_csv(args.fresh_disposition)
    translation_payload = read_json(args.translation_input)

    candidate_before = count_missing(candidate_rows)
    fresh_before = count_missing(fresh_rows)

    resolver = AbstractResolver(timeout=args.timeout)

    candidate_records = build_lookup_records(candidate_rows, "paper_id")
    fresh_records = build_lookup_records(fresh_rows, "fresh_id")

    candidate_resolutions = resolve_missing(candidate_rows, "paper_id", resolver, args.workers)
    fresh_resolutions = resolve_missing(fresh_rows, "fresh_id", resolver, args.workers)

    apply_candidate_backfill(candidate_rows, "paper_id", candidate_resolutions)
    apply_candidate_backfill(papers_master_rows, "paper_id", candidate_resolutions)
    apply_candidate_backfill(papers_master_raw_rows, "paper_id", candidate_resolutions)

    candidate_abstracts = {
        str(row.get("paper_id") or "").strip(): str(row.get("abstract") or "").strip()
        for row in candidate_rows
        if str(row.get("paper_id") or "").strip() and str(row.get("abstract") or "").strip()
    }
    candidate_sources = {
        record_id: resolution.source
        for record_id, resolution in candidate_resolutions.items()
        if resolution.abstract and resolution.source
    }

    apply_review_sheet_sync(manual_rows, candidate_abstracts, candidate_sources)
    apply_review_sheet_sync(rereview_rows, candidate_abstracts, candidate_sources)
    apply_translation_input_sync(translation_payload, candidate_abstracts)

    update_fresh_abstract_status(fresh_rows, fresh_resolutions)
    update_fresh_abstract_status(fresh_disposition_rows, fresh_resolutions)

    candidate_after = count_missing(candidate_rows)
    fresh_after = count_missing(fresh_rows)

    write_csv(args.candidate_pool, candidate_fields, candidate_rows)
    write_csv(args.papers_master, papers_master_fields, papers_master_rows)
    write_csv(args.papers_master_raw, papers_master_raw_fields, papers_master_raw_rows)
    write_csv(args.manual_review, manual_fields, manual_rows)
    write_csv(args.abstract_rereview, rereview_fields, rereview_rows)
    write_csv(args.fresh_abstracts, fresh_fields, fresh_rows)
    write_csv(args.fresh_disposition, fresh_disposition_fields, fresh_disposition_rows)
    write_json(args.translation_input, translation_payload)

    write_report_csv(args.report_csv, candidate_records, candidate_resolutions, "candidate_pool", True)
    write_report_csv(args.report_csv, fresh_records, fresh_resolutions, "fresh_l4", False)
    write_report_md(
        args.report_md,
        candidate_before,
        candidate_after,
        fresh_before,
        fresh_after,
        candidate_resolutions,
        fresh_resolutions,
        candidate_records,
        fresh_records,
    )

    print(
        json.dumps(
            {
                "candidate_missing_before": candidate_before,
                "candidate_missing_after": candidate_after,
                "fresh_missing_before": fresh_before,
                "fresh_missing_after": fresh_after,
                "candidate_resolution_status": Counter(res.status for res in candidate_resolutions.values()),
                "fresh_resolution_status": Counter(res.status for res in fresh_resolutions.values()),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
