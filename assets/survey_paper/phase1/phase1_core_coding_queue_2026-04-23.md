# Phase 1 Core Coding Queue

Date: 2026-04-23

Purpose: record the transition from planning to completed first-pass coding for the currently usable `Core` rows.

## Current state

After the representation adjudication memo, the original first-pass coding work on `2026-04-23`, and the local `pdf2text` extraction plus HC13/HC14 full-text adjudication on `2026-04-27`, the current `Core` state is:

- `19` coded system/configuration rows are now available
- there is no remaining Core PDF-acquisition blocker in the current queue
- `HC01` remains resolved as Adjacent/boundary evidence rather than stable Core social-behavior evidence
- `R3-01`, `R3-02`, and `R3-04` are now materialized in the stable coding table after Round 3 full-text sanity review
- a targeted `L4`-only follow-up search has now been completed and did not identify any new stable Core candidate

The seed table remains:

- `assets/survey_paper/phase1/phase1_core_evidence_table_seed_2026-04-23.csv`

The representation memo is:

- `assets/survey_paper/phase1/phase1_representation_adjudication_memo_2026-04-23.md`

The first-pass coding table is:

- `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`

The coding summary is:

- `assets/survey_paper/phase1/phase1_core_first_pass_coding_summary_2026-04-23.md`

## 2026-04-27 balance addendum

The stable table remains valid as the current baseline, but the representation mix is now judged too skewed for clean manuscript interpretation:

- `L1 = 1`
- `L2 = 0`
- `L3 = 15`
- `L4 = 0`
- `L5 = 3`

In addition, the current `text-only` slice still has no `observed_effect` row.

Operational consequence:

- reopen a **narrow** representation-balance supplementation pass
- keep this narrower than the earlier broad Core expansion question
- use `phase1_targeted_representation_balance_round4_2026-04-27.md` as the live memo for this reopened pass
- prioritize true `L2` candidates first, then `text-only + observed_effect`, then only secondary breadth cases

## 2026-04-27 boundary-relaxation addendum

The project has now decided that if the target is roughly `30` paper-level Core items, the old strict boundary is too narrow.

Operational consequence:

- keep the current stable table as `anchor_core` baseline
- reopen existing `Adjacent` and reserve cases as `bridge_core` reclassification candidates
- re-adjudicate known local bridge cases before doing more external search
- use `phase1_core_boundary_relaxation_memo_2026-04-27.md` for the rule change
- use `phase1_bridge_core_reclassification_2026-04-27.csv` and `.md` as the live reclassification queue

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
- `HC13` Fire evacuation cellular automata
- `HC14` Crowd evacuation disaster scenarios
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
- the formerly blocked HC13/HC14 rows are now materialized in the stable coding table
- the admitted Round 3 rows are now materialized in the stable coding table

## 2. Resolved acquisition item

### HC01 TravelAgent

Status:

- PDF archived at `assets/survey_paper/pdfs/phase1_core/00_HC01_TravelAgent_Noyman2025.pdf`
- full-text adjudication recorded in `phase1_hc01_travelagent_fulltext_adjudication_2026-04-27.md`

Decision:

- do not add HC01 to the Core first-pass coding table as stable social-behavior evidence
- use it as Adjacent/boundary evidence for built-environment spatial interfaces

Reason:

- the paper supports `3D_engine / L5` spatial-interface coding
- the current experiments are single-agent navigation and wayfinding
- multi-agent interaction and social dynamics are future work, not current evidence

## 3. HC13 and HC14 closure

Status:

- both PDFs are archived locally under `assets/survey_paper/pdfs/phase1_core/`
- local `pdf2text` extraction produced `.fulltext.md` and `.meta.json` artifacts for both papers
- full-text adjudication is recorded in `phase1_hc13_hc14_fulltext_adjudication_2026-04-27.md`

Stable conservative reading:

- `HC13`: `2D_grid / L3`, observed evacuation outcomes, keep in `Core`
- `HC14`: `graph_based / L3`, observed evacuation outcomes plus report-level validation, keep in `Core`
- neither paper should be used to strengthen `L5` or direct-geometry claims

## 4. Round 3 integration

Admitted now:

- `R3-01` MineLand: `3D_engine / L5 / observed_effect`
- `R3-02` GATSim: `graph_based / L3 / observed_effect`
- `R3-04` LLM-driven epidemic-economic dynamics: `2D_grid / L3 / observed_effect`

Operational meaning:

- the former `L5 + observed_effect` gap is now closed
- the observed-effect side is now close to balanced against designed-affordance rows
- `R3-03` remains reserve only
- `R3-05` remains Adjacent/boundary only

## 5. Practical implication

The project is no longer blocked on:

- broad `Core` expansion
- first-pass coding of the usable core set
- row-level splitting of the ambiguous representation families
- acquisition of the remaining high-value Phase 1 Core PDFs

The immediate path is now:

1. use the stable evidence-map outputs from the `19` coded rows as the manuscript baseline
2. treat targeted Round 3 as closed unless a new manuscript need appears
3. treat `L4` as a negative finding documented in `phase1_targeted_l4_search_memo_2026-04-27.md`, not as an active queue item
4. keep older acquisition memos as historical trace rather than current task drivers

## 6. Seed-table convention

The seed CSV still retains split-aware or provisional values for unresolved families such as:

- `pending_split`
- `mixed_L3_to_L5_split_required`
- `L5_present_but_split_required`

It now also records post-review states for rows that needed extra adjudication, including `HC13` and `HC14`.
