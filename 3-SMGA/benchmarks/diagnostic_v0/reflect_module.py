#!/usr/bin/env python3
"""GA-faithful reflection module for the M0_GA_reflect baseline.

The original Generative Agents (Park et al. 2023) memory has a REFLECTION layer
our raw-log M0_GA baseline lacks: it periodically distills high-level insights from
the memory stream (insight_and_evidence prompt) and planning memos
(planning_thought_on_convo prompt), stored back as thought nodes. This module
reproduces that layer faithfully and is given GA's STRONGEST form: it may emit both
descriptive insights AND planning-relevant notes. It is condition-blind (never sees
probes), exactly like GA's reflection and like our SMGA memory module.

Crucially, GA reflections are FREE-TEXT, untyped, and carry no currency_status or
typed affordances — that is the contrast with SMGA's structured affordance memory.

Usage:
    FHL_API_KEY=... python3 reflect_module.py seeds/seed_0001 \
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

REFLECT_SYSTEM_PROMPT = (
    "You are a generative agent reflecting on your past social interactions, in the "
    "style of the Generative Agents memory-stream reflection step. From the event "
    "history you distill a small set of HIGH-LEVEL INSIGHTS about the people, their "
    "relationships, reliability, norms, and routines, plus any notes worth REMEMBERING "
    "FOR FUTURE PLANNING. You are NOT given any task, question, or probe; reflect in "
    "general. Insights are natural-language inferences grounded in the events; do not "
    "invent facts. Return ONLY a single JSON object, no prose."
)


def build_reflect_user_prompt(entity_catalog: str, event_history: str) -> str:
    schema = (
        "Infer 6-10 high-level reflections from the statements below. Each reflection "
        "is a single natural-language sentence; it may be a descriptive insight (e.g. "
        "what someone is like, how a relationship changed) or a planning note (what to "
        "keep in mind when working with them next). Ground them in the history; reflect "
        "the most current state when earlier facts were later revised.\n"
        'Output ONLY: {"insights": ["reflection 1", "reflection 2", ...]}'
    )
    return "\n\n".join([
        "Entity catalog:", entity_catalog,
        "Scripted event history:", event_history,
        "Task:", schema,
    ])


def run_reflection(prompts_path: Path, config: Path, output_dir: Path) -> Path:
    cmd = [
        sys.executable, str(HERE / "model_calling_runner.py"), str(prompts_path),
        "--config", str(config), "--output-dir", str(output_dir),
    ]
    subprocess.run(cmd, check=True, cwd=str(HERE))
    candidates = sorted(output_dir.glob("*_raw_outputs.jsonl"))
    if not candidates:
        raise FileNotFoundError(f"no raw_outputs in {output_dir}")
    return candidates[-1]


def extract_insights(raw_path: Path) -> list[str]:
    with raw_path.open(encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            for source in (rec.get("parsed_response_json"), _try_json(rec.get("raw_response_text", ""))):
                if isinstance(source, dict) and isinstance(source.get("insights"), list):
                    return [str(x) for x in source["insights"] if str(x).strip()]
    return []


def _try_json(raw: str) -> Any:
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description="GA-faithful reflection module.")
    parser.add_argument("seed_dir", type=Path)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    package = load_seed(args.seed_dir)
    out_dir = args.output_dir or (HERE / "tmp" / "smga_reflect")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Reflection reads the FULL history (GA's persistent memory stream), not the
    # windowed current session.
    prompt_record = {
        "probe_id": f"{package.seed_id}_reflection",
        "system_prompt": REFLECT_SYSTEM_PROMPT,
        "user_prompt": build_reflect_user_prompt(
            format_entity_catalog(package), format_event_history(package)
        ),
        "expected_raw_output_schema": {"insights": []},
    }
    prompts_path = out_dir / f"{package.seed_id}_reflect_prompts.jsonl"
    with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(prompt_record, ensure_ascii=False) + "\n")

    raw_path = run_reflection(prompts_path, args.config, out_dir)
    insights = extract_insights(raw_path)
    if not insights:
        print("error: no insights parsed from model output", file=sys.stderr)
        return 1

    artifact = {
        "scenario_id": package.scenario_id,
        "seed_id": package.seed_id,
        "source": "reflect_module.py GA-faithful reflection (insights + planning notes)",
        "insight_count": len(insights),
        "insights": insights,
    }
    artifact_path = out_dir / f"{package.seed_id}_reflection_artifact.json"
    with artifact_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(artifact, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\nformed {len(insights)} insights -> {artifact_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
