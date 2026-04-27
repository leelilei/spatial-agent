# Phase 1 Targeted Core Supplementation Round 3

Date: 2026-04-27

Purpose: identify a small number of plausible Core supplementation candidates without reopening broad search. This memo is a scan and triage artifact only; existing screening and coding tables were not edited.

## Scope Read Before Search

Read first:

- `docs/plans/survey_plan_v4.md`
- `docs/plans/coding_manual.md`
- `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`
- `assets/survey_paper/phase1/phase1_hc01_travelagent_fulltext_adjudication_2026-04-27.md`

Current operative Core boundary:

- LLM or VLM-driven agents.
- Multi-agent, population, community, society, crowd, or team setting.
- A recognizable spatial environment, not just an abstract task space.
- Some social or group behavior: interaction, communication, cooperation, conflict, mobility, norm formation, social structure, or aggregate urban/crowd dynamics.
- L0-L5 must code agent-accessible spatial representation, not environment backend fidelity.

Current evidence gap from the first-pass coding file:

- `14` coded Core rows from `12` paper-level Core items.
- Most rows are conservative `L3`; only `HC06` and `HC12A` are currently coded `L5`.
- `L4` remains absent.
- `HC13` and `HC14` remain unresolved full-text blockers, but they should not block evidence-map synthesis.
- `HC01` is a strong `3D_engine / L5` built-environment interface case, but is Adjacent because the current experiments are single-agent navigation rather than multi-agent social behavior.

## Search Strategy

This was a targeted supplementation scan, not a new broad PRISMA search. I used narrow query families aimed at gap-filling:

1. Geometry/vision/embodied multi-agent:
   - `"LLM" "multi-agent" "Minecraft" "social" agents`
   - `"MineLand" "LLM" "multi-agent"`
   - `"MINDcraft" "MineCollab" "multi-agent LLM"`
   - `"Building Cooperative Embodied Agents Modularly with Large Language Models"`
2. Built environment, urban, mobility, city, community:
   - `"LLM" "agent-based" "urban mobility" "spatial" "multi-agent"`
   - `"GATSim" "generative agents" "urban mobility"`
   - `"Cognitive Agents in Urban Mobility" "SimFleet"`
3. Crowd, evacuation, crisis, proximity:
   - `"large language model" "pedestrian" "evacuation" "agent-based" simulation`
   - `"crowd dynamics" "large language model" "agent model"`
   - `"LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic-Economic Dynamics"`
4. Spatial-social game environments:
   - `"VillagerAgent" "Minecraft" "large language model" multi-agent`
   - `"Collab-Overcooked" "large language model"`
   - `"LLM-PySC2" "StarCraft II" "Large Language Model"`
   - `"CivRealm" "language agents" "Civilization"`

Source priority was primary paper pages, publisher pages, arXiv/OpenReview/ACL pages, project pages, and author repositories. ResearchGate/SSRN/search-result snippets were used only when primary pages were unavailable or as preprint discovery signals.

## Inclusion and Exclusion Criteria

### Include for Round 3 triage

- Likely LLM/VLM/generative-agent system.
- More than one agent, or a population-level agent-based simulation.
- Explicit spatial environment: 3D world, game map, city network, grid, road network, cellular automata, building, or proximity-based environment.
- Plausible behavior signal: cooperation, communication, mobility adaptation, crowd evacuation, disease/economic spread through proximity, route choice, congestion, norm/cooperation dynamics.
- Potential to fill at least one current gap: `L5`, city/built-environment/crowd setting, or observed spatial-behavior effect.

### Exclude or demote at this stage

- Single-agent navigation, even if spatially rich.
- Generic LLM agent frameworks without spatial environment.
- Debate, code, office-task, or purely textual task-space systems.
- Pure social-network platforms unless later scope re-broadens digital platform environments.
- Embodied task benchmarks where collaboration exists but social/group behavior is too narrow; these are retained only as borderline Core or Adjacent candidates.
- LLM used only as analyst, planner, or evacuation advisor, rather than as the cognitive core of simulated agents.

## Candidate Table

