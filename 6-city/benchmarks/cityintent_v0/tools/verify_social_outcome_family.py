"""Oracle-winnability verification for the social-outcome scenario family.

The `social_outcome` family thickens the rc1 headline ("legal but ineffective":
frameworks stay feasible yet fail co-presence outcomes) from a single meeting
scenario into a family that varies coordination gating, window tightness,
multi-party ordering, a competing errand, and decoy-location discrimination.

Each scenario must be a *fair* test: winnable by a correct agent. This tool holds
the oracle winning plan for each on-disk scenario and drives it through the real
`execute_action` + `score_trace` (via `run_compliance_probe.run_oracle_trace`),
asserting task_completion == 1.0, trace_feasibility == 1.0, zero violations, and
an accepted co-presence interaction for every co_presence outcome.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
for extra in (ROOT, ROOT / "tools"):
    if str(extra) not in sys.path:
        sys.path.insert(0, str(extra))

import run_baseline_traces as rbt  # noqa: E402
from run_compliance_probe import load_json, run_oracle_trace  # noqa: E402

SCENARIO_DIR = ROOT / "scenarios"
WORLD_PATH = ROOT / "worlds" / "micro_city.json"
REPO_ROOT = ROOT.parents[2]
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1" / "social_outcome_family_oracle"
)

# Oracle winning plan per scenario (verified against the world graph + windows).
ORACLE_PLANS: dict[str, list[dict[str, Any]]] = {
    "social_copresence_open_meet": [
        {"kind": "move", "target": "park"},
        {"kind": "enter", "target": "park"},
        {"kind": "dwell", "minutes": 12},
        {"kind": "interact", "to": "casey", "minutes": 2},
        {"kind": "finish"},
    ],
    "social_copresence_message_gated": [
        {"kind": "message", "to": "ben", "content": "Ben, confirming quiet cafe at 12:40."},
        {"kind": "move", "target": "quiet_cafe"},
        {"kind": "enter", "target": "quiet_cafe"},
        {"kind": "buy", "target": "quiet_cafe", "item": "tea", "minutes": 12},
        {"kind": "interact", "to": "ben", "minutes": 2},
        {"kind": "finish"},
    ],
    "social_copresence_event_window": [
        {"kind": "move", "target": "market"},
        {"kind": "enter", "target": "market"},
        {"kind": "buy", "target": "market", "item": "groceries", "minutes": 9},
        {"kind": "interact", "to": "casey", "minutes": 2},
        {"kind": "finish"},
    ],
    "social_copresence_two_party": [
        {"kind": "move", "target": "park"},
        {"kind": "enter", "target": "park"},
        {"kind": "interact", "to": "casey", "minutes": 2},
        {"kind": "move", "target": "cafe_central"},
        {"kind": "enter", "target": "cafe_central"},
        {"kind": "buy", "target": "cafe_central", "item": "coffee", "minutes": 5},
        {"kind": "interact", "to": "ben", "minutes": 2},
        {"kind": "finish"},
    ],
    "social_copresence_with_errand": [
        {"kind": "move", "target": "pharmacy"},
        {"kind": "enter", "target": "pharmacy"},
        {"kind": "buy", "target": "pharmacy", "item": "medicine", "minutes": 5},
        {"kind": "move", "target": "market"},
        {"kind": "enter", "target": "market"},
        {"kind": "interact", "to": "casey", "minutes": 2},
        {"kind": "finish"},
    ],
    "social_copresence_decoy_location": [
        {"kind": "message", "to": "ben", "content": "Ben, meeting you at the quiet cafe."},
        {"kind": "move", "target": "quiet_cafe"},
        {"kind": "enter", "target": "quiet_cafe"},
        {"kind": "buy", "target": "quiet_cafe", "item": "tea", "minutes": 10},
        {"kind": "interact", "to": "ben", "minutes": 2},
        {"kind": "finish"},
    ],
}


def verify_scenario(world: rbt.CityWorld, scenario_id: str) -> dict[str, Any]:
    scenario = load_json(SCENARIO_DIR / f"{scenario_id}.json")
    trace = run_oracle_trace(world, scenario, ORACLE_PLANS[scenario_id])
    metrics = trace["metrics"]
    outcome_conditions = [c for c in trace["conditions"] if c["role"] == "outcome"]
    copresence_conditions = [c for c in outcome_conditions if c["type"] == "co_presence"]
    every_outcome_evidenced = all(
        c["score"] >= 1.0 and c["evidence"] for c in outcome_conditions
    )
    copresence_ok = bool(copresence_conditions) and all(
        c["score"] >= 1.0 and c["evidence"] for c in copresence_conditions
    )
    passed = (
        metrics.get("task_completion") == 1.0
        and metrics.get("trace_feasibility") == 1.0
        and not trace["violations"]
        and every_outcome_evidenced
        and copresence_ok
    )
    return {
        "scenario_id": scenario_id,
        "passed": passed,
        "task_completion": metrics.get("task_completion"),
        "trace_feasibility": metrics.get("trace_feasibility"),
        "constraint_satisfaction": metrics.get("constraint_satisfaction"),
        "violation_count": len(trace["violations"]),
        "co_presence_outcomes": len(copresence_conditions),
        "accepted_interactions": trace["interactions"],
        "final_time": trace["final_time"],
        "final_budget": trace["final_budget"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    world = rbt.CityWorld(load_json(WORLD_PATH))
    results = [verify_scenario(world, sid) for sid in ORACLE_PLANS]
    all_passed = all(r["passed"] for r in results)

    report = {
        "verifier": "social_outcome_family_oracle",
        "generated": datetime.now(timezone.utc).isoformat(),
        "family": "social_outcome",
        "scenario_count": len(results),
        "all_passed": all_passed,
        "scenarios": results,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "social_outcome_family_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=== Social-Outcome Family Oracle Verification ===")
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"[{status}] {r['scenario_id']}: task={r['task_completion']} "
              f"feas={r['trace_feasibility']} co_presence_outcomes={r['co_presence_outcomes']} "
              f"interactions={len(r['accepted_interactions'])} viol={r['violation_count']}")
    print(f"\nALL PASSED: {all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
