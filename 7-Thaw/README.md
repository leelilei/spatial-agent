# Thaw

**Project 7. Codename "Thaw" (provisional).** Sibling of [5-Telephone](../5-Telephone).

> **One line:** If a social belief gets *frozen* by path-dependent entrenchment (5-Telephone's
> core mechanism), does **forgetting** *thaw* it — restoring the society's ability to take a
> late correction? Thaw studies forgetting not as a defect of social memory but as a possible
> **natural error-correction mechanism** for stuck collective beliefs.

## Status
**Proposal stage (2026-06-25).** Spun out of 5-Telephone, to start after the Telephone paper is
closed. No experiments run yet. Construct + hypotheses in `docs/project/kickoff_2026-06-25.md`.

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
