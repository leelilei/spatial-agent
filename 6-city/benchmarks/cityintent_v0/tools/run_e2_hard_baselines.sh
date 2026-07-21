#!/bin/bash
# E2 baseline side: 2 paper-backed baselines x 6 hard social scenarios x 3 repeats.
# Written 2026-07-09; safe to re-run (--skip-existing resumes).
cd "$(dirname "$0")/.." || exit 1
exec python3 tools/run_repeated_experiment.py \
  --agents api_llm_react_tool_policy,api_llm_plan_and_execute \
  --scenario-ids hard_three_meeting_relay,hard_budget_entangled_meet,hard_deadline_then_meet,hard_stale_plan_override,hard_full_evening_chain,hard_overlapping_windows \
  --repeats 3 \
  --llm-config "$(pwd)/configs/fhl_gpt54mini.json" \
  --judge-config "$(pwd)/configs/fhl_gpt54mini.json" \
  --skip-existing \
  --output-dir /Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/paper_backed_baselines_2x6hardx3_gpt54mini_2026-07-09
