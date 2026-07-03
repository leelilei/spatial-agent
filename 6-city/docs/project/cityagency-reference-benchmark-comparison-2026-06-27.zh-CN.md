# CityAgency 相关 Benchmark 中文对比

日期：2026-06-27

## 目的与范围

本文档比较与 CityAgency 最相关的研究，统一回答以下问题：

1. Benchmark 想测什么？
2. 测试了哪些 Agent 架构或基础模型？
3. 如何构造并运行测试？
4. 使用哪些指标？
5. 得出了什么结论？
6. 对城市研究有什么意义？

正式 benchmark、经验验证工作和带评估的模拟系统在表中分别说明。CitySim 和 GATSim
属于经过实验评估的模拟系统，并不是标准化 benchmark suite。

## 测试架构、模型与城市研究意义

这里区分 Agent 架构、基础模型和评估器。只更换 LLM 的实验主要说明模型差异；固定
LLM、改变规划或记忆架构的实验，才能更直接地说明 Agent 架构差异。

| Reference | 测试的 Agent 架构或系统 | 测试的基础模型 | 人类基线或评估器 | 对城市研究的意义 |
|---|---|---|---|---|
| LiveCultureBench | 动态图城市中的目标居民、支持居民，以及带不确定性校准的 LLM Verifier | Gemini 2.5 Pro/Flash、Qwen 3、Llama 3、Ministral 3 Reasoning | 人工标注文化规范；每类任务使用 400 个样本校准 Verifier | 最接近的社会城市竞品：已经覆盖小城市、每日目标和规范遵守，因此 CityAgency 必须贡献物理执行证据，而不能只依赖“城市 + 目标”的设定 |
| MobilityBench | 确定性 API Replay Sandbox 中的工具调用路线规划 Agent | Qwen3、DeepSeek-R1/V3.2、GPT-4.1/5.2、Claude 4.5、Gemini 3 Pro/Flash | 冻结服务返回值后程序化判断结果，无需人类作为主评估器 | 建立真实移动请求的可复现评估，并显示带个性化偏好的路线规划仍然薄弱 |
| DeliveryBench | 程序生成 3D 城市中的长程单/多 Agent 配送系统 | GPT-5、GPT-4o、Claude-3.7-Sonnet、Gemini-2.5-Flash、Qwen2.5-VL-72B/32B、Llama-3.2-90B-Vision | 人类玩家使用同一界面和协议 | 直接测截止时间、成本、电量和交互约束下的城市执行，把 CityAgency 的创新进一步压缩到通用意图与证据协议 |
| GenWorld | 经验数据驱动的合成人口与离线 LLM 策略编译 | 教师模型决策编译为可复用策略，而不是在线调用 196,608 个居民 | 东广岛人口普查、建筑、POI、道路和移动证据 | 给出微观行为扩展到城市尺度的可行路线；CityAgency 则保留在线 Agent 以诊断个体失效 |
| Limits of Agency | AgentTorch 中的启发式 Agent、完全自适应 LLM Agent 和 LLM Archetype | 在群体原型层调用 LLM，并向同组 Agent 采样行为 | 纽约疫情与劳动力市场数据支撑 840 万 Agent 案例 | 明确提出 agency 与规模的权衡，为 CityAgency 的高 agency、小规模设计提供理论边界 |
| Validation Is the Central Challenge | 生成式 ABM 系统综述，不是模型跑分 Benchmark | 不适用 | 对照各论文的建模目的与验证方法 | 说明面孔效度和与机制关系松散的结果指标不足以支撑城市或社会科学结论 |
| Mechanism Plausibility | 面向生成式 ABM 的四级机制可信度清单 | 不适用 | 双评审校准，并分别评价 Agent 层和 ABM 层 | 防止把 CityAgency 的 Agent 层执行证据直接升级为宏观城市真实性或因果有效性 |
| MobiSim-Bench | 18 支队伍提交的 `LLM as Brain`、`LLM as Glue`、`LLM as Extra` 三类架构，共部署 967 个 Agent | 多种参赛 LLM 配置，核心比较单位是架构类别 | 真实移动轨迹和飓风出行统计 | 直接检验日常和灾害条件下的移动模拟是否可信；说明同一架构未必能同时适用于常态和异常城市情境 |
| When Plausible Is Not Realistic | AgentSociety 与统一基础设施下重建的 CitySim | AgentSociety 使用 Qwen2.5-32B-Instruct 推荐配置；CitySim 重建遵循 GPT-4o-mini 设计 | 巴黎大区和上海真实移动数据，不以 LLM Judge 作为主要真实性依据 | 说明合成居民进入交通、可达性、土地利用或政策研究前，必须先通过经验移动规律验证 |
| CitySim | CitySim 与 Generative Agents、AGA、HumanoidAgent、MobileCity、AgentSociety，并包含模块消融 | 除特别说明外均使用 GPT-4o-mini | GPT-4o 微观类人度评价；真实时间利用和 POI 数据用于宏观比较 | 可用于探索时间利用、地点热度、拥挤和幸福感，但当前验证不足以直接支持政策推断 |
| GATSim | 移动基础模型、层级记忆、规划、反应和反思组成的 GATSim，与人类角色扮演者比较 | 原型使用 GPT-4o | 5 名人类完成 50 个案例；GPT-o1 盲测配对评价 | 为交通模拟提供自适应行为层，可研究路径选择、拥堵和扰动响应，但角色扮演不等于真实出行行为 |
| CityBench | 面向不同任务的零样本/少样本 LLM、VLM Agent 与传统领域基线 | GPT-4/4o、GPT-3.5、Llama 3、Qwen、InternLM/InternVL、Mistral/Mixtral、DeepSeek-V2、LLaVA-NeXT、CogVLM2、MiniCPM-V 等约 30 个模型 | 任务真值和传统领域指标 | 刻画模型在城市感知、地理推理、导航、移动预测和交通控制上的能力边界 |
| USTBench | 统一城市 Agent wrapper；非推理模型、推理模型与传统领域基线 | Qwen2.5、GLM4、Llama-3.3、GPT-4o、DeepSeek-R1/Distill、QwQ、GLM-Z1、o4-mini | 结构化 QA 和下游城市任务真值 | 揭示预测、长期规划和反馈适应中的过程性错误，关系到交通、设施、道路和社会经济任务的可靠性 |
| CityEQA | PMA、PMA 消融、Blind Agent、随机探索、前沿探索和人类 EQA | PMA 使用 GPT-4o VLM 与 GPT-4 LLM；Blind Agent 包含 GPT-4、Qwen2.5、Llama-3.1-8B、DeepSeek-V3 | 人类 EQA 轨迹和答案；开放答案使用 LLM Judge | 支持城市巡检、信息采集、地图更新和公共空间观察，但不是居民自主行为模拟 |
| EmbodiedCity | 场景理解、QA、对话、VLN 和任务规划上的多模态模型 | Fuyu-8B、Qwen-VL、Claude 3、GPT-4 Turbo，VLN 还测试 GPT-4o | 参考答案和导航真值 | 为城市机器人和城市服务提供真实室外感知与导航测试场，但实验成本高于可控行为研究 |
| SOTOPIA | 统一角色扮演接口下的模型-模型、模型-人类和人类-人类交互 | GPT-4、GPT-3.5、Llama-2-70B-Chat、MPT-30B-Chat | GPT-4 与人类 Judge；SOTOPIA-hard 上有人类基线 | 方法学意义：私有目标、关系和社会规范是研究居民协调、谈判和冲突的必要组成 |
| AgentSense | 多人角色扮演，加自评、对方评价、外部评价和多数投票 Judge | Llama-2/3、Mistral-7B、Qwen2.5、GPT-3.5-Turbo、GPT-4o | 人工验证；GPT-4o、Qwen2.5-72B、Llama-3-70B 组成 Judge ensemble | 方法学意义：多方目标和隐藏信息可支持社区互动、公众参与和社会协调研究 |
| Lifelong-SOTOPIA | 完整历史记忆与 episode 摘要记忆；额外的历史依赖困难场景 | Gemini-1.5、GPT-4o、Llama-3.1，困难场景加入 Llama-3.2 | 人类纵向基线；GPT-4 主评，Llama-3.1 复核 | 方法学意义：研究城市惯例、邻里关系和政策适应时，Agent 必须跨日记住地点、承诺和历史互动 |
| Misleading Success | 全知 `SCRIPT`、独立 `AGENTS`、`MINDREADERS` 和微调 Agent | GPT-3.5、Mixtral-8x7B/MoE；GPT-3.5 还使用 SCRIPT 轨迹微调 | GPT-4 评价目标；人类评价自然度 | 警告城市模拟不能给居民全知视角，否则会夸大居民对封路、他人目标和政策变化的协调能力 |
| Multi-Turn Human Behavior | Prompt-only、任务微调和推理轨迹增强微调 | DeepSeek-R1、Llama 3.1/3.2、Mixtral/Mistral、Qwen2.5、Claude 3/3.5/3.7 | 31,865 个真实购物 session 作为动作真值 | 方法学意义：行为看起来可信，不代表逐步动作接近真实人；城市行为主张最终需要人类轨迹验证 |
| ChinaTravel | ReAct、LLM-only、TTG、LLM-modulo、NeSy Planning、Oracle DSL NeSy 和偏好优化变体 | DeepSeek-V3/R1、GPT-4o、Qwen3-8B、Llama-3-8B、Mistral-7B | 人类请求；sandbox 和 DSL 确定性评估 | 展示如何形式化并验证城市活动中的可达性、时间、预算、交通、POI 和偏好约束 |
| FeasiGen | 单 Agent 与 Planner-Executor 多 Agent；标准模式与推理模式 | GPT、GPT-OSS、DeepSeek-V4、Qwen3.5、Llama-3.1 等 9 个模型 | 人工验证不可行任务标签 | 方法学意义：城市扰动可能使行程不再可行，Agent 必须会修复、改道或停止，而不是盲目继续 |
| tau-bench | 原生 Function Calling 与文本 ReAct；同任务重复运行 | GPT-4 系列、Claude 3、Gemini 1.5、Mistral/Mixtral、Llama-3-70B | GPT-4 用户模拟器；最终数据库和消息状态确定性评估 | 方法学意义：城市研究需要多次运行的可靠行为和权威状态验证，不能依赖一次幸运 rollout |
| AppWorld | ReAct、Plan-and-Execute、FullCodeRefl、CodeAct 和 ToolLLaMA | GPT-4o/4 Turbo/4、Llama-3-70B、DeepSeek-Coder-33B，另测 Gemini 1.5 Pro | 程序化状态单元测试 | 方法学意义：状态和副作用测试可迁移到城市库存、预算、预约、承诺和共享资源验证 |
| WebArena | Direct 与 CoT 浏览器 Agent；包含不可达任务提示消融 | GPT-4、GPT-3.5、text-bison/PaLM 系列 | 人类任务基线；主要是程序评估，少量模糊答案使用 GPT-4 | 方法学意义：可重置环境和功能结果验证可用于构建允许多条有效路径的城市 Agent 实验 |
| TheAgentCompany | 不同版本 OpenHands CodeAct 和 OWL RolePlay 多 Agent | Gemini 2.5/2.0/1.5、Claude 3.7/3.5、GPT-4o、o3-mini、Nova Pro、Llama 3.1/3.3、Qwen2/2.5 | 确定性 checkpoint，主观交付物使用 LLM | 方法学意义：城市义务同样具有长程、多方、部分完成、成本和下游影响，可借鉴 checkpoint 评估 |

