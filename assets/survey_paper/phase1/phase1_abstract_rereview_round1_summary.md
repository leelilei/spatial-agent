# Phase 1 Abstract Rereview Round 1 Summary

日期：2026-04-13

## 决策统计

- `keep`: `80`
- `downgrade`: `1`
- `exclude`: `25`
- `hold_ambiguous_space`: `3`
- `hold_missing_abstract`: `8`

## R1 推荐层级

- `core`: `11`
- `adjacent`: `36`
- `foundational`: `45`
- `excluded`: `25`

## 说明

- 这一版是 `abstract-only` 复核，不是最终定稿。
- `hold_ambiguous_space` 表示摘要显示社会模拟存在，但空间环境是否满足本综述定义仍需全文确认。
- `hold_missing_abstract` 表示当前缺英文摘要，不能只靠 abstract 做稳健判断。

## 需要优先全文复核的变化项

- `hold_ambiguous_space` | `core -> core` | OASIS: Open Agent Social Interaction Simulations with One Million Agents | 摘要强调社交媒体平台环境，但是否可算作本文需要的空间环境仍需全文裁定；先 hold。
- `hold_ambiguous_space` | `core -> core` | Unveiling the Truth and Facilitating Change: Towards Agent-based Large-scale Social Movement Simulation | 摘要是 Twitter-like 社交媒体仿真，空间维度不明确；先 hold，等待全文确认。
- `hold_missing_abstract` | `core -> core` | Agent-Based Modelling Meets Generative AI in Social Network Simulations | 当前缺英文摘要，abstract-only 复核无法完成；需补全文或元数据。
- `exclude` | `core -> excluded` | Can A Society of Generative Agents Simulate Human Behavior and Inform Public Health Policy? A Case Study on Vaccine Hesitancy | 摘要聚焦社交网络与健康决策，没有明确可识别空间环境，按 E1 先排除。
- `exclude` | `core -> excluded` | Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations? | 摘要讨论社交网络结构与 friendship paradox，并非空间环境中的社会行为，按 E1 排除。
- `exclude` | `core -> excluded` | CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation | 这是角色扮演对话 benchmark，不含空间环境，按 E1 排除。
- `downgrade` | `core -> adjacent` | Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios | 摘要更像单 agent + user 的 environment-aware VR interaction，不是多智能体社会模拟，先降到 adjacent。
- `exclude` | `core -> excluded` | Generative Agent Simulations of 1,000 People | 摘要是 interview-conditioned human behavior replication，没有明确空间环境，按 E1 排除。
- `exclude` | `core -> excluded` | Harnessing Large Language Models to Simulate Realistic Human Responses to Social Engineering Attacks: A Case Study | 摘要聚焦 phishing/social engineering response simulation，不含空间环境，按 E1 排除。
- `hold_ambiguous_space` | `core -> core` | Multimodal Safety Evaluation in Generative Agent Social Simulations | 摘要提到 rich multimodal settings，但未说明空间结构输入如何进入 agent，先 hold。
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
- `hold_missing_abstract` | `adjacent -> adjacent` | Reasoning Paths with Reference Objects Elicit Quantitative Spatial Reasoning in Large Vision-Language Models | 当前缺英文摘要，abstract-only 复核无法完成；需补全文或元数据。
- `exclude` | `adjacent -> excluded` | The Rise and Potential of Large Language Model Based Agents: A Survey | 通用 LLM agent survey，不直接服务 spatial boundary，按 E1 排除。
- `exclude` | `adjacent -> excluded` | Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling | 聚焦 generative social simulation validation，而非空间能力边界，先按 E1 排除。
- `hold_missing_abstract` | `foundational -> foundational` | Space is the Machine: A Configurational Theory of Architecture | 当前缺英文摘要，abstract-only 复核无法完成；需补全文或元数据。
- `hold_missing_abstract` | `foundational -> foundational` | The Social Logic of Space | 当前缺英文摘要，abstract-only 复核无法完成；需补全文或元数据。
- `exclude` | `foundational -> excluded` | <b>Language and space.</b> Ed. By Paul Bloom, Mary A. Peterson, Lynn Nadel, and Merrill F. Garrett. Cambridge, MA &amp; London: MIT Press/Bradford, 1996. Pp. x, 597. $50.00. | 这是 broad book review，不是本综述需要的直接桥接证据，先排除。
- `hold_missing_abstract` | `foundational -> foundational` | Building Problem Spaces for Deaf and Hard of Hearing Students’ Spatial Cognition in a Programming Language | 当前缺英文摘要，abstract-only 复核无法完成；需补全文或元数据。
- `exclude` | `foundational -> excluded` | Handbook of spatial cognition. | 通用 handbook 过宽，不适合作为本轮 foundational 主体。
- `exclude` | `foundational -> excluded` | LANGUAGE AND SPACE | 通用语言与空间汇编过宽，先排除以收缩 foundational。
- `exclude` | `foundational -> excluded` | Language, cognition, and space:the state of the art and new directions | 广义 edited volume，当前超出本轮最小桥接集，先排除。
