#!/usr/bin/env python3
"""Combine the seed-41 pilots and seed-42--45 extensions for Table 1."""

from __future__ import annotations

import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "sim" / "runs"
OUT = RUNS / "table_power_n5_2026-07-24" / "combined_n5_summary.json"
T95_DF4 = 2.7764451051977987

SOURCES = {
    "book_club": [
        RUNS / "table_fill_n1_2026-07-24" / "book_club" / "runs.json",
        RUNS / "table_power_n5_2026-07-24" / "book_club" / "runs.json",
    ],
    "carpool": [
        RUNS / "table_fill_n1_2026-07-24" / "carpool" / "runs.json",
        RUNS / "table_power_n5_2026-07-24" / "carpool" / "runs.json",
    ],
    "dues": [
        RUNS / "table_fill_n1_2026-07-24" / "dues" / "runs.json",
        RUNS / "table_power_n5_2026-07-24" / "dues" / "runs.json",
    ],
    "three_step": [
        RUNS
        / "table_complete_n1_2026-07-24"
        / "three_step_matched_r7"
        / "runs.json",
        RUNS
        / "table_power_n5_2026-07-24"
        / "three_step_matched_r7"
        ,
        RUNS
        / "table_power_n5_2026-07-24"
        / "resume_three_memorybank"
        ,
        RUNS
        / "table_power_n5_2026-07-24"
        / "resume_three_prov"
        ,
    ],
    "long_horizon": [
        RUNS / "table_complete_n1_2026-07-24" / "long_horizon" / "runs.json",
        RUNS
        / "table_power_n5_2026-07-24"
        / "long_horizon"
        ,
        RUNS
        / "table_power_n5_2026-07-24"
        / "resume_long_memorybank"
        ,
        RUNS / "table_power_n5_2026-07-25" / "retry2_long_mb_seed44",
        RUNS / "table_power_n5_2026-07-25" / "retry2_long_mb_seed45",
        RUNS / "prov_horizon" / "prov_r10_final" / "runs.json",
    ],
}

R5_SOURCES = {
    "repair_drive": [
        RUNS / "table_repair" / "raw" / "runs.json",
        RUNS / "table_repair" / "mem0" / "runs.json",
        RUNS / "table_repair" / "amem" / "runs.json",
        RUNS / "prov_batch" / "ga_r5" / "runs.json",
        RUNS / "table_repair" / "smga3g" / "runs.json",
        RUNS / "table_repair" / "memorybank" / "runs.json",
        RUNS / "prov_fair" / "prov" / "runs.json",
    ],
    "book_club": SOURCES["book_club"] + [
        RUNS / "table_3scenario" / "book_club_amem" / "runs.json",
        RUNS / "table_3scenario" / "book_club_ga" / "runs.json",
        RUNS / "table_3scenario" / "book_club_smga3g" / "runs.json",
        RUNS / "table_3scenario" / "book_club_prov" / "runs.json",
    ],
    "carpool": SOURCES["carpool"] + [
        RUNS / "table_3scenario" / "carpool_amem" / "runs.json",
        RUNS / "table_3scenario" / "carpool_ga" / "runs.json",
        RUNS / "table_3scenario" / "carpool_smga3g" / "runs.json",
        RUNS / "table_3scenario" / "carpool_prov" / "runs.json",
    ],
    "dues": SOURCES["dues"] + [
        RUNS / "dues" / "amem" / "runs.json",
        RUNS / "dues" / "ga" / "runs.json",
        RUNS / "dues" / "smga3g" / "runs.json",
        RUNS / "dues" / "prov" / "runs.json",
    ],
}


