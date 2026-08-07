# Evidence table

| Claim | 当前证据 | 状态 | 所需下一证据 |
|---|---|---|---|
| WikiChurches 局部框覆盖有限 | 139 图、631 框的原始 JSON | 已确认规模，不等于已确认漏标 | 双人盲审补全 |
| 官方标注倾向每图每 leaf label 只选一个实例 | 139 图仅 6 图含重复 leaf label；631 框仅 6 个为同图同标签后续实例 | 强提示代表性选择，尚非协议证明 | 层级兼容统计与作者确认 |
| 框外存在可由冻结 VLM 检索到的同标签候选 | 185/708 候选同时超过同图官方框中位数且在 69 标签中 rank≤5，覆盖 43/50 图 | 支持优先复核，不是正例证明 | 专家盲审候选精度 |
| 构件通常很小 | 原始框相对面积分布 | 可计算 | 报告中位数、四分位数 |
| 框外区域含正例 | 8 图配对复核中发现多处镜像/重复同类构件候选 | 初步支持，尚非盲审结论 | 双人独立新增框与原始框匹配 |
| PN 会受假负监督损害 | 25% 受控缺失探针中 PN−Ignore：ROC-AUC −0.008、AP −0.013，标签级 paired bootstrap CI 不跨 0 | 支持局部机制，尚未传递到 few-shot 分类 | 真实补全标注上的 PN/Ignore |
| 正确恢复隐藏正例存在上界增益 | 受控探针中 Oracle−PN：ROC-AUC +0.020、AP +0.032 | 支持受控上界，不是真实 Oracle | 人工补全训练标注 |
| 普通 PU 不足 | 8 抽样种子 × 9 标签 × 30 split：IPW−Ignore AUC −0.082（分层 95% CI −0.125–−0.043），AP −0.101（−0.149–−0.051） | 当前无裁决路线已确认 No-Go | 人工真值下的 PU/Oracle 对照 |
| 已知 q 的候选抽样校正有效 | 10,800 行结果中 IPW−unweighted nnPU AUC +0.018（+0.005–+0.034），8/8 sampler seed 为正 | AUC 机制可复现，AP 未确认 | 更大已知 q 样本或人工真值 |
| 高置信 U 可作为弱正例改善模型 | 保守 4/5 ensemble 投票后每 split 选 0.79 个；PositiveExpansion−Ignore AUC −0.0022（−0.0047–−0.0004）、AP −0.0067（−0.0137–−0.0008） | 不成立；8/8 seed、9/9 label 均无正 AUC 增益 | 人工确认候选，或停止 missing-positive 主张 |
| 官方构件框含有超出匹配随机区域的风格判别信息 | 97 个 train+val church、433 个框、3,464 个同图面积/长宽比匹配对照；图像级 CLIP style-margin 配对差 +0.00649，bootstrap 95% CI +0.00511–+0.00803；church-disjoint prototype balanced accuracy 73.43% vs 49.22% | 区域信息探针 Go；只证明选择框有信号，不证明端到端分类增益 | 已完成最小 positive-only adapter 传递实验，见下一行 |
| 原始 positive-only box-anchor 分数可稳定改善 Tip-F | 448px dense tokens、train-only 每类 16 锚点、8 组随机控制、1/4/16-shot×3 seed；1-shot +1.62pp，但 4/16-shot 均按稳健规则退回 γ=0；仅 1 个 shot 稳健为正、总胜场 2/9；test 编码数 0 | 不成立，开发阶段 NO-GO；未触碰测试集 | 若继续，只验证 train-only 类校准 residual evidence 与低置信门控，不再扩大直接加和网格 |
| Train-LOCO 类校准 residual evidence 可消除局部分支类别偏置 | 每类 8 锚点；90 个 train church LOCO 估计负类均值/尺度；低置信门控后 1-shot +1.13pp、4-shot +0.97pp，2 个 shot 稳健为正且总胜场 5/9，但 Gothic 平均 −10.26pp，Baroque +8.12pp；test 编码数 0 | 总体门槛改善但类别安全门槛失败，NO-GO；逐类独立校准不能修复跨类混淆 | 最多再验证一次 train-only 强收缩 4×4 multinomial residual head；仍失败则停止 WikiChurches 局部融合 |
| Train-only 4×4 multinomial residual head 可修复跨类混淆并迁移到 validation | 90 个 train-LOCO church 上选中 λ=0.01，稳健 CV balanced accuracy 86.28%；但 1/4/16-shot 所有非零 validation 候选均违反类别安全线，最接近候选仍使 Gothic 下降 5.77–13.46pp；最终全部回退 γ=0，test 编码数 0 | 不成立，最终 NO-GO；带框 train 子集内可分但不能迁移，支持选择偏差/覆盖不足解释 | 停止 WikiChurches 局部融合；需要补全代表性标注或更换具有完整区域监督的数据集 |
| 带框 train church 对 canonical validation 存在选择性覆盖偏差 | 同一 90 个带框 church 的 Global CLIP train→val BA 84.46→57.36（−27.10pp，分层置换 p=0.00120），Local residual 86.22→52.18（−34.03pp，p=0.00070）；Gothic recall −65.43pp、局部偏移排名第 1；全部 5,750 个 canonical-train church 的 global control 不显著（p=0.47965） | 支持；偏移特异于带框子集，而非一般 train–val 域差；test 编码数 0 | 查明标注/采样机制，或补标代表性 church；当前 validation 不再用于新融合器开发 |
| CUB 可提供完整区域 Oracle | CUB 主要提供部件点而非完整区域框 | 不成立 | 改写为合成缺失点监督，或另找区域数据 |
