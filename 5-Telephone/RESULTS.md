# Telephone — results

## Experiment ledger (RULE: every run gets a row here — even small/failed ones)

| date | id | what | key config | headline result | status |
|---|---|---|---|---|---|
| 06-19 | M0 | DE-RISK capability ladder mini→gpt-5.4→gpt-5.5 | GA mem, 25a m2 r5 t3, seeds 41-43, n=3 | DE-RISK PASSES: current FLAT 16%→20%→21%; scaling does NOT fix decay — it converts forgetting into CONFIDENT corruption (stale 2.3→9→10; Sat-dom 8→16→15) | done |

> Origin evidence (from the parent project) motivating Telephone:
> `../3-SMGA/sim/RESULTS.md` → **S5L-diag** (weak-model diffusion corrupts a fact-update;
> seed 41: 18/22 "receivers" were Saturday-dominant — stale-persistence + detail drift).

| 06-19 | M1 | (capability × connectivity) phase diagram | GA, 25a r5 t3, 3×3, seeds 41-43 | CORRUPTION EVERYWHERE: current ≤28% in all cells; connectivity↑ AMPLIFIES corruption (5.4 Sat:Sun 0.9×→10.4× as meetings 1→3). Neither capability nor connectivity saves truth | done |

| 06-19 | M2 | MEMORY AXIS raw/ga/smga/smga3g | mini, 25a m2 r5 t3, n=3 | smga3g cur 56% — **NOT REPLICATED** (see M3, was n=3 outlier). Real signal: smga3g relays Sunday more in conversations, but it does NOT lift truth-recall | done(superseded) |

| 06-19 | M3 | VERIFY smga3g flip: ga vs smga3g × meetings{2,3} | mini, 25a r5 t3, n≈4-5 | M2 FLIP DID NOT REPLICATE: smga3g current ≈ ga (Δ -1.0 @m2, +3.7 @m3, both ns). Dissociation: smga3g relays Sunday in streams (m2 Sat:Sun 4:28) but truth-recall unchanged. Memory does NOT robustly fix corruption | done |

| 06-19 | M4 | AUTHORITATIVE RE-BROADCAST (C4 closure) + dissociation | GA, mini, 25a m2 r5, n=5 | source re-broadcast FAILS (Δ+0.8 ns) though it flips what agents SAY (Sun:Sat 25:5 by r5); only brute BROADCAST (inject all/round) works (99%, +21.8 SIG) = spoon-feeding, bypasses society. DISSOCIATION proven: speech≠belief; collective belief is sticky | done |

| 06-19 | G1 | GENERALITY (P1): M4 dissociation on 2 NEW scenarios | GA mini m2 r5 n=5, book_club + carpool | REPLICATES across all 3 scenarios: source FAILS (Δ ns ×3) despite flipping SAID; broadcast WORKS (Δ SIG ×3 →~25/25). Single-scenario-artifact attack DEAD | done |

| 06-19 | P1-mech | DISSOCIATION MECHANISM (P4): heard-ratio vs recency | analysis of M4+G1 (0-API) | dose-response real (held rises with heard cur-frac, →95%) BUT mean ratio similar across baseline/source/broadcast (0.64/0.72/0.73) w/ opposite outcomes → naive ratio REFUTED; points to RECENCY | done |
| 06-19 | P1-rec | RECENCY test: broadcast at LAST round only vs baseline vs every-round | repair_drive GA mini m2 r5 n=5 | does a single fresh broadcast right before the probe suffice (=recency) or not? | RUNNING |

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

---

# M2 — MEMORY AXIS: is the corruption GA's fault, or fundamental? (2026-06-19)

