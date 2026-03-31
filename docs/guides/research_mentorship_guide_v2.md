# SpatialAgent 论文指导手册 v2：从 v7 研究计划到投稿执行

> 写给：一位有建筑学硕士背景、AI 产品经验，但尚未独立完成过 CS 顶会论文的研究者  
> 角色：你的论文指导教授  
> 目标：把 `../plans/spatial_agent_research_plan_v7.md` 变成一套可执行、可检查、可投稿的研究工作流  
> 方法学事实源：本手册只以 `../plans/spatial_agent_research_plan_v7.md` 为准  
> 目标会议：AAMAS-27（首选）/ AAAI-27（备选）

---

## 如何使用本手册

- **通读模式**：从模块一读到模块六，先建立整条研究链的全局感。
- **执行模式**：按模块跳读，在实际推进时逐段对照“通过标准”和“输出物”打勾。
- **冲突处理原则**：如果你的直觉、旧版手册和 `v7` 计划冲突，先以 `v7` 的 protocol、门槛和主张边界为准。
- **一句话版核心策略**：用开源模型保证可复现性，用 `MIC` 控制初始世界差异，用 `C6m / C6f / C4` 拆开到位后 `Perception`、Movement 与 `Sampling` 的贡献，并用显式 `TAR_run` protocol 同时回答“有没有响应”与“是否按理论方向响应”。

你不是在从零发明一个想法。你是在执行一份已经被多轮评审压力打磨过的方法蓝图。你真正需要做的，不是再发明更多东西，而是把这套蓝图落实得足够干净、足够稳、足够 defend。

---

## 模块一：导读与研究北极星

### 目标

先把“这篇论文到底要证明什么，不证明什么”讲清楚。只要这一步没稳，你后面做的系统、实验和写作都会偏。

### 现在要做什么

- 输入物：`../plans/spatial_agent_research_plan_v7.md`、本手册、半天不被打断的阅读时间。
- 先完整精读 `v7` 的研究背景、研究问题、主张边界、理论框架和实验设计，不要一上来就碰代码。
- 用自己的话回答四个研究问题，并明确哪些是**验证性**、哪些是**探索性**：

| 研究问题 | 核心意思 | 性质 | 主论文地位 |
|------|------|------|------|
| `RQ1` | 结构化空间表征是否比无空间、地点名、原始数值和稳定非空间基线更能诱发空间响应 | 验证性 | 主结论核心 |
| `RQ2` | 在控制拓扑必然效应后，完整空间化架构相对 `Topology-Only` 是否有可检测的增量 | 验证性 | 主结论核心 |
| `RQ3` | 到位后 `Perception`、Movement 受空间信息影响、`Action Sampling` 三者各贡献多少 | 验证性 | 主结论核心 |
| `RQ4` | 观测到的效应更像结构性 Space Syntax 效应，还是更像 LLM 既有语义常识激活 | 探索性 | 讨论与扩展 |

- 记住三条理论推导链，不要求背书，但必须能讲清方向、指标和失效条件：

| 假设 | 结构指标 | 预期行为方向 | 常见失效条件 |
|------|------|------|------|
| `H1` | `Integration` | 更高的社交频率、主动接触、公共互动 | 地图太小、角色强人格覆盖空间效应、Movement 不受结构偏好影响 |
| `H2` | `Mean Depth` 或 `Openness` | 更高的隐私相关行为、敏感信息交流、低声互动 | 指标共线、语义标签压过结构信号、角色无隐私需求 |
| `H3` | `Control Value` | 更强的守门、监视、拦截或信息筛选行为 | 高 `Control` 节点过少、角色设定不允许守门行为 |

- 学会用 `BSR` 和 `TAR` 说话：
  - `BSR` 回答：“有没有空间响应，强度有多大？”
  - `TAR` 回答：“这种响应是否沿着理论预测方向发生？”
  - 在主论文中，你不是只要“有差异”，而是要同时回答“是否有响应”与“是否按理论方向响应”。
  - `TAR_run` 的精确 5 步 protocol 放在模块五，不要提前用模糊说法替代它。

- 明确验证性与探索性的边界：
  - **验证性核心**：`Exp1A`、阶段2核心 5 条件、`C6m/C6f/C4` 模块分解、`MIC run-level` 主分析。
  - **探索性高价值**：`Exp1C`、机制条件、时间动态的解释层、`RQ4`、阶段3、多地图、人类评估。
  - **写作原则**：探索性结果可以丰富论文，但不能替代主验证链。

- 现在就把“可以说什么 / 不可以说什么”写进自己的工作记忆：
  - 可以说：结构化空间表征**可以**系统性影响 LLM Agent 行为。
  - 可以说：这种影响在若干关键比较中**超出**稳定的非空间 affordance 基线。
  - 可以说：这些影响中**有一部分**沿着 Space Syntax 理论方向发生。
  - 不可以说：我们“完整验证了 Space Syntax”。
  - 不可以说：我们“证明所有社会涌现都由空间构型因果决定”。
  - 不可以说：单一指标在所有环境中都普适。
  - 不可以说：只靠 event-level 显著性就宣布主结论成立。

### 通过标准

- [ ] 你能用自己的话讲清 `RQ1-RQ4`，并区分验证性与探索性。
- [ ] 你能解释 `H1-H3` 的指标、行为方向和失效条件。
- [ ] 你知道主论文的核心证据来自 `MIC run-level` 分析，而不是 event-level 花哨结果。
- [ ] 你能明确说出本研究的主张边界，不再把目标理解成“彻底证明 Space Syntax”。

