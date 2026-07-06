# Oracle Compliance Probe — Summary

Generated: 2026-07-06T09:01:53.316923+00:00

Refutes the adapter-artifact confound: (A) the evidence contract is
satisfiable, and (B) adapter action surfaces can express the winning move.

| Scenario | Evidence focus | Tier A task_completion | Tier A feasible | Tier B surfaces | Pass |
|---|---|---:|---:|---|:--:|
| `meeting_wait_trap` | accepted co-presence interaction with ben | 1.0 | 1.0 | SOTOPIA=ok, GenerativeAgents=ok, AgentSociety=ok | PASS |
| `school_pickup_social_detour` | accepted child_pickup service before deadline | 1.0 | 1.0 | SOTOPIA=ok, GenerativeAgents=ok, AgentSociety=ok | PASS |
| `budget_errand_chain` | accepted purchase + service under budget | 1.0 | 1.0 | SOTOPIA=ok, GenerativeAgents=ok, AgentSociety=ok | PASS |

**All passed:** True

Tier B exercises the real translation functions (SOTOPIA `_parse_command`,
shared `validate_actions`). End-to-end live-model runs through the verified
framework checkouts are the complement, to run where `tmp/external/` exists.
