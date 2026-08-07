import json
import sys
from pathlib import Path


V1_ROOT = Path(__file__).resolve().parents[1] / "v1_1"
PILOT = V1_ROOT / "native_pilot"
WAVE4 = PILOT / "expansion_wave4"
sys.path.insert(0, str(PILOT))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))

import audit_wave4_design as design_audit  # noqa: E402
import audit_wave4_distinctness as distinctness  # noqa: E402
import generate_expansion_wave4 as wave4  # noqa: E402
import verify_native_pilot as verifier  # noqa: E402


CONSTRUCTS = (
    "disruption_recovery", "time_window_scheduling", "resource_budget_allocation",
    "poi_availability_service_evidence", "memory_conditioned_preference",
    "social_coordination_copresence", "multi_party_commitment", "compound_long_horizon",
)


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_design_contract_is_valid_and_actor_runs_stay_unauthorized():
    report = design_audit.audit()
    assert report["errors"] == []
    assert report["construct_count"] == 8
    assert report["unique_mechanism_count"] == 8
    assert report["unique_transition_count"] == 8
    # Public actor runs are a separate authorization step, never implied by design.
    assert report["actor_runs_authorized"] is False


def test_generated_pool_covers_every_construct_in_three_public_worlds():
    manifest = load(WAVE4 / "manifest.json")
    assert manifest["scenario_count"] == 24
    assert manifest["rejection_count"] == 0
    assert manifest["construct_counts"] == {construct: 3 for construct in CONSTRUCTS}
    assert manifest["status"].endswith("not_release")

    worlds = set()
    for path in (WAVE4 / "scenarios").glob("*.json"):
        scenario = load(path)
        worlds.add(scenario["world_id"])
        assert scenario["benchmark_metadata"]["world_visibility"] == "public"
        assert scenario["benchmark_metadata"]["split"] == "calibration_public"
    assert len(worlds) == 3


def test_every_item_declares_its_mechanism_contract():
    design = load(PILOT / "wave4_mechanism_design.json")["constructs"]
    for path in (WAVE4 / "scenarios").glob("*.json"):
        scenario = load(path)
        contract = scenario["benchmark_metadata"]["mechanism_contract"]
        expected = design[scenario["family"]]
        assert contract["state_transition"] == expected["state_transition"]
        assert contract["negative_failure"] == expected["negative_failure"]
        assert set(contract["novelty_against"]) == {"base", "wave2", "wave3"}
        assert scenario["benchmark_metadata"]["mechanism_id"] == expected["mechanism_id"]


def test_oracle_and_matched_negative_gates_pass_for_all_items():
    report = verifier.verify(root=WAVE4)
    assert report["scenario_count"] == 24
    assert report["all_passed"], [
        row["scenario_id"] for row in report["results"] if not row["passed"]
    ]
    for row in report["results"]:
        assert row["oracle_task_completion"] == 1.0
        assert row["oracle_trace_feasibility"] == 1.0
        assert row["oracle_violations"] == 0
        assert row["headroom"] >= 0.15


def test_wave4_items_are_structurally_distinct_from_all_prior_pools():
    report = distinctness.audit()
    assert report["scenario_count"] == 24
    assert report["all_structurally_distinct"], [
        row["scenario_id"] for row in report["results"] if not row["structurally_distinct"]
    ]
    for row in report["results"]:
        assert row["prior_item_count"] > 0, row["scenario_id"]


def test_generation_is_deterministic_from_the_archived_generator():
    worlds = sorted((V1_ROOT / "worlds" / "public").glob("*.json"))
    world = load(worlds[0])
    a_scenario, a_plan = wave4.build_item(world, "disruption_recovery", 0)
    b_scenario, b_plan = wave4.build_item(world, "disruption_recovery", 0)
    assert a_scenario == b_scenario
    assert a_plan == b_plan
    assert a_scenario["benchmark_metadata"]["seed"] == b_scenario["benchmark_metadata"]["seed"]


def test_release_accounting_is_untouched_by_wave4_calibration():
    registry = load(V1_ROOT / "manifests" / "calibration_template_registry.json")
    # Wave-4 is calibration evidence only until its public six-system gate runs.
    assert registry["release_accepted_count"] == 0
    assert registry["evidence_scope"] == "public_world_calibration_only"