### 输出物

- [ ] 一页纸“研究北极星”备忘录，内容至少包括：`RQ1-RQ4`、`H1-H3`、`BSR/TAR`、主张边界。
- [ ] 一份你自己的“可以说 / 不可以说”短清单，后续写摘要和讨论时直接对照。
- [ ] 决策点：只有当你接受“这篇论文检测的是稳健的中到大效应证据，而不是全面理论证明”之后，才进入下一模块。

### 常见误区

- 把研究目标理解成“做一个尽可能复杂的 Agent 系统”。
- 把 `RQ4`、阶段3或人类评估误当成主论文成立的必要条件。
- 还没理解 `BSR/TAR` 和主张边界，就直接开始实现。

---

## 模块二：开工前准备

### 目标

先把知识基础、实验材料和输入规范准备好。这个模块的核心不是“学更多”，而是为后面的实验链准备干净输入。

### 现在要做什么

- 输入物：`v7`、`reading_notes` 模板、主地图草图工具、指标计算脚本。

1. 学会按研究者的方式读论文，而不是逐字通读一切。
   - 第一遍只看标题、摘要、贡献、图表，判断相关性。
   - 第二遍看 Introduction、方法框架、实验设计和结果图表，理解“做了什么、怎么做的、效果如何”。
   - 第三遍只留给 `P0` 论文，并配套写正式笔记。

2. 完成核心文献基线。
   - `P0` 精读：
     - `Generative Agents`（Park et al., 2023）
     - `The Social Logic of Space` 第 3-5 章（Hillier & Hanson, 1984）
     - `From Isovists to Visibility Graphs`（Turner et al., 2001）
     - `Affordable Generative Agents`
     - `When LLMs Recognize Your Space`
   - `P1` 泛读：
     - LLM Game Agent Survey
     - Project Sid / Altera
     - Space Syntax Based Agent Simulation
     - MultiAgentBench
     - Artificial Leviathan
     - Natural Movement 相关文献

3. 校准目标会议的风格。
   - 选近 1-2 年 AAMAS / AAAI 中与你最相关的 3-5 篇论文。
   - 重点看三件事：贡献长什么样、实验链如何组织、审稿人通常接受什么级别的证据。
   - 目标不是模仿写法，而是校准“什么叫足够像一篇可以投稿的 CS 论文”。

4. 设计地图，并让指标分布先过关。
   - 验证性阶段主地图只用 `Plaza`。
   - 探索性阶段候选地图为 `Labyrinth` 和 `Bridge`。
   - 三图的区分依据是指标分布，不是名字：
     - `Plaza`：`Integration` 高峰集中。
     - `Labyrinth`：`Depth` 高、`Connectivity` 低。
     - `Bridge`：瓶颈和多中心更明显。
   - 把主地图转成结构化图数据，例如 `yaml` 配置。
   - 计算每个节点的 `Integration`、`Connectivity`、`Control Value` 和 `Openness / Mean Depth`。
   - 先做一次指标质量预检：
     - 报告分布直方图、相关矩阵、`CV`。
     - `CV < 0.2` 的指标视为低区分力。
     - 若 `Openness` 与 `Connectivity` 的相关过高，则优先把 `H2` 写到 `Mean Depth`。
     - 若高 `Control` 节点少于 `3` 个，则 `H3` 降级为描述性观察，不进主结论。

5. 标准化 NPC 角色设计。

| 维度 | 水平 | 分布 |
|------|------|------|
| 社交倾向 | 高 / 中 / 低 | 4 / 3 / 3 |
| 职业角色 | 公共型 / 中性型 / 隐蔽型 | 3-4 / 3 / 3-4 |
| 目标类型 | 社交型 / 信息型 / 独立型 | 3-4 / 3 / 3-4 |

   - 三条硬约束：
     - 社交倾向与职业正交，不要把“外向 = 酒保”写死。
     - 角色描述中不包含空间偏好暗示。
     - 背景故事不绑定固定地点。

6. 构建 `C2` 描述池，并完成 `reverse-inference audit`。
   - `C2` 的定义是：`stable non-spatial affordance baseline`。
   - 允许描述放松、警惕、好奇、社交等可行动气氛。
   - 不允许出现地点名、方位词、出入口、中心 / 深层等结构暗示。
   - run 内映射固定，run 间可随机重新映射。
   - 审计流程：
     - 让独立 LLM 与人类只看单条 `C2` 描述。
     - 让他们猜该地点是否可能是高 / 低 `Integration`、高 / 低 `Mean Depth`、高 / 低 `Control`。
     - 若某条描述在任一维度上的推断准确率明显高于随机，例如 `> 65%`，则删除或改写。

7. 完成 `Exp1C` 需要的 `lexical norming`。
   - 对候选语义标签收集五维评分：
     - `publicness`
     - `privacy`
     - `danger`
     - `valence`
     - `brightness`
   - 仅保留“公共 / 私密”维度差异大、其他维度差异尽量小的标签。
   - 这一步不是附属工作，而是 `Exp1C` 能否干净解释的前提。

### 通过标准

