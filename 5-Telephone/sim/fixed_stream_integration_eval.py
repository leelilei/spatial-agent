#!/usr/bin/env python3
"""Paired fixed-stream test of listener-side memory integration.

The full Telephone simulation lets memory affect later speech, so GA and PROV
normally receive different downstream conversations.  This audit freezes the
realized event stream from an existing PROV run, reconstructs the structured
provenance metadata that was present during that run, and replays the identical
per-agent observations into fresh GA and PROV memories.  The only experimental
difference is how the two memories represent, consolidate, retrieve, and answer
from the same received evidence.

Each source run (schedule seed) is one independent experimental unit.  The
script validates its reconstruction against the original PROV final states
before making any API calls, writes resumable per-seed results, and reports a
95% t interval over paired seed-level differences.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import math
import statistics as st
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RUNS_ROOT = ROOT / "sim" / "runs" / "prov_fair" / "prov" / "gpt-5.4-mini" / "prov"
DEFAULT_OUT = ROOT / "sim" / "runs" / "fixed_stream_integration_2026-07-23"
INTERVIEW_SYSTEM = (
    "Answer the question using ONLY the memory notes, reflecting the CURRENT state. "
    'Reply with one short sentence. Return ONLY JSON: {"answer": "..."}'
)
QUESTION = "When and where is the repair drive being held now?"
CURRENT_MARKERS = ("sunday", "community center")
STALE_MARKERS = ("saturday", "front porch", "porch")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def mean_ci95(values: list[float]) -> list[float]:
    if not values:
        return [0.0, 0.0, 0.0]
    if len(values) == 1:
        return [values[0], values[0], values[0]]
    mean = st.mean(values)
    sem = st.stdev(values) / math.sqrt(len(values))
    tcrit = {
        2: 12.706,
        3: 4.303,
        4: 3.182,
        5: 2.776,
        6: 2.571,
        7: 2.447,
        8: 2.365,
        9: 2.306,
        10: 2.262,
    }.get(len(values), 1.96)
    half = tcrit * sem
    return [round(mean, 4), round(mean - half, 4), round(mean + half, 4)]


def reconstruct_fixed_stream(run_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    """Rebuild per-agent observations and the PROV side channel from round logs.

    Encounters within a round are generated before any of that round's
    observations are committed, so every utterance is stamped from the
    speaker's state at the start of the round.  Injection occurs after encounter
    observations, matching society.run_round.
    """
    summary = load_json(run_dir / "sim_summary.json")
    agents = summary.get("agents", [])
    if not agents:
        raise ValueError(f"missing agents in {run_dir / 'sim_summary.json'}")
    name_to_id = {row["name"]: row["id"] for row in agents}
    events: dict[str, list[dict[str, Any]]] = {row["id"]: [] for row in agents}
    state: dict[str, dict[str, Any] | None] = {row["id"]: None for row in agents}

    round_paths = sorted(run_dir.glob("round_*.json"))
    if not round_paths:
        raise ValueError(f"no round logs in {run_dir}")

    for round_path in round_paths:
        round_log = load_json(round_path)
        round_idx = int(round_log["round"])
        start_state = {aid: (dict(value) if value else None) for aid, value in state.items()}
        observations: list[tuple[str, str, dict[str, Any]]] = []

        for encounter in round_log.get("encounters", []):
            a_id = name_to_id[encounter["a"]]
            b_id = name_to_id[encounter["b"]]
            for utterance in encounter.get("utterances", []):
                event = {
                    "round": round_idx,
                    "text": utterance["text"],
                    "speaker": utterance["speaker"],
                    "listener": utterance["listener"],
                }
                speaker_id = name_to_id.get(utterance["speaker"])
                speaker_state = start_state.get(speaker_id) if speaker_id else None
                if speaker_state:
                    event["prov"] = {
                        "value": speaker_state["value"],
                        "version": speaker_state["version"],
                        "source": speaker_id,
                    }
                observations.append((a_id, b_id, event))

        # Society applies all encounter observations only after generating the round.
        for a_id, b_id, event in observations:
            for agent_id in (a_id, b_id):
                events[agent_id].append(dict(event))
                prov = event.get("prov")
                current_version = int(state[agent_id]["version"]) if state[agent_id] else -1
                if prov and int(prov.get("version", -1)) > current_version:
                    state[agent_id] = {
                        "version": int(prov["version"]),
                        "value": str(prov.get("value", "")),
                    }

        for injection in round_log.get("injected", []):
            agent_id = name_to_id[injection["agent"]]
            event = {
                "round": round_idx,
                "text": injection["text"],
                "speaker": "world",
                "listener": injection["agent"],
                "injected": True,
                "prov": {
                    "version": round_idx,
                    "value": injection["text"],
                    "auth": True,
                    "source": "ORIGIN",
                    "path": ["ORIGIN"],
                },
            }
            events[agent_id].append(event)
            current_version = int(state[agent_id]["version"]) if state[agent_id] else -1
            if round_idx > current_version:
                state[agent_id] = {"version": round_idx, "value": injection["text"]}

    original = load_json(run_dir / "memory_snapshots.json")
    mismatches: list[dict[str, Any]] = []
    for agent_id in events:
        expected = {
            "version": int(original[agent_id].get("version", -1)),
            "value": str(original[agent_id].get("value", "")),
        }
        actual = state[agent_id] or {"version": -1, "value": ""}
        if expected != actual:
            mismatches.append({"agent_id": agent_id, "expected": expected, "actual": actual})
    if mismatches:
        raise ValueError(
            f"provenance reconstruction mismatch for {run_dir}: "
            f"{json.dumps(mismatches[:3], ensure_ascii=False)}"
        )

    id_to_name = {row["id"]: row["name"] for row in agents}
    snapshot = {
        agent_id: {"kind": "fixed_stream", "name": id_to_name[agent_id], "events": rows}
        for agent_id, rows in events.items()
    }
    all_events = [event for rows in events.values() for event in rows]
    manifest = {
        "source_run": str(run_dir),
        "schedule_seed": summary.get("schedule_seed"),
        "agent_count": len(agents),
        "rounds": len(round_paths),
        "event_observations": len(all_events),
        "provenance_observations": sum(1 for event in all_events if event.get("prov")),
        "provenance_receivers": sum(
            1 for rows in events.values() if any(event.get("prov") for event in rows)
        ),
        "reconstruction_matches_original": True,
    }
    return snapshot, manifest


def tally(results: dict[str, Any]) -> dict[str, int]:
    counts = {"current": 0, "stale": 0, "unknown": 0}
    for row in results.values():
        verdict = str(row.get("verdict", "unknown"))
        counts[verdict if verdict in counts else "unknown"] += 1
    return counts


def replay_agent(memory: str, agent_id: str, stream: dict[str, Any], llm: Any) -> dict[str, Any]:
    """Replay one agent independently; fixed streams make agents conditionally separable."""
    from society import build_memory_factory

    memory_obj = build_memory_factory(memory, llm)()
    by_round: dict[int, list[dict[str, Any]]] = {}
    for event in stream.get("events", []):
        by_round.setdefault(int(event.get("round", 0)), []).append(event)
    for round_idx in sorted(by_round):
        for event in by_round[round_idx]:
            memory_obj.observe(event)
        memory_obj.consolidate()

    context = memory_obj.retrieve(QUESTION)
    out = llm.complete_json(
        INTERVIEW_SYSTEM,
        f"Memory notes:\n{context or '(none)'}\n\nQuestion: {QUESTION}",
    )
    answer = str(out.get("answer", ""))
    lower = answer.lower()
    has_current = any(marker in lower for marker in CURRENT_MARKERS)
    has_stale = any(marker in lower for marker in STALE_MARKERS)
    verdict = "current" if (has_current and not has_stale) else ("stale" if has_stale else "unknown")
    return {
        "agent_id": agent_id,
        "interview": {"name": stream.get("name", agent_id), "answer": answer, "verdict": verdict},
        "memory": memory_obj.snapshot(),
    }


def condition_result(
    memory: str,
    snapshot: dict[str, Any],
    llm: Any,
    *,
    workers: int,
    out_dir: Path,
) -> dict[str, Any]:
    checkpoint_dir = out_dir / f"checkpoints_{memory}"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    records: dict[str, dict[str, Any]] = {}
    pending: list[tuple[str, dict[str, Any]]] = []
    for agent_id, stream in snapshot.items():
        checkpoint = checkpoint_dir / f"{agent_id}.json"
        if checkpoint.exists():
            records[agent_id] = load_json(checkpoint)
        else:
            pending.append((agent_id, stream))

    failures: list[dict[str, str]] = []
    if pending:
        executor = ThreadPoolExecutor(max_workers=max(1, workers))
        future_to_agent = {
            executor.submit(replay_agent, memory, agent_id, stream, llm): agent_id
            for agent_id, stream in pending
        }
        try:
            for future in as_completed(future_to_agent):
                agent_id = future_to_agent[future]
                try:
                    record = future.result()
                except Exception as exc:
                    failures.append({"agent_id": agent_id, "error_type": type(exc).__name__})
                    for queued in future_to_agent:
                        queued.cancel()
                    break
                records[agent_id] = record
                write_json(checkpoint_dir / f"{agent_id}.json", record)
                print(f"  {memory}: checkpoint {agent_id} ({len(records)}/{len(snapshot)})", flush=True)
        finally:
            executor.shutdown(wait=True, cancel_futures=True)

    if failures or len(records) != len(snapshot):
        write_json(
            out_dir / f"incomplete_{memory}.json",
            {
                "completed_agents": sorted(records),
                "missing_agents": sorted(set(snapshot) - set(records)),
                "failures": failures,
                "policy": "condition incomplete; rerun resumes only missing agents",
            },
        )
        raise RuntimeError(f"incomplete {memory} condition")

    interviews = {agent_id: records[agent_id]["interview"] for agent_id in sorted(records)}
    memory_snapshots = {agent_id: records[agent_id]["memory"] for agent_id in sorted(records)}
    write_json(out_dir / f"interview_{memory}.json", interviews)
    write_json(out_dir / f"memory_{memory}.json", memory_snapshots)
    counts = tally(interviews)
    return {
        "counts": counts,
        "current_rate": counts["current"] / len(snapshot),
        "stale_rate": counts["stale"] / len(snapshot),
        "unknown_rate": counts["unknown"] / len(snapshot),
    }


def configure_transport_limits(llm: Any, *, timeout: int, retries: int) -> None:
    """Bound provider stalls without changing the shared project configuration file."""
    if dataclasses.is_dataclass(llm.config):
        llm.config = dataclasses.replace(llm.config, timeout=timeout, retries=retries)
    if dataclasses.is_dataclass(llm.client):
        llm.client = dataclasses.replace(llm.client, timeout=timeout)


def aggregate_results(seed_results: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [row for row in seed_results if set(row.get("conditions", {})) == {"ga", "prov"}]
    conditions: dict[str, Any] = {}
    for memory in ("ga", "prov"):
        current = [row["conditions"][memory]["current_rate"] for row in valid]
        stale = [row["conditions"][memory]["stale_rate"] for row in valid]
        unknown = [row["conditions"][memory]["unknown_rate"] for row in valid]
        conditions[memory] = {
            "current_rate_ci95": mean_ci95(current),
            "stale_rate_ci95": mean_ci95(stale),
            "unknown_rate_ci95": mean_ci95(unknown),
            "per_seed_current_rate": current,
        }

    d_current = [
        row["conditions"]["prov"]["current_rate"] - row["conditions"]["ga"]["current_rate"]
        for row in valid
    ]
    d_net = [
        (row["conditions"]["prov"]["current_rate"] - row["conditions"]["prov"]["stale_rate"])
        - (row["conditions"]["ga"]["current_rate"] - row["conditions"]["ga"]["stale_rate"])
        for row in valid
    ]
    positives = sum(value > 0 for value in d_current)
    negatives = sum(value < 0 for value in d_current)
    non_ties = positives + negatives
    tail = min(positives, negatives)
    sign_p = min(
        1.0,
        2.0 * sum(math.comb(non_ties, i) for i in range(tail + 1)) / (2**non_ties),
    ) if non_ties else 1.0
    return {
        "design": "paired fixed per-agent event stream; independent unit = source schedule seed",
        "n_seeds": len(valid),
        "seeds": [row["schedule_seed"] for row in valid],
        "conditions": conditions,
        "paired_prov_minus_ga": {
            "current_rate_ci95": mean_ci95(d_current),
            "net_current_minus_stale_rate_ci95": mean_ci95(d_net),
            "per_seed_current_rate_difference": d_current,
            "prov_higher_seed_count": positives,
            "ga_higher_seed_count": negatives,
            "ties_seed_count": sum(value == 0 for value in d_current),
            "exact_two_sided_sign_test_p": round(sign_p, 6),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs-root", type=Path, default=DEFAULT_RUNS_ROOT)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="provider config for memory replay; unused with --prepare-only",
    )
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--max-streams", type=int, default=8)
    parser.add_argument(
        "--prepare-only",
        action="store_true",
        help="reconstruct and validate frozen streams without making API calls",
    )
    args = parser.parse_args()

    run_dirs = sorted(path for path in args.runs_root.glob("run_*") if path.is_dir())[: args.max_streams]
    if not run_dirs:
        raise ValueError(f"no source run directories in {args.runs_root}")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    prepared: list[tuple[dict[str, Any], dict[str, Any], Path]] = []
    for run_dir in run_dirs:
        snapshot, manifest = reconstruct_fixed_stream(run_dir)
        seed_dir = args.out_dir / f"seed_{manifest['schedule_seed']}"
        write_json(seed_dir / "fixed_stream.json", snapshot)
        write_json(seed_dir / "manifest.json", manifest)
        prepared.append((snapshot, manifest, seed_dir))
        print(
            f"prepared seed={manifest['schedule_seed']} events={manifest['event_observations']} "
            f"prov={manifest['provenance_observations']} receivers={manifest['provenance_receivers']}",
            flush=True,
        )

    if args.prepare_only:
        print(f"validated {len(prepared)} fixed streams -> {args.out_dir}")
        return 0

    from llm import DEFAULT_CONFIG, LLM

    llm = LLM(config=args.config or DEFAULT_CONFIG, model=args.model)
    configure_transport_limits(llm, timeout=max(10, args.timeout), retries=max(0, args.retries))
    seed_results: list[dict[str, Any]] = []
    for snapshot, manifest, seed_dir in prepared:
        result_path = seed_dir / "result.json"
        if result_path.exists():
            existing = load_json(result_path)
            if set(existing.get("conditions", {})) == {"ga", "prov"}:
                print(f"resume seed={manifest['schedule_seed']} from {result_path}", flush=True)
                seed_results.append(existing)
                continue
            print(f"continue partial seed={manifest['schedule_seed']} from {result_path}", flush=True)
            row = existing
        else:
            row = {
                "schedule_seed": manifest["schedule_seed"],
                "manifest": manifest,
                "conditions": {},
            }
        # PROV is cheap (no reflection calls) and provides an early reconstruction sanity check.
        for memory in ("prov", "ga"):
            interview_path = seed_dir / f"interview_{memory}.json"
            memory_path = seed_dir / f"memory_{memory}.json"
            if interview_path.exists() and memory_path.exists():
                print(f"reuse seed={manifest['schedule_seed']} condition={memory}", flush=True)
                counts = tally(load_json(interview_path))
                row["conditions"][memory] = {
                    "counts": counts,
                    "current_rate": counts["current"] / len(snapshot),
                    "stale_rate": counts["stale"] / len(snapshot),
                    "unknown_rate": counts["unknown"] / len(snapshot),
                }
                write_json(result_path, row)
                continue
            print(f"seed={manifest['schedule_seed']} condition={memory}", flush=True)
            try:
                row["conditions"][memory] = condition_result(
                    memory,
                    snapshot,
                    llm,
                    workers=max(1, args.workers),
                    out_dir=seed_dir,
                )
            except Exception as exc:
                # Do not stringify provider exceptions: subprocess errors may embed
                # authorization headers in their command representation.
                failure = {
                    "schedule_seed": manifest["schedule_seed"],
                    "condition": memory,
                    "error_type": type(exc).__name__,
                    "policy": "discard entire seed-condition and rerun; never score as unknown",
                }
                write_json(seed_dir / f"failure_{memory}.json", failure)
                print(
                    f"FAILED seed={manifest['schedule_seed']} condition={memory} "
                    f"error={type(exc).__name__}; no result recorded",
                    flush=True,
                )
                return 2
            write_json(result_path, row)
        seed_results.append(row)

    aggregate = aggregate_results(seed_results)
    aggregate["source_stream_model"] = "gpt-5.4-mini"
    aggregate["replay_model"] = args.model
    aggregate["stream_conditioning"] = (
        "realized PROV-run dialogue streams; both replay memories receive identical text and metadata"
    )
    aggregate["failure_policy"] = "no provider failure scored as unknown; incomplete agents are checkpointed and rerun"
    write_json(args.out_dir / "aggregate.json", aggregate)
    print(json.dumps(aggregate, ensure_ascii=False, indent=2))
    print(f"fixed-stream results -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
