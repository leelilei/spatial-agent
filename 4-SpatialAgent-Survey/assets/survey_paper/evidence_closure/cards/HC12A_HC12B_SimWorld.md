# HC12A/HC12B Closure Card - SimWorld

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence rows: `HC12A`, `HC12B`

Paper: Ren et al. 2025, *SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/12_HC12_SimWorld.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_core/12_HC12_SimWorld.fulltext.md`
- Markdown dossier A: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC12A_SimWorld_visual_GPS_embodied_interface.md`
- Markdown dossier B: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC12B_SimWorld_scene_graph_and_abstract_layout_interface.md`
- Extraction status: `pdfplumber`, `24` pages, `status: ok`

## Coding Decision

| Row | Field | Decision | Closure assessment |
|---|---|---|---|
| `HC12A` | `core_layer` | `anchor_core` | Keep. SimWorld is a direct LLM/VLM-agent simulator for embodied physical and social worlds. |
| `HC12A` | `environment_side_representation` | `3D_engine` | Keep. The backend is Unreal Engine 5 with high-fidelity scenes, assets, physics, weather, traffic, vehicles, robots, and humanoids. |
| `HC12A` | `agent_accessible_representation` | `L5` | Keep. Agents can receive first-person RGB images, depth maps, semantic segmentation masks, GPS-like localization, and visual-based executor inputs. |
| `HC12B` | `core_layer` | `anchor_core` | Keep. This row intentionally captures a different SimWorld interface mode. |
| `HC12B` | `environment_side_representation` | `3D_engine` | Keep. Same Unreal/3D environment-side basis as `HC12A`. |
| `HC12B` | `agent_accessible_representation` | `L3` | Keep. SimWorld also exposes semantic scene graphs, abstract city layout, waypoint navigation, and rule-based action planning that operate as structured symbolic/layout abstractions. |
| Both | `behavioral_scale` | `mixed` | Keep. The paper includes embodied navigation, delivery, economy, cooperation, competition, and social-interaction affordances. |
| Both | `evidence_status` | `designed_affordance_only` for spatial-representation claims | Keep. The paper demonstrates platform capabilities and delivery-task evaluations, but it does not isolate spatial representation as the causal factor. |

## Evidence Notes

SimWorld should remain split because the paper exposes two materially different agent-facing interfaces. The environment itself is clearly a `3D_engine`: Unreal Engine provides realistic rendering, physics, collision, gravity, inertia, weather, lighting, characters, vehicles, robots, humanoid animation, object assets, traffic, and procedural city generation.

`HC12A` captures the embodied visual/GPS interface. Section 2.3.2 says agents can access first-person color images, depth maps, semantic segmentation masks, semantic scene graphs, and GPS-like localization. Section 2.3.4 further distinguishes a visual-based executor that directly consumes visual observations from the simulator, allowing VLM/VLA-style perception-reasoning-action. This supports `L5`: direct visual/geometric/pose-bearing input can enter the agent loop.

`HC12B` captures the structured abstraction interface. The same paper also exposes semantic scene graphs, object/entity relations, GPS-like positions, waypoint graphs, abstract city-layout information, and a rule-based executor that computes paths from symbolic/high-level instructions. This is not a separate environment, but it is a separate agent-accessible representation. It supports `L3`: structured local/semantic/waypoint/layout affordances without requiring direct visual embodiment.

The evidence status should remain conservative for spatial-effect claims. SimWorld reports delivery-task evaluations and ablations involving model competition, environmental configurations, and persona settings. These are useful platform demonstrations, but they do not isolate whether visual input, scene graphs, waypoints, GPS-like localization, or geometry specifically caused an observed social or spatial behavior. The split rows should be used to show representational breadth, not causal spatial mediation.

## Page/Section Anchors

Use these anchors for manuscript support:

- Abstract and Introduction, pages 1-3: SimWorld is an Unreal Engine 5 simulator for LLM/VLM agents with realistic open-ended world simulation and rich multimodal interfaces.
- Figure 2 and Section 2.1, page 4: hierarchical architecture, Unreal backend, environment layer, agent layer, scene graph, GPS, observations, actions, and closed perception-planning-action loop.
- Sections 2.1.1-2.1.3, pages 5-7: handcrafted/procedural scenes, assets, embodiments, weather, lighting, and physical dynamics.
- Sections 2.2.1-2.2.4, pages 8-11: procedural city generation, scene graph editing, waypoint system, and traffic system.
- Section 2.3.1-2.3.4, pages 11-13: agent framework, first-person color/depth/segmentation observations, semantic scene graph, GPS-like localization, high-level/low-level actions, rule-based executor, and visual-based executor.
- Section 3, pages 15-20: delivery task, multi-agent collaboration/competition, action hierarchy, and model/persona/environment ablations.

## Claim Boundary

Allowed manuscript use:

- SimWorld is strong evidence that contemporary LLM/VLM agent platforms can expose both embodied visual/geometric inputs and structured semantic/layout inputs.
- `HC12A` can be used as an `L5` example because visual observations, depth, segmentation, and GPS-like localization are directly agent-accessible.
- `HC12B` can be used as an `L3` example because semantic scene graphs, waypoint/layout abstractions, and rule-based planners support high-level symbolic spatial interaction.
- The split is useful for arguing that one 3D engine can support multiple agent-accessible representation layers.

Disallowed manuscript use:

- Do not merge `HC12A` and `HC12B` into a single representation code if the figure/table is about agent-accessible representation.
- Do not claim SimWorld demonstrates Space Syntax or global configurational metrics.
- Do not use delivery-task profit or action frequency as proof that a specific spatial representation caused behavior.
- Do not assume all SimWorld agents use raw vision; the paper explicitly supports both visual and structured abstraction modes.

## Follow-Up

No acquisition action is needed. Keep the split rows: `HC12A = 3D_engine / L5 / designed_affordance_only`; `HC12B = 3D_engine / L3 / designed_affordance_only`.
