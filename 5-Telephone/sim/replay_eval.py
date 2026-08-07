#!/usr/bin/env python3
"""Controlled, low-variance memory eval: replay a FIXED society event stream.

The full society sim is chaotically stochastic (temp-0 does not give bit
reproducibility; one different token cascades into divergent conversation paths),
so single runs cannot attribute an outcome to the memory architecture. This harness
removes the dominant noise source — behavioural divergence — by holding the event
stream FIXED: we take the per-agent observed events from one society snapshot and
replay the SAME events into fresh GA and SMGA memories, then interview. The only
remaining stochasticity is the consolidation + interview LLM calls, which we average
over `--replays`. Because both conditions see identical events, the comparison is
fair and isolates how each memory REPRESENTS / RESOLVES / RETRIEVES currency.

This is the (C) instrument in the B+C plan: a clean mechanism read, and the fast
test rig for evaluating the (B) entity-centric currency-propagation memory.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics as st
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

from llm import DEFAULT_CONFIG, LLM
from society import INTERVIEW_SYSTEM, build_memory_factory, demo_world

QUESTION = "When and where is the repair drive being held now?"
CURRENT_MARKERS = ("sunday", "community center")


def resilient_interview(
    world: Any,
    question: str,
    llm: LLM,
    *,
    workers: int = 1,
    strict: bool = False,
) -> dict[str, Any]:
    """Per-agent interview that survives a provider hiccup (one failure -> unknown)."""
    current_markers = ("sunday", "community center")
    stale_markers = ("saturday", "front porch", "porch")
    def interview_agent(a: Any) -> tuple[str, dict[str, Any]]:
        try:
            ctx = a.memory.retrieve(question)
            out = llm.complete_json(INTERVIEW_SYSTEM, f"Memory notes:\n{ctx or '(none)'}\n\nQuestion: {question}")
            ans = str(out.get("answer", ""))
        except Exception as exc:
            if strict:
                raise
            print(f"  interview failed {a.agent_id}: {type(exc).__name__}", flush=True)
            return a.agent_id, {"name": a.name, "answer": "", "verdict": "unknown"}
        low = ans.lower()
        has_cur = any(m in low for m in current_markers)
        has_sta = any(m in low for m in stale_markers)
        verdict = "current" if (has_cur and not has_sta) else ("stale" if has_sta else "unknown")
        return a.agent_id, {"name": a.name, "answer": ans, "verdict": verdict}

    if workers > 1 and len(world.agents) > 1:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            rows = list(executor.map(interview_agent, world.agents))
    else:
        rows = [interview_agent(agent) for agent in world.agents]
    return dict(rows)


def per_agent_round_events(snapshot: dict[str, Any]) -> dict[str, dict[int, list[dict[str, Any]]]]:
    out: dict[str, dict[int, list[dict[str, Any]]]] = {}
    for aid, s in snapshot.items():
        by_round: dict[int, list[dict[str, Any]]] = {}
        for e in s.get("events", []):
            by_round.setdefault(int(e.get("round", 0)), []).append(e)
        out[aid] = by_round
    return out


def replay_once(memory_kind: str, snapshot: dict[str, Any], llm: LLM, *,
                agent_count: int, workers: int,
                strict: bool = False) -> tuple[dict[str, Any], dict[str, Any]]:
    """Build fresh memories, replay the fixed event stream round by round, interview."""
    world = demo_world(build_memory_factory(memory_kind, llm), agent_count=agent_count)
    ev = per_agent_round_events(snapshot)
    rounds = sorted({r for a in ev.values() for r in a})
    def safe_consolidate(a: Any) -> None:
        try:
            a.memory.consolidate()
        except Exception as exc:  # one provider hiccup must not drop the whole replay
            if strict:
                raise
            print(f"  consolidate failed {a.agent_id}: {type(exc).__name__}", flush=True)

    for r in rounds:
        print(f"  {memory_kind}: replay round {r}", flush=True)
        for a in world.agents:
            for e in ev.get(a.agent_id, {}).get(r, []):
                a.memory.observe(e)
        if workers > 1 and len(world.agents) > 1:
            with ThreadPoolExecutor(max_workers=workers) as ex:
                list(ex.map(safe_consolidate, world.agents))
        else:
            for a in world.agents:
                safe_consolidate(a)
    print(f"  {memory_kind}: interview", flush=True)
    results = resilient_interview(world, QUESTION, llm, workers=workers, strict=strict)
    snapshots = {a.agent_id: a.memory.snapshot() for a in world.agents}
    return results, snapshots


def tally(results: dict[str, Any]) -> dict[str, int]:
    t = {"current": 0, "stale": 0, "unknown": 0}
    for item in results.values():
        v = str(item.get("verdict", "unknown"))
        t[v if v in t else "unknown"] += 1
    return t


def receiver_ids(snapshot: dict[str, Any]) -> set[str]:
    """Agents whose fixed event stream contains the current update signal."""
    ids: set[str] = set()
    for aid, state in snapshot.items():
        for event in state.get("events", []):
            text = str(event.get("text", "")).lower()
            if any(marker in text for marker in CURRENT_MARKERS):
                ids.add(aid)
                break
    return ids


def tally_subset(results: dict[str, Any], ids: set[str]) -> dict[str, int]:
    return tally({aid: item for aid, item in results.items() if aid in ids})


def ci95(xs: list[float]) -> tuple[float, float, float]:
    n = len(xs)
    if n < 2:
        x = xs[0] if xs else 0.0
        return (x, x, x)
    m = st.mean(xs)
    se = st.stdev(xs) / math.sqrt(n)
    t = {2: 12.71, 3: 4.30, 4: 3.18, 5: 2.78, 6: 2.57, 7: 2.45, 8: 2.36,
         9: 2.31, 10: 2.26}.get(n, 2.04)
    return m, m - t * se, m + t * se


def main() -> int:
    p = argparse.ArgumentParser(description="Replay a fixed society event stream into memory conditions.")
    p.add_argument("--snapshot", type=Path, required=True, help="memory_snapshots.json providing the fixed event stream")
    p.add_argument("--memory", action="append", default=None, help="memory condition; repeatable (default ga, smga)")
    p.add_argument("--model", default="gpt-5.4-mini")
    p.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    p.add_argument("--replays", type=int, default=5)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--save-memory-snapshots", action="store_true")
    p.add_argument("--out-dir", type=Path, default=Path("sim/runs/replay_eval/latest"))
    args = p.parse_args()

    memories = tuple(args.memory or ("ga", "smga"))
    snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    agent_count = len(snapshot)
    receivers = receiver_ids(snapshot)
    receiver_count = len(receivers)
    llm = LLM(config=args.config, model=args.model)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    per_cond_tallies: dict[str, list[dict[str, int]]] = {m: [] for m in memories}
    per_cond_receiver_tallies: dict[str, list[dict[str, int]]] = {m: [] for m in memories}
    per_replay_agent_verdicts: list[dict[str, dict[str, str]]] = []  # [{cond: {agent_id: verdict}}]

    for i in range(args.replays):
        replay_record: dict[str, dict[str, str]] = {}
        for m in memories:
            try:
                print(f"replay {i} {m}: start", flush=True)
                res, memory_snapshots = replay_once(
                    m, snapshot, llm, agent_count=agent_count, workers=args.workers)
            except Exception as exc:
                print(f"!! replay {i} {m} failed (skipped): {exc}", flush=True)
                continue
            per_cond_tallies[m].append(tally(res))
            per_cond_receiver_tallies[m].append(tally_subset(res, receivers))
            replay_record[m] = {aid: r["verdict"] for aid, r in res.items()}
            (args.out_dir / f"replay_{i:02d}_{m}.json").write_text(
                json.dumps({"question": QUESTION, "results": res}, ensure_ascii=False, indent=2), encoding="utf-8")
            if args.save_memory_snapshots:
                (args.out_dir / f"replay_{i:02d}_{m}_memory_snapshots.json").write_text(
                    json.dumps(memory_snapshots, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"replay {i} {m}: {tally(res)}", flush=True)
        per_replay_agent_verdicts.append(replay_record)

    # aggregate
    summary: dict[str, Any] = {"snapshot": str(args.snapshot), "agent_count": agent_count,
                               "receiver_agent_count": receiver_count, "receiver_ids": sorted(receivers),
                               "replays": args.replays, "memories": list(memories), "conditions": {}}
    for m in memories:
        ts = per_cond_tallies[m]
        rates = {k: [t[k] / agent_count for t in ts] for k in ("current", "stale", "unknown")}
        rts = per_cond_receiver_tallies[m]
        rrates = {k: [t[k] / receiver_count for t in rts] for k in ("current", "stale", "unknown")}
        summary["conditions"][m] = {
            "mean_counts": {k: round(st.mean([t[k] for t in ts]), 2) for k in ("current", "stale", "unknown")},
            "current_rate_ci": [round(x, 3) for x in ci95(rates["current"])],
            "stale_rate_ci": [round(x, 3) for x in ci95(rates["stale"])],
            "net_rate": round(st.mean([(t["current"] - t["stale"]) / agent_count for t in ts]), 3),
            "receiver_mean_counts": {k: round(st.mean([t[k] for t in rts]), 2)
                                     for k in ("current", "stale", "unknown")},
            "receiver_current_rate_ci": [round(x, 3) for x in ci95(rrates["current"])],
            "receiver_stale_rate_ci": [round(x, 3) for x in ci95(rrates["stale"])],
            "receiver_net_rate": round(st.mean([(t["current"] - t["stale"]) / receiver_count
                                                for t in rts]), 3),
        }

    # paired (same fixed events): per replay, current_rate diff between conditions
    if len(memories) >= 2:
        paired: dict[str, Any] = {}
        for i_a, a in enumerate(memories):
            for b in memories[i_a + 1:]:
                n_pair = min(len(per_cond_tallies[a]), len(per_cond_tallies[b]))
                dcur = [(per_cond_tallies[b][i]["current"] - per_cond_tallies[a][i]["current"]) / agent_count
                        for i in range(n_pair)]
                dnet = [((per_cond_tallies[b][i]["current"] - per_cond_tallies[b][i]["stale"])
                         - (per_cond_tallies[a][i]["current"] - per_cond_tallies[a][i]["stale"])) / agent_count
                        for i in range(n_pair)]
                rdcur = [(per_cond_receiver_tallies[b][i]["current"] -
                          per_cond_receiver_tallies[a][i]["current"]) / receiver_count
                         for i in range(n_pair)]
                rdnet = [((per_cond_receiver_tallies[b][i]["current"] -
                           per_cond_receiver_tallies[b][i]["stale"])
                          - (per_cond_receiver_tallies[a][i]["current"] -
                             per_cond_receiver_tallies[a][i]["stale"])) / receiver_count
                         for i in range(n_pair)]
                paired[f"{b}-{a}"] = {
                    "d_current_rate_ci": [round(x, 3) for x in ci95(dcur)],
                    "d_net_rate_ci": [round(x, 3) for x in ci95(dnet)],
                    "receiver_d_current_rate_ci": [round(x, 3) for x in ci95(rdcur)],
                    "receiver_d_net_rate_ci": [round(x, 3) for x in ci95(rdnet)],
                }
        summary["paired_diff"] = paired

    (args.out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print("\n" + json.dumps(summary["conditions"], ensure_ascii=False, indent=2))
    if "paired_diff" in summary:
        print("\npaired:", json.dumps(summary["paired_diff"], ensure_ascii=False))
    print(f"\nreplay-eval logs -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
