---
canonical: true
title: "Validation Is the Central Challenge for Generative Social Simulation: A Critical Review of LLMs in Agent-Based Modeling"
category: 09_surveys
role: "systematic review of generative-ABM validation"
decision: must-cite
source: "https://doi.org/10.1007/s10462-025-11412-6"
pdf: "assets/papers/pdf/09_surveys/03_Validation_Central_Larooij2026.pdf"
fulltext: "assets/papers/fulltext/09_surveys/03_Validation_Central_Larooij2026.fulltext.md"
quality_flags: ["text_encoding_noise"]
note_status: reviewed
---

# Validation Is the Central Challenge for Generative Social Simulation

## Why This Paper Matters For 6-city

This systematic review provides the broad methodological motivation for CityAgency: generative ABMs gain expressive behavior from LLMs but often lack validation aligned with the mechanisms and scientific claims they make.

## Core Claim / Contribution

Larooij and Tornberg categorize application targets and validation practices across generative ABM studies and argue that black-box, biased, stochastic LLMs may worsen rather than resolve the long-standing validation problem.

## Evidence We May Cite

- Validation practices include human or human-like judgment, known social patterns, comparison with other models, human-generated data, and internal consistency.
- Many studies rely on face validity or outcome metrics only loosely connected to underlying mechanisms.
- A simulation's validation method must follow its intended scientific use and target phenomenon.

## City Benchmark Bridge

- What it already measures: literature-level coverage and methodological adequacy of validation practices.
- What it does not measure: comparative agent performance in a shared executable urban environment.
- How it informs CityAgency: justify environment-owned evidence, construct-validity auditing, repeated trials, and a strict boundary on urban-science claims.

## What We Add Beyond This Paper

CityAgency instantiates a concrete validation protocol for one narrow construct: whether an LLM city agent can convert an intention into a feasible, continuous, state-supported trace.

## Draft-Ready Use Sentence

> Because generative ABMs often validate plausible outputs without tying evidence to mechanisms, CityAgency makes the execution mechanism itself observable and falsifiable.

## Caveats / Follow-Up

- The extracted text has encoding noise; verify quotations against the PDF.
- Use the published 2026 journal citation and DOI.

## Citation Decision

Decision: `must-cite`

Reason: Central methodological justification for a validation-first benchmark.

## Extracted Abstract Snapshot

The review argues that generative ABMs occupy an unresolved methodological space unless calibration and validation are tied to explicit modeling goals and mechanisms.
