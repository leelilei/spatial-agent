#!/usr/bin/env python3
"""Live progress + per-architecture accuracy for the SMGA diagnostic pilot.

Reads the judge summaries written under tmp/smga_*/judge/ and shows, per seed,
the headline accuracy of each condition (architecture), plus running per-condition
averages and overall completion progress. probe_0003 is a flagged no-history
control and is reported separately, never in the headline.

Usage:
    python3 progress_monitor.py                 # one snapshot
    python3 progress_monitor.py --watch         # refresh every 5s
    python3 progress_monitor.py --start 1 --end 40 --watch --interval 3
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONDITIONS = ["M0_GA", "M0_prompted", "M2_memory_only", "M3_placebo", "M3_actionable"]
LABELS = {
    "M0_GA": "M0_GA",
    "M0_prompted": "M0_prmpt",
    "M2_memory_only": "M2_mem",
    "M3_placebo": "M3_plcbo",
    "M3_actionable": "M3_act",
}


def load_verdicts() -> dict[tuple[str, str], dict[str, bool]]:
    out: dict[tuple[str, str], dict[str, bool]] = {}
    for path in glob.glob(str(HERE / "tmp" / "smga_*" / "judge" / "*_judge_summary.json")):
        try:
            doc = json.load(open(path, encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue  # a summary being written right now; skip this tick
        key = (doc.get("seed_id"), doc.get("condition_id"))
        out[key] = {r.get("probe_id"): bool(r.get("pass")) for r in doc.get("results", [])}
    return out


def seed_probe_split(seed_id: str) -> tuple[list[str], list[str]]:
    """Return (headline_probe_ids, control_probe_ids) from the seed's probes.json."""
    probes_path = HERE / "seeds" / seed_id / "probes.json"
    headline, control = [], []
    try:
        probes = json.load(open(probes_path, encoding="utf-8")).get("probes", [])
    except (OSError, json.JSONDecodeError):
        return headline, control
    for p in probes:
        (control if p.get("no_history_solvability_flag") else headline).append(p["probe_id"])
    return headline, control


def render(start: int, end: int) -> str:
    seeds = [f"seed_{i:04d}" for i in range(start, end + 1)]
    V = load_verdicts()

    lines: list[str] = []
    lines.append(f"SMGA pilot live progress  ({time.strftime('%H:%M:%S')})")
    lines.append("=" * 86)

    # per-condition running tallies over completed cells
    pass_sum = {c: 0 for c in CONDITIONS}
    total_sum = {c: 0 for c in CONDITIONS}
    ctrl_pass = {c: 0 for c in CONDITIONS}
    ctrl_total = {c: 0 for c in CONDITIONS}
    seeds_complete = 0

    header = f"{'seed':10} " + " ".join(f"{LABELS[c]:>9}" for c in CONDITIONS) + f"  {'ctrl':>5}"
    lines.append(header)
    lines.append("-" * 86)

    for seed in seeds:
        headline, control = seed_probe_split(seed)
        if not headline:
            continue  # seed not generated yet
        present = [c for c in CONDITIONS if (seed, c) in V]
        if len(present) == len(CONDITIONS):
            seeds_complete += 1
        if not present:
            continue  # nothing scored for this seed yet — skip the row entirely

        cells = []
        ctrl_cells = []
        for c in CONDITIONS:
            v = V.get((seed, c))
            if v is None:
                cells.append(f"{'·':>9}")
                continue
            hp = sum(1 for pid in headline if v.get(pid))
            pass_sum[c] += hp
            total_sum[c] += len(headline)
            cells.append(f"{hp}/{len(headline):<7}")
            cp = sum(1 for pid in control if v.get(pid))
            ctrl_pass[c] += cp
            ctrl_total[c] += len(control)
            ctrl_cells.append(cp == len(control))
        ctrl_mark = "ok" if ctrl_cells and all(ctrl_cells) else ("mix" if ctrl_cells else "-")
        lines.append(f"{seed:10} " + " ".join(cells) + f"  {ctrl_mark:>5}")

    lines.append("-" * 86)
    # running average accuracy per condition
    avg_cells = []
    for c in CONDITIONS:
        if total_sum[c]:
            avg_cells.append(f"{pass_sum[c] / total_sum[c] * 100:>7.0f}%")
        else:
            avg_cells.append(f"{'-':>8}")
    lines.append(f"{'AVG acc':10} " + " ".join(f"{a:>9}" for a in avg_cells))

    # overall mean over all conditions scored so far
    grand_pass = sum(pass_sum.values())
    grand_total = sum(total_sum.values())
    overall = f"{grand_pass / grand_total * 100:.1f}%" if grand_total else "n/a"

    lines.append("=" * 86)
    lines.append(
        f"seeds complete: {seeds_complete}/{len(seeds)}   "
        f"scored cells: {sum(1 for s in seeds for c in CONDITIONS if (s, c) in V)}/{len(seeds) * len(CONDITIONS)}   "
        f"overall mean acc (all conditions): {overall}"
    )
    # headline gaps once there is data
    if total_sum["M3_actionable"] and total_sum["M0_GA"]:
        m3 = pass_sum["M3_actionable"] / total_sum["M3_actionable"] * 100
        m0 = pass_sum["M0_GA"] / total_sum["M0_GA"] * 100
        plc = pass_sum["M3_placebo"] / total_sum["M3_placebo"] * 100 if total_sum["M3_placebo"] else 0
        lines.append(
            f"M3_act {m3:.0f}%  vs  M0_GA {m0:.0f}%  (gap +{m3 - m0:.0f}pp)   "
            f"vs  M3_placebo {plc:.0f}%  (gap +{m3 - plc:.0f}pp)"
        )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Live SMGA pilot progress monitor.")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=40)
    parser.add_argument("--watch", action="store_true", help="Refresh continuously.")
    parser.add_argument("--interval", type=float, default=5.0, help="Watch refresh seconds.")
    args = parser.parse_args()

    if not args.watch:
        print(render(args.start, args.end))
        return 0
    try:
        while True:
            os.system("clear")
            print(render(args.start, args.end))
            print(f"\n(watching every {args.interval:g}s — Ctrl-C to stop)")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
