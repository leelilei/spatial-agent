# SpatialAgent Survey Todo List

> 更新日期：2026-04-14  
> 依据文档：`survey_research_guide.md`、`survey_plan_v4.md`、`coding_manual.md`、`claim_matrix.md`  
> 用途：查看当前 survey 执行进度，明确下一步要做什么

---

## 当前进度总览

### 已完成

- [x] `Phase 0` 基础设施已搭好
- [x] `Phase 0` gate 已正式确认关闭
- [x] `survey_plan_v4.md` 已定稿进入执行状态
- [x] `spatial-agent-survey/` 子项目骨架已建立
- [x] `guide`、`survey_paper` 工作区与 Phase 1 工作流边界已写清
- [x] `Phase 1` 原始检索池已扩展到 `417` 篇候选
- [x] 第一轮 assistant 预筛已完成，收敛到 `117` 篇保留池
- [x] `Phase 1` abstract rereview round 1 已人工接受
- [x] `hold_ambiguous_space` 的 `3` 个条目已裁定完成
- [x] `hold_missing_abstract` 的 `8` 个条目已补摘要/补元数据并裁定完成
- [x] 正式 `screening_sheet_phase1_2026-04-13.csv` 已写实化
- [x] 首轮 `E1-E3` 排除原因已批量落表
- [x] `Phase 1` exclusion recheck sample 已跑通，当前 QC 未阻塞后续阶段
- [x] 首轮 targeted expansion search 已产出两轮候选清单

### 进行中

- [ ] 将 targeted expansion round 1 / round 2 正式 ingest 到 `papers_master`
- [x] 已形成 draft `core-confirmation shortlist`
- [ ] 准备 `system / configuration` 级编码入口

### 未开始

- [ ] `Phase 1` 正式 coding
- [ ] `Phase 2` evidence map / appendix 导出
- [ ] `Phase 3` 正文写作与 claim check

---

## 一句话判断

当前我们已经完成了：

- `Phase 0` 的全部 gate
- `Phase 1` 现有 `417` 篇候选池的正式筛选落表
- unresolved 条目的清零

当前还没有完成的是：

- 把补强搜索得到的新 `Core` 候选正式并入主表
- 把 `Core` 从“当前 12 篇正式落表”提升为“20+ 可编码 shortlist”
- 从 paper-level screening 切到 system-level coding

所以现在项目状态最准确的表述是：

- `Phase 0 = 100%`
- `Phase 1 base corpus formalization = 已完成`
- `Phase 1 core expansion / confirmation = 进行中`
- `Phase 1.5 coding preparation = 待启动`

---

## 执行优先级

> 原则：优先处理会影响 `Core` 规模与后续编码质量的任务。  
> 当前关键路径是：`formalized screening -> broadened core expansion -> core confirmation shortlist -> system-level coding -> analysis/export -> manuscript`

### Priority 0：当前主线

- [ ] 将 `phase1_targeted_core_seed_2026-04-14.jsonl` 导入主流程
- [ ] 将 `phase1_targeted_core_seed_round2_2026-04-14.jsonl` 导入主流程
- [ ] 重新跑 dedupe / prescreen，把新增候选并入正式 `papers_master`
- [x] 建立 dated draft `core-confirmation shortlist`
- [ ] 把 shortlist 标为三档：
  - `high-confidence core`
  - `borderline but keep`
  - `likely demote later`

说明：
当前最大的风险已经不是“unresolved 没处理完”，而是 `Core` 仍可能偏小。下一步最重要的是把 broadened-core 候选正式纳入流程，而不是直接开始写正文。

### Priority 1：紧跟在 P0 后面

- [ ] 确认 broadened-core 后的高优先级全文 PDF 是否齐全
- [ ] 为 `Core` 建立首版 `system family` 清单
- [ ] 按 `system / environment configuration` 拆分编码单位
- [ ] 建立第一版 `systems_master`
- [ ] 建立第一版 `core_evidence`

说明：
这一层的目标是把项目从“paper screening”推进到“system-level evidence coding”。

### Priority 2：质量与边界收紧

- [ ] 继续压缩 `Adjacent`，只保留真正服务“空间能力边界”的条目
- [ ] 继续压缩 `Foundational`，只保留最小理论桥接集
- [ ] 检查 `E4 / E5` 是否确实为零，还是尚未细分
- [ ] 为后续 `merge / split` 建立真实日志

说明：
这一步不是为了扩库，而是为了让后续 claim 不被过宽语料拖散。

### Priority 3：延后启动

- [ ] `Phase 2` evidence map / appendix 导出
- [ ] `Phase 3` 正文写作与 claim check

说明：
这两层必须建立在已确认的 `Core` 编码结果之上，当前不属于主攻方向。

---

## Phase 0：基础设施与协议

### 状态

- [x] 完成

### 已完成项

