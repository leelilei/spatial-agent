# CityIntent v0 Benchmark Smoke Test

Status: draft, locally validated.

This package is the first runnable benchmark skeleton for CityIntent. It is not
yet a full experiment runner. Its job is to verify that our proposed benchmark
object is concrete enough to support agent comparisons.

## What This Tests

CityIntent v0 starts with four agent architectures:

| Agent id | Architecture | Purpose |
|---|---|---|
| `utility_planner` | `UtilityPlannerAgent` | Deterministic non-LLM baseline using time, distance, cost, needs, and relationships |
| `llm_direct_actor` | `LLMDirectActor` | SOTOPIA-like direct next-action policy |
| `reactive_replanner` | `ReactiveReplannerAgent` | Observe each step and replan after disruption |
| `memory_reflection` | `MemoryReflectionAgent` | Generative-agent-style memory, reflection, and planning |

The benchmark deliberately does **not** start by evaluating SimCity or CitySim
as full systems. CitySim-style agents can become a later adapter. The first
scientific question is whether different agent architectures behave differently
in the same verifiable city environment.

## Contents

```text
benchmark_config.json        # benchmark-level metrics and agent architecture list
schema/scenario.schema.json  # JSON schema for scenario packages
worlds/micro_city.json       # graph city with POIs, opening hours, prices, and edges
scenarios/*.json             # eight seed scenarios
tools/validate_cityintent_v0.py
```

## Verification

Run from the repository root:

```bash
python 6-city/benchmarks/cityintent_v0/tools/validate_cityintent_v0.py
```

The validator checks:

- world graph connectivity
- location and agent references
- episode time windows
- metric coverage
- scenario coverage
- architecture probes for the four first-test agents
- graph reachability from the primary agent to critical POIs

## Next Implementation Step

The next code step is to implement the common agent interface:

```text
initialize(persona, private_goal, known_world, memory_seed)
observe(public_state, local_observation, messages, last_action_result)
propose_action() -> typed action + optional rationale
update(action_result, new_observation)
```

Then add a trace runner and deterministic scorer that can compare the four
architectures on these eight scenarios.
