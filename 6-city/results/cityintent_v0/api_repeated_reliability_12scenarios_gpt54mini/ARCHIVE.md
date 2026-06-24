# CityIntent Repeated Experiment Archive

Timestamp: 2026-06-24T00:17:04

## Config

```json
{
  "benchmark": "cityintent_v0",
  "script": "D:\\0-Research\\6-city\\benchmarks\\cityintent_v0\\tools\\run_repeated_experiment.py",
  "repeats": 3,
  "agents": [
    "utility_planner",
    "api_llm_direct_actor",
    "api_llm_plan_then_act",
    "api_llm_reactive_replanner"
  ],
  "scenario_ids": [],
  "limit_scenarios": null,
  "llm_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54mini.json",
  "output_dir": "6-city\\results\\cityintent_v0\\api_repeated_reliability_12scenarios_gpt54mini",
  "skip_existing": true,
  "judge_sleep": 0.0,
  "timestamp": "2026-06-24T00:17:04"
}
```

## Completed Runs

| Repeat | Traces | Judged | Traces dir | Judged dir |
|---:|---:|---:|---|---|
| 1 | 48 | 48 | `6-city\results\cityintent_v0\api_repeated_reliability_12scenarios_gpt54mini\repeat_01\traces` | `6-city\results\cityintent_v0\api_repeated_reliability_12scenarios_gpt54mini\repeat_01\judged` |
| 2 | 48 | 48 | `6-city\results\cityintent_v0\api_repeated_reliability_12scenarios_gpt54mini\repeat_02\traces` | `6-city\results\cityintent_v0\api_repeated_reliability_12scenarios_gpt54mini\repeat_02\judged` |
| 3 | 48 | 48 | `6-city\results\cityintent_v0\api_repeated_reliability_12scenarios_gpt54mini\repeat_03\traces` | `6-city\results\cityintent_v0\api_repeated_reliability_12scenarios_gpt54mini\repeat_03\judged` |

## Derived Files

- row count: 144
- `repeated_summary.md`
- `all_runs.csv`
- `agent_repeated_summary.csv`
- `scenario_agent_repeated_summary.csv`
- `failure_taxonomy_summary.csv`
- `manifest.json`
- `run_config.json`
- `runs.json`
