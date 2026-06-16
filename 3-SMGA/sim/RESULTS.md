# Society sim — head-to-head results

> Date: 2026-06-16. Scenario: 4-agent neighborhood, 5 rounds, one currency stress —
> at round 1 the repair drive moves from "Saturday / front porch" to "Sunday /
> community center". Final probe to every agent: "When and where is the repair drive
> now?" Verdict by keyword (current = Sunday/community center; stale = Saturday/porch).
> Memory conditions identical except `retrieve()`: GA reflection (events + free-text
> reflections) vs SMGA v2 (currency-resolved current facts). Same conversation prompt.

## Currency coherence (agents on the CURRENT truth)

```text
run               current  stale  unknown
GA   (gpt-5.4)       3       0       1
SMGA (gpt-5.4)       4       0       0
GA   (gpt-5.4-mini)  0       0       4    <- GA reflection collapses on the weak model
SMGA (gpt-5.4-mini)  4       0       0    <- SMGA v2 holds
```

## Read

- SMGA v2 keeps agents on the current state better than GA reflection, and the gap
  **widens as the per-agent model weakens**: +1 agent (strong) -> +4 agents (mini).
- On mini, GA's free-text reflection LOST the updated time/place for every agent
  ("the notes don't say when/where"); SMGA v2's currency-resolved facts retained it.
- No agent went *stale* (acting on the superseded value) — consistent with strong
  models resisting that mode; the weak-model failure showed up as information LOSS.
- This is the SMGA v2 hypothesis, demonstrated in a LIVE multi-agent society (not a
  single-shot diagnostic): currency-tracked retrievable social memory maintains higher
  long-horizon coherence, and the advantage grows with model weakness.

## Caveats / next (S5)

```text
Preliminary: n=1 run, 4 agents, 1 probe, 1 scenario. To make it a result:
- more agents + rounds; multiple runs for variance.
- more coherence dimensions: C1 commitment-honoring, C2 belief-grounding/anti-hallucination.
- (run outputs in sim/runs/ are gitignored; this file captures the headline numbers.)
```
