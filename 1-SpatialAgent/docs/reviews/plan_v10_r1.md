# Review of "Can Computable Spatial Configuration Shape LLM-Agent Social Behavior?"

**Conference**: AAMAS-27 (primary) / AAAI-27 (backup)
**Reviewer**: Expert Reviewer (AAMAS PC Member)
**Date**: 2026-05-02
**Plan Version**: v10
**Recommendation**: Major Revision
**Score**: 6.5/10
**Confidence**: High

---

## Overall Assessment

v10 在 v8.2 基础上完成了一次值得称赞的"定位前移"——把研究问题从"Space Syntax 在 LLM-agent 社会中是否成立"重写为"computable spatial configuration 是否能在语义场景之外充当 agent-facing behavioral input"。这个转变是正确的，因为它把审稿人最容易抓的"你又不能证明 Space Syntax 对"攻击面整体让出，转而把负担压在一个更狭窄、更可证伪的实证陈述上。条件矩阵在 v8.2 基础上加入 `C2b`（非空间结构化描述）与 `C2c`（真正非空间控制），与 `C_shuffle` / `C_counter` / `C_judge_only` / `C_rule_scorer` 一起，几乎覆盖了"prompt 格式 vs 内容"、"语言关联 vs 结构推理"、"actor 效应 vs judge 效应"三类常见反驳。

但 plan 在三个层面留下未封堵的攻击面：(1) confirmatory 假设清单与统计端点的预注册颗粒度仍不够，特别是 H2/H3 与 run-level 主端点的关系不明；(2) 没有 power analysis 支撑 4 maps × 15 seeds 与 minimum 3 maps × 10 seeds 的样本量决策；(3) §9.3 的显式构型描述模板使用 "exposed / secluded / central / overlap" 这些自带社会涵义的词汇，`C_shuffle` 不能闭合此攻击。此外，§1.1 引用的 survey 数字与 appendix CSV 不一致。这些都是可修复的，但若不在投稿前补齐，AAMAS 审稿人很可能据此要求 Major Revision。

---

## Strengths

### 1. 主张重定位为 "behavioral input layer"

§0、§2.3、§5.3、§20 在四处反复明确"本文不证明 Space Syntax 成立，而是检验 computable configuration 能否充当 input layer"。这种自我克制是 v10 相对 v8.2 的最大改进，把整篇文章从"理论验证"题材改成"表征工程实证检验"题材，后者在 AAMAS 评审里更安全。

### 2. 三层非空间控制条件 (`C2` / `C2b` / `C2c`)

§9.2 把 "implicit affordance"、"非空间结构化描述"、"truly non-spatial" 拆成三个独立条件，反掉了"结构化模板本身造成差异"这一条最常见的 confound 归因。`C6m vs C2b` 的对比尤其关键，它单独检验"空间内容"而不仅仅是"结构化格式"。

### 3. 机制条件矩阵接近完整

§9.4 与 §13.1 的 `C_shuffle` / `C_counter` / `C_fixed_path` / `C_judge_only` / `C_rule_scorer` 主动应对：(a) 正确空间映射是否必要，(b) 结构 vs 语义标签竞争，(c) movement 与 perception 解耦，(d) LLM judge 是否制造效应，(e) 非 LLM scorer 下方向是否保留。这套设计比 v8.2 与 v7 都更成熟。

### 4. 总效应可加分解

§12.4 的 `C4 − C1 = (C6m − C1) + (C6f − C6m) + (C4 − C6f)` 把 perception / movement / sampling 的贡献分开归因，使得即便总效应显著、其内部结构也是可解释的。这一点对论文 discussion 章的写作非常友好。

### 5. Tier 1-4 解释框架预先承认负结果有价值

§16 显式列出四档结论强度（强/中/弱/负），且 §20 重申"有地图、有空间词、有 3D backend，并不自动意味着 LLM-agent 系统有空间机制"。这降低了 selective reporting 风险，也给负结果留了发表通道。

---

## Major Concerns

