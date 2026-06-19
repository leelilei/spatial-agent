# Telephone — Path to Publication

> Concrete remaining work to take the M0–M4 findings (see `../project/conclusions.md`) to a
> submittable paper. Ordered by leverage = (reduces a reviewer's first attack) × (cheap).
> Target venues (proposal_v1): COLM / NeurIPS / ICLR; big-splash if it generalizes cleanly.

## The four gaps between "internally consistent finding" and "publishable"

| # | Gap | Reviewer attack it blocks | Effort |
|---|---|---|---|
| **P1** | **Generality**: single scenario | "It's an artifact of one prompt/scenario" (FIRST attack) | medium |
| **P2** | **Metric**: keyword current/stale | "Your metric is circular / surface-level" | medium |
| **P3** | **Power**: n=3–5 on M0–M3 | "Underpowered; could be noise" | low (just runs) |
| **P4** | **Mechanism depth**: say-ratio is coarse | "You assert dissociation but don't localize it" | medium |

## P1 — Generality (HIGHEST leverage, do first)

Parametrize the scenario (event name, old/new day+place, update text, interview question,
verdict markers) and replicate the **two headline results on ≥2 structurally different,
non-Chinese scenarios**:
- **Capability-flat + confident-corruption (M0)** — does it hold for scenario B/C?
- **Speech–belief dissociation (M4-source fails, broadcast works)** — the spine; must replicate.
If both replicate across scenarios → the artifact attack dies and the claim is general.

Scenario B candidate: a book club moves Tuesday@library → Thursday@cafe.
Scenario C candidate: a shift swap / a carpool pickup time+place change.

## P2 — A defensible fidelity metric

Replace (or back up) the keyword current/stale with a **provenance- + judge-based** metric:
- "received the update" = the agent's stream carries the injected update (provenance tag),
  defined INDEPENDENTLY of the answer keyword (kills circularity).
- fidelity = an LLM judge on a frozen rubric (proposition / detail / currency correctness),
  human-audited on a sample, judge-agreement reported.
- keep the conversation-level say-ratio and the held-recall as the two dissociation axes.

## P3 — Power (cheap; do alongside P1)

Re-run M0 (capability ladder) and M1 (connectivity) at **n≥8 + 95% CIs**; firm up the M1
"connectivity amplifies corruption" cells (esp. gpt-5.4 meetings=3, which was a dramatic
single-batch number). M4 is already n=5 with tight CIs — extend to n=8 for symmetry.
Operating note: keep total in-flight ≤ ~40 (provider sustained throughput), short jobs.

## P4 — Localize the dissociation (the mechanism, the paper's spine)

Instrument WHERE the truth is lost between hearing and holding:
- per round, per agent: HEARD (stream Sun:Sat) → HELD (belief Sun:Sat, via a cheap probe or
  memory inspection) → SAID (utterance Sun:Sat). Track the three trajectories.
- test the **evidence-ratio hypothesis**: is held-belief predicted by the agent's *cumulative
  heard* Sun:Sat ratio (Bayesian re-weighting), rather than by the most recent/authoritative
  mention? If yes, that *explains* why a lone authority loses and why broadcast (which floods
  the ratio) wins.

## Suggested execution order

1. **P1 scenario parametrization + replicate M0 & M4 on scenario B** (kills the #1 attack).
2. **P3** higher-n + CIs on M0/M1 (cheap, runs in parallel).
3. **P4** dissociation localization (the mechanism figure — the paper's spine).
4. **P2** the clean fidelity metric (re-score everything; the rigor pass).
5. Then write: Intro (the hook) → Method (instrument + metric) → Results (decay; failed
   levers; the dissociation) → Discussion (collective epistemics; implications for MAS).

## Definition of "publishable-ready"

The dissociation (M4) + capability-flat (M0) + connectivity-worsens (M1) replicate on ≥2
scenarios, at n≥8 with CIs, under the provenance/judge metric, with a mechanism figure
localizing where belief detaches from speech. At that point it is a complete, defensible
"phenomenon + laws + mechanism + honest non-cure" paper.
