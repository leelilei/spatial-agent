"""Screening helpers and PRISMA-style summaries."""

from __future__ import annotations

import random
import re
from collections import Counter
from typing import Dict, Iterable, List, Sequence

from .schemas import ExclusionReason, FinalStatus, PaperRecord

PHASE1_UNRELATED_TERMS = [
    "materials science",
    "biomedical",
    "tumor",
    "ecological",
    "ecosystem",
    "root vole",
    "face recognition",
    "chemical editor",
    "numpy",
    "diagnostic imaging",
    "optimization algorithm",
    "recommender systems",
    "pose estimation",
    "liver tumor",
    "marketing",
    "consumer behavior",
    "human resource management",
    "education",
    "open-ai models",
    "multimodal biomedical",
    "deep residual learning",
    "imagej",
    "avogadro",
    "array programming",
    "uav-vln",
    "uavs",
    "manufacturing",
    "cern for ai",
    "creative coding",
    "diagnostic artificial intelligence",
    "logistics synchronization",
    "responsible ai systems and regulation",
]

PHASE1_CORE_KNOWN_TITLES = [
    "generative agents: interactive simulacra of human behavior",
    "affordable generative agents",
    "project sid",
    "artificial leviathan",
    "concordia",
    "oasis: open agent social interaction simulations",
    "agentsociety",
    "unveiling the truth and facilitating change: towards agent-based large-scale social movement simulation",
    "travelagent: generative agents in the built environment",
    "exploring large language model-driven agents for environment-aware spatial interactions and conversations in virtual reality role-play scenarios",
    "can generative agent-based modeling replicate the friendship paradox in social media simulations?",
    "agent-based modelling meets generative ai in social network simulations",
    "multimodal safety evaluation in generative agent social simulations",
    "generative agent simulations of 1,000 people",
    "user behavior simulation with large language model-based agents",
    "user behavior simulation with large language model based agents",
    "psychologically-valid generative agents",
]

PHASE1_CORE_PHRASES = [
    "generative agent",
    "social simulation",
    "agent-based modeling",
    "agent-based simulation",
    "social network simulations",
    "behavior simulation",
    "many-agent simulations",
    "virtual reality role-play",
    "simulacra",
    "social movement simulation",
    "user behavior simulation",
    "public health policy",
    "vaccine hesitancy",
]

PHASE1_LLM_TERMS = [
    "large language model",
    "llm",
    "gpt",
    "language model",
    "generative ai",
]

PHASE1_SURVEY_TERMS = [
    "survey",
    "review",
    "perspective",
    "taxonomy",
    "scoping review",
    "systematic review",
    "critical review",
]

PHASE1_ADJACENT_LLM_TERMS = [
    "large language model",
    "llm",
    "gpt",
    "vision-language model",
    "foundation model",
    "language model",
    "multimodal large language model",
    "vision language",
]

PHASE1_ADJACENT_SPATIAL_TERMS = [
    "spatial reasoning",
    "spatially aware",
    "path planner",
    "spatial-temporal reasoning",
    "geospatial reasoning",
    "navigation",
    "spatial benchmark",
    "spatial understanding",
    "qualitative spatial",
    "3d spatial",
    "object navigation",
    "visual language object navigation",
    "geospatial tasks",
    "gis",
    "spatial concepts",
]

PHASE1_ADJACENT_EXCLUDE_TERMS = [
    "special section",
    "robotics: design principles",
    "visual spatial reasoning",
]

PHASE1_FOUNDATIONAL_SYNTAX_TERMS = [
    "space syntax",
    "visibility graph",
    "isovist",
    "depthmap",
    "axial line",
    "spatial configuration",
    "spatial metrics",
    "urban network analysis",
]

PHASE1_FOUNDATIONAL_COGNITION_TERMS = [
    "cognitive map",
    "place cells",
    "grid cells",
    "spatial language",
    "space in language and cognition",
    "spatial cognition",
]

PHASE1_FOUNDATIONAL_SOCIAL_TERMS = [
    "social interaction",
    "social behavior",
    "movement",
    "pedestrian",
    "wayfinding",
    "crime",
    "evacuation",
    "office layout",
    "office layouts",
    "housing",
]


def build_screening_sheet(papers: Sequence[PaperRecord]) -> List[Dict]:
    rows: List[Dict] = []
    for paper in papers:
        rows.append(
            {
                "paper_id": paper.paper_id,
                "title": paper.title,
                "year": paper.year or "",
                "venue": paper.venue,
                "source_families": "; ".join(paper.source_families),
                "final_status": "",
                "corpus_tier": "",
                "exclusion_reason": "",
                "notes": "",
            }
        )
    return rows


def normalize_title_key(title: str) -> str:
    return re.sub(r"\s+", " ", str(title).strip().lower())


