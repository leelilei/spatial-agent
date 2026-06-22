# Discussion and Limitations Notes

## Section Job

Explain what the results mean for designing agent societies, and state the boundary between
realistic social repair and idealized protocol assistance.

## Main Claim

The paper should not claim that ordinary LLM societies naturally preserve truth. The current
evidence supports a sharper claim:

> Social truth maintenance requires preserving provenance. Structured PROV shows the value
> of provenance-aware memory, while PROV-text-free shows that ordinary natural dialogue does
> not reliably carry source/version by default.

## Is Structured PROV Cheating?

This is the central reviewer risk and must be handled directly.

Structured PROV is **not broadcast**:

- Broadcast writes the current fact directly into every agent.
- Structured PROV still requires propagation through meetings; agents only benefit if the
  update reaches them through the social network.
- PROV can be weakened by loss, garbling, sparse mention, horizon, and topology.

But structured PROV is also **not fully naturalistic**:

- It assumes source/version survives the relay as structured metadata.
- It should be framed as an idealized protocol or upper bound.
- Its job is to show that the missing variable is provenance preservation, not to prove
  that default LLM conversation already solves the problem.

Honest wording:

> Structured PROV is a mechanism probe: it asks what happens if provenance is preserved
> through social transmission. The answer is that held truth can be repaired. PROV-text-free
> then asks whether ordinary LLM dialogue preserves that provenance unaided; the initial
> answer is no.

## Is Source/Version A Memory Improvement?

Yes, if memory is understood as social state representation and belief revision rather
than only storage capacity.

Source/version improves memory at four layers:

- **Representation:** store claim + source + version rather than claim text alone.
- **Integration:** resolve conflict by provenance/revision order instead of frequency alone.
- **Retrieval:** surface the source-grounded current claim over stale but similar events.
- **Communication:** expose attribution so the revision cue can propagate.

This is a memory improvement because it changes what the agent remembers and how conflicting
memories are reconciled. It is not merely a bigger buffer, a better embedding model, or
a stronger reflection prompt.

## Human-Society Interpretation

Human societies also suffer from true messages becoming unreliable after retelling. The
contribution is not that LLM agents uniquely fail. The contribution is that agent societies
make the failure instrumentable: every utterance, memory snapshot, source injection, and
final answer can be observed.

This also means the telephone effect is not always a defect. If the goal is to simulate human
social communication, then selective absorption, compression, reinterpretation, and provenance
loss are exactly the phenomena we may want to reproduce. The paper's normative claim is narrower:
when agent societies are used for reliable coordination over changing facts, human-like
telephone effects become an engineering risk rather than an end state.

The human analogy also legitimizes provenance:

```text
The school just sent an updated notice.
I checked with the organizer directly.
Ignore the old chat message; the latest announcement says Sunday.
```

These are natural-language source/version markers, not hidden metadata. The engineering
lesson is that agent societies may need explicit communication norms that preserve these
markers.

## PROV-Text Implication

PROV-text-free currently appears to fail because agents do not spontaneously keep phrases
like `official round 1` or `source update` in ordinary dialogue. This turns the next design
question into:

> Can explicit attribution norms in text, without hidden metadata and without broadcast,
> improve held truth over GA?

The key future comparison:

```text
GA                no provenance
PROV-text-free    natural dialogue, no attribution norm
PROV-text-norm    explicit source/version in utterance text
Structured PROV   hidden metadata upper bound
Broadcast         overwrite ceiling
```

The current strong PROV-text-norm result answers this question positively but with a caveat:
75/75 agents answer current, yet the transcript is visibly protocolized. It should be framed as
a strong attribution-norm upper bound, not as evidence that ordinary human-like communication
naturally preserves provenance.

The next result the paper actually needs is a norm-strength ablation:

```text
PROV-text-light     natural attribution only when relevant
PROV-text-medium    explicit attribution when reporting changed facts
PROV-text-strong    current Official-round protocol
```

This would let us separate three claims: whether default agents lose provenance, whether any
text attribution can repair it, and how much protocol structure is needed before the repair
becomes reliable.

## Open Questions

- How strong should the PROV-text-norm prompt be before it becomes unnatural?
- Should attribution be required in every utterance, or only when reporting updates?
- Can listeners extract source/version robustly from varied natural-language attributions?
- Does PROV-text-norm help across scenarios, or only repair_drive?
- How should the final paper position structured PROV if PROV-text-norm only partially works?