## A. 城市移动真实性与城市模拟

| Reference | 想测什么 | 测试方法 | 主要指标 | 主要结论 | 与 CityAgency 的边界 |
|---|---|---|---|---|---|
| [MobiSim-Bench](../../assets/papers/notes/05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.md) | LLM Agent 能否稳定、真实地模拟日常及灾害条件下的人类移动 | AgentSociety 中运行 Daily Mobility 与 Hurricane Mobility；真实画像、地图和轨迹；18 支队伍参赛 | 运行完成；回转半径、地点数、意图序列、活动比例；出行变化率和时间分布 | 没有一种架构同时做好鲁棒性、真实性和响应性 | 主要判断群体移动质量，CityAgency 解释单个 Agent 是否通过有效轨迹完成私有目标 |
| [When Plausible Is Not Realistic](../../assets/papers/notes/05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.md) | 城市模拟生成的是经验真实移动，还是合理叙事 | 用巴黎和上海真实数据统一验证 AgentSociety 与 CitySim | 出行距离、回转半径、OD 流、时间节律、motif、行为画像、语义活动及转移 | 能复现部分粗粒度活动和简单惯例，但空间流、时间节律、活动顺序和探索异质性偏差明显 | 提供宏观经验依据；CityAgency 提供受控的微观失效原因 |
| [CitySim](../../assets/papers/notes/02_citysim_agents/01_CitySim_Wang2025.md) | 价值驱动 Agent 能否产生类人的日程、移动、对话和聚合城市现象 | 使用需求、习惯、信念、目标和空间记忆进行递归活动规划，并做微观 Judge 与宏观数据比较 | 活动、对话、移动和反应的 1-5 类人度；时间利用与 POI 热度相关性 | 提出的模块提高了类人度，但存在循环 LLM Judge 和现实上下文缺失问题 | 是模拟系统，不是带私有目标 verifier 和统一失败分类的可重置 benchmark |
| [GATSim](../../assets/papers/notes/02_citysim_agents/02_GATSim_Liu2025.md) | 移动专用生成式 Agent 是否能做出自适应且类人的交通决策 | 50 个受控案例比较 Agent 和人类角色扮演回答，再验证宏观交通模式 | 配对胜率、情境适切性、推理一致性、行为合理性、出发和拥堵模式 | Agent 在角色扮演比较中接近人类，但不是与真实出行行为比较 | CityAgency 验证实际状态变化和目标证据，而不只评价决策文本是否像人 |
| [GenWorld](../../assets/papers/notes/07_large_scale_urban_sim/01_GenWorld_Li2026.md) | 经验数据驱动的 LLM-Agent 城市能否扩展到完整人口 | 用人口和地理数据构造 196,608 个居民，把教师模型决策编译为离线策略，运行工作日、周末和扰动场景 | 人口与就业地匹配、活动和移动分布、运行效率、扰动响应 | 离线策略编译使城市尺度 LLM-Agent 研究具有可行性 | CityAgency 保持在线决策和小规模，使个体执行错误可观测 |
| [Limits of Agency](../../assets/papers/notes/07_large_scale_urban_sim/02_Limits_of_Agency_Chopra2025.md) | 行为表达能力与 ABM 人口规模如何权衡 | 在 840 万人纽约疫情与经济模型中比较启发式、完全 LLM 和 Archetype Agent | 预测与反事实拟合、计算规模、行为异质性 | Archetype 级 LLM 调用可支持人口尺度模拟，但会压缩个体差异 | CityAgency 研究高分辨率 agency，而不解决人口尺度计算 |
| [TrajGenAgent](../../assets/papers/notes/08_route_planning_agents/03_TrajGenAgent_Li2026.md) | 无需微调的个性化移动轨迹生成 | LLM 生成基于历史证据的活动链，再用确定性流程落地点、旅行时间和停留时间 | 聚合时空统计、行为异常和语义异常 | 分层 grounding 同时改善统计拟合和个体轨迹一致性 | 属于开环轨迹生成；CityAgency 测闭环行动、结果观察和重规划 |
| [AgentMob](../../assets/papers/notes/08_route_planning_agents/04_AgentMob_Chen2026.md) | 高效且有证据支撑的下一地点预测 | LLM 调用移动分析工具箱，并使用 fast path 控制成本 | Brightkite、YJMob100K、Shanghai ISP 上的 Acc@1 等排名指标 | 工具证据有帮助，但不同数据集性能差异很大 | 预测依据不等于行动发生后的环境证据 |

