#!/usr/bin/env python3
"""LLM-judge scorer for SMGA diagnostic probes (condition-blind, substance-based).

Motivation: the rule-based probe_success_scorer matches literal keyword markers
and affordance labels, which penalizes substantively-correct answers that use
different wording. This judge evaluates each response by *meaning* against a
plain-language rubric derived from the locked success/failure conditions.

Design:
- Condition-blind: the judge never sees condition_id (M0_GA / M0_prompted / M3).
- It reuses the proven provider transport by running judge prompts through
  `model_calling_runner.py` (the only path that reliably reaches the provider).
- Each judge prompt = scenario probe + rubric + the agent's response, and asks
  for strict JSON {probe_id, pass, rationale}.

Usage:
    FHL_API_KEY=... python3 judge_scorer.py seeds/seed_0001 \
        tmp/fhl_gpt54_baseline/seed_0001_M0_GA_responses.raw_draft.json \
        --config configs/fhl_responses_gpt54_config.example.json
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent

AFFORDANCE_PHRASES = {
    "repair_relationship": "repair the relationship (apologize / make amends / rebuild trust)",
    "follow_commitment": "follow through on the missed or standing commitment",
    "seek_contact": "go find, reach, or contact the relevant person/place",
    "maintain_privacy": "keep the private information confidential",
    "avoid_contact": "back off and avoid further intrusion",
    "choose_collaboration_context": "make a deliberate collaboration / planning choice",
    "share_information": "share the information",
    "seek_information": "seek out more information",
    "ignore_commitment": "ignore the commitment",
}

STATUS_PHRASES = {
    "contradicted": "acknowledge that an earlier fact or commitment was broken / contradicted",
    "revised": "reflect the revised state (e.g. reduced trust, only partial repair)",
    "active": "reflect the currently-active fact",
    "expired": "treat the fact as no longer in force",
    "unknown": "acknowledge the information is uncertain",
}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def readable_entity(entity_id: str) -> str:
    for prefix in ("person_", "place_", "topic_", "norm_", "info_", "activity_", "rel_"):
        if entity_id.startswith(prefix):
            return entity_id[len(prefix):].replace("_", " ")
    return entity_id.replace("_", " ")


def build_rubric(probe: dict[str, Any]) -> str:
    sc = probe.get("success_condition", {})
    fc = probe.get("failure_condition", {})
    lines: list[str] = []

    affordances = [AFFORDANCE_PHRASES.get(a, a) for a in sc.get("acceptable_affordance_types", [])]
    if affordances:
        lines.append("- Choose an action whose intent is to: " + "; or ".join(affordances) + ".")

    targets = [readable_entity(t) for t in sc.get("required_target_entities", [])]
    if targets:
        lines.append("- The action should clearly involve / be directed at: " + ", ".join(targets) + ".")

    statuses = [STATUS_PHRASES.get(s, s) for s in sc.get("required_current_status", [])]
    if statuses:
        lines.append("- The reasoning should " + "; and ".join(statuses) + ".")

    key_points = sc.get("required_response_markers", [])
    if key_points:
        lines.append(
            "- Substantively (judge by MEANING, not exact words) the answer should address: "
            + ", ".join(f'"{k}"' for k in key_points)
            + f" (at least {sc.get('minimum_marker_count', 1)} of these ideas)."
        )

    forbidden_aff = [AFFORDANCE_PHRASES.get(a, a) for a in fc.get("forbidden_affordance_types", [])]
    if forbidden_aff:
        lines.append("- It must NOT choose an action whose intent is to: " + "; or ".join(forbidden_aff) + ".")

    forbidden_markers = fc.get("forbidden_response_markers", [])
    if forbidden_markers:
        lines.append(
            "- It must NOT take a stance equivalent to: "
            + "; ".join(f'"{m}"' for m in forbidden_markers)
            + "."
        )
    return "\n".join(lines)


JUDGE_SYSTEM_PROMPT = (
    "You are a strict, impartial evaluator of an AI social agent's decision in a "
    "scripted scenario. You do NOT know which system produced the answer; judge "
    "ONLY on the rubric and the answer's meaning, never on its wording or format. "
    "An answer PASSES only if it satisfies every rubric criterion in substance. "
    "Return strict JSON with exactly these keys: probe_id (string), pass (boolean), "
    "rationale (one short sentence)."
)


def build_judge_prompt_record(probe: dict[str, Any], response_text: str) -> dict[str, Any]:
    probe_id = probe["probe_id"]
    user_prompt = (
        f"Scenario probe:\n{probe.get('prompt', '')}\n\n"
        f"Rubric for an acceptable answer:\n{build_rubric(probe)}\n\n"
        f"Agent's answer to evaluate:\n\"\"\"\n{response_text}\n\"\"\"\n\n"
        f'Output JSON:\n{{"probe_id": "{probe_id}", "pass": true, "rationale": "..."}}'
    )
    return {
        "probe_id": probe_id,
        "system_prompt": JUDGE_SYSTEM_PROMPT,
        "user_prompt": user_prompt,
        "expected_raw_output_schema": {"probe_id": probe_id, "pass": True, "rationale": "..."},
    }


def run_runner(prompts_path: Path, config: Path, output_dir: Path) -> Path:
    cmd = [
        sys.executable,
        str(HERE / "model_calling_runner.py"),
        str(prompts_path),
        "--config",
        str(config),
        "--output-dir",
        str(output_dir),
    ]
    subprocess.run(cmd, check=True, cwd=str(HERE))
    raw = output_dir / f"{prompts_path.stem.replace('_prompts', '')}_raw_outputs.jsonl"
    if not raw.exists():
        # fall back to whatever *_raw_outputs.jsonl was produced
        candidates = sorted(output_dir.glob("*_raw_outputs.jsonl"))
        if not candidates:
            raise FileNotFoundError(f"no raw_outputs produced in {output_dir}")
        raw = candidates[-1]
    return raw


def parse_verdicts(raw_path: Path) -> dict[str, dict[str, Any]]:
    verdicts: dict[str, dict[str, Any]] = {}
    with raw_path.open(encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            pid = rec.get("probe_id")
            parsed = rec.get("parsed_response_json") or {}
            verdicts[pid] = {
                "pass": bool(parsed.get("pass")) if isinstance(parsed, dict) else False,
                "rationale": (parsed.get("rationale") if isinstance(parsed, dict) else "") or "",
                "status": rec.get("status"),
            }
    return verdicts


def main() -> int:
    parser = argparse.ArgumentParser(description="LLM-judge scorer for SMGA probes.")
    parser.add_argument("seed_dir", type=Path)
    parser.add_argument("responses_json", type=Path, help="Model responses (raw_draft or normalized).")
    parser.add_argument("--config", type=Path, required=True, help="Provider config for the judge model.")
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    probes_doc = load_json(args.seed_dir / "probes.json")
    responses_doc = load_json(args.responses_json)
    probes = {p["probe_id"]: p for p in probes_doc.get("probes", [])}
    responses = {
        r.get("probe_id"): str(r.get("response_text", ""))
        for r in responses_doc.get("responses", [])
        if isinstance(r, dict)
    }

    out_dir = args.output_dir or (args.responses_json.parent / "judge")
    out_dir.mkdir(parents=True, exist_ok=True)
    cond = responses_doc.get("condition_id", "cond")
    prompts_path = out_dir / f"{args.seed_dir.name}_{cond}_judge_prompts.jsonl"
    with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
        for pid, probe in probes.items():
            if pid not in responses:
                continue
            f.write(json.dumps(build_judge_prompt_record(probe, responses[pid]), ensure_ascii=False))
            f.write("\n")

    raw = run_runner(prompts_path, args.config, out_dir)
    verdicts = parse_verdicts(raw)

    headline = [pid for pid in probes if not probes[pid].get("no_history_solvability_flag")]
    passed = sum(1 for pid in headline if verdicts.get(pid, {}).get("pass"))
    total = len(headline)
    print(f"{cond} [LLM-judge]: {passed}/{total} headline probes passed ({passed / total:.1%})" if total else f"{cond}: no probes")
    for pid in probes:
        v = verdicts.get(pid, {})
        mark = "PASS" if v.get("pass") else "FAIL"
        print(f"  {pid}: {mark}  — {v.get('rationale', '(no verdict)')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
