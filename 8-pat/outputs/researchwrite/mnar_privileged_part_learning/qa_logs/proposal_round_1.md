# QA report

- Round: 1
- Mode: hybrid
- Text type: supervisor-facing proposal draft

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| 研究问题清晰度 | 9.0 | 类别标签完整、部件 PI 缺失及负迁移终点均独立定义。 |
| 科学张力 | 8.5 | WikiChurches 的“有信息但不可迁移”构成直接矛盾。 |
| 证据匹配 | 8.0 | 内部实验和最接近论文均已回链；绝对新颖性仍降级表述。 |
| 逻辑链 | 8.5 | 现实失败→受控 Oracle→候选机制→Few-shot/OOD→真实压力测试。 |
| 方法可行性 | 8.0 | 首个协议已有数据、表示、机制、arms、grid 与 test 禁令。 |
| 创新性 | 7.5 | 问题交叉点可辩护，但方法仍可能被视为已有模块组合。 |
| 风险边界 | 9.0 | Oracle、全关闭、support violation、validation 污染均有硬停止条件。 |
| 语言质量 | 8.5 | 未使用“首次”“保证”等不受支持的强化表达。 |

平均分：8.38 / 10。

## Main risks

1. 方法创新尚未由正结果支持；
2. Privileged Pooling 的直接适配可能已经足够强；
3. 合成 MNAR 与真实选择偏差之间只能建立压力测试，不能直接建立因果等价；
4. PartImageNet 与 foundation backbone 存在潜在预训练重叠。

## Required fixes

1. 完成 train-only manifest 并封存 SHA256；
2. 实现 Global、Naive、IPW、Support-aware 与 Oracle 的同预算版本；
3. 在首次 validation 读取前保存候选选择报告；
4. 若首轮 No-Go，不得围绕同一 validation 继续调 gate。

## Recommendation

当前达到 supervisor-facing internal draft，可进入实验；正式投稿文本必须等待
PAT-C-260728-001 结果和完整引用链查重。

