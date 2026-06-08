import json

import pandas as pd

from spatial_agent_survey.analysis import compute_evidence_map, compute_l4_gap_summary, evaluate_claim_text
from spatial_agent_survey.coding import pilot_system_examples, system_records_to_rows
from spatial_agent_survey.export import export_evidence_assets


def test_evidence_map_and_l4_summary_export(tmp_path):
    frame = pd.DataFrame(system_records_to_rows(pilot_system_examples()))
    outputs = export_evidence_assets(frame, output_dir=tmp_path / "results")
    assert outputs["evidence_map_csv"].exists()
    assert outputs["evidence_map_md"].exists()
    assert outputs["representation_gap_examples_csv"].exists()
    summary = json.loads(outputs["l4_gap_summary_json"].read_text(encoding="utf-8"))
    assert summary["total_systems"] == 3
    assert summary["l4_count"] == 0


def test_compute_evidence_map_counts_by_expected_axes():
    frame = pd.DataFrame(system_records_to_rows(pilot_system_examples()))
    evidence_map = compute_evidence_map(frame)
    assert {"agent_accessible_representation", "behavioral_scale", "evidence_status", "count"} == set(evidence_map.columns)
    assert evidence_map["count"].sum() == 3


def test_claim_text_flags_overstrong_language():
    result = evaluate_claim_text(
        "Current evidence shows that spatial configuration shapes LLM-agent social behavior.",
        corpus_tier="core",
        evidence_status="designed_affordance_only",
    )
    assert result["is_safe"] is False
    assert "claim_too_strong_for_evidence_status" in result["issues"]
