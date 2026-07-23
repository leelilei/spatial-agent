# CityIntent Repeated Experiment Archive

Timestamp: 2026-07-23T10:11:59+08:00

## Config

```json
{
  "benchmark": "cityintent_v0",
  "benchmark_version": "1.0-rc1",
  "benchmark_status": "release_candidate_pending_human_audit",
  "script": "/Users/mac/Documents/6-Research/6-city/benchmarks/cityintent_v0/tools/run_repeated_experiment.py",
  "repeats": 3,
  "agents": [
    "api_llm_react_tool_policy",
    "api_llm_plan_and_execute"
  ],
  "scenario_ids": [
    "hard_three_meeting_relay",
    "hard_budget_entangled_meet",
    "hard_deadline_then_meet",
    "hard_stale_plan_override",
    "hard_full_evening_chain",
    "hard_overlapping_windows"
  ],
  "limit_scenarios": null,
  "llm_config": "/Users/mac/Documents/6-Research/6-city/benchmarks/cityintent_v0/configs/fhl_gpt56luna.json",
  "judge_config": "/Users/mac/Documents/6-Research/6-city/benchmarks/cityintent_v0/configs/fhl_gpt54mini.json",
  "output_dir": "/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10",
  "skip_existing": true,
  "judge_sleep": 0.0,
  "skip_judge": false,
  "timestamp": "2026-07-23T10:11:59+08:00",
  "updated_at": "2026-07-23T10:47:58+08:00"
}
```

## Completed Runs

| Repeat | Traces | Judged | Traces dir | Judged dir |
|---:|---:|---:|---|---|
| 1 | 12 | 12 | `/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10/repeat_01/traces` | `/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10/repeat_01/judged` |
| 2 | 12 | 12 | `/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10/repeat_02/traces` | `/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10/repeat_02/judged` |
| 3 | 12 | 12 | `/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10/repeat_03/traces` | `/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3_backbone_luna_2x6hardx3_2026-07-10/repeat_03/judged` |

## Derived Files

- row count: 36
- `repeated_summary.md`
- `all_runs.csv`
- `agent_repeated_summary.csv`
- `scenario_agent_repeated_summary.csv`
- `failure_taxonomy_summary.csv`
- `manifest.json`
- `run_config.json`
- `runs.json`
