# E3e Qwen archive

Formal matrix: 2 policies × 6 hard scenarios × 3 repeats.

- Actor: Yunwu `qwen3-235b-a22b-instruct-2507`
- Judge: FHL `gpt-5.4-mini` (`soft_plausibility_only`)
- Actor traces: 36/36
- Judged traces: 36/36
- Actor calls: 195/195 successful
- Actor tokens: 714,144, all from provider usage

Each `repeat_0N/` contains `traces/` and `judged/`. Top-level tables aggregate
all 36 rows. The combined cross-model statistics are in
`../e3e_multivendor_backbone_analysis_2026-07-31/`.

