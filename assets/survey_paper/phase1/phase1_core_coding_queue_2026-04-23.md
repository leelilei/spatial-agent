# Phase 1 Core Coding Queue

Date: 2026-04-23

Purpose: move the project from "expand the core search surface" to "code the current Core 15 with explicit handling of missing full text and representation ambiguity."

## Queue split

The current `Core 15` now falls into three operational queues:

- `7` rows are ready for first-pass coding
- `5` rows need representation adjudication or configuration splitting
- `3` rows are blocked by missing local full text

The paired seed table is:

- `assets/survey_paper/phase1/phase1_core_evidence_table_seed_2026-04-23.csv`

## 1. Ready for first-pass coding

These rows already have enough local evidence to code conservatively at the current paper-level seed granularity.

- `HC02` Generative Agents
- `HC04` Affordable Generative Agents
- `HC05` Artificial Leviathan
- `HC07` OASIS
- `HC08` Lyfe Agents
- `HC09` Spontaneous Emergence
- `HC15` CitySim

Working rule:

- keep the current paper-level row
- code conservatively
- only escalate to adjudication if the first-pass extraction exposes genuine row-splitting pressure

## 2. Representation adjudication queue

These rows are stable `Core` papers, but they should not be treated as final one-row codings yet.

- `HC03` Concordia
  Reason: framework family spans multiple environment and interface configurations
- `HC06` Project Sid
  Reason: Minecraft backend is clearly rich, but the exact agent-facing representation still needs extraction
- `HC10` Real world community oriented high-definition social simulation
  Reason: GIS, BIM, and Unreal environment details may justify a higher representation level than the current conservative seed
- `HC12` SimWorld
  Reason: multiple observation modalities and embodiments mean a flat one-row coding would hide real variation
- `BK01` AgentSociety
  Reason: environment-side spatial structure is visible, but the agent-accessible representation is still unresolved

Working rule:

- do not reopen search because of these papers
- resolve them by method extraction, not by more screening
- split into multiple system or configuration rows only when the interface difference is real and behavior-relevant

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

1. code the `7` ready rows
2. resolve the `5` representation rows through method extraction
3. continue PDF acquisition for the `3` blocked rows
4. only then judge whether any true conceptual cell is still empty

## 5. Seed-table convention

The seed CSV intentionally keeps a small number of provisional values such as:

- `pending_extract`
- `pending_split`
- `L3_pending_extract`
- `L5_pending_split`
- `unknown_pending_extract`

These are not final coding labels.

They exist to prevent premature certainty while still letting the project move into systematic extraction now.
