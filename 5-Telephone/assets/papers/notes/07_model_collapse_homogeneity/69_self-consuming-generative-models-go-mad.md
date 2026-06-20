---
telephone_index: 69
canonical: true
aliases: []
title: "Self-Consuming Generative Models Go MAD"
category: 07_model_collapse_homogeneity
role: model-collapse analogy / diversity-quality tradeoff
decision: cite
doi: 10.52591/lxai202312101
venue: "LatinX in AI at Neural Information Processing Systems Conference 2023"
year: 2023
source_quality: conference
fulltext: assets/papers/fulltext/07_model_collapse_homogeneity/69_self-consuming-generative-models-go-mad.fulltext.md
pdf: assets/papers/pdf/07_model_collapse_homogeneity/69_self-consuming-generative-models-go-mad.pdf
read_status: deep-read
deep_read_scope: manual-project-deep-read

---

# Self-Consuming Generative Models Go MAD

## Why This Paper Matters For Telephone

This paper strengthens the model-collapse framing by emphasizing self-consuming
loops and the tradeoff between quality and diversity. It is helpful because
Telephone is not only about wrong answers; it is also about a society converging
onto a low-diversity stale version of reality.

## Core Claim / Result

The paper analyzes autophagous training loops in which generative models are
trained on data produced by previous models. Across scenarios, without enough
fresh real data, future models progressively lose either quality or diversity.
The authors call this condition Model Autophagy Disorder.

## Evidence We May Cite

- Self-consuming loops can degrade generative systems over generations.
- Fresh real data can prevent or reduce degradation; fixed real data may delay but
  not prevent it.
- Biased sampling can trade off quality and diversity, making collapse more subtle
  than a single scalar performance drop.
- Repeated reuse can amplify artifacts.

## Telephone Bridge

- Fidelity vs reach: The paper distinguishes quality and diversity degradation;
  Telephone can analogously distinguish current-truth accuracy from version
  diversity/consensus.
- Speech vs belief: Not directly studied.
- Entrenchment / path dependence: Supports the idea that recursive loops amplify
  earlier artifacts unless fresh grounding enters effectively.
- Communication-time collapse analogy: Our source condition is interesting in
  this light: a fresh truth source exists, but it is not socially integrated into
  held belief unless broadcast early and broadly.
- Measurement / rigor: Helps justify tracking not only mean current count, but
  version distribution and dominance.

## What We Add Beyond This Paper

Go MAD is about training generative models on synthetic data. Telephone is about
inference-time communication among LLM agents. The link is conceptual: recursive
reuse can degrade fidelity and diversity. The difference is mechanistic: our
degradation emerges through social memory, conversation, and belief probing.

## Draft-Ready Use Sentence

> Self-consuming generative loops can progressively reduce quality or diversity
> without sufficient fresh real data; Telephone shows that even when a fresh truth
> source exists, communication dynamics can fail to integrate it into collective
> held belief.

## Caveats

- Source-quality issues: DOI and venue are recorded, but final bibliography should
  decide whether to cite the DOI version or arXiv version.
- Extraction issues: local fulltext is usable and unflagged.
- Not our claim: do not imply LLM-agent conversations are equivalent to training
  on synthetic data.

## Citation Decision

Decision: `cite`

Reason: Strong supporting citation for the collapse analogy and diversity framing,
but secondary to The Curse of Recursion.
