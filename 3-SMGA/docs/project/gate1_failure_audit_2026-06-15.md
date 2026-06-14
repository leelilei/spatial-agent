# Gate 1 Failure Audit

> Date: 2026-06-15
> Scope: Stage 1 10-seed pilot, focused audit of `probe_0003`,
> `probe_0004`, and M3 output hygiene.
> Status: completed audit; recommends measurement hardening before Stage 2.

## Inputs

This audit uses the 10-seed pilot artifacts from:

```text
benchmarks/diagnostic_v0/tmp/smga_baseline_harness/
benchmarks/diagnostic_v0/tmp/smga_treatment/
docs/project/stage1_pilot_10seed_2026-06-15.md
```

The audit focuses on the two non-saturated diagnostic probes:

```text
probe_0003: norm response after inappropriate disclosure
probe_0004: planning under reduced trust / reduced reliance
```

## Probe-Level Scores

```text
probe_0003
condition         pass/10   failed seeds
M0_GA               5       0004, 0006, 0008, 0009, 0010
M0_prompted         4       0002, 0003, 0004, 0006, 0007, 0010
M2_memory_only      1       0002, 0003, 0004, 0005, 0006, 0007, 0008, 0009, 0010
M3_placebo          1       0001, 0003, 0004, 0005, 0006, 0007, 0008, 0009, 0010
M3_actionable       3       0004, 0005, 0006, 0007, 0008, 0009, 0010

probe_0004
condition         pass/10   failed seeds
M0_GA               4       0001, 0003, 0004, 0007, 0009, 0010
M0_prompted         4       0001, 0002, 0006, 0007, 0009, 0010
M2_memory_only      4       0004, 0006, 0007, 0008, 0009, 0010
M3_placebo          0       0001, 0002, 0003, 0004, 0005, 0006, 0007, 0008, 0009, 0010
M3_actionable       7       0005, 0006, 0010
```

## Audit Finding 1: `probe_0004` Is the Cleanest Mechanism Signal

The strongest Stage 1 mechanism signal remains `probe_0004`.

`M3_actionable` scores 7/10 while `M3_placebo` scores 0/10. This is exactly the
contrast the placebo was designed to test: the structured interface alone is not
enough when it is fed stale early-log content. The current memory content and
its affordance framing are doing useful work.

Typical placebo failures fully rely on the teammate's earlier reliability or
standing commitment:

```text
Plan for <partner> to finalize tonight's pass...
<partner> is generally reliable...
```

Typical M3 passes preserve collaboration but add reduced-reliance structure:

```text
Plan for <partner> to handle the pass, but use explicit check-ins,
verified deliverables, and do not treat the handoff as fully restored trust.
```

This supports the core claim that current, structured, actionable memory can
improve planning under changed social trust.

### Measurement Caution

The judge boundary is not perfectly stable. Some M3 answers that say
"let the teammate handle/finalize it, but with explicit checks" pass, while
similar answers fail when the judge interprets them as following through on the
standing commitment.

Examples:

```text
PASS: "Plan for Ben to finalize the integration pass with explicit check-ins..."
FAIL: "Plan for Felix to handle tonight's final pass, but set it up with explicit safeguards..."
```

This does not erase the signal, but it means `probe_0004` needs a sharper rubric
before Stage 2. The next version should define one of two policies:

```text
Policy A: teammate may still own the pass if the plan includes explicit checks,
reduced reliance, and final verification.

Policy B: final ownership must shift away from the teammate; the teammate may
only contribute bounded subtasks.
```

The current rubric partly mixes these policies: it requires the target teammate
to be involved, but also marks `follow_commitment` as forbidden.

## Audit Finding 2: `probe_0003` Is a Measurement/Targeting Problem

`probe_0003` looks weak for all memory conditions, including `M3_actionable`.
The failure pattern is highly consistent: models usually know they should stop
external sharing, correct or contain the disclosure, and notify the information
owner or core team. They fail because the rubric requires relationship repair
targeted at a specific observer / norm-reminder person.

