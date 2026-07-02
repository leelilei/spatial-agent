"""Build a blinded, balanced human-audit packet from repeated CityIntent traces."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[2]
DEFAULT_SOURCE = (
    REPO_ROOT
    / "6-city"
    / "results"
    / "cityintent_v03"
    / "external_frameworks_4x4x3_gpt54mini_2026-07-01"
)
DEFAULT_OUTPUT = (
    REPO_ROOT / "6-city" / "annotation" / "cityintent_v03_blind_pilot_2026-07-01"
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def file_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def load_scenarios() -> dict[str, dict[str, Any]]:
    return {
        path.stem: load_json(path)
        for path in sorted((ROOT / "scenarios").glob("*.json"))
    }


def collect_repeated_traces(source_dir: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for trace_path in sorted(source_dir.glob("repeat_*/traces/traces.json")):
        repeat_id = int(trace_path.parents[1].name.split("_", 1)[1])
        traces = load_json(trace_path)
        if not isinstance(traces, list):
            raise ValueError(f"trace archive must be a list: {trace_path}")
        for trace in traces:
            rows.append(
                {
                    "repeat_id": repeat_id,
                    "source_path": str(trace_path),
                    "trace": trace,
                }
            )
    if not rows:
        raise ValueError(f"no repeated traces found under {source_dir}")
    return rows


def balanced_sample(
    rows: list[dict[str, Any]], sample_per_cell: int, seed: int
) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        trace = row["trace"]
        groups[(trace["scenario_id"], trace["agent_type"])].append(row)
    rng = random.Random(seed)
    selected: list[dict[str, Any]] = []
    for key in sorted(groups):
        candidates = sorted(groups[key], key=lambda row: row["repeat_id"])
        if sample_per_cell > len(candidates):
            raise ValueError(
                f"requested {sample_per_cell} samples for {key}, only {len(candidates)} available"
            )
        selected.extend(rng.sample(candidates, sample_per_cell))
    rng.shuffle(selected)
    return selected


def parse_time(value: str) -> int:
    hour, minute = value.split(":", 1)
    return int(hour) * 60 + int(minute)


def compact_action(
    step: dict[str, Any], traversals: list[dict[str, Any]]
) -> dict[str, Any]:
    action = step.get("action", {})
    start = parse_time(step["start_time"])
    end = parse_time(step["end_time"])
    executed = [
        traversal
        for traversal in traversals
        if start < int(traversal["arrive_time"]) <= end
    ]
    return {
        "step": step.get("step"),
        "start_time": step.get("start_time"),
        "start_location": step.get("start_location"),
        "action": {
            key: action.get(key)
            for key in (
                "kind",
                "target",
                "path",
                "minutes",
                "to",
                "content",
                "item",
                "service",
                "reason",
            )
        },
        "end_time": step.get("end_time"),
        "end_location": step.get("end_location"),
        "budget_after": step.get("budget"),
        "route_interruptions": step.get("route_interruptions", []),
        "executed_traversals": executed,
    }


def accepted_dwell_minutes(trace: dict[str, Any]) -> dict[str, int]:
    dwell: dict[str, int] = defaultdict(int)
    prior_violation_count = 0
    for step in trace.get("trace", []):
        violation_count = len(step.get("violations", []))
        action = step.get("action", {})
        if (
            action.get("kind") == "dwell"
            and violation_count == prior_violation_count
        ):
            dwell[step["start_location"]] += max(1, int(action.get("minutes", 0)))
        prior_violation_count = violation_count
    return dict(dwell)


def blind_item(
    audit_id: str,
    row: dict[str, Any],
    scenario: dict[str, Any],
) -> dict[str, Any]:
    trace = row["trace"]
    primary = next(
        agent
        for agent in scenario["agents"]
        if agent["agent_id"] == scenario["primary_agent"]
    )
    return {
        "audit_id": audit_id,
        "scenario": {
            "id": scenario["scenario_id"],
            "title": scenario["title"],
            "family": scenario["family"],
            "episode": scenario["episode"],
            "public_context": scenario.get("public_context", ""),
            "events": scenario.get("events", []),
            "success_conditions": scenario["success_conditions"],
        },
        "primary_agent": {
            "id": primary["agent_id"],
            "persona": primary["persona"],
            "private_intention": primary["private_intention"],
            "start_location": primary["start_location"],
            "budget": primary["budget"],
            "memory_seeds": primary.get("memory_seeds", []),
        },
        "other_agents": [
            {
                "id": agent["agent_id"],
                "persona": agent["persona"],
                "private_intention": agent["private_intention"],
                "start_location": agent["start_location"],
            }
            for agent in scenario.get("agents", [])
            if agent["agent_id"] != scenario["primary_agent"]
        ],
        "action_trace": [
            compact_action(step, trace.get("traversals", []))
            for step in trace["trace"]
        ],
        "observable_outcomes": {
            "final_time": trace["final_state"]["time"],
            "final_location": trace["final_state"]["location"],
            "final_budget": trace["final_state"]["budget"],
            "entries": trace.get("entries", []),
            "services": trace.get("services", []),
            "purchases": trace.get("purchases", []),
            "messages": trace.get("messages", []),
            "interactions": trace.get("interactions", []),
            "route_interruptions": trace.get("route_interruptions", []),
            "accepted_dwell_minutes_by_location": accepted_dwell_minutes(trace),
        },
    }


def trace_role_score(
    trace: dict[str, Any], scenario: dict[str, Any], role: str
) -> float | None:
    metric_key = {
        "outcome": "task_completion",
        "constraint": "constraint_satisfaction",
        "process": "process_success",
    }[role]
    if metric_key in trace.get("metrics", {}):
        return trace["metrics"][metric_key]
    role_by_id = {
        condition["id"]: condition.get("role", "outcome")
        for condition in scenario["success_conditions"]
    }
    selected = [
        condition
        for condition in trace.get("conditions", [])
        if role_by_id.get(condition.get("id"), "outcome") == role
    ]
    total_weight = sum(float(condition.get("weight", 0)) for condition in selected)
    if total_weight <= 0:
        return None
    return round(
        sum(
            float(condition.get("score", 0)) * float(condition.get("weight", 0))
            for condition in selected
        )
        / total_weight,
        3,
    )


def sealed_row(
    audit_id: str, row: dict[str, Any], scenario: dict[str, Any]
) -> dict[str, Any]:
    trace = row["trace"]
    return {
        "audit_id": audit_id,
        "repeat_id": row["repeat_id"],
        "scenario_id": trace["scenario_id"],
        "agent_type": trace["agent_type"],
        "goal_completion": trace["metrics"]["goal_completion"],
        "task_completion": trace_role_score(trace, scenario, "outcome"),
        "constraint_satisfaction": trace_role_score(trace, scenario, "constraint"),
        "process_success": trace_role_score(trace, scenario, "process"),
        "trace_feasibility": trace["metrics"]["trace_feasibility"],
        "replanning_success": trace["metrics"].get("replanning_success"),
        "verified_replan_count": len(trace.get("replans", [])),
        "violation_count": len(trace["final_state"].get("violations", [])),
        "failure_taxonomy": json.dumps(
            trace.get("failure_taxonomy", {}), sort_keys=True
        ),
        "source_path": row["source_path"],
    }


ANNOTATION_FIELDS = [
    "audit_id",
    "annotator_id",
    "completion_label",
    "feasibility_label",
    "replan_label",
    "evidence_sufficient",
    "first_invalid_step",
    "confidence",
    "notes",
]


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def safe_cell(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def write_packet_markdown(path: Path, items: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Blinded Human Audit Packet\n\n")
        f.write("Use `RUBRIC.md` and `world_reference.json`. Do not access `sealed/` while annotating.\n\n")
        for item in items:
            scenario = item["scenario"]
            agent = item["primary_agent"]
            f.write(f"## {item['audit_id']}\n\n")
            f.write(f"Scenario: {scenario['title']}  \n")
            f.write(f"Episode: {scenario['episode']['start_time']} to {scenario['episode']['end_time']}  \n")
            f.write(f"Persona: {agent['persona']}  \n")
            f.write(f"Private intention: {agent['private_intention']}  \n")
            f.write(f"Start: {agent['start_location']}; budget: {agent['budget']}\n\n")
            if item.get("other_agents"):
                f.write("Other agents:\n\n")
                for other in item["other_agents"]:
                    f.write(
                        f"- `{other['id']}`: {other['persona']} Start: "
                        f"`{other['start_location']}`. Intention: {other['private_intention']}\n"
                    )
                f.write("\n")
            f.write("Success conditions:\n\n")
            for condition in scenario["success_conditions"]:
                f.write(f"- `{condition['id']}`: `{json.dumps(condition, ensure_ascii=False)}`\n")
            f.write("\n| step | time | from | action | target/detail | proposed path | executed route | end | location | budget | interruption |\n")
            f.write("|---:|---|---|---|---|---|---|---|---|---:|---|\n")
            for step in item["action_trace"]:
                action = step["action"]
                details = []
                for key in ("target", "to", "item", "service", "content", "reason"):
                    value = action.get(key)
                    if value:
                        details.append(f"{key}={value}")
                detail = "; ".join(details)
                interruptions = ", ".join(
                    event.get("event_id", "")
                    for event in step.get("route_interruptions", [])
                )
                route = ">".join(
                    [step["executed_traversals"][0]["from"]]
                    + [edge["to"] for edge in step["executed_traversals"]]
                ) if step["executed_traversals"] else ""
                f.write(
                    f"| {step['step']} | {step['start_time']} | {safe_cell(step['start_location'])} | "
                    f"{safe_cell(action.get('kind'))} | {safe_cell(detail)} | "
                    f"{safe_cell('>'.join(action.get('path') or []))} | {safe_cell(route)} | {step['end_time']} | "
                    f"{safe_cell(step['end_location'])} | {step['budget_after']} | {safe_cell(interruptions)} |\n"
                )
            outcomes = item["observable_outcomes"]
            f.write(
                f"\nFinal observable state: time {outcomes['final_time']}, location "
                f"{outcomes['final_location']}, budget {outcomes['final_budget']}.\n\n"
            )
            f.write("Accepted environment outcomes:\n\n")
            for key in (
                "entries",
                "services",
                "purchases",
                "accepted_dwell_minutes_by_location",
                "messages",
                "interactions",
                "route_interruptions",
            ):
                f.write(
                    f"- `{key}`: `{json.dumps(outcomes.get(key), ensure_ascii=False)}`\n"
                )
            f.write("\n")
    cleaned = "\n".join(line.rstrip() for line in path.read_text(encoding="utf-8").splitlines())
    path.write_text(cleaned.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_rubric(path: Path) -> None:
    path.write_text(
        """# CityIntent Human Audit Rubric

