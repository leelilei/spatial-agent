# CityIntent Repeated Experiment Archive

Timestamp: 2026-07-06T20:21:49+08:00

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
    "sotopia_official_llm_agent",
    "generative_agents_official_planner",
    "agentsociety_official_plan_blocks"
  ],
  "scenario_ids": [
    "social_copresence_open_meet",
    "social_copresence_message_gated",
    "social_copresence_event_window",
    "social_copresence_two_party",
    "social_copresence_with_errand",
    "social_copresence_decoy_location"
  ],
  "limit_scenarios": null,
  "llm_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54mini.json",
  "judge_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54mini.json",
  "output_dir": "6-city\\results\\cityintent_v1_rc1\\external_frameworks_4x6socialx1_gpt54mini_2026-07-06",
  "skip_existing": true,
  "judge_sleep": 0.0,
  "skip_judge": false,
  "timestamp": "2026-07-06T20:21:49+08:00",
  "updated_at": "2026-07-06T20:36:26+08:00"
}
```

## Completed Runs

| Repeat | Traces | Judged | Traces dir | Judged dir |
|---:|---:|---:|---|---|
| 1 | 24 | 24 | `6-city\results\cityintent_v1_rc1\external_frameworks_4x6socialx1_gpt54mini_2026-07-06\repeat_01\traces` | `6-city\results\cityintent_v1_rc1\external_frameworks_4x6socialx1_gpt54mini_2026-07-06\repeat_01\judged` |
| 2 | 24 | 24 | `6-city\results\cityintent_v1_rc1\external_frameworks_4x6socialx1_gpt54mini_2026-07-06\repeat_02\traces` | `6-city\results\cityintent_v1_rc1\external_frameworks_4x6socialx1_gpt54mini_2026-07-06\repeat_02\judged` |
| 3 | 24 | 24 | `6-city\results\cityintent_v1_rc1\external_frameworks_4x6socialx1_gpt54mini_2026-07-06\repeat_03\traces` | `6-city\results\cityintent_v1_rc1\external_frameworks_4x6socialx1_gpt54mini_2026-07-06\repeat_03\judged` |

## Derived Files

- row count: 72
- `repeated_summary.md`
- `all_runs.csv`
- `agent_repeated_summary.csv`
- `scenario_agent_repeated_summary.csv`
- `failure_taxonomy_summary.csv`
- `manifest.json`
- `run_config.json`
- `runs.json`
