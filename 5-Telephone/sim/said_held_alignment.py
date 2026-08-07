#!/usr/bin/env python3
"""Seed-level SAID statistics and descriptive agent-level SAID--HELD alignment.

The manuscript's headline SAID statistic pools final-round value-bearing
utterances across five societies.  This audit additionally treats a schedule
seed as the independent unit and reports the paired source-minus-baseline
difference.  It also describes, without a causal interpretation, the final
HELD outcomes of agents who publicly uttered a current marker in the final
round.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics as st
from pathlib import Path
from typing import Any


CURRENT_MARKERS = ("sunday", "community center")
# Public-utterance coding uses the registered stale values.  The looser bare
# "porch" marker is retained only by the private-answer scorer to catch terse
# stale interviews; treating any public use of "porch" as value-bearing would
# also capture unrelated porch conversation.
SAID_STALE_MARKERS = ("saturday", "front porch")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


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
    return [mean, mean - half, mean + half]


def classify(text: str) -> tuple[bool, bool]:
    lower = text.lower()
    return (
        any(marker in lower for marker in CURRENT_MARKERS),
        any(marker in lower for marker in SAID_STALE_MARKERS),
    )


def analyze_run(run_dir: Path, condition: str) -> dict[str, Any]:
    summary = load_json(run_dir / "sim_summary.json")
    round_paths = sorted(run_dir.glob("round_*.json"))
    if not round_paths:
        raise ValueError(f"no round logs in {run_dir}")
    final_round = load_json(round_paths[-1])

    name_to_id = {str(agent["name"]): str(agent["id"]) for agent in summary["agents"]}
    current_utterances = 0
    stale_utterances = 0
    value_bearing_utterances = 0
    final_utterances = 0
    agents_said_current: set[str] = set()
    agents_said_value: set[str] = set()

    for encounter in final_round.get("encounters", []):
        for utterance in encounter.get("utterances", []):
            final_utterances += 1
            text = str(utterance.get("text", ""))
            has_current, has_stale = classify(text)
            if has_current:
                current_utterances += 1
            if has_stale:
                stale_utterances += 1
            if has_current or has_stale:
                value_bearing_utterances += 1
            speaker_id = name_to_id.get(str(utterance.get("speaker", "")))
            if speaker_id and (has_current or has_stale):
                agents_said_value.add(speaker_id)
            if speaker_id and has_current:
                agents_said_current.add(speaker_id)

    interviews = load_json(run_dir / "interview_currency.json")
    interview_rows = interviews.get("results", interviews)
    if not isinstance(interview_rows, dict):
        raise ValueError(f"unexpected interview schema in {run_dir}")

    def held_counts(agent_ids: set[str]) -> dict[str, int]:
        counts = {"current": 0, "stale": 0, "unknown": 0}
        for agent_id in agent_ids:
            row = interview_rows.get(agent_id, {})
            verdict = str(row.get("verdict", "unknown"))
            counts[verdict if verdict in counts else "unknown"] += 1
        return counts

    all_ids = set(name_to_id.values())
    said_current_held = held_counts(agents_said_current)
    not_said_current_held = held_counts(all_ids - agents_said_current)
    said_value_held = held_counts(agents_said_value)
    current_share = (
        current_utterances / value_bearing_utterances
        if value_bearing_utterances
        else None
    )
    return {
        "condition": condition,
        "run": run_dir.name,
        "schedule_seed": int(summary["schedule_seed"]),
        "final_round": int(final_round["round"]),
        "final_utterances": final_utterances,
        "current_utterances": current_utterances,
        "stale_utterances": stale_utterances,
        "value_bearing_utterances": value_bearing_utterances,
        "said_current_share": current_share,
        "agents_said_current": len(agents_said_current),
        "agents_said_value": len(agents_said_value),
        "held_among_agents_said_current": said_current_held,
        "held_among_agents_not_said_current": not_said_current_held,
        "held_among_agents_said_value": said_value_held,
    }


def pooled_alignment(rows: list[dict[str, Any]], field: str) -> dict[str, Any]:
    counts = {"current": 0, "stale": 0, "unknown": 0}
    agents = 0
    count_field = field.replace("held_among_", "")
    for row in rows:
        agents += int(row[count_field])
        for verdict in counts:
            counts[verdict] += int(row[field][verdict])
    return {
        "agents": agents,
        "counts": counts,
        "current_rate": counts["current"] / agents if agents else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("sim/runs/m4_rebroadcast"),
        help="directory containing baseline/ and source/ experiment folders",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("sim/runs/m4_rebroadcast/said_held_alignment.json"),
    )
    args = parser.parse_args()

    rows: dict[str, list[dict[str, Any]]] = {}
    for condition in ("baseline", "source"):
        run_root = args.root / condition / "gpt-5.4-mini" / "ga"
        rows[condition] = [
            analyze_run(run_dir, condition)
            for run_dir in sorted(run_root.glob("run_*"))
            if run_dir.is_dir()
        ]
        if not rows[condition]:
            raise ValueError(f"no runs in {run_root}")

    by_seed = {
        condition: {row["schedule_seed"]: row for row in condition_rows}
        for condition, condition_rows in rows.items()
    }
    paired_seeds = sorted(set(by_seed["baseline"]) & set(by_seed["source"]))
    paired_differences = [
        by_seed["source"][seed]["said_current_share"]
        - by_seed["baseline"][seed]["said_current_share"]
        for seed in paired_seeds
    ]

    conditions: dict[str, Any] = {}
    for condition, condition_rows in rows.items():
        shares = [row["said_current_share"] for row in condition_rows]
        pooled_current = sum(row["current_utterances"] for row in condition_rows)
        pooled_value = sum(row["value_bearing_utterances"] for row in condition_rows)
        conditions[condition] = {
            "n_seeds": len(condition_rows),
            "pooled_current_utterances": pooled_current,
            "pooled_value_bearing_utterances": pooled_value,
            "pooled_said_current_share": pooled_current / pooled_value,
            "seed_level_said_current_share_ci95": mean_ci95(shares),
            "per_seed_said_current_share": {
                str(row["schedule_seed"]): row["said_current_share"]
                for row in condition_rows
            },
            "said_current_agent_alignment": pooled_alignment(
                condition_rows, "held_among_agents_said_current"
            ),
            "said_value_agent_alignment": pooled_alignment(
                condition_rows, "held_among_agents_said_value"
            ),
        }

    output = {
        "design": (
            "SAID uses final-round value-bearing utterances; seed-level inference treats "
            "one schedule seed as the independent unit. Agent-level alignment is descriptive."
        ),
        "conditions": conditions,
        "paired_source_minus_baseline": {
            "seeds": paired_seeds,
            "per_seed_difference": paired_differences,
            "mean_difference_ci95": mean_ci95(paired_differences),
        },
        "per_run": rows,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
