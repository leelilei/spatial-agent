# Research canon

## Literature facts

1. 非随机缺失标签的半监督学习已经存在成熟工作：
   - Hu et al., *On Non-Random Missing Labels in Semi-Supervised Learning*,
     ICLR 2022，提出 class-aware propensity、imputation 与 doubly robust
     估计；
   - Duan et al., *Towards Semi-supervised Learning with Non-random Missing
     Labels*, ICCV 2023，处理类别分布不匹配下的伪标签纠偏。
2. Xie et al., *Semi-supervised Learning with Support Isolation by
   Small-Paced Self-Training*, AAAI 2023，研究由过滤机制导致的 labeled /
   unlabeled 支持域隔离。
3. Rodríguez et al., *Fine-Grained Species Recognition with Privileged
   Pooling*, TPAMI 2023，已经覆盖训练期关键点监督、细粒度识别、少样本和
   偏置数据；其 CCT20 设置包含约 13K 训练图和约 1,180 张关键点标注图。
4. Learning Using Partially Available Privileged Information（LUPAPI）已经
   研究只在部分训练样本中提供特权信息，但现有代表工作主要是医疗 SVM
   场景，并未处理部件标注的选择机制。
5. Privileged knowledge distillation 与 selective distillation 已研究错误
   教师导致的负迁移及自适应权重，但代表工作不是非随机缺失部件标注。
6. 截至 2026-07-28 的 CrossRef、arXiv、CVF、OpenReview/PMLR 与官方
   论文页检索中，尚未找到同时满足以下条件的工作：
   - 每张图类别标签完整；
   - 只有部件/区域特权标注选择性缺失；
   - 显式区分 MCAR / MAR / MNAR；
   - 以最终细粒度或少样本分类负迁移为核心终点；
   - 同时包含完整标注 Oracle 与真实选择偏差压力测试。
7. 上述“尚未找到”不是绝对新颖性证明；Scopus、Web of Science、CNKI、
   专利和完整引用链仍待复核。

## Experimental facts

1. WikiChurches 官方构件框具有风格判别信息：
   church-disjoint prototype balanced accuracy 为 73.43%，匹配随机区域为
   49.22%。
2. 普通 nnPU/IPW 与高可信正例扩展均未超过 Ignore。
3. 三代 positive-only 局部融合器均未通过 validation-only 停止门槛。
4. 90 个带框 train church 的 Global CLIP train→validation balanced
   accuracy 从 84.46% 降至 57.36%，分层置换 p=0.00120。
5. 同一子集的 Local residual balanced accuracy 从 86.22% 降至 52.18%，
   p=0.00070；Gothic recall 下降 65.43pp。
6. 全部 canonical-train church 与 validation 的 global control 不显著偏移，
   p=0.47965。
7. 当前证据支持“局部框有信息，但带框样本子集存在选择性覆盖偏差”；不支持
   “只需进一步调整局部融合器”。
8. WikiChurches canonical test 在上述开发中编码数始终为 0。

## Model facts

1. 训练数据形式定义为：

   \[
   \mathcal D=\{(x_i,y_i,s_i,s_i z_i)\}_{i=1}^{N},
   \]

   其中图像 \(x_i\) 与最终类别 \(y_i\) 对所有训练样本可用；部件特权标注
   \(z_i\) 仅在选择变量 \(s_i=1\) 时可见。
2. MCAR：\(s\) 与 \(x,y,z\) 独立；MAR：\(s\) 可依赖已观测的 \(x,y\)；
   MNAR：\(s\) 还可能依赖未观测部件状态 \(z\) 或其可见性/典型性。
3. 当 \(P(s=1\mid x,y)=0\) 的区域存在时，普通 inverse propensity
   weighting 不能识别该区域的特权监督收益；必须报告 support violation，
   不能用极端权重掩盖。
4. Global-only 是安全参照，不是弱基线；任何局部方法都必须同时报告平均
   收益和最差类别/机制的负迁移。

## Supervisor constraints

1. 目标仍是少样本细粒度模式识别方法论文，而不是仅对 WikiChurches 的应用。
2. 实验必须端到端且包含消融，但不能在问题未成立前堆叠复杂网络。
3. WikiChurches 中构件语义难以由非专家稳定识别，不再依赖大规模人工补框作为
   主证据。
4. 优先进行便宜、可停止、能排除方向的实验。

## Terminology definitions

- Privileged part annotation: 训练时可用、推理时不可用的部件点、框或 mask。
- Annotation selection variable \(s\): 某样本是否获得部件特权标注。
- Annotation support: 满足 \(P(s=1\mid x,y)>0\) 的输入—类别区域。
- Negative transfer: 加入局部特权监督后，最终分类风险高于同训练预算下的
  global-only。
- Safe transfer: 在预注册评价范围内控制平均及分组负迁移；当前阶段不等同于
  分布无关的理论保证。

## Forbidden claims

1. 禁止声称“首次研究非随机缺失标签”；该问题已有 ICLR 2022 和 ICCV 2023。
2. 禁止声称“首次用部件标注提升细粒度/少样本识别”；Privileged Pooling 等已覆盖。
3. 禁止把 sparse part supervision、LUPI、propensity weighting、self-training、
   selective KD 或 OOD gate 单独列为创新。
4. 禁止把 WikiChurches 诊断解释为构件标注选择机制的因果证明。
5. 禁止在没有完整标注 Oracle 的数据上估计真实 MNAR 恢复误差。
6. 禁止把 validation 上调出的规则称为 train-only 安全机制。
7. 禁止在开发完成前加载 canonical test。

## Unresolved claims

1. 完整问题组合是否在 Scopus、Web of Science、CNKI 或最新预印本中已有同题工作。
2. PartImageNet 的官方 split、part ontology 和许可是否适合形成完整实验。
3. WikiChurches 的真实选择变量是否可由已观测图像/类别近似，还是存在不可识别的
   MNAR 成分。
4. 支持域感知的局部迁移能否稳定优于 global-only，而非仅通过回退实现零收益。
5. 是否能建立强于普通 PRG/CADR/Small-Paced Self-Training/Privileged Pooling
   直接适配的机制差异。

