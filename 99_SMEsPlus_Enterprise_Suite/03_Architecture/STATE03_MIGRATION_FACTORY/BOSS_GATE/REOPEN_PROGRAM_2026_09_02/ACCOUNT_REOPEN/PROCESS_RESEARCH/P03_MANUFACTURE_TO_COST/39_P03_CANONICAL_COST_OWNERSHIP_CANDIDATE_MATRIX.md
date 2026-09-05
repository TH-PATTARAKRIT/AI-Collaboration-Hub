# 39 — P03 CANONICAL COST OWNERSHIP CANDIDATE MATRIX

**LAYER 2 — AUDIT QUARANTINE.**
**Classification: `DESIGN CANDIDATE` ONLY. P03 may not freeze this.**
`AASP-VETO-01` stands — `45`.

---

## 1. Reading rule

*Economic owner* — whose resource is consumed. *Event owner* — the record that proves it
happened. *Allocation owner* — what decides how much reaches a cost object. *Accounting
effect owner* — the process that posts it. *WIP injection owner* — what puts it into
inventory value. *Peer owner* — the process whose register governs the decision.

Two modules may not own one economic injection unless evidence proves they represent
different cost facts.

## 2. The matrix

| Cost | Economic owner | Event owner | Allocation owner | Accounting effect | WIP injection | Peer owner |
|---|---|---|---|---|---|---|
| **Material** | Supplier / inventory | Component-issue move | none — actual | Inventory valuation | **P03** | **P01** buys, **Inventory** values |
| **Direct labour** | Employee time | **Time log** — absent in every deployment | none — actual | should be P03 | **none today** | HR/Payroll for rate; **`DEP-07` unbridged** |
| **Work centre / machine** | Machine occupancy | **`BE-07` — no owner exists** | work-centre rate | should be P03 | **none today** | **P03**, pending `R-01` |
| **Equipment** | The machine | equipment register — `TENANT`, no cost | none | none | none | **P04** |
| **Depreciation** | The asset | Depreciation entry | analytic — **nets to zero** | **P04** posts it | **none — no path** | **P04**; `BLK-07` Boss |
| **Maintenance** | Maintenance order | maintenance record | none | P04 | none | **P04**; `BLK-08` Boss |
| **Energy** | Supplier bill | Vendor bill | none | **P01** | none | **P01**, then P03 to absorb |
| **Indirect labour** | Payroll | Payroll entry | none | HR/Payroll | none | **unowned** |
| **Overhead pool** | — | **no object** | **no denominator** | — | — | **unowned** |
| **Extra unit cost** | manual / subcontract | free float on the order | none | P03, **no relief** | P03 | **P03**; subcontract half is **P01** |
| **Subcontract** | Vendor | Subcontract receipt | receipt price | P03 + P01 | P03 | **P01** bills, **P03** capitalises |

## 3. Three ownership failures the matrix exposes

| # | Failure | Consequence |
|---|---|---|
| **O-1** | **Machine occupancy has no event owner.** Every measurement resolves to a work centre, and machine cost is a function of *human* time logs (`06` §3) | Machine cost is not causally connected to machine use. A design that fixes nothing else must fix this |
| **O-2** | **Overhead has neither an event owner nor an allocation owner.** No pool, no denominator | `BLK-07` decides a denominator for a pool that does not exist |
| **O-3** | **Indirect labour and the overhead pool are owned by no process.** Not P03, not P04, not P09, not HR | Recorded as `P03-GAP-08`; routing is Boss's, per `12` §3's precedent for `P03-GAP-02` |

## 4. Candidate ownership for SMEsPlus — non-binding

| Cost | Proposed economic owner | Proposed WIP injection owner | Blocked by |
|---|---|---|---|
| Material | Inventory | **one** path, P03-owned | — |
| Direct labour | Time capture — must exist first | P03 | `R-16` event identity |
| Machine | **Machine-grain usage record** — must exist first | P03 | `R-01`, and `BE-07` |
| Depreciation | Asset | **P03 absorbs, P04 computes** | **`BLK-07`** |
| Maintenance | Asset/maintenance | P03 absorbs planned only | **`BLK-08`** |
| Energy | Procurement | P03 absorbs | pool object |
| Overhead | **a pool object that does not exist** | P03 | **`O-2`, `BLK-07`** |
| Subcontract | Procurement | P03 | `DEP-06` |

**Every row in the "blocked by" column is owned by someone other than P03.** That is the
honest summary of P03's position: it can state where manufacturing cost *should* be owned,
and it cannot decide a single one of the blockers that would let that be built.

## 5. Prohibition restated

This matrix is **not** frozen, **not** approved, **not** a specification, and **not**
authorisation to implement. `21` §3 carries the consolidated requirement register under the
same prohibition. E4's preserved dissent (`20` §1 `D-03`) — that numbering candidates
creates a de facto baseline — applies to this file with equal force and is not resolved.
