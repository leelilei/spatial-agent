# HC15 Closure Card - CitySim

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC15`

Paper: Bougie and Watanabe 2025, *CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/13_HC15_CitySim.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/13_HC15_CitySim.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC15_CitySim_Modeling_Urban_Behaviors_and_City_Dynamics_with_Large_Scale_LLM_Driven_A.md`
- Extraction status: `pdfplumber`, `13` pages, `status: ok`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. CitySim is a large-scale LLM-driven urban social simulation framework. |
| `environment_side_representation` | `graph_based` | Keep. The city is represented through urban areas, POIs, distance/proximity, home/work/school anchors, transport options, and co-location/social networks. |
| `agent_accessible_representation` | `L3` | Keep. Agents use place candidates, POI descriptions/beliefs, location memory, proximity, distance, transport choices, and co-location; no whole-network/global configurational metrics are shown as agent inputs. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The reported outcomes include city-scale activity distributions, POI popularity, crowd density, well-being prediction, dialogue, mobility, and event reaction. |
| `evidence_status` | `observed_effect` | Keep. The paper compares simulated outputs with time-use data, POI popularity, crowd density, and ablation results. |

## Evidence Notes

CitySim provides strong evidence for a graph/place-level urban interface. Agents have demographic personas, spatial anchors such as home and work/school, temporal/reflective/spatial memory, needs, long-term goals, place beliefs, and mobility modules. The spatial memory stores beliefs about POIs across attributes such as price, atmosphere, satisfaction, and convenience. Place selection uses macro-level area selection and micro-level POI selection, combining distance, popularity, POI type, and belief-weighted gravity.

The environment-side representation is best coded as `graph_based` rather than `3D_engine`. The paper grounds home/work/school assignments in OpenStreetMap and Japanese population density, considers nearby areas and candidate POIs, and models available transport modes such as walk, bicycle, car, bus, and train. It also includes a weighted social network and face-to-face interactions for co-located agents.

The agent-accessible representation remains `L3`. Agents reason over structured place candidates, distances, POI descriptions, beliefs, current location, time, weather, transport options, and co-located partners. This is richer than a simple text-only state but still not `L4`: the paper does not show agents receiving global graph centrality, community structure, axial-line integration, whole-city betweenness, visibility graphs, or other global configurational measures. It is also not `L5`, because no first-person images, depth, meshes, or embodied sensor streams are exposed.

Observed-effect status is supported. CitySim reports macro-level activity realism against Japanese time-use statistics, POI popularity prediction in Shibuya, crowd-density heatmap comparison against smartphone location data, well-being prediction, and ablation studies showing reduced scores when removing belief, recursive planning, long-term goals, needs, or persona. These effects support the urban-social simulation row. The manuscript should avoid claiming that the paper isolates a Space Syntax mechanism.

## Page/Section Anchors

Use these anchors for manuscript support:

- Method, pages 2-3: persona module, spatial anchors, temporal/reflective/spatial memory, belief and perception modules.
- Section 3.2, pages 3-4: recursive planning, place selection, gravity model, distance decay, POI candidates, transport choice, and social co-location.
- Section 4, pages 4-6: time-use distribution, POI popularity, crowd density, and well-being evaluations.
- Appendix A, pages 9-10: OpenStreetMap-based home/work/school assignment, nearby-area and POI candidate limits, transport modes, and memory node schema.
- Appendix C.4-C.5, pages 12-13: belief estimation and ablation study.

## Claim Boundary

Allowed manuscript use:

- CitySim is a strong anchor example of LLM agents using place-level urban structure, spatial memory, distance, POI beliefs, and transport choices.
- It supports `graph_based / L3 / observed_effect` because place selection and mobility are operationalized and evaluated against urban data.
- It can support the argument that LLM-agent urban simulation is moving toward structured spatial environments, but mostly through POI/graph/place abstractions.

Disallowed manuscript use:

- Do not code CitySim as `L4`; global urban analytics are not shown as direct agent inputs.
- Do not claim CitySim demonstrates Space Syntax integration/choice/visibility effects.
- Do not code it as `L5`; it is not an embodied visual-navigation simulator.
- Do not overstate crowd-density or POI-popularity alignment as proof of spatial-configuration causality.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / graph_based / L3 / emergent_social_structure / observed_effect`.