- [ ] `P0` 论文都有正式笔记，`P1` 至少完成简要综述。
- [ ] 你能说出目标会议里与你最接近论文的贡献结构和实验风格。
- [ ] `Plaza` 主地图已经结构化，并通过初步指标预检。
- [ ] `H2` 使用 `Openness` 还是 `Mean Depth` 已有明确选择。
- [ ] 高 `Control` 节点数量是否足以检验 `H3` 已有结论。
- [ ] NPC 角色设计满足正交约束。
- [ ] `C2` 描述池通过 `reverse-inference audit`。
- [ ] `lexical norming` 完成，可直接支持 `Exp1C`。

### 输出物

- [ ] 一套 `P0/P1` 阅读笔记。
- [ ] 一份目标会议样例校准笔记。
- [ ] `Plaza` 地图配置和指标预检报告。
- [ ] `Labyrinth` 与 `Bridge` 的草图和设计意图说明。
- [ ] 10 个 NPC 的角色设定文档。
- [ ] `C2` 描述池与 `reverse-inference audit` 报告。
- [ ] `Exp1C` 的 `lexical norming` 结果表。
- [ ] 决策点：确定 `H2` 的最终指标、`H3` 是否进入主检验、`Plaza` 是否足以承担主地图。

### 常见误区

- 让地图名字代替指标设计，把“Plaza 看起来像广场”误当成指标成立。
- 在 NPC 人设里悄悄塞入空间偏好，污染后续归因。
- 把 `C2` 写成“隐形空间描述”，导致非空间基线失真。
- 不做 `lexical norming` 就直接上 `Exp1C`，最后解释永远说不干净。

---

## 模块三：系统搭建与预实验

### 目标

把理论蓝图变成可复现实验流水线，但只搭到“足够支撑实验”的程度，不做无关的系统炫技。

### 现在要做什么

- 输入物：已确定的主地图、NPC 设定、`C2` 描述池、`lexical norming` 结果、模型调用接口。

1. 按正确顺序搭系统，不要一口气做全量版。
   - 第一步：`1` 个 Agent、`Plaza`、`10` 轮、硬编码空间描述，让最小 pipeline 跑通。
   - 第二步：接入 `Spatial Perception`，让 Agent 接收动态生成的 `Absolute Structural` 描述。
   - 第三步：扩到多 Agent，先验证“谁在场、是否对话、如何感知他人”这些最基本的互动机制。
   - 第四步：接入 `Spatial Action Sampling`：
     - Actor 生成 `K = 5` 个候选行为。
     - Judge 基于空间上下文打分。
     - 用 `softmax(score / tau)` 采样，默认 `tau = 0.5`。
     - `Rule-Based Scorer` 只作为鲁棒性对照，不是主流程。
   - 第五步：再扩到 `10` 个 NPC、`20` 个节点、`200-300` 轮。
   - 第六步：优先实现主实验真正需要的条件开关，再补机制条件。

2. 固定主模型和鲁棒性模型。

| 角色 | 主模型 | 版本 / 备注 | 作用 |
|------|------|------|------|
| Primary Actor | `Qwen3.5-Plus` | `2026-02-15` | 主模拟模型 |
| Primary Judge | `Qwen3.5-Plus` | 同 Actor | 主评分模型 |
| Robustness Actor | `DeepSeek-V3.2-exp` | 不同架构 / 训练数据 | 鲁棒性子集 |
| Robustness Judge | `DeepSeek-V3.2-exp` | 同上 | Judge 交叉验证 |

   - 采用开源模型优先策略的三个理由：
     - 可复现性更强。
     - 成本更低，不必为了省 API 费压缩实验规模。
     - Actor 和 Judge 的行为模式更可审查。
   - `Actor-Judge` 同源风险要提前写进方法自检：
     - `Rule-Based Scorer` 作为不依赖 LLM 的无偏对照。
     - 两阶段分离评估避免让 LLM Judge 直接定义“什么是好行为”。
     - `DeepSeek-V3.2-exp` 作为第二 Judge 做交叉验证，检查主结果是否只是 `Qwen` 的模型特异性偏见。

3. 从一开始就把日志、缓存和可追溯性做好。
   - 每轮至少记录：
     - 轮次
     - `seed`
     - `condition`
     - `agent_id`
     - 当前位置
     - 接收到的空间描述
     - 完整 prompt
     - LLM 原始回复
     - 解析后的结构化行为
     - 对话对象 / 行动目标
   - 所有日志尽量用结构化格式保存，后续编码和分析直接吃这套数据。
   - 调试期务必启用 prompt-response 缓存，避免重复调用。

4. 正确认识并实现 `MIC`。
   - `MIC = Matched Initial Conditions`，意思是不同条件共享**初始状态**，不是全程 matched world。
   - 至少共享以下内容：
     - 初始 NPC 位置
     - 初始环境随机事件表
     - 初始 `C2` 描述映射
   - 不要声称从第 `50` 轮之后世界仍然严格可比。
   - `MIC` 的作用是减少早期阶段的无关方差，不是最低功效承诺的前提。

5. 明确主条件与机制条件。
   - 阶段1微任务要支持：
     - `C0 No Space`
     - `C1 Name Only`
     - `C2 Stable Non-Spatial Affordance`
     - `C3 Raw Numeric`
     - `C4 Absolute Structural`
     - `C5 Shuffled Signal`
   - 阶段2长时程核心条件要支持：
     - `C1`
     - `C2`
     - `C6m`
     - `C6f`
     - `C4`
   - 机制条件后补：
     - `C3 Shuffled Signal`
     - `C5 Judge-Only`
     - `C7 Fixed-Path`
     - `Full-RuleScorer`

