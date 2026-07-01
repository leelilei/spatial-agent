# 核心实验审计 + 重定位决策(2026-07-01)

> 承接 `lit_positioning_scan_2026-06-30.md`(定位风险)和 `p1_rec_audit_2026-06-30.md`(P1-rec 撤回)。
> 本文档存档:(1) 触发事件;(2) 核心实验注入审计结果;(3) 站着 vs 塌了的盘点;(4) 重定位决策
> (从 provenance 工具 → SAY≠HOLD 解离);(5) 下一步。

## 1. 触发:三重打击

1. **P1-rec 撤回(2026-06-30)** —— `r5_broadcast` 5/5 runs 零注入(round-index bug:5 轮跑 0..4 却
   配了 index 5)。"晚期全体广播失败"实为"根本没注入 ≈ baseline";修正后 last-round broadcast =
   25/25。**entrenchment / recency 反驳 全部撤回**(论文 §4.3 + Fig 3 作废)。
2. **Thaw H1 推翻(2026-07-01)** —— 构造真 frozen incumbent(H1b:2/8 current)后,seed41 看似单调
   (25→37.5%),但 n=5(seeds 42-46)不复现:40%→22.5%→40%(非单调 dip),stale rehearsal 平
   (73→76→73)。**H1(monotone thaw)作为 clean negative 关闭。**
3. **定位风险(2026-06-30)** —— provenance-fidelity 框架 2025-26 拥挤,PROV/APM 核心被 MemClaw /
   MemIR / Delayed-Verification(arXiv 2606.27409,还有闭式解)/ LLM-MAS 综述 覆盖。

## 2. 核心实验注入审计(2026-07-01) —— 全部通过

方法:逐个读 `sim/runs/**/round_*.json` 的 `injected` 字段(即 P1-rec 那类 bug 的检查),统计每轮
实际注入的 agent 数。

| 实验 | 每轮注入(agent 数) | 预期 | 判定 |
|---|---|---|---|
| M4 baseline | r1=1,其余 0 | 一次性注入 source | ✓ |
| M4 source | r1–r4 每轮=1(a01) | 每轮重播 | ✓ |
| **M4 broadcast** | **r1–r4 每轮=25(全体)** | 每轮全体覆盖 | ✓ **真注入全体** |
| C3 PROV(fair) | r1=1,其余 0 | 一次性 source | ✓ |
| C5 GA / PROV(r5) | r1=1,其余 0 | 一次性 source | ✓ |
| C16 adversary | r1=1(真值到 source) | 真值注入 source(伪造走 encounter) | ✓ |

**无一例零注入、无轮次错误、注入数量全部符合预期。P1-rec 的 bug 是孤立事故,未系统性扩散。**
数据脚本见本次会话记录。

## 3. 盘点:站着 vs 塌了

| 块 | 状态 | 独特性 |
|---|---|---|
| fidelity decay(现象) | ✅ 保留(M5 长程待审计) | 拥挤 |
| single-source failure(M4) | ✅ 保留 | 中 |
| **SAY/HOLD 解离** | ✅ **保留**(注入✓ + P2 judge✓) | **唯一可能独特** |
| broadcast 上限对照 | ✅ 保留(注入✓) | — |
| PROV/APM 对比 | ✅ 数据地基实(注入✓);但**作为卖点被覆盖** | 红海 |
| entrenchment 机制 | ❌ **撤回**(P1-rec bug) | — |

**未审计:** M5 长程轨迹;PROV/APM 的 provenance 传播代码逻辑(非数据层)。

## 4. 重定位决策:从 provenance 工具 → SAY≠HOLD 解离

**新卖点:** 不再是"造了个更好的记忆(provenance)",而是一个发现——
> **在 LLM 智能体社会里,"说"和"信"会解离:一个群体可被驱动去说当前真相却不持有它;且这不是
> "没听到",是"听到、说了、但没内化"。** → 读 agent 社会的集体输出(它们"说"的)不代表其集体信念。

**为什么比 provenance 值:** (a) 独特——那堆撞车工作看的是信息传播失真,没人分开测"说 vs 信";
(b) 有 so-what——直接威胁"把 LLM agent 社会当民意/审议模拟器"这条热门线的方法论。

**新旧对比:**

| 维度 | 旧(draft_v1) | 新(解离为核心) |
|---|---|---|
| 论文类型 | systems / 工具 | measurement + phenomenon |
| 核心贡献 | PROV/APM 架构 | SAY≠HOLD 解离 + HEARD/SAID/HELD 探针 |
| 机制 | entrenchment(已撤回) | 更朴素但干净:言语由社交语境驱动、持有由记忆检索驱动,两者脱钩 |
| PROV/APM 地位 | 主角 | 配角(mechanism probe:什么整合能让持有跟上说) |
| 标题 | *When Truth Loses Its Source: Provenance Memory* | 解离主题(如 *Saying Without Believing*) |
| 独特性 | 被覆盖(红海) | 唯一没被覆盖 |

**关键手法:** 把 PROV/APM 从"贡献"降级为"探针",从而**绕开 provenance 红海**——不再 claim provenance
是新东西(不和 MemClaw/MemIR 竞争),只用它证明"持有可改、且需特定整合规则才改得动"。

**诚实代价:** (1) 机制变弱(entrenchment 撤回,新机制更朴素、难做强因果,论文少一块深度);
(2) 必须 crisp 区分 解离 vs sycophancy/unfaithfulness(否则一击);(3) 论文从三幕大戏缩成
一个发现+方法(更小,但更真、更独特)。

## 5. 下一步(按序)

1. **【必做,先做】确认解离的绝对独特性** —— 搜 `stated vs internal belief` / `sycophancy
   multi-agent/collective` / `faithfulness LLM belief vs utterance`。整篇要压在解离上,必须先确认
   它真没被做。**这一搜决定重定位能否立**(是"唯一活路"还是"连这条也被占、得换赛道")。
2. **若独特 → 重写骨架:** 新标题 + 新 abstract;Results 删 entrenchment(4.3),PROV/APM 压成
   一节 mechanism probe;Related work 改对标 sycophancy/faithfulness/deliberation-sim;强化解离
   稳健性(G1/G2/P2 + 跨模型)。
3. **按需补实验(先别急):** 解离因果证据可再硬(现为 M4"source 改说不改持有";可加"什么条件下
   说与持有重新耦合")。先确认独特性 + 重写骨架,实验按缺口补。

## 状态

- Thaw:H1 negative,前提(P1-rec)也没了 → 正确关闭/暂停(go/no-go 规则起作用)。
- Telephone:地基(解离)审计过关 → 重定位到解离,待第 1 步搜索确认独特性后启动重写。
