"""Two-sided verification for the social_outcome_hard scenario family.

The hard tier exists because a good execution scaffold (ReAct) saturates the
base `social_outcome` family at 21/21 accepted co-presence outcomes: without
headroom, a model/backbone sweep cannot discriminate. Each hard scenario is
therefore verified in BOTH directions through the real executor + verifier:

  Positive control (fairness): a hand-authored oracle plan must reach
    task_completion == 1.0, trace_feasibility == 1.0, zero violations, with
    accepted evidence for every outcome — the scenario is winnable.

  Negative control (difficulty): a *plausible greedy/reactive* plan — the
    natural nearest-first / salience-first / stale-memory play — must score
    task_completion < 1.0. The difficulty mechanism is proven, not asserted.

Difficulty mechanisms (one per scenario):
  hard_three_meeting_relay   sequencing relay; nearest-first forfeits window 1
  hard_budget_entangled_meet irreversible side purchase starves the paid wait
  hard_deadline_then_meet    far deadline first beats near social salient
  hard_stale_plan_override   fresh public update must beat remembered plan
  hard_full_evening_chain    meal duration bridges into the window; early exit fails
  hard_overlapping_windows   far window closes first; near-first play loses it
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
    REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1"
    / "social_outcome_hard_family_oracle"
)

# sid -> {oracle, greedy, mechanism}
PLANS: dict[str, dict[str, Any]] = {
    "hard_three_meeting_relay": {
        "mechanism": "sequencing relay: windows open in strict order; nearest-first play forfeits the first window",
        "oracle": [
            # office->park is 25' via city_hall/market, so the relay runs 2'
            # earlier than the naive 27' route; the paid buys bridge exactly
            # onto each window opening (12:50 and 13:15).
            {"kind": "move", "target": "park"},
            {"kind": "enter", "target": "park"},
            {"kind": "interact", "to": "casey", "minutes": 2},
            {"kind": "move", "target": "market"},
            {"kind": "enter", "target": "market"},
            {"kind": "buy", "target": "market", "item": "groceries", "minutes": 13},
            {"kind": "interact", "to": "dana", "minutes": 2},
            {"kind": "move", "target": "budget_diner"},
            {"kind": "enter", "target": "budget_diner"},
            {"kind": "buy", "target": "budget_diner", "item": "snack", "minutes": 19},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "finish"},
        ],
        "greedy": [
            # nearest-first: market is 17' from the office; waiting there for
            # dana's window means the park window (closes 12:40) is forfeited.
            {"kind": "move", "target": "market"},
            {"kind": "enter", "target": "market"},
            {"kind": "buy", "target": "market", "item": "groceries", "minutes": 33},
            {"kind": "interact", "to": "dana", "minutes": 2},
            {"kind": "move", "target": "park"},
            {"kind": "enter", "target": "park"},
            {"kind": "interact", "to": "casey", "minutes": 2},
            {"kind": "move", "target": "budget_diner"},
            {"kind": "enter", "target": "budget_diner"},
            {"kind": "buy", "target": "budget_diner", "item": "snack", "minutes": 5},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "finish"},
        ],
    },
    "hard_budget_entangled_meet": {
        "mechanism": "irreversible budget entanglement: a routine side purchase makes the required paid wait unaffordable",
        "oracle": [
            {"kind": "move", "target": "pharmacy"},
            {"kind": "enter", "target": "pharmacy"},
            {"kind": "buy", "target": "pharmacy", "item": "medicine", "minutes": 5},
            {"kind": "move", "target": "quiet_cafe"},
            {"kind": "enter", "target": "quiet_cafe"},
            {"kind": "buy", "target": "quiet_cafe", "item": "tea", "minutes": 9},
            {"kind": "interact", "to": "casey", "minutes": 2},
            {"kind": "move", "target": "home_aria"},
            {"kind": "enter", "target": "home_aria"},
            {"kind": "finish"},
        ],
        "greedy": [
            {"kind": "move", "target": "market"},
            {"kind": "enter", "target": "market"},
            {"kind": "buy", "target": "market", "item": "groceries", "minutes": 5},
            {"kind": "move", "target": "pharmacy"},
            {"kind": "enter", "target": "pharmacy"},
            {"kind": "buy", "target": "pharmacy", "item": "medicine", "minutes": 5},
            {"kind": "move", "target": "quiet_cafe"},
            {"kind": "enter", "target": "quiet_cafe"},
            {"kind": "buy", "target": "quiet_cafe", "item": "tea", "minutes": 9},
            {"kind": "interact", "to": "casey", "minutes": 2},
            {"kind": "move", "target": "home_aria"},
            {"kind": "finish"},
        ],
    },
    "hard_deadline_then_meet": {
        "mechanism": "non-greedy ordering under a hard deadline: far task first, social salient second",
        "oracle": [
            {"kind": "move", "target": "pharmacy"},
            {"kind": "enter", "target": "pharmacy"},
            {"kind": "use_service", "target": "pharmacy", "service": "prescription_pickup", "minutes": 5},
            {"kind": "move", "target": "quiet_cafe"},
            {"kind": "enter", "target": "quiet_cafe"},
            {"kind": "buy", "target": "quiet_cafe", "item": "tea", "minutes": 14},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "finish"},
        ],
        "greedy": [
            {"kind": "move", "target": "quiet_cafe"},
            {"kind": "enter", "target": "quiet_cafe"},
            {"kind": "move", "target": "pharmacy"},
            {"kind": "enter", "target": "pharmacy"},
            {"kind": "use_service", "target": "pharmacy", "service": "prescription_pickup", "minutes": 5},
            {"kind": "move", "target": "quiet_cafe"},
            {"kind": "enter", "target": "quiet_cafe"},
            {"kind": "buy", "target": "quiet_cafe", "item": "tea", "minutes": 10},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "finish"},
        ],
    },
    "hard_stale_plan_override": {
        "mechanism": "stale-memory override: a fresh public update must beat a remembered arrangement",
        "oracle": [
            {"kind": "dwell", "minutes": 5},
            {"kind": "message", "to": "ben", "content": "Got it — quiet cafe now, on my way."},
            {"kind": "move", "target": "quiet_cafe"},
            {"kind": "enter", "target": "quiet_cafe"},
            {"kind": "buy", "target": "quiet_cafe", "item": "tea", "minutes": 1},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "finish"},
        ],
        "greedy": [
            {"kind": "dwell", "minutes": 40},
            {"kind": "message", "to": "ben", "content": "See you at the plaza at one."},
            {"kind": "move", "target": "plaza"},
            {"kind": "enter", "target": "plaza"},
            {"kind": "dwell", "minutes": 20},
            {"kind": "finish"},
        ],
    },
    "hard_full_evening_chain": {
        "mechanism": "four-outcome chain: the meal duration is the bridge into the social window; salience-first play exits early",
        "oracle": [
            {"kind": "move", "target": "market"},
            {"kind": "enter", "target": "market"},
            {"kind": "buy", "target": "market", "item": "groceries", "minutes": 5},
            {"kind": "move", "target": "budget_diner"},
            {"kind": "enter", "target": "budget_diner"},
            {"kind": "use_service", "target": "budget_diner", "service": "meal", "minutes": 13},
            {"kind": "interact", "to": "casey", "minutes": 2},
            {"kind": "move", "target": "home_aria"},
            {"kind": "enter", "target": "home_aria"},
            {"kind": "finish"},
        ],
        "greedy": [
            {"kind": "move", "target": "budget_diner"},
            {"kind": "enter", "target": "budget_diner"},
            {"kind": "use_service", "target": "budget_diner", "service": "meal", "minutes": 13},
            {"kind": "move", "target": "market"},
            {"kind": "enter", "target": "market"},
            {"kind": "buy", "target": "market", "item": "groceries", "minutes": 5},
            {"kind": "move", "target": "home_aria"},
            {"kind": "enter", "target": "home_aria"},
            {"kind": "finish"},
        ],
    },
    "hard_overlapping_windows": {
        "mechanism": "overlapping windows, far-closes-first: the near already-reachable option is the trap",
        "oracle": [
            {"kind": "move", "target": "park"},
            {"kind": "enter", "target": "park"},
            {"kind": "interact", "to": "casey", "minutes": 2},
            {"kind": "move", "target": "cafe_central"},
            {"kind": "enter", "target": "cafe_central"},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "finish"},
        ],
        "greedy": [
            {"kind": "move", "target": "cafe_central"},
            {"kind": "enter", "target": "cafe_central"},
            {"kind": "buy", "target": "cafe_central", "item": "coffee", "minutes": 29},
            {"kind": "interact", "to": "ben", "minutes": 2},
            {"kind": "move", "target": "park"},
            {"kind": "enter", "target": "park"},
            {"kind": "interact", "to": "casey", "minutes": 2},
            {"kind": "finish"},
        ],
    },
}


def verify_scenario(world: rbt.CityWorld, scenario_id: str) -> dict[str, Any]:
    scenario = load_json(SCENARIO_DIR / f"{scenario_id}.json")
    plan = PLANS[scenario_id]

    pos = run_oracle_trace(world, scenario, plan["oracle"])
    pm = pos["metrics"]
    outcomes = [c for c in pos["conditions"] if c["role"] == "outcome"]
    evidenced = all(c["score"] >= 1.0 and c["evidence"] for c in outcomes)
    oracle_passed = (
        pm.get("task_completion") == 1.0
        and pm.get("trace_feasibility") == 1.0
        and not pos["violations"]
        and evidenced
    )

    neg = run_oracle_trace(world, scenario, plan["greedy"])
    nm = neg["metrics"]
    greedy_task = nm.get("task_completion") or 0.0
    greedy_failed = greedy_task < 1.0

    return {
        "scenario_id": scenario_id,
        "mechanism": plan["mechanism"],
        "passed": oracle_passed and greedy_failed,
        "oracle": {
            "task_completion": pm.get("task_completion"),
            "trace_feasibility": pm.get("trace_feasibility"),
            "violations": len(pos["violations"]),
            "outcomes_evidenced": evidenced,
            "final_time": pos["final_time"],
            "final_budget": pos["final_budget"],
        },
        "greedy": {
            "task_completion": greedy_task,
            "trace_feasibility": nm.get("trace_feasibility"),
            "violations": len(neg["violations"]),
            "final_time": neg["final_time"],
            "final_budget": neg["final_budget"],
        },
        "headroom": round(1.0 - greedy_task, 3),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    world = rbt.CityWorld(load_json(WORLD_PATH))
    results = [verify_scenario(world, sid) for sid in PLANS]
    all_passed = all(r["passed"] for r in results)

    report = {
        "verifier": "social_outcome_hard_family_two_sided",
        "generated": datetime.now(timezone.utc).isoformat(),
        "family": "social_outcome_hard",
        "scenario_count": len(results),
        "all_passed": all_passed,
        "scenarios": results,
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "social_outcome_hard_family_report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print("=== Social-Outcome HARD Family — Two-Sided Verification ===")
    for r in results:
        status = "PASS" if r["passed"] else "FAIL"
        print(f"\n[{status}] {r['scenario_id']}")
        print(f"  oracle: task={r['oracle']['task_completion']} feas={r['oracle']['trace_feasibility']} "
              f"viol={r['oracle']['violations']} evidenced={r['oracle']['outcomes_evidenced']} "
              f"end={r['oracle']['final_time']} budget={r['oracle']['final_budget']}")
        print(f"  greedy: task={r['greedy']['task_completion']} (headroom {r['headroom']}) "
              f"end={r['greedy']['final_time']} budget={r['greedy']['final_budget']}")
        print(f"  mechanism: {r['mechanism']}")
    print(f"\nALL PASSED: {all_passed}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
