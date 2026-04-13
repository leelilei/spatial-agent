from spatial_agent_survey.screening import (
    assistant_phase1_prescreen_decision,
    build_screening_sheet,
    compute_flip_rate,
    compute_raw_agreement,
    normalize_title_key,
    qc_gate_status,
    sample_exclusion_recheck,
    summarize_prisma,
)
from spatial_agent_survey.schemas import ExclusionReason, FinalStatus, PaperRecord


def test_screening_sheet_and_prisma_summary():
    papers = [
        PaperRecord(paper_id="p1", title="Paper 1", source_families=["A"]),
        PaperRecord(paper_id="p2", title="Paper 2", source_families=["B"]),
    ]
    rows = build_screening_sheet(papers)
    rows[0]["final_status"] = FinalStatus.CORE.value
    rows[1]["final_status"] = FinalStatus.EXCLUDED.value
    rows[1]["exclusion_reason"] = ExclusionReason.E2.value
    summary = summarize_prisma(rows)
    assert summary["core"] == 1
    assert summary["excluded"] == 1
    assert summary["excluded_by_reason"]["E2"] == 1


def test_exclusion_recheck_and_gate_thresholds():
    rows = [
        {"paper_id": "p1", "final_status": "excluded", "corpus_tier": "", "exclusion_reason": "E1"},
        {"paper_id": "p2", "final_status": "excluded", "corpus_tier": "", "exclusion_reason": "E2"},
        {"paper_id": "p3", "final_status": "core", "corpus_tier": "", "exclusion_reason": ""},
    ]
    sample = sample_exclusion_recheck(rows, sample_fraction=0.5, seed=1)
    assert sample

    rechecked = [{"paper_id": "p1", "rechecked_status": "core"}]
    flip_rate = compute_flip_rate(rows, rechecked)
    assert flip_rate == 1.0

    audit_rows = [
        {"original_label": "L2", "auditor_label": "L2"},
        {"original_label": "L3", "auditor_label": "L1"},
    ]
    raw_agreement = compute_raw_agreement(audit_rows, "original_label", "auditor_label")
    assert raw_agreement == 0.5

    gate = qc_gate_status(flip_rate=flip_rate, raw_agreement=raw_agreement)
    assert gate["full_rescreen_required"] is True
    assert gate["phase_gate_blocked"] is True


def test_assistant_phase1_prescreen_decision_core_seed_and_adjacent_rules():
    seed_map = {normalize_title_key("Generative Agents: Interactive Simulacra of Human Behavior"): "core"}
    core = assistant_phase1_prescreen_decision(
        {"title": "Generative Agents: Interactive Simulacra of Human Behavior", "abstract": ""},
        seed_tier_map=seed_map,
    )
    assert core["assistant_status"] == "core"
    assert core["assistant_confidence"] == "high"

    adjacent = assistant_phase1_prescreen_decision(
        {
            "title": "Can Large Language Models be Good Path Planners?",
            "abstract": "This paper studies spatial-temporal reasoning with large language models for navigation benchmarks.",
        }
    )
    assert adjacent["assistant_status"] == "adjacent"

    foundational = assistant_phase1_prescreen_decision(
        {
            "title": "Social networks and spatial configuration—How office layouts drive social interaction",
            "abstract": "",
        }
    )
    assert foundational["assistant_status"] == "foundational"
