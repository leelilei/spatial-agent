# Thaw

**Project 7. Codename "Thaw" (provisional).** Sibling of [5-Telephone](../5-Telephone).

> **One line:** If a social belief gets *frozen* by path-dependent entrenchment (5-Telephone's
> core mechanism), does **forgetting** *thaw* it — restoring the society's ability to take a
> late correction? Thaw studies forgetting not as a defect of social memory but as a possible
> **natural error-correction mechanism** for stuck collective beliefs.

## Status
**Novelty-gated pilot stage (2026-06-30).** The broad claim that "forgetting helps" is already
crowded. Thaw now targets the narrower competition between individual memory decay and social
rehearsal: can decay reopen a correction window after an erroneous collective attractor forms?
See `docs/project/lit_positioning_2026-06-30.md`; construct + hypotheses remain in
`docs/project/kickoff_2026-06-25.md`. The first valid frozen-state pilot shows only a weak n=1
signal (2/8 current at rate 0 vs 3/8 at rates 0.5 and 0.8); see `RESULTS.md`.

## Why it is its own project (not a knob in Telephone)
Forgetting has two faces. As a *friction knob* it merely lowers an equilibrium (redundant with
sparse comms — not worth adding). As a force that *collides with entrenchment* it can change the
system's qualitative dynamics (static attractor -> belief re-flow). Only the second is
interesting, and it is large enough to reframe the whole narrative — so it lives here, not inside
Telephone. Telephone asks *why beliefs freeze*; Thaw asks *whether forgetting melts them*.

## Reuse
Sim engine (`society.py` / `memories.py` / `llm.py`), the entrenchment finding (Telephone
P1-rec), and provenance/APM all carry over. Fresh: the forgetting mechanism, SIRS-style belief
re-flow dynamics, and flux/re-correction metrics.
