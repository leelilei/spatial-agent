# Phase 1 Targeted Expansion Search Round 2

Date: 2026-04-14  
Scope: broadened `Core` expansion after accepting that VR / virtual-world / community-oriented spatial-social systems count as `Core`

## 1. Why this round exists

Under the stricter earlier boundary, the working `Core` set was stuck at:

- `8` retained `core` systems in abstract rereview round 1
- `+3` high-confidence targeted additions from the first targeted expansion round

That only yields a working set of roughly `11`, which is too small if the survey is expected to support a stable `Core` corpus near or above `20`.

The key decision for this round is:

- Count explicit spatial-social systems in `VR`, `virtual worlds`, `metaverse`, `digital twin / community`, and `coordination-in-space` settings as `Core`
- Keep excluding pure spatial reasoning benchmarks and pure non-spatial social simulation

## 2. Promotion candidates already in the pool

These papers were already present in the Phase 1 pool and should now be treated as `core-candidate` under the broadened boundary.

### P01. Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios

- Status change: `adjacent -> core-candidate`
- Why:
  - explicit `VR` environment
  - explicit spatial interactions and conversations
  - socially interactive agent behavior in situated role-play

### P02. When LLMs Recognize Your Space: Research on Experiences with Spatially Aware LLM Agents

- Status change: `adjacent -> core-candidate`
- Why:
  - explicit spatially aware agent design
  - user experience and social interaction happen inside a recognized space rather than abstract prompting only

### P03. SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds

- Status change: `future-watch -> core-candidate`
- Source: `arXiv`
- DOI: `10.48550/arXiv.2512.01078`
- Why:
  - very explicit `physical and social worlds`
  - multi-agent task execution includes cooperation and competition in open-ended environments
  - this is no longer just an adjacent benchmark under the updated boundary

## 3. Newly added broadened-core candidates

The following items were not in the current Phase 1 pool and are worth adding as new `core-candidate` entries.

### N01. A Context-Aware Onboarding Agent for Metaverse Powered by Large Language Models

- Year: `2025`
- Venue: `CHI EA 2025`
- Why:
  - explicit `metaverse` environment
  - socially interactive onboarding in space-aware immersive settings

### N02. An Open-Domain Avatar Chatbot by Exploiting a Large Language Model

- Year: `2023`
- Venue: `SIGDIAL 2023`
- Why:
  - avatar-based social interaction in immersive or embodied conversational settings
  - more spatially situated than plain text chat systems

### N03. A Voice-Controlled Dialogue System for NPC Interaction using Large Language Models

- Year: `2024`
- Venue: `IJCCI 2024`
- Why:
  - explicit `NPC interaction`
  - game-world social interaction in an identifiable virtual environment

### N04. Mixed-Initiative Dialogue Management for Human-Virtual Agents Interaction in Forum Theatre Inspired Training

- Year: `2025`
- Venue: `IWSDS 2025`
- Why:
  - human-virtual-agent interaction in a staged spatial training setup
  - social interaction is central and environment is not abstract

### N05. Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment

- Year: `2026`
- Venue: `Safety Science`
- Why:
  - explicit spatial environment: `cellular automata environment` and `shopping mall fire scenario`
  - socially relevant multi-agent behavior under constraints

### N06. When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios

- Year: `2026`
- Venue: `Reliability Engineering & System Safety`
- URL: `https://www.sciencedirect.com/science/article/pii/S0951832025012554`
- Why:
  - explicit crowd movement in disaster space
  - combines environment, agent interaction, and collective behavior

### N07. CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation

- Year: `2025`
- Venue: `arXiv`
- DOI: `10.48550/arXiv.2506.21805`
- Why:
  - city-scale explicit urban environment
  - directly centered on urban behaviors and city dynamics

### N08. TongSIM: A General Platform for Simulating Intelligent Machines

- Year: `2025`
- Venue: `arXiv`
- DOI: `10.48550/arXiv.2512.20206`
- Why:
  - outdoor town simulation with embodied and social scenarios
  - broad simulator, but the environment and interaction structure are explicit enough to screen as `Core`

### N09. S^3: Social-network Simulation System with Large Language Model-Empowered Agents

- Year: `2024`
- Venue: `arXiv`
- DOI: `10.48550/arXiv.2404.08584`
- Why:
  - not physical space, but a structured digital social environment
  - counts under the same logic that allowed `OASIS`

### N10. Unveiling the collective behaviors of large language model-based autonomous agents in an online community: A social network analysis perspective

- Year: `2025`
- Venue: `Expert Systems with Applications`
- Why:
  - explicit online community environment
  - collective behavior and network-level social structure are central

### N11. Artificial intelligence chatbots mimic human collective behaviour

- Year: `2024`
- Venue: `Nature Human Behaviour`
- Why:
  - strong evidence for collective social dynamics among chatbots in a structured online environment
  - useful if digital social space remains admissible in `Core`

### N12. DeMAC: Enhancing Multi-Agent Coordination with Dynamic DAG and Manager-Player Feedback

- Year: `2025`
- Venue: `ACL 2025 Findings`
- Why:
  - explicit coordination in an interactive shared environment
  - weaker than urban / VR / community cases, but defensible under the broadened `coordination-in-space` boundary

## 4. Working-set count under the broadened boundary

Approximate `Core` working-set arithmetic after this round:

- existing retained `core`: `8`
- targeted expansion round 1 additions: `3`
- round 2 promotions from existing pool: `3`
- round 2 new broadened-core additions: `12`

This yields a broadened `Core` working set of about `26` candidate systems/papers before full-text confirmation.

That does **not** mean all `26` will survive final screening.
It does mean the survey is no longer blocked by an obviously undersized `Core` search surface.

## 5. Recommended next move

Do not jump straight from this list to narrative claims.

Instead:

1. Ingest the new round-2 seed batch.
2. Re-run dedupe and prescreen with the updated broadened-core heuristic.
3. Create a `core-confirmation shortlist` with three confidence levels:
   - `high-confidence core`
   - `borderline but keep`
   - `likely demote later`

That will let the project reach `20+` plausible `Core` candidates without pretending all of them are equally strong.
