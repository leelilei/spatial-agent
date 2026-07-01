# Telephone — results

> Data locations per experiment: docs/project/data_index.md  ·  rationale: docs/project/decisions.md

## Experiment ledger (RULE: every run gets a row here — even small/failed ones)

| date | id | what | key config | headline result | status |
|---|---|---|---|---|---|
| 06-19 | M0 | DE-RISK capability ladder mini→gpt-5.4→gpt-5.5 | GA mem, 25a m2 r5 t3, seeds 41-43, n=3 | DE-RISK PASSES: current FLAT 16%→20%→21%; scaling does NOT fix decay — it converts forgetting into CONFIDENT corruption (stale 2.3→9→10; Sat-dom 8→16→15) | done |

> Origin evidence (from the parent project) motivating Telephone:
> `../3-SMGA/sim/RESULTS.md` → **S5L-diag** (weak-model diffusion corrupts a fact-update;
> seed 41: 18/22 "receivers" were Saturday-dominant — stale-persistence + detail drift).

| 06-19 | M1 | (capability × connectivity) phase diagram | GA, 25a r5 t3, 3×3, seeds 41-43 | corruption everywhere (current ≤28%); 'connectivity AMPLIFIES corruption' (10.4×) **NOT REPLICATED** (P3b: ratio ~1.0 at n=3-4) → connectivity is NEUTRAL, not amplifier. Neither capability nor connectivity SAVES truth | done(tempered) |

| 06-19 | M2 | MEMORY AXIS raw/ga/smga/smga3g | mini, 25a m2 r5 t3, n=3 | smga3g cur 56% — **NOT REPLICATED** (see M3, was n=3 outlier). Real signal: smga3g relays Sunday more in conversations, but it does NOT lift truth-recall | done(superseded) |

| 06-19 | M3 | VERIFY smga3g flip: ga vs smga3g × meetings{2,3} | mini, 25a r5 t3, n≈4-5 | M2 FLIP DID NOT REPLICATE: smga3g current ≈ ga (Δ -1.0 @m2, +3.7 @m3, both ns). Dissociation: smga3g relays Sunday in streams (m2 Sat:Sun 4:28) but truth-recall unchanged. Memory does NOT robustly fix corruption | done |

| 06-19 | M4 | AUTHORITATIVE RE-BROADCAST (C4 closure) + dissociation | GA, mini, 25a m2 r5, n=5 | source re-broadcast FAILS (Δ+0.8 ns) though it flips what agents SAY (Sun:Sat 25:5 by r5); only brute BROADCAST (inject all/round) works (99%, +21.8 SIG) = spoon-feeding, bypasses society. DISSOCIATION proven: speech≠belief; collective belief is sticky | done |

| 06-19 | G1 | GENERALITY (P1): M4 dissociation on 2 NEW scenarios | GA mini m2 r5 n=5, book_club + carpool | REPLICATES across all 3 scenarios: source FAILS (Δ ns ×3) despite flipping SAID; broadcast WORKS (Δ SIG ×3 →~25/25). Single-scenario-artifact attack DEAD | done |

| 06-19 | P1-mech | DISSOCIATION MECHANISM (P4): heard-ratio vs recency | analysis of M4+G1 (0-API) | dose-response real (held rises with heard cur-frac, →95%) BUT mean ratio similar across baseline/source/broadcast (0.64/0.72/0.73) w/ opposite outcomes → naive ratio REFUTED; points to RECENCY | done |
| 06-19 | P1-rec | RECENCY vs ENTRENCHMENT: r1-broadcast vs r5-broadcast | repair_drive GA mini m2 r5 (n=5) | **RETRACTED 2026-06-30:** raw logs show r5 injected into 0 agents in every run (round-index bug). Correct last-round index=4 rerun gives 25/25 current. This experiment does not establish entrenchment or refute recency. | retracted(config invalid) |

