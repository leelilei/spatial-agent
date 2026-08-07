# Evidence table

| Claim | Evidence/source | Strength | Usable section | Risk | Status |
|---|---|---|---|---|---|
| Strong embeddings and simple classifiers are competitive in FSL | SimpleShot; Tian et al. 2020; Hu et al. 2022 | Peer-reviewed/primary literature | Motivation | Mostly standard FSL benchmarks, not CUB-200-way | evidence-backed |
| DINOv2-B + RBF is a stable CUB reference | PAT-H-003/005/006 | Direct three-episode local evidence | Baselines | Train-only episodes | evidence-backed |
| Local/adaptation complexity did not improve B | PAT-H-001--011 and PAT-I-001 | Direct local evidence | Motivation, ablation | Many arms are method-specific | evidence-backed |
| DINOv2-L improves B by >=1pp | PAT-J-260729-001 | Pending | Results | Central scaling hypothesis | unsupported |
| DCKS improves or robustly matches L | PAT-J-260729-001/002 | Pending | Method results | Could collapse to L endpoint | unsupported |
| Findings transfer beyond CUB | Future second-dataset gate | Pending | Generalization | Required for paper credibility | unsupported |
