# CitySim Agent Related Projects

Date: 2026-06-22

Working direction: spatial environment x generative agents x verifiable evaluation.

Core question:

> In a constrained but open urban environment, can generative agents form stable, explainable, spatially sensitive daily behavior rather than merely executing scripted schedules?

## Comparison Table

| Project | Main focus | Agent autonomy mechanism | Spatial / world mechanism | Evaluation style | Reproducibility | What it tells us | Gap for our direction |
|---|---|---|---|---|---|---|---|
| [Generative Agents](https://arxiv.org/abs/2304.03442) | Believable social agents in a small town | Memory, reflection, planning, natural-language action | 2D sandbox town; spatial setting is mostly a stage for social behavior | Human believability and ablations of memory/planning/reflection | Code available: [GitHub](https://github.com/joonspk-research/generative_agents) | The classic architecture for memory-reflection-planning agents | Spatial layout is not treated as a causal variable; movement is not the main research object |
| [AI Town](https://github.com/a16z-infra/ai-town) | Deployable starter kit for AI characters living and chatting in a town | Character routines and conversations, inspired by Generative Agents | Shared virtual town with simulation state | Mostly demo/product evaluation | Open-source and easy to extend | Good engineering substrate for visible multi-agent town demos | Not designed as a controlled urban research benchmark |
| [Concordia](https://github.com/google-deepmind/concordia) | General generative agent-based modeling framework | Game Master mediates natural-language actions; modular components for agents and environment | Grounded physical, social, or digital environments through GM | Experiment-design oriented; depends on user-defined scenario metrics | Open-source Python library | Useful pattern: let agents express intent, let environment/GM validate outcomes | It is a framework, not a citysim benchmark; spatial constraints must be built by us |
| [AgentSociety](https://arxiv.org/abs/2502.08691) / [GitHub](https://github.com/tsinghua-fib-lab/agentsociety/) | Large-scale LLM-driven social simulation in urban/social/economic environments | Needs, motivations, cognition, mobility, employment, consumption, social interaction | Realistic societal environment integrating urban, social, and economic spaces | Large-scale performance plus social experiments such as polarization, UBI, hurricanes | Code available; large system | Shows that city/social simulation is moving toward full-stack engines and social-science workflows | Too broad and large; not optimized for small, controlled spatial-causal experiments |
| [CitySim](https://arxiv.org/html/2506.21805) | LLM-driven urban behavior and city dynamics | Needs, long-term goals, recursive value-driven planning, beliefs, spatial/temporal memory | Graph-structured urban environment; belief-aware gravity model for POI choice; transport choice | Time-use distribution, human preference, travel patterns, POI popularity, crowd density, well-being | Some data are proprietary; reproducibility limited | Closest prior art. It directly addresses autonomous schedule generation, spatial memory, place choice, and macro alignment | Still mostly validates aggregate realism; autonomy itself and controlled layout effects are not isolated as first-class evaluation targets |
| [GATSim](https://github.com/qiliuchn/gatsim) / [paper](https://arxiv.org/html/2506.23306) | Generative-agent transport simulation | Memory, planning, reaction, reflection tailored for mobility; dynamic schedule adaptation | Urban transportation environment; agents perceive traffic, events, social context | Travel behavior realism, human annotator comparisons, traffic pattern validation | Open-source prototype | Strong evidence that generative agents can model adaptive mobility better than fixed rules | Transport-centric; less focused on public-space layout, social encounters, and relationship-network formation |
| [OpenCity](https://arxiv.org/abs/2410.21286) / [GitHub](https://github.com/tsinghua-fib-lab/OpenCity) | Scalable simulation of urban activities with massive LLM agents | Group-and-distill prompt optimization; activity simulation at large scale | Six global cities; large-scale urban activity simulation | Compares simulated urban activities with real-world data; emphasizes efficiency | Code repo available | Important for cost reduction and scaling many urban agents | Its main contribution is throughput and scale, not agent will/autonomy or controlled spatial experiment design |
| [CityBench](https://arxiv.org/abs/2406.13945) / [GitHub](https://github.com/tsinghua-fib-lab/CityBench) | Benchmark for LLM/VLM urban tasks | LLMs solve perception-understanding and decision-making tasks | CityData + CitySimu across 13 cities | 8 urban tasks; cross-model/cross-city benchmark | Open-source | Good evaluation vocabulary for urban LLM capabilities | Benchmark is task-oriented, not a long-running life simulation with emergent movement |
| [USTBench](https://arxiv.org/abs/2505.17572) | Urban spatiotemporal reasoning benchmark | LLMs act as urban agents in structured QA and task settings | Interactive city environment UAgentEnv | Understanding, forecasting, planning, reflection with feedback | Benchmark paper; code status should be checked | Useful decomposition of urban reasoning into process-level abilities | Not primarily about autonomous daily life, social encounters, or layout causality |
| [CityEQA](https://arxiv.org/abs/2502.12532) / [GitHub](https://github.com/BiluYong/CityEQA) | Embodied question answering in city space | Hierarchical Planner-Manager-Actor agent | Realistic 3D city simulator; cognitive map; active exploration | Open-vocabulary EQA accuracy and exploration efficiency | Dataset/code available | Strong reference for embodied spatial intelligence and cognitive maps | Goal-directed QA/navigation, not free daily urban behavior |
| [UrbanLLM](https://arxiv.org/html/2406.12360) | Autonomous urban activity planning and management as problem-solving | Decomposes urban queries into sub-tasks and schedules specialized spatiotemporal models | Location-based service and urban management tasks | Query-response accuracy, human-annotated task evaluation, ablations | Code link in paper; status should be checked | Shows LLMs can orchestrate urban-analysis workflows | This is an urban copilot/planner, not simulated resident behavior |
| [TrajAgent](https://github.com/tsinghua-fib-lab/TrajAgent) | Unified trajectory modeling workflow | LLM agent automates data/model workflow for trajectory tasks | UniEnv for trajectory datasets and specialized models | Prediction, linkage, anomaly detection, etc. | Open-source | Useful for trajectory modeling baselines and data workflows | More ML workflow automation than behavioral agent simulation |
| [ChatSUMO](https://arxiv.org/abs/2409.09040) | Natural-language SUMO scenario generation | LLM converts user intent into scripts/scenario settings and summarizes outputs | SUMO + OSM road network generation | Scenario generation success, accuracy, user customization | Paper; implementation status should be checked | Good example of "simulation copilot" rather than "god model" | Does not model autonomous urban residents |
| [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) | High-fidelity robotics simulation and synthetic data | Policies can be tested/evaluated in physically based virtual scenes | Omniverse/OpenUSD, physics, sensors, robotics scenes | SIL/HIL validation, synthetic data, robot testing | Open-source reference framework with licensing caveats | Useful analogy: environment truth and physics stay outside the agent | Too low-level/robotic for our first citysim prototype |
| [NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab) | Robot learning at scale | RL, imitation learning, motion planning, manager/direct workflows | Built on Isaac Sim; GPU-accelerated physics/rendering | Policy training/evaluation in simulation | Open-source, BSD-3-Clause | Shows how to make environment-agent loops measurable and repeatable | Focuses on motor policies, not social/urban cognition |
| [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/) | World foundation models for physical AI | World/action models for reasoning, simulation, action generation, synthetic data | Generative world simulation; physical-scene prediction; closed-loop evaluation | Synthetic data and physical AI policy development | Open models/code under NVIDIA ecosystem | Important conceptual link: world model + policy model + closed-loop evaluation | Too heavy for our current scope; useful as analogy and future layer, not MVP |
| [NVIDIA ENPIRE](https://research.nvidia.com/labs/gear/enpire/) | Agentic robot policy self-improvement in the real world | Coding agents edit policy code, run rollouts, inspect failures, improve policies | Physical robot environment with automatic reset and automatic verification | AutoEnvBench tracks research progress over wall-clock time, not just final success | Research project page | Very relevant as a pattern for verifiable autonomy: reset, verify, roll out, inspect, improve | It optimizes robot task policies; our analogue would optimize/evaluate urban behavior policies |

## What Looks Closest

The closest work to our idea is CitySim, followed by GATSim and AgentSociety.

CitySim already has many components we were imagining: needs, long-term goals, spatial memory, belief updates, recursive activity planning, POI selection, transport choice, and social interactions. This means the broad claim "LLM agents can autonomously move in a city" is no longer novel by itself.

The possible opening is narrower:

> Make autonomy itself measurable in a controlled urban environment.

Instead of competing on city scale or realism, we can build a small benchmark where the independent variables are controlled:

- Same population, different layouts.
- Same layout, different memory policies.
- Same needs and persona, different decision mechanisms.
- Same facilities, different centrality/accessibility.
- Same social graph, different public-space affordances.

## Possible Differentiated Research Question

> Can intention-driven urban agents respond to spatial affordances in a stable, interpretable, and non-scripted way?

Sub-questions:

- Autonomy: Do agents choose differently when needs, memory, spatial cost, and social opportunities conflict?
- Spatial sensitivity: Does changing layout while holding facility count constant change behavior in predictable ways?
- Consistency: Does the same agent retain preferences and relationships over long simulations?
- Constraint compliance: Are plans physically and temporally feasible?
- Mechanism tracing: Can each action be traced to candidate options, internal state, memory retrieval, and environmental constraints?

## Why NVIDIA Physical AI Is Related

NVIDIA's embodied/physical AI stack is not doing city social simulation directly. It is mostly about robots: world models, synthetic data, simulation, policy training, and sim-to-real transfer.

But it is highly related at the architecture level:

| NVIDIA physical AI idea | Urban agent analogue |
|---|---|
| Isaac Sim: high-fidelity physics and sensors | City/world simulator that owns ground truth for space, time, paths, capacity, and events |
| Isaac Lab: repeatable policy training/evaluation loop | Repeatable citysim harness with resettable scenarios and comparable policies |
| Cosmos: world model for physical AI | Possible future world model for generating/forecasting urban scenes and events |
| GR00T / robot foundation models | Possible future "urban resident policy model" or decision policy |
| ENPIRE: coding agents improve robot policies through reset/evaluate/rollout/evolve | Research harness where agents/policies improve through simulated urban rollouts and measurable failures |

The strongest transfer is methodological:

1. Do not let the LLM invent the world state.
2. Make the environment resettable and automatically verifiable.
3. Evaluate trajectories and intermediate progress, not only final outcomes.
4. Separate high-level reasoning from low-level execution.
5. Use controlled perturbations to expose whether behavior is robust or just scripted.

For our MVP, NVIDIA's stack is probably too heavy. But its pattern is exactly what we need: agent autonomy only becomes scientifically useful when the environment can reset, constrain, verify, and score behavior.

## Current Judgment

This direction is meaningful only if we avoid a vague "AI people in a city" demo.

A sharper contribution would be:

> A controllable benchmark and simulator for evaluating intention-driven urban generative agents under spatial constraints.

The first prototype should likely be small:

- 20-50 agents.
- 20-40 POIs.
- 3-5 controlled layouts.
- Rule-based path/time/capacity constraints.
- LLM only for high-level intention and explanation.
- Baselines: fixed schedule, utility-only policy, LLM schedule policy, LLM intention policy.
- Metrics: autonomy, spatial sensitivity, plan feasibility, consistency, social encounter network, token/cost.

If the LLM intention policy does not beat simpler baselines on adaptation, consistency, or interpretability, that is also a valuable negative result.
