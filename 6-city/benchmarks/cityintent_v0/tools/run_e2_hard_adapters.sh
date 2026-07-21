#!/bin/bash
# E2 adapter side: 4 official framework adapters x 6 HARD social scenarios x 3 repeats.
# Run on the checkout machine (needs tmp/external/ verified checkouts).
# Prerequisite: git pull (brings the 6 hard_* scenarios + this script).
# Windows (cmd) equivalent: replace line continuations with ^ and paths with backslashes.
cd "$(dirname "$0")/.." || exit 1
exec python3 tools/run_repeated_experiment.py \
  --agents gatsim_official_planner,sotopia_official_llm_agent,generative_agents_official_planner,agentsociety_official_plan_blocks \
  --scenario-ids hard_three_meeting_relay,hard_budget_entangled_meet,hard_deadline_then_meet,hard_stale_plan_override,hard_full_evening_chain,hard_overlapping_windows \
  --repeats 3 \
  --llm-config "$(pwd)/configs/fhl_gpt54mini.json" \
  --judge-config "$(pwd)/configs/fhl_gpt54mini.json" \
  --skip-existing \
  --output-dir "$(pwd)/../../results/cityintent_v1_rc1/external_frameworks_4x6hardx3_gpt54mini_2026-07-10"
