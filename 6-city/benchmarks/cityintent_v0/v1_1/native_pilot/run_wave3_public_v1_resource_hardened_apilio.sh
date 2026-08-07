#!/bin/bash
set -euo pipefail

V0_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
RESULT_ROOT="$V0_ROOT/../../results/cityintent_v1_1_candidate"
RUNNER="$V0_ROOT/tools/run_baseline_traces.py"
BENCHMARK="$V0_ROOT/v1_1/native_pilot/expansion_wave3/benchmark_config.json"
AGENTS=api_llm_react_tool_policy,api_llm_plan_and_execute
SCENARIO=ci11w3_reso_harbor_grid_v1_v1

[ -n "${APILIO_API_KEY:-}" ] || { echo "APILIO_API_KEY MISSING"; exit 1; }

run_model() {
  name="$1"
  config="$2"
  output="$RESULT_ROOT/native_wave3_public_v1_resource_hardened_2x1x1_2026-08-06_${name}"
  resume_flag=
  [ -f "$output/traces.json" ] && resume_flag=--resume
  python "$RUNNER" --benchmark-config "$BENCHMARK" --agents "$AGENTS" \
    --llm-config "$config" --scenario-ids "$SCENARIO" --results-dir "$output" $resume_flag
}

run_model claude "$V0_ROOT/configs/apilio_claude_sonnet45_20250929.json"
run_model qwen "$V0_ROOT/configs/apilio_qwen3_235b_a22b_instruct_2507.json"
run_model deepseek "$V0_ROOT/configs/apilio_deepseek_v4flash.json"
