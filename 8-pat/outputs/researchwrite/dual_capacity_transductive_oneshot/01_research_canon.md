# Research canon

## Hard experimental facts

1. The 200-way 10-shot DINOv2-B RBF baseline is about 86.3%, leaving little room.
2. In 200-way 1-shot, BL nearest support averages 68.17% over three train-only episodes.
3. Frozen DCTPR averages 74.85%, a +6.68pp gain over BL nearest support.
4. DCTPR exceeds the strongest implemented paired comparator by +1.30pp, +1.27pp,
   and +1.43pp across Episodes 1--3.
5. On matched CUB features, TIM-ADM reaches 76.19%; DCTPR is 1.35pp lower but
   about 3.8x faster and exceeds MAP/PT-MAP and LaplacianShot arms.
6. On three disjoint Stanford Dogs episodes, DCTPR reaches 70.36%, gains 6.27pp
   over BL nearest support, trails MAP-RAW by 0.61pp, and is about 49x faster.
7. DCTPR is positive versus BL nearest support in all 30 Dogs rotations.
8. Under imbalanced CUB queries, uniform-prior DCTPR falls to 68.34--68.86%;
   oracle counts recover 72.87--73.35%.
9. DCCR failed its gate and is not an active method.
10. A locked official-test audit was completed on 2026-08-05 after all method
    and baseline constants were frozen. It used 2,000 unique CUB test images
    and 3,600 unique Stanford Dogs test images; no test label selected a value.
11. A preregistered SAGE ensemble confirmation on three untouched Dogs episodes
    improved over the strongest single solver by only +0.0617pp and failed its
    +0.10pp primary gate; it is closed and is not a paper claim.
12. DCPR closed 46.6% of the unknown-prior oracle gap and transferred at about
    +0.966pp over TIM, but its development gain was +0.9644pp against a frozen
    +1.0pp gate; it is closed and is not a paper claim.

## Literature facts

1. TIM, LaplacianShot, and PT-MAP-family methods establish strong transductive
   few-shot baselines.
2. Balanced query marginals can materially simplify transductive inference and
   may be unrealistic outside benchmark episodes.
3. Feature ensembles and prototype refinement are established ideas; novelty
   must be claimed at the scoped combination/evaluation level only.

## Forbidden claims

- State of the art before published-baseline reproduction.
- First use of Sinkhorn, prototype refinement, transduction, or backbone fusion.
- Robustness to unknown query priors from balanced CUB episodes.
- Paper-level GO before a second dataset.

## Resolved boundaries

1. DCTPR does not beat TIM-ADM on CUB and must not claim accuracy SOTA.
2. The gain transfers to Stanford Dogs under a completely frozen method.
3. Uniform-prior DCTPR is not robust to query imbalance; this is a measured limitation.

## Remaining risks

1. Published baselines are matched reimplementations on DINO features, not executions
   of the authors' legacy end-to-end repositories.
2. Exact balance is a substantive task assumption.
3. Statistical intervals across support rotations are descriptive because rotations
   share episode images.
4. No accuracy-SOTA result has been confirmed; the SAGE confirmation is a No-Go.
5. PAT-K-005/008 use a custom 200-way stress protocol and cannot be compared
   numerically with the public 5-way Dirichlet benchmark.
6. The locked audit reduces protocol risk but does not turn matched feature-level
   reimplementations into full legacy-pipeline reproductions.

## Locked official-test audit (PAT-K-260805-009)

1. CUB official test: BL-NCC 67.95%, DCTPR 74.64%, TIM-ADM 76.18%; DCTPR
   gains 6.69pp over BL-NCC and trails the strongest matched solver by 1.53pp.
2. Stanford Dogs official test (three disjoint episodes): BL-NCC 63.56%,
   DCTPR 70.49%, MAP-RAW 71.48%; DCTPR gains 6.92pp over BL-NCC and trails
   the strongest matched solver by 0.99pp.
3. The audit preserves the accuracy--efficiency story but does not establish
   accuracy SOTA. Retuning from official-test labels remains forbidden.
4. B/L feature extraction took 42.2 s for the 2,000-image CUB episode and
   24.7--25.1 s per 1,200-image Dogs episode, with peak allocated GPU memory
   of 0.44 GB (B) and 1.34 GB (L) on an RTX 3080 Ti.
5. Train-only one-factor scans show a non-fragile short update schedule but
   measurable temperature sensitivity; the original tau=0.05 remains frozen.
