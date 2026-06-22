# CityAgency Related-Work Broad Scan

Date: 2026-06-22

Question:

> Has "Plausible Plans, Impossible Traces: a benchmark for urban agent agency"
> already been done, and which nearby papers most threaten the novelty claim?

Raw metadata pass:

- `paper-search-raw-2026-06-22.md`

## Short Answer

I did not find an exact replacement for CityAgency.

The closest existing work clusters are:

1. **LLM urban mobility simulation realism**: already strong, and directly
   overlaps with "plausible is not realistic".
2. **LLM city / urban benchmarks**: strong on urban reasoning, world models, and
   embodied city QA, but less focused on private-goal action traces.
3. **Social-agent benchmarks**: strong on private goals and interaction, but
   mostly non-spatial.
4. **General agent execution benchmarks**: strong on state validation,
   feasibility, and tool/user interaction, but not urban.

The CityAgency opening is narrower and sharper:

> A micro-level urban agency benchmark that measures whether plausible plans
> become executable city traces under spatial, temporal, budget, POI, disruption,
> and social-interruption constraints.

## Search Groups

Queries used:

- `LLM urban agent benchmark agency`
- `LLM urban simulation mobility realism benchmark`
- `LLM agent trace feasibility benchmark planning`
- `social agent benchmark private goals LLM`
- `embodied agent benchmark planning constraints LLM`
- `plausibility feasibility LLM agents benchmark planning`
- `environment validates LLM agents benchmark`
- specific known neighbors: `MobiSim-Bench`, `CitySim`, `GATSim`, `USTBench`,
  `SOTOPIA`, `AgentSense`, `tau-bench`, `AppWorld`, `ChinaTravel`, `FeasiGen`

Sources used:

- Web search
- arXiv
- OpenReview
- GitHub / project pages
- existing archived `6-city` paper notes
- `0-Tools/research-standard/paper_search.py` first-pass metadata search

## Strongest Novelty Threats

