#!/usr/bin/env python3
"""Pool multiple SAME-CONFIG sweep out-dirs into one n + 95% CI (offline, no API).

Use to EXTEND n without re-running existing seeds: run new seeds into a fresh dir
(`--seed <next> --runs <k>`, non-overlapping), then pool the old + new dir here.

Usage:
    python sim/pool_runs.py DIR1 DIR2 [DIR3 ...]
Each DIR is a sweep --out-dir containing aggregate.json. Warns on config mismatch or
overlapping seeds (which would double-count, not add independent samples).
"""
from __future__ import annotations
import json
import math
import os
import sys


def load_rows(d: str) -> list[dict]:
    with open(os.path.join(d, "aggregate.json")) as fh:
        return json.load(fh).get("rows", [])


def main(dirs: list[str]) -> int:
    if not dirs:
        print(__doc__)
        return 1
    rows: list[dict] = []
    configs: set = set()
    for d in dirs:
        rs = load_rows(d)
        for r in rs:
            rows.append(r)
            configs.add((r.get("memory"), r.get("model"), r.get("rounds"),
                         r.get("turns"), r.get("agent_count")))
    if not rows:
        print("no runs found")
        return 1
    if len(configs) > 1:
        print("WARNING: configs differ across dirs (pooling may be invalid):")
        for c in configs:
            print("   memory/model/rounds/turns/agents =", c)
    seeds = [r.get("schedule_seed") for r in rows]
    dup = sorted({s for s in seeds if seeds.count(s) > 1})
    if dup:
        print(f"WARNING: overlapping seeds {dup} — these double-count, not add independent samples.")

    rates = []
    for r in rows:
        t = r["currency_interview"]
        tot = sum(t.values())
        rates.append(t["current"] / tot * 100 if tot else 0.0)
    n = len(rates)
    m = sum(rates) / n
    sd = (sum((x - m) ** 2 for x in rates) / n) ** 0.5
    sem = sd / math.sqrt(n)
    print(f"pooled n={n}  HOLD current = {m:.1f}%  95% CI [{m-1.96*sem:.1f}, {m+1.96*sem:.1f}]  (std {sd:.1f})")
    per = sorted((r.get("schedule_seed"), round(rt)) for r, rt in zip(rows, rates))
    print("per-seed (seed, current%):", per)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
