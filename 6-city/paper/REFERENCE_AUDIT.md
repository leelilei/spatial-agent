# Reference Audit

Last verified: 2026-08-06

## Summary

- Total unique BibTeX records: **48**
- Verified against arXiv API metadata: **41**
- Verified against Crossref DOI metadata: **5**
- Verified against ICLR/OpenReview plus the archived first page: **1** (SOTOPIA)
- Check suggested: **2**
- Index titles without a metadata match: **0**

## Critical Correction

The old reference index described DOI `10.1016/j.simpat.2025.103234` as the published version of GATSim. Crossref and OpenAlex identify that DOI as *Generative agents for urban mobility: A cognitive framework for realistic travel behavior simulation* by Qi Liu, Can Li, and Wanjing Ma. The bibliography therefore keeps GATSim and this journal article as distinct works.

## Check Suggested

| Key | Issue | Required action |
|---|---|---|
| `anonymous2026mobisimbench` | The archived ICLR 2026 submission is double-blind and lists anonymous authors. | Replace the author field when OpenReview exposes the final author list; do not use this entry in a camera-ready manuscript before then. |
| `liu2026generativeagentsurban` | Crossref assigns the volume/issue to 2026, while the DOI was registered in 2025 and OpenAlex labels the work 2025. | Keep 2026 for the issue citation; recheck the publisher export at submission time if the target style uses online-first year. |

## Scope Notes

- arXiv entries use the first-submission year and current arXiv title/author order. Venue claims embedded in free-text comments were not promoted to publication fields without a DOI or first-party proceedings record.
- Crossref entries use registered title, author order, publication container, volume/issue/pages when supplied by the publisher.
- SOTOPIA uses its ICLR 2024 record and archived paper author order; its arXiv identifier is included for retrieval.
- The archived PDF was used to repair an arXiv Atom author-splitting error for `lu2025canllmagents` and a capitalization typo for ChatSUMO.
- The bibliography includes the two validation papers omitted from the older index table: *Validation is the central challenge...* and the FAccT 2026 paper *Mechanism Plausibility in Generative Agent-Based Modeling*.

## Record Inventory

