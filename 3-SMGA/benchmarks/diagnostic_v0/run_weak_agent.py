#!/usr/bin/env python3
"""Full weak-agent condition: the WEAK model forms memory AND reflection AND answers.

The model_sweep test held memory quality constant (gpt-5.4-formed) and only weakened
the planner. This is the realistic deployment test: a fully weak agent. The weak model
forms its own structured memory (M2/M3) and GA reflection (M0_GA_reflect), then answers
with that memory. The JUDGE stays gpt-5.4 (constant measurement).

Decisive question: does M3 still hold when the weak model forms the memory, and does
faithful GA degrade more (because the weak model writes worse free-text reflections)?

Usage:
    FHL_API_KEY=... python3 run_weak_agent.py --seeds 1-10 --parallel 4
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

import run_ga_reflect

HERE = Path(__file__).resolve().parent
CONDITIONS = ["M2_memory_only", "M3_actionable", "M0_GA_reflect"]


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


def run_seed(seed_id: str, args: argparse.Namespace) -> None:
    seed_dir = args.seeds_dir / seed_id
    mem_artifact = args.mem_dir / f"{seed_id}_memory_artifact.json"
    refl_artifact = args.refl_dir / f"{seed_id}_reflection_artifact.json"

    # 1. weak-model memory + reflection formation
    maybe([sys.executable, "memory_module.py", str(seed_dir),
           "--config", str(args.weak_config), "--output-dir", str(args.mem_dir)], mem_artifact)
    maybe([sys.executable, "reflect_module.py", str(seed_dir),
           "--config", str(args.weak_config), "--output-dir", str(args.refl_dir)], refl_artifact)

    # 2. build prompts from the weak-formed artifacts
    maybe([sys.executable, "treatment_harness.py", str(seed_dir), str(mem_artifact),
           "--output-dir", str(args.out_dir)],
          args.out_dir / f"{seed_id}_M3_actionable_prompts.jsonl")
    ga_args = argparse.Namespace(seeds_dir=args.seeds_dir, reflect_dir=args.refl_dir, out_dir=args.out_dir)
    if not (args.out_dir / f"{seed_id}_M0_GA_reflect_prompts.jsonl").exists():
        run_ga_reflect.build_reflect_prompts(seed_id, ga_args)

    # 3. answer with the weak model, judge with gpt-5.4
    for condition in CONDITIONS:
        prompt = args.out_dir / f"{seed_id}_{condition}_prompts.jsonl"
        template = args.out_dir / f"{seed_id}_{condition}_responses.template.json"
        response = args.out_dir / f"{seed_id}_{condition}_responses.raw_draft.json"
        judge_summary = args.out_dir / "judge" / f"{seed_id}_{condition}_judge_summary.json"
        maybe([sys.executable, "model_calling_runner.py", str(prompt), "--config", str(args.weak_config),
               "--model", args.weak_model, "--response-template", str(template), "--output-dir", str(args.out_dir)],
              response)
        maybe([sys.executable, "judge_scorer.py", str(seed_dir), str(response),
               "--config", str(args.judge_config), "--output-dir", str(args.out_dir / "judge")],
              judge_summary)


def main() -> int:
    parser = argparse.ArgumentParser(description="Full weak-agent condition (weak forms + answers, gpt-5.4 judges).")
    parser.add_argument("--seeds", default="1-10")
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--weak-config", type=Path, default=Path("configs/fhl_responses_gpt54mini_config.json"))
    parser.add_argument("--weak-model", default="gpt-5.4-mini")
    parser.add_argument("--judge-config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--mem-dir", type=Path, default=Path("tmp/smga_memory_mini"))
    parser.add_argument("--refl-dir", type=Path, default=Path("tmp/smga_reflect_mini"))
    parser.add_argument("--out-dir", type=Path, default=Path("tmp/smga_weak"))
    parser.add_argument("--parallel", type=int, default=1)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

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
