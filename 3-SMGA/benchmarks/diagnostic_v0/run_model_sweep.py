#!/usr/bin/env python3
"""Model-capability sweep: re-answer the EXISTING prompts with a weaker model.

Holds memory quality constant (prompts were built from gpt-5.4-formed memory and
reflections) and varies only the PLANNER model. The judge stays gpt-5.4 (constant
measurement). Tests whether structure helps a weaker planner use the memory — i.e.
whether the M3 > faithful-GA > M0 gaps widen as the answering model weakens.

Conditions reuse prompt files already on disk:
  M0_GA          tmp/smga_baseline_harness
  M0_GA_reflect  tmp/smga_ga_reflect
  M2_memory_only tmp/smga_treatment
  M3_actionable  tmp/smga_treatment

Usage:
    FHL_API_KEY=... python3 run_model_sweep.py --model gpt-5.4-mini --seeds 1-10 --parallel 5
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROMPT_DIR = {
    "M0_GA": Path("tmp/smga_baseline_harness"),
    "M0_GA_reflect": Path("tmp/smga_ga_reflect"),
    "M2_memory_only": Path("tmp/smga_treatment"),
    "M3_actionable": Path("tmp/smga_treatment"),
}


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


def run_unit(seed_id: str, condition: str, args: argparse.Namespace) -> None:
    src = PROMPT_DIR[condition]
    prompt = src / f"{seed_id}_{condition}_prompts.jsonl"
    template = src / f"{seed_id}_{condition}_responses.template.json"
    if not prompt.exists():
        raise FileNotFoundError(f"missing prompt file: {prompt}")
    out_dir = args.out_dir / args.model.replace(".", "").replace("-", "_")
    out_dir.mkdir(parents=True, exist_ok=True)
    response = out_dir / f"{seed_id}_{condition}_responses.raw_draft.json"
    judge_summary = out_dir / "judge" / f"{seed_id}_{condition}_judge_summary.json"

    maybe(
        [sys.executable, "model_calling_runner.py", str(prompt), "--config", str(args.config),
         "--model", args.model, "--response-template", str(template), "--output-dir", str(out_dir)],
        response,
    )
    # Judge stays on the config model (gpt-5.4) for constant measurement.
    maybe(
        [sys.executable, "judge_scorer.py", str(args.seeds_dir / seed_id), str(response),
         "--config", str(args.config), "--output-dir", str(out_dir / "judge")],
        judge_summary,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Re-answer existing prompts with a weaker planner model.")
    parser.add_argument("--model", required=True, help="Planner model id, e.g. gpt-5.4-mini")
    parser.add_argument("--seeds", default="1-10")
    parser.add_argument("--conditions", nargs="+", default=list(PROMPT_DIR.keys()))
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--out-dir", type=Path, default=Path("tmp/smga_modelsweep"))
    parser.add_argument("--parallel", type=int, default=1)
    args = parser.parse_args()

    units = [(s, c) for s in parse_seeds(args.seeds) for c in args.conditions]

    def attempt(unit: tuple[str, str]) -> str | None:
        seed_id, condition = unit
        try:
            run_unit(seed_id, condition, args)
            return None
        except (subprocess.CalledProcessError, OSError) as exc:
            print(f"!! {seed_id}/{condition} failed: {exc}", flush=True)
            return f"{seed_id}/{condition}"

    if args.parallel > 1:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=args.parallel) as ex:
            failed = [u for u in ex.map(attempt, units) if u]
    else:
        failed = [u for u in (attempt(u) for u in units) if u]
    if failed:
        print(f"\nfailed: {', '.join(failed)}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
