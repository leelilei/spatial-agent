# Data Index — experiment → data location

> Maps each experiment ID (the `RESULTS.md` ledger) to its run directory under `sim/runs/`.
> Goal + headline + config summary live in `RESULTS.md`; rationale in `decisions.md`; this file
> is the **traceability link** (which data backs which claim). Each run dir contains:
> `run_config.json` (full CLI args — added 2026-06-22; older dirs: config is in the dir name +
> the ledger), `aggregate.json` (per-condition means + per-run rows), `runs.json`,
> and per-run `round_*.json` / `interview_currency.json` / `memory_snapshots.json` / `sim_summary.json`.

| ID | what | data dir(s) under `sim/runs/` |
|---|---|---|
| M0 | capability ladder | `m0_strong/seed_4{1,2,3}`, `m0_strong55/seed_4{1,2,3}` (+ mini reused) |
| M1 | capability×connectivity grid | `m1/` |
| M2 | memory axis raw/ga/smga/smga3g | `m2_memory/{raw,ga,smga,smga3g}` |
| M3 | verify smga3g flip | `m3_verify/{ga_m2,ga_m3,smga3g_m2,smga3g_m3}` |
| M4 | authoritative re-broadcast + dissociation | `m4_rebroadcast/{baseline,source,broadcast}` |
| M5 | long-horizon decay trajectory (Fig 2) | `fig2_r30/{baseline,source,broadcast}`, `fig2_trajectory/` |
| G1 | dissociation on book_club/carpool | `g1_scenarios/{book_club,carpool}_{baseline,source,broadcast}` |
| G2 | persona-depth (thick) robustness | `g2_persona/{baseline,source,broadcast}` |
| P1-rec | recency vs entrenchment | `p1rec/{r1_broadcast,r5_broadcast}` |
| P3 | power (capability/connectivity, CIs) | `p3_power/{m0_mini,m0_gpt54,m0_gpt55,m1_mini_m1,m1_mini_m3}` |
| P3b | connectivity on gpt-5.4 | `p3b_conn54/{m1,m3}` |
| C1 | CURE de-risk PROV vs GA | `prov_derisk/{ga,prov}` |
| C2 | CURE validation (power + source + r30) | `prov_batch/{ga_r5,prov_r5,ga_source,prov_source,prov_r30}` |
| C3 | FAIR/generalized PROV (n=8) | `prov_fair/prov` (vs `prov_batch/ga_r5`) |
| C5 | architecture table (repair_drive) | `table_repair/{raw,smga3g,amem,memorybank,mem0}` (+ `prov_batch/ga_r5`, `prov_fair/prov`) |
| C5 | PROV horizon climb r5/r10/r20 | `prov_fair/prov`, `prov_horizon/{prov_r10_final,prov_r20_final}` |
| C5-stress | lossy channel (drop) | `prov_lossy/{loss03,loss06,loss09}` |
| C5-stress | lossy channel (garble) | `prov_garble/{garble03,garble06,garble09}` |
| C6 | PROV-v2 (corroboration + decay), neg result | `provv2/{clean_r10,clean_r20,garble06_r10}` |
| C7 | sparse comms (prov_mention sweep) | `sparse/{v1_m01_r10,v2_m03_r10,v2_m01_r10}` |
| C8 | architecture table × 3 scenarios | `table_3scenario/{book_club,carpool}_{ga,prov,smga3g,amem}` (+ C5 repair_drive) |
| C9 | numeric fact-type (dues) | `dues/{ga,prov,smga3g,amem}` |
| C10 | topology robustness (ring/smallworld) | `topology/{ring,smallworld}_{ga,prov}` |
| C11 | PROV-text deterministic text relay mechanism probe | `provtext_context_relay_probe_v2` |
| C12 | PROV-text-free real LLM dialogue + partial GA/PROV comparator | `provtext_llm_only_r10_n5`, `provtext_llm_long_r10_n5` |
| C13 | PROV-text-norm strong attribution dialogue | `provtext_norm_r10_n3` |
| C14 | capability check on cure (DeepSeek-V4-Flash), n=8 | pool: `cap_deepseek_prov_vs_ga_pilot` (41-43) + `cap_deepseek_prov_vs_ga_n8ext` (GA 44-48, PROV 44) + `cap_deepseek_prov_n8fill` (PROV 45-48) + `cap_deepseek_prov_seed44` (PROV 44 interview) |
| C15 | APM architecture pilot (DeepSeek) | `cap_apm_clean_r5_pilot` (K=2, deadlock) + `cap_apm_k1_r5_pilot` (K=1, ≈PROV) |
| C16 | adversarial-liar robustness (mini/FHL) | `cap_c16_mini_adversary` (PROV vs APM, adversary a13@r2, n=3) + `cap_c16_adversary_pilot` (ds PROV seed41 cross-check) |
| C17 | APM realistic-friction equilibrium (saturation check), n=8 | `cap_c17_mini_sparse_r10` (41-43) + `cap_c17_mini_sparse_r10_ext` (44-48) — apm vs ga, mention 0.1, r10 |

## Reproducibility notes
- **`run_config.json`** (per out-dir) records every CLI arg + timestamp → a run is now
  self-describing. Re-run: `python sim/run_society_sweep.py` with those args.
- LLM societies at temperature 0 are still chaotic (a single divergent token cascades), so
  per-seed values vary; we report n>=5 with 95% CIs and treat per-seed spread as the unit.
- Provider transport + diagnostic config: `../../3-SMGA/benchmarks/diagnostic_v0/configs/`.
