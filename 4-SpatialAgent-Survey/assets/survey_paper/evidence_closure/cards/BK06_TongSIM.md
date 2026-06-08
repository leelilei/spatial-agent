# BK06 Closure Card - TongSIM

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `BK06`

Paper: *TongSIM: A General Platform for Simulating Intelligent Machines*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_adjacent/09_BK06_TongSIM.pdf`
- Full-text markdown: `assets/survey_paper/pdfs/phase1_adjacent/09_BK06_TongSIM.fulltext.md`
- Extraction status: `26` pages, `status: ok`, `text_char_count: 80787`

## Coding Decision

| Field | Decision | Closure assessment |
|---|---|---|
| `core_layer` | `bridge_core` | Keep. TongSIM is a broad embodied-AI simulation platform; it is adjacent rather than a direct LLM social-simulation paper. |
| `environment_side_representation` | `3D_engine` | Keep. It is built on Unreal Engine 5.6 and includes indoor, outdoor, urban, physics, semantic, and NPC systems. |
| `agent_accessible_representation` | `L5` | Keep. Multiple tasks expose embodied sensor streams such as egocentric RGB, depth, voxel grids, RGB-D, 3D LiDAR, GPS, and radial sensors. |
| `behavioral_scale` | `mixed` | Keep. The platform spans navigation, cooperation, social navigation, human-robot interaction, and spatially situated social intelligence tasks. |
| `evidence_status` | `designed_affordance_only` | Keep. It is platform evidence; reported benchmarks are not direct evidence of LLM social behavior effects. |

## Evidence Notes

TongSIM is a high-fidelity simulation platform built on UE5.6 with 115 scenes, semantic annotations, object states, scene metadata, segmentation maps, NPC systems, physics, and indoor/outdoor environments. It supports embodied AI tasks ranging from navigation and home composite tasks to multi-agent cooperation, human-robot social navigation, and spatially situated social intelligence testing.

The `L5` classification is supported by agent-facing sensor channels. Indoor navigation includes egocentric RGB images, depth maps, and voxel grids. The MACS task uses localized radial sensors with distance, orientation, velocity, and sensing range. Robot social navigation uses RGB-D camera, 3D LiDAR, and GPS. S3IT further situates LLM-driven NPCs in 3D rooms and asks a test agent to reason over environment and NPC preferences.

The bridge boundary is equally important. TongSIM is not primarily an LLM-driven social-simulation paper; it is a general simulator and benchmark platform. Its strongest contribution to the survey is showing that embodied, multimodal, high-fidelity spatial infrastructure exists adjacent to LLM-agent social simulation.

## Page/Section Anchors

- Overview and Table 1, pages 1-4: UE5.6 platform, 115 scenes, NPC control, multi-agent support, and benchmark categories.
- Section 3.1-3.4, pages 5-8: architecture, high-fidelity scenes, semantic annotations, physics, and spatial interaction anchors.
- Section 4.1, pages 9-11: egocentric RGB, depth, and voxel-grid observations for navigation.
- Section 4.2, pages 12-13: multi-agent cooperative search and radial local sensors.
- Section 4.4, pages 14-16: robot social navigation with RGB-D, 3D LiDAR, and GPS.
- Section 4.5, pages 17-19: spatially situated social intelligence test with rooms and NPC preferences.

## Claim Boundary

Allowed manuscript use:

- Use `BK06` as a bridge/platform example showing availability of `3D_engine / L5` embodied simulation infrastructure.
- Use it to contrast rich platform affordances with the more limited agent-facing representations in many LLM social-simulation papers.

Disallowed manuscript use:

- Do not treat TongSIM as anchor-core evidence of LLM-driven emergent social structure.
- Do not imply its L5 affordances are necessarily used by LLM agents in all tasks.
- Do not claim Space Syntax or global configurational metrics unless a specific task exposes them to the agent.

## Follow-Up

No acquisition action is needed. Current coding can remain `bridge_core / 3D_engine / L5 / mixed / designed_affordance_only`.
