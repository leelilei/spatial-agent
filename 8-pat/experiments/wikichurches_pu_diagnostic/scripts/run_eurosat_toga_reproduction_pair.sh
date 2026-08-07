#!/usr/bin/env bash
set -Eeuo pipefail

if [[ "$#" -ne 2 ]]; then
  echo "Usage: $0 SEED SHOTS" >&2
  exit 2
fi

seed="$1"
shots="$2"
case "$seed" in
  1|2|3) ;;
  *) echo "Invalid seed: $seed" >&2; exit 2 ;;
esac
case "$shots" in
  1|2|4|8|16) ;;
  *) echo "Invalid shots: $shots" >&2; exit 2 ;;
esac

TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
DATA_ROOT="${DATA_ROOT:-/root/workspace/datasets}"
OUT_DIR="${OUT_DIR:-/root/workspace/results/eurosat_toga_reproduction_20260727/formal}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
NUM_WORKERS="${NUM_WORKERS:-0}"
RUN_TIMEOUT_SECONDS="${RUN_TIMEOUT_SECONDS:-1800}"

mkdir -p \
  "$OUT_DIR/json" \
  "$OUT_DIR/logs" \
  "$OUT_DIR/audit/status_fragments" \
  "$OUT_DIR/audit/locks"
cd "$TOGA_DIR"

lock_dir="$OUT_DIR/audit/locks/seed${seed}_shots${shots}.lock"
if ! mkdir "$lock_dir" 2>/dev/null; then
  echo "Pair is already running elsewhere; skipping: seed=$seed shots=$shots"
  exit 0
fi
cleanup() {
  rmdir "$lock_dir" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

for method in tip_adapter_f toga; do
  run_id="${method}_s${shots}_seed${seed}"
  log_path="$OUT_DIR/logs/${run_id}.log"
  json_path="$OUT_DIR/json/${run_id}.json"
  status_path="$OUT_DIR/audit/status_fragments/${run_id}.tsv"

  if [[ -s "$json_path" ]]; then
    printf "%s\t%s\t%s\tREUSED\tREUSED\t0\t0\n" \
      "$seed" "$shots" "$method" > "$status_path"
    continue
  fi

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
    > "$status_path"

  if [[ "$run_status" -ne 0 || ! -s "$json_path" ]]; then
    echo "Run failed: $run_id (exit=$run_status); see $log_path" >&2
    exit 1
  fi
done
