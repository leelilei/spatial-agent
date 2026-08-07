# Execution provenance and reproducibility boundary

This record accompanies the anonymous DAI 2026 artifact. It contains no API
credential, authorization header, account identifier, or response payload from
the provider.

## Model transport

- Main model string supplied to the endpoint: `gpt-5.4-mini`
- Model-family check string: `DeepSeek-V4-Flash`
- Transport: third-party OpenAI-compatible Responses API, invoked through the
  project's `curl` transport
- Access route used by the accepted runs: `https://www.fhl.mom`
- Response format: JSON requested in the prompt; transport-level JSON mode was
  disabled
- Response storage: disabled in the client configuration
- Nominal temperature in the configuration: `0`; the access configuration set
  `omit_temperature=true`, so the field was not sent when unsupported by the
  endpoint
- Default transport policy: 120-second timeout, three retries, five-second
  retry delay, and at most ten concurrent requests

The endpoint, rather than this client, resolved the public model string to a
served checkpoint. Proprietary weights, endpoint-side checkpoint revision, and
provider-side sampling implementation cannot be archived. The client did not
set an explicit context-window or output-token limit, and the endpoint did not
expose a checkpoint-specific context-window declaration in the saved run
records. No prompt was truncated by the local client.

## Access dates

- Core baseline/source/broadcast societies: 2026-06-19
- Eight-run GA and provenance architecture societies: 2026-06-21
- Fixed-stream and selector replays: 2026-07-23
- GA-generated cross-source replay: 2026-07-23

Dates above are taken from the accepted artifact files and experiment ledger.
Saved accepted outputs, rather than regeneration, are the evidential record.

## Retrieval backend

The GA implementation attempts
`minishlab/potion-retrieval-32M` through `model2vec` and falls back to a
deterministic lexical ranker if that optional dependency cannot be loaded or
encoding fails. Historical accepted run records did not persist the backend
selected on every retrieval call, so an exact fallback frequency cannot be
reconstructed after the fact. This is a reproducibility limitation, not a
zero-fallback claim. New executions should record the selected backend in their
run manifest.

## Failure policy

A transport failure is never converted to a substantive `unknown` answer.
Fixed-stream conditions use per-agent checkpoints and are accepted only when
all 25 agents complete. Interrupted or incomplete conditions resume missing
agents and are excluded from aggregation until complete.
