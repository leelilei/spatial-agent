# Provider concurrency states (FHL)

Measured with `sim/concurrency_probe.py` — raw requests (no retry masking), tiny prompt,
N simultaneous calls per concurrency level. 429 = rate-limit (shared account-level RPM
budget, ~20s recovery), not a hard per-model concurrency cap.

## State 1 (2026-06-19, before user switch)

```text
gpt-5.4-mini
 conc |   ok    | p50s | maxs | errors
    8 |  8/8    |  1.9 |  2.5 |
   16 | 16/16   |  1.8 |  3.0 |
   24 | 24/24   |  1.9 |  7.4 |
   32 |  2/32   |  1.7 |      | 30x HTTP 429
   48 | 47/48   |  2.8 |  6.1 | 1x 503   (window had reset)
   64 |  2/64   |  4.2 |      | 62x HTTP 429

gpt-5.5 (clean, after a 20s cooldown — earlier all-429 was contamination by the mini burst)
 conc |   ok    | p50s | maxs
    1 |  1/1    |  3.3
    2 |  2/2    |  2.8
    4 |  4/4    |  2.7
    8 |  8/8    |  2.7
   12 | 12/12   |  2.4
```

Read (State 1): shared account-level RPM budget. mini clean to ~24 concurrent, 429 above.
gpt-5.5 clean to ≥12 (limit higher, untested). The two models SHARE the 429 budget. Operating
point: keep total in-flight ≈16–24 across all parallel jobs; single-model run workers 16–20;
strong-model jobs workers 4–8. Transient 429s are absorbed by the LLM wrapper's retry loop.

## State 2 (2026-06-19, after user switch) — much higher / no rate limit

```text
gpt-5.4-mini
 conc |   ok    | p50s | maxs | errors
    8 |  8/8    |  2.6 |  5.1 |
   16 | 16/16   |  2.2 | 11.2 |
   24 | 24/24   |  2.1 |  4.4 |
   32 | 32/32   |  2.3 |  5.5 |   <- State 1 broke here (429)
   48 | 48/48   |  2.5 |  5.6 |
   64 | 64/64   |  3.2 |  5.4 |   <- still clean

gpt-5.5
 conc |   ok    | p50s | maxs
    4 |  4/4    |  2.6
    8 |  8/8    |  2.3
   16 | 16/16   |  2.5
   24 | 24/24   |  3.2
   32 | 32/32   |  3.3        <- clean
```

Read (State 2): the 429 rate-limiting is essentially gone. mini clean to ≥64 concurrent,
gpt-5.5 clean to ≥32 — neither ceiling reached. Operating point upgraded: single-model runs
can use workers 32–48 (mini) / 24+ (gpt-5.5); large parallel sweeps are now throughput-bound
by latency (~2–3s/call), not rate limits. Re-test if behaviour changes again.
