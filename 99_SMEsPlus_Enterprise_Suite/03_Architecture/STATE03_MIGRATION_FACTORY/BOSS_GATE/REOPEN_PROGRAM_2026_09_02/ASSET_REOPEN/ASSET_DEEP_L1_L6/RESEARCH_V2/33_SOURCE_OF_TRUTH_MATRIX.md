# 33 — SOURCE-OF-TRUTH MATRIX
**LAYER 2 — AUDIT QUARANTINE**

Required matrix G (§82). For each fact: the authoritative store, what derives from
it, and how a consumer can get it wrong.

| Fact | **Authority** | Derived stores | How a consumer gets it wrong |
|---|---|---|---|
| What the asset cost | The vendor bill line balances | The asset's original value | Reading the asset row after someone edited it — the field is user-overridable |
| How much has been depreciated | **The posted journal entries** | The asset's depreciable value, book value | Summing naively — reversals, reversed entries and value-change entries must all be excluded |
| What the asset is worth now | **Derived, not stored** | The stored book value | Reading one row — book value aggregates the child tree |
| What the depreciation schedule is | **The journal entries** | The schedule display | Expecting a board table. There is none |
| When depreciation started | The prorata date, shifted by paused days | — | Reading the prorata date alone on a paused asset |
| How long the asset lives | Duration × period length, from the prorata date | The computed lifetime | Reading duration as "months". It is periods |
| **How days are counted** | **The computation mode field** | Everything numeric | **Assuming a calendar. The default is 30/360** |
| What accounts were used | **The posted entries** | The asset's account triple | Reading the triple — it can be changed after posting |
| What analytic was attributed | **The posted journal items** | The asset's distribution | Reading the asset's distribution — it can differ from its own history |
| Whether the asset is finished depreciating | **Derived: depreciable value = 0** | — | Looking for a state. **There is none** |
| Whether the asset was sold or scrapped | **The disposal entry's move type** | — | Reading the asset state. Both are `close` |
| The gain or loss on disposal | **The disposal entry** | The stored gain field | Reading the stored field — it can differ by the not-depreciable value |
| Which machine an asset is | **Nothing authoritative** | A manual custom field | Trusting it. Optional, unconstrained, duplicable |
| Whether a machine is in production | The equipment's work-centre link | — | Assuming the asset knows. It does not |
| A machine's operational status | The equipment row | — | Not knowing a **financial** action mutates it |
| Whether a machine is available | The resource calendar | Maintenance requests | Expecting a cost consequence. There is none |
| What a work order cost | The work order's snapshotted rate × duration | Analytic lines, valuation | Reading the work **centre**'s current rate. It may have changed |
| What a finished good cost | The stock valuation layer | — | Expecting machine depreciation in it. It is not there |
| Thai statutory maximum rate | **Royal Decree 145 s.4** | — | Treating it as a required schedule. It is a **ceiling** |
| Thai pro-ration requirement | **Revenue Code s.65 bis (2)** | — | Treating the software default as compliant |
| Whether the pro-ration unit is the day | **Not established** | — | Asserting it. `UNR-01` |
