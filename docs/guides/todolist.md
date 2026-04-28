# SpatialAgent Survey Todo List

> 更新日期：2026-04-28
> 当前主线：优先推进 `survey`，暂不启动新的 broad core expansion
> 依据文档：`survey_research_guide.md`、`survey_plan_v4.md`、`coding_manual.md`、`claim_matrix.md`、`phase1_shortlist_closure_summary_2026-04-22.md`、`phase1_core_gap_audit_2026-04-22.md`、`phase1_core_coding_queue_2026-04-23.md`、`phase1_core_first_pass_coding_summary_2026-04-23.md`

---

## 2026-04-28 当前覆盖说明

今天的 widened-Core 执行结果覆盖本 todo 中较早的 `Core 15`、`14 rows`、`L4 = 0` 等旧快照，但不删除这些历史记录。

当前应以以下 Phase 1 产物为准：

- `assets/survey_paper/phase1/phase1_widened_core_execution_memo_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_widened_core_evidence_map_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_widened_core_evidence_map_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_targeted_widened_p1_optimistic_recheck_2026-04-28.md`
- `assets/survey_paper/phase1/phase1_plan_guide_alignment_after_widening_2026-04-27.md`

当前工作口径：

- strict baseline: `17` paper-level `anchor_core` items, `19` rows
- widened evidence map: `33` paper-level items, `35` rows
- row layers: `anchor_core = 19`, `bridge_core = 16`
- representation distribution: `L1 = 1 / L2 = 8 / L3 = 18 / L4 = 1 / L5 = 7`
- claim discipline: `L4` only appears in widened digital-network `bridge_core`, not in strict `anchor_core`

写作参考口径：

- 使用 `docs/guides/survey_exemplar_usage_guide.md` 作为 drafting 前的结构、图表和范文使用指南。
- 使用 `docs/guides/survey_reference_gap_memo_2026-04-28.md` 锁定最小新增参考清单。
- `assets/survey_paper/pdfs/review_library/` 中 13 篇综述足够支撑 topic/background positioning 与 scoping review 写法参考。
- 不启动新的 broad background-survey search；只补 `4` 篇 scoping review 方法/报告规范引用和 `2` 篇计算/AI/HCI 风格范文。
- 先按 guide 固定 `§3 Evidence Map`、PRISMA、L0-L5 taxonomy 和核心图表，再进入正文段落扩写。

下一步不进入正文定稿；先清理旧 guide/todo 引用，把 `TW-02` 仅保留为 scope-boundary 对照，不纳入 stable widened-Core，并按 exemplar guide 准备 drafting scaffold。

---

## 当前进度总览

### 已完成

- [x] `Phase 0` 基础设施、协议、seed corpus 与 readiness gate 已关闭
- [x] `survey_plan_v4.md`、`coding_manual.md`、`claim_matrix.md` 已作为执行基线
- [x] `spatial-agent-survey/` 子项目骨架、数据目录、脚本与测试样例已建立
- [x] `Phase 1` 原始候选池已完成首轮 formalization：`417` 篇 candidate pool
- [x] 第一轮 assistant 预筛已完成：`117` 篇保留池
- [x] `hold_ambiguous_space` 与 `hold_missing_abstract` 已清零
- [x] 正式 `screening_sheet_phase1_2026-04-13.csv` 已落表
- [x] 排除原因首轮已落表：`E1 = 85 / E2 = 54 / E3 = 177 / E4 = 0 / E5 = 0`
- [x] `Phase 1` exclusion recheck sample 已跑通：`47` 行，`raw_agreement = 1.0`
- [x] 两轮 targeted expansion 已完成候选搜集并进入 shortlist 复核
- [x] `Phase 1` shortlist 已收敛：`15 Core / 9 Adjacent / 2 Excluded`
- [x] 当前 `Core 15` 已完成 gap audit，结论是暂不启动新的 broad search
- [x] representation adjudication 已完成，不需要改 taxonomy
- [x] 可用 Core 已完成 first-pass coding：`14` 个 system/configuration rows
- [x] `HC03` Concordia 已拆为 `HC03A / HC03B`
- [x] `HC12` SimWorld 已拆为 `HC12A / HC12B`

### 进行中

