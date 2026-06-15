#!/usr/bin/env python3
"""Run ONLY the operationalization probes (probe_0006, probe_0007) across the
decisive bracket of conditions, to test whether the probe_0001 affordance
advantage replicates beyond a single probe.

Conditions: M0_GA (raw current session), M2_memory_only (facts), M3_actionable
(structured affordance), M0_GA_reflect (faithful GA). Reuses the frozen memory and
reflection artifacts; only the two new probes cost API calls.

Usage:
    FHL_API_KEY=... python3 run_oper_probes.py --seeds 1-10
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import baseline_harness as bh
import treatment_harness as th
from benchmark_loader import load_seed

HERE = Path(__file__).resolve().parent
OPER_PROBES = {"probe_0006", "probe_0007"}
CONDITIONS = ["M0_GA", "M2_memory_only", "M3_actionable", "M0_GA_reflect"]


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


def memory_block(condition: str, memories: list[dict[str, Any]]) -> str:
    if condition == "M2_memory_only":
        return th.serialize_m2(memories)
    return th.serialize_m3(memories)  # M3_actionable


def build_user_prompt(condition: str, package, probe: dict[str, Any], args: argparse.Namespace) -> tuple[str, str]:
    """Return (system_prompt, user_prompt) for one (condition, probe)."""
    if condition == "M0_GA":
        cond = bh.CONDITIONS["M0_GA"]
        events = bh.format_event_history(package, events=bh.baseline_visible_events(package))
        user = bh.build_user_prompt(
            condition=cond, entity_catalog=bh.format_entity_catalog(package),
            event_history=events, probe=probe,
        )
        return bh.build_system_prompt(cond), user

    if condition == "M0_GA_reflect":
        artifact = json.loads((args.reflect_dir / f"{package.seed_id}_reflection_artifact.json").read_text(encoding="utf-8"))
        insight_block = "\n".join(f"- {s}" for s in artifact.get("insights", []))
        events = bh.format_event_history(package, events=bh.baseline_visible_events(package))
        user = "\n\n".join([
            "Condition: M0_GA_reflect",
            "Entity catalog:", bh.format_entity_catalog(package),
            "Scripted event history (current session):", events,
            "Reflections (high-level insights distilled from your earlier interactions):",
            insight_block,
            "Probe:", str(probe["prompt"]),
            "Output JSON:",
            json.dumps({"probe_id": probe["probe_id"], "response_text": "your answer here"}, ensure_ascii=False),
        ])
        return bh.build_system_prompt(bh.CONDITIONS["M0_GA"]), user

    # M2 / M3 treatment conditions
    artifact = json.loads((args.memory_dir / f"{package.seed_id}_memory_artifact.json").read_text(encoding="utf-8"))
    block = memory_block(condition, artifact.get("memories", []))
    system = th.SYSTEM_M2 if condition == "M2_memory_only" else th.SYSTEM_M3
    return system, th.build_user_prompt(condition, block, probe)


def minimal_template(package, condition: str, probes: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "scenario_id": package.scenario_id,
        "seed_id": package.seed_id,
        "condition_id": condition,
        "model_config": {"provider": "TODO", "model": "TODO", "temperature": 0},
        "responses": [
            {"probe_id": p["probe_id"], "response_text": "", "raw_model_output": None,
             "normalization_notes": "operationalization probe run"}
            for p in probes
        ],
    }


def run_seed_condition(seed_id: str, condition: str, args: argparse.Namespace) -> None:
    package = load_seed(args.seeds_dir / seed_id)
    probes = [p for p in package.probes if p["probe_id"] in OPER_PROBES]

    prompts_path = args.out_dir / f"{seed_id}_{condition}_prompts.jsonl"
    template_path = args.out_dir / f"{seed_id}_{condition}_responses.template.json"
    response = args.out_dir / f"{seed_id}_{condition}_responses.raw_draft.json"
    judge_summary = args.out_dir / "judge" / f"{seed_id}_{condition}_judge_summary.json"

    args.out_dir.mkdir(parents=True, exist_ok=True)
    if not prompts_path.exists():
        records = []
        for probe in probes:
            system, user = build_user_prompt(condition, package, probe, args)
            records.append({
                "scenario_id": package.scenario_id, "seed_id": package.seed_id,
                "condition_id": condition, "probe_id": probe["probe_id"],
                "system_prompt": system, "user_prompt": user,
                "expected_raw_output_schema": {"probe_id": probe["probe_id"], "response_text": "..."},
            })
        with prompts_path.open("w", encoding="utf-8", newline="\n") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        with template_path.open("w", encoding="utf-8", newline="\n") as f:
            json.dump(minimal_template(package, condition, probes), f, indent=2, ensure_ascii=False)
            f.write("\n")

    maybe(
        [sys.executable, "model_calling_runner.py", str(prompts_path), "--config", str(args.config),
         "--response-template", str(template_path), "--output-dir", str(args.out_dir)],
        response,
    )
    maybe(
        [sys.executable, "judge_scorer.py", str(args.seeds_dir / seed_id), str(response), "--config", str(args.config)],
        judge_summary,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run operationalization probes across the condition bracket.")
    parser.add_argument("--seeds", default="1-10")
    parser.add_argument("--conditions", nargs="+", default=CONDITIONS)
    parser.add_argument("--seeds-dir", type=Path, default=Path("seeds"))
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--memory-dir", type=Path, default=Path("tmp/smga_memory"))
    parser.add_argument("--reflect-dir", type=Path, default=Path("tmp/smga_reflect"))
    parser.add_argument("--out-dir", type=Path, default=Path("tmp/smga_oper"))
    parser.add_argument("--parallel", type=int, default=1, help="(seed,condition) units to run concurrently.")
    args = parser.parse_args()

    units = [(s, c) for s in parse_seeds(args.seeds) for c in args.conditions]

    def attempt(unit: tuple[str, str]) -> str | None:
        seed_id, condition = unit
        try:
            run_seed_condition(seed_id, condition, args)
            return None
        except (subprocess.CalledProcessError, OSError, KeyError) as exc:
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
