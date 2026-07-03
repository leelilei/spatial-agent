"""Analyze repeated CityIntent runs for reliability and face-trace dissociation."""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any


AGENT_LABELS = {
    "agentsociety_official_plan_blocks": "AgentSociety",
    "gatsim_official_planner": "GATSim",
    "generative_agents_official_planner": "Generative Agents",
    "sotopia_official_llm_agent": "SOTOPIA",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def number(row: dict[str, str], key: str) -> float | None:
    value = row.get(key, "").strip()
    return None if value == "" else float(value)


def mean(values: list[float]) -> float:
    return sum(values) / len(values)


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 2:
        return None
    x_mean = mean(xs)
    y_mean = mean(ys)
    numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, ys))
    x_var = sum((x - x_mean) ** 2 for x in xs)
    y_var = sum((y - y_mean) ** 2 for y in ys)
    if x_var <= 0 or y_var <= 0:
        return None
    return numerator / math.sqrt(x_var * y_var)


def average_ranks(values: list[float]) -> list[float]:
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    ranks = [0.0] * len(values)
    cursor = 0
    while cursor < len(ordered):
        end = cursor + 1
        while end < len(ordered) and ordered[end][1] == ordered[cursor][1]:
            end += 1
        rank = (cursor + 1 + end) / 2
        for index, _ in ordered[cursor:end]:
            ranks[index] = rank
        cursor = end
    return ranks


def spearman(xs: list[float], ys: list[float]) -> float | None:
    return pearson(average_ranks(xs), average_ranks(ys))


def wilson_interval(successes: int, total: int, z: float = 1.96) -> tuple[float, float]:
    if total <= 0:
        return (0.0, 0.0)
    p = successes / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    margin = z * math.sqrt(p * (1 - p) / total + z * z / (4 * total * total)) / denominator
    return (max(0.0, center - margin), min(1.0, center + margin))


def rate_fields(prefix: str, successes: int, total: int) -> dict[str, Any]:
    low, high = wilson_interval(successes, total)
    return {
        f"{prefix}_count": successes,
        f"{prefix}_rate": round(successes / total, 3) if total else None,
        f"{prefix}_ci95_low": round(low, 3),
        f"{prefix}_ci95_high": round(high, 3),
    }


def analyze_agents(
    rows: list[dict[str, str]], face_threshold: float
) -> list[dict[str, Any]]:
    output = []
    for agent in sorted({row["agent_type"] for row in rows}):
        selected = [row for row in rows if row["agent_type"] == agent]
        cells: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in selected:
            cells[row["scenario_id"]].append(row)
        plausible = [number(row, "judge_face_plausibility") >= face_threshold for row in selected]
        task_success = [number(row, "task_completion") >= 0.999 for row in selected]
        feasible = [number(row, "trace_feasibility") >= 0.999 for row in selected]
        plausible_task_failure = [p and not t for p, t in zip(plausible, task_success)]
        plausible_infeasible = [p and not f for p, f in zip(plausible, feasible)]
        pass_k_task = sum(
            all(number(row, "task_completion") >= 0.999 for row in cell_rows)
            for cell_rows in cells.values()
        )
        pass_k_feasible = sum(
            all(number(row, "trace_feasibility") >= 0.999 for row in cell_rows)
            for cell_rows in cells.values()
        )
        item: dict[str, Any] = {
            "agent_type": agent,
            "agent": AGENT_LABELS.get(agent, agent),
            "n": len(selected),
            "scenario_count": len(cells),
            "repeat_count": len({row["repeat_id"] for row in selected}),
        }
        for prefix, values in (
            ("plausible", plausible),
            ("full_task_success", task_success),
            ("fully_feasible", feasible),
            ("plausible_task_failure", plausible_task_failure),
            ("plausible_infeasible", plausible_infeasible),
        ):
            item.update(rate_fields(prefix, sum(values), len(values)))
        item.update(rate_fields("pass_k_task", pass_k_task, len(cells)))
        item.update(rate_fields("pass_k_feasible", pass_k_feasible, len(cells)))
        for metric in (
            "task_completion",
            "trace_feasibility",
            "judge_face_plausibility",
            "judge_trace_believability",
            "face_believability_gap",
            "llm_calls",
            "llm_total_tokens",
        ):
            values = [number(row, metric) for row in selected]
            numeric = [value for value in values if value is not None]
            item[f"{metric}_mean"] = round(mean(numeric), 3) if numeric else None
        output.append(item)
    return output


