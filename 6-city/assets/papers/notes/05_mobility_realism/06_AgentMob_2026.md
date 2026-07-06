---
canonical: true
title: "Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agents (AgentMob)"
category: 05_mobility_realism
role: "training-free evidence-grounded next-location prediction agent; fast-path/slow-path adaptive inference"
decision: cite
source: "https://arxiv.org/abs/2606.05130"
pdf: "assets/papers/pdf/05_mobility_realism/06_AgentMob_2026.pdf"
fulltext: "assets/papers/fulltext/05_mobility_realism/06_AgentMob_2026.fulltext.md"
quality_flags: [abstract_may_include_layout_noise]
note_status: first_pass
---

# Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agents (AgentMob)

## Why This Paper Matters For 6-city

AgentMob (UTokyo et al.) makes "evidence grounding" a first-class dimension of a mobility agent: it
formulates next-location prediction as adaptive, evidence-controlled decision making, resolving routine
cases via a fast historical-regularity path and ambiguous cases via slow iterative retrieval over
mobility/geographic evidence with self-correction. This is conceptually adjacent to CityAgency's
action-evidence protocol, though applied to prediction rather than to verifying a committed action.

## Core Claim / Contribution

A training-free LLM-driven agent framework for next-location prediction using a fast-path (historical
regularity) / slow-path (iterative evidence retrieval + self-correction) design grounded in mobility and
geographic evidence. Across three datasets it is the strongest training-free LLM method (e.g. GPT-5.4
reaches 71.42% Acc@1 on BW, 33.14% on YJMob100K).

## Evidence We May Cite

- Evidence-grounded, adaptive fast/slow inference as an alternative to static-prompt single-pass prediction.
- Interpretability + grounding as explicit goals (addresses DNN black-box and prompt-bottleneck drawbacks).
- Strong training-free numbers on standard mobility datasets (incl. YJMob100K, shared with GenWorld's diagnostic).

## City Benchmark Bridge

- What it already measures: accuracy and evidence-grounding of predicting the next location from history + geographic knowledge.
- What it does not measure: whether an agent actually executes and completes a private intention; it predicts where a person will go, not whether a committed goal was realized with environment evidence.
- How it informs our SOTOPIA-style city benchmark: the "evidence-controlled decision" idea supports CityAgency's insistence that claims be backed by retrievable world evidence; the fast/slow adaptive pattern is a candidate baseline architecture.

## What We Add Beyond This Paper

CityAgency shifts from predicting movement to verifying committed action: evidence is owned by the
environment and gates completion, rather than being retrieved by the agent to justify a prediction.

## Draft-Ready Use Sentence

> Evidence-grounded mobility predictors such as AgentMob ground next-location guesses in retrievable
> geographic evidence; CityAgency moves evidence from the predictor to the environment, making it the
> arbiter of whether a committed intention was actually completed.

## Caveats / Follow-Up

- Extraction issues: page 1 figure captions are interleaved into the abstract; use PDF for the framework figure and full metric table.
- Need to verify: the third dataset name and full Acc@1/@5 numbers.

## Citation Decision

Decision: `cite`

Reason: Introduces the evidence-grounding dimension for mobility agents that parallels CityAgency's
action-evidence protocol; useful support and a candidate baseline pattern.

## Extracted Abstract Snapshot

AgentMob: training-free LLM-driven agent for next-location prediction as adaptive evidence-controlled
decision making. Fast path (historical regularity) for routine cases; slow iterative evidence-retrieval +
self-correction for ambiguous cases, grounded in mobility and geographic evidence. Strongest training-free
LLM method across three datasets (GPT-5.4: 71.42% Acc@1 on BW, 33.14% on YJMob100K).
