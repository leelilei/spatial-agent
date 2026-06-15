#!/usr/bin/env python3
"""De-risk pilot: does implicit reconciliation (GA-style) mis-track CHAINED
contradictions, and does explicit currency-tracking fix it?

A single fact (a recurring meeting's location) is revised L times: A->B->C->...,
interleaved with distractor events. The question always asks for the CURRENT
value. We compare three digestion framings, all using the same model:

  raw      : list the events in order, then ask the current value (no digestion).
  reflect  : first ask for a free-text summary of what to remember (GA reflection),
             then ask the current value given that summary.
  currency : first ask the model to list each changing fact's CURRENT value and mark
             older values as superseded (explicit currency tracking), then ask.

If currency > reflect > raw on naming the current value as chain length grows,
explicit currency structure earns its keep where GA's implicit reconciliation
breaks. If all are equal, a strong model tracks chains unaided and currency
structure adds little (at least at these lengths).

Usage:
    FHL_API_KEY=... python3 verify_chain_tracking.py --lengths 3 5 8 --n 6
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import model_calling_runner as mcr

HERE = Path(__file__).resolve().parent

PLACES = ["the east wing", "the annex", "the rooftop room", "the basement lab",
          "the library alcove", "the garden office", "the north studio",
          "the pier cabin", "the atrium", "the vault room", "the loft", "the dock house"]
PEOPLE = ["Ada", "Ben", "Cora", "Dane", "Esa", "Fox", "Gus", "Hana", "Ivo", "Jae"]
TOPICS = ["budget", "design", "hiring", "launch", "audit", "press"]


def make_scenario(rng: random.Random, chain_len: int) -> tuple[list[str], str, str, str]:
    """Return (event_lines, meeting_name, final_place, question)."""
    owner = rng.choice(PEOPLE)
    topic = rng.choice(TOPICS)
    meeting = f"{owner}'s {topic} sync"
    places = rng.sample(PLACES, chain_len + 1)
    others = [p for p in PEOPLE if p != owner]

    chain_events = []
    for i in range(chain_len + 1):
        when = f"day {i+1}"
        if i == 0:
            chain_events.append(f"[{when}] {meeting} is held in {places[i]}.")
        else:
            chain_events.append(f"[{when}] {meeting} is moved from {places[i-1]} to {places[i]}.")

    # distractor events about OTHER meetings/people, ~1.5x the chain length
    distractors = []
    for _ in range(int(chain_len * 1.5) + 2):
        a, b = rng.sample(others, 2)
        distractors.append(f"[note] {a} and {b} discussed the {rng.choice(TOPICS)} plan in {rng.choice(PLACES)}.")

    # interleave: keep chain events in order, scatter distractors around them
    events = []
    di = 0
    for ci, ev in enumerate(chain_events):
        # drop 0-2 distractors before each chain event
        for _ in range(rng.randint(0, 2)):
            if di < len(distractors):
                events.append(distractors[di]); di += 1
        events.append(ev)
    while di < len(distractors):
        events.append(distractors[di]); di += 1

    question = f"Where is {meeting} held right now?"
    return events, meeting, places[chain_len], question


def names_place(answer: str, place: str) -> bool:
    a = answer.lower()
    # match on the distinctive noun of the place (e.g. "rooftop", "annex")
    key = place.replace("the ", "").split()[0]
    return key in a


def ask(client, system: str, user: str) -> str:
    return client.complete({"system_prompt": system, "user_prompt": user})


def run_framing(client, framing: str, events: list[str], question: str) -> str:
    history = "\n".join(events)
    if framing == "raw":
        sys_p = "You answer questions from a list of timestamped events. Reply with one short sentence."
        return ask(client, sys_p, f"Events:\n{history}\n\nQuestion: {question}")
    if framing == "reflect":
        sys_p = "You are a generative agent reflecting on your memory stream."
        summary = ask(client, sys_p, f"Events:\n{history}\n\nSummarize the key things to remember from these events, in a few sentences.")
        return ask(client, "You answer using the summary. Reply with one short sentence.",
                   f"Summary of what you remember:\n{summary}\n\nQuestion: {question}")
    if framing == "currency":
        sys_p = "You track which facts are currently true. Some facts change over time; only the latest value is current."
        digest = ask(client, sys_p,
                     f"Events:\n{history}\n\nFor each fact that changed over time, write its CURRENT value and list the older values as SUPERSEDED. Be explicit about what is current now.")
        return ask(client, "You answer using the current-facts digest. Reply with one short sentence.",
                   f"Current-facts digest:\n{digest}\n\nQuestion: {question}")
    raise ValueError(framing)


def main() -> int:
    parser = argparse.ArgumentParser(description="Chained-contradiction tracking de-risk pilot.")
    parser.add_argument("--config", type=Path, default=Path("configs/fhl_responses_gpt54_config.example.json"))
    parser.add_argument("--lengths", type=int, nargs="+", default=[3, 5, 8])
    parser.add_argument("--n", type=int, default=6, help="scenarios per chain length")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument("--out", type=Path, default=Path("tmp/chain_tracking_results.json"))
    args = parser.parse_args()

    cfg_args = argparse.Namespace(config=args.config, provider=None, model=None, temperature=None,
                                  timeout=None, sleep=None, no_json_mode=False, workers=None)
    client = mcr.build_client(mcr.resolve_run_config(cfg_args))
    framings = ["raw", "reflect", "currency"]

    results: dict[str, dict[int, list[bool]]] = {f: {L: [] for L in args.lengths} for f in framings}
    rng = random.Random(args.seed)
    for L in args.lengths:
        for i in range(args.n):
            events, meeting, final_place, question = make_scenario(rng, L)
            for f in framings:
                try:
                    ans = run_framing(client, f, events, question)
                    ok = names_place(ans, final_place)
                except Exception as exc:  # capture provider errors per item
                    print(f"  L={L} #{i} {f}: ERROR {exc}", flush=True)
                    ok = False
                    ans = f"ERROR {exc}"
                results[f][L].append(ok)
                print(f"L={L} #{i} {f:8} -> {'OK ' if ok else 'MISS'}  (want {final_place}) :: {ans[:90]}", flush=True)

    print("\n=== accuracy: name the CURRENT value (chain length L) ===")
    header = "framing    " + "  ".join(f"L={L:>2}" for L in args.lengths)
    print(header)
    for f in framings:
        cells = []
        for L in args.lengths:
            v = results[f][L]
            cells.append(f"{sum(v)}/{len(v)}")
        print(f"{f:10} " + "  ".join(f"{c:>5}" for c in cells))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps({f: {str(L): results[f][L] for L in args.lengths} for f in framings}, indent=2))
    print(f"\nsaved -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