Annotate independently. Do not inspect `sealed/`, source traces, framework
names, benchmark scores, or another annotator's file before submission.

## Labels

`completion_label`

- `complete`: every `outcome` condition is completed with observable evidence.
  Constraint or process points cannot substitute for a missing intended outcome.
- `partial`: meaningful progress or some conditions are completed, but at least
  one important part is missing.
- `not_complete`: little or none of the intended outcome is completed.
- `uncertain`: the packet lacks enough information to decide.

`feasibility_label`

- `feasible`: every executed transition is physically, temporally, financially,
  and procedurally valid in the supplied city world.
- `infeasible`: at least one executed transition is invalid. Record the first
  invalid step when possible.
- `uncertain`: validity cannot be determined from the packet.

Goal incompletion alone is not infeasibility. A legal early `finish` can be
feasible and not complete.

## CityIntent execution rules

- A `move` with an empty proposed path is resolved by the environment's
  shortest available path. Judge the `executed route`, not path nullness.
- A successful move arrives outside the destination and clears indoor state.
  A following `enter` at the same graph location is required, not duplicate.
- A proposed explicit path can be rejected. Judge each step separately: a later
  valid move may recover, but the rejected step still makes the trace infeasible.
- `enter` must occur at an open current location before indoor activity.
- At a location with `typical_cost > 0`, `buy` or `use_service` deducts that
  cost. `dwell` there requires prior purchase/service evidence.
