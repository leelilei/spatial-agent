---
canonical: true
title: "When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation"
category: 05_mobility_realism
role: "empirical urban-mobility realism critique"
decision: must-cite
source: "https://arxiv.org/abs/2606.13835"
pdf: "assets/papers/pdf/05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.pdf"
fulltext: "assets/papers/fulltext/05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.fulltext.md"
quality_flags: []
note_status: first_pass
---

# When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation

## Why This Paper Matters For 6-city

This work provides direct evidence for our motivating gap: coherent mobility narratives
can still violate empirical spatial, temporal, and transition patterns.

## Core Claim / Contribution

The paper validates AgentSociety and CitySim against real mobility data and reports
substantial discrepancies across mobility laws, rhythms, motifs, transitions, and
profiles.

## Evidence We May Cite

- Multi-dimensional comparison with mobility data from Greater Paris and Shanghai.
- Explicit separation between narrative plausibility and empirical mobility realism.

## City Benchmark Bridge

- What it already measures: population-level spatial, temporal, network, semantic, and profile realism.
- What it does not measure: attribute failure to an individual agent's planning, action validity, goal maintenance, or recovery decisions.
- How it informs our SOTOPIA-style city benchmark: Connect micro-level execution failures to downstream macro-level mobility distortions without claiming to replace empirical realism validation.

## What We Add Beyond This Paper

CityAgency supplies controlled causal probes beneath macro statistics, showing which
agent behaviors produce implausible aggregate traces.

## Draft-Ready Use Sentence

> Empirical validation reveals that plausible urban narratives need not yield realistic mobility; CityAgency studies the individual execution failures beneath that discrepancy.

## Caveats / Follow-Up

- Extraction issues: none flagged by converter.
- Need to verify exact metrics, datasets, and numbers against the PDF before using
  them in final related-work prose.
- This is a first-pass note generated from extracted fulltext plus the project
  literature map, not a deep manual reading.

## Citation Decision

Decision: `must-cite`

Reason: Direct support for the paper title and the micro-versus-macro benchmark distinction.

## Extracted Abstract Snapshot

LLM-based generative agents are increasingly used in urban simulators, yet it remains unclear whether they reproduce empirically realistic human mobility patterns or merely generate plausible mobility narratives. We introduce a validation framework for evaluating the mobility of generative agents of LLM-based urban simulators against real-world mobility data. For this, we use mobility laws, temporal rhythms, network motifs, semantic activity transitions, and behavioral mobility profiles. Using datasets from the Greater Paris region and Shanghai, we evaluate AgentSociety and CitySim across multiple dimensions of mobility realism. Our analysis reveals a substantial gap between narrative plausibility and empirical mobility realism. Although the simulators capture some high-level semantic activity distributions, they struggle to reproduce core spatial and temporal constraints, including realistic trip-length distributions, origin-destination flows, dwell times, and transition dynamics. We further observe that realistic mobility diversity is unstable across default prompting configurations and may require explicit profile-aware initialization.
