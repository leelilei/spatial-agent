# Evidence table

| Claim | Evidence/source | Strength | Usable section | Risk | Status |
|---|---|---|---|---|---|
| Naive sparse keypoint supervision has weak isolated value | PAT-D-260728-010: K1-K0 +0.40pp, Full-K0 +1.10pp | Direct, architecture-matched local evidence | Motivation | Limited to old PrPool/ResNet mechanism | evidence-backed |
| Frozen DINOv2 CLS + RBF is the mandatory reference | PAT-H-003/005/006: 86.20/86.85/85.90% | Direct three-episode local evidence | Baselines, gates | Train-only episodes, no official test | evidence-backed |
| Class-specific sparse DINO anchors are insufficient | PAT-H-260729-001: best local arm below CLS-Ridge and later RBF | Direct local evidence | Excluded routes | Different detector and aggregation from current proposal | evidence-backed |
| Training-only keypoint attention can improve sample efficiency | Rodriguez et al., TPAMI 2023 | Primary peer-reviewed source | Related work, rationale | Does not prove benefit with DINO or this protocol | evidence-backed |
| Pose-normalized parts can help few-shot FG recognition | Tang et al., CVPR 2020 | Primary peer-reviewed source | Rationale | Their localization and episode setting differ | evidence-backed |
| Label-only part discovery is established | PDiscoNet 2023; PDiscoFormer 2024 | Primary peer-reviewed sources | Novelty boundary | Full-text comparison still needed | evidence-backed |
| DINO tokens contain enough semantic structure for a linear part detector | DINOv2/SalViT literature plus current cache motivation | Indirect | Hypothesis only | Not established on this CUB split | hypothesis |
| Full semantic queries improve BA over K0 | PAT-I-260729-001: 85.50% vs 80.90%, +4.60pp | Direct five-fold OOF local evidence | Results | K0 is weak uniform pooling | evidence-backed |
| Full semantic queries improve BA over CLS RBF | PAT-I-260729-001: 85.50% vs 86.20%, -0.70pp | Direct five-fold OOF local evidence | Results, stopping decision | Central claim is falsified on episode 1 | evidence-backed |
| Full detector localizes held-out semantic parts | PAT-I-260729-001: 19,904/24,020 3x3-token hits, 82.86% | Direct held-out OOF mechanism evidence | Results | Not standard PCK and K0 argmax is a trivial baseline | evidence-backed |
| K1 retains a useful fraction of the Full-query gain | Not tested because Full failed the strong-baseline gate | Stopped by protocol | Forbidden | No experiment may be run under current route | unsupported |