| ID | Title | Year | Source | Link | Why candidate | Core risk | Status |
|---|---|---:|---|---|---|---|---|
| R3-01 | MineLand: Simulating Large-Scale Multi-Agent Interactions with Limited Multimodal Senses and Physical Needs | 2024 | arXiv / GitHub | https://arxiv.org/abs/2403.19267 | Strong gap fit. Multi-agent Minecraft simulator; source reports 64+ agents, limited visual/auditory/environmental awareness, communication and collaboration for physical needs, and collective behavior. Likely `3D_engine`, potentially `L5` if agent observations expose visual/environmental state directly. | Need full-text check on whether LLM/VLM agents are the primary experimental agents and whether behavior is reported as social/group behavior rather than platform capability only. | High-priority Core candidate. Download/read next. |
| R3-02 | GATSim: Urban Mobility Simulation with Generative Agents | 2025/2026 | arXiv / Transportation Research Part C / Simulation Modelling Practice and Theory | https://arxiv.org/abs/2506.23306 | Direct urban mobility simulation with generative agents, spatial-temporal memory retrieval, transport simulation environment, and realistic macroscopic traffic patterns. Fills city/mobility and observed aggregate dynamics gap. | May be mobility ABM rather than social interaction. Need check if agents interact through congestion/system state only or also through social/environmental coupling. Agent-accessible representation may be `L3` rather than `L5`. | High-priority Core candidate, likely city/mobility Core if full text confirms multi-agent spatial coupling. |
| R3-03 | Cognitive Agents in Urban Mobility: Integrating LLM Reasoning into Multi-Agent Simulations | 2025 | Sensors / PubMed | https://www.mdpi.com/1424-8220/25/18/5688 | Integrates LLM cognitive agents into SimFleet; 20-day simulation with 320 individuals; spatially embedded/geolocated agents, transport modalities, positions, destinations, infrastructure, disruptions, and emergent adaptation patterns. | Similar to GATSim: may be better coded as mobility/population behavior than social interaction. Need check whether LLM prompt receives route/map/position data or only trip summaries. | High-priority Core candidate, especially if urban mobility is retained as group behavior. |
| R3-04 | An LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic-Economic Dynamics | 2026 | Information / MDPI | https://www.mdpi.com/2078-2489/17/3/259 | Explicit LLM-driven multi-agent simulation in a rectangular 2D grid abstract city. Includes persons, businesses, government, households, employment links, physical proximity/contact distance, movement, work, consumption, lockdown/stimulus policies, and emergent socio-economic/epidemic trajectories. | Spatial environment is abstract rather than built-environment realistic. Need inspect prompts to determine whether agents receive coordinates/locality/contact information directly. | High-priority Core candidate for grid/proximity-mediated social dynamics. |
| R3-05 | Building Cooperative Embodied Agents Modularly with Large Language Models | 2024 | ICLR / arXiv / project page | https://arxiv.org/abs/2307.02485 | Peer-reviewed embodied multi-agent cooperation paper. Uses decentralized control, raw sensory observations, costly communication, embodied environments, and emergent effective communication; project page names ThreeDWorld Multi-Agent Transport and Communicative Watch-And-Help environments. Useful for L5/vision-like interface and cooperation. | More an embodied cooperation benchmark than social simulation. It supports cooperation/communication, but not necessarily social structure or spatial effects. | Screen as borderline Core; likely strong Adjacent if Core remains strictly social-simulation focused. |
| R3-06 | Collaborating Action by Action: A Multi-agent LLM Framework for Embodied Reasoning | 2025 | arXiv | https://arxiv.org/abs/2504.17950 | Introduces MINDcraft and MineCollab for LLM agents controlling Minecraft characters; tests embodied collaborative reasoning and communication under open-world spatial conditions. | Task/benchmark focus; may not report broader social behavior. Spatial representation likely tool/text mediated rather than raw geometry. | Borderline Core or Adjacent; read after R3-01. |
| R3-07 | VillagerAgent: A Graph-Based Multi-Agent Framework for Coordinating Complex Task Dependencies in Minecraft | 2024 | arXiv/CatalyzeX/GitHub | https://github.com/cnsdqd-dyb/VillagerAgent | Minecraft benchmark with spatial, causal, and temporal constraints; multi-agent collaboration, workload distribution, dynamic adaptation, synchronized execution, and environmental/agent state tracking. | Central graph coordination and task completion may dominate; social/group behavior may be too instrumental. Need primary arXiv/full text and prompt/interface evidence. | Borderline Core. Screen if R3-01/R3-06 confirm a Minecraft cluster worth including. |
| R3-08 | MindAgent: Emergent Gaming Interaction | 2023/2024 | arXiv / NAACL / Microsoft Research | https://arxiv.org/abs/2309.09971 | Multi-agent gaming infrastructure; CuisineWorld involves multiple agents playing simultaneously, collaboration efficiency metrics, VR CuisineWorld deployment, and Minecraft adaptation. | Collaboration benchmark rather than social simulation; space may be game-task layout only. | Borderline Core or Adjacent; useful comparison case for embodied/game collaboration. |
| R3-09 | Agent Model Based on Large Language Model as a Pathway to General Artificial Intelligence in Revolutionizing Crowd Dynamics Research | 2025 | SSRN preprint | https://ssrn.com/abstract=5496390 | Direct crowd dynamics and evacuation candidate. Abstract claims LLM agents identify congestion, adapt movement strategies from real-time data/environmental change, and show enhanced social interactivity. | SSRN/preprint status; title and abstract are ambitious, need methodology quality check. Could overlap with HC13/HC14 but may add a third crowd/evacuation case. | Watchlist. Acquire/read only after peer-reviewed/high-priority candidates. |
| R3-10 | Collab-Overcooked: Benchmarking and Evaluating Large Language Models as Collaborative Agents | 2025 | EMNLP / arXiv | https://arxiv.org/abs/2502.20073 | LLM-MAS benchmark in Overcooked-AI interactive environments, natural-language communication, 30 open-ended tasks, and process metrics for collaboration. | Strong collaboration, but spatial setting is a small task grid and not social simulation. | Likely Adjacent; keep only if task-grid collaboration is needed as boundary evidence. |
| R3-11 | Towards Efficient LLM Grounding for Embodied Multi-Agent Collaboration | 2025 | ACL / arXiv | https://arxiv.org/abs/2405.14314 | Multi-agent LLM planning in embodied tasks; evaluated on Overcooked-AI and RoCoBench variants; reports success and coordination efficiency. | Method paper; spatial representation and social behavior are not the research target. | Adjacent unless full text shows spatial interface evidence needed for taxonomy examples. |
| R3-12 | LLM-PySC2: StarCraft II Learning Environment for Large Language Models | 2025 | NeurIPS OpenReview / arXiv | https://openreview.net/forum?id=Xr73jEYG29 | StarCraft II is spatial and multi-agent; source reports complete PySC2 action space, multimodal information, multi-agent collaboration, and macro/micro decision scenarios. | Benchmark/platform for decision-making rather than social behavior; game strategy may not map cleanly to survey's social-effect claim. | Borderline/Adjacent. Screen only if needing another high-dimensional spatial game environment. |
| R3-13 | CivRealm: A Learning and Reasoning Odyssey in Civilization for Decision-Making Agents | 2024 | ICLR OpenReview / arXiv | https://openreview.net/forum?id=UBVNwD3hPN | Civilization-like map/game environment with changing players, imperfect information, diplomacy and negotiation, and language-agent interfaces. | Primary purpose is benchmark/decision-making; unclear whether experiments are LLM multi-agent social simulation or mostly environment setup. | Borderline/Adjacent. Lower priority than Minecraft/urban/crisis candidates. |
| R3-14 | Embodied LLM Agents Learn to Cooperate in Organized Teams | 2026 | IEEE TCSS / Princeton page | https://doi.org/10.1109/TCSS.2025.3637527 | Multi-agent cooperation with embodied LLM agents, leadership/organization prompts, spontaneous cooperative behavior, and human-agent collaboration. Social behavior is stronger than many task benchmarks. | Need full-text access and environment details; current accessible abstract does not establish agent-accessible spatial representation. | Watchlist. Screen if PDF becomes available. |

