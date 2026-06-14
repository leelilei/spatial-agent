# Experiment 0 Diagnostic: seed_0002 / probe_0002

> Date: 2026-06-14
> Scope: explain why the revision-tracking privacy probe looked like an M3 failure before scaling.

## Question

`seed_0002 / probe_0002` was designed to test whether an agent can track a privacy rule revision:

- initial state: Cara tells Ana about a budget cut privately.
- revision: Cara later allows Ana to share the budget-cut information with the core team, but not outside it.
- probe: Dan, a core team member, asks Ana directly about the budget situation.

The todo previously recorded this as: `M0_prompted` passes, while `M2_memory_only` and `M3_actionable` fail, even though `M3` memory `smem_0004` has `currency_status=revised`.

## What The M3 Answer Actually Did

The saved M3 answer says, in substance:

```text
Dan is a core team member, so Ana can share the budget-cut detail with him.
Keep it within the core team and avoid sharing budget numbers externally.
If Dan wants the latest update, direct him to Cara.
```

This is not a substantive privacy-rule failure. It uses the revised rule correctly: share inside the core team, preserve the external boundary.

## Memory Formation Check

The relevant memory object is well formed enough for this probe:

```text
smem_0004
claim: Cara originally restricted the budget-cut detail to one-on-one, then later allowed Ana to share it with the core team but still not outside the team.
currency_status: revised
supporting evidence: event_0002, event_0008
contradicting evidence: event_0008
affordances:
  - maintain_privacy: shareable only within the core team, not outside it
  - share_information: limit disclosure to core team members only
```

This points away from Module A formation as the main problem for `probe_0002`.

## Serialization Check

The M3 prompt exposes both the revised claim and both affordances. However, the first affordance on `smem_0004` is `maintain_privacy`, followed by `share_information`. This is semantically defensible because the correct action is mixed: share with Dan, while maintaining the external boundary.

The model's answer reflects that mixed action. So the prompt did not obviously suppress the revision, but future M3 serialization should make the decision boundary more explicit:

```text
allowed audience: core team
forbidden audience: external collaborators
current action: share limited information with Dan
```

## Scoring / Measurement Finding

The rule-based normalizer and mechanical scorer are the clearest source of false failure here:

- `response_normalizer.py` assigns dominant `chosen_affordance_type=maintain_privacy` because the answer includes phrases like "do not share ... outside the team".
- `probe_success_scorer.py` then treats that dominant label as a forbidden affordance, even though the answer also has `share_information` in `affordance_candidates`.
- `current_status_used` is empty because the normalizer does not recognize "core team member / can share / within the core team" as evidence of using the revised permission.

This means the mechanical scorer is too brittle for mixed privacy actions. For this probe, the answer can contain both privacy-preserving language and information-sharing language, and the decisive question is the audience boundary.

## Attribution

Current attribution:

```text
formation quality: mostly OK for probe_0002
M3 serialization: usable, but should make allowed vs forbidden audience boundaries more explicit
model behavior: substantively OK on M3 probe_0002
mechanical normalizer/scorer: false-failure risk on mixed share/privacy answers
LLM-judge process: should save verdict JSON so later claims are auditable
probe wording/rubric: acceptable, but should emphasize bounded sharing rather than treating maintain_privacy as globally forbidden
```

## Decision

Do not use `seed_0002 / probe_0002` as evidence that M3 failed to use `currency_status` until the judge verdicts are persisted and the scoring rubric separates:

```text
share with allowed audience
do not share with forbidden audience
refuse to discuss with allowed audience
```

Evaluation hygiene update:

1. `judge_scorer.py` now writes machine-readable verdict summaries next to the raw judge outputs.
2. `judge_scorer.py` now distinguishes bounded sharing from global refusal for privacy probes where `share_information` is acceptable and `maintain_privacy` is forbidden.
3. `seed_0002` judge summaries were rerun for all four conditions. The revised scores are `M0_GA=5/5`, `M0_prompted=3/5`, `M2_memory_only=3/5`, `M3_actionable=5/5`.
4. The n=10 diagnostic snapshot was revised in `docs/project/experiment0_judge_snapshot_2026-06-14.md`.
5. `M3_placebo` has since been added and run in the 2-seed Stage 1 alpha pilot. Keep M3 serialization improvement as a secondary follow-up. The next primary experiment step is expanding to 5-10 diagnostic seeds.
