#!/usr/bin/env python3
"""Probe the provider's safe concurrency ceiling.

Fires N minimal calls concurrently for increasing N and reports successes, errors
(429 / rate-limit flagged separately), and wall time. Use the highest N with no
rate-limit errors as the safe total in-flight budget for experiment runs.

Usage:
    FHL_API_KEY=... python3 probe_rate_limit.py --levels 10 20 30 40
"""

from __future__ import annotations

import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import model_calling_runner as mcr

MINIMAL_PROMPT = {"system_prompt": "", "user_prompt": "Reply with exactly: ok"}


def one_call(client) -> tuple[bool, str]:
    try:
        client.complete(MINIMAL_PROMPT)
        return True, ""
    except Exception as exc:  # categorize rate limits separately
        msg = str(exc)
        return False, msg


def is_rate_limit(msg: str) -> bool:
    m = msg.lower()
    return "429" in m or "rate" in m or "too many" in m or "quota" in m


def main() -> int:
    parser = argparse.ArgumentParser(description="Probe provider concurrency ceiling.")
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--levels", type=int, nargs="+", default=[10, 20, 30, 40])
    args = parser.parse_args()

    cfg_args = argparse.Namespace(config=args.config, provider=None, model=None, temperature=None,
                                  timeout=None, sleep=None, no_json_mode=False, workers=None)
    client = mcr.build_client(mcr.resolve_run_config(cfg_args))

    print(f"{'N':>4} {'ok':>5} {'rate-limited':>13} {'other-err':>10} {'wall_s':>8} {'calls/s':>8}")
    for n in args.levels:
        start = time.monotonic()
        oks = rl = err = 0
        with ThreadPoolExecutor(max_workers=n) as ex:
            futs = [ex.submit(one_call, client) for _ in range(n)]
            for f in as_completed(futs):
                ok, msg = f.result()
                if ok:
                    oks += 1
                elif is_rate_limit(msg):
                    rl += 1
                else:
                    err += 1
        wall = time.monotonic() - start
        print(f"{n:>4} {oks:>5} {rl:>13} {err:>10} {wall:>8.1f} {n / wall:>8.1f}", flush=True)
        if rl > 0:
            print(f"  -> rate-limit errors appeared at N={n}; safe ceiling is below this.", flush=True)
        time.sleep(2)  # brief cooldown between levels
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
