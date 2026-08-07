# Evidence table

| Claim | Evidence/source | Strength | Usable section | Risk | Status |
|---|---|---|---|---|---|
| WikiChurches 构件框包含最终风格信息 | PAT-B-260727-002：73.43% vs 49.22% church-disjoint BA | 强 | Motivation / Problem Analysis | 只证明信息性 | evidence-backed |
| 带框样本子集不代表目标分布 | PAT-B-260728-001：global drop 27.10pp, p=0.00120；全部 train control p=0.47965 | 强 | Motivation / Real-world Evidence | 非因果 | evidence-backed |
| 选择偏差会导致局部知识负迁移 | PAT-B-260727-003/004/005：三代融合器均触发类别安全停止 | 中强 | Motivation / Baselines | 方法特异性 | evidence-backed |
| 非随机缺失类别标签已有成熟研究 | ICLR 2022 CADR；ICCV 2023 PRG | 强 | Related Work | 必须避免宽泛 novelty claim | evidence-backed |
| 支持域隔离已有渐进 self-training 解法 | AAAI 2023 Small-Paced Self-Training | 强 | Related Work / Baselines | 与拟议支持迁移相近 | evidence-backed |
| 部件特权监督可改善少样本和偏置数据泛化 | TPAMI 2023 Privileged Pooling | 强 | Related Work / Baselines | 最接近直接先例 | evidence-backed |
| 部分可用特权信息已有 LUPAPI | IEEE JBHI 2021 | 强 | Related Work | 不能把“部分 PI”作为创新 | evidence-backed |
| 非随机缺失部件 PI 的安全迁移是独立问题 | 当前检索未见完整五条件重合 | 中 | Gap / Research Question | 负面检索不能证明绝对首次 | plausible-inference |
| 估计 annotation support 可减少负迁移 | 尚无本项目实验 | 弱 | Hypothesis / Method | 可能仅学会回退 | hypothesis |
| 风险下界门控可在多个 MNAR 机制下优于 global-only | 尚无本项目实验 | 弱 | Hypothesis / Experiments | 关键 Go/No-Go | hypothesis |
| PartImageNet 可提供完整 mask Oracle | 官方 Seg archive 3,124,435,169 bytes，SHA256 精确通过；PAT-C-260728-001 train 1,600 / val 170 | 强 | Dataset / Experiments | ImageNet/CLIP 预训练重叠 | evidence-backed |
| 冻结 CLIP 线性局部残差的 Oracle 上界不足 | PAT-C-260728-001：validation 三 seed 平均 +0.7407pp，最差类别 −11.1111pp | 强 | Results / Stopping rule | 只否定当前机制，不否定研究问题 | evidence-backed |
| 论文式监督注意力池化仍无法修复冻结 patch 上界 | PAT-C-260728-002：train OOF +1.625pp，最差类别 −6.25pp；0/6 候选安全 | 强 | Results / Mechanism boundary | 只否定冻结 patch head | evidence-backed |
| 有限 backbone adaptation 后完整部件 Oracle 仍无正向上界 | PAT-C-260728-003：Adapted Global 94.5625%，Adapted PrPool Oracle 94.0625%，差 −0.5000pp，最差类别 −2.5000pp | 强 | Results / Stopping rule | 只否定当前 PartImageNet 设置与机制族 | evidence-backed |
| CUB 具有正向关键点特权监督 Oracle 上界 | PAT-D-260728-001：Global 65.45%，Full-Keypoint Oracle 70.95%，五折均为正，总增益 +5.50pp | 强 | Results / Next experiment | ImageNet 预训练重叠；23% 类别下降 | evidence-backed |
| 当前 25% 标注预算下，非随机选择比 MCAR 导致更大伤害 | PAT-D-260728-002：MCAR 69.85%；MAR-X 70.15%；MNAR-Z 70.60%；SI-HARD 70.00%，预注册伤害门未通过 | 强反证（限当前设置） | Results / Stopping rule | 仅一个筛查 seed；偏置方向偏向典型/完整样本 | contradicted-in-current-setting |
| 12.5% 强稀疏和姿态支持隔离会相对 MCAR 造成至少 2pp 伤害 | PAT-D-260728-003：MCAR-1 69.65%；Atypical 69.55%；Incomplete 69.85%；SI-Pose 69.10%，最大下降仅 0.55pp | 强反证（限 CUB/PrPool） | Results / Direction decision | 单筛查 seed；但操纵差异很强 | contradicted-in-current-setting |
| CUB 10-shot 中每类仅一张关键点标注仍保留大部分平均收益 | PAT-D-260728-003：MCAR-1 69.65% vs Global 65.45%，+4.20pp；Full Oracle +5.50pp | 强 | Results / New direction | 类别级伤害仍存在；尚未做标注成本曲线 | evidence-backed |
| CUB 每类一张随机关键点标注的收益可重复且对选择稳健 | PAT-D-260728-004：三选择 seed BA 69.55/69.65/69.00%，均值 +3.95pp，保留 71.8% Oracle 增益，范围 0.65pp | 强 | Results / Main finding | 仅 train-only 10-shot CUB；类别负迁移率 24.2% | evidence-backed |
| 关键点标注预算存在明显边际收益递减 | PAT-D-260728-004：K1/K2/K4/Full 平均 BA 69.40/69.68/70.00/70.95%；K1→K4 成本四倍仅 +0.60pp | 强 | Results / Motivation for selection | Full Oracle 为历史冻结 reference，训练 seed 不同 | evidence-backed |
