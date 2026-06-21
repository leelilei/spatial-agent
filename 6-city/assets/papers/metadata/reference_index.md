# Reference Index

Downloaded / archived on 2026-06-22.

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
| `../pdf/02_citysim_agents/02_GATSim_Liu2025.pdf` | GATSim: Urban Mobility Simulation with Generative Agents | [arXiv 2506.23306](https://arxiv.org/abs/2506.23306) | Directly uses generative agents for urban mobility; close to our city-agent benchmark idea. |
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

## Current Gap Hypothesis

Most existing urban benchmarks evaluate urban knowledge, spatiotemporal reasoning,
planning judgment, multimodal perception, or navigation / QA. The open opportunity is
a controlled SOTOPIA-style benchmark for intention-driven city agents: private goals,
spatial constraints, social relations, environmental perturbations, and verifiable
trajectory-level scoring.


