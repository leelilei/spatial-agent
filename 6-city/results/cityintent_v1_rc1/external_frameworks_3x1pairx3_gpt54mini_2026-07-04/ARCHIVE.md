# CityIntent Repeated Experiment Archive

Timestamp: 2026-07-04T11:21:15+08:00

## Config

```json
{
  "benchmark": "cityintent_v0",
  "benchmark_version": "1.0-rc1",
  "benchmark_status": "release_candidate_pending_human_audit",
  "script": "D:\\0-Research\\6-city\\benchmarks\\cityintent_v0\\tools\\run_repeated_experiment.py",
  "repeats": 3,
  "agents": [
    "gatsim_official_planner",
    "generative_agents_official_planner",
    "agentsociety_official_plan_blocks"
  ],
  "scenario_ids": [
    "paired_study_a",
    "paired_study_b"
  ],
  "limit_scenarios": null,
  "llm_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54mini.json",
  "judge_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54mini.json",
  "output_dir": "6-city\\results\\cityintent_v1_rc1\\external_frameworks_3x1pairx3_gpt54mini_2026-07-04",
  "skip_existing": true,
  "judge_sleep": 0.0,
  "skip_judge": false,
  "timestamp": "2026-07-04T11:21:15+08:00",
  "updated_at": "2026-07-04T11:21:15+08:00"
}
```

## Completed Runs

| Repeat | Traces | Judged | Traces dir | Judged dir |
|---:|---:|---:|---|---|
| 1 | 6 | 6 | `6-city\results\cityintent_v1_rc1\external_frameworks_3x1pairx3_gpt54mini_2026-07-04\repeat_01\traces` | `6-city\results\cityintent_v1_rc1\external_frameworks_3x1pairx3_gpt54mini_2026-07-04\repeat_01\judged` |
| 2 | 6 | 6 | `6-city\results\cityintent_v1_rc1\external_frameworks_3x1pairx3_gpt54mini_2026-07-04\repeat_02\traces` | `6-city\results\cityintent_v1_rc1\external_frameworks_3x1pairx3_gpt54mini_2026-07-04\repeat_02\judged` |
| 3 | 6 | 6 | `6-city\results\cityintent_v1_rc1\external_frameworks_3x1pairx3_gpt54mini_2026-07-04\repeat_03\traces` | `6-city\results\cityintent_v1_rc1\external_frameworks_3x1pairx3_gpt54mini_2026-07-04\repeat_03\judged` |

## Derived Files

- row count: 18
- `repeated_summary.md`
- `all_runs.csv`
- `agent_repeated_summary.csv`
- `scenario_agent_repeated_summary.csv`
- `failure_taxonomy_summary.csv`
- `manifest.json`
- `run_config.json`
- `runs.json`