## B. 城市 LLM 与具身城市 Benchmark

| Reference | 想测什么 | 测试方法 | 主要指标 | 主要结论 | 与 CityAgency 的边界 |
|---|---|---|---|---|---|
| [CityBench](../../assets/papers/notes/01_urban_benchmarks/01_CityBench_Feng2024.md) | LLM/VLM 的城市感知、理解、规划和决策能力 | CityData 与 CitySimu；13 个城市、8 类任务、约 30 个模型 | Accuracy、F1、RMSE、R2、导航成功率、步数、距离、排队长度、吞吐量 | 常识和语义任务较好，专业知识、数值地理预测和交通控制较弱 | 不测试居民 Agent 在一个连续 episode 中维持私有意图 |
| [USTBench](../../assets/papers/notes/01_urban_benchmarks/04_USTBench_Liu2025.md) | 城市 Agent 的过程级时空推理 | UAgentEnv 中测试理解、预测、规划和反思；62,466 个 QA 与 9 个下游任务 | QA Accuracy、MAPE、拥堵预测、可达性、生态覆盖、道路成本和旅行距离 | 理解和预测强于长期规划与反馈反思；通用推理模型不一定更好 | CityAgency 关注 Agent 实际做了什么，以及世界状态能否证明完成 |
| [CityEQA](../../assets/papers/notes/01_urban_benchmarks/08_CityEQA_Zhang2025.md) | Agent 能否在 3D 城市主动探索并回答开放问题 | 1,412 个任务；PMA 分层执行导航、探索和信息收集 | 问答准确率、Navigation Error、Mean Time Steps | PMA 达到人类问答准确率的 60.73%，但效率低且存在长程错误累积 | 测外部分配的 EQA，CityAgency 测内部目标、承诺、扰动和完成证据 |
| [EmbodiedCity](../../assets/papers/notes/03_embodied_city/01_EmbodiedCity_Zhou2024.md) | 开放城市中的多模态感知、导航和规划能力 | 3D 城市中的场景理解、QA、对话、VLN 与任务规划 | BLEU、ROUGE、METEOR、CIDEr、Sentence-BERT、SR、SPL、NE | 大模型整体更强，但长距离导航明显退化 | 强具身参考，但不隔离私有目标驱动的日常城市行为 |

