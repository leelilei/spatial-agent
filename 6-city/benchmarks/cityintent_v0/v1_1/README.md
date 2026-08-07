# CityIntent v1.1 workspace

This directory contains the in-progress multi-world benchmark release. It is
not a public benchmark until every gate in `release_spec.json` passes.

Generated candidate layout:

```text
worlds/public/
worlds/private/
scenarios/examples/
scenarios/development/
scenarios/public_test/
scenarios/private_test/
manifests/
rejection_logs/
submission/
```

Regenerate the deterministic candidate data and run structural validation:

```bash
python v1_1/generate_worlds.py
python v1_1/generate_scenarios.py
python tools/validate_cityintent_v0.py --benchmark-config v1_1/benchmark_config.json
```

The organizer commands above use local, git-ignored private specifications.
Inside a public package, regenerate only public assets with:

```bash
python generate_worlds.py --public-only
python generate_scenarios.py --public-only
```

The scenario manifest intentionally reports `accepted_count: 0` until the
oracle and negative-control acceptance gates have run. A structurally valid
candidate is not yet an accepted benchmark item.

The existing `1.0-rc1` package remains immutable evidence for the diagnostic
study while v1.1 is built alongside it.
