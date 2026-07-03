---
canonical: true
title: "TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation"
category: 08_route_planning_agents
role: "hierarchical evidence-grounded trajectory generator"
decision: cite
source: "https://arxiv.org/abs/2606.12657"
pdf: "assets/papers/pdf/08_route_planning_agents/03_TrajGenAgent_Li2026.pdf"
fulltext: "assets/papers/fulltext/08_route_planning_agents/03_TrajGenAgent_Li2026.fulltext.md"
quality_flags: []
note_status: reviewed
---

# TrajGenAgent

## Why This Paper Matters For 6-city

TrajGenAgent is a current technical reference for turning a high-level activity chain into grounded locations, travel times, and durations without fine-tuning the LLM.

## Core Claim / Contribution

Its two-stage orchestrator-worker design uses an LLM to generate personalized activity chains from historical evidence, then a deterministic workflow grounds locations and temporal dynamics. Two anomaly detectors add behavioral and semantic fidelity checks beyond aggregate statistics.

## Evidence We May Cite

- Explicit separation of macro activity planning from micro spatiotemporal realization.
- Historical evidence retrieval and verification support personalization.
- Evaluation combines aggregate mobility statistics with individual behavioral and semantic anomaly detection.

## City Benchmark Bridge

- What it already measures: realism and fidelity of generated mobility trajectories.
- What it does not measure: an online agent observing action outcomes, responding to disruptions, and proving private-goal completion.
- How it informs CityAgency: hierarchical baselines should separate plan generation from deterministic grounding.

## What We Add Beyond This Paper

CityAgency evaluates interactive closed-loop execution and failure recovery, rather than open-loop synthetic trajectory generation.

## Draft-Ready Use Sentence

> TrajGenAgent improves personalized trajectory generation through hierarchical deterministic grounding; CityAgency tests whether an agent can maintain such coherence while acting in a changing world.

## Caveats / Follow-Up

- Extract exact dataset and baseline names before using numerical results.
- Its anomaly detectors may provide useful secondary trace-realism baselines.

## Citation Decision

Decision: `cite`

Reason: Relevant architecture and micro-trajectory evaluation reference.

## Extracted Abstract Snapshot

The framework combines LLM-generated activity chains, deterministic spatial-temporal grounding, and anomaly-based individual trajectory evaluation.