## C. 社会与人类行为 Benchmark

| Reference | 想测什么 | 测试方法 | 主要指标 | 主要结论 | 与 CityAgency 的边界 |
|---|---|---|---|---|---|
| [SOTOPIA](../../assets/papers/notes/04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.md) | Agent 在部分可观测社会互动中实现私有目标的能力 | 用场景、角色、关系、秘密和私有目标构造多轮角色扮演 | Goal、Believability、Knowledge、Secret、Relationship、Social Rules、Financial Benefit | SOTOPIA-hard 上存在显著人类差距；模型容易泄密、违规并被交互对象带偏 | 提供 episode 结构；CityAgency 加入地图、移动、时间、资源和确定性轨迹验证 |
| [AgentSense](../../assets/papers/notes/04_social_benchmark_foundations/03_AgentSense_2024.md) | 多目标复杂互动中的目标完成和隐私推理 | 从剧本构造 1,225 个多人场景，进行互动、访谈和隐私问答 | 多视角目标完成、隐私推理准确率、Profile Sensitivity Index | 高层成长目标、竞争、冲突处理和私有信息推理仍然困难 | 行动空间主要是对话，不包含可执行城市状态变化 |
| [Lifelong-SOTOPIA](../../assets/papers/notes/04_social_benchmark_foundations/04_Lifelong_SOTOPIA_2025.md) | Agent 是否能跨 episode 保持社会能力并利用记忆 | 每对角色最多连续 40 个 episode，比较完整历史和摘要记忆 | Goal Completion、Believability、扩展一致性检查和随时间的性能变化 | 交互越长，目标完成和可信度越低；高级记忆有帮助，但历史依赖任务仍落后人类 | 可启发 CityAgency 的跨日地点、承诺和历史扰动记忆测试 |
| [Misleading Success](../../assets/papers/notes/04_social_benchmark_foundations/05_Misleading_Success_2024.md) | 全知视角是否夸大 Agent 的社会能力 | 比较 SCRIPT、AGENTS 和 MINDREADERS 三种信息条件，并加入微调实验 | 目标完成、自然度、交易结果和 SOTOPIA 指标 | 全知模拟看起来更成功，但在真实信息不对称下性能明显下降 | CityAgency 必须将 Agent 观察与环境权威状态分离 |
| [Multi-Turn Human Behavior](../../assets/papers/notes/04_social_benchmark_foundations/06_Can_LLM_Agents_Simulate_Multi_Turn_Human_Behavior_2025.md) | 可信 Agent 是否真的复现人类逐步动作 | 在 31,865 个真实购物 session 上预测下一动作 | 每个 session 的 Exact Match Action Accuracy 和最终购买 F1 | 最佳 prompted model 动作准确率约 11.86%；微调后仍然有限 | 支持区分表面可信度和轨迹真实性；CityAgency 初期先验证逻辑轨迹，后续再加入人类城市轨迹 |
| [LiveCultureBench](../../assets/papers/notes/04_social_benchmark_foundations/07_LiveCultureBench_Pham2026.md) | 居民能否在动态小城中完成每日目标并遵守文化规范 | 图结构城市、目标居民和支持居民、5 类任务、英德中画像、结构化 Verifier、Conformal Uncertainty 和人工标注 | Goal Completion、规范违反、任务-规范权衡、跨文化退化、Verifier 不确定性 | 强模型常能保持目标完成，但文化适切性下降；不确定样本仍需人工监督 | 已覆盖城市图、每日目标、支持 Agent 和 Verifier；CityAgency 必须以有类型的物理状态变化和 impossible-trace 证据区分 |

