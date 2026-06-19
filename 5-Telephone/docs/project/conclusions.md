# Telephone — Deep Conclusions (archival synthesis)

> Archive of the core result and its deep interpretation, after the M0–M4 run-batch
> (2026-06-19). Numbers: `../../RESULTS.md`. Living narrative: `../../paper/narrative.md`.
> This file is the stable, citable statement of what we concluded.

## The result in one paragraph

In a simulated society of LLM agents, we inject one ground-truthed update (an event's
day/place changes) and let it propagate through agent-to-agent conversation. The society
does **not** converge on the truth. It converges on a **corrupted/stale consensus** — the
superseded value persists, dominates, and spreads. This truth-decay is **robust**: it is
not fixed by scaling the model, is made *worse* by more connectivity, is not fixed by
changing the memory architecture, and is not fixed by a persistent authoritative source.
Only **directly overwriting every agent's memory every round** (a brute-force broadcast that
bypasses the social dynamics) restores the truth. The mechanism is a **dissociation between
speech and belief**: interventions readily change what agents *say*, but the society's
*held* belief is sticky — anchored by the network evidence-ratio, not by what any source can
be made to utter.

## The five load-bearing findings

1. **Truth-decay exists and is robust** (M0–M4). Truth-recall ≤ ~28% in every natural
   configuration; the society reliably reaches a corruption attractor.
2. **Capability does not fix it** (M0). mini→gpt-5.4→gpt-5.5: recall flat (16→21%). Worse,
   capability shifts the failure mode — weak models *forget*, strong models *confidently
   converge on the stale version*. **Scaling makes the society more confidently wrong.**
3. **Connectivity makes it worse** (M1). More agent-to-agent communication amplifies the
   stale version (Sat:Sun dominance ratio up to ~10× at high connectivity). **More
   communication, less truth** — the opposite of redundancy-as-error-correction.
4. **No realistic intervention restores it** (M2/M3 memory; M4-source authority). A
   currency-resolving memory looked like a cure (M2, n=3) but did not replicate (M3). A
   persistent authoritative re-broadcaster fails (M4-source, Δ ns). Only brute broadcast —
   bypassing the society — works (M4-broadcast, 99%).
5. **The mechanism is a SPEECH–BELIEF DISSOCIATION** (M4). The clean, tight-CI demonstration:
   under a persistent authoritative source the society *says* the truth (utterances Sun:Sat
   25:5 by round 5) yet *holds* the stale version (recall 3.8/25, unchanged). You can make
   the society parrot the truth; you cannot make it believe the truth without overwriting
   every memory.

## Why it matters (the deep interpretation)

- **For multi-agent LLM systems (engineering).** Agent-to-agent communication is a *lossy,
  corrupting channel for time-sensitive facts*, and the corruption is **not** an alignment
  or capability problem you can scale away, nor a reachability problem you can fix by adding
  an authoritative announcer. Any pipeline that relies on LLMs relaying state to each other
  is exposed to a silent, self-reinforcing drift toward stale/corrupted consensus.
- **For the "model collapse" lineage.** This is the *inference-time, social* analog of
  model collapse: degradation through communication rather than recursive training. And it
  has a feature training-time collapse does not foreground — the **dissociation**: the
  surface signal (speech) can be corrected while the latent consensus (belief) stays
  collapsed.
- **For collective epistemics.** The society's held belief is a **path-dependent
  entrenchment attractor**: the version established FIRST and BROADLY wins, and the held
  belief is decoupled from individual outputs (speech). The stale value is the original plan
  everyone knew from round 0, so it is entrenched from the start; the update arrives late and
  narrow and loses by path-dependence. Truth has to win the *aggregate* competition, not just
  be *uttered* — an authority that speaks the truth but is outnumbered by entrenched stale
  repetition loses.

## The mechanism, nailed down (P1-rec): TIMING, not recency

A clean timing contrast (same single broadcast to all agents, different round) refutes
recency and isolates entrenchment:
- **early broadcast (round 1, all) → 24.8/25** — and this *equals* broadcasting every round
  (24.8): you don't need to keep shouting, you need to be **first**.
- **late broadcast (round 5 = right before the probe, all) → 3.3/25** — and this *equals*
  doing nothing (baseline 3.0): a late correction at full breadth is worthless.
So WHEN the truth is established is decisive — early = total success, late = total failure,
independent of breadth and contrary to recency. The collective belief is locked in by
**first-mover / path-dependence**, which is *why* the decay is so robust and why every
realistic (late, narrow) intervention fails. This resonates with first-mover-advantage and
entrenchment in the misinformation literature — demonstrated here in a controlled society.

## The sharpest, most novel claim

**Speech ≠ belief in agent societies.** Standard interventions (a louder/persistent truth
source) move what agents *output* without moving the *collective belief*. This dissociation
— directly measured (say-ratio vs held-recall) with tight CIs — is the paper's spine and is,
as far as we know, unreported.

## Honest boundaries (what must still be done — see `../plans/path_to_publication.md`)

Single scenario ("repair drive" reschedule); keyword-based current/stale metric (the
provenance Sat/Sun-dominance signal agrees, which is reassuring); n=3–5 on M0–M3 (M4 is
n=5 with tight CIs); the say-ratio is a coarse dissociation proxy. None of these change the
qualitative chain, which is internally consistent and consistent with the 3-SMGA prior — but
generality (≥2 scenarios), a provenance fidelity metric, n≥8 + CIs, and a deeper
mechanistic probe of the dissociation are required before submission.
