import importlib.util
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "v1_1" / "generate_scenarios.py"
SPEC = importlib.util.spec_from_file_location("cityintent_v1_1_generate_scenarios", MODULE_PATH)
assert SPEC and SPEC.loader
scenariogen = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scenariogen
SPEC.loader.exec_module(scenariogen)


def test_candidate_matrix_meets_declared_scale_and_balance():
    candidates = scenariogen.build_candidates()
    assert len(candidates) == 144
    assert len({item["scenario_id"] for item in candidates}) == 144
    assert Counter(item["benchmark_metadata"]["split"] for item in candidates) == {
        "examples": 24,
        "development": 36,
        "public_test": 36,
        "private_test": 48,
    }
    assert set(Counter(item["benchmark_metadata"]["construct_family"] for item in candidates).values()) == {18}
    assert Counter(item["benchmark_metadata"]["difficulty_tier"] for item in candidates) == {
        "easy": 48,
        "medium": 48,
        "hard": 48,
    }


def test_private_worlds_never_appear_in_public_splits():
    for item in scenariogen.build_candidates():
        metadata = item["benchmark_metadata"]
        assert (metadata["split"] == "private_test") == (metadata["world_visibility"] == "private")
        assert metadata["candidate_status"] == "pending_acceptance_gates"
