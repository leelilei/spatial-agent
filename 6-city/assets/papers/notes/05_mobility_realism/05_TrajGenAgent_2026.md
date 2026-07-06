---
canonical: true
title: "TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation"
category: 05_mobility_realism
role: "training-free hierarchical LLM agent for individual mobility trajectory generation; behavioral-fidelity evaluation"
decision: cite
source: "https://arxiv.org/abs/2606.12657"
pdf: "assets/papers/pdf/05_mobility_realism/05_TrajGenAgent_2026.pdf"
fulltext: "assets/papers/fulltext/05_mobility_realism/05_TrajGenAgent_2026.fulltext.md"
quality_flags: []
note_status: first_pass
---

# TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation

## Why This Paper Matters For 6-city

TrajGenAgent (Emory + Novateur) represents the current technical ceiling for LLM-driven individual
trajectory generation, and — importantly for CityAgency — it argues that aggregate spatiotemporal
statistics do **not** capture behavioral fidelity or realism of individual trajectories, motivating a
per-trajectory anomaly-aware evaluation. That is the same "aggregate looks fine, individual trace may
not" concern CityAgency raises at the outcome level.

## Core Claim / Contribution

A training-free, semantic-aware, two-stage orchestrator–worker framework: stage 1 an LLM synthesizes a
day's activity chain via in-context learning over historic examples; stage 2 a deterministic workflow
instantiates each visit with distance-aware rule-based location retrieval and LLM-augmented,
kinematics-aware temporal generation. Introduces an anomaly-aware evaluation of individual-trajectory
fidelity beyond aggregate statistics.

## Evidence We May Cite

- Two-stage macro-activity / micro-spatiotemporal decoupling as an architecture pattern.
- Explicit critique that aggregate mobility metrics miss individual behavioral fidelity.
- Training-free (no fine-tuning) yet spatiotemporally grounded generation.

## City Benchmark Bridge

- What it already measures: realism/fidelity of generated individual mobility trajectories (activity chain + timed visits).
- What it does not measure: whether a trajectory satisfies a private goal, respects hard city constraints under disruption, or produces environment-verified completion evidence — it generates plausible movement, it does not verify goal achievement.
- How it informs our SOTOPIA-style city benchmark: reuse the activity-chain → timed-visit decomposition for scenario construction and the "individual fidelity ≠ aggregate statistics" argument.

## What We Add Beyond This Paper

CityAgency does not generate believable movement; it tests whether an agent's own executed movement is
feasible and whether it realizes a held intention with typed evidence — evaluation of accountability,
not generation of plausibility.

## Draft-Ready Use Sentence

> Trajectory generators such as TrajGenAgent already note that aggregate statistics miss individual
> behavioral fidelity; CityAgency pushes this to the outcome level, asking whether an individual trace
> is not just realistic but goal-achieving under environment verification.

## Caveats / Follow-Up

- Extraction issues: IEEE two-column de-spacing; use PDF for metric names and datasets.
- Need to verify: the anomaly-aware metric definition and which mobility datasets are used.

## Citation Decision

Decision: `cite`

Reason: Technical-ceiling reference for LLM trajectory generation and a supporting voice for the
individual-vs-aggregate fidelity argument; sits alongside MobiSim-Bench and When-Plausible.

## Extracted Abstract Snapshot

TrajGenAgent: training-free hierarchical LLM agent for human mobility trajectory generation. Two-stage
orchestrator–worker: LLM synthesizes an activity chain (in-context over historic examples), then a
deterministic workflow instantiates visits with distance-aware retrieval + kinematics-aware temporal
generation. Introduces anomaly-aware individual-trajectory fidelity evaluation beyond aggregate statistics.
