# GPT-5.4 预实验正式报告（20轮核心子集）

> 日期：2026-03-19  
> 模型：`gpt-5.4`  
> 提供商：`aixj.vip`  
> 实际可用接口：`/v1/chat/completions`  
> 批次范围：`20` 个独立在线重复  
> 任务范围：`comprehension`、`behavioral_inference`、`prompt_position`

## 摘要

本报告整理了 `gpt-5.4` 在 SpatialAgent v7 预实验中的 `20` 轮核心在线测试结果。  
本批次的目标是验证三个最直接影响后续实验启动决策的门控问题：

- 模型是否稳定通过 `LLM gate`
- prompt 位置是否存在较稳定的优选
- 单轮满分是否只是偶然现象

结论如下：

- `comprehension` 平均准确率为 `0.95`
- `behavioral_inference` 平均准确率为 `0.9167`
- `prompt_position` 平均准确率为 `0.9194`
- 按当前门槛，`20` 轮中有 `14` 轮通过理解门控
- 推荐 prompt 位置以 `system_prefix` 为主，占 `14/20`

因此，`gpt-5.4` 在当前任务上**总体具备进入后续预实验与阶段1的能力**，但表现存在可见波动，不宜只依赖单轮结果做最终判断。

## 运行设置

- 使用仓库内预实验编排脚本：`experiments/run_preflight.py`
- 使用 `gpt54` 配置：`configs/experiments/preflight_v7.yaml:24`
- 在线接口经健康检查确认：
  - `GET /v1/models` 可用
  - `POST /v1/chat/completions` 可用
  - `POST /v1/responses` 返回 `502`
- 因此本批次固定走 `chat/completions`
- 为控制总时长，本次 `20` 轮只跑核心子集，不包含：
  - `reverse_inference_audit`
  - `lexical_norming`
  - `coding_pilot_llm`

说明：这些扩展项已经完成**单轮**在线预实验，可参考 `results/preflight/reports/preflight_summary.md:1`。

## 汇总结果

### 1. 理解门控

当前门槛：

- `Comprehension >= 0.85`
- `Behavioral Inference >= 0.70`

20轮平均结果：

- `comprehension_mean_accuracy = 0.95`
- `behavioral_inference_mean_accuracy = 0.9167`

按轮通过情况：

- `gate_pass_count = 14 / 20`

解释：

- 从均值看，`gpt-5.4` 明显高于门槛
- 从逐轮看，存在少量波动轮次，说明该模型在该供应商链路下并非完全无噪声

### 2. Prompt 位置

20轮平均 prompt 准确率：

- `prompt_mean_accuracy = 0.9194`

推荐位置分布：

- `system_prefix = 14`
- `memory_suffix = 4`
- `action_context = 2`

解释：

- 三种位置都可以工作
- 若必须固定单一方案，当前证据最支持 `system_prefix`
- 这与早先单轮结果一致，但 20 轮结果让这个结论更稳

### 3. 稳定性观察

逐轮结果显示：

- `comprehension` 只有少数轮次降到 `0.6667`
- `behavioral_inference` 波动略大于 `comprehension`
- `prompt_position` 前半段波动明显，后半段趋于稳定
- 第 `15-20` 轮三项指标都达到或接近满分

这提示两种可能：

- 供应商侧推理链路或路由存在轻微随机性
- 当前任务规模较小，单题失误会明显拉低单轮比例

## 决策建议

基于本批次，建议把以下内容写入正式预实验决策：

- `gpt-5.4` 作为当前可用主模型之一，可以继续使用
- `system_prefix` 作为默认 prompt 位置
- 对“是否通过理解门控”的表述应采用：
  - **均值层面通过**
  - **单轮层面存在波动**
- 若后续要写入论文或正式方法附录，建议报告：
  - `20` 轮平均准确率
  - `14/20` 轮门控通过
  - prompt 位置选择频数

## 局限

- 本报告只覆盖核心门控子集，不等于完整 preflight 全套稳定性
- `reverse_inference_audit`、`lexical_norming`、`coding_pilot_llm` 尚未做 `20` 轮重复
- 当前结果依赖特定供应商链路 `aixj.vip`
- 当前任务题量较小，单轮准确率对个别题目失误敏感

## 产物

- 汇总 JSON：`results/preflight/gpt54_core20/aggregate_summary.json:1`
- 逐轮 CSV：`results/preflight/gpt54_core20/aggregate_runs.csv:1`
- 单轮完整 preflight：`results/preflight/reports/preflight_summary.md:1`

## 推荐写法

可在论文方法或内部记录中使用如下表述：

> On March 19, 2026, we ran 20 independent online preflight repetitions for the GPT-5.4 actor on the core gating subset (comprehension, behavioral inference, and prompt-position tasks). Mean accuracies were 0.95, 0.9167, and 0.9194, respectively. The model passed the gate in 14 of 20 runs, and `system_prefix` was the most frequently selected prompt placement (14/20).

