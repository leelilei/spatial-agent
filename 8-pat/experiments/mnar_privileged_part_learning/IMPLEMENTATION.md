# Sparse keypoint active-selection pipeline

> **Status: STOPPED.** `PAT-D-260728-005`, `007`, and `008` failed their
> method gates. `PAT-D-260728-010` then showed that the apparent sparse
> keypoint gain was largely an architecture confound: PrPool-K0/K1/Full
> averaged 69.33/69.73/70.43% BA, so K1−K0 was only +0.40pp and failed the
> frozen isolated-value gate. Do not run the CCT or final stages below.

The implementation is stage-gated. A later stage must not run when its
dependency summary reports a failed gate.

## PAT-D-260728-005

1. `extract_cub_selector_features.py` creates an image-only sanitized manifest
   and frozen ResNet-50 features.
2. `prepare_cub_active_selection.py` freezes Medoid, Boundary,
   Discriminative, and Balanced Annotation Value K1 masks.
3. `run_cub_active_selection.py` runs the smoke and formal CUB screen and
   automatically selects a winner only when the benefit or safety branch
   passes.

## PAT-D-260728-006

`run_cub_active_confirmation.py` compares the frozen winner with Random in
three paired model-seed packs and computes the dual confirmation gate plus
class-bootstrap intervals.

## PAT-E-260728-001

1. `download_cct20plus.sh` resumes and verifies the official 1024px CCT20
   image archive, official split annotations, and the current PrPool keypoint
   CSV.
2. `prepare_cct20plus_manifest.py` records the 1,233-versus-1,182 discrepancy,
   applies the preregistered eligibility rules, and freezes sequence-grouped
   folds.
3. The existing image-only feature extractor is reused on the sanitized CCT
   manifest.
4. `prepare_cct_active_selection.py` freezes the 12.5% per-class Random and
   transferred-winner masks.
5. `run_cct20plus_validation.py` first runs Global versus Full Oracle, then
   allows the three paired selector groups only if the Oracle gain is at least
   2pp.

## PAT-F-260728-001

`create_final_eval_lock.py` refuses to create the immutable lock unless all
four development gates pass, all test counters are zero, and every supplied
artifact can be hashed. `final_eval_control.py` verifies every dependency hash
and provides an atomic one-shot state ledger for final-split adapters. A
second final run is rejected after the state leaves `LOCKED_READY`.

Every formal run must archive its protocol, masks, feature summaries,
predictions, complete log, result report, standard experiment log, and
`SHA256SUMS`.
