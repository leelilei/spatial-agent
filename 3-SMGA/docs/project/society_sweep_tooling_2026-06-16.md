# Society Sweep Tooling

> Date: 2026-06-16
> Status: implemented tooling; real multi-run LLM sweep still pending.

## Why This Exists

The first society result in `sim/RESULTS.md` is a useful signal, but it is still
one run, four agents, one currency probe. The next step is S5: make the live
multi-agent simulation repeatable enough to estimate variance before expanding
the scenario or moving the evaluation back into `3-SMGA-EVAL`.

## What Changed

`sim/society.py` now supports:

```text
--agent-count  number of agents from the demo roster
--seed         deterministic encounter schedule seed
```

It also writes run artifacts with explicit UTF-8 encoding.

`sim/run_society_sweep.py` now runs repeated simulations across:

```text
memory condition: raw / ga / smga
model: config model or explicit --model
schedule seed: base seed + run index
agent count
round count
turn count
```

It writes:

```text
runs.json       one row per simulation run
aggregate.json  grouped current/stale/unknown counts and per-run variance
```

## Smoke Test

Offline smoke command:

```bash
python sim/run_society_sweep.py \
  --mock --memory raw \
  --runs 2 --rounds 2 --agent-count 6 \
  --seed 21 \
  --out-dir sim/runs/smoke_sweep_raw
```

Observed aggregate:

```text
model=mock, memory=raw, runs=2, agents_total=12
current=0, stale=4, unknown=8
```

This is not a scientific result; it only verifies the scheduler, artifact layout,
mechanical interview path, and aggregation.

## Next Real Run

Recommended first real S5 run:

```powershell
$env:FHL_API_KEY=[Environment]::GetEnvironmentVariable('FHL_API_KEY','User')
python sim/run_society_sweep.py `
  --model gpt-5.4-mini `
  --memory ga --memory smga `
  --runs 3 --rounds 5 --agent-count 6 `
  --out-dir sim/runs/mini_6agent_currency
```

Success criterion:

```text
SMGA current_rate > GA current_rate, with a nonzero gap across repeated schedules.
```

If the gap holds, add two more interviews:

```text
C1 commitment-honoring: who still plans to help / who knows the new commitment?
C2 anti-hallucination: does the agent invent unsupported time/place/helper details?
```

The current runner is intentionally narrow: it supports C4 currency coherence
first, because that is the signal already observed in the single-run society demo.

## First Real 6-Agent Smoke

Command:

```powershell
$env:FHL_API_KEY=[Environment]::GetEnvironmentVariable('FHL_API_KEY','User')
python sim/run_society_sweep.py `
  --model gpt-5.4-mini `
  --memory ga --memory smga `
  --runs 1 --rounds 4 --turns 3 --agent-count 6 `
  --seed 31 `
  --out-dir sim/runs/mini_6agent_smoke
```

Result:

```text
condition   current  stale  unknown
GA             2       0       4
SMGA           2       0       4
```

Interpretation:

```text
The six-agent smoke did not reproduce the 4-agent C4 gap. The bottleneck was
diffusion: only Rosa and Oren learned the Sunday/community-center update within
four rounds. This is useful, because it separates "memory currency" from
"information propagation through the society".
```

Secondary observation:

```text
GA unsupported_specific:   3/6
SMGA unsupported_specific: 0/6
```

GA often answered unknown cases with unsupported concrete details ("Sam's place",
"tool drop-off table"). SMGA more often said the notes did not specify the
time/place. The sweep runner now tracks `unsupported_specific` as a lightweight
C2 anti-hallucination proxy.