- Passing through or arriving outside a location is not entry or task
  completion.
- Repeating a completed purchase/service, using a closed place, exceeding the
  budget or episode end, or attempting a visible blocked edge is infeasible.
- A disruption that appears after movement starts may interrupt the route
  without making the pre-disruption action an agent error.
- Completion must be supported by `Accepted environment outcomes`, not by a
  claimed action that the environment rejected.
- A social meeting requires an accepted `interaction` record naming the other
  agent, location, and time. Presence at the venue alone is insufficient.

`replan_label`

- `successful`: after a visible disruption, the trace adopts a feasible changed
  route or strategy that avoids the disrupted option.
- `failed`: a relevant disruption occurs but the trace does not recover.
- `not_applicable`: no disruption requires replanning in this item.
- `uncertain`: the packet does not support a decision.

`evidence_sufficient`: `yes`, `no`, or `uncertain` for whether the observable
trace is sufficient to support your labels.

`confidence`: integer 1 (low) through 5 (high).

## Procedure

1. Read the private intention, events, and success conditions.
2. Use `world_reference.json` to check paths, hours, and costs.
3. Read every action in order. Do not infer an unrecorded purchase, entry,
   service, meeting, or return.
4. Label completion and feasibility separately.
5. For infeasible traces, record the first invalid action step and explain the
   issue briefly in `notes`.
""",
        encoding="utf-8",
        newline="\n",
    )


def write_readme(path: Path, output_dir: Path, item_count: int) -> None:
    try:
        output_ref = output_dir.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        output_ref = output_dir.as_posix()
    path.write_text(
        f"""# CityIntent Blinded Human Audit

This package contains {item_count} anonymized traces sampled evenly across the
available scenario-adapter cells.

