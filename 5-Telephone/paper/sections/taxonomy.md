# Taxonomy Notes

## Section Job

Make the paper's categories explicit. The taxonomy should prevent the work from being read
as a single binary accuracy benchmark. Our object is social truth maintenance, so the paper
needs categories for:

- what agents finally hold;
- how truth fails during transmission;
- what kind of repair an intervention represents;
- whether provenance is preserved as metadata, text, or not at all.

## Taxonomy 1: Held-Answer Verdict

This is the scoring taxonomy used throughout the experiments.

| Class | Meaning | Why it matters |
|---|---|---|
| **current** | The agent holds the latest ground-truthed value. | Successful social truth maintenance. |
| **stale** | The agent holds the old superseded value. | Active corruption: old consensus displaced the update. |
| **unknown** | The agent does not hold either value. | Information loss or failed retention, distinct from corruption. |
| **unsupported specific** | The answer is scored unknown but invents a concrete time/place/value. | A grounding failure hidden by ordinary unknown scoring. |

The load-bearing split is **stale vs unknown**. A binary correct/incorrect score would hide
whether an intervention creates active false belief or merely fails to install the update.

## Taxonomy 2: Transmission Failure Modes

These categories describe how a true update degrades as it moves through a society.

| Failure mode | Description | Example |
|---|---|---|
| **Loss** | The update disappears; agents later answer unknown. | "The notes don't say when or where." |
| **Stale persistence** | The old value keeps circulating and out-competes the update. | Saturday/front porch survives after Sunday/community center update. |
| **Detail drift** | The value mutates while staying superficially plausible. | community center -> community hall / shed; 8am -> morning. |
| **Version splitting** | Different subgroups hold different versions. | One cluster says Sunday, another says Saturday, another says unknown. |
| **Unsupported concretization** | Agents invent a concrete answer not supported by the trace. | "9 AM at the community shed." |
| **Source/version loss** | The content may survive, but attribution and revision order are lost. | "Sunday" is repeated without "official update from Rosa." |
| **Speech-belief dissociation** | Agents utter the current value but later do not hold it when probed. | Source condition moves SAY but not HOLD. |

The current title centers the sixth category: truth loses force when it loses its source.

## Taxonomy 3: Intervention / Channel Type

This is important for the "is PROV cheating?" critique.

| Intervention | Channel | What it tests | Paper status |
|---|---|---|---|
| **GA baseline** | Ordinary natural language + GA-style memory. | Default social transmission. | Main baseline. |
| **Persistent source** | One authoritative source repeats the update socially. | Does exposure from authority repair belief? | Fails to repair HOLD. |
| **Broadcast** | Direct write to every agent. | Positive control / overwrite ceiling. | Works, but bypasses social transmission. |
| **Structured PROV** | Social propagation plus hidden source/version metadata. | Upper bound if provenance is preserved. | Works strongly; idealized. |
| **PROV-text-free** | Source/version must survive in ordinary utterance text. | Do agents naturally preserve provenance? | Initial result: no. |
| **PROV-text-norm** | Source/version is explicitly required in utterance text. | Can a natural-language attribution norm repair social memory? | Next target. |

Structured PROV is not broadcast because it still requires network propagation. But it is
not fully naturalistic because it assumes provenance survives as a reliable protocol signal.

## Taxonomy 4: Memory Mechanism Type

This helps position source/version as a memory improvement without reducing the paper to a
memory-module benchmark.

| Memory type | What it stores/emphasizes | Expected weakness |
|---|---|---|
| **Raw stream** | Append-only utterance history. | Recency and noise dominate. |
| **GA reflection** | Events plus free-text reflections. | Reflections can compress away source/version. |
| **Recency memory / MemoryBank-like** | Recently relevant events. | Stale relays can be recent. |
| **Evolving note / A-MEM-like** | A compact current note. | Needs reliable textual change cues. |
| **Currency extraction / SMGA-like** | Attempts to maintain current facts. | Can fail to propagate socially. |
| **Provenance-aware memory** | Claim + source + version. | Requires provenance to survive communication. |

The claim is not "our memory is bigger." The claim is that changing facts need a memory
semantics that preserves provenance and revision order.

## How This Should Enter The Paper

The taxonomy should probably appear in Method / Measurement, not as a standalone long
section. A compact table can define:

1. held-answer verdicts;
2. failure modes;
3. intervention/channel types.

Then Results can refer back to the terms:

- GA mostly creates unknown/loss and sometimes stale persistence.
- Stronger models can convert loss into confident stale corruption.
- Persistent source changes speech but not held answer.
- Structured PROV removes source/version loss under an idealized protocol.
- PROV-text-free shows ordinary language drops source/version.

## Open Questions

- Should "mixed" be a fourth held-answer class, or should mixed stay under stale if it
  mentions the superseded value?
- Should unsupported specific be a primary class or a secondary flag?
- Should source/version loss be measured directly from transcripts in all PROV-text runs?
- Can failure modes be auto-coded reliably, or should we report them as qualitative trace
  audits plus current/stale/unknown counts?
