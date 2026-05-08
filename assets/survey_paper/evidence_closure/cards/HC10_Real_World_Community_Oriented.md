# HC10 Closure Card - Real World Community Oriented HD Social Simulation

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC10`

Paper: Lu 2026, *Real world community oriented high-definition social simulation: Combining reinforcement learning and large language models*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/11_HC10_Real_World_Community_Oriented.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/11_HC10_Real_World_Community_Oriented.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC10_Real_world_community_oriented_high_definition_social_simulation_Combining_reinfo.md`
- Extraction status: `pdfplumber`, `16` pages, `status: ok`, DOI `10.1016/j.cities.2025.106468`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. The paper simulates a community-scale population of AI agents using RL plus LLM evaluation in a real-world community setting. |
| `environment_side_representation` | `3D_engine` | Keep. The backend is a high-definition Unreal Engine replica based on real GIS/BIM/community data. |
| `agent_accessible_representation` | `L3` | Keep. The agent/RL state exposes categorical time, action, location, last location, phone usage, and age fields rather than raw geometry or first-person perception. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The system evaluates population-level action, sleep, phone-usage, and location dynamics for 3000 agents. |
| `evidence_status` | `observed_effect` | Keep for community-behavior realism, not for isolated spatial-configuration causality. The paper compares simulated phone usage/action/location patterns against real community data. |

## Evidence Notes

HC10 has a rich environment-side representation. The paper builds a high-definition virtual replica of Yisheng Garden Community in Unreal Engine using real GIS/BIM/community data, with buildings, pathways, entrances, green spaces, apartments, stores, and public areas. The simulation populates this environment with 3000 agents derived from real demographic data.

The closure boundary is the agent-accessible representation. Section 4.6 lists 10 observations: day of week, holiday, hour, minute, current action, last action, current location, last location, phone usage, and age. Movement actions are high-level destinations such as `Go Home`, `Go to Workplace`, `Go to School`, `Go to Public Area`, and `Go to Stores`. Non-movement actions are restricted by location category: home, public area, stores, workplace, and school.

This supports `3D_engine` on the environment side but only `L3` for agent access. Agents operate over time, categorical location labels, destination/action categories, and location-restricted affordances. The paper does not show agent decisions consuming meshes, coordinates, first-person images, depth, metric geometry, route topology, global layout descriptors, or Space Syntax metrics.

The observed-effect coding is valid for reported social-simulation outcomes. The paper evaluates weekly/daily phone usage alignment, sleep/action patterns, group behavior by life stage, and dynamic location distributions against real-world community data. However, the observed outcomes validate the RL+LLM community simulator as a whole. They do not isolate the causal effect of high-definition 3D geometry or layout configuration.

## Page/Section Anchors

Use these anchors for manuscript support:

- Introduction, page 1: high-definition 3D virtual community in Unreal Engine and 3000 AI agents.
- Results, pages 3-8: comparison with real phone usage, action patterns, sleep patterns, and location distributions.
- Section 4.1, page 10: Unreal Engine construction, Yisheng Garden Community, buildings, pathways, entrances, green land, apartments, stores, and public areas.
- Section 4.2, pages 10-11: demographic feature generation and resident attributes.
- Section 4.6, pages 13-14: 10 observations, movement actions, and location-restricted non-movement actions.
- Discussion, pages 9-10: limitations on nearby environments, action variance, and physical/emotional needs.

## Claim Boundary

Allowed manuscript use:

- HC10 is a strong example of a physically rich 3D community simulator with a comparatively shallow agent-facing state interface.
- It supports the environment-side versus agent-accessible distinction: `3D_engine` backend, `L3` categorical location/action interface.
- It can be used as evidence that LLM/RL social simulators are beginning to align population-level behavior with real community data.

Disallowed manuscript use:

- Do not code HC10 as `L5`; the paper does not show raw visual, geometric, or embodied sensor streams entering the agent decision loop.
- Do not claim the 3D built form itself was experimentally isolated as the cause of social behavior.
- Do not treat location distribution validation as Space Syntax evidence.
- Do not infer route-choice, visibility, or global configuration reasoning beyond the listed observation/action fields.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / 3D_engine / L3 / emergent_social_structure / observed_effect`, with the caveat that observed effects are simulator-level behavioral realism rather than isolated spatial-representation effects.
