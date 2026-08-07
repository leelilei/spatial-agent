# Section contracts

## Section: Motivation and evidence reset

- Purpose: explain why the project is being rebuilt after PAT-H-011.
- Inputs: PAT-D-010, PAT-G-001, PAT-H-001--011.
- Allowed claims: earlier mechanisms failed; a new positive keypoint upper bound is required.
- Forbidden claims: earlier results prove keypoints are useless in general.
- Required evidence: architecture-matched numeric comparisons.
- Validation checklist: every number links to a local report; official-test status stated.

## Section: Related work and novelty boundary

- Purpose: position the candidate against Privileged Pooling, pose normalization, part discovery, transformer patch selection, and keypoint detection.
- Inputs: targeted literature audit.
- Allowed claims: a narrow combination was not found in the targeted search.
- Forbidden claims: first-ever or comprehensive-search language.
- Required evidence: DOI/title-level verified references.
- Validation checklist: each component prior is acknowledged; overlap risks remain explicit.

## Section: Method

- Purpose: specify semantic detector fitting, uniform control, part pooling, and classification.
- Inputs: frozen protocol and code.
- Allowed claims: deterministic architecture and leakage controls.
- Forbidden claims: expected accuracy or safety before results.
- Required evidence: formulas, dimensions, hyperparameters, fold boundaries.
- Validation checklist: no outer-fold keypoint enters detector fitting; standard `SVC.predict` reference retained.

## Section: Mechanism gate

- Purpose: define falsifiable Full-oracle prerequisites.
- Inputs: episode 1 cached features and frozen thresholds.
- Allowed claims: Go/No-Go on one development episode.
- Forbidden claims: cross-episode or cross-dataset validation.
- Required evidence: BA, localization hit rate, class deltas, complete predictions.
- Validation checklist: all conjunctive gates reported without post-hoc changes.

## Section: Conditional roadmap

- Purpose: state what success and failure permit.
- Inputs: gate result.
- Allowed claims: success unlocks a new K1 protocol; failure stops this route.
- Forbidden claims: automatic progression to official test.
- Required evidence: explicit decision tree.
- Validation checklist: episode 4/5, CCT20+, and official test remain locked unless prior gates pass.
