# Target Figure Reference Analysis for Figure 1-Figure 6

Status: local exemplar PDF extraction pipeline is in place and the figure/table assets are available as flat caption-level PNG/Markdown pairs under `assets/survey_paper/exemplar_assets/`.

This document is the pre-generation analysis layer for rewriting GPT-Image-2 prompts. It should be read before `spatial-agent-survey/paper/figures/gpt_image_2/prompts.md` is revised.

## Reference-use rule

Use the exemplar images as visual and rhetorical references, not as content to copy. The target figures must keep the survey's own counts, labels, and claim boundaries.

Global visual direction:

- Publication-safe academic infographic.
- Sparse exact text; the caption and paper body carry details.
- Prefer clean vector-like geometry, high legibility, and muted color.
- Avoid decorative icons unless they directly clarify a concept.
- Avoid visual claims that make `bridge_core` look equivalent to `anchor_core`.
- Avoid implying `Adjacent` or `Foundational` are direct empirical evidence for spatial effects in LLM-agent societies.

## Figure 1. Corpus and Evidence Roles

Target purpose: explain that the survey separates corpus roles before making claims. The figure must show that evidence strength depends on role, core layer, and evidence status.

Primary reference images:

- `13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure3_bubble_plots_showing_the_distribution_of_identified_study_designs_types_of_conversational_agents_and_healthcare_topics_in_the_included_articles_plotte.png`
- `15_Peters2024_JBI_Scoping_Reviews/figures/table11_3_example_tabular_presentation_of_data_for_a_scoping_review.png`
- `15_Peters2024_JBI_Scoping_Reviews/figures/figure11_3_example_of_data_presentation_ikt_approaches_or_strategies_enablers_barriers_and_outcomes_gagliardi_et_al_2015.png`

What to borrow:

- From Tudor-Car Figure 3: separated panels/lane logic. Different evidence roles can sit in distinct visual regions instead of being forced into one homogeneous box.
- From JBI Table 11.3: scoping-review charting discipline. A role is not merely a visual category; it has a defined function and a defined result type.
- From JBI Figure 11.3: directional conceptual mapping from supporting conditions to approach to outcome. This helps distinguish supporting corpora from the main evidence map.

What not to borrow:

- Do not copy bubble-plot time axes, publication-year framing, or healthcare labels.
- Do not make a dense table as the final figure; Figure 1 should orient readers quickly in the Introduction.
- Do not use overlapping circles in a way that suggests `Adjacent` or `Foundational` overlap into stable widened Core.

Mandatory content:

- `anchor_core: 17 sources / 19 rows`
- `bridge_core: 15 sources / 15 rows`
- `Adjacent: feasibility and boundary evidence`
- `Foundational: theory and transferable hypotheses`
- `Boundary: HC01 / TW-02 not counted as stable Core`
- Claim rule: `role -> layer -> evidence status`

Prompt implication:

The image model should build a central Core boundary with a strong inner `anchor_core` nucleus and a visibly lighter `bridge_core` layer. `Adjacent`, `Foundational`, and `Boundary` should be outside the Core boundary as support lanes or side cards. Counts should be large enough to read, but hierarchy should be carried by containment and color weight, not by long prose.

Claim boundary:

`bridge_core` extends the descriptive map under widened rules; it is not equivalent to the strict anchor. `Adjacent` and `Foundational` support feasibility, boundary reasoning, and theory, not direct LLM-agent social-effect claims.

## Figure 2. PRISMA-ScR Screening and Evidence-Map Stabilization

Target purpose: separate bibliographic screening counts from later evidence-map stabilization counts.

Primary reference images:

- `11_Silacci2026_LLM_Agents_Scoping_Review/figures/figure1_the_prisma_preferred_reporting_items_for_systematic_reviews_and_meta_analyses_flowchart_provided_by_covidence_with_the_search_and_the_selection_proces.png`
- `12_Leiser2025_LLM_Architectures_Scoping_Review/figures/figure1_prisma_scr_preferred_reporting_items_for_systematic_reviews_and_meta_analyses_extension_for_scoping_reviews_flowchart_for_inclusion_and_exclusion_of_m.png`
- `13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure2_prisma_flow_chart.png`
- `15_Peters2024_JBI_Scoping_Reviews/figures/figure11_5_flow_diagram_for_the_scoping_review_process_adapted_from_the_prisma_statement_by_moher_and_colleagues_2009.png`

Secondary protocol reference:

- `14_Tricco2018_PRISMA_ScR/figures/figure1_methods_flow_416.png` was extracted as a reference-list/page artifact, not as the flow diagram itself. Do not use it as a visual reference. Keep Tricco 2018 only as the PRISMA-ScR methodological anchor.

What to borrow:

