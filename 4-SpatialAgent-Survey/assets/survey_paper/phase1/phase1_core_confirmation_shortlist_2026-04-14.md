# Phase 1 Core Confirmation Shortlist

日期：2026-04-14  
状态：`draft v1`  
用途：把当前 `Core` 相关材料统一成一份可人工复核的 shortlist，避免继续混用“正式落表 core”“扩展搜索候选”“broadened-core working set”三个不同口径。

---

## 1. 这份 shortlist 的口径

这份清单按 **唯一 title** 计数，不再按 `paper row` 计数。

因此它和当前正式 `screening_sheet_phase1_2026-04-13.csv` 中的 `12 core` 不是同一个口径：

- 正式主表里的 `12 core` 是 `paper rows`
- 去重到唯一 title 后，现有正式 `core` 只有 `8` 个

在此基础上，再把两轮 targeted expansion 与池内可升级条目并进来，形成当前的 `26` 个 `core-related` unique titles：

- `8` 个：已正式落表的 unique `core`
- `2` 个：当前池内、建议从 `adjacent -> core-candidate` 的 promotion 候选
- `16` 个：两轮 targeted expansion 新增 seed

这份 shortlist 的目的不是“直接宣布 26 篇都进入 Core”，而是把它们分成三个复核优先级：

- `high-confidence core`
- `borderline but keep`
- `likely demote later`

---

## 2. 当前 shortlist 总数

- `high-confidence core`: `15`
- `borderline but keep`: `8`
- `likely demote later`: `3`
- 合计 unique titles: `26`

当前建议理解为：

- `15` 篇可以作为下一轮 full-text sanity check 的优先主线
- `8` 篇值得保留，但需要进一步确认其“空间环境”和“多智能体社会行为”是否同时成立
- `3` 篇先不删，但大概率会在下一轮降级到 `adjacent` 或 `excluded`

---

## 3. High-Confidence Core

这些条目已经满足或大概率满足本文 `Core` 的三项基本条件：

1. `LLM / generative-agent` 系统  
2. 存在可识别空间环境  
3. 涉及社会行为或群体互动

| ID | Title | 来源 | 当前状态 | 为什么先放高优先级 |
|---|---|---|---|---|
| HC01 | TravelAgent: Generative agents in the built environment | formal core | `core` | `built environment` 明确，行为与环境耦合明确。 |
| HC02 | Generative Agents: Interactive Simulacra of Human Behavior | formal core | `core` | 最强 anchor，沙盒城镇、日常活动、社会互动都明确。 |
| HC03 | Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia | formal core | `core` | 直接把 actions grounded in physical/social/digital space 写进系统定义。 |
| HC04 | Affordable Generative Agents | formal core | `core` | 明确包含 agent-environment 与 inter-agent interaction。 |
| HC05 | Artificial Leviathan: Exploring Social Evolution of LLM Agents Through the Lens of Hobbesian Social Contract Theory | formal core | `core` | 沙盒生存环境与社会秩序演化都足够明确。 |
| HC06 | Project Sid: Many-agent simulations toward AI civilization | formal core | `core` | `Minecraft environment` 与 many-agent civilization 都是强空间社会信号。 |
| HC07 | OASIS: Open Agent Social Interaction Simulations with One Million Agents | formal core | `core` | 已接受数字/图结构平台环境逻辑，社会传播效应明确。 |
| HC08 | Lyfe Agents: Generative agents for low-cost real-time social interactions | targeted seed round 1 | `not yet ingested` | 自定义 `3D virtual environment` + 多 agent 社会互动。 |
| HC09 | Spontaneous Emergence of Agent Individuality Through Social Interactions in Large Language Model-Based Communities | targeted seed round 1 | `not yet ingested` | `50 x 50 2D grid`、邻近通信、社区形成都很强。 |
| HC10 | Real world community oriented high-definition social simulation: Combining reinforcement learning and large language models | targeted seed round 1 | `not yet ingested` | 真实社区 `GIS/BIM + Unreal Engine`，空间环境很强。 |
| HC11 | Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios | pool promotion | `adjacent` | 若接受 broadened-core 边界，VR role-play 中的空间互动与社会对话足够强。 |
| HC12 | SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds | targeted seed round 2 | `not yet ingested` | 标题与摘要都把 `physical and social worlds` 作为核心设定。 |
| HC13 | Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment | targeted seed round 2 | `not yet ingested` | 显式空间约束、多人行为与协调都成立。 |
| HC14 | When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios | targeted seed round 2 | `not yet ingested` | crowd movement + disaster space + collective behavior 边界清楚。 |
| HC15 | CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation | targeted seed round 2 | `not yet ingested` | 城市尺度环境与行为动态都直接命中 survey 主线。 |

