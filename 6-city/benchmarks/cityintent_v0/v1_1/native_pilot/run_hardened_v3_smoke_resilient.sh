#!/bin/bash
# Resume-safe calibration for the four hardened-v3 construct templates.
set -u

V0_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PILOT_ROOT="$V0_ROOT/v1_1/native_pilot"
RESULT_ROOT="$V0_ROOT/../../results/cityintent_v1_1_candidate"
PYTHON=/opt/anaconda3/bin/python
RUNNER="$V0_ROOT/tools/run_baseline_traces.py"
BENCHMARK="$PILOT_ROOT/benchmark_config.json"
AGENTS=api_llm_react_tool_policy,api_llm_plan_and_execute
SCENARIOS=ci11n_disr_harbor_grid_v1_v0,ci11n_memo_metro_radial_v1_v0,ci11n_poi__harbor_grid_v1_v0,ci11n_soci_suburb_polycentric_v1_v0
RUN_TAG=native_pilot_hardened_v3_smoke_2x4x1_2026-08-04

[ -n "${DEEPSEEK_API_KEY:-}" ] || { echo "DEEPSEEK_API_KEY MISSING"; exit 1; }

run_model() {
  name="$1"
  config="$2"
  output="$RESULT_ROOT/${RUN_TAG}_${name}"
  for attempt in $(seq 1 30); do
    if [ -f "$output/run_manifest.json" ] && [ "$(jq -r '.status' "$output/run_manifest.json")" = "complete" ]; then
      echo "$name COMPLETE"
      return 0
    fi
    echo "$name attempt $attempt"
    if [ -f "$output/traces.json" ]; then
      "$PYTHON" "$RUNNER" --benchmark-config "$BENCHMARK" --agents "$AGENTS" \
        --llm-config "$config" --scenario-ids "$SCENARIOS" \
        --results-dir "$output" --resume && true
    else
      "$PYTHON" "$RUNNER" --benchmark-config "$BENCHMARK" --agents "$AGENTS" \
        --llm-config "$config" --scenario-ids "$SCENARIOS" \
        --results-dir "$output" && true
    fi
    sleep 30
  done
  echo "$name INCOMPLETE"
  return 1
}

run_model claude "$V0_ROOT/configs/yunwu_claude_sonnet45_20250929.json" || exit 1
run_model qwen "$V0_ROOT/configs/yunwu_qwen3_235b_a22b_instruct_2507.json" || exit 1
run_model deepseek "$V0_ROOT/configs/yunwu_deepseek_v4flash.json" || exit 1
