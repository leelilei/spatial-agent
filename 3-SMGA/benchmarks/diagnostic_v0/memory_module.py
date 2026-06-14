#!/usr/bin/env python3
"""SMGA memory-formation module (Module A) for Experiment 0.

Condition-blind: a model reads only the entity catalog + scripted event history
(the same history the M0 baselines see) and distills StructuredSocialMemory
objects per docs/project/smga_memory_schema_v0.1.md. It never sees probes, gold
facts, or success conditions, so it cannot leak the answer.

The formed memory artifact becomes the shared candidate set for M2_memory_only
and M3_actionable. Output is validated against the frozen schema enums and the
scenario's entity/event IDs.

Usage:
    FHL_API_KEY=... python3 memory_module.py seeds/seed_0001 \
        --config configs/fhl_responses_gpt54_config.example.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from baseline_harness import format_entity_catalog, format_event_history
from benchmark_loader import load_seed

HERE = Path(__file__).resolve().parent

MEMORY_TYPES = {
    "relationship_memory", "commitment_memory", "reputation_memory",
    "secret_or_privacy_memory", "norm_memory", "preference_memory",
    "routine_memory", "information_ownership_memory", "conflict_or_repair_memory",
}
CURRENCY_STATUS = {"current", "revised", "contradicted", "stale", "superseded", "uncertain"}
AFFORDANCE_TYPES = {
    "seek_contact", "avoid_contact", "seek_information", "share_information",
    "repair_relationship", "maintain_privacy", "choose_collaboration_context", "follow_commitment",
}

FORMATION_SYSTEM_PROMPT = (
    "You are SMGA's memory-formation module. You read a scripted event history of "
    "social interactions among several people and distill it into a small set of "
    "STRUCTURED SOCIAL MEMORY objects that a planner could later reuse. You are NOT "
    "given any task, question, or probe; form general-purpose social memories only. "
    "Ground every memory in event IDs from the history. When a later event breaks, "
    "revises, narrows, or supersedes an earlier fact, mark its currency_status "
    "accordingly and link the contradicting event — never present an outdated claim "
    "as current. Return ONLY a single JSON object, no prose."
)


def build_formation_user_prompt(entity_catalog: str, event_history: str) -> str:
    schema = (
        "Produce 6-10 structured social memories covering the salient social facts "
        "(relationships, commitments, secrets/privacy, norms, routines, reputation, "
        "conflicts/repairs). Each memory object has these fields:\n"
        "  memory_id: smem_0001, smem_0002, ...\n"
        f"  memory_type: one of {sorted(MEMORY_TYPES)}\n"
        "  subject_entities: list of entity_ids from the catalog\n"
        "  claim: one atomic natural-language social claim\n"
        "  supporting_evidence_ids: list of event_ids that support the claim\n"
        "  contradicting_evidence_ids: list of event_ids that revise/contradict it ([] if none)\n"
        "  validity_scope: {time_window: string, contexts: [entity_ids]}\n"
        f"  currency_status: one of {sorted(CURRENCY_STATUS)}\n"
        "  planning_affordances: list of {affordance_type, target_entities, suggested_context, supporting_evidence_ids}\n"
        f"    where affordance_type is one of {sorted(AFFORDANCE_TYPES)}\n"
        'Output ONLY: {"memories": [ ... ]}'
    )
    return "\n\n".join([
        "Entity catalog:", entity_catalog,
        "Scripted event history:", event_history,
        "Task:", schema,
    ])


def run_formation(prompts_path: Path, config: Path, output_dir: Path) -> Path:
    cmd = [
        sys.executable, str(HERE / "model_calling_runner.py"), str(prompts_path),
        "--config", str(config), "--output-dir", str(output_dir),
    ]
    subprocess.run(cmd, check=True, cwd=str(HERE))
    candidates = sorted(output_dir.glob("*_raw_outputs.jsonl"))
    if not candidates:
        raise FileNotFoundError(f"no raw_outputs in {output_dir}")
    return candidates[-1]


def extract_memories(raw_path: Path) -> list[dict[str, Any]]:
    with raw_path.open(encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            parsed = rec.get("parsed_response_json")
            if isinstance(parsed, dict) and isinstance(parsed.get("memories"), list):
                return parsed["memories"]
            raw = rec.get("raw_response_text", "")
            try:
                obj = json.loads(raw)
                if isinstance(obj, dict) and isinstance(obj.get("memories"), list):
                    return obj["memories"]
            except json.JSONDecodeError:
                pass
    return []


def validate(memories: list[dict[str, Any]], entity_ids: set[str], event_ids: set[str]) -> list[str]:
    issues: list[str] = []
    required = ["memory_id", "memory_type", "subject_entities", "claim",
                "supporting_evidence_ids", "validity_scope", "currency_status"]
    for i, m in enumerate(memories):
        tag = m.get("memory_id", f"#{i}")
        for field in required:
            if field not in m:
                issues.append(f"{tag}: missing {field}")
        if m.get("memory_type") not in MEMORY_TYPES:
            issues.append(f"{tag}: bad memory_type {m.get('memory_type')!r}")
        if m.get("currency_status") not in CURRENCY_STATUS:
            issues.append(f"{tag}: bad currency_status {m.get('currency_status')!r}")
        for e in m.get("subject_entities", []) or []:
            if e not in entity_ids:
                issues.append(f"{tag}: subject entity not in catalog: {e}")
        for ev in (m.get("supporting_evidence_ids", []) or []) + (m.get("contradicting_evidence_ids", []) or []):
            if ev not in event_ids:
                issues.append(f"{tag}: evidence id not in event log: {ev}")
        for aff in m.get("planning_affordances", []) or []:
            if aff.get("affordance_type") not in AFFORDANCE_TYPES:
                issues.append(f"{tag}: bad affordance_type {aff.get('affordance_type')!r}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="SMGA memory-formation module (Module A).")
    parser.add_argument("seed_dir", type=Path)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    package = load_seed(args.seed_dir)
    entity_ids = {str(e.get("entity_id")) for e in package.entities}
    event_ids = {str(ev.get("event_id")) for ev in package.events}

    out_dir = args.output_dir or (HERE / "tmp" / "smga_memory")
    out_dir.mkdir(parents=True, exist_ok=True)

    prompt_record = {
        "probe_id": "memory_formation",
        "system_prompt": FORMATION_SYSTEM_PROMPT,
        "user_prompt": build_formation_user_prompt(
            format_entity_catalog(package), format_event_history(package)
        ),
        "expected_raw_output_schema": {"memories": []},
    }
    prompts_path = out_dir / f"{package.seed_id}_memory_formation_prompts.jsonl"
    with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(prompt_record, ensure_ascii=False) + "\n")

    raw = run_formation(prompts_path, args.config, out_dir)
    memories = extract_memories(raw)
    if not memories:
        print("error: no memories parsed from model output", file=sys.stderr)
        return 1

    issues = validate(memories, entity_ids, event_ids)
    artifact = {
        "scenario_id": package.scenario_id,
        "seed_id": package.seed_id,
        "source": "memory_module.py (Module A, model-formed, condition-blind)",
        "memory_count": len(memories),
        "validation_issues": issues,
        "memories": memories,
    }
    artifact_path = out_dir / f"{package.seed_id}_memory_artifact.json"
    with artifact_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(artifact, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nformed {len(memories)} memories -> {artifact_path}")
    print(f"validation issues: {len(issues)}")
    for issue in issues:
        print(f"  - {issue}")
    print("\nmemory summary:")
    for m in memories:
        affs = ",".join(a.get("affordance_type", "?") for a in m.get("planning_affordances", []) or [])
        print(f"  {m.get('memory_id')} [{m.get('memory_type')}/{m.get('currency_status')}] "
              f"ev={m.get('supporting_evidence_ids')} contra={m.get('contradicting_evidence_ids') or []} aff=[{affs}]")
        print(f"     {m.get('claim','')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