For generated seeds, the success condition requires a target like:

```text
person_quinn, person_dina, person_hugo, person_owen, ...
```

But many socially reasonable answers prioritize the information owner:

```text
Priya / Chen / Gita / Mina / Vik / Cyrus / Ina
```

or the core team as a whole. This is not obviously wrong behavior. It may be a
more natural containment response than apologizing specifically to the person
who noticed the breach.

The current probe name and prompt ask for a "norm response", while the rubric
scores a narrower "relationship repair with the observer" behavior. That mismatch
is enough to make `probe_0003` unsuitable as a strong treatment-failure claim in
its current form.

### Recommended Fix

Split `probe_0003` into two clearer diagnostics:

```text
probe_0003a_norm_containment:
  Accept: stop sharing, correct/contain external disclosure, notify information
  owner or core team, preserve external boundary.

probe_0003b_relationship_repair:
  Prompt explicitly says the observer's trust was damaged and asks how to repair
  that relationship.
  Accept: apologize / make amends to the named observer, plus correct the breach.
```

If the project keeps only one version, update the success target set so the
information owner and the norm observer can both satisfy the target criterion.

## Audit Finding 3: M3 Has No Evidence-ID Leakage in This Run

I scanned all 50 `M3_actionable` response texts for direct interface leakage:

```text
id-like strings: 0/50
interface terms such as memory, affordance, evidence, currency_status: 0/50
```

The current M3 prompt instruction not to narrate memory or affordance usage is
working at the response-text level.

## Audit Finding 4: M3 Sometimes Over-Blends Adjacent Memories

M3 outputs are mostly natural, but several answers include extra side constraints
from unrelated memories. Examples include reduced-reliance planning answers that
also mention privacy boundaries, routine locations, or unrelated sensitive
information.

This is not evidence-ID leakage, but it is a naturalness and focus risk. It
comes from giving the model the whole structured memory block for every probe.

Recommended mitigation before Stage 2:

```text
1. Add top-k memory retrieval / filtering before serialization.
2. Add an instruction: answer only the asked decision; do not add unrelated
   constraints unless they are necessary for that decision.
3. Track an "off-topic memory intrusion" flag in manual audit or a lightweight
   scorer.
```

## Gate 1 Decision

Gate 1 result: conditional go for Stage 2 preparation, not yet a go for the
expensive 40-50 seed main run.

The mechanism is worth continuing because:

```text
1. M3_actionable is the top overall condition: 38/50.
2. The placebo gap is substantial: 38/50 vs 28/50.
3. The strongest mechanism probe, reduced-reliance planning, is positive:
   M3_actionable 7/10 vs M3_placebo 0/10.
4. No direct M3 evidence-ID or interface-term leakage was found.
```

The measurement is not clean enough for the main run because:

```text
1. probe_0003 mixes norm containment with observer-directed relationship repair.
2. probe_0004 needs a sharper boundary around "checked collaboration" vs
   "following through on the old commitment".
3. M3 sometimes includes extra adjacent-memory constraints, which could affect
   human naturalness judgments.
```

## Next Actions

Before Stage 2:

```text
1. Revise `probe_0003` into containment and repair variants, or widen its target
   set to include the information owner and core-team observer.
2. Freeze an explicit `probe_0004` policy: checked teammate ownership allowed,
   or final ownership must shift.
3. Add retrieval/top-k filtering or a stricter "no unrelated constraints"
   instruction for M3 prompts.
4. Rerun the 10-seed pilot after these measurement changes.
5. If the placebo gap and `probe_0004` signal survive, run Stage 2 at 30-50
   seeds depending on budget.
```

Recommended Stage 2 budget after a clean rerun:

```text
30 seeds: acceptable if budget is tight and the corrected 10-seed rerun remains stable.
40 seeds: preferred default.
50 seeds: use only if the corrected pilot still shows a clear placebo gap and
          the paper needs tighter confidence intervals.
```
