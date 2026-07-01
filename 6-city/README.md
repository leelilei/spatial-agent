# 6-city

CityAgency / urban generative-agent benchmark research workspace.

Working paper story:

> Plausible Plans, Impossible Traces: a benchmark for measuring whether urban
> agents can turn reasonable-sounding plans into executable city traces.

## North Star

Build a small, controllable, verifiable benchmark for embodied or spatially
situated city agents: agents should maintain private intentions, respect city
constraints, recover from disruptions, and produce traces that can be evaluated
by spatial feasibility, adaptation, social context, and goal completion rather
than by demo plausibility alone.

## Current Focus

- Literature map: urban benchmark papers, CitySim-like agent simulation papers, and
  embodied-city / navigation references.
- Benchmark design: SOTOPIA-style scenario packages for city agents.
- Opportunity framing: CityAgency as a controlled microfoundational benchmark
  for urban agency, connecting individual decision failures to larger city
  simulation and mobility-realism questions.

## Key Notes

- `docs/project/citysim-agent-projects.md`: comparison table for related projects.
- `docs/plans/proposal.md`: current CityAgency proposal.
- `docs/project/cityintent_agent_eval_plan.md`: candidate agent architectures for the first CityAgency / CityIntent evaluation track.
- `benchmarks/cityintent_v0/`: runnable v0 CityIntent track with toy city, scenarios, and validator.
- `docs/project/sotopia-style-city-benchmark.md`: SOTOPIA-style benchmark design sketch.
- `docs/project/urban-benchmark-literature.md`: urban benchmark literature scan.
- `assets/papers/metadata/reference_index.md`: curated reference index and archive map.

## Project Layout

```text
.
|-- docs/
|   |-- guides/          # execution guides and active todos
|   |-- plans/           # proposal versions and staged research plans
|   `-- project/         # research notes, decisions, literature maps
|-- assets/
|   `-- papers/
|       |-- metadata/    # generated indexes, manifests, source maps
|       |-- pdf/         # archived reference PDFs
|       |-- fulltext/    # extracted Markdown full text
|       `-- notes/       # human / project reading notes
|-- benchmarks/          # benchmark definitions, scenarios, runners, and tests
|-- experiments/         # runnable experiment scripts and prototypes
|-- annotation/          # blinded audit packets, rubrics, and annotation forms
|-- results/             # archived experiment outputs and analysis artifacts
|-- sim/                 # future simulation environment prototypes
|-- city-agency-core/    # future reusable city-agent core code
`-- paper/               # future paper draft, figures, tables, bibliography
```

## Directory Roles

- `docs/project/`: living analysis and project decisions.
- `assets/papers/pdf/01_urban_benchmarks/`: city / urban benchmark papers.
- `assets/papers/pdf/02_citysim_agents/`: CitySim, generative-agent, and social simulation papers.
- `assets/papers/pdf/03_embodied_city/`: embodied city, visual navigation, and urban VLM papers.
- `assets/papers/pdf/04_social_benchmark_foundations/`: social-agent benchmark foundations such as SOTOPIA.
- `assets/papers/fulltext/`: Markdown full text extracted from archived PDFs.
- `assets/papers/notes/`: project-facing reading notes and citation decisions.
- `benchmarks/`: benchmark specs, seeds, environment schemas, and scoring code.
- `experiments/`: scripts for model runs, sweeps, ablations, and replication.
- `results/`: run outputs, tables, plots, and analysis notebooks.
