# Figure Content Plan V2

Status: content-level replanning before rewriting image prompts.

Date: 2026-05-01

Source inputs:

- `docs/plans/survey_plan_v4.md`
- `spatial-agent-survey/paper/sections/02_space_syntax_primer.md`
- `spatial-agent-survey/paper/sections/03_evidence_map.md`
- `spatial-agent-survey/paper/sections/05_social_simulation.md`
- `spatial-agent-survey/paper/sections/06_evaluation_dimensions.md`
- `spatial-agent-survey/paper/sections/07_research_agenda.md`
- `spatial-agent-survey/paper/tables/table_3_core_evidence_map.md`
- `spatial-agent-survey/paper/tables/table_4_environment_side_vs_agent_accessible_examples.md`
- `spatial-agent-survey/paper/tables/table_6_space_syntax_proposition_transfer.md`
- `spatial-agent-survey/paper/tables/table_7_evaluation_dimensions.md`
- `assets/survey_paper/exemplar_assets/target_figure_reference_analysis.md`

## Planning Premise

The figure set should not be a set of decorative summaries. It should be the argument spine of the survey.

The paper's central question is:

> What is known, what is missing, and what is needed to study how spatial configuration may shape social behavior in LLM multi-agent systems?

The figures should therefore move through six argumentative jobs:

1. Define the gap and evidence roles.
2. Explain how the review converts screened records into a stabilized evidence map.
3. Define the agent-facing representation code used by the map.
4. Show the main empirical result of the map.
5. Explain why the `L3`/`L4` distinction matters theoretically.
6. Translate the gap into a future evidence ladder.

This means the current prompts are too shallow in two ways:

- They often describe what the figure should look like before deciding what argumentative work the figure must do.
- They underuse the survey's strongest assets: the widened-Core evidence map, the environment-side versus agent-accessible distinction, the evidence-status split, and the evaluation ladder.

## Figure Set Narrative

| figure | new argumentative job | paper section | main claim supported |
|---|---|---|---|
| Figure 1 | Show the WHERE gap and the review's claim architecture. | `§1` | The paper is a scoping review of a missing intersection, not a causal proof paper. |
| Figure 2 | Show the record-to-row pipeline and why counts change by layer. | `§3.1` / Appendix | PRISMA screening counts and evidence-map row counts are different objects. |
| Figure 3 | Show the agent-interface coding rule as a decision system. | `§3.2` / `§3.5` | Representation level depends on what the agent consumes, not backend richness. |
| Figure 4 | Show the evidence-map result as a representation-by-behavior matrix. | `§3.3` / `§3.4` | Current evidence is dense at `L3`, sparse at `L4`, and uneven by evidence status. |
| Figure 5 | Show why local adjacency and global configuration are different claim layers. | `§2.3` / `§5.4` | Space Syntax propositions require agent-facing global structure before LLM-agent claims can be tested. |
| Figure 6 | Show the research agenda as an evidence ladder. | `§6` / `§7` | Future work must move from spatial affordance to sensitivity, mediation, and replicated mechanism. |

## Global Design Rules

- Use figures to state claims, not just categories.
- Keep table-like detail in tables; use figures to show relationships, gaps, and transitions.
- Use exact numbers only where they advance the claim.
- Use repeated visual grammar across the six figures:
  - dark green: strict `anchor_core`;
  - light green or blue-green: `bridge_core`;
  - blue: `Adjacent` feasibility/boundary material;
  - tan/gray: `Foundational` or boundary/theory material;
  - orange/amber: warning, gap, or future-work requirement;
  - rose/red: exclusion or insufficient evidence only.
- Keep `bridge_core` visibly lower-weight than `anchor_core`.
- Never place `Adjacent` or `Foundational` inside the stable Core evidence-map boundary.
- Do not use icon-heavy survey style unless icons directly support the concept.

## Figure 1. WHERE Gap and Evidence-Role Architecture

### Current Weakness

The current Figure 1 is mainly a corpus-role diagram. It explains role separation, but it does not yet show why the paper exists or how the three contribution layers fit together.

### New Purpose

Figure 1 should introduce the paper's intellectual problem: three bodies of evidence exist, but their intersection remains underdeveloped.

The figure should answer:

- What does each corpus role contribute?
- What does each role not prove?
- Where is the missing research intersection?
- What kind of claim can this survey safely make?

### Reference Use

Use these references from `target_figure_reference_analysis.md`:

- Tudor-Car Figure 3 for separated evidence lanes.
- JBI Table 11.3 for scoping-review charting discipline.
- JBI Figure 11.3 for support-to-approach-to-outcome logic.

