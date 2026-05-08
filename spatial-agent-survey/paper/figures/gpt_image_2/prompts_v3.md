# GPT-Image-2 Figure Redraw Prompts V3

Status: content-replanned prompts based on `../figure_content_plan_v2.md`.

Purpose: regenerate Figure 1-Figure 6 as argument-bearing survey figures, not decorative summaries.

## Global Generation Contract

Model: `gpt-image-2`

Recommended use:

- Use image edit or reference-guided generation when reference inputs are available.
- Provide the current target figure render as the structural target when useful.
- Provide exemplar images only as visual and rhetorical references.
- Do not copy exemplar content, domain labels, counts, citations, or paper-specific text.

Shared paper premise:

The paper is a scoping review plus structured research agenda. It does not prove that spatial configuration already shapes LLM-agent societies. It maps what is known, what is missing, and what evidence would be needed to test configurational social effects.

Shared visual style:

- Publication-safe academic information graphic.
- Vector-like raster output, crisp geometry, high legibility.
- Warm off-white or very light neutral background.
- Muted colors with strong hierarchy.
- Sparse exact text only.
- No decorative clutter, logos, watermarks, paper names, or invented citations.
- Use generous whitespace and keep all labels readable at paper-figure scale.

Shared color grammar:

- Dark green: strict `anchor_core`.
- Light green or blue-green: `bridge_core`.
- Blue: `Adjacent` feasibility or boundary material.
- Tan or gray: `Foundational`, theory, or boundary material.
- Amber or orange: warning, gap, or future-work requirement.
- Rose or muted red: exclusion or insufficient evidence.

Shared claim discipline:

- Do not imply `bridge_core` is equivalent to `anchor_core`.
- Do not place `Adjacent` or `Foundational` inside stable Core.
- Do not imply current evidence proves configuration-mediated LLM-agent social behavior.
- If a figure is explanatory or agenda-setting, make it look like explanation or future work, not current proof.

Shared text rule:

- Use only exact labels listed in the figure prompt.
- Prefer fewer readable labels over many illegible labels.
- Do not invent extra categories, counts, metrics, arrows, or stage names.

Output naming:

- `figure_1_where_gap_claim_architecture_gpt_image_2_v3.png`
- `figure_2_record_to_row_pipeline_gpt_image_2_v3.png`
- `figure_3_agent_interface_coding_system_gpt_image_2_v3.png`
- `figure_4_evidence_map_matrix_gpt_image_2_v3.png`
- `figure_5_local_global_claim_boundary_gpt_image_2_v3.png`
- `figure_6_research_agenda_evidence_ladder_gpt_image_2_v3.png`

