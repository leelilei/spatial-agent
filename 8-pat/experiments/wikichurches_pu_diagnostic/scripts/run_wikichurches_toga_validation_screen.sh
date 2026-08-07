#!/usr/bin/env bash
set -Eeuo pipefail

OUT_DIR="${OUT_DIR:-/root/workspace/results/wikichurches_toga_tuning_20260727/validation_screen}"
TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
CANDIDATE_FILE="${CANDIDATE_FILE:-/root/workspace/wikichurches_toga_validation_candidates.json}"
RUNNER="${RUNNER:-/root/workspace/run_wikichurches_toga_validation_candidate.sh}"
AGGREGATOR="${AGGREGATOR:-/root/workspace/aggregate_wikichurches_toga_validation_screen.py}"
PARALLEL_JOBS="${PARALLEL_JOBS:-6}"

mkdir -p "$OUT_DIR/audit"
date -Is > "$OUT_DIR/audit/start_time.txt"
"$PY_BIN" --version > "$OUT_DIR/audit/python_version.txt" 2>&1
"$PY_BIN" -m pip freeze > "$OUT_DIR/audit/pip_freeze.txt"
nvidia-smi -q > "$OUT_DIR/audit/nvidia_smi_q.txt"
cp "$CANDIDATE_FILE" "$OUT_DIR/audit/candidates.json"
sha256sum \
  "$TOGA_DIR/main.py" \
  "$TOGA_DIR/utils.py" \
  "$TOGA_DIR/datasets/utils.py" \
  "$TOGA_DIR/datasets/wikichurches.py" \
  "$TOGA_DIR/configs/wikichurches.yaml" \
  "$CANDIDATE_FILE" \
  "$RUNNER" \
  "$AGGREGATOR" \
  > "$OUT_DIR/audit/code_sha256.txt"

monitor_pid=""
cleanup() {
  if [[ -n "$monitor_pid" ]]; then
    kill "$monitor_pid" 2>/dev/null || true
  fi
}
trap cleanup EXIT INT TERM
(
  while true; do
    nvidia-smi \
      --query-gpu=timestamp,utilization.gpu,memory.used,power.draw,temperature.gpu \
      --format=csv,noheader,nounits
    sleep 2
  done
) > "$OUT_DIR/audit/gpu.csv" 2>&1 &
monitor_pid=$!

"$PY_BIN" - "$CANDIDATE_FILE" <<'PY' |
import json
import sys

document = json.load(open(sys.argv[1], encoding="utf-8"))
for candidate_id in document["candidates"]:
    for shots in (1, 4, 16):
        for seed in (1, 2, 3):
            print(candidate_id, shots, seed)
PY
xargs -P "$PARALLEL_JOBS" -n 3 "$RUNNER"

printf "candidate_id\tshots\tseed\tstart\tend\telapsed_seconds\texit_code\n" \
  > "$OUT_DIR/audit/run_status.tsv"
sort -t $'\t' -k2,2n -k3,3n -k1,1 \
  "$OUT_DIR"/audit/status_fragments/*.tsv \
  >> "$OUT_DIR/audit/run_status.tsv"

if grep -ERq \
  "Loading visual features and labels from test|Evaluating on the test set|test accuracy" \
  "$OUT_DIR/logs"; then
  echo "Validation screen log contains a test access/evaluation marker." >&2
  exit 1
fi

"$PY_BIN" "$AGGREGATOR" \
  --json-dir "$OUT_DIR/json" \
  --candidate-file "$CANDIDATE_FILE" \
  --out-dir "$OUT_DIR/aggregate"
date -Is > "$OUT_DIR/audit/end_time.txt"
