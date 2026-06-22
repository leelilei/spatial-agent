# Paper Search Standard

Purpose: make literature search repeatable across research projects.

This standard is for early-stage direction finding, related-work audits, and
pre-submission novelty checks. It does not replace careful reading. It gives a
project a consistent first-pass search artifact that can be archived, extended,
and cited in later notes.

## When To Use

Use this workflow when a project asks any of these questions:

- Has this benchmark / method / framing already been done?
- What nearby papers threaten the novelty claim?
- Which research clusters should the proposal position against?
- Which papers should be archived before writing the related-work section?

## Required Outputs

Every paper-search pass should write one project note under:

```text
docs/project/
```

Recommended filename:

```text
related-work-search-YYYY-MM-DD.md
```

The note should include:

1. Search question.
2. Query groups.
3. Source coverage.
4. Candidate paper table.
5. Clustered takeaways.
6. Novelty threats.
7. Next archiving / reading priorities.

## Source Coverage

Use at least three source types:

- Search engine queries for broad discovery.
- arXiv / OpenAlex / Crossref / Semantic Scholar style metadata search.
- Project pages, GitHub repos, benchmark leaderboards, or conference pages when
  available.

For AI benchmark work, include:

- arXiv
- OpenReview when relevant
- official project or GitHub pages
- conference CFP / track pages for submission planning

For urban / mobility work, include:

- arXiv
- transportation / urban computing venues where available
- dataset or simulator project pages
- papers that report empirical mobility-realism metrics

## Query Design

Use query groups rather than one broad keyword.

Example groups:

```text
core phrase:
  "LLM agent" "urban" "benchmark"

claim phrase:
  "plausible" "feasible" "LLM agents"

neighbor benchmark:
  "social agent benchmark" "private goals"

domain realism:
  "LLM urban simulation" "mobility realism"

execution validation:
  "LLM agent" "environment validation" "trace"
```

## Relevance Labels

Use these labels in the candidate table:

- `direct`: same problem surface or very close benchmark claim.
- `adjacent`: same domain or method, but missing one core element.
- `foundation`: older or broader work needed for positioning.
- `distant`: useful context, not a novelty threat.

## Novelty-Threat Rules

Mark a paper as a strong novelty threat if it has at least three of these:

- LLM or generative agents.
- Urban / city / mobility environment.
- Interactive episodes or action traces.
- Private goals, intention, or agency.
- Deterministic feasibility validation.
- Replanning under perturbation.
- Social interruption or social-spatial coupling.
- Benchmark release with scenarios and metrics.

If a paper has only macro mobility realism, it is a neighbor rather than a direct
replacement for micro-agency evaluation. If a paper has only social interaction,
it is a neighbor rather than a city benchmark.

## Tool

Use `paper_search.py` for a first metadata pass:

```bash
python D:/0-Research/0-Tools/research-standard/paper_search.py ^
  --query "LLM urban agent benchmark agency" ^
  --query "LLM urban simulation mobility realism benchmark" ^
  --max-results 8 ^
  --out D:/0-Research/6-city/docs/project/paper-search-raw-2026-06-22.md
```

The script is dependency-free and queries public metadata endpoints. Treat its
output as a discovery aid. Always follow up with direct paper/project pages for
the final related-work note.

