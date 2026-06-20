#!/usr/bin/env python3
"""Download open-access PDFs for titles mentioned in reference-report.md.

Sources are intentionally conservative:
- arXiv API title search
- Semantic Scholar openAccessPdf

The script does not bypass paywalls. It writes a JSON manifest and a Markdown summary so
the reference collection can continue manually for missing or paywalled items.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import http.cookiejar
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REPORT = ROOT / "assets" / "papers" / "metadata" / "reference-report.md"
OUT_DIR = ROOT / "assets" / "papers" / "pdf"
MANIFEST = ROOT / "assets" / "papers" / "metadata" / "pdf_download_manifest.json"
SUMMARY = ROOT / "assets" / "papers" / "metadata" / "pdf_download_summary.md"

HEADERS = {
    "User-Agent": "Mozilla/5.0 TelephoneResearchPDFCollector/0.1 (open-access literature collection)"
}

COOKIE_JAR = http.cookiejar.CookieJar()
OPENER = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(COOKIE_JAR))

MANUAL_ARXIV = {
    "generative agents": "2304.03442",
    "generative agents interactive simulacra of human behavior": "2304.03442",
    "camel communicative agents for mind exploration of llm society": "2303.17760",
    "autogen enabling next gen llm applications via multi agent conversation": "2308.08155",
    "agentverse facilitating multi agent collaboration and exploring emergent behaviors in agents": "2308.10848",
    "metagpt meta programming for a multi agent collaborative framework": "2308.00352",
    "chatdev communicative agents for software development": "2307.07924",
    "sotopia interactive evaluation for social intelligence in language agents": "2310.11667",
    "improving factuality and reasoning through multiagent debate": "2305.14325",
    "improving factuality and reasoning in language models through multiagent debate": "2305.14325",
    "truthfulqa measuring how models mimic human falsehoods": "2109.07958",
    "truthfulqa": "2109.07958",
    "selfcheckgpt": "2303.08896",
    "halu eval": "2305.11747",
    "halueval": "2305.11747",
    "memgpt": "2310.08560",
    "reflexion": "2303.11366",
    "react": "2210.03629",
    "voyager": "2305.16291",
    "a mem": "2502.12110",
    "a mem agentic memory for llm agents": "2502.12110",
    "agent hospital": "2405.02957",
    "agent hospital a simulacrum of hospital with evolvable medical agents": "2405.02957",
    "ai models collapse when trained on recursively generated data": "2305.17493",
    "the curse of recursion": "2305.17493",
    "self consuming generative models go mad": "2307.01850",
    "how bad is training on synthetic data": "2404.05090",
    "how bad is training on synthetic data a statistical analysis of language model collapse": "2404.05090",
    "trustworthy llm mediated communication laac": "2511.04184",
    "trustworthy llm mediated communication evaluating information fidelity in llm as a communicator laac framework in multiple application domains": "2511.04184",
    "artificial hivemind": "2510.22954",
    "artificial hivemind the open ended homogeneity of language models and beyond": "2510.22954",
}

MANUAL_PDF_URLS = {
    "detecting hallucinations in large language models using semantic entropy": (
        "https://www.nature.com/articles/s41586-024-07421-0.pdf",
        "Nature:10.1038/s41586-024-07421-0",
    ),
    "can corrections spread misinformation to new audiences": (
        "https://cognitiveresearchjournal.springeropen.com/counter/pdf/10.1186/s41235-020-00241-6.pdf",
        "SpringerOpen:10.1186/s41235-020-00241-6",
    ),
    "cumulative cultural evolution in the laboratory": (
        "https://www.pnas.org/doi/pdf/10.1073/pnas.0802861105",
        "PNAS:10.1073/pnas.0802861105",
    ),
}

CATEGORY_BY_INDEX = {
    1: "01_agent_societies",
    11: "01_agent_societies",
    12: "01_agent_societies",
    13: "01_agent_societies",
    14: "01_agent_societies",
    15: "01_agent_societies",
    16: "01_agent_societies",
    17: "01_agent_societies",
    18: "01_agent_societies",
    19: "01_agent_societies",
    3: "02_debate_consensus",
    4: "02_debate_consensus",
    20: "02_debate_consensus",
    21: "02_debate_consensus",
    22: "02_debate_consensus",
    23: "02_debate_consensus",
    24: "02_debate_consensus",
    25: "02_debate_consensus",
    26: "02_debate_consensus",
    27: "02_debate_consensus",
    28: "02_debate_consensus",
    5: "03_hallucination_factuality",
    29: "03_hallucination_factuality",
    30: "03_hallucination_factuality",
    31: "03_hallucination_factuality",
    32: "03_hallucination_factuality",
    33: "03_hallucination_factuality",
    34: "03_hallucination_factuality",
    35: "03_hallucination_factuality",
    36: "03_hallucination_factuality",
    37: "03_hallucination_factuality",
    38: "03_hallucination_factuality",
    39: "03_hallucination_factuality",
    40: "03_hallucination_factuality",
    41: "03_hallucination_factuality",
    42: "04_memory_state_agents",
    43: "04_memory_state_agents",
    44: "04_memory_state_agents",
    45: "04_memory_state_agents",
    46: "04_memory_state_agents",
    47: "04_memory_state_agents",
    48: "04_memory_state_agents",
    49: "04_memory_state_agents",
    2: "05_misinformation_correction",
    50: "05_misinformation_correction",
    51: "05_misinformation_correction",
    53: "05_misinformation_correction",
    54: "05_misinformation_correction",
    55: "05_misinformation_correction",
    61: "05_misinformation_correction",
    66: "06_transmission_culture",
    67: "06_transmission_culture",
    9: "07_model_collapse_homogeneity",
    10: "07_model_collapse_homogeneity",
    68: "07_model_collapse_homogeneity",
    69: "07_model_collapse_homogeneity",
    70: "07_model_collapse_homogeneity",
    71: "07_model_collapse_homogeneity",
}


def normalize(text: str) -> str:
    text = text.lower()
    text = text.replace("llm’s", "llms").replace("it's", "its")
    text = re.sub(r"[\u2018\u2019\u201c\u201d]", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def slugify(text: str, max_len: int = 88) -> str:
    text = normalize(text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"[^a-z0-9\-\u4e00-\u9fff]", "", text)
    return text[:max_len].strip("-") or hashlib.sha1(text.encode()).hexdigest()[:12]


def pdf_path_for(title: str, index: int, out_dir: Path) -> Path:
    category = CATEGORY_BY_INDEX.get(index, "99_uncategorized")
    return out_dir / category / f"{index:02d}_{slugify(title)}.pdf"


def extract_titles(report: Path) -> list[str]:
    titles: list[str] = []
    seen: set[str] = set()
    for line in report.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if not cols:
            continue
        title = re.sub(r"\ue200.*?\ue201", "", cols[0]).strip()
        if title in {"论文", "文献", "来源"} or title.startswith("<"):
            continue
        key = normalize(title)
        if len(key) < 4 or key in seen:
            continue
        seen.add(key)
        titles.append(title)
    return titles


def http_get(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with OPENER.open(req, timeout=timeout) as resp:
        return resp.read()


def close_enough(a: str, b: str) -> bool:
    an, bn = normalize(a), normalize(b)
    if not an or not bn:
        return False
    if an == bn or an in bn or bn in an:
        return True
    return difflib.SequenceMatcher(None, an, bn).ratio() >= 0.82


def arxiv_pdf_url(title: str) -> tuple[str | None, str | None]:
    key = normalize(title)
    if key in MANUAL_ARXIV:
        arxiv_id = MANUAL_ARXIV[key]
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf", f"arXiv:{arxiv_id}"

    query = urllib.parse.urlencode({
        "search_query": f'ti:"{title}"',
        "start": "0",
        "max_results": "3",
    })
    url = f"https://export.arxiv.org/api/query?{query}"
    try:
        raw = http_get(url, timeout=20)
    except Exception:
        return None, None

    ns = {"a": "http://www.w3.org/2005/Atom"}
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return None, None
    for entry in root.findall("a:entry", ns):
        found_title = "".join(entry.findtext("a:title", default="", namespaces=ns).split())
        if not close_enough(title, found_title):
            continue
        entry_id = entry.findtext("a:id", default="", namespaces=ns)
        arxiv_id = entry_id.rsplit("/", 1)[-1]
        return f"https://arxiv.org/pdf/{arxiv_id}.pdf", f"arXiv:{arxiv_id}"
    return None, None


def manual_pdf_url(title: str) -> tuple[str | None, str | None]:
    return MANUAL_PDF_URLS.get(normalize(title), (None, None))


def semantic_scholar_pdf_url(title: str) -> tuple[str | None, str | None]:
    params = urllib.parse.urlencode({
        "query": title,
        "limit": "5",
        "fields": "title,year,openAccessPdf,externalIds,url",
    })
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?{params}"
    try:
        data = json.loads(http_get(url, timeout=25).decode("utf-8"))
    except Exception:
        return None, None

    for paper in data.get("data", []):
        found_title = paper.get("title") or ""
        if not close_enough(title, found_title):
            continue
        oa = paper.get("openAccessPdf") or {}
        pdf_url = oa.get("url")
        if pdf_url:
            ids = paper.get("externalIds") or {}
            label = ids.get("ArXiv") or ids.get("DOI") or paper.get("url") or "SemanticScholar"
            return pdf_url, str(label)
    return None, None


def crossref_pdf_urls(title: str) -> list[tuple[str, str]]:
    params = urllib.parse.urlencode({
        "query.title": title,
        "rows": "5",
        "select": "title,DOI,link,URL",
    })
    url = f"https://api.crossref.org/works?{params}"
    try:
        data = json.loads(http_get(url, timeout=25).decode("utf-8"))
    except Exception:
        return []

    candidates: list[tuple[str, str]] = []
    for item in (data.get("message") or {}).get("items", []):
        found_title = " ".join(item.get("title") or [])
        if not close_enough(title, found_title):
            continue
        doi = item.get("DOI") or "Crossref"
        for link in item.get("link") or []:
            link_url = link.get("URL")
            content_type = (link.get("content-type") or "").lower()
            if link_url and ("pdf" in content_type or link_url.lower().endswith(".pdf")):
                candidates.append((link_url, str(doi)))
    return candidates


def openalex_pdf_urls(title: str) -> list[tuple[str, str]]:
    params = urllib.parse.urlencode({
        "search": title,
        "per-page": "5",
    })
    url = f"https://api.openalex.org/works?{params}"
    try:
        data = json.loads(http_get(url, timeout=25).decode("utf-8"))
    except Exception:
        return []

    candidates: list[tuple[str, str]] = []
    for item in data.get("results", []):
        found_title = item.get("title") or ""
        if not close_enough(title, found_title):
            continue
        label = (item.get("doi") or item.get("id") or "OpenAlex").replace("https://doi.org/", "")
        seen: set[str] = set()
        locations = []
        if item.get("primary_location"):
            locations.append(item["primary_location"])
        locations.extend(item.get("locations") or [])
        for location in locations:
            pdf_url = location.get("pdf_url")
            if pdf_url and pdf_url not in seen:
                seen.add(pdf_url)
                candidates.append((pdf_url, str(label)))
    return candidates


def is_pdf(raw: bytes) -> bool:
    head = raw[:1024].lstrip()
    return head.startswith(b"%PDF")


def normalize_pdf_url(url: str) -> str:
    if "arxiv.org/pdf/" in url and not url.lower().endswith(".pdf"):
        return f"{url}.pdf"
    return url


def download_one(title: str, index: int, out_dir: Path) -> dict:
    path = pdf_path_for(title, index, out_dir)
    if path.exists() and is_pdf(path.read_bytes()):
        return {
            "index": index,
            "title": title,
            "status": "downloaded",
            "source": "existing",
            "url": None,
            "path": str(path.relative_to(ROOT)),
            "note": f"{path.stat().st_size} bytes",
        }

    result = {
        "index": index,
        "title": title,
        "status": "not_found",
        "source": None,
        "url": None,
        "path": None,
        "note": "",
    }

    candidates = []
    manual_url, manual_label = manual_pdf_url(title)
    if manual_url:
        candidates.append((manual_url, manual_label or "manual"))

    arxiv_url, arxiv_label = arxiv_pdf_url(title)
    if arxiv_url:
        candidates.append((arxiv_url, arxiv_label or "arXiv"))

    s2_url, s2_label = semantic_scholar_pdf_url(title)
    if s2_url and s2_url not in {c[0] for c in candidates}:
        candidates.append((s2_url, s2_label or "SemanticScholar"))
    for cr_url, cr_label in crossref_pdf_urls(title):
        if cr_url not in {c[0] for c in candidates}:
            candidates.append((cr_url, cr_label or "Crossref"))
    for oa_url, oa_label in openalex_pdf_urls(title):
        if oa_url not in {c[0] for c in candidates}:
            candidates.append((oa_url, oa_label or "OpenAlex"))

    if not candidates:
        result["note"] = "No open PDF found via arXiv or Semantic Scholar."
        return result

    path.parent.mkdir(parents=True, exist_ok=True)
    for url, label in candidates:
        url = normalize_pdf_url(url)
        try:
            raw = http_get(url, timeout=60)
        except urllib.error.HTTPError as exc:
            result["note"] = f"HTTP error from {url}: {exc.code}"
            continue
        except Exception as exc:  # noqa: BLE001
            result["note"] = f"Download error from {url}: {exc}"
            continue
        if not is_pdf(raw):
            result["note"] = f"Downloaded content was not a PDF from {url}."
            continue
        path.write_bytes(raw)
        result.update({
            "status": "downloaded",
            "source": label,
            "url": url,
            "path": str(path.relative_to(ROOT)),
            "note": f"{len(raw)} bytes",
        })
        return result

    result["status"] = "failed"
    result["url"] = candidates[0][0]
    result["source"] = candidates[0][1]
    return result


def load_manifest() -> list[dict]:
    if not MANIFEST.exists():
        return []
    try:
        return json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError:
        return []


def write_manifest(results: list[dict]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")


def write_summary(results: list[dict]) -> None:
    lines = [
        "# PDF Download Summary",
        "",
        f"Total titles: {len(results)}",
        f"Downloaded: {sum(r['status'] == 'downloaded' for r in results)}",
        f"Missing/failed: {sum(r['status'] != 'downloaded' for r in results)}",
        "",
        "## Downloaded",
        "",
        "| # | Title | Source | Path |",
        "|---|---|---|---|",
    ]
    for r in results:
        if r["status"] == "downloaded":
            lines.append(f"| {r['index']} | {r['title']} | {r['source']} | `{r['path']}` |")
    lines.extend(["", "## Missing Or Failed", "", "| # | Title | Status | Note |", "|---|---|---|---|"])
    for r in results:
        if r["status"] != "downloaded":
            note = (r.get("note") or "").replace("|", "\\|")
            lines.append(f"| {r['index']} | {r['title']} | {r['status']} | {note} |")
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="download only first N titles")
    parser.add_argument("--sleep", type=float, default=0.7, help="delay between titles")
    parser.add_argument("--force", action="store_true", help="retry titles even if a manifest result exists")
    parser.add_argument("--force-missing", action="store_true", help="retry only manifest entries that are not downloaded")
    parser.add_argument("--indexes", default="", help="comma-separated 1-based title indexes to process")
    args = parser.parse_args()

    titles = extract_titles(REPORT)
    if args.limit:
        titles = titles[: args.limit]
    only_indexes = {
        int(part.strip())
        for part in args.indexes.split(",")
        if part.strip().isdigit()
    }

    existing = {r.get("index"): r for r in load_manifest()}
    results = [existing[i] for i in sorted(existing) if isinstance(i, int) and i <= len(titles)]
    for index, title in enumerate(titles, 1):
        if only_indexes and index not in only_indexes:
            continue
        if (
            not args.force
            and index in existing
            and not (args.force_missing and existing[index].get("status") != "downloaded")
        ):
            print(f"[{index}/{len(titles)}] {title}", flush=True)
            print(f"  -> skip {existing[index].get('status')} {existing[index].get('path') or existing[index].get('note')}", flush=True)
            continue
        print(f"[{index}/{len(titles)}] {title}", flush=True)
        res = download_one(title, index, OUT_DIR)
        print(f"  -> {res['status']} {res.get('path') or res.get('note')}", flush=True)
        existing[index] = res
        results = [existing[i] for i in sorted(existing) if isinstance(i, int) and i <= len(titles)]
        write_manifest(results)
        write_summary(results)
        time.sleep(args.sleep)

    results = [existing[i] for i in sorted(existing) if isinstance(i, int) and i <= len(titles)]
    write_manifest(results)
    write_summary(results)
    print(f"Wrote {MANIFEST}")
    print(f"Wrote {SUMMARY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
