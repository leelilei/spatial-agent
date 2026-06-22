# CityIntent Agent Evaluation Plan

Date: 2026-06-22

Purpose: define which city-agent policies the first CityAgency / CityIntent
track should evaluate, and clarify what SOTOPIA actually compared.

Naming note: **CityAgency** is now the umbrella project name. **CityIntent** is
the v0 track that focuses on intention persistence, feasible city action, and
replanning under constraints.

## Short Answer

SOTOPIA did **not** benchmark many agent architectures. It mainly benchmarked
different language models under the same simple role-play policy:

```text
scenario + character + private goal + interaction history -> next action
```

The compared agents were GPT-4, GPT-3.5, Llama-2-70b-chat, and MPT-30b-chat,
with humans added on SOTOPIA-hard as a comparison point. The paper explicitly
leaves richer prompting / control methods such as Chain-of-Thought and ReAct as
future work.

This creates the opening for CityIntent: we can make **agent architecture** a
first-class benchmark axis, not only the underlying LLM.

## What SOTOPIA Evaluated

SOTOPIA builds two-agent social episodes from:

- character profiles
- relationships
- shared scenario context
- private social goals
- multi-turn action history
- seven-dimensional SOTOPIA-EVAL scoring

The main experimental matrix compares models as agents:

| Axis | SOTOPIA choice |
|---|---|
| Agent policy | Simple prompt-based role-play/action generation |
| Model agents | GPT-4, GPT-3.5, Llama-2-70b-chat, MPT-30b-chat |
| Human comparison | Human-human and human-GPT-4 interactions on SOTOPIA-hard |
| Architecture ablations | Not the main focus |
| Future methods named | Chain-of-Thought, ReAct |
| Main finding style | Dynamic interaction reveals failures not visible in static benchmarks |

For CityIntent, the corresponding question should be:

> Given the same city world, personas, private intentions, and perturbations, do
> different agent architectures produce measurably different urban behavior?

## Evaluation Axes For CityIntent

CityIntent should separate two variables:

1. **Agent architecture**: memory, planning, replanning, utility calculation,
   spatial grounding, reflection, and action validation.
2. **Base model**: GPT-4-class, smaller OpenAI model, open-weight model, or
   local model.

For v0, prioritize architecture first. A benchmark that shows architecture
differences under one strong model is more diagnostic than a model leaderboard
where all agents share the same weak policy.

## Recommended V0 Agent Set

These are the agents we should implement or wrap first.

| Priority | Agent | What it tests | Why include it |
|---|---|---|---|
| P0 | FixedScheduleAgent | Script-following baseline | Shows how much performance comes from prewritten routines rather than agency |
| P0 | UtilityPlannerAgent | Non-LLM decision baseline | Gives a deterministic floor using time, distance, cost, need, and relationship weights |
| P0 | LLMDirectActor | SOTOPIA-like direct action prompt | Closest analogue to SOTOPIA's main agent policy |
| P0 | LLMPlanThenActAgent | Initial plan commitment | Tests whether one-shot planning survives spatial constraints and disruptions |
| P0 | LLMReactiveReplanner | Observe-update-act loop | Tests short-horizon adaptation when routes, POIs, or social opportunities change |
| P0 | GenerativeAgentMemoryAgent | Memory + reflection + planning | Tests the classic generative-agent claim: stable intent across time and space |
| P0 | OraclePlannerAgent | Upper-bound reference | Tells us whether a scenario is feasible before blaming LLMs |

This seven-agent set is enough for a first benchmark paper table. It gives us
scripted, rule-based, direct-LLM, planning, reactive, memory-based, and oracle
baselines.

## Literature-Inspired Adapters

After the v0 baselines work, add adapters inspired by adjacent city-agent
systems. These do not need to be full reproductions at first. They can be
faithful lightweight policies that expose the same CityIntent action interface.

| Priority | Adapter | Source inspiration | CityIntent role |
|---|---|---|---|
| P1 | CitySimStyleValueAgent | CitySim | Needs, long-term goals, value-driven activity planning, spatial memory, POI choice |
| P1 | GATSimStyleMobilityAgent | GATSim | Mobility-focused schedule adaptation and travel behavior realism |
| P1 | ConcordiaStyleComponentAgent | Concordia | Component-based agent state plus game-master-style environment mediation |
| P2 | CityEQAStyleHierarchicalAgent | CityEQA | Hierarchical planner / manager / actor pattern for embodied-city tasks |
| P2 | OpenCityScaleAgent | OpenCity / MobileCity | Efficient large-population activity simulation, useful after micro-benchmark validation |

The P1 adapters are most useful because they touch CityIntent's core: intention,
memory, movement, and environment validation. The P2 adapters are valuable later
when we add embodied perception or scale.

## What Each Agent Must Expose

Every agent should implement the same episode contract:

```text
initialize(persona, private_goal, known_world, memory_seed)
observe(public_state, local_observation, messages, last_action_result)
propose_action() -> typed action + optional rationale
update(action_result, new_observation)
```

The environment, not the agent, owns truth:

- map connectivity
- travel time
- POI opening hours
- prices and budgets
- capacity and crowding
- co-presence
- successful or failed meetings
- hidden perturbations

This keeps "will" and "world" separate: the agent can intend, but the city
decides what is possible.

## Suggested V0 Experimental Matrix

Use a compact matrix first:

```text
7 agent policies
x 20-30 scenario packages
x 3 seeds per scenario
x 1 strong LLM
```

Then add a second matrix for model sensitivity:

```text
3 representative policies
x 20-30 scenario packages
x 3 base models
```

Recommended representative policies for the model-sensitivity run:

- LLMDirectActor
- LLMReactiveReplanner
- GenerativeAgentMemoryAgent

This keeps cost manageable while showing whether architecture effects survive
model changes.

## Metrics

CityIntent should combine deterministic metrics and judge-based metrics.

Deterministic metrics:

- goal completion
- feasibility violation rate
- travel-time consistency
- budget consistency
- opening-hour consistency
- perturbation recovery
- route efficiency
- co-presence / meeting success

Judge-based or rubric-based metrics:

- intentional consistency
- believable routine
- social appropriateness
- relationship maintenance
- explanation-action alignment

The key benchmark claim should not depend only on LLM judges. Spatial and
temporal validity must be computed directly from the environment trace.

## Opportunity

The clearest opportunity is not "make a larger city simulation." CitySim,
GATSim, AgentSociety, OpenCity, and MobileCity are already moving in that
direction.

Our stronger angle is:

> CityIntent evaluates whether an agent's private intention remains stable,
> adaptive, and spatially feasible when the city pushes back.

SOTOPIA showed that dynamic interaction exposes failures hidden by static
benchmarks. CityIntent can extend that lesson from dialogue to urban agency, and
go one step further by comparing the architectures that make agency possible.

## Immediate Next Step

The first benchmark smoke package now lives at
`benchmarks/cityintent_v0/`. It defines the toy world, scenario package format,
eight seed scenarios, and a dependency-free validator.

The next implementation step is to implement the P0 agent interface and run the
toy world with these scenarios:

1. lunch meeting under time pressure
2. commute disruption
3. closed POI and replacement choice
4. conflicting private goal and social obligation
5. low-budget errand chain
6. avoid-crowd preference during public event
7. memory-dependent place choice
8. unexpected friend encounter

If the seven P0 agents behave differently on these scenarios, CityIntent has a
real benchmark signal.
