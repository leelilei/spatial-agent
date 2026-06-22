# CityAgency Proposal

> Version: v0.3
> Updated: 2026-06-22
> Status: draft

## Title

**Plausible Plans, Impossible Traces: CityAgency as a Benchmark for Urban Agent Agency**

## One-Sentence Thesis

CityAgency is a microfoundational benchmark for measuring the gap between
plausible urban plans and executable urban traces: whether language-model agents
can maintain private intentions, respect city constraints, recover from urban
disruptions, and produce action traces that are verified by an environment
rather than merely judged as plausible text.

## Motivation

Recent work has made rapid progress on urban LLM benchmarks, embodied city
navigation, and large-scale LLM-driven urban simulation. CityBench, CityGPT,
STBench, and USTBench evaluate urban knowledge, spatial cognition, and
spatiotemporal reasoning. CityEQA, EmbodiedCity, UrBench, and UrbanLLaVA move
toward embodied or multimodal city-space understanding. CitySim, GATSim,
OpenCity, MobileCity, and AgentSociety demonstrate increasingly ambitious
large-scale simulations of urban activity and agent societies.

Recent mobility-realism work also shows an important gap: LLM-driven city
simulation can produce plausible narratives while failing to reproduce empirical
mobility patterns such as trip distributions, dwell times, OD flows, activity
transitions, and temporal rhythms. That line of work is valuable, but it mainly
tests **macro-level realism**.

What remains under-specified is a benchmark for **micro-level urban agency**:
the local decision mechanisms that should make macro urban behavior credible in
the first place. Many systems can answer city questions, plan activities, or
simulate aggregate mobility, but we still lack a compact and resettable benchmark
that asks:

> Given private goals, social context, and a constrained city environment, can an
> agent choose actions that remain feasible, goal-directed, spatially sensitive,
> and adaptive over time?

This is the gap CityAgency targets. The project should not compete by building a
larger CitySim or by claiming to replace macro mobility-realism benchmarks. It
should compete by making the micro-mechanisms of city-agent behavior
**measurable**.

## Core Claim

Current urban-agent work tends to optimize one of three surfaces:

1. **Urban knowledge and reasoning**: QA, planning, spatial cognition, or
   professional judgment.
2. **Embodied perception and navigation**: visual city understanding,
   exploration, or question answering.
3. **Large-scale simulation realism**: aggregate activity, mobility, and
   city-dynamic patterns.

Social-agent benchmarks add another important surface:

4. **Interactive social intelligence**: hidden goals, dialogue strategy,
   relationship management, and social norm reasoning.

CityAgency targets a missing middle between these surfaces:

5. **Verifiable micro-level urban agency**: agents with hidden private goals act in a
   city world where the environment owns truth about location, time, cost,
   co-presence, opening hours, and disruptions.

The benchmark contribution is to separate **what the agent wants** from **what
the city allows**, and to score the trace where those two meet.

The project should therefore make a precise claim:

> Macro mobility realism tells us whether a simulated city looks statistically
> realistic. CityAgency diagnoses whether the individual agents have the
> micro-level agency needed to generate such behavior under urban constraints.

## Central Hypothesis: The Plausibility-Feasibility Gap

The paper should be organized around a sharper empirical hypothesis:

> Current LLM urban agents can often produce plausible plans and explanations,
> but their executed traces become impossible when the city pushes back.

This gap is not a stylistic flaw. It is a mechanism failure. An agent may explain
why it should commute, visit a pharmacy, keep a lunch appointment, avoid a crowd,
or comfort a friend, while the trace shows that it crossed a blocked route,
entered a closed POI, exceeded the episode time window, repeated an already
completed errand, or lost the original goal after a social interaction.

CityAgency should therefore report two scores side by side:

1. **Plan plausibility**: whether the agent's plan, rationale, or dialogue reads
   as reasonable urban behavior.
2. **Trace feasibility**: whether the environment can execute the resulting
   action trace under map, time, budget, POI, and social constraints.

