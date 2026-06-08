# Phase 1 Targeted L4 Search Memo

Date: 2026-04-27

Purpose: run one narrow follow-up search aimed only at the remaining `L4` gap after `R3-01`, `R3-02`, and `R3-04` were integrated into the stable Core table.

## L4 rule used here

The coding threshold was the current manual's strict definition:

- `L4` means the agent directly receives global configurational or topological indicators such as `integration`, `depth`, `control`, `choice`, or a clearly equivalent whole-layout structural measure.
- Plain maps, road graphs, adjacency, nearby-area lists, direction-distance cues, GPS, coordinates, route options, or local service accessibility do **not** count as `L4` by themselves.
- A paper was eligible only if it still met the normal `Core` boundary: LLM/VLM-driven agent system, multi-agent or population setting, recognizable spatial environment, and social/group behavior.

## Search scope

Targeted searches were run against current primary-source pages and open-access records, focusing on combinations of:

- `space syntax`
- `integration / depth / control / choice`
- `LLM / generative agents / multi-agent`
- `urban planning / participatory planning / simulation`

Direct query families included:

- `"space syntax" "large language model" agent`
- `"integration" "large language model" "multi-agent" simulation`
- `"LLM" multi-agent urban planning space syntax`
- `"configurational" "large language model" agent-based`

## Screening outcome

### 1. Large Language Model for Participatory Urban Planning

Primary source:

- arXiv abstract and full HTML: `https://arxiv.org/abs/2402.17161`

Why it looked promising:

- clear LLM multi-agent planning setup
- real urban regions
- planner plus thousands of residents
- whole-region planning plus neighborhood feedback

Why it does **not** fill `L4`:

- the planner receives a region map plus textual descriptions of positions and nearby areas
- residents are informed of direction and distance for areas within `500m`
- the paper uses service accessibility and ecology metrics for evaluation
- no evidence was found that agents directly receive `integration`, `depth`, `control`, `choice`, visibility-graph metrics, or any equivalent whole-layout configurational index

Conservative reading:

- best coded as strong `L3`, not `L4`

### 2. Simulating Multi-Stakeholder Decision-Making with Generative Agents in Urban Planning

Primary source:

- IOS/SAGE open full text: `https://doi.org/10.3233/ATDE251076`

Why it looked promising:

- LLM generative agents
- explicit multi-stakeholder urban planning discussion
- real redevelopment case

Why it does **not** fill `L4`:

- agent prompts are role, demographics, daily life/value, and task format
- the operational setup is stakeholder deliberation over proposals, not spatially structured agent input
- no configurational metrics or global topology indicators are exposed to the agents

Conservative reading:

- not an `L4` candidate
- likely outside the stable Core evidence map unless urban deliberation itself becomes a separate scope

### 3. AI Agent as Urban Planner: Steering Stakeholder Dynamics in Urban Planning via Consensus-based Multi-Agent Reinforcement Learning

Primary source:

- arXiv abstract and full HTML: `https://arxiv.org/abs/2310.16772`

Why it looked promising:

- participatory urban planning
- multi-agent collective decision making
- explicit spatial graph structure

Why it does **not** fill `L4`:

- the system is not an LLM multi-agent Core paper; it is a consensus-based MARL framework
- the environment is abstracted into a spatial graph processed by GNNs
- no direct evidence shows agent-facing configurational indicators equivalent to `integration / depth / control / choice`

Conservative reading:

- useful bridge case for planning computation
- not a stable `Core L4` candidate

### 4. UrbanLLM: Autonomous Urban Activity Planning and Management with Large Language Models

Primary sources:

- arXiv abstract: `https://arxiv.org/abs/2406.12360`
- ACL Anthology record: `https://aclanthology.org/2024.findings-emnlp.98/`

Why it looked promising:

- strong urban/spatio-temporal task framing
- LLM explicitly orchestrates urban analysis subtasks

Why it does **not** fill `L4`:

- it is primarily a problem-solving/orchestration system, not a multi-agent social simulation
- no evidence was found that its agent input contains global configurational indicators in the manual's `L4` sense
- it is better treated as `Adjacent` if needed, not as a stable `Core` supplement

## Negative search signal

The most direct `L4`-oriented query family produced no stable Core hit:

- no convincing `space syntax + LLM multi-agent` system paper was found
- no convincing paper was found where LLM agents explicitly receive `integration`, `depth`, `control`, or `choice`
- no convincing `Core` paper was found where whole-layout configurational metrics are part of the agent-facing state rather than only an external evaluation layer

## Decision

This pass did **not** identify a stable `L4` Core candidate.

Current interpretation:

- the `L4 = 0` cell remains open
- after a targeted search pass, the absence now looks more like a real literature gap than a simple retrieval miss
- the nearest urban-planning candidates strengthen the case that current systems often stop at maps, graphs, directions, local accessibility, or planner-side global views, rather than exposing explicit configurational metrics to agents

## Operational consequence

- Do not add any new stable Core row from this `L4` search pass.
- Keep `L4` as a manuscript-level negative finding.
- Reopen search only if the project later decides to widen scope toward `Adjacent` bridge systems or to count planner-side configurational analytics that are not yet agent-accessible under the current coding manual.
