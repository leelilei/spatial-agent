# CityIntent Repeated Experiment Archive

Timestamp: 2026-07-04T01:04:44+08:00

## Config

```json
{
  "benchmark": "cityintent_v0",
  "benchmark_version": "1.0-rc1",
  "benchmark_status": "release_candidate_pending_human_audit",
  "script": "D:\\0-Research\\6-city\\benchmarks\\cityintent_v0\\tools\\run_repeated_experiment.py",
  "repeats": 1,
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
  "llm_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54.json",
  "judge_config": "6-city\\benchmarks\\cityintent_v0\\configs\\fhl_gpt54mini.json",
  "output_dir": "6-city\\results\\cityintent_v1_rc1\\external_frameworks_4x4x1_gpt54_2026-07-04",
  "skip_existing": true,
  "judge_sleep": 0.0,
  "skip_judge": false,
  "timestamp": "2026-07-04T01:04:44+08:00",
  "updated_at": "2026-07-04T01:04:54+08:00"
}
```

## Completed Runs

| Repeat | Traces | Judged | Traces dir | Judged dir |
|---:|---:|---:|---|---|
| 1 | 16 | 16 | `6-city\results\cityintent_v1_rc1\external_frameworks_4x4x1_gpt54_2026-07-04\repeat_01\traces` | `6-city\results\cityintent_v1_rc1\external_frameworks_4x4x1_gpt54_2026-07-04\repeat_01\judged` |

## Derived Files

- row count: 16
- `repeated_summary.md`
- `all_runs.csv`
- `agent_repeated_summary.csv`
- `scenario_agent_repeated_summary.csv`
- `failure_taxonomy_summary.csv`
- `manifest.json`
- `run_config.json`
- `runs.json`