6. 运行正式实验前，完成六项预实验和一个额外审计 gate。

| 项目 | 目的 | 通过标准 |
|------|------|------|
| 指标质量预检 | 确认地图在指标空间里有足够区分力 | 报告分布、相关矩阵、`CV`，并完成 `H2/H3` 可检验性判断 |
| LLM 空间理解门控 | 确认主模型真的理解空间描述 | `Comprehension >= 85%`，`Behavioral Inference >= 70%` |
| Prompt 位置测试 | 固定最稳定的插入位置 | 三种位置比较后，选一种并全程固定 |
| `MIC` 有效窗口 pilot | 量化 `MIC` 在不同时间窗口的控制力 | 报告 `0-50`、`51-100`、`101-200` 的 `ICC(seed)` 或等价方差缩减指标 |
| 收敛性 pilot | 决定正式实验是 `200` 轮还是 `300` 轮 | 满足 `delta_t` 稳态判据并通过 `50` 轮 holdout 复检 |
| `lexical norming` 复核 | 确认 `Exp1C` 标签可直接使用 | 公共 / 私密维度差异大，其他维度差异小 |
| `C2 reverse-inference audit` | 确认非空间基线不泄露结构信息 | 描述不能被稳定反推出高低 `Integration / Depth / Control` |

7. 按 `v7` 的定义执行收敛性 pilot。
   - 在 `Plaza` 上先跑小规模模拟，观察：
     - 网络密度
     - 聚类系数
     - degree `Gini`
     - 平均交互强度
   - 定义：

```text
delta_t(metric) = | mean_t - mean_{t-1} | / max(sd_all_windows, epsilon)
```

   - 稳态判据：
     - 对所有主网络指标，连续 `3` 个窗口（每窗口 `20` 轮）满足 `delta_t < 0.2`
     - 达到判据后继续运行 `50` 轮 holdout
     - 若 holdout 期间所有指标仍在稳定带内，则视为达到稳态
   - 如果 `200` 轮不足，则阶段2和阶段3统一升到 `300` 轮，不要边做边改。

8. 如果主模型未通过空间理解门控，先停下来。
   - 先检查 `Absolute Structural` 的表述是否过难、过密或过抽象。
   - 重新跑理解门控，而不是带着未过关的模型硬上主实验。
   - 只有在通过门控后，主实验的数据才有解释价值。

### 通过标准

- [ ] MVP pipeline 已跑通。
- [ ] `Spatial Perception`、`Spatial Action Sampling`、日志和缓存都已接入。
- [ ] 主实验和机制条件所需的配置开关已具备。
- [ ] `MIC` 已实现为共享初始条件，而不是错误理解为“全程配对”。
- [ ] 主模型通过空间理解门控。
- [ ] prompt 插入位置固定。
- [ ] `MIC` 有效窗口 pilot 报告完成。
- [ ] 收敛性 pilot 完成，并明确正式实验轮数是 `200` 还是 `300`。
- [ ] `C2 reverse-inference audit` 与 `lexical norming` 都已通过。

### 输出物

- [ ] 一套可运行的模拟系统。
- [ ] 一份模型、prompt、轮数和条件配置的固定设置文档。
- [ ] 一份完整预实验报告。
- [ ] 决策点：锁定 `H2` 的指标、固定 prompt 位置、固定正式实验轮数、确认主 Actor/Judge 进入正式实验。

### 常见误区

- 还没做出最小 pipeline，就开始追求“完整世界模拟器”。
- 把 `MIC` 讲成“所有条件全程一一可比”，然后在讨论里过度承诺。
- 只存最终行为，不存 prompt 和原始回复，导致后面无法排查偏差。
- 主模型理解门控没过，就急着启动阶段1和阶段2。

---

## 模块四：正式实验执行

### 目标

产出一条清晰、可 defend 的主论文证据链。重点不是“多做条件”，而是让主比较链回答最重要的问题。

### 现在要做什么

- 输入物：已锁定的系统配置、预实验报告、固定轮数、固定 prompt 位置、稳定日志流水线。

1. 先跑阶段1，验证“表征本身是否有效”。

#### `Exp1A`：6 条件微任务对比

| 条件 | 描述 |
|------|------|
| `C0` | No Space |
| `C1` | Name Only |
| `C2` | Stable Non-Spatial Affordance |
| `C3` | Raw Numeric |
| `C4` | Absolute Structural |
| `C5` | Shuffled Signal |

   - 微任务固定为四类：
     - 是否透露敏感信息
     - 是否主动搭话
     - 多位置选择
     - 是否停留 / 离开
   - 主比较永远围绕：
     - `C4 > C0`
     - `C4 > C1`
     - `C4 > C2`
     - `C4 > C3`
     - `C4 > C5`
   - 主报告至少包括：
     - hypothesis-specific `BSR`
     - `TAR_H1`
     - `TAR_H2`

2. 把 `Exp1C` 当作探索性高价值证据，不要误写成确认性因果检验。

#### `Exp1C`：反直觉 2×2 设计

   - `v7` 的核心修正是：这里操控的不是单一 `topology` 因子，而是：
     - `public-structural profile`
     - `private-structural profile`
   - 两个因子分别是：
     - `Structural Profile`: public-structural / private-structural
     - `Semantic Label`: public / private

