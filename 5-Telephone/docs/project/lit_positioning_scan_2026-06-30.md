# 定位风险调研 —— Telephone 在 2025–2026 文献中的位置(2026-06-30)

> 触发:human 的根本质疑 ——「我们最大的贡献是把 GA 社会传输的真相率提升了。在 society
> research 里这真的重要吗?是不是工具化、甚至冗余?如果意义不在 GA-society,该锚定哪?」
> 本文档存档一轮真实文献调研(WebSearch, 2026-06-30)的结论,作为方向决策依据。

## 结论(一句话)

**我们以为的"新维度"(多 LLM 系统的事实保真 + provenance 修复)在 2025–2026 已经相当拥挤,
且有几篇在先/并发工作直接覆盖了我们的核心贡献,有的还更强(闭式解)。继续以 PROV/APM 为
卖点会被淹没。唯一可能未被覆盖的核心点是 SAY≠HOLD 解离 —— 需进一步确认。**

## 直接撞车的工作

| 工作 | 它做了什么 | 与我们的关系 |
|---|---|---|
| **Delayed Verification Destabilizes Multi-Agent LLM Belief**(arXiv 2606.27409, 2026-06) | false claim 在 agent 图上传播,延迟共识 + grounded corrector;**纠正时机的闭式失稳阈值**("纠正太强/太晚→震荡");hallucination snowballing | **≈ 我们的 entrenchment(晚期纠正失败),但有数学闭式解,比我们的实验更强**。同期。 |
| **MemClaw**(governed shared memory w/ provenance) | 命名四失败模式:**stale propagation、provenance collapse**、contradiction persistence、leakage | **= 我们的核心现象 + PROV 修复方向** |
| **MemIR**(typed memory + source monitoring) | "provenance-role collapse";架构分离 raw evidence / claims;只有 supported claim 可 truth-authorized | **≈ APM 的可审计 + 证据/主张分离** |
| **Memory in LLM-MAS(survey)** | "Provenance is crucial — track author/timestamp/confidence/evidence;冲突时 inspect provenance 决定保留谁" | **我们 PROV 的核心思想已是综述里的 established principle** |
| **BeliefMem**(arXiv 2605.05583) | probabilistic memory,保留多个候选结论 + 概率,避免 self-reinforcing error | ≈ 我们 abstain / 多源佐证的思路 |
| multi-agent debate/verification(AutoGen, ChatEval, Truth in Debate) | agent 互相挑战过滤幻觉 | 覆盖"对抗/纠错"那一面 |

## 奠基与方法论邻居(框架已被占)

- **When LLMs Play the Telephone Game**(Perez et al., arXiv 2407.04503, 2024) —— 奠基性。
  transmission chain,测 **text properties 演化(toxicity/length/style)+ attractor**。
  注意:**测的是风格漂移,不是有 ground-truth 的事实保真** —— 这是和我们的一个真实区别。
- **LLM as a Broken Telephone**(arXiv 2502.20258, 2025) —— iterative generation 扭曲信息(链式)。
- **PIMMUR Principles**(arXiv 2509.18052) —— 批评 telephone-game 实验"指示 agent 准确转述"
  违反 minimal-control(测的是任务服从,非真实保真)。**对我们有利:我们用自然对话,避开此批评。**

## 我们可能仍然独特的点(待确认)

1. **SAY ≠ HOLD 解离** —— 把 agent **嘴上说的(utterance)**与**私下持有的(probed belief)**
   分开测,并证明权威干预改 SAID 不改 HELD。**在本轮所有结果里都没看到。** 但需再确认
   (可能有人用 sycophancy / stated-vs-internal belief / faithfulness 术语做过)。
2. **自然对话设定** —— 不指示 agent 准确转述,恰好满足 PIMMUR 的 minimal-control。方法论加分,
   非主贡献。
3. **事实保真(current/stale/unknown)而非风格漂移** —— 区别于 Perez 2024 那条线,但和
   MemClaw/2606.27409 的"事实/belief"重叠。

## 残酷判断

- 在 **"用 provenance 修复多 agent 事实保真"** 框架里,我们不是开拓者、不在并列前沿。
- 现象、provenance 修复、纠正时机失稳 —— 都被在先/并发覆盖,有的更强。
- **若坚持 PROV/APM 卖点 → 被淹没。**

## 下一步决策点

先做一轮**决定性确认搜索**:SAY≠HOLD 解离是否独特(stated-vs-internal belief / sycophancy /
faithfulness multi-agent),并顺带探"**遗忘解固化**"(7-Thaw 方向)是否有人做。两种结局:

1. **解离未被做** → Telephone 整篇重心转到**解离(诊断)**,PROV/APM 降级为机制证据。
   卖点:"agent 集体会**说真话但不持有真话**" —— 未被 provenance 工作覆盖,能立住。
2. **解离也被做 / 仍嫌拥挤** → 当前 framing 下 Telephone 基本被前沿吞没;认真考虑把力气
   转向 **7-Thaw(遗忘解固化)** —— 本轮调研里**没看到有人做**,可能是更空的坑。

## Sources(2026-06-30)
- When LLMs Play the Telephone Game — arXiv:2407.04503
- LLM as a Broken Telephone — arXiv:2502.20258
- Delayed Verification Destabilizes Multi-Agent LLM Belief — arXiv:2606.27409
- From Agent Traces to Trust (evidence/execution provenance) — arXiv:2606.04990
- BeliefMem — arXiv:2605.05583
- Memory in LLM-based Multi-agent Systems (survey) — techrxiv 1367390
- PIMMUR Principles — arXiv:2509.18052
