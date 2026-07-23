"""Item analysis for the CityIntent scenario set (zero-API).

Standard benchmark practice: a scenario earns its place only if it *separates*
policies. This reports, per scenario:

- mean task_completion across policies (difficulty)
- spread across policies (discrimination: sd + range)
- item-total correlation — does a scenario rank policies the way the whole
  benchmark does? Low or negative means the item measures something else, or noise.
- ceiling / floor flags — every policy at 1.0 or at 0.0 carries no information

Aggregates over every archived run that has an `all_runs.csv`, grouped by tier.
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics as st
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[2]
RESULTS = REPO_ROOT / "6-city" / "results" / "cityintent_v1_rc1"
SCENARIO_DIR = ROOT / "scenarios"
DEFAULT_OUTPUT = RESULTS / "scenario_discrimination_2026-07-10"


def scenario_family(scenario_id: str) -> str:
    path = SCENARIO_DIR / f"{scenario_id}.json"
    if not path.exists():
        return "unknown"
    with path.open(encoding="utf-8") as f:
        return json.load(f).get("family", "unknown")


def collect(run_dirs: list[Path]) -> dict[str, dict[str, list[float]]]:
    """scenario -> policy -> [task_completion per repeat]"""
    data: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    for run_dir in run_dirs:
        path = run_dir / "all_runs.csv"
        if not path.exists():
            continue
        with path.open(encoding="utf-8") as f:
            for row in csv.DictReader(f):
                value = row.get("task_completion")
                if value in (None, ""):
                    continue
                data[row["scenario_id"]][row["agent_type"]].append(float(value))
    return data


def pearson(xs: list[float], ys: list[float]) -> float | None:
    if len(xs) < 3:
        return None
    mx, my = st.mean(xs), st.mean(ys)
    num = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    dx = sum((a - mx) ** 2 for a in xs) ** 0.5
    dy = sum((b - my) ** 2 for b in ys) ** 0.5
    return None if dx == 0 or dy == 0 else num / (dx * dy)


def analyse(data: dict[str, dict[str, list[float]]]) -> list[dict[str, Any]]:
    # policy mean per scenario
    per: dict[str, dict[str, float]] = {
        s: {p: st.mean(v) for p, v in pol.items() if v} for s, pol in data.items()
    }
    policies = sorted({p for pol in per.values() for p in pol})
    # overall policy ability = mean across scenarios
    ability = {
        p: st.mean([per[s][p] for s in per if p in per[s]])
        for p in policies
    }
    rows: list[dict[str, Any]] = []
    for scenario, scores in per.items():
        shared = [p for p in policies if p in scores]
        vals = [scores[p] for p in shared]
        # item-total correlation, excluding this item from the total
        rest = {
            p: st.mean([per[s][p] for s in per if s != scenario and p in per[s]] or [0.0])
            for p in shared
        }
        corr = pearson(vals, [rest[p] for p in shared])
        rows.append({
            "scenario": scenario,
            "family": scenario_family(scenario),
            "policies": len(shared),
            "mean": round(st.mean(vals), 3),
            "sd": round(st.pstdev(vals), 3) if len(vals) > 1 else 0.0,
            "range": round(max(vals) - min(vals), 3),
            "item_total_r": None if corr is None else round(corr, 3),
            "ceiling": all(v >= 0.999 for v in vals),
            "floor": all(v <= 0.001 for v in vals),
        })
    rows.sort(key=lambda r: (r["family"], -r["range"]))
    return rows


def render(rows: list[dict[str, Any]]) -> str:
    out = [
        "# Scenario Discrimination (item analysis)",
        "",
        "Per scenario: difficulty (mean task_completion across policies), how well it",
        "separates policies (sd / range), and item-total correlation against the rest",
        "of the benchmark. A scenario with range ≈ 0 carries no information; a negative",
        "item-total correlation means it ranks policies against the overall ordering.",
        "",
        "| Scenario | Family | Policies | Mean | SD | Range | Item-total r | Flag |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        flags = []
        if r["ceiling"]:
            flags.append("CEILING")
        if r["floor"]:
            flags.append("FLOOR")
        if r["range"] < 0.15:
            flags.append("low-discrimination")
        if r["item_total_r"] is not None and r["item_total_r"] < 0:
            flags.append("anti-correlated")
        out.append(
            f"| `{r['scenario']}` | {r['family']} | {r['policies']} | {r['mean']} | "
            f"{r['sd']} | {r['range']} | {r['item_total_r']} | {', '.join(flags) or 'ok'} |"
        )
    good = [r for r in rows if r["range"] >= 0.15 and not r["ceiling"] and not r["floor"]]
    out += [
        "",
        f"**Informative scenarios: {len(good)}/{len(rows)}** "
        "(range ≥ 0.15, not at ceiling or floor).",
    ]
    return "\n".join(out) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    run_dirs = sorted(d for d in RESULTS.iterdir() if d.is_dir() and (d / "all_runs.csv").exists())
    data = collect(run_dirs)
    rows = analyse(data)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "scenario_discrimination.json").write_text(
        json.dumps({
            "generated": datetime.now(timezone.utc).isoformat(),
            "source_runs": [d.name for d in run_dirs],
            "rows": rows,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
    text = render(rows)
    (args.output_dir / "scenario_discrimination.md").write_text(text, encoding="utf-8")
    print(f"sources: {len(run_dirs)} runs")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
