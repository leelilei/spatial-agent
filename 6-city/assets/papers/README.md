# Papers

Curated reference archive for the city-agent benchmark project.

## Layout

- `metadata/`: generated indexes, manifests, source maps, and conversion summaries.
- `pdf/01_urban_benchmarks/`: urban benchmark and city-task benchmark papers.
- `pdf/02_citysim_agents/`: CitySim-like agent simulation and generative-agent papers.
- `pdf/03_embodied_city/`: embodied city, city navigation, and urban multimodal papers.
- `pdf/04_social_benchmark_foundations/`: benchmark foundations imported from social-agent research.
- `fulltext/`: Markdown full text extracted from archived PDFs.
- `notes/`: human-written project notes and citation decisions.

## Rule

Keep source PDFs, indexes, extracted fulltext, and paper notes here. Put
experiments, code, and benchmark seeds in top-level `experiments/`, `sim/`, and
`benchmarks/`.

Convert archived PDFs into Markdown fulltext with:

```bash
python D:/0-Research/0-Tools/research-standard/convert_pdfs_to_fulltext.py D:/0-Research/6-city
```