- From Silacci Figure 1: modern PRISMA styling with stage bands, left-side stage labels, pale background group areas, and clean blue outlines.
- From Leiser Figure 1: explicit stage headings and right-side exclusion-reason boxes.
- From Tudor-Car Figure 2 and JBI Figure 11.5: classic vertical flow with side exclusions and added-source side nodes.

What not to borrow:

- Do not include database names, duplicate-removal logic, or article counts from exemplars.
- Do not imply the final `32` stable widened-Core paper-level sources are the same counting layer as `12` bibliographic Core records.
- Do not make the diagram a single PRISMA pipeline only; the second panel must show evidence-map stabilization.

Mandatory content:

- Panel A: `Bibliographic screening`
- `Records screened: 417`
- `Core: 12`
- `Adjacent: 42`
- `Foundational: 47`
- `Excluded: 316`
- `E1: 85 / E2: 54 / E3: 177`
- Panel B: `Evidence-map stabilization`
- `Strict anchor: 17 sources / 19 rows`
- `Bridge review`
- `HC01: Adjacent`
- `TW-02: boundary only`
- `Stable widened Core: 32 sources / 34 rows`
- Note: `screening counts != coded rows`

Prompt implication:

Use a two-panel figure. Panel A should feel PRISMA-like and procedural. Panel B should feel like a stabilization/curation layer, not a continuation of article screening. The visual link between panels should be a labeled transition such as `full-text recheck + row-level coding`, so readers understand why counts change.

Claim boundary:

The figure is methodological. It explains count provenance and scope decisions; it should not imply that all included bibliographic categories support the same claim strength.

## Figure 3. Agent-Accessible Spatial Representation Taxonomy

Target purpose: define `L0-L5` as an agent-facing coding rule and prevent confusion between backend richness and agent-accessible spatial input.

Primary reference images:

- `01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure2_a_taxonomy_of_large_language_model_empowered_spatial_intelligence_with_representative_examples.png`
- `07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure2_a_taxonomy_of_large_language_model_agent_methodologies.png`
- `01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure4_conceptual_framework_of_abstract_spatial_reasoning_the_framework_illustrates_three_primary_dimensions_of_spatial_reasoning_capabilities_qualitative_re.png`

What to borrow:

- From Feng Figure 2: taxonomy-tree credibility and left-to-right category expansion.
- From Luo Figure 2: method-survey visual language with a root concept, mid-level categories, and right-side concrete examples.
- From Feng Figure 4: high-level card layout with compact conceptual examples and an explicit challenge strip.

What not to borrow:

- Do not copy the dense literature-citation boxes from either taxonomy figure.
- Do not make `L0-L5` look like a simple maturity ladder where higher is always better.
- Do not use "spatial intelligence" levels from Feng as our levels; our levels are agent-accessible representation levels.

Mandatory content:

- Rule: `code agent input, not backend`
- `L0 none: 0`
- `L1 labels: 1`
- `L2 semantic scene: 8`
- `L3 local relations: 18`
- `L4 global abstract: 1`
- `L5 geometry / embodiment: 6`
- Backend strip: `text-only`, `2D grid`, `graph`, `3D engine`
- Caution: `rich backend != higher level unless agent-facing`

Prompt implication:

Use a left-to-right sequence of six level cards with a lower backend strip. The model can choose whether cards are connected as a taxonomy tree or as a stepped sequence, but the key visual relation must be "agent interface filters backend richness." Counts should appear as secondary badges, not as the main visual logic.

Claim boundary:

`L4` appears once and only in the widened digital-network bridge layer. The figure should frame `L4` as underexplored, not validated as a field-wide standard.

## Figure 4. Representation Distribution by Core Layer

Target purpose: show the row-level distribution of representation levels while preserving `anchor_core` versus `bridge_core`.

Primary reference image:

- `13_TudorCar2020_Conversational_Agents_Scoping_Review/figures/figure3_bubble_plots_showing_the_distribution_of_identified_study_designs_types_of_conversational_agents_and_healthcare_topics_in_the_included_articles_plotte.png`

What to borrow:

- Compact distribution encoding across categories.
- Clear separation between categories without long explanatory text.
- Legend-based reading where mark size/color maps to counts or category membership.

What not to borrow:

- Do not include publication years or three unrelated panels.
- Do not use healthcare categories.
- Do not use bubble size if it makes exact counts hard to read; exact small integers matter here.

Mandatory data:

| level | anchor_core rows | bridge_core rows | total rows |
|---|---:|---:|---:|
| `L1` | 1 | 0 | 1 |
| `L2` | 0 | 8 | 8 |
| `L3` | 15 | 3 | 18 |
| `L4` | 0 | 1 | 1 |
| `L5` | 3 | 3 | 6 |
| total | 19 | 15 | 34 |

Prompt implication:

Prefer a stacked or grouped bar chart with exact labels. Use dark green for `anchor_core` and a lighter green or pale blue-green for `bridge_core`. Add a small callout to `L4` saying `absent from anchor_core`. A bubble variant is acceptable only if every count is printed clearly.

