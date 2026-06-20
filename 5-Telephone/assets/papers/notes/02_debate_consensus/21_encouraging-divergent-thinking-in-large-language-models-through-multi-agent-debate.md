---
telephone_index: 21
canonical: true
aliases: []
title: "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate"
category: 02_debate_consensus
role: debate diversity / divergent thinking
decision: cite
doi: 10.18653/v1/2024.emnlp-main.992
venue: "Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing"
year: 2024
source_quality: conference
fulltext: assets/papers/fulltext/02_debate_consensus/21_encouraging-divergent-thinking-in-large-language-models-through-multi-agent-debate.fulltext.md
pdf: assets/papers/pdf/02_debate_consensus/21_encouraging-divergent-thinking-in-large-language-models-through-multi-agent-debate.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This is one of the most useful debate papers for our contrast because it diagnoses Degeneration-of-Thought: self-reflection can get stuck once a model is confident. Telephone's path-dependence story is socially distributed, but the family resemblance is strong.

## Core Question

The paper asks how to overcome the tendency of self-reflection to stop producing novel alternatives after an initial confident answer.

## Method / Evidence Base

It proposes multi-agent debate with opposed or tit-for-tat stances and a judge, testing the framework on commonsense machine translation and counterintuitive arithmetic reasoning.

## Core Claim / Result

Multi-agent debate can encourage divergent thinking and outperform self-reflection in the studied tasks, but the authors also find that judge behavior and debate intensity matter. This is an optimistic interaction result with important constraints.

## Evidence We May Cite

- Self-reflection can degenerate when initial confidence locks in a line of thought.
- Multi-agent debate is proposed as a way to reintroduce disagreement and novelty.
- The paper notes that debate design and judging are not neutral details.

## Telephone Bridge

- Entrenchment / path dependence: Degeneration-of-Thought is a single-model analogue of getting stuck after early commitment.
- Failed natural lever: debate may help reasoning, yet Telephone shows source correction or breadth need not repair held belief.
- Speech vs belief: argued alternatives can appear in dialogue without guaranteeing later belief update.

## What We Add Beyond This Paper

Telephone moves from reasoning tasks to factual update transmission and shows that social interaction can fail even when the correct content is present in the communicative environment.

## Draft-Ready Use Sentence

> Multi-agent debate has been used to counter Degeneration-of-Thought by forcing divergent arguments; Telephone shows a complementary social path-dependence problem in which corrected information can be spoken without becoming the agent's later held answer.

## Caveats

- Good for contrast, not as a direct misinformation paper.
- If citing results, verify task names and reported numbers from the PDF.

## Citation Decision

Decision: `cite`

Reason: Strong debate/path-dependence contrast.
