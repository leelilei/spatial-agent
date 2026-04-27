# Phase 1 Core First-Pass Coding Summary

Date: 2026-04-23

Purpose: record completion of the current `Core` first-pass coding work after representation adjudication.

## Completed now

- `10` paper-level rows coded directly from the ready queue
- `2` split-required papers materialized into `4` configuration rows
- total coded rows now available for the evidence map: `14`

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

## Remaining blocked work

Only two acquisition-blocked rows remain outside first-pass coding:

- `HC13` Fire evacuation cellular automata
- `HC14` Crowd evacuation disaster scenarios

`HC01` TravelAgent was archived and full-text reviewed on `2026-04-27`. The paper is a strong `3D_engine / L5` spatial-interface case, but the current experiments are single-agent navigation and wayfinding rather than multi-agent social simulation. It should therefore be treated as Adjacent/boundary evidence unless the review scope is intentionally broadened.

## Practical consequence

The project has now completed the two immediate tasks that were previously pending:

1. first-pass coding of the ready queue
2. row-level splitting of the two split-required families

The next operational task is no longer representation adjudication.
It is either:

- continued acquisition for the remaining `2` blocked core papers
- or evidence-map synthesis based on the `14` coded rows already available

After the HC01 review, the acquisition path is narrower:

- continue acquisition for `HC13` and `HC14`
- keep the Core first-pass table at `14` rows until those papers are resolved
