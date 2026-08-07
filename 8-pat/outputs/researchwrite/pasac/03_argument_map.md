# Argument map

1. Full keypoints are costly, but naive sparse supervision has weak isolated value.
2. The strong K0 result shows the architecture already learns useful attention.
3. Those learned channels are permutation-symmetric and lack semantic identities.
4. Sparse annotations are better used to identify existing channels than to relearn attention from scratch.
5. A fold-local Hungarian assignment supplies a one-to-one semantic identity without OOF leakage.
6. Sparse fine-tuning can still disturb a strong K0 classifier.
7. Frozen-teacher logit and attention preservation constrain that disturbance on unannotated images.
8. Therefore PASAC should improve semantic attention hit rate while preserving, and ideally improving, BA.
9. The identity, permutation-only, and PASAC arms separately test steps 5 and 7.

