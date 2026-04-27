"""Schemas and enum types for survey workflow artifacts."""

from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, field_validator


class StrEnum(str, Enum):
    """String-backed enum for stable CSV and JSON serialization."""


class FinalStatus(StrEnum):
    CORE = "core"
    ADJACENT = "adjacent"
    FOUNDATIONAL = "foundational"
    EXCLUDED = "excluded"


class CoreLayer(StrEnum):
    ANCHOR = "anchor_core"
    BRIDGE = "bridge_core"


class ExclusionReason(StrEnum):
    E1 = "E1"
    E2 = "E2"
    E3 = "E3"
    E4 = "E4"
    E5 = "E5"


class AgentCount(StrEnum):
    SOLO = "1"
    SMALL = "2-10"
    MEDIUM = "10-100"
    LARGE = "100+"


class EnvironmentSideRepresentation(StrEnum):
    TEXT_ONLY = "text-only"
    GRID_2D = "2D_grid"
    ISOMETRIC_25D = "2.5D_isometric"
    ENGINE_3D = "3D_engine"
    GRAPH_BASED = "graph_based"


class AgentAccessibleRepresentation(StrEnum):
    L0 = "L0"
    L1 = "L1"
    L2 = "L2"
    L3 = "L3"
    L4 = "L4"
    L5 = "L5"


class BehavioralScale(StrEnum):
    LOCAL_ACTION = "local_action"
    INTERACTION = "interaction"
    EMERGENT_SOCIAL_STRUCTURE = "emergent_social_structure"


class EvidenceStatus(StrEnum):
    OBSERVED_EFFECT = "observed_effect"
    DESIGNED_AFFORDANCE_ONLY = "designed_affordance_only"
    HYPOTHESIZED_BUT_NOT_TESTED = "hypothesized_but_not_tested"


class SpatialBehaviorCoupling(StrEnum):
    NONE = "none"
    IMPLICIT = "implicit"
    EXPLICIT = "explicit"


class EvaluationMethod(StrEnum):
    HUMAN_EVAL = "human_eval"
    AUTO_METRIC = "auto_metric"
    LLM_AS_JUDGE = "llm_as_judge"
    MIXED = "mixed"
    NONE = "none"


class PaperRecord(BaseModel):
    """Normalized paper-level record used for screening."""

    paper_id: str
    title: str
    abstract: str = ""
    year: Optional[int] = None
    venue: str = ""
    url: str = ""
    doi: str = ""
    authors: List[str] = Field(default_factory=list)
    source_families: List[str] = Field(default_factory=list)
    final_status: Optional[FinalStatus] = None
    corpus_tier: Optional[FinalStatus] = None
    core_layer: Optional[CoreLayer] = None
    exclusion_reason: Optional[ExclusionReason] = None
    notes: str = ""

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("title must not be blank")
        return value


class SystemEvidenceRecord(BaseModel):
    """System/configuration-level record used for the evidence map."""

    core_layer: Optional[CoreLayer] = None
    system_name: str
    environment_configuration: str = ""
    system_family: str
    paper_refs: List[str] = Field(default_factory=list)
    year: Optional[int] = None
    agent_count: AgentCount
    environment_side_representation: EnvironmentSideRepresentation
    agent_accessible_representation: AgentAccessibleRepresentation
    representation_gap_note: str = ""
    behavioral_scale: BehavioralScale
    behavior_type: List[str] = Field(default_factory=list)
    evidence_status: EvidenceStatus
    spatial_behavior_coupling: SpatialBehaviorCoupling
    evaluation_method: EvaluationMethod
    space_syntax_construct: List[str] = Field(default_factory=list)
    notes: str = ""

    @field_validator("system_name", "system_family")
    @classmethod
    def required_text_fields(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("required text field must not be blank")
        return value

    @field_validator("paper_refs", "behavior_type", "space_syntax_construct")
    @classmethod
    def normalize_list_values(cls, value: List[str]) -> List[str]:
        return [item.strip() for item in value if item and item.strip()]


class AuditMetrics(BaseModel):
    """Summary metrics for QC gates."""

    flip_rate: float = 0.0
    raw_agreement: float = 1.0
    full_rescreen_required: bool = False
    phase_gate_blocked: bool = False


def paper_fieldnames() -> List[str]:
    return list(PaperRecord.model_fields.keys())


def system_fieldnames() -> List[str]:
    return list(SystemEvidenceRecord.model_fields.keys())


def split_semicolon_list(value: str | List[str] | None) -> List[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return [part.strip() for part in str(value).split(";") if part.strip()]


def paper_from_row(row: Dict) -> PaperRecord:
    payload = dict(row)
    payload["authors"] = split_semicolon_list(payload.get("authors"))
    payload["source_families"] = split_semicolon_list(payload.get("source_families"))
    if payload.get("year") in ("", None):
        payload["year"] = None
    if payload.get("final_status"):
        payload["final_status"] = FinalStatus(str(payload["final_status"]).strip())
    else:
        payload["final_status"] = None
    if payload.get("corpus_tier"):
        payload["corpus_tier"] = FinalStatus(str(payload["corpus_tier"]).strip())
    else:
        payload["corpus_tier"] = None
    if payload.get("core_layer"):
        payload["core_layer"] = CoreLayer(str(payload["core_layer"]).strip())
    else:
        payload["core_layer"] = None
    if payload.get("exclusion_reason"):
        payload["exclusion_reason"] = ExclusionReason(str(payload["exclusion_reason"]).strip())
    else:
        payload["exclusion_reason"] = None
    return PaperRecord(**payload)


def system_from_row(row: Dict) -> SystemEvidenceRecord:
    payload = dict(row)
    payload["paper_refs"] = split_semicolon_list(payload.get("paper_refs"))
    payload["behavior_type"] = split_semicolon_list(payload.get("behavior_type"))
    payload["space_syntax_construct"] = split_semicolon_list(payload.get("space_syntax_construct"))
    if payload.get("year") in ("", None):
        payload["year"] = None
    if payload.get("core_layer"):
        payload["core_layer"] = CoreLayer(str(payload["core_layer"]).strip())
    else:
        payload["core_layer"] = None
    payload["agent_count"] = AgentCount(str(payload["agent_count"]).strip())
    payload["environment_side_representation"] = EnvironmentSideRepresentation(
        str(payload["environment_side_representation"]).strip()
    )
    payload["agent_accessible_representation"] = AgentAccessibleRepresentation(
        str(payload["agent_accessible_representation"]).strip()
    )
    payload["behavioral_scale"] = BehavioralScale(str(payload["behavioral_scale"]).strip())
    payload["evidence_status"] = EvidenceStatus(str(payload["evidence_status"]).strip())
    payload["spatial_behavior_coupling"] = SpatialBehaviorCoupling(
        str(payload["spatial_behavior_coupling"]).strip()
    )
    payload["evaluation_method"] = EvaluationMethod(str(payload["evaluation_method"]).strip())
    return SystemEvidenceRecord(**payload)
