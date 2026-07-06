# 6-city 方向确认终判(2026-07-04)

> 承接人的核心质疑:「我们一定要做人工标注吗?这个这么重要吗?」→ 先按准绳 4
> 做方向复核,再决定要不要为 v1 freeze 投入人工审计。本文档存档这一轮的一手
> 文献确认结果与战略判断。方法对齐 `5-Telephone/docs/project/direction_verdict_2026-07-01.md`。

## 方法(践行准绳 4 + 上次教训)

- 一手 arxiv `export.arxiv.org/api` 查询,**不依赖 WebSearch**(5-Telephone 曾被 WebSearch 注入伪造文献 `2602.06286`)。
- 下列三篇新并发工作的 arxiv ID 与摘要均通过 `id_list` 端点一手核实,非二手转述。

## 一手复核:邻居很密,但核心格子仍开放(2026)

CityAgency 自己的对比文档(`cityagency-reference-benchmark-comparison-2026-06-27.md`)已**诚实承认**:
卖点不是任何单一组件新,而是「组合新」——one controlled urban episode + state-changing evidence。
组合型 benchmark 最容易被审稿人判「增量」。本轮搜索检验:那个「组合格子」是否已被占。

| 并发工作 | arxiv | 共享 CityAgency 的哪一条轴 | 判定(逐篇细看后) |
|---|---|---|---|
| **STT-Arena** | 2605.18548 (2026-05) | 可执行环境 + 注入时空扰动使计划失效 + 强制 replanning + **事后验证**(失败模式明列 "Missing Post-Adaptation Verification");227 任务 9 类冲突 4 级可解性;还训了 STT-Agent-4B 超过前沿模型 | **邻居,非占据者**:只共享扰动-重规划-验证这条轴;是 tool-use,无城市移动/私有居民目标/社交层,非城市接地 |
| **GenWorld** | 2606.27650 (2026-06) | building-level 合成城市 + 结构化 agent-环境接口 + **auditable replanning traces**;19.6 万居民、真实普查/地理数据接地、手机数据校验 | **邻居,非占据者**:是人口级聚合真实性(编译成 lookup policy),与「单 agent 私有目标证据契约」是两端 |
| **Trip+** | 2606.21169 (2026-06) | 分钟级行程生成/修订 + 环境驱动 replanning + 可行性/个性化/交互联合评估;18 模型;发现「模型偏好可行但反偏好的行程」 | **对照物,非占据者**:用 LLM-simulator 评主观体验 —— 恰是 CityAgency 证据契约要拒绝的验证方式 |

叠加对比表里**已知**的在先/并发工作:
- **When Plausible Is Not Realistic**(2026):直接拥有「plausible ≠ realistic urban」这个 headline —— 几乎就是 CityAgency 的论文标题概念。
- **MobiSim-Bench**(2026):18 队、967 agents 的挑战赛,拥有「城市 mobility agent 是否真实」。
- **FeasiGen / tau-bench / AppWorld / ChinaTravel**:拥有「不信自报完成、用权威状态验证」。
- **SOTOPIA / AgentSense / Misleading Success**:拥有「私有目标 + 信息不对称」。

## 元判断(2026-07-04 首判 → 同日修正)

**首判过重、已修正。** 初稿套用 5-Telephone 的红海模式,把这三篇当成「占了格子」。逐篇细看后
纠正:**它们各只共享 CityAgency 的一条轴,没有一篇占据精确格子**,且和本项目目标不冲突:

| 并发工作 | 共享的轴 | 关键差异(为何没占格子) |
|---|---|---|
| STT-Arena | 扰动→重规划→验证 | 是 tool-use,无城市移动 / 私有居民目标 / 社交层,非城市接地 |
| GenWorld | 受控接地城市仿真 | 人口级聚合真实性(19.6 万编译成 lookup policy),非单 agent 的证据契约 |
| Trip+ | 可行性+偏好+replanning | 用 **LLM-simulator 评主观体验** —— 恰是 CityAgency 证据契约要拒绝的验证方式,是对照物不是对手 |

