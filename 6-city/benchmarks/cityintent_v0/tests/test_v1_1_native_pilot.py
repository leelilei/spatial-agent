import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PILOT = ROOT / "v1_1" / "native_pilot"


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


generator = load_module("cityintent_native_pilot_generator", PILOT / "generate_native_pilot.py")
verifier = load_module("cityintent_native_pilot_verifier", PILOT / "verify_native_pilot.py")
expansion = load_module("cityintent_native_expansion_wave1", PILOT / "generate_expansion_wave1.py")
time_v7 = load_module("cityintent_time_v7_matrix", PILOT / "generate_time_v7_matrix.py")
wave2 = load_module("cityintent_native_expansion_wave2", PILOT / "generate_expansion_wave2.py")
wave3 = load_module("cityintent_native_expansion_wave3", PILOT / "generate_expansion_wave3.py")
distinctness = load_module("cityintent_wave3_distinctness", PILOT / "audit_wave3_distinctness.py")
wave4_design = load_module("cityintent_wave4_design_audit", PILOT / "audit_wave4_design.py")


def test_native_pilot_covers_all_constructs_and_passes_two_sided_gate():
    generator.generate()
    report = verifier.verify()
    assert report["scenario_count"] == 16
    assert report["pass_count"] == 16
    assert {item["construct_family"] for item in report["results"]} == set(generator.CONSTRUCTS)


def test_expansion_wave1_covers_every_construct_and_world_and_passes_two_sided_gate():
    manifest = expansion.generate()
    root = PILOT / "expansion_wave1"
    report = verifier.verify(root)
    assert manifest["scenario_count"] == 40
    assert set(manifest["construct_counts"]) == set(generator.CONSTRUCTS)
    assert set(manifest["construct_counts"].values()) == {5}
    assert set(manifest["world_counts"].values()) == {8}
    assert report["scenario_count"] == 40
    assert report["pass_count"] == 40


def test_time_v7_public_matrix_preserves_all_constructs_and_passes_two_sided_gate():
    manifest = time_v7.generate()
    root = PILOT / "time_v7" / "public_matrix"
    report = verifier.verify(root)
    assert manifest["scenario_count"] == 24
    assert len(manifest["time_scenario_ids"]) == 3
    assert all("time7" in scenario_id for scenario_id in manifest["time_scenario_ids"])
    assert report["scenario_count"] == 24
    assert report["pass_count"] == 24


def test_expansion_wave2_adds_one_mechanism_per_construct_and_passes_two_sided_gate():
    manifest = wave2.generate()
    root = PILOT / "expansion_wave2"
    report = verifier.verify(root)
    assert manifest["scenario_count"] == 24
    assert manifest["rejection_count"] == 0
    assert set(manifest["mechanisms"]) == set(generator.CONSTRUCTS)
    assert len(set(manifest["mechanisms"].values())) == 8
    assert set(manifest["construct_counts"].values()) == {3}
    assert report["scenario_count"] == 24
    assert report["pass_count"] == 24


def test_expansion_wave3_design_is_oracle_valid_but_not_promotable():
    manifest = wave3.generate()
    report = verifier.verify(PILOT / "expansion_wave3")
    assert manifest["scenario_count"] == 24
    assert manifest["status"] == "mechanism_distinctness_review_pending_not_release"
    assert len(manifest["mechanisms"]) == 8
    assert report["scenario_count"] == 24
    assert report["pass_count"] == 24


def test_expansion_wave3_has_structural_delta_for_every_public_candidate():
    wave3.generate()
    report = distinctness.audit()
    assert report["scenario_count"] == 24
    assert report["structurally_distinct_count"] == 24
    assert report["all_structurally_distinct"] is True
    assert report["status"] == "review_required_not_release"


def test_expansion_wave3_semantic_review_is_explicitly_non_promotable():
    wave3.generate()
    review = __import__("json").loads((PILOT / "expansion_wave3" / "semantic_review.json").read_text())
    assert review["status"] == "public_calibration_promoted_not_release"
    assert review["promotion_allowed"] is False
    assert review["calibration_promotion_allowed"] is True
    assert set(review["constructs"]) == set(generator.CONSTRUCTS)
    assert "cross_world_promotion_8_templates_24_instances" in review["completed_public_gates"]


def test_wave4_design_is_complete_but_actor_runs_remain_disabled():
    report = wave4_design.audit()
    assert report["status"] == "design_valid_generation_pending"
    assert report["construct_count"] == 8
    assert report["unique_mechanism_count"] == 8
    assert report["unique_transition_count"] == 8
    assert report["actor_runs_authorized"] is False
    assert report["errors"] == []
