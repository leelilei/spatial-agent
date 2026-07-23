#!/bin/bash
# Resilient wrapper for the E2 adapter side: re-invokes the repeated experiment
# with --skip-existing (which resumes completed traces via --resume) until the
# top-level agent_repeated_summary.csv is written, tolerating transient provider
# timeouts that would otherwise abort the whole multi-repeat run. Changes no
# config; pure retry-to-completion.
set -u
cd "$(dirname "$0")/.." || exit 1
source ~/.zshrc 2>/dev/null
[ -n "${FHL_API_KEY:-}" ] || { echo "KEY MISSING"; exit 1; }

OUT=/Users/mac/Documents/6-Research/6-city/results/cityintent_v1_rc1/e3c_easy_luna_6x6easyx3_2026-07-10
SUMMARY="$OUT/agent_repeated_summary.csv"
CFG="$(pwd)/configs/fhl_gpt56luna.json"

# Patient backoff: FHL returns HTTP 503/429 under load, so wait between attempts
# to let capacity recover rather than hammering. --skip-existing/--resume means no
# completed work is lost across attempts.
for attempt in $(seq 1 30); do
  if [ -f "$SUMMARY" ] && [ "$(wc -l < "$SUMMARY")" -gt 2 ]; then
    echo "COMPLETE after $((attempt-1)) attempts"; break
  fi
  echo "=== attempt $attempt ($(date +%H:%M:%S)) ==="
  /opt/anaconda3/bin/python3 tools/run_repeated_experiment.py \
    --agents api_llm_react_tool_policy,api_llm_plan_and_execute,gatsim_official_planner,sotopia_official_llm_agent,generative_agents_official_planner,agentsociety_official_plan_blocks \
    --scenario-ids social_copresence_open_meet,social_copresence_message_gated,social_copresence_event_window,social_copresence_two_party,social_copresence_with_errand,social_copresence_decoy_location \
    --repeats 3 \
    --llm-config "$CFG" \
    --judge-config "$(pwd)/configs/fhl_gpt54mini.json" \
    --skip-existing \
    --output-dir "$OUT" \
    && echo "attempt $attempt ok" || echo "attempt $attempt failed (will resume after backoff)"
  sleep 60
done

if [ -f "$SUMMARY" ] && [ "$(wc -l < "$SUMMARY")" -gt 2 ]; then
  echo "FINAL: agent_repeated_summary.csv present"; exit 0
else
  echo "FINAL: still incomplete after retries"; exit 1
fi
