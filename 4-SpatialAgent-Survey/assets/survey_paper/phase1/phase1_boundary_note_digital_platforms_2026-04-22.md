# Phase 1 Boundary Note on Digital Platforms and Online Communities

Date: 2026-04-22

## Decision

For the current survey boundary, `structured digital social platform` and `online community` cases are retained as relevant but not automatically `Core`.

## Working rule

A paper should not enter `Core` only because it studies:

- a social network platform
- a forum-like community
- a recommendation-driven online interaction space

Those cases are still important, but they are better treated as `Adjacent` unless the paper's central contribution is the explicit design of an agent-operable environment representation or environment interface that is itself a main methodological object of the survey.

## Practical interpretation

This rule separates two kinds of digital-platform papers:

1. Boundary behavior papers

These papers mainly demonstrate collective behavior, diffusion, polarization, or online interaction patterns inside a structured digital platform. They are relevant to the survey, but their "space" is primarily structural or informational. Under the current boundary, they should remain `Adjacent`.

2. Environment-architecture anchor papers

These papers explicitly define the environment layer itself: state structure, action space, update loop, visibility or filtering logic, and the interface through which agents operate. If that environment design is a central methodological contribution, the paper may still remain in `Core` as a system or environment anchor.

## Immediate consequences for the current shortlist

- `BK07 -> Adjacent`
- `BK08 -> Adjacent`
- `OASIS` can remain a `Core` anchor because its main contribution is the architecture of a reusable digital environment, not only an online-behavior finding
- `SoMoSiMu` remains excluded because the available evidence still does not establish a strong enough environment-side representation signal

## Survey-ready paragraph

Structured digital social platforms and online communities are clearly relevant to LLM multi-agent social simulation, but in this review they are treated as boundary rather than default core cases. The reason is that their operative "space" is usually structural or informational, not a physical or navigable virtual environment with an explicitly modeled spatial interface. We therefore retain such papers as adjacent evidence unless the paper's main contribution is the environment architecture itself, including the state representation, action interface, and update logic through which agents perceive and act.
