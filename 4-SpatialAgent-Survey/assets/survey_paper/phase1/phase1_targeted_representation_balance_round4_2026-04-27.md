# Phase 1 Targeted Representation-Balance Round 4

Date: 2026-04-27

Purpose: reopen a narrow supplementation pass because the current stable `Core` representation mix is too skewed for clean manuscript interpretation, even though the earlier broad-search and `L4`-only decisions remain documented.

## Why reopen now

Current stable `Core` base:

- `19` system/configuration rows
- `17` paper-level Core items

Current representation distribution:

- `L1 = 1` (`5.3%`)
- `L2 = 0` (`0.0%`)
- `L3 = 15` (`78.9%`)
- `L4 = 0` (`0.0%`)
- `L5 = 3` (`15.8%`)

Current environment distribution:

- `text-only = 3` (`15.8%`)
- `2D_grid = 5` (`26.3%`)
- `graph_based = 5` (`26.3%`)
- `3D_engine = 6` (`31.6%`)

Current evidence-status distribution:

- `observed_effect = 9` (`47.4%`)
- `designed_affordance_only = 10` (`52.6%`)

Most problematic balance signals:

- `L2 = 0`
- `L4 = 0`
- `L3` dominates the table at nearly four-fifths of all rows
- all current `text-only` rows are still `designed_affordance_only`

So the issue is no longer simple evidence acquisition. It is manuscript-facing balance.

## Reopen rule

This is **not** a new broad expansion round.

This pass should only admit candidates that help repair a real distributional weakness while still respecting the current `Core` boundary as much as possible:

1. LLM/VLM/generative agents must remain part of the decision architecture.
2. The system must still be multi-agent, population-level, or clearly group-based.
3. The environment must remain spatially recognizable.
4. The new candidate must improve at least one currently skewed slice rather than merely add another ordinary `L3` case.

## Priority order

### Priority A: true `L2` Core or near-Core candidate

Best-case repair target:

- agent receives location descriptions or scene descriptions without explicit topology
- system is still multi-agent and socially interactive
- environment is not just a generic benchmark board

Reason:

- `L2 = 0` is now the most obvious representation-balance weakness after the `L4` negative finding was already documented.

### Priority B: `text-only + observed_effect`

Best-case repair target:

- text-mediated environment
- still reports observed behavior differences tied to resource competition, layout, movement, or interaction opportunity

Reason:

- the current `text-only` slice exists, but all of it is `designed_affordance_only`

### Priority C: extra `L5` or embodied breadth only if it also fixes a weak slice

Reason:

- `L5` is thin, but no longer empty after `R3-01`
- adding more `L5` rows that are only embodied cooperation benchmarks does not solve the current ratio problem by itself

## Current candidate slate from this reopening

### S4-01 INDOORWORLD

Primary sources:

- `https://aclanthology.org/2025.findings-emnlp.590/`
- `https://aclanthology.org/2025.findings-emnlp.590.pdf`
- DOI: `10.18653/v1/2025.findings-emnlp.590`

Why it matters:

- strong `text-based` multi-agent office environment
- explicit social behavior plus physical-task coupling
- experiments directly test `multi-agent collaboration`, `resource competition`, and `spatial layout`
- text-mediated environment is not merely decorative; it is used to study behavior under alternative office designs

Conservative provisional reading:

- likely `Core`
- likely `text-only / L3 / observed_effect`

Operational value:

- does not fix `L2`
- does fix the weaker `text-only` slice by adding an observed-effect case

Decision:

- advance first

### S4-02 BOOKWORLD

Primary sources:

- `https://aclanthology.org/2025.acl-long.773/`
- `https://aclanthology.org/2025.acl-long.773.pdf`
- DOI: `10.18653/v1/2025.acl-long.773`

Why it looked useful:

- explicit multi-agent social simulation framing
- textual world model includes location profiles plus a distance graph
- agents interact with both characters and environments

Why it is weaker than `INDOORWORLD`:

- primary evaluation target is story quality and fidelity to source novels
- spatial structure is present, but manuscript-facing evidence is not primarily about spatial-social effect estimation

Conservative provisional reading:

- likely `L3`, not `L2`
- likely `designed_affordance_only`
- may become `Adjacent` or reserve instead of stable `Core`

Decision:

- advance cautiously after `INDOORWORLD`

### S4-03 Cognitive Agents in Urban Mobility

Existing source base:

- already screened in `phase1_targeted_core_supplementation_round3_screening_2026-04-27.md`

Why it remains relevant:

- it is already the cleanest existing reserve row if we later need one more observed-effect urban case quickly

Why it is not the main repair target:

- it is still another likely `L3` row
- it does not solve `L2 = 0`

Decision:

- keep as reserve only

### S4-04 CoELA and similar embodied cooperation papers

Why they remain secondary:

- they help `L5` breadth
- they do not fix the manuscript’s most awkward imbalance, which is the near-absence of lower-structure intermediate cases

Decision:

- only reopen if the project deliberately widens toward embodied cooperation boundary evidence

### S4-05 Social-VR and role-play bridge cases

Examples:

- `Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios`
- `Building LLM-based AI Agents in Social Virtual Reality`
- `ELLMA-T`

Current reading:

- these are the nearest visible `L2` bridge cases
- however, they are mostly human-agent or single-NPC interaction systems rather than stable multi-agent social simulation

Decision:

- do not silently promote them into stable `Core`
- keep them available only if the manuscript later adds an explicit bridge layer beyond strict `Core`

## Working interpretation

At this point:

- `L4` still looks like a true negative finding under the current strict rule
- `L2` looks less like a missing-search problem and more like a boundary-layer problem, because most visible candidates cluster in `Adjacent` social-VR or situated human-agent interaction rather than stable multi-agent social simulation
- `text-only + observed_effect` looks repairable, with `INDOORWORLD` as the first serious candidate

## Next operational step

1. acquire and locally archive `INDOORWORLD`, then do a full-text sanity check
2. run one more very narrow `L2`-focused search aimed at social-VR / metaverse / indoor role-play multi-agent cases
3. if that pass still finds no stable `L2` Core hit, document `L2` as mostly a bridge/Adjacent layer rather than distorting the stable Core table
