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
