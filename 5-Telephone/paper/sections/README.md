# Section-First Writing Plan

We will not treat LaTeX as the thinking surface. Each major paper block should be
argued, challenged, and stabilized in Markdown first. LaTeX becomes the final assembly
format only after the section-level story is clear.

## Rule

For every major paper section, maintain one Markdown file with:

- the section's job in the paper;
- the claim it must prove;
- the evidence it uses;
- the failure modes or reviewer objections it must answer;
- the current draft text or paragraph plan;
- open questions before migration to LaTeX.

## Current Section Map

| Paper block | Markdown source | Status |
|---|---|---|
| Title / thesis / story spine | `../narrative.md` | active |
| Introduction | `../introduction.md` | active |
| Taxonomy | `taxonomy.md` | active |
| Architecture (APM vs GA) | `architecture_apm_vs_ga.md` | active; APM integration features are C15+ (not yet built) |
| Related work | `../references.md` | active citation spine; needs prose section |
| Measurement / method | `../measurement_grounding.md` | active |
| Results | `../results.md`, `../results_tables.md` | active; needs result-story consolidation |
| Figures | `../figures.md` | active |
| Discussion / limitations | `discussion.md` | needs expansion |
| Conclusion | `conclusion.md` | placeholder |

## Before Editing LaTeX

1. Update the relevant Markdown section.
2. Check whether the claim depends on unfinished experiments, especially PROV-text.
3. Record the honest caveat in Markdown before polishing prose.
4. Only then migrate the stable paragraphs into `../latex/main.tex`.

## Current Core Framing

Working title:

> When Truth Loses Its Source: Provenance-Aware Memory for Socially Distributed Agents

Core thesis:

> Agent societies do not merely need larger memories or better retrievers; they need
> social memory interfaces that preserve source/version through communication.

Current caution:

Structured PROV is an idealized upper bound, not a fully naturalistic cure. PROV-text-free
shows that ordinary LLM dialogue does not spontaneously preserve source/version markers.
The next realistic target is PROV-text-norm: explicit attribution carried as natural text.
