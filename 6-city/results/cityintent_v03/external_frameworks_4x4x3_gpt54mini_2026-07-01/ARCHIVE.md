# CityIntent Repeated Experiment Archive

Timestamp: 2026-07-01T20:26:33+08:00

## Config

```json
{
  "benchmark": "cityintent_v0",
  "script": "D:\\0-Research\\6-city\\benchmarks\\cityintent_v0\\tools\\run_repeated_experiment.py",
  "repeats": 3,
  "agents": [
    "gatsim_official_planner",
    "sotopia_official_llm_agent",
    "generative_agents_official_planner",
    "agentsociety_official_plan_blocks"
  ],
  "scenario_ids": [
    "detour_commute_midroute_block",
    "closed_study_spot_replacement",
    "school_pickup_social_detour",
    "meeting_wait_trap"
  ],
  "limit_scenarios": null,
  "llm_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54mini.json",
  "output_dir": "6-city\\results\\cityintent_v03\\external_frameworks_4x4x3_gpt54mini_2026-07-01",
  "skip_existing": true,
  "judge_sleep": 0.0,
  "skip_judge": true,
  "timestamp": "2026-07-01T20:26:33+08:00",
  "updated_at": "2026-07-01T21:03:39+08:00"
}
```

## Completed Runs

| Repeat | Traces | Judged | Traces dir | Judged dir |
|---:|---:|---:|---|---|
| 1 | 16 | 0 | `6-city\results\cityintent_v03\external_frameworks_4x4x3_gpt54mini_2026-07-01\repeat_01\traces` | `6-city\results\cityintent_v03\external_frameworks_4x4x3_gpt54mini_2026-07-01\repeat_01\judged` |
| 2 | 16 | 0 | `6-city\results\cityintent_v03\external_frameworks_4x4x3_gpt54mini_2026-07-01\repeat_02\traces` | `6-city\results\cityintent_v03\external_frameworks_4x4x3_gpt54mini_2026-07-01\repeat_02\judged` |
| 3 | 16 | 0 | `6-city\results\cityintent_v03\external_frameworks_4x4x3_gpt54mini_2026-07-01\repeat_03\traces` | `6-city\results\cityintent_v03\external_frameworks_4x4x3_gpt54mini_2026-07-01\repeat_03\judged` |

## Derived Files

- row count: 48
- `repeated_summary.md`
- `all_runs.csv`
- `agent_repeated_summary.csv`
- `scenario_agent_repeated_summary.csv`
- `failure_taxonomy_summary.csv`
- `manifest.json`
- `run_config.json`
- `runs.json`
