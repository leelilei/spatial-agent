# CityIntent v0 Repeated Reliability Experiment

Date: 2026-06-23

Purpose:

> Produce the first real CityAgency benchmark table with repeated API runs,
> deterministic city validation, second-pass plausibility judging, and
> mean/std reporting.

## Run

Command:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_repeated_experiment.py ^
  --repeats 3 ^
  --agents utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --output-dir 6-city/results/cityintent_v0/api_repeated_reliability_gpt54mini ^
  --skip-existing
```

Output:

- `6-city/results/cityintent_v0/api_repeated_reliability_gpt54mini/repeated_summary.md`
- `6-city/results/cityintent_v0/api_repeated_reliability_gpt54mini/all_runs.csv`
- `6-city/results/cityintent_v0/api_repeated_reliability_gpt54mini/agent_repeated_summary.csv`
- `6-city/results/cityintent_v0/api_repeated_reliability_gpt54mini/scenario_agent_repeated_summary.csv`
- `6-city/results/cityintent_v0/api_repeated_reliability_gpt54mini/failure_taxonomy_summary.csv`

Design:

- 8 scenarios
- 4 agents
- 3 repeats
- 96 judged scenario-agent traces

## Main Agent Table

Each cell is mean +/- sample standard deviation across judged scenario traces.

| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 24 | 0.921 +/- 0.168 | 0.930 +/- 0.108 | 0.914 +/- 0.179 | 1.000 +/- 0.000 | 0.835 +/- 0.111 | 0.513 +/- 0.236 | 0.322 +/- 0.165 | 0.070 +/- 0.108 |
| `api_llm_plan_then_act` | 24 | 0.963 +/- 0.105 | 0.958 +/- 0.141 | 0.931 +/- 0.190 | 1.000 +/- 0.000 | 0.930 +/- 0.060 | 0.846 +/- 0.165 | 0.085 +/- 0.111 | 0.042 +/- 0.141 |
| `api_llm_reactive_replanner` | 24 | 0.938 +/- 0.169 | 0.875 +/- 0.338 | 0.875 +/- 0.338 | 0.000 +/- 0.000 | 0.898 +/- 0.120 | 0.813 +/- 0.219 | 0.087 +/- 0.109 | 0.125 +/- 0.338 |
| `utility_planner` | 24 | 0.906 +/- 0.178 | 0.875 +/- 0.338 | 0.844 +/- 0.336 | 0.000 +/- 0.000 | 0.820 +/- 0.153 | 0.619 +/- 0.260 | 0.202 +/- 0.178 | 0.125 +/- 0.338 |

## Diagnostic Table

| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 0.806 +/- 0.270 | 0.917 +/- 0.282 | 0.750 +/- 0.452 | 0.167 +/- 0.381 | 0.042 +/- 0.204 |
| `api_llm_plan_then_act` | 0.865 +/- 0.255 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_reactive_replanner` | 0.911 +/- 0.241 | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `utility_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.750 +/- 0.452 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Highest Gap Rows

The largest face-believability gaps are concentrated in direct-action and
premature-completion failures:

| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility |
|---|---|---:|---:|---:|---:|
| `avoid_crowd_event` | `api_llm_direct_actor` | 0.453 +/- 0.342 | 0.360 +/- 0.338 | 1.000 +/- 0.000 | 0.933 +/- 0.115 |
| `unexpected_friend_encounter` | `api_llm_direct_actor` | 0.453 +/- 0.081 | 0.180 +/- 0.100 | 0.650 +/- 0.173 | 0.875 +/- 0.125 |
| `budget_errand_chain` | `api_llm_direct_actor` | 0.423 +/- 0.040 | 0.367 +/- 0.046 | 1.000 +/- 0.000 | 0.783 +/- 0.029 |
| `unexpected_friend_encounter` | `utility_planner` | 0.420 +/- 0.183 | 0.227 +/- 0.092 | 0.750 +/- 0.000 | 1.000 +/- 0.000 |
| `commute_disruption` | `utility_planner` | 0.343 +/- 0.257 | 0.343 +/- 0.091 | 0.500 +/- 0.000 | 0.000 +/- 0.000 |

## Failure Taxonomy

| Agent | Failure | Count | Rate/trace |
|---|---|---:|---:|
| `api_llm_direct_actor` | `done_state_loop` | 4 | 0.167 |
| `api_llm_direct_actor` | `goal_drift` | 2 | 0.083 |
| `api_llm_direct_actor` | `money_budget_failure` | 2 | 0.083 |
| `api_llm_direct_actor` | `social_derailment` | 1 | 0.042 |
| `api_llm_plan_then_act` | `closed_place_action` | 2 | 0.083 |
| `api_llm_reactive_replanner` | `impossible_route` | 3 | 0.125 |
| `utility_planner` | `impossible_route` | 3 | 0.125 |

## Interpretation

This is the first table that looks like a benchmark result rather than a demo.
The main conclusion is:

> Direct next-action agents can retain high goal completion and acceptable
> deterministic feasibility, while still producing much less believable urban
> traces.

`api_llm_direct_actor` is the clearest example. It has 0.921 goal completion and
0.930 trace feasibility, but only 0.513 trace believability and the largest
face-believability gap, 0.322. This is a meaningful CityAgency signal: ordinary
goal metrics would make the agent look usable, while the benchmark exposes
done-state loops, drift, budget failures, and socially derailed traces.

`api_llm_plan_then_act` is strongest in this run. It has the best goal,
feasibility, and believability balance, with the lowest face-believability gap.
For the paper story, this suggests that explicit episode-level planning helps
convert plausible local actions into coherent traces.

`api_llm_reactive_replanner` is more complicated. It looks believable to the LLM
judge, but repeatedly fails the deterministic commute-disruption route check.
This is useful: it shows why CityAgency cannot rely only on LLM plausibility
judgment. The deterministic city validator catches route impossibility that a
language judge may overlook when the narrative sounds reasonable.

## Caveats

1. This is still a small v0 benchmark: 8 scenarios and 3 repeats.
2. The judge and actor use the same configured provider, so judge independence
   is limited.
3. `replanning_success` is defined only on disruption-style scenarios; it should
   be reported carefully as conditional rather than universal ability.
4. The reactive replanner needs trace-level debugging on `commute_disruption`
   before we can claim it is robust.

## Next Step

The next experiment should not just increase repeats. It should add targeted
scenario pressure:

- more disruption cases with blocked paths and replacement routes;
- more social-interruption cases where private goals compete with salient
  encounters;
- more time-window cases where waiting looks plausible but misses the actual
  objective;
- a small human-coded judge set for calibrating trace believability.