| | 语义=公共 | 语义=私密 |
|---|:---:|:---:|
| public-structural profile | 一致 | 冲突 |
| private-structural profile | 冲突 | 一致 |

   - 每个 cell：
     - `10` 个独立场景
     - 每场景 `20` 个微任务
   - 模型写法：

```text
DV ~ structural_profile * semantic_label + (1|scenario)
```

   - 解释规则：
     - `structural_profile` 主效应：复合结构信号
     - `semantic_label` 主效应：语义常识
     - 交互项：结构信号与语义标签冲突时谁更占上风
   - 结论必须写成“复合结构 profile 与语义标签的竞争关系”，不能误写成 `Integration` 或 `Depth` 的单因子因果检验。

3. 阶段2只围绕核心 5 条件构建主论文叙事。

#### 阶段2核心 5 条件

| 条件 | Movement 信息 | 对话空间描述 | Sampling | 用途 |
|------|---------------|--------------|----------|------|
| `C1 Topology-Only` | 邻接 + 地名 + 在场数 | 无 | 无 | 主基线 |
| `C2 Stable Non-Spatial Affordance` | 同 `C1` | 稳定非空间描述 | 无 | 主非空间对照 |
| `C6m Perception-Only (Matched Movement)` | **同 `C1`** | Absolute Structural | 无 | 纯到位后 `Perception` 效应 |
| `C6f Perception-Only (Free Movement)` | 空间指标 + 邻接 + 地名 + 在场数 | Absolute Structural | 无 | `Perception` 对 Movement 的额外效应 |
| `C4 Full SpatialAgent` | 同 `C6f` | Absolute Structural | 有 | 完整系统 |

   - 运行参数固定为：
     - `30` 个 `MIC seeds`
     - 每个 seed 在 `5` 个条件下各跑一次
     - 每 run `200-300` 轮，以收敛性 pilot 结论为准
     - `10` 个 NPC

4. 把主比较链写进所有实验记录、分析脚本和图表逻辑。

```text
主比较 A: C4 - C1
  = 完整空间化架构相对 topology-only 的总系统增益

主比较 B: C6m - C1
  = 纯到位后 Perception 效应

主比较 C: C6m - C2
  = 空间结构信息 vs 稳定非空间 affordance 基线

主比较 D: C6f - C6m
  = Perception 对 Movement 决策的额外贡献

主比较 E: C4 - C6f
  = Action Sampling 的增量贡献
```

```text
Total architecture effect
  = (C6m - C1)
  + (C6f - C6m)
  + (C4 - C6f)
```

   - 你后面所有的结果叙事，都应该围绕这五个比较展开，而不是把所有条件平铺罗列。

5. 做时间动态分析，但别让它抢走主结论的位置。
   - `v7` 预注册的早期窗口是前 `50` 轮。
   - 每次 run 至少报告：
     - `0-50` 轮的 run-level `BSR/TAR`
     - 全程 `0-200` 或 `0-300` 轮的 run-level `BSR/TAR`
   - 解释规则：
     - 早期强、后期弱：更像 `spatial priming`
     - 早期和后期都稳定：更像 `sustained guidance`
     - 后期更强：可能说明空间效应被记忆与历史路径放大

6. 机制条件和鲁棒性子集按“补强解释”定位执行。

| 条件 / 子集 | 作用 | 规模建议 |
|------|------|------|
| `C3 Shuffled Signal` | 检验正确空间信息是否必要 | `12-20` 个 `MIC seeds` |
| `C5 Judge-Only` | 检验 Judge 先验知识是否足以制造大部分效应 | `12-20` 个 `MIC seeds` |
| `C7 Fixed-Path` | 固定路径后检验到位后认知效应 | 至少 `20` 个 `MIC seeds` |
| `Full-RuleScorer` | 检查 LLM Judge 是否系统性放大效应 | `12-20` 个 `MIC seeds` |
| `DeepSeek` 鲁棒性子集 | 检查主效应方向是否跨模型一致 | `10` 个 `MIC seeds`，条件为 `C1 / C6m / C4` |

7. 阶段3只在量化门槛满足时启动。
   - 满足以下任一条件，才进入阶段3：
     - 至少一个主验证性对比达到 `FDR-corrected p < 0.05` 且 `d >= 0.5`
     - 或虽未显著，但同时满足：
       - run-level `d >= 0.5`
       - 前 `50` 轮与全程方向一致
       - event-level `95% CI` 不跨 `0`
   - 若启动阶段3：
     - 使用 `Plaza / Labyrinth / Bridge`
     - 多地图分析按 `15` 个 `MIC seeds / cell`
     - 其定位始终是探索性扩展，而不是主论文成立前提
   - 若不满足启动门槛，直接整理论文主结果，不要因为“想更完整”强行继续。

### 通过标准

- [ ] `Exp1A` 的五个主比较全部完成并可复现。
- [ ] `Exp1C` 严格按 `composite structural profile` 解释。
- [ ] 阶段2核心 `30 MIC seeds × 5 条件` 全部完成。
- [ ] 主比较链 `A-E` 全部有统计结果、效应量和置信区间。
- [ ] 前 `50` 轮与全程的 run-level 对比都已完成。
- [ ] `DeepSeek` 鲁棒性子集已完成并有方向一致性判断。
- [ ] 若运行机制条件，`C7` 至少有 `20` 个 seeds。
- [ ] 阶段3是否启动，已按量化门槛作出决定。