def analyze_correlations(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    pairs = [
        ("face_vs_task", "judge_face_plausibility", "task_completion"),
        ("face_vs_feasibility", "judge_face_plausibility", "trace_feasibility"),
        ("trace_believability_vs_task", "judge_trace_believability", "task_completion"),
        (
            "trace_believability_vs_feasibility",
            "judge_trace_believability",
            "trace_feasibility",
        ),
    ]
    groups = [("all", rows)] + [
        (agent, [row for row in rows if row["agent_type"] == agent])
        for agent in sorted({row["agent_type"] for row in rows})
    ]
    output = []
    for group, selected in groups:
        for name, x_key, y_key in pairs:
            values = [
                (number(row, x_key), number(row, y_key))
                for row in selected
                if number(row, x_key) is not None and number(row, y_key) is not None
            ]
            xs = [x for x, _ in values]
            ys = [y for _, y in values]
            p = pearson(xs, ys)
            s = spearman(xs, ys)
            output.append(
                {
                    "group": group,
                    "comparison": name,
                    "x_metric": x_key,
                    "y_metric": y_key,
                    "n": len(values),
                    "pearson_r": round(p, 3) if p is not None else None,
                    "spearman_rho": round(s, 3) if s is not None else None,
                }
            )
    cell_groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        cell_groups[(row["scenario_id"], row["agent_type"])].append(row)
    for name, x_key, y_key in pairs:
        residual_x: list[float] = []
        residual_y: list[float] = []
        for selected in cell_groups.values():
            values = [
                (number(row, x_key), number(row, y_key))
                for row in selected
                if number(row, x_key) is not None and number(row, y_key) is not None
            ]
            if not values:
                continue
            x_mean = mean([x for x, _ in values])
            y_mean = mean([y for _, y in values])
            residual_x.extend(x - x_mean for x, _ in values)
            residual_y.extend(y - y_mean for _, y in values)
        p = pearson(residual_x, residual_y)
        s = spearman(residual_x, residual_y)
        output.append(
            {
                "group": "within_scenario_agent",
                "comparison": name,
                "x_metric": x_key,
                "y_metric": y_key,
                "n": len(residual_x),
                "pearson_r": round(p, 3) if p is not None else None,
                "spearman_rho": round(s, 3) if s is not None else None,
            }
        )
    return output


def analyze_cells(rows: list[dict[str, str]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        groups[(row["scenario_id"], row["agent_type"])].append(row)
    output = []
    for (scenario, agent), selected in sorted(groups.items()):
        output.append(
            {
                "scenario_id": scenario,
                "agent_type": agent,
                "repeat_count": len(selected),
                "all_task_success": int(
                    all(number(row, "task_completion") >= 0.999 for row in selected)
                ),
                "all_fully_feasible": int(
                    all(number(row, "trace_feasibility") >= 0.999 for row in selected)
                ),
                "any_task_success": int(
                    any(number(row, "task_completion") >= 0.999 for row in selected)
                ),
                "any_infeasible": int(
                    any(number(row, "trace_feasibility") < 0.999 for row in selected)
                ),
                "task_completion_mean": round(
                    mean([number(row, "task_completion") for row in selected]), 3
                ),
                "face_plausibility_mean": round(
                    mean([number(row, "judge_face_plausibility") for row in selected]),
                    3,
                ),
            }
        )
    return output


def write_markdown(
    path: Path,
    agents: list[dict[str, Any]],
    correlations: list[dict[str, Any]],
    face_threshold: float,
) -> None:
    overall = {
        row["comparison"]: row
        for row in correlations
        if row["group"] == "all"
    }
    within = {
        row["comparison"]: row
        for row in correlations
        if row["group"] == "within_scenario_agent"
    }
    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# CityIntent Evidence Reliability And Dissociation\n\n")
        f.write(
            f"A trace is face-plausible when judge score >= {face_threshold:.2f}; "
            "full task success and full feasibility require score >= 0.999.\n\n"
        )
        f.write("## Architecture Table\n\n")
        f.write(
            "| Agent | n | Full task | Fully feasible | Plausible | "
            "Plausible task failure | Plausible infeasible | pass^k task | "
            "pass^k feasible |\n"
        )
        f.write("|---|---:|---:|---:|---:|---:|---:|---:|---:|\n")
        for row in agents:
            f.write(
                f"| {row['agent']} | {row['n']} | "
                f"{row['full_task_success_rate']:.3f} | "
                f"{row['fully_feasible_rate']:.3f} | "
                f"{row['plausible_rate']:.3f} | "
                f"{row['plausible_task_failure_rate']:.3f} | "
                f"{row['plausible_infeasible_rate']:.3f} | "
                f"{row['pass_k_task_rate']:.3f} | "
                f"{row['pass_k_feasible_rate']:.3f} |\n"
            )
        f.write("\n`pass^k` uses all available repeats for each scenario-agent cell.\n\n")
        f.write("## Metric Dissociation\n\n")
        f.write(
            "| Comparison | n | Pooled Pearson | Pooled Spearman | "
            "Within-cell Pearson | Within-cell Spearman |\n"
        )
        f.write("|---|---:|---:|---:|---:|---:|\n")
        for name in (
            "face_vs_task",
            "face_vs_feasibility",
            "trace_believability_vs_task",
            "trace_believability_vs_feasibility",
        ):
            row = overall[name]
            within_row = within[name]
            f.write(
                f"| `{name}` | {row['n']} | {row['pearson_r']} | "
                f"{row['spearman_rho']} | {within_row['pearson_r']} | "
                f"{within_row['spearman_rho']} |\n"
            )
        f.write("\n## Reading\n\n")
        f.write(
            "- No architecture dominates all proof obligations: task completion, "
            "feasibility, face plausibility, and repeated reliability rank systems differently.\n"
        )
        f.write(
            "- Face plausibility is not a valid substitute for environment-owned task "
            "or feasibility evidence in this sample.\n"
        )
        f.write(
            "- These are architecture-by-scenario pilot estimates, not human behavioral "
            "realism claims; human construct validation remains a separate release gate.\n"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--face-threshold", type=float, default=0.70)
    args = parser.parse_args()
    rows = read_csv(args.input)
    if not rows:
        raise SystemExit("input contains no rows")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    agents = analyze_agents(rows, args.face_threshold)
    correlations = analyze_correlations(rows)
    cells = analyze_cells(rows)
    write_csv(args.output_dir / "evidence_reliability.csv", agents)
    write_csv(args.output_dir / "metric_correlations.csv", correlations)
    write_csv(args.output_dir / "scenario_cell_reliability.csv", cells)
    write_markdown(
        args.output_dir / "evidence_analysis.md",
        agents,
        correlations,
        args.face_threshold,
    )
    manifest = {
        "input": str(args.input),
        "row_count": len(rows),
        "agent_count": len(agents),
        "scenario_cell_count": len(cells),
        "face_threshold": args.face_threshold,
        "task_success_threshold": 0.999,
        "feasibility_threshold": 0.999,
        "outputs": [
            "evidence_reliability.csv",
            "metric_correlations.csv",
            "scenario_cell_reliability.csv",
            "evidence_analysis.md",
        ],
    }
    with (args.output_dir / "evidence_analysis_manifest.json").open(
        "w", encoding="utf-8", newline="\n"
    ) as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Wrote repeated evidence analysis for {len(rows)} rows to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