Do not borrow healthcare categories, publication-year axes, or dense table rows.

### Proposed Content

Use a three-lane convergence diagram rather than only nested circles.

Lane 1: `Foundational`

- Role: Space Syntax and physical-space evidence.
- Contributes: `configuration -> movement / encounter hypotheses`.
- Boundary: transferable theory, not direct LLM-agent evidence.

Lane 2: `Adjacent`

- Role: LLM spatial reasoning and spatially aware agents.
- Contributes: feasibility and boundary evidence.
- Boundary: capability evidence, not social-effect evidence.

Lane 3: `Core`

- Role: LLM multi-agent systems with identifiable space and social behavior.
- Contributes: evidence map of current practice.
- Boundary: mostly local/semantic interfaces; limited configurational tests.

Central gap:

- `Missing intersection: agent-facing spatial configuration + observed social behavior`

Claim architecture:

- `Primary: evidence map`
- `Secondary: Space Syntax bridge`
- `Tertiary: research agenda`

Optional count chips:

- `stable Core: 32 sources / 34 rows`
- `anchor_core: 17 sources / 19 rows`
- `bridge_core: 15 sources / 15 rows`

Avoid showing `Adjacent = 42` and `Foundational = 47` here unless the label clearly says those are bibliographic screening categories. Figure 2 is the better place for screening counts.

### Caption Thesis

The figure should say that the paper maps a missing intersection between spatial-configuration theory, LLM spatial capability, and LLM multi-agent social simulation. The figure should also make clear that the paper's strongest current claim is descriptive and gap-oriented.

### Prompt Consequence

The next prompt should not ask for a generic "corpus evidence roles" diagram. It should ask for a "WHERE gap and claim architecture" diagram, with corpus roles as one part of the visual.

## Figure 2. Record-to-Row Review Pipeline

### Current Weakness

The current Figure 2 already separates PRISMA screening from stabilization, but it still reads like a polished flowchart rather than the methodological answer to why different counts appear in the paper.

### New Purpose

Figure 2 should make the counting logic impossible to misunderstand:

- Records are screened bibliographically.
- Papers are assigned corpus roles.
- Core papers are recoded at the `system / environment configuration` row level.
- Boundary and bridge decisions produce the stable widened-Core evidence map.

### Reference Use

Use these references:

- Silacci Figure 1 for modern PRISMA stage bands.
- Leiser Figure 1 for explicit stage headings and exclusion-reason boxes.
- Tudor-Car Figure 2 and JBI Figure 11.5 for classic side-exclusion flow.

Do not use the extracted Tricco visual artifact as a visual reference.

### Proposed Content

Panel A: `Bibliographic screening`

- `Records screened: 417`
- `Core: 12`
- `Adjacent: 42`
- `Foundational: 47`
- `Excluded: 316`
- `E1: 85 / E2: 54 / E3: 177`

Panel B: `Evidence-map stabilization`

- `Full-text recheck`
- `Targeted widened review`
- `Unit shift: paper -> system / environment configuration`
- `Strict anchor: 17 sources / 19 rows`
- `Bridge layer: 15 sources / 15 rows`
- `Stable widened Core: 32 sources / 34 rows`

Boundary decisions:

- `HC01: Adjacent / boundary`
- `TW-02: boundary only`

Required warning:

- `screening counts != coded rows`

### Caption Thesis

The figure should say that the evidence map is not a direct restatement of the PRISMA category counts. It is produced by later full-text rechecks, widened bridge review, and row-level coding.

### Prompt Consequence

The next prompt should emphasize "record-to-row pipeline" and "unit shift" more than generic PRISMA styling.

## Figure 3. Agent-Interface Representation Coding System

### Current Weakness

The current Figure 3 is a level list. It explains `L0-L5`, but it does not fully show the decision logic that makes this taxonomy valuable: backend richness can fail to reach the agent.

### New Purpose

Figure 3 should function as the visual codebook for the evidence map.

It should answer:

- What is being coded?
- How does the coder decide between levels?
- Why can the same backend type map to different representation levels?
- Why is `L4` not the same as researcher-side graph analysis?

### Reference Use

Use these references:

- Feng Figure 2 for taxonomy credibility and branching logic.
- Luo Figure 2 for survey-method taxonomy structure.
- Feng Figure 4 for compact conceptual cards plus a challenge strip.

Do not copy citation-heavy boxes.

### Proposed Content

Core visual: an agent-interface decision path.

Start node:

- `What does the agent receive?`

Decision path:

