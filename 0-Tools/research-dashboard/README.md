# Research Dashboard

Local HTML dashboard for research todo files under `/Users/mac/Documents/6-Research`.

The dashboard reads:

```text
/Users/mac/Documents/1-ProjectRes/Personal Todo/sources.json
```

Each enabled source points to a markdown todo file. The server reads the config
and markdown files on every API request, so edits are visible after refresh.

Roadmap visualization can be upgraded with an optional sibling file:

```text
docs/guides/roadmap.yaml
```

When present, `roadmap.yaml` controls visual roadmap structure. Checkbox counts
and next actions still come from `todolist.md`.

## Run

```bash
cd /Users/mac/Documents/6-Research/0-Tools/research-dashboard
python3 server.py --port 8765 --open
```

Open:

```text
http://127.0.0.1:8765
```

## Check Parsed State

```bash
python3 server.py --check
```

## Markdown Support

The parser recognizes:

- `更新日期`
- `当前主线`
- `## ... Phase N ...` headings
- `## 执行优先级`
- `### Priority N` headings
- `- [ ]` and `- [x]` checkbox tasks

Tasks under `## 暂不做` are ignored for active progress. Missing todo files are
shown as unreadable sources and are not created automatically.

## Structured Roadmap YAML

The YAML schema is intentionally small:

```yaml
version: 1
project: 3-SMGA
currentPhase: 2
tracks:
  - id: infrastructure
    name: Infrastructure
    accent: "#ff9500"
    order: 2
phases:
  - number: 2
    title: Experiment 0 Infrastructure
    track: infrastructure
    status: current
    summary: Turn seed_0001 into a stable validate-load-score loop.
    outputs:
      - benchmark_loader.py
```

If a source has no `roadmap.yaml`, the dashboard falls back to phases parsed
from markdown headings.
