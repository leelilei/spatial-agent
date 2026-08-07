#!/usr/bin/env python3
"""Replay available hand-authored v1.0 oracles on v1.1 world instances."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V0_ROOT = ROOT.parent
TOOLS = V0_ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import run_baseline_traces as runner  # noqa: E402
from run_compliance_probe import ORACLE_PLANS as COMPLIANCE_PLANS, run_oracle_trace  # noqa: E402
from verify_social_outcome_family import ORACLE_PLANS as SOCIAL_PLANS  # noqa: E402
from verify_social_outcome_hard_family import PLANS as HARD_PLANS  # noqa: E402


LOCATION_ROLE = {
    "home_aria": "home_primary", "home_ben": "home_friend", "office": "office",
    "transit_hub": "transit_hub", "plaza": "plaza", "cafe_central": "meeting_cafe",
    "quiet_cafe": "quiet_cafe", "library": "library", "coworking": "coworking",
    "city_hall": "civic_service", "park": "park", "gym": "gym", "market": "market",
    "pharmacy": "pharmacy", "clinic": "clinic", "budget_diner": "budget_food",
    "school": "school", "theatre": "culture", "bookstore": "bookstore",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def translate_actions(actions: list[dict[str, Any]], world_raw: dict[str, Any]) -> list[dict[str, Any]]:
    role_to_id = {location["semantic_role"]: location["id"] for location in world_raw["locations"]}
    id_map = {source_id: role_to_id[role] for source_id, role in LOCATION_ROLE.items()}
    translated = copy.deepcopy(actions)
    for action in translated:
        if action.get("target") in id_map:
            action["target"] = id_map[action["target"]]
        if action.get("path"):
            action["path"] = [id_map.get(node, node) for node in action["path"]]
    return translated


def source_plan(template_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]] | None, str | None] | None:
    if template_id in HARD_PLANS:
        plan = HARD_PLANS[template_id]
        return plan["oracle"], plan["greedy"], plan["mechanism"]
    if template_id in SOCIAL_PLANS:
        return SOCIAL_PLANS[template_id], None, None
    if template_id in COMPLIANCE_PLANS:
        return COMPLIANCE_PLANS[template_id]["actions"], None, COMPLIANCE_PLANS[template_id]["evidence_focus"]
    return None


def verify(root: Path = ROOT) -> dict[str, Any]:
    config = load_json(root / "benchmark_config.json")
    raw_worlds = {load_json(root / ref)["world_id"]: load_json(root / ref) for ref in config["worlds"]}
    worlds = {world_id: runner.CityWorld(raw) for world_id, raw in raw_worlds.items()}
    results = []
    for path in sorted((root / "scenarios").rglob("*.json")):
        scenario = load_json(path)
        template_id = scenario["benchmark_metadata"]["template_id"]
        plans = source_plan(template_id)
        if plans is None:
            continue
        oracle_actions, negative_actions, mechanism = plans
        world_raw = raw_worlds[scenario["world_id"]]
        oracle_trace = run_oracle_trace(worlds[scenario["world_id"]], scenario, translate_actions(oracle_actions, world_raw))
        om = oracle_trace["metrics"]
        outcomes = [condition for condition in oracle_trace["conditions"] if condition["role"] == "outcome"]
        oracle_passed = (
            om["task_completion"] == 1.0
            and om["trace_feasibility"] == 1.0
            and not oracle_trace["violations"]
            and all(condition["score"] >= 1.0 and condition["evidence"] for condition in outcomes)
        )
        negative = None
        negative_passed = False
        if negative_actions is not None:
            negative_trace = run_oracle_trace(worlds[scenario["world_id"]], scenario, translate_actions(negative_actions, world_raw))
            nm = negative_trace["metrics"]
            headroom = round(float(om["task_completion"]) - float(nm["task_completion"]), 3)
            negative_passed = headroom >= 0.15
            negative = {
                "task_completion": nm["task_completion"],
                "trace_feasibility": nm["trace_feasibility"],
                "headroom": headroom,
                "passed": negative_passed,
            }
        results.append(
            {
                "scenario_id": scenario["scenario_id"],
                "template_id": template_id,
                "world_id": scenario["world_id"],
                "mechanism": mechanism,
                "oracle_passed": oracle_passed,
                "oracle": {
                    "task_completion": om["task_completion"],
                    "trace_feasibility": om["trace_feasibility"],
                    "constraint_satisfaction": om["constraint_satisfaction"],
                    "violation_count": len(oracle_trace["violations"]),
                    "outcomes_evidenced": all(condition["score"] >= 1.0 and condition["evidence"] for condition in outcomes),
                },
                "negative_control_available": negative_actions is not None,
                "negative_control_passed": negative_passed,
                "negative_control": negative,
            }
        )
    return {
        "schema_version": "cityintent_oracle_evidence_v1",
        "benchmark_version": "1.1.0-candidate",
        "scenario_count": len(results),
        "oracle_pass_count": sum(item["oracle_passed"] for item in results),
        "negative_control_available_count": sum(item["negative_control_available"] for item in results),
        "negative_control_pass_count": sum(item["negative_control_passed"] for item in results),
        "template_counts": dict(sorted(Counter(item["template_id"] for item in results).items())),
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    report = verify(root)
    output = args.output.resolve() if args.output else root / "manifests" / "oracle_evidence.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("scenario_count", "oracle_pass_count", "negative_control_available_count", "negative_control_pass_count")}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
