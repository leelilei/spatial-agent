# E4 — Oracle end-to-end through the REAL framework adapters

Date: 2026-07-10

## Question

The 2026-07-06 compliance probe showed (a) the evidence contract is satisfiable
and (b) each adapter's *translation surface* can express the winning move — but
it could not run a full episode through the real adapters, because the pinned
framework checkouts were absent from that machine. They were set up locally on
2026-07-10 (with the CRLF hash fix), so this closes the gap.

## Method

Each adapter is instantiated for real, including `verify_official_checkout`
against the pinned commit and file hashes. Only the LLM call is replaced, by a
deterministic replay emitting the oracle plan **in that framework's own native
output format** (SOTOPIA: per-turn AgentAction; Generative Agents: `{"plan":[...]}`;
AgentSociety: `{"plan":{"steps":[...]}}`; GATSim: 6-tuple activity list). The
framework's own parsing, queueing, replanning triggers and evidence synthesis,
plus the typed executor and evidence-contract verifier, all run for real.

Tool: `tools/run_oracle_through_adapters.py`.
Archived: `results/cityintent_v1_rc1/oracle_through_adapters_2026-07-10/`.

## Result — 11/12 pass

| Scenario | GATSim | SOTOPIA | Generative Agents | AgentSociety |
|---|---|---|---|---|
| `meeting_wait_trap` | **FAIL** task 0.0, feas 0.444, 5 violations | 1.0 | 1.0 | 1.0 |
| `school_pickup_social_detour` | 1.0 | 1.0 | 1.0 | 1.0 |
| `budget_errand_chain` | 1.0 | 1.0 | 1.0 | 1.0 |

Passing cells earn full environment-accepted evidence (entries, purchases,
services, and an accepted `interaction` with Ben) with zero violations.

## Finding 1 — the pipeline objection is closed for three of four adapters

For SOTOPIA, Generative Agents and AgentSociety, an oracle decision driven
end-to-end through the real adapter produces every required piece of accepted
evidence. Their low scores in the rc1 and social-family runs are therefore
**decision quality**, not a pipeline that cannot represent success.

## Finding 2 — GATSim has a real, located capability gap: it cannot send messages

GATSim fails `meeting_wait_trap` even given a perfect destination plan.
`grep '"kind": "message"'` over `gatsim_official.py` returns **zero**: its
evidence synthesiser covers `buy`, `use_service`, `dwell` (to wait for a window)
and `interact`, but never `message`. `meeting_wait_trap` gates co-presence behind
a `send_message` condition, so `interaction_target_available` refuses every
`interact` attempt; the adapter retries, accumulating 5 violations and dropping
feasibility to 0.444.

This is the one place where the "adapter artifact" concern is **justified**, and
it is now pinned to a specific missing action rather than left as a general
suspicion. It means part of GATSim's co-presence shortfall in the social family
(15/21 easy, 21/27 hard) is architectural rather than decisional, and any
per-policy claim about GATSim and message-gated meetings must say so.

That the probe caught this rather than passing everything is itself evidence the
artifact check is sensitive rather than a rubber stamp.

## Follow-up

- Report GATSim's message-gated co-presence results with this caveat.
- Optionally extend the GATSim adapter's evidence synthesiser to emit the required
  coordinating `message`; that would change results, so it must be a versioned
  change with a re-run, not a silent patch.
