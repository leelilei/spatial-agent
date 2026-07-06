---
canonical: true
title: "STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics"
category: 06_agent_execution_benchmarks
role: "spatio-temporal disruption + adaptive-replanning + post-adaptation-verification benchmark (tool-use, not city-grounded)"
decision: must-cite
source: "https://arxiv.org/abs/2605.18548"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/07_STT_Arena_2026.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/07_STT_Arena_2026.fulltext.md"
quality_flags: []
note_status: first_pass
---

# STT-Arena: A More Realistic Environment for Tool-Using with Spatio-Temporal Dynamics

## Why This Paper Matters For 6-city

STT-Arena is the closest concurrent neighbor to CityAgency's disruption→replanning→verification
spine. It isolates exactly the capability CityAgency scores under urban pressure: abandoning a
failed plan and reconstructing an alternative multi-step strategy when a sudden spatio-temporal
change invalidates prior decisions. Its named failure mode "Missing Post-Adaptation Verification"
is essentially CityAgency's argument that an agent must produce environment-verified evidence
after recovery, not a new rationale. It is a must-cite because it stakes the "replanning under
spatio-temporal dynamics" claim first; CityAgency must position tightly against it.

## Core Claim / Contribution

Existing dynamic benchmarks mostly measure whether an LLM detects temporal change *quickly*;
STT-Arena instead measures *adaptive replanning and recovery* after a mid-task trigger invalidates
the plan. It contributes 227 interactive tasks across 9 spatio-temporal conflict types and 4
solvability levels, an executable environment with injected triggers, and a trained STT-Agent
(SFT + online RL, 4B) that beats frontier LLMs on the benchmark.

## Evidence We May Cite

- Even SOTA proprietary models (incl. Claude-4.6-Opus) score <40% overall — a large capability gap on adaptive replanning.
- Three recurring failure modes: Stale-State Execution, Misdiagnosis of Dynamic Triggers, Missing Post-Adaptation Verification.
- Iterative trajectory refinement that removes these failure patterns from training data, combined with online RL.

## City Benchmark Bridge

- What it already measures: detect state shift → construct revised multi-step plan → (should) verify after adaptation, in an executable tool environment.
- What it does not measure: physical urban movement, private resident intentions held over an episode, social co-presence/coordination, or map-owned feasibility of a continuous trajectory. It is tool-use (e.g. flight booking), not a spatially situated city resident.
- How it informs our SOTOPIA-style city benchmark: reuse the "trigger invalidates plan mid-execution" design and the post-adaptation-verification requirement, but bind them to a city world with movement, POIs, budget, deadlines, and other agents.

## What We Add Beyond This Paper

CityAgency grounds the same replanning-and-verify skill in a physical urban episode with a
private-intention agent and an environment-owned evidence contract (entry/purchase/service/
interaction), so recovery must be proven by city state, not by a revised plan or self-report.
It also grades repair type (reroute, substitute, wait, justified abandon) rather than scoring a
single revised strategy.

## Draft-Ready Use Sentence

> Recent tool-use benchmarks show that even frontier models fail to replan and verify after
> mid-task spatio-temporal disruptions (STT-Arena, <40% for SOTA); CityAgency asks the same of a
> city resident whose recovery must be confirmed by environment-owned evidence rather than a
> revised rationale.

## Caveats / Follow-Up

- Extraction issues: page 1 has arXiv sidebar noise (`6202 yaM 81 ...`); use PDF for exact author/affiliation strings.
- Need to verify: whether their "verification" is environment-checked or self-report; whether any task involves physical movement graphs (appears tool/API-centric).

## Citation Decision

Decision: `must-cite`

Reason: First-staking concurrent claim on adaptive replanning under spatio-temporal disruption
with post-adaptation verification; CityAgency's replanning axis must be positioned against it.

## Extracted Abstract Snapshot

LLM agents must replan when mid-task disruptions invalidate prior decisions. STT-Arena: 227 tasks,
9 conflict types, 4 solvability levels, executable environment with injected spatio-temporal
triggers. SOTA (incl. Claude-4.6-Opus) <40%. Failure modes: Stale-State Execution, Misdiagnosis of
Dynamic Triggers, Missing Post-Adaptation Verification. Proposes iterative trajectory refinement +
online RL → STT-Agent-4B beats frontier LLMs.
