# CityAgency Results Ledger

This file is the canonical experiment ledger for `6-city`, following the same
role as `5-Telephone/RESULTS.md`.

Raw and derived experiment outputs live under:

```text
6-city/results/
```

Human-readable experiment notes live under:

```text
6-city/docs/experiments/
```

## Archive Standard

Each repeated experiment directory should contain:

- `run_config.json`: command-level configuration and timestamp
- `runs.json`: one row per repeat with trace/judge artifact locations
- `manifest.json`: metrics, scenario/agent set, row count, and run records
- `repeated_summary.md`: paper-facing table
- `all_runs.csv`: one row per repeat/scenario/agent
- `agent_repeated_summary.csv`: agent-level mean/std table
- `scenario_agent_repeated_summary.csv`: scenario-agent diagnostics
- `failure_taxonomy_summary.csv`: aggregated failure counts
- `repeat_XX/traces/`: first-pass city trace outputs
- `repeat_XX/judged/`: second-pass plausibility judge outputs

Single-run or smoke experiments should still keep:

- the exact command in a `docs/experiments/*.md` note
- result tables under `6-city/results/`
- enough raw JSON/CSV artifacts to rerun the analysis

## Experiment Ledger

| Date | Experiment | Result dir | Note | Status |
|---|---|---|---|---|
| 2026-06-22 | API smoke and early hard cases | `results/cityintent_v0/api_smoke_gpt54mini/`, `results/cityintent_v0/api_hard_gpt54mini/`, `results/cityintent_v0/api_all_gpt54mini/` | `docs/experiments/cityintent_v0_api_smoke_2026-06-22.md` | Archived note; early runner outputs |
| 2026-06-23 | Architecture gap, 8 scenarios | `results/cityintent_v0/api_architecture_gap_gpt54mini/` | `docs/experiments/cityintent_v0_architecture_gap_2026-06-23.md` | Archived |
| 2026-06-23 | Plausibility judge v2, 8 scenarios | `results/cityintent_v0/api_architecture_gap_gpt54mini_judged_v2/` | `docs/experiments/cityintent_v0_plausibility_judge_2026-06-23.md` | Archived |
| 2026-06-23 | Repeated reliability, 8 scenarios, 3 repeats | `results/cityintent_v0/api_repeated_reliability_gpt54mini/` | `docs/experiments/cityintent_v0_repeated_reliability_2026-06-23.md` | Archived; rerun metadata refreshed after archive-standard upgrade |
| 2026-06-23 | Pressure scenario smoke, 4 new scenarios | `results/cityintent_v0/pressure_scenarios_smoke_gpt54mini/` | `docs/experiments/cityintent_v0_pressure_scenarios_2026-06-23.md` | Archived; rerun metadata refreshed after archive-standard upgrade |
| 2026-06-23 | Full reliability table, 12 scenarios, 3 repeats | `results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/` | `docs/experiments/cityintent_v0_full_12scenario_table_2026-06-23.md` | Archived |

## Next Pending Result

Next recommended result: cross-model or human-calibrated judge audit for the
12-scenario table.
