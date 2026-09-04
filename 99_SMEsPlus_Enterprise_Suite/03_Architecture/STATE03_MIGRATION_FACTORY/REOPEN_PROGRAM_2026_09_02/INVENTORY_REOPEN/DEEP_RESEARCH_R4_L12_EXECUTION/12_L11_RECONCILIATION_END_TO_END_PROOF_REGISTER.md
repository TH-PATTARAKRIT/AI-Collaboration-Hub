# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 12 — L11 Reconciliation / End-to-End Proof Register

Level: `L11 — Reconciliation / End-to-End Proof`
Scope: `10 mandated proof scenarios, mapped to the Boss-approved 22-scenario cross-proof baseline`
Control Level: `/L9999.9999`
Status: `L11 COMPLETE FOR 10/10 SCENARIOS — 0 SCENARIOS PROVABLE UNDER THE BOSS-APPROVED CONTRACT — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. The Standard Being Applied

Two Boss-approved controls govern L11 and neither may be softened.

**The 22-Scenario Cross-Proof Baseline.** Boss approved a minimum set of 22 controlled Accounting × Inventory scenarios as the joint cross-proof baseline. Each must preserve and verify the business trigger, Inventory-owned facts, Accounting-owned facts, handoff payload, quantity and unit, valuation basis where applicable, physical date, accounting effective date, product/batch/serial context, warehouse/location context, tenant/company context, source document and event identity, provenance, reversal path, migration or replay batch identity, idempotency identity, evidence source, proof state and dependency status.

**The Minimum Handoff Data Contract.** Sixteen elements must be known, traceable and evidence-backed for every material handoff. A scenario **may not be declared verified** if any material element is missing, ambiguous, unsupported, contradictory, dependent on an unapproved assumption, unable to link a reversal to its original, unable to prevent duplicate or replayed effects, or missing company/tenant isolation context.

**The convergence rule.** Accounting and Inventory Final Solutions must not be independently frozen and only reconciled afterward. The sequence is: candidate plus candidate → joint 22-scenario cross-proof → delta backflow → re-verification → integrated freeze candidate.

R4 prepares Inventory's candidate side. It does not perform the joint cross-proof, which requires both domains, and it does not freeze anything.

---

## 2. The Structural Result, Stated First

Applying the handoff contract as written to all ten mandated scenarios produces one result, and it is the same result for every scenario:

**No scenario in this register can be declared verified, and the reason is not primarily the Accounting COGS Gap.**

Three of the sixteen handoff elements are unsuppliable by Inventory for reasons that have nothing to do with Accounting:

- Element 14, migration or replay batch identity — the provenance reference does not exist (`GAP-FS-08`).
- Element 15, deterministic idempotency identity — no stable identity making a retry safe exists (`RISK-C02`).
- Element 10, company and tenant context as a *guarantee* — the Inventory-side multi-tenant invariant set does not exist (`RISK-U03`).

All three are **Lane A — not COGS-gated**. The consequence is `R4-F-16`: **even if the Joint track resolved every one of `JT-01` through `JT-12` tomorrow, not one of these scenarios could be declared verified**, because the three structural elements would still be missing.

This is the single most important thing R4 has to say at L11, and it reframes the programme's critical path. The Inventory track has been waiting on Accounting. Three of its own preconditions were never commissioned.

---

## 3. The Ten Mandated Proof Scenarios

Each scenario below records: the flow, which of the Boss-approved 22 it corresponds to, which handoff elements fail, the blocking Joint decisions, and the proof state.

Proof-state vocabulary: `NOT PROVABLE — STRUCTURAL` (fails on elements 10, 14 or 15), `NOT PROVABLE — DEPENDENCY` (additionally fails on elements 4 or 7), `PARTIALLY SPECIFIABLE` (the Inventory-owned half can be specified now).

### `L11-01` Buy → receive → stock → bill → valuation

| Aspect | Content |
|---|---|
| Boss scenarios | 1, 2, 5 |
| Flow | Purchase commitment → receipt operation → movement fact done → batch identities created → acquisition value fact emitted → supplier bill reconciled |
| Inventory-owned facts | Received quantity, unit, physical date, batch, location, source document, over/under-receipt exception |
| Failing elements | 4 (financial recognition date), 7 (cost basis), 10, 14, 15 |
| Blocking Joint decisions | `JT-02`, `JT-03`, `JT-06` |
| Additional open items | Over-receipt tolerance `GAP-FS-16` / `GAP-MD-06`; late-bill-after-close has **no prior-period attribution mechanism in the reference system at all**, making `JT-06` largely original design work |
| Proof state | `NOT PROVABLE — DEPENDENCY`. Inventory half `PARTIALLY SPECIFIABLE`. |

### `L11-02` Sale → reserve → deliver → COGS dependency

| Aspect | Content |
|---|---|
| Boss scenarios | 3, 4, 6, 7 |
| Flow | Sales commitment → operation → reservation → movement fact done → delivery outcome returned → cost-release fact emitted |
| Inventory-owned facts | Reserved quantity, delivered quantity, physical date, batch, location, shortfall disposition |
| Failing elements | 4, 7, 10, 14, 15 |
| Blocking Joint decisions | `JT-03`, `JT-04` — **`JT-04` is formally NOT DECIDABLE** |
| Additional open items | Reservation is held as a quantity on the balance rather than as an independent fact, so an adjustment can silently break it (`L5-03`); the concurrency conflict `C-04` / `N-CONC-01` is reconciled to a hold, not settled; reservation policy default `GAP-FS-22` unvalidated |
| Proof state | `NOT PROVABLE — DEPENDENCY`. `JT-04` decides whether Inventory's dispatch event or Accounting's invoice event is authoritative — the two answers are different designs, not variants. |

### `L11-03` Manufacture → consume → WIP → finished goods

| Aspect | Content |
|---|---|
| Boss scenarios | 16, 17 |
| Flow | Production order → component consumption facts → output facts → batch genealogy established → WIP and output value facts emitted |
| Inventory-owned facts | Consumed quantities and batches, produced quantities and batches, genealogy linkage |
| Failing elements | 4, 7, 10, 14, 15 |
| Blocking Joint decisions | `JT-09`, conditional on `GAP-FS-19` |
| Additional open items | Whether Manufacturing is in SMEsPlus scope is an unresolved **Boss** decision, so the whole scenario is conditional. **No manufacturing standard-cost variance posting mechanism exists in the reference ERP** — if SMEsPlus needs one it is original design work. |
| Proof state | `NOT PROVABLE — DEPENDENCY`, and conditional on a scope decision. Batch genealogy is Inventory-owned and `PARTIALLY SPECIFIABLE`. |

### `L11-04` Return and COGS reversal dependency

| Aspect | Content |
|---|---|
| Boss scenarios | 8, 9, 11 |
| Flow | Original delivery → return operation → reversing movement fact linked to the original → return value fact emitted |
| Inventory-owned facts | Returned quantity, batch, physical return date, link to the original movement |
| Failing elements | 4, 7, 10, 14, 15 |
| Blocking Joint decisions | `JT-05` — **formally NOT DECIDABLE** |
| Additional open items | Under a weighted-average policy the return is valued at the current average, not the original cost, with no retroactive rebase, producing a documented discrepancy against the credit note whose reference remedy is a manual adjustment. Under first-in-first-out the layer behaviour on return is **community-corroborated only, not primary-documented**. Three dates — sale, physical return, credit note — are independently settable with no forced alignment. |
| Proof state | `NOT PROVABLE — DEPENDENCY`. **R4's Inventory-owned contribution:** if the original cost basis is chosen, Inventory must carry per-unit original-cost lineage — a data-model requirement that must be understood before the decision, not after. |

### `L11-05` Scrap and salvage dependency

| Aspect | Content |
|---|---|
| Boss scenario | 13 |
| Flow | Scrap request → authorisation → movement to a loss destination → loss fact emitted → salvage recovery, if any |
| Inventory-owned facts | Quantity, batch, reason, authoriser, destination |
| Failing elements | 7, 10, 14, 15 |
| Blocking Joint decisions | `JT-07`-adjacent |
| Additional open items | Scrap has **no approval state** (`R4-F-04`) so the authoriser fact has nowhere to live in the reference pattern; salvage has **no concept at all** (`R4-F-03`); loss classification is configuration-dependent with **no safe default documented**; shrinkage has no distinct concept and folds into adjustment loss. Thai destruction evidence `TH-HOLD-02` **held**. |
| Proof state | `NOT PROVABLE — DEPENDENCY`. The salvage half is not merely unproven; it is undefined. |

### `L11-06` Inventory adjustment and approval evidence

| Aspect | Content |
|---|---|
| Boss scenario | 12 |
| Flow | Count → variance → approval → application → adjustment fact emitted |
| Inventory-owned facts | Counted quantity, system quantity at count time, difference, reason, counter, approver, count date, application date |
| Failing elements | 7, 10, 14, 15 |
| Blocking Joint decisions | `JT-07`-adjacent |
| Additional open items | No approval state exists in the reference pattern (`R4-F-02`); count freeze policy `GAP-MD-02` / `GAP-FS-17` unselected and unvalidated |
| Proof state | `NOT PROVABLE — STRUCTURAL`, and `PARTIALLY SPECIFIABLE` on the Inventory half. This is one of the closest scenarios to being specifiable, because every fact it needs is Inventory-owned — what is missing is the approval mechanism, which is original design work rather than a dependency. |

### `L11-07` Landed cost and allocation dependency

| Aspect | Content |
|---|---|
| Boss scenarios | 1, 5 (cost timing variants) |
| Flow | Cost document → allocation across target goods → value adjustment for goods on hand → residual for goods already gone |
| Inventory-owned facts | Base amount, allocation basis, per-line amount, which goods were still on hand at allocation time |
| Failing elements | 4, 7, 10, 14, 15 |
| Blocking Joint decisions | `JT-08` — open with an **Audit VETO concern retained** |
| Additional open items | Three mutually incompatible reference behaviours for the residual, one of which is a documented failure mode producing no entry at all. The adopted conclusion stands: **SMEsPlus must design its own handling rather than adopt any of the three.** `R4-F-05` — weight- and volume-based allocation distorts silently when those attributes are unmaintained. |
| Proof state | `NOT PROVABLE — DEPENDENCY`. `LC-02` (allocation statement inspectable before validation) and `LC-03` (explicit statement of on-hand versus gone) are Inventory-owned and specifiable now. |

### `L11-08` Period close and report tie-out

| Aspect | Content |
|---|---|
| Boss scenario | 19 |
| Flow | Period guard enforced → close snapshot produced → valuation tied to the ledger |
| Inventory-owned facts | The guard enforcement, exception grants with grantor/reason/expiry, the snapshot content |
| Failing elements | 4, 7, 10, 14, 15 |
| Blocking Joint decisions | `JT-06`, `JT-07`, `JT-12` |
| Additional open items | The v1.0 guard design — native guard at entry and validation, Accounting supplies the lock date, exception path recorded, **global unaudited bypass rejected** — is fixed and not re-litigated. What is open is the late-cost consequence. |
| Proof state | `NOT PROVABLE — DEPENDENCY`. **R4's non-blocked contribution, and it matters:** the tie-out claim must be qualified. Cross-system reconciliation holds **at the closing boundary, not continuously**; under a periodic posture the two sides are expected to diverge between closings by design. Any SMEsPlus reconciliation output must disclose which posture it measures against. An unqualified claim that the two balances always match is not supported by any evidence in this programme. |

### `L11-09` Multi-company isolation proof

| Aspect | Content |
|---|---|
| Boss scenarios | 14, 15 |
| Flow | Internal transfer with no financial effect; cross-company transfer treated as a paired sale and purchase |
| Inventory-owned facts | Source and destination location and company, movement facts on both sides |
| Failing elements | 10 above all, plus 14 and 15 |
| Blocking Joint decisions | `JT-10` |
| Additional open items | `RISK-U03` — the invariant set does not exist, so isolation cannot be proven at all (`10_L9...` §3). `GAP-FS-07` — the cross-company transfer path has **never been traced end to end**. `R4-F-06` and `R4-F-09` — company-less identities and company-less locations are structurally possible. |
| Proof state | `NOT PROVABLE — STRUCTURAL`. Scenario 14 in the Boss set specifically requires proving that an internal transfer produces **no inappropriate financial effect**; R4 records at `R4-F-18` that no independent check of that currently exists and one is required. |

### `L11-10` Migration opening tie-out

| Aspect | Content |
|---|---|
| Boss scenarios | 20, 21, 22 |
| Flow | Legacy position → transform → SMEsPlus opening balance → reconciliation → certification |
| Inventory-owned facts | Opening quantities by product, location, batch and owner; exception quarantine |
| Failing elements | 7, 10, **14 above all**, 15 |
| Blocking Joint decisions | `JT-11` / `G-5` |
| Additional open items | The provenance reference **does not exist**; `RC-08` requires human certification; prior evidence names this the highest fabrication-risk point in the whole Inventory scope. `R4-F-23` and `R4-F-24` — migration-specific hazards raised by R4. |
| Proof state | `NOT PROVABLE — STRUCTURAL`. **`R4-F-25`:** the quantity half of the tie-out is achievable independently of the value half and should not be deferred behind it. |

---

## 4. Coverage Against The Boss-Approved 22 Scenarios

R4 covers the Inventory side of every scenario in the Boss baseline. Scenario numbers below are the Boss numbering.

| Boss scenario | Covered at | Inventory-side proof state |
|---|---|---|
| 1 Purchase receipt → handoff | `L11-01`, `L11-07` | NOT PROVABLE — DEPENDENCY |
| 2 Vendor bill timing variation | `L11-01` | NOT PROVABLE — DEPENDENCY |
| 3 Sales delivery → cost handoff | `L11-02` | NOT PROVABLE — DEPENDENCY |
| 4 Customer invoice timing variation | `L11-02` | NOT PROVABLE — DEPENDENCY (`JT-04` NOT DECIDABLE) |
| 5 Partial receipt | `L11-01`, `L6-04` | NOT PROVABLE — DEPENDENCY |
| 6 Partial delivery | `L11-02`, `L6-03` | NOT PROVABLE — DEPENDENCY |
| 7 Backorder | `L11-02`, `L6-02` | NOT PROVABLE — STRUCTURAL; quantity half specifiable |
| 8 Purchase return | `L11-04` | NOT PROVABLE — DEPENDENCY |
| 9 Sales return | `L11-04`, `L6-05`, `L6-06` | NOT PROVABLE — DEPENDENCY (`JT-05` NOT DECIDABLE) |
| 10 Cancellation before execution | `INV-F-10`, `L6` §4 `C-01` | NOT PROVABLE — STRUCTURAL; **`C-01` cancellation symmetry remains an unarbitrated conflict** |
| 11 Correction after execution | `INV-F-40`, `L11-04` | NOT PROVABLE — STRUCTURAL |
| 12 Count / adjustment | `L11-06` | NOT PROVABLE — STRUCTURAL; closest to specifiable |
| 13 Scrap / damage / write-off | `L11-05` | NOT PROVABLE — DEPENDENCY; salvage undefined |
| 14 Internal transfer, no inappropriate financial effect | `L11-09`, `L5-08` | NOT PROVABLE — STRUCTURAL; no independent check exists (`R4-F-18`) |
| 15 Multi-company / tenant boundary | `L11-09`, `10_L9...` | NOT PROVABLE — STRUCTURAL; **0 of 8 isolation proofs achieved** |
| 16 Manufacturing RM → WIP → FG | `L11-03` | NOT PROVABLE — DEPENDENCY; conditional on scope |
| 17 Manufacturing reversal / scrap / variance | `L11-03` | NOT PROVABLE — DEPENDENCY; **no variance mechanism exists in the reference ERP** |
| 18 Stockable vs consumable vs service routing | `INV-F-16`, `INV-F-17` | NOT PROVABLE — STRUCTURAL; two-axis classification tie-break undefined (`GAP-FS-04`) |
| 19 Period-end / cut-off | `L11-08` | NOT PROVABLE — DEPENDENCY |
| 20 Historical migration across fiscal years | `L11-10` | NOT PROVABLE — STRUCTURAL |
| 21 Migration mapping + deterministic reconciliation | `L11-10`, `L10-04`, `L10-08` | NOT PROVABLE — STRUCTURAL; **deterministic reconciliation requires the provenance reference, which does not exist** |
| 22 Retry / idempotency / replay | `R4-F-16`, `L8-09` | NOT PROVABLE — STRUCTURAL; **this scenario is the direct expression of `RISK-C02`** |

**22 of 22 covered on the Inventory side. 0 of 22 declarable verified.** Scenario 22 deserves particular note: it is a Boss-approved mandatory scenario whose subject matter — retry, idempotency and replay — is precisely the capability that does not exist. It cannot be deferred as an edge case, because Boss has already ruled it part of the minimum baseline.

---

## 5. What Inventory Can Specify Now

R4 ends this register constructively. Despite zero provable scenarios, the following are Inventory-owned, **not COGS-gated**, and specifiable without any Joint decision:

1. Every non-sale stock reduction carries a classification distinguishing it from a sale — which is what stops the periodic cost-of-sales computation from silently mislabelling scrap, shrinkage, write-down and adjustment as cost of sales (`05` §5 identity 4, `L7-08`).
2. Reversal-to-original linkage on every correction (`INV-F-40`, handoff elements 12 and 13).
3. Physical event date and entry date carried as two distinct values on every movement (`INV-F-07`, handoff element 3).
4. Landed cost allocation stating base, basis, per-line amount, and which goods were on hand versus gone, inspectable **before** validation (`LC-02`, `LC-03`).
5. Quantity-side cutover reconciliation and certification, independent of value (`R4-F-25`).
6. An independent check that movements between two internal locations net to zero value effect (`R4-F-18`).
7. Movement history with an explicitly stated and consistently applied ordering rule (`R4-F-08`).

Items 1 and 2 are the highest-leverage: together they supply Accounting with the two things it most needs from Inventory and neither requires a Joint decision to specify.

---

## 6. L11 Coverage Result

| Measure | Result |
|---|---:|
| Mandated proof scenarios | 10 |
| Given full L11 treatment | 10 |
| Boss-approved 22 scenarios covered on the Inventory side | 22 of 22 |
| **Scenarios declarable verified under the Boss-approved contract** | **0** |
| Scenarios failing on structural elements alone (not COGS-gated) | 8 |
| Scenarios additionally failing on the Accounting COGS Gap | 14 |
| Inventory-owned items specifiable now | 7 |
| Scenarios closed by this session | **0** |

---

## 7. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