The human asked whether the truth-decay is a GA-reflection artifact or something deeper.
We added MEMORY as a third axis (the others held at mini, meetings=2, r5, seeds 41-43, n=3)
and compared raw / GA-reflection / SMGA-v2 (currency facts) / SMGA-v3-general (smga3g,
scenario-agnostic currency extractor, NO scenario-value anchor). Cell = mean current/25,
stale, unknown, and receiver Saturday-dom : Sunday-dom (Σ over 3 seeds — measured on the
agents' event STREAMS, i.e. what they heard, independent of the interview metric).

```text
memory   current     stale  unknown   receiver Sat-dom : Sun-dom
raw      3.3/25       1.0    20.7      4 : 15     (doesn't corrupt, but barely spreads)
ga       5.0/25       3.0    17.0     17 : 13     (corrupts — relays stale)
smga v2  7.7/25      11.7     5.7     41 : 17     (spreads stale WIDELY — worst corruption)
smga3g  14.0/25       0.0    11.0      4 : 19     (relays the TRUTH — flips the society)
```

Finding (SURPRISING — partially overturns the M0/M1 "nothing saves truth" reading):
**memory architecture is a powerful lever.** raw (no reflection compression) does not
corrupt but barely propagates; GA-reflection and SMGA-v2 actively CORRUPT (their agents
relay the stale Saturday version, v2 widest); but **smga3g (a currency-resolving memory)
FLIPS the society from corruption-convergence to truth-convergence** — current 56% vs GA's
20%, ZERO stale, and the society's conversations become Sunday-dominant (19 vs 4). The
Sunday-dominance is measured on event streams (what agents said to each other), so it is a
real **anti-entropy relay** effect, not an interview-keyword artifact.

So the answer to "is it GA's fault?": substantially YES + more — reflection/free-text
memory (ga, v2) is a corruption SOURCE; raw is inert; and a currency-resolving memory
(smga3g) is a genuine CURE (a working C4). The decay is NOT a fundamental, memory-
independent property of agent societies; the memory architecture largely determines
truth- vs corruption-convergence.

CAUTION (we have been burned by smga3g before): this CONTRADICTS the 3-SMGA finding that
smga3g ≈ GA (S5kg/S5L). The difference is plausibly live-coupling + different seeds (41-43)
+ n=3 noise. Before building on it: (a) re-run with n≥6 seeds + CIs; (b) audit that smga3g
is genuinely relaying (inspect conversations/registry), not exploiting the keyword metric;
(c) re-interpret M0/M1 — those used GA memory, so "nothing saves truth" was GA-specific.

---

# M3 — VERIFY the smga3g flip (and it does NOT replicate) (2026-06-19)

M2 (n=3) showed a dramatic smga3g flip (current 56% vs ga 20%). We were rightly skeptical
(smga3g has fooled us before). Verification: ga vs smga3g × meetings{2,3}, mini, n≈4-5
(some runs lost to the runtime cap; n unequal). current/25 mean [95% CI], receiver Sat:Sun:

```text
meetings=2   ga      current 4.2/25 [1.5,6.9]   receivers 58:  Sat 22 / Sun 23   (n=5)
             smga3g  current 4.0/25 [1.1,6.9]   receivers 38:  Sat  4 / Sun 28   (n=4)
             Δ(smga3g-ga) = -1.0/25  95% CI [-4.9,+2.9]  ns
meetings=3   ga      current 3.0/25             receivers 32:  Sat 17 / Sun 12   (n=3)
             smga3g  current 6.0/25 [0.3,11.7]  receivers 81:  Sat 35 / Sun 36   (n=4)
             Δ(smga3g-ga) = +3.7/25  95% CI [-10.5,+17.8]  ns
```

Findings:
1. **The M2 smga3g flip (56%) did NOT replicate.** At n=4-5, smga3g current ≈ ga (~16%),
   Δ not significant at either connectivity. The M2 14/25 was an n=3 lucky draw. (The
   discipline — verify a surprising result before building on it — paid off; smga3g fooled
   us again, and we caught it.)
2. **Real but weaker signal — a DISSOCIATION.** smga3g does make the conversation streams
   more Sunday-dominant at meetings=2 (Sat:Sun 4:28 vs ga 22:23) — agents DO relay "Sunday"
   more. But this does NOT translate into higher interview truth-recall (current unchanged).
   Memory changes what agents SAY without changing what the society HOLDS.
3. So memory architecture does NOT robustly restore truth. The pendulum swings back toward
   the M0/M1 reading: the corruption is substantially fundamental (transmission bottleneck +
   network evidence dynamics), not fixable by a memory swap. Consistent with 3-SMGA's prior
   (smga3g ≈ GA).

Implication: retract M2's "memory fixes it / C4 works" narrative. Honest current thesis:
truth-decay in agent societies is robust — scaling capability doesn't fix it (M0), more
connectivity worsens it (M1), and swapping the memory architecture doesn't fix it either
(M3). The dissociation (memory shifts speech but not collective belief) is itself an
interesting sub-finding worth pinning down. Caveat: M3 n is small/unequal (runtime-cap
losses); a clean n≥8 rerun would tighten it, but the non-replication is already clear.

---

# M4 — authoritative re-broadcast (C4 closure) + the dissociation, proven (2026-06-19)

The last untested lever and the sharpest sub-finding, in one experiment. GA agents, mini,
meetings=2, r5, n=5. Three conditions: baseline (one-time update at round 1); SOURCE
(the source agent a01 re-announces the truth every round — a realistic, minimal
intervention: a designated authoritative source / moderator / ground-truth oracle); and
BROADCAST (the update is injected into EVERY agent every round — a heavy-handed positive
CONTROL / upper bound, not a realistic cure: it bypasses the social dynamics by overwriting
everyone's memory directly). We also instrument the DISSOCIATION: per-round Sunday:Saturday
counts in what agents SAY (utterances), vs the final HELD belief (interview).

```text
cond       current/25 [95%CI]  stale  unknown  said Sunday:Saturday by round (r1..r5)
baseline   3.0 [0.7,5.3]        3.0    19.0     0:9   0:18  10:18  18:26  18:14
source     3.8 [2.4,5.2]        0.6    20.6     0:13  0:13  10:11  12:4   25:5
broadcast  24.8 [24.2,25.4]     0.0     0.2     0:11  0:28  190:4  210:8  221:3
Δ(source-baseline)    current  +0.8  95% CI [-1.4,+3.0]  ns
Δ(broadcast-baseline) current +21.8  95% CI [+19.1,+24.5]  SIGNIFICANT
```

Findings:
1. **A realistic authoritative source FAILS to restore held belief** (source Δ +0.8, ns) —
   even though it visibly changes what the society SAYS: by round 5 utterances are
   Sunday-dominant 25:5. So a persistent truth-teller flips the society's SPEECH but not its
   HELD belief (current stays ~3.8/25, unknown 20.6). **The dissociation, crisp.**
2. **Only brute-force BROADCAST works** (99% current) — but only by injecting the truth into
   every agent every round, i.e. directly overwriting each memory and BYPASSING the social
   dynamics. That is spoon-feeding, not an emergent cure (a positive control / upper bound,
   exactly the heavy-handed override one should be skeptical of).
3. **Mechanism — collective belief is STICKY beyond speech.** Interventions readily move
   what agents utter; the society's held belief is anchored by the network evidence-ratio
   (the entrenched stale version), so it does not follow speech. Speech ≠ belief.

This CLOSES C4 honestly: truth-decay in agent societies resists every realistic lever
(capability M0, connectivity M1, memory M2/M3, authoritative re-broadcast M4-source); only
bypassing the society (M4-broadcast) "works". The DISSOCIATION (say ≠ hold; collective
belief is sticky) is the paper's sharpest mechanistic claim and is now directly demonstrated
with tight CIs.

Caveats: n=5, single scenario, GA memory, keyword metric; the said-ratio is a coarse proxy.
But the source-fails / broadcast-works contrast and the speech-vs-belief gap are large and
clean. Next (for resume): pin the dissociation mechanistically (where does belief get
anchored?), provenance fidelity metric, ≥2 scenarios.

---

# G1 — GENERALITY: the dissociation replicates on 2 new scenarios (2026-06-19)

P1 (the #1 publishability gap): is the M4 dissociation a one-scenario artifact? Replicated
baseline / source-rebroadcast / broadcast on two structurally-identical but surface-different
scenarios (GA, mini, meetings=2, r5, n=5): **book_club** (Tuesday@library → Thursday@cafe)
and **carpool** (7am@school → 8am@church). current/25 mean [95% CI]; SAID = utterance
current:stale counts by round.

```text
scenario       baseline cur   source cur (Δ vs base)        broadcast cur (Δ)        source SAID by round
repair_drive*  3.0            3.8  (+0.8  ns)               24.8 (+21.8 SIG)         flips Sun, holds stale
book_club      9.6 [7.5,11.7] 12.8 (+3.2  ns) [-0.9,+7.3]   24.8 (+15.2 SIG)         48:19→161:53 (Thu≫Tue)
carpool        3.2 [1.2,5.2]  4.0  (+0.8  ns) [-1.2,+2.8]   25.0 (+21.8 SIG)         …→42:0 (8am only)
```
(* repair_drive = the M4 reference.)

Finding: **the dissociation generalizes.** In all THREE scenarios:
1. a persistent authoritative SOURCE fails to restore held belief (Δ ns everywhere) — even
   though it visibly flips what agents SAY (book_club utterances Thursday≫Tuesday; carpool
   agents say "8am" and essentially never "7am");
2. only brute BROADCAST works (Δ significant everywhere, → ~25/25);
3. so speech ≠ collective belief, robustly, beyond the original scenario.

This kills the #1 reviewer attack (single-prompt artifact). Note the baseline corruption
LEVEL varies by scenario (book_club holds more truth at baseline, 9.6/25, vs repair/carpool
~3/25) — the absolute decay is scenario-dependent, but the INTERVENTION pattern (source-fails
/ broadcast-works / say≠hold) is invariant. Carpool is the cleanest dissociation: agents say
the new "8am" almost exclusively yet hold it only 4/25 (the stale value isn't even repeated —
the failure there is non-retention, not stale-persistence, yet source still can't fix it).

Toward publication (path_to_publication.md): P1 generality — DONE for the dissociation spine
(3 scenarios). Remaining: capability(M0)/connectivity(M1) on ≥2 scenarios; provenance/judge
metric (P2); mechanism localization of the dissociation (P4); n≥8 symmetric (P3).

---

# P1-mech (P4 first cut) — mechanism of the dissociation: ratio vs RECENCY (2026-06-19)

Zero-API analysis of M4+G1 data (repair_drive/book_club/carpool × baseline/source/broadcast).
For each agent: HEARD current:stale fraction (from its event stream) vs HELD verdict.

Dose-response (pooled): held-current rises with the agent's heard-current fraction —
[0,0.2)→0% · [0.2,0.4)→11% · [0.4,0.6)→40% · [0.6,0.8)→95%. So at the INDIVIDUAL level the
heard evidence ratio matters.

BUT the naive "held = f(mean heard ratio)" hypothesis is REFUTED at the population level:
mean heard-current-fraction is similar across baseline (0.64), source (0.72), broadcast
(0.73) — yet held-current is low/low/99%. Similar ratio, opposite outcome ⇒ the MEAN ratio
does not explain why source fails and broadcast works.

Refined hypothesis → RECENCY: broadcast re-injects the truth every round INCLUDING the last
(right before the probe), so the truth is what agents heard most RECENTLY, and GA retrieval
is recency-weighted. The dissociation may be governed by the recency/freshness of the last
authoritative mention, not the cumulative ratio. Discriminating test (P1-rec, launched): a
SINGLE broadcast at the LAST round vs baseline (single broadcast at round 1) vs every-round.
If last-round-only ≈ every-round ⇒ RECENCY; if last-round-only fails ⇒ cumulative/threshold.