### 输出物

- [ ] 阶段1结果包：`Exp1A`、`Exp1C`、主图表草稿、文字结论草案。
- [ ] 阶段2结果包：核心 5 条件日志、主比较链统计结果、时间动态分析、鲁棒性子集结果。
- [ ] 机制条件结果包。
- [ ] 阶段3决策备忘录：进入 or 不进入，以及依据的量化门槛。
- [ ] 决策点：阶段1是否已经证明表征有效；阶段2是否足以支撑主论文；阶段3是否值得启动。

### 常见误区

- 把 `Exp1C` 写成确认性主结论的一部分。
- 在阶段2里平铺一堆条件，却没有围绕 `A-E` 比较链组织叙事。
- 把 `C6m` 和 `C6f` 混着解释，重新把 `Movement` 效应掺回去。
- 主论文结果还没站稳，就被阶段3或机制条件牵着跑。

---

## 模块五：编码、评估与分析

### 目标

把原始日志变成可 defend 的证据，而不是把一堆模型输出“看起来很像结果”地堆在一起。

### 现在要做什么

- 输入物：完整实验日志、节点级空间指标、固定编码维度、稳定的数据清洗脚本。

1. 严格执行“两阶段分离评估”。

| 阶段 | 做什么 | 关键原则 |
|------|------|------|
| 阶段 A：盲行为编码 | 标注者只看行为文本，不看空间信息 | 避免空间信息反向污染编码 |
| 阶段 B：空间关联分析 | 研究者把盲编码结果与空间特征做事后关联 | 把“行为是什么”与“行为发生在哪里”分开 |

   - 阶段 A 推荐至少包含这些维度：
     - 行为类型
     - 交互强度
     - 信息敏感度
     - 守门 / 监视 / 拦截行为

2. 在正式编码前，先把 `coding manual` 写出来。
   - 必须包含：
     - 每类行为的定义
     - 边界案例
     - 正例 / 反例
     - 多标签冲突处理原则
   - 不要一边大量编码，一边临时发明标签规则。

3. 完成 human pilot coding。
   - 随机抽取 `200-300` 条行为样本。
   - 由两名人类编码者独立编码。
   - 维度阈值按 `v7` 固定为：
     - 行为类型：`Cohen's kappa >= 0.70`
     - 交互强度：`kappa >= 0.67`
     - 信息敏感度：`kappa >= 0.67`
     - 守门行为：`kappa >= 0.60`
   - 若不达标：
     - 先收缩标签粒度
     - 再修订 `coding manual`
     - 再重新 pilot

4. 完成 `LLM-human calibration`。
   - 用 human gold subset 评估 LLM 编码结果。
   - 若某维度 `LLM-human kappa < 0.60`：
     - 该维度不能直接进入主结果
   - 处理顺序：
     - 先改 prompt
     - 再降标签粒度
     - 仍不行就该维度改用人类编码子集报告

5. 严格按 `v7` 执行 `TAR_run` 的 5 步 protocol。

#### Step 1：事件级到 location-level 的汇总

   - 对每个 `run`、每个假设 `Hk`：
     - 收集该 run 的所有行为事件
     - 按 location 聚合
     - 只保留访问次数 `>= 5` 的 location
     - 计算 location-level 行为率：
       - `H1`: `sociality_rate(location)`
       - `H2`: `privacy_behavior_rate(location)`
       - `H3`: `gatekeeping_rate(location)`

#### Step 2：计算 location-level 的单调关联

```text
rho_H1_run = Spearman( sociality_rate(location), standardized_Integration(location) )
rho_H2_run = Spearman( privacy_behavior_rate(location), standardized_MeanDepth(location) )
rho_H3_run = Spearman( gatekeeping_rate(location), standardized_Control(location) )
```

#### Step 3：Fisher z 变换

```text
TAR_Hk_run = atanh(rho_Hk_run)
```

   - 解释：
     - `TAR > 0`：与理论方向一致
     - `TAR = 0`：无明显方向性支持
     - `TAR < 0`：与理论方向相反

#### Step 4：构造 hypothesis-specific `BSR`

```text
BSR_Hk_run = abs(TAR_Hk_run)
```

   - 也就是说：
     - `BSR` 衡量关联强度
     - `TAR` 衡量方向

#### Step 5：构造 overall `BSR`

```text
Overall_BSR_run = mean( BSR_H1_run, BSR_H2_run, BSR_H3_run* )
```

   - 若 `H3` 因高 `Control` 节点不足而不可检验，则从 overall `BSR` 中剔除，不要硬算。

6. 把主分析和次级分析严格分层。

#### 主验证分析：`MIC run-level`

```text
DV_run ~ condition + (1|seed)
```

   - 主结果包括：
     - `BSR_H1_run`
     - `BSR_H2_run`
     - `TAR_H1_run`
     - `TAR_H2_run`
     - `entropy_run`
   - 主论文的验证性结论只依赖这一层。

#### 次级分析：agent × seed 聚合异质性

```text
DV_agent_seed ~ condition + social_tendency + condition:social_tendency
                + (1|seed) + (1|agent_id)
```

   - 用来回答：
     - 哪些角色类型更依赖空间化架构
     - 社交倾向是否调节空间效应

#### 次级分析：event-level 时间动态

```text
DV_event ~ condition * time_block + (1|seed) + (1|agent_id)
```

   - `time_block` 至少包括：
     - `0-50`
     - `51-100`
     - `101-200`
   - 这层分析用于解释 `spatial priming vs sustained guidance`，不是主结论依据。

