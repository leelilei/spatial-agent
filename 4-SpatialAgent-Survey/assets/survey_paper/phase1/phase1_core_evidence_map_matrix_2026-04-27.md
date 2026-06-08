# Phase 1 Core Evidence Map Matrix

Date: 2026-04-27

Purpose: summarize the stable Phase 1 `Core` coding table after `HC13`/`HC14` closure and targeted Round 3 integration, then determine whether any real structural gap still remains.

## Input

- Stable coding table: `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`
- Scope: `19` system/configuration rows from `17` paper-level `Core` items
- Boundary note: `HC01` TravelAgent is excluded from the stable Core matrix because it is now Adjacent/boundary evidence

## Top-level distributions

### Agent-accessible representation

| Level | Count | Notes |
|---|---:|---|
| `L1` | 1 | Only `HC03B` |
| `L2` | 0 | No stable row |
| `L3` | 15 | Dominant stable representation level |
| `L4` | 0 | No stable configurational row after targeted follow-up search |
| `L5` | 3 | `HC06`, `HC12A`, `R3-01` |

### Environment-side representation

| Environment | Count |
|---|---:|
| `text-only` | 3 |
| `2D_grid` | 5 |
| `graph_based` | 5 |
| `3D_engine` | 6 |

### Behavioral scale

| Behavioral scale | Count |
|---|---:|
| `interaction` | 3 |
| `emergent_social_structure` | 10 |
| `mixed` | 6 |

### Evidence status

| Evidence status | Count |
|---|---:|
| `observed_effect` | 9 |
| `designed_affordance_only` | 10 |
| `hypothesized_but_not_tested` | 0 |

## Key cross-cells

### Representation x evidence status

| Representation | `designed_affordance_only` | `observed_effect` | Total |
|---|---:|---:|---:|
| `L1` | 1 | 0 | 1 |
| `L3` | 7 | 8 | 15 |
| `L4` | 0 | 0 | 0 |
| `L5` | 2 | 1 | 3 |

### Environment x evidence status

| Environment | `designed_affordance_only` | `observed_effect` | Total |
|---|---:|---:|---:|
| `text-only` | 3 | 0 | 3 |
| `2D_grid` | 2 | 3 | 5 |
| `graph_based` | 1 | 4 | 5 |
| `3D_engine` | 4 | 2 | 6 |

## Reading

### What is now covered

- `HC13` and `HC14` are no longer blocker rows; evacuation and disaster-space evidence is stable inside the Core table.
- `R3-01`, `R3-02`, and `R3-04` are now materialized as stable Core rows after full-text sanity review.
- Observed-effect evidence already exists in:
  - `2D_grid` settings: `HC09`, `HC13`, `R3-04`
  - `graph_based` settings: `HC07`, `HC14`, `HC15`, `R3-02`
  - `3D_engine` settings: `HC10`, `R3-01`
- Stable `L5 + observed_effect` evidence now exists via `R3-01` MineLand.
- Built, urban, evacuation, and city/population environments are no longer missing as environment families.

### What remains structurally thin

- There is still no `L4` row. A targeted `L4`-only follow-up search documented in `assets/survey_paper/phase1/phase1_targeted_l4_search_memo_2026-04-27.md` did not identify any stable Core candidate under the current strict rule.
- `3D_engine` rows still lean toward `designed_affordance_only`, but the skew is reduced to `4/6`.
- `text-only` rows remain entirely `designed_affordance_only`.
- The only real empty structural cell that still persists is `L4`, and it should now be interpreted as a manuscript-level negative finding rather than an unsearched gap.

## Decision

- Do not reopen broad Core search.
- The current stable table is sufficient for evidence-map synthesis and claim-check work.
- Targeted Round 3 is now operationally closed because:
  - the `L5 + observed_effect` gap is closed by `R3-01`
  - the observed-effect balance is now `9` versus `10`
  - the admitted supplements already cover embodied 3D, graph-based urban mobility, and 2D proximity-mediated macro dynamics
- Keep `R3-03` as reserve only.
- Keep `R3-05` as Adjacent/boundary only.
- Treat `L4` as a real gap unless scope is later widened beyond the current manual.
