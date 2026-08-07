# MNAR privileged part learning

This directory contains the new experiment line started after the WikiChurches
PU/local-fusion route reached its pre-registered stop condition.

## Current scientific question

All training images have target class labels. Keypoints are training-time
privileged annotations available only under a fixed annotation budget. The
current project asks which ordinary images should receive keypoint annotations
to maximize fine-grained recognition benefit while controlling class-level
negative transfer.

## First experiment

`PAT-C-260728-001` is a frozen-feature PartImageNet Seg pilot. It uses the
official complete masks as hidden Oracle, simulates four annotation-selection
mechanisms on train, and keeps the official test split unopened.

The machine-readable protocol is:

`configs/PAT-C-260728-001_protocol.json`

The train-only manifest must be generated and hashed before validation features
can be encoded.

## Execution order

The order is enforced in code:

1. `prepare_train_manifest.py` reads only `train.json`, selects the frozen
   Quadruped classes, and creates crop-aligned 14×14 targets.
2. `extract_clip_features.py` encodes the train manifest with the frozen
   OpenAI QuickGELU ViT-B/16.
3. `finalize_train_manifest.py` freezes MCAR/MAR-X/MNAR-Z/SI-Hard indicators.
4. `select_oracle_hparams.py` performs train-only five-fold OOF selection for
   the Global versus Full-Part Oracle feasibility gate.
5. Only after `selected_oracle_hparams.json` exists may
   `prepare_val_manifest.py` read validation data.
6. `evaluate_oracle_gate.py` evaluates the validation split once across three
   fixed seeds. If mean Oracle gain is below 2 pp, the experiment stops before
   spending compute on missingness corrections.

Every image loader throws on a manifest row whose split is `test`; the official
test split is not extracted for this pilot.

## Current status

The PartImageNet method-development line is stopped after three pre-registered
mechanism gates:

1. `PAT-C-260728-001`: additive local-logit residual failed the one-shot
   validation Oracle gate.
2. `PAT-C-260728-002`: a Privileged-Pooling-inspired frozen patch head failed
   the train-only Oracle and class-safety gates.
3. `PAT-C-260728-003`: adapting the last CLIP visual block strengthened Global
   to 94.5625% OOF BA, while the Full-Part Oracle reached only 94.0625%.

No missingness-correction arm was run, and the test split remained unread and
unencoded. Method work may resume only after reproducing a positive
privileged-part Oracle on a different benchmark.

`PAT-D-260728-001` established a +5.50pp Full-Keypoint Oracle gain on
CUB-200-2011. `PAT-D-260728-002` and `PAT-D-260728-003` did not support the
synthetic MNAR harm hypothesis, so that method line is stopped.

`PAT-D-260728-004` initially appeared to establish a positive premise: one
randomly selected keypoint-annotated image per class retained 71.8% of the
Full-Oracle gain relative to a Global reference. `PAT-D-260728-010` later
showed that this ratio is architecture-confounded and must not be interpreted
as a causal keypoint-annotation effect.

The implemented successor is documented in
[`IMPLEMENTATION.md`](./IMPLEMENTATION.md). It contains:

1. `PAT-D-260728-005`: image-only K1 selector screen;
2. `PAT-D-260728-006`: paired multi-seed confirmation;
3. `PAT-E-260728-001`: CCT20+ grouped cross-dataset validation;
4. `PAT-F-260728-001`: immutable one-time final-evaluation lock.

Every development loader rejects official test rows. Final splits remain
unopened until all four development gates required by the lock have passed.

`PAT-D-260728-005` subsequently rejected all four K1 point-scoring selectors.
`PAT-D-260728-007` then tested the last preregistered active-selection
alternative at K2: exact feature-space and task-gradient facility pairs. The
best arm reached 69.80% OOF BA, only +0.12pp over the Random-K2 mean, while its
negative-transfer rate was 23.0%. Neither dual gate passed. The active-selector
direction is therefore stopped and no CCT/final split has been opened.

`PAT-D-260728-008` then fixed the Random-K1 masks and tested
classification-protective projection of conflicting keypoint gradients.
Conflicts occurred in 76.9% of training batches, but mean BA changed by
−0.07pp and the negative-transfer rate improved by only 0.17pp. Both gates
failed. This gradient-safety mechanism is also stopped; all final splits remain
locked.

`PAT-D-260728-009` finally repeated Global, Random-K1, and Full Oracle on three
independently sampled official-train 10-shot episodes. The complete PrPool arms
were stable, but the audit exposed that Global and PrPool used different
pooling architectures and that fixed nine-epoch Global undertrained relative
to its previously observed median best epoch of 18.

`PAT-D-260728-010` therefore added the missing architecture-matched PrPool-K0
control. K0, K1, and Full Oracle averaged 69.33%, 69.73%, and 70.43% BA. The
isolated K1 gain was only +0.40pp (class-bootstrap 95% interval −0.28 to
+1.10pp), and Full Oracle gained only +1.10pp over K0. Both preregistered gates
failed. The CUB sparse-keypoint direction is stopped; CCT20+, CUB official
test, and CCT Cis/Trans remain locked and unopened.
