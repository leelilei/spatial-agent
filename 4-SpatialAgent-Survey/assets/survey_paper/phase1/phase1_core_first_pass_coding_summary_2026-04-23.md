# Phase 1 Core First-Pass Coding Summary

Date: 2026-04-23

Purpose: record completion of the current `Core` first-pass coding work after representation adjudication.

## Completed now

- `15` paper-level rows are now coded directly in the stable table
- `2` split-required papers are materialized into `4` configuration rows
- total coded rows now available for the evidence map: `19`

The coding table is:

- `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`

## Split decisions materialized

### HC03 Concordia

Split into:

- `HC03A` Riverbend elections town configuration
- `HC03B` phone-calendar digital action-space configuration

Operational implication:

- the family is no longer blocked on a paper-level ambiguity
- downstream analysis can now show that Concordia spans both spatially local town interaction and weaker digital action-space exposure

### HC12 SimWorld

Split into:

- `HC12A` visual-GPS embodied interface
- `HC12B` scene-graph and abstract-layout interface

Operational implication:

- the family no longer needs to be held in an undifferentiated `L5_pending_split` state
- downstream evidence maps can show both an `L5` interface and a more abstract `L3` interface inside the same simulator family

## HC13 and HC14 now materialized

The two papers that previously sat outside first-pass coding because of missing local PDFs are now fully extracted locally and written into the stable table:

- `HC13` Fire evacuation cellular automata
- `HC14` Crowd evacuation disaster scenarios

Local extraction note:

- `spatial-agent-survey/scripts/pdf2text.py` now produces reusable `.fulltext.md` and `.meta.json` artifacts
- `HC13` extracted about `70k` text characters with `pdfplumber`
- `HC14` extracted about `77k` text characters with `pdfplumber`

Conservative coding implication:

- `HC13` remains `2D_grid / L3`
- `HC14` remains `graph_based / L3`
- both remain `Core`
- neither should be used to strengthen `L5` or direct-geometry claims

`HC01` TravelAgent was archived and full-text reviewed on `2026-04-27`. The paper is a strong `3D_engine / L5` spatial-interface case, but the current experiments are single-agent navigation and wayfinding rather than multi-agent social simulation. It should therefore be treated as Adjacent/boundary evidence unless the review scope is intentionally broadened.

## Practical consequence

The project has now completed the three immediate tasks that were previously pending:

1. first-pass coding of the ready queue
2. row-level splitting of the two split-required families
3. conservative row materialization for the previously blocked `HC13` and `HC14` papers

Round 3 supplementation has also now been materialized into the stable table:

- `R3-01` MineLand
- `R3-02` GATSim
- `R3-04` LLM-driven epidemic-economic dynamics

The next operational task is no longer representation adjudication or PDF acquisition.
It is now:

- evidence-map synthesis based on the stable `19` coded rows
- claim-check drafting against the updated evidence map

## 2026-04-27 addendum

HC13 and HC14 full-text adjudication is recorded in:

- `assets/survey_paper/phase1/phase1_hc13_hc14_fulltext_adjudication_2026-04-27.md`

Operational consequence:

- there is no remaining Core acquisition blocker in the current Phase 1 queue
- the stable Core first-pass table is now the operative source for downstream evidence-map work
- the previously open `L5 + observed_effect` gap is now closed by `R3-01`
