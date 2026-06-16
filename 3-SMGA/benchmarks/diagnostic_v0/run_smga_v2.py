#!/usr/bin/env python3
"""Test the revised SMGA v2 memory condition (M4_smga_v2) on existing seeds.

SMGA v2 drops pre-committed affordances (which our experiments showed are
double-edged and do not generalize) and instead surfaces currency + an
implication-reasoning, multi-action de-biasing instruction in the system prompt.
This reuses the gpt-5.4-formed memory artifacts; only the new condition costs API.

Decisive checks vs M3_actionable / M2 / faithful GA:
  - keep the probe_0001 operationalization gain?
  - FIX the probe_0007 affordance frame-bias?
  - GENERALIZE to Family B (where M3 reversed below faithful GA)?

Usage:
    FHL_API_KEY=... python3 run_smga_v2.py --seeds 1-10,1001-1024 --parallel 8
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONDITION = "M4_smga_v2"


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
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            out.extend(range(int(a), int(b) + 1))
        else:
            out.append(int(part))
    return [f"seed_{i:04d}" for i in out]


def run_seed(seed_id: str, args: argparse.Namespace) -> None:
    seed_dir = args.seeds_dir / seed_id
    mem_artifact = args.memory_dir / f"{seed_id}_memory_artifact.json"
    if not mem_artifact.exists():
        raise FileNotFoundError(f"missing memory artifact: {mem_artifact}")

    prompt = args.out_dir / f"{seed_id}_{CONDITION}_prompts.jsonl"
    template = args.out_dir / f"{seed_id}_{CONDITION}_responses.template.json"
    response = args.out_dir / f"{seed_id}_{CONDITION}_responses.raw_draft.json"
    judge_summary = args.out_dir / "judge" / f"{seed_id}_{CONDITION}_judge_summary.json"

    # 1. build M4 prompts (treatment_harness builds all conditions; we only run M4).
    if not prompt.exists():
        run([sys.executable, "treatment_harness.py", str(seed_dir), str(mem_artifact),
             "--output-dir", str(args.out_dir)])
    # 2. answer with the (strong) config model, judge with the same config.
    maybe([sys.executable, "model_calling_runner.py", str(prompt), "--config", str(args.config),
           "--response-template", str(template), "--output-dir", str(args.out_dir)], response)
    maybe([sys.executable, "judge_scorer.py", str(seed_dir), str(response),
           "--config", str(args.config), "--output-dir", str(args.out_dir / "judge")], judge_summary)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the SMGA v2 (M4) condition on existing seeds.")
    parser.add_argument("--seeds", default="1-10,1001-1024")
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--memory-dir", type=Path, default=Path("tmp/smga_memory"))
    parser.add_argument("--out-dir", type=Path, default=Path("tmp/smga_treatment"))
    parser.add_argument("--parallel", type=int, default=1)
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