## Figure 1. WHERE Gap and Evidence-Role Architecture

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_1_corpus_evidence_roles.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure3_bubble_plots_showing_the_distribution_of_identified_study_designs_types_of_conversational_agents_and_healthcare_topics_in_the_included_articles_plotte.png`
- `assets/survey_paper/exemplar_assets/15_Peters2024_JBI_Scoping_Reviews/figures/table11_3_example_tabular_presentation_of_data_for_a_scoping_review.png`
- `assets/survey_paper/exemplar_assets/15_Peters2024_JBI_Scoping_Reviews/figures/figure11_3_example_of_data_presentation_ikt_approaches_or_strategies_enablers_barriers_and_outcomes_gagliardi_et_al_2015.png`

### Prompt

Create a polished academic information graphic titled exactly:

`Figure 1. WHERE Gap and Evidence-Role Architecture`

What this figure is:

A scoping-review opening figure. It introduces the missing intersection between spatial-configuration theory, LLM spatial capability, and LLM multi-agent social simulation. It also shows the claim architecture of the paper.

Why the paper needs it:

The reader must immediately understand that this paper is not a causal proof paper. It is a scoping review that maps a missing intersection, separates evidence roles, and builds a research agenda from the gap.

Reader takeaway:

Three bodies of literature contribute different kinds of support, but none alone proves configuration-mediated LLM-agent social behavior. The strongest current contribution is a descriptive evidence map, followed by a Space Syntax bridge and a future research agenda.

Reference use:

- Borrow separated evidence-lane logic from the Tudor-Car distribution reference.
- Borrow scoping-review charting discipline from the JBI table reference.
- Borrow support-to-approach-to-outcome abstraction from the JBI concept-map reference.
- Do not copy healthcare categories, publication-year axes, dense table rows, or overlapping-circle content.

Required visual structure:

- Use a three-lane convergence diagram.
- Lane 1: `Foundational`.
- Lane 2: `Adjacent`.
- Lane 3: `Core`.
- The three lanes should converge toward a central gap, but only `Core` should feed the main coded evidence map.
- Show a claim architecture block with three contribution levels.
- Keep corpus roles visually distinct from contribution levels.

Mandatory exact text:

- `Foundational`
- `Space Syntax and physical-space evidence`
- `configuration -> movement / encounter hypotheses`
- `transferable theory, not direct LLM-agent evidence`
- `Adjacent`
- `LLM spatial reasoning and spatially aware agents`
- `feasibility and boundary evidence`
- `capability evidence, not social-effect evidence`
- `Core`
- `LLM multi-agent systems with space and social behavior`
- `evidence map of current practice`
- `mostly local / semantic interfaces`
- `Missing intersection`
- `agent-facing spatial configuration + observed social behavior`
- `Primary: evidence map`
- `Secondary: Space Syntax bridge`
- `Tertiary: research agenda`
- `stable Core: 32 sources / 34 rows`
- `anchor_core: 17 sources / 19 rows`
- `bridge_core: 15 sources / 15 rows`
- `BK02: source-note-only bridge caveat`

Style:

- Mature academic diagram, not playful.
- Use three clean horizontal or vertical evidence lanes.
- Use a subtle convergence zone for the missing intersection.
- Use dark green for `Core`, blue for `Adjacent`, tan or gray for `Foundational`, and amber for the missing intersection.
- Use compact cards and arrows, not long paragraphs.

Claim boundary:

- Do not make `Adjacent` or `Foundational` look like direct evidence in the stable Core.
- Do not imply the missing intersection is already solved.
- Do not show `bridge_core` with the same weight as `anchor_core`.
- Do not let `BK02` carry strong evidence weight.

Let the image model choose the exact layout, but preserve the three-lane logic, the missing-intersection focus, and the three contribution levels.

### QA Checklist

- The figure reads as a scoping-review claim architecture.
- The missing intersection is central and unsolved.
- `Foundational`, `Adjacent`, and `Core` are visibly different evidence roles.
- Contribution levels are present and not confused with corpus roles.
- Counts are correct and not mixed with PRISMA screening counts.

## Figure 2. Record-to-Row Review Pipeline

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_2_prisma_scr_flow.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/11_Silacci2026_LLM_Agents_Scoping_Review/figures/figure1_the_prisma_preferred_reporting_items_for_systematic_reviews_and_meta_analyses_flowchart_provided_by_covidence_with_the_search_and_the_selection_proces.png`
- `assets/survey_paper/exemplar_assets/12_Leiser2025_LLM_Architectures_Scoping_Review/figures/figure1_prisma_scr_preferred_reporting_items_for_systematic_reviews_and_meta_analyses_extension_for_scoping_reviews_flowchart_for_inclusion_and_exclusion_of_m.png`
- `assets/survey_paper/exemplar_assets/13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure2_prisma_flow_chart.png`
- `assets/survey_paper/exemplar_assets/15_Peters2024_JBI_Scoping_Reviews/figures/figure11_5_flow_diagram_for_the_scoping_review_process_adapted_from_the_prisma_statement_by_moher_and_colleagues_2009.png`

Do not use `14_Tricco2018_PRISMA_ScR/figures/figure1_methods_flow_416.png` as a visual reference because the local crop captured a reference-list page artifact rather than the flow diagram itself.

