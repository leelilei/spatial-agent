---
canonical: true
title: "GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies"
category: 02_citysim_agents
role: "empirically grounded, population-scale urban simulation infrastructure (aggregate realism, offline-compiled policies)"
decision: must-cite
source: "https://arxiv.org/abs/2606.27650"
pdf: "assets/papers/pdf/02_citysim_agents/09_GenWorld_2026.pdf"
fulltext: "assets/papers/fulltext/02_citysim_agents/09_GenWorld_2026.fulltext.md"
quality_flags: []
note_status: first_pass
---

# GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies

## Why This Paper Matters For 6-city

GenWorld is the newest large-scale, empirically grounded urban simulation infrastructure, and it
occupies the opposite end of the agency-vs-scale continuum from CityAgency. It grounds ~196k
synthetic residents in real census and geospatial data and compiles LLM decisions offline into
lookup policies for scalable rollout — trading individual agency for population scale. It even
produces "auditable replanning traces" in a warning-response perturbation, which superficially
resembles CityAgency's replanning story, so it must be cited and clearly distinguished.

## Core Claim / Contribution

LLM-agent urban simulation faces a joint grounding–scaling problem. GenWorld combines a
building-level synthetic city, a structured agent–environment interface, and offline compilation of
LLM-derived decision signals into lookup policies for scalable rollout. Reference instantiation:
Higashi-Hiroshima, Japan; 196,608 residents grounded in census + geospatial data; demographic
consistency validated against census tabulations; YJMob100K mobile-phone data as a commuting
diagnostic.

## Evidence We May Cite

- 196,608 census-grounded synthetic residents; demographic validation against census tabulations.
- Three reproducible cases: full-city weekday rollout, weekday–weekend behavioral contrast, warning-response perturbation with auditable replanning traces.
- Explicitly states calibrated forecasting (traffic, evacuation, policy) remains future work — i.e. it is infrastructure/realism, not an individual-capability verifier.

## City Benchmark Bridge

- What it already measures: population-scale grounded mobility/activity realism and reproducibility; aggregate behavioral contrasts and perturbation response.
- What it does not measure: whether a single agent maintained a private intention and completed it through an environment-verified trace. Its scalability comes from compiling decisions into lookup policies, which removes exactly the per-step individual autonomy CityAgency stresses.
- How it informs our SOTOPIA-style city benchmark: cite as the "grounded + scalable but low-agency" end; CityAgency covers the "high-agency, micro-scale, verifiable individual trace" end. Their auditable replanning traces are aggregate/behavioral, not deterministic per-agent evidence contracts.

## What We Add Beyond This Paper

CityAgency keeps every agent a live, online, individually-reasoning resident with hidden goals and
scores its trace with an environment-owned evidence contract. GenWorld's offline lookup-policy
compilation is the design choice CityAgency deliberately avoids, because it forecloses the
per-agent plausible-vs-verified dissociation CityAgency is built to measure.

## Draft-Ready Use Sentence

> Population-scale grounded simulators such as GenWorld compile LLM decisions into lookup policies
> to reach city scale, trading individual agency for scalability; CityAgency instead holds the
> high-agency, micro-scale end, verifying whether one autonomous resident's trace actually realizes
> its private intention.

## Caveats / Follow-Up

- Extraction issues: two-column layout interleaves Abstract with Introduction §1.1; use PDF for clean section boundaries and figures.
- Need to verify: what exactly "auditable replanning traces" contains (aggregate behavior vs per-agent evidence) and whether any individual-goal completion metric is reported.

## Citation Decision

Decision: `must-cite`

Reason: Newest empirically grounded large-scale urban sim; anchors the agency-vs-scale contrast and
pre-empts confusion between its aggregate "auditable replanning" and CityAgency's per-agent evidence.

## Extracted Abstract Snapshot

GenWorld: grounding+scaling for LLM-agent urban simulation. Building-level synthetic city +
structured agent–environment interface + offline compilation of LLM decisions into lookup policies.
Higashi-Hiroshima instantiation: 196,608 census-grounded residents; census demographic validation;
YJMob100K commuting diagnostic. Cases: weekday rollout, weekday–weekend contrast, warning-response
perturbation with auditable replanning traces. Calibrated forecasting = future work.
