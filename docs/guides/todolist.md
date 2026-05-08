# SpatialAgent Survey Todo List

> 更新日期：2026-04-29
> 当前主线：优先推进 `survey` 写作准备，不启动新的 broad search 或 broad core expansion
> 依据文档：`survey_research_guide.md`、`survey_plan_v4.md`、`coding_manual.md`、`claim_matrix.md`、`survey_exemplar_usage_guide.md`、`survey_reference_gap_memo_2026-04-28.md`

---

## 当前判断

当前 survey 已经完成 corpus formalization、shortlist closure、widened-Core evidence-map 稳定化，以及主 section scaffold 的第一轮落地。

接下来真正的主线不是继续找更多 survey，也不是直接写完整正文，而是：

1. 固定 `§3 Evidence Map` 的计数、表图和段落口径
2. 用已更新的 `claim_matrix` 反向检查 section scaffold
3. 将 `§3-§6` scaffold 推进到 paragraph-level drafting
4. 清理旧 guide / todo / 章节草稿中的过时数字与旧 baseline

---

## 当前统一口径

以下数字与边界判断应作为后续写作和 claim check 的统一基线：

- strict baseline：`17` paper-level `anchor_core` items，`19` rows
- stable widened Core：`32` paper-level items，`34` rows
- row layers：`anchor_core = 19`，`bridge_core = 15`
- representation distribution：`L1 = 1 / L2 = 8 / L3 = 18 / L4 = 1 / L5 = 6`
- `L4` 仅出现在 widened digital-network `bridge_core`，不进入 strict `anchor_core`
- `TW-02` 仅保留为 scope-boundary 对照，不纳入 stable widened-Core
- `HC01` 仅作为 Adjacent / boundary / feasibility evidence
- 新补的 `6` 篇方法与范文文献只服务 methods、protocol、reporting、structure，不扩 substantive evidence map

当前应以以下产物为准：

- `assets/survey_paper/phase1/phase1_widened_core_execution_memo_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_widened_core_evidence_map_2026-04-27.csv`
- `assets/survey_paper/phase1/phase1_widened_core_evidence_map_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_targeted_widened_p1_optimistic_recheck_2026-04-28.md`
- `assets/survey_paper/phase1/phase1_proxy_abstract_recheck_2026-04-28.md`
- `assets/survey_paper/phase1/phase1_tw02_scope_decision_2026-04-28.md`
- `docs/guides/survey_exemplar_usage_guide.md`
- `docs/guides/survey_reference_gap_memo_2026-04-28.md`
- `docs/plans/claim_matrix.md`
- `spatial-agent-survey/results/tables/evidence_map.csv`
- `spatial-agent-survey/results/tables/evidence_map.md`
- `spatial-agent-survey/results/tables/representation_gap_examples.csv`
- `spatial-agent-survey/results/logs/l4_gap_summary.json`

---

## 当前状态

### 已完成

- [x] `Phase 0` 基础设施、protocol、coding manual、claim matrix 基线已建立
- [x] `Phase 1` candidate pool、screening、shortlist closure 已完成
- [x] broad core expansion 已被明确暂停
- [x] widened-Core evidence map 初版已形成
- [x] appendix evidence table 初版已导出
- [x] `HC01`、`HC13`、`HC14` acquisition blockers 已关闭
- [x] reference-gap decision 已明确：topic/background survey 已足够，不再扩背景综述
- [x] exemplar usage guide 已明确：先固定 `§3` 与核心图表，再进入正文扩写
- [x] `claim_matrix` 已按 widened-Core baseline 更新
- [x] `03 / 04 / 05 / 06` 主 section scaffold 已创建，并进入 widened-Core 口径对齐阶段
- [x] stable widened-Core 本地归档已补齐，当前 working set 不再有 remote-only 缺口

### 进行中

- [ ] 将 `§3 Evidence Map` 的结构、表图、计数口径固定为可起草状态
- [ ] 将 `§3 / §5 / §4 / §6` scaffold 推进到 paragraph-level drafting
- [ ] 为 `§2` 补齐与后文严格对齐的短版 functional scaffold
- [ ] 清理旧 guide、todo、章节草稿中的旧数字、旧 baseline 与过时优先级
- [ ] 将 `HC13 / HC14 / R3` 的保守裁决写入稳定 coding rows
- [ ] 将 PRISMA / appendix / exported tables 与 `34 rows / 32 papers` 稳定 baseline 完全同步

### 暂不做

- [ ] 不启动新的 broad background-survey search
- [ ] 不启动新的 broad core expansion
- [ ] 不把 online community / generic simulator / single-agent interaction 扩回 Core 主线
- [ ] 不把物理空间或 Adjacent 文献写成 LLM multi-agent social behavior 的直接证据
- [ ] 不在 `§3` 核心图表口径固定前进入正文定稿

---

## 接下来一周的主线任务

### Priority 0：更新执行基线