The central result should be a **plausibility-feasibility gap**: cases where
agents look competent in language but fail as city actors.

## Research Questions

1. **Agency persistence**: Does the agent maintain and pursue a private goal
   across multiple steps, or does it drift with local prompt context?
2. **Constraint awareness**: Are movements and POI choices feasible under the map,
   travel times, opening hours, and capacity constraints?
3. **Spatial sensitivity**: When the same agents and goals are placed in a
   different urban layout, do their behaviors change in explainable ways?
4. **Adaptation**: When the environment changes, such as a closure, delay,
   crowding event, or route blockage, does the agent replan without inventing
   impossible success?
5. **Social interruption recovery**: When social interaction competes with the
   private goal, can the agent behave socially while still recovering the
   original task?
6. **Micro-to-macro relevance**: Do failures in individual agency explain
   downstream mobility or activity-chain failures, rather than appearing only as
   local task mistakes?

## Benchmark Object

A CityAgency item is a scenario package, not a question. Each package contains:

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

The current `cityintent_v0` benchmark package should be treated as the first
CityAgency task track. In this structure:

- **CityAgency** is the overall benchmark and research frame.
- **CityIntent** is the first track, focused on intention persistence and
  constraint-sensitive action.
- Future tracks can add richer replanning, social recovery, activity-chain, and
  macro-calibration probes without renaming the project again.

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
| Plan plausibility | human/LLM | Whether the proposed plan or rationale reads as reasonable urban behavior. |
| Trace feasibility | yes | Whether the action trace can be executed under map, time, budget, POI, and social constraints. |
| Plausibility-feasibility gap | mixed | Whether a plausible plan produces an impossible or invalid trace. |
| Intention completion | mixed | Whether the private goal was satisfied. |
| Agency persistence | mixed | Whether the agent keeps pursuing the goal after delays, distractions, and partial success. |
| Constraint compliance | yes | Violations of time, budget, opening hours, capacity, or role constraints. |
| Spatial sensitivity | yes/mixed | Whether behavior changes appropriately under layout or access perturbations. |
| Adaptation and replanning | mixed | Recovery after route blockage, POI closure, delay, or missed meeting. |
| Done-state awareness | yes/mixed | Whether the agent stops repeating completed errands and avoids redundant action loops. |
| Social recovery | mixed | Whether relationship behavior helps or distracts from the private goal. |
| Activity-chain coherence | mixed | Whether the trace forms a plausible daily sequence rather than isolated task completions. |
| Believability | human/LLM | Whether the trace reads as plausible urban behavior. |
| Efficiency | yes | LLM calls, tokens, invalid-action retries, and unnecessary movement. |

The benchmark should prioritize automatic scoring for trace correctness. LLM or
human judges should be reserved for plan plausibility, believability, or
relationship quality. This separation is essential: the paper's core story
depends on comparing what sounds plausible with what the city can actually
execute.

## Impossible Trace Taxonomy

The first paper should make failure types concrete enough to count.

| Failure type | Urban meaning | Example validator signal |
|---|---|---|
| Impossible route | Spatial execution failure | The trace crosses a blocked or disconnected edge. |
| Closed-place action | Institutional constraint failure | The agent enters or buys from a POI outside opening hours. |
| Time-budget failure | Time-geography failure | The trace misses an appointment or exceeds the episode window. |
| Money-budget failure | Resource/accessibility failure | The agent spends more than its available budget. |
| Goal drift | Agency persistence failure | The agent stops pursuing the private goal without justified abandonment. |
| Social derailment | Social recovery failure | The agent interacts socially but fails to return to the original task. |
| Done-state loop | State tracking failure | The agent repeats an already completed errand or purchase. |
| Plausible-but-invalid rationale | Language-world mismatch | The rationale says the plan is feasible while the validator rejects the trace. |

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

### Family E: Micro-to-Macro Mechanism Probes

Connect individual agency failures to city-research phenomena.

Examples:

- a transit disruption changes commute mode, work arrival time, and after-work
  errands
- a low-budget agent compresses its activity space and drops optional services
- a service closure shifts demand to nearby substitutes and changes local crowding
- social or care obligations create non-work trips that alter activity chains

Primary metrics:

- activity-chain completion
- trip substitution or cancellation
- time-geography constraint violations
- accessibility loss under budget or mobility limits
- downstream changes in POI load, OD flow, or encounter opportunities

## Baselines

CityAgency should compare agents, not only models.

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

The expected first-result pattern is:

- Rule-based agents may be more feasible but brittle and less socially natural.
- Direct LLM actors may produce plausible rationales but more impossible traces.
- Reactive or memory-based agents should reduce some failures, especially
  disruption recovery, goal drift, and done-state loops.
- Oracle or validator-assisted policies define how much of the gap is caused by
  agent architecture rather than scenario infeasibility.

This comparison supports the paper's main punchline: urban agent quality is not
only a language-model capability. It depends on architectures that separate
intention, planning, memory, and environment validation.

## Expected Contribution

CityAgency should claim four contributions:

1. **Microfoundational benchmark formulation**: a scenario-package format for
   private-goal urban agent episodes that links individual decision mechanisms to
   city-level behavior questions.
2. **Plausibility-feasibility evaluation**: a protocol that scores plan
   plausibility separately from executable trace feasibility.
3. **Scoring framework**: automatic spatial and temporal validation combined with
   limited soft judging for believability and social effects.
4. **Diagnostic findings**: evidence about where current LLM-agent policies fail,
   such as goal drift, spatial insensitivity, invalid action hallucination, or weak
   replanning after disruption.

## Relationship To Prior Work

CityAgency is inspired by SOTOPIA's interactive evaluation structure, but it
should not be framed as a SOTOPIA derivative. The right positioning is:

- **Generative Agents** motivates memory, reflection, planning, and believable
  simulated daily behavior.
- **SOTOPIA** motivates private-goal interactive episodes and multi-dimensional
  evaluation.
- **AgentSense and related social-agent benchmarks** motivate evaluation of
  social intelligence, norm awareness, and private-goal behavior under
  interaction.
- **Concordia** motivates environment-grounded action and game-master style world
  control.
- **CityBench / USTBench / STBench / CityGPT** motivate the urban and
  spatiotemporal benchmark landscape.
- **CityEQA / EmbodiedCity / UrBench / UrbanLLaVA** define the embodied and
  multimodal city-space branch.
- **CitySim / GATSim / OpenCity / MobileCity / AgentSociety** define large-scale
  city and society simulation neighbors.
- **MobiSim-Bench** is the closest mobility-simulation benchmark neighbor,
  evaluating LLM-agent-based human mobility simulation through robustness,
  realism, and responsiveness.
- **Mobility-realism benchmarks**, especially recent work arguing that plausible
  LLM city simulations are not necessarily realistic, motivate the macro
  validation layer: simulated traces should eventually be checked against
  empirical mobility regularities, OD flows, dwell times, temporal rhythms, and
  activity transitions.
- **tau-bench, AppWorld, WebArena, and TheAgentCompany** motivate executable
  agent evaluation: environment-owned state, domain rules, repeat trials, and
  task completion judged by state changes rather than by text alone.
- **FeasiGen and related feasibility-awareness work** motivate explicit
  infeasible-task evaluation and false-continue metrics.
- **Travel-planning benchmarks such as ChinaTravel** motivate compositional
  constraint validation over multi-POI plans with implicit user intent.

The novel position is:

> CityAgency evaluates the micro-level agency mechanisms behind urban behavior:
> intention persistence, feasible action, social recovery, and replanning under
> city constraints. It complements macro mobility-realism benchmarks, social
> benchmarks, and general executable-agent benchmarks rather than replacing them.

## MVP Plan

### Phase 0: Specification

