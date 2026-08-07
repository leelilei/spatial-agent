# Section contracts

## Section: Introduction

- Purpose: 从“局部标注有信息但不可迁移”的矛盾引出问题。
- Inputs: WikiChurches PAT-B-260727-002/003/004/005 与 PAT-B-260728-001。
- Allowed claims: 项目实验观察到选择性覆盖偏差与负迁移。
- Forbidden claims: 选择机制已经得到因果识别；该问题绝对首次提出。
- Required evidence: 所有数值链接到正式实验日志。
- Validation checklist: 信息性、代表性、可迁移性三者必须分开表述。

## Section: Related Work

- Purpose: 区分 MNAR-SSL、support isolation、LUPI/partial PI、Privileged
  Pooling、selective KD 和 weakly supervised parts。
- Inputs: 专项查重表与原论文。
- Allowed claims: 当前检索未发现完整五条件重合。
- Forbidden claims: “现有工作均假设随机缺失”等绝对化表述。
- Required evidence: 每个差异点引用原论文问题定义或实验设置。
- Validation checklist: Privileged Pooling 必须作为最接近工作正面讨论。

## Section: Problem Formulation

- Purpose: 定义 \(x,y,z,s\)、MCAR/MAR/MNAR、annotation support 与 negative
  transfer。
- Inputs: 统计缺失数据定义、MNAR-SSL 与 LUPI 文献。
- Allowed claims: 在无 overlap 时普通 IPW 不可用；需要显式报告 support violation。
- Forbidden claims: 无额外假设下可完整识别真实 MNAR。
- Required evidence: 数学符号与假设逐项说明。
- Validation checklist: 最终类别标签必须对所有训练样本已知。

## Section: Candidate Method

- Purpose: 给出可证伪的 support-aware safe transfer 原型。
- Inputs: 全局分类器、局部特权教师、选择模型、条件收益估计。
- Allowed claims: 候选机制；预计控制预注册范围内负迁移。
- Forbidden claims: 理论安全保证、SOTA、完整方法已经成立。
- Required evidence: train-only 选择协议、回退规则与 ablation。
- Validation checklist: gate 不能读取 validation 标签；必须报告全关闭比例。

## Section: Experiments

- Purpose: 用完整 Oracle 区分 MCAR/MAR/MNAR，并在真实选择偏差上压力测试。
- Inputs: PartImageNet、CUB 点监督、WikiChurches。
- Allowed claims: 合成机制下的因果比较；真实数据上的关联性验证。
- Forbidden claims: 合成 MNAR 等价于现实 MNAR；WikiChurches test 可用于开发。
- Required evidence: 多 seed、类别级结果、最差机制、Oracle、计算预算。
- Validation checklist: 所有停止门槛和候选选择在首次 validation 前冻结。

## Section: Limitations

- Purpose: 明确不可识别性、数据集偏差、预训练重叠与安全定义范围。
- Inputs: 实验失败模式和数据来源。
- Allowed claims: 方法只在指定机制、数据和置信水平内有效。
- Forbidden claims: 用“未来工作”掩盖核心门槛失败。
- Required evidence: support violation、回退率、各机制结果。
- Validation checklist: 如果方法只等于 global-only，必须判为 No-Go。

