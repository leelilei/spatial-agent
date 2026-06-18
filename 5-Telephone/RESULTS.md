# Telephone — results

## Experiment ledger (RULE: every run gets a row here — even small/failed ones)

| date | id | what | key config | headline result | status |
|---|---|---|---|---|---|
| 06-19 | M0 | DE-RISK capability ladder mini→gpt-5.4→gpt-5.5 | GA mem, 25a m2 r5 t3, seeds 41-43, n=3 | DE-RISK PASSES: current FLAT 16%→20%→21%; scaling does NOT fix decay — it converts forgetting into CONFIDENT corruption (stale 2.3→9→10; Sat-dom 8→16→15) | done |

> Origin evidence (from the parent project) motivating Telephone:
> `../3-SMGA/sim/RESULTS.md` → **S5L-diag** (weak-model diffusion corrupts a fact-update;
> seed 41: 18/22 "receivers" were Saturday-dominant — stale-persistence + detail drift).

| 06-19 | M1 | (capability × connectivity) phase diagram | GA, 25a r5 t3, 3×3, seeds 41-43 | CORRUPTION EVERYWHERE: current ≤28% in all cells; connectivity↑ AMPLIFIES corruption (5.4 Sat:Sun 0.9×→10.4× as meetings 1→3). Neither capability nor connectivity saves truth | done |

| 06-19 | M2 | MEMORY AXIS: is corruption GA's fault or fundamental? raw / ga / smga(v2) / smga3g(v3-general) | mini, 25a m2 r5 t3, seeds 41-43 | does any honest memory restore truth, or do all corrupt (=fundamental, not GA-specific)? Also = first cut of C4 | RUNNING |

Detailed write-ups follow below as runs land.

---

# M0 — DE-RISK: does truth-decay survive model capability? (2026-06-19)

The load-bearing question for the whole project (raised by the human): is the truth-decay
just a weak-model artifact? We ran the SAME propagating scenario (GA-reflection agents, 25
agents, meetings=2, r5, turns=3, seeds 41–43) across a capability ladder — mini (reused
from 3-SMGA live GA runs) → gpt-5.4 → gpt-5.5 (the strongest FHL model available).

```text
model     mean current   mean stale   receivers: Sat-dom / Sun-dom (Σ over 3 seeds)
mini       4.0/25 (16%)   2.3/25        8 / 8
gpt-5.4    5.0/25 (20%)   9.0/25       16 / 9
gpt-5.5    5.3/25 (21%)  10.0/25       15 / 9
```

Two findings:

1. **Truth preservation is FLAT across capability** (16% → 20% → 21%). Going from a small
   model to the strongest available barely moves how much of the society holds the current
   truth. **You cannot scale your way out of social truth-decay.** This passes the de-risk:
   the phenomenon is NOT a weak-model artifact; it survives capability.

2. **Bonus, non-obvious result — capability shifts the FAILURE MODE, not the failure.** As
   capability rises, `stale` jumps (2.3 → 9 → 10) and Saturday-dominance among receivers
   rises (8 → 16 → 15). Weak models fail by FORGETTING (the update is lost → `unknown`);
   strong models COMMIT — but commit to the stale corruption attractor. i.e.
   **scaling the model makes the society more confidently WRONG, not more right.** (e.g.
   gpt-5.5 seed 41 = 16/25 stale, seed 43 = 14/25 stale — hard convergence on the
   superseded Saturday plan.)

Sub-observation: receiver counts (how far the update reaches at all) are similar-to-lower
for stronger models (Σ 29 → 27 → 26) — stronger agents are terser/less repetitive, so the
update is repeated less and reaches no further; capability does not buy wider faithful
reach either.

Caveats (honest): n=3, single scenario, single connectivity, GA-reflection only; the
`current/stale` verdict is still the SMGA keyword metric (the cleaner Sat/Sun-dominance
provenance signal agrees, so the conclusion is robust to that). Next: M1 — full
(capability × connectivity) phase diagram with more seeds + CIs and the pre-registered
fidelity metric; this M0 already shows the capability axis alone does not save the society.

---

# M1 — (capability × connectivity) phase diagram (2026-06-19)

3×3 grid: capability {mini, gpt-5.4, gpt-5.5} × connectivity meetings {1,2,3}, GA agents,
25a r5 t3, seeds 41-43 (n=3). meetings=2 reuses M0. Cell = mean current/25, mean stale,
and receiver Saturday-dominant : Sunday-dominant (Σ over 3 seeds).

```text
meetings |        mini          |       gpt-5.4         |       gpt-5.5
   1     | cur2.7 sta5.0 13:10  | cur7.0 sta4.3  9:10   | cur4.0 sta11.7 18:6
   2     | cur4.0 sta2.3  8:8   | cur5.0 sta9.0 16:9    | cur5.3 sta10.0 15:9
   3     | cur5.3 sta4.3 18:13  | cur7.0 sta9.7 52:5    | cur5.3 sta9.7  28:6
```

Sat:Sun dominance ratio among receivers (the clean corruption signal):
```text
meetings |  mini  | gpt-5.4 | gpt-5.5
   1     |  1.3   |  0.9    |  3.0
   2     |  1.0   |  1.8    |  1.7
   3     |  1.4   | 10.4    |  4.7
```

Findings:
1. **No truth-winning regime.** current-rate is 11%–28% across the ENTIRE grid (best 7/25).
   In no tested (capability × connectivity) does the society hold the truth. This is starker
   than a "phase boundary": the corruption regime fills the whole tested space.
2. **Connectivity AMPLIFIES corruption** (hypothesis B, not the redundancy-as-error-
   correction hypothesis A). The Saturday:Sunday dominance ratio EXPLODES with connectivity
   for strong models (gpt-5.4: 0.9× → 1.8× → 10.4× as meetings 1→3; gpt-5.5: → 4.7×). More
   communication spreads the STALE version wider, not the truth. "More communication, less
   truth" (echo-chamber / repetition reinforcement).
3. **Combined with M0** (capability → confident corruption): neither scaling the model NOR
   increasing connectivity preserves truth — both push the society harder into the stale
   corruption attractor.

Implication for the thesis: C2 reframes from "a boundary between truth and corruption
regions" to "the corruption regime dominates the entire (capability × connectivity) space,
intensifying along both axes." This makes C4 (a minimal corrective intervention) the
pivotal question — if scale and connectivity both fail, what (if anything) restores truth?

Caveats: n=3, single scenario, GA memory, coarse 3×3; current-rate is noisy (the receiver
Saturday-dominance is the cleaner signal); the 5.4 meetings=3 52:5 is striking but needs
CIs. Next: more seeds + CIs on the connectivity-amplifies-corruption result; then M2
(corruption taxonomy) and M3 (does ANY intervention move the needle — the real test).
