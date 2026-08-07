# Anonymous artifact: Said but Not Held

This artifact supports the DAI 2026 submission. It contains the simulator and memory
implementations, accepted experiment outputs, fixed-stream reconstruction, the strict
selector-only ablation, and the manuscript source. It contains no API credentials or model
weights.

Sanitized transport details, access dates, the context-window boundary, retrieval-backend
limitations, and the failure policy are documented in `EXECUTION_PROVENANCE.md`.

## Environment

- Python 3.10 or newer
- Dependencies in `sim/requirements.txt`
- A provider configuration compatible with `sim/llm.py` is needed only for fresh LLM calls.
- Re-aggregation, reconstruction, and the selector-only symbolic audit require no provider.

Paths stored by older runs are replaced with `<REPO_ROOT>` in the packaged copy. Some older
`run_config.json` files are explicitly marked `_reconstructed`; their immutable aggregate rows
and the project experiment ledger are the source of truth for those fields.

## Headline evidence

| Claim | Runner / accepted output |
|---|---|
| SAID–HELD dissociation | `sim/runs/m4_rebroadcast/` |
| Complete GA-versus-PROV fixed-stream replay | `sim/fixed_stream_integration_eval.py`; `sim/runs/fixed_stream_integration_2026-07-23/` |
| GA-generated cross-source replay | `sim/cross_source_integration_eval.py`; `sim/runs/cross_source_integration_2026-07-23/` |
| Selector-only frequency-versus-version ablation | `sim/matched_policy_ablation.py`; `sim/runs/matched_policy_ablation_2026-07-23/` |
| Controlled memory motifs | `sim/runs/table_repair/` |
| Scenario and fact-type checks | `sim/runs/table_3scenario/`; `sim/runs/dues/` |
| Topology checks | `sim/runs/topology/` |
| Text-only provenance boundary | `sim/runs/provtext_llm_only_r10_n5/`; `sim/runs/provtext_norm_r10_n3/` |
| Forged-version pilot | `sim/runs/cap_c16_mini_adversary/` |

## Deterministic checks

From the artifact root:

```bash
python3 sim/fixed_stream_integration_eval.py \
  --runs-root sim/runs/prov_fair/prov/gpt-5.4-mini/prov \
  --out-dir /tmp/fixed_stream_check \
  --prepare-only
```

This reconstructs all eight frozen streams and verifies each recovered final version/value
against the saved PROV snapshot before making any model call.

```bash
python3 sim/matched_policy_ablation.py \
  --stream-root sim/runs/fixed_stream_integration_2026-07-23 \
  --out-dir /tmp/matched_policy_check \
  --symbolic-only
```

Expected selector-only result:

- mention frequency: 62.5% current, seed-level 95% CI 52.7–72.3%;
- maximum version: 71.5% current, seed-level 95% CI 64.3–78.8%;
- paired difference: +9.0 points, 95% CI 4.4–13.6;
- maximum version higher in 8/8 seeds; exact two-sided sign test `p = 0.0078125`.

The accepted full run contains 400 common-prompt interview checkpoints. Behavioral answers
match the selected symbolic state in every case.

The complementary cross-source runner reconstructs eight GA-generated streams and attaches
controlled-task versions only to unambiguous value mentions:

```bash
python3 sim/cross_source_integration_eval.py \
  --runs-root sim/runs/prov_batch/ga_r5/gpt-5.4-mini/ga \
  --out-dir /tmp/cross_source_check \
  --prepare-only
```

The accepted online replay yields GA 15.0% versus PROV 41.0% current answers
(paired difference +26.0 points, 95% CI 16.5–35.5; positive in 8/8 seeds).
This is conditional on supplied task versions and does not validate automatic
provenance extraction.

## Integrity and failure policy

- `SHA256SUMS` covers every packaged file other than the manifest itself.
- A provider failure is never scored as `unknown`.
- A condition is accepted only after all 25 agents complete.
- Per-agent checkpoints make reruns resumable without silently changing completed records.
- The independent unit for inference is the schedule seed, not an agent or utterance.

## Scope

The complete fixed-stream replay changes the full listener-side memory pipeline. The
selector-only ablation changes only conflict selection after controlled-task candidate
normalization. Text-derived versions in that ablation are oracle analysis annotations, not
evidence that ordinary dialogue supplies or authenticates provenance.
