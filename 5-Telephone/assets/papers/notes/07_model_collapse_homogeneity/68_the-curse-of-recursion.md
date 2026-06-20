---
telephone_index: 68
canonical: true
aliases: [9]
title: "The Curse of Recursion"
category: 07_model_collapse_homogeneity
role: model-collapse analogy
decision: must-cite
doi:
venue: arXiv
year: 2023
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/07_model_collapse_homogeneity/68_the-curse-of-recursion.fulltext.md
pdf: assets/papers/pdf/07_model_collapse_homogeneity/68_the-curse-of-recursion.pdf
read_status: deep-read
deep_read_scope: manual-project-deep-read

---

# The Curse of Recursion

## Why This Paper Matters For Telephone

This is the core model-collapse analogy for our framing. The paper studies what
happens when models are trained recursively on model-generated data. The key
phenomenon is degradation through reuse: the learned distribution loses parts of
the original data distribution, especially tails, and the process can become
irreversible.

Telephone should cite this carefully as an analogy, not as the same mechanism. We
study inference-time social exchange, not training-time recursive data ingestion.

## Core Claim / Result

The paper argues that training on model-generated content causes model collapse:
models lose information about the true underlying distribution, with tail events
disappearing over generations. It presents theoretical intuition and empirical
examples across generative model families, including language models.

## Evidence We May Cite

- Recursive use of generated content can degrade future model behavior.
- Collapse involves loss of distributional support/diversity, not merely random
  noise.
- Access to genuine human-produced data is framed as crucial for avoiding
  collapse.
- The collapse metaphor is established in the context of synthetic data and
  recursive training.

## Telephone Bridge

- Fidelity vs reach: Model collapse is about fidelity to the original data
  distribution; Telephone is about fidelity to a current social fact.
- Speech vs belief: Not addressed directly.
- Entrenchment / path dependence: Recursive training shows how early/generated
  distributions shape later generations; Telephone shows an inference-time social
  analog where an early broad version dominates later belief.
- Communication-time collapse analogy: This is the main contrast. Our degradation
  happens during communication among agents, not model training.
- Measurement / rigor: Warns us to state analogy boundaries explicitly.

## What We Add Beyond This Paper

The Curse of Recursion concerns data pipelines and learned model distributions.
Telephone concerns agent societies at inference time: agents talk, retrieve,
remember, and are probed for held belief. Our result is not that models collapse
from synthetic data, but that social exchange can collapse a fact into the stale
version even when the current truth enters the conversation.

## Draft-Ready Use Sentence

> Model-collapse work shows that recursive reuse of generated data can erase
> parts of an original distribution; Telephone studies a communication-time analog
> in which recursive social exchange causes a current fact to lose the competition
> against an entrenched stale version.

## Caveats

- Source-quality issues: local metadata uses arXiv title; final Nature citation
  should be verified if we cite the published version.
- Extraction issues: local fulltext is usable and unflagged.
- Not our claim: do not say our experiment demonstrates training-time model
  collapse.

## Citation Decision

Decision: `must-cite`

Reason: It anchors the model-collapse analogy, one of the paper's main framing
hooks.
