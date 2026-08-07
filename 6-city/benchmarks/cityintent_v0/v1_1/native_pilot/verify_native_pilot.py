#!/usr/bin/env python3
"""Two-sided acceptance verifier for the native v1.1 pilot."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V0_ROOT = ROOT.parents[1]
TOOLS = V0_ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
import run_baseline_traces as runner  # noqa: E402
from run_compliance_probe import run_oracle_trace  # noqa: E402


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def verify(
    root: Path = ROOT,
    config_path: Path | None = None,
    scenario_dir: Path | None = None,
    plans_path: Path | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    config_path = (config_path or root / "benchmark_config.json").resolve()
    scenario_dir = (scenario_dir or root / "scenarios").resolve()
    plans_path = (plans_path or root / "oracle_negative_plans.json").resolve()
    plans = {item["scenario_id"]: item for item in load_json(plans_path)}
    config = load_json(config_path)
    worlds = runner.load_worlds(config, config_path.parent)
    results = []
    for path in sorted(scenario_dir.glob("*.json")):
        scenario = load_json(path)
        plan = plans[scenario["scenario_id"]]
        oracle = run_oracle_trace(worlds[scenario["world_id"]], scenario, plan["oracle"])
        negative = run_oracle_trace(worlds[scenario["world_id"]], scenario, plan["negative"])
        om, nm = oracle["metrics"], negative["metrics"]
        headroom = round(float(om["task_completion"]) - float(nm["task_completion"]), 3)
        passed = om["task_completion"] == 1.0 and om["trace_feasibility"] == 1.0 and not oracle["violations"] and headroom >= .15
        results.append({
            "scenario_id": scenario["scenario_id"], "construct_family": plan["construct_family"], "passed": passed,
            "oracle_task_completion": om["task_completion"], "oracle_trace_feasibility": om["trace_feasibility"],
            "oracle_violations": len(oracle["violations"]), "negative_task_completion": nm["task_completion"],
            "negative_trace_feasibility": nm["trace_feasibility"], "headroom": headroom,
        })
    return {"scenario_count": len(results), "pass_count": sum(item["passed"] for item in results), "all_passed": all(item["passed"] for item in results), "results": results}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--scenario-dir", type=Path)
    parser.add_argument("--plans", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify(args.root, args.config, args.scenario_dir, args.plans)
    output = (args.output or args.root / "acceptance_report.json").resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("scenario_count", "pass_count", "all_passed")}, sort_keys=True))
    raise SystemExit(0 if report["all_passed"] else 1)
