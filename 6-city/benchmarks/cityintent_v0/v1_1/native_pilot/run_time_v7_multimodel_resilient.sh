#!/bin/bash
# Resume-safe Yunwu calibration for the three deconfounded time-v7 items.
set -u

V0_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PILOT_ROOT="$V0_ROOT/v1_1/native_pilot"
RESULT_ROOT="$V0_ROOT/../../results/cityintent_v1_1_candidate"
CITYINTENT_PYTHON="${CITYINTENT_PYTHON:-python}"
RUNNER="$V0_ROOT/tools/run_baseline_traces.py"
BENCHMARK="$PILOT_ROOT/time_v7/public_matrix/benchmark_config.json"
AGENTS=api_llm_react_tool_policy,api_llm_plan_and_execute
SCENARIOS=ci11n_time7_metro_radial_v1_v0,ci11n_time7_suburb_polycentric_v1_v1,ci11n_time7_harbor_grid_v1_v2
RUN_TAG=native_time_v7_public_2x3x1_2026-08-04

[ -n "${DEEPSEEK_API_KEY:-}" ] || { echo "DEEPSEEK_API_KEY MISSING"; exit 1; }

run_model() {
  name="$1"
  config="$2"
  output="$RESULT_ROOT/${RUN_TAG}_${name}"
  for attempt in $(seq 1 20); do
    if [ -f "$output/run_manifest.json" ] && [ "$(jq -r '.status' "$output/run_manifest.json")" = "complete" ]; then
      echo "$name COMPLETE"
      return 0
    fi
    echo "$name attempt $attempt"
    if [ -f "$output/traces.json" ]; then
      "$CITYINTENT_PYTHON" "$RUNNER" --benchmark-config "$BENCHMARK" --agents "$AGENTS" \
        --llm-config "$config" --scenario-ids "$SCENARIOS" --results-dir "$output" --resume && true
    else
      "$CITYINTENT_PYTHON" "$RUNNER" --benchmark-config "$BENCHMARK" --agents "$AGENTS" \
        --llm-config "$config" --scenario-ids "$SCENARIOS" --results-dir "$output" && true
    fi
    sleep 15
  done
  return 1
}

run_model claude "$V0_ROOT/configs/yunwu_claude_sonnet45_20250929.json" || exit 1
run_model qwen "$V0_ROOT/configs/yunwu_qwen3_235b_a22b_instruct_2507.json" || exit 1
run_model deepseek "$V0_ROOT/configs/yunwu_deepseek_v4flash.json" || exit 1
