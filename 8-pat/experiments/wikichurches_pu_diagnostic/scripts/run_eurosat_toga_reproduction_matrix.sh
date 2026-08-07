#!/usr/bin/env bash
set -Eeuo pipefail

TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
DATA_ROOT="${DATA_ROOT:-/root/workspace/datasets}"
OUT_DIR="${OUT_DIR:-/root/workspace/results/eurosat_toga_reproduction_20260727/formal}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
NUM_WORKERS="${NUM_WORKERS:-0}"
RUN_TIMEOUT_SECONDS="${RUN_TIMEOUT_SECONDS:-1800}"

mkdir -p "$OUT_DIR/json" "$OUT_DIR/logs" "$OUT_DIR/audit"
cd "$TOGA_DIR"

date -Is > "$OUT_DIR/audit/start_time.txt"
"$PY_BIN" --version > "$OUT_DIR/audit/python_version.txt" 2>&1
"$PY_BIN" -m pip freeze > "$OUT_DIR/audit/pip_freeze.txt"
nvidia-smi -q > "$OUT_DIR/audit/nvidia_smi_q.txt"
sha256sum \
  main.py \
  utils.py \
  datasets/utils.py \
  datasets/eurosat.py \
  datasets/__init__.py \
  configs/eurosat.yaml \
  configs/configs.yaml \
  > "$OUT_DIR/audit/code_sha256.txt"
sha256sum \
  "$DATA_ROOT/eurosat/EuroSAT.zip" \
  "$DATA_ROOT/eurosat/split_zhou_EuroSAT.json" \
  > "$OUT_DIR/audit/data_sha256.txt"

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

printf "seed\tshots\tmethod\tstart\tend\telapsed_seconds\texit_code\n" \
  > "$OUT_DIR/audit/run_status.tsv"

for seed in 1 2 3; do
  for shots in 1 2 4 8 16; do
    for method in tip_adapter_f toga; do
      run_id="${method}_s${shots}_seed${seed}"
      log_path="$OUT_DIR/logs/${run_id}.log"
      json_path="$OUT_DIR/json/${run_id}.json"
      start_iso=$(date -Is)
      start_s=$(date +%s)

      set +e
      timeout "$RUN_TIMEOUT_SECONDS" "$PY_BIN" main.py \
        --config ./configs/eurosat.yaml \
        --root_path "$DATA_ROOT" \
        --shots "$shots" \
        --seed "$seed" \
        --method "$method" \
        --num_workers "$NUM_WORKERS" \
        --wandb_mode disabled \
        --output_json "$json_path" \
        > "$log_path" 2>&1
      run_status=$?
      set -e

      end_s=$(date +%s)
      end_iso=$(date -Is)
      elapsed=$((end_s - start_s))
      printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\n" \
        "$seed" "$shots" "$method" "$start_iso" "$end_iso" "$elapsed" "$run_status" \
        >> "$OUT_DIR/audit/run_status.tsv"

      if [[ "$run_status" -ne 0 || ! -s "$json_path" ]]; then
        echo "Run failed: $run_id (exit=$run_status); see $log_path" >&2
        exit 1
      fi
    done
  done
done

date -Is > "$OUT_DIR/audit/end_time.txt"
"$PY_BIN" "$TOGA_DIR/../aggregate_eurosat_toga_reproduction.py" \
  --json-dir "$OUT_DIR/json" \
  --out-dir "$OUT_DIR/aggregate"

