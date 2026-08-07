#!/usr/bin/env python3
"""Audit structural mechanism differences between Wave-2 and Wave-3 candidates."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def signature(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "event_types": sorted(event.get("type") for event in row.get("events", [])),
        "conditions": sorted(
            json.dumps(
                {key: value for key, value in condition.items() if key not in {"weight", "role"}},
                sort_keys=True,
                ensure_ascii=False,
            )
            for condition in row.get("success_conditions", [])
        ),
        "oracle_kinds": [action.get("kind") for action in row.get("oracle", [])],
        "memory_seed_count": sum(len(agent.get("memory_seeds", [])) for agent in row.get("agents", [])),
    }


def audit(wave2_root: Path = ROOT / "expansion_wave2", wave3_root: Path = ROOT / "expansion_wave3") -> dict[str, Any]:
    old = {load(path)["scenario_id"].replace("ci11w2", ""): load(path) for path in (wave2_root / "scenarios").glob("*.json")}
    new_rows = [load(path) for path in (wave3_root / "scenarios").glob("*.json")]
    results = []
    for row in sorted(new_rows, key=lambda item: item["scenario_id"]):
        key = row["scenario_id"].replace("ci11w3", "")
        prior = old.get(key)
        current_sig = signature(row)
        prior_sig = signature(prior) if prior else None
        results.append({
            "scenario_id": row["scenario_id"],
            "construct_family": row["family"],
            "mechanism_id": row["benchmark_metadata"]["mechanism_id"],
            "structural_delta": current_sig != prior_sig,
            "current": current_sig,
            "wave2": prior_sig,
        })
    return {
        "scenario_count": len(results),
        "structurally_distinct_count": sum(item["structural_delta"] for item in results),
        "all_structurally_distinct": all(item["structural_delta"] for item in results),
        "status": "review_required_not_release",
        "results": results,
    }


if __name__ == "__main__":
    output = ROOT / "expansion_wave3" / "distinctness_audit.json"
    report = audit()
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("scenario_count", "structurally_distinct_count", "all_structurally_distinct", "status")}))
