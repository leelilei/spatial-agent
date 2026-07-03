# 方向确认终判 + 战略选择(2026-07-01)

> 承接 `lit_positioning_scan_2026-06-30.md`(provenance 红海)+ `repositioning_dissociation_2026-07-01.md`
> (核心审计过关、拟转解离)。人的核心质疑:我们这个点对 GA/社会涌现有意义吗?若无,切什么点?
> **必须先确认方向真没人做、值得、让人 excited,再做实验(准绳 4)。** 本文档存档这一轮的三搜
> 文献确认结果与由此得出的战略判断。

## 三搜文献确认(2026-07-01)——三个候选框架全部被占

践行准绳 4,不再拍脑袋,做定向文献搜索。三个候选新框架(均以解离为核心、均绕开 provenance 红海):

| 框架 | 已有/在先工作 | 判定 |
|---|---|---|
| **A. 解离(说≠信)本身** | sycophancy 多篇;**Persona Inconstancy in Multi-Agent LLM(arXiv 2405.03862, 2024-05):agent 群聊说一套、私下问回到原意,归因 conformity** | **灭顶(比我们早一年多,且机制更成熟)** |
| **B. Agent-society-as-simulator 效度攻击(言≠信不可靠)** | Do Role-Playing Agents Practice What They Preach(2507.02197);~~When Agents Say One Thing and Do Another(2602.06286)~~ **⚠️ FABRICATED**(2026-07-02 修正:此 ID 在 arxiv export API 返回 NOT FOUND,标题短语全文检索零结果——为 WebSearch 注入的伪造文献);*AI Review* 效度 critical review(Larooij & Törnberg 2025) | 成熟活跃领域 |
| **C. 单源操控集体表达** | Nature Sci Rep persuasion-driven adversarial(单 agent 降准 10–40%、增错误共识 30%+);The Consensus Trap(2604.17139,注入+防御);AgentAuditor(2602.09341) | 完整"操控+防御"弧线已做 |

加上前一轮已确认被占:**provenance 修复**(MemClaw/MemIR/LLM-MAS 综述)、**entrenchment**(Delayed-Verification 2606.27409 有闭式解)、**遗忘解固化**(Thaw H1 自身 n=5 negative)。

## 元判断:整个区域红海,首创窗口已关

**不是没找到对的框架,是整片"LLM agent society 的信念 / 言行 / 保真 / 操控"在 2024–2026 这波热潮里被填满了。** 我们想到的每一个角度——现象、机制、解法、效度、操控——都有 1–3 篇在先或并发工作,有的更早、有的更强(闭式解 / CHI / Nature)。在此再切缝 = 红海里找缝,做不出"让人 excited 的首创工作"。

## 准绳 4 的价值与教训

一轮三搜,挡住了"在解离/操控方向再堆 C18–C25、最后发现全被做"的巨大浪费。**教训:这轮搜索该在 C1 之前做。** 5-Telephone 把大量精力堆进实验(C1–C17)、APM、曲线、LaTeX、论文——若先做确认,能省下绝大部分。已写进准绳 4:**新课题第一步就搜,不是第 N 步。**

## 战略选择

1. **低野心收尾** —— 已有干净结果(严谨 sim + 负结果 + PROV 对照 + APM 对抗)作为诚实小贡献投 workshop/短文。**保底,不 excited。**
2. **换赛道(推荐)** —— 离开这片红海。真正的可迁移资产不是任何一个 claim,而是**一套能精细控制+测量多 LLM 交互内部状态的实验平台 + 严谨方法论**。用它去碰一个**还没被这波热潮填的问题**。
3. **封存** —— 承认沉没成本,5-Telephone/7-Thaw 作为经验封存。

## 可迁移资产盘点(供"找新赛道")

- **平台能力**:单/多源注入、多轮点对点传播、逐 agent 逐轮 **SAID 与 HELD 分离测量**、对抗性伪造注入、拓扑/连通/稀疏通信旋钮、多 provider(mini-FHL / ds-yunwu)、model2vec 检索、每次 run 自描述(`run_config.json`)。
- **方法论**:current/stale/unknown 三分类、LLM-judge 验证、多 seed + CI、pre-registered go/no-go、审计文化(injected 字段核查)、pool_runs n-扩展。
- **管线**:可复现 LaTeX(user-mode newtx,`paper/latex/BUILD.md`)、matplotlib 图表脚本、写作骨架。

## "找新赛道"的方法(准绳 4,下一轮系统做,不拍脑袋)

1. 列出"这套平台能碰的问题空间"(不限于 agent-society 信念);
2. 对每个候选,**先搜是否被填**(准绳 4);
3. 只保留 (真空白 ∩ 值得做 ∩ excited) 的,再投入实验。
4. **不在旧资产上找缝** —— 那是这次失败的根源(从解法倒推)。

## 当前状态

- **5-Telephone**:作为"首创 excited 论文"的目标**不可达**;待人定"低野心收尾 / 封存"。
- **7-Thaw**:H1 negative,已关。
- **下一步**:专门用一轮,以准绳 4 认真"找新赛道"——先找问题、先确认空白,再谈实验。

## 2026-07-02 修正

- **B 行 `2602.06286` 标注为 FABRICATED**。三重验证:arxiv export API `id:2602.06286` → NOT FOUND;标题短语全文检索 → 零结果;topic 检索 "preference falsification" + "pluralistic ignorance" + LLM → 零结果。该文献来自 WebSearch 通道的对抗注入——伪造 ID + 伪造标题 + 伪造 URL。已在行内标记。
- 此次修正源自 2026-07-02 的 arxiv first-party 验证 + neighbor-verification 扫描(详见 `preference_falsification_scan_2026-07-02.md`)。