## D. Agent 执行、可行性与状态验证

| Reference | 想测什么 | 测试方法 | 主要指标 | 主要结论 | 与 CityAgency 的边界 |
|---|---|---|---|---|---|
| [ChinaTravel](../../assets/papers/notes/06_agent_execution_benchmarks/01_ChinaTravel_Shao2024.md) | 开放多日旅行计划是否满足组合硬约束与软偏好 | 旅行 sandbox 加 DSL；使用 1,154 名参与者的开放需求 | Delivery Rate、Environmental/Logical/Conditional/Final Pass Rate、偏好排序 | 神经符号方法显著优于纯 LLM，但人类请求上的最终通过率仍约 37% | 验证行程方案，CityAgency 进一步验证逐事件执行、重规划和社会承诺 |
| [FeasiGen](../../assets/papers/notes/06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.md) | Agent 是否能识别任务已不可行并正确停止 | 从成功轨迹提取关键工具，屏蔽工具构造不可行变体 | 可行任务成功率、False Continue Rate、正确早停与失败继续的 Token Cost | FCR 为 23.5%-73.9%；多 Agent 分解将平均 FCR 从 54.6% 降至 17.5% | CityAgency 还要区分改道、替代、等待和有理由放弃 |
| [tau-bench](../../assets/papers/notes/06_agent_execution_benchmarks/03_tau_bench_Yao2024.md) | Agent 与用户互动、遵守规则并稳定改变状态的能力 | 零售和航空场景；调用 API；比较最终数据库与目标状态 | `pass^1`、`pass^k`、`pass@k` | 单次成功不代表可靠，多次全部成功的概率快速下降 | 提供权威状态和重复实验先例；CityAgency 还验证中间移动轨迹 |
| [AppWorld](../../assets/papers/notes/06_agent_execution_benchmarks/04_AppWorld_Trivedi2024.md) | 跨应用复杂数字任务的执行能力 | 9 个应用、457 个 API、750 个任务；状态单元测试允许多种解法并检查副作用 | Task Goal Completion、Scenario Goal Completion | GPT-4o 约完成 49% 普通任务和 30% 困难任务 | 可借鉴 verifier 和 collateral damage；CityAgency 将其用于位置、物品、预算、时间和其他 Agent |
| [WebArena](../../assets/papers/notes/06_agent_execution_benchmarks/05_WebArena_Zhou2023.md) | 真实网页环境中的长程功能正确性 | 可重置网站、浏览器动作和多类结果检查 | End-to-end Task Success Rate | 最佳 GPT-4 Agent 为 14.41%，人类为 78.24% | 说明可重置世界与结果检查的重要性；CityAgency 增加物理可行性和轨迹可信度 |
| [TheAgentCompany](../../assets/papers/notes/06_agent_execution_benchmarks/06_TheAgentCompany_Xu2024.md) | 跨工具、代码、网站和同事的后果性专业任务 | 模拟软件公司中的 175 个任务，用加权 checkpoint 评价 | 完整成功率、部分完成得分、步骤数和 Token Cost | 最佳 Agent 完整完成 30.3%，部分得分 39.3% | 可借鉴多方任务和部分得分；CityAgency 将后果落实为空间、时间和承诺变化 |
| [MobilityBench](../../assets/papers/notes/08_route_planning_agents/01_MobilityBench_Song2026.md) | 真实移动请求上的可复现路线 Agent 能力 | 22 个国家、350 多个城市的 100,000 条高德请求，确定性回放路线 API | 结果有效性、指令理解、规划、工具使用和效率 | 基础检索和普通路线较好，个性化偏好约束明显更难 | 测单次移动请求；CityAgency 测多动作 episode 中持续变化的状态和证据 |
| [DeliveryBench](../../assets/papers/notes/08_route_planning_agents/02_DeliveryBench_Mao2025.md) | 城市配送任务中的长程、约束感知具身执行 | 7 个 VLM Agent 和人类在 9 个程序生成城市设置中运行 2 个虚拟小时 | 净利润、规划、截止时间/成本/电量合规、交互和完整轨迹 | 所有模型仍显著落后人类，决策短视并经常违反常识约束 | 与城市执行直接重叠；CityAgency 增加通用私有意图、不可行配对、完成声称审计和框架适配器 |

