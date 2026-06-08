# Phase 1 Widened Core Evidence Map

Date: 2026-04-27

CSV companion:

- `assets/survey_paper/phase1/phase1_widened_core_evidence_map_2026-04-27.csv`

Purpose: provide a widened-Core evidence-map draft after local bridge-core reclassification. This file does not replace the strict `anchor_core` baseline.

## Scope

Included rows:

- `19` strict `anchor_core` system/configuration rows
- `15` accepted `bridge_core` rows
- `34` total widened-Core rows

Excluded from count:

- `HC01`, kept as Adjacent/boundary evidence because the full-text adjudication confirms a rich `L5` interface but only single-agent navigation rather than stable multi-agent social-behavior evidence
- `LD01`, kept as reserve
- `TW-02`, excluded from stable widened-Core because citation-network science-of-science is outside the accepted spatial-social bridge scope
- `TW-10`, kept as adjacent because VR is mainly modality/presentation rather than clear agent-facing spatial context

Paper-level count:

- `17` strict `anchor_core` papers
- `15` accepted `bridge_core` papers
- `32` total widened-Core papers

## Core Layer Distribution

| Core layer | Rows |
|---|---:|
| `anchor_core` | 19 |
| `bridge_core` | 15 |
| **Total** | **34** |

## Agent-Accessible Representation Distribution

| Representation | Rows |
|---|---:|
| `L1` | 1 |
| `L2` | 8 |
| `L3` | 18 |
| `L4` | 1 |
| `L5` | 6 |
| **Total** | **34** |

## Representation by Core Layer

| Core layer | L1 | L2 | L3 | L4 | L5 | Total |
|---|---:|---:|---:|---:|---:|---:|
| `anchor_core` | 1 | 0 | 15 | 0 | 3 | 19 |
| `bridge_core` | 0 | 8 | 3 | 1 | 3 | 15 |
| **Total** | **1** | **8** | **18** | **1** | **6** | **34** |

## Evidence Status

| Evidence status | Rows |
|---|---:|
| `observed_effect` | 19 |
| `designed_affordance_only` | 15 |
| `hypothesized_but_not_tested` | 0 |
| **Total** | **34** |

## Representation by Evidence Status

| Representation | Designed affordance only | Observed effect | Total |
|---|---:|---:|---:|
| `L1` | 1 | 0 | 1 |
| `L2` | 4 | 4 | 8 |
| `L3` | 7 | 11 | 18 |
| `L4` | 0 | 1 | 1 |
| `L5` | 3 | 3 | 6 |
| **Total** | **15** | **19** | **34** |

## Environment-Side Representation

| Environment-side representation | Rows |
|---|---:|
| `2D_grid` | 5 |
| `text-only` | 4 |
| `3D_engine` | 16 |
| `graph_based` | 9 |
| **Total** | **34** |

## Reading

The widened-Core pass solves the immediate corpus-size problem at the row level:

- row-level evidence map rises from `19` to `30`
- after the L4 robustness search, row-level evidence map rises further to `31`
- after the targeted widened P0 and optimistic reserve rechecks, the stable widened-Core map reaches `34` rows once `HC01` is returned to Adjacent/boundary status
- paper-level corpus rises from `17` to `32`

It also materially improves the thin representation slices:

- `L2` rises from `0` to `8`
- `L5` rises from `3` to `6`
- `observed_effect` becomes slightly more common than `designed_affordance_only`

The original local widening pass did not solve `L4`, but the later robustness search identified one widened-bridge `L4` case:

- `L4R-01` Network formation and dynamics among multi-LLMs is coded as `bridge_core / L4`
- `BK07` and `BK08` are accepted as `bridge_core` but remain `L3`, because global network/community metrics appear to be researcher-side analysis rather than agent-facing global abstract structure
- `HC01` is no longer counted in the stable widened-Core table because later full-text adjudication keeps it as Adjacent/boundary evidence
- `TW-02` CiteAgent is excluded from stable widened Core because it is farther from the spatial-social target than online-community and social-network bridge cases
- therefore `L4` is no longer entirely absent in widened Core, but it remains absent from strict `anchor_core` and appears only in a single digital-network bridge case

## Claim Discipline

Do not flatten the evidence:

- `anchor_core` remains the strict baseline for the strongest descriptive mapping.
- `bridge_core` can support widened-Core distributional discussion and bridge-level observations.
- `bridge_core` should not be used alone for strong mechanism claims.
- Any statement about `L2` coverage should specify that the recovered `L2` slice is mainly bridge-core human-agent, VR, metaverse, NPC, and tutoring interaction evidence.
- Any statement about `L4` should state that it appears only after widening into digital-network bridge evidence, not in the strict physical/virtual spatial-social anchor corpus.
