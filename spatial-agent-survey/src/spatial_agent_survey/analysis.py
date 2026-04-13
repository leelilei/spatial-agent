"""Analysis helpers for evidence-map and claim-discipline outputs."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def compute_evidence_map(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame(
            columns=[
                "agent_accessible_representation",
                "behavioral_scale",
                "evidence_status",
                "count",
            ]
        )
    grouped = (
        frame.groupby(
            ["agent_accessible_representation", "behavioral_scale", "evidence_status"],
            dropna=False,
        )
        .size()
        .reset_index(name="count")
        .sort_values(
            by=["agent_accessible_representation", "behavioral_scale", "evidence_status"],
            kind="stable",
        )
    )
    return grouped


def compute_l4_gap_summary(frame: pd.DataFrame) -> Dict:
    if frame.empty:
        return {"total_systems": 0, "l4_count": 0, "share_l4": 0.0, "below_l4_count": 0}
    total = int(len(frame))
    l4_count = int((frame["agent_accessible_representation"] == "L4").sum())
    below_l4_count = int(frame["agent_accessible_representation"].isin(["L0", "L1", "L2", "L3"]).sum())
    return {
        "total_systems": total,
        "l4_count": l4_count,
        "share_l4": l4_count / total if total else 0.0,
        "below_l4_count": below_l4_count,
    }


def select_representation_gap_examples(frame: pd.DataFrame, limit: int = 3) -> pd.DataFrame:
    if frame.empty:
        return frame.copy()
    filtered = frame[
        (frame["representation_gap_note"].fillna("") != "")
        | (frame["environment_side_representation"] != frame["agent_accessible_representation"])
    ]
    return filtered.head(limit)


def evaluate_claim_text(text: str, corpus_tier: str, evidence_status: str) -> Dict:
    lowered = text.lower()
    strong_verbs = ["shows", "proves", "demonstrates", "establishes"]
    weak_verbs = ["suggests", "may", "appears", "motivates"]
    issues: List[str] = []
    if any(verb in lowered for verb in strong_verbs):
        issues.append("contains_strong_claim_verb")
    if corpus_tier == "foundational" and "llm" in lowered and "physical-space" not in lowered:
        issues.append("foundational_claim_needs_bridge_language")
    if evidence_status in {"designed_affordance_only", "hypothesized_but_not_tested"} and any(
        verb in lowered for verb in strong_verbs
    ):
        issues.append("claim_too_strong_for_evidence_status")
    return {
        "text": text,
        "corpus_tier": corpus_tier,
        "evidence_status": evidence_status,
        "is_safe": not issues or any(verb in lowered for verb in weak_verbs),
        "issues": issues,
    }
