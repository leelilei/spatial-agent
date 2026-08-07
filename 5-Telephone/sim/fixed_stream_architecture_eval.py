#!/usr/bin/env python3
"""Replay one archived society dialogue stream through alternative memories.

This is an integration-only fallback for model/provider conditions where fresh
end-to-end dialogue generation is unavailable.  Every target memory receives
the same realized utterances, participants, order, and authoritative injection.
The target model is still used for memory consolidation and final interviews.
Results must therefore be reported as fixed-stream pilots, not end-to-end runs.
"""

from __future__ import annotations

import argparse
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from llm import LLM
from run_society_sweep import tally_currency, write_json
from society import (
    INTERVIEW_SYSTEM,
    build_memory_factory,
    demo_world,
)


def load_rounds(source_dir: Path) -> list[dict[str, Any]]:
    paths = sorted(source_dir.glob("round_*.json"))
    if not paths:
        raise FileNotFoundError(f"no round logs in {source_dir}")
    return [json.loads(path.read_text(encoding="utf-8")) for path in paths]


def replay_round(world: Any, payload: dict[str, Any], *, workers: int) -> None:
    round_idx = int(payload["round"])
    by_name = {agent.name: agent for agent in world.agents}
    for encounter in payload.get("encounters", []):
        a = by_name[str(encounter["a"])]
        b = by_name[str(encounter["b"])]
        for utterance in encounter.get("utterances", []):
            event = {
                "round": round_idx,
                "text": str(utterance.get("text", "")),
                "speaker": str(utterance.get("speaker", "")),
                "listener": str(utterance.get("listener", "")),
            }
            a.memory.observe(event)
            b.memory.observe(event)

    for injection in payload.get("injected", []):
        agent = by_name[str(injection["agent"])]
        text = str(injection["text"])
        agent.memory.observe({
            "round": round_idx,
            "text": text,
            "speaker": "world",
            "listener": agent.name,
            "injected": True,
            "prov": {
                "version": round_idx,
                "value": text,
                "auth": True,
                "source": "ORIGIN",
                "path": ["ORIGIN"],
            },
        })

    with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        list(executor.map(lambda agent: agent.memory.consolidate(), world.agents))


def parallel_interview(world: Any, llm: LLM, *, workers: int) -> dict[str, Any]:
    def ask(agent: Any) -> tuple[str, dict[str, Any]]:
        context = agent.memory.retrieve(world.question)
        out = llm.complete_json(
            INTERVIEW_SYSTEM,
            f"Memory notes:\n{context or '(none)'}\n\nQuestion: {world.question}",
        )
        answer = str(out.get("answer", ""))
        lower = answer.lower()
        has_current = any(marker in lower for marker in world.current_markers)
        has_stale = any(marker in lower for marker in world.stale_markers)
        verdict = (
            "current" if has_current and not has_stale
            else "stale" if has_stale
            else "unknown"
        )
        return agent.agent_id, {
            "name": agent.name,
            "answer": answer,
            "verdict": verdict,
        }

    with ThreadPoolExecutor(max_workers=max(1, workers)) as executor:
        return dict(executor.map(ask, world.agents))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--memory", required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--scenario", default="repair_drive")
    parser.add_argument("--seed", type=int, default=41)
    parser.add_argument("--agent-count", type=int, default=25)
    parser.add_argument("--meetings", type=int, default=2)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    llm = LLM(config=args.config)
    world = demo_world(
        build_memory_factory(args.memory, llm, scenario=args.scenario),
        rng_seed=args.seed,
        agent_count=args.agent_count,
        meetings_per_round=args.meetings,
        scenario=args.scenario,
    )
    rounds = load_rounds(args.source_dir)
    usage_before = llm.usage_snapshot()
    for payload in rounds:
        replay_round(world, payload, workers=args.workers)

    snapshots = {agent.agent_id: agent.memory.snapshot() for agent in world.agents}
    results = parallel_interview(world, llm, workers=args.workers)
    usage_after = llm.usage_snapshot()
    usage = {
        key: int(usage_after[key]) - int(usage_before[key])
        for key in ("logical_calls", "transport_attempts", "successful_calls")
    }
    usage["logical_calls_per_agent"] = usage["logical_calls"] / args.agent_count
    tally = tally_currency(results)
    model = str(getattr(llm.config, "model", "config-model"))
    summary = {
        "evaluation": "fixed_stream_architecture_replay",
        "source_dir": str(args.source_dir),
        "source_stream_memory": "ga",
        "target_memory": args.memory,
        "model": model,
        "scenario": args.scenario,
        "schedule_seed": args.seed,
        "rounds": len(rounds),
        "agent_count": args.agent_count,
        "currency_interview": tally,
        "current_rate": tally["current"] / args.agent_count,
        "llm_usage": usage,
        "scope": (
            "Integration-only fixed-stream pilot. Dialogue generation is held fixed; "
            "not an end-to-end target-memory society run."
        ),
    }
    write_json(args.out_dir / "run_config.json", {
        **vars(args),
        "source_dir": str(args.source_dir),
        "config": str(args.config),
        "out_dir": str(args.out_dir),
    })
    write_json(args.out_dir / "memory_snapshots.json", snapshots)
    write_json(args.out_dir / "interview_currency.json", {
        "question": world.question,
        "results": results,
        "mode": "llm_fixed_stream",
    })
    write_json(args.out_dir / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
