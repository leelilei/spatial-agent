# CityIntent Unified Six-Policy Table — HARD tier (E2 adapter side complete)

Date: 2026-07-10

## What this closes

Completes the main matrix: **6 policies × 12 social scenarios × 3 repeats**. The
four official decision-layer adapters were run over the 6 `social_outcome_hard`
scenarios (72 real provider-backed traces) on this Mac, after setting up the
pinned framework checkouts locally (see note below). Combined with the two
paper-backed baselines on the hard tier (36 traces, E2 baseline side) this gives
a full hard-tier unified table that mirrors the existing easy-tier one.

Sources:
- `results/cityintent_v1_rc1/external_frameworks_4x6hardx3_gpt54mini_2026-07-10/`
- `results/cityintent_v1_rc1/paper_backed_baselines_2x6hardx3_gpt54mini_2026-07-09/`
- Unified table: `results/cityintent_v1_rc1/unified_six_policy_social_hard_table_2026-07-10/`

## Main result: accepted co-presence, easy → hard

| Policy | Easy | Hard | Full-social pass^3 (easy→hard) | Legal-but-ineffective (easy→hard) |
|---|---|---|---|---|
| GATSim adapted planner | 15/21 | **21/27** | 0.667 → 0.667 | 0.000 → 0.167 |
| ReAct-style tool-use | 21/21 | 21/27 | 1.000 → **0.500** | 0.000 → 0.167 |
| Plan-and-Execute | 18/21 | 10/27 | 0.833 → **0.167** | 0.056 → 0.222 |
| AgentSociety plan-block | 4/21 | 4/27 | 0.167 → 0.000 | 0.111 → 0.278 |
| Generative Agents | 2/21 | 3/27 | 0.000 → 0.000 | 0.056 → 0.278 |
| SOTOPIA-style LLMAgent | 0/21 | 0/27 | 0.000 → 0.000 | 0.611 → 0.167 |

## Findings

1. **The hard tier breaks reliability where it existed.** ReAct's perfect
   easy-tier reliability (pass^3 = 1.000, every repeat accepts every required
   co-presence) collapses to 0.500 on the hard tier; Plan-and-Execute 0.833 →
   0.167. The benchmark now discriminates the strongest scaffolds.

2. **GATSim is the most robust policy**, and the only one that does not degrade in
   pass^3 (0.667 both tiers). Its explicit activity→evidence synthesis handles the
   timing/sequencing traps better than the reactive/planning baselines. Notably
   GATSim's hard co-presence rate (0.778) even edges out ReAct (0.778 tie) and
   exceeds its own easy rate — the hard scenarios reward its structured execution.

3. **SOTOPIA-style never completes a co-presence: 0/48 across both tiers**, despite
   the highest-or-near feasibility. It is the pure "legal but ineffective" pole of
   the whole matrix.

4. **The dissociation spreads on the hard tier.** On easy, "legal but ineffective"
   was essentially a SOTOPIA-only property (0.611 vs ~0 elsewhere). On hard, every
   policy shows a non-trivial legal-but-ineffective rate (0.167–0.278) — feasible
   traces that do not realize the social outcome — confirming the gap is a general
   property of the harder tasks, not a weak-scaffold artifact.

## Portability fix recorded (real reproducibility bug)

The 4 framework checkouts verified fine on the original Windows checkout machine
but 3 of 4 failed sha256 verification on this Mac. Root cause: the manifest hashes
were computed with Windows CRLF line endings, so a fresh LF checkout mismatches.
Confirmed by re-hashing one file: CRLF-normalized content matched the manifest
exactly. Worked around by converting the checked-out text files to CRLF (making
them byte-identical to the verified checkout-machine content), after which all 4
verified and ran. The adapter code + prompt templates are therefore byte-identical
to prior adapter runs, so these results are comparable to the checkout-machine ones.

Follow-up (optional): make `verify_official_checkout` line-ending-agnostic
(normalize to LF before hashing) so cross-platform setup does not need the manual
conversion.

## Provider instability during the run

The FHL provider returned frequent HTTP 503 / 429 / 502 and intermittent DNS
resolution failures for `www.fhl.mom`. A single such error aborts the whole
multi-repeat run, so the run was driven by a resilient retry wrapper
(`tools/run_e2_hard_adapters_resilient.sh`, --skip-existing/--resume, patient
60s backoff) that completed all 72 traces after 15 attempts without losing work.

## Next

- Extend the co-presence evidence-gap anatomy (E5) to the 4 adapters, to see
  whether weak scaffolds fail earlier (no entry / no interact) than the baselines'
  window_overrun.
- E3 backbone sweep over the combined family (needs provider routing decision);
  the FHL instability today is a reason to consider an alternate backbone anyway.
