#!/usr/bin/env python3
"""Probe the provider's real concurrency capacity (raw, no retry masking)."""
import time, statistics
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from llm import LLM

CFG = Path("/Users/mac/Documents/6-Research/3-SMGA/benchmarks/diagnostic_v0/configs/fhl_responses_gpt54mini_config.json")
PROMPT = {"system_prompt": "reply ok", "user_prompt": "say ok"}


def probe(model, levels):
    llm = LLM(config=CFG, model=model)
    print("\n=== %s ===" % model)
    print("%5s | %8s | %6s | %6s | errors" % ("conc", "ok", "p50s", "maxs"))
    for C in levels:
        def one(_):
            t = time.time()
            try:
                llm.client.complete(PROMPT)
                return (True, time.time() - t, None)
            except Exception as e:
                return (False, time.time() - t, str(e)[:40])
        with ThreadPoolExecutor(max_workers=C) as ex:
            res = list(ex.map(one, range(C)))
        oks = [r for r in res if r[0]]
        lat = [r[1] for r in oks]
        errs = [r[2] for r in res if not r[0]]
        p50 = statistics.median(lat) if lat else 0.0
        mx = max(lat) if lat else 0.0
        es = " | ".join("%dx %s" % (n, e) for e, n in Counter(errs).most_common(2))
        print("%5d | %4d/%-3d | %6.1f | %6.1f | %s" % (C, len(oks), C, p50, mx, es))


if __name__ == "__main__":
    probe("gpt-5.4-mini", [8, 16, 24, 32, 48, 64])
    print("\n... 25s cooldown (clear shared RPM window before next model) ...")
    time.sleep(25)
    probe("gpt-5.5", [4, 8, 16, 24, 32])
