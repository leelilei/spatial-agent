# Research Tools

This directory contains shared helper tools for projects under
`/Users/mac/Documents/6-Research`.

## Tools

- `research-dashboard/`: recommended local HTML dashboard for research project
  progress and markdown todo files
- `research-todo/`: deprecated native macOS menu bar app kept for reference
- `research-standard/`: scaffold, compliance checks, migration helpers, and
  standard literature-asset and LLM API tooling

## Standard Literature Workflow

After archiving PDFs under a project such as `6-city/assets/papers/pdf/`, convert
them to Markdown fulltext with:

```bash
python D:/0-Research/0-Tools/research-standard/convert_pdfs_to_fulltext.py D:/0-Research/6-city
```

The converter writes:

- `assets/papers/fulltext/**/*.fulltext.md`
- `assets/papers/fulltext/**/*.meta.json`
- `assets/papers/metadata/fulltext_manifest.json`
- `assets/papers/metadata/fulltext_summary.md`

## Standard LLM API Client

Projects should use the shared dependency-free client instead of copying API
transport code between projects:

```bash
python D:/0-Research/0-Tools/research-standard/llm_client.py ^
  --config D:/0-Research/0-Tools/research-standard/templates/llm_config.mock.json
```

See `research-standard/LLM-CLIENT-STANDARD.md` for config fields, key handling,
and migration notes from `3-smga` / `5-Telephone`.

## Standard Paper Search

Use the shared first-pass search protocol before locking a proposal's novelty
claim:

```bash
python D:/0-Research/0-Tools/research-standard/paper_search.py ^
  --query "LLM urban agent benchmark agency" ^
  --query "LLM urban simulation mobility realism benchmark" ^
  --max-results 8 ^
  --out D:/0-Research/6-city/docs/project/paper-search-raw-2026-06-22.md
```

See `research-standard/PAPER-SEARCH-STANDARD.md` for query design, required
outputs, relevance labels, and novelty-threat rules.
