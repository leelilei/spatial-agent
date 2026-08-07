---
experiment_id: PAT-LIT-260729-011
date: 2026-07-29
status: completed-targeted-audit
scope: class-safe selective correction on frozen few-shot representations
---

# PAT-LIT-260729-011 文献与创新边界审计

## 结论

“根据置信度、邻域纯度和分类器分歧选择性地切换预测”本身不是新方法。
它与 dynamic classifier selection、META-DES 和局部混淆矩阵能力估计高度
接近。把查询集整体做图传播或分布优化，也会直接落入 TPN、
LaplacianShot、TIM 和 PT-MAP 的既有路线。

当前仍可验证、但尚不能预先声称创新成立的窄机制是：

> 在强冻结 RBF 上，仅用 fold-training 的嵌套 OOF 预测估计有序混淆对的
> 改判净收益，并以零历史伤害的保守门控限制改判；最终同时检验总体增益
> 和类别级零负迁移。

这里可能形成贡献的是“少样本场景下的无泄漏净收益估计、类别安全约束和
完整负迁移报告”的组合，而不是 RBF、kNN、原型或路由本身。若开发门通过，
仍需在写论文前对 2024--2026 年 selective prediction、dynamic selection
和 foundation-model few-shot adaptation 做一次更深的全文查重。

## 检索方法与局限

- 主题块：transductive few-shot inference、label propagation、optimal
  transport、selective classification/reject option、dynamic classifier
  selection、local competence/confusion matrix、few-shot calibration。
- 数据源：通过 OpenAlex API 检索其整合的 Crossref 与 arXiv 元数据，并按
  DOI/标题去重。
- 当前环境未挂载 academic-search MCP，因此未调用 Semantic Scholar、
  Scopus 或 Web of Science；本报告是定向查重，不是系统综述。
- 检索日期为 2026-07-29；引用数仅用于发现排序，不作为证据强度判断。

## 最近邻方法

| 文献 | 核心机制 | 与候选方案的关系 | 边界判断 |
|---|---|---|---|
| Ziko et al., *Laplacian Regularized Few-Shot Learning* (2020), doi:10.48550/arXiv.2006.15486 | 查询集图拉普拉斯正则化与联合指派 | 同为冻结表征后的纠正，但依赖整个 query graph | 不能把图传播写成新贡献 |
| Boudiaf et al., *Transductive Information Maximization for Few-Shot Learning* (2020), doi:10.48550/arXiv.2008.11297 | 在支持集监督下最大化查询预测互信息 | 同为冻结特征上的后处理 | 避免使用查询类别边际作为隐含先验 |
| Hu et al., *Leveraging the Feature Distribution in Transfer-Based Few-Shot Learning* (2021), doi:10.1007/978-3-030-86340-1_39 | PT-MAP，以最优传输匹配查询分布 | 与全局重分配/分布校准重叠 | 当前机制应保持逐样本、训练统计驱动 |
| Liu et al., *Learning to Propagate Labels: Transductive Propagation Network for Few-shot Learning* (2018), doi:10.48550/arXiv.1805.10002 | 学习图构造并向查询传播标签 | 覆盖可学习图传播路线 | 不开发新的 query-set label propagation |
| Veilleux et al., *Realistic Evaluation of Transductive Few-Shot Learning* (2022), doi:10.48550/arXiv.2204.11181 | 证明类平衡查询假设可导致显著性能下降 | 直接约束实验设计 | 不利用每类固定查询数做平衡校正 |
| Geifman and El-Yaniv, *Selective Classification for Deep Neural Networks* (2017), arXiv:1705.08500 | 置信度驱动的选择性预测 | “只处理低置信样本”已有成熟先例 | 本项目输出改判而非拒识，仍须明确区分 |
| Geifman and El-Yaniv, *SelectiveNet* (2019), doi:10.48550/arXiv.1901.09192 | 联合优化分类和拒识的 risk-coverage | 覆盖端到端 reject option | 不声称发明 selective prediction |
| Cruz et al., *Dynamic Classifier Selection: Recent Advances and Perspectives* (2018), doi:10.1016/j.inffus.2017.09.010 | 按样本局部能力选择分类器 | 与 RBF/原型/kNN 路由最接近 | 路由本身创新性不足 |
| Cruz et al., *META-DES* (2015), doi:10.1016/j.patcog.2014.12.003 | 用元特征估计基分类器局部能力 | 覆盖基于分歧、置信和邻域的元选择 | 不引入通用元路由器表述 |
| Trajdos and Kurzynski, *A Dynamic Model of Classifier Competence Based on the Local Fuzzy Confusion Matrix* (2016), doi:10.1515/amcs-2016-0012 | 用局部混淆与跨能力组合分类器 | 与混淆对可靠性直接相邻 | 有序混淆对统计不能单独作为创新点 |

## 对实验协议的约束

1. 使用标准 `SVC.predict` 作为不可替换的参考预测。
2. 不读取整个查询集的类别比例，不做平衡最优传输或图传播。
3. 所有阈值与混淆对可靠性必须在每个外折的训练部分通过 OOF 得到。
4. 外折评价标签不能参与策略选择、阈值、pair table 或回退决策。
5. 无可靠纠错证据时保留 RBF，不允许为了提高覆盖率强制改判。
6. 开发成功必须同时满足至少 +0.50pp 和零受损类别；否则停止并归档
   为 No-Go，不生成 episode 4/5。

## 可允许的论文表述

若且仅若跨新 episode 和第二数据集均通过，可使用：

- “class-safe selective correction under nested OOF estimation”；
- “post-hoc correction of a strong frozen classifier without query-label-marginal
  assumptions”；
- “joint overall-accuracy and class-level non-degradation gate”。

当前不得使用：

- “novel dynamic classifier selection”；
- “novel transductive label propagation”；
- “guaranteed safe”或理论保证；
- “state of the art”。
