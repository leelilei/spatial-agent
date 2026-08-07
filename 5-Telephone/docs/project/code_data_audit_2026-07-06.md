# M5 注入审计 + PROV/APM 传播代码复查(2026-07-06)

> 收割计划(`harvest_plan_2026-07-06.md`)第 2 步:补齐最后两个未审计项。
> 背景:P1-rec 曾因注入配置 bug 被撤回;07-01 核心审计覆盖了 M4/C3/C5/C16,
> 但 M5 数据与 PROV/APM 传播代码逻辑当时未查。本文档闭合这两项。零 API 成本。

## 一、M5(fig2_r30 长时程)注入审计 — **PASS**

方法:对 `sim/runs/fig2_r30/{baseline,source,broadcast}` 全部逐轮 `round_*.json`
统计 `injected` 数组条目数(P1-rec 式核查)。

| 条件 | 预期 | 实测 | 判定 |
|---|---|---|---|
| baseline (n=2) | 仅 r1 注入 1 人 | run_000/run_001:round_001=1,其余全 0 | ✅ |
| source (n=1) | r1 起每轮 1 人(持续源) | round_000=0;round_001–029 全=1(Rosa) | ✅ |
| broadcast (n=1) | r1 起每轮 25 人 | round_000=0;round_001–029 全=25 | ✅ |

M5 的"truth peaks ~r6 then decays"轨迹与 broadcast 持续高位结论建立在正确注入之上。
P1-rec 的 bug 确认为孤立事件(与 07-01 核心审计结论一致)。

## 二、PROV/APM 传播代码复查(`sim/memories.py` + `sim/society.py`)— **PASS**

逐条核对论文承重主张:

| 主张 | 代码事实 | 判定 |
|---|---|---|
| auth 只能由注入铸造 | `society.py:351` 注入路径独有 `auth:True, source:"ORIGIN"`;唯一铸造点 | ✅ |
| 对抗者无法铸 auth | `society.py:277` 伪造载荷硬编码 `auth:False`,且替换(非叠加)撒谎者的诚实转发 | ✅ |
| prov 只随真实相遇传播 | 载荷只存在于 `_run_encounter` 的 observations 中,无旁路;非听者接触不到 | ✅ |
| PROV "fair"(没被喂答案) | `PROVMemory.observe` 只认 event['prov'] 里听到的最高 version;无答案硬编码;更高版本的错误值同样会赢 | ✅ |
| APM K=独立源(非值频次) | `support[version][value][source]`,source=直接转发者 id,K 数 distinct sources | ✅ |
| 源头免佐证 | `observe`:`injected and auth` → 立即 commit(它就是 origin) | ✅ |
| abstain 语义 | 未 commit 时 `provenance()` 返回 None、`retrieve()` 明示 abstain | ✅ |
| 审计链真实 | commit 保存 sources+最短 path,relay 时 `path+[self_id]` 延伸 | ✅ |

### Caveat 1(不影响任何已报数字):APM 自回声 × garble 的潜在重提交路径

说者自己也 observe 自己的话语(`society.py:337-340` 双方都观察)。PROV 无害
(自己的 version 不高于自身,提前返回)。APM:自己转发的(已 commit 的)值会进入
自己的 support 表——正常时无害(commit 在先);但若 `prov_garble>0` 且 K=1,
理论上存在"自己 garble 出的 stale 值以相同 version 重提交给自己"的路径
(`_reconsider` 用 `>=`)。**已报结果无一命中该组合**(C15/C16 无 garble;
C17/C17b garble=0;garble 系列 C5-stress/C6/C7 用的是 PROV/PROVv2)。
若未来跑 APM×garble,需先修此处(`>=` 改 `>`,或排除 source==self_id)。

### Caveat 2(可复现性,非有效性):门控 RNG 未接 seed

`prov_loss/garble/mention` 的抽样用未播种的 `random.Random()`(`memories.py:303 等`),
不受实验 seed 控制。LLM 调用本身即非确定(temperature),多 seed+CI 的统计结论
不受影响;但同 seed 重跑不会逐位复现。论文无需改动;工程上可在未来把 factory
的 seed 传入门控 RNG。

## 结论

收割计划第 2 步闭合:M5 与 PROV/APM 代码两项均 PASS。至此论文承重的
数据层(07-01 核心审计 + 本次 M5)与代码层(本次)全部经过一手审计;
两条 caveat 均不触及任何已报告数字,已记录在案。
