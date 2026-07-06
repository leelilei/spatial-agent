# Reference Index

Downloaded / archived on 2026-06-22, 2026-06-23, and 2026-07-03.

Archive status on 2026-07-03: **45 verified unique references, 44 archived
PDF/fulltext/note packages, and 1 verified paper awaiting a retrievable PDF**.
The published GATSim journal article is counted as a version update, not a new paper.

This archive is for the `6-city` research direction: city-scale or micro-city
generative agents, SOTOPIA-style benchmark design, spatially grounded autonomy, and
verifiable evaluation.

## Reading Order

1. Start from `04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.pdf` for the
   benchmark pattern: scenario, private goals, interaction trace, evaluator.
2. Read `02_citysim_agents/01_CitySim_Wang2025.pdf` and
   `02_citysim_agents/02_GATSim_Liu2025.pdf` for closest city-agent simulation work.
3. Read `01_urban_benchmarks/01_CityBench_Feng2024.pdf`,
   `01_urban_benchmarks/04_USTBench_Liu2025.pdf`, and
   `01_urban_benchmarks/08_CityEQA_Zhang2025.pdf` to understand the benchmark
   landscape.
4. Read `03_embodied_city/01_EmbodiedCity_Zhou2024.pdf` if the benchmark moves from
   graph/grid space toward embodied navigation.
5. Read `05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.pdf` and
   `05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.pdf` for
   the macro mobility-realism boundary.
6. Read `06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.pdf`,
   `06_agent_execution_benchmarks/03_tau_bench_Yao2024.pdf`, and
   `06_agent_execution_benchmarks/04_AppWorld_Trivedi2024.pdf` for executable
   state-validation and infeasibility-evaluation patterns.