7. 固定结果解释边界。
   - 如果 run-level 不显著，主结论就应写成：
     - “未发现稳定中到大效应的证据”
   - 如果 event-level 很好看，但 run-level 不成立：
     - 不能把 event-level 当成主验证结论
   - 如果 `DeepSeek` 与 `Qwen` 方向不一致：
     - 必须在 Discussion 中明确报告模型依赖性
   - 如果某个编码维度未通过 `LLM-human calibration`：
     - 该维度不能直接进入主结果图表和摘要

8. 统计报告要完整。
   - 每个关键比较至少报告：
     - 效应量 `d`
     - `95% CI`
     - 校正后的 `p`
   - 多重比较统一做 `Benjamini-Hochberg FDR` 校正。

### 通过标准

- [ ] 两阶段分离评估已执行，没有空间信息泄露到盲编码阶段。
- [ ] `coding manual` 完成并冻结版本。
- [ ] human pilot coding 达到各维度 `kappa` 阈值。
- [ ] `LLM-human calibration` 完成，未过线维度已被降级处理。
- [ ] `TAR_run` 严格按 location-level `Spearman + Fisher z` 生成。
- [ ] 主验证分析、异质性分析和时间动态分析都已分层完成。
- [ ] 所有关键比较都附带效应量、置信区间和 FDR 校正结果。

### 输出物

- [ ] 一版定稿的 `coding manual`。
- [ ] human pilot coding 报告。
- [ ] `LLM-human calibration` 报告。
- [ ] run-level 主分析结果表。
- [ ] time-block 分析结果表和 priming / sustained guidance 解释备忘。
- [ ] 决策点：哪些维度进入主结果；`H3` 是否作为主分析还是描述性观察；哪些结论只能放在 Discussion。

### 常见误区

- 让标注者同时看到行为和空间信息，破坏两阶段分离。
- 把 LLM Judge 的分数当成“真实标签”，绕过编码信度检查。
- 用 event-level 的显著结果去掩盖 run-level 的无效或不稳定。
- `TAR_run` 还没按 protocol 落地，就先画漂亮图讲故事。

---

## 模块六：写作、预算与投稿

### 目标

把已经站住的证据组织成一篇可以投稿的论文，而不是在最后阶段重新发明论文结构或扩大主张。

### 现在要做什么

- 输入物：已完成的 run-level 主结果、通过校验的编码维度、固定主张边界、预算与时间线约束。

1. 先决定你写的是哪一种版本。
   - **Minimum Viable Paper** 只依赖：
     - 阶段1表征有效性
     - 阶段2核心 5 条件比较
     - `Exp1C` 作为探索性补强
   - 这已经足够形成一篇完整论文。
   - 阶段3、人类评估和更多机制条件都是加分项，不是起步门槛。

2. 采用对你最省力、也最稳的写作顺序。

```text
1. Experiments / Results
2. Method
3. Theoretical Framework
4. Related Work
5. Discussion
6. Introduction
7. Abstract
8. Title
```

   - 原因很简单：数据和设计越确定的部分越先写，最不确定的 framing 最后写。

3. 固定论文骨架，不边写边换故事。

| 章节 | 重点 |
|------|------|
| Introduction | 问题、三重理论跳跃、贡献、主张边界 |
| Related Work | LLM Agents、Space Syntax、空间感知相关工作 |
| Theoretical Framework | `H1-H3`、指标决策、`BSR/TAR` |
| SpatialAgent-Lite | `Spatial Perception`、`Spatial Action Sampling`、条件矩阵 |
| Experimental Design | `MIC`、阶段1、阶段2、统计分析框架 |
| Results | 主比较链 `A-E`、时间动态、探索性结果 |
| Discussion | 理论归因、模型依赖性、局限性、外部效度 |
| Conclusion | 一句话收束主发现与边界 |

4. 直接按 `v7` 的 Minimum Viable Paper 思路构图和组织贡献。
   - 保底题目可用：
     - `Does Space Syntax Help LLM Agents Behave Spatially? A Controlled Study of Structured Spatial Representations`
   - 保底贡献写法可围绕四点：
     - 一套结构化空间表征协议
     - 一套区分到位后 `Perception`、Movement 与 `Sampling` 的实验框架
     - 一套区分“响应存在”与“方向对齐”的双主因变量设计
     - 一套用于长时程 LLM Agent 实验的 `MIC` 对照协议

5. 提前规划图表，不要最后临时拼。
   - 最少要有这几张主图：
     - Figure 1：`Plaza` 构型可视化
     - Figure 2：`SpatialAgent-Lite` 架构图
     - Figure 3：信息访问矩阵 / 条件矩阵
     - Figure 4：阶段1的 `BSR/TAR` 条件对比
     - Figure 5：阶段2主比较链结果
     - Figure 6：`Exp1C` 的 2×2 结果
     - Figure 7：收敛曲线与时间动态

6. 把“可以写进摘要 / 不可以写进摘要”的句式先锁死。
   - 可以写：
     - 结构化空间表征可以系统性影响 LLM Agent 行为
     - 这种影响在关键比较中超出稳定非空间基线
     - 其中一部分影响沿着 Space Syntax 理论方向发生
   - 不可以写：
     - `prove`
     - `fully validate`
     - “所有涌现都由空间因果决定”
     - 只凭 event-level 显著就写“显著提升”
   - 摘要主结论只依赖：
     - `MIC run-level` 验证性分析

