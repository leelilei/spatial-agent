# GPT-Image-2 Figure Redraw Prompts V2

Draft status: reference-informed prompts for regenerating Figure 1-Figure 6 after local exemplar extraction and visual analysis.

Supersession note: these prompts are preserved as a v2 test draft. Content planning has since moved to `../figure_content_plan_v2.md`; write `prompts_v3.md` from that plan before the next serious generation pass.

Source analysis:

- `assets/survey_paper/exemplar_assets/target_figure_reference_analysis.md`
- `assets/survey_paper/exemplar_assets/target_figure_reference_map.md`

## Global Generation Contract

Model: `gpt-image-2`

Recommended mode: image edit or reference-guided generation.

Input strategy:

- Provide the current target figure render as the structural target when available.
- Provide the listed exemplar images as visual references only.
- The exemplar images are references for academic figure language, layout discipline, and abstraction level. Do not copy their content, labels, domains, or counts.

Shared style:

- Academic survey-paper information graphic.
- Vector-like raster output, crisp geometry, high legibility.
- Warm off-white or very light neutral background.
- Muted color palette, no neon colors, no decorative clutter.
- Sparse exact text only.
- Large labels suitable for a two-column or full-width paper figure.
- No logos, no watermarks, no paper names, no citations inside the image unless explicitly listed.

Shared claim discipline:

- Do not imply `bridge_core` is equivalent to `anchor_core`.
- Do not imply `Adjacent` or `Foundational` are direct empirical evidence for LLM-agent social effects.
- Do not claim current evidence proves spatial configuration shapes LLM-agent societies.
- If a figure is explanatory or agenda-setting, make it look like explanation or future work, not current empirical proof.

Text reliability rule:

- Use only the exact labels specified in each prompt.
- Keep text short and high contrast.
- If exact text rendering is uncertain, favor fewer labels over invented labels.
- Do not invent extra categories, metrics, counts, or arrows.

Output naming:

- `figure_1_corpus_evidence_roles_gpt_image_2_v2.png`
- `figure_2_prisma_scr_flow_gpt_image_2_v2.png`
- `figure_3_l0_l5_taxonomy_gpt_image_2_v2.png`
- `figure_4_representation_distribution_gpt_image_2_v2.png`
- `figure_5_local_vs_global_configuration_gpt_image_2_v2.png`
- `figure_6_research_agenda_map_gpt_image_2_v2.png`