## E. 验证与机制主张

| Reference | 想测什么 | 测试方法 | 主要指标 | 主要结论 | 与 CityAgency 的边界 |
|---|---|---|---|---|---|
| [Validation Is the Central Challenge](../../assets/papers/notes/09_surveys/03_Validation_Central_Larooij2026.md) | 生成式 ABM 的验证方法是否匹配其科学目的 | 系统综述并分类目标系统和验证方法 | 文献覆盖与验证证据、建模目标之间的定性一致性 | 研究经常依赖面孔效度或与机制弱相关的结果指标，LLM 不透明性和随机性会加重验证问题 | CityAgency 只验证一个狭窄的 Agent 层机制，不能单独验证宏观城市主张 |
| [Mechanism Plausibility](../../assets/papers/notes/09_surveys/04_Mechanism_Plausibility_Zhao2026.md) | 模拟对现象或解释性主张的支持强度 | 从 Sandbox 到有经验依据机制的四级清单，并用双评审校准 | Agent 层和 ABM 层等级、Weighted Kappa | 论文经常把 Agent 层证据误当成 ABM 层可信度；评审一致性也只有一般到中等 | CityAgency 应公开构念审计，并把结果表述为执行机制证据，而不是人类或城市层真实性证明 |

## 跨 Benchmark 结论

