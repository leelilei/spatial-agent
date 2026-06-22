#!/usr/bin/env python3
"""Run repeated society simulations and aggregate currency-coherence results.

This is the S5 bridge: the initial society demo was one run, one scenario, four
agents. This runner keeps the scenario fixed but varies scheduling seeds, agent
count, memory condition, and model so we can estimate variance before making the
simulation more complex.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from llm import DEFAULT_CONFIG, LLM
from society import (
    build_memory_factory,
    demo_world,
    interview,
    make_llm_converse,
    mock_converse,
    run_sim,
)


DEFAULT_MEMORIES = ("ga", "smga")
DEFAULT_QUESTION = "When and where is the repair drive being held now?"
CURRENT_MARKERS = ("sunday", "community center")
STALE_MARKERS = ("saturday", "front porch", "porch")
UNKNOWN_MARKERS = (
    "do not say",
    "does not say",
    "don't say",
    "doesn't say",
    "dont say",
    "doesnt say",
    "do not mention",
    "does not mention",
    "don't mention",
    "doesn't mention",
    "unknown",
    "not mention",
    "not say when",
    "not say where",
    "notes do not",
    "notes don't",
    "no specific",
    "not specified",
    "isn't specified",
    "haven't been specified",
    "not shared",
    "haven't been shared",
    "not confirmed",
    "haven't been confirmed",
    "not finalized",
    "don't know",
    "can't tell",
    "pending",
)
UNSUPPORTED_SPECIFIC_MARKERS = (
    "today",
    "happening now",
    "held now",
    "being held now",
    "this weekend",
    "school pickup",
    "pickup window",
    "work area",
    "garage",
    "community shed",
    "community hall",
    "corner store",
    "around 4",
    "at 3",
    " by the ",
    "sam's place",
    "tool drop-off",
    "later at the repair drive",
)


def safe_label(value: str | None) -> str:
    if not value:
        return "config_model"
    return "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "_" for ch in value)


def model_label(model: str | None, llm: LLM | None, *, mock: bool) -> str:
    if mock:
        return "mock"
    if model:
        return safe_label(model)
    if llm is not None:
        return safe_label(getattr(llm.config, "model", None))
    return "config_model"


def tally_currency(results: dict[str, Any]) -> dict[str, int]:
    tally = {"current": 0, "stale": 0, "unknown": 0}
    for item in results.values():
        verdict = str(item.get("verdict", "unknown"))
        if verdict not in tally:
            verdict = "unknown"
        tally[verdict] += 1
    return tally


def count_unsupported_specific(results: dict[str, Any]) -> int:
    """Count unknown answers that still invent a specific time/place detail.

    This is a deliberately small C2 proxy for the current repair-drive scenario:
    if the answer is scored unknown, a good answer should say the notes do not
    specify the current time/place. A concrete but unsupported location/time is
    an anti-grounding failure.
    """
    count = 0
    for item in results.values():
        answer = str(item.get("answer", ""))
        lower = answer.lower().replace("\u2019", "'")
        if item.get("verdict") != "unknown":
            continue
        if any(marker in lower for marker in UNSUPPORTED_SPECIFIC_MARKERS):
            count += 1
            continue
        if any(marker in lower for marker in UNKNOWN_MARKERS):
            continue
        if any(marker in lower for marker in (" at ", " on ", " around ")):
            count += 1
    return count


def verdict_from_text(text: str) -> str:
    lower = text.lower()
    has_current = any(marker in lower for marker in CURRENT_MARKERS)
    has_stale = any(marker in lower for marker in STALE_MARKERS)
    if has_current and not has_stale:
        return "current"
    if has_stale:
        return "stale"
    return "unknown"


def mechanical_interview(world: Any, question: str) -> dict[str, Any]:
    results = {}
    for agent in world.agents:
        context = agent.memory.retrieve(question)
        results[agent.agent_id] = {
            "name": agent.name,
            "answer": context,
            "verdict": verdict_from_text(context),
        }
    return results


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def run_one(
    *,
    memory: str,
    model: str | None,
    llm: LLM | None,
    run_index: int,
    schedule_seed: int,
    args: argparse.Namespace,
) -> dict[str, Any]:
    if args.mock:
        if memory != "raw":
            raise ValueError("--mock currently supports only --memory raw")
        converse = mock_converse
    else:
        if llm is None:
            raise ValueError("llm is required unless --mock is set")
        converse = make_llm_converse(llm, turns=args.turns)

    world = demo_world(
        build_memory_factory(memory, llm, scenario=args.scenario, prov_loss=args.prov_loss,
                             prov_garble=args.prov_garble, prov_mention=args.prov_mention),
        rng_seed=schedule_seed,
        agent_count=args.agent_count,
        meetings_per_round=args.meetings,
        rebroadcast_every=args.rebroadcast_every,
        rebroadcast_scope=args.rebroadcast_scope,
        scenario=args.scenario,
        rebroadcast_rounds=args.rebroadcast_rounds,
        persona_depth=args.persona_depth,
        topology=args.topology,
    )
    question = world.question  # scenario-correct probe (overrides the default)
    label = model_label(model, llm, mock=args.mock)
    run_dir = args.out_dir / label / memory / f"run_{run_index:03d}"

    trajectory: list[dict[str, Any]] = []
    round_hook = None
    if args.interview_every_round and not args.mock:
        assert llm is not None

        def round_hook(w: Any, r: int) -> None:  # per-round held-belief snapshot (decay curve)
            res = interview(w, question, llm)
            trajectory.append({"round": r, "tally": tally_currency(res)})

    summary = run_sim(world, args.rounds, converse, run_dir, workers=max(1, args.workers),
                      round_hook=round_hook)
    if trajectory:
        write_json(run_dir / "trajectory.json", {"question": question, "trajectory": trajectory})
    summary.update({
        "memory": memory,
        "model": label,
        "run_index": run_index,
        "schedule_seed": schedule_seed,
        "agent_count": args.agent_count,
    })

    if args.mock:
        interview_results = mechanical_interview(world, question)
    else:
        assert llm is not None
        interview_results = interview(world, question, llm)
    write_json(run_dir / "interview_currency.json", {
        "question": question,
        "results": interview_results,
        "mode": "mechanical" if args.mock else "llm",
    })
    tally = tally_currency(interview_results)
    unsupported_specific = count_unsupported_specific(interview_results)

    summary["currency_interview"] = tally
    summary["unsupported_specific"] = unsupported_specific
    write_json(run_dir / "sim_summary.json", summary)

    return {
        "memory": memory,
        "model": label,
        "run_index": run_index,
        "schedule_seed": schedule_seed,
        "agent_count": args.agent_count,
        "rounds": args.rounds,
        "turns": args.turns,
        "out_dir": str(run_dir),
        "currency_interview": tally,
        "unsupported_specific": unsupported_specific,
    }


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    groups: dict[tuple[str, str], dict[str, Any]] = {}
    for row in rows:
        key = (str(row["model"]), str(row["memory"]))
        group = groups.setdefault(key, {
            "model": key[0],
            "memory": key[1],
            "runs": 0,
            "agents_total": 0,
            "current": 0,
            "stale": 0,
            "unknown": 0,
            "unsupported_specific": 0,
            "per_run_current_rate": [],
            "per_run_unsupported_rate": [],
        })
        tally = row["currency_interview"]
        total = sum(int(tally.get(k, 0)) for k in ("current", "stale", "unknown"))
        group["runs"] += 1
        group["agents_total"] += total
        for verdict in ("current", "stale", "unknown"):
            group[verdict] += int(tally.get(verdict, 0))
        unsupported = int(row.get("unsupported_specific", 0))
        group["unsupported_specific"] += unsupported
        group["per_run_current_rate"].append((int(tally.get("current", 0)) / total) if total else 0.0)
        group["per_run_unsupported_rate"].append((unsupported / total) if total else 0.0)

    summaries = []
    for group in groups.values():
        rates = group.pop("per_run_current_rate")
        unsupported_rates = group.pop("per_run_unsupported_rate")
        total = int(group["agents_total"])
        mean = sum(rates) / len(rates) if rates else 0.0
        variance = sum((rate - mean) ** 2 for rate in rates) / len(rates) if rates else 0.0
        unsupported_mean = sum(unsupported_rates) / len(unsupported_rates) if unsupported_rates else 0.0
        group["current_rate"] = (int(group["current"]) / total) if total else 0.0
        group["unsupported_specific_rate"] = (int(group["unsupported_specific"]) / total) if total else 0.0
        group["mean_run_current_rate"] = mean
        group["mean_run_unsupported_specific_rate"] = unsupported_mean
        group["min_run_current_rate"] = min(rates) if rates else 0.0
        group["max_run_current_rate"] = max(rates) if rates else 0.0
        group["std_run_current_rate"] = variance ** 0.5
        summaries.append(group)

    return {
        "groups": sorted(summaries, key=lambda item: (item["model"], item["memory"])),
        "rows": rows,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run repeated SMGA society simulations.")
    parser.add_argument("--memory", action="append", default=None, help="memory condition; repeatable")
    parser.add_argument("--model", action="append", default=None, help="model override; repeatable")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--runs", type=int, default=3)
    parser.add_argument("--seed", type=int, default=7, help="base random seed")
    parser.add_argument("--agent-count", type=int, default=4)
    parser.add_argument("--meetings", type=int, default=1, help="encounters per agent per round (connectivity)")
    parser.add_argument("--rebroadcast-every", type=int, default=0, help="re-announce the truth every k rounds (0=once)")
    parser.add_argument("--rebroadcast-scope", default="source", choices=["source", "broadcast"], help="re-broadcast target")
    parser.add_argument("--scenario", default="repair_drive", help="scenario key (repair_drive, book_club, carpool)")
    parser.add_argument("--rebroadcast-rounds", default="", help="explicit inject rounds, comma-sep (overrides --rebroadcast-every; for recency tests)")
    parser.add_argument("--persona-depth", default="thin", choices=["thin", "thick"], help="thin one-liner vs rich Park-2024-style personas")
    parser.add_argument("--interview-every-round", action="store_true", help="interview after every round (held-belief decay trajectory)")
    parser.add_argument("--prov-loss", type=float, default=0.0, help="PROV lossy-channel: prob provenance fails to survive a relay")
    parser.add_argument("--prov-garble", type=float, default=0.0, help="PROV lossy-channel: prob a relay corrupts the value to stale (keeps version)")
    parser.add_argument("--prov-mention", type=float, default=1.0, help="PROV sparse comms: prob the agent conveys the fact in a given utterance (1.0=every utterance)")
    parser.add_argument("--topology", default="random", choices=["random","ring","star","smallworld"], help="contact topology")
    parser.add_argument("--rounds", type=int, default=5)
    parser.add_argument("--turns", type=int, default=4)
    parser.add_argument("--workers", type=int, default=1, help="concurrent encounters/consolidations per round")
    parser.add_argument("--question", default=DEFAULT_QUESTION)
    parser.add_argument("--mock", action="store_true", help="offline smoke test; supports raw memory only")
    parser.add_argument("--out-dir", type=Path, default=Path("sim/runs/sweeps/latest"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    memories = tuple(args.memory or (("raw",) if args.mock else DEFAULT_MEMORIES))
    models = tuple(args.model or ((None,) if not args.mock else ("mock",)))
    rows: list[dict[str, Any]] = []

    # Reproducibility: dump the FULL config (all CLI args) so every run dir is self-describing.
    import datetime as _dt
    cfg = {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()}
    cfg["_timestamp"] = _dt.datetime.now().isoformat(timespec="seconds")
    write_json(args.out_dir / "run_config.json", cfg)

    llm_by_model: dict[str | None, LLM | None] = {}
    if not args.mock:
        for model in models:
            llm_by_model[model] = LLM(config=args.config, model=model)

    for model in models:
        llm = llm_by_model.get(model)
        for memory in memories:
            for run_index in range(args.runs):
                schedule_seed = args.seed + run_index
                print(
                    f"model={model_label(model, llm, mock=args.mock)} "
                    f"memory={memory} run={run_index} seed={schedule_seed}",
                    flush=True,
                )
                try:
                    rows.append(run_one(
                        memory=memory,
                        model=model,
                        llm=llm,
                        run_index=run_index,
                        schedule_seed=schedule_seed,
                        args=args,
                    ))
                except Exception as exc:  # one failed run (e.g. provider outage) must not lose the sweep
                    print(f"!! run failed (skipped): memory={memory} run={run_index} seed={schedule_seed}: {exc}",
                          flush=True)

    if not rows:
        print("no runs completed", flush=True)
        return 1
    result = aggregate(rows)
    write_json(args.out_dir / "runs.json", rows)
    write_json(args.out_dir / "aggregate.json", result)
    print(json.dumps(result["groups"], ensure_ascii=False, indent=2))
    print(f"\nsweep logs -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
