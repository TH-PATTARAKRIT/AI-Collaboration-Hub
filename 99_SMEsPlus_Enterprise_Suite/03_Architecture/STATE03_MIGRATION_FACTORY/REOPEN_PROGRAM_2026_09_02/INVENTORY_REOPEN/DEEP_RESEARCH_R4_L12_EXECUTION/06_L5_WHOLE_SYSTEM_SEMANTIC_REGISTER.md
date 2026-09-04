# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 06 — L5 Whole-System Semantic Register

Level: `L5 — Whole-System Semantic`
Control Level: `/L9999.9999`
Status: `L5 COMPLETE FOR 10/10 MANDATED SEMANTICS — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Purpose

L5 asks whether each Inventory business meaning survives intact across the whole ERP, or whether it changes meaning as it crosses a boundary. A semantic that means one thing in Inventory and another in Sale, Accounting or Reporting is a defect even when every individual module is internally correct.

Each of the ten mandated semantics is recorded with: its meaning, where it is stated, where it is consumed, the drift risk, and R4's status.

---

## 2. The Ten Mandated Semantics

### `L5-01` Stock on hand

| Aspect | Content |
|---|---|
| Meaning | The quantity physically present at a location, derived only from completed movement facts. `CN-26`; `P-03` — derived, never edited. |
| Stated by | Inventory. |
| Consumed by | Sale (indirectly), Purchase, Manufacturing, Accounting (as the quantity side of valuation), Reporting. |
| Drift risk | **HIGH.** Users conflate on-hand with available. `L2-OBS`: the reference pattern displays available clamped at zero while true on-hand can be negative, so a genuinely negative position is indistinguishable from an empty one on screen (`R4-F-07`). Prior evidence also records a manual-override path onto the available-quantity concept that was noted twice across nine rounds and **never actually read** (`N-A13-01`) — meaning a write path onto a supposedly derived value may exist and has never been examined. |
| R4 status | Semantic is clear; **its display and its immutability are not proven.** `N-A13-01` remains a named unread lead. R4 does not close it. |

### `L5-02` Forecast stock

| Aspect | Content |
|---|---|
| Meaning | On hand, plus expected incoming, minus expected outgoing, over a horizon. |
| Stated by | Inventory. |
| Consumed by | Replenishment, Purchase, Manufacturing. |
| Drift risk | **HIGH.** The horizon and the set of commitments counted are configuration-dependent, so two users can legitimately see two different forecasts. `L2-OBS`: the shortfall computation reads a forecast that already includes in-progress supply, so the same question asked twice can give two answers (`R4-F-14`). |
| R4 status | The definition of forecast — specifically which commitments count and over what horizon — is `GAP-MD-23`, **open**. Any planning run must record its own input snapshot or its output is not reproducible (`P-06`). |

### `L5-03` Reserved stock

| Aspect | Content |
|---|---|
| Meaning | Quantity committed to a specific operation and no longer available to any other. `CN-23`. |
| Stated by | Inventory. |
| Consumed by | Sale (as a promise), Manufacturing, Reporting. |
| Drift risk | **HIGH.** `L2-OBS`: reservation is held as a quantity on the balance record rather than as an independent reservation record. An adjustment can therefore reduce a reservation without any actor intending to break a customer promise. The concurrency question (`C-04` / `N-CONC-01`) is a **preserved unarbitrated conflict** — one prior pass called it a blocking unknown with an unfollowed lead, another called it partially verified and not blocking; it was reconciled to a hold, not settled. |
| R4 status | **Semantic drift confirmed as structurally possible.** R4 records that a reservation must be a first-class, addressable fact if the promise it represents is to survive an adjustment. Carried, not closed. |

### `L5-04` Incoming stock

| Aspect | Content |
|---|---|
| Meaning | Quantity expected to arrive under an existing commitment. |
| Stated by | Purchase and Manufacturing as commitments; Inventory as expected movements. |
| Consumed by | Replenishment, Sale (as a future promise). |
| Drift risk | **MEDIUM-HIGH.** Double counting: a proposal that has become a purchase order, and the purchase order itself, can both appear as incoming if the conversion linkage is weak. This is exactly the exposure created by the absence of a stable identity (`RISK-C02`). |
| R4 status | The semantic is sound; **its uniqueness is not guaranteed.** Directly connected to `R4-F-11` (overlapping reordering rules on nested locations can each raise supply for the same shortfall). |

### `L5-05` Available stock

| Aspect | Content |
|---|---|
| Meaning | On hand minus reserved. The number a salesperson may promise against. |
| Stated by | Inventory. |
| Consumed by | Sale, above all. |
| Drift risk | **HIGHEST IN THIS REGISTER.** This is the number that destroys system credibility when it is wrong, and it is derived from two other numbers each of which has an open integrity question (`L5-01`, `L5-03`). |
| R4 status | R4 records a naming requirement rather than a design decision: the three quantities must be separately and explicitly labelled in Thai — `คงเหลือจริง`, `จองแล้ว`, `พร้อมใช้` — because a single undifferentiated "stock" figure is the fastest route to user distrust in a Thai SME. Carried from `TH-10`; still `UNVALIDATED`. |

### `L5-06` Lot and serial traceability

| Aspect | Content |
|---|---|
| Meaning | An unbroken forward and backward chain from supplier batch through storage and production to customer delivery. `CN-17`, `CN-18`. |
| Stated by | Inventory. |
| Consumed by | Quality, Sale (recall and warranty), Manufacturing (genealogy), Accounting where batch-level valuation is enabled. |
| Drift risk | **HIGH.** `R4-F-06`: identity uniqueness is scoped to (identifier, product, company) and company-less identities are possible. A supplier reusing a batch code across companies, or a company-less identity, breaks the chain's uniqueness assumption. Amending or merging a batch identity (`INV-F-20`) rewrites the chain outright. |
| R4 status | The semantic is well defined; **its identity guarantee is not.** `IV-04` (uniqueness enforced below the application layer) is confirmed by R4 as necessary rather than merely desirable. `GAP-MD-11` carried. |

### `L5-07` Ownership and location semantics

| Aspect | Content |
|---|---|
| Meaning | Two orthogonal questions: *where* goods are, and *whose* they are. Consignment stock is at our location but not ours; goods at a customer site on approval may be ours but not at our location. |
| Stated by | Inventory. |
| Consumed by | Accounting (what may be valued as our asset), Sale, Purchase. |
| Drift risk | **HIGH and under-examined.** Thai SMEs routinely treat consignment stock informally as "ours". The v1.0 concept model carries an owner dimension on the balance (`CN-26`), so the structure exists; what does not exist is a decided policy on what may be valued. |
| R4 status | `GAP-MD-09` (consignment stock, `N-A5-02`/`N-A5-03` lineage) remains **open**. The valuation consequence is `DEPENDENCY: ACCOUNTING COGS GAP`. R4 states the boundary — location and ownership are independent and must not be collapsed — and does not decide the policy. |

### `L5-08` Internal transfer versus valuation movement

| Aspect | Content |
|---|---|
| Meaning | A movement between two internal locations changes where goods are and must not change what they are worth. A movement crossing to or from a non-internal counterpart is a valuation event. `P-04`. |
| Stated by | Inventory, through the location kind. |
| Consumed by | Accounting. |
| Drift risk | **HIGH.** The entire financial neutrality of internal movement rests on the location kind being correct. `R4-F-09` — a location's company assignment is optional — and the ability to change a location's kind retrospectively both threaten it. A misconfigured operation type default (`INV-M21`) produces the same failure invisibly. |
| R4 status | **This is the single most load-bearing semantic in the module** and R4 records it as such. It is also the one most vulnerable to silent configuration error. `INV-F-28` requires the kind change to be approved and versioned. Multi-step routes create additional intermediate positions that must all remain neutral, which multiplies the surface. |

### `L5-09` Scrap versus loss versus salvage

| Aspect | Content |
|---|---|
| Meaning | Three genuinely distinct things. **Scrap** is a deliberate removal of unusable goods with a reason. **Loss** is an unexplained shortfall discovered at counting. **Salvage** is value recovered from goods already removed. |
| Stated by | Inventory. |
| Consumed by | Accounting (classification), Tax (deductibility), Management (shrinkage analysis). |
| Drift risk | **HIGHEST DRIFT IN THE MODULE.** The evidence records that scrap is documented as *not* cost of sales but as a distinct inventory-loss classification — and that this is configuration-dependent with **no documented fallback for an unconfigured loss**. It further records that shrinkage has no separate concept at all and is folded into adjustment loss unless a scrap document is raised. So all three meanings can collapse into one undifferentiated number. |
| R4 status | **Confirmed as a real and present semantic collapse.** Three separate findings converge here: `R4-F-03` (no salvage concept exists at all in the reference pattern), the configuration-dependence of loss classification, and the absence of a distinct shrinkage concept. R4's position — which is Inventory-owned and **not COGS-gated** — is that Inventory must guarantee every non-sale stock reduction carries a reason classification that distinguishes scrap, count loss, write-down and salvage from a sale. That obligation is precisely what reconciliation identity 4 in `05_L4_CROSS_MODULE_DEPENDENCY_MAP.md` §5 requires. The *accounting classification* of each remains `DEPENDENCY: ACCOUNTING COGS GAP`. Whether a distinct damaged-goods state is needed before scrap is `RISK-U02` / `U-02`, **open** and never asked of a Thai user. |

### `L5-10` Landed cost allocation meaning

| Aspect | Content |
|---|---|
| Meaning | Additional acquisition cost belongs to the goods it was incurred for, so inventory value reflects true landed cost. |
| Stated by | Inventory as an allocation fact; Accounting as a posting. |
| Consumed by | Accounting, Valuation reporting, Margin analysis. |
| Drift risk | **HIGH.** The meaning breaks down precisely where Thai importers need it most: when the cost document arrives after some or all of the goods have been sold. At that point the cost can no longer belong to inventory and must belong to something else, and the reference evidence records three mutually incompatible behaviours for that residual, one of which produces no entry at all. |
| R4 status | `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-08` open with an **Audit VETO concern retained**. The adopted conclusion, which R4 does not weaken, is that **SMEsPlus must design its own landed-cost-after-sale handling rather than adopt any of the three reference behaviours**. Inventory's non-blocked obligation is to state, at allocation time, exactly which goods were still on hand and which had gone (`LC-03`). `R4-F-05` adds that weight- and volume-based allocation silently distorts when those attributes are unmaintained. |

---

## 3. Cross-Semantic Findings

### `R4-F-17` — Three semantics depend on a guarantee that does not exist

`L5-01` (on hand), `L5-03` (reserved) and `L5-04` (incoming) each depend on movement facts being uniquely identified. No stable identity making a retry safe exists (`RISK-C02` / `IV-06`). A duplicate movement inflates on hand, a duplicated reservation over-commits, and a duplicated proposal double-orders. These are not three separate risks; they are one missing capability expressed three times. Severity **BLOCKING**; owner **Boss**; **Lane A — not COGS-gated**.

### `R4-F-18` — The neutrality of internal movement is protected only by configuration

`L5-08` holds only while location kinds and operation type defaults are correct. There is no independent check that an internal transfer produced no value effect. R4 records a required control: a continuous reconciliation asserting that movements between two internal locations net to zero value (`RC-04` extends naturally to this). Severity **MATERIAL**; owner Inventory; not COGS-gated in mechanism, though the value definition is.

### `R4-F-19` — Semantic labels are the delivery mechanism and none are validated

Every semantic in this register reaches a Thai SME user as a word on a screen. `GAP-FS-11` records that **no Thai user has validated any label, flow, reason code, document name or report title**, and this has been unremedied since the founding Thai business-reality control document. The semantics can be perfectly designed and still fail entirely at the point of use. Severity **BLOCKING for user-facing design**; owner **Boss to commission**; **Lane A — not COGS-gated**.

---

## 4. L5 Coverage Result

| Measure | Result |
|---|---:|
| Mandated semantics | 10 |
| Given full L5 treatment | 10 |
| Semantics whose meaning is clear but whose guarantee is unproven | 5 — `L5-01`, `L5-03`, `L5-04`, `L5-06`, `L5-08` |
| Semantics with confirmed present drift | 2 — `L5-09`, `L5-10` |
| Semantics fully dependency-locked | 1 — `L5-10` |
| Semantics closed by this session | **0** |

---

## 5. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
