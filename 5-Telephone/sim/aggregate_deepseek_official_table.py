#!/usr/bin/env python3
"""Aggregate official-API DeepSeek Table 1 coverage runs.

The sweep writer only emits ``runs.json`` after a full method finishes.  This
aggregator also recovers completed runs from their per-run artifacts, so an
interrupted provider sweep can be audited without silently dropping data.
"""

from __future__ import annotations

import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUN_ROOT = (
    ROOT / "sim" / "runs" / "deepseek_official_table_n5_2026-07-25"
)
OUT = RUN_ROOT / "combined_summary.json"
T95 = {
    1: 12.706204736432095,
    2: 4.302652729696142,
    3: 3.182446305284263,
    4: 2.7764451051977987,
}


def recover_rows(method_dir: Path) -> list[dict]:
    rows = []
    for interview_path in sorted(method_dir.glob("**/interview_currency.json")):
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
                "method": summary["memory"],
                "model": summary["model"],
                "seed": int(summary["schedule_seed"]),
                "agent_count": int(summary["agent_count"]),
                "current": counts["current"],
                "stale": counts["stale"],
                "unknown": counts["unknown"],
                "run_dir": str(run_dir.relative_to(ROOT)),
            }
        )
    return rows


def summarize(rows: list[dict]) -> dict:
    if not rows:
        return {"n": 0}
    by_seed = {}
    for row in rows:
        seed = row["seed"]
        if seed in by_seed:
            raise ValueError(f"duplicate completed run for seed {seed}")
        by_seed[seed] = row
    ordered = [by_seed[seed] for seed in sorted(by_seed)]
    rates = [100.0 * row["current"] / row["agent_count"] for row in ordered]
    mean = statistics.mean(rates)
    if len(rates) > 1:
        df = len(rates) - 1
        if df not in T95:
            raise ValueError(f"unsupported sample size n={len(rates)}")
        half = T95[df] * statistics.stdev(rates) / math.sqrt(len(rates))
        ci = [max(0.0, mean - half), min(100.0, mean + half)]
    else:
        ci = None
    return {
        "n": len(ordered),
        "seeds": [row["seed"] for row in ordered],
        "seed_current_rates_pct": rates,
        "pooled_counts": {
            verdict: sum(row[verdict] for row in ordered)
            for verdict in ("current", "stale", "unknown")
        },
        "mean_pct": mean,
        "ci95_pct": ci,
        "table": {
            "mean": round(mean, 1),
            "lo": round(ci[0], 1) if ci else None,
            "hi": round(ci[1], 1) if ci else None,
        },
        "runs": ordered,
    }


def main() -> None:
    result = {
        "model": "deepseek-v4-flash",
        "endpoint_class": "official DeepSeek API",
        "scenario": "repair_drive",
        "estimator": "seed-level mean with two-sided Student-t 95% CI",
        "methods": {},
    }
    for method_dir in sorted(path for path in RUN_ROOT.iterdir() if path.is_dir()):
        result["methods"][method_dir.name] = summarize(recover_rows(method_dir))
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(OUT)
    for method, summary in result["methods"].items():
        print(f"{method}: n={summary['n']} {summary.get('table')}")


if __name__ == "__main__":
    main()
