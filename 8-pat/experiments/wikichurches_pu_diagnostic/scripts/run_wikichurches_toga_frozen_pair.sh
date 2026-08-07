#!/usr/bin/env bash
set -Eeuo pipefail

if [[ "$#" -ne 2 ]]; then
  echo "Usage: $0 SHOTS SEED" >&2
  exit 2
fi

shots="$1"
seed="$2"
case "$shots" in
  1|4|16) ;;
  *) echo "Invalid shots: $shots" >&2; exit 2 ;;
esac
case "$seed" in
  4|5|6) ;;
  *) echo "Invalid fresh confirmation seed: $seed" >&2; exit 2 ;;
esac

TOGA_DIR="${TOGA_DIR:-/root/workspace/TOGA}"
DATA_ROOT="${DATA_ROOT:-/root/workspace/datasets}"
OUT_DIR="${OUT_DIR:-/root/workspace/results/wikichurches_toga_tuning_20260727/frozen_confirmation}"
PY_BIN="${PY_BIN:-/usr/local/miniconda3/envs/py312/bin/python}"
FROZEN_FILE="${FROZEN_FILE:-/root/workspace/wikichurches_toga_frozen_configs.json}"
RUN_TIMEOUT_SECONDS="${RUN_TIMEOUT_SECONDS:-1800}"

mkdir -p \
  "$OUT_DIR/json" \
  "$OUT_DIR/logs" \
  "$OUT_DIR/audit/status_fragments" \
  "$OUT_DIR/audit/locks"

mapfile -t frozen_values < <(
  "$PY_BIN" - "$FROZEN_FILE" "$shots" <<'PY'
import json
import sys

path, shots = sys.argv[1:]
document = json.load(open(path, encoding="utf-8"))
choice = document["selected_by_shot"][shots]
hyperparameters = choice["hyperparameters"]
print(choice["candidate_id"])
for key in (
    "lr",
    "init_delta",
    "lambda_teacher",
    "pooling_ratio",
    "dropout_rate",
    "focal_loss_gamma",
):
    print(hyperparameters[key])
PY
)
if [[ "${#frozen_values[@]}" -ne 7 ]]; then
  echo "Failed to resolve frozen configuration for ${shots}-shot" >&2
  exit 2
fi
candidate_id="${frozen_values[0]}"
lr="${frozen_values[1]}"
init_delta="${frozen_values[2]}"
lambda_teacher="${frozen_values[3]}"
pooling_ratio="${frozen_values[4]}"
dropout_rate="${frozen_values[5]}"
focal_loss_gamma="${frozen_values[6]}"

pair_id="s${shots}_seed${seed}"
lock_dir="$OUT_DIR/audit/locks/${pair_id}.lock"
if ! mkdir "$lock_dir" 2>/dev/null; then
  echo "Pair is already running: $pair_id"
  exit 0
fi
cleanup() {
  rmdir "$lock_dir" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

cd "$TOGA_DIR"
for method in tip_adapter_f toga; do
  run_id="${method}_s${shots}_seed${seed}"
  json_path="$OUT_DIR/json/${run_id}.json"
  log_path="$OUT_DIR/logs/${run_id}.log"
  status_path="$OUT_DIR/audit/status_fragments/${run_id}.tsv"

  if [[ -s "$json_path" ]]; then
    printf "%s\t%s\t%s\t%s\tREUSED\tREUSED\t0\t0\n" \
      "$shots" "$seed" "$method" "$candidate_id" > "$status_path"
    continue
  fi

  start_iso=$(date -Is)
  start_s=$(date +%s)
  command=(
    timeout "$RUN_TIMEOUT_SECONDS" "$PY_BIN" main.py
    --config ./configs/wikichurches.yaml
    --root_path "$DATA_ROOT"
    --shots "$shots"
    --seed "$seed"
    --method "$method"
    --train_epoch 20
    --batch_size 16
    --num_workers 0
    --wandb_mode disabled
    --run_namespace "confirm_${candidate_id}_s${shots}"
    --lr "$lr"
    --output_json "$json_path"
  )
  if [[ "$method" == "toga" ]]; then
    command+=(
      --init_delta "$init_delta"
      --lambda_teacher "$lambda_teacher"
      --pooling_ratio "$pooling_ratio"
      --dropout_rate "$dropout_rate"
      --focal_loss_gamma "$focal_loss_gamma"
    )
  fi

  set +e
  "${command[@]}" > "$log_path" 2>&1
  run_status=$?
  set -e
  end_s=$(date +%s)
  end_iso=$(date -Is)
  elapsed=$((end_s - start_s))
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" \
    "$shots" "$seed" "$method" "$candidate_id" \
    "$start_iso" "$end_iso" "$elapsed" "$run_status" > "$status_path"

  if [[ "$run_status" -ne 0 || ! -s "$json_path" ]]; then
    echo "Run failed: $run_id (exit=$run_status); see $log_path" >&2
    exit 1
  fi
done