Claim boundary:

The widened bridge layer broadens the descriptive map. It must not visually erase that the strict anchor is concentrated at `L3` and has no `L4`.

## Figure 5. Local Adjacency Is Not Global Configuration

Target purpose: provide a toy example that explains why `L3` local relations are not equivalent to `L4` global abstract structure.

Primary reference images:

- `01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure1_multiple_scale_spatial_intelligence_in_real_world_from_embodied_spatial_intelligence_to_earth_spatial_intelligence.png`
- `01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure4_conceptual_framework_of_abstract_spatial_reasoning_the_framework_illustrates_three_primary_dimensions_of_spatial_reasoning_capabilities_qualitative_re.png`
- `01_Feng2025_Spatial_Intelligence_Across_Scales/figures/figure2_a_taxonomy_of_large_language_model_empowered_spatial_intelligence_with_representative_examples.png`

What to borrow:

- From Feng Figure 1: multi-scale explanatory contrast. It shows how a figure can move from local embodied scenes to broader spatial structures.
- From Feng Figure 4: graph-reasoning iconography and high-level conceptual cards.
- From Feng Figure 2: the idea of separating graph-theoretical reasoning from other spatial representations.

What not to borrow:

- Do not use real-world robot, urban, or earth imagery; our figure is a toy graph.
- Do not imply that whole-layout global measures are currently fed to most LLM agents.
- Do not add equations for integration, control, or choice; the figure is explanatory, not a metric tutorial.

Mandatory content:

- Panel A: `Local view: same immediate neighbors`
- Node `B: local degree 2`
- Node `G: local degree 2`
- Panel B: `Whole-layout position differs`
- `L3: local adjacency`
- `L4: global configuration`
- Bottom note: `local neighbors do not equal depth, integration, control, or choice`

Prompt implication:

Use two panels. Panel A should show two egocentric local neighborhoods that look equivalent. Panel B should reveal the larger graph where one focal node sits near the main spine and the other sits deeper in a branch. The image model should preserve this logical contrast above visual decoration.

Claim boundary:

This is an explanatory diagram. It should not be presented as evidence from a coded system.

## Figure 6. Research Agenda Map

Target purpose: organize future work around the evidence-map gap without overstating current evidence.

Primary reference images:

- `05_Mou2024_Social_Simulation_LLM_Agents_Survey/figures/figure4_illustration_of_society_simulations_to_construct_society_simulations_the_corresponding_society_s_construction_elements_i_e_com_position_network_social.png`
- `05_Mou2024_Social_Simulation_LLM_Agents_Survey/figures/figure7_illustration_of_society_simulation_trend_which_goes_through_three_stages_constructing_preliminary_environments_exploring_alignment_on_specific_scenari.png`
- `07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure1_an_overview_of_the_llm_agent_ecosystem_organized_into_four_interconnected_dimensions_agent_methodology_covering_the_foundational_aspects_of_constructi.png`
- `07_Luo2025_LLM_Agent_Methodology_Survey/figures/figure4_an_overview_of_real_world_issues_in_llm_agent_systems_organized_into_three_domains_security_challenges_including_agent_centric_and_data_centric_threat.png`

What to borrow:

- From Mou Figure 4: agenda components arranged as construction elements plus evaluation.
- From Mou Figure 7: forward-moving research-stage trajectory.
- From Luo Figure 1: quadrant-style survey overview that makes multiple directions scannable.
- From Luo Figure 4: matrix-style grouping with dashed dividers and right-side category labels.

What not to borrow:

- Do not use cartoon-heavy or icon-dense visual language from the exemplars unless simplified.
- Do not list many paper names or scenario examples.
- Do not make the agenda look like a proven pipeline where richer representation automatically improves outcomes.

Mandatory content:

- Center: `Evidence-map result: L3 concentrated / L4 sparse`
- `1. Representation`
- `2. Mechanism`
- `3. Emergence`
- `4. Generalization`
- `5. Applications`
- Guardrail: `future-work claims require exposed structure + observed evidence`

Prompt implication:

Use a hub-and-spoke or staged roadmap. The model can decide between radial and left-to-right layout, but it must show that the agenda starts from an evidence-map gap and moves toward progressively stronger evidence requirements. The guardrail should be visually attached to the whole agenda, not hidden as a small caption.

Claim boundary:

This figure supports future-work claims only. It must not imply that richer spatial representation has already been validated for LLM-agent social simulation.

## Next prompt-writing move

Rewrite `spatial-agent-survey/paper/figures/gpt_image_2/prompts.md` into a v2 prompt file that includes, for each figure:

- What the target figure is.
- Why the paper needs it.
- What the reader should take away.
- Which reference images to provide.
- Mandatory text/data.
- Claim boundaries.
- Overall style constraints.
- A short instruction that lets GPT-Image-2 decide exact composition within these constraints.