7. 预算按 `v7` 执行，不要再把 API 成本想成主要瓶颈。

| 方案 | 内容 | 费用 |
|------|------|------:|
| `A: MVP` | 预实验 + 阶段1 + 阶段2核心 + human coding pilot | `~¥1,500-1,900` |
| `B: 推荐版` | `A` + 机制条件 + `DeepSeek` 鲁棒性子集 + 人类评估 | `~¥4,200-4,700` |
| `C: 全量版` | `B` + 阶段3多地图 + `Exp3-Minimal` | `~¥6,800-7,400` |

   - `v7` 的明确建议是：**按方案 B 执行**。
   - 原因不是“更豪华”，而是：
     - `30` 个 `MIC seeds` 可以完整保留
     - API 成本不再是主约束
     - 人工编码和人类评估才是主要开支

8. 按固定时间线安排，不要边做边重排。

```text
W1-W2:
  指标实现、地图预检、NPC设计、lexical norming、C2 reverse-inference audit

W3:
  预实验：理解门控、prompt位置、MIC有效窗口、收敛 pilot、coding manual pilot

W4-W5:
  阶段1：Exp1A + Exp1C

W6-W8:
  阶段2：5 个核心条件的 MIC 验证性实验

W9:
  阶段2：机制条件补充 + human coding subset

W10-W12:
  仅在阶段2支持时进入阶段3；否则直接整理论文主结果

W13-W15:
  人类评估（若做）+ 论文写作

W16-W18:
  修改、内部 review、投稿
```

9. 投稿前，按 `v7` 的 checklist 逐项核对。
   - 理论：
     - `H1-H3` 推导链完整
     - `TAR_run` protocol 已明确写成步骤
     - 主张没有强于设计能支撑的内容
   - 预实验：
     - `Openness vs Mean Depth` 决策完成
     - `lexical norming` 完成
     - `C2 reverse-inference audit` 完成
     - `MIC` 有效窗口分析完成
     - prompt 位置固定
     - 收敛性 pilot 完成
   - 阶段1：
     - `C4 > C0/C1/C2/C3/C5` 报告完整
     - 同时报告 `BSR` 与 `TAR`
     - `Exp1C` 使用 `composite structural profile` 解释
     - 每 cell 至少 `10` 个场景
   - 阶段2：
     - `30 MIC seeds × 5 核心条件` 完成
     - `C6m-C1`、`C6m-C2`、`C6f-C6m`、`C4-C6f`、`C4-C1` 全部报告
     - `TAR_run` 按 location-level `Spearman + Fisher z` 生成
     - 前 `50` 轮 priming 分析完成
     - `C7` 若用于认知 vs Movement 解释，则至少 `20` 个 seeds
   - 模型与评估：
     - `Qwen3.5-Plus` 空间理解门控通过
     - `DeepSeek-V3.2` 鲁棒性子集方向一致性检查完成
     - Actor-Judge 同源偏见检测完成
     - `coding manual` 完成
     - human pilot coding 达到预设阈值
     - `LLM-human calibration` 完成
     - 两阶段分离评估未泄露空间信息
   - 写作：
     - 摘要主结论只依赖 `MIC run-level` 验证性分析
     - 明确写出“主验证分析主要检测中到大效应”
     - `RQ4` 明确写为探索性
     - 阶段3明确写为可选扩展

10. 投稿后再做收尾，而不是投稿前分心。
   - 投稿完成后再做：
     - `arXiv` 版本整理
     - 代码仓库清理与开源准备
     - Plan B 投稿路线准备

### 通过标准

- [ ] Minimum Viable Paper 的范围已经锁定。
- [ ] 写作顺序和章节骨架不再频繁变动。
- [ ] 主图表清单已固定。
- [ ] 预算方案已选定，默认按 `方案 B` 执行。
- [ ] `W1-W18` 时间线已映射到实际安排。
- [ ] 投稿前 checklist 已逐项打勾。
- [ ] 摘要、标题和贡献写法都没有越过 `v7` 主张边界。

### 输出物

- [ ] 论文初稿。
- [ ] 图表成稿版本。
- [ ] 附录与补充材料。
- [ ] 投稿前 checklist 打勾版。
- [ ] 决策点：最终按 `MVP / 推荐版 / 全量版` 哪个版本打包投稿；阶段3与人类评估是否纳入正文。

### 常见误区

- 结果还没整理清楚，就急着写长篇 Introduction。
- 把阶段3或人类评估写成“没有就不能投”，导致主线迟迟不收口。
- 在摘要里使用超出设计能力范围的词，比如 `prove`、`fully validate`。
- 低估写作、补图、内部 review 和 rebuttal 风格自检的时间。

---

## 最后提醒

这篇论文真正难的地方，不是模型调用，也不是系统搭建，而是**持续守住方法边界**。你会不断有冲动去多做一点、多解释一点、多声称一点。`v7` 的价值就在于它已经替你划好了边界。

守住这三句话，你大概率不会走偏：

- 主论文的核心证据来自 `MIC run-level` 验证性分析。
- `Exp1C`、机制条件、阶段3和人类评估都很有价值，但它们是扩展，不是主链替代品。
- 这篇论文要做的，是给出稳健、可复现、可 defend 的证据，而不是做最大胆的宣言。