| Paper / benchmark | Relevance | What it already does | Why it does not replace CityAgency |
|---|---|---|---|
| [MobiSim-Bench](https://openreview.net/forum?id=3QFvAXuNl7) | direct-adjacent | Multi-perspective benchmark for LLM-agent-based human mobility simulation; evaluates robustness, realism, and responsiveness with Daily Mobility and Hurricane Mobility scenarios. | Strongest mobility benchmark neighbor, but the focus is mobility simulation performance, not micro-scenario agency with private goals, social interruption recovery, and deterministic action-trace failure taxonomy. |
| [When Plausible Is Not Realistic](https://arxiv.org/abs/2606.13835) | direct-adjacent | Evaluates whether LLM urban simulators reproduce empirical mobility patterns such as trip length, OD flow, dwell time, temporal rhythms, semantic transitions, and mobility profiles. | Very close to our paper story, but macro validation oriented. CityAgency should cite it as motivation and then move one level down to micro-mechanism diagnosis. |
| [ChinaTravel](https://openreview.net/forum?id=0YRVlxY9BH) | adjacent-strong | Open-ended multi-day, multi-POI travel planning benchmark with DSL-based feasibility, constraint satisfaction, preference comparison, and implicit intent. | Very relevant to constraint validation and "plausible plans", but it is travel itinerary planning rather than city-agent episodes with environment-owned state, social interruptions, and execution traces over time. |
| [Do Agents Know What They Can't Do? / FeasiGen](https://arxiv.org/html/2605.28532v1) | adjacent-strong | Constructs infeasible tool-using tasks and evaluates whether agents detect infeasibility instead of continuing execution. | Gives us a useful feasibility-awareness framing, but it is tool/API dependency focused, not urban spatial-temporal agency. |
| [USTBench](https://arxiv.org/html/2505.17572v1) | adjacent | Benchmarks and dissects spatiotemporal reasoning of LLMs as urban agents. | Strong urban-reasoning benchmark, but still closer to QA/process reasoning than free-running private-goal action traces. |
| [CityBench](https://arxiv.org/html/2406.13945v1) | adjacent | Evaluates LLM/VLM capability as city-scale world models over geospatial understanding and decision-making tasks across cities. | Broad urban benchmark, but not focused on daily-life agency, hidden intentions, social recovery, or impossible trace taxonomy. |
| [SOTOPIA](https://arxiv.org/abs/2310.11667) / [AgentSense](https://arxiv.org/html/2410.19346v1) | adjacent-foundation | Interactive private-goal social intelligence benchmarks. | Strong foundation for private goals and social evaluation, but not urban/spatial/temporal feasibility. |
| [tau-bench](https://arxiv.org/abs/2406.12045) / [AppWorld](https://appworld.dev/) | adjacent-method | Interactive agent benchmarks with state/database validation, domain rules, APIs, and end-state checking. | Good evaluation-pattern references. They validate digital-world action outcomes, not city mobility/activity agency. |

## Cluster A: Urban Mobility Realism And City Simulation

These papers are the closest to the citysim side.

| Work | What to cite it for | CityAgency boundary |
|---|---|---|
| [CitySim](https://arxiv.org/html/2506.21805v1) | Large-scale LLM-driven urban behavior and city-dynamics simulation. | We are not building a larger city simulator; we are building a diagnostic benchmark for agent policies. |
| [GATSim](https://arxiv.org/html/2506.23306v2) | Generative-agent transport / mobility simulation with memory, preferences, and adaptive travel behavior. | GATSim is a simulator/framework neighbor; CityAgency should test whether such agents maintain feasible micro-level agency under controlled stressors. |
| [MobiSim-Bench](https://openreview.net/forum?id=3QFvAXuNl7) | Benchmarking mobility simulation via robustness, realism, and responsiveness. | This is the most important new related work to add to the proposal. |
| [When Plausible Is Not Realistic](https://arxiv.org/abs/2606.13835) | Macro evidence that narrative plausibility and empirical mobility realism diverge. | CityAgency should become a micro-diagnostic companion to this macro critique. |
| OpenCity / MobileCity / AgentSociety | Large-scale city and society simulation with LLM agents. | Useful as systems to evaluate later; not a replacement for controlled micro-scenario benchmark. |

Takeaway:

> The macro mobility-realism space is already occupied. CityAgency should not
> claim to be the first LLM mobility realism benchmark. It should claim to
> diagnose micro-level failures that can explain macro mobility-realism gaps.

## Cluster B: Urban LLM Benchmarks And Embodied City Agents

These papers are strong urban benchmark neighbors.

| Work | What it tests | CityAgency boundary |
|---|---|---|
| [CityBench](https://arxiv.org/html/2406.13945v1) | LLM/VLM city-scale world-model abilities and urban decision tasks. | Broad urban capability benchmark; weak on private-goal trace execution. |
| [USTBench](https://arxiv.org/html/2505.17572v1) | Urban spatiotemporal reasoning, forecasting, planning, and reflection. | Process-level reasoning benchmark; not a daily-life agency trace benchmark. |
| [EmbodiedCity](https://arxiv.org/abs/2410.09604) | Embodied AI in realistic 3D city environments with perception, planning, acting tasks. | Much heavier environment; stronger on embodied perception than agency mechanisms. |
| [CityEQA](https://arxiv.org/abs/2502.12532) | Open-vocabulary embodied question answering in dynamic city space with hierarchical PMA agent. | Goal-directed exploration/QA, not open daily activity with private intentions and social interruption. |

Takeaway:

> CityAgency should cite these as the urban benchmark landscape, then emphasize
> that it evaluates executable micro-agency rather than urban knowledge,
> perception, or QA.

## Cluster C: Social And Human-Behavior Agent Benchmarks

These papers provide the social/private-goal backbone.

| Work | What it tests | CityAgency boundary |
|---|---|---|
| [SOTOPIA](https://arxiv.org/abs/2310.11667) | Private-goal social interaction and social intelligence. | No map, POI, route, budget, opening-hours, or city trace validator. |
| [Lifelong-SOTOPIA](https://arxiv.org/html/2506.12666v1) | Longitudinal social intelligence and memory across interactions. | Useful for memory/social history; still not urban execution. |
| [AgentSense](https://arxiv.org/html/2410.19346v1) | Social intelligence through diverse interactive scenarios. | Strong social benchmark; not spatially grounded. |
| [Misleading Success](https://arxiv.org/html/2403.05020v4) | Shows social simulations can look successful under unrealistic information conditions. | Very relevant to the "plausible but not executable/realistic" critique. |
| [Can LLM Agents Simulate Multi-Turn Human Behavior?](https://arxiv.org/html/2503.20749v7) | Human behavior simulation from real online customer behavior data. | Useful for human-behavior realism and action prediction; not city-space agency. |

Takeaway:

> CityAgency can borrow private goals and interaction structure from social
> benchmarks, but its contribution is to put those goals inside a city world that
> owns the feasibility truth.

## Cluster D: General Agent Execution, Feasibility, And State Validation

These papers are methodologically important for evaluation design.

| Work | What to borrow | CityAgency boundary |
|---|---|---|
| [tau-bench](https://arxiv.org/abs/2406.12045) | Dynamic user interaction, domain rules, database end-state evaluation, reliability over repeated trials. | Digital service tasks, not city-world action. |
| [AppWorld](https://appworld.dev/) | High-fidelity executable app world, API state validation, programmatic tests. | Digital apps rather than physical/social city constraints. |
| [WebArena](https://arxiv.org/abs/2307.13854) | Realistic reproducible web environment and functional task correctness. | Web navigation; useful for environment-evaluation rigor. |
| [TheAgentCompany](https://arxiv.org/abs/2412.14161) | Consequential long-horizon workplace tasks in a simulated organization. | Workplace agents, not urban residents. |
| [FeasiGen](https://arxiv.org/html/2605.28532v1) | Feasibility awareness, infeasible tasks, false-continue rate. | Tool feasibility rather than spatial-temporal feasibility. |
| [ChinaTravel](https://openreview.net/forum?id=0YRVlxY9BH) | Multi-POI constraint validation, implicit intent, neuro-symbolic planning. | Travel itinerary planning rather than stateful urban-agent episodes. |

Takeaway:

> The strongest methodology lesson is that CityAgency needs executable state
> validation, repeated-trial reliability, and explicit infeasibility/failure
> categories. These are not optional details; they are the core AAAI-style
> benchmark contribution.

## What This Means For The CityAgency Story

The current title still works:

> **Plausible Plans, Impossible Traces: CityAgency as a Benchmark for Urban Agent
> Agency**

But the related-work section must be careful:

1. Do not claim "first benchmark for LLM city agents".
2. Do not claim "first mobility-realism benchmark".
3. Do not claim "first feasibility benchmark for agents".
4. Claim the missing middle:

> Existing work evaluates urban knowledge, embodied city perception, macro
> mobility realism, social interaction, or executable digital-world agents.
> CityAgency evaluates the micro-level urban agency gap between plausible plans
> and executable traces.

## Recommended Proposal Updates

Add these papers explicitly:

- MobiSim-Bench
- When Plausible Is Not Realistic
- FeasiGen / Do Agents Know What They Can't Do?
- ChinaTravel
- tau-bench / AppWorld as evaluation-pattern references

Add these metric ideas:

- false-continue under infeasible city constraints
- repeated-trial reliability, analogous to `pass^k`
- plan plausibility vs trace feasibility gap
- impossible trace taxonomy by failure category
- architecture-level comparison, not only model leaderboard

## Reading / Archiving Priority

P0:

1. MobiSim-Bench
2. When Plausible Is Not Realistic
3. CitySim
4. USTBench
5. FeasiGen
6. ChinaTravel
7. tau-bench
8. AppWorld
9. SOTOPIA
10. AgentSense

P1:

1. GATSim
2. EmbodiedCity
3. CityEQA
4. TheAgentCompany
5. WebArena
6. Lifelong-SOTOPIA
7. Misleading Success
8. Can LLM Agents Simulate Multi-Turn Human Behavior?

## Bottom Line

The search makes CityAgency more constrained, but not weaker.

The strongest competitive pressure is from **MobiSim-Bench** and **When
Plausible Is Not Realistic**. They already cover macro mobility simulation
evaluation. That means CityAgency should avoid a broad mobility-realism claim.

The strongest support comes from **FeasiGen**, **tau-bench**, **AppWorld**, and
**ChinaTravel**. They show that modern agent benchmarks are moving toward
environment-owned validation and infeasibility detection. CityAgency can bring
that evaluation discipline into urban agency.

The clean contribution remains:

> CityAgency is a benchmark for measuring when plausible urban plans fail to
> become executable city traces.

