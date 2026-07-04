# CityIntent Agent Evaluation Plan

Date: 2026-06-22
Updated: 2026-07-04

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

## Verified External Adapters

The project has moved beyond style-only placeholder policies. Four adapters now
pin and verify official source files and commits, preserve identifiable official
prompt/control surfaces, and map their proposed decisions into the same typed
CityIntent executor. They remain adapted decision layers rather than native
end-to-end framework backends.

| Adapter | Pinned source surface | Integration role |
|---|---|---|
| GATSim | Daily mobility planning and schedule-update prompts | Mobility plan generation and disruption update |
| SOTOPIA | `LLMAgent` per-turn private-goal action prompt | Direct observation-to-action social policy |
| Generative Agents | Daily planning, reflection, and schedule revision prompts | Memory/reflection-oriented planning policy |
| AgentSociety | TPB guidance, detailed plan, and mobility place-analysis blocks | Structured plan-block policy |

Every archived trace records repository, commit, verified files, integration
level, provider/model metadata, prompt hashes, call success, latency, and token
usage. Results must be described as evidence about these adapted decision layers,
not the complete native systems.

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

## Current Experimental Status

Four complementary external-adapter matrices are complete:

```text
4 verified adapted decision layers
x 4 pressure scenarios
x 3 real-provider repeats
x 1 fixed agent model (gpt-5.4-mini)
= 48 traces
```

```text
4 verified adapted decision layers
x all 12 current scenarios
x 1 real-provider run
x 1 fixed agent model (gpt-5.4-mini)
= 48 breadth traces
```

The breadth matrix reuses repeat 1 for the four overlapping pressure scenarios,
and a matched 16-trace `gpt-5.4` agent-model screen is also complete. The archive
therefore contains 136 trace records and 120 unique agent executions after adding
a 24-trace matched perturbation screen. All traces
have deterministic evidence scores. Two soft evaluators, `gpt-5.4-mini` and
`gpt-5.4`, independently judged every matrix. The experiments find no
universal winner, persistent architecture-specific failure signatures, and only
moderate cross-judge agreement.

The next automatic matrices should be prioritized as:

1. repeat matched perturbation cells with joint-success reversals, prioritizing the study-place pair;
2. repeat model-sensitivity cells whose architecture ranking reversed;
3. repeat selected broad-scenario cells whose first run changes the architecture ranking;
4. only then scale repeats beyond three for cells with unstable outcomes.

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

Scenario breadth, model sensitivity, and the first matched perturbation screen are
complete. The paired screen holds all non-event scenario fields fixed and finds
architecture-specific feasibility loss under network, facility, and social
events. The strongest next step is targeted repetition of high-information paired
cells, especially the study-place closure and adapters whose joint success drops
from control to treatment. This tests whether the observed event effects survive
provider sampling before expanding the pair library.

The separate human-validation task should proceed in parallel. It calibrates the
construct and soft evidence rubric; it should not delay scenario breadth or model-
sensitivity experiments, but v1 cannot be frozen without it.