**精确组合格子**(城市居民 + 私有意图 + 移动/可行性 + 确定性「环境-拥有的结果证据」+ 拒绝
叙述/抵达/自报/LLM-judge 代理 + 分级 replanning + 社交共现)**目前无直接占据者**。加上邻居
MobiSim / When-Plausible / MobilityBench 等,只能说明**这个问题域是热的、被公认重要**——对 benchmark
反而是利好(审稿人认这是活问题),不是判死。

**首判里两个「致命」论点也被修正:**

1. ~~benchmark 需靠规模/采用度取胜,单人打不过多队~~ —— **过度概括**。很多有影响力的 benchmark
   靠的是**锋利的 construct + 一个干净的意外发现**(tau-bench 的 pass^k 可靠性崩塌、WebArena 的
   14% vs 78%),不是靠 leaderboard 规模。CityAgency 可以靠「plausible↔verified 差距有多大」取胜。
2. ~~「又一个组合 benchmark」不 excited~~ —— 只有当卖点是「首个/权威 urban benchmark」时才弱;
   当卖点是「证据契约 construct + 实测差距」时并不弱。

**「benchmark vs 发现」是个假二分。** 一篇 benchmark 论文本来就是**交付这个发现的载体**。真正的
决策不是「做不做 benchmark」,而是**论文的 framing 重心与野心范围**:是 leading with
「the plausible-verified gap, measured」,而不是 leading with「the first urban benchmark」。

## 已有的真实发现(benchmark 的弹药)

> v1-rc1 external-adapter 实验(4 官方框架 × 4 压力场景)显示:`task_completion`(环境-证据)
> 与 legacy 加权 goal **系统性背离**——SOTOPIA 全程发消息却无人真的碰面;无一框架产出被环境
> 接受的 meeting interaction。这是一个可度量的「计划合理性 vs 环境可验证结果」差距。

这既是 benchmark 的核心 headline,也是发现本身——两者同一。

## 战略选择(供人定夺,修正版)

1. **继续做 benchmark,但按「证据契约 + 差距发现」定位(推荐)** —— 保留 CityAgency 作为
   benchmark,不卖「首个/权威 urban benchmark」,而是 leading with「环境-拥有的证据契约」这个
   construct 和「plausible↔verified-outcome 差距」这个实测结果。Related work 对上述邻居做**紧位**
   区分(每条 novelty 收窄)。复用全部已建资产。
2. **换赛道** —— 若判 benchmark 采用度战争不值得打,带方法论去碰未被填的问题(需再一轮空白确认)。
3. **低野心收尾 / 封存** —— 现有 rc1 作为诚实小结存档。

三者中 (1) 与人的直觉一致(准绳:solve problems, don't abandon;aim for big Claim A),
且与已建资产、已有发现最契合。

## 人工标注的定位(回答人最初的问题)

无论走 (1) 还是把发现单独拎出,**人工标注都值得做,但它是「证明 verifier ≈ 人判」的可信度校验,
不是唯一命门**。16 条 × 2 人成本极低(人自己可当一名标注员)。它证明的是证据契约不是自定义的
任意数,而是和人类判断一致——这是 construct validity 的硬证据,benchmark 路线尤其需要它。
所以答案:重要、值得做、但没到「不做就一切归零」的程度。

## 当前状态

- **精确组合格子**:经一手复核(STT-Arena / GenWorld / Trip+ 逐篇核),**仍开放**,无直接占据者。
- **benchmark 路线**:可行;卖点应是证据契约 construct + 差距发现,而非「首个 urban benchmark」。
- **已有发现**:rc1 显示 task_completion 与 legacy goal 系统性背离 —— benchmark 的核心弹药已在手。
- **人工标注**:值得做的 construct-validity 校验,非唯一命门。
- **下一步**:待人在三选一(推荐 1);若选 1,则推进 16 条人工标注 + 收紧 related-work 紧位。

## 备注:一手核实的 ID(防伪造)

以下 ID 均通过 arxiv `id_list` 端点直接取回标题+摘要,本会话内核实:
2605.18548(STT-Arena)、2606.27650(GenWorld, urban 版,注意另有 2506.10975 同名不同题)、
2606.21169(Trip+)。对比表内其余文献沿用既有存档,未在本轮重新一手核。
