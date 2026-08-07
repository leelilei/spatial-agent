# Novelty audit, 2026-07-29

OpenAlex fallback search was used because the academic-search MCP was not
mounted. Relevant boundary papers include:

1. Ziko et al., *Laplacian Regularized Few-Shot Learning*, 2020,
   doi:10.48550/arXiv.2006.15486.
2. Boudiaf et al., *Transductive Information Maximization For Few-Shot Learning*,
   2020, doi:10.48550/arXiv.2008.11297.
3. Hu et al., *Leveraging the Feature Distribution in Transfer-based Few-Shot
   Learning*, 2020, doi:10.48550/arXiv.2006.03806.
4. Veilleux et al., *Realistic Evaluation of Transductive Few-Shot Learning*,
   2022, doi:10.48550/arXiv.2204.11181.
5. Zhu and Koniusz, *Transductive Few-shot Learning with Prototype-based Label
   Propagation by Iterative Graph Refinement*, 2023,
   doi:10.48550/arXiv.2304.11598.
6. Tian et al., *Prototypes-oriented Transductive Few-shot Learning with
   Conditional Transport*, 2023, doi:10.48550/arXiv.2308.03047.

Conclusion: neither balanced transport nor iterative prototype refinement is a
defensible standalone novelty claim. DCTPR must be positioned as a scoped
dual-capacity, high-way fine-grained method/evaluation contribution and must be
compared against the listed families.

## Implementation audit update

The matched feature-level implementations were checked against the authors'
public repositories:

- TIM: `mboudiaf/TIM`, official temperature 15, loss weights [0.1, 1.0, 0.1],
  150 TIM-ADM iterations and alpha 1.0.
- LaplacianShot: `imtiazziko/LaplacianShot`, directed kNN argument 3, 20 bound
  updates, and the published lambda grid.
- PT-MAP: `yhu01/PT-MAP`, OT lambda 10, MAP alpha 0.2, and 20 epochs. Because
  DINO CLS features are signed, the power arm explicitly uses a signed square
  root and is labelled an adaptation rather than an official reproduction.

The experiments show that TIM-ADM exceeds DCTPR on CUB, while MAP-RAW narrowly
exceeds it on Stanford Dogs. Therefore the defensible contribution is the
cross-dataset accuracy--efficiency tradeoff and strict prior-boundary audit.
