# Phase 1 Core Acquisition Routes
## 2026-04-27 closure addendum

This route sheet is now historical rather than active for `HC13` and `HC14`.

- `HC13` was archived as `assets/survey_paper/pdfs/phase1_core/14_HC13_Fire_Evacuation_CA.pdf`
- `HC14` was archived as `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.pdf`
- local `pdf2text` extraction and full-text adjudication are complete for both rows
- neither paper should be treated as a live acquisition blocker or Round 3 dependency

Use these files for the live workflow instead:

- `assets/survey_paper/phase1/phase1_hc13_hc14_fulltext_adjudication_2026-04-27.md`
- `assets/survey_paper/phase1/phase1_core_first_pass_coding_2026-04-23.csv`
- `assets/survey_paper/phase1/phase1_core_evidence_map_matrix_2026-04-27.md`


日期：2026-04-22  
用途：为当前 `Core` 工作集建立一份合法、可执行的落库路线表，区分“可以自动下载”“需要浏览器人工下载”“需要机构访问/作者提供”的不同情况。

---

## 1. 当前结论

当前不是“没有入口”，而是不同条目卡在不同层级：

- `HC08 / HC12 / HC15`：已自动落库
- `HC09`：开放获取，但命令行下载被站点策略拦截
- `HC10`：ScienceDirect 标注 `Complimentary access`，更像浏览器/反爬问题，不像真正 paywall
- `HC13 / HC14`：当前只确认到期刊落地页与摘要，命令行没有拿到 PDF，更像需要机构访问或作者版本

---

## 2. 分条目路线

### HC09. Spontaneous Emergence of Agent Individuality Through Social Interactions in Large Language Model-Based Communities

- 当前状态：`未自动落库`
- 访问性质：`Open Access`
- 已确认入口：
  - MDPI 文章页：https://www.mdpi.com/1099-4300/26/12/1092
  - PubMed 记录（含 `PMCID: PMC11675631`）：https://pubmed.ncbi.nlm.nih.gov/39766721/
  - ResearchGate 显示 `Article PDF Available`：https://www.researchgate.net/publication/387033243_Spontaneous_Emergence_of_Agent_Individuality_Through_Social_Interactions_in_Large_Language_Model-Based_Communities
- 阻塞类型：
  - 命令行直连 MDPI / PMC PDF 时返回 HTML 或 `Access Denied`
- 建议动作：
  1. 用正常浏览器打开 MDPI 或 ResearchGate 页面，手动点击 `Download PDF`
  2. 若浏览器也失败，至少先保存 MDPI HTML 全文页面作为临时本地全文副本

### HC10. Real world community oriented high-definition social simulation: Combining reinforcement learning and large language models

- 当前状态：`未自动落库`
- 访问性质：`ScienceDirect complimentary access`
- 已确认入口：
  - ScienceDirect：https://www.sciencedirect.com/science/article/pii/S0264275125007693
  - DOI：https://doi.org/10.1016/j.cities.2025.106468
  - ResearchGate 条目：https://www.researchgate.net/publication/399296750_Real_world_community_oriented_high-definition_social_simulation_Combining_reinforcement_learning_and_large_language_models
- 阻塞类型：
  - 命令行访问 `pdfft` 只拿到反爬 HTML，不是真 PDF
- 建议动作：
  1. 在正常浏览器中打开 ScienceDirect 页面，优先尝试 `View PDF`
  2. 若浏览器可见全文但无法直接下载，另存为 PDF
  3. 若浏览器仍失败，再转作者请求或机构访问

### HC13. Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment

- Resolution on `2026-04-27`: local PDF archived and full-text adjudication completed; no further acquisition action needed.

- 当前状态：`已于 2026-04-27 归档并完成全文抽取`
- 访问性质：`historical pre-resolution state only; local PDF archived on 2026-04-27`
- 已确认入口：
  - ScienceDirect：https://www.sciencedirect.com/science/article/pii/S0925753525001602
  - DOI：https://doi.org/10.1016/j.ssci.2025.106935
  - ResearchGate 条目：https://www.researchgate.net/publication/397145175_Large-language-model-driven_agents_for_fire_evacuation_simulation_in_a_cellular_automata_environment
- 阻塞类型：
  - 命令行 `pdfft` 返回 HTML 占位页
  - 暂未发现公开作者 PDF
- 建议动作：
  1. 先用浏览器测试 ScienceDirect 是否存在可见 `View PDF`
  2. 若没有，则走机构访问
  3. 若你没有机构权限，走 `ResearchGate Request full-text` 或直接发邮件给作者

### HC14. When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios

- Resolution on `2026-04-27`: local PDF archived and full-text adjudication completed; no further acquisition action needed.

- 当前状态：`已于 2026-04-27 归档并完成全文抽取`
- 访问性质：`historical pre-resolution state only; local PDF archived on 2026-04-27`
- 已确认入口：
  - ScienceDirect：https://www.sciencedirect.com/science/article/pii/S0951832025012554
  - DOI：https://doi.org/10.1016/j.ress.2025.112056
  - ResearchGate 条目：https://www.researchgate.net/publication/398196301_When_Agents_Learn_to_Think_Large_Language_Model-Enhanced_Agent-Based_Modeling_for_Crowd_Evacuation_in_Disaster_Scenarios
- 阻塞类型：
  - 命令行 `pdfft` 返回 HTML 占位页
  - 公开镜像只看到摘要，未看到开放 PDF
- 建议动作：
  1. 先用浏览器测试 ScienceDirect 页面是否能直接 `View PDF`
  2. 若浏览器无权访问，则转机构权限或作者请求

---

## 3. 推荐落库顺序

按成功率与价值排序，建议这样推进：

1. `HC09`
   原因：开放获取，最有可能通过浏览器手动下载解决。
2. `HC10`
   原因：`Complimentary access`，更像技术性拦截，不像版权阻塞。
3. `HC13`
   原因：已确认期刊页和摘要，但大概率需要机构访问或作者提供。
4. `HC14`
   原因：与 `HC13` 类似，但当前公开全文线索更弱。

---

## 4. 现实判断

如果目标是“所有 `Core` 都要有本地全文”，当前最稳的执行路径不是继续用脚本盲抓，而是：

1. 先自动收完 `arXiv / PMC / 明确 OA` 来源
2. 对 `ScienceDirect complimentary access` 用真实浏览器手动下载
3. 对仍然拿不到的 Elsevier/IEEE 正式版，用机构权限补
4. 最后对仍缺的条目，用作者公开版或 `Request full-text`

也就是说：

- `HC09 / HC10` 仍有较大概率在不依赖机构权限的情况下补齐
- `HC13 / HC14` 很可能最终需要机构权限或作者提供版本
