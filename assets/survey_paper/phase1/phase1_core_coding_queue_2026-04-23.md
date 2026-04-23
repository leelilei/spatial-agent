# Phase 1 Core Coding Queue

Date: 2026-04-23

Purpose: move the project from "expand the core search surface" to "code the current Core 15 with explicit handling of missing full text and the remaining split-required cases."

## Queue split

After the representation adjudication memo on `2026-04-23`, the current `Core 15` falls into three operational queues:

- `10` rows are ready for first-pass coding
- `2` rows require configuration or interface splitting before final coding
- `3` rows are blocked by missing local full text

The paired seed table is:

- `assets/survey_paper/phase1/phase1_core_evidence_table_seed_2026-04-23.csv`

The representation memo is:

- `assets/survey_paper/phase1/phase1_representation_adjudication_memo_2026-04-23.md`

## 1. Ready for first-pass coding

These rows already have enough local evidence to code conservatively at the current paper-level seed granularity.

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

Working rule:

- keep the current paper-level row
- code conservatively
- only escalate to adjudication if the first-pass extraction exposes genuine row-splitting pressure

## 2. Split-required queue

These rows are stable `Core` papers, but they should not be treated as final one-row codings yet because the paper-level row still collapses materially different interfaces.

- `HC03` Concordia
  Reason: framework family spans multiple environment and interface configurations
- `HC12` SimWorld
  Reason: multiple observation modalities and embodiments mean a flat one-row coding would hide real variation

Working rule:

- do not reopen search because of these papers
- split into multiple system or configuration rows only when the interface difference is real and behavior-relevant
- treat the split question as resolved conceptually, but not yet materialized into row-level coding

## 3. Acquisition-blocked queue

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

## 4. Practical implication

The project is no longer blocked on broad `Core` expansion.

The immediate path is:

1. code the `10` ready rows
2. split `HC03` and `HC12` into coding-ready configuration rows
3. continue PDF acquisition for the `3` blocked rows
4. only then judge whether any true conceptual cell is still empty

## 5. Seed-table convention

The seed CSV intentionally keeps a small number of split-aware or provisional values such as:

- `pending_extract`
- `pending_split`
- `mixed_L3_to_L5_split_required`
- `L5_present_but_split_required`

These are not ordinary final coding labels.

They exist to prevent premature certainty while still letting the project move into systematic coding now.
