# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 05 — L4 Cross-Module Dependency Map

Level: `L4 — Cross-Module Dependency`
Control Level: `/L9999.9999`
Status: `L4 COMPLETE — 16-ELEMENT HANDOFF CONTRACT APPLIED — 2 ELEMENTS NOT SUPPLIABLE — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Ownership Boundary

The Boss-approved boundary governs this entire register and is not re-opened:

`Inventory Core = Stock Truth Owner.`
`Accounting Core = Financial Truth Owner.`

Restated as the architectural interface rule carried from prior evidence and adopted here without qualification:

**Inventory emits facts. Accounting decides postings.** Inventory never writes a journal entry, never selects an account, and never decides recognition timing.

Lineage: the Menu Deep Challenge round mapped 28 handoffs (`HO-01` .. `HO-28`); the v1.0 Final Solution mapped 31 (`HX-01` .. `HX-31`). R4 does not renumber either. It applies the newer Boss-approved 16-element Minimum Handoff Data Contract across them and reports which elements can and cannot be supplied.

---

## 2. The Seven Mandatory Dependency Maps

### 2.1 Sale → Delivery → Stock Movement

| Step | Owner | Fact passed | R4 status |
|---|---|---|---|
| Sales commitment confirmed | Sale | Product, quantity, date, customer, delivery address, priority | Mapped (`HO-01`) |
| Demand received as an operation | Inventory | Operation created in waiting state | Mapped (`INV-F-05`) |
| Reservation taken | Inventory | Available quantity committed | Mapped (`INV-F-06`) — **integrity question open**: reservation is held as a quantity on the balance rather than as an independent record, and the concurrent-locking conflict (`C-04` / `N-CONC-01`) was reconciled to a hold, not settled |
| Goods physically leave | Inventory | Movement fact, done | Mapped (`INV-F-07`) |
| Delivery outcome returned | Inventory → Sale | Delivered quantity, date, batch/serial, shortfall status | Mapped (`HO-02`) |
| Cost released | Inventory → Accounting | Cost-release fact | **`DEPENDENCY: ACCOUNTING COGS GAP`** — `JT-04` recognition timing is formally NOT DECIDABLE. R4 may not state whether Inventory's dispatch event or Accounting's invoice event is authoritative. |

The reservation-policy default itself (reserve on confirmation or reserve on picking) is `GAP-FS-22`, **open**, and requires Thai user validation.

### 2.2 Purchase → Receipt → Stock Valuation

| Step | Owner | Fact passed | R4 status |
|---|---|---|---|
| Purchase commitment confirmed | Purchase | Product, quantity, expected date, supplier, price reference | Mapped (`HO-04`) |
| Receipt operation created | Inventory | Operation in waiting state | Mapped |
| Goods physically arrive | Inventory | Movement fact, done; batch identities created | Mapped (`INV-F-07`, `INV-F-19`) |
| Receipt outcome returned | Inventory → Purchase | Received quantity, date, batch, over/under receipt | Mapped (`HO-05`) — over-receipt tolerance policy `GAP-FS-16` / `GAP-MD-06` **open** |
| Acquisition value emitted | Inventory → Accounting | Receipt valuation fact | Mapped as a fact (`HO-07`); posting is Accounting's |
| Supplier bill reconciled against receipt | Accounting → Inventory | Price difference against the receipt cost basis | **`DEPENDENCY: ACCOUNTING COGS GAP`** — the price-difference account scope is a recorded contradiction blocking `JT-02`; a late bill after close is `JT-06`, and the evidence records **no documented prior-period attribution mechanism exists in the reference system at all**, making `JT-06` largely original design work |

### 2.3 Manufacturing → Raw Material, WIP, Finished Goods, Capacity, Cost

| Step | Owner | Fact passed | R4 status |
|---|---|---|---|
| Production order confirmed | Manufacturing | Component demand, expected output | Mapped (`HO-18`) |
| Components issued | Inventory | Consumption movement facts | Mapped (`HO-19`) |
| Output received | Inventory | Production movement facts, output batch identities | Mapped (`HO-19`) |
| Batch genealogy established | Inventory | Component batches linked to output batches | Mapped — this is the linkage that makes recall possible and it is Inventory-owned |
| Work-in-progress recognised | Inventory → Accounting | WIP timing fact | **`DEPENDENCY: ACCOUNTING COGS GAP`** — `JT-09` open and conditional on `GAP-FS-19` |
| Production variance | — | — | **No reference pattern exists.** The evidence records that no manufacturing standard-cost variance posting mechanism exists in the reference ERP. If SMEsPlus needs one it is original design work. |
| Capacity | Manufacturing | — | **Out of Inventory scope.** Capacity is a Manufacturing concern; Inventory contributes only material availability. R4 states this boundary explicitly because the L4 requirement names capacity, and naming it without claiming ownership is the correct treatment. |

Whether Manufacturing is in SMEsPlus scope at all is `GAP-FS-19`, **a Boss decision, unresolved**. This whole map is therefore conditional.

### 2.4 Accounting → Valuation, Interim, COGS, Landed Cost, Return, Scrap, Close

This is the dependency-locked map. Every row is study-only.

| Area | Inventory obligation | Blocking decision | R4 status |
|---|---|---|---|
| Valuation policy ownership | Supply the category, product and warehouse structure the policy could attach to | `JT-01` | **NOT DECIDABLE** — eight named sub-facts missing, two requiring live-instance access |
| Costing methods and change rules | Supply the fact that method is a company-scoped property of the category, and that a method change does not retroactively rebase existing on-hand value | `JT-02` | Blocked by a recorded contradiction on price-difference account scope |
| Continuous versus periodic timing | Emit facts at the physical event regardless of posture | `JT-03` | Open. The evidence establishes the reference ERP has **no single stable pattern across versions**, so "do whatever the reference does" is not an available option |
| Interim positions between physical and financial | Supply the physical event and its date | — | Interim bridging accounts are Accounting's structure; Inventory supplies the timing gap that makes them necessary |
| COGS recognition timing | Emit the cost-release fact at dispatch | `JT-04` | **NOT DECIDABLE** |
| Landed cost eligibility and posting | Emit the allocation with base, basis and per-line amount, and state which goods were still on hand | `JT-08` | Open with an **Audit VETO concern retained**; three incompatible reference behaviours documented, one of them a failure mode producing no entry |
| Return cost basis | Emit the return fact and the link to the original movement | `JT-05` | **NOT DECIDABLE**. R4's material contribution: **if the original cost basis is chosen, Inventory must carry per-unit original-cost lineage — a data-model requirement, not a report requirement.** Stating that consequence is within Inventory's authority; choosing the basis is not. |
| Scrap and salvage accounting | Emit the loss fact with reason and a distinguishable loss classification | `JT-07`-adjacent | Configuration-dependent with **no safe default documented**; salvage has **no reference pattern at all** (`R4-F-03`) |
| Period close and late movement | Enforce the guard; emit the close snapshot | `JT-06`, `JT-07`, `JT-12` | `JT-12` mechanism may be scoped now; late-cost consequence gated |
| Inventory-to-ledger reconciliation | Produce a reproducible as-of position | `JT-01`, `JT-03`, `JT-07` | See §5 |

### 2.5 Approval → Controlled Changes

| Controlled change | Approval required | Reference pattern available | R4 status |
|---|---|---|---|
| Inventory adjustment | Yes | **No approval state exists** (`R4-F-02`) | Original control design; `GAP-MD-02` open |
| Scrap | Yes | **No approval state exists** (`R4-F-04`) | Original control design |
| Costing category assignment or method change | Yes | Partially | `DEPENDENCY: ACCOUNTING COGS GAP` |
| Location kind change | Yes | No | Original control design |
| Route or rule change | Yes | No | Original control design |
| Operation type numbering change | Yes | No | Original control design; `TH-HOLD-09` |
| Unit conversion factor or precision change | Yes | No | Original control design |
| Packaging contained quantity change | Yes | No | Original control design |
| Attribute change after variants hold stock | Yes | No | `GAP-FS-03` open |
| Batch identity amendment or merge | Yes | No | Original control design |
| Period exception grant | Yes, with named grantor, reason and expiry | Reference offers a **global unaudited bypass**, explicitly **rejected** by the v1.0 design | Position fixed; not re-litigated |
| Capability switch change | Yes | No | `GAP-MD-14` open |

R4's summary finding at L4: **the reference system supplies almost no approval infrastructure for the changes that matter most to stock integrity.** Twelve controlled changes are identified; a reference pattern exists for at most one and a half of them. Approval control in SMEsPlus Inventory is therefore predominantly original design work, and this is a larger origination scope than earlier rounds had made explicit. Recorded as `R4-F-15`.

### 2.6 Document → Evidence Attachment

| Function | Evidence that must be attachable | Status |
|---|---|---|
| Adjustment (`INV-F-04`) | Count sheet, variance explanation, approver record | Required |
| Scrap (`INV-F-12`) | Authorisation, photographic or witness evidence, destruction evidence where claimed | Required; Thai destruction evidence `TH-HOLD-02` **HOLD** |
| Landed cost (`INV-F-14`) | Freight, duty and clearing invoices | Required; Thai import duty and VAT treatment `TH-HOLD-03` **HOLD** |
| Receipt / delivery (`INV-F-07`) | Delivery note, packing evidence, carrier document | Required; delivery-document-to-tax-invoice linkage `TH-HOLD-09` **HOLD** |
| Opening balance (`INV-F-41`) | The accountant's certified opening position | Required; `RC-08` demands **human certification** |
| Batch (`INV-F-19`) | Certificate of analysis, supplier batch document | Required for tracked industries; sector obligations `TH-HOLD-08` **HOLD** |

Every Thai statutory item above is `HOLD / EVIDENCE REQUIRED` and routes to the Accounting-Tax track. R4 makes no Thai statutory claim.

`GAP-MD-29` — the PDPA scope for Inventory documents — has **zero coverage anywhere in the evidence chain** and remains open. R4 confirms it is still unaddressed and records it as needing to be scoped as a joint item with the Account and Legal tracks.

### 2.7 Reporting → Reconciliation

The ten reconciliation requirements `RC-01` .. `RC-10` are carried forward unchanged from v1.0. R4 re-reads them against the newer COGS evidence and records the following, which is a **disclosure requirement rather than a decision** and is therefore not blocked:

- `RC-01` conservation and `RC-05` reservations-never-exceed-on-hand are Inventory-owned and continuously checkable.
- `RC-02` stock-card reproducibility is Inventory-owned but depends on the ordering rule being stated (`R4-F-08`).
- `RC-03` valuation agreeing with the ledger **holds at the closing boundary, not continuously.** Under a periodic posture the two sides are expected to diverge between closings by design. Any SMEsPlus reconciliation output must state which posture it is measuring against. An unqualified claim that the two balances always match is not supported by any evidence in this programme.
- `RC-04`, `RC-06`, `RC-07` are Inventory-owned.
- `RC-08` opening balance requires human certification and is unresolved (`JT-11` / `G-5`).
- `RC-09` requires Accounting to record disposition of every emitted fact.
- `RC-10` export fidelity remains a required acceptance test because the reference export was found defective in practice (`RISK-G7`).

---

## 3. Consolidated Handoff Classification

R4 re-reads the 31 v1.0 handoffs against the current COGS evidence. The classification does not change; what changes is that three of the Joint items are now known to be **formally not decidable** rather than merely open.

| Class | Count | Meaning | R4 movement |
|---|---:|---|---|
| `INV-OWNED` | 14 | Inventory owns and can specify now | Unchanged — these are the actionable set |
| `ACCT-IF` | 7 | Inventory states a requirement of Accounting | Unchanged |
| `JOINT` | 9 | Neither domain may decide alone | **3 now formally NOT DECIDABLE** (`JT-01`, `JT-04`, `JT-05`) |
| `TAX-HOLD` | 4 | Thai statutory, Accounting-Tax track | Unchanged |

The convergence sequence approved by Boss is binding and is restated here because it constrains what any Inventory session may do:

`Account Final Solution Candidate + Inventory Final Solution Candidate → Joint 22-Scenario Cross-Proof → Delta Backflow to Each Domain → Re-Verification → Integrated Final Freeze Candidate.`

Accounting and Inventory **must not be independently frozen and only reconciled afterward.** R4 therefore prepares Inventory's candidate side and does not freeze it.

---

## 4. The 16-Element Minimum Handoff Data Contract Applied

This is the newest binding control and the most consequential part of R4's L4 work. For every material Inventory-to-Accounting handoff, sixteen elements must be known, traceable and evidence-backed. R4 assesses Inventory's ability to supply each.

| # | Element | Can Inventory supply it today? | Basis |
|---:|---|---|---|
| 1 | `WHAT happened` | **Yes** | Movement fact (`CN-25`) is a first-class concept |
| 2 | `WHO owns the fact` | **Yes** | Ownership boundary is Boss-approved and unambiguous |
| 3 | `WHEN physical event occurred` | **Yes** | Effective date is captured on the movement |
| 4 | `WHEN financial recognition occurs` | **No — and this is a genuine finding** | `DEPENDENCY: ACCOUNTING COGS GAP`. `JT-04` is NOT DECIDABLE. `L2-OBS` establishes that in the reference pattern the financial entry date defaults to the **processing date, not the physical event date**, unless explicitly overridden — so the two dates genuinely diverge by default. Inventory can supply the physical date and can flag the divergence; it cannot supply the recognition date. Recorded as `HOLD` per the contract's own instruction. |
| 5 | `HOW MUCH quantity` | **Yes** | |
| 6 | `WHICH UOM` | **Yes**, with a caveat | Conversion rounding defaults upward (`R4-F-13`); the emitted UOM must be the one actually used, with the conversion recorded |
| 7 | `WHAT valuation / cost basis applies` | **No** | `DEPENDENCY: ACCOUNTING COGS GAP`. `JT-01`, `JT-02`, `JT-05` all open; `JT-01` and `JT-05` NOT DECIDABLE. Recorded as `HOLD`. |
| 8 | `WHICH Product / Lot / Serial` | **Yes**, with a caveat | Identity scope is (identifier, product, company) and company-less identities are possible (`R4-F-06`) |
| 9 | `WHICH Warehouse / Location` | **Yes**, with a caveat | Company-less locations are possible (`R4-F-09`) |
| 10 | `WHICH Company / Tenant` | **Partially** | `RISK-U03` / `GAP-FS-10` — the Inventory-side multi-tenant invariant set **does not exist**. The context can be carried on a record; that it is *guaranteed* cannot yet be asserted. |
| 11 | `WHICH Source Document` | **Yes** | |
| 12 | `WHICH Original Event` | **Yes** | Reversal-to-original linkage is a design requirement of `INV-F-40` |
| 13 | `WHICH Reversal / Correction` | **Yes** | As above |
| 14 | `WHICH Migration / Replay Batch` | **No** | `GAP-FS-08` — the provenance reference (`CN-36`) **does not exist and must be originated**. Lane A: not COGS-gated, actionable now. |
| 15 | `WHICH Idempotency Identity` | **No** | `RISK-C02` / `IV-06` / `GAP-MD-21` — no stable identity making retry safe exists. Lane A: not COGS-gated, actionable now. |
| 16 | `WHAT Evidence proves it` | **Yes** | Document attachment per §2.6 |

### 4.1 Result

**Eleven of sixteen elements can be supplied today. Two are gated behind the Accounting COGS Gap. Three cannot be supplied because the underlying Inventory capability does not exist.**

The contract states that a scenario may not be declared verified if any material required element is missing, ambiguous, unsupported, contradictory, dependent on an unapproved assumption, unable to link a reversal to its original, unable to prevent duplicate or replayed effects where idempotency is required, or missing company/tenant isolation context.

Measured against that standard:

- Elements 4 and 7 fail on `DEPENDENCY: ACCOUNTING COGS GAP` — resolvable only by the Joint track.
- Elements 14 and 15 fail on "unable to prevent duplicate or replayed effects" — **and both are Lane A, not COGS-gated.**
- Element 10 fails on "missing company/tenant isolation context" as a *guarantee* — `RISK-U03` is Lane A, Boss-owned, and also **not COGS-gated**.

**This is R4's single most useful finding at L4.** Three of the five failing elements are not blocked by the Accounting COGS Gap at all. They are blocked by work nobody has commissioned. Even if the Joint track resolved every one of `JT-01` .. `JT-12` tomorrow, **no Inventory-to-Accounting handoff could be declared verified under the Boss-approved contract**, because idempotency identity, provenance identity and the multi-tenant invariant set would still be missing.

Recorded as `R4-F-16`, severity **BLOCKING**, owner Boss, and carried as the lead recommendation in `21_PMO_REVIEW_AND_RECOMMENDATION.md`.

---

## 5. Inventory-To-Ledger Reconciliation Identities

R4 adopts the five identities from the COGS evidence without weakening any of them, and records Inventory's position on each.

| # | Identity | Status in evidence | Inventory position |
|---:|---|---|---|
| 1 | Physical stock conservation | `CANDIDATE` — Inventory-owned; Accounting cannot verify it | Inventory owns this and can prove it, **but only once a stable movement identity exists** (`RISK-C02` is a precondition, not a nicety) |
| 2 | Inventory value identity | `CANDIDATE` — internally consistent by construction, which is not proof of correctness | Breaks on unresolved landed cost, mid-period method change, and negative stock — all three are live in R4's findings |
| 3 | Cost release to an approved classification | `VERIFIED` as a governing constraint only | The rule set that performs the classification is itself `HOLD` |
| 4 | Periodic COGS candidate | `CANDIDATE` with a **material correction** | The naive opening-plus-purchases-minus-closing formula silently mislabels every non-sale inventory reduction as cost of sales unless scrap, shrinkage, write-down and adjustment are separately identified and subtracted first. **Inventory is the domain that can supply those separations** — this is a concrete, non-blocked Inventory obligation and R4 records it as such. |
| 5 | Cross-system reconciliation | `CANDIDATE`, strongest support, **holds only at the closing boundary** | Inventory must disclose the posture its as-of report measures against |

Identity 4 deserves emphasis. It is the one place in the entire dependency map where Inventory can materially de-risk the Accounting side **without waiting for any Joint decision**: by guaranteeing that every non-sale stock reduction carries a reason classification distinguishable from a sale. That obligation is Inventory-owned, Lane A, and actionable now.

---

## 6. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
