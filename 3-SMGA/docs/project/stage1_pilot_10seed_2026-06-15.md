# Stage 1 Pilot, 10-Seed Diagnostic Run

> Date: 2026-06-15
> Scope: 10 diagnostic seeds x 5 conditions x 5 probes.
> Status: completed pilot run; use for Gate 1 analysis, not final paper claims.
> Follow-up audit: `gate1_failure_audit_2026-06-15.md`.

## Why This Run Exists

The 2-seed alpha showed a positive but tiny `M3_actionable` signal after adding
`M3_placebo`. This run expands the diagnostic set to 10 seeds before committing
to the larger Stage 2 budget.

`seed_0001` and `seed_0002` are the original hand-authored diagnostic seeds.
`seed_0003` through `seed_0010` were generated with
`benchmarks/diagnostic_v0/generate_stage1_seeds.py` from the same five-probe
diagnostic pattern.

The full run used:

```text
M0_GA
M0_prompted
M2_memory_only
M3_placebo
M3_actionable
```

`M3_placebo` keeps the structured M3 interface but uses stale early-log content
before current-update events. This preserves the interface while removing the
updated evidence that should matter for contradiction, privacy revision, and
reduced-reliance probes.

## Execution Notes

The run was executed with the `fhl` Responses API config for `gpt-5.4`.

Artifacts were produced by:

```text
generate_stage1_seeds.py
run_stage1_pilot.py --start 3 --end 10
```

The original two seeds were already present from the alpha run and included in
the final aggregation. After the batch run, three empty response records and two
judge call errors were repaired by hardening the `curl` transport to decode
stdout as UTF-8 and rerunning only the affected probes / judge summaries.

Final audit:

```text
response draft errors: 0
empty response_text fields: 0
judge summary status errors: 0
judge summaries present: 50/50
```

## Headline Scores

```text
condition         pass/total   rate
M0_GA              37/50       74%
M0_prompted        35/50       70%
M2_memory_only     33/50       66%
M3_placebo         28/50       56%
M3_actionable      38/50       76%
```

## Per-Seed Scores

Each cell is passed headline probes out of 5.

```text
seed       M0_GA  M0_prompted  M2_memory_only  M3_placebo  M3_actionable
seed_0001    4        4              5             3             5
seed_0002    5        3              3             4             5
seed_0003    4        4              4             2             4
seed_0004    3        4              3             3             4
seed_0005    5        5              4             3             3
seed_0006    4        3              3             3             3
seed_0007    4        2              3             3             3
seed_0008    4        4              3             3             4
seed_0009    2        3              3             2             4
seed_0010    2        3              2             2             3
```

## Probe-Level Pattern

```text
condition         p0001   p0002   p0003   p0004   p0005
M0_GA             8/10    10/10   5/10    4/10    10/10
M0_prompted       7/10    10/10   4/10    4/10    10/10
M2_memory_only    10/10   8/10    1/10    4/10    10/10
M3_placebo        10/10   7/10    1/10    0/10    10/10
M3_actionable     8/10    10/10   3/10    7/10    10/10
```

Probe meanings:

```text
probe_0001: relationship repair after missed commitment
probe_0002: bounded privacy revision
probe_0003: norm response after inappropriate disclosure
probe_0004: planning under reduced trust / reduced reliance
probe_0005: routine lookup
```

## Interpretation

This run is a useful mechanism signal, but not yet a decisive treatment result.

`M3_actionable` is the top condition at 38/50, but only narrowly above `M0_GA`
at 37/50 and `M0_prompted` at 35/50. The strongest evidence for the structured
memory mechanism is the placebo gap: `M3_actionable` beats the interface-matched
stale-memory placebo by 10/50.

The clearest probe-level advantage is `probe_0004`. `M3_actionable` reaches
7/10 on reduced-reliance planning, while `M3_placebo` is 0/10 and the other
conditions are 4/10. This suggests current structured memory is helping with
the intended trust-update planning affordance.

`probe_0002` also supports the mechanism after the bounded-sharing rubric fix:
`M3_actionable` is 10/10, while `M2_memory_only` is 8/10 and `M3_placebo` is
7/10.

The main weakness is `probe_0003`. All memory conditions struggle, including
`M3_actionable` at 3/10. Failures often take a reasonable containment action
but do not clearly apologize to or repair the relationship with the directly
affected person. This may be a prompt/interface issue, a rubric strictness
issue, or a real limitation in how the memory affordances frame social repair.

## Gate 1 Recommendation

Do not jump straight to the 40-50 seed main experiment as if the result were
settled. The 10-seed run is good enough to justify one focused analysis pass:

```text
1. Blind-audit failed judge rationales for probe_0003 and probe_0004.
2. Check M3 outputs for social naturalness and evidence-ID leakage.
3. Add or run the claim/planning-grounding scorers on this 10-seed set.
4. Decide Stage 2 budget after the audit: likely 30-50 seeds if the probe_0004
   mechanism survives manual review.
```

Gate 1 failure audit is now recorded in
`docs/project/gate1_failure_audit_2026-06-15.md`. Its recommendation is a
conditional go for Stage 2 preparation, but not yet a go for the expensive
40-50 seed main run. First harden `probe_0003`, clarify the `probe_0004`
rubric boundary, reduce unrelated-memory intrusion in M3 prompts, and rerun the
10-seed pilot.
