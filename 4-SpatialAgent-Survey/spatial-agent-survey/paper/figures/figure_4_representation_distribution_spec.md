# Figure 4. Evidence-Map Matrix: Representation, Behavior, and Evidence Status

Draft status: figure spec aligned to the 2026-05-01 closure baseline.

## Purpose

Show the main empirical result of the evidence map: representation level, behavioral scale, evidence status, and core layer jointly reveal a corpus concentrated at `L3`, sparse at `L4`, and uneven in observed-effect support.

## Matrix Data

Primary matrix rows:

- `L1 labels`
- `L2 semantic scene`
- `L3 local relations`
- `L4 global abstract`
- `L5 geometry / embodiment`

Primary matrix columns:

- `interaction`
- `emergent_social_structure`
- `mixed`

Cell counts should split `designed_affordance_only` and `observed_effect`.

| level | interaction | emergent_social_structure | mixed |
|---|---|---|---|
| `L1` | `1 designed` | `0` | `0` |
| `L2` | `4 designed + 4 observed` | `0` | `0` |
| `L3` | `2 designed` | `3 designed + 8 observed` | `2 designed + 3 observed` |
| `L4` | `0` | `1 observed` | `0` |
| `L5` | `2 observed` | `1 designed` | `2 designed + 1 observed` |

Secondary marginal bars by representation level and core layer:

| level | anchor_core rows | bridge_core rows | total rows |
|---|---:|---:|---:|
| `L1` | 1 | 0 | 1 |
| `L2` | 0 | 8 | 8 |
| `L3` | 15 | 3 | 18 |
| `L4` | 0 | 1 | 1 |
| `L5` | 3 | 3 | 6 |
| total | 19 | 15 | 34 |

## Required Visual Message

- The strict nucleus is concentrated at `L3`.
- The widened bridge layer contributes all `L2` rows and the only admitted `L4` row.
- `L4` remains a gap in the strict anchor core, not a solved layer.
- Observed effects exist, but they are uneven by representation level and behavioral scale.
- Bridge recovery is not anchor evidence.

## Caption

Figure 4. Evidence-map matrix crossing agent-accessible spatial representation with behavioral scale and evidence status. The current literature is not spatially empty: it contains local, semantic, and embodied spatial interfaces and several reported observed effects. The gap is specifically configurational: `L4` appears only once, only in a widened digital-network bridge row, and remains absent from the strict `anchor_core`. The marginal bars keep `anchor_core` and `bridge_core` separate so bridge recovery is not mistaken for strict anchor evidence.

## Rendering Notes

- Use a matrix as the primary visual.
- Use small exact counts in nonzero cells.
- Use two cell colors or split tokens for `designed_affordance_only` versus `observed_effect`.
- Add small marginal bars for `anchor_core` and `bridge_core` by representation level.
- Include callouts for `L3 dense center`, `L4 bridge-only`, and `observed effects uneven`.
