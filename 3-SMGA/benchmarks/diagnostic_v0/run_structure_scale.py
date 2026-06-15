#!/usr/bin/env python3
"""Run the structure-at-scale experiment.

For each seed and each memory-scale level K, build the three scale conditions
(M2_aff_scale / M3_dump_scale / M3_retr_scale) by padding the existing memory
artifact with K distractor memories, then run the model and the LLM judge. Reuses
the frozen memory artifacts; only the new conditions cost API calls.

Usage:
    FHL_API_KEY=... python3 run_structure_scale.py --seeds 1-10 --k 0 50
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCALE_CONDITIONS = ("M2_aff_scale", "M3_dump_scale", "M3_retr_scale")


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


def run_seed(seed_id: str, k: int, args: argparse.Namespace) -> None:
    out_dir = args.base_dir / f"smga_scale_k{k}"
    memory_artifact = args.memory_dir / f"{seed_id}_memory_artifact.json"
    if not memory_artifact.exists():
        raise FileNotFoundError(f"missing memory artifact: {memory_artifact}")

    maybe(
        [sys.executable, "treatment_harness.py", str(args.seeds_dir / seed_id),
         str(memory_artifact), "--output-dir", str(out_dir), "--memory-scale", str(k)],
        out_dir / f"{seed_id}_M3_retr_scale_prompts.jsonl",
    )

    for condition in SCALE_CONDITIONS:
        prompt = out_dir / f"{seed_id}_{condition}_prompts.jsonl"
        template = out_dir / f"{seed_id}_{condition}_responses.template.json"
        response = out_dir / f"{seed_id}_{condition}_responses.raw_draft.json"
        maybe(
            [sys.executable, "model_calling_runner.py", str(prompt), "--config", str(args.config),
             "--response-template", str(template), "--output-dir", str(out_dir)],
            response,
        )
        judge_summary = out_dir / "judge" / f"{seed_id}_{condition}_judge_summary.json"
        maybe(
            [sys.executable, "judge_scorer.py", str(args.seeds_dir / seed_id), str(response),
             "--config", str(args.config)],
            judge_summary,
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the structure-at-scale experiment.")
    parser.add_argument("--seeds", default="1-10")
    parser.add_argument("--k", type=int, nargs="+", default=[0, 50])
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--memory-dir", type=Path, default=Path("tmp/smga_memory"))
    parser.add_argument("--base-dir", type=Path, default=Path("tmp"))
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    args = parser.parse_args()

    failed: list[str] = []
    for k in args.k:
        for seed_id in parse_seeds(args.seeds):
            try:
                run_seed(seed_id, k, args)
            except (subprocess.CalledProcessError, OSError) as exc:
                print(f"!! {seed_id} k={k} failed: {exc}", flush=True)
                failed.append(f"{seed_id}@k{k}")
    if failed:
        print(f"\nfailed: {', '.join(failed)}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
