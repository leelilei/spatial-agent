# QA report

- Round: 0
- Mode: hybrid
- Text type: proposal foundation

## Scores

| Dimension | Score | Notes |
|---|---:|---|
| 研究问题清晰度 | 9.0 | \(x,y,z,s\) 已定义，问题可由负迁移终点证伪。 |
| 科学张力 | 8.5 | WikiChurches 已直接显示“有信息但不可迁移”的矛盾。 |
| 证据匹配 | 8.0 | 项目数值均可追踪；文献完整同题仍只能写“当前未检索到”。 |
| 逻辑链 | 8.5 | 诊断证据→新问题→完整 Oracle→安全迁移门槛闭合。 |
| 方法可行性 | 7.5 | 数据与冻结特征路线可执行；候选 gate 公式仍需协议化。 |
| 创新性 | 7.5 | 交叉问题有空位，但 Privileged Pooling、MNAR-SSL 和 selective KD 风险高。 |
| 风险边界 | 9.0 | support violation、全关闭退化和 test 冻结均已列为停止条件。 |
| 语言质量 | 8.5 | 术语与禁用表达明确。 |

平均分：8.31 / 10。

## Main risks

1. 最接近工作 Privileged Pooling 已覆盖稀疏关键点、偏置数据和少样本；
2. 候选安全机制可能退化成永远使用 global-only；
3. PartImageNet 的合成 MNAR 不必然代表真实选择机制；
4. 完整闭源索引与引用链查重尚未完成。

## Required fixes

1. 首次 validation 前冻结缺失机制、候选选择与回退率门槛；
2. 把 PRG、CADR、Small-Paced Self-Training 和 Privileged Pooling 列为必须适配的基线；
3. 将“不是全关闭”写为硬性 Go 条件；
4. 明确 Seg split 只做同类受控机制，OOD split 只在 Go 后做 few-shot。

## Recommendation

Foundation 分数超过 7.5，可进入 proposal 草稿和首个实验协议。

