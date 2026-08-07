#!/usr/bin/env python3
"""Audit Wave-4 mechanism novelty against every prior public mechanism pool.

The Wave-4 design contract claims novelty against Base, Wave-2 and Wave-3, so
this audit is stronger than the Wave-3 pairwise check: a Wave-4 candidate must
differ structurally from *every* prior candidate in the same construct family,
not only from its same-id predecessor.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
PRIOR_POOLS = {
    "base": ROOT / "scenarios",
    "wave1": ROOT / "expansion_wave1" / "scenarios",
    "wave2": ROOT / "expansion_wave2" / "scenarios",
    "wave3": ROOT / "expansion_wave3" / "scenarios",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def signature(row: dict[str, Any]) -> dict[str, Any]:
    """Structural fingerprint of the item's state/evidence contract."""
    return {
        "event_types": sorted(str(event.get("type")) for event in row.get("events", [])),
        "condition_types": sorted(
            str(condition.get("type")) for condition in row.get("success_conditions", [])
        ),
        "conditions": sorted(
            json.dumps(
                {
                    key: value for key, value in condition.items()
                    if key not in {"weight", "role"}
                },
                sort_keys=True,
                ensure_ascii=False,
            )
            for condition in row.get("success_conditions", [])
        ),
        "memory_seed_count": sum(
            len(agent.get("memory_seeds", [])) for agent in row.get("agents", [])
        ),
        "agent_count": len(row.get("agents", [])),
    }


def comparable(sig: dict[str, Any]) -> str:
    """Order-insensitive key used for equality against prior mechanisms."""
    return json.dumps(sig, sort_keys=True, ensure_ascii=False)


def audit(wave4_root: Path = ROOT / "expansion_wave4") -> dict[str, Any]:
    prior: dict[str, list[dict[str, Any]]] = {}
    for pool, directory in PRIOR_POOLS.items():
        for path in sorted(directory.glob("*.json")):
            row = load(path)
            prior.setdefault(row["family"], []).append({
                "pool": pool,
                "scenario_id": row["scenario_id"],
                "signature": comparable(signature(row)),
                "condition_types": sorted(
                    str(condition.get("type")) for condition in row.get("success_conditions", [])
                ),
            })

    results = []
    for path in sorted((wave4_root / "scenarios").glob("*.json")):
        row = load(path)
        family = row["family"]
        current = signature(row)
        key = comparable(current)
        collisions = [
            {"pool": item["pool"], "scenario_id": item["scenario_id"]}
            for item in prior.get(family, [])
            if item["signature"] == key
        ]
        # A shared condition-type set is allowed, but a Wave-4 mechanism should
        # introduce at least one evidence type no prior item in its family used.
        prior_types = {
            ctype for item in prior.get(family, []) for ctype in item["condition_types"]
        }
        novel_types = sorted(set(current["condition_types"]) - prior_types)
        results.append({
            "scenario_id": row["scenario_id"],
            "construct_family": family,
            "mechanism_id": row["benchmark_metadata"]["mechanism_id"],
            "prior_item_count": len(prior.get(family, [])),
            "structurally_distinct": not collisions,
            "collisions": collisions,
            "novel_condition_types": novel_types,
            "condition_types": current["condition_types"],
        })

    return {
        "scenario_count": len(results),
        "prior_pools": sorted(PRIOR_POOLS),
        "structurally_distinct_count": sum(row["structurally_distinct"] for row in results),
        "all_structurally_distinct": all(row["structurally_distinct"] for row in results),
        "families_with_novel_condition_type": sorted({
            row["construct_family"] for row in results if row["novel_condition_types"]
        }),
        "status": "review_required_not_release",
        "results": results,
    }


if __name__ == "__main__":
    report = audit()
    output = ROOT / "expansion_wave4" / "distinctness_audit.json"
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        key: report[key] for key in (
            "scenario_count", "structurally_distinct_count",
            "all_structurally_distinct", "families_with_novel_condition_type",
        )
    }, ensure_ascii=False))
