# Phase 1 Abstract Rereview Round 1 Summary

日期：2026-04-13

## 决策统计

- `keep`: `87`
- `downgrade`: `1`
- `exclude`: `29`
- `hold_ambiguous_space`: `0`
- `hold_missing_abstract`: `0`

## R1 推荐层级

- `core`: `8`
- `adjacent`: `36`
- `foundational`: `44`
- `excluded`: `29`

## 说明

- 这一版是 `abstract-only` 复核，不是最终定稿。
- `hold_ambiguous_space` 表示摘要显示社会模拟存在，但空间环境是否满足本综述定义仍需全文确认。
- `hold_missing_abstract` 表示当前缺英文摘要，不能只靠 abstract 做稳健判断。

## 需要优先全文复核的变化项

- `exclude` | `core -> excluded` | Unveiling the Truth and Facilitating Change: Towards Agent-based Large-scale Social Movement Simulation | 当前材料只显示 Twitter-like 社交媒体响应仿真与 benchmark，没有足够证据证明存在可识别空间环境或 agent-facing 空间结构；按 E1 排除。
- `exclude` | `core -> excluded` | Agent-Based Modelling Meets Generative AI in Social Network Simulations | 补到的摘要显示其核心是社交网络用户仿真、内容转发与推荐机制；仍未给出可识别空间环境或 agent-facing 空间结构，按 E1 排除。
- `exclude` | `core -> excluded` | Can A Society of Generative Agents Simulate Human Behavior and Inform Public Health Policy? A Case Study on Vaccine Hesitancy | 摘要聚焦社交网络与健康决策，没有明确可识别空间环境，按 E1 先排除。
- `exclude` | `core -> excluded` | Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations? | 摘要讨论社交网络结构与 friendship paradox，并非空间环境中的社会行为，按 E1 排除。
- `exclude` | `core -> excluded` | CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation | 这是角色扮演对话 benchmark，不含空间环境，按 E1 排除。
- `downgrade` | `core -> adjacent` | Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios | 摘要更像单 agent + user 的 environment-aware VR interaction，不是多智能体社会模拟，先降到 adjacent。
- `exclude` | `core -> excluded` | Generative Agent Simulations of 1,000 People | 摘要是 interview-conditioned human behavior replication，没有明确空间环境，按 E1 排除。
- `exclude` | `core -> excluded` | Harnessing Large Language Models to Simulate Realistic Human Responses to Social Engineering Attacks: A Case Study | 摘要聚焦 phishing/social engineering response simulation，不含空间环境，按 E1 排除。
- `exclude` | `core -> excluded` | Multimodal Safety Evaluation in Generative Agent Social Simulations | 摘要强调 multimodal/text-visual social situations 与 safety evaluation，但没有给出可识别空间环境或结构化空间输入；rich settings 不能直接视为空间环境，按 E1 排除。
- `exclude` | `core -> excluded` | Psychologically-Valid Generative Agents: A Novel Approach to Agent-Based Modeling in Social Sciences | 摘要是通用 cognitive/stance framework，没有明确空间环境，按 E1 排除。
- `exclude` | `core -> excluded` | Simulating Public Administration Crisis: A Novel Generative Agent-Based Simulation System to Lower Technology Barriers in Social Science Research | 摘要描述虚拟政府与公共事件仿真，但未给出明确空间环境，按 E1 排除。
- `exclude` | `core -> excluded` | User Behavior Simulation with Large Language Model based Agents | 摘要聚焦 recommendation/social network 用户仿真，没有明确空间环境，按 E1 排除。
- `exclude` | `core -> excluded` | User Behavior Simulation with Large Language Model-based Agents | 摘要聚焦 recommendation/social network 用户仿真，没有明确空间环境，按 E1 排除。
- `exclude` | `adjacent -> excluded` | AgentSims: An Open-Source Sandbox for Large Language Model Evaluation | 摘要聚焦通用 agent evaluation sandbox，空间目标不明确，先按 E1 排除出本轮空间相关语料。
- `exclude` | `adjacent -> excluded` | A survey on large language model based autonomous agents | 通用 agent survey，不是 spatial reasoning / spatially-aware corpus，按 E1 排除。
- `exclude` | `adjacent -> excluded` | A Survey on Large Language Model-Based Game Agents | 综述范围过宽，未直接服务 spatial capability boundary，先按 E1 排除出正式 Phase 1 语料。
- `exclude` | `adjacent -> excluded` | Large language models empowered agent-based modeling and simulation: a survey and perspectives | 这是 general LLM+ABM survey，不直接回答空间能力边界，先按 E1 排除出本轮正式语料。
- `exclude` | `adjacent -> excluded` | Methods That Support the Validation of Agent-Based Models: An Overview and Discussion | 传统 ABM validation overview，既非 LLM 也非空间能力论文，按 E3 排除。
- `exclude` | `adjacent -> excluded` | On The Planning Abilities of OpenAI's o1 Models: Feasibility, Optimality, and Generalizability | 标题与摘要不显示空间目标，属于一般 planning 能力，不纳入本轮空间语料。
- `exclude` | `adjacent -> excluded` | The Rise and Potential of Large Language Model Based Agents: A Survey | 通用 LLM agent survey，不直接服务 spatial boundary，按 E1 排除。
- `exclude` | `adjacent -> excluded` | Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling | 聚焦 generative social simulation validation，而非空间能力边界，先按 E1 排除。
- `exclude` | `foundational -> excluded` | <b>Language and space.</b> Ed. By Paul Bloom, Mary A. Peterson, Lynn Nadel, and Merrill F. Garrett. Cambridge, MA &amp; London: MIT Press/Bradford, 1996. Pp. x, 597. $50.00. | 这是 broad book review，不是本综述需要的直接桥接证据，先排除。
- `exclude` | `foundational -> excluded` | Building Problem Spaces for Deaf and Hard of Hearing Students’ Spatial Cognition in a Programming Language | 现有元数据仅显示它是编程语言中的空间认知教育研究，不直接提供本综述所需的社会行为或 Space Syntax 桥接证据，按 E2 排除。
- `exclude` | `foundational -> excluded` | Handbook of spatial cognition. | 通用 handbook 过宽，不适合作为本轮 foundational 主体。
- `exclude` | `foundational -> excluded` | LANGUAGE AND SPACE | 通用语言与空间汇编过宽，先排除以收缩 foundational。
- `exclude` | `foundational -> excluded` | Language, cognition, and space:the state of the art and new directions | 广义 edited volume，当前超出本轮最小桥接集，先排除。
- `exclude` | `foundational -> excluded` | Space in language and cognition explorations in cognitive diversity | 通用认知多样性 volume，当前不直接服务本文的空间-社会桥接。
- `exclude` | `foundational -> excluded` | Space in Languages | 语言类型学范围过宽，当前先不进入正式 foundational 集。
- `exclude` | `foundational -> excluded` | Spatial cognition : brain bases and development | 这是广义空间认知基础书，不是最直接的社会/构型桥接证据，先排除。
- `exclude` | `foundational -> excluded` | Thought Without Language | 过于宽泛的语言-思维讨论，不作为当前 foundational 主集合。