- `No spatial input` -> `L0`
- `Place / action labels only` -> `L1`
- `Semantic scene description` -> `L2`
- `Local relations: adjacency, co-presence, nearby agents, movement options` -> `L3`
- `Global abstract structure: integration, depth, control, choice, network position` -> `L4`
- `Geometry / embodiment: coordinates, visual field, physical constraints` -> `L5`

Backend strip:

- `text-only`
- `2D grid`
- `graph_based`
- `3D_engine`

Example mismatch chips from Table 4:

- `3D_engine -> L5: HC06 / HC12A`
- `3D_engine -> L3: HC10 / HC12B`
- `graph_based -> L3: HC14`
- `graph_based -> L4: L4R-01`

Central rule:

- `code agent input, not backend`

Warning:

- `rich backend != higher level unless agent-facing`

Optional count badges:

- `L0: 0`
- `L1: 1`
- `L2: 8`
- `L3: 18`
- `L4: 1`
- `L5: 6`

### Caption Thesis

The figure should say that the survey codes the structure available to the agent, not the simulator's internal richness or the analyst's post-hoc calculations.

### Prompt Consequence

The next prompt should ask for a "decision system" or "visual codebook," not just a six-card taxonomy.

## Figure 4. Evidence-Map Matrix: Representation, Behavior, and Evidence Status

### Current Weakness

The current Figure 4 only shows representation distribution by core layer. That is useful but too shallow for the primary contribution. The primary contribution is not just "how many L-levels," but how representation level, behavioral scale, evidence status, and core layer jointly reveal the gap.

### New Purpose

Figure 4 should be the main empirical figure of the paper.

It should show:

- the concentration at `L3`;
- the near absence of `L4`;
- the fact that observed effects exist but are unevenly distributed;
- the difference between strict anchor evidence and bridge recovery.

### Reference Use

Use Tudor-Car Figure 3 for compact distribution logic, but do not copy its three-panel time-axis bubble plot.

### Proposed Content

Primary visual: a matrix.

Rows:

- `L1 labels`
- `L2 semantic scene`
- `L3 local relations`
- `L4 global abstract`
- `L5 geometry / embodiment`

Columns:

- `interaction`
- `emergent_social_structure`
- `mixed`

Cell encoding:

- Split each cell by evidence status:
  - `designed_affordance_only`
  - `observed_effect`
- Show exact small counts in each nonzero cell.

Mandatory matrix counts:

| level | interaction | emergent_social_structure | mixed |
|---|---|---|---|
| `L1` | `1 designed` | `0` | `0` |
| `L2` | `4 designed + 4 observed` | `0` | `0` |
| `L3` | `2 designed` | `3 designed + 8 observed` | `2 designed + 3 observed` |
| `L4` | `0` | `1 observed` | `0` |
| `L5` | `2 observed` | `1 designed` | `2 designed + 1 observed` |

Secondary marginal bars:

- By representation level and core layer:
  - `L1: 1 anchor / 0 bridge`
  - `L2: 0 anchor / 8 bridge`
  - `L3: 15 anchor / 3 bridge`
  - `L4: 0 anchor / 1 bridge`
  - `L5: 3 anchor / 3 bridge`
- Totals:
  - `anchor_core: 19 rows`
  - `bridge_core: 15 rows`
  - `stable widened Core: 34 rows`

Required callouts:

- `strict anchor concentrated at L3`
- `L4 absent from anchor_core`
- `observed effects exist, but are uneven`
- `bridge recovery is not anchor evidence`

### Caption Thesis

The figure should say that the current literature is not spatially empty; it contains many local/semantic/embodied spatial interfaces and several observed-effect rows. The gap is specifically configurational: agent-facing global abstract structure is almost absent, especially in the strict anchor core.

### Prompt Consequence

The next prompt should replace the simple bar-chart request with a matrix-plus-marginal-bars request. If image generation struggles with text accuracy, generate a cleaner matrix layout and overlay exact labels deterministically later.

## Figure 5. Local-to-Global Claim Boundary

### Current Weakness

The current Figure 5 is logically correct but too small in argumentative scope. It shows local adjacency versus global configuration, but it does not connect the distinction to Space Syntax propositions or to the evidence-map taxonomy.

### New Purpose

Figure 5 should be the theoretical bridge figure. It should teach the reader why `L3` and `L4` are different claim layers.

It should answer:

- Why can two local views look identical?
- What whole-layout information is missing from the local view?
- Which Space Syntax concepts become testable only if global structure is agent-facing?
- What claim is allowed at `L3`, and what claim requires `L4`?

### Reference Use

Use these Feng references:

- Figure 1 for multi-scale explanatory contrast.
- Figure 4 for graph-reasoning cards and abstract spatial concepts.
- Figure 2 for taxonomy separation of graph-theoretical reasoning.

