#!/usr/bin/env python3
"""Build and audit CityIntent's paper bibliography from first-party metadata."""

from __future__ import annotations

import datetime as dt
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / "assets/papers/metadata/reference_index.md"
OUTPUT = ROOT / "paper/references.bib"
AUDIT = ROOT / "paper/REFERENCE_AUDIT.md"

ARXIV_API = "https://export.arxiv.org/api/query"
CROSSREF_API = "https://api.crossref.org/works/{}"
ATOM = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}

EXTRA_ARXIV_IDS: set[str] = set()

DOIS = {
    "10.1109/TAI.2025.3566362": "validation survey",
    "10.1016/j.simpat.2025.103234": "urban mobility framework",
    "10.3233/ATDE251076": "multi-stakeholder urban planning",
    "10.1007/s10462-025-11412-6": "generative simulation validation",
    "10.1145/3805689.3812388": "mechanism plausibility",
}

ARXIV_OVERRIDES = {
    # arXiv Atom currently splits "Zheshen (Jessie) Wang" into two author nodes.
    "2503.20749": {
        "author": "Yuxuan Lu and Jing Huang and Yan Han and Bingsheng Yao and Sisong Bei and Jiri Gesi and Yaochen Xie and Yisi Sang and Zheshen (Jessie) Wang and Qi He and Dakuo Wang",
    },
    # Correct an isolated capitalization typo in the current Atom title.
    "2409.09040": {
        "title": "ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban Mobility",
    },
}

MANUAL = [
    {
        "type": "inproceedings",
        "key": "zhou2024sotopia",
        "title": "SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents",
        "author": "Xuhui Zhou and Hao Zhu and Leena Mathur and Ruohong Zhang and Zhengyang Qi and Haofei Yu and Louis-Philippe Morency and Yonatan Bisk and Daniel Fried and Graham Neubig and Maarten Sap",
        "booktitle": "International Conference on Learning Representations",
        "year": "2024",
        "url": "https://openreview.net/forum?id=mM7VurbA4r",
        "eprint": "2310.11667",
        "archiveprefix": "arXiv",
    },
    {
        "type": "misc",
        "key": "anonymous2026mobisimbench",
        "title": "MobiSim-Bench: A Multi-Perspective Benchmark for Evaluating LLM-Agent-Based Human Mobility Simulation",
        "author": "{Anonymous authors}",
        "year": "2026",
        "howpublished": "ICLR 2026 submission",
        "url": "https://openreview.net/forum?id=3QFvAXuNl7",
        "note": "Author list was not public in the archived double-blind manuscript; replace after de-anonymization",
    },
]

STOPWORDS = {
    "a", "an", "and", "as", "at", "for", "from", "in", "into", "is", "of",
    "on", "the", "through", "to", "towards", "using", "with",
}