- [x] 补齐剩余 `2` 篇 acquisition-blocked Core 全文：`HC13`、`HC14`
- [x] `HC01` TravelAgent PDF 已归档并完成 full-text adjudication；当前作为 Adjacent/boundary evidence，不进入稳定 Core social-behavior claims
- [x] 基于 `14` 条已编码 Core rows 生成 evidence-map views
- [x] 把 first-pass coding 结果同步到正式 appendix/evidence table 产物
- [x] 完成 targeted Core supplementation round 3 scan，形成候选补充 memo
- [x] 获取并检查 `round 3` 重点全文：`MineLand`、`GATSim`、`Cognitive Agents in Urban Mobility`、`LLM-driven epidemic-economic dynamics`
- [ ] 更新与当前进度不一致的旧 guide / todo 引用

### 暂不做

- [ ] 不启动新的 broad core expansion
- [ ] 不把 online community / generic simulator / single-agent interaction 重新扩成 Core 主线
- [ ] 不在 `HC13 / HC14` 完成保守 row-level 编码前使用它们支撑强 representation claims；`HC01` 只作为边界/可行性证据使用
- [ ] 不直接进入正文定稿，先完成 evidence map 与 claim check

---

## 一句话判断

当前 survey 已经从 `paper-level screening` 推进到 `system/configuration-level first-pass coding`。

现在最准确的状态是：

- `Phase 0 = 完成`
- `Phase 1 corpus formalization = 完成`
- `Phase 1 shortlist closure = 完成`
- `Phase 1 Core first-pass coding = 可用部分完成`
- `Phase 1 evidence acquisition = PDF blockers closed，保守编码待补`
- `Phase 2 evidence map / appendix export = 初版完成`
- `Phase 3 manuscript / claim check = 可在 evidence map 初版基础上启动`

关键瓶颈不再是“缺 Core 候选”，而是：

- `HC01` 已有本地 PDF，但全文显示当前实现更适合作为单智能体空间导航边界案例
- `HC13` 已有本地 PDF；目录确认 multi-agent / cell-semantic hybrid / 3D scenario / evacuation metrics
- `HC14` 已有本地 PDF；目录确认 prompt generation / batched inference / evacuation environment / emergent behaviors / validation
- 现有 `14` 条编码已转成 evidence map、gap summary 和 appendix assets
- `round 3` 已完成 targeted scan 与 top candidate full-text sanity check；`R3-01 / R3-02 / R3-04` 可进入下一步 preliminary coding-row 编辑，`R3-03` 保留为 borderline/reserve

---

## 当前核心数字

- [x] 原始检索与 seed 后 raw ingestion：`449`
- [x] 全局去重后 candidate pool：`417`
- [x] assistant first-pass 保留池：`117`
- [x] 正式 screening 分布：`12 core / 42 adjacent / 47 foundational / 316 excluded`
- [x] shortlist closure 后工作集：`15 Core / 9 Adjacent / 2 Excluded`
- [x] 当前可编码完成：`14` 个 Core system/configuration rows
- [x] 当前 acquisition-blocked：`0` 篇 Core papers
- [x] 当前 unresolved：`0`
- [x] 当前建议：不要继续 broad search；准备 `R3-01 / R3-02 / R3-04` preliminary coding rows，并把 `HC13 / HC14` 推进到保守 first-pass coding

---

## 执行优先级

> 原则：Survey 优先。`14` 条已编码 Core rows 足以启动 evidence map 初版；剩余 `2` 篇阻塞全文并行补齐。只有 evidence map 显示真实结构空洞时，才考虑新的 targeted search。

### 提醒事项规则

- 同步格式：`短标题 | 短详情`
- 标题最长 `10` 字，必须一眼看出“做什么 + 对谁做”
- 详情控制在 `10-20` 字，优先级放最前面，如 `P0`、`P1`
- 详情只写“具体要做什么”，不写板块、目的、背景
- 不写标签，不额外塞分类信息
- 避免抽象词：`收口`、`扫尾`、`挂表`、`补记`、`压缩`、`校准`
- 优先用具体对象命名：论文名、表名、章节号、文档名

### Priority 0：全文补齐与证据完整性

- [x] 获取并归档 `HC01` TravelAgent PDF
- [x] 对 `HC01` 做 full-text sanity check 与边界裁决：转为 Adjacent/boundary evidence
- [x] 补HC13全文 | P0 获取HC13有效全文
- [x] 补HC14全文 | P0 获取HC14有效全文
- [x] 更新 `phase1_pdf_archive_manifest_2026-04-22.md`，记录 `HC01` 与 `round 3` acquisition/check 状态
- [x] 定HC13/14去留 | P0 入表或降级裁决

