#!/usr/bin/env python3
"""P2: re-score interview answers with an LLM JUDGE (semantic, not keyword).

Addresses the "your current/stale metric is surface-keyword / circular" critique. Given a
scenario's ground truth, an LLM classifies each held answer as current / stale / unknown
WITHOUT keyword matching, and we report judge-vs-keyword agreement + the re-aggregated
headline. Run on the dissociation runs to show the result survives a non-keyword metric.
"""
from __future__ import annotations
import argparse, glob, json, statistics as st, math
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from llm import LLM
from society import SCENARIOS

JUDGE_SYS = (
    "You classify whether a person's answer reflects the CURRENT (updated) truth, the STALE "
    "(old, now-wrong) value, or is UNKNOWN/uncertain. Judge MEANING, not exact words. Return "
    'ONLY JSON: {"verdict": "current" | "stale" | "unknown"}.'
)


def desc(markers):
    return " / ".join(markers)


def judge_answer(llm, sc, answer):
    if not str(answer).strip():
        return "unknown"
    user = (
        f"Event: {sc['event']}.\n"
        f"CURRENT truth (updated): {desc(sc['current_markers'])}.\n"
        f"STALE value (old, now wrong): {desc(sc['stale_markers'])}.\n\n"
        f"Answer to classify: \"{answer}\"\n\n"
        "current = asserts the updated value; stale = asserts the old value; unknown = "
        "neither / says it doesn't know / no time+place given."
    )
    try:
        out = llm.complete_json(JUDGE_SYS, user)
        v = str(out.get("verdict", "unknown")).lower().strip()
        return v if v in ("current", "stale", "unknown") else "unknown"
    except Exception:
        return "unknown"


def rescore_run(llm, sc, ivfile, workers):
    iv = json.loads(Path(ivfile).read_text())["results"]
    items = list(iv.items())
    with ThreadPoolExecutor(max_workers=workers) as ex:
        judged = list(ex.map(lambda kv: judge_answer(llm, sc, kv[1].get("answer", "")), items))
    keyword = [info["verdict"] for _, info in items]
    return keyword, judged


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--runs-glob", required=True, help="glob to interview_currency.json files")
    p.add_argument("--scenario", default="repair_drive")
    p.add_argument("--config", type=Path,
                   default=Path("/Users/mac/Documents/6-Research/3-SMGA/benchmarks/diagnostic_v0/configs/fhl_responses_gpt54mini_config.json"))
    p.add_argument("--workers", type=int, default=16)
    args = p.parse_args()
    llm = LLM(config=args.config, model="gpt-5.4-mini")
    sc = SCENARIOS[args.scenario]
    files = sorted(glob.glob(args.runs_glob))
    agree = total = 0
    kw_cur = []; jd_cur = []
    confusion = Counter()
    for f in files:
        kw, jd = rescore_run(llm, sc, f, args.workers)
        for a, b in zip(kw, jd):
            total += 1; agree += (a == b); confusion[(a, b)] += 1
        kw_cur.append(sum(1 for x in kw if x == "current"))
        jd_cur.append(sum(1 for x in jd if x == "current"))
    print(f"files={len(files)} answers={total}")
    print(f"keyword vs judge AGREEMENT: {agree}/{total} = {agree/total:.0%}")
    print(f"keyword current/run mean {st.mean(kw_cur):.1f}  |  judge current/run mean {st.mean(jd_cur):.1f}")
    print("confusion (keyword→judge):", dict(confusion))


if __name__ == "__main__":
    main()
