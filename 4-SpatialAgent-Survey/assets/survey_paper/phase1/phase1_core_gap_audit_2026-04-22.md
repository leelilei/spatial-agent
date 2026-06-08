# Phase 1 Core Gap Audit

Date: 2026-04-22

Purpose: determine, after `HC13`/`HC14` closure and targeted Round 3 integration, whether any real structural gap still remains in the stable Core table.

## Bottom line

Do **not** reopen broad Core expansion.

The current stable Core base is now sufficient for evidence-map synthesis:

- the stable first-pass table contains `19` system/configuration rows from `17` paper-level Core items
- `HC13` and `HC14` are no longer acquisition blockers
- `HC01` is resolved as Adjacent/boundary evidence rather than stable Core social-behavior evidence
- `R3-01`, `R3-02`, and `R3-04` are now materialized in the stable table
- the remaining thin cells are now residual structural gaps, not search gaps

## Matrix snapshot

Source files:

- `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`
- `assets/survey_paper/phase1/phase1_core_evidence_map_matrix_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_core_evidence_map_matrix_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_targeted_l4_search_memo_2026-04-27.md`

Key stable distributions:

- representation: `L1=1 / L3=15 / L4=0 / L5=3`
- evidence status: `observed_effect=9 / designed_affordance_only=10`
- environment-side representation: `text-only=3 / 2D_grid=5 / graph_based=5 / 3D_engine=6`

Most important cross-cells:

- `L3 + observed_effect = 8`
- `L5 + designed_affordance_only = 2`
- `L5 + observed_effect = 1`
- `3D_engine + observed_effect = 2`, and one of those rows is now `L5`

## What is now covered

The current stable Core set already covers:

- grid or cellular social simulation: `HC02`, `HC04`, `HC09`, `HC13`, `R3-04`
- graph or road-network environments: `HC07`, `HC14`, `HC15`, `R3-02`, `BK01`
- 3D-engine backends: `HC06`, `HC08`, `HC10`, `HC12A`, `HC12B`, `R3-01`
- evacuation and disaster-space evidence: `HC13`, `HC14`
- urban or city-scale observed-effect cases: `HC10`, `HC14`, `HC15`, `R3-02`
- embodied `L5 + observed_effect` evidence: `R3-01`
- proximity-mediated epidemic-economic macro dynamics: `R3-04`

So the earlier reason for caution around `HC13` and `HC14` is gone. The evidence map is no longer blocked on evacuation-space acquisition.

## What remains structurally thin

### A. No stable `L4` row

This remains a true empty cell.

A targeted `L4`-only follow-up search is now documented in `phase1_targeted_l4_search_memo_2026-04-27.md`.

That pass did **not** identify any stable `Core` candidate under the current strict rule that the agent must directly receive global configurational indicators such as `integration`, `depth`, `control`, or `choice`.

The nearest urban-planning and participatory-planning cases still stop at maps, road graphs, direction-distance cues, local accessibility information, or planner-side evaluation metrics rather than agent-facing configurational state.

At this point the absence is more plausibly a literature pattern than a retrieval failure.

### B. `L5` evidence is still thin even though the empty cell is closed

The previous `L5 + observed_effect` gap is now closed by `R3-01`, but the `L5` slice is still small overall.

Current `L5` coverage exists only in:

- `HC06` Project Sid
- `HC12A` SimWorld visual-GPS interface
- `R3-01` MineLand

Only one of these three rows is `observed_effect`.

### C. `3D_engine` evidence is improved but still somewhat skewed

There are now `6` stable `3D_engine` rows, and `2` report observed effects:

- `HC10`
- `R3-01`

This is much better than the earlier state, but the family still leans toward `designed_affordance_only`.

## What is no longer a live gap

These no longer justify new broad search:

- "need valid PDFs for HC13 and HC14"
- "need at least one evacuation-space Core paper"
- "need any graph-based observed-effect evidence"
- "need any city or crowd observed-effect evidence"
- "need one stable `L5 + observed_effect` Core row"
- "need a targeted `L4`-only follow-up search"

Those issues are now closed inside the stable table.

## Decision

Current recommendation: **hold broad Core expansion closed**.

Current recommendation: **treat targeted Round 3 as closed**.

Keep:

1. `R3-03` reserve only
2. `R3-05` Adjacent / boundary only

## Operational consequence

The next practical task is not more search.

It is:

1. use the stable evidence-map and claim-check outputs from the current `19` rows as the manuscript baseline
2. write the manuscript-facing interpretation that `L4` remains absent even after a targeted follow-up search, while `L5 + observed_effect` is now present but sparse
3. reopen search only if the project later widens scope toward Adjacent bridge systems or decides to count planner-side configurational analytics that are not yet agent-accessible under the current manual
