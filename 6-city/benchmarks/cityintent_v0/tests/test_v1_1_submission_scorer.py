import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "v1_1" / "submission" / "score_submission.py"
SPEC = importlib.util.spec_from_file_location("cityintent_v1_1_score_submission", MODULE_PATH)
assert SPEC and SPEC.loader
scorer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = scorer
SPEC.loader.exec_module(scorer)


def test_replay_scores_actions_instead_of_accepting_self_report():
    scenario_path = sorted((ROOT / "v1_1" / "scenarios" / "examples").glob("*.json"))[0]
    scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
    config = scorer.load_json(ROOT / "v1_1" / "benchmark_config.json")
    worlds = scorer.runner.load_worlds(config, ROOT / "v1_1")
    baseline = scorer.runner.run_trace(worlds[scenario["world_id"]], scenario, "utility_planner")
    actions = [entry["action"] for entry in baseline["trace"]]
    replayed = scorer.replay_episode(worlds[scenario["world_id"]], scenario, actions)
    assert replayed["metrics"]["task_completion"] == baseline["metrics"]["task_completion"]


def test_contract_rejects_self_reported_metrics():
    scenario_path = sorted((ROOT / "v1_1" / "scenarios" / "examples").glob("*.json"))[0]
    scenario = json.loads(scenario_path.read_text(encoding="utf-8"))
    row = {key: None for key in scorer.REQUIRED_TOP_LEVEL}
    row.update({"scenario_id": scenario["scenario_id"], "benchmark_version": "1.1.0", "split_hash": "0" * 64, "actions": [], "metrics": {"task_completion": 1.0}})
    with pytest.raises(scorer.SubmissionError, match="forbidden or unknown fields"):
        scorer.validate_episode_contract(row, scenario, "0" * 64)
