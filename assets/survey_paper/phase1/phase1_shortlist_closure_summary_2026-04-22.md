# Phase 1 Shortlist Closure Summary

Date: 2026-04-22

Purpose: provide one place to see the current closed-form status of the shortlisted Phase 1 papers after the batch reviews and boundary decisions completed on 2026-04-22.

## Current outcome

- Final `Core` shortlist count: `14`
- Final `Adjacent` shortlist count: `10`
- Final `Excluded` shortlist count: `2`

## 2026-04-27 addendum

`HC01` TravelAgent is no longer an acquisition blocker. A user-supplied arXiv preprint PDF was archived at:

- `assets/survey_paper/pdfs/phase1_core/00_HC01_TravelAgent_Noyman2025.pdf`

Full-text review changes its operational use:

- representation evidence is strong: `3D_engine / L5`
- current behavior evidence is single-agent navigation and wayfinding
- multi-agent interaction and social dynamics are future work, not current evidence

Decision:

- treat `HC01` as Adjacent/boundary evidence unless the review scope is intentionally broadened
- do not use it as stable Core evidence for multi-agent social-behavior claims
- `HC13` and `HC14` were subsequently resolved through local full-text extraction and stable first-pass coding

## 2026-04-27 Round 3 addendum

The counts above remain the closure state for the original shortlist only.

After targeted Round 3 integration, the operative stable Core table now contains:

- `19` system/configuration rows
- `17` paper-level Core items
- newly admitted items: `R3-01`, `R3-02`, `R3-04`

## 2026-04-27 widened-core addendum

The `17` paper-level figure should now be treated as the strict `anchor_core` baseline rather than the final desired corpus size.

Under the widened boundary documented in `phase1_core_boundary_relaxation_memo_2026-04-27.md`, the project is reopening a `bridge_core` reclassification pass over already known local cases.

Live bridge-core queue:

- `assets/survey_paper/phase1/phase1_bridge_core_reclassification_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_bridge_core_reclassification_2026-04-27.md`

Expected effect:

- immediate bridge promotions can move the paper-level Core count from `17` to about `23`
- immediate plus quick-recheck bridge promotions can move it from `17` to about `28`
- only after that local widening pass should new search be used to top the corpus up toward `30`

## Core set

Previously retained high-confidence anchors:

- `HC02` Generative Agents
- `HC03` Concordia
- `HC04` Affordable Generative Agents
- `HC05` Artificial Leviathan
- `HC06` Project Sid
- `HC07` OASIS

Newly stabilized through the 2026-04-22 review pass:

- `HC08` Lyfe Agents
- `HC09` Spontaneous Emergence
- `HC10` Real world community oriented high-definition social simulation
- `HC12` SimWorld
- `HC13` Fire evacuation cellular automata
- `HC14` Crowd evacuation disaster scenarios
- `HC15` CitySim
- `BK01` AgentSociety

## Adjacent set

- `HC01`
- `HC11`
- `BK02`
- `BK03`
- `BK04`
- `BK05`
- `BK06`
- `BK07`
- `BK08`
- `LD01`

`LD01` remains only as a low-priority adjacent tail reference, not as an active Core candidate.

## Excluded tail

- `LD02`
- `LD03`

## Still incomplete at the evidence-acquisition level

- `BK08`: official endpoint still returned anti-bot HTML, but this no longer blocks screening because the paper has been finalized as `Adjacent`

## Policy note

Structured digital social platforms and online communities are now treated as relevant boundary cases, not default `Core` environments. This is why `BK07` and `BK08` settle in `Adjacent`, while `OASIS` remains in `Core` as an environment-architecture anchor rather than only an online-behavior paper.

## Files to use from here

- `phase1_core_first_pass_coding_2026-04-23.csv`
- `phase1_core_evidence_map_matrix_2026-04-27.md`
- `phase1_batch1_final_adjudication_2026-04-22.csv`
- `phase1_batch2_final_adjudication_2026-04-22.csv`
