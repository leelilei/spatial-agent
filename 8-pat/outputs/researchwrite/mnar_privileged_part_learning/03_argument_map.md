# Argument map

## Scientific tension

- What is known:
  - 少量部件监督可以提高细粒度模型的数据效率和可解释性；
  - MNAR-SSL、部分特权信息学习和 selective distillation 各自已有方法。
- What is unknown:
  - 当最终类别标签完整、但部件特权标注只落在一个选择性样本子集上时，如何判断
    这些局部知识是否能安全迁移到未覆盖样本；
  - 如何区分“局部标注有信息”与“局部标注对目标分布可迁移”。
- Why the gap matters:
  - 直接训练局部分支可能在标注子集内部获得很高准确率，却损害目标分布中的类别；
  - 平均精度会掩盖某些类别的负迁移；
  - 若不显式建模标注支持域，增加昂贵部件标注可能反而降低最终识别。

## Central research question

> 在所有训练样本都有类别标签、但部件特权标注按非随机机制只覆盖部分样本时，
> 能否识别局部监督的有效支持范围，并在不稳定区域退回全局证据，从而避免细粒度
> 少样本分类的负迁移？

## Central thesis

候选论点是：把“是否拥有部件标注”作为观测变量，而不是默认其随机缺失；联合
估计标注支持、局部知识条件收益和不确定性，可以比无条件部件蒸馏更可靠地决定
局部知识何时可迁移。但该论点必须由完整标注 Oracle 下的 MCAR/MAR/MNAR 对照和
真实选择偏差压力测试共同验证。

## Supporting arguments

### Argument 1

- Claim: 局部标注的信息性不推出其对目标分布的可迁移性。
- Evidence: WikiChurches box-vs-random 探针通过，但三代融合器均 No-Go；
  split-shift 诊断显示偏移集中于带框样本子集。
- Limitation: 单一真实数据集，选择机制未知。

### Argument 2

- Claim: 现有 MNAR-SSL 和 LUPAPI 没有直接回答“类别标签完整、局部 PI 选择性缺失”
  的最终分类风险。
- Evidence: CADR/PRG 缺失的是类别标签；LUPAPI 不建模部件选择机制；
  Privileged Pooling 未系统区分部件标注 MCAR/MAR/MNAR。
- Limitation: 仍需完整引用链和闭源索引复核。

### Argument 3

- Claim: 完整部件标注数据可以将真实不可观测问题转化为可证伪的受控实验。
- Evidence: PartImageNet 提供 part segmentation，可隐藏标注并保留 Oracle。
- Limitation: 合成 MNAR 机制未必等价于 WikiChurches 的真实选择过程。

## Counterarguments / alternative explanations

1. Global-only 已足够强，局部监督在现代 foundation backbone 上没有增益。
2. 所谓安全门控可能只学会完全关闭局部分支，形成无贡献的“零伤害”。
3. PRG/CADR 或 Small-Paced Self-Training 的直接适配可能已经解决问题。
4. PartImageNet 的类别结构未必足够细粒度。
5. 真实 MNAR 在无额外假设下不可识别，任何 propensity 估计都可能失效。

## Final move

小规模完整 Oracle pilot 已表明冻结 CLIP 线性局部残差的 validation 上界仅
+0.74pp，并伴随 −11.11pp 最差类别伤害，因此该机制已经停止。研究题目暂时
保留，但下一步必须先复现更强的 Privileged Pooling 风格参考机制并重新建立
Oracle 上界；在此之前不进入 MNAR 纠偏。
