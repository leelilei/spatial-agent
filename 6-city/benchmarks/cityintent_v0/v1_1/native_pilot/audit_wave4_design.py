#!/usr/bin/env python3
"""Audit Wave-4 mechanism design completeness before scenario generation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
DESIGN = ROOT / "wave4_mechanism_design.json"


def audit(path: Path = DESIGN) -> dict[str, Any]:
    design = json.loads(path.read_text(encoding="utf-8"))
    rows = design["constructs"]
    mechanism_ids = [row["mechanism_id"] for row in rows.values()]
    transitions = [row["state_transition"] for row in rows.values()]
    errors = []
    if len(rows) != 8:
        errors.append("expected_eight_constructs")
    if len(set(mechanism_ids)) != len(mechanism_ids):
        errors.append("duplicate_mechanism_id")
    if len(set(transitions)) != len(transitions):
        errors.append("duplicate_state_transition")
    for construct, row in rows.items():
        if set(row["novelty_against"]) != {"base", "wave2", "wave3"}:
            errors.append(f"incomplete_novelty_contract:{construct}")
        if not row["required_actions"] or not row["required_conditions"]:
            errors.append(f"missing_evidence_contract:{construct}")
        if not row["negative_failure"]:
            errors.append(f"missing_negative_failure:{construct}")
    return {
        "status": "design_valid_generation_pending" if not errors else "design_rejected",
        "construct_count": len(rows),
        "unique_mechanism_count": len(set(mechanism_ids)),
        "unique_transition_count": len(set(transitions)),
        "actor_runs_authorized": bool(design["actor_runs_authorized"]),
        "errors": errors,
    }


if __name__ == "__main__":
    print(json.dumps(audit(), sort_keys=True))