## Continuity Checks: Existing Evacuation Blockers

These are not new Round 3 candidates because they are already in the acquisition queue, but they remain high-value if full texts become available:

- `HC13` Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment. ScienceDirect snippets confirm LLM-driven multi-agent fire evacuation, spatial semantics plus cellular automata, shopping mall scenario, and LiDAR/3D reconstruction evidence. Continue PDF acquisition.
- `HC14` When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios. ResearchGate/ScienceDirect metadata indicate pedestrian and vehicle evacuation, environmental observations, decision histories, interpersonal communication, and real-world disaster case study. Continue PDF acquisition.

## Recommended Next Actions

1. Do not restart broad search. Use this memo as a targeted pickup list.
2. Download and full-text screen the top five in this order:
   - `R3-01` MineLand
   - `R3-02` GATSim
   - `R3-03` Cognitive Agents in Urban Mobility
   - `R3-04` LLM-driven epidemic-economic dynamics
   - `R3-05` CoELA
3. For each top-five candidate, create a short full-text sanity note before any table edits:
   - multi-agent confirmed?
   - agent-accessible spatial representation level?
   - social/group behavior confirmed?
   - evidence status: observed effect vs designed affordance only?
   - duplicate/system-family relation to existing Core?
4. If at least `3` of the top five survive as stable Core, stop supplementation and return to evidence-map synthesis.
5. If fewer than `3` survive, screen `R3-06`, `R3-07`, and `R3-09` as second wave. Do not screen the lower-priority benchmark rows unless a specific taxonomy gap remains.
6. Keep `HC13` and `HC14` acquisition running in parallel; they are more valuable than most lower-priority game benchmarks if full text can be obtained.

## Stop Rule

Round 3 should stop when any one condition is met:

- `3-5` new stable Core papers are confirmed from the high-priority list.
- `10` Round 3 candidates have received title/abstract plus primary-source sanity checks.
- Two consecutive high-priority candidates demote for the same reason, indicating a boundary pattern rather than a missing-paper problem.

Do not expand into generic LLM agent, generic embodied AI, generic game AI, or pure social-network simulation after this point. The purpose is not to inflate Core count; it is to fill visible gaps in `L5`, urban/built/crowd environments, and observed spatial-behavior coupling.
