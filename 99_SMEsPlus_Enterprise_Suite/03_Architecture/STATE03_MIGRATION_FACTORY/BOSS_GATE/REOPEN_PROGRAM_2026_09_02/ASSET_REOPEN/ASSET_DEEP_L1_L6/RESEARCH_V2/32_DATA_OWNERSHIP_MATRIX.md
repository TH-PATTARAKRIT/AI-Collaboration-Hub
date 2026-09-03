# 32 — DATA OWNERSHIP MATRIX
**LAYER 2 — AUDIT QUARANTINE**

Required matrix F (§82), §41. Ownership is separated into five distinct kinds
because they genuinely differ, and conflating them is how "the asset record holds
the asset's value" became a working assumption on this project.

| Data object | Business owner | Module owner | Model owner | Field owner | **Where the truth lives** |
|---|---|---|---|---|---|
| Original asset value | Accounting | asset | asset | asset (computed) | **The vendor bill line balances** |
| Non-deductible tax component | Accounting | asset | asset | asset (computed) | The bill's tax repartition |
| Not-depreciable value | Accounting | asset | asset | asset | The asset row — or the template's percentage rule |
| Depreciable base | Accounting | asset | asset | computed only | Derived: original − not-depreciable |
| Accumulated depreciation | Accounting | asset | **none — no field exists** | — | **The posted journal entries** |
| Depreciable (remaining) value | Accounting | asset | asset | computed only | Derived from the entries |
| Book value | Accounting | asset | asset | stored + **recursive** | Derived: entries + not-depreciable + the child tree |
| Depreciation amount, per period | Accounting | asset | journal entry | journal entry | **The journal entry** |
| Depreciation schedule | Accounting | asset | journal entry | — | **The journal entries. There is no board table** |
| Imported prior depreciation | Migration | asset | asset | asset | The asset row — **with no GL counterpart** |
| Gain / loss on disposal | Accounting | asset | journal entry | journal entry | **The disposal entry** (the stored field can differ) |
| Asset analytic distribution | Controlling | analytic mixin | asset | asset | The asset row, **seeded from the bill** |
| Posted analytic attribution | Controlling | analytic | journal item | journal item | **The journal item, at the time it was posted** |
| Equipment identity | Operations | maintenance | equipment | equipment | The equipment row |
| Equipment serial / reference | Operations | custom | equipment | **custom** | The equipment row |
| Equipment ↔ Asset association | **unowned** | custom | asset | **custom** | The asset row, **set by hand** |
| Equipment operational status | Operations | custom | equipment | custom | The equipment row — **mutated by the asset confirm** |
| Equipment ↔ Work centre | Operations | manufacturing bridge | equipment | bridge | The equipment row |
| Machine downtime / availability | Operations | maintenance + bridge | calendar leave | bridge | The resource calendar |
| Work centre hourly rate | **Controlling, manually** | manufacturing | work centre | work centre | **A human's keystroke** |
| Work order cost | Controlling | manufacturing | work order | computed | `duration × the rate snapshotted at creation` |
| Work order analytic | Controlling | manufacturing-accounting | analytic line | analytic line | The analytic lines |
| Finished-goods unit cost | Costing | manufacturing-accounting | stock move | price unit | The stock valuation layer |
| COGS | Accounting | stock accounting | journal entry | — | The journal entries |
| **Machine cost pool** | — | **none** | **none** | **none** | **Does not exist** |
| **Per-machine usage** | — | **none** | **none** | **none** | **Does not exist** |
| **Post-depreciation internal usage** | — | **none** | **none** | **none** | **Does not exist** |

## The four rows that matter most

1. **Accumulated depreciation has no field.** It exists only as a sum over posted
   entries. Any migration or integration expecting a column will not find one, and
   the only place to put such a number is the import field — which creates
   sub-ledger/GL divergence by design (`22` §7).

2. **Book value is a recursive tree aggregate.** Not a row property. Reading it from
   one row is wrong for every revalued asset (`04` §2.3).

3. **The Equipment↔Asset association is unowned.** No business process owns it, no
   function consumes it, nothing validates it. It is the single bridge between the
   two truths and nobody is responsible for it (`19`).

4. **The work centre hourly rate is owned by a person, not a system.** Nothing
   derives it, validates it or reconciles it. That is exactly the space SMEsPlus
   proposes to occupy — and it is also why the current numbers cannot be trusted
   without checking whether anyone has set them (`UNR-15`).
