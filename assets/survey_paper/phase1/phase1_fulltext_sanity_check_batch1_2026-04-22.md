# Phase 1 Full-Text Sanity Check Batch 1

日期：2026-04-22  
用途：把当前最值得先看的 `8` 篇高优先级新增条目落成一份统一核查表，用于决定它们是否进入下一轮 confirmed `Core`。

---

## 1. 这份表回答什么

对每篇全文，只先回答三件事：

1. 是否真的是 `LLM multi-agent` 系统
2. Agent 是否真的拿到了可访问的空间表示
3. 是否存在可识别的社会行为或群体互动

如果三项都能被全文支持，则该条目可进入 `confirmed Core` 候选主线。  
如果第 2 项或第 3 项站不住，则优先降回 `Adjacent` 或 `Excluded`，不要靠摘要强行保留。

---

## 2. 与后续编码的衔接

这不是正式 `systems_master` 或 `core_evidence`。

它的作用只是做首轮全文 sanity check，并为后续编码先留下三个最关键的过渡字段：

- `provisional_agent_repr_level`
- `provisional_behavioral_scale`
- `provisional_tier_decision`

这样确认通过的条目可以更顺滑地进入 `system / environment configuration` 级编码。

---

## 3. 文件位置

可手填 CSV：

- `assets/survey_paper/phase1/phase1_fulltext_sanity_check_batch1_2026-04-22.csv`

---

## 4. 当前本地初判状态

截至本轮检查：

- 本地已找到 PDF：`3 / 8`
- 已完成的是：`local abstract-level prefill + partial full-text pass for HC08 / HC15`
- `HC09` 的 MDPI PDF 远端仍返回 `Access Denied`，暂时未能自动落库

当前最保守的本地判断是：

- provisional `core`: `7`
- provisional `undecided`: `0`
- provisional `adjacent`: `1`

其中：

- 更接近 `core` 的是：`HC08 / HC09 / HC10 / HC12 / HC13 / HC14 / HC15`
- 仍需重点确认 agent 是否真的拿到空间输入的是：`HC10`
- 当前最不该强推回 `core` 的是：`HC11`

---

## 5. 建议使用规则

- `multi_agent_confirmed`：填 `yes / no / unclear`
- `agent_accessible_space_confirmed`：填 `yes / no / unclear`
- `social_behavior_confirmed`：填 `yes / no / unclear`
- `provisional_tier_decision`：填 `core / adjacent / excluded / undecided`
- `provisional_agent_repr_level`：按 `L0-L5`
- `provisional_behavioral_scale`：填 `local_action / interaction / emergent_social_structure / mixed / unknown`

---

## 6. 本批优先顺序

1. `Lyfe Agents`
2. `Spontaneous Emergence...`
3. `Real world community oriented...`
4. `SimWorld`
5. `CitySim`
6. `fire evacuation`
7. `crowd evacuation`
8. `VR role-play`

这批处理完之后，应该就能判断当前 `Core` 是否足够稳定地扩到 `15+` 的 confirmed 工作集。
