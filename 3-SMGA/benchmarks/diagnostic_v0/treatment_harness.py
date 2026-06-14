#!/usr/bin/env python3
"""Build M2_memory_only and M3_actionable prompt bundles from a memory artifact.

Both conditions receive the SAME model-formed memory candidate set (the matched-
candidate rule, schema v0.1 §13). They differ only in serialization:
- M2_memory_only: the memories as plain-text notes.
- M3_actionable: the same memories as structured objects (types, currency status,
  evidence links) plus a planning contract over their affordances.

So M3-vs-M2 isolates the benefit of actionable structure; M3/M2-vs-M0 tests the
overall SMGA benefit. Neither condition sees probes' gold facts or success
conditions (the memories were formed condition-blind upstream).

Usage:
    python3 treatment_harness.py seeds/seed_0001 tmp/smga_memory/seed_0001_memory_artifact.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from baseline_harness import build_response_template
from benchmark_loader import load_seed

CONDITIONS = ("M2_memory_only", "M3_actionable")


def serialize_m2(memories: list[dict[str, Any]]) -> str:
    lines = []
    for m in memories:
        contra = m.get("contradicting_evidence_ids") or []
        contra_text = f" [revised/contradicted by: {', '.join(contra)}]" if contra else ""
        ev = ", ".join(m.get("supporting_evidence_ids", []) or [])
        lines.append(f"- {m.get('claim','')} (Evidence: {ev}; status: {m.get('currency_status')}){contra_text}")
    return "\n".join(lines)


def serialize_m3(memories: list[dict[str, Any]]) -> str:
    compact = []
    for m in memories:
        compact.append({
            "memory_id": m.get("memory_id"),
            "memory_type": m.get("memory_type"),
            "claim": m.get("claim"),
            "currency_status": m.get("currency_status"),
            "supporting_evidence_ids": m.get("supporting_evidence_ids", []),
            "contradicting_evidence_ids": m.get("contradicting_evidence_ids", []),
            "planning_affordances": [
                {
                    "affordance_type": a.get("affordance_type"),
                    "target_entities": a.get("target_entities", []),
                    "suggested_context": a.get("suggested_context"),
                }
                for a in (m.get("planning_affordances", []) or [])
            ],
        })
    return json.dumps(compact, ensure_ascii=False, indent=2)


SYSTEM_M2 = (
    "You are answering a social-planning probe using a set of prepared memory notes "
    "about past interactions. Use only these notes; do not invent new facts. "
    "Return valid JSON with exactly two keys: probe_id and response_text."
)
SYSTEM_M3 = (
    "You are answering a social-planning probe using structured social memories. Each "
    "memory has a currency_status and attached planning_affordances (candidate actions "
    "with target entities). Choose your next action from the affordances of the relevant "
    "memories, respect currency_status (never act on a contradicted/superseded claim as "
    "if it were current), and ground your choice in the memories. Use only these memories; "
    "do not invent new facts. Return valid JSON with exactly two keys: probe_id and response_text."
)


def build_user_prompt(condition: str, memory_block: str, probe: dict[str, Any]) -> str:
    header = (
        "Structured social memories (typed, with currency status and planning affordances):"
        if condition == "M3_actionable"
        else "Memory notes:"
    )
    parts = [
        f"Condition: {condition}",
        header,
        memory_block,
    ]
    if condition == "M3_actionable":
        parts.append(
            "Planning contract: select your next action from the planning_affordances of the "
            "relevant memories; respect each memory's currency_status; briefly say which memory "
            "and affordance you relied on."
        )
    parts += [
        "Probe:",
        str(probe["prompt"]),
        "Output JSON:",
        json.dumps({"probe_id": probe["probe_id"], "response_text": "your answer here"}, ensure_ascii=False),
    ]
    return "\n\n".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build M2/M3 prompt bundles from a memory artifact.")
    parser.add_argument("seed_dir", type=Path)
    parser.add_argument("memory_artifact", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("tmp/smga_treatment"))
    args = parser.parse_args()

    package = load_seed(args.seed_dir)
    artifact = json.loads(args.memory_artifact.read_text(encoding="utf-8"))
    memories = artifact.get("memories", [])
    probes = json.loads((args.seed_dir / "probes.json").read_text(encoding="utf-8")).get("probes", [])

    serializers = {"M2_memory_only": serialize_m2, "M3_actionable": serialize_m3}
    systems = {"M2_memory_only": SYSTEM_M2, "M3_actionable": SYSTEM_M3}

    args.output_dir.mkdir(parents=True, exist_ok=True)
    for condition in CONDITIONS:
        memory_block = serializers[condition](memories)
        records = [
            {
                "probe_id": probe["probe_id"],
                "condition_id": condition,
                "scenario_id": package.scenario_id,
                "seed_id": package.seed_id,
                "system_prompt": systems[condition],
                "user_prompt": build_user_prompt(condition, memory_block, probe),
                "expected_raw_output_schema": {"probe_id": probe["probe_id"], "response_text": "..."},
            }
            for probe in probes
        ]
        prompts_path = args.output_dir / f"{package.seed_id}_{condition}_prompts.jsonl"
        with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        template_path = args.output_dir / f"{package.seed_id}_{condition}_responses.template.json"
        with template_path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(build_response_template(package, condition), f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"{condition}: {len(records)} prompts -> {prompts_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
