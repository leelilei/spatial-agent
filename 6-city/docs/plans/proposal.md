# CityIntent Proposal

> Version: v0.1
> Updated: 2026-06-22
> Status: draft

## Title

**CityIntent: Evaluating Intention-Driven Agents in Verifiable Urban Spaces**

## One-Sentence Thesis

CityIntent is a benchmark for testing whether language-model agents can pursue
private intentions through spatially constrained urban environments, producing
feasible, adaptive, and socially coherent trajectories that can be verified by an
environment rather than merely judged as plausible text.

## Motivation

Recent work has made rapid progress on urban LLM benchmarks, embodied city
navigation, and large-scale LLM-driven urban simulation. CityBench, CityGPT,
STBench, and USTBench evaluate urban knowledge, spatial cognition, and
spatiotemporal reasoning. CityEQA, EmbodiedCity, UrBench, and UrbanLLaVA move
toward embodied or multimodal city-space understanding. CitySim, GATSim,
OpenCity, MobileCity, and AgentSociety demonstrate increasingly ambitious
large-scale simulations of urban activity and agent societies.

What remains under-specified is a benchmark for **intentional urban agency**.
Many systems can answer city questions, plan activities, or simulate aggregate
mobility, but we still lack a compact and resettable benchmark that asks:

> Given private goals, social context, and a constrained city environment, can an
> agent choose actions that remain feasible, goal-directed, spatially sensitive,
> and adaptive over time?

This is the gap CityIntent targets. The project should not compete by building a
larger CitySim. It should compete by making city-agent behavior **measurable**.

## Core Claim

Current urban-agent work tends to optimize one of three surfaces:

1. **Urban knowledge and reasoning**: QA, planning, spatial cognition, or
   professional judgment.
2. **Embodied perception and navigation**: visual city understanding,
   exploration, or question answering.
3. **Large-scale simulation realism**: aggregate activity, mobility, and
   city-dynamic patterns.

CityIntent targets a fourth surface:

4. **Verifiable intentional agency**: agents with hidden private goals act in a
   city world where the environment owns truth about location, time, cost,
   co-presence, opening hours, and disruptions.

The benchmark contribution is to separate **what the agent wants** from **what
the city allows**, and to score the trace where those two meet.

## Research Questions

1. **Intentionality**: Does the agent maintain and pursue a private goal across
   multiple steps, or does it drift with local prompt context?
2. **Spatial grounding**: Are movements and POI choices feasible under the map,
   travel times, opening hours, and capacity constraints?
3. **Spatial sensitivity**: When the same agents and goals are placed in a
   different urban layout, do their behaviors change in explainable ways?
4. **Adaptation**: When the environment changes, such as a closure, delay,
   crowding event, or route blockage, does the agent replan without inventing
   impossible success?
5. **Social-spatial coupling**: Do social goals and relationships interact with
   spatial constraints, such as deciding whether to make a long trip to meet a
   friend, avoid someone, or preserve a promise?

## Benchmark Object

A CityIntent item is a scenario package, not a question. Each package contains:

```text
urban world
+ agent personas
+ private intentions
+ public scenario context
+ social relationships
+ action schema
+ hidden or visible perturbations
+ deterministic environment validator
+ scoring rules
```

An episode runs as a closed loop:

```text
observe -> choose action/intention -> validate -> execute -> update world
-> observe outcome -> update memory -> continue
```

The LLM may choose intentions, explain tradeoffs, and select actions. The
environment decides whether the action is possible.

## Environment Scope

The first version should be **weakly embodied**, not full 3D.

Recommended MVP environment:

- graph-based city layout
- 20 to 40 POIs
- 10 to 30 agents
- 2 to 8 hour simulated episodes
- explicit travel times and route costs
- POI opening hours, tags, prices, and capacity
- social relationships and known-place memories
- disruptions such as closure, congestion, or changed meeting place

This scope is intentionally smaller than CitySim or EmbodiedCity. The aim is
control, repeatability, and causal comparison, not visual realism.

