# CityIntent v0 Benchmark Smoke Test

Status: draft, locally validated.

This package is the first runnable CityAgency track. It keeps the `CityIntent`
name because v0 focuses on intention persistence and constraint-sensitive
action. It is not yet a full experiment runner. Its job is to verify that our
proposed benchmark object is concrete enough to support agent comparisons.

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
tools/run_baseline_traces.py
configs/fhl_gpt54mini.json
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

## Baseline Smoke Run

Run deterministic first-pass baselines from the repository root:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_baseline_traces.py
```

Default outputs are written to:

```text
6-city/results/cityintent_v0/baseline_smoke/
```

The current offline runner supports:

- `utility_planner`
- `llm_direct_actor`
- `reactive_replanner`
- `memory_reflection`
- `api_llm_direct_actor` for a real configured provider

Important: the current LLM-named agents are offline architecture proxies. They
do not call external models and should not be reported as real LLM results.
Only `api_llm_direct_actor` calls a model provider.

Small API smoke run:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_baseline_traces.py ^
  --agents utility_planner,api_llm_direct_actor ^
  --scenario-ids closed_poi_replacement,memory_dependent_place_choice ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --results-dir 6-city/results/cityintent_v0/api_smoke_gpt54mini
```

## Next Implementation Step

The next code step is to connect the common agent interface to real policies:

```text
initialize(persona, private_goal, known_world, memory_seed)
observe(public_state, local_observation, messages, last_action_result)
propose_action() -> typed action + optional rationale
update(action_result, new_observation)
```

Then replace the offline proxies with API-backed LLM policies while keeping the
same trace and scoring contract.
