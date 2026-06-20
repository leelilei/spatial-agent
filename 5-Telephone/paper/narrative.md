# Telephone — paper narrative / 论文思路（活文档）

> **Working title:** *Speech is not belief: Fidelity decay in LLM agent societies*

> Concept-level story; numbers live in `../RESULTS.md`. Append a section whenever a
> CONCEPTUAL (not just numeric) step lands. Started 2026-06-19.

## 0. The one-sentence thesis

In LLM-agent societies, a ground-truthed update degrades predictably as it propagates (a
"telephone" effect); we characterize this fidelity-decay, identify what governs it, and
ask whether better agent memory acts as error-correction.

## 1. Why this is worth doing (the reframe from 3-SMGA)

3-SMGA tried to use the society sim to RANK memory architectures and kept failing under
rigor — the apparent wins were artifacts (keyword circularity, chaotic variance), and the
real bottleneck turned out to be **conversation/diffusion fidelity**, not memory. The
honest discovery hiding in those "failures": **the society does not faithfully propagate
an update — it plays telephone.** That phenomenon, not the memory ranking, is the prize.
The same noise/sensitivity that defeated the SMGA framing is, here, the OBJECT of study.

## 2. What's genuinely new

GA-lineage work shows information *spreads* (Isabella's party) and treats that as success.
Nobody asks if the spread is *faithful*. We measure the fidelity, not just the reach —
moving from "did agent X remember" (individual, benchmark view) to "what does the SOCIETY
converge on" (collective epistemics).

## 3. Open design questions (resolve before first real run)
- A non-circular definition of "received the update" and "fidelity" (avoid the SMGA trap).
- A corruption taxonomy: stale-persistence / drift / fabrication / loss.
- The right epidemic-style summary: fidelity-decay vs hops; truth-share vs corruption-share.

## 4. The attractor reframe (2026-06-19, after the lit review)

The single most valuable upgrade from the literature: **corruption is not degradation-to-
noise, it is convergence-to-an-attractor.** Iterated-learning experiments (Kirby 2008 PNAS;
Bartlett 1932) show serial transmission contracts information toward a simpler, "more
learnable" form. So the right object is not "the message got noisier" but **"the society
converges to a truth attractor or a corruption attractor, separated by a phase boundary."**
This is more elegant, more falsifiable, and rides a respected cog-sci lineage. It rewrites
C2 (phase boundary between attractors) and adds a metric (version *diversity*, not just
truth-share — a low-diversity, high-consensus error is its own attractor; cf. MAD,
Alemohammad 2023). Our seed-41 evidence (18/22 confidently Saturday) is exactly a
low-diversity corruption attractor.

## 5. Where memory honestly re-enters (C4)

Not "structured memory wins." C4 = "the minimal cure for a now-quantified failure," and it
has near-isomorphic theory: Yi et al. (2025) show an external verifier halts model collapse
but pulls the system to the verifier's knowledge center — our **authoritative re-broadcast**
is the social-channel version; **currency-resolving memory** mirrors temporal conflict-
resolution memory (APEX-MEM 2026); and memory can also *amplify* error (Xiong 2025). So the
intervention is principled, not a recycled SMGA headline.

## 6. Competitive clock (honest)
Two 2026 preprints (Becker — benign-MAS misinformation; Jamshidi — hallucination cascade)
are in our neighborhood but stop at task-correctness in debate/cascade. They do NOT do
society-scale decay-vs-hops, version-share/diversity, the phase boundary, or a minimal
correction. That is our wedge — but the space is filling, so M0 should plant a flag fast,
with measurement rigor + society-scale dynamics as the moat.

---

# FINDINGS — what M0–M3 actually showed (2026-06-19)

> Sections 0–6 above were the PLAN (pre-experiment hypotheses). This section is what we
> actually found in the first run-batch (mini→gpt-5.5, GA/raw/v2/v3 memory, 25 agents, r5,
> n=3–5, single "repair drive" reschedule scenario). Numbers + caveats in `../RESULTS.md`
> (M0–M3). Read this as the honest, sober update to the plan.

## The phenomenon is real and ROBUST
A ground-truthed update ("the repair drive moved Saturday→Sunday") does NOT propagate
faithfully through an LLM-agent society. The society converges on a **corruption attractor**
(the stale Saturday version persists, dominates, and spreads). Truth-recall is low (≤~28%)
in every configuration we tried. So far the headline is a strong NEGATIVE: **truth-decay in
agent societies is hard to avoid.**

## What does NOT fix it (three failed levers)
1. **Capability (M0).** Scaling mini → gpt-5.4 → gpt-5.5 leaves truth-recall FLAT
   (16%→20%→21%). Worse, capability shifts the FAILURE MODE: weak models forget (unknown),
   strong models **confidently converge on the stale version** (stale 2.3→10, Sat-dominance
   8→16). *Scaling makes the society more confidently wrong, not more right.*
2. **Connectivity (M1).** More communication AMPLIFIES corruption, not truth. The
   Saturday:Sunday dominance ratio explodes with connectivity for strong models (gpt-5.4
   0.9×→10.4× as meetings 1→3). *More communication, less truth* (echo-chamber / repetition
   reinforcement) — the opposite of redundancy-as-error-correction.
3. **Memory architecture (M2→M3).** A currency-resolving memory (smga3g) APPEARED to flip
   the society to truth (M2, 56%) — but that was an **n=3 outlier; it did NOT replicate**
   (M3, n=4–5: smga3g current ≈ GA, Δ ns). Swapping memory does not robustly restore truth.

## The most interesting sub-finding: a DISSOCIATION
smga3g DOES make agents *say* "Sunday" more (event streams shift Sunday-dominant, m2 Sat:Sun
4:28) — yet the society's *held* belief (interview truth-recall) does not improve. **Memory
changes what agents SAY without changing what the society HOLDS.** Speech ≠ collective
belief. This gap is worth pinning down — it suggests the corruption attractor is sustained
by something downstream of any one agent's output (the network evidence-ratio / Bayesian
re-weighting), not by what individuals can be made to utter.

