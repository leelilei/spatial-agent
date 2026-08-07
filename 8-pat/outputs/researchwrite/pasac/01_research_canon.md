# Research canon

## Locked observations

1. Architecture-matched PrPool-K0 reaches 69.33% mean OOF BA over three CUB 10-shot episodes.
2. Random-K1 reaches 69.73%; its mean gain over K0 is +0.40pp and its class-bootstrap 95% interval crosses zero.
3. Full-keypoint Oracle reaches 70.43%; its mean gain over K0 is +1.10pp.
4. Therefore, direct sparse auxiliary supervision is not a sufficient paper contribution.
5. Official CUB test and CCT Cis/Trans access counters remain zero.

## Hypothesis

K0 already discovers classification-useful regions, but its 15 part channels have no stable semantic identity. Fixed-channel sparse supervision creates identity mismatch, while unconstrained fine-tuning can damage K0 classification features. Fold-local one-to-one semantic assignment plus frozen-teacher preservation should improve semantic localization without material classification loss.

## Falsifiers

- Hungarian assignments are unstable or no better than identity on held-out attention hit rate.
- PASAC fails both frozen screening branches.
- Gains disappear across episodes 2–3.
- Improvements require accessing unselected keypoints, OOF keypoints during training, or official test data.

## Claims allowed after the first screen

- Gate passes: PASAC is promising on one frozen CUB development episode; it is not yet validated.
- Gate fails: permutation-aware sparse calibration is unsupported under the fixed protocol.
- No result permits a general SOTA or “first ever” claim.

