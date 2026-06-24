# CityAgency Four-Paper Positioning

Date: 2026-06-23

Purpose:

> Step 1 for the CityAgency push: read the four strongest related-work anchors
> and decide exactly how CityAgency should position itself before adding metrics
> and new agent architectures.

## Short Take

The four papers make the CityAgency story narrower, but stronger.

CityAgency should **not** claim to be the first benchmark for LLM city agents,
human mobility simulation, constraint-aware planning, or infeasibility
detection. Those spaces are already active.

The stronger claim is:

> Existing work evaluates macro mobility realism, travel-plan constraint
> satisfaction, tool-task infeasibility, or executable digital tasks. CityAgency
> evaluates a missing middle: whether plausible city-agent plans become
> executable urban traces under spatial, temporal, budget, POI, disruption, and
> social-interruption constraints.

## Paper 1: MobiSim-Bench

Local fulltext:

- `assets/papers/fulltext/05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.fulltext.md`

### What It Does

MobiSim-Bench evaluates LLM-agent-based human mobility simulation from three
perspectives:

- **Robustness**: can agents complete day-level simulation without execution
  errors?
- **Realism**: do simulated behaviors match real-world mobility data at both
  microscopic intention and macroscopic statistical levels?
- **Responsiveness**: do agents adapt to abnormal environmental changes?

Its benchmark has:

- Daily Mobility Simulation for realism.
- Hurricane Mobility Simulation for responsiveness.
- Real mobility traces and profiles.
- Metrics such as gyration radius, number of visited locations, intention
  sequence, intention proportion, travel change rate, and temporal travel
  distribution.
- A competition setting with 18 teams and hundreds of agent submissions.

### Why It Matters

This is the strongest direct neighbor on the mobility-simulation side. It already
does some things we considered:

- long-horizon mobility simulation
- environment perturbation
- micro intention plus macro statistics
- architecture comparison

### CityAgency Boundary

MobiSim-Bench asks:

> Can LLM agents simulate realistic human mobility over day-level scenarios?

CityAgency should ask:

> Can an individual city agent turn a plausible plan into an executable trace
> while preserving private intent under local city constraints?

The distinction:

| Axis | MobiSim-Bench | CityAgency |
|---|---|---|
| Primary level | mobility simulation benchmark | micro-scenario agency benchmark |
| Main truth source | real-world mobility data | deterministic city environment validator |
| Main output | mobility trajectories and aggregate statistics | typed action traces with failure taxonomy |
| Perturbation | hurricane / environmental change | route blocks, closures, time windows, budget, social interruptions |
| Agency test | intention sequence/proportion and responsiveness | intention persistence, trace feasibility, done-state awareness, social recovery |

## Paper 2: When Plausible Is Not Realistic

Local fulltext:

- `assets/papers/fulltext/05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.fulltext.md`

### What It Does

This paper evaluates whether LLM urban simulators reproduce empirical mobility
patterns or merely generate plausible narratives. It evaluates AgentSociety and
CitySim against real-world mobility data using:

- mobility laws
- temporal rhythms
- network motifs
- semantic activity transitions
- behavioral mobility profiles
- trip-length distributions
- OD flows
- dwell times
- transition dynamics

Its core finding is directly relevant:

> Narrative plausibility does not imply empirical mobility realism.

### Why It Matters

This paper already owns the macro claim:

> plausible LLM urban simulation can be unrealistic.

CityAgency should not repeat that claim at the macro mobility level.

### CityAgency Boundary

This paper says:

> The generated city is not empirically realistic.

CityAgency says:

> One reason such simulations may fail is that agents do not have reliable
> micro-level urban agency. They produce plausible plans but invalid traces.

CityAgency can function as a diagnostic layer beneath their macro validation:

| Macro failure in mobility realism | Micro failure CityAgency can detect |
|---|---|
| unrealistic trip lengths | inefficient or invalid route choices |
| OD flow mismatch | wrong destination selection under goals/constraints |
| dwell-time mismatch | failure to satisfy time windows or activity duration |
| transition dynamics mismatch | done-state loops or poor activity-chain coherence |
| weak behavioral profiles | weak private-intent persistence or persona consistency |

## Paper 3: FeasiGen

Local fulltext:

- `assets/papers/fulltext/06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.fulltext.md`

### What It Does

FeasiGen constructs infeasible tool-using tasks by identifying critical tools
from successful traces and masking them. It evaluates whether agents detect
infeasibility and stop instead of wasting execution.

Key concepts:

- infeasible task construction
- feasibility-aware evaluation
- explicit STOP signal
- False Continue Rate (FCR)
- token cost of early stop vs failed execution
- finding: agents often fail to detect infeasibility; FCR can be high

### Why It Matters

FeasiGen gives CityAgency the right language for impossible traces:

> A benchmark should test not only task success, but whether an agent recognizes
> that success is impossible under current environment constraints.