### Prompt

Create a polished academic review-methods figure titled exactly:

`Figure 2. Record-to-Row Review Pipeline`

What this figure is:

A two-panel method pipeline showing how bibliographic screening records are transformed into a stabilized row-level evidence map.

Why the paper needs it:

The paper has two counting layers. PRISMA screening counts classify records bibliographically. The evidence map later codes `system / environment configuration` rows after full-text recheck, widened bridge review, and boundary decisions.

Reader takeaway:

`Core: 12` from bibliographic screening is not the same object as `Stable widened Core: 32 sources / 34 rows`. The final evidence map is produced by later row-level stabilization.

Reference use:

- Borrow stage bands and clean blue-outline PRISMA styling from Silacci.
- Borrow explicit stage labels and side exclusion boxes from Leiser.
- Borrow classic vertical flow and side-exclusion logic from Tudor-Car and JBI.
- Do not copy exemplar database names, duplicate counts, exclusion reasons, article totals, or included-study counts.

Required visual structure:

- Two large panels.
- Panel A: `Bibliographic screening`.
- Panel B: `Evidence-map stabilization`.
- Put a clear transition between panels: `full-text recheck + row-level coding`.
- Include a visible unit-shift callout: `paper -> system / environment configuration`.
- Boundary decisions should appear as side cards, not as stable Core rows.

Mandatory exact text:

- `Bibliographic screening`
- `Records screened: 417`
- `Core: 12`
- `Adjacent: 42`
- `Foundational: 47`
- `Excluded: 316`
- `E1: 85 / E2: 54 / E3: 177`
- `full-text recheck + row-level coding`
- `paper -> system / environment configuration`
- `Evidence-map stabilization`
- `Full-text recheck`
- `Targeted widened review`
- `Strict anchor: 17 sources / 19 rows`
- `Bridge layer: 15 sources / 15 rows`
- `Stable widened Core: 32 sources / 34 rows`
- `HC01: Adjacent / boundary`
- `TW-02: boundary only`
- `screening counts != coded rows`

Style:

- PRISMA-inspired but not a generic PRISMA copy.
- Pale blue-gray stage backgrounds.
- Thin charcoal outlines.
- Muted green for stable Core outputs.
- Muted blue for Adjacent.
- Tan or amber for boundary decisions.
- Rose or muted red for Excluded.
- Keep text compact and readable.

Claim boundary:

- Do not collapse bibliographic `Core: 12` into the stable widened Core.
- Do not imply `HC01` or `TW-02` are counted in stable widened Core.
- Do not imply `Adjacent` and `Foundational` are discarded or irrelevant.

Let the image model choose the exact flow geometry, but the record-to-row transformation and count separation must dominate the figure.

### QA Checklist

- The figure shows two counting layers.
- `paper -> system / environment configuration` is visible.
- `screening counts != coded rows` is visible.
- Stable widened Core count is exactly `32 sources / 34 rows`.
- No exemplar database names or exemplar counts appear.

## Figure 3. Agent-Interface Coding System

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_3_l0_l5_taxonomy.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure2_a_taxonomy_of_large_language_model_empowered_spatial_intelligence_with_representative_examples.png`
- `assets/survey_paper/exemplar_assets/07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure2_a_taxonomy_of_large_language_model_agent_methodologies.png`
- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure4_conceptual_framework_of_abstract_spatial_reasoning_the_framework_illustrates_three_primary_dimensions_of_spatial_reasoning_capabilities_qualitative_re.png`

### Prompt

Create a polished academic visual codebook titled exactly:

`Figure 3. Agent-Interface Coding System`

What this figure is:

A decision-system figure for coding agent-accessible spatial representation. It defines `L0` to `L5` by what the agent receives, not by what the environment stores or what the analyst computes later.

Why the paper needs it:

The evidence map depends on a strict distinction between environment-side richness and agent-facing structure. A 3D engine, graph backend, or GIS layer does not automatically imply `L4` or `L5`.

Reader takeaway:

Representation level is coded at the agent interface. The same backend type can map to different levels depending on what is actually exposed to the agent.

Reference use:

- Borrow taxonomy credibility and branching logic from Feng's taxonomy.
- Borrow survey-method structure from Luo's taxonomy.
- Borrow compact conceptual cards and a challenge strip from Feng's abstract spatial reasoning figure.
- Do not copy citation-heavy boxes, spatial-intelligence category names, or methodology labels from the references.

Required visual structure:

- Start with a prominent decision question: `What does the agent receive?`
- Show a decision path or branching visual from `L0` to `L5`.
- Include a separate backend strip below or beside the decision path.
- Add mismatch chips from Table 4 showing that backend type does not determine level.
- Make `code agent input, not backend` the central rule.

Mandatory exact text:

- `What does the agent receive?`
- `code agent input, not backend`
- `L0: no spatial input`
- `L1: place / action labels`
- `L2: semantic scene`
- `L3: local relations`
- `adjacency, co-presence, nearby agents, movement options`
- `L4: global abstract structure`
- `integration, depth, control, choice, network position`
- `L5: geometry / embodiment`
- `coordinates, visual field, physical constraints`
- `text-only`
- `2D grid`
- `graph_based`
- `3D_engine`
- `3D_engine -> L5: HC06 / HC12A`
- `3D_engine -> L3: HC10 / HC12B`
- `graph_based -> L3: HC14`
- `graph_based -> L4: L4R-01`
- `rich backend != higher level unless agent-facing`

Optional count badges, if space permits:

- `L0: 0`
- `L1: 1`
- `L2: 8`
- `L3: 18`
- `L4: 1`
- `L5: 6`

Style:

- Refined visual codebook, not a simple ladder.
- Warm off-white background.
- Six compact level cards or decision nodes.
- Backend strip in muted gray-blue.
- Mismatch chips in amber or outlined callouts.
- Crisp connectors and high legibility.

Claim boundary:

- Do not show higher levels as automatically better.
- Do not imply `3D_engine` automatically means `L5`.
- Do not imply researcher-side graph analysis automatically means `L4`.
- Do not imply `L4` is mature or common.

Let the image model choose a branching or stepped decision layout, but the agent-interface rule and mismatch examples must be visually central.

### QA Checklist

- The figure reads as a coding decision system.
- Backend strip is visually separate from agent-facing representation.
- All mismatch chips are correct.
- `rich backend != higher level unless agent-facing` is prominent.
- No backend type is visually mapped to only one representation level.

