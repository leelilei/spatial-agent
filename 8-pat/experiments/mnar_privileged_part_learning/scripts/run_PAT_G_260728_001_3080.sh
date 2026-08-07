#!/usr/bin/env bash
set -euo pipefail

project_root="${PAT_PROJECT_ROOT:-/root/workspace/8-pat}"
dataset_root="${CUB_DATASET_ROOT:-/root/workspace/datasets/cub_200_2011}"
work_root="${project_root}/experiments/mnar_privileged_part_learning"
episode_data="${project_root}/raw/experiments/2026.07.28_CUB_EpisodeReliability_PAT-D-260728-009/data"
reference_dir="${project_root}/raw/experiments/2026.07.28_CUB_EpisodeReliability_PAT-D-260728-009/formal"
protocol="${work_root}/configs/PAT-G-260728-001_protocol.json"
runner="${work_root}/scripts/run_cub_permutation_calibration.py"
output_root="${project_root}/runs/PAT-G-260728-001"

if [[ ! -f "${dataset_root}/CUB_200_2011/images.txt" ]]; then
  dataset_archive="${dataset_root}/CUB_200_2011.tgz"
  if [[ ! -f "${dataset_archive}" ]]; then
    bash "${work_root}/scripts/download_cub_parallel.sh" \
      "${dataset_archive}" "${output_root}/download"
  fi
  mkdir -p "${dataset_root}"
  tar -xzf "${dataset_archive}" -C "${dataset_root}"
fi

test -f "${dataset_root}/CUB_200_2011/images.txt"
test -f "${episode_data}/episode_1/cub_train_10shot_manifest.jsonl"
test -f "${episode_data}/episode_1/random_k1_selection.npz"
test -f "${reference_dir}/episode_1_predictions.npz"
test -f "${protocol}"

export PYTHONPATH="${work_root}/scripts${PYTHONPATH:+:${PYTHONPATH}}"
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-8}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-8}"
export CUDA_DEVICE_ORDER=PCI_BUS_ID
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"

mkdir -p "${output_root}/smoke" "${output_root}/formal"

nvidia-smi
python3 - <<'PY'
import scipy
import sklearn
import torch
import torchvision
print({
    "torch": torch.__version__,
    "torchvision": torchvision.__version__,
    "scipy": scipy.__version__,
    "sklearn": sklearn.__version__,
    "cuda": torch.version.cuda,
    "gpu": torch.cuda.get_device_name(0),
    "vram_gib": round(torch.cuda.get_device_properties(0).total_memory / 2**30, 2),
})
assert torch.cuda.is_available()
PY

if python3 -c "import pytest" >/dev/null 2>&1; then
  python3 -m pytest -q \
    "${work_root}/tests/test_permutation_aware_calibration.py"
else
  python3 - <<'PY'
import numpy as np
from permutation_aware_calibration import attention_hit_counts, derive_mapping
targets = np.zeros((2, 3, 5, 5))
attention = np.full((2, 3, 5, 5), -8.0)
locations = ((0, 0), (2, 3), (4, 1))
expected = np.array([2, 0, 1])
for image in range(2):
    for part, (yy, xx) in enumerate(locations):
        targets[image, part, yy, xx] = 1.0
        attention[image, expected[part], yy, xx] = 8.0
actual = derive_mapping(attention, targets)
hits, visible = attention_hit_counts(attention, targets, actual)
assert np.array_equal(actual, expected)
assert hits == visible == 6
print({"fallback_self_test": "PASS", "mapping": actual.tolist()})
PY
fi

python3 "${runner}" \
  --dataset-root "${dataset_root}" \
  --episode-data-dir "${episode_data}" \
  --stored-reference-dir "${reference_dir}" \
  --protocol "${protocol}" \
  --output-dir "${output_root}/smoke" \
  --episodes 1 \
  --smoke 2>&1 | tee "${output_root}/smoke/run.log"

python3 "${runner}" \
  --dataset-root "${dataset_root}" \
  --episode-data-dir "${episode_data}" \
  --stored-reference-dir "${reference_dir}" \
  --protocol "${protocol}" \
  --output-dir "${output_root}/formal" \
  --episodes 1 2>&1 | tee "${output_root}/formal/run.log"

find "${output_root}" -type f ! -name SHA256SUMS -print0 \
  | sort -z \
  | xargs -0 sha256sum > "${output_root}/SHA256SUMS"

python3 - <<PY
import json
from pathlib import Path
p = Path("${output_root}/formal/summary.json")
d = json.loads(p.read_text())
print(json.dumps({
    "experiment_id": d["experiment_id"],
    "overall_gate_pass": d["overall_gate_pass"],
    "official_test_images_decoded_or_encoded": d[
        "official_test_images_decoded_or_encoded"
    ],
    "summary": str(p),
}, indent=2))
PY