## 01 Urban Benchmarks

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/01_urban_benchmarks/01_CityBench_Feng2024.pdf` | CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks | [arXiv 2406.13945](https://arxiv.org/abs/2406.13945) | Broad urban-task benchmark; useful baseline for what current city benchmarks already cover. |
| `../pdf/01_urban_benchmarks/02_CityGPT_CityEval_Feng2024.pdf` | CityGPT: Empowering Urban Spatial Cognition of Large Language Models | [arXiv 2406.13948](https://arxiv.org/abs/2406.13948) | CityEval / urban spatial cognition framing; helps separate spatial knowledge from agent behavior. |
| `../pdf/01_urban_benchmarks/03_STBench_Wang2024.pdf` | STBench: Assessing the Ability of Large Language Models in Spatio-Temporal Analysis | [arXiv 2406.19065](https://arxiv.org/abs/2406.19065) | Spatiotemporal reasoning benchmark; relevant to city-agent scheduling and movement. |
| `../pdf/01_urban_benchmarks/04_USTBench_Liu2025.pdf` | USTBench: Benchmarking and Dissecting Spatiotemporal Reasoning of LLMs as Urban Agents | [arXiv 2505.17572](https://arxiv.org/abs/2505.17572) | Most directly adjacent benchmark for LLMs as urban agents; important comparison point. |
| `../pdf/01_urban_benchmarks/05_UrbanPlanBench_Luo2025.pdf` | UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large Language Models | [arXiv 2504.21027](https://arxiv.org/abs/2504.21027) | Urban-planning benchmark; useful contrast against daily-life / intention-driven agents. |
| `../pdf/01_urban_benchmarks/06_UPBench_Liu2026.pdf` | Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment | [arXiv 2606.11678](https://arxiv.org/abs/2606.11678) | Professional-judgment planning benchmark; useful for evaluation rubric design. |
| `../pdf/01_urban_benchmarks/07_UrBench_Liu2024.pdf` | UrBench: A Comprehensive Benchmark for Evaluating Large Multimodal Models in Multi-View Urban Scenarios | [arXiv 2408.17267](https://arxiv.org/abs/2408.17267) | Multimodal urban perception benchmark; adjacent if we add visual city observations. |
| `../pdf/01_urban_benchmarks/08_CityEQA_Zhang2025.pdf` | CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space | [arXiv 2502.12532](https://arxiv.org/abs/2502.12532) | Embodied city-space QA; strong reference for navigation + question answering evaluation. |
| `../pdf/01_urban_benchmarks/09_OpenCity_Ma2024.pdf` | OpenCity: A Scalable Platform to Simulate Urban Activities with Massive LLM Agents | [arXiv 2410.21286](https://arxiv.org/abs/2410.21286) | Large-scale urban activity simulation platform; important system-level comparison. |
| `../pdf/01_urban_benchmarks/10_MobileCity_Li2025.pdf` | MobileCity: An Efficient Framework for Large-Scale Urban Behavior Simulation | [arXiv 2504.16946](https://arxiv.org/abs/2504.16946) | Efficient large-scale behavior simulation; useful when thinking about scale beyond micro-city. |

## 02 CitySim Agents

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/02_citysim_agents/01_CitySim_Wang2025.pdf` | CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation | [arXiv 2506.21805](https://arxiv.org/abs/2506.21805) | Closest named CitySim reference; central comparison for agent autonomy and city dynamics. |
| `../pdf/02_citysim_agents/02_GATSim_Liu2025.pdf` | GATSim: Urban Mobility Simulation with Generative Agents | [arXiv 2506.23306](https://arxiv.org/abs/2506.23306); [journal DOI 10.1016/j.simpat.2025.103234](https://doi.org/10.1016/j.simpat.2025.103234) | Directly uses generative agents for urban mobility; the 2025 journal article is the published version of this archived work, not a separate reference. |
| `../pdf/02_citysim_agents/03_AgentSociety_Gao2025.pdf` | AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society | [arXiv 2502.08691](https://arxiv.org/abs/2502.08691) | Large-scale LLM society simulation; useful for population-level evaluation and realism claims. |
| `../pdf/02_citysim_agents/04_Concordia_Vezhnevets2023.pdf` | Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia | [arXiv 2312.03664](https://arxiv.org/abs/2312.03664) | Framework precedent for grounding actions in explicit spaces and game-master style control. |
| `../pdf/02_citysim_agents/05_ChatSUMO_Mao2024.pdf` | ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban Mobility | [arXiv 2409.09040](https://arxiv.org/abs/2409.09040) | Traffic / SUMO angle; useful if benchmark tasks include road-network mobility. |
| `../pdf/02_citysim_agents/06_UrbanLLM_Zhang2024.pdf` | UrbanLLM: Autonomous Urban Activity Planning and Management with Large Language Models | [arXiv 2406.12360](https://arxiv.org/abs/2406.12360) | Urban activity planning with LLMs; relevant to intention selection and daily schedules. |
| `../pdf/02_citysim_agents/07_TrajAgent_Zhang2024.pdf` | TrajAgent: An LLM-Agent Framework for Trajectory Modeling via Large-and-Small Model Collaboration | [arXiv 2410.20445](https://arxiv.org/abs/2410.20445) | Trajectory modeling reference; useful for movement behavior and trace evaluation. |
| `../pdf/02_citysim_agents/08_Urban_Generative_Intelligence_Li2023.pdf` | Urban Generative Intelligence (UGI): A Foundational Platform for Agents in Embodied City Environment | [arXiv 2312.11813](https://arxiv.org/abs/2312.11813) | Early embodied-city agent platform framing; bridges city sim and embodied environments. |

## 03 Embodied City

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/03_embodied_city/01_EmbodiedCity_Zhou2024.pdf` | EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-world City Environment | [arXiv 2410.09604](https://arxiv.org/abs/2410.09604) | Key reference for embodied city navigation and realistic observations. |
| `../pdf/03_embodied_city/02_UrbanLLaVA_Feng2025.pdf` | UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence with Spatial Reasoning and Understanding | [arXiv 2506.23219](https://arxiv.org/abs/2506.23219) | Urban multimodal/spatial reasoning reference; relevant if observations become visual. |

## 04 Social Benchmark Foundations

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/04_social_benchmark_foundations/01_Generative_Agents_Park2023.pdf` | Generative Agents: Interactive Simulacra of Human Behavior | [arXiv 2304.03442](https://arxiv.org/abs/2304.03442) | Foundation for memory, reflection, planning, and believable agent behavior. |
| `../pdf/04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.pdf` | SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents | [OpenReview](https://openreview.net/forum?id=mM7VurbA4r) | Benchmark design model: private goals, social situations, interaction traces, evaluator. |
| `../pdf/04_social_benchmark_foundations/03_AgentSense_2024.pdf` | AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios | [arXiv 2410.19346](https://arxiv.org/abs/2410.19346) | Social-agent benchmark neighbor; useful for private-goal and social-recovery evaluation. |
| `../pdf/04_social_benchmark_foundations/04_Lifelong_SOTOPIA_2025.pdf` | Lifelong-SOTOPIA: Evaluating Social Intelligence for Lifelong LLM Agents | [arXiv 2506.12666](https://arxiv.org/abs/2506.12666) | Longitudinal social memory benchmark; useful if CityAgency adds repeated social histories. |
| `../pdf/04_social_benchmark_foundations/05_Misleading_Success_2024.pdf` | Is this the real life? Is this just fantasy? The Misleading Success of Simulating Social Interactions With LLMs | [arXiv 2403.05020](https://arxiv.org/abs/2403.05020) | Cautionary reference on simulation realism and information conditions. |
| `../pdf/04_social_benchmark_foundations/06_Can_LLM_Agents_Simulate_Multi_Turn_Human_Behavior_2025.pdf` | Can LLM Agents Simulate Multi-Turn Human Behavior? | [arXiv 2503.20749](https://arxiv.org/abs/2503.20749) | Human-behavior simulation benchmark; useful for action-trace realism and behavioral prediction framing. |
| `../pdf/04_social_benchmark_foundations/07_LiveCultureBench_Pham2026.pdf` | LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations | [arXiv 2603.01952](https://arxiv.org/abs/2603.01952) | Closest newly identified competitor: graph-based town, resident daily goals, supporting agents, task completion, cultural norms, and verifier reliability. CityAgency must differentiate through deterministic physical execution evidence and continuous trace validation. |

## 05 Mobility Realism

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.pdf` | MobiSim-Bench: A Multi-Perspective Benchmark for Evaluating LLM-Agent-Based Human Mobility Simulation | [OpenReview](https://openreview.net/forum?id=3QFvAXuNl7) | Strongest mobility-simulation benchmark neighbor; evaluates robustness, realism, responsiveness, microscopic intentions, and macroscopic mobility statistics. |
| `../pdf/05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.pdf` | When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation | [arXiv 2606.13835](https://arxiv.org/abs/2606.13835) | Key motivation for the plausibility-vs-realism gap; CityAgency should position itself as micro-level diagnosis beneath this macro validation. |

## 06 Agent Execution Benchmarks

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/06_agent_execution_benchmarks/01_ChinaTravel_Shao2024.pdf` | ChinaTravel: An Open-Ended Travel Planning Benchmark for Language Agents in Chinese Travel | [arXiv 2412.13682](https://arxiv.org/abs/2412.13682) | Multi-day, multi-POI planning with feasibility and constraint validation; close neighbor for plausible plans under constraints. |
| `../pdf/06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.pdf` | Do Agents Know What They Can't Do? Evaluating Feasibility Awareness of Language Agents Under Environment Constraints | [arXiv 2605.28532](https://arxiv.org/abs/2605.28532) | Feasibility-awareness benchmark; useful for false-continue and infeasible-task metrics. |
| `../pdf/06_agent_execution_benchmarks/03_tau_bench_Yao2024.pdf` | tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | [arXiv 2406.12045](https://arxiv.org/abs/2406.12045) | Strong reference for dynamic user interaction, domain rules, repeat trials, and state-based evaluation. |
| `../pdf/06_agent_execution_benchmarks/04_AppWorld_Trivedi2024.pdf` | AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents | [arXiv 2407.18901](https://arxiv.org/abs/2407.18901) | Executable app-world benchmark with programmatic state validation and collateral-damage checks. |
| `../pdf/06_agent_execution_benchmarks/05_WebArena_Zhou2023.pdf` | WebArena: A Realistic Web Environment for Building Autonomous Agents | [arXiv 2307.13854](https://arxiv.org/abs/2307.13854) | Reproducible web environment and functional task correctness; useful evaluation design precedent. |
| `../pdf/06_agent_execution_benchmarks/06_TheAgentCompany_Xu2024.pdf` | TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks | [arXiv 2412.14161](https://arxiv.org/abs/2412.14161) | Long-horizon workplace-agent benchmark; useful comparison for consequential, stateful agent evaluation. |
| `../pdf/06_agent_execution_benchmarks/07_STT_Arena_2026.pdf` | STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics | [arXiv 2605.18548](https://arxiv.org/abs/2605.18548) | *Archived 2026-07-04.* 227 executable tasks, 9 spatio-temporal conflict types, 4 solvability levels; injected triggers abruptly invalidate an ongoing plan, forcing detect→revise→verify. Frontier models (incl. Claude-4.6-Opus) score <40%. Failure modes: Stale-State Execution, Misdiagnosis of Dynamic Triggers, **Missing Post-Adaptation Verification**. **Closest neighbor to CityAgency's disruption→replanning→verification spine, but tool-use (no urban movement / private-resident goals / social layer) and not city-grounded.** Confirms the axis is hot; does not occupy the city-resident + evidence-contract cell. |

Local extracted text / metadata copied from `3-SMGA`:

- `../fulltext/04_social_benchmark_foundations/01_Generative_Agents_Park2023.fulltext.md`
- `../fulltext/04_social_benchmark_foundations/01_Generative_Agents_Park2023.meta.json`
- `../fulltext/04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.fulltext.md`
- `../fulltext/04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.meta.json`

## Related Project Links Not Archived as PDFs

- AI Town: [a16z-infra/ai-town](https://github.com/a16z-infra/ai-town)
- Concordia code: [google-deepmind/concordia](https://github.com/google-deepmind/concordia)
- GATSim code: [qiliuchn/gatsim](https://github.com/qiliuchn/gatsim)
- CityEQA code: [tsinghua-fib-lab/cityeqa](https://github.com/tsinghua-fib-lab/cityeqa)
- EmbodiedCity code: [tsinghua-fib-lab/EmbodiedCity](https://github.com/tsinghua-fib-lab/EmbodiedCity)
- UrbanLLaVA code: [tsinghua-fib-lab/UrbanLLaVA](https://github.com/tsinghua-fib-lab/UrbanLLaVA)
- NVIDIA Isaac Sim: [developer.nvidia.com/isaac/sim](https://developer.nvidia.com/isaac/sim)
- NVIDIA Isaac Lab: [developer.nvidia.com/isaac/lab](https://developer.nvidia.com/isaac/lab)
- NVIDIA Cosmos: [nvidia.com/en-us/ai/cosmos](https://www.nvidia.com/en-us/ai/cosmos/)
- NVIDIA ENPIRE: [research.nvidia.com/labs/gear/enpire](https://research.nvidia.com/labs/gear/enpire/)

## 07 Large-Scale Urban Simulation & Scaling

*Identified on 2026-07-01; archived and reviewed on 2026-07-03.*

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/02_citysim_agents/09_GenWorld_2026.pdf` | GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies | [arXiv 2606.27650](https://arxiv.org/abs/2606.27650) | 196K synthetic residents on real Higashi-Hiroshima census + geographic data; LLM decisions compiled offline to lookup policies; city-wide weekday rollout + perturbation response with auditable replanning. Latest large-scale empirically grounded urban sim. CityAgency should compare: GenWorld tests aggregate mobility patterns, CityAgency tests individual private-goal trace feasibility. |
| `../pdf/02_citysim_agents/10_Limits_of_Agency_2024.pdf` | On the Limits of Agency in Agent-Based Models | [arXiv 2409.10568](https://arxiv.org/abs/2409.10568) (AAMAS 2025) | Introduces LLM archetypes: group population by demographics, one LLM call per archetype, sample behavior for all agents in group. 8.4M-agent NYC COVID-19 simulation via AgentTorch. Formalizes the agency-vs-scale trade-off — agents' expressiveness and population size are fundamentally in tension. CityAgency occupies the high-agency, micro-scale end of this continuum. |

## 08 Route-Planning & Mobility Agents

*Identified on 2026-07-01; archived and reviewed on 2026-07-03.*

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| `../pdf/05_mobility_realism/03_MobilityBench_2026.pdf` | MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios | [arXiv 2602.22638](https://arxiv.org/abs/2602.22638) | 100K real user route queries × 350+ cities; deterministic API-replay sandbox. Core finding: preference-constrained route planning (e.g. "avoid highways, stop by a convenience store en route") is the weak spot for all LLM agents. Closest neighbor to CityAgency's movement validation. Key difference: MobilityBench tests single route-planning requests; CityAgency tests a full multi-step episode with private intentions. |
| `../pdf/05_mobility_realism/04_DeliveryBench_2025.pdf` | DeliveryBench: Can Agents Earn Profit in Real World? | [arXiv 2512.19234](https://arxiv.org/abs/2512.19234) | Food-delivery agent benchmark: real city maps, order acceptance, route planning, time-window constraints, profitability. Adds "profit feasibility" as a constraint dimension relevant to CityAgency's budget/economic constraints. |
| `../pdf/05_mobility_realism/05_TrajGenAgent_2026.pdf` | TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation | [arXiv 2606.12657](https://arxiv.org/abs/2606.12657) | Hierarchical LLM agent generates human mobility trajectories. Represents current technical ceiling for LLM-driven trajectory generation. Fits in 05_mobility_realism family alongside MobiSim-Bench and When Plausible Is Not Realistic. |
| `../pdf/05_mobility_realism/06_AgentMob_2026.pdf` | Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent (AgentMob) | [arXiv 2606.05130](https://arxiv.org/abs/2606.05130) | Evidence-grounded individual mobility prediction with LLM agent. Adds "evidence grounding" dimension to mobility agent evaluation — agent must cite real-world POI/transport data when predicting movement. Relevant to CityAgency's action-evidence protocol. |
| `../pdf/06_agent_execution_benchmarks/08_TripPlus_2026.pdf` | Trip+: Benchmarking Agents in Personalized Interactive Travel Planning | [arXiv 2606.21169](https://arxiv.org/abs/2606.21169) | *Archived 2026-07-04.* Minute-level itinerary generation and revision under evolving preferences and environment-driven disruptions; 18 LMs; finds models favor technically-feasible-but-exhausting itineraries far from profiled preferences. Overlaps CityAgency's feasibility + replanning + preference axes, **but scores plan-level experience via an LLM simulator (subjective metrics like fatigue) — the exact LLM-judge-as-verifier stance CityAgency's environment-owned evidence contract rejects.** A contrast, not an occupant of the cell. |

## 09 Validation, Surveys & Adjacent Urban Applications

*Expanded and reviewed on 2026-07-03.*

| Local archive | Paper | Source | Why keep it |
|---|---|---|---|
| *(paywalled — no arxiv PDF)* | Generative Agents in Agent-Based Modeling: Overview, Validation, and Emerging Challenges | [IEEE TAI 2025](https://ieeexplore.ieee.org/document/10985773) | Comprehensive survey of generative agents in ABMs, with specific focus on validation frameworks and urban science applications. Useful for establishing the GA-for-urban-simulation landscape in related work. |
| *(paywalled — no arxiv PDF)* | Generative Agents for Urban Mobility: A Cognitive Framework for Realistic Travel Behavior Simulation | [ScienceDirect S1569190X25001698](https://www.sciencedirect.com/science/article/abs/pii/S1569190X25001698) | Cognitive architecture for LLM-based urban mobility agents. Bridges cognitive science and travel behavior modeling. Adjacent to GATSim and the CityAgency cognitive baselines. |
| *(paywalled — no arxiv PDF)* | Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning | [SAGE ATDE 2025](https://journals.sagepub.com/doi/full/10.3233/ATDE251076) | LLM-based generative agents for multi-party urban planning deliberation. Adjacent to CityAgency's social-recovery and co-presence scenarios; useful for future multi-stakeholder track. |

## Updated Reading Order (2026-07-01)

For the expanded set:

7. Read `04_social_benchmark_foundations/07_LiveCultureBench_Pham2026.pdf` first because it is the closest small-city goal-and-social-context competitor.
8. Read `08_route_planning_agents/01_MobilityBench_Song2026.pdf` and `08_route_planning_agents/02_DeliveryBench_Mao2025.pdf` for deterministic route replay and long-horizon constraint execution.
9. Read `07_large_scale_urban_sim/01_GenWorld_Li2026.pdf` and `07_large_scale_urban_sim/02_Limits_of_Agency_Chopra2025.pdf` for the agency-versus-scale boundary.
10. Read `09_surveys/03_Validation_Central_Larooij2026.pdf` and `09_surveys/04_Mechanism_Plausibility_Zhao2026.pdf` before making urban-science claims.

## Current Gap Hypothesis (Updated 2026-07-03)

The previous gap statement was too broad. LiveCultureBench already combines a small-city
location graph, resident daily goals, supporting agents, task completion, cultural norms, and
an uncertainty-aware LLM verifier. DeliveryBench already tests long-horizon urban execution
under dense temporal, economic, physical, and social constraints. MobilityBench already
provides deterministic replay for route-agent tools.

The remaining defensible opportunity is narrower: a framework-comparative benchmark in
which the environment owns physical truth and emits typed evidence for every state transition,
allowing researchers to measure the gap between a plausible plan or completion claim and a
continuous executable trace. CityAgency should claim agent-level execution-mechanism
validation, not human realism or macro-level urban validity without additional empirical evidence.

### 2026-07-04 neighbor check (first-hand arxiv)

Three fresh 2026 concurrent works were checked against the exact CityAgency cell; each shares
one axis but none occupies the cell (private urban resident + hidden intentions + movement/feasibility
+ deterministic environment-owned outcome evidence + graded replanning + social co-presence):

- **STT-Arena (2605.18548)** — owns disruption→replan→verify, but tool-use, not city-grounded.
- **GenWorld (2606.27650)** — owns grounded controllable urban sim, but population-scale aggregate, not individual evidence contract.
- **Trip+ (2606.21169)** — owns feasibility+preference+replanning travel planning, but uses LLM-simulator scoring, the stance CityAgency rejects.

Conclusion: the region is hot (evidence the problem is recognized), but the exact combination cell
remains open. See `docs/project/direction_verdict_2026-07-04.md`.