## Figure 4. Evidence-Map Matrix

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_4_representation_distribution.svg` rendered to PNG

Visual reference:

- `assets/survey_paper/exemplar_assets/13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure3_bubble_plots_showing_the_distribution_of_identified_study_designs_types_of_conversational_agents_and_healthcare_topics_in_the_included_articles_plotte.png`

### Prompt

Create a polished academic evidence-map figure titled exactly:

`Figure 4. Evidence-Map Matrix`

What this figure is:

The main empirical figure of the survey. It shows how agent-accessible spatial representation level, behavioral scale, evidence status, and core layer jointly reveal the central gap.

Why the paper needs it:

The primary contribution is not just a list of representation levels. It is a structured evidence map showing that current work is dense at `L3`, sparse at `L4`, and uneven by evidence status and core layer.

Reader takeaway:

Current LLM-agent systems are not spatially empty. They contain many local, semantic, and embodied spatial interfaces and some observed-effect rows. The specific gap is configurational: agent-facing global abstract structure is nearly absent, especially in the strict anchor core.

Reference use:

- Borrow compact category-based distribution logic from Tudor-Car's bubble-plot figure.
- Do not copy publication-year axes, healthcare categories, three-panel layout, or bubble-size legend.

Required visual structure:

- Use a matrix as the primary visual.
- Rows are representation levels: `L1`, `L2`, `L3`, `L4`, `L5`.
- Columns are behavioral scales: `interaction`, `emergent_social_structure`, `mixed`.
- Each nonzero cell should show exact counts, split by evidence status when needed.
- Add small marginal bars or side chips for `anchor_core` versus `bridge_core` by representation level.
- Add callouts for the main claims.

Mandatory matrix text:

- `interaction`
- `emergent_social_structure`
- `mixed`
- `designed`
- `observed`
- `L1 labels`
- `L2 semantic scene`
- `L3 local relations`
- `L4 global abstract`
- `L5 geometry / embodiment`

Mandatory cell counts:

- `L1 interaction: 1 designed`
- `L2 interaction: 4 designed + 4 observed`
- `L3 interaction: 2 designed`
- `L3 emergent: 3 designed + 8 observed`
- `L3 mixed: 2 designed + 3 observed`
- `L4 emergent: 1 observed`
- `L5 interaction: 2 observed`
- `L5 emergent: 1 designed`
- `L5 mixed: 2 designed + 1 observed`

Mandatory marginal layer counts:

- `L1: 1 anchor / 0 bridge`
- `L2: 0 anchor / 8 bridge`
- `L3: 15 anchor / 3 bridge`
- `L4: 0 anchor / 1 bridge`
- `L5: 3 anchor / 3 bridge`
- `anchor_core: 19 rows`
- `bridge_core: 15 rows`
- `stable widened Core: 34 rows`

Required callouts:

- `strict anchor concentrated at L3`
- `L4 absent from anchor_core`
- `observed effects exist, but are uneven`
- `bridge recovery is not anchor evidence`

Style:

- Clean academic matrix, not a decorative chart.
- Warm off-white background.
- Use dark green for `anchor_core`, light green or blue-green for `bridge_core`.
- Use one restrained mark style for `designed` and another for `observed`.
- Use amber callouts for gap and claim-boundary warnings.
- Keep gridlines subtle and labels large.

Claim boundary:

- Do not imply `L4` is solved.
- Do not visually merge `anchor_core` and `bridge_core`.
- Do not add percentages, trend lines, or extra data series.
- Do not imply observed-effect rows are mechanism proof.

Let the image model choose exact matrix geometry, but the figure must clearly communicate `L3` density, `L4` sparsity, evidence-status unevenness, and anchor-versus-bridge separation.

### QA Checklist

- The figure is a matrix, not only a bar chart.
- `L4` has exactly `1 observed` in emergent social structure.
- `L4 absent from anchor_core` is visible.
- `L3` is visibly dominant.
- Marginal layer counts are correct.
- No percentages or invented totals appear.

### Text Fallback

If GPT-Image-2 cannot render the matrix text accurately, use it only to generate a clean matrix-style background and then overlay exact matrix labels deterministically with SVG or HTML tooling.

## Figure 5. Local-to-Global Claim Boundary

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_5_local_vs_global_configuration.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure1_multiple_scale_spatial_intelligence_in_real_world_from_embodied_spatial_intelligence_to_earth_spatial_intelligence.png`
- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure4_conceptual_framework_of_abstract_spatial_reasoning_the_framework_illustrates_three_primary_dimensions_of_spatial_reasoning_capabilities_qualitative_re.png`
- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure2_a_taxonomy_of_large_language_model_empowered_spatial_intelligence_with_representative_examples.png`

### Prompt

Create a polished academic theory-bridge figure titled exactly:

`Figure 5. Local-to-Global Claim Boundary`

What this figure is:

A three-panel explanatory graph that shows why `L3` local adjacency and `L4` global configuration are different claim layers.

Why the paper needs it:

The survey uses Space Syntax as a theoretical bridge, but physical-space findings only become testable in LLM-agent systems when the relevant global structure is exposed to the agent. The figure teaches this boundary visually.

