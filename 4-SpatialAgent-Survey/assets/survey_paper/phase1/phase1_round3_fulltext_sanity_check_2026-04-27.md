# Phase 1 Round 3 Full-Text Sanity Check

Date: 2026-04-27

Purpose: validate the locally acquired Round 3 supplementation materials before editing the Core coding table.

Input memos:

- `assets/survey_paper/phase1/phase1_targeted_core_supplementation_round3_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_targeted_core_supplementation_round3_screening_2026-04-27.md`

Operational rule: this is a sanity check, not a final coding-table update. A paper can be marked as a Core candidate here only if full text supports all four operative Core conditions: LLM/VLM or generative agents, multi-agent or population setting, recognizable spatial environment, and social/group/population behavior that can be linked to an agent-accessible spatial representation.

## Acquisition Status

| ID | Candidate | Local artifact | Validation result | Status |
|---|---|---|---|---|
| R3-01 | MineLand: Simulating Large-Scale Multi-Agent Interactions with Limited Multimodal Senses and Physical Needs | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-01_MineLand_2024.pdf` | Valid PDF. Parsed as 33 pages with `pdfplumber`; extracted about 88k text characters. | Acquired and sanity checked. |
| R3-02 | GATSim: Urban Mobility Simulation with Generative Agents | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-02_GATSim_2025.pdf` | Valid PDF. Parsed as 56 pages with `pdfplumber`; extracted about 103k text characters. | Acquired and sanity checked. |
| R3-03 | Cognitive Agents in Urban Mobility: Integrating LLM Reasoning into Multi-Agent Simulations | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-03_Cognitive_Agents_Urban_Mobility_2025.fulltext.md` | Direct MDPI PDF request produced access-denied HTML. Jina/Markdown full text is locally archived and sufficient for text-level sanity check. | Full text acquired as Markdown; PDF still blocked. |
| R3-04 | An LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic-Economic Dynamics | `assets/survey_paper/pdfs/phase1_round3_candidates/R3-04_LLM_Epidemic_Economic_Dynamics_2026.fulltext.md` | Direct MDPI PDF request produced access-denied HTML. Jina/Markdown full text is locally archived and sufficient for text-level sanity check. | Full text acquired as Markdown; PDF still blocked. |
| R3-05 | Building Cooperative Embodied Agents Modularly with Large Language Models | Not acquired in this pass | Already demoted to Adjacent/boundary in the screening memo. | Defer unless the scope is deliberately widened to embodied cooperation benchmarks. |

Note: `pdfinfo`, `pdftotext`, and `pdftoppm` were not available in the local shell, so this pass used `pdfplumber` text extraction rather than rendered page inspection. This is sufficient for Core-boundary screening but not for layout-sensitive PDF review.

## Candidate Decisions

| ID | Decision after full-text sanity check | Suggested tier | Suggested environment representation | Suggested agent-accessible representation | Suggested behavior scale | Evidence status | Main caution |
|---|---|---|---|---|---|---|---|
| R3-01 | Advance | Core candidate | `3D_engine` | `L5` | `interaction` / `mixed` | `observed_effect` | Do not overclaim that every reported social result is caused by spatial constraints; code the observed bounded-sense and distance-limited communication evidence explicitly. |
| R3-02 | Advance cautiously | Provisional Core | `graph_based` / transport network | `L3` | `emergent_social_structure` / `mixed` | `observed_effect` | Treat as population-level urban mobility dynamics, not interpersonal social interaction. |
| R3-03 | Keep borderline | Provisional Core or Adjacent | geospatial transport simulation / network | `L3` | `mixed` | `observed_effect` | Strong mobility adaptation case, but direct social interaction is weak. |
| R3-04 | Advance | Core candidate | `2D_grid` | `L3` | `emergent_social_structure` | `observed_effect` | Spatial environment is abstract, so it strengthens observed proximity-mediated social dynamics but not the built-environment or `L5` gap. |
| R3-05 | Do not advance now | Adjacent / boundary | embodied 3D tasks | `L5` | `interaction` | `observed_effect` | Valuable boundary evidence, but it remains a cooperation benchmark rather than a spatial social simulation paper. |

## R3-01 MineLand

Decision: advance as a Core candidate.

Full-text evidence:

- The paper is explicitly a large-scale multi-agent Minecraft simulator.
- The abstract and methods support `64+` agents, and the appendix reports up to `128` headless agents and a `100`-agent combat scenario.
- Agents receive multimodal observation streams: touch, first-person RGB visual information, and sound.
- Perception is spatially bounded by distance attenuation, environmental obstructions, and directional constraints.
- Communication is distance constrained: nearby agents can receive Minecraft chat messages, while auditory and body-language channels are also distance-limited.
- The experiments include social dynamics, cooperation and competition, cooperation efficiency, personality-mediated cooperation, and large-scale combat/scalability examples.
- The agent implementation uses GPT-4 Vision style VLM access, making the agent interface materially closer to raw embodied perception than to a text-only map.

Preliminary coding if admitted:

- `environment_side_representation = 3D_engine`
- `agent_accessible_representation = L5`
- `behavioral_scale = interaction` or `mixed`
- `behavior_type = cooperation; conflict; communication; mobility`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- Best current Round 3 supplement for the `L5 + multi-agent behavior` gap.
- Stronger than HC01 for Core because MineLand is multi-agent and reports group/cooperation/competition behavior, while HC01 remained single-agent navigation in the available full text.

## R3-02 GATSim

Decision: advance cautiously as provisional Core.

Full-text evidence:

- The paper proposes an urban mobility simulation with generative agents.
- The system combines an urban mobility foundation model, generative-agent cognitive architecture, and a transport simulation environment.
- The transport environment uses a network representation with graph, tilemap, and bitmap forms; the graph is the primary LLM-facing structure for scenario generation and reasoning.
- Each activity is associated with a network node, and traffic dynamics are simulated on a transportation network.
- Agent memory includes spatial coverage and temporal scope. Retrieval combines keyword matching, semantic similarity, and spatial-temporal relevance.
- The decision process includes perception, memory retrieval, interaction, and reasoning.
- Experiments report human-agent behavioral comparison, emergent macroscopic traffic patterns, peak spreading, and incident response to a capacity reduction on a specific network link.

Preliminary coding if admitted:

- `environment_side_representation = graph_based`
- `agent_accessible_representation = L3`
- `behavioral_scale = emergent_social_structure` or `mixed`
- `behavior_type = mobility; route adaptation; congestion response`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- Good supplement for urban/population-scale spatial behavior.
- Useful for the observed-effect side of the evidence map because system-level traffic patterns emerge from distributed generative-agent decisions.

Boundary caution:

- The social behavior is mostly mediated through shared mobility infrastructure, congestion, and population-level route adaptation. It should not be described as rich interpersonal social interaction unless a later coding pass finds stronger agent-agent evidence.

## R3-03 Cognitive Agents in Urban Mobility

Decision: keep as borderline; do not rely on it as one of the three stable Round 3 Core additions unless the project explicitly treats urban mobility adaptation as sufficient group behavior.

Full-text evidence:

- The paper integrates LLM cognitive agents into SimFleet.
- SimFleet provides geolocated agents, route-following, spatial localization, infrastructure agents, bus stops, stations, and proximity-based interactions with infrastructure.
- The cognitive architecture uses weekly planning, daily reflection, short-term memory, long-term memory, and environmental context.
- The experiment simulates `320` cognitive agents over `20` days in a Valencia-inspired multimodal transport environment.
- The disruption scenario deactivates `80%` of taxis for five consecutive days, producing observed modal adaptation and memory-dependent behavior.
- Figure captions and methods explicitly frame the result as spatial environments conditioning feasible mobility options while cognitive reasoning determines the final modal choice.

Preliminary coding if admitted:

- `environment_side_representation = graph_based` or geospatial transport network
- `agent_accessible_representation = L3`
- `behavioral_scale = mixed`
- `behavior_type = mobility; disruption adaptation`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- Useful as an urban mobility population case if the review includes mobility-system adaptation as social/group behavior.

Boundary caution:

- The paper is closer to many individual LLM agents adapting travel plans in a shared transport system than to a social simulation with direct interpersonal interaction. It is weaker than GATSim because the group-level coupling is less central to the contribution.

## R3-04 LLM-Driven Epidemic-Economic Dynamics

Decision: advance as a Core candidate.

Full-text evidence:

- The paper proposes an LLM-driven multi-agent simulation for coupled epidemic-economic dynamics.
- The environment is a rectangular `2D` grid abstract city.
- Agent types include Persons, Businesses, and Government.
- Persons can move, work, and consume; Businesses manage workforce and operating mode; Government issues policies and stimulus.
- Epidemic spread is spatially mediated by a contact distance threshold (`d_contact = 1.0`), and disease transmission occurs through a dynamic physical contact layer superimposed on household and employment structures.
- The LLM-driven cognitive architecture uses a Perception-Deliberation-Action loop and constrained observations from the environment.
- Experiments report macro epidemic-economic trajectories across laissez-faire, lockdown/stimulus, and remote-work scenarios; robustness is also tested across population scales and LLM backends.

Preliminary coding if admitted:

- `environment_side_representation = 2D_grid`
- `agent_accessible_representation = L3`
- `behavioral_scale = emergent_social_structure`
- `behavior_type = mobility; economic behavior; epidemic transmission; policy response`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`

Core value:

- Strong supplement for observed proximity-mediated social dynamics.
- Helps balance the current evidence map, which has too many designed-affordance-only rows.

Boundary caution:

- This does not fill the `L5` gap. It is an abstract spatial social simulation, not a high-fidelity built-environment or embodied-perception system.

## Round 3 Outcome

Stable Core candidates after full-text sanity check:

- `R3-01` MineLand
- `R3-04` LLM-driven epidemic-economic dynamics

Provisional Core candidate that can probably be added if population-level urban mobility is accepted as group/social behavior:

- `R3-02` GATSim

Borderline case to keep in reserve:

- `R3-03` Cognitive Agents in Urban Mobility

Adjacent/boundary:

- `R3-05` CoELA

Recommended next action:

1. `R3-01`, `R3-02`, and `R3-04` have now been admitted into the stable first-pass coding table.
2. Keep `R3-03` as reserve only.
3. Keep `CoELA` as Adjacent, and do not continue second-wave screening unless a new manuscript need appears.