def fetch_json(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "CityIntent bibliography audit/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response)


def fetch_arxiv(ids: list[str]) -> list[dict]:
    query = urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": 100})
    request = urllib.request.Request(f"{ARXIV_API}?{query}", headers={"User-Agent": "CityIntent bibliography audit/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        root = ET.parse(response).getroot()

    records = []
    for entry in root.findall("a:entry", ATOM):
        arxiv_url = entry.findtext("a:id", namespaces=ATOM) or ""
        arxiv_id = re.search(r"(\d{4}\.\d{4,5})", arxiv_url).group(1)
        authors = [node.findtext("a:name", namespaces=ATOM) for node in entry.findall("a:author", ATOM)]
        comment = entry.findtext("x:comment", namespaces=ATOM)
        journal_ref = entry.findtext("x:journal_ref", namespaces=ATOM)
        doi = entry.findtext("x:doi", namespaces=ATOM)
        record = {
                "type": "misc",
                "title": clean_space(entry.findtext("a:title", namespaces=ATOM) or ""),
                "author": " and ".join(author for author in authors if author),
                "year": (entry.findtext("a:published", namespaces=ATOM) or "")[:4],
                "eprint": arxiv_id,
                "archiveprefix": "arXiv",
                "primaryclass": (entry.find("x:primary_category", ATOM).attrib.get("term") if entry.find("x:primary_category", ATOM) is not None else None),
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "doi": doi,
                "note": journal_ref or comment,
            }
        record.update(ARXIV_OVERRIDES.get(arxiv_id, {}))
        records.append(record)
    return records


def fetch_crossref(doi: str) -> dict:
    item = fetch_json(CROSSREF_API.format(urllib.parse.quote(doi, safe="")))["message"]
    authors = []
    for author in item.get("author", []):
        name = " ".join(part for part in (author.get("given"), author.get("family")) if part)
        if name:
            authors.append(name)
    date_parts = (item.get("published-print") or item.get("published-online") or item.get("published") or {}).get("date-parts", [[None]])
    crossref_type = item.get("type")
    record_type = {
        "journal-article": "article",
        "proceedings-article": "inproceedings",
    }.get(crossref_type, "incollection")
    record = {
        "type": record_type,
        "title": clean_space((item.get("title") or [""])[0]),
        "author": " and ".join(authors),
        "year": str(date_parts[0][0]),
        "doi": item.get("DOI", doi),
        "url": item.get("URL") or f"https://doi.org/{doi}",
        "publisher": item.get("publisher"),
    }
    containers = item.get("container-title") or []
    if record_type == "article":
        record.update(
            {
                "journal": containers[0] if containers else None,
                "volume": item.get("volume"),
                "number": item.get("issue"),
                "pages": item.get("page"),
            }
        )
    else:
        record["booktitle"] = containers[-1] if containers else None
    return record


def clean_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().lstrip("\ufeff")


def bib_escape(value: str) -> str:
    return value.replace("&", r"\&").replace("%", r"\%").replace("#", r"\#")


def family_name(author_field: str) -> str:
    first = author_field.split(" and ", 1)[0].strip("{} ")
    return re.sub(r"[^A-Za-z0-9]", "", first.split()[-1]).lower() or "unknown"


def title_slug(title: str) -> str:
    prefix = title.split(":", 1)[0]
    words = re.findall(r"[A-Za-z0-9]+", prefix)
    kept = [word.lower() for word in words if word.lower() not in STOPWORDS]
    return "".join(kept[:3])[:36] or "work"


def assign_keys(records: list[dict]) -> None:
    used = {record["key"] for record in records if record.get("key")}
    for record in records:
        if record.get("key"):
            continue
        base = f"{family_name(record['author'])}{record['year']}{title_slug(record['title'])}"
        key = base
        suffix = ord("a")
        while key in used:
            key = f"{base}{chr(suffix)}"
            suffix += 1
        record["key"] = key
        used.add(key)


def render_bib(records: list[dict]) -> str:
    field_order = [
        "title", "author", "booktitle", "journal", "year", "volume", "number", "pages",
        "publisher", "doi", "eprint", "archiveprefix", "primaryclass", "howpublished", "url", "note",
    ]
    blocks = [
        "% Generated from arXiv, Crossref, and first-party conference records.",
        f"% Last verified: {dt.date.today().isoformat()}",
        "% See REFERENCE_AUDIT.md before citing entries marked as provisional.",
        "",
    ]
    for record in sorted(records, key=lambda item: item["key"]):
        lines = [f"@{record['type']}{{{record['key']},"]
        for field in field_order:
            value = record.get(field)
            if value:
                lines.append(f"  {field} = {{{bib_escape(str(value))}}},")
        lines.append("}")
        blocks.append("\n".join(lines))
        blocks.append("")
    return "\n".join(blocks)


def normalized_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]", "", title.lower())


def index_titles(text: str) -> list[str]:
    titles = []
    for line in text.splitlines():
        if line.startswith("| ") and " | [" in line:
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) >= 3 and cells[1] != "Paper":
                titles.append(cells[1])
    return titles


def render_audit(records: list[dict], indexed_titles: list[str]) -> str:
    known = {normalized_title(record["title"]): record for record in records}
    unmatched = [title for title in indexed_titles if normalized_title(title) not in known]
    check_suggested = 2
    arxiv_count = sum(1 for record in records if record.get("archiveprefix") == "arXiv" and record["key"] != "zhou2024sotopia")
    doi_count = sum(1 for record in records if record.get("doi") and not record.get("eprint"))
    lines = [
        "# Reference Audit",
        "",
        f"Last verified: {dt.date.today().isoformat()}",
        "",
        "## Summary",
        "",
        f"- Total unique BibTeX records: **{len(records)}**",
        f"- Verified against arXiv API metadata: **{arxiv_count}**",
        f"- Verified against Crossref DOI metadata: **{doi_count}**",
        "- Verified against ICLR/OpenReview plus the archived first page: **1** (SOTOPIA)",
        f"- Check suggested: **{check_suggested}**",
        f"- Index titles without a metadata match: **{len(unmatched)}**",
        "",
        "## Critical Correction",
        "",
        "The old reference index described DOI `10.1016/j.simpat.2025.103234` as the published version of GATSim. Crossref and OpenAlex identify that DOI as *Generative agents for urban mobility: A cognitive framework for realistic travel behavior simulation* by Qi Liu, Can Li, and Wanjing Ma. The bibliography therefore keeps GATSim and this journal article as distinct works.",
        "",
        "## Check Suggested",
        "",
        "| Key | Issue | Required action |",
        "|---|---|---|",
        "| `anonymous2026mobisimbench` | The archived ICLR 2026 submission is double-blind and lists anonymous authors. | Replace the author field when OpenReview exposes the final author list; do not use this entry in a camera-ready manuscript before then. |",
        "| `liu2026generativeagentsurban` | Crossref assigns the volume/issue to 2026, while the DOI was registered in 2025 and OpenAlex labels the work 2025. | Keep 2026 for the issue citation; recheck the publisher export at submission time if the target style uses online-first year. |",
        "",
        "## Scope Notes",
        "",
        "- arXiv entries use the first-submission year and current arXiv title/author order. Venue claims embedded in free-text comments were not promoted to publication fields without a DOI or first-party proceedings record.",
        "- Crossref entries use registered title, author order, publication container, volume/issue/pages when supplied by the publisher.",
        "- SOTOPIA uses its ICLR 2024 record and archived paper author order; its arXiv identifier is included for retrieval.",
        "- The archived PDF was used to repair an arXiv Atom author-splitting error for `lu2025canllmagents` and a capitalization typo for ChatSUMO.",
        "- The bibliography includes the two validation papers omitted from the older index table: *Validation is the central challenge...* and the FAccT 2026 paper *Mechanism Plausibility in Generative Agent-Based Modeling*.",
    ]
    if unmatched:
        lines.extend(["", "## Unmatched Index Titles", ""] + [f"- {title}" for title in unmatched])
    lines.extend(["", "## Record Inventory", "", "| Key | Year | Verification source | Title |", "|---|---:|---|---|"])
    for record in sorted(records, key=lambda item: (item["year"], item["key"])):
        if record["key"] == "anonymous2026mobisimbench":
            source = "Archived OpenReview PDF (provisional)"
        elif record["key"] == "zhou2024sotopia":
            source = "ICLR/OpenReview + arXiv"
        elif record.get("doi") and not record.get("eprint"):
            source = "Crossref DOI"
        else:
            source = "arXiv API"
        lines.append(f"| `{record['key']}` | {record['year']} | {source} | {record['title']} |")
    return "\n".join(lines) + "\n"


def main() -> None:
    index_text = INDEX.read_text(encoding="utf-8-sig")
    arxiv_ids = set(re.findall(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", index_text))
    arxiv_ids.update(EXTRA_ARXIV_IDS)
    records = fetch_arxiv(sorted(arxiv_ids))
    for doi in DOIS:
        records.append(fetch_crossref(doi))
    records.extend(MANUAL)
    assign_keys(records)

    normalized = [normalized_title(record["title"]) for record in records]
    if len(normalized) != len(set(normalized)):
        raise RuntimeError("Duplicate normalized titles detected")
    if len(records) != 48:
        raise RuntimeError(f"Expected 48 unique records, found {len(records)}")

    OUTPUT.write_text(render_bib(records), encoding="utf-8")
    AUDIT.write_text(render_audit(records, index_titles(index_text)), encoding="utf-8")
    print(f"Wrote {len(records)} records to {OUTPUT}")
    print(f"Wrote audit to {AUDIT}")


if __name__ == "__main__":
    main()
