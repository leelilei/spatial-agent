"""Analyze environment-accepted social outcomes in CityIntent trace archives."""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


DISPLAY_NAMES = {
    "agentsociety_official_plan_blocks": "AgentSociety",
    "gatsim_official_planner": "GATSim",
    "generative_agents_official_planner": "Generative Agents",
    "sotopia_official_llm_agent": "SOTOPIA",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def load_scenarios(scenario_dir: Path) -> dict[str, dict[str, Any]]:
    return {
        scenario["scenario_id"]: scenario
        for path in sorted(scenario_dir.glob("*.json"))
        for scenario in [load_json(path)]
    }


def classify_trace(
    item: dict[str, Any],
    scenario: dict[str, Any],
    repeat_id: int,
) -> dict[str, Any]:
    conditions = [
        condition
        for condition in scenario.get("success_conditions", [])
        if condition.get("type") == "co_presence" and condition.get("role") == "outcome"
    ]
    scores = {
        condition["id"]: float(condition.get("score", 0.0))
        for condition in item.get("conditions", [])
    }
    accepted = sum(scores.get(condition["id"], 0.0) >= 0.999 for condition in conditions)
    required = len(conditions)
    counterpart_ids = {
        agent_id
        for condition in conditions
        for agent_id in condition.get("agents", [])
        if agent_id != scenario.get("primary_agent")
    }
    target_locations = {
        location
        for condition in conditions
        for location in (
            condition.get("location_any_of")
            or ([condition["location"]] if condition.get("location") else [])
        )
    }
    messages = [
        message
        for message in item.get("messages", [])
        if message.get("to") in counterpart_ids
    ]
    interact_attempts = [
        step
        for step in item.get("trace", [])
        if step.get("action", {}).get("kind") == "interact"
        and step.get("action", {}).get("to") in counterpart_ids
    ]
    target_entries = [
        entry
        for entry in item.get("entries", [])
        if entry.get("location") in target_locations and entry.get("kind") != "start"
    ]
    full_social = required > 0 and accepted == required
    metrics = item.get("metrics", {})
    judgment = item.get("plausibility_judgment", {})
    face = float(judgment.get("face_plausibility", 0.0))
    feasibility = float(metrics.get("trace_feasibility", 0.0))
    task = float(metrics.get("task_completion", 0.0))
    return {
        "repeat_id": repeat_id,
        "scenario_id": item["scenario_id"],
        "agent_type": item["agent_type"],
        "required_copresence_outcomes": required,
        "accepted_copresence_outcomes": accepted,
        "copresence_outcome_rate": accepted / required if required else 0.0,
        "full_social_success": float(full_social),
        "accepted_interaction_events": len(item.get("interactions", [])),
        "message_count_to_counterparts": len(messages),
        "interact_attempt_count": len(interact_attempts),
        "target_entry_count": len(target_entries),
        "message_without_social_success": float(bool(messages) and not full_social),
        "attempt_without_social_success": float(bool(interact_attempts) and not full_social),
        "target_entry_without_social_success": float(bool(target_entries) and not full_social),
        "legal_but_ineffective": float(feasibility >= 0.999 and not full_social),
        "plausible_but_unverified": float(face >= 0.70 and not full_social),
        "task_completion": task,
        "trace_feasibility": feasibility,
        "joint_success": float(task >= 0.999 and feasibility >= 0.999),
        "judge_face_plausibility": face,
        "judge_trace_believability": float(judgment.get("trace_believability", 0.0)),
        "llm_calls": float(item.get("model_info", {}).get("llm_telemetry_summary", {}).get("calls", 0)),
        "llm_total_tokens": float(
            item.get("model_info", {}).get("llm_telemetry_summary", {}).get("total_tokens", 0)
        ),
    }


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def summarize_agents(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row["agent_type"]].append(row)
    summary = []
    for agent_type, items in sorted(grouped.items()):
        required = sum(item["required_copresence_outcomes"] for item in items)
        accepted = sum(item["accepted_copresence_outcomes"] for item in items)
        cells: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for item in items:
            cells[item["scenario_id"]].append(item)
        pass_k = mean(
            [
                float(all(item["full_social_success"] >= 0.999 for item in cell_items))
                for cell_items in cells.values()
            ]
        )
        summary.append(
            {
                "agent_type": agent_type,
                "n_traces": len(items),
                "required_copresence_outcomes": required,
                "accepted_copresence_outcomes": accepted,
                "copresence_outcome_rate": accepted / required if required else 0.0,
                "full_social_trace_rate": mean([item["full_social_success"] for item in items]),
                "social_pass_k_rate": pass_k,
                "full_task_rate": mean([float(item["task_completion"] >= 0.999) for item in items]),
                "fully_feasible_rate": mean(
                    [float(item["trace_feasibility"] >= 0.999) for item in items]
                ),
                "joint_success_rate": mean([item["joint_success"] for item in items]),
                "legal_but_ineffective_rate": mean(
                    [item["legal_but_ineffective"] for item in items]
                ),
                "plausible_but_unverified_rate": mean(
                    [item["plausible_but_unverified"] for item in items]
                ),
                "message_without_social_success_rate": mean(
                    [item["message_without_social_success"] for item in items]
                ),
                "attempt_without_social_success_rate": mean(
                    [item["attempt_without_social_success"] for item in items]
                ),
                "target_entry_without_social_success_rate": mean(
                    [item["target_entry_without_social_success"] for item in items]
                ),
                "mean_task_completion": mean([item["task_completion"] for item in items]),
                "mean_trace_feasibility": mean([item["trace_feasibility"] for item in items]),
                "mean_face_plausibility": mean(
                    [item["judge_face_plausibility"] for item in items]
                ),
                "mean_llm_calls": mean([item["llm_calls"] for item in items]),
                "mean_llm_total_tokens": mean([item["llm_total_tokens"] for item in items]),
            }
        )
    return summary


def summarize_scenarios(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[(row["scenario_id"], row["agent_type"])].append(row)
    summary = []
    for (scenario_id, agent_type), items in sorted(grouped.items()):
        required = sum(item["required_copresence_outcomes"] for item in items)
        accepted = sum(item["accepted_copresence_outcomes"] for item in items)
        summary.append(
            {
                "scenario_id": scenario_id,
                "agent_type": agent_type,
                "n_repeats": len(items),
                "accepted_copresence_outcomes": accepted,
                "required_copresence_outcomes": required,
                "copresence_outcome_rate": accepted / required if required else 0.0,
                "social_pass_k": float(
                    all(item["full_social_success"] >= 0.999 for item in items)
                ),
                "mean_task_completion": mean([item["task_completion"] for item in items]),
                "mean_trace_feasibility": mean([item["trace_feasibility"] for item in items]),
            }
        )
    return summary


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, summary: list[dict[str, Any]], repeat_count: int) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Social-Outcome Family Analysis\n\n")
        f.write(f"Repeated runs per scenario-adapter cell: {repeat_count}.\n\n")
        f.write("| Adapter | Accepted outcomes | Outcome rate | Full social traces | Social pass^k | Full task | Fully feasible | Joint success | Legal but ineffective | Plausible but unverified |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in summary:
            f.write(
                f"| {DISPLAY_NAMES.get(row['agent_type'], row['agent_type'])} | "
                f"{row['accepted_copresence_outcomes']}/{row['required_copresence_outcomes']} | "
                f"{row['copresence_outcome_rate']:.3f} | {row['full_social_trace_rate']:.3f} | "
                f"{row['social_pass_k_rate']:.3f} | {row['full_task_rate']:.3f} | "
                f"{row['fully_feasible_rate']:.3f} | {row['joint_success_rate']:.3f} | "
                f"{row['legal_but_ineffective_rate']:.3f} | "
                f"{row['plausible_but_unverified_rate']:.3f} |\n"
            )
        f.write("\n## Evidence-Gap Diagnostics\n\n")
        f.write("| Adapter | Message without meeting | Interact attempt without success | Target entry without meeting | Mean task | Mean feasibility | Mean face plausibility |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|\n")
        for row in summary:
            f.write(
                f"| {DISPLAY_NAMES.get(row['agent_type'], row['agent_type'])} | "
                f"{row['message_without_social_success_rate']:.3f} | "
                f"{row['attempt_without_social_success_rate']:.3f} | "
                f"{row['target_entry_without_social_success_rate']:.3f} | "
                f"{row['mean_task_completion']:.3f} | {row['mean_trace_feasibility']:.3f} | "
                f"{row['mean_face_plausibility']:.3f} |\n"
            )
        f.write("\n`Social pass^k` is the fraction of scenario cells where every repeat accepts all required co-presence outcomes.\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-dir", type=Path, required=True)
    parser.add_argument("--scenario-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()

    scenarios = load_scenarios(args.scenario_dir)
    rows = []
    repeat_ids = []
    for repeat_dir in sorted(args.experiment_dir.glob("repeat_*")):
        judged_path = repeat_dir / "judged" / "judged_traces.json"
        if not judged_path.exists():
            continue
        repeat_id = int(repeat_dir.name.split("_")[-1])
        repeat_ids.append(repeat_id)
        for item in load_json(judged_path):
            scenario = scenarios[item["scenario_id"]]
            if str(scenario.get("family", "")).startswith("social_outcome"):
                rows.append(classify_trace(item, scenario, repeat_id))
    if not rows:
        raise SystemExit("no judged social_outcome traces found")

    output_dir = args.output_dir or args.experiment_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    agent_summary = summarize_agents(rows)
    scenario_summary = summarize_scenarios(rows)
    write_csv(output_dir / "social_outcome_traces.csv", rows)
    write_csv(output_dir / "social_outcome_agent_summary.csv", agent_summary)
    write_csv(output_dir / "social_outcome_scenario_summary.csv", scenario_summary)
    write_markdown(output_dir / "social_outcome_analysis.md", agent_summary, len(set(repeat_ids)))
    manifest = {
        "schema_version": "cityintent_social_outcome_analysis_v1",
        "experiment_dir": str(args.experiment_dir),
        "scenario_dir": str(args.scenario_dir),
        "trace_count": len(rows),
        "repeat_count": len(set(repeat_ids)),
        "agents": sorted({row["agent_type"] for row in rows}),
        "scenarios": sorted({row["scenario_id"] for row in rows}),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    (output_dir / "social_outcome_analysis_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Analyzed {len(rows)} social-outcome traces")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
