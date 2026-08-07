#!/bin/bash
# Resume-safe public-only Wave-3 smoke over one event-ordering scenario.
set -u

V0_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
PILOT_ROOT="$V0_ROOT/v1_1/native_pilot"
RESULT_ROOT="$V0_ROOT/../../results/cityintent_v1_1_candidate"
CITYINTENT_PYTHON="${CITYINTENT_PYTHON:-python}"
RUNNER="$V0_ROOT/tools/run_baseline_traces.py"
BENCHMARK="$PILOT_ROOT/expansion_wave3/benchmark_config.json"
AGENTS=api_llm_react_tool_policy,api_llm_plan_and_execute
SCENARIO=ci11w3_soci_harbor_grid_v1_v1
RUN_DATE=2026-08-05

[ -n "${DEEPSEEK_API_KEY:-}" ] || { echo "DEEPSEEK_API_KEY MISSING"; exit 1; }

run_model() {
  name="$1"
  config="$2"
  output="$RESULT_ROOT/native_wave3_public_smoke_2x1x1_${RUN_DATE}_${name}"
  for attempt in $(seq 1 20); do
    if [ -f "$output/run_manifest.json" ] && [ "$(jq -r '.status' "$output/run_manifest.json")" = "complete" ]; then
      echo "$name COMPLETE"
      return 0
    fi
    echo "$name attempt $attempt"
    resume_flag=
    [ -f "$output/traces.json" ] && resume_flag=--resume
    "$CITYINTENT_PYTHON" "$RUNNER" \
      --benchmark-config "$BENCHMARK" \
      --agents "$AGENTS" \
      --llm-config "$config" \
      --scenario-ids "$SCENARIO" \
      --results-dir "$output" \
      $resume_flag && true
    sleep 10
  done
  echo "$name INCOMPLETE"
  return 1
}

run_model claude "$V0_ROOT/configs/yunwu_claude_sonnet45_20250929.json" || exit 1
run_model qwen "$V0_ROOT/configs/yunwu_qwen3_235b_a22b_instruct_2507.json" || exit 1
run_model deepseek "$V0_ROOT/configs/yunwu_deepseek_v4flash.json" || exit 1
