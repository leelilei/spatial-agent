# Novelty audit: capacity-aware kernel selection

## Search scope

Targeted OpenAlex discovery covered frozen visual foundation models, transfer-based few-shot learning, strong embedding baselines, transformer capacity, register tokens, feature fusion, and multiple-kernel learning. OpenAlex integrates Crossref and arXiv metadata. Semantic Scholar, Scopus, Web of Science, and the academic-search MCP were unavailable, so this is not exhaustive.

## Closest work and boundary

| Work | Overlap | Boundary |
|---|---|---|
| Wang et al., *SimpleShot* (2019), arXiv:1911.04623 | Simple normalized frozen features and nearest classifiers | DCKS studies capacity-specific RBF kernels and nested task-local selection |
| Tian et al., *A Good Embedding Is All You Need?* (ECCV 2020), doi:10.1007/978-3-030-58568-6_16 | Embedding quality dominates FSL | Supports the paper question; prevents claiming the observation as new |
| Hu et al., *Pushing the Limits of Simple Pipelines for FSL* (CVPR 2022), doi:10.1109/CVPR52688.2022.00886 | External pretraining, transformers, and simple pipelines | DCKS focuses on 200-way fine-grained tasks, kernel geometry, and class risk |
| Oquab et al., *DINOv2* (2023), arXiv:2304.07193 | General frozen visual features | Backbone source, not method novelty |
| Classical multiple-kernel learning | Convex combinations of heterogeneous kernels | DCKS cannot claim new MKL theory; contribution is its leakage-controlled task-local use and empirical analysis |

## Permitted claim

If confirmation succeeds, the paper may claim a reproducible task-local kernel-selection pipeline and controlled evidence about capacity scaling in few-shot fine-grained recognition. It may not claim invention of kernel fusion or foundation-model benchmarking.