说明：
`HC13 / HC14` 的全文获取瓶颈已经关闭。当前剩余工作不再是检索，而是把保守的全文裁决写入 stable coding rows；在这一步完成前，仍不应拿它们支撑强 representation claims。`HC01` 已解决获取问题，但全文裁决为边界证据。

### Priority 1：Evidence Map Synthesis

- [x] 基于 `phase1_core_first_pass_coding_2026-04-23.csv` 生成 evidence map 大表
- [x] 生成 `agent-accessible representation × behavioral scale × evidence status` 交叉表
- [x] 生成 `environment-side vs agent-accessible representation` gap examples
- [x] 生成 `L4 gap` 摘要
- [x] 生成 Core evidence map 的 Markdown 与 CSV 两版
- [x] 将 evidence map 同步到 `spatial-agent-survey/results/tables/`
- [x] 将 appendix evidence table 同步到 `spatial-agent-survey/paper/appendix/`

说明：
Evidence map 初版已完成。当前结构是 `L1=1 / L3=11 / L5=2 / L4=0`，且 `observed_effect=4 / designed_affordance_only=10`。

### Priority 1.5：Targeted Core Supplementation

- [x] 完成 `round 3` targeted scan memo
- [x] 完成 top 5 初筛：`MineLand / GATSim / Cognitive Agents in Urban Mobility / LLM-driven epidemic-economic dynamics / CoELA`
- [x] 获取并归档 `MineLand` PDF，完成 full-text sanity check
- [x] 获取并归档 `GATSim` PDF，完成 full-text sanity check
- [x] 尝试获取 `LLM-driven epidemic-economic dynamics` PDF；MDPI PDF 直链被拒，已归档 blocker HTML 与 Markdown full text，并完成 full-text sanity check
- [x] 尝试获取 `Cognitive Agents in Urban Mobility` PDF；MDPI PDF 直链被拒，已归档 blocker HTML 与 Markdown full text，并完成 full-text sanity check，当前作为 borderline urban mobility case
- [x] 保留 `CoELA` 为 Adjacent/boundary，不进入 Core 主表
- [ ] 写R3编码稿 | P1 写R3三篇编码草案
- [ ] 定GATSim去留 | P1 判断是否纳入Core

说明：
这不是 broad search。目标只是补 `L5`、urban/built/crowd、observed spatial-behavior coupling 这些可见缺口。当前全文检查后，`MineLand` 最能补 `L5 + multi-agent`，`LLM-driven epidemic-economic dynamics` 最能补 proximity-mediated observed effects，`GATSim` 是可接受但需保守表述的 urban mobility/population case。

### Priority 2：Adjacent / Foundational 边界收紧

- [ ] 补边界编码 | P2 完成Adjacent最小补编
- [ ] 删桥接文献 | P2 精简桥接文献清单
- [ ] 写平台边界 | P2 写平台边界方法规则

说明：
Adjacent 不应拖慢 Core evidence map。只做足以支撑边界论证的编码。

### Priority 3：Claim Check 与正文准备

- [ ] 更新Claim矩阵 | P3 更新claim与强度标记
- [ ] 套范文指南 | P3 按guide定章节图表
- [ ] 更新正文03-06 | P3 更新03到06节正文

说明：
正文写作应在 evidence map 初版之后启动，否则容易写出无法回溯到编码表的 claim。

### Priority 4：审计性维护

- [ ] 清旧引用 | P4 清理旧引用与ingest

说明：
4 月 14 日 todo 中的 targeted expansion ingest 曾是 P0；但 4 月 22 日 shortlist closure 与 gap audit 已经把主线推到 Core 15 编码阶段，所以它现在不是当前执行瓶颈。

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

## Phase 1：检索、预筛、分层、Core 收敛

### 状态

- [x] corpus formalization 已完成
- [x] shortlist closure 已完成
- [x] 可用 Core first-pass coding 已完成
- [ ] evidence acquisition 尚未完全完成

### 已完成项

