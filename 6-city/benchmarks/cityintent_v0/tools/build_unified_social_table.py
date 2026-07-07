"""Build the unified six-policy social-outcome comparison table."""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[2]
RESULTS_ROOT = REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1"
DEFAULT_EXTERNAL_DIR = RESULTS_ROOT / "external_frameworks_4x6socialx1_gpt54mini_2026-07-06"
DEFAULT_PAPER_BACKED_DIR = (
    RESULTS_ROOT / "paper_backed_baselines_2x6socialx3_gpt54mini_2026-07-07"
)
DEFAULT_OUTPUT_DIR = RESULTS_ROOT / "unified_six_policy_social_table_2026-07-08"


AGENT_META = {
    "gatsim_official_planner": {
        "display_name": "GATSim adapted planner",
        "family": "adapted_official_decision_layer",
        "lineage": "GATSim",
    },
    "sotopia_official_llm_agent": {
        "display_name": "SOTOPIA-style LLMAgent adapter",
        "family": "adapted_official_decision_layer",
        "lineage": "SOTOPIA",
    },
    "generative_agents_official_planner": {
        "display_name": "Generative Agents adapted planner",
        "family": "adapted_official_decision_layer",
        "lineage": "Generative Agents",
    },
    "agentsociety_official_plan_blocks": {
        "display_name": "AgentSociety plan-block adapter",
        "family": "adapted_official_decision_layer",
        "lineage": "AgentSociety",
    },
    "api_llm_react_tool_policy": {
        "display_name": "ReAct-style tool-use policy",
        "family": "paper_backed_execution_baseline",
        "lineage": "ReAct / tau-bench / AppWorld-style execution",
    },
    "api_llm_plan_and_execute": {
        "display_name": "Plan-and-Execute policy",
        "family": "paper_backed_execution_baseline",
        "lineage": "Plan-and-Execute / AppWorld-style execution",
    },
}