| Key | Year | Verification source | Title |
|---|---:|---|---|
| `park2023generativeagents` | 2023 | arXiv API | Generative Agents: Interactive Simulacra of Human Behavior |
| `vezhnevets2023generativeagentbased` | 2023 | arXiv API | Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia |
| `xu2023urbangenerativeintelligence` | 2023 | arXiv API | Urban Generative Intelligence (UGI): A Foundational Platform for Agents in Embodied City Environment |
| `zhou2023webarena` | 2023 | arXiv API | WebArena: A Realistic Web Environment for Building Autonomous Agents |
| `chopra2024limitsagencyagent` | 2024 | arXiv API | On the limits of agency in agent-based models |
| `du2024trajagent` | 2024 | arXiv API | TrajAgent: An LLM-Agent Framework for Trajectory Modeling via Large-and-Small Model Collaboration |
| `feng2024citybench` | 2024 | arXiv API | CityBench: Evaluating the Capabilities of Large Language Models for Urban Tasks |
| `feng2024citygpt` | 2024 | arXiv API | CityGPT: Empowering Urban Spatial Cognition of Large Language Models |
| `gao2024embodiedcity` | 2024 | arXiv API | EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-world City Environment |
| `jiang2024urbanllm` | 2024 | arXiv API | UrbanLLM: Autonomous Urban Activity Planning and Management with Large Language Models |
| `li2024chatsumo` | 2024 | arXiv API | ChatSUMO: Large Language Model for Automating Traffic Scenario Generation in Simulation of Urban Mobility |
| `li2024stbench` | 2024 | arXiv API | STBench: Assessing the Ability of Large Language Models in Spatio-Temporal Analysis |
| `mou2024agentsense` | 2024 | arXiv API | AgentSense: Benchmarking Social Intelligence of Language Agents through Interactive Scenarios |
| `shao2024chinatravel` | 2024 | arXiv API | ChinaTravel: An Open-Ended Travel Planning Benchmark with Compositional Constraint Validation for Language Agents |
| `trivedi2024appworld` | 2024 | arXiv API | AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents |
| `xu2024theagentcompany` | 2024 | arXiv API | TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks |
| `yan2024opencity` | 2024 | arXiv API | OpenCity: A Scalable Platform to Simulate Urban Activities with Massive LLM Agents |
| `yao2024bench` | 2024 | arXiv API | $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains |
| `zhou2024sotopia` | 2024 | ICLR/OpenReview + arXiv | SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents |
| `zhou2024thisreallife` | 2024 | arXiv API | Is this the real life? Is this just fantasy? The Misleading Success of Simulating Social Interactions With LLMs |
| `zhou2024urbench` | 2024 | arXiv API | UrBench: A Comprehensive Benchmark for Evaluating Large Multimodal Models in Multi-View Urban Scenarios |
| `adornetto2025generativeagentsagent` | 2025 | Crossref DOI | Generative Agents in Agent-Based Modeling: Overview, Validation, and Emerging Challenges |
| `bougie2025citysim` | 2025 | arXiv API | CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation |
| `feng2025urbanllava` | 2025 | arXiv API | UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence with Spatial Reasoning and Understanding |
| `gao2025simulatingmultistakeholder` | 2025 | Crossref DOI | Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning |
| `goel2025lifelongsotopia` | 2025 | arXiv API | LIFELONG SOTOPIA: Evaluating Social Intelligence of Language Agents Over Lifelong Social Interactions |
| `lai2025ustbench` | 2025 | arXiv API | USTBench: Benchmarking and Dissecting Spatiotemporal Reasoning of LLMs as Urban Agents |
| `larooij2025validationcentralchallenge` | 2025 | Crossref DOI | Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling |
| `liu2025gatsim` | 2025 | arXiv API | GATSim: Urban Mobility Simulation with Generative Agents |
| `lu2025canllmagents` | 2025 | arXiv API | Can LLM Agents Simulate Multi-Turn Human Behavior? Evidence from Real Online Customer Behavior Data |
| `mao2025deliverybench` | 2025 | arXiv API | DeliveryBench: Can Agents Earn Profit in Real World? |
| `piao2025agentsociety` | 2025 | arXiv API | AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society |
| `ye2025mobilecity` | 2025 | arXiv API | MobileCity: An Efficient Framework for Large-Scale Urban Behavior Simulation |
| `zhao2025cityeqa` | 2025 | arXiv API | CityEQA: A Hierarchical LLM Agent on Embodied Question Answering Benchmark in City Space |
| `zheng2025urbanplanbench` | 2025 | arXiv API | UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large Language Models |
| `anonymous2026mobisimbench` | 2026 | Archived OpenReview PDF (provisional) | MobiSim-Bench: A Multi-Perspective Benchmark for Evaluating LLM-Agent-Based Human Mobility Simulation |
| `chen2026efficientevidencegrounded` | 2026 | arXiv API | Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent |
| `chen2026trip` | 2026 | arXiv API | Trip+: Benchmarking Agents in Personalized Interactive Travel Planning |
| `cheng2026doagentsknow` | 2026 | arXiv API | Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents |
| `deng2026canaireason` | 2026 | arXiv API | Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment |
| `hui2026sttarena` | 2026 | arXiv API | STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics |
| `li2026genworld` | 2026 | arXiv API | GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies |
| `li2026trajgenagent` | 2026 | arXiv API | TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation |
| `liu2026generativeagentsurban` | 2026 | Crossref DOI | Generative agents for urban mobility: A cognitive framework for realistic travel behavior simulation |
| `pham2026liveculturebench` | 2026 | arXiv API | LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations |
| `santos2026whenplausiblenot` | 2026 | arXiv API | When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation |
| `song2026mobilitybench` | 2026 | arXiv API | MobilityBench: A Benchmark for Evaluating Route-Planning Agents in Real-World Mobility Scenarios |
| `zhao2026mechanismplausibilitygenerative` | 2026 | Crossref DOI | Mechanism Plausibility in Generative Agent-Based Modeling |