| 06-19 | P3 | POWER: M0 capability n=8/5 + M1 connectivity n=8 (mini) with CIs | GA, 25a r5 | TEMPERS n=3 claims: M0 capability gives MODEST bump (mini 18%→strong ~32%) but recall stays ≤34% (scale doesn't solve it); M1 connectivity on MINI ~null (ratio 0.8-1.1) — the dramatic 10× was strong-model-only (n=3), confirming w/ P3b | done |
| 06-19 | P3b | confirm M1 connectivity on gpt-5.4 (n=5) | GA 25a r5 meetings{1,3} | does connectivity amplify corruption on a STRONG model (the n=3 52:5 cell)? | RUNNING |

| 06-19 | P2 | METRIC VALIDATION: LLM-judge (semantic) vs keyword on M4 | repair_drive, 375 answers | keyword↔judge agree 99-100%; judge current = keyword current exactly (baseline 3.0, source 3.8, broadcast 24.8). Metric is NOT a keyword artifact; dissociation holds under semantic judge | done |

| 06-20 | G2 | PERSONA-DEPTH robustness (vs Park 2024): thick personas | repair_drive GA mini m2 r5 n=5, baseline/source/broadcast | YES, IDENTICAL to thin: baseline 14% (vs 12%), source 12% (vs 15%, still ≈baseline = dissociation holds), broadcast 98% (vs 99%). Persona depth is NOT a lever; 'thin-persona artifact' critique DEAD; mechanism confirmed structural | done |

| 06-20 | M5 | LONG-HORIZON decay trajectory (Fig 2): per-round interview, r30 | repair_drive GA mini m2, baseline n=2 / source n=1 / broadcast n=1 | truth RISES to peak ~28% @ r6 then DECAYS to ~6% by r30; authoritative SOURCE also decays (36%→4%, converges to baseline); only BROADCAST sustains (~97%). r5 was a near-PEAK transient → r5 snapshots slightly OVER-state steady-state truth | done |

| 06-21 | C1 | CURE de-risk: PROVENANCE-aware integration vs GA | repair_drive mini m2 r5 n=5, prov vs ga | PROV **HOLD 18%->58%** (~3.2x), unknown 91->18/125; first NON-OVERWRITE lever that works (broadcast=99% upper bound). Strong but variant (seed42 no move). Provenance integration breaks entrenchment | de-risk PASS |

| 06-21 | C2 | CURE validation: PROV vs GA, power n=8 + source + r30 | repair_drive mini m2, n=8 (r5) / n=3 (r30) | PROV ~2x GA: baseline 40%[28-53] vs 22%[13-30]; **closes dissociation**: source GA 21 (dead) vs PROV 51[37-65]; unknown 68%->28%; **r30: PROV sustains ~55% (flat, no decay) while GA decays to 6%**. PROV=first non-overwrite cure | done |

| 06-21 | C3 | FAIR (generalized) PROV: origin/version metadata propagation vs GA | repair_drive mini m2 r5 n=8 | **fair-PROV 57% [49-65] vs GA 22% [13-30]** (~2.6x, CIs DISJOINT); unknown 68%->40%; **8/8 seeds improve**; provenance carried as event metadata, NOT hardcoded answer. CURE survives fair impl (stronger+cleaner than marker version's 40%) | done |

| 06-22 | C5 | ARCHITECTURE TABLE (repair_drive) + PROV HORIZON climb | mini m2, 7 memories n=8 + PROV r5/r10/r20 | **All recognized memories fail** (Raw14 Mem0-18 A-MEM19 GA22 GA-curr25 MemBank25); **PROV 57 alone**. **PROV climbs with propagation time: r5 57 -> r10 93 -> r20 100%** (unk 40->7->0); GA stays ~20/decays. Cure CLOSES the gap to overwrite ceiling, decentralized, no verifier | done |

| 06-22 | C5-stress | PROV LOSSY-CHANNEL stress test (the 100% danger signal) | repair_drive mini r10, prov_loss/garble {0.3,0.6,0.9} n=5 | DROP robust (0.3->100 0.6->93 0.9->26); GARBLE graceful-degrade (0.3->74 0.6->42 0.9->24) — beats GA(22) until severe. **Cure NOT a pure channel artifact: survives heavy drop + moderate value-corruption; depends on value fidelity (limitation)** | done(garble n=4-5) |

| 06-22 | C6 | PROV-v2 (corroboration + Ebbinghaus decay) — both upgrades FAIL | repair_drive mini r10/r20 n=3-5 | clean still 99-100% (decay never fires: re-broadcast reinforces every round); **garble0.6 -> 7% (93% STALE, WORSE than PROV 42 & GA 22)**: corroboration backfires (systematic garble corroborates the STALE value too). Lessons: 100%-lock is a COMMS-MODEL artifact (every-round re-broadcast), not memory; corroboration defends a lone liar not a noisy channel | done(neg) |

| 06-22 | C7 | SPARSE COMMS (fix every-round broadcast): prov_mention sweep | repair_drive mini r10 n=5, provv2 mention {1.0,0.3,0.1} | The 100% lock was a COMMS-MODEL artifact: with sparse mention + Ebbinghaus decay, v2 settles to a real EQUILIBRIUM — mention 1.0->99, 0.3->96, **0.1->40 [~] (stale 0, ~2x GA 22)**. Decay only bites once comms are sparse enough; provenance still beats frequency under realistic sparse comms | done(v2m01 n=4-5) |

| 06-22 | C8 | GENERALITY: architecture table across 3 scenarios | {ga,prov,smga3g,amem} x {book_club,carpool} mini m2 r5 n=5 (+ repair_drive from C5) | **PROV is #1 in ALL 3 scenarios**: repair_drive 57 vs GA22; book_club 69 vs GA47/A-MEM52; carpool 59 vs GA18. Cure generalizes; single-scenario-artifact attack DEAD | done |

| 06-22 | C9 | FACT-TYPE generality: NUMERIC correction (dues $40->$60) | dues mini m2 r5 n=5, {ga,prov,smga3g,amem} | **PROV 59 [49-69] leads** > GA 28 > A-MEM 25 > GA-curr 7. Cure works on a numeric fact change, not just day/place reschedule -> not a fact-type artifact | done |
| 06-22 | C10 | TOPOLOGY robustness: GA vs PROV on ring/smallworld | repair_drive mini m2 r10 n=5 | **PROV >> GA on every topology**, gap LARGER on structured nets: random GA22/PROV93; ring GA6/PROV68; smallworld GA10/PROV83. GA collapses on slow nets, PROV's sticky propagation still spreads -> not a single-topology artifact | done |
| 06-22 | C11 | PROV-text mechanism probe (deterministic text relay) | repair_drive mock context relay, 25a r10 m1 n=5, raw/prov/provtext | If utterances explicitly preserve `Official round 1 update`, PROV-text reaches 125/125 current without hidden `prov` payload. Mechanism feasible, but probe is scripted/text-normed, not natural dialogue | done |
| 06-22 | C12 | PROV-text-free real LLM dialogue | repair_drive gpt-5.4-mini, 25a r10 m1 t2, provtext n=3 (+ GA/PROV partial comparator) | **Natural dialogue drops source/version**: PROV-text-free 16/75 current, 0 stale, 59 unknown; source/version phrase mentions 0/720; only a01/Rosa holds version>=1. Structured PROV remains upper bound; next target = PROV-text-norm | done(neg; stopped after signal) |
| 06-23 | C13 | PROV-text-norm strong attribution dialogue | repair_drive gpt-5.4-mini, 25a r10 m1 t2, provtextnorm n=3 | **Strong text attribution repairs held truth: 75/75 current, 0 stale, 0 unknown.** Audit: 610/720 utterances contain source/version-like markers; 75/75 memory snapshots hold version>=1. Caveat: this is a protocolized attribution norm / text-only upper bound, not natural human dialogue | done(strong-norm upper bound) |
| 06-23 | C14 | CAPABILITY CHECK ON THE CURE: PROV vs GA on a NON-mini model (DeepSeek-V4-Flash, yunwu.ai) | repair_drive deepseek-v4-flash, 25a m2 r5 t3, {ga,prov} **n=8** (seeds 41-48) | **The CURE survives capability (n=8, CIs DISJOINT): PROV 64.0% [57.8-70.2] (median 62) vs GA 15.5% [10.1-20.9] (median 14).** Mirrors M0: GA stays low on a new model family (ds 15.5 ≈ mini median 18, CIs overlap → phenomenon survives capability); PROV wins decisively, slightly WIDER than mini (ds 64 vs mini 57). n=8 corrects the n=3 over-estimate (was PROV 70.7/GA 17.3 on the first 3 high seeds). Pooled across pilot+n8ext+n8fill+seed44 dirs | **done(n=8)** |
| 06-24 | C15 | APM (Auditable Provenance Memory): does adding anti-spoof + corroboration + abstain + auditability to PROV preserve the cure? | repair_drive deepseek-v4-flash, 25a m2 r5 t3, memory=apm n=3 (seeds 41-43); K={1,2} | **APM K=1 ≈ PROV, cure preserved + interpretable: 64.0% (48/75) vs PROV 70.7% vs GA 17.3%; per-seed [56-76].** Failure mode is SAFE (abstain: unknown 20, stale 7 — not confidently wrong like GA). **Auditability real:** 60-76% of agents hold a belief with a COMPLETE provenance chain to ORIGIN (avg 3.2 hops); rest abstain. Anti-spoof unit-tested (liar's unauthenticated high-version rejected). **APM K=2 (commit-gated) DEADLOCKS: 12% (worse than GA) — only origin commits; auth can't bootstrap because abstaining agents don't relay.** -> multi-source corroboration needs relay-before-commit (next). Lesson: interpretability+spoof-resistance cost ~7pts vs PROV; K knob dials flood(K1)<->over-conservative(K2-gated) | done(n=3 pilot) |
| 06-25 | C16 | ADVERSARIAL-LIAR robustness (the test that justifies APM as an architecture): one agent broadcasts a FORGED high-version stale claim (auth=False). PROV vs APM(K=1) | repair_drive gpt-5.4-mini (FHL; yunwu/ds was 429-overloaded), 25a m2 r5 t3, adversary=a13 from r2, n=3 (seeds 41-43) | **Only APM survives the attack. APM 64.0% [60-72] held-current with STALE=0 (ZERO hijack); PROV 33.3% [24-40] with STALE=43/75 (mass hijack).** vs no-adversary baseline (PROV 57% mini / APM≈PROV): the liar collapses PROV (57->33, 43 agents believe the forgery) but APM is UNMOVED (≈64, unchanged). Audit: 15-18/25 APM agents hold a committed belief, 0 contaminated by the forged v999 — anti-spoof holds society-wide, not just in the unit test. Mechanism unit-tested separately (PROV adopts forgery, APM rejects). This is APM's unique value: ≈PROV without an adversary, the ONLY one standing with one. ds cross-check (seed41): PROV adv 36% (consistent) | **done(n=3)** |
| 06-25 | C17 | APM realistic-friction EQUILIBRIUM (the saturation check, pre-registered): does APM settle to a stable <100% equilibrium under sparse comms + long horizon, or flood to 100%? | repair_drive gpt-5.4-mini (FHL), 25a m2 **r10**, **--prov-mention 0.1**, apm(K=1) vs ga, **n=8** (seeds 41-48) | **APM does NOT saturate: settles to 40.5% [27.2-53.8] (median 44), STALE=0/200.** vs GA 21.5% [14.7-28.3], stale 30/200. Two honest reads: (1) saturation check PASSES decisively — 40.5% is far from the 100% comms-artifact ceiling (C7), a healthy sub-100% equilibrium under realistic sparse comms. (2) The held-current edge over GA (~1.9x) is SUGGESTIVE not decisive — high APM variance (std 19) under sparse comms makes the 95% CIs marginally overlap at n=8. **The DECISIVE difference is quality: APM stale=0 vs GA stale=30 (disjoint).** Takeaway: under hard sparse comms nobody spreads truth widely (breadth gap shrinks), but APM guarantees the informed are never misled (zero error), GA does not. | done(n=8) |
| 06-26 | C17b | APM communication-sufficiency CURVE (n=5): held-current vs mention probability | mini r10, apm K=1, 11 points (mention 0->0.8), n=5 (0.1 is n=8) | **Smooth MONOTONIC S-curve: 11%(m=0) -> 16(0.03) -> 23(0.05) -> 38(0.07) -> 40(0.1) -> 49(0.15) -> 74(0.2) -> 87(0.25) -> 87(0.3) -> 100(0.5,0.8). STALE==0 everywhere.** n=5 RESOLVES the n=3 reversal: 0.25 & 0.3 converge to 87% (the saturating-knee plateau) -> curve now fully monotonic. mention=0 MEASURED at 11% (not clean 4%: dialogue TEXT leaks truth even with the provenance channel off). No propagation threshold; 100% only at the unrealistic dense limit. -> Fig 9. | done(n=5) |

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
2. **Connectivity AMPLIFIES corruption** — ⚠ **RETRACTED (see P3b below): did NOT replicate
   at n=3-4 (Sat:Sun ratio ~1.0 at every connectivity); the 10.4× was an n=3 outlier.
   Connectivity is NEUTRAL, not an amplifier. Original text kept below for provenance.**
   (hypothesis B, not the redundancy-as-error-
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

---

# P1-rec — RETRACTED after configuration audit (2026-06-30)

> **Do not cite the original timing result.** Raw logs show that `r5_broadcast` performed zero
> injections in all five runs. The apparent late-broadcast failure was therefore a no-treatment
> condition. See `docs/project/p1_rec_audit_2026-06-30.md`.

The corrected last-round broadcast uses zero-based round index `4`. Under the original
25-agent / meetings=2 / rounds=5 / turns=3 / seed=41 configuration, a `forget_rate=0`
GA-equivalent rerun yields **25/25 current**. Late all-agent broadcast succeeds when it is
actually delivered. P1-rec does not distinguish recency from entrenchment.

<details>
<summary>Retracted original interpretation (kept only for audit history)</summary>

To distinguish the candidate mechanisms (cumulative ratio vs recency), a clean contrast:
the SAME single broadcast to ALL agents, differing only in TIMING. repair_drive, GA, mini,
meetings=2, r5.

```text
condition                              current/25
baseline (inject r1, SOURCE only=1 ag)   3.0
r1_broadcast (all hear @round 1 only)   25.0   <- early + broad → WINS
r5_broadcast (all hear @round 5 = last)  0.0   <- latest possible, all hear it → FAILS
every_broadcast (all, every round)      24.8
```
(r1/r5 broadcast n=2 here — jobs cut short; the effect is saturated [25,25] vs [0,0], so the
direction is certain; re-running to n=5 for the CI.)

RECENCY is REFUTED: the MOST RECENT broadcast (r5, right before the probe, heard by everyone)
yields 0/25, while the EARLIEST broadcast (r1) yields 25/25. The opposite of recency.

The mechanism is ENTRENCHMENT / PATH-DEPENDENCE, with two requirements visible in the
contrasts:
- TIMING: r1_broadcast (win) vs r5_broadcast (fail) — same dose, different timing. Establishing
  the truth EARLY lets it self-reinforce through subsequent conversation; a LATE injection
  cannot dislodge the stale version that has already entrenched over 4 rounds of repetition.
- BREADTH: baseline (r1, 1 agent, fail) vs r1_broadcast (r1, all, win) — same timing, different
  breadth. The truth must be established across the POPULATION; one persistent voice is not enough.

Deep "why" (the paper's mechanistic spine): the stale value is the ORIGINAL plan everyone knew
from the start — it is entrenched from round 0. The update arrives late and narrow (one agent
at round 1). The incumbent belief wins by path-dependence unless the correction matches its
breadth AND arrives before further entrenchment. This is why truth-decay is so robust, why a
persistent authoritative source fails (it is narrow and late relative to the entrenched
incumbent), and why only early+broad (or continuous) broadcast works. It resonates with the
first-mover-advantage / entrenchment dynamics in the misinformation literature — here
demonstrated cleanly in a controlled agent society.

### P1-rec confirmation (n=5/n=3)

```text
r1_broadcast (early, all):  current 24.8/25 [24.2,25.4]  n=5   ≈ every_broadcast (24.8)
r5_broadcast (last,  all):  current  3.3/25 [0.0,10.9]    n=3   ≈ baseline (3.0)
```

Two clean equalities nail the ENTRENCHMENT mechanism:
- **r1_broadcast ≈ every_broadcast** (24.8 ≈ 24.8): establishing the truth ONCE, EARLY, is as
  good as repeating it every round. You don't need to keep shouting — you need to be FIRST.
- **r5_broadcast ≈ baseline** (3.3 ≈ 3.0): a late broadcast to EVERYONE is worth no more than
  doing nothing. Late correction is worthless even at full breadth.
⇒ TIMING is decisive: early = total success, late = total failure, independent of breadth.
Pure first-mover / path-dependence. Recency definitively refuted.

</details>

---

# P2 — metric validation: semantic LLM-judge vs keyword (2026-06-19)

Addresses "your current/stale metric is surface-keyword / circular." Re-scored every M4
interview answer (repair_drive, baseline/source/broadcast, n=5, 375 answers) with an LLM
JUDGE that classifies current/stale/unknown by MEANING vs the scenario ground truth
(`judge_rescore.py`), and compared to the keyword verdict.

```text
condition   keyword↔judge agreement   keyword current/run   judge current/run
baseline    124/125 = 99%             3.0                   3.0
source      125/125 = 100%            3.8                   3.8
broadcast   125/125 = 100%            24.8                  24.8
```

The semantic judge agrees with the keyword metric at 99-100% and yields IDENTICAL headline
numbers. The dissociation (source 3.8 ≈ baseline; broadcast 24.8) is unchanged under the
judge. So the keyword current/stale metric is not a surface artifact — an independent
semantic judge confirms it. P2 (defensible metric) cleared for the headline. (A full
provenance-based "received" definition + multi-dimensional fidelity rubric remains for the
camera-ready, but the core verdict metric is validated.)

---

# P3 — POWER: M0/M1 with CIs (tempers the n=3 claims) (2026-06-19)

Re-ran the "failed lever" results at higher n with 95% CIs (GA, repair_drive, r5).

M0 — capability ladder (meetings=2):
```text
model       current/25 [95% CI]   n
mini        4.6  18% [3.0, 6.2]    8
gpt-5.4     8.6  34% [6.2,11.0]    5
gpt-5.5     7.6  30% [5.2,10.0]    5
```
Refinement vs the n=3 "completely flat (16→21%)": capability gives a MODEST improvement
(mini 18% → strong ~30-34%; CIs barely overlap), but truth-recall stays LOW (≤34%) — the
society never holds the truth. Honest claim: scaling helps a little but does NOT solve
social truth-decay (not "completely flat", but "modest bump, still fails").

M1 — connectivity (mini, meetings 1/2/3):
```text
meetings   current/25 [95% CI]   Sat:Sun ratio   n
1          4.9 [3.2,6.5]         0.8             8
2          4.6 [3.0,6.2]         0.8             8
3          3.5 [2.6,4.4]         1.1             8
```
Refinement: on MINI, connectivity does NOT amplify corruption (current flat-to-slightly-
down; Sat:Sun ratio ~0.8-1.1, nowhere near the n=3 10×). The dramatic "connectivity
amplifies corruption" (M1, gpt-5.4 meetings=3 = 52:5) was a STRONG-MODEL, n=3 effect.
P3b re-runs gpt-5.4 connectivity at n=5 to confirm or retract the "more communication, less
truth" claim before it goes in the paper.

Net: the SPINE (dissociation + entrenchment, M4/G1/P1-rec) is untouched and solid; P3 just
tempers the two supporting "failed lever" claims to their honest, CI-backed form.

---

# P3b — connectivity-amplifies-corruption does NOT replicate (M1 tempered) (2026-06-19)

The M1 (n=3) headline "more communication, less truth" rested on one dramatic cell: gpt-5.4
meetings=3 Sat:Sun = 52:5 (ratio 10.4). Re-ran gpt-5.4 connectivity with more seeds:

```text
gpt-5.4   meetings=1: current 5.8/25  Sat:Sun 14:16 (ratio 0.9)  n=4
          meetings=3: current 6.7/25  Sat:Sun 25:24 (ratio 1.0)  n=3
```

The amplification DOES NOT REPLICATE: at n=3-4 the Sat:Sun ratio is ~1.0 at BOTH
connectivities; the 10.4× was an n=3 outlier (one seed with extreme stale-dominance).
**RETRACT the "connectivity amplifies corruption / more communication, less truth" claim.**
What survives: current-rate stays LOW at every connectivity (5.8-6.7/25 ≈ 23-27%), so
connectivity does NOT fix truth-decay — but it is roughly NEUTRAL on the corruption level,
not an amplifier. (Third n=3 over-claim caught by the verify-before-build discipline, after
M2-smga3g and the M0 confident-corruption magnitude.) The paper's spine (dissociation +
entrenchment) is unaffected; M1 downgrades from "amplifies" to "does not help (neutral)."

---

# G2 — persona-depth robustness: does richer (Park-2024-style) persona change the decay? (2026-06-20)

**Motivation.** Park et al. 2024 ("1,000 People", arXiv:2411.10109) get high INDIVIDUAL
fidelity from rich, self-report-grounded personas. The obvious reviewer attack on us: our
agents have THIN one-line personas + GA-reflection, so maybe the truth-decay is a shallow-
agent artifact and richer agents would propagate faithfully. We added a `--persona-depth
thick` switch (25 scenario-agnostic, individuating 2-3-sentence personas: background +
temperament + how the person handles news + social role) and re-ran the M4 dissociation
triple (baseline / authoritative source re-broadcast / brute broadcast), repair_drive, GA,
mini, 25a, meetings=2, r5, n=5 — identical to M4 except persona depth.

```text
condition        thin persona (M4)     thick persona (G2)
baseline         3.0/25  (12%)         3.6/25  (14%)
source           3.8/25  (15%)         3.0/25  (12%)      <- still ≈ baseline (Δ ns)
broadcast       24.8/25  (99%)        24.6/25  (98%)
```

**Result: a clean null — persona depth changes nothing.** All three conditions land within
noise of their thin counterparts. (1) Decay persists: baseline truth-recall stays ~14%.
(2) The DISSOCIATION persists: a persistent authoritative source still fails to lift held
belief (source 12% ≈ baseline 14%), exactly as with thin personas — it flips what agents
SAY, not what the society HOLDS. (3) The broadcast control still works (~98%), so the
machinery is intact; only spoon-feeding every agent restores truth.

**Interpretation.** This kills the "thin-persona artifact" critique and, more importantly,
POSITIVELY confirms the mechanism is STRUCTURAL: truth-decay + the speech-belief dissociation
are properties of the collective propagation dynamics (path-dependent entrenchment / network
evidence-ratio), not of how rich any individual agent is. Individual fidelity (Park 2024) and
collective fidelity (ours) are genuinely orthogonal axes — making each agent a richer person
does not make the society a more faithful carrier of a fact-update. The entrenchment account
PREDICTED this (persona depth is not among timing/breadth, the decisive variables).

**Caveats.** "Thick" here = individuating multi-sentence personas, not a full Park-style
2-hour interview transcript per agent; a maximally rich self-report grounding is untested
(but the direction — more persona content, identical outcome — makes a reversal unlikely).
n=5, single scenario (repair_drive), mini, GA memory.

---

# M5 — long-horizon decay trajectory (Fig 2) (2026-06-20)

**Motivation (raised by the human).** All prior experiments interview only at the END of a
short run (r5). Is r5 the steady state, or a transient? For a real *decay curve* we added a
per-round interview hook (`--interview-every-round`; verified read-only — `interview()` only
calls `memory.retrieve`, so it does NOT contaminate the run) and ran to r30. Per-round
interviewing over 30 rounds is heavy (~2-3 min/round late, GA context grows), so: baseline
n=2, source n=1, broadcast n=1 (the trajectory needs SHAPE; end-state CIs already exist at
n=5 from M4/G2). Figure: `paper/figures/fig2_decay.png`; data: `paper/figures/fig2_trajectory.csv`.

```text
held CURRENT-truth %      r4    r5    r6(peak)   r15    r29
baseline (n=2)            14    20    28         16     6
authoritative source(n=1) 24    36    36(r5/9)   32     4
broadcast (n=1)          100   100    96        100    92
```

**Findings.**
1. **Truth rises then DECAYS — a real telephone curve.** Baseline climbs to a peak (~28% @
   r6) as the update diffuses, then erodes monotonically to ~6% by r30. The long-horizon
   attractor is LOW-truth and **unknown-dominated** (~85-90% unknown): over many rounds the
   update washes OUT of retrievable GA memory (buried under accumulating reflections) rather
   than being overwritten by the stale version — failure mode = LOSS, not stale-corruption.
2. **r5 was a near-PEAK transient.** Our earlier r5 snapshots caught the society on the rising
   edge / at peak, so they slightly OVER-state steady-state truth. The corrected steady state
   is LOWER (~5-6%) — this STRENGTHENS the decay claim, and is why running to r30 mattered
   (a single run, run_000, even froze at a fake-looking flat plateau; n=2 revealed continued
   slow decay).
3. **The authoritative source also collapses.** A persistent source re-broadcasting every
   round lifts truth higher and longer early (transient), but by r30 it ALSO decays to ~4%,
   converging to baseline. Persistent authority DELAYS but does not PREVENT entrenchment/decay.
4. **Only brute broadcast sustains truth.** Injecting truth into every agent every round holds
   ~97% throughout (slight drift 100→92). Consistent with M4: sustaining truth requires
   bypassing the social dynamics, not seeding them.

**Caveats (honest).** source/broadcast are n=1 (single seed 41); the source EARLY-peak (36%)
is seed-specific noise — the robust signal is the long-horizon DECAY toward baseline, not the
early lift. baseline n=2 (run_000 froze ~8%, run_001 kept drifting down). r30 is near- but not
perfectly-settled (still drifting at r29). Single scenario, mini, GA. The qualitative chain —
rise→peak→decay; source converges to baseline; only broadcast sustains — is unambiguous.

---

# C1 — CURE de-risk: provenance-aware integration (PROV) vs GA (2026-06-21)

**The cure hypothesis.** Decay is driven by entrenchment: GA integrates heard claims by
frequency/recency, so the stale incumbent (majority) wins. smga3g resolved currency in memory
but moved SAY without HOLD -- because the LISTENER side still integrated by frequency. PROV
adds the missing lever: provenance-based integration -- an explicit authoritative-LATEST value
supersedes the frequent older one, is held STICKILY (a later stale majority cannot revert it),
and is FOREGROUNDED when the agent speaks so it propagates. NOT an overwrite: the current value
must still be HEARD via conversation; an agent that never hears it stays stale/unknown.

```text
            HOLD-current     unknown    n
GA            18% (23/125)    91/125     5
PROV          58% (73/125)    18/125     5     <- ~3.2x GA, unknown collapses
broadcast    ~99%            (overwrite upper bound, not a fair social cure)
per-seed GA->PROV:  41:40->68  42:20->20  43:12->92  44:12->88  45:8->24
```

**Findings.** (1) PROV ~3.2x GA held-truth (18->58%); the dramatic shift is in UNKNOWN
(91->18/125): provenance-sticky belief + active relay actually PROPAGATES the current value
through the society instead of letting it wash out. (2) PROV is the FIRST non-overwrite
intervention that substantially restores held truth (capability/connectivity/memory/source all
failed; only god-mode broadcast worked before). It recovers ~half the gap to the overwrite
ceiling. (3) Honest variance: 3/5 seeds jump hugely, 1 modest, seed 42 unchanged -- PROV is
powerful but not guaranteed; the win likely depends on the update reaching a well-connected
agent early enough to lock+relay.

**Interpretation (mechanism, causal).** Swapping ONLY the integration rule (frequency ->
provenance), holding the society/contact model/model fixed, lifts held truth 3x. This is causal
evidence that the decay is produced by frequency-based social integration, not an inherent
limit -- so PROV is both a cure candidate and a mechanism proof.

**Caveats / next.** n=5, single scenario (repair_drive), mini, baseline condition only.
Provenance here is encoded via scenario value-markers (current supersedes stale); the paper
version must generalize to origin-round/version tags carried per claim. To make this Claim A:
(i) power to n>=8 with CIs; (ii) generalize across book_club/carpool; (iii) test PROV under the
SOURCE condition (does it also close the say-hold dissociation?) and over the long horizon r30
(does it resist decay?); (iv) build the comparison table vs recognized non-overwrite baselines
(RAG, MemoryBank, MemGPT, A-MEM, currency/smga3g, multi-agent debate).

---

# C2 — CURE validation: PROV powered (n=8) + source + long-horizon (2026-06-21)

Followed C1 de-risk with a powered, multi-condition validation (mini, repair_drive, m2).
Figure: `paper/figures/fig_cure_prov.png`.

```text
condition        HOLD%  95%CI      unknown/200
GA   baseline     22    [13-30]    135 (68%)
PROV baseline     40    [28-53]     57 (28%)
GA   source       21    [16-26]    136 (68%)   <- authority does NOT lift GA (dissociation)
PROV source       51    [37-65]     50 (25%)   <- authority DOES lift PROV
broadcast        ~99    (overwrite ceiling)
long horizon r30:  GA peaks 28% @r6 -> decays to 6% ;  PROV climbs to ~55% and SUSTAINS flat to r30 (n=3)
```

**Findings.**
1. **PROV ~doubles held truth** (baseline 40 vs 22). Note: at n=8 the baseline-vs-baseline 95% CIs
   marginally touch (28 vs 30) -- a strong signal, not yet airtight on that single contrast.
2. **The robust, clean wins are two:** (a) **unknown collapses** 68% -> 28% -- PROV actually
   PROPAGATES the fact instead of letting it wash out (tight, large effect); (b) **PROV closes the
   speech-belief dissociation** -- under an authoritative source GA stays at 21% (= its baseline:
   authority moves speech, not belief) while PROV rises to 51% (CIs cleanly separated). PROV is the
   lever that makes the society RESPOND to authoritative correction.
3. **PROV resists long-horizon decay (r30):** GA peaks ~28% then erodes to ~6%; PROV climbs to ~55%
   and holds flat through round 30 (n=3) -- ~9x GA's steady state, with no decay.

**Interpretation.** Swapping ONLY the social integration rule (frequency -> provenance), holding
society/model/contact-model fixed, (a) propagates the fact, (b) restores responsiveness to authority,
and (c) prevents long-run decay -- causal evidence that frequency-based integration is the cause of
the decay, and that provenance-aware integration is a genuine, non-overwrite cure.

**Caveats / next.** Provenance is encoded via scenario value-markers (paper version must generalize to
per-claim origin/version tags). Next: generalize across
book_club/carpool; build the comparison table vs recognized non-overwrite baselines (RAG, MemoryBank,
MemGPT, A-MEM, currency/smga3g, multi-agent debate); generalize the provenance encoding.

---

# C3 — FAIR/generalized PROV: the cure survives without being handed the answer (2026-06-21)

C1/C2 used marker-PROV (told which value is current = unfair vs baselines). C3 generalizes:
each claim carries a **version tag** (origin round) as conversation METADATA (`event['prov']`);
the authoritative update arrives carrying its version; an agent holds the highest version it
has HEARD and re-broadcasts that versioned belief when it speaks; listeners take max version.
PROV is NEVER told which value is correct -- it infers currency from version, and an agent that
never hears the versioned update stays unknown. Fair vs baselines (which simply don't track
provenance). Fig: `paper/figures/fig_cure_fair_prov.png`.

```text
              HOLD%   95%CI      unknown
GA (n=8)       22    [13-30]    68%
fair-PROV      57    [49-65]    40%      <- CIs DISJOINT; ~2.6x
per-seed GA->fair-PROV (8/8 up): 41:48->76 42:28->56 43:24->64 44:24->52 45:12->32 46:12->60 47:12->56 48:12->60
```

**Findings.** (1) The cure SURVIVES a fair implementation: 22->57%, 95% CIs disjoint, and
**every one of 8 seeds improves**. (2) Fair-PROV is actually STRONGER and cleaner than the
marker version (40%, overlapping CI, one seed flat) -- metadata propagation is more robust than
text-marker matching. (3) unknown collapses 68->40%: provenance propagates the fact. This
removes the "you handed PROV the answer" objection and makes PROV a legitimate architectural
contribution: *tracking provenance* vs memories that do not.

**Caveats / next.** Single scenario (repair_drive), mini, baseline condition. The source and
r30 conditions and the cure figure still reflect marker-PROV (C2) -- re-run with fair-PROV
before final. Next: BUILD THE ARCHITECTURE TABLE -- fair-PROV vs recognized non-overwrite
baselines {raw/RAG, GA, currency/smga3g, A-MEM, MemoryBank, debate} x {repair_drive, book_club,
carpool}.

---

# C5 — architecture comparison table + PROV horizon climb (2026-06-22)

Two results that together make PROV a strong (not marginal) cure. Fig: `paper/figures/fig_cure_table_horizon.png`.

**(a) Head-to-head vs recognized non-overwrite memory architectures (repair_drive, mini, r5, n=8):**
```text
Raw (RAG)        14 [6-23]      A-MEM           19 [12-26]
Mem0             18 [14-23]     GA reflection   22 [13-30]
GA-currency      25 [15-35]     MemoryBank      25 [19-31]
PROV (ours)      57 [49-65]                     Broadcast (ceiling) 99
```
Every recognized memory that tracks the current value INDIVIDUALLY (Mem0 extract/update,
A-MEM note-evolution, GA-currency, MemoryBank recency) still fails (14-25%) because none
PROPAGATE provenance to listeners. PROV (decentralized provenance propagation) alone lifts
held truth (57%), with cleanly disjoint CI.

**(b) PROV closes the gap given propagation time** (the 57% was reach-limited — only ~3
propagation rounds from 1 seed by r5; diagnosis: 59% of agents had received the versioned
update, interview faithfully matched at 57%, measurement gap ~2pts):
```text
horizon:   r5      r10      r20
PROV:      57%     93%      100%     (unknown 40% -> 7% -> 0%)
GA:        ~20%    ~22%     ~14% (decays; M5: ->6% by r30)
```
PROV monotonically reaches ~100% (the overwrite ceiling) PURELY via decentralized provenance
propagation, no overwrite/verifier; GA stays low and decays, so the gap WIDENS with time.

**Interpretation.** This upgrades the cure from "~2.6x GA" to "**fully restores social truth
fidelity given propagation time, decentralized, without overwriting**." It also sharpens the
contrast with the closest neighbor (Spark-to-Fire suppresses error spread to 89% via a
centralized governance+verifier; we propagate a correction to ~100% via per-agent provenance).

**DANGER SIGNAL (must address):** the 100%% is from a LOSSLESS/AUTOMATIC provenance side-channel (perfect gossip flood that bypasses the lossy LLM relay) — an IDEALIZED upper bound, not emergent reasoning. Next experiment = lossy provenance channel (survive relay w.p. 1-loss); if PROV still beats GA under loss, the integration rule is the real cure (see decisions 2026-06-22 late). **Caveats / next.** Single scenario (repair_drive), mini. Next per decisions 2026-06-22 D3:
(1) extend table + horizon to book_club/carpool; (2) topology robustness (chain/star/small-world);
(3) capability check (gpt-5.4). PROV's value blob = update text; fairness via origin-round metadata.

---

# C5-stress — PROV under a lossy provenance channel (the 100% danger-signal probe) (2026-06-22)

C5 found PROV climbs to 100% by r20 — but the human flagged 100% (zero variance) as a DANGER
SIGNAL: PROV's provenance is a lossless/automatic/always-adopted side-channel (a perfect gossip
flood that BYPASSES the lossy LLM relay, the very cause of corruption). To test whether PROV's
win is a pure artifact of that idealized channel, we degrade the channel two ways at r10:
- **DROP** (`--prov-loss p`): a relay fails to convey provenance w.p. p (value stays clean when
  it does arrive).
- **GARBLE** (`--prov-garble p`): a relay corrupts the VALUE to the stale value w.p. p, keeping
  the high version (the harder test — the clean channel itself carries a corrupted value, as LLM
  retelling would). Fig: `paper/figures/fig_prov_lossy_stress.png`.

```text
loss fraction:    0     0.3    0.6    0.9
DROP   (HOLD%):   93    100     93     26
GARBLE (HOLD%):   93     74     42     24
GA ref: 22                          (n=5 drop; n=4-5 garble)
```

**Findings.**
1. **Robust to DROP.** Provenance need not survive every relay — redundancy (many meetings +
   sticky belief) recovers it; PROV stays ~93-100% up to 60% drop, only collapsing to GA at 90%.
2. **Graceful degradation under GARBLE.** Value-corruption hurts more (as predicted: a garbled
   stale@high-version is sticky and a same-version correct claim cannot overturn it), but PROV
   degrades smoothly and **still beats GA across moderate corruption** (0.6 -> 42% ~= 2x GA),
   only reaching GA at severe (0.9) corruption.
3. **Verdict on the danger signal: substantially addressed.** PROV's advantage is NOT a pure
   artifact of a magic lossless channel — it survives heavy drop and moderate value-corruption.
   The 100% (p=0) is an idealized UPPER BOUND; the realistic operating range still clears GA.

**Honest limitation (for the paper).** PROV assumes provenance metadata conveys the value with
reasonable fidelity; under heavy value-corruption its advantage narrows to GA. This points to a
PROV design improvement: same-version conflicts should not be first-wins-sticky (a correct claim
at the same version cannot currently overturn a garbled one) — future work (trust/verification or
same-version arbitration).

**Caveats.** Single scenario (repair_drive), mini, r10. Loss is modeled as a per-relay probability
(a clean abstraction of the lossy text channel); literal text-embedded provenance is a further
variant. The injection into the source is never lost (it is a direct authoritative receipt, not a
relay) — fixed after an initial run where loss zeroed the source.

---

# C6 — PROV-v2 (corroboration + Ebbinghaus decay): an honest NEGATIVE result (2026-06-22)

Following the architecture reflection (decisions 2026-06-22), we built PROV-v2 to fix two flaws
of PROV: (1) the absorbing 100% lock, via Ebbinghaus confidence decay; (2) the garble/exploit
fragility, via corroboration-gated adoption (a claim needs >=k distinct sources; same-version
conflicts break by corroboration). Smoke tests confirmed both mechanisms work in isolation.
In the SOCIETY, both FAILED.

```text
                 PROV-v2     vs PROV    vs GA
clean r10:         99%          93         22
clean r20:        100%         100
garble=0.6 r10:     7% (stale-dom 93%)   42    22
```

**Why decay failed.** The fact is re-broadcast by every believer every round, so confidence is
reinforced (reset to 1.0) faster than it decays -> it never drops below the forget threshold ->
the 100% lock persists. **The 100% lock is a property of the COMMUNICATION MODEL (constant
re-broadcast), not of missing memory-decay.** A realistic fix must drop the "agents restate every
fact every meeting" assumption, not add memory decay.

**Why corroboration backfired.** garble here is SYSTEMATIC (every relay corrupts the value w.p.
0.6), so the STALE value is itself corroborated by many agents, easily clears the k-source gate,
is held confidently, and spreads -> the society converges CONFIDENTLY on stale (93%), worse than
both PROV and GA. **Corroboration defends against a LONE adversary (one high-version liar), not
against a noisy CHANNEL that corrupts everyone's relays.**

**Lessons (valuable).** (1) Breaking the 100% requires a realistic communication/attention model,
not memory decay. (2) Defending held-belief against systematic value-corruption needs source
credibility / external verification (cf. Spark-to-Fire's verifier) -- a fundamentally harder
problem that a decentralized memory rule alone cannot solve. (3) This sharpens PROV's honest
scope: a clean EXISTENCE PROOF that provenance integration breaks frequency-entrenchment under
benign channels; NOT a robust defense against an adversarial/garbling channel. PROV-v2 (as
designed) is recorded as a failed upgrade -- do not ship it.

**Status.** clean n=3-5 (finishing), garble n=3. Negative result is stable.

---

# C7 — sparse communication: the 100% lock is a comms-model artifact (2026-06-22)

C6 showed PROV-v2's Ebbinghaus decay failed because the fact was re-broadcast EVERY utterance
(reinforcement outran decay). The human flagged the root cause: agents broadcasting the fact
every round is unrealistic (people don't restate every fact every conversation). We added
`--prov-mention p`: an agent conveys the fact in a given utterance only with prob p (sparse,
topic-gated comms). Fig: `paper/figures/fig_sparse_comms_equilibrium.png`.

```text
prov_mention:   1.0     0.3     0.1
PROV-v2 HOLD:    99      96      40   (stale 0; unknown rises)   GA ref: 22
(v1 sticky, mention 0.1: 40 [34-46] -- would keep climbing, no decay)
```

**Findings.**
1. **The 100% lock was an artifact of every-utterance broadcast.** With realistic SPARSE mention,
   reinforcement no longer outruns decay, and PROV-v2 settles to a DYNAMIC EQUILIBRIUM (~40% at
   mention 0.1) instead of locking at 100% -- a genuine "mention-rate vs forgetting" balance.
2. **Provenance still wins under realistic comms.** At the realistic operating point the
   equilibrium (~40%) is ~2x GA (22%) and CLEAN (stale 0% -- forgotten agents go to unknown, not
   corrupted). So the cure survives the realism fix; it just no longer claims an unrealistic 100%.
3. **Decay needs sparse comms to matter.** At mention 0.3 the society still saturates (96%) --
   decay only bites once mention is sparse enough (<=0.1 here). This locates the realistic regime.

**Interpretation.** This is the correct fix to the C5/C6 danger signal: the 100% was never
emergent truth, it was constant re-broadcast. Under sparse, realistic communication with
forgetting, the honest cure result is a stable equilibrium well above GA -- not saturation. This
is the number to report as PROV's realistic effect; 100% is the every-round-broadcast upper bound.

**Caveats.** Single scenario, mini, r10; v2 mention-0.1 n=4-5. prov_mention is a probability per
utterance (a clean proxy for topic-gated sparse comms); a text-coupled version is a further
variant. Equilibrium level depends on (mention rate, decay, connectivity) -- a small phase
diagram (mention x decay) is natural future work.

---

# C8 — architecture comparison across 3 scenarios (generality) (2026-06-22)

Generalizes the C5 repair_drive table to book_club + carpool (mini, m2, r5, n=5).

```text
scenario        GA          PROV(ours)   GA-currency  A-MEM
repair_drive    22 [13-30]  57 [49-65]   25 [15-35]   19 [12-26]
book_club       47 [45-49]  69 [62-76]   42 [17-67]   52 [38-66]
carpool         18 [10-25]  59 [49-69]   24 [17-31]   30 [25-34]
(broadcast ceiling ~99 all scenarios)
```

**Finding: PROV is the top method in ALL THREE scenarios.** repair_drive and carpool show clean CI
separation (PROV >> all baselines); book_club has higher baselines (GA 47, A-MEM 52 -- this
scenario is intrinsically easier) but PROV (69) is still highest. No recognized memory architecture
matches PROV in any scenario. This kills the single-scenario-artifact critique and answers the
Spark-to-Fire-style demand for a head-to-head architecture comparison: provenance integration
beats frequency-based memories generally, not just on one task. Next (decisions D3): topology
robustness + a different fact-TYPE scenario (numeric correction).

---

# C9 / C10 — fact-type + topology generality (2026-06-22)

Closing two external-validity gaps (decisions D3) the way Spark-to-Fire's breadth invites.

**C9 — different FACT TYPE (numeric correction).** New `dues` scenario: membership dues change
40 -> 60 dollars (a numeric value, not a day/place reschedule). repair_drive table re-run on it
(mini, m2, r5, n=5):
```text
GA 28 [18-38]   PROV 59 [49-69]   GA-currency 7   A-MEM 25 [20-30]
```
PROV still leads (~2x GA), so the cure is not tied to the reschedule fact-type.

**C10 — TOPOLOGY robustness (repair_drive, r10).** GA vs PROV across contact structures:
```text
topology      GA      PROV
random       ~22       93     (from C5)
ring           6       68
smallworld    10       83
```
PROV >> GA on every topology, and the margin GROWS on harder (slower-mixing) structures: on a
ring GA barely propagates (6%) while PROV still reaches 68%. The decay is worse on structured
nets (GA), but provenance propagation is largely topology-robust. (star is degenerate under the
per-round degree cap -> deferred; a broadcast-hub variant is future work.)

**Together:** PROV beats frequency-based memory across 4 scenarios (3 reschedule + 1 numeric)
AND across 3 topologies -- the single-scenario / single-topology / single-fact-type artifact
critiques are all closed. Some cells finishing to n=5 (GA-currency dues n=4; ring/smallworld GA
n=2-3); the PROV>>GA conclusion is stable.

---

# C11 -- text-coupled provenance probe (2026-06-22)

Question: is GA already the natural-language-only society, and does PROV still work if
provenance must travel through the utterance text instead of a hidden `event["prov"]` channel?

Implementation: added `PROVTextMemory`, which has no `provenance()` method and therefore cannot
attach structured metadata to ordinary conversation events. It adopts a relayed update only when
the utterance itself contains an explicit attribution cue such as `official round 1` plus the
scenario value. Direct world injections still carry authoritative provenance, as before.

Fast mechanism probe: `--mock --context-relay-mock`, repair_drive, 25 agents, r10, m1, n=5.
This deterministic text-only relay says one natural sentence from the speaker's retrieved memory
notes, avoiding API latency while keeping relays as text.

Held-belief snapshot tally:

```text
condition      current    stale    unknown
raw              0/125    42/125    83/125
PROV           125/125     0/125     0/125
PROV-text      125/125     0/125     0/125
```

Audit: PROV-text ordinary conversation events have no hidden `prov` payload; propagation occurs
through utterances containing `Official round 1 update: ...`.

Interpretation: this confirms the mechanism is not inherently dependent on a binary side channel:
if agents explicitly preserve source/version language, text-coupled provenance can propagate like
structured PROV. It is still a mechanism probe, not the final realism result. The unresolved next
experiment is an LLM conversation run where agents may or may not naturally preserve the source
phrase; initial full LLM sweeps were too slow for this turn and should be run as a longer job.

---

# C12 -- PROV-text-free under real LLM dialogue (2026-06-22)

Question: will ordinary LLM agent dialogue naturally preserve source/version language well enough
for text-coupled provenance to propagate, without the hidden `event["prov"]` side channel?

Config: repair_drive, `gpt-5.4-mini`, 25 agents, r10, m1, t2.

Data:
- Main PROV-text-free run: `sim/runs/provtext_llm_only_r10_n5`
- Partial same-job comparator archive: `sim/runs/provtext_llm_long_r10_n5`
- Each directory has `ARCHIVE.md`, `run_config.json`, reconstructed `aggregate.json`, and
  `runs.json` where applicable.

Completed PROV-text-free rows:

```text
seed 301: 5 current, 0 stale, 20 unknown
seed 302: 3 current, 0 stale, 22 unknown
seed 303: 8 current, 0 stale, 17 unknown

total:    16/75 current = 21.3%; 0 stale; 59 unknown
```

Retention audit:

```text
utterances containing source/version markers: 0/720
agents holding version>=1 in memory snapshots: 1/25 per run (only a01/Rosa)
```

Comparator rows from the stopped mixed job:

```text
GA, same setting:              21/100 current, 4 stale, 75 unknown
Structured PROV, same setting: 50/50 current, 0 stale, 0 unknown
```

Incomplete/excluded runs:
- `provtext_llm_long_r10_n5/ga/run_000`: provider HTTP 403 after round 0.
- `provtext_llm_long_r10_n5/prov/run_002`: completed dialogue but no final interview.
- `provtext_llm_only_r10_n5/provtext/run_003`: empty directory after manual stop.

**Finding.** Natural dialogue does **not** spontaneously preserve source/version. PROV-text-free
does not improve over GA; it stays near the GA level and is unknown-dominated. The mechanism is
not stale corruption here: the provenance cue simply fails to leave the source agent.

**Interpretation.** This is a useful negative result. Structured PROV should be framed as an
idealized provenance-preserving protocol / upper bound, not as a fully naturalistic cure. The
real design target is now PROV-text-norm: explicit source/version attribution carried in natural
language, still propagated socially and not broadcast.

**Decision.** Stop PROV-text-free at n=3 because the mechanism signal is already clear
(0/720 source/version mentions; only a01 holds version>=1). Do not spend more budget confirming
the same negative. Next P0 = implement and run PROV-text-norm.

---

# C13 -- PROV-text-norm strong attribution dialogue (2026-06-23)

Question: after PROV-text-free fails, can provenance still propagate through text if agents use
an explicit attribution norm, without hidden `event["prov"]` metadata and without broadcast?

Config: repair_drive, `gpt-5.4-mini`, 25 agents, r10, m1, t2, n=3.

Data:
- Run archive: `sim/runs/provtext_norm_r10_n3`
- Files: `run_config.json`, `aggregate.json`, `runs.json`, per-run transcripts, memory snapshots,
  and `ARCHIVE.md`.

Completed rows:

```text
seed 301: 25 current, 0 stale, 0 unknown
seed 302: 25 current, 0 stale, 0 unknown
seed 303: 25 current, 0 stale, 0 unknown

total:    75/75 current = 100%; 0 stale; 0 unknown
```

Retention audit:

```text
run_000: 200/240 utterances contain source/version-like markers; 25/25 agents version>=1
run_001: 221/240 utterances contain source/version-like markers; 25/25 agents version>=1
run_002: 189/240 utterances contain source/version-like markers; 25/25 agents version>=1

total:   610/720 marker utterances; 75/75 agents version>=1
```

**Finding.** A strong attribution norm makes text-only provenance work: every completed agent
answers with the current fact, and every agent's memory snapshot contains versioned provenance.

**Caveat.** This is not a natural-human dialogue result. The norm is strong and visibly
protocolized (`Official round 1 update...`). It should be reported as a text-only provenance
upper bound: if a society preserves attribution explicitly, held truth can be repaired without
broadcast. It should not be used to claim that ordinary conversation naturally preserves
source/version.

**Interpretation.** The combination of C12 and C13 is the clean story:

```text
PROV-text-free: ordinary dialogue drops provenance -> weak held truth.
PROV-text-norm: explicit attribution in text preserves provenance -> strong held truth.
```

This supports a design claim rather than a pure memory-module claim: useful agent societies may
need provenance-preserving social memory interfaces, spanning both memory representation and
communication norms.

**Next experiment.** Do not scale the current strong norm blindly. The next useful step is an
attribution-strength ablation: light natural attribution, medium update attribution, and strong
protocolized attribution, with a listener that extracts varied natural source cues rather than
only `Official round` phrases.

---

# C14 — Capability check on the cure: PROV vs GA on DeepSeek-V4-Flash (2026-06-23)

This closes the one real gap the capstone flagged: every cure run (C1–C13) was on `mini`, so we
had not shown the *cure* (not just the phenomenon) survives a change of model. M0 had already
shown the *phenomenon* survives capability (truth-recall flat 16→21% across mini→gpt-5.4→gpt-5.5).
C14 is the symmetric test for the cure, on a DIFFERENT model FAMILY — DeepSeek-V4-Flash via the
OpenAI-compatible yunwu.ai gateway — at the headline cure settings (repair_drive, 25 agents,
meetings=2, rounds=5, turns=3, GA vs fair-PROV).

n=8 (seeds 41–48):

```text
memory  held-current @ r5     median   95% CI          std
GA       15.5%                14.0%    [10.1, 20.9]     7.9
PROV     64.0%                62.0%    [57.8, 70.2]     8.9
```

(per-seed GA: 16,28,8,12,8,8,28,16 · PROV: 80,72,60,64,48,60,68,60)

**Finding.** The cure survives capability. PROV ≈ 4× GA, and the 95% CIs are DISJOINT
([57.8,70.2] vs [10.1,20.9]). The first-3-seed n=3 pilot over-estimated both arms
(PROV 70.7 / GA 17.3); n=8 settles to the honest PROV 64.0 / GA 15.5.

**Symmetry with M0 / mini (both arms now n=8).**

```text
              mini (n=8)              DeepSeek-V4-Flash (n=8)
GA            21.5% mean / 18% median  15.5% mean / 14% median   CIs OVERLAP -> phenomenon survives capability
PROV          57% [49-65]              64.0% [57.8-70.2]         PROV > GA on both; cure survives capability
PROV > GA?    yes (disjoint)           yes (disjoint)
```

GA is statistically indistinguishable across model families (mini median 18 ≈ ds 14; CIs
overlap) -> the phenomenon is not a mini artifact. PROV wins on both, slightly stronger on ds
(64 vs 57). NB the mini GA mean (21.5) is pulled up by one high seed (seed41=48%, audited as
real variance, not a fault — kept); the median (18) is the robust comparator and is ≈ ds.

**Provider note.** DeepSeek/yunwu concurrency probe (4→32 burst): 100% success up to conc 24,
one transient SSL at 32 (absorbed by retries=3). Tail-latency bound (stragglers 30–49s), NOT
throttle-bound; workers=16 ≈ workers=8 in wall-clock (~2 min/round). No rate-limit observed.

**Status.** COMPLETE at n=8 (2026-06-24). Both arms pooled across dirs: `cap_deepseek_prov_vs_ga_pilot`
(seeds 41-43), `cap_deepseek_prov_vs_ga_n8ext` (GA 44-48 + PROV 44), `cap_deepseek_prov_n8fill`
(PROV 45-48), `cap_deepseek_prov_seed44` (PROV 44 interview backfill). The capability-check gap is
closed at full n=8 rigor.

---

# C15 — APM (Auditable Provenance Memory): the interpretable architecture (2026-06-24)

The question (raised by the human, re "not a deployable architecture"): can we turn the naive
PROV *lever* into an actual interpretable, spoof-resistant architecture without losing the cure?
APM (implemented in `memories.py::APMMemory`) adds three things PROV lacks — origin anchoring
(anti-spoof), chain corroboration by K independent sources, and abstain — plus a full auditable
provenance trace. C15 pilots it on DeepSeek at the C14 settings (repair_drive, 25a m2 r5 t3, n=3).

```text
memory          held-current @ r5     failure mode
GA               17.3% (13/75)        stale (confidently wrong)
APM K=2 (gated)  12.0% ( 9/75)        DEADLOCK (only origin commits)
APM K=1          64.0% (48/75)        abstain (unknown, not stale)
PROV             70.7% (53/75)        --
```

**Finding 1 — the cure survives interpretability + spoof-resistance (APM K=1 ≈ PROV).**
APM K=1 (64.0%, per-seed [56-76]) is within a few points of naive PROV (70.7%) and far above GA
(17.3%). Adding anti-spoof + abstain + full auditability costs ~7 points of held-current. APM does
NOT reduce to a worse PROV; it is PROV's performance plus properties PROV lacks.

**Finding 2 — auditability is real and measured.** 15-19 of 25 agents per run (60-76%) hold a
belief with a COMPLETE provenance chain traced to ORIGIN (avg path length 3.2 hops). The remainder
abstain. Black-box memories (GA / Mem0 / A-MEM / MemBank) cannot produce this justification.

**Finding 3 — safer failure direction.** APM's misses are *unknown* (20/75), not *stale* (7/75):
it abstains rather than confidently propagating the wrong value. GA fails the opposite way (stale).

**Finding 4 — K=2 commit-gated DEADLOCKS (recorded negative).** With K=2 and "relay only what you
committed", only the origin ever commits: each neighbor hears the truth from one source (the
origin), 1 < K=2, so it abstains and never relays, so `auth` cannot bootstrap. Result 12% (below
GA). This is the OPPOSITE of the saturation worry — corroboration can choke propagation. Multi-source
corroboration therefore needs **relay-before-commit** (forward authenticated claims pre-commit so
`auth` spreads); that is the next implementation, required for the garble/adversarial robustness story.

**Interpretation.** APM earns its place as an architecture (not just a lever): near-PROV held truth,
spoof-resistant, fail-safe (abstain), and interpretable-by-construction. The K knob dials between
flood (K=1, PROV-like) and over-conservatism (K=2-gated). Remaining APM work is bounded to two
questions (pre-registered in `paper/sections/architecture_apm_vs_ga.md`): (a) adversarial-liar
scenario where APM must beat naive PROV via anti-spoof; (b) realistic-friction equilibrium
(sparse comms / longer horizon) confirming a stable sub-100% value. After those, APM's scientific
job is done — further hardening is product, not paper.

---

# C17 — APM realistic-friction equilibrium: the saturation check (2026-06-25)

The second and last pre-registered APM question, and the direct answer to the human's recurring
worry ("will APM also flood to 100% like PROV did?"). Telephone C7 already showed the 100%
ceiling is a COMMUNICATION-model artifact (every-utterance broadcast + lossless + sticky), not a
property of provenance integration. C17 confirms it for APM: under realistic SPARSE comms
(`--prov-mention 0.1`: an agent conveys the fact in only ~10% of utterances) + long horizon (r10),
does APM settle to a stable sub-100% equilibrium? Run on gpt-5.4-mini/FHL. **n=8 (seeds 41-48).**

```text
                held-current        stale       unknown
APM @m0.1 r10   40.5% [27.2-53.8]   0/200       159
GA  @m0.1 r10   21.5% [14.7-28.3]   30/200      ~129
   (per-seed APM: 52 72 8 52 36 20 32 52 ; std 19.2 — high, sparse-comms variance)
```

**Finding 1 — APM does NOT saturate (the check PASSES decisively).** It settles to 40.5%, far
from 100%. The 100% in idealized comms was a gossip-flood ceiling (Telephone C7); under realistic
sparse comms APM's abstain caps it at a healthy sub-100% equilibrium. This is the honest cure
number under friction — a real, reasonable lift, not a saturation artifact.

**Finding 2 — the held-current edge over GA is SUGGESTIVE, not decisive (honest at n=8).** APM
40.5% vs GA 21.5% (~1.9x) by mean and median (44 vs 24), BUT APM's sparse-comms variance is high
(std 19.2) so the 95% CIs marginally overlap ([27.2-53.8] vs [14.7-28.3]). At n=8 we cannot call
the *breadth* advantage statistically significant. (Note: this is the breadth axis only.)

**Finding 3 — the DECISIVE difference is quality/safety: stale 0 vs 30 (disjoint).** Across 200
agents APM is wrong ZERO times; GA is wrong 30. APM's misses all go to *unknown* (abstain), never
to a forged/stale value. This separation is clean and large.

**Takeaway.** Under hard sparse comms nobody spreads the truth widely (the breadth gap between
any two methods shrinks — information just doesn't reach enough agents). What APM still guarantees,
decisively, is that **the informed are never misled**: zero confident errors vs GA's 30. The
honest C17 claim is therefore "non-saturating healthy equilibrium + decisive safety (stale=0)",
not "≈3x GA in breadth" (that was the n=3 over-read; n=8 corrects it).

**Status — APM's scientific job is DONE.** Both pre-registered questions are now answered:
C16 (adversarial robustness: APM survives, PROV hijacked) and C17 (realistic equilibrium: APM
non-saturating at 40.5%, n=8, with decisive safety stale=0 vs GA 30; breadth edge suggestive
under sparse-comms variance). Per the scoping discipline, further APM hardening is product, not
paper. Forgetting as a first-class variable — which would re-open the dynamics — is deliberately
deferred to the sequel project 7-Thaw, not folded in here.

---

# C16 — Adversarial-liar robustness: the test that justifies APM (2026-06-25)

The one experiment that makes APM an architecture rather than a re-skin of PROV: APM and PROV
are equivalent WITHOUT an adversary (both ≈ the cure level); the question is what happens WITH a
deliberate attacker. One agent (a13) is turned into a liar that, from round 2, broadcasts a
FORGED claim — the stale value carried at version 999 with `auth=False` (the attacker cannot mint
`auth`; that is the trust model). Run on gpt-5.4-mini via FHL (yunwu/ds was 429-overloaded at the
time). repair_drive, 25a m2 r5 t3, n=3.

```text
                held-current     stale (HIJACKED)   unknown
PROV (adv)      33.3% [24-40]     43/75              7
APM  (adv)      64.0% [60-72]      0/75              27
no-adversary    PROV 57% (mini, C3) ;  APM ≈ PROV (verified on ds, both 64%)
```

**Finding — only APM survives the attack.** The liar collapses PROV from 57% to 33% and drives
43 of 75 agents to believe the forgery (stale). APM is essentially UNMOVED (≈64%, its
no-adversary level) and **not one agent is hijacked: stale = 0**. APM's misses go to *unknown*
(abstain), never to the forged value.

**Audit (interpretability under attack).** 15-18 of 25 APM agents per run hold a committed
belief; **0 are contaminated by the forged v999**. The anti-spoof property (origin anchoring)
holds society-wide, not merely in the isolated unit test — and every surviving belief remains
traceable to the authoritative origin.

**Mechanism (unit-tested separately).** Given the same forged claim, naive PROV adopts it
(belief -> FORGED stale; only checks version), while APM rejects it (require_origin: no auth).
C16 shows that micro-mechanism scales to the society.

**Interpretation — APM's reason to exist.** Without an adversary, APM ≈ PROV (interpretability is
nearly free, C15). With an adversary, PROV is hijacked and APM is the ONLY architecture left
standing. This is the deployable-architecture answer to the human's original worry ("not a
deployable architecture"): provenance integration HARDENED with origin anchoring resists a
forgery attack that defeats naive provenance. ds cross-check (seed41) agrees: PROV-adv = 36%.

**Scope note.** This closes the first of APM's two pre-registered remaining questions
(adversarial robustness). The second (realistic-friction sub-100% equilibrium under sparse comms /
longer horizon) remains; after it, APM's scientific job is done.
