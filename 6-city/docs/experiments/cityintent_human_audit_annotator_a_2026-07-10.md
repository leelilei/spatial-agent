# Human Audit — annotator_a (uncalibrated → calibrated)

Date: 2026-07-10

## What was done

The 16-item blinded audit was annotated by annotator_a three times: an
uncalibrated first pass, then two passes after the instrument was fixed.
All three CSVs are archived under `annotations/`.

## Result: human vs deterministic verifier

| Pass | completion | feasibility | replan |
|---|---|---|---|
| uncalibrated | 0.312 (5/16) | 0.333 (5/15) | incoherent (successful 7 / failed 5 / n.a. 3) |
| calibrated v1 | 0.625 (10/16) | 0.833 but n=6 (10 × `uncertain`) | n.a. 15 / uncertain 1 |
| **calibrated v2 (final)** | **0.625 (10/16)** | **0.688 (11/16)** | n.a. 15 / uncertain 1 |

Calibration roughly doubled completion agreement and fixed the replan label
entirely (the annotator now correctly identifies that most items contain no
disruption at all).

## Why the first pass was so low — instrument defects, not judgement

Three defects in the audit instrument were found and fixed:

1. **De-blinding bug.** Every action's `reason` named its source framework
   ("follow GATSim official activity-plan destination") — 102 occurrences in both
   `audit_packet.md` and `audit_items.jsonl`, 105 more in the embedded workbench
   data, across all 16 items. The rubric forbids seeing framework names, so the
   blind audit was not blind. Redacted everywhere; `build_human_audit.py` fixed
   so future packets are blind by construction.
2. **Unreadable evidence.** Conditions rendered as raw JSON; accepted outcomes
   rendered as raw JSON with times as integer minutes (`864` rather than `14:24`),
   which made time-window judgements require mental arithmetic.
3. **No rules at the point of decision.** The rubric was not in the UI at all.

Fixed by a guided workbench: per-item fact questions auto-derived from that
item's `success_conditions`, a violation checklist, plain-language rendering,
an always-visible rule cheat-sheet, and `ANNOTATION_GUIDE.md` with worked
examples of the two most-misapplied rules (arrival ≠ entry; goal-incompletion ≠
infeasibility).

## Methodological position taken

- **Feasibility is a mechanical property of the trace.** Human annotation of it
  measures whether a person can hand-execute a violation check, which is not
  scientifically interesting, and automating the check in the UI would make
  agreement tautological. Feasibility agreement is therefore reported as a
  mechanical cross-check only and **does not carry construct validity**.
- **Construct validity rests entirely on `completion`** — "did this actually get
  done" is the judgement a machine cannot make about itself.
- **The verifier was NOT tuned to match the annotator.** A reclassification of
  `episode_overtime` and `interaction_target_unavailable` out of feasibility was
  considered and **rejected**: the purpose of the audit is to *measure* the
  human↔verifier gap, and adjusting the yardstick until it agrees with the
  measurement destroys it. Fixing the *instrument* is legitimate; fixing the
  *yardstick* is not.

## Open finding (not resolved, deliberately)

The residual completion disagreement is directional: in 3/16 items the annotator
said `partial` where the verifier said `complete` — the human is *stricter* than
the machine, seeing "conditions satisfied but the thing wasn't really achieved".
If that pattern holds with a second annotator it is a real boundary of the
`task_completion` construct and belongs in the paper, not a bug to patch.

One candidate verifier bug was identified but **not** applied: `invalid_explicit_path`
rejects a proposed path that lists only the destination (e.g. `['transit_hub']`),
while an *empty* path is documented as resolving via shortest route — an arbitrary
encoding asymmetry that wasted three consecutive steps in H016. It accounts for
7.1% of all violations across the 419 rc1 traces. Fixing it would require
re-running affected experiments, so it is recorded here as known-issue rather than
silently patched.

## Gate status

Still **not satisfied**: the gate requires two independent annotators for
inter-annotator agreement and Cohen's kappa. `annotator_b` remains blank; the
handoff zip is now clean (de-blinded, guided) and can be given to a second person.