## Action Space

The initial action set should be small and typed:

```text
move(destination)
wait(duration)
enter(poi)
leave(poi)
buy(item)
talk(agent, message)
invite(agent, poi, time)
ask_info(target)
revise_plan(reason)
abandon_goal(reason)
```

Invalid actions are not silently corrected. They are logged and scored.

## Evaluation Dimensions

| Dimension | Mostly automatic? | What it measures |
|---|---|---|
| Goal completion | mixed | Whether the private intention was satisfied. |
| Spatial feasibility | yes | Whether movement and POI use were physically and temporally possible. |
| Constraint compliance | yes | Violations of time, budget, opening hours, capacity, or role constraints. |
| Spatial sensitivity | yes/mixed | Whether behavior changes appropriately under layout or access perturbations. |
| Adaptation and replanning | mixed | Recovery after route blockage, POI closure, delay, or missed meeting. |
| Persona consistency | mixed | Alignment with preferences, habits, mobility limits, and prior choices. |
| Social-spatial coupling | mixed | Whether relationship goals affect movement and interaction decisions. |
| Believability | human/LLM | Whether the trace reads as plausible urban behavior. |
| Efficiency | yes | LLM calls, tokens, invalid-action retries, and unnecessary movement. |

The benchmark should prioritize automatic scoring first. LLM or human judges
should be reserved for soft dimensions such as believability or relationship
quality.

## Scenario Families

### Family A: Layout Sensitivity

Hold agents, POIs, and goals constant while changing the city graph.

Question:

> Do agents react to urban morphology, such as central plazas, linear corridors,
> bottlenecks, clustered neighborhoods, or dispersed POIs?

Primary metrics:

- travel time
- encounter rate
- missed appointments
- POI diversity
- invalid moves
- behavior divergence across layouts

### Family B: Intention Conflict

Give an agent conflicting needs and obligations.

Example:

- The agent is hungry and tired.
- A friend invites them to a distant event.
- A nearby cafe is cheap but unappealing.
- A preferred cafe is far and crowded.

Primary metrics:

- goal tradeoff quality
- consistency across paraphrases
- route and time feasibility
- relationship outcome

### Family C: Disruption and Replanning

Introduce a change after the agent has formed a plan.

Examples:

- a store closes early
- a subway segment fails
- a route is blocked
- a friend changes the meeting place
- a public event creates crowding

Primary metrics:

- recovery success
- adaptation latency
- invalid action rate
- final goal completion
- explanation quality

### Family D: Social Encounters in Space

Test whether spatial co-presence creates social consequences.

Examples:

- repeated incidental encounters in a central space
- private information spreads faster in compact layouts
- dispersed layouts reduce accidental meetings but increase intentional trips

Primary metrics:

- encounter-to-interaction conversion
- relationship change
- information spread
- privacy leakage
- social goal completion

## Baselines

CityIntent should compare agents, not only models.

Initial baselines:

1. **Fixed schedule baseline**: follows a pre-generated daily schedule.
2. **Utility policy baseline**: chooses actions by explicit utility over distance,
   time, need, and relationship weights.
3. **LLM one-shot planner**: writes a plan once, then follows it.
4. **LLM reactive agent**: observes the current world state and chooses each next
   action.
5. **LLM memory agent**: uses memory, reflection, or structured state across the
   episode.
6. **Oracle planner**: has full map/state access and provides an approximate upper
   bound for feasibility and goal completion.

The interesting comparison is not only which LLM is stronger. It is whether an
agent architecture preserves intention while respecting environment constraints.

## Expected Contribution

CityIntent should claim three contributions:

1. **Benchmark formulation**: a scenario-package format for private-goal urban
   agent episodes.
2. **Scoring framework**: automatic spatial and temporal validation combined with
   limited soft judging for believability and social effects.
3. **Diagnostic findings**: evidence about where current LLM-agent policies fail,
   such as goal drift, spatial insensitivity, invalid action hallucination, or weak
   replanning after disruption.

