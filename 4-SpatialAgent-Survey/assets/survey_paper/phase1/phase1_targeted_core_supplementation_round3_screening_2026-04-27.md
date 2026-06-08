# Phase 1 Targeted Core Supplementation Round 3 Screening

Date: 2026-04-27

Purpose: screen the top five Round 3 supplementation candidates against the current Core boundary after the evidence-map first pass.

Input memo:

- `assets/survey_paper/phase1/phase1_targeted_core_supplementation_round3_2026-04-27.md`

Current gap motivating the screen:

- Current stable Core export has `19` system/configuration rows from `17` paper-level Core items.
- Representation distribution is `L1=1 / L3=15 / L5=3 / L4=0`.
- Evidence-status distribution is `observed_effect=9 / designed_affordance_only=10`.
- Therefore the most useful supplements are not generic LLM-agent papers, but papers that add one of:
  - true configurational `L4` evidence
  - additional `L5` breadth beyond the now-closed single-row observed-effect case
  - optional extra urban/population observed-effect evidence only if later synthesis exposes a manuscript-specific need

## Screening Rule Used Here

A Round 3 candidate can move forward as provisional Core only if it satisfies all of the following:

1. LLM/VLM/generative agents are part of the agent decision architecture.
2. The system is multi-agent, population-level, or explicitly group/crowd/team based.
3. The environment is spatially recognizable: 3D world, city/transport network, grid, road network, building, cellular automata, or proximity space.
4. The reported behavior goes beyond single-agent navigation: cooperation, competition, communication, crowd/population dynamics, epidemic/economic coupling, route adaptation, or other group-level behavior.
5. The paper provides enough evidence to code agent-accessible spatial representation conservatively.

## Top-Five Screening Outcome

| ID | Candidate | Decision | Suggested tier | Suggested repr | Suggested behavior scale | Evidence status | Rationale |
|---|---|---|---|---|---|---|---|
| R3-01 | MineLand: Simulating Large-Scale Multi-Agent Interactions with Limited Multimodal Senses and Physical Needs | Advance | Core | `L5` | `interaction` / `emergent_social_structure` | `observed_effect` | Strongest supplement. Multi-agent Minecraft; VLM/LLM-friendly agent framework; limited raw visual/auditory/tactile observations; distance-limited communication; cooperation, competition, physical needs, and social dynamics are directly evaluated. |
| R3-02 | GATSim: Urban Mobility Simulation with Generative Agents | Advance cautiously | Provisional Core | `L3` | `emergent_social_structure` / `mixed` | `observed_effect` | Urban mobility generative-agent simulation with spatial-temporal memory and macroscopic traffic patterns. Good urban/population supplement, but social interaction is mostly aggregate mobility/system coupling rather than direct interpersonal interaction. |
| R3-03 | Cognitive Agents in Urban Mobility: Integrating LLM Reasoning into Multi-Agent Simulations | Advance cautiously | Provisional Core or Adjacent | `L3` | `mixed` | `observed_effect` | 320 LLM cognitive agents in SimFleet over 20 days; geolocated agents, destinations, transport modes, disruption adaptation. Strong urban mobility case, but may be closer to individual travel-plan adaptation aggregated over a population than social interaction. |
| R3-04 | An LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic-Economic Dynamics | Advance | Core | `L3` | `emergent_social_structure` | `observed_effect` | LLM-driven persons/businesses/government in a 2D abstract city. Physical proximity/contact distance, household/employment networks, movement/work/consumption actions, and macro epidemic-economic trajectories make it a strong proximity-mediated social simulation. |
| R3-05 | Building Cooperative Embodied Agents Modularly with Large Language Models (CoELA) | Demote for current Core; keep as Adjacent | Adjacent / boundary | `L5` | `interaction` | `observed_effect` | Strong embodied cooperation paper with raw sensory observations, costly communication, and multi-agent tasks. However, it is primarily a cooperation/embodied benchmark rather than a social simulation or spatial-social effect study. Useful as L5 cooperation boundary evidence. |

## Candidate Notes

### R3-01 MineLand

Decision: `Advance to provisional Core`.

