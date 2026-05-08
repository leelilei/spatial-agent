# HC06 Closure Card - Project Sid

Status: `C3 closed_card_done`

Date: 2026-05-01

Evidence row: `HC06`

Paper: Altera 2024, *Project Sid: Many-agent simulations toward AI civilization*

Current artifact:

- PDF: `assets/survey_paper/pdfs/phase1_core/03_Project_Sid_Altera2024.pdf`
- Markdown dossier: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/HC06_Project_Sid_Many_agent_simulations_toward_AI_civilization.md`
- Extraction status in dossier: `pypdf`, `35` pages, `status: ok`, `text_char_count: 88894`

## Coding Decision

| Field | Current decision | Closure assessment |
|---|---|---|
| `core_layer` | `anchor_core` | Keep. This is a large-scale multi-agent simulation in Minecraft with social and civilizational outcomes. |
| `environment_side_representation` | `3D_engine` | Keep. Minecraft provides an open-ended 3D sandbox environment. |
| `agent_accessible_representation` | `L5` | Keep. The agent configuration includes coordinate-bearing location memories and spawn locations; agents act in Minecraft with embodied action/skill execution. |
| `behavioral_scale` | `emergent_social_structure` | Keep. The paper studies specialization, collective rules, cultural transmission, religion, social relationships, and social graphs. |
| `evidence_status` | `designed_affordance_only` | Consider revising. The paper reports limited spatially relevant outcomes such as spawn-location variability and town/rural differences in meme propagation. This may qualify as limited `observed_effect`, though not mechanism or controlled spatial mediation. |

## Evidence Notes

Project Sid is a Minecraft-based many-agent simulation. The environment-side coding as `3D_engine` is well supported. Agents operate in an open-ended Minecraft world and can talk, act, gather items, move through villages/towns, and participate in social/civilizational processes.

The `L5` agent-facing representation is also supported. The appendix configurations include explicit coordinate-bearing `location_memories` and `spawn_location` fields. Examples include named village/resource locations with approximate coordinates, as well as spawn positions using `x`, `y`, and `z`. This means the agent-facing state is not only a semantic town description; it contains geometry/position-bearing information.

The paper also states that individual progression varies substantially with spawn locations. In the larger cultural transmission simulation, agents live in towns and rural areas, agents migrate between towns, and meme propagation differs between towns and rural areas. This is spatially relevant evidence, but it should be handled carefully: the paper does not isolate spatial representation levels or run matched layout controls.

The current `designed_affordance_only` status is conservative. A stronger row-level coding could be `observed_effect` if the table treats reported town/rural or spawn-location differences as spatially relevant observed outcomes. The manuscript should still avoid mechanism language because these are associations in one system, not controlled configurational mediation.

## Page/Section Anchors

Use these anchors for manuscript support:

- Section 3.1-3.2, pages 6-7: Minecraft environment and spawn-location variability in item progression.
- Section 4.2, pages 8-9: 50-agent Minecraft societies, autonomous actions, social relationships, and social graph measures.
- Section 5.3, pages 15-16: 500-agent multi-society simulation, town/rural populations, migration, meme propagation, and religion spread.
- Appendix C, page 28: specialization configuration with `location_memories` and `spawn_location`.
- Appendix E, pages 33-34: multi-society/cultural transmission configurations with named towns and coordinates.
- Limitations, page 18: authors note weak vision/spatial reasoning, which should temper any `L5` interpretation.

## Claim Boundary

Allowed manuscript use:

- Project Sid is a strong anchor example of geometry/position-bearing agent input in a large-scale LLM-agent simulation.
- It supports the claim that some current systems expose richer embodied or coordinate-bearing spatial input.
- It can support limited discussion of observed spatially relevant associations, especially town/rural or spawn-location differences, if the evidence table is revised accordingly.

Disallowed manuscript use:

- Do not claim Project Sid proves spatial configuration mediates social behavior.
- Do not treat Minecraft embodiment as equivalent to Space Syntax-style `L4` configuration.
- Do not ignore the authors' limitation that agents still lack robust vision/spatial reasoning.
- Do not treat social graph structure as agent-facing global network structure unless the paper shows it was provided to agents.

## Follow-Up

Recommended table action: keep `L5`; consider changing `evidence_status` from `designed_affordance_only` to limited `observed_effect`, or add a note that the observed-effect evidence concerns spawn/town/rural spatial association rather than controlled configurational mediation.

