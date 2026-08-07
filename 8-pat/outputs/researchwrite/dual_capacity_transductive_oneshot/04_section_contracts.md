# Section contracts

## Introduction

- Purpose: motivate 200-way one-shot prototype bias.
- Allowed: three-episode CUB facts and label-efficiency motivation.
- Forbidden: SOTA, first-method, and deployment claims.

## Method

- Purpose: define feature normalization, concatenation, Sinkhorn, and three updates.
- Required: equations, known balanced prior, all frozen constants, zero query-label use.
- Forbidden: describing established components as inventions.

## Experiments

- Required: B/L/BL inductive arms, no-refinement arm, single-capacity refinement,
  TIM, LaplacianShot, PT-MAP-family, DCCR ablation, second dataset, imbalance stress.
- Forbidden: selecting hyperparameters on confirmation labels.
- Status: all required experiment families completed; Dogs uses CUB-frozen constants.

## Discussion

- Required: balanced-prior limitation and simple-combination positioning.
- Forbidden: generalization beyond tested datasets.
- Required conclusion: competitive accuracy--efficiency, not accuracy SOTA.
