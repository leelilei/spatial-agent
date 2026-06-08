# Table 4. Environment-Side Richness vs Agent-Accessible Structure

Purpose: show why rich backends should not be coded automatically as rich agent-facing spatial representation.

| row | environment-side representation | agent-accessible representation | why this coding matters |
|---|---|---|---|
| `HC06` `Project Sid` | `3D_engine` | `L5` | Direct coordinate-bearing memories and explicit spawn/location state reach the agent interface, so geometry is genuinely agent-facing. |
| `HC10` Real-world community HD social simulation | `3D_engine` | `L3` | The GIS/BIM/Unreal stack is rich, but the agent still receives categorical, prompt-mediated state rather than direct geometry. |
| `HC11` Environment-aware VR roleplay | `3D_engine` | `L2` | Coordinate-like fields are treated as structured text-schema context, not as embodied geometry consumed by the agent. |
| `HC12A` `SimWorld` visual-GPS split | `3D_engine` | `L5` | The embodied split row includes visual plus GPS-like position-bearing input, so geometry is part of the usable interface. |
| `HC12B` `SimWorld` scene-graph split | `3D_engine` | `L3` | The same system family also exposes an abstracted scene-graph/layout interface, which stays below direct geometry. |
| `HC14` Crowd evacuation disaster | `graph_based` | `L3` | A GIS-derived road network with road attributes does not become `L5` when the agent sees only text summaries, nearby communications, and route context. |
| `L4R-01` Network formation among multi-LLMs | `graph_based` | `L4` | This is the one admitted widened bridge case where global abstract structure is truly agent-facing through node degree, neighbors, and community information. |
| `BK06` `TongSIM` | `3D_engine` | `L5` | A platform can expose embodied or geometry-bearing interfaces, but this supports interface feasibility more than direct LLM social-simulation mediation. |
| `R3-05` `CoELA` | `3D_engine` | `L5` | Embodied cooperation is relevant to spatial coordination, but it is a benchmark setting rather than population-level social simulation. |
| `TW-13` `TUMSphere` | `3D_engine` | `L5` | VR guidance and navigation show object-location and route-state integration, not emergent configurational social mediation. |

Reading rule: code what the agent can actually consume, not what the simulator, renderer, or analyst can compute behind the scenes. `L4` and `L5` should remain distinct: global abstract structure, embodied geometry, platform capability, and navigation support license different claims.
