# CityIntent v0 Pressure Scenario Expansion

Date: 2026-06-23

Purpose:

> Add targeted pressure scenarios that stress the CityAgency claim: plausible
> local actions can turn into unbelievable or impossible city traces.

This update expands CityIntent v0 from 8 to 12 scenarios.

## Added Scenarios

| Scenario | Family | Pressure type | Intended diagnostic |
|---|---|---|---|
| `detour_commute_midroute_block` | `disruption` | A route becomes blocked after departure but before traversal completes. | Tests whether agents can avoid mid-route impossibility rather than narrating a normal commute. |
| `closed_study_spot_replacement` | `poi_closure` | A preferred quiet place is temporarily closed. | Tests replacement choice, closure awareness, and unnecessary spending. |
| `school_pickup_social_detour` | `social_spatial_tradeoff` | A salient friend invitation competes with a pickup deadline. | Tests whether social interaction derails a private spatial obligation. |
| `meeting_wait_trap` | `time_pressure` | Waiting at a plausible cafe can miss the actual coordination objective. | Tests the difference between plausible waiting and completed co-presence. |

## Smoke Run

Command:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_repeated_experiment.py ^
  --repeats 1 ^
  --agents utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner ^
  --scenario-ids detour_commute_midroute_block,closed_study_spot_replacement,school_pickup_social_detour,meeting_wait_trap ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --output-dir 6-city/results/cityintent_v0/pressure_scenarios_smoke_gpt54mini ^
  --skip-existing
```

Output:

- `6-city/results/cityintent_v0/pressure_scenarios_smoke_gpt54mini/repeated_summary.md`
- `6-city/results/cityintent_v0/pressure_scenarios_smoke_gpt54mini/all_runs.csv`

Design:

- 4 new scenarios
- 4 agents
- 1 repeat
- 16 judged traces

## Agent-Level Smoke Table

| Agent | n | Goal | Feasibility | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 4 | 0.750 +/- 0.196 | 0.844 +/- 0.237 | 0.470 +/- 0.306 | 0.385 +/- 0.216 | 0.156 +/- 0.237 |
| `api_llm_plan_then_act` | 4 | 0.913 +/- 0.103 | 0.938 +/- 0.125 | 0.840 +/- 0.188 | 0.088 +/- 0.130 | 0.062 +/- 0.125 |
| `api_llm_reactive_replanner` | 4 | 0.750 +/- 0.196 | 0.719 +/- 0.483 | 0.600 +/- 0.406 | 0.260 +/- 0.277 | 0.281 +/- 0.483 |
| `utility_planner` | 4 | 0.738 +/- 0.275 | 0.500 +/- 0.577 | 0.465 +/- 0.325 | 0.260 +/- 0.186 | 0.500 +/- 0.577 |

## Highest Gap Rows

| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility | Reading |
|---|---|---:|---:|---:|---:|---|
| `detour_commute_midroute_block` | `api_llm_direct_actor` | 0.580 | 0.160 | 0.650 | 0.875 | The commute sounds locally reasonable but the full route is not believable. |
| `detour_commute_midroute_block` | `api_llm_reactive_replanner` | 0.560 | 0.120 | 0.650 | 0.875 | Replanning architecture still struggles with a mid-route block. |
| `meeting_wait_trap` | `api_llm_direct_actor` | 0.560 | 0.260 | 0.550 | 1.000 | The trace is physically feasible, but waiting does not achieve the meeting. |
| `school_pickup_social_detour` | `utility_planner` | 0.440 | 0.280 | 0.800 | 0.000 | The route objective is handled poorly despite simple utility logic. |
| `meeting_wait_trap` | `api_llm_reactive_replanner` | 0.430 | 0.410 | 0.550 | 1.000 | Feasible action is not the same as believable completed agency. |

## Interpretation

The pressure suite improves the benchmark in two ways.

First, it increases the number of scenario families that reveal the gap between
local plausibility and full-trace believability. `meeting_wait_trap` is the
cleanest example: agents can remain deterministically feasible while still
failing to produce a convincing human-like meeting trace.

Second, it gives the deterministic validator a stronger role. The mid-route
block and school-pickup scenarios create cases where an LLM judge can find the
narrative reasonable, while the city-world validator catches impossible or
invalid traces.

This makes the CityAgency story sharper:

> We need both urban-world validation and human-agency believability judgment;
> either one alone misses important failures.

## Caveats

1. This is a 1-repeat smoke run. The new scenarios should be folded into the
   3-repeat reliability table before being treated as final benchmark evidence.
2. Some new scenarios are intentionally adversarial, so the paper should frame
   them as pressure tests rather than representative daily mobility.
3. `meeting_wait_trap` uses the existing simplified co-presence scorer, so a
   future version should model Ben's movement more explicitly.

## Next Step

Run the full 12-scenario reliability table:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_repeated_experiment.py ^
  --repeats 3 ^
  --agents utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --output-dir 6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini ^
  --skip-existing
```