- Define the scenario package schema.
- Define the action API.
- Define automatic validators for movement, time, POI access, and co-presence.
- Create 10 to 20 seed scenarios across intention persistence, layout
  sensitivity, social recovery, and disruption.

### Phase 1: Simulator and Scorer

- Implement a graph-based city environment.
- Implement deterministic transition and validation.
- Implement trace logging.
- Implement goal completion, feasibility, invalid-action, travel-cost, and
  adaptation metrics.
- Implement the impossible-trace taxonomy so failures can be reported by type.

### Phase 2: Agent Baselines

- Run fixed schedule, utility planner, LLM one-shot, LLM reactive, and LLM memory
  agents.
- Evaluate across repeated seeds and paraphrased prompts.
- Add a lightweight plausibility judge for plans, rationales, and final trace
  narratives.
- Compare not only mean scores, but the gap between plausible plans and feasible
  traces.

### Phase 3: Benchmark Paper

- Present the benchmark and scenario families.
- Report baseline failures and qualitative trace analysis.
- Release scenario packages, scorer, and reference agents.
- Position `cityintent_v0` as the first CityAgency track, then describe which
  macro mobility-realism hooks should be added next.
- Make the first main result a plausibility-feasibility gap table: agent policy
  by plan plausibility, trace feasibility, goal completion, and impossible-trace
  failure type.

## Success Criteria

The first paper is viable if CityAgency can show:

1. The benchmark catches failures that static urban QA does not catch.
2. Layout or disruption perturbations produce measurable differences in agent
   behavior.
3. Current LLM agents often produce plausible explanations while violating
   environment constraints or drifting from private goals.
4. Micro-level failures can be connected to urban behavior mechanisms such as
   activity-chain breakdown, accessibility loss, missed appointments, or disrupted
   service use.
5. Automatic scorers can handle the hard correctness dimensions, reducing
   over-reliance on LLM judges.
6. The plausibility-feasibility gap varies by agent architecture, not only by
   base model.

## Key Risks

1. **Too small to matter**: A graph-based micro-city may look toy-like. Mitigation:
   connect each scenario family to a recognized urban mechanism such as
   time-geography constraints, activity chains, accessibility, service
   substitution, or social co-presence.
2. **Too subjective**: Believability and social quality can become judge-dependent.
   Mitigation: make automatic feasibility and perturbation metrics the core.
3. **Too close to existing city benchmarks**: USTBench and CityEQA are close.
   Mitigation: emphasize private goals, multi-step traces, and social-spatial
   coupling.
4. **Too close to CitySim**: CitySim is the obvious neighbor. Mitigation: frame
   CityAgency as a benchmark harness for evaluating agent policies, not a
   large-scale simulator.
5. **Too detached from macro urban research**: Micro agency can become an AI toy
   task if it is not tied to city phenomena. Mitigation: include a
   micro-to-macro analysis layer and describe how v0 failures would scale into
   mobility, activity, or accessibility errors.

## First Paper Shape

The paper can be organized as:

1. Introduction: plausible urban plans can still produce impossible traces.
2. Related Work: urban benchmarks, embodied city agents, large-scale city sims,
   social-agent benchmarks, and mobility-realism evaluation.
3. Benchmark Design: scenario packages, environment loop, action schema.
4. Metrics: plan plausibility, trace feasibility, agency persistence, and
   impossible-trace taxonomy.
5. Baselines: fixed, utility, direct LLM, one-shot planning, reactive replanning,
   memory, and oracle.
6. Results: the plausibility-feasibility gap across agent architectures.
7. Failure Analysis: impossible routes, closed-place actions, time-budget failure,
   social derailment, done-state loops, and goal drift.
8. Discussion: why controlled micro-cities are a useful bridge from language
   plausibility to larger city simulations and mobility realism.

## Working Claim

CityAgency should make a modest but sharp claim:

> A city-agent benchmark should not only ask whether agents know cities, generate
> plausible schedules, or match aggregate mobility statistics. It should test
> whether plausible plans become executable traces when the city constrains what
> agents can actually do.

