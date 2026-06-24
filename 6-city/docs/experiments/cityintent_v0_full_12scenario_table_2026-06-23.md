# CityIntent v0 Full 12-Scenario Reliability Table

Date: 2026-06-23

Purpose:

> Produce the first full CityAgency table after expanding the benchmark from 8
> seed scenarios to 12 seed + pressure scenarios.

## Run

Command:

```bash
python 6-city/benchmarks/cityintent_v0/tools/run_repeated_experiment.py ^
  --repeats 3 ^
  --agents utility_planner,api_llm_direct_actor,api_llm_plan_then_act,api_llm_reactive_replanner ^
  --llm-config 6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json ^
  --output-dir 6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini ^
  --skip-existing
```

Output:

- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/repeated_summary.md`
- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/ARCHIVE.md`
- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/run_config.json`
- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/runs.json`
- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/all_runs.csv`
- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/agent_repeated_summary.csv`
- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/scenario_agent_repeated_summary.csv`
- `6-city/results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/failure_taxonomy_summary.csv`

Design:

- 12 scenarios
- 4 agents
- 3 repeats
- 144 judged scenario-agent traces

## Main Agent Table

Each cell is mean +/- sample standard deviation across judged scenario traces.

| Agent | n | Goal | Feasibility | Intention | Replanning | Face plaus. | Trace believ. | Face-believ. gap | Impossible rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 36 | 0.832 +/- 0.233 | 0.873 +/- 0.185 | 0.790 +/- 0.272 | 0.833 +/- 0.408 | 0.805 +/- 0.154 | 0.500 +/- 0.256 | 0.305 +/- 0.169 | 0.127 +/- 0.185 |
| `api_llm_plan_then_act` | 36 | 0.918 +/- 0.141 | 0.906 +/- 0.221 | 0.843 +/- 0.263 | 1.000 +/- 0.000 | 0.903 +/- 0.104 | 0.784 +/- 0.249 | 0.120 +/- 0.192 | 0.094 +/- 0.221 |
| `api_llm_reactive_replanner` | 36 | 0.913 +/- 0.171 | 0.822 +/- 0.379 | 0.799 +/- 0.380 | 0.500 +/- 0.548 | 0.883 +/- 0.102 | 0.718 +/- 0.276 | 0.167 +/- 0.218 | 0.178 +/- 0.379 |
| `utility_planner` | 36 | 0.850 +/- 0.216 | 0.750 +/- 0.439 | 0.713 +/- 0.425 | 0.000 +/- 0.000 | 0.756 +/- 0.197 | 0.508 +/- 0.324 | 0.248 +/- 0.209 | 0.250 +/- 0.439 |

## Diagnostic Table

| Agent | Travel eff. | Budget | Social approp. | Done-loop | Social derailment |
|---|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 0.804 +/- 0.273 | 0.972 +/- 0.167 | 0.667 +/- 0.383 | 0.222 +/- 0.422 | 0.083 +/- 0.280 |
| `api_llm_plan_then_act` | 0.869 +/- 0.238 | 0.917 +/- 0.280 | 0.778 +/- 0.352 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |
| `api_llm_reactive_replanner` | 0.902 +/- 0.229 | 0.972 +/- 0.167 | 0.861 +/- 0.230 | 0.028 +/- 0.167 | 0.000 +/- 0.000 |
| `utility_planner` | 1.000 +/- 0.000 | 1.000 +/- 0.000 | 0.667 +/- 0.383 | 0.000 +/- 0.000 | 0.000 +/- 0.000 |

## Highest Gap Rows

| Scenario | Agent | Face-believ. gap | Trace believ. | Goal | Feasibility |
|---|---|---:|---:|---:|---:|
| `meeting_wait_trap` | `api_llm_direct_actor` | 0.547 +/- 0.110 | 0.227 +/- 0.092 | 0.550 +/- 0.000 | 1.000 +/- 0.000 |
| `unexpected_friend_encounter` | `api_llm_direct_actor` | 0.527 +/- 0.130 | 0.153 +/- 0.031 | 0.450 +/- 0.000 | 0.750 +/- 0.000 |
| `meeting_wait_trap` | `utility_planner` | 0.467 +/- 0.219 | 0.187 +/- 0.162 | 0.800 +/- 0.000 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `api_llm_reactive_replanner` | 0.437 +/- 0.040 | 0.377 +/- 0.038 | 0.700 +/- 0.260 | 1.000 +/- 0.000 |
| `meeting_wait_trap` | `api_llm_plan_then_act` | 0.400 +/- 0.087 | 0.407 +/- 0.121 | 0.700 +/- 0.260 | 1.000 +/- 0.000 |

## Interpretation

The full 12-scenario table strengthens the CityAgency story.

First, `api_llm_direct_actor` still has relatively high hard feasibility
(`0.873`) but very low trace believability (`0.500`) and the largest
face-believability gap (`0.305`). This means direct next-action policies can
look plausible locally while producing globally weak urban agency.

Second, `api_llm_plan_then_act` is the strongest architecture in this full run:
best goal completion, best feasibility among API agents, highest trace
believability, and lowest face-believability gap. This suggests that explicit
episode-level planning is a strong mitigation for plausible-but-unbelievable
traces.

Third, `meeting_wait_trap` becomes the clearest pressure scenario. All agents can
remain physically feasible, but several fail to produce believable completed
coordination behavior. This gives the benchmark a clean way to separate
city-world feasibility from human-like agency.

## Archive Status

This experiment now follows the `5-Telephone`-style archive pattern:

- command/config in `run_config.json`
- repeat-level artifact locations in `runs.json`
- metrics and row count in `manifest.json`
- paper table in `repeated_summary.md`
- raw traces and judged traces under `repeat_XX/`
- human interpretation in this note

## Caveats

1. The same configured provider is used for actor and judge, so judge
   independence is limited.
2. Three repeats are enough for a first full table, but not for a final paper
   confidence estimate.
3. Some pressure scenarios are intentionally adversarial and should be labeled
   as diagnostic, not representative daily mobility.