## Figure 1. Corpus and Evidence Roles

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_1_corpus_evidence_roles.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure3_bubble_plots_showing_the_distribution_of_identified_study_designs_types_of_conversational_agents_and_healthcare_topics_in_the_included_articles_plotte.png`
- `assets/survey_paper/exemplar_assets/15_Peters2024_JBI_Scoping_Reviews/figures/table11_3_example_tabular_presentation_of_data_for_a_scoping_review.png`
- `assets/survey_paper/exemplar_assets/15_Peters2024_JBI_Scoping_Reviews/figures/figure11_3_example_of_data_presentation_ikt_approaches_or_strategies_enablers_barriers_and_outcomes_gagliardi_et_al_2015.png`

### Prompt

Create a polished academic information graphic titled exactly:

`Figure 1. Corpus and Evidence Roles`

What this figure is: a role-separation diagram for a survey paper. It explains how the corpus is divided before evidence claims are made.

Why the paper needs it: readers must understand that not all cited work has the same claim strength. The figure should make the difference between strict Core evidence, widened bridge evidence, adjacent boundary evidence, and foundational theory visually obvious.

Reader takeaway: the main evidence map is built from Core rows, with `anchor_core` as the strict nucleus and `bridge_core` as a visibly lower-weight widened layer. `Adjacent` and `Foundational` support context and theory, not direct social-effect claims.

Use the reference images only for visual discipline:

- Borrow separated-panel and lane logic from the Tudor-Car bubble-plot reference.
- Borrow scoping-review charting discipline from the JBI table reference.
- Borrow directional support-to-outcome abstraction from the JBI concept-map reference.
- Do not copy any healthcare labels, publication-year axes, table rows, or overlapping-circle content.

Required visual structure:

- A central Core boundary.
- Inside Core, show a strong inner nucleus for `anchor_core`.
- Around or beside it, show a lighter `bridge_core` layer that is connected but visibly lower weight.
- Place `Adjacent`, `Foundational`, and `Boundary` outside the Core boundary as side lanes or support cards.
- Use containment and color weight to communicate claim strength.

Mandatory exact text:

- `anchor_core: 17 sources / 19 rows`
- `bridge_core: 15 sources / 15 rows`
- `Adjacent: feasibility and boundary evidence`
- `Foundational: theory and transferable hypotheses`
- `Boundary: HC01 / TW-02 not counted as stable Core`
- `role -> layer -> evidence status`

Style:

- Refined journal-ready infographic.
- Warm off-white background.
- Muted deep green for `anchor_core`.
- Muted light green for `bridge_core`.
- Muted blue for `Adjacent`.
- Muted tan or gray for `Foundational` and `Boundary`.
- Crisp vector-like shapes, generous whitespace, readable labels.

Claim boundary:

- Do not imply `bridge_core` is equivalent to `anchor_core`.
- Do not place `Adjacent` or `Foundational` inside the stable Core evidence-map boundary.
- Do not imply `HC01` or `TW-02` are counted in stable widened Core.

Let the image model choose the exact geometric composition, but preserve the role hierarchy and mandatory text exactly.

### QA Checklist

- `anchor_core` is visually strongest.
- `bridge_core` is connected but lower weight.
- `Adjacent`, `Foundational`, and `Boundary` are outside the Core boundary.
- No extra counts or evidence categories appear.

## Figure 2. PRISMA-ScR Screening and Evidence-Map Stabilization

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_2_prisma_scr_flow.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/11_Silacci2026_LLM_Agents_Scoping_Review/figures/figure1_the_prisma_preferred_reporting_items_for_systematic_reviews_and_meta_analyses_flowchart_provided_by_covidence_with_the_search_and_the_selection_proces.png`
- `assets/survey_paper/exemplar_assets/12_Leiser2025_LLM_Architectures_Scoping_Review/figures/figure1_prisma_scr_preferred_reporting_items_for_systematic_reviews_and_meta_analyses_extension_for_scoping_reviews_flowchart_for_inclusion_and_exclusion_of_m.png`
- `assets/survey_paper/exemplar_assets/13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure2_prisma_flow_chart.png`
- `assets/survey_paper/exemplar_assets/15_Peters2024_JBI_Scoping_Reviews/figures/figure11_5_flow_diagram_for_the_scoping_review_process_adapted_from_the_prisma_statement_by_moher_and_colleagues_2009.png`

Do not use `14_Tricco2018_PRISMA_ScR/figures/figure1_methods_flow_416.png` as a visual reference because the local extraction captured a reference-list page artifact rather than the flow diagram itself.

### Prompt

Create a polished two-panel academic PRISMA-style information graphic titled exactly:

`Figure 2. Screening and Evidence-Map Stabilization`

What this figure is: a method-flow diagram for a scoping-review survey. It separates formal bibliographic screening counts from later row-level evidence-map stabilization.

Why the paper needs it: readers may otherwise confuse the initial `Core = 12` bibliographic screening result with the later stable widened Core of `32` paper-level sources and `34` coded rows.

Reader takeaway: Panel A reports bibliographic screening; Panel B reports full-text recheck, widened bridge review, boundary decisions, and final coded evidence-map stabilization. These are different counting layers.

Use the reference images only for visual discipline:

- Borrow stage bands and clean blue-outline PRISMA styling from Silacci.
- Borrow explicit stage labels and right-side exclusion boxes from Leiser.
- Borrow classic vertical flow and side-exclusion logic from Tudor-Car and JBI.
- Do not copy exemplar database names, duplicate-removal counts, exclusion reasons, article totals, or included-study counts.

Required visual structure:

- Two large panels with clear separation.
- Panel A should feel PRISMA-like and procedural.
- Panel B should feel like evidence-map curation and stabilization, not another database-screening step.
- Add a labeled transition between panels: `full-text recheck + row-level coding`.

Mandatory exact text:

- `Bibliographic screening`
- `Records screened: 417`
- `Core: 12`
- `Adjacent: 42`
- `Foundational: 47`
- `Excluded: 316`
- `E1: 85 / E2: 54 / E3: 177`
- `Evidence-map stabilization`
- `Strict anchor: 17 sources / 19 rows`
- `Bridge review`
- `HC01: Adjacent`
- `TW-02: boundary only`
- `Stable widened Core: 32 sources / 34 rows`
- `screening counts != coded rows`

Style:

- Academic PRISMA-inspired layout.
- Pale blue-gray stage backgrounds.
- Charcoal text and thin dark outlines.
- Muted green for included or stable Core boxes.
- Muted red or rose for excluded boxes.
- Muted yellow or tan for boundary decisions.
- Avoid dense paragraphs.

Claim boundary:

- Do not collapse `Core: 12` into `Stable widened Core: 32 sources / 34 rows`.
- Do not imply `Adjacent` and `Foundational` are discarded evidence.
- Do not imply all screening categories have the same claim strength.

Let the image model choose exact flow geometry, but preserve the two-panel count distinction and mandatory text exactly.

### QA Checklist

- Panel A and Panel B are visually separate.
- The transition says `full-text recheck + row-level coding`.
- No exemplar counts or database names appear.
- `screening counts != coded rows` is visible.

## Figure 3. Agent-Accessible Spatial Representation Taxonomy

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_3_l0_l5_taxonomy.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure2_a_taxonomy_of_large_language_model_empowered_spatial_intelligence_with_representative_examples.png`
- `assets/survey_paper/exemplar_assets/07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure2_a_taxonomy_of_large_language_model_agent_methodologies.png`
- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure4_conceptual_framework_of_abstract_spatial_reasoning_the_framework_illustrates_three_primary_dimensions_of_spatial_reasoning_capabilities_qualitative_re.png`

### Prompt

Create a polished academic taxonomy diagram titled exactly:

`Figure 3. Agent-Accessible Spatial Representation Taxonomy`

What this figure is: a coding taxonomy for a survey evidence map. It defines `L0` to `L5` by what spatial information the agent can consume, not by what the simulator, dataset, or analyst has in the background.

Why the paper needs it: readers may incorrectly assume a rich backend such as a 3D engine, GIS layer, or graph analysis automatically means the agent receives high-level spatial representation.

Reader takeaway: the coding level is determined by the agent-facing interface. Backend richness only counts when exposed to the agent.

Use the reference images only for visual discipline:

- Borrow taxonomy credibility and left-to-right expansion from Feng's taxonomy.
- Borrow survey-method category structure from Luo's methodology taxonomy.
- Borrow compact conceptual cards and a challenge strip from Feng's abstract spatial reasoning figure.
- Do not copy citation-heavy boxes, spatial-intelligence labels, or LLM-agent methodology labels.

Required visual structure:

- A clear sequence or taxonomy from `L0` to `L5`.
- A lower backend strip with `text-only`, `2D grid`, `graph`, and `3D engine`.
- A visual filter or warning showing that backend richness only counts when exposed to the agent interface.
- Counts should appear as secondary badges or small chips.

Mandatory exact text:

- `code agent input, not backend`
- `L0 none: 0`
- `L1 labels: 1`
- `L2 semantic scene: 8`
- `L3 local relations: 18`
- `L4 global abstract: 1`
- `L5 geometry / embodiment: 6`
- `text-only`
- `2D grid`
- `graph`
- `3D engine`
- `rich backend != higher level unless agent-facing`

Style:

- Refined academic taxonomy.
- Warm off-white background.
- Six level cards with subtle color progression.
- Bottom backend strip in muted gray-blue.
- Crisp connectors, readable labels, minimal icons.

Claim boundary:

- Do not show the taxonomy as a simple maturity ladder where higher always means better.
- Do not imply that `3D engine` automatically means `L5`.
- Do not imply that researcher-side network analysis automatically means `L4`.
- Do not imply `L4` is field-wide or validated; it is sparse in the evidence map.

Let the image model decide whether to use a connected taxonomy tree or a stepped sequence, but the agent-interface rule must dominate the composition.

### QA Checklist

- All six levels appear exactly once.
- Backend strip is visually separate from coded agent input.
- The warning about rich backend is prominent.
- Counts are correct: `0, 1, 8, 18, 1, 6`.