| 被验证的对象 | 代表工作 | 通过意味着什么 | 仍不能证明什么 |
|---|---|---|---|
| 城市能力答案 | CityBench、USTBench | 模型能回答或优化特定城市任务 | Agent 能连续经历并完成一个城市 episode |
| 社会互动质量 | SOTOPIA、AgentSense、LiveCultureBench | 对话或城镇互动能合理追求私有目标并可能遵守规范 | 物理行动和声称结果在权威城市状态中真实发生 |
| 移动真实性 | MobiSim-Bench、When Plausible Is Not Realistic | 生成群体在部分指标上接近人类移动 | 某个 Agent 持续维护并完成了自己的意图 |
| 可执行结果 | ChinaTravel、tau-bench、AppWorld、MobilityBench、DeliveryBench | 计划、路线、配送 episode 或最终状态满足明确约束 | 通用居民意图能在不同城市 Agent 框架中持续产生证据 |

因此，CityAgency 的可辩护缺口不是“以前没人测过城市 Agent”，而是：

> 现有工作已经测试城市推理、小城社会目标、路线执行、约束密集的配送 episode、经验
> 移动分布和可执行最终状态。CityAgency 测试不同城市 Agent 框架能否把合理的私有计划
> 执行为连续且环境有效的轨迹，并由有类型的状态变化支持其完成声称。

