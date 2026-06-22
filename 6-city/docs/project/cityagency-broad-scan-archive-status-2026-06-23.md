# CityAgency Broad Scan Archive Status

Date: 2026-06-23

Source note:

- `cityagency-related-work-broad-scan-2026-06-22.md`

## Newly Archived On 2026-06-23

| Cluster | PDF | Fulltext |
|---|---|---|
| Mobility realism | `assets/papers/pdf/05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.pdf` | `assets/papers/fulltext/05_mobility_realism/01_MobiSim_Bench_Zhang2026_OpenReview.fulltext.md` |
| Mobility realism | `assets/papers/pdf/05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.pdf` | `assets/papers/fulltext/05_mobility_realism/02_When_Plausible_Is_Not_Realistic_Santos2026.fulltext.md` |
| Agent execution benchmarks | `assets/papers/pdf/06_agent_execution_benchmarks/01_ChinaTravel_Shao2024.pdf` | `assets/papers/fulltext/06_agent_execution_benchmarks/01_ChinaTravel_Shao2024.fulltext.md` |
| Agent execution benchmarks | `assets/papers/pdf/06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.pdf` | `assets/papers/fulltext/06_agent_execution_benchmarks/02_FeasiGen_Do_Agents_Know_What_They_Cant_Do_2026.fulltext.md` |
| Agent execution benchmarks | `assets/papers/pdf/06_agent_execution_benchmarks/03_tau_bench_Yao2024.pdf` | `assets/papers/fulltext/06_agent_execution_benchmarks/03_tau_bench_Yao2024.fulltext.md` |
| Agent execution benchmarks | `assets/papers/pdf/06_agent_execution_benchmarks/04_AppWorld_Trivedi2024.pdf` | `assets/papers/fulltext/06_agent_execution_benchmarks/04_AppWorld_Trivedi2024.fulltext.md` |
| Agent execution benchmarks | `assets/papers/pdf/06_agent_execution_benchmarks/05_WebArena_Zhou2023.pdf` | `assets/papers/fulltext/06_agent_execution_benchmarks/05_WebArena_Zhou2023.fulltext.md` |
| Agent execution benchmarks | `assets/papers/pdf/06_agent_execution_benchmarks/06_TheAgentCompany_Xu2024.pdf` | `assets/papers/fulltext/06_agent_execution_benchmarks/06_TheAgentCompany_Xu2024.fulltext.md` |
| Social benchmark foundations | `assets/papers/pdf/04_social_benchmark_foundations/03_AgentSense_2024.pdf` | `assets/papers/fulltext/04_social_benchmark_foundations/03_AgentSense_2024.fulltext.md` |
| Social benchmark foundations | `assets/papers/pdf/04_social_benchmark_foundations/04_Lifelong_SOTOPIA_2025.pdf` | `assets/papers/fulltext/04_social_benchmark_foundations/04_Lifelong_SOTOPIA_2025.fulltext.md` |
| Social benchmark foundations | `assets/papers/pdf/04_social_benchmark_foundations/05_Misleading_Success_2024.pdf` | `assets/papers/fulltext/04_social_benchmark_foundations/05_Misleading_Success_2024.fulltext.md` |
| Social benchmark foundations | `assets/papers/pdf/04_social_benchmark_foundations/06_Can_LLM_Agents_Simulate_Multi_Turn_Human_Behavior_2025.pdf` | `assets/papers/fulltext/04_social_benchmark_foundations/06_Can_LLM_Agents_Simulate_Multi_Turn_Human_Behavior_2025.fulltext.md` |

## Already Archived Before This Pass

The broad scan also cites these existing archived papers:

- `assets/papers/pdf/01_urban_benchmarks/01_CityBench_Feng2024.pdf`
- `assets/papers/pdf/01_urban_benchmarks/04_USTBench_Liu2025.pdf`
- `assets/papers/pdf/01_urban_benchmarks/08_CityEQA_Zhang2025.pdf`
- `assets/papers/pdf/01_urban_benchmarks/09_OpenCity_Ma2024.pdf`
- `assets/papers/pdf/01_urban_benchmarks/10_MobileCity_Li2025.pdf`
- `assets/papers/pdf/02_citysim_agents/01_CitySim_Wang2025.pdf`
- `assets/papers/pdf/02_citysim_agents/02_GATSim_Liu2025.pdf`
- `assets/papers/pdf/02_citysim_agents/03_AgentSociety_Gao2025.pdf`
- `assets/papers/pdf/03_embodied_city/01_EmbodiedCity_Zhou2024.pdf`
- `assets/papers/pdf/04_social_benchmark_foundations/02_SOTOPIA_Zhou2024_ICLR.pdf`

## Verification

- All newly downloaded PDFs were checked for the `%PDF` signature.
- Fulltext extraction was run with the bundled Codex Python runtime:

```bash
C:/Users/lee/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe \
  0-Tools/research-standard/convert_pdfs_to_fulltext.py 6-city
```

- The converter refreshed:
  - `assets/papers/metadata/fulltext_manifest.json`
  - `assets/papers/metadata/fulltext_summary.md`

