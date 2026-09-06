# P04 → P11 HANDOFF (Core Reconciliation / Architecture)

**LAYER 2.** Surviving contradictions and Boss decisions only.

## Boss decisions P04 carries and does not close

| ID | Decision | State |
|---|---|---|
| `BLK-07` | Allocation denominator — normal capacity vs actual hours, plus the third option | **Open.** P03 routed it back to this register; P04 keeps it open |
| `P04-BD-05` | Units-of-production as TAS 16 method with normal capacity as TAS 2 denominator | Offered as a genuine third option, not a displacement |
| `P04-BD-06` | Must derecognition post automatically? | Recommendation on file, **not approved** |
| `P04-BD-07` | Is scrap a distinct retire event? | Recommendation on file, **not approved** |
| `P04-BD-08` | Capitalise-vs-expense threshold and its scope | **No decision point exists in the estate at all** |
| `P04-BD-09` | Asset model — tenant template or company accounting truth | Both readings defensible |

## Architecture contradictions surviving this closure

| # | Contradiction | Note |
|---|---|---|
| 1 | Policy is applied by **three call sites**, not by the record (`P04-F-145`) | Any fourth writer silently produces an asset with no accounts |
| 2 | **Ten snapshot fields and one live field** on the same object (`P04-F-146`) | Neither pure snapshot nor pure reference |
| 3 | **Two lock behaviours** in one module (`P04-F-155`) | One raises, one silently skips |
| 4 | Company scope **asymmetric** between two Many2ones in one custom module (`P04-F-156`) | Downgraded to a question, `P04-B-54` |
| 5 | The reference product's asset engine **cannot post off-balance** (`P04-F-154`) | Constrains a Boss-approved policy input |
| 6 | Cardinality of asset↔equipment **unconstrained** (`P04-F-149`) | Blocks the 100 % reconciliation invariant until decided |

## Evidence-basis item

`P04-B-51` — **no series-16 source exists on this host**, so every P04 source claim is bounded
to series 18 and none is asserted of the v16 deployment. P04 relies on P03's enumeration and
**declares the reliance**. If a series-16 tree is mounted, this becomes closable for both
packages at once.

**Nothing above is proposed for adoption.** `UNRESOLVED ≠ ADOPTED`.
