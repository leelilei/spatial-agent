# CityIntent v0.3 Blinded Human Audit Design

Date: 2026-07-01

## Purpose

The deterministic verifier is useful only if independent readers agree that its
completion, feasibility, and replanning labels match the observable city trace.
This pilot prepares that calibration without exposing framework identity or
benchmark outputs to annotators.

## Sample

The source is the 48-trace `4 scenarios x 4 adapters x 3 repeats` real-model
matrix. Using seed `20260701`, the builder samples one repeat from every
scenario-adapter cell and shuffles the 16 selected traces into anonymous ids
`H001` through `H016`.

This is a balanced diagnostic pilot, not an estimate weighted by the natural
frequency of urban behaviors.

## Blinding

Annotators can see:

- scenario, private intention, events, and success conditions;
- city locations, hours, costs, and graph edges;
- typed actions, message content, reasons, times, locations, and budgets;
- direct observable outcomes such as entries, purchases, services, messages,
  interactions, and route interruptions.

Annotators cannot see:

- adapter or framework identity;
- repeat id or source result path;
- model information;
- benchmark metrics, violations, failure taxonomy, or verified replans;
- the other annotator's labels.

The mapping and deterministic labels are stored in `sealed/audit_key.csv` and
must not be shared before both annotation files are locked.

## Labels

Each annotator independently labels:

- completion: complete, partial, not complete, or uncertain;
- feasibility: feasible, infeasible, or uncertain;
- disruption replanning: successful, failed, not applicable, or uncertain;
- whether the observable evidence is sufficient;
- first invalid step, confidence, and notes.

The scorer reports exact agreement and Cohen's kappa, then compares each
annotator with the deterministic verifier.

## Important Risk Exposed During Packet Review

Current `co_presence` scoring primarily observes the primary agent's presence in
the required place and time window. The packet does not contain an independent
trajectory proving that the second agent arrived. Annotators are explicitly told
not to infer an unrecorded meeting.

This is not silently patched before the audit because it is exactly the kind of
construct-validity problem the audit should reveal. If humans consistently mark
such evidence insufficient or completion lower than the verifier, CityIntent
should require an explicit second-agent trajectory, interaction event, or
environment-generated co-presence record.

## Status

The packet, two blank annotation forms, rubric, world reference, sealed key, and
agreement tool are complete. The repository contains no human labels yet.

Package:
`6-city/annotation/cityintent_v03_blind_pilot_2026-07-01/`

## 2026-07-02 Disposition

A two-profile model dry run confirmed that the packet can expose the
co-presence evidence gap, but model labels are not human validation. The dry
run also motivated showing executed traversals and accepted outcomes explicitly.

The benchmark implementation has moved to `1.0-rc1`: co-presence now requires
an accepted counterpart interaction, pickup requires typed service evidence,
and outcome completion is separated from process and constraint scores. A new
v1 trace sample and two independent human annotations are still required before
freeze.
