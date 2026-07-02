# 找新赛道(第一轮)——候选 A 判定 + 问题空间地图 v0(2026-07-02)

> 承接 `direction_verdict_2026-07-01.md`(整片"LLM agent society 的信念/言行/保真/操控"红海,
> 首创窗口已关;战略 2 = 换赛道)。本文档存档"换对象域、系统找新赛道"的第一步:按准绳 4
> 先搜候选机制 A、得出元判断、并产出问题空间地图 v0。**决策(2026-07-02):人选"换对象域,
> 系统找新赛道"。**

## 候选 A(goal-drift 动力学)判定:红海,且被"我们想做的确切形态"占

用户此前提出还想做 Telephone 式"钻研一个方面的技术"(深钻一个机制)。我提的第一个候选交点 =
"goal-drift 动力学 + 城市硬环境客观真值"。定向搜索(准绳 4)结果:这是一个已成链的活跃子领域
(2025–2026),四段全满:

- **现象+分类**:semantic / coordination / behavioral drift,task-drift vs reasoning-drift
  —— Agent Drift (arXiv 2601.04170)、Emergent Mind: Agent Drift。
- **多轮语境漂移均衡分析**:Drift No More? Context Equilibria (arXiv 2510.07777)。
- **理论形式化**:Shahnovsky & Dror 2026,POMDP 证明 step-by-step agent 因弱长程规划特别易漂移。
- **缓解**:收敛到 hierarchical planning + goal re-anchoring(arXiv 2603.19685;Zylos 2026-04-03)。
- **最致命**:Push Your Agent (arXiv 2605.23574) 提出 Quantitative Goal Persistence (QGP) +
  PushBench,用 **external verifier-backed work units** 直接测 progress drift / false completion。
  **这恰好就是我提的"Telephone 手法 + 硬环境客观真值 + 目标持久性测量"那个交点。**

## 元判断:连撞六次,是路径本身的问题

| 我们想的角度 | 在先/并发工作 |
|---|---|
| provenance 修复保真 | MemClaw / MemIR / 综述 |
| 说≠信 解离 | Persona Inconstancy (2405.03862, 早一年) |
| 单源操控集体 | Consensus Trap / Nature Sci Rep |
| entrenchment | Delayed-Verification(有闭式解) |
| 遗忘解固化 | Thaw H1 自身 n=5 negative |
| goal-drift(本轮) | PushBench/QGP、POMDP 形式化 |

不是"没找到对的机制",而是 **2024–2026 这波热潮把"拿 LLM agent 当研究对象、深钻它某个机制"
这条路系统性填满了**。每次胡同是同一条:在最热赛道里找缝。**准绳 4 现在拦的不是某个机制,而是
"再挑第 7 个机制"这个动作本身。** 因此不再顺手搜 B/C/D 堆判定(那仍是在旧资产找缝——失败根源)。

## 换对象域的筛选标准(避免又撞红海)

一个候选要同时满足:
1. **不是"把 LLM agent 当对象深钻它某个通用机制"**(已连撞六次);
2. **有客观/环境硬真值**(绕开 Telephone 软判据效度陷阱);
3. **恰好契合我们独特资产**(逐 agent 逐轮 SAID/HELD 分离测量 + 精细注入 + 对抗伪造 + 拓扑旋钮)
   —— 但**问题驱动**,不是能力倒推。

## 问题空间地图 v0

| # | 候选问题域 | 核心问题 | 为什么可能空白 | 红海风险预判 |
|---|---|---|---|---|
| C1 | 惯例/协议自发涌现与锁定 | 无中央协调时群体自发通信惯例如何被早期少数锁定 | 路径依赖是强项 | **高**——Ashery et al. 2024(Science Adv,LLM 群体自发语言惯例+临界质量)已开山 |
| C2 | 人-agent 混合信息系统 | 混入真人(硬锚)后信念传播/操控动力学如何改变 | 真人=硬真值;"混合 society 保真"具体缝可能没满 | **中**,需搜 |
| **C4** | **多 agent 集体错误的因果可归因性** | **出错时能否从交互 trace 客观定位"谁的哪句话导致了集体错误"** | **已有 injected ground-truth + adversary + 审计,天然能做因果归因;作为测量科学可能还空** | **中低**,最值得搜 |
| C5 | agent society 涌现量的标度律 | society 规模/拓扑与某涌现量的 scaling 关系 | 系统做标度的人少 | 未知,需搜 |
| C3 | agent 经济体隐性合谋/公平 | 有真实支付函数时的策略涌现 | 硬真值(支付) | **高**——LLM algorithmic collusion 2024-25 已热 |

## 下一步(准绳 4,先搜空白)

- 优先级:**C4(集体错误的因果可归因性)** > **C2(人-agent 混合硬锚)**;C4 把 APM/审计/对抗
  资产从"工具"翻正成真科学问题("多主体系统集体错误的因果责任能否客观归因"),契合"诊断+解药+
  架构"框架,又非保真红海。
- 方式:**串行搜**(省预算、避限流),各跑一遍"先确认空白",再回来给判定。
- **不在旧资产找缝**;只保留(真空白 ∩ 值得做 ∩ excited)的候选,再谈实验。

## 当前状态

- 5-Telephone / 7-Thaw:首创目标不可达(见 direction_verdict);待"低野心收尾 / 封存"择机处理。
- 新赛道:方向域已定为"换对象域";C4/C2 待搜确认空白。