Reader takeaway:

Two locations can look identical from local adjacency alone, while occupying different whole-layout positions. `L3` can support local opportunity claims. `L4` is needed for configuration-wide claims.

Reference use:

- Borrow multi-scale explanatory contrast from Feng's scale figure.
- Borrow clean graph-reasoning cards from Feng's abstract spatial reasoning figure.
- Borrow taxonomy separation from Feng's taxonomy.
- Do not use robot, city, earth, real-world photos, dense taxonomy boxes, or citations.

Required visual structure:

- Three panels.
- Panel A: local agent view.
- Panel B: whole layout.
- Panel C: claim boundary.
- Keep the same highlighted nodes `B` and `G` across panels.
- `B` should be highlighted in muted green.
- `G` should be highlighted in muted amber.

Panel A content:

- Show two egocentric mini-graphs.
- Node `B` has two immediate neighbors.
- Node `G` has two immediate neighbors.
- The two local views should look structurally equivalent.

Panel B content:

- Show a larger connected graph.
- Node `B` is near a main spine or shallow position.
- Node `G` is deeper in a side branch.
- Add subtle overlays or small tags for `depth`, `integration`, `control`, and `choice`.

Panel C content:

- Show a compact claim-boundary card contrasting `L3` and `L4`.
- Indicate that global structure must be agent-facing before configuration-level claims are testable.

Mandatory exact text:

- `Local agent view`
- `B: local degree 2`
- `G: local degree 2`
- `L3 can see local adjacency`
- `Whole layout`
- `depth`
- `integration`
- `control`
- `choice`
- `Claim boundary`
- `L3 claim: local opportunity / co-presence`
- `L4 claim: configuration-wide position`
- `Needed for testing: agent-facing global structure`
- `local neighbors do not equal depth, integration, control, or choice`

Style:

- Clean node-link graph visuals.
- Warm off-white background.
- Pale blue-gray panel cards.
- Charcoal lines and text.
- Muted green for `B`.
- Muted amber for `G`.
- High contrast, generous spacing, no equations.

Claim boundary:

- This is an explanatory diagram, not empirical evidence.
- Do not imply global graph metrics are currently exposed to most LLM agents.
- Do not add equations, formulas, or quantitative values for Space Syntax metrics.

Let the image model choose the exact graph shape, but preserve the logical contrast between identical local views and different whole-layout positions.

### QA Checklist

- Three panels are present.
- Panel A local views are structurally equivalent.
- Panel B shows different global positions.
- Panel C states the claim boundary.
- `B` and `G` colors remain consistent.
- No equations or empirical-effect claims appear.