- [x] `assets/survey_paper/phase1/phase1_search_log.md`
- [x] `assets/survey_paper/phase1/phase1_paper_list.md`
- [x] `assets/survey_paper/phase1/phase1_candidate_pool_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_screening_backlog_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_assistant_prescreen_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_prescreen_keep_pool_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_manual_tier_review_sheet_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_abstract_rereview_round1_2026-04-13.csv`
- [x] `assets/survey_paper/phase1/phase1_ambiguous_space_resolution_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_missing_abstract_resolution_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_screening_formalization_summary_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_targeted_expansion_search_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_targeted_expansion_search_round2_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_core_confirmation_shortlist_2026-04-14.md`
- [x] `assets/survey_paper/phase1/phase1_shortlist_closure_summary_2026-04-22.md`
- [x] `assets/survey_paper/phase1/phase1_core_gap_audit_2026-04-22.md`
- [x] `assets/survey_paper/phase1/phase1_representation_adjudication_memo_2026-04-23.md`
- [x] `assets/survey_paper/phase1/phase1_core_coding_queue_2026-04-23.md`
- [x] `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`
- [x] `assets/survey_paper/phase1/phase1_core_first_pass_coding_summary_2026-04-23.md`

### 当前阻塞项

- [x] `HC01` TravelAgent：PDF 已归档；全文裁决为 Adjacent/boundary evidence
- [x] `HC13` Fire evacuation cellular automata：PDF 已归档；full-text outline adjudication 已完成
- [x] `HC14` Crowd evacuation disaster scenarios：PDF 已归档；full-text outline adjudication 已完成

### Phase 1 完成标准

- [x] 候选池与筛选表稳定
- [x] Core shortlist 稳定为 `15`
- [x] 可用 Core 已完成 first-pass coding
- [x] `HC13 / HC14` 全文获取与 sanity check 完成
- [x] 阻塞项处理结果写回 PDF manifest、coding queue、closure summary

---

## Phase 2：Evidence Map 与 Appendix 导出

### 状态

- [x] 初版完成

### 输入

- [x] `14` 条已编码 Core system/configuration rows
- [x] representation split 决策已明确
- [x] Core expansion 暂停决策已明确

### 计划产物

- [x] `results/tables/evidence_map.csv`
- [x] `results/tables/evidence_map.md`
- [x] `results/tables/representation_gap_examples.csv`
- [x] `results/logs/l4_gap_summary.json`
- [x] `paper/appendix/appendix_evidence_table.csv`
- [ ] PRISMA-ScR 统计结果正式版
- [ ] Core evidence map 解释 memo

### 完成标准

- [ ] 每个 Core row 都能回溯到 source basis 和 local artifact
- [ ] 每个主要 claim 都能映射到 evidence table 行
- [ ] `environment_side_representation` 与 `agent_accessible_representation` 的差异可以被清楚解释
- [ ] `L4 gap` 被判定为真实 pattern、暂时空洞，或需要后续 targeted search

---

## Phase 3：正文写作与 Claim Check

### 状态

- [ ] 未开始

### 进入条件

- [x] evidence map 初版完成
- [x] appendix evidence table 初版完成
- [ ] `claim_matrix` 已根据真实 evidence 更新
- [x] `HC01` 已有明确处理决策：Adjacent/boundary evidence
- [x] `HC13 / HC14` 至少已有明确处理决策

### 待办

- [ ] 写/改 `01_introduction.md`
- [ ] 写/改 `02_space_syntax_primer.md`
- [ ] 写/改 `03_evidence_map.md`
- [ ] 写/改 `04_feasibility.md`
- [ ] 写/改 `05_social_simulation.md`
- [ ] 写/改 `06_evaluation_dimensions.md`
- [ ] 写/改 `07_research_agenda.md`
- [ ] 写/改 `08_conclusion.md`

---

## 需要人工优先提供的材料

请优先补以下任一类材料：

- [x] `HC13` Fire evacuation cellular automata 的有效 PDF 或可访问全文链接
- [x] `HC14` Crowd evacuation disaster scenarios 的有效 PDF 或可访问全文链接

在 stable coding rows 补齐前，当前执行策略是：

- [x] 先用 `14` 条已编码 rows 生成 evidence map 初版
- [x] 把 `HC13 / HC14` 标为 provisional Core，不进入强论断；`HC01` 按 Adjacent/boundary evidence 处理
- [ ] 在后续 claim check 中明确写出 evidence completeness limitation