Primary-source evidence:

- arXiv page: `https://arxiv.org/abs/2403.19267`
- HTML full text: `https://ar5iv.labs.arxiv.org/html/2403.19267v2`

Why it fits:

- It is explicitly a multi-agent Minecraft simulator.
- The paper says the simulator supports dozens of agents; the full text reports 48 agents headless and 16 with visual display on a mainstream PC.
- Agent observations include touch, vision, and sound; the visual channel is first-person RGB video.
- Senses are explicitly limited by distance, environmental obstructions, and directional constraints.
- Communication is spatially constrained: messages are received only by agents within a distance threshold.
- Experiments report cooperation, competition, limited-sense communication, physical needs, multitasking, and social dynamics.

Preliminary coding if accepted:

- `environment_side_representation = 3D_engine`
- `agent_accessible_representation = L5`
- `behavioral_scale = interaction` or `emergent_social_structure`
- `behavior_type = cooperation; conflict; dialogue; mobility; other`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- This is the best current candidate for filling the `L5 + multi-agent behavior` gap.

Risk:

- It is still partly a simulator/benchmark paper. The final coding should avoid overclaiming spatial causality unless the experiments isolate spatial constraints such as limited senses or distance-limited communication.

### R3-02 GATSim

Decision: `Advance to provisional Core`, but code conservatively.

Primary-source evidence:

- arXiv page: `https://arxiv.org/abs/2506.23306`
- ScienceDirect / Transportation Research Part C record: `https://www.sciencedirect.com/science/article/abs/pii/S0968090X26000641`
- ScienceDirect / Simulation Modelling Practice and Theory record: `https://www.sciencedirect.com/science/article/pii/S1569190X25001698`

Why it fits:

- It is explicitly an urban mobility simulation with generative agents.
- Agents have socioeconomic profiles, lifestyles, preferences, memory, planning, reaction, and reflection.
- The framework integrates an urban mobility foundation model, agent cognitive systems, and a transport simulation environment.
- The paper reports realistic macroscopic traffic patterns, route learning, incident response, and peak spreading.
- Spatial-temporal associations are part of memory retrieval.

Preliminary coding if accepted:

- `environment_side_representation = graph_based` or transport-network environment
- `agent_accessible_representation = L3`
- `behavioral_scale = emergent_social_structure` or `mixed`
- `behavior_type = mobility; other`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- Good supplement for urban/population-scale spatial behavior and observed aggregate mobility dynamics.

Risk:

- The paper may not show interpersonal social behavior. It should be framed as population-level mobility dynamics rather than social interaction unless full text shows agent-agent coupling beyond shared traffic/network state.

### R3-03 Cognitive Agents in Urban Mobility

Decision: `Advance to full-text sanity check`, but likely weaker than GATSim.

Primary-source evidence:

- MDPI page: `https://www.mdpi.com/1424-8220/25/18/5688`
- PubMed page: `https://pubmed.ncbi.nlm.nih.gov/41012927/`

Why it fits:

- The paper proposes LLM cognitive agents for urban mobility.
- It integrates the architecture into SimFleet.
- It reports a 20-day simulation involving over 320 individuals.
- Agents dynamically generate, adjust, and reflect on travel plans.
- The system includes geolocated agents, positions, destinations, transport modes, and disruption adaptation.
- Experimental results report emergent adaptation patterns under stable and disrupted transport conditions.

Preliminary coding if accepted:

- `environment_side_representation = graph_based`
- `agent_accessible_representation = L3`
- `behavioral_scale = mixed`
- `behavior_type = mobility; other`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- Useful as urban mobility population evidence, especially if we want more built/urban cases.

Risk:

- It may be closer to many single agents adapting their own travel plans than a social simulation with meaningful interaction. If screened strictly, it may become Adjacent rather than Core.

### R3-04 LLM-Driven Epidemic-Economic Dynamics

Decision: `Advance to provisional Core`.

Primary-source evidence:

- MDPI page: `https://www.mdpi.com/2078-2489/17/3/259`

Why it fits:

- The system is explicitly an LLM-driven multi-agent simulation.
- The simulation environment is a rectangular 2D grid abstract city.
- Agents include persons, businesses, and government.
- Person agents move, work, consume, and deliberate about health/economic tradeoffs.
- Disease transmission is spatially mediated by physical proximity/contact distance.
- The environment includes a social household layer, an employment/business layer, a government layer, and a dynamic physical contact layer.
- The paper reports emergent epidemic-economic trajectories and robustness across LLM backends.

Preliminary coding if accepted:

- `environment_side_representation = 2D_grid`
- `agent_accessible_representation = L3`
- `behavioral_scale = emergent_social_structure`
- `behavior_type = cooperation; conflict; mobility; other`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- Strong supplement for proximity-mediated social simulation and observed macro effects.

Risk:

- The spatial environment is abstract, not built-environment rich. It will not fill the `L5` gap, but it does strengthen the `observed_effect` side of the evidence map.

### R3-05 CoELA

Decision: `Do not add to Core now`; keep as Adjacent/boundary.

Primary-source evidence:

- arXiv page: `https://arxiv.org/abs/2307.02485`

Why it is valuable:

- It addresses multi-agent cooperation with decentralized control.
- It uses raw sensory observations, costly communication, memory, planning, and execution.
- It reports embodied environments, long-horizon tasks, and emergent effective communication.
- It is peer-reviewed at ICLR 2024.

Why it is not Core under the current scope:

- The unit of contribution is an embodied cooperation method/benchmark, not a spatial social simulation.
- The social behavior is task cooperation rather than broader situated social behavior, group structure, or spatially mediated social effects.
- It is useful for L5 embodied-agent boundary discussion, but it would dilute the Core corpus if treated as equal to Generative Agents, Project Sid, CitySim, OASIS, or AgentSociety.

Recommended use:

- Adjacent/boundary evidence for `L5` embodied cooperation.
- Use if the manuscript needs to explain why raw sensory embodied-agent papers are related but not the main Core corpus.

## Screening Summary

Advance as provisional Core:

- `R3-01` MineLand
- `R3-02` GATSim
- `R3-04` LLM-driven epidemic-economic dynamics

Advance to full-text sanity check, likely borderline:

- `R3-03` Cognitive Agents in Urban Mobility

Keep as Adjacent/boundary:

- `R3-05` CoELA

## Recommendation

Do not start a broad search.

Next operational step:

1. Do not reopen broad search.
2. `R3-01`, `R3-02`, and `R3-04` have now been admitted into the stable first-pass coding table.
3. Keep `R3-03` as reserve and `CoELA` as Adjacent unless the review scope is deliberately expanded to embodied cooperation benchmarks.
4. Treat targeted Round 3 as closed unless a new manuscript need appears after synthesis.

Expected effect if the three strongest candidates survive:

- Core paper-level evidence increases by about `3`.
- The evidence map gains at least one new `L5 + multi-agent observed/bounded-interaction` case via `MineLand`.
- The `observed_effect` side strengthens via `GATSim` and epidemic-economic dynamics.
- The `L4` gap likely remains, which is increasingly interpretable as a real literature pattern rather than merely missing search.

## Full-Text Acquisition Addendum

Added 2026-04-27:

- Local full-text sanity memo: `assets/survey_paper/phase1/phase1_round3_fulltext_sanity_check_2026-04-27.md`
- `R3-01` MineLand: valid PDF acquired and sanity checked.
- `R3-02` GATSim: valid PDF acquired and sanity checked.
- `R3-03` Cognitive Agents in Urban Mobility: MDPI direct PDF request returned access-denied HTML; Jina/Markdown full text archived and sanity checked. Decision remains borderline.
- `R3-04` LLM-driven epidemic-economic dynamics: MDPI direct PDF request returned access-denied HTML; Jina/Markdown full text archived and sanity checked. Decision remains Core candidate.

Net update: `R3-01`, `R3-02`, and `R3-04` have now been added to the stable first-pass coding table. `R3-03` should remain reserve/Adjacent unless the manuscript needs a second urban mobility population case, and no further action should be driven by `HC13` or `HC14` because those blockers are already closed.