## Honest current thesis (updated after M4)
Truth-decay in LLM-agent societies is **robust** — it resists EVERY realistic lever:
capability (M0), connectivity (M1, which makes it worse), memory architecture (M2/M3), AND
a persistent authoritative source (M4-source re-broadcast, Δ ns). The society reliably
converges on a corrupted/stale consensus. **Only brute-force BROADCAST** — injecting the
truth into every agent every round, i.e. bypassing the social dynamics by overwriting each
memory — restores it (M4-broadcast, 99%); that is spoon-feeding, not an emergent cure.

## The mechanism (M4): a DISSOCIATION — speech ≠ collective belief
This is the project's sharpest claim, now demonstrated with tight CIs. Interventions readily
change what agents SAY but not what the society HOLDS. In M4-source, a persistent authoritative
source flips the society's utterances to Sunday-dominant (said Sun:Sat 25:5 by round 5) yet
the HELD belief stays stale/unknown (current 3.8/25, unchanged from baseline). The collective
belief is **sticky** — anchored by the network evidence-ratio (the entrenched stale version),
not by what any source can be made to utter. You can make the society parrot the truth; you
cannot (short of overwriting every memory) make it BELIEVE the truth.

## Caveats (do not over-read yet)
n=3–5, single scenario, single update, keyword-based current/stale metric (the receiver
Sat/Sun-dominance provenance signal agrees, which is reassuring), runtime-cap losses made
some M3 cells unequal-n. To make any of this publishable: provenance fidelity metric, n≥8
+ CIs, ≥2–3 scenarios. But the qualitative chain (robust decay; capability/connectivity/
memory don't fix it; the dissociation) is consistent across M0–M3 and with the 3-SMGA prior.

## Open threads (for when we resume)
- **C4 closure**: test authoritative re-broadcast (the stronger, untested intervention).
- **Pin the dissociation** (speech vs collective belief) — possibly the paper's sharpest idea.
- **Rigor**: provenance fidelity metric; n≥8 + CIs; ≥2 non-Chinese scenarios; firm up the
  M1 "connectivity amplifies corruption" cell (gpt-5.4 m3 52:5 needs CIs).
