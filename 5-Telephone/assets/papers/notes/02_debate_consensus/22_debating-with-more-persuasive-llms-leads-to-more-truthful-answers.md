---
telephone_index: 22
canonical: true
aliases: []
title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
category: 02_debate_consensus
role: persuasive debate / truthful answers
decision: cite
doi: 
venue: "International Conference on Machine Learning (ICML 2024)"
year: 2024
source_quality: conference
fulltext: assets/papers/fulltext/02_debate_consensus/22_debating-with-more-persuasive-llms-leads-to-more-truthful-answers.fulltext.md
pdf: assets/papers/pdf/02_debate_consensus/22_debating-with-more-persuasive-llms-leads-to-more-truthful-answers.pdf
read_status: deep-read
deep_read_scope: abstract-introduction-method-results-conclusion-fulltext-pass
---


# Debating with More Persuasive LLMs Leads to More Truthful Answers

## Deep Read Status

Deep-read note completed for Telephone. This note is written from the local
PDF/fulltext and is intended to support citation triage, related-work drafting,
and claim-boundary checking.

## Why This Paper Matters For Telephone

This paper is useful because it studies whether weaker models can use debate between stronger models to reach more truthful answers. It gives us a clean contrast between persuasion/judgment and Telephone's belief-retention question.

## Core Question

The paper asks whether a weaker judge can assess correctness when stronger models debate, anticipating future oversight where humans or weaker models supervise stronger systems.

## Method / Evidence Base

It sets up debates involving more persuasive or stronger LLMs and evaluates whether the judge's final answers become more truthful.

## Core Claim / Result

The relevant finding is that debate can help weaker judges identify truthful answers in some settings. This supports the expectation that social argument should improve factual outcomes, which our findings complicate.

## Evidence We May Cite

- Debate is evaluated as a truth-improving mechanism under asymmetric competence.
- Persuasiveness and truthfulness can be studied together in LLM debate.
- The paper belongs in the optimistic debate/factuality background.

## Telephone Bridge

- Fidelity vs reach: a judged final answer differs from persistent agent belief after transmission.
- Speech vs belief: persuasion can change expressed answer; Telephone asks whether belief state follows.
- Failed natural lever: if debate can improve truth in oversight, our social-transmission failure is more surprising.

## What We Add Beyond This Paper

Telephone removes the judge-as-final-output setup and asks what happens to ordinary agents after information moves through a network.

## Draft-Ready Use Sentence

> Debate studies show that persuasive LLMs can help weaker evaluators reach more truthful answers; Telephone asks a different reliability question, whether corrected facts remain installed in agents after social transmission rather than only winning a debate round.

## Caveats

- Do not cite as evidence that debate always improves truth.
- Use as contrast in a debate paragraph.

## Citation Decision

Decision: `cite`

Reason: Relevant optimistic debate baseline for factuality.