def recovered_rows(root: Path) -> list[dict]:
    """Recover completed rows when an interrupted sweep did not write runs.json."""
    rows = []
    for interview_path in sorted(root.glob("**/interview_currency.json")):
        run_dir = interview_path.parent
        summary_path = run_dir / "sim_summary.json"
        if not summary_path.exists():
            continue
        summary = json.loads(summary_path.read_text())
        interview = json.loads(interview_path.read_text())
        counts = defaultdict(int)
        for result in interview["results"].values():
            counts[result["verdict"]] += 1
        rows.append(
            {
                "memory": summary["memory"],
                "model": summary["model"],
                "schedule_seed": summary["schedule_seed"],
                "agent_count": summary["agent_count"],
                "currency_interview": {
                    "current": counts["current"],
                    "stale": counts["stale"],
                    "unknown": counts["unknown"],
                },
            }
        )
    return rows


def read_rows(paths: list[Path]) -> list[dict]:
    rows: list[dict] = []
    for path in paths:
        if path.is_dir():
            rows.extend(recovered_rows(path))
        elif path.exists():
            rows.extend(json.loads(path.read_text()))
    return rows


def summarize_rates(rates: list[float], seeds: list[int]) -> dict:
    mean = statistics.mean(rates)
    if len(rates) > 1:
        sem = statistics.stdev(rates) / math.sqrt(len(rates))
        half = T95_DF4 * sem if len(rates) == 5 else float("nan")
        ci = [max(0.0, mean - half), min(100.0, mean + half)]
    else:
        ci = None
    return {
        "n": len(rates),
        "seeds": seeds,
        "seed_current_rates_pct": rates,
        "mean_pct": mean,
        "ci95_pct": ci,
        "table": {
            "mean": round(mean),
            "lo": round(ci[0]) if ci else None,
            "hi": round(ci[1]) if ci else None,
        },
    }


def summarize(rows: list[dict]) -> dict[str, dict]:
    by_method: dict[str, dict[int, dict]] = defaultdict(dict)
    for row in rows:
        method = row["memory"]
        seed = int(row["schedule_seed"])
        if seed in by_method[method]:
            raise ValueError(f"duplicate row for {method=} {seed=}")
        by_method[method][seed] = row

    summary: dict[str, dict] = {}
    for method, seeded in sorted(by_method.items()):
        seeds = sorted(seeded)
        ordered = [seeded[seed] for seed in seeds]
        rates = [
            100.0 * row["currency_interview"]["current"] / row["agent_count"]
            for row in ordered
        ]
        summary[method] = summarize_rates(rates, seeds)
    return summary


def r5_macro_average() -> dict[str, dict]:
    """Equal-weight macro-average of the four reported matched r=5 task means."""
    by_scenario = {
        scenario: summarize(read_rows(paths))
        for scenario, paths in R5_SOURCES.items()
    }
    methods = sorted(set.intersection(*[
        set(scenario_rows) for scenario_rows in by_scenario.values()
    ]))
    output = {}
    for method in methods:
        task_means = {
            scenario: scenario_rows[method]["mean_pct"]
            for scenario, scenario_rows in by_scenario.items()
        }
        macro_mean = statistics.mean(task_means.values())
        output[method] = {
            "n_tasks": len(task_means),
            "task_means_pct": task_means,
            "macro_mean_pct": macro_mean,
            "table": {"mean": round(macro_mean, 1)},
        }
    return output


def main() -> None:
    result = {
        "method": "seed-level mean with two-sided Student-t 95% CI (df=4)",
        "scenarios": {
            scenario: summarize(read_rows(paths))
            for scenario, paths in SOURCES.items()
        },
        "r5_macro_average": r5_macro_average(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(OUT)
    for scenario, methods in result["scenarios"].items():
        cells = ", ".join(
            f"{method}: n={value['n']} {value['table']}"
            for method, value in methods.items()
        )
        print(f"{scenario}: {cells}")
    macro_cells = ", ".join(
        f"{method}: tasks={value['n_tasks']} {value['table']}"
        for method, value in result["r5_macro_average"].items()
    )
    print(f"r5_macro_average: {macro_cells}")


if __name__ == "__main__":
    main()