## Figure 6. Research Agenda as an Evidence Ladder

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_6_research_agenda_map.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/05_Mou2024_Social_Simulation_LLM_Agents_Survey/figures/figure4_illustration_of_society_simulations_to_construct_society_simulations_the_corresponding_society_s_construction_elements_i_e_com_position_network_social.png`
- `assets/survey_paper/exemplar_assets/05_Mou2024_Social_Simulation_LLM_Agents_Survey/figures/figure7_illustration_of_society_simulation_trend_which_goes_through_three_stages_constructing_preliminary_environments_exploring_alignment_on_specific_scenari.png`
- `assets/survey_paper/exemplar_assets/07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure1_an_overview_of_the_llm_agent_ecosystem_organized_into_four_interconnected_dimensions_agent_methodology_covering_the_foundational_aspects_of_constructi.png`
- `assets/survey_paper/exemplar_assets/07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure4_an_overview_of_real_world_issues_in_llm_agent_systems_organized_into_three_domains_security_challenges_including_agent_centric_and_data_centric_threat.png`

### Prompt

Create a polished academic research-roadmap figure titled exactly:

`Figure 6. Research Agenda as an Evidence Ladder`

What this figure is:

A future-work roadmap that translates the survey's evidence-map diagnosis into progressively stronger evidence requirements.

Why the paper needs it:

The research agenda should not look like a generic list of directions. It should show how the field can move from current spatial affordances toward spatial sensitivity, spatial mediation, and eventually replicated mechanisms.

Reader takeaway:

Richer spatial representation is a research target, not a validated result. Stronger future claims require exposed agent-facing structure, matched controls, observed behavioral changes, and replication across layouts, tasks, populations, models, and seeds.

Reference use:

- Borrow construction-element plus evaluation organization from Mou's society-simulation figure.
- Borrow staged-roadmap logic from Mou's trend figure.
- Borrow quadrant overview clarity from Luo's ecosystem figure.
- Borrow matrix grouping and dashed dividers from Luo's issues figure.
- Do not copy cartoon-heavy icons, paper names, scenario examples, or dense category lists.

Required visual structure:

- Start with a left-side or top-side `Current diagnosis` block.
- Then show five linked agenda stages.
- Overlay or attach an evidence ladder that rises from weaker to stronger claims.
- Make the global guardrail visually apply to the whole figure.
- The roadmap should read as future work, not proof.

Current diagnosis block, exact text:

- `Current diagnosis`
- `L3 concentrated`
- `L4 sparse: 1 / 34 rows, bridge-only`
- `15 designed affordance only / 19 observed effect`
- `backend richness != agent input`

Agenda stages, exact text:

- `1. Representation`
- `specify what agents receive`
- `distinguish L2 / L3 / L4 / L5`
- `2. Mechanism`
- `matched controls`
- `L1/L2 vs L3`
- `L3 vs L4`
- `L3/L4 vs L5`
- `3. Emergence`
- `movement`
- `co-presence`
- `encounter`
- `group formation`
- `role differentiation`
- `4. Generalization`
- `layouts`
- `tasks`
- `populations`
- `models`
- `seeds`
- `5. Applications`
- `tie claims to representation level`
- `behavioral scale`
- `evidence status`

Evidence ladder, exact text:

- `spatial affordance`
- `spatial sensitivity`
- `spatial mediation`
- `replicated mechanism`

Global guardrail, exact text:

- `future-work claims require exposed structure + observed evidence`
- `agenda is not current proof`

Style:

- Refined staged roadmap or evidence ladder.
- Warm off-white background.
- Muted stage colors with clear progression.
- Minimal icons, only if they clarify stages.
- Crisp arrows, cards, or ladder rungs.
- Large labels and strong visual hierarchy.

Claim boundary:

- Do not imply richer spatial representation has already been validated.
- Do not imply a causal pipeline from representation to better social simulation.
- Do not present future directions as current evidence.
- Do not treat the one `L4` bridge row as physical-layout validation.

Let the image model choose a left-to-right, vertical, or hybrid roadmap, but preserve the diagnosis-to-agenda-to-evidence-ladder logic.

### QA Checklist

- The figure starts from current evidence-map diagnosis.
- All five agenda stages appear once.
- Evidence ladder is visible and ordered from weaker to stronger.
- Guardrail is prominent.
- The figure reads as future work, not proof.

## Recommended Generation Order

1. Generate Figure 5 first to validate the deeper visual language with moderate text load.
2. Generate Figure 4 second because it is the main empirical figure and may need deterministic text overlay.
3. Generate Figure 3 third because it supports Figure 4's coding logic.
4. Generate Figure 2 fourth after checking text reliability.
5. Generate Figure 1 fifth once the introduction wording is stable.
6. Generate Figure 6 last after Sections 6 and 7 are prose-stable.

## Final QA Pass For All Figures

- Check exact text and numbers.
- Check that `anchor_core` and `bridge_core` are visually distinct.
- Check that `Adjacent` and `Foundational` are not treated as direct LLM-agent social-effect evidence.
- Check that explanatory figures do not look like empirical proof.
- Check that agenda figures do not imply current validation.
- If text rendering is unreliable, keep the generated layout and overlay exact text deterministically.
