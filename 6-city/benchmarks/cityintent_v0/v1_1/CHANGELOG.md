# Changelog

## 1.1.0-candidate — 2026-08-01

- Defined a machine-readable release specification and benchmark card.
- Added three public and two organizer-only topology-distinct city worlds.
- Added a deterministic 144-item candidate generator with fixed splits,
  provenance, hashes, and an explicit zero-accepted initial state.
- Added structural, leakage, ceiling/floor, and provisional discrimination
  audits.
- Added a strict JSONL submission contract and deterministic replay scorer.
- Ran 576 non-API baseline episodes; the acceptance audit found 87 ceiling
  candidates, 7 floor candidates, and 101 with insufficient provisional
  headroom. These findings block release rather than being hidden.