- [ ] 查 section 口径 | P0 用最新 `claim_matrix` 逐段检查 `03-06` scaffold
- [ ] 清旧口径 | P0 清理 guide/todo/草稿中的旧数字、旧 baseline 与旧优先级
- [ ] 定边界材料 | P0 固定 `TW-02`、`HC01`、`HC13`、`HC14`、`R3` 的写作位置
- [ ] 同步导出资产 | P0 核对 appendix / evidence tables / PRISMA 摘要是否全部落在 `34 rows / 32 papers`

说明：
先把“现在到底能说什么、不能说什么”写清楚，再开始扩正文。

### Priority 1：固定 `§3 Evidence Map`

- [ ] 定 `03` 骨架 | P1 搭好 `03_evidence_map.md` 的段落结构
- [ ] 定 `Table 3` | P1 固定 widened-Core evidence map 主表口径
- [ ] 定 `Table 4` | P1 固定 environment-side vs agent-accessible 示例表
- [ ] 定 `Figure 2` | P1 准备 PRISMA-ScR flowchart 输入口径
- [ ] 定 `Figure 3` | P1 固定 L0-L5 taxonomy 图的文字口径
- [ ] 写 `§3` 注释 | P1 写清 `anchor_core / bridge_core / Adjacent / Foundational` 角色
- [ ] 改旧数字 | P1 清掉 `03_evidence_map.md` 中残留的旧 `35 rows / 33 papers` 口径

说明：
`§3` 是后续全文的证据中心。没有这个骨架，其他章节容易漂。

### Priority 2：准备正文 scaffold

- [ ] 扩 `§5` 段落 | P2 把 current systems use of space 的主点扩成可落笔段落
- [ ] 扩 `§4` 段落 | P2 固定 feasibility 只谈 richer spatial input，不谈 social effect proof
- [ ] 搭 `§2` 短版框架 | P2 保持 Space Syntax primer 短而功能化，并与 `§3-§6` 对齐
- [ ] 扩 `§6` 段落 | P2 以 `Table 7` 为中心组织 evaluation dimensions

说明：
正文扩写顺序按 exemplar guide：`§3 -> §5 -> §4 -> §2 -> §6 -> §7 -> §1 -> §8`。

### Priority 3：补最小必要资产

- [ ] 加方法文献 | P3 将新增 `6` 篇方法/范文文献写入 bibliography 或 README
- [ ] 定 `Table 1` | P3 准备多综述定位矩阵
- [ ] 定 `Table 6` | P3 准备 proposition transfer table
- [ ] 定 `Table 7` | P3 准备 evaluation dimension table

说明：
这些资产服务写作结构，不应反过来驱动新的 corpus 扩张。

---

## 当前写作顺序

正文与图表准备应固定按以下顺序推进：

1. `§3 Evidence Map`
2. `§5 Space in LLM Social Simulation`
3. `§4 Feasibility`
4. `§2 Space Syntax Primer`
5. `§6 Evaluation`
6. `§7 Research Agenda`
7. `§1 Introduction`
8. `§8 Conclusion`

在 `§3` 核心图表口径固定前，其他章节只允许做 paragraph-level scaffold，不进入定稿。

---

## 图表最低集合

当前 full draft 至少应先准备以下图表：

- `Table 1`：multi-survey positioning matrix
- `Figure 1`：corpus / evidence-role diagram
- `Figure 2`：PRISMA-ScR flowchart
- `Figure 3`：L0-L5 taxonomy
- `Table 3`：core evidence map
- `Table 4`：environment-side vs agent-accessible examples
- `Table 6`：proposition transfer table
- `Table 7`：evaluation dimensions

可延后到文字稳定后再做：

- `Figure 4`：representation distribution chart
- `Figure 5`：worked example graph
- `Figure 6`：research agenda map

---

## Claim 纪律

后续写作必须持续遵守以下约束：

- `Foundational` 只服务理论背景与可迁移命题，不作 LLM-agent 直接证据
- `Adjacent` 只服务 feasibility、boundary 或对照，不作 Core effect 证据
- physical-space empirical findings 只能写成 transferable hypotheses 或 motivation
- navigation / embodied planning 成功不等于 social behavior 已被空间结构中介
- `L4 gap` 应写成当前覆盖稀缺或结构空洞，不写成 `L4` 无效

---

## 完成标准

只有以下条件同时成立，才算真正进入正文写作阶段：

- [x] `claim_matrix` 已按 widened-Core 更新
- [ ] `03_evidence_map.md` 骨架已固定
- [ ] `Table 3`、`Table 4`、`Figure 2`、`Figure 3` 口径已固定
- [ ] 旧 guide / todo / 草稿中的旧数字已清理
- [ ] `HC13 / HC14 / R3` 的保守裁决已写入稳定编码或明确保留为边界材料
- [ ] `§5 / §4 / §2 / §6` 已具备可扩写 paragraph-level scaffold

如果以上任一项未完成，当前工作都应视为 drafting preparation，而不是正文定稿。