### CityAgency Boundary

FeasiGen's infeasibility is mostly:

> missing tools / unavailable execution capabilities.

CityAgency's infeasibility is:

> city-world constraints: blocked routes, closed POIs, insufficient budget,
> time-window impossibility, unreachable meetings, and social-task conflict.

Metric to borrow:

- **False Continue Rate** for infeasible city conditions.

CityAgency version:

```text
city_false_continue =
  P(agent continues impossible plan | environment makes current plan infeasible)
```

Examples:

- pharmacy is closed, but agent keeps trying to go there
- transit edge is blocked, but agent keeps traversing it
- remaining time cannot satisfy the meeting, but agent still claims it can
- budget is insufficient, but agent continues a paid errand chain

## Paper 4: ChinaTravel

Local fulltext:

- `assets/papers/fulltext/06_agent_execution_benchmarks/01_ChinaTravel_Shao2024.fulltext.md`

### What It Does

ChinaTravel is an open-ended travel planning benchmark with compositional
constraint validation. It uses:

- a practical travel sandbox
- multi-day, multi-POI planning
- DSL-based feasibility and constraint validation
- human queries with implicit intent
- hard constraints and soft preferences
- neuro-symbolic planning and backtracking

It reports that neuro-symbolic methods improve constraint satisfaction, while
pure LLM methods struggle with complex constraint grounding and compositional
generalization.

### Why It Matters

ChinaTravel is the closest "plausible plan under constraints" benchmark.

It means CityAgency cannot claim:

> We are the first to validate LLM plans against spatial/temporal/budget
> constraints.

### CityAgency Boundary

ChinaTravel asks:

> Can a language agent produce a feasible travel itinerary satisfying open-ended
> user constraints?

CityAgency asks:

> Can a city agent execute a step-by-step trace while maintaining private intent
> and recovering from changing urban/social conditions?

The distinction:

| Axis | ChinaTravel | CityAgency |
|---|---|---|
| Object | itinerary plan | interactive action trace |
| Time | multi-day plan output | simulated episode loop |
| Constraints | travel sandbox and DSL | environment-owned city state |
| Social | mostly user preferences | co-presence, relationship obligations, social derailment |
| State | plan validation | action-by-action state transition and violations |
| Key failure | constraint grounding / satisfaction | plausible plan becoming impossible trace |

## Revised CityAgency Claims

### Claims To Avoid

- "First LLM city-agent benchmark."
- "First benchmark for urban mobility realism."
- "First benchmark for infeasible agent tasks."
- "First benchmark for constraint-aware travel/city planning."

### Claims To Make

1. **Missing middle claim**

   Existing work evaluates macro mobility realism, social intelligence, travel
   planning constraints, or executable tool/app tasks. CityAgency evaluates the
   missing middle: micro-level urban agency through executable city traces.

2. **Plausibility-feasibility gap claim**

   CityAgency measures when plausible city plans and rationales fail under
   deterministic city-world validation.

3. **Architecture diagnosis claim**

   CityAgency compares agent architectures, not only base models, to identify
   which control structures reduce impossible traces.

4. **Micro-to-macro bridge claim**

   CityAgency does not replace mobility-realism benchmarks. It helps explain
   macro realism failures by exposing micro agency failures.

## Metrics To Add In Step 2

Required:

- `trace_feasibility`
- `plan_plausibility`
- `plausibility_feasibility_gap`
- `impossible_trace_rate`
- `city_false_continue`
- `done_state_loop_rate`
- `social_derailment_rate`
- `constraint_violation_breakdown`

Optional later:

- repeated-trial reliability / `pass^k`
- macro hooks: trip distance, dwell, activity-chain transition, OD proxy

## Agent Architectures To Add In Step 3

Priority:

1. `api_llm_plan_then_act`
2. `api_llm_reactive_replanner`

Why:

- FeasiGen suggests planning-stage feasibility detection matters.
- ChinaTravel suggests LLM-only planning benefits from symbolic validation or
  backtracking.
- MobiSim-Bench suggests architecture role matters, not just model strength.

Expected first result:

| Agent | Expected strength | Expected weakness |
|---|---|---|
| `utility_planner` | feasible, cheap, deterministic | less flexible / less socially natural |
| `api_llm_direct_actor` | plausible local actions | impossible traces, goal drift, done-state loops |
| `api_llm_plan_then_act` | better global coherence | brittle when disruptions occur |
| `api_llm_reactive_replanner` | better recovery | may overreact or lose long-term intent |

## Next Implementation Decision

Step 2 should modify the CityIntent v0 runner/scorer so that every result row
contains:

```text
plan_plausibility
trace_feasibility
plausibility_feasibility_gap
impossible_trace_rate
city_false_continue
failure taxonomy counts
```

This can be implemented deterministically first, using agent rationales and
trace outcomes. A real LLM plausibility judge can be added after the first table
exists.