## Relationship To Prior Work

CityIntent is inspired by SOTOPIA's interactive evaluation structure, but it
should not be framed as a SOTOPIA derivative. The right positioning is:

- **Generative Agents** motivates memory, reflection, planning, and believable
  simulated daily behavior.
- **SOTOPIA** motivates private-goal interactive episodes and multi-dimensional
  evaluation.
- **Concordia** motivates environment-grounded action and game-master style world
  control.
- **CityBench / USTBench / STBench / CityGPT** motivate the urban and
  spatiotemporal benchmark landscape.
- **CityEQA / EmbodiedCity / UrBench / UrbanLLaVA** define the embodied and
  multimodal city-space branch.
- **CitySim / GATSim / OpenCity / MobileCity / AgentSociety** define large-scale
  city and society simulation neighbors.

The novel position is:

> CityIntent evaluates intentional city behavior under resettable spatial and
> social constraints, rather than evaluating urban knowledge, visual perception,
> aggregate realism, or simulator scale alone.

## MVP Plan

### Phase 0: Specification

- Define the scenario package schema.
- Define the action API.
- Define automatic validators for movement, time, POI access, and co-presence.
- Create 10 to 20 seed scenarios across Layout Sensitivity and Disruption.

### Phase 1: Simulator and Scorer

- Implement a graph-based city environment.
- Implement deterministic transition and validation.
- Implement trace logging.
- Implement goal completion, feasibility, invalid-action, travel-cost, and
  adaptation metrics.

### Phase 2: Agent Baselines

- Run fixed schedule, utility planner, LLM one-shot, LLM reactive, and LLM memory
  agents.
- Evaluate across repeated seeds and paraphrased prompts.
- Compare not only mean scores, but failure modes.

### Phase 3: Benchmark Paper

- Present the benchmark and scenario families.
- Report baseline failures and qualitative trace analysis.
- Release scenario packages, scorer, and reference agents.

## Success Criteria

The first paper is viable if CityIntent can show:

1. The benchmark catches failures that static urban QA does not catch.
2. Layout or disruption perturbations produce measurable differences in agent
   behavior.
3. Current LLM agents often produce plausible explanations while violating
   environment constraints or drifting from private goals.
4. Automatic scorers can handle the hard correctness dimensions, reducing
   over-reliance on LLM judges.

## Key Risks

1. **Too small to matter**: A graph-based micro-city may look toy-like. Mitigation:
   focus on controlled causal tests and transparent failure modes.
2. **Too subjective**: Believability and social quality can become judge-dependent.
   Mitigation: make automatic feasibility and perturbation metrics the core.
3. **Too close to existing city benchmarks**: USTBench and CityEQA are close.
   Mitigation: emphasize private goals, multi-step traces, and social-spatial
   coupling.
4. **Too close to CitySim**: CitySim is the obvious neighbor. Mitigation: frame
   CityIntent as a benchmark harness for evaluating agent policies, not a
   large-scale simulator.

## First Paper Shape

The paper can be organized as:

1. Introduction: city agents need verifiable intentional agency.
2. Related Work: urban benchmarks, embodied city agents, large-scale city sims,
   social-agent benchmarks.
3. Benchmark Design: scenario packages, environment loop, action schema.
4. Metrics: automatic validation plus soft judging.
5. Baselines: fixed, utility, LLM one-shot, LLM reactive, LLM memory.
6. Results: feasibility, goal completion, spatial sensitivity, adaptation.
7. Failure Analysis: goal drift, invalid action, spatial blindness, weak replanning.
8. Discussion: why controlled micro-cities are a useful bridge toward larger city
   simulations.

## Working Claim

CityIntent should make a modest but sharp claim:

> A city-agent benchmark should not only ask whether agents know cities or can
> generate plausible schedules. It should test whether agents can maintain private
> intentions while acting in a world that constrains what they can actually do.

