# 6-city Reading Notes Pipeline

> Updated: 2026-06-27
> Scope: first-pass notes for all archived urban benchmarks, city-agent systems,
> embodied-city work, social benchmarks, mobility-realism studies, and agent
> execution benchmarks.

## Purpose

The notes are a bridge between the paper archive and the 6-city research direction:
a controlled benchmark for intention-driven city agents under spatial constraints,
private goals, social context, and verifiable trajectory-level scoring.

Each note should answer four practical questions:

1. What does this paper already benchmark or simulate?
2. Does it evaluate autonomous city behavior, or mainly knowledge / planning / QA?
3. What evaluation pattern can we reuse?
4. Where is the gap that CityAgency can claim without overstating novelty?

The project generator is additive by default: it creates missing notes and refreshes
the index without overwriting notes that have already been reviewed or edited. Use
`--force` only when a full regeneration is intentional.

## Note Status

- `first_pass`: generated from extracted fulltext plus project-level literature map.
- `reviewed`: manually checked against PDF / official source.
- `deep_read`: read carefully enough to support related-work prose.

## Citation Decisions

- `must-cite`: central foundation, closest neighbor, or direct benchmark competitor.
- `cite`: useful support for a subsection.
- `maybe`: keep until the related-work structure settles.
- `background`: useful context but unlikely to be central.
- `replace`: right topic, but weaker than another archived source.
- `exclude`: wrong source, wrong PDF, or not useful.

## Quality Rule

If `quality_flags` includes `abstract_may_include_layout_noise`, use the full text
and PDF before making specific claims or quoting numbers.

