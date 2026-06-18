# Telephone — results

## Experiment ledger (RULE: every run gets a row here — even small/failed ones)

| date | id | what | key config | headline result | status |
|---|---|---|---|---|---|
| 06-19 | M0 | DE-RISK capability ladder mini→gpt-5.4→gpt-5.5 | GA mem, 25a m2 r5 t3, seeds 41-43, n=3 | DE-RISK PASSES: current FLAT 16%→20%→21%; scaling does NOT fix decay — it converts forgetting into CONFIDENT corruption (stale 2.3→9→10; Sat-dom 8→16→15) | done |

> Origin evidence (from the parent project) motivating Telephone:
> `../3-SMGA/sim/RESULTS.md` → **S5L-diag** (weak-model diffusion corrupts a fact-update;
> seed 41: 18/22 "receivers" were Saturday-dominant — stale-persistence + detail drift).

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
