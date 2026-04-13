"""Coding templates and merge/split rules for system-level evidence."""

from __future__ import annotations

from typing import Dict, Iterable, List, Tuple

from .schemas import (
    AgentAccessibleRepresentation,
    AgentCount,
    BehavioralScale,
    EnvironmentSideRepresentation,
    EvaluationMethod,
    EvidenceStatus,
    SpatialBehaviorCoupling,
    SystemEvidenceRecord,
)


def merge_or_split_recommendation(existing: Dict, new: Dict) -> Tuple[str, List[str]]:
    reasons: List[str] = []
    if existing.get("agent_accessible_representation") != new.get("agent_accessible_representation"):
        reasons.append("agent_accessible_representation_changed")
    if existing.get("environment_side_representation") != new.get("environment_side_representation"):
        reasons.append("environment_side_representation_changed")
    if existing.get("environment_configuration") != new.get("environment_configuration"):
        reasons.append("environment_configuration_changed")
    if existing.get("behavioral_scale") != new.get("behavioral_scale"):
        reasons.append("behavioral_scale_changed")
    if existing.get("agent_count") != new.get("agent_count"):
        reasons.append("agent_count_changed")
    if reasons:
        return "split", reasons
    return "merge", ["no_structural_change_detected"]


def build_system_templates(core_rows: Iterable[Dict]) -> List[Dict]:
    templates: List[Dict] = []
    for row in core_rows:
        status = str(row.get("final_status") or row.get("corpus_tier") or "").strip().lower()
        if status != "core":
            continue
        templates.append(
            {
                "system_name": row.get("title", ""),
                "environment_configuration": "",
                "system_family": row.get("title", ""),
                "paper_refs": row.get("paper_id", ""),
                "year": row.get("year", ""),
                "agent_count": "",
                "environment_side_representation": "",
                "agent_accessible_representation": "",
                "representation_gap_note": "",
                "behavioral_scale": "",
                "behavior_type": "",
                "evidence_status": "",
                "spatial_behavior_coupling": "",
                "evaluation_method": "",
                "space_syntax_construct": "",
                "notes": "",
            }
        )
    return templates


def pilot_system_examples() -> List[SystemEvidenceRecord]:
    return [
        SystemEvidenceRecord(
            system_name="Generative Agents",
            environment_configuration="Small-town sandbox",
            system_family="Generative Agents",
            paper_refs=["park2023-generative-agents"],
            year=2023,
            agent_count=AgentCount.SMALL,
            environment_side_representation=EnvironmentSideRepresentation.TEXT_ONLY,
            agent_accessible_representation=AgentAccessibleRepresentation.L2,
            representation_gap_note="Locations are described semantically, not structurally.",
            behavioral_scale=BehavioralScale.INTERACTION,
            behavior_type=["dialogue", "mobility"],
            evidence_status=EvidenceStatus.DESIGNED_AFFORDANCE_ONLY,
            spatial_behavior_coupling=SpatialBehaviorCoupling.IMPLICIT,
            evaluation_method=EvaluationMethod.HUMAN_EVAL,
            space_syntax_construct=[],
            notes="Pilot example for semantic spatial descriptions.",
        ),
        SystemEvidenceRecord(
            system_name="Project Sid",
            environment_configuration="Large-scale simulated society",
            system_family="Project Sid",
            paper_refs=["altera2024-project-sid"],
            year=2024,
            agent_count=AgentCount.LARGE,
            environment_side_representation=EnvironmentSideRepresentation.TEXT_ONLY,
            agent_accessible_representation=AgentAccessibleRepresentation.L1,
            representation_gap_note="Environment includes places but exposes limited structure to agents.",
            behavioral_scale=BehavioralScale.EMERGENT_SOCIAL_STRUCTURE,
            behavior_type=["role_differentiation", "norm_formation"],
            evidence_status=EvidenceStatus.OBSERVED_EFFECT,
            spatial_behavior_coupling=SpatialBehaviorCoupling.IMPLICIT,
            evaluation_method=EvaluationMethod.MIXED,
            space_syntax_construct=[],
            notes="Pilot example for macro social emergence with weak explicit space structure.",
        ),
        SystemEvidenceRecord(
            system_name="SARAH",
            environment_configuration="3D embodied household task world",
            system_family="SARAH",
            paper_refs=["oh2025-sarah"],
            year=2025,
            agent_count=AgentCount.SOLO,
            environment_side_representation=EnvironmentSideRepresentation.ENGINE_3D,
            agent_accessible_representation=AgentAccessibleRepresentation.L3,
            representation_gap_note="3D backend present, but pilot coding assumes the agent receives structured observations rather than raw geometry.",
            behavioral_scale=BehavioralScale.LOCAL_ACTION,
            behavior_type=["mobility"],
            evidence_status=EvidenceStatus.OBSERVED_EFFECT,
            spatial_behavior_coupling=SpatialBehaviorCoupling.EXPLICIT,
            evaluation_method=EvaluationMethod.AUTO_METRIC,
            space_syntax_construct=[],
            notes="Pilot example used to guard against over-labeling L5.",
        ),
    ]


def system_records_to_rows(records: Iterable[SystemEvidenceRecord]) -> List[Dict]:
    rows: List[Dict] = []
    for record in records:
        row = record.model_dump()
        row["paper_refs"] = "; ".join(row["paper_refs"])
        row["behavior_type"] = "; ".join(row["behavior_type"])
        row["space_syntax_construct"] = "; ".join(row["space_syntax_construct"])
        row["agent_count"] = row["agent_count"].value
        row["environment_side_representation"] = row["environment_side_representation"].value
        row["agent_accessible_representation"] = row["agent_accessible_representation"].value
        row["behavioral_scale"] = row["behavioral_scale"].value
        row["evidence_status"] = row["evidence_status"].value
        row["spatial_behavior_coupling"] = row["spatial_behavior_coupling"].value
        row["evaluation_method"] = row["evaluation_method"].value
        rows.append(row)
    return rows