def _normalize_screen_text(*parts: str) -> str:
    text = " ".join(str(part or "") for part in parts)
    return re.sub(r"\s+", " ", text.lower()).strip()


def _has_any(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def assistant_phase1_prescreen_decision(row: Dict, seed_tier_map: Dict[str, str] | None = None) -> Dict[str, str]:
    """Heuristic first-pass screening recommendation for the Phase 1 broad pool."""

    seed_tier_map = seed_tier_map or {}
    title = str(row.get("title") or "")
    abstract = str(row.get("abstract") or "")
    normalized_title = normalize_title_key(title)
    text = _normalize_screen_text(title, abstract)

    if normalized_title in seed_tier_map:
        status = seed_tier_map[normalized_title]
        return {
            "assistant_status": status,
            "assistant_corpus_tier": status if status != FinalStatus.EXCLUDED.value else "",
            "assistant_exclusion_reason": "",
            "assistant_confidence": "high",
            "assistant_priority": "high",
            "assistant_rule": "seed_anchor",
            "assistant_rationale": "Matched the manually curated Phase 1 seed list.",
        }

    if _has_any(text, PHASE1_UNRELATED_TERMS):
        return {
            "assistant_status": FinalStatus.EXCLUDED.value,
            "assistant_corpus_tier": "",
            "assistant_exclusion_reason": ExclusionReason.E3.value,
            "assistant_confidence": "high",
            "assistant_priority": "low",
            "assistant_rule": "unrelated_domain",
            "assistant_rationale": "Appears outside LLM-agent scope and outside the foundational spatial theory bridge.",
        }

    if any(marker in normalized_title for marker in PHASE1_CORE_KNOWN_TITLES):
        return {
            "assistant_status": FinalStatus.CORE.value,
            "assistant_corpus_tier": FinalStatus.CORE.value,
            "assistant_exclusion_reason": "",
            "assistant_confidence": "high",
            "assistant_priority": "high",
            "assistant_rule": "known_core_title",
            "assistant_rationale": "Explicitly matches a known LLM multi-agent social simulation/system title.",
        }

    if _has_any(text, PHASE1_SURVEY_TERMS) and _has_any(
        text,
        [
            "llm agent",
            "large language model based agents",
            "autonomous agents",
            "social simulation",
            "spatial intelligence",
            "game agents",
            "agent-based modeling and simulation",
        ],
    ):
        return {
            "assistant_status": FinalStatus.ADJACENT.value,
            "assistant_corpus_tier": FinalStatus.ADJACENT.value,
            "assistant_exclusion_reason": "",
            "assistant_confidence": "medium",
            "assistant_priority": "medium",
            "assistant_rule": "survey_adjacent",
            "assistant_rationale": "Useful survey/review background, but not a Core evidence-map system.",
        }

    if _has_any(text, PHASE1_LLM_TERMS) and _has_any(text, PHASE1_CORE_PHRASES) and not _has_any(text, PHASE1_SURVEY_TERMS):
        return {
            "assistant_status": FinalStatus.CORE.value,
            "assistant_corpus_tier": FinalStatus.CORE.value,
            "assistant_exclusion_reason": "",
            "assistant_confidence": "medium",
            "assistant_priority": "high",
            "assistant_rule": "llm_social_simulation",
            "assistant_rationale": "Looks like an LLM/generative-agent system paper about social simulation or behavior simulation.",
        }

    if _has_any(text, PHASE1_ADJACENT_LLM_TERMS) and _has_any(text, PHASE1_ADJACENT_SPATIAL_TERMS) and not _has_any(text, PHASE1_ADJACENT_EXCLUDE_TERMS):
        return {
            "assistant_status": FinalStatus.ADJACENT.value,
            "assistant_corpus_tier": FinalStatus.ADJACENT.value,
            "assistant_exclusion_reason": "",
            "assistant_confidence": "medium",
            "assistant_priority": "medium",
            "assistant_rule": "llm_spatial_reasoning",
            "assistant_rationale": "Relevant as an Adjacent paper on LLM spatial reasoning or spatially-aware agents.",
        }

    if _has_any(text, PHASE1_FOUNDATIONAL_SYNTAX_TERMS) and _has_any(text, PHASE1_FOUNDATIONAL_SOCIAL_TERMS):
        return {
            "assistant_status": FinalStatus.FOUNDATIONAL.value,
            "assistant_corpus_tier": FinalStatus.FOUNDATIONAL.value,
            "assistant_exclusion_reason": "",
            "assistant_confidence": "medium",
            "assistant_priority": "medium",
            "assistant_rule": "space_syntax_bridge",
            "assistant_rationale": "Useful as foundational evidence on spatial configuration, movement, or social interaction.",
        }

    if _has_any(text, PHASE1_FOUNDATIONAL_COGNITION_TERMS):
        return {
            "assistant_status": FinalStatus.FOUNDATIONAL.value,
            "assistant_corpus_tier": FinalStatus.FOUNDATIONAL.value,
            "assistant_exclusion_reason": "",
            "assistant_confidence": "medium",
            "assistant_priority": "medium",
            "assistant_rule": "spatial_cognition_anchor",
            "assistant_rationale": "Useful as foundational spatial cognition background rather than Core system evidence.",
        }

    if _has_any(text, PHASE1_LLM_TERMS):
        return {
            "assistant_status": FinalStatus.EXCLUDED.value,
            "assistant_corpus_tier": "",
            "assistant_exclusion_reason": ExclusionReason.E1.value,
            "assistant_confidence": "low",
            "assistant_priority": "low",
            "assistant_rule": "llm_no_space_environment",
            "assistant_rationale": "Mentions LLM/agents but does not clearly indicate a spatial environment relevant to this review.",
        }

    if "space" in text or "spatial" in text:
        return {
            "assistant_status": FinalStatus.EXCLUDED.value,
            "assistant_corpus_tier": "",
            "assistant_exclusion_reason": ExclusionReason.E2.value,
            "assistant_confidence": "low",
            "assistant_priority": "low",
            "assistant_rule": "space_without_target_behavior",
            "assistant_rationale": "Touches space/spatial topics but does not clearly fit Adjacent or Foundational target behavior scope.",
        }

    return {
        "assistant_status": FinalStatus.EXCLUDED.value,
        "assistant_corpus_tier": "",
        "assistant_exclusion_reason": ExclusionReason.E3.value,
        "assistant_confidence": "low",
        "assistant_priority": "low",
        "assistant_rule": "fallback_exclude",
        "assistant_rationale": "Does not appear to fit Core, Adjacent, or Foundational corpus definitions.",
    }


def summarize_prisma(rows: Iterable[Dict]) -> Dict:
    counter = Counter()
    excluded_counter = Counter()
    total = 0
    for row in rows:
        total += 1
        status = str(row.get("final_status") or row.get("corpus_tier") or "").strip().lower()
        if status:
            counter[status] += 1
        reason = str(row.get("exclusion_reason") or "").strip()
        if reason:
            excluded_counter[reason] += 1
    return {
        "total_screened": total,
        "core": counter.get(FinalStatus.CORE.value, 0),
        "adjacent": counter.get(FinalStatus.ADJACENT.value, 0),
        "foundational": counter.get(FinalStatus.FOUNDATIONAL.value, 0),
        "excluded": counter.get(FinalStatus.EXCLUDED.value, 0),
        "excluded_by_reason": dict(sorted(excluded_counter.items())),
    }


def sample_exclusion_recheck(rows: Sequence[Dict], sample_fraction: float = 0.15, seed: int = 42) -> List[Dict]:
    excluded_rows = [
        row for row in rows
        if str(row.get("final_status") or row.get("corpus_tier") or "").strip().lower() == FinalStatus.EXCLUDED.value
    ]
    if not excluded_rows:
        return []
    sample_size = max(1, round(len(excluded_rows) * sample_fraction))
    rng = random.Random(seed)
    sample = rng.sample(excluded_rows, min(sample_size, len(excluded_rows)))
    return [dict(row, recheck_required="yes") for row in sample]


def compute_flip_rate(original_rows: Sequence[Dict], rechecked_rows: Sequence[Dict]) -> float:
    original = {row["paper_id"]: row for row in original_rows}
    flips = 0
    compared = 0
    for row in rechecked_rows:
        paper_id = row["paper_id"]
        if paper_id not in original:
            continue
        compared += 1
        original_status = str(original[paper_id].get("final_status") or original[paper_id].get("corpus_tier") or "")
        rechecked_status = str(row.get("rechecked_status") or row.get("final_status") or row.get("corpus_tier") or "")
        if original_status != rechecked_status:
            flips += 1
    if compared == 0:
        return 0.0
    return flips / compared


def compute_raw_agreement(rows: Sequence[Dict], left_key: str, right_key: str) -> float:
    compared = 0
    agreements = 0
    for row in rows:
        left_value = str(row.get(left_key) or "").strip()
        right_value = str(row.get(right_key) or "").strip()
        if not left_value or not right_value:
            continue
        compared += 1
        if left_value == right_value:
            agreements += 1
    if compared == 0:
        return 1.0
    return agreements / compared


def qc_gate_status(flip_rate: float, raw_agreement: float) -> Dict[str, bool]:
    return {
        "full_rescreen_required": flip_rate > 0.10,
        "phase_gate_blocked": raw_agreement < 0.80,
    }
