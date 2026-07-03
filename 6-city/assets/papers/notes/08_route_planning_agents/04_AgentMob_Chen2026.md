---
canonical: true
title: "Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent"
category: 08_route_planning_agents
role: "tool-using evidence-grounded mobility predictor"
decision: cite
source: "https://arxiv.org/abs/2606.05130"
pdf: "assets/papers/pdf/08_route_planning_agents/04_AgentMob_Chen2026.pdf"
fulltext: "assets/papers/fulltext/08_route_planning_agents/04_AgentMob_Chen2026.fulltext.md"
quality_flags: []
note_status: reviewed
---

# AgentMob

## Why This Paper Matters For 6-city

AgentMob provides an adjacent notion of evidence grounding: a tool-using LLM agent draws on mobility-analysis functions and observed history when predicting the next location.

## Core Claim / Contribution

The system combines a mobility-analysis toolbox with an LLM controller and an efficiency fast path for next-location prediction across Brightkite, YJMob100K, and Shanghai ISP data.

## Evidence We May Cite

- Compares tool-agent control with statistical and LLM baselines across multiple mobility datasets.
- Reports strong dataset dependence; GPT-5.4 Acc@1 is 71.42% on Brightkite but about 33% on YJMob100K and Shanghai ISP.
- Tool selection provides gains on non-fast-path cases, supporting explicit evidence use rather than unconstrained narration.

## City Benchmark Bridge

- What it already measures: next-location prediction accuracy, tool use, and efficiency.
- What it does not measure: voluntary goal pursuit, multi-step execution, action legality, or completion evidence.
- How it informs CityAgency: distinguish evidence used to predict an action from evidence produced by executing an action.

## What We Add Beyond This Paper

CityAgency's evidence is environment-owned post-action state change, not merely retrieved context that supports a prediction.

## Draft-Ready Use Sentence

> AgentMob grounds mobility prediction in analytical tools and personal history; CityAgency instead requires world-state evidence that an intended urban action actually occurred.

## Caveats / Follow-Up

- Do not treat prediction accuracy as an agency metric.
- The listed GPT-5.4 results are version-sensitive and should be cited with the paper date.

## Citation Decision

Decision: `cite`

Reason: Useful distinction between predictive evidence grounding and executable evidence.

## Extracted Abstract Snapshot

AgentMob uses an LLM-controlled mobility toolbox to improve efficient, evidence-grounded next-location prediction across three datasets.
