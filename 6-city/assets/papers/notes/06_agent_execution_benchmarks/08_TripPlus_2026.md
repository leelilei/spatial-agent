---
canonical: true
title: "Trip+: Benchmarking Agents in Personalized Interactive Travel Planning"
category: 06_agent_execution_benchmarks
role: "personalized interactive travel-planning benchmark (feasibility + preference + replanning, LLM-simulator scored)"
decision: cite
source: "https://arxiv.org/abs/2606.21169"
pdf: "assets/papers/pdf/06_agent_execution_benchmarks/08_TripPlus_2026.pdf"
fulltext: "assets/papers/fulltext/06_agent_execution_benchmarks/08_TripPlus_2026.fulltext.md"
quality_flags: []
note_status: first_pass
---

# Trip+: Benchmarking Agents in Personalized Interactive Travel Planning

## Why This Paper Matters For 6-city

Trip+ overlaps three CityAgency axes at once — feasibility, personalization/preference, and
environment-driven replanning over multiple turns — so it is a natural related-work neighbor.
Crucially, it is also a *contrast*, not a competitor for the same cell: Trip+ evaluates end-to-end
traveler experience via an **LLM-based simulator** (subjective metrics like fatigue), which is
exactly the LLM-judge-as-verifier stance CityAgency's environment-owned evidence contract is built
to reject. It is useful precisely for drawing that line.

## Core Claim / Contribution

Existing travel benchmarks test feasibility, personalization, or interaction in isolation. Trip+
measures holistic travel planning: given traveler profiles and dynamic multi-turn interactions,
agents generate and revise minute-level itineraries, scored by an LLM simulator that models the
traveler experience. Scenarios range from simple request resolution to complex environment-driven
replanning.

## Evidence We May Cite

- 18 LMs evaluated; a consistent gap in experiential quality.
- Models favor technically feasible but exhausting itineraries that diverge sharply from profiled preferences (feasible ≠ preference-aligned).
- Positions travel benchmarks along "personalization richness" × "interaction richness"; the joint high-personalization + long-horizon-interaction frontier is underexplored.

## City Benchmark Bridge

- What it already measures: profile-conditioned itinerary generation/revision, multi-turn preference tracking, environment-driven replanning, subjective experience.
- What it does not measure: environment-owned deterministic outcome evidence. Success is judged by an LLM simulator, not by authoritative world state; no physical trajectory feasibility check or social co-presence verification.
- How it informs our SOTOPIA-style city benchmark: borrow the profile→preference→replanning interaction structure, but replace LLM-simulator experience scoring with deterministic environment evidence for completion, keeping soft LLM judgment only for plausibility/experience, never for the completion verdict.

## What We Add Beyond This Paper

CityAgency separates "plan looks good / experience feels good" (LLM-judgeable) from "the outcome
actually happened" (environment-verified). Where Trip+ scores the plan's experiential quality,
CityAgency scores whether the executed trace produced state-changing evidence — the dissociation
Trip+ cannot see because its verifier is itself an LLM.

## Draft-Ready Use Sentence

> Interactive travel benchmarks such as Trip+ score itinerary quality with an LLM-based experience
> simulator; CityAgency deliberately refuses LLM-judged completion, requiring environment-owned
> evidence so that a plausible, preference-aligned plan is not mistaken for a realized outcome.

## Caveats / Follow-Up

- Extraction issues: Figure 1 caption text is interleaved with body (vertical-axis labels leaked into prose); use PDF for the positioning figure.
- Need to verify: exact LLM-simulator scoring rubric and whether any objective feasibility check exists alongside the subjective metrics.

## Citation Decision

Decision: `cite`

Reason: Strong neighbor on feasibility+preference+replanning and a clean foil for CityAgency's
"reject LLM-judge-as-verifier" stance; useful in related work, not a direct competitor for the cell.

## Extracted Abstract Snapshot

Trip+: holistic personalized interactive travel planning. Traveler profiles + dynamic interactions;
agents generate/revise minute-level itineraries; end-to-end experience scored by an LLM-based
simulator (e.g. fatigue). 18 LMs; consistent experiential-quality gap; models favor
technically-feasible-but-exhausting itineraries diverging from profiled preferences.
Repo: github.com/junle-chen/trip-plus. Date: 2026-06-23.
