#!/usr/bin/env python3
"""Run the faithful GA baseline: M0_GA_reflect = current session + GA reflections.

Our plain M0_GA only dumps the current-session event log. The real Generative
Agents memory adds a REFLECTION layer (distilled insights / planning notes). This
runner gives M0 that layer: per seed it generates GA-faithful reflections from the
full history (reflect_module), then builds an M0_GA_reflect prompt that appends
those reflections to the current-session observations, and scores it with the same
judge. The decisive comparison is M3_actionable vs M0_GA_reflect.

Usage:
    FHL_API_KEY=... python3 run_ga_reflect.py --seeds 1-10
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from baseline_harness import (
    CONDITIONS as BASELINE_CONDITIONS,
    baseline_visible_events,
    build_response_template,
    build_system_prompt,
    format_entity_catalog,
    format_event_history,
)
from benchmark_loader import load_seed

HERE = Path(__file__).resolve().parent
CONDITION = "M0_GA_reflect"


def run(cmd: list[str]) -> None:
    print("\n$ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=str(HERE), check=True)


def maybe(cmd: list[str], output: Path) -> None:
    if output.exists():
        print(f"skip existing: {output}", flush=True)
        return
    run(cmd)


def parse_seeds(spec: str) -> list[str]:
    out: list[int] = []
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return [f"seed_{i:04d}" for i in out]


def build_reflect_prompts(seed_id: str, args: argparse.Namespace) -> None:
    package = load_seed(args.seeds_dir / seed_id)
    artifact = json.loads((args.reflect_dir / f"{seed_id}_reflection_artifact.json").read_text(encoding="utf-8"))
    insights = artifact.get("insights", [])
    insight_block = "\n".join(f"- {s}" for s in insights)

    entity_catalog = format_entity_catalog(package)
    current_events = format_event_history(package, events=baseline_visible_events(package))
    system = build_system_prompt(BASELINE_CONDITIONS["M0_GA"])

    records: list[dict[str, Any]] = []
    for probe in package.probes:
        user = "\n\n".join([
            f"Condition: {CONDITION}",
            "Entity catalog:", entity_catalog,
            "Scripted event history (current session):", current_events,
            "Reflections (high-level insights distilled from your earlier interactions):",
            insight_block,
            "Probe:", str(probe["prompt"]),
            "Output JSON:",
            json.dumps({"probe_id": probe["probe_id"], "response_text": "your answer here"}, ensure_ascii=False),
        ])
        records.append({
            "scenario_id": package.scenario_id,
            "seed_id": package.seed_id,
            "condition_id": CONDITION,
            "probe_id": probe["probe_id"],
            "system_prompt": system,
            "user_prompt": user,
            "expected_raw_output_schema": {"probe_id": probe["probe_id"], "response_text": "..."},
        })

    args.out_dir.mkdir(parents=True, exist_ok=True)
    prompts_path = args.out_dir / f"{seed_id}_{CONDITION}_prompts.jsonl"
    with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    template_path = args.out_dir / f"{seed_id}_{CONDITION}_responses.template.json"
    with template_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(build_response_template(package, CONDITION), f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{CONDITION}: {len(records)} prompts -> {prompts_path}")


def run_seed(seed_id: str, args: argparse.Namespace) -> None:
    # 1. GA-faithful reflection from the full history (condition-blind).
    maybe(
        [sys.executable, "reflect_module.py", str(args.seeds_dir / seed_id),
         "--config", str(args.config), "--output-dir", str(args.reflect_dir)],
        args.reflect_dir / f"{seed_id}_reflection_artifact.json",
    )
    # 2. Build the M0_GA_reflect prompts (current session + reflections).
    prompts_path = args.out_dir / f"{seed_id}_{CONDITION}_prompts.jsonl"
    if not prompts_path.exists():
        build_reflect_prompts(seed_id, args)
    # 3. Model + judge.
    template = args.out_dir / f"{seed_id}_{CONDITION}_responses.template.json"
    response = args.out_dir / f"{seed_id}_{CONDITION}_responses.raw_draft.json"
    maybe(
        [sys.executable, "model_calling_runner.py", str(prompts_path), "--config", str(args.config),
         "--response-template", str(template), "--output-dir", str(args.out_dir)],
        response,
    )
    judge_summary = args.out_dir / "judge" / f"{seed_id}_{CONDITION}_judge_summary.json"
    maybe(
        [sys.executable, "judge_scorer.py", str(args.seeds_dir / seed_id), str(response),
         "--config", str(args.config)],
        judge_summary,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the faithful GA (M0_GA_reflect) baseline.")
    parser.add_argument("--seeds", default="1-10")
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--reflect-dir", type=Path, default=Path("tmp/smga_reflect"))
    parser.add_argument("--out-dir", type=Path, default=Path("tmp/smga_ga_reflect"))
    parser.add_argument("--parallel", type=int, default=1, help="Seeds to run concurrently.")
    args = parser.parse_args()

    def attempt(seed_id: str) -> str | None:
        try:
            run_seed(seed_id, args)
            return None
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"!! {seed_id} failed: {exc}", flush=True)
            return seed_id

    seeds = parse_seeds(args.seeds)
    if args.parallel > 1:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=args.parallel) as ex:
            failed = [s for s in ex.map(attempt, seeds) if s]
    else:
        failed = [s for s in (attempt(s) for s in seeds) if s]
    if failed:
        print(f"\nfailed: {', '.join(failed)}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