AGENT_ORDER = [
    "api_llm_react_tool_policy",
    "api_llm_plan_and_execute",
    "gatsim_official_planner",
    "agentsociety_official_plan_blocks",
    "generative_agents_official_planner",
    "sotopia_official_llm_agent",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def pct(value: Any) -> str:
    return f"{float(value):.3f}"


def as_int(value: Any) -> int:
    return int(float(value))


def enrich_agent_row(row: dict[str, str], source_dir: Path) -> dict[str, Any]:
    agent = row["agent_type"]
    meta = AGENT_META.get(agent, {})
    required = as_int(row["required_copresence_outcomes"])
    accepted = as_int(row["accepted_copresence_outcomes"])
    return {
        "agent_type": agent,
        "display_name": meta.get("display_name", agent),
        "agent_family": meta.get("family", "unknown"),
        "source_lineage": meta.get("lineage", ""),
        "source_archive": source_dir.relative_to(REPO_ROOT).as_posix(),
        "n_traces": as_int(row["n_traces"]),
        "accepted_copresence_outcomes": accepted,
        "required_copresence_outcomes": required,
        "accepted_over_required": f"{accepted}/{required}",
        "copresence_outcome_rate": float(row["copresence_outcome_rate"]),
        "full_social_trace_rate": float(row["full_social_trace_rate"]),
        "social_pass_k_rate": float(row["social_pass_k_rate"]),
        "full_task_rate": float(row["full_task_rate"]),
        "fully_feasible_rate": float(row["fully_feasible_rate"]),
        "joint_success_rate": float(row["joint_success_rate"]),
        "legal_but_ineffective_rate": float(row["legal_but_ineffective_rate"]),
        "plausible_but_unverified_rate": float(row["plausible_but_unverified_rate"]),
        "message_without_social_success_rate": float(row["message_without_social_success_rate"]),
        "attempt_without_social_success_rate": float(row["attempt_without_social_success_rate"]),
        "target_entry_without_social_success_rate": float(row["target_entry_without_social_success_rate"]),
        "mean_task_completion": float(row["mean_task_completion"]),
        "mean_trace_feasibility": float(row["mean_trace_feasibility"]),
        "mean_face_plausibility": float(row["mean_face_plausibility"]),
        "mean_llm_calls": float(row["mean_llm_calls"]),
        "mean_llm_total_tokens": float(row["mean_llm_total_tokens"]),
    }


def enrich_scenario_row(row: dict[str, str], source_dir: Path) -> dict[str, Any]:
    agent = row["agent_type"]
    meta = AGENT_META.get(agent, {})
    accepted = as_int(row["accepted_copresence_outcomes"])
    required = as_int(row["required_copresence_outcomes"])
    return {
        "scenario_id": row["scenario_id"],
        "agent_type": agent,
        "display_name": meta.get("display_name", agent),
        "agent_family": meta.get("family", "unknown"),
        "source_archive": source_dir.relative_to(REPO_ROOT).as_posix(),
        "n_repeats": as_int(row["n_repeats"]),
        "accepted_copresence_outcomes": accepted,
        "required_copresence_outcomes": required,
        "accepted_over_required": f"{accepted}/{required}",
        "copresence_outcome_rate": float(row["copresence_outcome_rate"]),
        "social_pass_k": float(row["social_pass_k"]),
        "mean_task_completion": float(row["mean_task_completion"]),
        "mean_trace_feasibility": float(row["mean_trace_feasibility"]),
    }


def enrich_failure_row(row: dict[str, str], source_dir: Path) -> dict[str, Any]:
    agent = row["agent_type"]
    meta = AGENT_META.get(agent, {})
    return {
        "agent_type": agent,
        "display_name": meta.get("display_name", agent),
        "agent_family": meta.get("family", "unknown"),
        "source_archive": source_dir.relative_to(REPO_ROOT).as_posix(),
        "failure": row["failure"],
        "count": as_int(row["count"]),
        "events_per_trace": float(row["events_per_trace"]),
    }


def agent_sort_key(row: dict[str, Any]) -> tuple[int, str]:
    try:
        return (AGENT_ORDER.index(row["agent_type"]), row["agent_type"])
    except ValueError:
        return (len(AGENT_ORDER), row["agent_type"])


def load_sources(source_dirs: list[Path]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    agent_rows: list[dict[str, Any]] = []
    scenario_rows: list[dict[str, Any]] = []
    failure_rows: list[dict[str, Any]] = []
    for source_dir in source_dirs:
        agent_path = source_dir / "social_outcome_agent_summary.csv"
        scenario_path = source_dir / "social_outcome_scenario_summary.csv"
        failure_path = source_dir / "failure_taxonomy_summary.csv"
        if not agent_path.exists() or not scenario_path.exists():
            raise FileNotFoundError(f"missing social outcome summaries in {source_dir}")
        agent_rows.extend(enrich_agent_row(row, source_dir) for row in read_csv(agent_path))
        scenario_rows.extend(enrich_scenario_row(row, source_dir) for row in read_csv(scenario_path))
        if failure_path.exists():
            failure_rows.extend(enrich_failure_row(row, source_dir) for row in read_csv(failure_path))
    agent_rows.sort(key=agent_sort_key)
    scenario_rows.sort(key=lambda row: (row["scenario_id"], agent_sort_key(row)))
    failure_rows.sort(key=lambda row: (agent_sort_key(row), row["failure"]))
    return agent_rows, scenario_rows, failure_rows


def write_markdown(
    path: Path,
    agent_rows: list[dict[str, Any]],
    scenario_rows: list[dict[str, Any]],
    failure_rows: list[dict[str, Any]],
    source_dirs: list[Path],
) -> None:
    by_agent = {row["agent_type"]: row for row in agent_rows}
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Unified Six-Policy Social Table\n\n")
        f.write("Date: 2026-07-08\n\n")
        f.write("## Scope\n\n")
        f.write(
            "This table combines the four adapted official decision-layer social "
            "matrix with the two paper-backed execution baselines. All rows use "
            "the same six oracle-winnable `social_outcome` scenarios, three "
            "repeats per scenario-policy cell, the same typed CityIntent "
            "executor, and deterministic environment-owned co-presence evidence.\n\n"
        )
        f.write("Source archives:\n\n")
        for source_dir in source_dirs:
            f.write(f"- `{source_dir.relative_to(REPO_ROOT).as_posix()}`\n")
        f.write("\n## Main Table\n\n")
        f.write(
            "| Policy | Family | Accepted co-presence | Outcome rate | Full social | "
            "Social pass^3 | Full task | Fully feasible | Joint success | "
            "Legal but ineffective | Plausible but unverified | Calls | Tokens |\n"
        )
        f.write("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in agent_rows:
            f.write(
                f"| {row['display_name']} | {row['agent_family']} | "
                f"{row['accepted_over_required']} | {pct(row['copresence_outcome_rate'])} | "
                f"{pct(row['full_social_trace_rate'])} | {pct(row['social_pass_k_rate'])} | "
                f"{pct(row['full_task_rate'])} | {pct(row['fully_feasible_rate'])} | "
                f"{pct(row['joint_success_rate'])} | "
                f"{pct(row['legal_but_ineffective_rate'])} | "
                f"{pct(row['plausible_but_unverified_rate'])} | "
                f"{pct(row['mean_llm_calls'])} | {round(row['mean_llm_total_tokens'])} |\n"
            )
        f.write("\n`Social pass^3` is the fraction of scenario-policy cells where all three repeats accept all required co-presence outcomes.\n\n")
        f.write("## Evidence-Gap Diagnostics\n\n")
        f.write(
            "| Policy | Mean task | Mean feasibility | Mean face plausibility | "
            "Message without meeting | Interact attempt without success | "
            "Target entry without meeting |\n"
        )
        f.write("|---|---:|---:|---:|---:|---:|---:|\n")
        for row in agent_rows:
            f.write(
                f"| {row['display_name']} | {pct(row['mean_task_completion'])} | "
                f"{pct(row['mean_trace_feasibility'])} | {pct(row['mean_face_plausibility'])} | "
                f"{pct(row['message_without_social_success_rate'])} | "
                f"{pct(row['attempt_without_social_success_rate'])} | "
                f"{pct(row['target_entry_without_social_success_rate'])} |\n"
            )
        f.write("\n## Scenario Outcome Heatmap\n\n")
        agents = [row["agent_type"] for row in agent_rows]
        scenarios = sorted({row["scenario_id"] for row in scenario_rows})
        cell_lookup = {
            (row["scenario_id"], row["agent_type"]): row["accepted_over_required"]
            for row in scenario_rows
        }
        f.write("| Scenario | " + " | ".join(by_agent[agent]["display_name"] for agent in agents) + " |\n")
        f.write("|---|" + "|".join("---:" for _ in agents) + "|\n")
        for scenario in scenarios:
            values = [cell_lookup.get((scenario, agent), "") for agent in agents]
            f.write(f"| `{scenario}` | " + " | ".join(values) + " |\n")
        f.write("\n## Dominant Failure Counts\n\n")
        f.write("| Policy | Top recorded failures |\n")
        f.write("|---|---|\n")
        failures_by_agent: dict[str, list[dict[str, Any]]] = {}
        for row in failure_rows:
            failures_by_agent.setdefault(row["agent_type"], []).append(row)
        for agent in agents:
            failures = sorted(
                failures_by_agent.get(agent, []),
                key=lambda row: (-row["count"], row["failure"]),
            )[:3]
            text = ", ".join(f"{row['failure']}={row['count']}" for row in failures) or "none"
            f.write(f"| {by_agent[agent]['display_name']} | {text} |\n")
        f.write("\n## Main Reading\n\n")
        f.write(
            "The unified table strengthens the benchmark story. The six-scenario "
            "social family is not unwinnable: ReAct-style tool use completes "
            "21/21 required co-presence outcomes, Plan-and-Execute completes "
            "18/21, and GATSim completes 15/21. At the same time, the "
            "SOTOPIA-style LLMAgent adapter produces 0/21 accepted outcomes "
            "despite high feasibility and face plausibility. This is the core "
            "Plausible Plans, Impossible Traces pattern: plausible or legal "
            "behavior is not the same as verified urban agency.\n\n"
        )
        f.write(
            "The paper-backed execution baselines also add a useful ceiling. "
            "They show that the verifier can be satisfied by ordinary LLM-agent "
            "execution architectures, while exposing distinct costs and failure "
            "modes: ReAct is strongest but expensive and still shows terminal/"
            "paid-state issues; Plan-and-Execute is cheap and plausible but "
            "weakens on two-party simultaneous co-presence.\n"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-dir",
        type=Path,
        action="append",
        default=None,
        help="Experiment directory containing social_outcome_* summaries.",
    )
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    args = parser.parse_args()

    source_dirs = args.source_dir or [DEFAULT_EXTERNAL_DIR, DEFAULT_PAPER_BACKED_DIR]
    source_dirs = [path.resolve() for path in source_dirs]
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    agent_rows, scenario_rows, failure_rows = load_sources(source_dirs)
    write_csv(output_dir / "unified_social_agent_summary.csv", agent_rows)
    write_csv(output_dir / "unified_social_scenario_summary.csv", scenario_rows)
    write_csv(output_dir / "unified_social_failure_taxonomy.csv", failure_rows)
    write_markdown(
        output_dir / "unified_social_table.md",
        agent_rows,
        scenario_rows,
        failure_rows,
        source_dirs,
    )
    manifest = {
        "schema_version": "cityintent_unified_social_table_v1",
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source_dirs": [path.relative_to(REPO_ROOT).as_posix() for path in source_dirs],
        "output_dir": output_dir.relative_to(REPO_ROOT).as_posix(),
        "agent_count": len(agent_rows),
        "scenario_agent_rows": len(scenario_rows),
        "failure_rows": len(failure_rows),
        "agents": [row["agent_type"] for row in agent_rows],
    }
    (output_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote unified social table for {len(agent_rows)} policies to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
