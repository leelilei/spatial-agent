# HC13 Closure Card - Fire Evacuation Cellular Automata

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC13`

Paper: Dang et al. 2025, *Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/14_HC13_Fire_Evacuation_CA.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/14_HC13_Fire_Evacuation_CA.fulltext.md`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC13_Large_language_model_driven_agents_for_fire_evacuation_simulation_in_a_cellular_.md`
- Extraction status: `pdfplumber`, `13` pages, `status: ok`, DOI `10.1016/j.ssci.2025.106935`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. This is a direct LLM-agent evacuation simulation with multiple agents, local perception, memory, communication, and movement. |
| `environment_side_representation` | `2D_grid` | Keep. The agent simulation is executed in a cellular automata grid, despite being derived from LiDAR/3D reconstruction. |
| `agent_accessible_representation` | `L3` | Keep. Agents receive structured textual descriptions of cell-semantic environment information by direction, compressed movement history, visibility/smoke descriptions, and nearby communication. |
| `behavioral_scale` | `mixed` | Keep. The paper studies individual wayfinding, local interaction, communication, path length, evacuation time, and group-level evacuation outcomes. |
| `evidence_status` | `observed_effect` | Keep. The paper reports differences across LLM groups/control, evacuation paths, evacuation times, communication behavior, and decision changes. |

## Evidence Notes

HC13 is a good example of rich environment acquisition being transformed into a simpler agent-facing representation. The authors scan a real shopping mall using LiDAR, reconstruct a 3D scene, and build a `502 x 206` cellular automaton where each cell represents about `0.4 m x 0.4 m`. They manually add spatial semantics for 62 objects and simulate flames/smoke.

The agent-facing representation is not direct geometry or raw vision. The method explicitly says LLMs cannot directly perceive fire evacuation environments, so the environment is represented for the LLM through a spatial-semantic-cellular model. The system divides the agent field of view into directions, computes visibility and occlusion, and generates descriptive text for 8 or 4 directions. Before movement, prompts integrate structured textual environmental information plus compressed historical movement data.

This supports `L3`, not `L5`. The backend originates from LiDAR and 3D reconstruction, but the LLM agent receives directional textual descriptions, spatial semantics, visibility levels, current/previous movement context, and communications. The paper does not show first-person image, depth-map, raw point cloud, mesh, or direct metric geometry being consumed by the LLM.

Observed-effect status is supported. Experiments compare LLM-driven groups with a Unity/A* control group, report evacuation distances and times, direction changes, dangerous smoke-cell passages, group communication, fire notification behavior, and background-setting effects. These effects support LLM-agent evacuation behavior in a spatially structured CA environment, but they should not be reframed as Space Syntax evidence.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract, page 1: LLM agents with memory/cognition/decision-making in a spatial-semantic cellular automata evacuation environment.
- Section 3.1, pages 2-4: short-term/long-term memory, building layout, fire location, current location/direction, and prompt compression.
- Section 3.2.1, pages 4-5: spatial-semantic-cellular model, 2D grid with height/occlusion, directional perception, and textual descriptions for 8 or 4 directions.
- Section 3.3, page 6: nearby-agent communication within `3.6 m`, short-term memory update, move/communicate/respond actions, and JSON communication.
- Section 4.1, pages 6-7: LiDAR scan, 3D reconstruction, `502 x 206` CA grid, `0.4 m x 0.4 m` cell scale, and 62 spatial semantic objects.
- Section 4.2 and Section 5, pages 7-12: evacuation outcomes, path differences, communication frequency, decision changes, and reasoning-based evacuation decisions.

## Claim Boundary

Allowed manuscript use:

- HC13 supports the claim that LLM agents can use cell-semantic, directionally described evacuation environments for adaptive wayfinding and communication.
- It is useful for the environment-side versus agent-accessible distinction: a 3D-scanned mall becomes an L3 textual/cellular interface for the LLM.
- It supports observed-effect claims about evacuation behavior in this modeled environment.

Disallowed manuscript use:

- Do not code HC13 as `L5`; the agent-facing input is textual/cell-semantic, not raw LiDAR, mesh, image, or depth.
- Do not claim the paper demonstrates global spatial-configuration or Space Syntax effects.
- Do not generalize the results beyond small-N evacuation experiments and the specific mall-fire setup.
- Do not treat the LiDAR/Unity reconstruction itself as proof that agents reason over direct geometry.

## Follow-Up

No acquisition action is needed. Current coding can remain `anchor_core / 2D_grid / L3 / mixed / observed_effect`.
