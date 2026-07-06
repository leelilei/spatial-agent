# 红海判决审计(2026-07-06)——终版:一手核验后的裁定

> 触发:人质疑「tele 做了那么多实验就没意义了吗?你复核过实验吗?真的在红海里吗?」
> 背景:06-30/07-01 判决依赖 WebSearch,而该通道 07-02 实锤会注入伪造文献。
> 本审计:(一)逐行重读实验台账;(二)对判决全部承重引用做 export.arxiv.org
> 一手核验(https 直连,阳性对照 69534 条通过)。**状态:已完成。**

## 一、实验台账复核(2026-07-06)

逐行重读 `RESULTS.md`(M0–C17b)。**实验资产是完整、经审计、自我纠错的科学弧线:**
现象跨场景/能力/persona/拓扑;解离 judge 验证 99–100%;三次主动撤回假信号(P1-rec、
M1、M2);C3 fair-PROV 8/8 seed CI 分离;C14 跨模型族 n=8 CI 分离;C16 对抗 stale=0
vs PROV 崩溃;C17b S 曲线全程 stale=0。另:文献底座 58 篇一手全文 + 54 篇精读。

## 二、承重引用一手核验(全部完成)

| 引用 | 核验结果 | 精确射程(关键) |
|---|---|---|
| MemClaw | ✅ **真实** 2606.24535 "Governed Shared Memory for Multi-Agent LLM Systems" (06-23) | **中心化共享记忆服务**(fleet-memory 治理原语:scoped retrieval、temporal supersession、provenance tracking)。命名 stale propagation / provenance collapse。系统论文 |
| MemIR | ✅ **真实** 2605.25869 "Mitigating Provenance-Role Collapse…Typed Memory" (05-25) | **单 agent** 长期记忆架构,source-monitoring 作结构约束,evidence/claims 分离 |
| Delayed-Verification | ✅ 真实 2606.27409 (06-30) | verifier/critic 共识系统的延迟纠正,grounded Laplacian 闭式失稳阈值。**工程化共识网,非自然对话社会**;我们的 entrenchment 已自撤,此格不再承重 |
| BeliefMem | ✅ 真实 2605.05583 | **单 agent** 部分可观测下的概率记忆 |
| PIMMUR | ✅ 真实 2509.18052 | 方法论审计(39 studies 六缺陷)——**对我们有利**(自然对话满足 minimal-control) |
| Traces to Trust | ✅ 真实 2606.04990 | execution-provenance 综述,外围 |
| Consensus Trap | ✅ 真实 2604.17139 | **任务求解聚合**(majority voting)的对抗注入与 token 级防御,非社会信念传播 |
| AgentAuditor | ✅ 真实 2602.09341 | 推理树审计 vs 多数票,任务求解聚合 |
| Spark to Fire | ✅ 真实 2603.04474(PDF 在手) | 谣言注入攻防 + 中心化 lineage-graph 治理插件;5 条已存档差异 |
| Persona Inconstancy | ✅ 真实 2405.03862 | say≠私下意见(conformity),无 do、无解药、无架构对比 |
| PushBench / Who&When / Agent Drift | ✅ 全真实 2605.23574 / 2505.00212 / 2601.04170 | goal-drift 与 failure-attribution 判决的砖也全为真 |
| "When Agents Say One Thing…" 2602.06286 | ❌ **唯一伪造**(07-02 实锤) | 07-01 B 行少一块砖,但 B 行另有真实工作(2507.02197) |

**核验结论:12 块承重砖,11 真 1 伪。判决的证据基础基本为真;
本审计此前对 MemClaw/MemIR 的"高度可疑"怀疑被一手证据否定,予以纠正。**

## 三、终局裁定

1. **红海判决的实质成立,但力度措辞需精确化:是"被包围",不是"被占据"。**
   - "provenance 当解药"作为**卖点**:确认拥挤(MemClaw/MemIR/survey/Spark to Fire
     四面压住思想空间)→ 06-30 判决维持:以 PROV/APM 为卖点会被淹没。
   - "say≠believe 解离"作为**卖点**:被 Persona Inconstancy(早一年)压住 → 维持。
   - **但没有任何一篇占据我们的精确格子**:去中心自然对话社会 + 每-agent 记忆 +
     分离引出的 SAY vs HELD + 7 记忆架构横评 + 对抗撒谎者 + 稀疏通信均衡曲线。
     占据者们分别是:单 agent 记忆(MemIR/BeliefMem)、中心化服务(MemClaw)、
     工程共识网(Delayed-Verif)、任务聚合(ConsensusTrap/AgentAuditor)、治理插件
     (Spark to Fire)、风格漂移(Telephone Game)、无 do 无解药(Persona Inconstancy)。
2. **实验没有白做。** 三条价值通道:(a) 以"组合"紧位定位,可写一篇诚实的
   中档论文(focused venue / strong workshop)——不是旗舰首创,但是可辩护的真贡献;
   (b) 方法论(分离引导、审计文化、go/no-go、多 seed)已成为 6-city 的骨架;
   (c) SAID/HELD 分离测量直接复用进 6-city Family D(say/do/think)。
3. **战略排序不变**:主线 = 6-city(格子开放 + 发现在手 + 硬证据体制);
   Telephone = 有界收割(组合定位论文,野心校准为中档);PF → Family D v2 种子。

## 四、方法论教训(写进准绳执行细则)

- **承重引用必须一手核验(id+摘要语义一致),WebSearch 只提供线索不提供判决。**
  本次 12 砖 11 真,说明通道污染是**低频、定向**的——对策不是不信一切,
  而是"判决级引用必须一手"这一条纪律。
- 判决措辞要区分"被占据(occupied)"与"被包围(encircled)":前者杀死方向,
  后者杀死的是**某种卖点措辞**,组合贡献仍可定位。
- 阳性对照 + https 直连 + id_list 端点 = 标准核验姿势(http 会 301 到 https,
  裸 curl 不带 -L 会拿到空 body——本次踩坑记录)。
