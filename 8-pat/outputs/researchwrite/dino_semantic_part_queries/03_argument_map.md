# Argument map

## Scientific tension

- What is known: DINOv2 CLS already gives a strong 86.32% three-episode mean, while generic adaptation and post-hoc local corrections fail.
- What is unknown: whether semantic keypoints can reorganize frozen patch evidence into a more discriminative representation without adapting the backbone.
- Why the gap matters: without a positive architecture-matched keypoint upper bound over the strong DINO baseline, sparse annotation selection has no defensible causal target.

## Central research question

Can fold-training semantic keypoints supervise a cross-class detector over frozen DINOv2 patch tokens that improves held-out few-shot fine-grained classification beyond both uniform part pooling and CLS-only RBF?

## Central thesis

The project should continue only if semantic supervision yields a held-out localization gain and a classification gain under the same frozen token cache and classifier family. Otherwise, DINO already contains the useful information in CLS and keypoint budgeting is not a viable paper route in this setup.

## Supporting arguments

### Argument 1
- Claim: the previous keypoint story failed because architecture effects dominated.
- Evidence: PAT-D-260728-010 architecture-matched K0/K1/Full comparison.
- Limitation: it does not exclude a different use of keypoints with foundation-model tokens.

### Argument 2
- Claim: cross-class semantic supervision is distinct from one class-specific anchor per part.
- Evidence: PAT-H-001 used one selected class anchor and no learned global semantic detector.
- Limitation: both approaches still depend on DINO patch semantics and may fail for the same reason.

### Argument 3
- Claim: a Full oracle gate is required before sparse-budget or active-selection work.
- Evidence: all prior selector and safety mechanisms lacked a strong architecture-matched causal ceiling.
- Limitation: a one-episode oracle pass would still require untouched episodes and a second dataset.

## Counterarguments / alternative explanations

1. The linear detector may improve localization but not classification because CLS already integrates the relevant parts.
2. Any gain may come from adding mean-patch features rather than semantic supervision; K0 uniform pooling controls this.
3. Full-keypoint fitting may exploit CUB-specific landmark definitions and fail to transfer.
4. Direct-resize geometry may make localization easier than realistic augmented training.

## Final move

Run one frozen episode 1 Full-oracle screen. Pass requires joint localization and classification evidence. Failure stops the route without K1 tuning; success unlocks a separately preregistered sparse-budget study.
