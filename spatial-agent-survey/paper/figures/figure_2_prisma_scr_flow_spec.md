# Figure 2. PRISMA-ScR Screening and Evidence-Map Stabilization Flow

Draft status: figure spec aligned to the 2026-05-01 closure baseline.

## Purpose

Show that the review has two distinct counting layers:

- bibliographic screening counts from the formal Phase 1 screening sheet;
- row-level evidence-map stabilization after full-text rechecks, targeted widened review, and scope-boundary decisions.

This figure must not collapse `12` bibliographic `Core` records from the formal screening summary into the final `32` paper-level stable widened Core. The final evidence map is the result of later stabilization and row-level coding.

## Source Data

Primary screening summary:

- `spatial-agent-survey/results/logs/prisma_summary.json`
- `total_screened = 417`
- `Core = 12`
- `Adjacent = 42`
- `Foundational = 47`
- `Excluded = 316`
- `Excluded by reason`: `E1 = 85`, `E2 = 54`, `E3 = 177`

Stable evidence-map baseline:

- strict `anchor_core`: `17` paper-level sources, `19` rows
- stable widened Core: `32` paper-level sources, `34` rows
- row layers: `anchor_core = 19`, `bridge_core = 15`
- `HC01`: Adjacent / boundary / feasibility evidence
- `TW-02`: scope-boundary comparison, excluded from stable widened Core
- `BK02`: source-note-only bridge row pending full-text acquisition or downgrade

## Visual Structure

Use a two-panel vertical flow.

Panel A: PRISMA-ScR bibliographic screening

1. Records screened: `n = 417`
2. Included after screening:
   - `Core = 12`
   - `Adjacent = 42`
   - `Foundational = 47`
3. Excluded: `n = 316`
4. Exclusion reasons:
   - `E1 = 85`
   - `E2 = 54`
   - `E3 = 177`

Panel B: Evidence-map stabilization

1. Strict anchor baseline:
   - `17` paper-level sources
   - `19` coded rows
2. Widened bridge review:
   - added socially and spatially meaningful bridge cases
   - retained layer distinction
3. Scope-boundary decisions:
   - `HC01` retained as Adjacent / boundary
   - `TW-02` retained only as scope-boundary comparison
4. Stable widened Core:
   - `32` paper-level sources
   - `34` coded rows
   - `19` `anchor_core` rows
   - `15` `bridge_core` rows
   - `BK02` retained only as source-note bridge evidence until resolved

## Caption

Figure 2. PRISMA-ScR screening and evidence-map stabilization flow. The bibliographic screening stage starts from `417` screened records and separates `Core`, `Adjacent`, `Foundational`, and excluded records. The evidence-map stage then operates at the `system / environment configuration` level, preserving the strict `anchor_core` baseline while adding selected `bridge_core` rows under widened scope rules. Counts therefore differ by layer: the final stable widened Core contains `32` paper-level sources and `34` coded rows. `HC01` and `TW-02` are retained as boundary materials rather than counted in the stable widened-Core evidence map; `BK02` remains a source-note-only bridge row until resolved.

## Rendering Notes

- Label Panel A as `Bibliographic screening`.
- Label Panel B as `Evidence-map stabilization`.
- Use different visual treatment for `Adjacent`, `Foundational`, and `Excluded` so readers do not interpret them as discarded evidence.
- Add a footnote: `Rows count system/environment configurations, not only papers.`
