# Phase 0 Completion Confirmation

日期：2026-04-13

## Decision

`Phase 0` 现已确认完成，可以正式进入 `Phase 1` 的人工预筛与后续 system-level coding 准备。

## Why Phase 0 Is Considered Complete

### 方法规则已固定

- `docs/plans/survey_plan_v4.md`
- `docs/plans/coding_manual.md`
- `docs/plans/claim_matrix.md`

这三份文件已经能共同约束：

- corpus 分层
- unit of analysis
- `L0-L5` 判定
- `evidence_status` 边界
- claim 强度上限

### 基础工作流已跑通

- `spatial-agent-survey/` 子项目已建立
- seed corpus ingestion 已完成
- `papers_master.csv`、`screening_sheet.csv`、evidence templates 已可生成
- `test_phase0_seed_corpus.py` 已通过

### Pilot coding 已形成最小闭环

以下 3 个 pilot systems 已进入明确记录：

- `Generative Agents`
- `Project Sid`
- `SARAH`

对应证据：

- `data/processed/pilot_systems.csv`
- `paper/appendix/pilot_taxonomy_validation.md`
- `paper/appendix/adjudication_memo.md`
- `paper/appendix/taxonomy_change_log.md`

### 关键边界已写成文字，不再依赖口头约定

当前已经确认：

- `L2` 与 `L3` 的边界
- `3D_engine` 不等于 `L5`
- `backend richness` 不等于 `agent-accessible representation`
- `design affordance` 不等于 `observed effect`

## Residual Notes

`Phase 0` 完成不意味着后续不会再改 taxonomy，而是意味着：

- taxonomy 已经足够 operational
- 后续修改必须进入 `taxonomy_change_log.md`
- 新模糊案例必须进入 `adjudication_memo.md`

## Immediate Next Step

进入 `Phase 1` 人工预筛：

- 优先从 `assets/survey_paper/phase1/phase1_prescreen_keep_pool_2026-04-13.csv` 开始
- 先人工复核 `21 core`
- 再继续压缩 `adjacent` 与 `foundational`