---

## 4. Borderline But Keep

这些条目值得保留，但仍需重点确认以下问题之一：

- 是否真的是 `multi-agent social simulation`
- 是否只是 `human-agent interaction`
- 是否存在环境侧空间结构，但 agent 侧拿不到足够强的空间输入
- 是否更适合进入 `adjacent`

| ID | Title | 来源 | 当前状态 | 边界风险 |
|---|---|---|---|---|
| BK01 | AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society | formal core | `core` | 社会模拟很强，但空间环境如何表示仍需要全文确认。 |
| BK02 | When LLMs Recognize Your Space: Research on Experiences with Spatially Aware LLM Agents | pool promotion | `adjacent` | 空间识别很强，但更像体验研究，需确认是否足够多智能体。 |
| BK03 | A Context-Aware Onboarding Agent for Metaverse Powered by Large Language Models | targeted seed round 2 | `not yet ingested` | `metaverse` 明确，但可能偏单 agent onboarding。 |
| BK04 | A Voice-Controlled Dialogue System for NPC Interaction using Large Language Models | targeted seed round 2 | `not yet ingested` | `NPC interaction` 有场景，但要确认是否是社会模拟而非单点交互。 |
| BK05 | Mixed-Initiative Dialogue Management for Human-Virtual Agents Interaction in Forum Theatre Inspired Training | targeted seed round 2 | `not yet ingested` | 场景化强，但可能更偏训练交互而非多 agent 社会系统。 |
| BK06 | TongSIM: A General Platform for Simulating Intelligent Machines | targeted seed round 2 | `not yet ingested` | 环境明确，但可能更像通用 simulator 平台。 |
| BK07 | S^3: Social-network Simulation System with Large Language Model-Empowered Agents | targeted seed round 2 | `not yet ingested` | 若继续接受数字平台环境，可保留；否则可能降级。 |
| BK08 | Unveiling the collective behaviors of large language model-based autonomous agents in an online community: A social network analysis perspective | targeted seed round 2 | `not yet ingested` | 在线社区可视为空间的前提仍需保持一致。 |

---

## 5. Likely Demote Later

这些条目暂时不删，是为了避免过早损失边界案例；但以当前摘要强度看，更像后续会降回 `adjacent` 或 `excluded`。

| ID | Title | 来源 | 当前状态 | 为什么大概率降级 |
|---|---|---|---|---|
| LD01 | An Open-Domain Avatar Chatbot by Exploiting a Large Language Model | targeted seed round 2 | `not yet ingested` | avatar-based 不等于多智能体社会环境，当前更像 embodied chat。 |
| LD02 | Artificial intelligence chatbots mimic human collective behaviour | targeted seed round 2 | `not yet ingested` | 群体行为强，但空间环境证据仍然偏弱。 |
| LD03 | DeMAC: Enhancing Multi-Agent Coordination with Dynamic DAG and Manager-Player Feedback | targeted seed round 2 | `not yet ingested` | coordination 存在，但共享空间与社会行为边界不够稳。 |

---

## 6. 建议的复核顺序

### 第一批：先全文确认 high-confidence 的新增条目

优先顺序建议：

1. `Lyfe Agents`
2. `Spontaneous Emergence...`
3. `Real world community oriented...`
4. `SimWorld`
5. `CitySim`
6. `fire evacuation`
7. `crowd evacuation`
8. `VR role-play`

目标：

- 尽快把当前正式 `8` 个 unique `core` 扩到一个更稳的 `15+` confirmed core 工作集

### 第二批：再清理 borderline

优先顺序建议：

1. `AgentSociety`
2. `When LLMs Recognize Your Space`
3. `A Context-Aware Onboarding Agent for Metaverse...`
4. `NPC interaction`
5. `TongSIM`
6. `S^3`
7. `online community collective behaviors`
8. `forum theatre`

目标：

- 判断哪些是真正应该进入 `Core`
- 哪些应该稳定回落到 `Adjacent`

### 第三批：最后处理 likely demote later

这三篇暂不作为扩充 `Core` 数量的主依赖，不应让它们拖慢当前主线。

---

## 7. 对当前项目状态的更新

现在最准确的说法应该是：

- 已正式落表的 unique `core`：`8`
- 已形成 draft `core-confirmation shortlist`：`26`
- 下一步不是继续泛化搜索，而是把这 `26` 个条目完成一轮 `full-text sanity check`

也就是说，项目已经不再缺“可疑似进入 Core 的候选面”，现在真正需要的是：

- 正式 ingest
- dedupe
- full-text confirmation
- shortlist 收敛

