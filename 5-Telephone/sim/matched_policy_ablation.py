#!/usr/bin/env python3
"""Strict matched-policy ablation on frozen per-agent communication streams.

The earlier fixed-stream audit compares complete GA and PROV memory pipelines.
That design holds received events fixed but changes representation, consolidation,
retrieval, and prompting together.  This experiment instead uses one common
pipeline and changes exactly one decision rule:

* ``frequency`` selects the value with the most received mentions (ties: latest);
* ``version_max`` selects the candidate with the highest event version
  (ties: latest).

Every recognizable event claim is normalized into the same typed candidate
record.  The version annotation is supplied by the controlled task definition:
the initial Saturday/front-porch value is version 0 and the injected
Sunday/community-center value is version 1.  Ambiguous text that mentions both
values without structured provenance is excluded.  This normalization is a
mechanism assay, not evidence that ordinary dialogue supplies trustworthy
versions.

Both conditions share the candidate store, consolidation schedule, one-record
retrieval budget, context format, interview prompt, model, and frozen stream.
The script reports the selected-state accuracy and, unless ``--symbolic-only``
is set, the answer produced by the common LLM interview.
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
DEFAULT_STREAM_ROOT = ROOT / "sim" / "runs" / "fixed_stream_integration_2026-07-23"
DEFAULT_OUT = ROOT / "sim" / "runs" / "matched_policy_ablation_2026-07-23"
INTERVIEW_SYSTEM = (
    "Answer the question using ONLY the memory notes, reflecting the CURRENT state. "
    'Reply with one short sentence. Return ONLY JSON: {"answer": "..."}'
)
QUESTION = "When and where is the repair drive being held now?"
CURRENT_ANSWER = "The repair drive is being held on Sunday at the community center."
STALE_ANSWER = "The repair drive is being held on Saturday at the front porch."
CURRENT_MARKERS = ("sunday", "community center")
STALE_MARKERS = ("saturday", "front porch", "porch")
POLICIES = ("frequency", "version_max")


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


def exact_two_sided_sign_test(differences: list[float]) -> dict[str, Any]:
    positives = sum(value > 0 for value in differences)
    negatives = sum(value < 0 for value in differences)
    ties = sum(value == 0 for value in differences)
    non_ties = positives + negatives
    if not non_ties:
        p_value = 1.0
    else:
        tail = min(positives, negatives)
        p_value = min(
            1.0,
            2.0 * sum(math.comb(non_ties, i) for i in range(tail + 1)) / (2**non_ties),
        )
    return {
        "version_max_higher_seed_count": positives,
        "frequency_higher_seed_count": negatives,
        "ties_seed_count": ties,
        "exact_two_sided_sign_test_p": round(p_value, 6),
    }


def classify_text(text: str) -> str:
    lower = text.lower()
    has_current = any(marker in lower for marker in CURRENT_MARKERS)
    has_stale = any(marker in lower for marker in STALE_MARKERS)
    if has_current and not has_stale:
        return "current"
    if has_stale and not has_current:
        return "stale"
    return "ambiguous" if (has_current and has_stale) else "irrelevant"


def normalize_candidates(events: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    candidates: list[dict[str, Any]] = []
    audit = {
        "events_total": len(events),
        "explicit_provenance": 0,
        "unambiguous_text_annotation": 0,
        "ambiguous_excluded": 0,
        "irrelevant_excluded": 0,
    }
    for sequence, event in enumerate(events):
        provenance = event.get("prov")
        label = classify_text(str(event.get("text", "")))
        if provenance is not None:
            version = int(provenance.get("version", -1))
            value = "current" if version >= 1 else "stale"
            basis = "explicit_provenance"
            audit["explicit_provenance"] += 1
        elif label in {"current", "stale"}:
            value = label
            version = 1 if label == "current" else 0
            basis = "controlled_task_annotation"
            audit["unambiguous_text_annotation"] += 1
        else:
            audit[f"{label}_excluded"] += 1
            continue
        candidates.append(
            {
                "sequence": sequence,
                "round": int(event.get("round", 0)),
                "speaker": str(event.get("speaker", "")),
                "value": value,
                "version": version,
                "annotation_basis": basis,
            }
        )
    return candidates, audit


def select_candidate(candidates: list[dict[str, Any]], policy: str) -> dict[str, Any] | None:
    if not candidates:
        return None
    if policy == "version_max":
        return max(candidates, key=lambda row: (int(row["version"]), int(row["sequence"])))
    if policy == "frequency":
        counts = {
            "current": sum(row["value"] == "current" for row in candidates),
            "stale": sum(row["value"] == "stale" for row in candidates),
        }
        winning_value = (
            candidates[-1]["value"]
            if counts["current"] == counts["stale"]
            else max(counts, key=counts.get)
        )
        return max(
            (row for row in candidates if row["value"] == winning_value),
            key=lambda row: int(row["sequence"]),
        )
    raise ValueError(f"unknown policy: {policy}")


def render_context(selected: dict[str, Any] | None) -> str:
    if selected is None:
        return "(none)"
    answer = CURRENT_ANSWER if selected["value"] == "current" else STALE_ANSWER
    return (
        "Integrated event record:\n"
        f"- event version: {selected['version']}\n"
        f"- current stored answer: {answer}"
    )


def score_answer(answer: str) -> str:
    lower = answer.lower()
    has_current = any(marker in lower for marker in CURRENT_MARKERS)
    has_stale = any(marker in lower for marker in STALE_MARKERS)
    if has_current and not has_stale:
        return "current"
    if has_stale:
        return "stale"
    return "unknown"


def configure_transport_limits(llm: Any, *, timeout: int, retries: int) -> None:
    if dataclasses.is_dataclass(llm.config):
        llm.config = dataclasses.replace(llm.config, timeout=timeout, retries=retries)
    if dataclasses.is_dataclass(llm.client):
        llm.client = dataclasses.replace(llm.client, timeout=timeout)


def interview_one(
    llm: Any,
    *,
    seed: int,
    agent_id: str,
    policy: str,
    context: str,
) -> dict[str, Any]:
    out = llm.complete_json(
        INTERVIEW_SYSTEM,
        f"Memory notes:\n{context}\n\nQuestion: {QUESTION}",
    )
    answer = str(out.get("answer", ""))
    return {
        "schedule_seed": seed,
        "agent_id": agent_id,
        "policy": policy,
        "answer": answer,
        "verdict": score_answer(answer),
    }


def prepare_seed(seed_dir: Path) -> dict[str, Any]:
    manifest = load_json(seed_dir / "manifest.json")
    streams = load_json(seed_dir / "fixed_stream.json")
    records: dict[str, Any] = {}
    audit_total = {
        "events_total": 0,
        "explicit_provenance": 0,
        "unambiguous_text_annotation": 0,
        "ambiguous_excluded": 0,
        "irrelevant_excluded": 0,
    }
    for agent_id, stream in streams.items():
        candidates, audit = normalize_candidates(stream.get("events", []))
        for key, value in audit.items():
            audit_total[key] += value
        selections = {
            policy: select_candidate(candidates, policy)
            for policy in POLICIES
        }
        records[agent_id] = {
            "name": stream.get("name", agent_id),
            "candidate_count": len(candidates),
            "candidate_value_counts": {
                "current": sum(row["value"] == "current" for row in candidates),
                "stale": sum(row["value"] == "stale" for row in candidates),
            },
            "selections": selections,
            "contexts": {
                policy: render_context(selections[policy])
                for policy in POLICIES
            },
        }
    return {
        "schedule_seed": int(manifest["schedule_seed"]),
        "agent_count": len(records),
        "source_stream": str(seed_dir / "fixed_stream.json"),
        "normalization_audit": audit_total,
        "agents": records,
    }


def tally_seed(seed: dict[str, Any], behavioral: dict[str, Any] | None = None) -> dict[str, Any]:
    row: dict[str, Any] = {
        "schedule_seed": seed["schedule_seed"],
        "agent_count": seed["agent_count"],
        "eligible_agents": sum(
            record["candidate_count"] > 0 for record in seed["agents"].values()
        ),
        "symbolic": {},
    }
    for policy in POLICIES:
        counts = {"current": 0, "stale": 0, "unknown": 0}
        for record in seed["agents"].values():
            selected = record["selections"][policy]
            verdict = selected["value"] if selected else "unknown"
            counts[verdict] += 1
        row["symbolic"][policy] = {
            "counts": counts,
            "current_rate": counts["current"] / seed["agent_count"],
        }
    if behavioral is not None:
        row["behavioral"] = {}
        for policy in POLICIES:
            counts = {"current": 0, "stale": 0, "unknown": 0}
            for record in behavioral.values():
                if record["policy"] == policy:
                    counts[record["verdict"]] += 1
            row["behavioral"][policy] = {
                "counts": counts,
                "current_rate": counts["current"] / seed["agent_count"],
            }
    return row


def aggregate(seed_rows: list[dict[str, Any]], measure: str) -> dict[str, Any]:
    conditions: dict[str, Any] = {}
    for policy in POLICIES:
        rates = [row[measure][policy]["current_rate"] for row in seed_rows]
        conditions[policy] = {
            "current_rate_ci95": mean_ci95(rates),
            "per_seed_current_rate": rates,
        }
    differences = [
        row[measure]["version_max"]["current_rate"]
        - row[measure]["frequency"]["current_rate"]
        for row in seed_rows
    ]
    paired = {
        "current_rate_difference_ci95": mean_ci95(differences),
        "per_seed_current_rate_difference": differences,
    }
    paired.update(exact_two_sided_sign_test(differences))
    return {"conditions": conditions, "paired_version_max_minus_frequency": paired}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stream-root", type=Path, default=DEFAULT_STREAM_ROOT)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="provider config for behavioral interviews; unused with --symbolic-only",
    )
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--retries", type=int, default=1)
    parser.add_argument("--symbolic-only", action="store_true")
    args = parser.parse_args()

    seed_dirs = sorted(path for path in args.stream_root.glob("seed_*") if path.is_dir())
    if not seed_dirs:
        raise ValueError(f"no seed directories in {args.stream_root}")
    args.out_dir.mkdir(parents=True, exist_ok=True)

    prepared = [prepare_seed(seed_dir) for seed_dir in seed_dirs]
    for seed in prepared:
        write_json(args.out_dir / f"seed_{seed['schedule_seed']}" / "prepared.json", seed)

    behavioral_by_seed: dict[int, dict[str, Any]] = {}
    if not args.symbolic_only:
        from llm import DEFAULT_CONFIG, LLM

        llm = LLM(config=args.config or DEFAULT_CONFIG, model=args.model)
        configure_transport_limits(llm, timeout=max(10, args.timeout), retries=max(0, args.retries))
        jobs: list[tuple[int, str, str, str, Path]] = []
        for seed in prepared:
            seed_out = args.out_dir / f"seed_{seed['schedule_seed']}"
            behavioral_by_seed[seed["schedule_seed"]] = {}
            for agent_id, record in seed["agents"].items():
                for policy in POLICIES:
                    checkpoint = seed_out / "checkpoints" / policy / f"{agent_id}.json"
                    key = f"{policy}:{agent_id}"
                    if checkpoint.exists():
                        behavioral_by_seed[seed["schedule_seed"]][key] = load_json(checkpoint)
                    else:
                        jobs.append(
                            (
                                seed["schedule_seed"],
                                agent_id,
                                policy,
                                record["contexts"][policy],
                                checkpoint,
                            )
                        )

        failures: list[dict[str, str]] = []
        executor = ThreadPoolExecutor(max_workers=max(1, args.workers))
        future_to_job = {
            executor.submit(
                interview_one,
                llm,
                seed=seed,
                agent_id=agent_id,
                policy=policy,
                context=context,
            ): (seed, agent_id, policy, checkpoint)
            for seed, agent_id, policy, context, checkpoint in jobs
        }
        try:
            for completed, future in enumerate(as_completed(future_to_job), start=1):
                seed, agent_id, policy, checkpoint = future_to_job[future]
                try:
                    record = future.result()
                except Exception as exc:
                    failures.append(
                        {
                            "schedule_seed": str(seed),
                            "agent_id": agent_id,
                            "policy": policy,
                            "error_type": type(exc).__name__,
                        }
                    )
                    continue
                write_json(checkpoint, record)
                behavioral_by_seed[seed][f"{policy}:{agent_id}"] = record
                if completed % 25 == 0 or completed == len(jobs):
                    print(f"interviews completed: {completed}/{len(jobs)}", flush=True)
        finally:
            executor.shutdown(wait=True, cancel_futures=False)
        if failures:
            write_json(args.out_dir / "failures.json", failures)
            raise RuntimeError(f"{len(failures)} interview calls failed; rerun resumes checkpoints")

    seed_rows = []
    for seed in prepared:
        behavioral = None if args.symbolic_only else behavioral_by_seed[seed["schedule_seed"]]
        row = tally_seed(seed, behavioral)
        seed_rows.append(row)
        write_json(args.out_dir / f"seed_{seed['schedule_seed']}" / "result.json", row)

    result: dict[str, Any] = {
        "design": (
            "paired frozen stream; identical normalized candidate store, consolidation, "
            "one-record retrieval, context format, and interview; selector policy only differs"
        ),
        "normalization_boundary": (
            "versions for unambiguous text claims are analysis annotations from the controlled "
            "task definition; ambiguous unstructured claims are excluded"
        ),
        "independent_unit": "source schedule seed",
        "n_seeds": len(seed_rows),
        "agent_count_per_seed": seed_rows[0]["agent_count"],
        "symbolic": aggregate(seed_rows, "symbolic"),
        "seed_results": seed_rows,
    }
    if not args.symbolic_only:
        result["behavioral"] = aggregate(seed_rows, "behavioral")
        result["interview_model"] = args.model
        result["interview_prompt"] = INTERVIEW_SYSTEM
        result["failure_policy"] = "failed calls are checkpointed separately and never scored"
    write_json(args.out_dir / "aggregate.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"matched-policy results -> {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
