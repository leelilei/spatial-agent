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

## S5 tooling added

`sim/run_society_sweep.py` now runs repeated society simulations over memory
conditions, model choices, scheduling seeds, agent count, rounds, and turns. It
writes per-run logs plus:

```text
sim/runs/<sweep>/runs.json
sim/runs/<sweep>/aggregate.json
```

Example offline smoke test:

```bash
python sim/run_society_sweep.py \
  --mock --memory raw \
  --runs 2 --rounds 2 --agent-count 6 \
  --out-dir sim/runs/smoke_sweep_raw
```

Example real mini-model sweep:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 3 --rounds 5 --agent-count 6 \
  --out-dir sim/runs/mini_6agent_currency
```

The single-run `society.py` entrypoint also accepts `--agent-count` and `--seed`
so individual failures can be reproduced.

For 25-agent runs, use `--workers 4` as the current conservative concurrency
setting. It parallelizes independent same-round encounters and per-agent
consolidation without changing the encounter schedule. Higher values may be faster
but should be tested carefully because provider TLS/rate-limit noise can dominate.

## 6-Agent Mini Smoke

Command shape:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 1 --rounds 4 --turns 3 --agent-count 6 \
  --seed 31 \
  --out-dir sim/runs/mini_6agent_smoke
```

Observed C4 currency aggregate:

```text
condition   current  stale  unknown
GA             2       0       4
SMGA           2       0       4
```

Read: with six agents and only four rounds, the limiting factor was diffusion:
only Rosa and Oren learned the current Sunday/community-center update. The right
next move is not to over-read C4 from this smoke test; it is to run more schedules
and add explicit diffusion-sensitive probes.

However, the answers exposed a C2 anti-hallucination signal. Among the four
unknown answers, GA invented unsupported specifics such as "Sam's place" or
"tool drop-off table" in 3/6 agent interviews, while SMGA gave honest unknowns
in 0/6 unsupported-specific cases. `run_society_sweep.py` now records this as
`unsupported_specific` and `unsupported_specific_rate`.

## 25-Agent Pilot

Command shape:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 1 --rounds 3 --turns 2 --agent-count 25 \
  --seed 41 \
  --out-dir sim/runs/mini_25agent_pilot_retry
```

Observed C4 currency aggregate:

```text
condition   current  stale  unknown
GA             2       0       23
SMGA           2       0       23
```

Refined C2 unsupported-specific proxy after manual audit:

```text
condition   unsupported_specific
GA             7 / 25
SMGA           6 / 25
```

Read: at 25 agents with only three rounds and two utterances per encounter, both
conditions mostly fail by non-diffusion: only Rosa and Rey reach the current
Sunday/community-center answer. This is a useful baseline-scale smoke, not a
claim of SMGA superiority. It shows that the next 25-agent experiment needs a
stronger diffusion design (more rounds, more encounter opportunities, or explicit
event-publication mechanisms) plus formal C1/C2 interviews; otherwise C4 mostly
measures who happened to hear the injected update.

### Slightly Longer 25-Agent Pilot

Command shape:

```bash
python sim/run_society_sweep.py \
  --model gpt-5.4-mini \
  --memory ga --memory smga \
  --runs 1 --rounds 5 --turns 3 --agent-count 25 \
  --seed 41 \
  --out-dir sim/runs/mini_25agent_pilot_r5t3
```

Observed C4 currency aggregate:

```text
condition   current  stale  unknown
GA             2       14       9
SMGA           3        5      17
```

Refined C2 unsupported-specific proxy:

```text
condition   unsupported_specific
GA             4 / 25
SMGA          10 / 25
```

Read: adding rounds and turns changes the failure mode. GA spreads more content
but many agents keep or reconstruct the stale Saturday plan. SMGA has fewer stale
answers, but more agents answer with unsupported concrete details such as "garage
at 3". This is a useful negative/diagnostic result: SMGA's current-fact store
reduces some stale-plan persistence, but the retrieval/interview path still needs
a stronger "unknown unless supported" guard before the 25-agent setting can be
used as a clean baseline comparison.

## 25-Agent Longitudinal Pilot

Date: 2026-06-17. Fixed seed 41, 25 agents, `turns=3`, `workers=4`,
`model=gpt-5.4-mini`. The point of this run is vertical stretching: hold the
schedule seed fixed and compare the same society at longer horizons.

Command shape:

```bash
for rounds in 3 6 9; do
  python sim/run_society_sweep.py \
    --model gpt-5.4-mini \
    --memory ga --memory smga \
    --runs 1 --rounds "$rounds" --turns 3 \
    --agent-count 25 --seed 41 --workers 4 \
    --out-dir "sim/runs/longitudinal_25agent_seed41_workers4/rounds_$(printf '%03d' "$rounds")"
done
```

Aggregate:

```text
rounds  memory  current  stale  unknown  unsupported_specific
3       GA          4       0       21             2
3       SMGA        5       6       14             5
6       GA          3       2       20             1
6       SMGA       12       7        6             5
9       GA          0       0       25            14
9       SMGA       13       0       12             2
```

Rates:

```text
rounds  memory  current_rate  unsupported_specific_rate
3       GA          0.16              0.08
3       SMGA        0.20              0.20
6       GA          0.12              0.04
6       SMGA        0.48              0.20
9       GA          0.00              0.56
9       SMGA        0.52              0.08
```

Read: longitudinal stretching is informative. At three rounds the setting is still
mostly diffusion-limited. At six rounds, SMGA begins to recover the current
Sunday/community-center truth for many more agents than GA (12/25 vs 3/25), though
it still has stale and unsupported failures. At nine rounds, GA collapses into
unknown or unsupported-specific answers, while SMGA keeps 13/25 agents on the
current truth with no stale answers and only 2/25 unsupported-specific answers.

This is the strongest 25-agent pilot signal so far, but it remains a single seed.
The next clean baseline comparison should run multiple schedule seeds at the
25-agent scale and add an explicit evidence gate / unknown policy so SMGA does not
answer concretely unless a current fact directly supports the answer.
