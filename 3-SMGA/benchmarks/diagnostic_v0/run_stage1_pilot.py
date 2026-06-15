#!/usr/bin/env python3
"""Run the SMGA Stage 1 pilot pipeline with resume-friendly skips."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASELINE_CONDITIONS = ("M0_GA", "M0_prompted")
TREATMENT_CONDITIONS = ("M2_memory_only", "M2_aff_text", "M3_placebo", "M3_actionable")
ALL_CONDITIONS = (*BASELINE_CONDITIONS, *TREATMENT_CONDITIONS)


def run(cmd: list[str], *, cwd: Path = HERE) -> None:
    print("\n$ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=str(cwd), check=True)


def maybe_run(cmd: list[str], output: Path, *, force: bool = False) -> None:
    if output.exists() and not force:
        print(f"skip existing: {output}", flush=True)
        return
    run(cmd)


def seed_ids(start: int, end: int) -> list[str]:
    return [f"seed_{index:04d}" for index in range(start, end + 1)]


def response_path(seed_id: str, condition: str, output_dir: Path) -> Path:
    return output_dir / f"{seed_id}_{condition}_responses.raw_draft.json"


def judge_summary_path(seed_id: str, condition: str, condition_dir: Path) -> Path:
    return condition_dir / "judge" / f"{seed_id}_{condition}_judge_summary.json"


def build_condition_outputs(seed_id: str, condition: str, args: argparse.Namespace) -> tuple[Path, Path, Path]:
    if condition in BASELINE_CONDITIONS:
        prompt_dir = args.baseline_dir
        output_dir = args.baseline_dir
    else:
        prompt_dir = args.treatment_dir
        output_dir = args.treatment_dir
    prompt = prompt_dir / f"{seed_id}_{condition}_prompts.jsonl"
    template = prompt_dir / f"{seed_id}_{condition}_responses.template.json"
    response = response_path(seed_id, condition, output_dir)
    return prompt, template, response


def run_seed(seed_id: str, args: argparse.Namespace) -> None:
    seed_dir = args.seeds_dir / seed_id
    if not seed_dir.is_dir():
        raise FileNotFoundError(f"missing seed directory: {seed_dir}")

    print(f"\n=== {seed_id} ===", flush=True)

    run([sys.executable, "validate_seed.py", str(seed_dir)])

    maybe_run(
        [sys.executable, "baseline_harness.py", str(seed_dir), "--condition", "all", "--output-dir", str(args.baseline_dir)],
        args.baseline_dir / f"{seed_id}_M0_GA_prompts.jsonl",
        force=args.force_prompts,
    )

    memory_artifact = args.memory_dir / f"{seed_id}_memory_artifact.json"
    maybe_run(
        [sys.executable, "memory_module.py", str(seed_dir), "--config", str(args.config), "--output-dir", str(args.memory_dir)],
        memory_artifact,
        force=args.force_model,
    )

    maybe_run(
        [sys.executable, "treatment_harness.py", str(seed_dir), str(memory_artifact), "--output-dir", str(args.treatment_dir)],
        args.treatment_dir / f"{seed_id}_M3_placebo_prompts.jsonl",
        force=args.force_prompts,
    )

    for condition in ALL_CONDITIONS:
        prompt, template, response = build_condition_outputs(seed_id, condition, args)
        maybe_run(
            [
                sys.executable,
                "model_calling_runner.py",
                str(prompt),
                "--config",
                str(args.config),
                "--response-template",
                str(template),
                "--output-dir",
                str(args.baseline_dir if condition in BASELINE_CONDITIONS else args.treatment_dir),
            ],
            response,
            force=args.force_model,
        )

        judge_summary = judge_summary_path(
            seed_id,
            condition,
            args.baseline_dir if condition in BASELINE_CONDITIONS else args.treatment_dir,
        )
        maybe_run(
            [
                sys.executable,
                "judge_scorer.py",
                str(seed_dir),
                str(response),
                "--config",
                str(args.config),
            ],
            judge_summary,
            force=args.force_judge,
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run 5-condition Stage 1 pilot.")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=10)
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--baseline-dir", type=Path, default=Path("tmp/smga_baseline_harness"))
    parser.add_argument("--memory-dir", type=Path, default=Path("tmp/smga_memory"))
    parser.add_argument("--treatment-dir", type=Path, default=Path("tmp/smga_treatment"))
    parser.add_argument("--force-prompts", action="store_true")
    parser.add_argument("--force-model", action="store_true")
    parser.add_argument("--force-judge", action="store_true")
    parser.add_argument(
        "--parallel", type=int, default=1,
        help="Run this many seeds concurrently. Each seed uses up to max_concurrency "
        "in-flight calls, so total in-flight ~= parallel * max_concurrency; keep under "
        "the provider's measured ceiling.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    seeds = seed_ids(args.start, args.end)
    failed: list[str] = []

    def attempt(seed_id: str) -> str | None:
        try:
            run_seed(seed_id, args)
            return None
        except (subprocess.CalledProcessError, OSError) as exc:
            # One bad seed (e.g. a malformed model draft) must not abort the batch.
            print(f"!! seed {seed_id} failed and was skipped: {exc}", flush=True)
            return seed_id

    if args.parallel > 1:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=args.parallel) as ex:
            failed = [s for s in ex.map(attempt, seeds) if s]
    else:
        failed = [s for s in (attempt(seed_id) for seed_id in seeds) if s]

    if failed:
        print(f"\nCompleted with {len(failed)} failed seed(s): {', '.join(failed)}", flush=True)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
