# CityIntent v0.3 Annotation Model Dry Run

Date: 2026-07-02

Status: rubric debugging only; not human validation.

## Setup

Two deliberately different model-review profiles independently labeled the 16
blinded v0.3 audit items. The runner used the real configured API and wrote its
outputs under the audit package's `dry_run/` directory. It never wrote either
human annotation CSV.

## Agreement

| Dimension | Exact agreement | Cohen's kappa |
|---|---:|---:|
| Completion | 0.750 | 0.522 |
| Feasibility | 0.688 | 0.208 |
| Replanning | 0.875 | 0.652 |
| Evidence sufficient | 1.000 | 1.000 |

The low feasibility agreement exposed packet ambiguity around resolved routes
and rejected actions. The packet now shows proposed paths, executed traversals,
and accepted outcomes separately.

## Construct Findings

The most important finding was systematic, not a model-scoring result:

- v0.3 could award meeting credit from the primary agent's venue presence even
  though no accepted evidence showed that Ben arrived.
- school arrival could stand in for completion of child pickup.
- the weighted completion sum allowed constraints to mask a missing core
  outcome.

CityIntent `1.0-rc1` addresses these with accepted counterpart interactions,
typed `child_pickup` service evidence, and separate outcome/process/constraint
scores.

The model reviewers also made isolated route-reading errors even after packet
improvements. Their labels therefore cannot be used as ground truth. Two real,
independent annotators remain the release gate.
