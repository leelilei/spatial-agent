# Urban Benchmark Literature Scan

Date: 2026-06-22

Question:

> If we build a SOTOPIA-style benchmark for spatially grounded city agents, what existing urban benchmarks already exist, and where is the gap?

## Quick Take

There is already a strong cluster of urban LLM benchmarks. Most of them evaluate one of five things:

1. Urban world-model capability.
2. Urban spatial / spatiotemporal reasoning.
3. Urban planning professional knowledge.
4. Multimodal urban scene understanding.
5. Embodied city navigation / question answering.

The gap is narrower:

> Few benchmarks directly evaluate intention-driven, daily-life urban agents under controlled spatial layouts, private goals, social relationships, and resettable environment perturbations.

That gap still looks meaningful.

## Related Benchmarks

| Benchmark / paper | Year | What it evaluates | Environment / data | Evaluation style | Relation to our idea |
|---|---:|---|---|---|---|
| [CityBench](https://arxiv.org/html/2406.13945) / [GitHub](https://github.com/tsinghua-fib-lab/CityBench) | 2024 | LLMs as city-scale world models | CitySim integrates OSM, street/satellite imagery, human activity data; 13 cities | 7-8 urban tasks: geospatial understanding and decision-making | Closest "general urban benchmark"; but not focused on free daily-life agency or controlled layout causality |
| [CityGPT / CityEval](https://arxiv.org/abs/2406.13948) / [GitHub](https://github.com/tsinghua-fib-lab/CityGPT) | 2024 | Urban spatial cognition after instruction tuning | CityInstruction + CityEval | Tests urban tasks and enhanced urban LLMs | Useful for task taxonomy and urban knowledge injection; less about interactive resident behavior |
| [STBench](https://arxiv.org/abs/2406.19065) / [GitHub](https://github.com/LwbXc/STBench) | 2024 | Spatio-temporal analysis ability | 60k+ QA pairs across spatio-temporal tasks | Knowledge, reasoning, computation, downstream applications | Important for spatiotemporal reasoning; mostly QA/analysis rather than embodied action |
| [USTBench](https://arxiv.org/abs/2505.17572) / [GitHub](https://github.com/usail-hkust/USTBench) | 2025 | Spatiotemporal reasoning of LLMs as urban agents | UAgentEnv interactive city environment | Understanding, forecasting, planning, reflection with feedback; 62,466 QA pairs | Very relevant. It decomposes process-level urban reasoning, but does not cover broader social daily-life agency |
| [UrbanPlanBench](https://arxiv.org/abs/2504.21027) / [PlanBench GitHub](https://github.com/tsinghua-fib-lab/PlanBench) | 2025 | Professional urban planning knowledge | Planning exams/textbooks, UrbanPlanText SFT dataset | Principles, professional knowledge, management/regulation | Strong planning-domain benchmark; not about resident movement or spatial behavior |
| [UPBench](https://arxiv.org/html/2606.11678) | 2026 | Planning professional judgment | 4 knowledge pillars x 5 Bloom-style cognitive levels | Automated scoring + expert panel assessment; 25 LLMs | Useful idea: expert-judgment matrix and diagnostics. Not an agent/world benchmark |
| [UrBench](https://arxiv.org/abs/2408.17267) / [project](https://opendatalab.github.io/UrBench/) | 2024 | Multimodal urban scene understanding | Multi-view urban images from 11 cities; 11.6k questions | Geo-localization, scene reasoning, scene understanding, object understanding | Useful if we later add vision or street-view perception; not a social/mobility benchmark |
| [UrbanLLaVA](https://arxiv.org/html/2506.23219) / [GitHub](https://github.com/tsinghua-fib-lab/UrbanLLaVA) | 2025 | Multimodal urban intelligence model | Urban instruction data across multiple urban modalities | Enhanced urban task benchmark | Model/dataset paper; useful for multimodal extension, not core MVP |
| [EmbodiedCity](https://arxiv.org/abs/2410.09604) / [GitHub](https://github.com/tsinghua-fib-lab/EmbodiedCity) | 2024 | Embodied agents in real-world city environments | Realistic 3D city with buildings, roads, pedestrian/vehicle flows | EmbodiedAI tasks covering perception, planning, acting | Important "strong embodied city" reference; heavier than our first benchmark |
| [CityEQA](https://arxiv.org/html/2502.12532) / [GitHub](https://github.com/tsinghua-fib-lab/cityeqa) | 2025 | Embodied question answering in city space | 3D urban simulator, 1,412 human-annotated tasks | Open-vocabulary EQA, exploration/navigation efficiency, PMA agent | Good reference for hierarchical city agents and cognitive maps; goal-directed QA, not open daily behavior |
| [OpenCity](https://arxiv.org/abs/2410.21286) / [GitHub](https://github.com/tsinghua-fib-lab/OpenCity) | 2024 | Large-scale urban activity simulation with LLM agents | Six global cities; massive LLM agents | Compares simulated activity against real-world data; radius of gyration, OD matrix, segregation index | Useful for macro activity metrics and efficiency; less controlled at micro agency level |
| [MobileCity](https://arxiv.org/html/2504.16946) | 2025/2026 | Efficient large-scale urban behavior simulation | LLM-powered urban mobility/social behavior simulation | Large-scale mobility and social behavior realism | Relevant for scalable simulation; still not a SOTOPIA-style controlled agency benchmark |

## The Benchmark Landscape

### 1. City World-Model Benchmarks

CityBench and CityGPT/CityEval ask whether LLMs can understand and solve urban tasks. They cover multiple cities and modalities, and CityBench explicitly uses an interactive simulator.

What they do well:

- integrate urban data at city scale
- cover geospatial understanding and decision-making
- compare models across cities and tasks

What they do not isolate:

- whether agents have stable private intentions
- how social relationships affect movement
- how controlled layout perturbations change behavior
- whether the same agent responds consistently over repeated episodes

### 2. Spatiotemporal Reasoning Benchmarks

STBench and USTBench are important because they decompose reasoning instead of only reporting final task outcomes.

What we should borrow:

- process-level decomposition
- planning vs forecasting vs reflection distinction
- feedback-based evaluation
- structured QA pairs for diagnostic tests

What we should add:

- long-running action loop
- private goals and social consequences
- environment-owned feasibility checks
- repeated randomized city layouts

### 3. Planning Knowledge Benchmarks

UrbanPlanBench and UPBench evaluate whether LLMs can reason like planners. They are useful for professional urban planning, but they evaluate expert cognition rather than resident behavior.

What we should borrow:

- domain-specific scoring matrix
- expert/human scoring for open-ended professional judgment
- failure diagnostics, e.g. regulatory hallucination and context-insensitive reasoning

What we should avoid:

- becoming a planning-exam benchmark
- over-relying on textual professional knowledge

### 4. Multimodal / Embodied City Benchmarks

UrBench, UrbanLLaVA, EmbodiedCity, and CityEQA move toward perception and embodied action.

What they do well:

- evaluate visual/geospatial scene understanding
- expose cross-view inconsistency
- introduce active exploration in city space
- build realistic 3D city environments

What they do not center:

- daily-life intentions
- relationship-aware mobility
- controlled urban morphology effects
- micro-to-macro social behavior under spatial layouts

### 5. Large-Scale Urban Activity Simulation

OpenCity and MobileCity are closest to "agents living in cities" at scale.

What they do well:

- large populations
- cost/throughput optimization
- macro mobility/activity validation

What they leave open:

- transparent decision trace at each action
- benchmark items with hidden private goals
- repeated resettable scenarios
- controlled causal comparison of layouts

## Our Possible Niche

The strongest niche is not:

> another urban QA benchmark, another 3D city EQA benchmark, or another large-scale activity simulator.

The niche is:

> a SOTOPIA-style interactive benchmark for intention-driven urban agents, where the environment is spatially constrained, resettable, and scored with both automatic and social dimensions.

## Proposed Positioning

Working title:

**CityIntent: Evaluating Intention-Driven Agents in Verifiable Urban Spaces**

Positioning sentence:

> Existing urban LLM benchmarks evaluate city knowledge, spatiotemporal reasoning, planning expertise, multimodal perception, or aggregate urban activity realism. CityIntent instead evaluates whether generative agents with private intentions can produce feasible, consistent, and spatially sensitive behavior in controlled urban environments.

## Key Differentiators

1. **Private intentions**

   Like SOTOPIA, each agent has hidden goals. Unlike CityBench/USTBench, goals are embedded in daily-life action and social context.

2. **Controlled urban morphology**

   Same agents and POIs, different layouts. This lets us test causal effects of centrality, bottlenecks, mixed-use clustering, and public-space placement.

3. **Environment-owned feasibility**

   The simulator validates travel time, opening hours, capacity, co-presence, and budget. The LLM cannot hallucinate completion.

4. **Decision traces**

   Each action stores candidates, retrieved memories, internal needs, environmental constraints, selected action, and outcome.

5. **Mixed scoring**

   Automatic metrics score feasibility, travel time, encounters, invalid actions, and goal state. LLM/human judges only score soft dimensions such as believability and relationship quality.

## First Reading Priority

1. CityBench: understand urban task taxonomy and simulator interface.
2. USTBench: copy process-level decomposition for reasoning.
3. SOTOPIA: copy scenario/private-goal/eval design.
4. EmbodiedCity and CityEQA: understand where strong embodied city work begins, but do not copy for MVP.
5. OpenCity/MobileCity: borrow macro activity metrics and efficiency ideas.

## Immediate Design Implication

First benchmark version should probably not be "fully embodied 3D city" and not "real global cities."

It should be:

- graph-based city
- generated controlled layouts
- 20-50 agents
- 20-40 POIs
- hidden private goals
- 2-8 hour episodes
- automatic feasibility scorer
- optional LLM judge for explanation quality

This gives us a crisp benchmark before building a large simulator.

