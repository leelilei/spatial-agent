# CityAgency Results Ledger

This file is the canonical experiment ledger for `6-city`, following the same
role as `5-Telephone/RESULTS.md`.

Raw and derived experiment outputs live under:

```text
6-city/results/
```

Human-readable experiment notes live under:

```text
6-city/docs/experiments/
```

## Archive Standard

Each repeated experiment directory should contain:

- `run_config.json`: command-level configuration and timestamp
- `runs.json`: one row per repeat with trace/judge artifact locations
- `manifest.json`: metrics, scenario/agent set, row count, and run records
- `repeated_summary.md`: paper-facing table
- `all_runs.csv`: one row per repeat/scenario/agent
- `agent_repeated_summary.csv`: agent-level mean/std table
- `scenario_agent_repeated_summary.csv`: scenario-agent diagnostics
- `failure_taxonomy_summary.csv`: aggregated failure counts
- `repeat_XX/traces/`: first-pass city trace outputs
- `repeat_XX/judged/`: second-pass plausibility judge outputs

Single-run or smoke experiments should still keep:

- the exact command in a `docs/experiments/*.md` note
- result tables under `6-city/results/`
- enough raw JSON/CSV artifacts to rerun the analysis

## Experiment Ledger

| Date | Experiment | Result dir | Note | Status |
|---|---|---|---|---|
| 2026-06-22 | API smoke and early hard cases | `results/cityintent_v0/api_smoke_gpt54mini/`, `results/cityintent_v0/api_hard_gpt54mini/`, `results/cityintent_v0/api_all_gpt54mini/` | `docs/experiments/cityintent_v0_api_smoke_2026-06-22.md` | Archived note; early runner outputs |
| 2026-06-23 | Architecture gap, 8 scenarios | `results/cityintent_v0/api_architecture_gap_gpt54mini/` | `docs/experiments/cityintent_v0_architecture_gap_2026-06-23.md` | Archived |
| 2026-06-23 | Plausibility judge v2, 8 scenarios | `results/cityintent_v0/api_architecture_gap_gpt54mini_judged_v2/` | `docs/experiments/cityintent_v0_plausibility_judge_2026-06-23.md` | Archived |
| 2026-06-23 | Repeated reliability, 8 scenarios, 3 repeats | `results/cityintent_v0/api_repeated_reliability_gpt54mini/` | `docs/experiments/cityintent_v0_repeated_reliability_2026-06-23.md` | Archived; rerun metadata refreshed after archive-standard upgrade |
| 2026-06-23 | Pressure scenario smoke, 4 new scenarios | `results/cityintent_v0/pressure_scenarios_smoke_gpt54mini/` | `docs/experiments/cityintent_v0_pressure_scenarios_2026-06-23.md` | Archived; rerun metadata refreshed after archive-standard upgrade |
| 2026-06-23 | Full reliability table, 12 scenarios, 3 repeats | `results/cityintent_v0/api_repeated_reliability_12scenarios_gpt54mini/` | `docs/experiments/cityintent_v0_full_12scenario_table_2026-06-23.md` | Archived |
| 2026-06-29 | GATSim official-adapter smoke | `results/cityintent_v0/gatsim_official_smoke_gpt54mini_2026-06-29/` | `docs/experiments/cityagency_gatsim_official_adapter_smoke_2026-06-29.md` | Archived |
| 2026-06-30 | Four official frameworks smoke (GATSim/SOTOPIA/GenAgents/AgentSociety) | `results/cityintent_v0/external_frameworks_4way_gpt54mini_2026-06-30/` | `docs/experiments/cityagency_four_official_frameworks_smoke_2026-06-30.md` | Archived |
| 2026-06-30 | v0.2 action-evidence protocol: offline regression + 4-framework smoke | `results/cityintent_v02/offline_protocol_regression_2026-06-30/`, `results/cityintent_v02/four_framework_action_evidence_smoke_gpt54mini_2026-06-30/` | `docs/experiments/cityintent_v02_action_evidence_protocol_2026-06-30.md` | Archived |
| 2026-07-01 | v0.3 interruptible movement, 4 frameworks × 4 scenarios × 3 repeats | `results/cityintent_v03/external_frameworks_4x4x3_gpt54mini_2026-07-01/`, `results/cityintent_v03/offline_interruptible_regression_2026-07-01/` | `docs/experiments/cityintent_v03_interruptible_movement_4x4x3_2026-07-01.md` | Archived |
| 2026-07-01 | v0.3 blinded human-audit pilot packet built | `annotation/cityintent_v03_blind_pilot_2026-07-01/` | `docs/experiments/cityintent_v03_blinded_human_audit_design_2026-07-01.md` | Archived; pilot packet |
| 2026-07-02 | v0.3 annotation model dry-run (packet debug, not the human gate) | `annotation/cityintent_v03_blind_pilot_2026-07-01/dry_run/` | `docs/experiments/cityintent_v03_annotation_model_dry_run_2026-07-02.md` | Archived; model labels debug only |
| 2026-07-02 | v1-rc1 external-adapter, 4 frameworks × 4 scenarios × 1 (release-candidate diagnostic) | `results/cityintent_v1_rc1/external_frameworks_4x4x1_gpt54mini_2026-07-02/`, `results/cityintent_v1_rc1_offline_2026-07-02/` | `docs/experiments/cityintent_v1_rc1_external_4x4x1_2026-07-02.md` | Archived; task_completion vs legacy-goal dissociation shown |
| 2026-07-06 | Oracle compliance probe: contract satisfiability + adapter action-surface reachability (3 evidence-critical scenarios) | `results/cityintent_v1_rc1/compliance_probe_oracle/` | `docs/experiments/cityintent_v1_rc1_compliance_probe_2026-07-06.md` | Archived; ALL PASS — refutes adapter-artifact confound; guarded by `tests/test_compliance_probe.py` |
| 2026-07-06 | Social-outcome scenario family: 6 co-presence variants authored + oracle-winnability verified | `results/cityintent_v1_rc1/social_outcome_family_oracle/` | `docs/experiments/cityintent_social_outcome_family_2026-07-06.md` | Archived; ALL PASS (task=1.0, feasible, accepted co-presence); schema OK (social_outcome=6); guarded by `tests/test_social_outcome_family.py`. Framework runs pending checkout machine |
| 2026-07-06 | Social-outcome family, 4 official adapters x 6 scenarios x 3 repeats | `results/cityintent_v1_rc1/external_frameworks_4x6socialx1_gpt54mini_2026-07-06/` | `docs/experiments/cityintent_v1_rc1_social_outcome_4x6x3_2026-07-06.md` | Archived; 72 real traces; GATSim 15/21 accepted co-presence outcomes, AgentSociety 4/21, Generative Agents 2/21, SOTOPIA 0/21 with 61.1% fully feasible traces |
| 2026-07-07 | Paper-backed baselines 2x2 smoke | `results/cityintent_v1_rc1/paper_backed_baselines_2x2_smoke_v6_gpt54mini_2026-07-07/` | `docs/experiments/cityintent_paper_backed_baselines_2x2_smoke_2026-07-07.md` | Archived; after action-discipline v6, ReAct-style and Plan-and-Execute both pass `open_meet` and `message_gated` with task/feasibility/social = 1.0 |

## Next Pending Result

Two parallel, non-blocking tracks:

1. **Human-validation gate (blocks v1 freeze).** Two independent annotators must complete
`annotation/cityintent_v1_rc1_blind_validation_2026-07-02/annotations/annotator_{a,b}.csv`
(currently blank), then report exact agreement + Cohen's kappa vs the deterministic
`task_completion` / feasibility / replanning labels. Model labels cannot satisfy this gate.

2. **Claim-A hardening (does not block freeze).** The compliance probe closes the
strongest adapter-artifact confound, and the 72-trace social-outcome family run now
establishes the repeated "legal but ineffective" effect. Remaining gaps are (a)
end-to-end oracle-through-real-adapters, including GATSim, and (b) a targeted
backbone sweep to separate framework effects from a single `gpt-5.4-mini`
configuration.

See `docs/project/direction_verdict_2026-07-04.md` for why v1 stays
`release_candidate_pending_human_audit` and the recommended framing (lead with the
plausible↔verified-outcome gap, not "first urban benchmark").