## Handoff

1. Give each annotator `RUBRIC.md`, the complete `blinded/` directory, and only
   their own CSV from `annotations/`.
2. Do not share `sealed/`, source result paths, framework names, scores, or the
   other annotator's labels until both files are locked.
3. Use two independent annotators. Resolve disagreements only after computing
   pre-adjudication agreement.
4. After both CSV files are complete, run:

```bash
python 6-city/benchmarks/cityintent_v0/tools/score_human_audit.py ^
  --annotations-a {output_ref}/annotations/annotator_a.csv ^
  --annotations-b {output_ref}/annotations/annotator_b.csv ^
  --key {output_ref}/sealed/audit_key.csv ^
  --output-dir {output_ref}/agreement
```

The annotation CSVs are intentionally blank in the repository. Sharing labels
or the sealed key before both independent submissions would invalidate the audit.
""",
        encoding="utf-8",
        newline="\n",
    )


def build_packet(
    source_dir: Path,
    output_dir: Path,
    sample_per_cell: int,
    seed: int,
    overwrite: bool = False,
) -> dict[str, Any]:
    if (output_dir / "audit_manifest.json").exists() and not overwrite:
        raise FileExistsError(
            f"refusing to overwrite audit archive {output_dir}; pass --overwrite"
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = collect_repeated_traces(source_dir)
    selected = balanced_sample(rows, sample_per_cell, seed)
    scenarios = load_scenarios()
    items = []
    sealed = []
    for index, row in enumerate(selected, start=1):
        audit_id = f"H{index:03d}"
        scenario = scenarios[row["trace"]["scenario_id"]]
        items.append(blind_item(audit_id, row, scenario))
        sealed.append(sealed_row(audit_id, row, scenario))

    packet_jsonl = output_dir / "blinded" / "audit_items.jsonl"
    packet_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with packet_jsonl.open("w", encoding="utf-8", newline="\n") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    write_packet_markdown(output_dir / "blinded" / "audit_packet.md", items)
    write_json(
        output_dir / "blinded" / "world_reference.json",
        load_json(ROOT / "worlds" / "micro_city.json"),
    )
    for annotator in ("annotator_a", "annotator_b"):
        rows_for_annotator = [
            {
                "audit_id": item["audit_id"],
                "annotator_id": annotator,
                **{field: "" for field in ANNOTATION_FIELDS[2:]},
            }
            for item in items
        ]
        write_csv(
            output_dir / "annotations" / f"{annotator}.csv",
            rows_for_annotator,
            ANNOTATION_FIELDS,
        )
    sealed_fields = list(sealed[0]) if sealed else []
    write_csv(output_dir / "sealed" / "audit_key.csv", sealed, sealed_fields)
    write_rubric(output_dir / "RUBRIC.md")
    write_readme(output_dir / "README.md", output_dir, len(items))

    files = [
        output_dir / "blinded" / "audit_items.jsonl",
        output_dir / "blinded" / "audit_packet.md",
        output_dir / "blinded" / "world_reference.json",
        output_dir / "annotations" / "annotator_a.csv",
        output_dir / "annotations" / "annotator_b.csv",
        output_dir / "sealed" / "audit_key.csv",
        output_dir / "RUBRIC.md",
        output_dir / "README.md",
    ]
    manifest = {
        "schema_version": "cityintent_human_audit_v2",
        "source_dir": str(source_dir),
        "seed": seed,
        "sample_per_scenario_agent_cell": sample_per_cell,
        "available_trace_count": len(rows),
        "audit_item_count": len(items),
        "scenario_count": len({item["scenario"]["id"] for item in items}),
        "cell_count": len(
            {(row["scenario_id"], row["agent_type"]) for row in sealed}
        ),
        "blinding": {
            "hidden": [
                "agent_type",
                "repeat_id",
                "model_info",
                "metrics",
                "violations",
                "failure_taxonomy",
                "verified_replans",
            ],
            "sealed_key": "sealed/audit_key.csv",
        },
        "normalized_text_sha256": {
            str(path.relative_to(output_dir)).replace("\\", "/"): file_sha256(path)
            for path in files
        },
    }
    write_json(output_dir / "audit_manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--sample-per-cell", type=int, default=1)
    parser.add_argument("--seed", type=int, default=20260701)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    if args.sample_per_cell < 1:
        raise SystemExit("--sample-per-cell must be >= 1")
    manifest = build_packet(
        args.source_dir,
        args.output_dir,
        args.sample_per_cell,
        args.seed,
        overwrite=args.overwrite,
    )
    print(
        f"Wrote {manifest['audit_item_count']} blinded audit items to {args.output_dir}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
