# Review of "Where Agents Dwell: A Scoping Review of Spatial Representation and Its Social Effects in LLM Multi-Agent Systems"

**Reviewer**: Expert Reviewer (Survey / Spatial Computing / LLM Agents)  
**Date**: 2026-04-11  
**Plan Version**: `survey_plan_v4`  
**Recommendation**: Weak Accept

---

## Overall Assessment

这是目前为止最成熟的一版。`v4` 不只是“继续修补”了上一轮意见，而是把若干关键方法问题真正内化进了计划结构：`corpus` 分层、`system/environment configuration` 作为分析单位、`environment-side` 与 `agent-accessible` 的双层空间编码、行为分层编码、轻量质控方案、`coding manual` 的前置要求，以及对 Space Syntax primer 的显式限重。这些修改使文章第一次具备了“可以按此执行而不至于在中途失控”的方法基础。

和 `v3` 相比，这版最大的进步，不是多加了几个 protocol 字段，而是它终于把**证据对象、分析对象、叙事对象**分开了。对于这样一个跨领域 scoping review，这一点非常重要。现在这份计划已经明显从“好的研究想法”进入了“可实施的综述设计”。

我的总体判断是：**这版已经接近可直接开工。** 我给出 `Weak Accept` 而不是更高评价，主要是因为仍有几条执行规则需要在真正开始大规模编码前再写得更硬一些，否则后续仍可能在证据聚合和 claim discipline 上产生漂移。

---

## Major Improvements Over v3

### 1. Corpus 分层已经从口头区分变成了方法规则

第 2.2 节将 `Core / Adjacent / Foundational` 三层写进 protocol，并明确不同层的证据角色与编码方式。这直接回应了上一轮最重要的担忧，也让整篇文章的证据来源更可审计。

### 2. 分析单位终于与文章问题一致

第 2.6 节把 `bibliographic screening` 与 `evidence map` 的单位分开处理，尤其将 evidence map 设为 `system / environment configuration` 级别，这是一个非常关键的修正。它避免了把“论文数”误当成“系统证据数”。

### 3. 双层空间编码是本版最有价值的技术性补强

第 2.7-2.9 节将 `environment-side representation` 与 `agent-accessible representation` 分开，并明确 `L0-L5` 只编码后者。这一步让 taxonomy 从“概念上合理”变成了“执行上可判定”，尤其对避免 `L5` 误判非常重要。

### 4. 行为编码现在更接近可分析数据，而不是描述性标签

`behavioral scale + behavior type + evidence status` 的拆分是正确的。它显著降低了把“局部移动选择”“对话互动”“宏观角色分化”混写成同类证据的风险。

### 5. 质控机制终于出现了闭环

第 2.8 节的二次复核、adjudication memo、external audit、taxonomy 版本化，已经构成一个足够轻量但真实有效的单人研究质控框架。这一点足以让 reviewer 相信 taxonomy 不是一次性拍脑袋产物。

### 6. 第 2 章的限重处理得很对

把 Space Syntax primer 压到 `1500-2000` 词并删去额外 appendix，是成熟判断。现在它更像理论桥，而不是喧宾夺主的第二篇综述。

---

## Remaining Concerns

### 1. `system family` 的“按最新版编码”规则仍可能丢失关键版本差异

第 2.6 节写道，同一系统家族的多篇论文“按最新版编码，注明版本演变”。这个方向是对的，但当前表述仍略显激进。问题在于，有些系统家族的后续论文并不只是“更新版”，而可能在以下方面发生结构性变化：

- 空间输入形式改变
- 环境配置改变
- agent 数量与社会行为目标改变
- 评估方法改变

如果简单按最新版折叠，有可能把对本文最重要的变化抹平，尤其会影响“空间表征如何演化”的观察。

**Recommendation**:

- 不要把“最新版”设为默认最优表示
- 更稳的规则应是：
  - `system family` 作为去重和家族追踪字段保留
  - `environment configuration` 仍按可区分配置单独成行
  - 只有在后续论文不引入新的空间表征或行为结构时，才合并为同一证据点
- 建议在 `coding_manual.md` 中加入一个明确 decision rule：  
  `new paper in same family -> merge or split?`

### 2. 质控方案已有动作，但还缺“触发后怎么办”的明确阈值

第 2.8 节已经写了复核、audit 和一致率记录，这很好。但现在仍缺少几条最关键的触发规则：

- 如果 external audit 一致率偏低，下一步是什么？
- 如果 adjudication memo 暴露出某一层级边界持续模糊，是否回滚 taxonomy？
- 如果 pilot coding 中 `Generative Agents / Project Sid / SARAH` 三个样例都难以稳定编码，是否暂停进入 Phase 1？

