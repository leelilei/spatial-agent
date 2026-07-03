# CityIntent Blinded Human Audit

This package contains 16 anonymized traces sampled evenly across the
available scenario-adapter cells.

## Handoff

1. Give each annotator `RUBRIC.md`, the complete `blinded/` directory, and only
   their own CSV from `annotations/`.
2. Do not share `sealed/`, source result paths, framework names, scores, or the
   other annotator's labels until both files are locked.
3. Use two independent annotators. Resolve disagreements only after computing
   pre-adjudication agreement.
4. After both CSV files are complete, run:

```bash
python 6-city/benchmarks/cityintent_v0/tools/score_human_audit.py ^
  --annotations-a 6-city/annotation/cityintent_v1_rc1_blind_validation_2026-07-02/annotations/annotator_a.csv ^
  --annotations-b 6-city/annotation/cityintent_v1_rc1_blind_validation_2026-07-02/annotations/annotator_b.csv ^
  --key 6-city/annotation/cityintent_v1_rc1_blind_validation_2026-07-02/sealed/audit_key.csv ^
  --output-dir 6-city/annotation/cityintent_v1_rc1_blind_validation_2026-07-02/agreement
```

The annotation CSVs are intentionally blank in the repository. Sharing labels
or the sealed key before both independent submissions would invalidate the audit.

## Prepared Handoffs

Generate separate annotator archives with:

```powershell
python 6-city/benchmarks/cityintent_v0/tools/prepare_human_audit_handoff.py
```

Each ZIP contains the rubric, blinded packet, world reference, JSONL items, and
only that person's CSV. `handoff_manifest.json` records archive hashes and confirms
that sealed material is absent.

After scoring, complete every row in `agreement/material_findings.csv`. A finding
is resolved only when `status=resolved`, `action` and `rationale` are non-empty,
and any `action=rerun` row cites `rerun_evidence`.
