# Telephone — Reference Library

> Working title: *Speech is not belief: Fidelity decay in LLM agent societies*.
> Compiled from the project literature review (`../telephone-research.md`) + canonical works.
> **⚠ Bibliographic details (exact venue/year/pages) must be verified against the sources
> before camera-ready — assembled here without live web access.** Convert to `.bib` at draft
> time. ★ = MUST-CITE-AND-BEAT (close neighbor we position against).

---

## 1. Generative agents / multi-agent LLM systems (our setting)

- **Park, J. S., O'Brien, J. C., Cai, C. J., Ringel Morris, M., Liang, P., & Bernstein, M. S.
  (2023). Generative Agents: Interactive Simulacra of Human Behavior. UIST 2023.**
  → The canonical agent-society architecture + the famous info-diffusion success demo
  (Isabella's party spreads). *We measure FIDELITY of what spreads, the axis they skip.*
- ★ **Park, J. S., Zou, C. Q., Kamphorst, J., Egan, N., Shaw, A., Hill, B. M., Cai, C., Morris,
  M. R., Liang, P., Willer, R., & Bernstein, M. S. (2024). Generative Agent Simulations of
  1,000 People. arXiv:2411.10109.** (v2, 2026, retitled "LLM Agents Grounded in Self-Reports
  Enable General-Purpose Simulation of Individuals".) PDF: `assets/papers/2411.10109_*.pdf`.
  → 1,052 Americans; 2-hour interviews + GSS/Big-Five; held-out GSS accuracy **83% (interview)
  / 82% (survey) / 86% (combined)** of 2-week test-retest consistency vs **74% demographics-only**.
  *INDIVIDUAL-level predictive fidelity — agents do NOT interact or propagate. This is the
  GA authors' own follow-up and a KEY framing neighbor: it shows a single agent can be made
  faithful to a real PERSON; we show that a SOCIETY of agents is NOT faithful in propagating a
  fact — **individual fidelity ≠ collective fidelity**. Also flags the "thick (self-report-
  grounded) persona" axis our thin one-line personas do not test (→ a robustness check / limitation).*
- **Vezhnevets, A. S., Agapiou, J. P., et al. (2023). Generative agent-based modeling with
  actions grounded in physical/social/digital space using Concordia. arXiv.**
  → Configurable social-simulation infrastructure. *We add a fidelity axis to this lineage.*
- **Yan, B., Zhang, X., et al. (2025). Beyond Self-Talk: A communication-centric survey of
  LLM-based multi-agent systems. arXiv.** → Frames LLM-MAS as communication-protocol-bound.
  *We study communication QUALITY/fidelity, not another agent framework.*
- ★ **Cemri, M., Pan, M. Z., et al. (2025). Why Do Multi-Agent LLM Systems Fail? (MAST).
  arXiv.** → Trace-level failure taxonomy (1600+ traces). *Method model for our corruption
  taxonomy; but their endpoint is general MAS failure, not truth-fidelity dynamics.*
- ★ **Kim, Y., Gu, K., et al. (2025). Towards a Science of Scaling Agent Systems. arXiv.**
  → 180 configs; error amplification 17.2× (decentralized) vs 4.4×; ~45% single-agent
  capability crossover. *Closest "laws/phase" neighbor; we recast the endpoint from task
  PERFORMANCE to truth↔corruption dynamics.*

## 2. Transmission chains / iterated learning / cultural evolution (our paradigm)

- **Bartlett, F. C. (1932). Remembering: A Study in Experimental and Social Psychology.
  Cambridge University Press.** → Serial reproduction ("telephone"); memory is reconstructive,
  schema-driven. *Our corruption taxonomy = the machine version of Bartlett's distortions.*
- ★ **Kirby, S., Cornish, H., & Smith, K. (2008). Cumulative cultural evolution in the
  laboratory. PNAS 105(31), 10681–10686.** → Iterated learning contracts signals toward a
  structured ATTRACTOR. *Grounds our "corruption is convergence to an attractor, not noise."*
- **Mesoudi, A., & Whiten, A. (2008). The multiple roles of cultural transmission experiments.
  Phil. Trans. R. Soc. B 363(1509), 3489–3501.** → Legitimizes transmission-chain methodology.
  *Our M0–M4 = transmission-chain method extended to an LLM society.*
- **Ren, Y., Guo, S., et al. (2020). Compositional languages emerge in a neural iterated
  learning model. arXiv.** → Bridges iterated learning to neural agents. *Decay is structured.*

## 3. Model collapse / self-consuming generative models (our framing + C4 theory)

- **Shumailov, I., Shumaylov, Z., Zhao, Y., et al. (2024). AI models collapse when trained on
  recursively generated data. Nature 631, 755–759.** → Training-time recursive degradation
  (early/late collapse; tails vanish). *We are the inference-time, COMMUNICATIVE analog — the
  hook, stated as an analogy not an established term.*
- **Alemohammad, S., Casco-Rodriguez, J., et al. (2023). Self-Consuming Generative Models Go
  MAD. arXiv.** → Quality vs diversity loss in autophagous loops. *Motivates our version-
  DIVERSITY axis (a low-diversity, high-consensus error is its own failure).*
- **Seddik, M. E. A., Chen, S.-W., et al. (2024). How bad is training on synthetic data? A
  statistical analysis of language model collapse. arXiv.** → Threshold/bound formalism.
- ★ **Yi, B., Liu, Q., et al. (2025). Escaping model collapse via synthetic data verification.
  arXiv.** → An external verifier halts collapse but pulls the system to the verifier's
  "knowledge center". *Training-time isomorph of our authoritative re-broadcast (M4); helps
  frame why an external truth-source could (in principle) help — though in OUR society it fails.*

## 4. Misinformation / rumor / collective belief dynamics (our empirical cousins)

- **Del Vicario, M., Bessi, A., et al. (2016). The spreading of misinformation online. PNAS
  113(3), 554–559.** → Echo chambers, homophily, cascade dynamics. *Language for version-
  splitting / local consensus.*
- **Vosoughi, S., Roy, D., & Aral, S. (2018). The spread of true and false news online.
  Science 359(6380), 1146–1151.** → Falsehood spreads farther/faster/deeper (reach ≠ truth).
  *The canonical reach≠truth result we rebuild and EXPLAIN inside an agent society.*
- **Hu, T., Liakopoulos, D., et al. (2025). Simulating rumor spreading in social networks
  using LLM agents. arXiv.** → LLM-agent rumor sim; reach 0%–83% by structure. *Shows the
  platform is feasible; we upgrade the outcome from reach to held-belief fidelity.*
- ★ **Becker, J., Wahle, J. P., et al. (2026). Misinformation propagation in benign multi-agent
  systems (MINT). arXiv.** → Misinformation persists in benign MAD; group composition/protocol
  matter. *Closest contemporaneous baseline; they stop at task-correctness in DEBATE — we do
  society-scale decay, the speech–belief dissociation, and the entrenchment mechanism.*
- ★ **Jamshidi, S., Moradi Dakhel, A., et al. (2026). Hallucination Cascade: error propagation
  in multi-agent LLM systems. arXiv.** → In 3-agent chains hallucination ↓ but factual
  accuracy ALSO ↓. *Supports defining fidelity independently of hallucination; we add hops,
  version-share, the dissociation, and the mechanism.*
- ★ **Ashery, A. F., Aiello, L. M., & Baronchelli, A. (2025). Emergent social conventions and
  collective bias in LLM populations. Science Advances 11, eadu9368.** → LLM populations form
  collective conventions/bias; committed minorities can tip them. *Precursor to our
  truth↔corruption attractor + path-dependence; we add a ground-truthed correction target.*

## 5. Memory / retrieval / correction (the levers we test — M2/M3/M4)

- **Lewis, P., Perez, E., et al. (2020). Retrieval-augmented generation for knowledge-intensive
  NLP. NeurIPS 2020.** → External evidence improves factuality / supports updates. *Template
  for a provenance-aware authoritative source.*
- **Shinn, N., Cassano, F., et al. (2023). Reflexion: Language agents with verbal RL. arXiv.**
  → Reflection-as-memory improves decisions. *GA-reflection (our corrupting baseline) reframed.*
- **Xu, W., Liang, Z., et al. (2025). A-MEM: Agentic memory for LLM agents. arXiv.** → Self-
  organizing, evolving notes. *Closer to "version-updating" memory than static retrieval.*
- ★ **Xiong, Z., Lin, Y., et al. (2025). How memory management impacts LLM agents: experience-
  following behavior. arXiv.** → Memory can PROPAGATE old errors (addition/deletion effects).
  *Direct support that memory is not a pure fix — consistent with our M2/M3 null.*
- **Banerjee, P., Moshtaghi, M., et al. (2026). APEX-MEM: agentic semi-structured memory with
  temporal reasoning. arXiv.** → Append-only temporal store + retrieval-time conflict
  resolution; LOCOMO 88.9%. *The "currency-resolving memory" template (our smga3g cousin).*
- **MemoryAgentBench (2025) / Mem2ActBench (2025).** → Memory can RETRIEVE but not ACT on info.
  *Our held-belief metric is the social analog of "memory→action".*

## 6. Reflexive / critical evaluation (our rigor + caveats)

- ★ **Sense and Sensitivity: Evaluating the simulation of social dynamics via LLMs (2025).**
  → LLM social sims are hypersensitive to prompt wording; without a reference model many macro
  results are fragile artifacts. *Justifies our reproducibility/variance discipline (multi-seed,
  CIs, the verify-before-build catches of three n=3 over-claims) and the judge-validated metric.*
- **Are LLM Agents Behaviorally Coherent? Latent Profiles for Social Simulation (2025).**
  → Stated internal state ≠ displayed behavior across settings. *Cousin of our speech≠belief
  dissociation at the population level.*
- **Too Human to Model (2025).** → Over-rich LLM agents may obscure mechanism. *Why we keep the
  instrument controlled and the metric simple/validated.*

---

## How these map to our contributions

- **Phenomenon (fidelity decay):** §1 (reach demos) + §4 (reach≠truth) → we add fidelity.
- **Failed levers (capability/connectivity/memory/authority):** §1 (Kim scaling), §5 (memory),
  §3 (Yi verifier) → we show none fix it in a society.
- **Mechanism (entrenchment / path-dependence / first-mover):** §2 (iterated-learning attractor)
  + §4 (Ashery tipping; Vosoughi reach≠truth) → we give the timing+breadth law.
- **Sharpest claim (speech ≠ belief):** §6 (behavioral coherence) + §5 (retrieve≠act) → we
  demonstrate it cleanly with a say-ratio vs held-belief contrast, judge-validated.
- **Method/rigor:** §6 (Sense and Sensitivity) + §1 (MAST trace-level) → multi-seed CIs,
  provenance, semantic-judge validation.
