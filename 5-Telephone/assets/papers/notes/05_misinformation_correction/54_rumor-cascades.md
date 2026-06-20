---
telephone_index: 54
canonical: true
aliases: []
title: "Rumor Cascades"
category: 05_misinformation_correction
role: rumor dynamics / correction in cascades
decision: cite
doi: 10.1609/icwsm.v8i1.14559
venue: "Proceedings of the International AAAI Conference on Web and Social Media"
year: 2014
source_quality: article_pdf_layout_caution
fulltext: assets/papers/fulltext/05_misinformation_correction/54_rumor-cascades.fulltext.md
pdf: assets/papers/pdf/05_misinformation_correction/54_rumor-cascades.pdf
read_status: deep-read
deep_read_scope: manual-project-deep-read

---

# Rumor Cascades

## Why This Paper Matters For Telephone

This paper gives us concrete language for rumor propagation over social networks:
truth value, cascade depth, external correction links, deletion, continuing
propagation, and variant competition. It is useful background for explaining why
we care about the structure of social transmission, not merely individual model
accuracy.

## Core Claim / Result

The paper tracks thousands of Facebook rumors matched to Snopes.com and studies
how rumors of different truth values spread. It reports that rumor cascades run
deeper than reshare cascades in general, that Snopes-linked comments can increase
the likelihood of deletion, but that large cascades may continue propagating even
while accumulating many correction comments. It also shows that rumors mutate over
time, with different variants dominating different popularity bursts.

## Evidence We May Cite

- Rumor diffusion can be traced as cascades across a social network.
- Truth value and correction resources can be incorporated into propagation
  analysis.
- Correction signals can affect individual resharing/deletion while not stopping
  large cascades.
- Rumor variants mutate and compete over time.

## Telephone Bridge

- Fidelity vs reach: Rumor cascades demonstrate that diffusion paths and truth
  value are separate analytic dimensions.
- Speech vs belief: The paper studies public resharing/deletion, not internal
  belief. Telephone adds the held-belief endpoint.
- Entrenchment / path dependence: Variant dominance across bursts supports the
  idea that versions can compete and one can become socially dominant.
- Failed natural lever: Snopes comments increasing deletion but not necessarily
  halting large cascades is a human-network analog to source speech not fully
  repairing collective held belief.
- Measurement / rigor: Useful for motivating trace-level version tracking.

## What We Add Beyond This Paper

Rumor Cascades studies human social-media cascades and visible propagation
events. Telephone studies a controlled LLM-agent society where the true update,
interaction traces, and final held answers are all observable. This lets us test
not only whether correction appears in the stream, but whether it becomes the
society's final belief.

## Draft-Ready Use Sentence

> Rumor-cascade studies show that corrective references can coexist with ongoing
> propagation and variant competition; Telephone probes the analogous internal
> question in LLM-agent societies: which version becomes the held belief after
> social exchange?

## Caveats

- Source-quality issues: DOI and venue are resolved.
- Extraction issues: abstract has layout noise; use fulltext/PDF for exact
  wording.
- Not our claim: the paper does not measure mental belief or LLM-agent memory.

## Citation Decision

Decision: `cite`

Reason: Valuable mechanism background, but secondary to Belief Echoes and Science
fake-news framing.