当前计划对“检查”写得比“纠偏”更具体。

**Recommendation**:

- 在 `coding_manual.md` 或 readiness gate 中增加几条硬阈值，例如：
  - 二次复核翻转率 `> 10%` 时全量复核
  - external audit 一致率 `< 0.8` 时，修订 manual 并重编 audit sample
  - 若 pilot coding 的 3 个样例中有 `>=2` 个无法稳定归类，则暂停进入 Phase 1
- 这些阈值不必完美，但必须提前写清楚

### 3. 现在最需要补的一点，是“文献出现频率”与“证据强度”之间的防混淆规则

`v4` 已经加入 `evidence status`，这是正确的。但从最终写作角度看，还差最后一道安全阀：文章必须明确规定，**出现得多，不等于证据更强；设计中包含空间，不等于空间已被证明在行为上发挥作用。**

这是这类 scoping review 最容易发生的叙事漂移：

- 很多系统有空间环境
- 很多系统也有社会行为
- 于是作者很容易写出“空间在多 agent 社会模拟中扮演重要角色”

但真实情况可能只是：

- 空间作为背景存在
- 行为由其他机制驱动
- “空间影响行为”只是 affordance 设计意图，而非观察到的效果

**Recommendation**:

- 在正文写作规则里增加一条明确的 `claim discipline`：
  - 关于“空间已被观察到中介行为”的论断，只能基于 `observed effect`
  - `designed affordance only` 和 `hypothesized but not tested` 只能支持 agenda，不支持 empirical claim
- 最好在第 5 节或 Appendix 中加入一个简短的 `claim matrix`，说明不同 evidence status 允许支撑的 claim 类型

### 4. Adjacent corpus 的范围仍可能轻微膨胀，建议提前限定它的功能上限

第 2.2 节把 Adjacent corpus 定义为 `spatial reasoning benchmark + spatially-aware single-agent`，这本身合理。但这类文献往往数量增长很快，也很容易在写作时吞掉篇幅，尤其第 4 节又天然容易扩写成一篇“LLM 空间能力综述”。

`v4` 已经通过结构做了控制，但建议再加一句功能上限，否则执行时仍可能失焦。

**Recommendation**:

- 在 protocol 中写明：Adjacent corpus 的作用仅限于回答  
  `Is configurational input plausibly processable by current models?`
- 不在第 4 节追求 benchmark 全覆盖
- 若 Adjacent corpus 超出 15-20 篇，优先保留：
  - 直接涉及拓扑/几何区分的
  - 直接涉及结构输入的
  - 与 Oh et al. 这类 spatially-aware agent work 最接近的

---

## Minor Concerns

### 5. `Core corpus 25+ 个系统` 的门槛合理，但最好区分“系统数”与“可写证据点数”

有些系统可能最终只是 taxonomy 中的一行，而不构成正文讨论的强 evidence point。建议在内部执行时再区分：

- coded systems
- discussed systems

这样写作时会更干净。

### 6. `External audit` 最好说明审阅者看到什么材料

建议提前写清楚：external reviewer 是只看摘要、看原文、还是看你的编码摘录。不同设置会直接影响一致率的解释。

### 7. 短版产品提取时，要防止把 `L4 gap` 写得像已验证结论

短版会天然追求 sharp message，因此更需要在语气上守住：`L4 gap` 是对实现与文献覆盖的观察，不是对“L4 一定有效”的预先证明。

---

## Verdict

**Weak Accept**

`survey_plan_v4` 是第一版让我觉得“可以按此正式启动”的版本。它已经具备清晰的问题边界、可信的证据分层、合理的分析单位、可执行的 taxonomy、以及足够成形的质量控制框架。与其说它还需要“大改”，不如说它只需要在开工前把几条容易引发漂移的规则再写死。

如果作者在真正进入 Phase 1 前补上以下三项，我认为这份计划就已经足够强：

1. 明确 `system family` 的 merge/split 决策规则，避免“按最新版编码”过度折叠
2. 为 pilot coding / external audit / adjudication 写出触发后的处理阈值
3. 加入一页简短的 `claim discipline` 或 `claim matrix`，明确不同 evidence status 支撑何种论断

---

## Suggested Next Step

最值得立刻补的一份文档，不再是新的 plan，而是：

**`coding_manual.md` 的 v1 + 一页 claim matrix**

只要这两页写稳，`v4` 基本就可以进入执行阶段，而不必继续大幅改计划正文。
