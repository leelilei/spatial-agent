#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 OUTPUT_DIR" >&2
  exit 2
fi

output_dir="$1"
mkdir -p "$output_dir"
images="$output_dir/eccv_18_all_images_sm.tar.gz"
splits="$output_dir/eccv_18_annotations.tar.gz"
keypoints="$output_dir/keypoints_cct20plus.csv"

curl --location --fail --retry 8 --retry-all-errors --continue-at - \
  "https://storage.googleapis.com/public-datasets-lila/caltechcameratraps/eccv_18_all_images_sm.tar.gz" \
  --output "$images"
curl --location --fail --retry 8 --retry-all-errors --continue-at - \
  "https://storage.googleapis.com/public-datasets-lila/caltechcameratraps/eccv_18_annotations.tar.gz" \
  --output "$splits"
curl --location --fail --retry 8 --retry-all-errors \
  "https://raw.githubusercontent.com/ac-rodriguez/privilegedpooling/main/data/keypoints_cct20plus.csv" \
  --output "$keypoints"

(
  cd "$output_dir"
  printf '%s  %s\n' \
    "8143c17aa2a12872b66f284ff211531f" \
    "eccv_18_all_images_sm.tar.gz" \
    "66a1f481b44aa1edadf75c9cfbd27aba" \
    "eccv_18_annotations.tar.gz" \
    | md5sum --check -
)

python - "$keypoints" <<'PY'
import csv
import sys

path = sys.argv[1]
with open(path, newline="") as handle:
    rows = list(csv.DictReader(handle))
if len(rows) != 1233:
    raise SystemExit(f"Expected current upstream CSV to contain 1233 rows, got {len(rows)}")
if len({row["image_id"] for row in rows}) != len(rows):
    raise SystemExit("Upstream keypoint CSV contains duplicate image IDs")
print("CCT20+ archives and current 1233-row keypoint CSV verified")
PY
