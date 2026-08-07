# Scope

- Project: DINO semantic part queries for few-shot fine-grained recognition
- Mode: hybrid
- Text type: revised research proposal and executable mechanism gate
- Target reader: project owner and prospective EI-conference reviewers
- Language: Chinese, with stable English method terms
- Deliverable scope: foundation files, novelty audit, current proposal, frozen first protocol
- Desired version: internal executable draft
- Constraints: CUB official train only; official test and CCT Cis/Trans remain locked; architecture-matched controls; no post-hoc gate changes
- Vault access allowed: yes, limited to `/Users/mac/Documents/6-Research/8-pat`
- Archive after confirmation: yes

## Revision boundary

This revision does not revive PASAC, sparse-anchor reranking, active sample selection,
or class-safe post-hoc correction. It tests a distinct prerequisite: whether semantic
keypoint supervision can improve a representation derived from frozen DINOv2 patch
tokens before any sparse-budget or selection claim is made.
