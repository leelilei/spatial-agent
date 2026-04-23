# Phase 1 Core Coding Queue

Date: 2026-04-23

Purpose: record the transition from planning to completed first-pass coding for the currently usable `Core` rows.

## Current state

After the representation adjudication memo and first-pass coding work on `2026-04-23`, the current `Core` state is:

- `14` coded system/configuration rows are now available
- `3` core papers remain blocked by missing local full text

The seed table remains:

- `assets/survey_paper/phase1/phase1_core_evidence_table_seed_2026-04-23.csv`

The representation memo is:

- `assets/survey_paper/phase1/phase1_representation_adjudication_memo_2026-04-23.md`

The first-pass coding table is:

- `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`

The coding summary is:

- `assets/survey_paper/phase1/phase1_core_first_pass_coding_summary_2026-04-23.md`

## 1. First-pass coded rows

The following paper-level rows are now coded conservatively:

- `HC02` Generative Agents
- `HC04` Affordable Generative Agents
- `HC05` Artificial Leviathan
- `HC06` Project Sid
- `HC07` OASIS
- `HC08` Lyfe Agents
- `HC09` Spontaneous Emergence
- `HC10` Real world community oriented high-definition social simulation
- `HC15` CitySim
- `BK01` AgentSociety

Additionally, the former split-required families are now materialized as configuration rows:

- `HC03A` Concordia Riverbend elections town configuration
- `HC03B` Concordia phone-calendar digital action-space configuration
- `HC12A` SimWorld visual-GPS embodied interface
- `HC12B` SimWorld scene-graph and abstract-layout interface

Operational result:

- the ready queue is completed
- the split-required queue is completed

## 2. Acquisition-blocked queue

These rows should remain in `Core`, but they are not ready for stable coding yet because the local evidence base is incomplete.

- `HC01` TravelAgent
  Reason: still counted in `Core 15`, but there is no local PDF archived yet
- `HC13` Fire evacuation cellular automata
  Reason: local file is only a placeholder HTML page
- `HC14` Crowd evacuation disaster scenarios
  Reason: local file is only a placeholder HTML page

Working rule:

- keep these rows in the seed table
- mark them as provisional
- do not use them for strong representation claims until full text is local and verified

## 3. Practical implication

The project is no longer blocked on either:

- broad `Core` expansion
- first-pass coding of the usable core set
- row-level splitting of the ambiguous representation families

The immediate path is now:

1. continue PDF acquisition for the `3` blocked rows
2. build the evidence-map views from the `14` coded rows
3. only then judge whether any conceptual cell is truly empty

## 4. Seed-table convention

The seed CSV still retains split-aware or provisional values such as:

- `pending_extract`
- `pending_split`
- `mixed_L3_to_L5_split_required`
- `L5_present_but_split_required`

These are not ordinary final coding labels.

They remain useful as the audit trail behind the completed first-pass coding table.
