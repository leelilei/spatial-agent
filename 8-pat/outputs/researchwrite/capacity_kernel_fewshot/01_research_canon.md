# Research canon

## Literature facts

1. SimpleShot and *A Good Embedding Is All You Need?* established that representation quality and simple classifiers can rival complex few-shot methods.
2. PMF showed that external pretraining and transformer capacity strongly affect few-shot performance (Hu et al., CVPR 2022, doi:10.1109/CVPR52688.2022.00886).
3. DINOv2 provides general-purpose frozen visual features (Oquab et al., 2023, arXiv:2304.07193).
4. Multiple-kernel learning and heterogeneous feature fusion are established; DCKS cannot claim invention of kernel fusion.
5. Register tokens address high-norm ViT feature-map artifacts, primarily for dense processing; they are a later benchmark factor, not the first screen (Darcet et al., 2023, arXiv:2309.16588).

## Experimental facts

1. DINOv2-B/14 CLS + RBF SVC reaches 86.20%, 86.85%, and 85.90% on CUB train-only episodes 1--3, mean 86.32%.
2. RBF consistently exceeds Ridge, prototypes, local heuristics, and tested adapters on the same B features.
3. Patch-based keypoint mechanisms and part pooling do not exceed CLS RBF.
4. Official CUB test and CCT Cis/Trans access counts remain zero.

## Model facts

1. DINOv2-B/14 uses a 768-dimensional CLS feature; DINOv2-L/14 uses 1024 dimensions.
2. Both backbones accept the same deterministic 392x392 direct-resize inputs.
3. A convex sum of positive-semidefinite B/L RBF kernels is positive-semidefinite; a weighted geometric product of RBF kernels is also a valid RBF kernel on weighted concatenated distances.
4. The server has 12 GB GPU memory, 31 GB RAM, 52 GB free disk, and the local DINOv2 hub source; L weights are not yet cached.

## Constraints

1. Episode 1 is development; episodes 2/3 are confirmation only after a frozen Go.
2. DCKS kernel-bank selection occurs inside each outer fold using only its training rows and their original fold groups.
3. Outer labels cannot choose backbone, kernel family, or weight.
4. A paper-route Go does not imply a new algorithm claim; it unlocks confirmation and manuscript construction.

## Terminology

- DCKS: Dual-Capacity Kernel Selection over B-only, L-only, additive, and geometric B/L RBF kernels.
- Task-local selection: the kernel mode is selected from inner OOF predictions available within a new task's labeled support data.
- Route Go: evidence sufficient to continue the empirical paper, distinct from claiming DCKS beats every single backbone.

## Forbidden claims

- First multiple-kernel learner, first foundation-model few-shot study, or state of the art.
- DINOv2-L scaling as a novel method.
- Any official-test result before train-only multi-episode and second-dataset gates.
- Hiding endpoint selections when DCKS chooses L-only.

## Unresolved claims

1. Whether L improves B by at least 1pp under the locked CUB protocol.
2. Whether B/L errors are complementary enough for mixed kernels to beat L-only.
3. Whether task-local selection is stable across episodes and a second fine-grained dataset.