## CityAgency 应借鉴的组件

| CityAgency 组件 | 参考先例 | 在 CityAgency 中的实现 |
|---|---|---|
| 目标证据 | tau-bench、AppWorld、MobilityBench | 对位置、库存、预算、消息、共处和截止时间执行确定性谓词与回放 |
| 组合约束 | ChinaTravel | 为每个场景附加机器可读的硬约束与软偏好 |
| 不可行性意识 | FeasiGen | 构造可行/不可行配对，测错误继续、正确停止和修复成功 |
| 私有目标和社会压力 | SOTOPIA、AgentSense | 隐藏目标、关系、打断和独立的社会质量评分 |
| 信息边界 | Misleading Success | 将 Agent 可见观察与环境权威状态分开 |
| 长期记忆 | Lifelong-SOTOPIA | 连接多个 episode，测试地点、承诺和扰动记忆 |
| 轨迹真实性 | MobiSim-Bench、经验移动验证 | 先验证边和时间连续性，后续加入真实人类移动数据 |
| 重复可靠性 | tau-bench | 多次运行并报告全部运行成功的可靠性指标 |
| 软性可信度 | SOTOPIA、GATSim、LiveCultureBench | LLM/人类 Judge 只评价可信度和社会质量；不确定样本升级人工，不负责最终完成裁定 |
| 主张边界 | Validation Review、Mechanism Plausibility | 分开报告 Agent 层机制证据、行为真实性和宏观城市有效性 |

## 我们的工作

| Reference | 想测什么 | 测试的架构或模型 | 测试方法 | 主要指标 | 当前结果或预期结论 | 对城市研究的意义 |
|---|---|---|---|---|---|---|
| **CityAgency（ours）: Plausible Plans, Impossible Traces** | LLM 城市 Agent 能否把合理的私有计划执行为连续、可行、可信且可由环境证明完成的城市轨迹 | 当前：Utility Planner、API LLM Direct Actor、Plan-then-Act、Reactive Replanner；后续固定架构比较多种 LLM，并接入 CitySim/GATSim 类 Agent | 在可重置微型城市中设置私有目标、时间窗、预算、POI、社会关系和中途扰动；Agent 逐步行动，环境更新权威状态；确定性 verifier 判断完成，Judge 只评价软性可信度；同任务重复运行 | Goal Completion、Trace Feasibility、Impossible Trace Rate、Budget Consistency、Intention Consistency、Replanning Success、False Continue、False Completion Claim、Trace Believability、Face-Trace Gap、`pass^k` | 初步 12 场景实验中，Plan-then-Act 整体最好；Direct Actor 虽有较高目标完成和可行性，但轨迹可信度明显较低，初步支持“合理结果不等于可信执行”。最终论文结论仍需更多模型、架构、人类基线和真实城市数据验证 | 为使用 LLM Agent 研究交通、活动、设施可达性、灾害响应和政策行为提供微观有效性检查，避免把语言流畅但不可执行的合成轨迹当作城市证据 |