## Figure 4. Representation Distribution by Core Layer

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_4_representation_distribution.svg` rendered to PNG

Visual reference:

- `assets/survey_paper/exemplar_assets/13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure3_bubble_plots_showing_the_distribution_of_identified_study_designs_types_of_conversational_agents_and_healthcare_topics_in_the_included_articles_plotte.png`

### Prompt

Create a polished academic distribution chart titled exactly:

`Figure 4. Representation Distribution by Core Layer`

What this figure is: a row-level evidence-map distribution chart. It shows how `L1` to `L5` representation levels are distributed across `anchor_core` and `bridge_core`.

Why the paper needs it: the survey's key descriptive finding depends on preserving the split between the strict anchor nucleus and the widened bridge layer.

Reader takeaway: the strict anchor is concentrated at `L3`, while `L2` and the only admitted `L4` case come from the bridge layer. Bridge recovery broadens the map but is not anchor evidence.

Use the reference image only for visual discipline:

- Borrow compact category-based distribution logic.
- Borrow clear separation between categories and count encoding.
- Do not copy publication-year axes, healthcare categories, three-panel structure, or bubble-size legend.

Required visual structure:

- Prefer stacked or grouped bars by level.
- X-axis levels: `L1`, `L2`, `L3`, `L4`, `L5`.
- Show `anchor_core` and `bridge_core` as separate colors.
- Make the `L4` gap in `anchor_core` visually obvious.
- Print exact values where feasible.

Mandatory exact text:

- `anchor_core`
- `bridge_core`
- `L1`
- `L2`
- `L3`
- `L4`
- `L5`
- `L1: 1 anchor / 0 bridge`
- `L2: 0 anchor / 8 bridge`
- `L3: 15 anchor / 3 bridge`
- `L4: 0 anchor / 1 bridge`
- `L5: 3 anchor / 3 bridge`
- `L4 absent from anchor_core`
- `bridge recovery is not anchor evidence`

Mandatory data:

- `L1`: `1 anchor`, `0 bridge`, `1 total`
- `L2`: `0 anchor`, `8 bridge`, `8 total`
- `L3`: `15 anchor`, `3 bridge`, `18 total`
- `L4`: `0 anchor`, `1 bridge`, `1 total`
- `L5`: `3 anchor`, `3 bridge`, `6 total`
- Total: `19 anchor`, `15 bridge`, `34 rows`

Style:

- Publication-safe chart.
- Warm off-white background.
- Dark muted green for `anchor_core`.
- Light green or pale blue-green for `bridge_core`.
- Crisp axes, large readable labels, no percentages.
- Minimal gridlines.

Claim boundary:

- Do not visually merge `anchor_core` and `bridge_core`.
- Do not imply `L4` is solved.
- Do not add extra data series, percentages, or trend lines.

Let the image model choose grouped or stacked bars, but exact counts and the `L4` caution must remain clear.

### QA Checklist

- `L3` is visibly dominant in `anchor_core`.
- `L2` is entirely bridge.
- `L4` has no anchor bar.
- No percentages or invented totals appear.

## Figure 5. Local Adjacency Is Not Global Configuration

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_5_local_vs_global_configuration.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure1_multiple_scale_spatial_intelligence_in_real_world_from_embodied_spatial_intelligence_to_earth_spatial_intelligence.png`
- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure4_conceptual_framework_of_abstract_spatial_reasoning_the_framework_illustrates_three_primary_dimensions_of_spatial_reasoning_capabilities_qualitative_re.png`
- `assets/survey_paper/exemplar_assets/01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure2_a_taxonomy_of_large_language_model_empowered_spatial_intelligence_with_representative_examples.png`

### Prompt

Create a polished academic worked-example graph titled exactly:

`Figure 5. Local Adjacency Is Not Global Configuration`

What this figure is: a toy graph explanation for a survey paper. It explains why an agent receiving only immediate-neighbor information is coded as `L3` local relations, while claims about whole-layout position require `L4` global abstract configuration.

Why the paper needs it: readers may confuse local adjacency with global configuration. The figure should make the distinction visually obvious without equations.

Reader takeaway: two focal locations can have the same local degree and identical egocentric neighborhoods, yet occupy different positions in the whole layout.

Use the reference images only for visual discipline:

- Borrow multi-scale explanatory contrast from Feng's scale figure.
- Borrow clean graph-reasoning iconography and conceptual cards from Feng's abstract spatial reasoning figure.
- Borrow taxonomy separation between graph-theoretical reasoning and other spatial representations from Feng's taxonomy.
- Do not use real-world robot, city, or earth imagery.
- Do not copy dense taxonomy boxes or citations.

Required visual structure:

- Two-panel layout.
- Panel A shows two separate egocentric mini-graphs that look structurally equivalent.
- Panel B shows the same highlighted nodes inside a larger connected graph.
- In Panel B, node `B` should sit near the main spine or central corridor.
- In Panel B, node `G` should sit deeper in a side branch.

Mandatory exact text:

- `Local view: same immediate neighbors`
- `B: local degree 2`
- `G: local degree 2`
- `Whole-layout position differs`
- `L3: local adjacency`
- `L4: global configuration`
- `local neighbors do not equal depth, integration, control, or choice`

Style:

- Clean node-link graph visuals.
- Warm off-white background.
- Pale blue-gray panel cards.
- Charcoal lines and text.
- Muted green highlight for node `B`.
- Muted amber highlight for node `G`.
- High contrast, generous spacing, no equations.

Claim boundary:

- This is an explanatory toy diagram, not empirical evidence.
- Do not imply global graph metrics are currently exposed to most LLM agents.
- Do not add equations or named formulas for integration, depth, control, or choice.

Let the image model choose the exact graph shape, but preserve the logical contrast between identical local views and different whole-layout positions.

### QA Checklist

- Panel A local views are structurally equivalent.
- Panel B shows different global positions.
- `B` and `G` retain consistent colors across panels.
- No extra graph metrics or formulas appear.

## Figure 6. Research Agenda Map

### Input Images To Provide

Edit target:

- `spatial-agent-survey/paper/figures/figure_6_research_agenda_map.svg` rendered to PNG

Visual references:

- `assets/survey_paper/exemplar_assets/05_Mou2024_Social_Simulation_LLM_Agents_Survey/figures/figure4_illustration_of_society_simulations_to_construct_society_simulations_the_corresponding_society_s_construction_elements_i_e_com_position_network_social.png`
- `assets/survey_paper/exemplar_assets/05_Mou2024_Social_Simulation_LLM_Agents_Survey/figures/figure7_illustration_of_society_simulation_trend_which_goes_through_three_stages_constructing_preliminary_environments_exploring_alignment_on_specific_scenari.png`
- `assets/survey_paper/exemplar_assets/07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure1_an_overview_of_the_llm_agent_ecosystem_organized_into_four_interconnected_dimensions_agent_methodology_covering_the_foundational_aspects_of_constructi.png`
- `assets/survey_paper/exemplar_assets/07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure4_an_overview_of_real_world_issues_in_llm_agent_systems_organized_into_three_domains_security_challenges_including_agent_centric_and_data_centric_threat.png`

### Prompt

Create a polished academic research-agenda map titled exactly:

`Figure 6. Research Agenda Map`

What this figure is: a future-work map derived from the survey's evidence map. It organizes the research agenda around the observed gap between concentrated `L3` evidence and sparse `L4` evidence.

Why the paper needs it: Section 7 must move from descriptive evidence gaps to concrete future-work directions without overstating current results.

Reader takeaway: future work should progress from explicit agent-facing spatial representation to mechanism tests, emergent social measures, generalization checks, and application-specific validation. Each step requires exposed structure plus observed evidence.

Use the reference images only for visual discipline:

- Borrow construction-element plus evaluation organization from Mou's society-simulation figure.
- Borrow forward-moving roadmap logic from Mou's society-simulation trend figure.
- Borrow quadrant overview clarity from Luo's agent ecosystem figure.
- Borrow matrix grouping and dashed dividers from Luo's real-world-issues figure.
- Do not copy cartoon-heavy icons, paper names, scenario examples, or dense category lists.

Required visual structure:

- A central evidence-map result or starting point.
- Five agenda directions connected from the center or arranged as a staged roadmap.
- The guardrail should visually apply to the whole agenda, not appear as a hidden footnote.
- The figure must read as future work, not current empirical proof.

Mandatory exact text:

- `Evidence-map result: L3 concentrated / L4 sparse`
- `1. Representation`
- `2. Mechanism`
- `3. Emergence`
- `4. Generalization`
- `5. Applications`
- `future-work claims require exposed structure + observed evidence`

Optional short sublabels, only if space permits:

- `agent-facing spatial input`
- `controlled ablations`
- `multi-agent outcomes`
- `layout families`
- `fit-for-purpose validation`

Style:

- Refined hub-and-spoke or staged roadmap.
- Warm off-white background.
- Muted colors with clear hierarchy.
- Generous whitespace.
- Minimal icons, if any.
- Crisp arrows or connectors.

Claim boundary:

- Do not imply richer spatial representation has already been validated.
- Do not imply a causal pipeline from representation to improved social simulation.
- Do not present future-work directions as current evidence.

Let the image model choose between radial and left-to-right roadmap composition, but preserve the evidence-gap origin, five directions, and global guardrail.

### QA Checklist

- Agenda starts from `L3 concentrated / L4 sparse`.
- All five directions appear once.
- Guardrail is prominent.
- Figure reads as future work, not proof.