- [x] `survey_research_guide.md`
- [x] `survey_plan_v4.md`
- [x] `coding_manual.md`
- [x] `claim_matrix.md`
- [x] `spatial-agent-survey/` 目录与基础脚本
- [x] Phase 0 seed corpus 脚本和模板产物
- [x] `Phase 0 readiness checklist`
- [x] pilot taxonomy validation 相关 appendix 草案
- [x] `Adjudication memo` 已进入正式持续维护状态
- [x] `taxonomy_change_log` 已开始按真实案例记录

### 当前判断

- [x] `Phase 0` 已正式关闭，不再是项目瓶颈

---

## Phase 1：检索、预筛、分层

### 状态

- [ ] 进行中

### 已完成项

- [x] `assets/survey_paper/phase1/phase1_search_log.md`
- [x] `assets/survey_paper/phase1/phase1_paper_list.md`
- [x] `assets/survey_paper/phase1/phase1_candidate_pool_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_screening_backlog_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_assistant_prescreen_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_prescreen_keep_pool_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_manual_tier_review_sheet_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_manual_tier_review_sheet_summary.md`
- [x] `assets/survey_paper/phase1/phase1_abstract_rereview_round1_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_abstract_rereview_round1_summary.md`
- [x] `assets/survey_paper/phase1/phase1_ambiguous_space_resolution_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_missing_abstract_resolution_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_screening_formalization_summary_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_master_screening_sync_summary_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_targeted_expansion_search_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_targeted_expansion_search_round2_2026-04-14.md`
- [x] `spatial-agent-survey/data/processed/papers_master_phase1_2026-04-13.csv`
- [x] `spatial-agent-survey/data/processed/screening_sheet_phase1_2026-04-13.csv`
- [x] `spatial-agent-survey/data/raw/phase1_targeted_core_seed_2026-04-14.jsonl`
- [x] `spatial-agent-survey/data/raw/phase1_targeted_core_seed_round2_2026-04-14.jsonl`
- [x] `spatial-agent-survey/results/logs/prisma_summary_phase1_2026-04-13.json`
- [x] `spatial-agent-survey/results/logs/qc_summary.json`

### 当前数字

- [x] OpenAlex family 内去重后：`397`
- [x] 加入 seed batch 后 raw ingestion：`449`
- [x] 全局去重后 candidate pool：`417`
- [x] assistant first-pass 保留池：`117`
- [x] 正式 `screening_sheet` 当前分布：`12 core / 42 adjacent / 47 foundational / 316 excluded`
- [x] 当前排除原因统计：`E1 = 85 / E2 = 54 / E3 = 177 / E4 = 0 / E5 = 0`
- [x] unresolved：`0`
- [x] exclusion recheck sample：`47` 行，`raw_agreement = 1.0`
- [x] `phase_gate_blocked = false`

### 下一步必须做的事

- [ ] ingest 两轮 targeted expansion seed
- [ ] re-run dedupe / prescreen，并同步回 `papers_master`
- [x] 生成 broadened-core 后的 dated `core-confirmation shortlist`
- [ ] 判断正式 `Core` 是否能稳定到 `20+` 的工作集
- [ ] 为 shortlisted `Core` 补全文 PDF
- [ ] 对 broadened-core 候选进行首轮 full-text sanity check

### 这一阶段的完成标准

- [x] `papers_master` 对现有 `417` 篇底池已正式稳定
- [x] `screening_sheet` 已有完整首轮排除原因
- [x] 现有池中的 `Core / Adjacent / Foundational / Excluded` 已落表
- [ ] broadened-core 候选已并入正式主表
- [ ] `Core` shortlist 达到可编码规模
- [ ] 可以从正式筛选结果进入 `system-level coding`

---

## Phase 1.5：系统级编码准备

### 状态

- [ ] 尚未正式开始

### 已有基础

- [x] `systems_master_template.csv`
- [x] `core_evidence_template.csv`
- [x] `adjacent_evidence_template.csv`
- [x] `pilot_systems.csv`

### 下一步

- [ ] 从 confirmed `Core` 中提取 `system family`
- [ ] 按 `system / environment configuration` 拆分编码单位
- [ ] 建立第一版 `systems_master`
- [ ] 建立第一版 `core_evidence`
- [ ] 为 `merge / split` 决策建立真实日志
- [ ] 启动 `Generative Agents / Project Sid / Concordia / OASIS` 的优先编码

---

## Phase 2：分析与导出

### 状态

- [ ] 未开始

### 计划中的关键产物

- [ ] evidence map 大表
- [ ] `agent-accessible repr × behavioral scale × evidence status` 交叉表
- [ ] `environment-side vs agent-accessible` 对照示例表
- [ ] `L4 gap` 统计摘要
- [ ] appendix 完整 evidence table
- [ ] PRISMA-ScR 统计结果正式版

### 进入条件

- [ ] `Core` 正式编码完成
- [ ] `Adjacent` 补充编码完成
- [ ] QC 开始产生真实检查结果

---

## Phase 3：正文写作与论断检查

### 状态

- [ ] 未开始

### 进入条件

- [ ] long review 章节骨架已挂载真实图表
- [ ] `claim_matrix` 可逐条对照证据表
- [ ] appendix 产物可回溯每条关键论断
