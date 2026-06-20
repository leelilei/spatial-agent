#!/usr/bin/env python3
"""Resolve preferred citation sources for reference-report papers.

PDFs may be downloaded from arXiv, but citations should prefer the formal
journal/conference version when one exists. This script queries public metadata
APIs and writes a venue/DOI-first citation table.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "assets" / "papers" / "metadata" / "pdf_download_manifest.json"
OUT_JSON = ROOT / "assets" / "papers" / "metadata" / "citation_sources.json"
OUT_MD = ROOT / "assets" / "papers" / "metadata" / "citation_sources.md"

HEADERS = {
    "User-Agent": "TelephoneResearchCitationResolver/0.1 (mailto:local-research@example.invalid)"
}

FORMAL_DOI_PREFIXES = (
    "10.1145/",
    "10.18653/",
    "10.1038/",
    "10.1126/",
    "10.1073/",
    "10.1177/",
    "10.1037/",
    "10.1080/",
    "10.1609/",
    "10.1007/",
    "10.1140/",
    "10.1186/",
    "10.3389/",
)

MANUAL_OVERRIDES: dict[str, dict] = {
    "generative agents": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST 2023)",
        "doi": "10.1145/3586183.3606763",
        "year": 2023,
        "publisher_url": "https://doi.org/10.1145/3586183.3606763",
        "confidence": "manual",
    },
    "generative agents interactive simulacra of human behavior": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST 2023)",
        "doi": "10.1145/3586183.3606763",
        "year": 2023,
        "publisher_url": "https://doi.org/10.1145/3586183.3606763",
        "confidence": "manual",
    },
    "ai models collapse when trained on recursively generated data": {
        "preferred_source_type": "journal",
        "venue": "Nature",
        "doi": "10.1038/s41586-024-07566-y",
        "year": 2024,
        "publisher_url": "https://doi.org/10.1038/s41586-024-07566-y",
        "confidence": "manual",
    },
    "detecting hallucinations in large language models using semantic entropy": {
        "preferred_source_type": "journal",
        "venue": "Nature",
        "doi": "10.1038/s41586-024-07421-0",
        "year": 2024,
        "publisher_url": "https://doi.org/10.1038/s41586-024-07421-0",
        "confidence": "manual",
    },
    "the spread of true and false news online": {
        "preferred_source_type": "journal",
        "venue": "Science",
        "doi": "10.1126/science.aap9559",
        "year": 2018,
        "publisher_url": "https://doi.org/10.1126/science.aap9559",
        "confidence": "manual",
    },
    "the science of fake news": {
        "preferred_source_type": "journal",
        "venue": "Science",
        "doi": "10.1126/science.aao2998",
        "year": 2018,
        "publisher_url": "https://doi.org/10.1126/science.aao2998",
        "confidence": "manual",
    },
    "misinformation and its correction": {
        "preferred_source_type": "journal",
        "venue": "Psychological Science in the Public Interest",
        "doi": "10.1177/1529100612451018",
        "year": 2012,
        "publisher_url": "https://doi.org/10.1177/1529100612451018",
        "confidence": "manual",
    },
    "misinformation and its correction continued influence and successful debiasing": {
        "preferred_source_type": "journal",
        "venue": "Psychological Science in the Public Interest",
        "doi": "10.1177/1529100612451018",
        "year": 2012,
        "publisher_url": "https://doi.org/10.1177/1529100612451018",
        "confidence": "manual",
    },
    "sources of the continued influence effect": {
        "preferred_source_type": "journal",
        "venue": "Journal of Experimental Psychology: Learning, Memory, and Cognition",
        "doi": "10.1037/0278-7393.20.6.1420",
        "year": 1994,
        "publisher_url": "https://doi.org/10.1037/0278-7393.20.6.1420",
        "confidence": "manual",
    },
    "sources of the continued influence effect when misinformation in memory affects later inferences": {
        "preferred_source_type": "journal",
        "venue": "Journal of Experimental Psychology: Learning, Memory, and Cognition",
        "doi": "10.1037/0278-7393.20.6.1420",
        "year": 1994,
        "publisher_url": "https://doi.org/10.1037/0278-7393.20.6.1420",
        "confidence": "manual",
    },
    "debunking a meta analysis of the psychological efficacy of messages countering misinformation": {
        "preferred_source_type": "journal",
        "venue": "Psychological Science",
        "doi": "10.1177/0956797617714579",
        "year": 2017,
        "publisher_url": "https://doi.org/10.1177/0956797617714579",
        "confidence": "manual",
    },
    "cumulative cultural evolution in the laboratory": {
        "preferred_source_type": "journal",
        "venue": "Proceedings of the National Academy of Sciences",
        "doi": "10.1073/pnas.0802861105",
        "year": 2008,
        "publisher_url": "https://doi.org/10.1073/pnas.0802861105",
        "confidence": "manual",
    },
    "can corrections spread misinformation to new audiences": {
        "preferred_source_type": "journal",
        "venue": "Cognitive Research: Principles and Implications",
        "doi": "10.1186/s41235-020-00241-6",
        "year": 2020,
        "publisher_url": "https://doi.org/10.1186/s41235-020-00241-6",
        "confidence": "manual",
    },
    "truthfulqa": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics",
        "doi": "10.18653/v1/2022.acl-long.229",
        "year": 2022,
        "publisher_url": "https://doi.org/10.18653/v1/2022.acl-long.229",
        "confidence": "manual",
    },
    "truthfulqa measuring how models mimic human falsehoods": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics",
        "doi": "10.18653/v1/2022.acl-long.229",
        "year": 2022,
        "publisher_url": "https://doi.org/10.18653/v1/2022.acl-long.229",
        "confidence": "manual",
    },
    "just ask for calibration": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
        "doi": "10.18653/v1/2023.emnlp-main.330",
        "year": 2023,
        "publisher_url": "https://doi.org/10.18653/v1/2023.emnlp-main.330",
        "confidence": "manual",
    },
}

MANUAL_OVERRIDES.update({
    "simulating rumor spreading in social networks using llm agents": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2502.01450",
        "arxiv_id": "2502.01450",
        "confidence": "manual",
    },
    "improving factuality and reasoning through multiagent debate": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2305.14325",
        "arxiv_id": "2305.14325",
        "confidence": "manual",
    },
    "improving factuality and reasoning in language models through multiagent debate": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2305.14325",
        "arxiv_id": "2305.14325",
        "confidence": "manual",
    },
    "debate helps supervise unreliable experts": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2311.08702",
        "arxiv_id": "2311.08702",
        "confidence": "manual",
    },
    "artificial hivemind": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2510.22954",
        "arxiv_id": "2510.22954",
        "confidence": "manual",
    },
    "artificial hivemind the open ended homogeneity of language models and beyond": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2510.22954",
        "arxiv_id": "2510.22954",
        "confidence": "manual",
    },
    "camel communicative agents for mind exploration of llm society": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2303.17760",
        "arxiv_id": "2303.17760",
        "confidence": "manual",
    },
    "camel communicative agents for mind exploration of large language model society": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2303.17760",
        "arxiv_id": "2303.17760",
        "confidence": "manual",
    },
    "autogen enabling next gen llm applications via multi agent conversation": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2308.08155",
        "arxiv_id": "2308.08155",
        "confidence": "manual",
    },
    "agentverse facilitating multi agent collaboration and exploring emergent behaviors in agents": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2308.10848",
        "arxiv_id": "2308.10848",
        "confidence": "manual",
    },
    "metagpt meta programming for a multi agent collaborative framework": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2308.00352",
        "arxiv_id": "2308.00352",
        "confidence": "manual",
    },
    "chatdev communicative agents for software development": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics",
        "doi": "10.18653/v1/2024.acl-long.810",
        "year": 2024,
        "publisher_url": "https://doi.org/10.18653/v1/2024.acl-long.810",
        "confidence": "manual",
    },
    "agentscope a flexible yet robust multi agent platform": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2024,
        "publisher_url": "https://arxiv.org/abs/2402.14034",
        "arxiv_id": "2402.14034",
        "confidence": "manual",
    },
    "sotopia interactive evaluation for social intelligence in language agents": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2310.11667",
        "arxiv_id": "2310.11667",
        "confidence": "manual",
    },
    "prd peer rank and discussion improve llm based evaluations": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2307.02762",
        "arxiv_id": "2307.02762",
        "confidence": "manual",
    },
    "cortexdebate": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2507.03928",
        "arxiv_id": "2507.03928",
        "confidence": "manual",
    },
    "selene": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2024,
        "publisher_url": "https://arxiv.org/abs/2401.07663",
        "arxiv_id": "2401.07663",
        "confidence": "manual",
    },
    "debating with more persuasive llms leads to more truthful answers": {
        "preferred_source_type": "conference",
        "venue": "International Conference on Machine Learning (ICML 2024)",
        "doi": None,
        "year": 2024,
        "publisher_url": "https://proceedings.mlr.press/",
        "arxiv_id": "2402.06782",
        "confidence": "manual",
    },
    "selfcheckgpt": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
        "doi": "10.18653/v1/2023.emnlp-main.557",
        "year": 2023,
        "publisher_url": "https://doi.org/10.18653/v1/2023.emnlp-main.557",
        "arxiv_id": "2303.08896",
        "confidence": "manual",
    },
    "language models mostly know what they know": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2022,
        "publisher_url": "https://arxiv.org/abs/2207.05221",
        "arxiv_id": "2207.05221",
        "confidence": "manual",
    },
    "halueval": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
        "doi": "10.18653/v1/2023.emnlp-main.397",
        "year": 2023,
        "publisher_url": "https://doi.org/10.18653/v1/2023.emnlp-main.397",
        "arxiv_id": "2305.11747",
        "confidence": "manual",
    },
    "evaluating hallucinations in chinese large language models": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2310.03368",
        "arxiv_id": "2310.03368",
        "confidence": "manual",
    },
    "uhgeval": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics",
        "doi": "10.18653/v1/2024.acl-long.288",
        "year": 2024,
        "publisher_url": "https://doi.org/10.18653/v1/2024.acl-long.288",
        "arxiv_id": "2311.15296",
        "confidence": "manual",
    },
    "ragtruth": {
        "preferred_source_type": "conference",
        "venue": "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics",
        "doi": "10.18653/v1/2024.acl-long.585",
        "year": 2024,
        "publisher_url": "https://doi.org/10.18653/v1/2024.acl-long.585",
        "arxiv_id": "2401.00396",
        "confidence": "manual",
    },
    "the internal state of an llm knows when its lying": {
        "preferred_source_type": "conference",
        "venue": "Findings of the Association for Computational Linguistics: EMNLP 2023",
        "doi": "10.18653/v1/2023.findings-emnlp.68",
        "year": 2023,
        "publisher_url": "https://doi.org/10.18653/v1/2023.findings-emnlp.68",
        "arxiv_id": "2304.13734",
        "confidence": "manual",
    },
    "large language models cannot self correct reasoning yet": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2310.01798",
        "arxiv_id": "2310.01798",
        "confidence": "manual",
    },
    "delusions of large language models": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2503.06709",
        "arxiv_id": "2503.06709",
        "confidence": "manual",
    },
    "memgpt": {
        "preferred_source_type": "conference",
        "venue": "International Conference on Learning Representations (ICLR 2024)",
        "doi": None,
        "year": 2024,
        "publisher_url": "https://openreview.net/forum?id=0K6K9t25Yj",
        "arxiv_id": "2310.08560",
        "confidence": "manual",
    },
    "react": {
        "preferred_source_type": "conference",
        "venue": "International Conference on Learning Representations (ICLR 2023)",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://openreview.net/forum?id=WE_vluYUL-X",
        "arxiv_id": "2210.03629",
        "confidence": "manual",
    },
    "voyager": {
        "preferred_source_type": "journal",
        "venue": "Transactions on Machine Learning Research",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://openreview.net/forum?id=ehfRiF0R3a",
        "arxiv_id": "2305.16291",
        "confidence": "manual",
    },
    "a mem": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2502.12110",
        "arxiv_id": "2502.12110",
        "confidence": "manual",
    },
    "aios llm agent operating system": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2024,
        "publisher_url": "https://arxiv.org/abs/2403.16971",
        "arxiv_id": "2403.16971",
        "confidence": "manual",
    },
    "agent hospital": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2024,
        "publisher_url": "https://arxiv.org/abs/2405.02957",
        "arxiv_id": "2405.02957",
        "confidence": "manual",
    },
    "simulating misinformation propagation in social networks using large language models": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2511.10384",
        "arxiv_id": "2511.10384",
        "confidence": "manual",
    },
    "leveraging llms to detect influence campaigns in social media": {
        "preferred_source_type": "conference",
        "venue": "Companion Proceedings of the ACM Web Conference 2024",
        "doi": "10.1145/3589335.3651912",
        "year": 2024,
        "publisher_url": "https://doi.org/10.1145/3589335.3651912",
        "confidence": "manual",
    },
    "the curse of recursion": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2023,
        "publisher_url": "https://arxiv.org/abs/2305.17493",
        "arxiv_id": "2305.17493",
        "confidence": "manual",
    },
    "how bad is training on synthetic data": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2024,
        "publisher_url": "https://arxiv.org/abs/2404.05090",
        "arxiv_id": "2404.05090",
        "confidence": "manual",
    },
    "trustworthy llm mediated communication laac": {
        "preferred_source_type": "preprint_or_unresolved",
        "venue": "arXiv",
        "doi": None,
        "year": 2025,
        "publisher_url": "https://arxiv.org/abs/2511.04184",
        "arxiv_id": "2511.04184",
        "confidence": "manual",
    },
})


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[\u2018\u2019\u201c\u201d]", "", text)
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def close_enough(a: str, b: str) -> bool:
    an, bn = normalize(a), normalize(b)
    if not an or not bn:
        return False
    if an == bn or an in bn or bn in an:
        return True
    return difflib.SequenceMatcher(None, an, bn).ratio() >= 0.9


def http_json(url: str, timeout: int = 30) -> dict:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def clean_doi(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    value = value.replace("https://doi.org/", "").replace("http://dx.doi.org/", "")
    return value.lower()


def extract_arxiv(row: dict) -> str | None:
    for value in (row.get("source"), row.get("url")):
        if not value:
            continue
        match = re.search(r"arxiv[:/](?:pdf/)?([0-9]{4}\.[0-9]{4,5})(?:v[0-9]+)?", str(value), re.I)
        if match:
            return match.group(1)
    return None


def is_formal_doi(doi: str | None) -> bool:
    if not doi:
        return False
    doi = doi.lower()
    if doi.startswith("10.48550/"):
        return False
    return doi.startswith(FORMAL_DOI_PREFIXES) or not doi.startswith("10.48550/")


def source_type_from_crossref(item: dict) -> str:
    typ = item.get("type") or ""
    if "journal" in typ:
        return "journal"
    if "proceedings" in typ or "conference" in typ:
        return "conference"
    return typ or "unknown"


def query_crossref(title: str) -> dict | None:
    params = urllib.parse.urlencode({
        "query.title": title,
        "rows": "5",
        "select": "title,DOI,type,container-title,published-print,published-online,issued,URL",
    })
    data = http_json(f"https://api.crossref.org/works?{params}", timeout=25)
    best = None
    for item in (data.get("message") or {}).get("items", []):
        found_title = " ".join(item.get("title") or [])
        if not close_enough(title, found_title):
            continue
        doi = clean_doi(item.get("DOI"))
        container = " ".join(item.get("container-title") or [])
        if not doi:
            continue
        score = 2 if is_formal_doi(doi) else 0
        if container:
            score += 2
        if "arxiv" in doi:
            score -= 2
        candidate = {
            "source": "crossref",
            "matched_title": found_title,
            "doi": doi,
            "venue": container,
            "preferred_source_type": source_type_from_crossref(item),
            "publisher_url": item.get("URL") or f"https://doi.org/{doi}",
            "year": extract_year(item),
            "score": score,
            "confidence": "api",
        }
        if best is None or candidate["score"] > best["score"]:
            best = candidate
    return best


def extract_year(item: dict) -> int | None:
    for key in ("published-print", "published-online", "issued"):
        parts = ((item.get(key) or {}).get("date-parts") or [])
        if parts and parts[0]:
            return parts[0][0]
    return None


def query_openalex(title: str) -> dict | None:
    params = urllib.parse.urlencode({"search": title, "per-page": "5"})
    data = http_json(f"https://api.openalex.org/works?{params}", timeout=25)
    best = None
    for item in data.get("results", []):
        found_title = item.get("title") or ""
        if not close_enough(title, found_title):
            continue
        doi = clean_doi(item.get("doi"))
        primary = item.get("primary_location") or {}
        source = primary.get("source") or {}
        venue = source.get("display_name") or ""
        typ = item.get("type") or "unknown"
        score = 1
        if doi and is_formal_doi(doi):
            score += 2
        if venue:
            score += 2
        if doi and "10.48550" in doi:
            score -= 2
        candidate = {
            "source": "openalex",
            "matched_title": found_title,
            "doi": doi,
            "venue": venue,
            "preferred_source_type": typ,
            "publisher_url": item.get("doi") or item.get("id"),
            "year": item.get("publication_year"),
            "score": score,
            "confidence": "api",
        }
        if best is None or candidate["score"] > best["score"]:
            best = candidate
    return best


def query_semantic_scholar(title: str) -> dict | None:
    params = urllib.parse.urlencode({
        "query": title,
        "limit": "5",
        "fields": "title,year,venue,publicationVenue,externalIds,url",
    })
    data = http_json(f"https://api.semanticscholar.org/graph/v1/paper/search?{params}", timeout=25)
    best = None
    for item in data.get("data", []):
        found_title = item.get("title") or ""
        if not close_enough(title, found_title):
            continue
        venue_obj = item.get("publicationVenue") or {}
        venue = venue_obj.get("name") or item.get("venue") or ""
        ids = item.get("externalIds") or {}
        doi = clean_doi(ids.get("DOI"))
        arxiv = ids.get("ArXiv")
        score = 1
        if doi and is_formal_doi(doi):
            score += 2
        if venue:
            score += 2
        candidate = {
            "source": "semantic_scholar",
            "matched_title": found_title,
            "doi": doi,
            "venue": venue,
            "preferred_source_type": venue_obj.get("type") or "unknown",
            "publisher_url": item.get("url"),
            "year": item.get("year"),
            "arxiv_id": arxiv,
            "score": score,
            "confidence": "api",
        }
        if best is None or candidate["score"] > best["score"]:
            best = candidate
    return best


def choose_best(title: str, candidates: list[dict | None]) -> dict:
    key = normalize(title)
    if key in MANUAL_OVERRIDES:
        return MANUAL_OVERRIDES[key].copy()

    valid = [c for c in candidates if c]
    if not valid:
        return {
            "preferred_source_type": "preprint_or_unresolved",
            "venue": "",
            "doi": None,
            "publisher_url": None,
            "year": None,
            "confidence": "unresolved",
        }
    valid.sort(key=lambda c: c.get("score", 0), reverse=True)
    best = valid[0].copy()
    best.pop("score", None)
    return best


def preferred_label(row: dict) -> str:
    doi = row.get("doi")
    venue = row.get("venue") or ""
    arxiv_id = row.get("arxiv_id")
    if doi and is_formal_doi(doi):
        return f"{venue}; DOI:{doi}" if venue else f"DOI:{doi}"
    if venue and "arxiv" not in venue.lower():
        return venue
    if arxiv_id:
        return f"arXiv:{arxiv_id}"
    return "unresolved"


def write_outputs(rows: list[dict]) -> None:
    OUT_JSON.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    formal = sum(
        1
        for r in rows
        if (r.get("doi") and is_formal_doi(r.get("doi")))
        or (r.get("venue") and "arxiv" not in str(r.get("venue")).lower())
    )
    unresolved = sum(1 for r in rows if preferred_label(r) == "unresolved")
    lines = [
        "# Citation Sources",
        "",
        "Citation source policy: prefer the formally published journal/conference record; use arXiv only when no formal venue/DOI is found yet.",
        "",
        f"Total entries: {len(rows)}",
        f"Formal DOI/venue entries: {formal}",
        f"Unresolved entries: {unresolved}",
        "",
        "| # | Title | Preferred Citation Source | Venue | Year | DOI | PDF | Confidence |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        title = row["title"].replace("|", "\\|")
        venue = (row.get("venue") or "").replace("|", "\\|")
        doi = row.get("doi") if is_formal_doi(row.get("doi")) else ""
        pdf = row.get("pdf_path") or ""
        lines.append(
            f"| {row['index']} | {title} | {preferred_label(row)} | {venue} | "
            f"{row.get('year') or ''} | {doi} | `{pdf}` | {row.get('confidence') or ''} |"
        )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sleep", type=float, default=0.35)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
    if args.limit:
        manifest = manifest[: args.limit]

    existing = {}
    if OUT_JSON.exists() and not args.force:
        existing = {r.get("index"): r for r in json.loads(OUT_JSON.read_text(encoding="utf-8-sig"))}

    rows = []
    for item in manifest:
        index = item["index"]
        title = item["title"]
        arxiv_id = extract_arxiv(item)
        if index in existing and not args.force:
            row = existing[index]
            row["title"] = title
            row["download_status"] = item.get("status")
            row["pdf_path"] = item.get("path")
            row["pdf_source"] = item.get("source")
            row["arxiv_id"] = row.get("arxiv_id") or arxiv_id
            manual = MANUAL_OVERRIDES.get(normalize(title))
            if manual:
                row.update(manual)
            rows.append(row)
            rows.sort(key=lambda r: r["index"])
            write_outputs(rows)
            continue

        print(f"[{index}/{len(manifest)}] {title}", flush=True)
        candidates = []
        for func in (query_crossref, query_openalex, query_semantic_scholar):
            try:
                candidates.append(func(title))
            except Exception as exc:  # noqa: BLE001
                print(f"  {func.__name__}: {exc}", flush=True)
            time.sleep(args.sleep)

        best = choose_best(title, candidates)
        row = {
            "index": index,
            "title": title,
            "download_status": item.get("status"),
            "pdf_path": item.get("path"),
            "pdf_source": item.get("source"),
            "arxiv_id": arxiv_id or best.get("arxiv_id"),
            **best,
        }
        print(f"  -> {preferred_label(row)}", flush=True)
        rows.append(row)
        rows.sort(key=lambda r: r["index"])
        write_outputs(rows)

    write_outputs(sorted(rows, key=lambda r: r["index"]))
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