### 1. Survey 数字与 appendix 不一致

§1.1 line 54-59 写 "stable widened Core: 32 paper-level sources / 34 coded rows" 与 "anchor_core: 17 sources / 19 rows"。但 `spatial-agent-survey/paper/appendix/appendix_evidence_table.csv`（共 34 数据行）实际显示：unique anchor_core shortlist_ids = **19**（plan 写 17），unique stable widened Core sources = **34**（plan 写 32）。bridge_core 15/15 与 L 分布 (1/8/18/1/6) 与"strict anchor_core L4=0"与"唯一 L4 在 widened digital-network bridge_core"全部一致。差异只在于 source 计数。这不是大错，但 §1.1 是整篇 plan 的 motivation 起点，数字 drift 会被审稿人挑出。

**Recommendation**: 重新核对 sources vs rows 的计数口径。如果 17/32 来自合并某些 split-row（HC12A/HC12B 或 SimWorld 变体），应在 plan §1.1 注脚与 appendix 表头同时定义口径；否则按 CSV 实际值改写为 19/34。

### 2. Stage 1 → Stage 2 的 gating 逻辑缺位

§7.1 把 Stage 1 标为"支撑主结论"且 §11.3 给了 "至少 H1 或 H2…达到中等效应" 的 Stage 1A 通过标准——但没有定义 Stage 1A **失败**时 Stage 2 的处置方式。如果 micro-task 表征效应不存在，420-run 的长程模拟就成了沉没成本。

**Recommendation**: 在 §7 增加显式 gate：Stage 1A 的 H1 微任务 `C6m − C1` 若 d < 0.3 且 `C6m vs C_shuffle` 方向不正，Stage 2 自动降级为 minimum 版本（150 runs）并在论文中标注为 "exploratory long-run check"，而非主结论。同样的 gate 也应应用到 Stage 1B counter-stereotypical 全跟随语义标签的情况。

### 3. MIC 50-round divergence 与 run-level 主端点的张力

§12.3 承认 MIC 仅匹配初始条件、"50 轮以后世界可以自然分化"，而 §15.1 的主端点 `TAR_H1_run` 在整个 200 / 300 轮上聚合。如果 50 轮后的发散主要来自级联状态噪声而非空间输入持续作用，run-level effect 会被噪声稀释，且我们无法区分"空间 priming"与"sustained guidance"——而这正是 §15.3 时间动态本应回答的问题，目前却仅处于探索性位置。

**Recommendation**: 把主端点改为预注册两个互补对比 ——`TAR_H1_early`（rounds 0-50）与 `TAR_H1_full`（full run），对二者各自做主分析并报告一致性。任何"只有其一显著"的结果在 §16 Tier 框架里强制降一档。这同时把 §15.3 的 "spatial priming vs sustained guidance" 从探索性提升为 confirmatory 判别。

### 4. Confirmatory 假设清单未编号化

§6 RQ3 平等列出 H1/H2/H3，但 §11.2 与 §15.1 把 H1 当主、H2/H3 当探索；§13.1 又写 "若 high control 节点 < 5 则 H3 降级为描述性"。读者无法准确分辨什么是预注册的 confirmatory 方向、什么是 fallback、什么是探索。这在 OSF preregistration 阶段会被审稿人标红。

**Recommendation**: 在 §6 之后增加 "Hypothesis Registration" 小节，编号列出 H1a / H1b / H2a / H2b / H3，每条注明 (a) 方向（如 "high integration → ↑ encounter rate"），(b) 主分析单元（run / round / scenario），(c) confirmatory or exploratory，(d) 失败的 fallback。把 §15.1 的统计表与编号一一对应。

### 5. Power / sample size 论证缺失

§15.1 把 `d ≥ 0.5` 写为成功标准，但没有给出 4 maps × 15 seeds × 7 conditions 的 mixed model 在 `(1|seed)` 随机截距下的功效估计。最小可投稿版（3 maps × 10 seeds × 5 conditions = 150 runs，每条件配对 ≈ 30 runs）对 d=0.5 与 map × condition 交互项的检测力极可能不足 0.7。

