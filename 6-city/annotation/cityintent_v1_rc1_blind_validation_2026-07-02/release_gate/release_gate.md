# CityIntent v1 Release Gate

Status: `pending_human_audit`

Benchmark: `1.0-rc1` / `release_candidate_pending_human_audit`

## Blockers

- two-person human audit incomplete: {'annotator_a': 16, 'annotator_b': 16}

## Human Audit

Pending rows: `{"annotator_a": 16, "annotator_b": 16}`

Material findings: 0

## Runtime Checks

- `0`: `C:\Users\lee\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe -m unittest discover -s D:\0-Research\6-city\benchmarks\cityintent_v0\tests -p test_*.py`
- `0`: `C:\Users\lee\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe D:\0-Research\6-city\benchmarks\cityintent_v0\tools\validate_cityintent_v0.py`
- `0`: `C:\Users\lee\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe D:\0-Research\6-city\benchmarks\cityintent_v0\tools\validate_external_adapters.py --framework all`
