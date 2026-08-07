# Scope

- Project: capacity-aware frozen-foundation few-shot fine-grained recognition
- Mode: hybrid
- Text type: EI-conference empirical paper with a simple method
- Target reader: applied computer-vision reviewer
- Language: Chinese planning documents; English manuscript later
- Deliverable scope: foundation files, novelty audit, proposal, frozen DCKS protocol, reproducible code
- Desired version: executable internal draft
- Constraints: CUB official train only during development; no retroactive thresholds; standard `SVC.predict`; second dataset required before final evaluation
- Vault access allowed: yes
- Archive after confirmation: yes

## Strategic change

The paper no longer depends on keypoints or a novel neural adapter. It studies frozen visual
foundation-model capacity and proposes task-local Dual-Capacity Kernel Selection (DCKS),
which chooses or fuses DINOv2-B/L kernels using only inner OOF predictions.
