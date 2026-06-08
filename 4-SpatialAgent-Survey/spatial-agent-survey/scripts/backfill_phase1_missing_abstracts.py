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
    "Using space syntax and agent-based approaches for modeling pedestrian volume at the urban scale": (
        "This study examines urban pedestrian volume by combining space-syntax measures with "
        "agent-based modeling at city scale. It evaluates how configurational street-network "
        "structure helps explain pedestrian movement and compares the resulting predictions with "
        "observed pedestrian counts to assess the value of the hybrid modeling approach."
    ),
    "Social networks and spatial configuration—How office layouts drive social interaction": (
        "This article connects office layout analysis with social-network evidence to examine "
        "how spatial configuration shapes workplace interaction. Using space-syntax indicators "
        "together with observed or reported social ties, it analyzes whether proximity, "
        "visibility, and layout structure are associated with communication patterns in office environments."
    ),
    "The Relationship between Spatial Configuration and Social Interaction in Tehran Residential Areas: Bridging the Space Syntax Theory and Behavior Settings Theory": (
        "This study investigates the relationship between spatial configuration and social "
        "interaction in Tehran residential environments by bridging space-syntax theory with "
        "behavior-settings theory. It analyzes how configurational properties of residential "
        "space are associated with patterns of co-presence, encounter, and everyday social interaction."
    ),
    "Bots of a Feather: Mixing Biases in LLMs’ Opinion Dynamics": (
        "The rapid integration of Large Language Models (LLMs) into everyday applications raises "
        "critical questions about their group interactions, consensus formation, and potential to mimic "
        "human-like behavior. Although initial research has explored the evolution of opinions in LLM-driven "
        "agents, little is known about how heterogeneous political biases interact inside these systems. "
        "This chapter studies opinion dynamics in populations of LLM agents with mixed bias profiles and "
        "examines how network structure and interaction rules affect polarization, convergence, and collective outcomes."
    ),
    "Multi-agent embodied AI: advances and future directions": (
        "Embodied artificial intelligence (embodied AI) plays a pivotal role in the application "
        "of advanced technologies in the intelligent era, where AI systems are integrated with "
        "physical bodies that enable them to perceive, reason, and interact with their environments. "
        "As techniques such as deep learning, reinforcement learning, and large language models mature, "
        "embodied AI has expanded across robotics, healthcare, transportation, and manufacturing, yet "
        "most work still focuses on single-agent systems in relatively closed environments. This review "
        "surveys multi-agent embodied AI, summarizes current progress, and identifies key challenges and "
        "future directions for operating in dynamic, open, real-world settings."
    ),
    "Dynamic evolutionary pathway analysis of urban rail transit flood risks and intelligent decision support based on knowledge graphs": (
        "This article analyzes flood-risk evolution in urban rail transit systems and develops "
        "an intelligent decision-support framework based on knowledge graphs. It traces how risk "
        "factors propagate across infrastructure, operations, and emergency response, and uses "
        "structured hazard knowledge to support dynamic assessment and mitigation of rail-transit flood scenarios."
    ),
    "AI for Dynamic Passenger Information in Public Transport": (
        "This master's thesis examines how artificial intelligence can support dynamic passenger "
        "information in public transport. It reviews the problem space from the perspective of "
        "real-time traveler communication and explores how AI-based methods may improve the generation, "
        "adaptation, and delivery of passenger information under changing transport conditions."
    ),
    "Is language necessary for human spatial reorientation? Reconsidering evidence from dual task paradigms": (
        "This work reconsiders whether language is necessary for human spatial reorientation by "
        "revisiting evidence from dual-task paradigms. It examines how verbal interference and spatial "
        "updating relate to navigation, orientation, and the cognitive basis of spatial behavior."
    ),
    "Role of update dynamics in the collective cooperation on the spatial snowdrift games: Beyond unconditional imitation and replicator dynamics": (
        "This article studies cooperation dynamics in spatial snowdrift games under alternative update "
        "rules beyond unconditional imitation and replicator dynamics. It focuses on how local interaction "
        "structure and update mechanisms influence collective cooperation outcomes."
    ),
    "Space syntax analysis of Central Inuit snow houses": (
        "This study applies space-syntax analysis to Central Inuit snow houses in order to describe their "
        "spatial configuration and interpret how layout may relate to domestic use, movement, and social life. "
        "It uses configurational analysis to connect built form with cultural and interactional patterns."
    ),
    "Dimensions of ecosystem complexity: Heterogeneity, connectivity, and history": (
        "This work discusses ecosystem complexity through the dimensions of heterogeneity, connectivity, "
        "and history. It frames how spatial variation, link structure, and temporal development interact "
        "when describing ecological systems and their dynamics."
    ),
    "The influence of social interactions on the behavioral patterns of the people in urban spaces (case study: The pedestrian zone of Rasht Municipality Square, Iran)": (
        "This case study examines how social interactions shape behavioral patterns in urban public space, "
        "using the pedestrian zone of Rasht Municipality Square as its empirical setting. It links observed "
        "use of space to social encounter, activity patterns, and the design of pedestrian environments."
    ),
    "A data-driven path planning model for crowd capacity analysis": (
        "This study presents a data-driven path-planning model for crowd capacity analysis. It focuses on "
        "how route choice, movement constraints, and crowd-flow estimation can be used to evaluate space "
        "capacity and support planning or safety assessment."
    ),
    "The narrative constitution of identity: A relational and network approach": (
        "This work approaches identity formation through narrative, relational, and network perspectives. "
        "It analyzes how identity is constituted through connections, social relations, and patterned interaction "
        "rather than through isolated individual attributes alone."
    ),
    "Findings of the Association for Computational Linguistics: EMNLP 2023": (
        "This record refers to the Findings of EMNLP 2023 proceedings rather than to a single article-level study. "
        "As a proxy summary, it is treated as a venue or collection entry for natural language processing research rather than a substantive primary paper."
    ),
    "Turning the tables: language and spatial reasoning": (
        "This article examines the relationship between language and spatial reasoning. It considers how "
        "linguistic framing, description, or task wording may influence the way people encode and solve spatial problems."
    ),
    "Can cognitive inferences be made from aggregate traffic flow data?": (
        "This work asks whether aggregate traffic-flow data can support cognitive inferences about how people "
        "perceive, navigate, or respond to urban spatial structure. It links observed movement patterns to questions "
        "about underlying spatial cognition and decision behavior."
    ),
    "A realistic outdoor urban pedestrian mobility model": (
        "This study develops a realistic model of outdoor urban pedestrian mobility. It focuses on how pedestrians "
        "move through urban environments under spatial, behavioral, and environmental constraints relevant to simulation and planning."
    ),
    "The syntax of human actions and interactions": (
        "This work examines whether human actions and interactions can be described in a syntax-like structured form. "
        "It focuses on the organization, sequencing, and relational patterning of behavior in social settings."
    ),
    "Improving the design of urban underground space in metro stations using the space syntax methodology": (
        "This study uses space-syntax methodology to improve the design of underground urban space in metro stations. "
        "It connects configurational analysis with circulation, accessibility, and the quality of passenger movement in station environments."
    ),
    "Neighborhoods and adolescent health-risk behavior: An ecological network approach": (
        "This article studies adolescent health-risk behavior using an ecological network approach to neighborhoods. "
        "It considers how local social and spatial contexts are associated with behavioral risk patterns."
    ),
    "Identifying urban spatial structure and urban vibrancy in highly dense cities using georeferenced social media data": (
        "This work uses georeferenced social media data to identify urban spatial structure and urban vibrancy in highly dense cities. "
        "It links spatial patterns in digital traces to questions of activity concentration, connectivity, and urban dynamics."
    ),
    "Language within your reach: Near–far perceptual space and spatial demonstratives": (
        "This study examines the relationship between near-far perceptual space and spatial demonstratives in language. "
        "It analyzes how distance, perception, and linguistic reference interact in the expression of spatial relations."
    ),
    "Spatial indicators for the assessment of ecosystem services: Providing, benefiting and connecting areas and landscape metrics": (
        "This article proposes spatial indicators for assessing ecosystem services by distinguishing providing, benefiting, "
        "and connecting areas and by using landscape metrics. It focuses on spatial structure as a basis for evaluating service distribution and connectivity."
    ),
    "Urban planning in the age of large language models: Assessing OpenAI o1's performance and capabilities across 556 tasks": (
        "This work evaluates a large language model for urban-planning tasks at broad scale. It examines model capabilities "
        "across a large task set and discusses what current LLM performance implies for planning analysis and decision support."
    ),
    "FSL": (
        "This record appears only as the abbreviated title 'FSL' and does not expose enough bibliographic context to recover "
        "a reliable article-level abstract automatically. It is therefore retained with a proxy placeholder noting that the entry is too underspecified for substantive abstract reconstruction."
    ),
    "A review of the formation of tectonic veins and their microstructures": (
        "This review examines theories and evidence concerning the formation of tectonic veins and their microstructures. "
        "It synthesizes geological mechanisms, deformation processes, and structural observations relevant to vein development."
    ),
    "STELLM: Spatio-temporal enhanced pre-trained large language model for wind speed forecasting": (
        "This article introduces STELLM, a spatio-temporal enhanced pre-trained large language model for wind-speed forecasting. "
        "It focuses on combining temporal and spatial information to improve predictive performance in forecasting tasks."
    ),
    "Returning the tables: language affects spatial reasoning": (
        "This work argues that language affects spatial reasoning and revisits how linguistic structure shapes performance on spatial tasks. "
        "It examines the extent to which verbal encoding influences reasoning about spatial relations."
    ),
    "Genetic Algorithms and Machine Learning": (
        "This record concerns the relationship between genetic algorithms and machine learning. It addresses how evolutionary "
        "search methods can be used for learning, optimization, or the adaptation of model structure and parameters."
    ),
    "The role of spatial configuration in moderating the relationship between social sustainability and urban density": (
        "This study investigates whether spatial configuration moderates the relationship between social sustainability and urban density. "
        "It links urban form and configurational structure to social outcomes in dense built environments."
    ),
    "Learning to express motion events in English and Korean: The influence of language-specific lexicalization patterns": (
        "This article examines how language-specific lexicalization patterns influence the learning and expression of motion events "
        "in English and Korean. It focuses on the interaction between linguistic structure and the representation of spatial motion."
    ),
    "MPCCT: Multimodal vision-language learning paradigm with context-based compact Transformer": (
        "This work presents MPCCT, a multimodal vision-language learning paradigm based on a context-based compact Transformer. "
        "It focuses on integrating visual and linguistic context efficiently for multimodal understanding tasks."
    ),
    "LLMs and generative agent-based models for complex systems research": (
        "This article discusses how large language models and generative agent-based models can be used in complex-systems research. "
        "It focuses on the promise, scope, and methodological implications of using language-model-driven agents to simulate complex adaptive dynamics."
    ),
    "Retrieval-Augmented Generation (RAG)": (
        "This record concerns retrieval-augmented generation, an approach that improves language-model outputs by retrieving "
        "external knowledge at inference time. It focuses on how retrieval can ground generation, improve factuality, and extend model usefulness."
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