Do not use real-world robot, city, or earth imagery.

### Proposed Content

Panel A: `Local agent view`

- Two focal nodes: `B` and `G`.
- Both expose only two immediate neighbors.
- Labels:
  - `B: local degree 2`
  - `G: local degree 2`
- Message:
  - `L3 can see local adjacency`

Panel B: `Whole layout`

- Same two nodes in a larger graph.
- `B` near the main spine / shallow position.
- `G` deeper in a side branch.
- Use light overlays for:
  - `depth`
  - `integration`
  - `control`
  - `choice`

Panel C: `Claim boundary`

- `L3 claim: local opportunity / co-presence`
- `L4 claim: configuration-wide position`
- `Needed for testing: agent-facing global structure`

Required bottom note:

- `local neighbors do not equal depth, integration, control, or choice`

### Caption Thesis

The figure should say that local adjacency can support claims about immediate interaction opportunity, but configuration-level claims require additional agent-facing information about whole-layout position.

### Prompt Consequence

The next prompt should ask for a three-panel bridge figure rather than a two-panel toy graph only.

## Figure 6. Research Agenda as an Evidence Ladder

### Current Weakness

The current Figure 6 is a generic agenda map. It lists five directions but does not show how future work moves from the current evidence gap to stronger allowable claims.

### New Purpose

Figure 6 should convert Sections 6 and 7 into a roadmap of evidence requirements.

It should answer:

- What current diagnosis motivates the agenda?
- What must future studies specify?
- What controls are required?
- What outcomes should be measured?
- What claim level can be made if the test passes?

### Reference Use

Use these references:

- Mou Figure 4 for construction-element plus evaluation organization.
- Mou Figure 7 for staged research trajectory.
- Luo Figure 1 for quadrant overview clarity.
- Luo Figure 4 for matrix grouping and right-side category labels.

Do not copy cartoon-heavy icons, paper names, or scenario lists.

### Proposed Content

Start block: `Current diagnosis`

- `L3 concentrated`
- `L4 sparse: 1 / 34 rows`
- `15 designed affordance only / 19 observed effect`
- `backend richness != agent input`

Main roadmap: five linked agenda stages.

Stage 1: `Representation`

- Specify what agents receive.
- Distinguish `L2`, `L3`, `L4`, `L5`.

Stage 2: `Mechanism`

- Use matched controls.
- Compare:
  - `L1/L2 vs L3`
  - `L3 vs L4`
  - `L3/L4 vs L5`

Stage 3: `Emergence`

- Measure movement, co-presence, encounter, group formation, role differentiation.

Stage 4: `Generalization`

- Replicate across layouts, tasks, populations, models, and seeds.

Stage 5: `Applications`

- Tie claims to representation level, behavioral scale, and evidence status.

Evidence ladder overlay:

- `spatial affordance`
- `spatial sensitivity`
- `spatial mediation`
- `replicated mechanism`

Global guardrail:

- `future-work claims require exposed structure + observed evidence`

### Caption Thesis

The figure should say that the agenda is not a claim that richer spatial representation already works. It is a ladder for moving from current spatial affordances toward credible evidence of spatial sensitivity, mediation, and eventually replicated mechanisms.

### Prompt Consequence

The next prompt should ask for a staged evidence ladder or roadmap, not a generic hub-and-spoke agenda.

## What Changes Next

This document supersedes `prompts_v2.md` at the content-planning level. The next practical step is to write `prompts_v3.md` from this plan.

Expected prompt changes:

- Figure 1: from corpus-role diagram to WHERE-gap and claim architecture.
- Figure 2: from PRISMA flowchart to record-to-row pipeline.
- Figure 3: from taxonomy cards to agent-interface decision system.
- Figure 4: from stacked bars to evidence-map matrix plus marginal layer bars.
- Figure 5: from two-panel toy graph to three-panel local/global claim-boundary bridge.
- Figure 6: from generic agenda map to evidence ladder.

Recommended generation order:

1. Figure 5 first, because it has the simplest exact text and validates the visual language.
2. Figure 4 second, because it is the most important and text/data-heavy empirical figure.
3. Figure 3 third, because it defines the codebook used by Figure 4.
4. Figure 2 fourth, after deciding how much count text the image model can render reliably.
5. Figure 1 fifth, once the intro claim architecture is locked.
6. Figure 6 last, because it should synthesize the final wording of Sections 6 and 7.

Fallback rule:

If GPT-Image-2 cannot render Figure 4's exact matrix text reliably, use it only for the polished layout background and overlay the exact matrix labels with deterministic SVG/HTML tooling.
