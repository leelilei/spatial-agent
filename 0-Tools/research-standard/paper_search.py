#!/usr/bin/env python3
"""Dependency-free first-pass paper search for research projects.

The script queries arXiv and Crossref metadata, deduplicates by DOI/title, and
writes a compact Markdown or JSON candidate table. It is intentionally modest:
final related-work notes should still verify claims against papers directly.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


@dataclass
class PaperHit:
    source: str
    query: str
    title: str
    year: str
    authors: str
    venue: str
    url: str
    doi: str
    summary: str


def normalize_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title).strip().lower()
    title = re.sub(r"[^a-z0-9 ]+", "", title)
    return title


def clean_text(text: str | None) -> str:
    if not text:
        return ""
    return re.sub(r"\s+", " ", text).strip()


def fetch_json(url: str, timeout: int) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "research-standard-paper-search/0.1 "
            "(mailto:research@example.local)"
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def fetch_xml(url: str, timeout: int) -> ET.Element:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "research-standard-paper-search/0.1"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return ET.fromstring(response.read())


def search_arxiv(query: str, max_results: int, timeout: int) -> list[PaperHit]:
    encoded = urllib.parse.urlencode(
        {
            "search_query": f"all:{query}",
            "start": 0,
            "max_results": max_results,
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
    )
    url = f"https://export.arxiv.org/api/query?{encoded}"
    root = fetch_xml(url, timeout)
    hits: list[PaperHit] = []
    for entry in root.findall("atom:entry", ARXIV_NS):
        title = clean_text(entry.findtext("atom:title", namespaces=ARXIV_NS))
        published = clean_text(entry.findtext("atom:published", namespaces=ARXIV_NS))
        year = published[:4] if published else ""
        authors = ", ".join(
            clean_text(author.findtext("atom:name", namespaces=ARXIV_NS))
            for author in entry.findall("atom:author", ARXIV_NS)
        )
        link = clean_text(entry.findtext("atom:id", namespaces=ARXIV_NS))
        summary = clean_text(entry.findtext("atom:summary", namespaces=ARXIV_NS))
        doi = ""
        for child in entry:
            if child.tag.endswith("doi") and child.text:
                doi = clean_text(child.text)
                break
        hits.append(
            PaperHit(
                source="arXiv",
                query=query,
                title=title,
                year=year,
                authors=authors,
                venue="arXiv",
                url=link,
                doi=doi,
                summary=summary,
            )
        )
    return hits


def crossref_year(item: dict) -> str:
    for key in ("published-print", "published-online", "published", "created"):
        parts = item.get(key, {}).get("date-parts")
        if parts and parts[0]:
            return str(parts[0][0])
    return ""


def crossref_authors(item: dict, limit: int = 6) -> str:
    names = []
    for author in item.get("author", [])[:limit]:
        given = author.get("given", "")
        family = author.get("family", "")
        names.append(clean_text(f"{given} {family}"))
    if len(item.get("author", [])) > limit:
        names.append("et al.")
    return ", ".join(name for name in names if name)


def search_crossref(query: str, max_results: int, timeout: int) -> list[PaperHit]:
    params = urllib.parse.urlencode(
        {
            "query.bibliographic": query,
            "rows": max_results,
            "select": "title,author,published-print,published-online,published,created,DOI,URL,type,container-title,is-referenced-by-count",
        }
    )
    url = f"https://api.crossref.org/works?{params}"
    data = fetch_json(url, timeout)
    hits: list[PaperHit] = []
    for item in data.get("message", {}).get("items", []):
        titles = item.get("title") or []
        title = clean_text(titles[0] if titles else "")
        if not title:
            continue
        venues = item.get("container-title") or []
        hits.append(
            PaperHit(
                source="Crossref",
                query=query,
                title=title,
                year=crossref_year(item),
                authors=crossref_authors(item),
                venue=clean_text(venues[0] if venues else item.get("type", "")),
                url=clean_text(item.get("URL", "")),
                doi=clean_text(item.get("DOI", "")),
                summary="",
            )
        )
    return hits


def dedupe_hits(hits: Iterable[PaperHit]) -> list[PaperHit]:
    seen: set[str] = set()
    unique: list[PaperHit] = []
    for hit in hits:
        key = hit.doi.lower() if hit.doi else normalize_title(hit.title)
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(hit)
    return unique


def load_queries(args: argparse.Namespace) -> list[str]:
    queries = list(args.query or [])
    if args.queries_file:
        path = Path(args.queries_file)
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                queries.append(line)
    return queries


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_markdown(path: Path, hits: list[PaperHit], queries: list[str]) -> None:
    lines = [
        "# Paper Search Raw Results",
        "",
        "Generated by `0-Tools/research-standard/paper_search.py`.",
        "",
        "## Queries",
        "",
    ]
    lines.extend(f"- {query}" for query in queries)
    lines.extend(
        [
            "",
            "## Candidate Papers",
            "",
            "| Source | Year | Title | Authors | Venue | Query | Link |",
            "|---|---:|---|---|---|---|---|",
        ]
    )
    for hit in hits:
        title = markdown_escape(hit.title)
        authors = markdown_escape(hit.authors)
        venue = markdown_escape(hit.venue)
        query = markdown_escape(hit.query)
        link = f"[link]({hit.url})" if hit.url else ""
        lines.append(
            f"| {hit.source} | {hit.year} | {title} | {authors} | {venue} | {query} | {link} |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_json(path: Path, hits: list[PaperHit]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([asdict(hit) for hit in hits], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", action="append", help="Search query. Can repeat.")
    parser.add_argument("--queries-file", help="Plain text file with one query per line.")
    parser.add_argument("--max-results", type=int, default=8)
    parser.add_argument(
        "--sources",
        default="arxiv,crossref",
        help="Comma-separated sources: arxiv,crossref",
    )
    parser.add_argument("--out", required=True, help="Output .md or .json path.")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--sleep", type=float, default=1.0)
    args = parser.parse_args()

    queries = load_queries(args)
    if not queries:
        parser.error("provide at least one --query or --queries-file entry")

    sources = {source.strip().lower() for source in args.sources.split(",") if source.strip()}
    all_hits: list[PaperHit] = []
    for query in queries:
        if "arxiv" in sources:
            all_hits.extend(search_arxiv(query, args.max_results, args.timeout))
            time.sleep(args.sleep)
        if "crossref" in sources:
            all_hits.extend(search_crossref(query, args.max_results, args.timeout))
            time.sleep(args.sleep)

    hits = dedupe_hits(all_hits)
    out = Path(args.out)
    if out.suffix.lower() == ".json":
        write_json(out, hits)
    else:
        write_markdown(out, hits, queries)
    print(f"Wrote {len(hits)} unique hits to {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