**Recommendation**: §15 增加 power analysis 子节。或基于已有 LLM-agent 模拟先验（如 GovSim、SimulAgents、AgentSocial 类报告的效应量），用 simulation-based power 给出 `C4 vs C1` 与 `C6m vs C2c` 两个关键对比的功效曲线，据此固化 seed 数下限。如果 minimum 版本功效 < 0.7，应在 §17.2 写明该版本不能支撑 confirmatory 主张，仅作 pilot。

### 6. 构型描述模板的词汇泄漏风险

§9.3 模板使用 "highly integrated"、"structurally exposed"、"frequent path overlap"、"structurally secluded"、"requires several topological steps from central areas" 这些词汇，本身带有强社会涵义。`C_shuffle` 仅检测结构-描述的随机化映射是否破坏效应，并不检验**词汇的语言 prior** 是否独立驱动行为。一个完全不理解 graph 结构的 LLM 也可能仅基于 "exposed / secluded / central" 这些词做出符合 H1 方向的行为预测。

**Recommendation**: 在 §9.3 新增 `C6m_neutral` 子条件，把同构信息改写为去情感化措辞，例如 "this node has integration index 0.78, ranking 3 of 20" / "this node has mean depth 4.2, ranking 17 of 20"。在 Stage 1A 比较 `C6m_natural vs C6m_neutral`：若两者效应一致，可在 main paper 中明确否决"词汇 prior"假说；若 `C6m_neutral` 效应消失，则全文应改写为 "spatial-vocabulary-mediated" 而非 "configurational"。

---

## Minor Concerns

### 1. 模型版本未冻结

§8.3 仍写 "Qwen3.5-Plus 或当前可用等价模型"。pre-registration 前必须冻结：(a) 具体 endpoint 名称与日期，(b) temperature / top-p / max tokens，(c) prompt 模板 hash。否则结果不可复现。

### 2. 总预算未汇总

§17.1 给出 Stage 2 = 420 runs，但 Stage 1 micro-task（约 6 conditions × 30 scenarios × 多 task type）、Stage 3 robustness（最小 3 × 5 × 3 = 45，推荐 4 × 10 × 3 = 120）、Stage 4 human eval 的 token / 美元预算需要单独表格汇总，否则项目控制困难。

### 3. Stage 4 N=60 缺 power 论证

§14.4 的 pairwise preference "显著偏离 50%" 没给具体阈值。建议补 binomial power 计算：60 人成对比较，欲检出 60% preference 在 α=0.05 下功效约 0.69，欠 0.8；若想达 0.8 需要约 80 人。

### 4. `C_judge_only` / `C_rule_scorer` 在统计计划中未定位

§13.1 列出但 §15.1 的主分析表未指明它们如何进入推断——是替代主分析、补充审计、还是限定结论强度？建议在 §15.1 表格末尾加一行说明 "若 `C_judge_only` 显示主效应消失或方向反转，则全文结论降至 Tier 3"。

### 5. `plan_v9.md` 引用未在 plan 中链接

§0 与 §19 多次提及 v9 是"历史 protocol 参考"。`docs/plans/plan_v9.md` 确实存在，但 plan 没有指向它的相对路径或锚点；建议在 §0 与 §19 加上 markdown 链接，方便审稿人与合作者快速跳转。

---

## Final Recommendation

**Major Revision** — Score **6.5/10**, Confidence **High**。

v10 已经比 v8.2 更稳健，定位与条件矩阵不需要再大改。关键修复是：(1) 把 hypothesis 编号化并明确 confirmatory / exploratory 边界，(2) 补 power analysis，(3) 引入 `C6m_neutral` 闭合词汇 leak 攻击面。三项都是限时几天内可完成的写作工作，不需要重新采集数据。如果作者在下一轮做完上述修复，并把 §1.1 的数字与 appendix 对齐，本 reviewer 倾向把分数提到 7.5/10、Weak Accept。
