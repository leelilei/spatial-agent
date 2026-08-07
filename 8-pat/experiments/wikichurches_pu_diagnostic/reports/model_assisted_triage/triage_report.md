# Frozen-CLIP 框外候选诊断

- 模型：`ViT-B/32` / `openai`
- 设备：`mps`
- 图像：50
- 候选记录：708
- 框外候选分数不低于同图同标签官方框中位数：535/708 (75.6%)
- 同时满足上述条件且该标签在 69 个审计标签中 rank ≤ 5：185/708 (26.1%)

该比例只用于安排人工复核顺序，不能解释为漏标率或模型精度。

## 最高优先级候选

| audit_id | 标签 | pos margin | global rank | specificity |
|---|---|---:|---:|---:|
| WC-AUD-022 | Onion Dome | +0.005 | 1 | +0.025 |
| WC-AUD-030 | Cranked Cornice | +0.046 | 1 | +0.022 |
| WC-AUD-024 | Cranked Cornice | +0.063 | 1 | +0.015 |
| WC-AUD-020 | Pinnacle | +0.018 | 1 | +0.015 |
| WC-AUD-009 | Pinnacle | +0.048 | 1 | +0.013 |
| WC-AUD-022 | Onion Dome | +0.013 | 1 | +0.013 |
| WC-AUD-031 | Column | +0.003 | 1 | +0.013 |
| WC-AUD-016 | Buttress | +0.035 | 1 | +0.012 |
| WC-AUD-034 | Pinnacle | +0.024 | 1 | +0.011 |
| WC-AUD-006 | Cranked Cornice | +0.002 | 1 | +0.011 |
| WC-AUD-039 | Buttress Arch | +0.008 | 1 | +0.010 |
| WC-AUD-024 | Cranked Cornice | +0.060 | 1 | +0.009 |
| WC-AUD-039 | Buttress Arch | +0.007 | 1 | +0.009 |
| WC-AUD-030 | Cranked Cornice | +0.045 | 1 | +0.009 |
| WC-AUD-024 | Cranked Cornice | +0.067 | 1 | +0.008 |
| WC-AUD-030 | Cranked Cornice | +0.045 | 1 | +0.008 |
| WC-AUD-032 | Blind Arcade | +0.024 | 1 | +0.008 |
| WC-AUD-020 | Pinnacle | +0.020 | 1 | +0.008 |
| WC-AUD-014 | Quatrefoil | +0.094 | 1 | +0.007 |
| WC-AUD-015 | Pilaster | +0.068 | 1 | +0.007 |
| WC-AUD-028 | Conical Roof | +0.050 | 1 | +0.007 |
| WC-AUD-025 | Wimperg | +0.010 | 1 | +0.007 |
| WC-AUD-039 | Buttress | +0.015 | 1 | +0.006 |
| WC-AUD-033 | Buttress | +0.012 | 1 | +0.006 |
| WC-AUD-014 | Pinnacle | +0.058 | 1 | +0.006 |
| WC-AUD-040 | Buttress | +0.055 | 1 | +0.006 |
| WC-AUD-016 | Buttress | +0.027 | 1 | +0.006 |
| WC-AUD-013 | Buttress | +0.047 | 1 | +0.006 |
| WC-AUD-009 | Buttress | +0.032 | 1 | +0.005 |
| WC-AUD-041 | Buttress | +0.022 | 1 | +0.005 |
