---
telephone_index: 50
canonical: true
aliases: []
title: "Simulating Misinformation Propagation in Social Networks using Large Language Models"
category: 05_misinformation_correction
role: close neighbor / fidelity metric
decision: must-cite
doi:
venue: arXiv
year: 2025
source_quality: preprint_or_unresolved
fulltext: assets/papers/fulltext/05_misinformation_correction/50_simulating-misinformation-propagation-in-social-networks-using-large-language-models.fulltext.md
pdf: assets/papers/pdf/05_misinformation_correction/50_simulating-misinformation-propagation-in-social-networks-using-large-language-models.pdf
read_status: deep-read
deep_read_scope: manual-project-deep-read

---

# Simulating Misinformation Propagation in Social Networks using Large Language Models

## Why This Paper Matters For Telephone

This is one of the closest local neighbors because it explicitly uses LLM personas
as synthetic agents to study misinformation propagation through social networks.
It is useful for legitimizing the idea that LLM-agent networks can serve as a
testbed for misinformation dynamics. More importantly, it already uses the
language of factual fidelity and drift: news articles are rewritten through
persona-conditioned nodes, and a QA auditor tracks claim-level degradation across
sequential rewrites.

For Telephone, the paper is a close contrast rather than the same contribution.
It studies content drift through rewrite chains and persona effects; we study a
ground-truthed social update in a memory-bearing agent society and distinguish
what agents hear, say, and finally hold.

## Core Claim / Result

The paper proposes an auditor-node framework where persona-conditioned LLM nodes
rewrite news content as it moves through a network. A QA-based auditor estimates
factual fidelity at each step, using metrics such as a misinformation index and
misinformation propagation rate. Its reported pattern is that some identity- or
ideology-conditioned personas accelerate misinformation, while expert-like
personas preserve factual stability; early distortions can escalate through later
heterogeneous persona interactions.

## Evidence We May Cite

- LLM personas are used as networked social agents for misinformation simulation.
- The paper treats misinformation as a fidelity/degradation process, not merely
  as binary spread.
- It introduces claim-level auditing as a way to track factual drift across
  propagation steps.
- It identifies early distortions as consequential for downstream degradation,
  which resonates with our path-dependent entrenchment result.

## Telephone Bridge

- Fidelity vs reach: This paper already moves beyond reach by measuring factual
  degradation; Telephone moves from rewritten content fidelity to held-belief
  fidelity in a social memory system.
- Speech vs belief: The propagation object here is rewritten text. Telephone adds
  the distinction between conversation utterances and final agent belief.
- Entrenchment / path dependence: The finding that early distortions can escalate
  supports our mechanism language, but our P1-rec result tests timing/breadth
  directly.
- Failed natural lever: Expert personas preserving stability provide a natural
  reason to test authoritative/source-like interventions. Our source condition
  then shows that social authority can change speech without repairing held belief.
- Communication-time collapse analogy: Both papers study inference-time
  degradation through repeated social/agentic reuse of information.
- Measurement / rigor: QA auditing is a useful neighbor for our semantic-judge and
  provenance-style scoring.

## What We Add Beyond This Paper

This paper follows content as it is rewritten through persona-conditioned nodes.
Telephone follows a ground-truthed update through an agent society and measures
the gap between exposure, utterance, and held belief. We also test interventions:
model capability, connectivity, memory, persistent source, and broadcast timing.
The distinctive Telephone contribution is speech-belief dissociation and the
finding that late or narrow correction can be said without becoming collective
belief.

## Draft-Ready Use Sentence

> Recent LLM-agent misinformation simulations track factual drift as content is
> rewritten through persona-conditioned networks; Telephone extends this fidelity
> lens from propagated text to the held beliefs of memory-bearing agents after a
> ground-truthed social update.

## Caveats

- Source-quality issues: currently recorded as arXiv; venue/peer-reviewed status
  should be rechecked before final bibliography.
- Extraction issues: local extraction is usable and unflagged.
- Not our claim: do not cite this as evidence for speech-belief dissociation; it
  does not distinguish uttered content from final held belief.

## Citation Decision

Decision: `must-cite`

Reason: It is a very close LLM-agent misinformation propagation neighbor and
helps make our measurement shift from content drift to held-belief fidelity sharp.
