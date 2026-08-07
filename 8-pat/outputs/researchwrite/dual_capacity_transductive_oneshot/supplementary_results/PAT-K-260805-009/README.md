# PAT-K-260805-009 supplementary experiments

This directory contains the locked official-test audit and one-factor sensitivity
results used in the revised AIPR/SPIE manuscript.

- `FINAL_EVAL_LOCK.json`: immutable protocol, manifest, and code hashes.
- `selection_summary.json`: deterministic official-test manifest construction.
- `cub_official_test_summary.json`: one CUB 200-way test episode, 10 support rotations.
- `dogs_official_test_summary.json`: three disjoint Stanford Dogs 120-way test episodes, 30 support rotations.
- `cub_train_sensitivity_summary.csv/json`: CUB train-only one-factor scan.
- `dogs_train_sensitivity_summary.csv/json`: Dogs train-only one-factor scan.

The official-test manifests use one support and nine queries per class. CUB has
only one episode because its smallest official-test class contains 11 images;
Dogs has three disjoint episodes. All method constants and LaplacianShot values
were frozen before image decoding. Feature extraction and solver timing are
reported separately; the task-head timings exclude the common DINOv2 encoding
cost.
