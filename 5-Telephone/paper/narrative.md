# Telephone — paper narrative / 论文思路（活文档）

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
