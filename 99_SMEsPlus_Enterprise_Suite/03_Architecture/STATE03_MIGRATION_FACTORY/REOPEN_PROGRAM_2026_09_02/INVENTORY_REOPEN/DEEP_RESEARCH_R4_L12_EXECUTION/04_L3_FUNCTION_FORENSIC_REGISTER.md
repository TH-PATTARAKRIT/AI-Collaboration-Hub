# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 04 — L3 Function Forensic Register

Level: `L3 — Function Forensic`
Scope: `41 controlled functions across 29 of 29 Inventory menus`
Control Level: `/L9999.9999`
Status: `L3 COMPLETE FOR 41/41 FUNCTIONS — 14 CARRY A COGS DEPENDENCY LOCK — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Method

Each function is recorded against the eight L3 dimensions the standard requires: trigger, preconditions, postconditions, state transition, quantity impact, cost impact, document or event output, and audit evidence required.

Function IDs are `INV-F-01` .. `INV-F-41` and are stable for the rest of this package. Evidence tags `L2-OBS`, `L1-CF`, `L0-INF` carry the meanings defined in `03_L2_UI_FIELD_CONFIGURATION_FORENSIC.md` §1.

Two standing rules from the v1.0 baseline govern every row and are not re-litigated here:

- `P-07` / interface rule: **Inventory emits facts; Accounting decides postings.** No function below writes a journal entry, selects an account, or decides recognition timing. Where a row states a cost impact, that is the *fact Inventory emits*, never a posting Inventory performs.
- `P-02` / `IV-05`: a completed movement fact is immutable. Corrections are new reversing facts, never edits.

Where a cost impact cannot be stated without an Accounting decision, the row carries `DEPENDENCY: ACCOUNTING COGS GAP` and names the blocking Joint decision (`JT-01` .. `JT-12`).

---

## 2. Operations Functions

### `INV-F-01` — Compute replenishment shortfall (`INV-M01`, `INV-M06`)

| Dimension | Finding |
|---|---|
| Trigger | Scheduled automatic run, or a user-initiated run, or opening the replenishment view. |
| Preconditions | At least one active reordering rule not currently suspended; product and location exist; company context resolved. |
| Postconditions | A proposed quantity exists per product/location, with the rule that produced it identified. |
| State transition | None on stock. The proposal is a new record, not a change to an existing one. |
| Quantity impact | **None.** A proposal moves nothing. This distinction must be visible to the user (`P3` naming principle). |
| Cost impact | None. |
| Document / event output | Replenishment proposal (`CN-21`), plus a planning-run record (`CN-35`). |
| Audit evidence required | Which rule fired, what the forecast position was at the moment of computation, and which run produced the proposal. `L2-OBS`: the reference computation reads a forecast position that already includes in-progress supply, so the same input read at two moments legitimately gives two different answers — the run must therefore record its own input snapshot or the result is not reproducible (`P-06`). Recorded as `R4-F-14`. |

### `INV-F-02` — Convert a proposal into a supply action (`INV-M01`)

| Dimension | Finding |
|---|---|
| Trigger | User confirmation of a proposal, or automatic confirmation where the rule is set to automatic. |
| Preconditions | A supply route resolves to buy, make, or transfer; the target document type is available; the user holds the right to raise that document. |
| Postconditions | A purchase requirement, production requirement, or internal transfer request exists in the receiving domain. |
| State transition | Proposal → converted. |
| Quantity impact | None directly; creates a future incoming commitment which changes forecast availability. |
| Cost impact | None at Inventory. |
| Document / event output | A supply request handed to Purchase, Manufacturing, or Inventory itself. |
| Audit evidence required | The proposal identity, the rule identity, the converting user, and the resulting document identity, linked in both directions. Without a stable identity linking the three, a retried conversion cannot be distinguished from a second genuine conversion — this is `RISK-C02` / `IV-06` / `GAP-MD-21`, and R4 confirms it as a live exposure rather than a theoretical one. |

### `INV-F-03` — Record a physical count (`INV-M02`)

| Dimension | Finding |
|---|---|
| Trigger | A count is performed and entered, either as a scheduled cycle count or an ad-hoc count. |
| Preconditions | Product and location exist; the count date falls in a period the user is permitted to affect; lot/serial supplied where the product is tracked. |
| Postconditions | A counted quantity and a computed difference exist, not yet applied. |
| State transition | Count session opened → counted. |
| Quantity impact | **None yet.** Counting is not adjusting. `L2-OBS` confirms the reference pattern blurs this by holding the counted quantity on the balance record itself (finding `R4-F-02`); SMEsPlus separates them via `CN-27`. |
| Cost impact | None yet. |
| Document / event output | Count sheet (`TH-R14` `ใบตรวจนับสินค้า`). |
| Audit evidence required | Who counted, when, against which location, and what the recorded quantity was at the moment of counting. The system quantity at count time must be captured, because it changes afterwards. |

### `INV-F-04` — Approve and apply an adjustment (`INV-M02`)

| Dimension | Finding |
|---|---|
| Trigger | An authorised person accepts the counted difference. |
| Preconditions | A count exists; a reason is supplied; the approver is not the counter (segregation of duties); the effective date is in an open period, or an exception has been granted with a named grantor, reason and expiry (`IV-07`). |
| Postconditions | Recorded quantity equals counted quantity; a reason-coded, approver-identified adjustment fact exists. |
| State transition | Counted → approved → applied. |
| Quantity impact | **Yes** — a correction in either direction, against an adjustment counterpart location, never against thin air. |
| Cost impact | **Yes.** `DEPENDENCY: ACCOUNTING COGS GAP`. The evidence is explicit that whether an adjustment loss lands in cost of sales or in a distinct loss classification is configuration-dependent with **no safe default documented**. Inventory emits the fact; the classification is `JT-07`-adjacent and Accounting-owned. R4 does not choose. |
| Document / event output | Adjustment (`CN-28`); adjustment register (`TH-R07`). |
| Audit evidence required | Counter, approver, reason, count date, application date, before and after quantities, and the count sheet itself. `GAP-MD-02` (approval policy unselected) is unresolved — R4 confirms via `R4-F-02` that the reference pattern supplies no approval state to inherit, so this is original control design. |

### `INV-F-05` — Create a stock operation (`INV-M03`)

| Dimension | Finding |
|---|---|
| Trigger | A demand arrives from Sale, Purchase or Manufacturing, or a user creates an operation directly, or a rule generates one. |
| Preconditions | Operation type resolved; source and destination locations resolved; product is stock-controlled; company context consistent across all referenced records. |
| Postconditions | An operation exists in draft or waiting state with demanded quantities. |
| State transition | — → draft / waiting. |
| Quantity impact | None. A demanded quantity is a commitment, not a movement. |
| Cost impact | None. |
| Document / event output | Stock document (`CN-24`) of the receipt, delivery, transfer or return kind. |
| Audit evidence required | The originating demand identity, the rule identity where generated automatically, and the operation type applied. |

### `INV-F-06` — Reserve stock against an operation (`INV-M03`)

| Dimension | Finding |
|---|---|
| Trigger | Operation confirmation, or an explicit reserve action, or a scheduler pass. |
| Preconditions | Available quantity exists at the source location; the reservation policy on the operation type permits it. |
| Postconditions | A quantity is committed to this operation and is no longer available to others. |
| State transition | Waiting → ready (fully or partially). |
| Quantity impact | On-hand unchanged; **available reduced**. The distinction is the single most common source of user misunderstanding (`INV-M10`). |
| Cost impact | None. |
| Document / event output | Reservation (`CN-23`). |
| Audit evidence required | What was reserved, from which balance, when, and against which operation. `L2-OBS`: reservation is held as a quantity on the balance record rather than as an independent reservation record, which is why an adjustment can silently reduce a reservation. Combined with the unresolved `C-04` / `N-CONC-01` row-locking conflict — where the Council and the Special Team disagreed and the conflict was reconciled to `HOLD`, not settled — concurrent reservation remains an open integrity question. R4 does not settle it; it is carried and escalated to `L15`. |

### `INV-F-07` — Validate a stock operation (`INV-M03`)

| Dimension | Finding |
|---|---|
| Trigger | The operator confirms the goods have physically moved. |
| Preconditions | Done quantities entered; lot/serial supplied for tracked products; the effective date is in an open period or an approved exception exists; destination location is valid for the goods. |
| Postconditions | Movement facts are recorded as done and become immutable. |
| State transition | Ready / partially ready → done. |
| Quantity impact | **Yes** — the actual movement between source and destination. |
| Cost impact | **Yes where the movement crosses the internal / non-internal boundary** (`P-04`). Receipt from a supplier counterpart and delivery to a customer counterpart both produce a value event; an internal transfer between two internal locations must not. `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-03` (continuous versus periodic timing) and `JT-04` (recognition trigger) are both open and formally not decidable at present, so R4 may not state when the value is recognised, only that a fact is emitted. |
| Document / event output | Movement facts (`CN-25`); valuation fact (`CN-31`) where applicable; delivery or receipt note. |
| Audit evidence required | Who validated, when, physical effective date **and** entry date as two separate values, quantities demanded versus done, and lot/serial actually moved. R4 emphasises the two-date requirement because `L2-OBS` establishes that in the reference pattern the financial entry date defaults to the date of *processing*, not the date of the physical event — see `19_L13_PLUS_ESCALATION_REGISTER.md` `L13-01`. |

### `INV-F-08` — Handle a shortfall at validation: backorder or close (`INV-M03`)

| Dimension | Finding |
|---|---|
| Trigger | Done quantity is less than demanded quantity at validation. |
| Preconditions | The operation type's backorder policy is set to ask, always create, or never create. |
| Postconditions | Either a follow-up operation exists for the remainder, or the remainder is abandoned and the commitment is closed short. |
| State transition | Original → done; follow-up → waiting, or no follow-up. |
| Quantity impact | Only the done quantity moves. The remainder remains a commitment or ceases to be one. |
| Cost impact | Only on the moved quantity. |
| Document / event output | A follow-up operation, or a closure record. |
| Audit evidence required | The decision taken, by whom, and the resulting commitment position communicated back to Sale or Purchase (`HO-02`, `HO-05`). A silently abandoned remainder is a customer-promise failure that leaves no trace, so the closure decision must be an explicit recorded act. |

### `INV-F-09` — Handle over-delivery or over-receipt (`INV-M03`)

| Dimension | Finding |
|---|---|
| Trigger | Done quantity exceeds demanded quantity. |
| Preconditions | A tolerance policy exists, or the excess is refused. |
| Postconditions | Either the excess is accepted and moved, or it is refused. |
| State transition | As `INV-F-07`. |
| Quantity impact | The full done quantity moves if accepted. |
| Cost impact | On the accepted quantity. |
| Document / event output | Movement facts plus an exception record. |
| Audit evidence required | Threshold applied, approver where the threshold was exceeded, and notification to Purchase or Sale. `GAP-FS-16` / `GAP-MD-06` (over-receipt tolerance policy — threshold and approver) remains **open and unresolved**. R4 does not set the threshold; that is a business policy decision requiring Thai SME input. |

### `INV-F-10` — Cancel an operation before execution (`INV-M03`)

| Dimension | Finding |
|---|---|
| Trigger | The originating commitment is cancelled or reduced. |
| Preconditions | The operation is not yet done. |
| Postconditions | Reservations released; the operation is cancelled. |
| State transition | Draft / waiting / ready → cancelled. |
| Quantity impact | None to on-hand; **available increases** as reservations release. |
| Cost impact | None. |
| Document / event output | Cancellation record. |
| Audit evidence required | Who cancelled, why, and what was released. **`RISK-C01` / `C-01` / `MOV-31` — cancellation-cascade symmetry between the sales side and the purchase side — remains a preserved, unarbitrated conflict.** Two prior passes disagreed: one classified it partially verified, the other closed with evidence. R4 does not arbitrate; it records that the asymmetry is still unresolved and that a native re-trace within Inventory Core is the named required action. |

### `INV-F-11` — Return goods after execution (`INV-M03`)

| Dimension | Finding |
|---|---|
| Trigger | A customer returns delivered goods, or the business returns received goods to a supplier. |
| Preconditions | An original completed movement exists to return against; the return quantity does not exceed it. |
| Postconditions | A reversing movement exists, explicitly linked to the original. |
| State transition | New return operation → done. |
| Quantity impact | **Yes** — in the opposite direction to the original. |
| Cost impact | **Yes, and this is the single most material blocked area in the module.** `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-05` / `RISK-C03` / `C-03` / `FIN-DELTA-05` (return cost basis: original issue cost or current cost) is formally **NOT DECIDABLE** with three named missing inputs. The evidence further establishes that under a weighted-average policy the reference system values the return at the *current* average rather than the original cost and does not retroactively rebase, producing a documented discrepancy against the credit note that the reference system's own remedy is a manual adjustment. R4 states the fact and states the consequence — **if the original cost basis is chosen, Inventory must carry per-unit original-cost lineage, which is a data-model requirement, not a report requirement** — and stops there. The choice is Joint. |
| Document / event output | Return movement facts; return valuation fact; linkage to the original movement. |
| Audit evidence required | Original movement identity, return movement identity, the link between them, the cost basis applied, and the three independently settable dates (original sale, physical return, credit note) which the evidence confirms are not forced into alignment. |

### `INV-F-12` — Scrap goods (`INV-M04`)

| Dimension | Finding |
|---|---|
| Trigger | Goods are identified as unusable. |
| Preconditions | Goods exist at the source location; a scrap destination is configured; a reason is supplied. |
| Postconditions | Goods are moved out of usable stock to a loss destination. |
| State transition | `L2-OBS`: **draft → done, with no approval state in between** (finding `R4-F-04`). |
| Quantity impact | **Yes** — usable stock decreases. |
| Cost impact | **Yes.** `DEPENDENCY: ACCOUNTING COGS GAP`. The evidence is that scrap is documented as *not* cost of sales but as a distinct inventory-loss classification reached only through a dedicated loss location kind — and that this is configuration-dependent with **no documented fallback for an unconfigured loss**. Inventory emits the fact and the reason; the classification is Accounting's. |
| Document / event output | Scrap record (`CN-29`); scrap register (`TH-R08`). |
| Audit evidence required | Reason, quantity, lot/serial, authorising person, and — where destruction is claimed for Thai tax purposes — destruction evidence. `TH-HOLD-02` / `GAP-MD-04` (Thai statutory destruction procedure and deductibility evidence) is `HOLD / EVIDENCE REQUIRED` and belongs to the Accounting-Tax track. R4 makes no Thai statutory claim. |

### `INV-F-13` — Recover salvage value from scrapped goods (`INV-M04`)

| Dimension | Finding |
|---|---|
| Trigger | Scrapped goods are sold, recycled, or returned to a supplier for credit. |
| Preconditions | **Undefined — there is no reference pattern.** |
| Postconditions | Undefined. |
| State transition | Undefined. |
| Quantity impact | Undefined — whether salvaged goods re-enter stock as a different item, or leave stock entirely and generate only a financial recovery, is an open design question. |
| Cost impact | `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Undefined. |
| Audit evidence required | Undefined. |
| **R4 finding** | `R4-F-03`. `L2-OBS`: the reference scrap concept carries **no salvage-value field and no salvage-recovery mechanism of any kind**. The Boss-mandated L6 edge case "scrap with salvage value" therefore cannot be answered by transfer from the reference system — it is **original SMEsPlus design work**. This is a genuine R4 gap-fill: prior rounds treated the question as unresearched; R4 establishes that it is unanswerable from the benchmark. Escalated to `L13`. |

### `INV-F-14` — Allocate a landed cost (`INV-M05`)

| Dimension | Finding |
|---|---|
| Trigger | An additional acquisition cost document is received and applied to a target receipt or production order. |
| Preconditions | The target documents exist and are completed; the affected products are under a costing category that carries value in real time; the allocation basis is supplied and the products carry the data that basis needs. |
| Postconditions | The additional cost is distributed across the affected goods; goods still on hand carry a higher value, goods already gone do not. |
| State transition | Draft → done. |
| Quantity impact | **None.** Landed cost changes value, never quantity. This is a point Thai SME users routinely misunderstand and the label must make it explicit (`TH-05` note). |
| Cost impact | **Yes and material.** `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-08` / `LC-06` (landed cost eligibility and posting structure) is open with an **Audit VETO concern retained**, and the evidence records three mutually incompatible reference behaviours for the residual on already-sold goods, one of which is itself a documented failure mode producing no entry at all. The recorded conclusion — which R4 adopts and does not weaken — is that **SMEsPlus must design its own landed-cost-after-sale handling rather than adopt any of the three**. |
| Document / event output | Landed cost allocation (`CN-30`); allocation statement (`TH-R13`); linkage to the cost bill. |
| Audit evidence required | Base amount, allocation basis, per-line allocated amount, which goods were still on hand at allocation time and which had gone, and the cost bill itself. `LC-02` requires the allocation statement to be inspectable *before* validation, not only after. |

### `INV-F-15` — Run the planning engine on demand (`INV-M06`)

| Dimension | Finding |
|---|---|
| Trigger | A user presses run, or the schedule fires. |
| Preconditions | Rules exist; the previous run is not still in progress. |
| Postconditions | Proposals or supply documents exist; a run record exists. |
| State transition | Run started → completed or failed. |
| Quantity impact | None directly. |
| Cost impact | None. |
| Document / event output | Planning-run log (`CN-35`). |
| Audit evidence required | Run identity, scope, start and end, what was created, and whether it overlapped another run. **The precondition "the previous run is not still in progress" has no enforcement in the reference pattern.** `GAP-MD-21` is confirmed by R4 as a real exposure. Escalated to `L15`. |

---

## 3. Product And Master-Data Functions

### `INV-F-16` — Create or amend a product (`INV-M07`)

| Dimension | Finding |
|---|---|
| Trigger | A new item is needed, or an existing item's definition changes. |
| Preconditions | Naming, unit of measure and classification supplied; company or shared scope decided. |
| Postconditions | A master record exists that determines whether any stock behaviour occurs at all. |
| State transition | Draft → active; active → archived. |
| Quantity impact | None on creation. |
| Cost impact | None on creation. |
| Document / event output | Product master (`CN-11`). |
| Audit evidence required | Who created or changed it and what changed. `GAP-FS-04` / `GAP-MD-10` — the tie-break rule when the two-axis stock-control classification is ambiguous — is **unresolved**, and R4 confirms via `L2-OBS` that the two-axis structure persists in the target generation. Real data from an earlier round showed the reference system's own theoretical invariant violated in practice, so the ambiguity is not hypothetical. |

### `INV-F-17` — Change a product's stock-control classification while stock exists (`INV-M07`)

| Dimension | Finding |
|---|---|
| Trigger | A business reclassifies an item, typically from consumable to stock-controlled. |
| Preconditions | `IV-12` requires this to be an approved action. |
| Postconditions | The item begins or ceases to be stock-controlled. |
| State transition | Classification changed. |
| Quantity impact | **Ambiguous and dangerous.** Prior evidence records that promotion backfills history while demotion performs no clean-up. |
| Cost impact | `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | A controlled master-data change record. |
| Audit evidence required | Before and after classification, approver, effective date, and the disposition of any existing balance. R4 records this as one of the functions where the reference pattern is **asymmetric and unsafe in one direction**, and where SMEsPlus must define behaviour rather than inherit it. |

### `INV-F-18` — Generate or amend variants (`INV-M08`, `INV-M25`)

| Dimension | Finding |
|---|---|
| Trigger | Attribute values are added, removed, or the variant-creation mode changes. |
| Preconditions | The variant capability is enabled; attributes are defined. |
| Postconditions | The variant set changes. |
| State transition | Variants created or archived. |
| Quantity impact | **Potentially destructive** — a variant that holds stock and is removed from the matrix leaves stock attached to an identity no longer generated. |
| Cost impact | Follows quantity. `DEPENDENCY: ACCOUNTING COGS GAP` for the valuation consequence. |
| Document / event output | Variant records (`CN-12`). |
| Audit evidence required | The attribute change, the resulting variant delta, and the disposition of any stock on removed variants. `GAP-FS-03` is **unresolved**; `IV-14` (attribute value codes immutable once used) is the containing invariant. |

### `INV-F-19` — Create a batch or serial identity (`INV-M09`)

| Dimension | Finding |
|---|---|
| Trigger | Goods are received or produced under a tracked product. |
| Preconditions | The product's traceability policy requires it; the identifier is unique within its scope. |
| Postconditions | A traceable identity exists and attaches to subsequent movements. |
| State transition | Created → in use → exhausted or archived. |
| Quantity impact | None directly; it partitions quantity. |
| Cost impact | Where batch-level valuation is enabled, the identity becomes a valuation key. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Batch or serial record (`CN-17`, `CN-18`). |
| Audit evidence required | Origin document, supplier batch reference, expiry data, and the uniqueness scope actually applied. **`R4-F-06`** applies here: `L2-OBS` establishes uniqueness is scoped to (identifier, product, company) and that company-less identities are possible, creating a cross-company collision surface. `IV-04` (uniqueness enforced below the application layer) is confirmed as necessary. |

### `INV-F-20` — Amend or merge an existing batch identity (`INV-M09`)

| Dimension | Finding |
|---|---|
| Trigger | A batch was recorded wrongly, or two records represent one physical batch. |
| Preconditions | `IV-13` — a batch's value is immutable after its first movement. |
| Postconditions | Traceability history is rewritten. |
| State transition | Merged or amended. |
| Quantity impact | Balances consolidate. |
| Cost impact | `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | A controlled amendment record. |
| Audit evidence required | Before and after identities, approver, and the affected movement set. This function rewrites the recall chain and is therefore among the highest-control operations in the module. R4 records it as requiring approval by design; no reference pattern is relied upon. |

---

## 4. Reporting Functions

### `INV-F-21` — Derive the current stock position (`INV-M10`, `INV-M11`)

| Dimension | Finding |
|---|---|
| Trigger | A user opens the view or a report is generated. |
| Preconditions | Movement facts exist. |
| Postconditions | A read-only position is presented. |
| State transition | None. |
| Quantity impact | None — `P-03`, on-hand is derived and never edited. |
| Cost impact | None. |
| Document / event output | Stock position (`TH-R01`, `TH-R02`). |
| Audit evidence required | Reproducibility: the same as-of question must give the same answer. `RC-02` (stock card reproducible on demand) is the governing reconciliation requirement. `R4-F-07` applies — a true negative position must be shown as negative, not clamped to zero. |

### `INV-F-22` — Produce the movement history for a product (`INV-M12`)

| Dimension | Finding |
|---|---|
| Trigger | A user or auditor requests the history. |
| Preconditions | Completed movement facts exist. |
| Postconditions | An ordered history with a running balance. |
| State transition | None. |
| Quantity impact | None. |
| Cost impact | None at Inventory; the value column is `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | `TH-R03` `สต็อกการ์ด`. The statutory-style Thai name is `HOLD / EVIDENCE REQUIRED` (`TH-HOLD-01`, `GAP-MD-12`, naming conflict `N-5`) and R4 does not adopt it. |
| Audit evidence required | Immutability, and an explicit, stated ordering rule. `R4-F-08`: ordering by entry sequence and ordering by effective date give different running balances whenever anything is backdated, and backdating is routine in a Thai SME. The report must state which ordering it used. |

### `INV-F-23` — Produce the valuation position (`INV-M14`)

| Dimension | Finding |
|---|---|
| Trigger | Period close, an audit request, or a management query. |
| Preconditions | Valuation facts exist; the costing policy version applicable at the as-of date is known. |
| Postconditions | A value position as of a date. |
| State transition | None. |
| Quantity impact | None. |
| Cost impact | **This function *is* the cost surface.** `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-01`, `JT-02`, `JT-03`, `JT-07` all open, `JT-01` formally not decidable. |
| Document / event output | `TH-R05` valuation as of date; `TH-R06` valuation-to-ledger reconciliation. |
| Audit evidence required | `VR-01` .. `VR-07` carried from v1.0; `IV-10` (valuation as of a date reproducible and agreeing with the ledger after close). R4 adds one requirement from the evidence, which is a disclosure requirement rather than a decision and is therefore not blocked: **any as-of-date reconciliation output must state whether it is measuring at a closing boundary or continuously**, because under a periodic posture the two sides are expected to diverge between closings by design. An unqualified claim that the two balances always match is not supported by any evidence gathered in this programme. |

### `INV-F-24` — Produce warehouse analytics (`INV-M15`)

| Dimension | Finding |
|---|---|
| Trigger | Management request or dashboard refresh. |
| Preconditions | Sufficient movement history. |
| Postconditions | Analytical measures. |
| State transition | None. |
| Quantity impact | None. |
| Cost impact | Value-based measures are `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | `TH-R12`. |
| Audit evidence required | Reconcilability to the operational layer. `GAP-MD-25` / `GAP-FS-13` — the measure set has never been evidenced or validated against what a Thai SME owner actually wants — remains **open**, and this is the one menu R4 leaves genuinely evidence-thin. |

### `INV-F-25` — Export a report (`INV-M12`, `INV-M14`, `INV-M15`)

| Dimension | Finding |
|---|---|
| Trigger | User export request. |
| Preconditions | The report renders on screen. |
| Postconditions | A file matching the on-screen figures. |
| State transition | None. |
| Quantity impact | None. |
| Cost impact | None. |
| Document / event output | Export file. |
| Audit evidence required | `RC-10` — every report export must open correctly and match the on-screen figures. This exists as a reconciliation requirement precisely because `RISK-G7` / `G-7` recorded that the reference reconciliation export was defective in practice. R4 carries it forward as a required acceptance test, not as a resolved item. |

---

## 5. Configuration Functions

### `INV-F-26` — Change a capability switch (`INV-M16`)

| Dimension | Finding |
|---|---|
| Trigger | Implementation decision or a later business change. |
| Preconditions | Understanding of what already-existing data will mean afterwards. |
| Postconditions | Module behaviour changes globally for that company. |
| State transition | Capability on ↔ off. |
| Quantity impact | Indirect but potentially severe — enabling traceability where untracked stock already exists leaves balances with no batch identity. |
| Cost impact | Enabling or disabling valuation changes whether value events are produced at all. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | A versioned configuration record (`CN-34`, `IV-15`). |
| Audit evidence required | Before and after state, approver, effective date, and the disposition of pre-existing data. `GAP-MD-14` (switch-off guards, versioning versus regeneration, `SAAS-04`) **open**. |

### `INV-F-27` — Create or restructure a warehouse (`INV-M17`)

| Dimension | Finding |
|---|---|
| Trigger | A new site, or a change to the operational step model. |
| Preconditions | Company assigned. |
| Postconditions | Locations, operation types and routes are derived or re-derived. |
| State transition | Created, or reconfigured. |
| Quantity impact | None directly; but re-derivation on a live warehouse can re-point future operations. |
| Cost impact | `DEPENDENCY: ACCOUNTING COGS GAP` for warehouse-level valuation separation (`JT-01`). |
| Document / event output | Warehouse record (`CN-02`) and the derived structure. |
| Audit evidence required | What was derived, when, and what it replaced. `L2-OBS` confirms re-derivation on step-configuration change exists in the target generation, which is the `SAAS-04` regeneration risk. `IV-15` (version, never regenerate in place) is the required SMEsPlus divergence. Separately, `GAP-MD-15` / `TH-HOLD-06` — a warehouse must never be equated with a Thai tax branch — remains a hard naming rule and a statutory `HOLD`. |

### `INV-F-28` — Create or change a location, including its kind (`INV-M18`)

| Dimension | Finding |
|---|---|
| Trigger | Storage reorganisation, or a correction. |
| Preconditions | Parent location exists; the kind is chosen deliberately. |
| Postconditions | The structure and the financial semantics of movements through that location are set. |
| State transition | Created, changed, archived. |
| Quantity impact | None directly. |
| Cost impact | **Decisive but indirect.** The location kind is what makes an internal transfer financially neutral (`P-04`). Changing a kind retrospectively re-interprets completed history. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Location record (`CN-03`). |
| Audit evidence required | Before and after kind, approver, effective date, and the movements whose meaning changed. `R4-F-09` applies: a location's company assignment is optional, and a company-less location is the structural mechanism by which cross-company visibility occurs. |

### `INV-F-29` — Change a supply route or rule (`INV-M19`, `INV-M20`)

| Dimension | Finding |
|---|---|
| Trigger | Process redesign. |
| Preconditions | Company consistency between the route and its rules — `L2-OBS` confirms this is genuinely enforced in the reference pattern and is worth transferring. |
| Postconditions | Future generated operations change shape. |
| State transition | Changed. |
| Quantity impact | None retrospectively. |
| Cost impact | A wrong destination can route goods across a valuation boundary unintentionally. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Route and rule records (`CN-05`). |
| Audit evidence required | Before and after definition, approver, effective date, and — critically — the ability to explain any generated operation by naming the rule that created it (`P-06`). R4 records the explainability requirement as mandatory; without it a Thai SME cannot self-diagnose. |

### `INV-F-30` — Change an operation type, including its numbering (`INV-M21`)

| Dimension | Finding |
|---|---|
| Trigger | Process or document-control change. |
| Preconditions | Understanding of the numbering consequence. |
| Postconditions | Future operations inherit the new behaviour and numbering. |
| State transition | Changed. |
| Quantity impact | None. |
| Cost impact | Default locations set here determine the financial character of every operation of that class. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Operation type record (`CN-04`). |
| Audit evidence required | Numbering continuity and non-reuse across the change. `GAP-MD-22` (SoD matrix and Thai document numbering standards) **open**; `TH-HOLD-09` (delivery document to tax invoice linkage and numbering conventions) `HOLD / EVIDENCE REQUIRED`. R4 makes no Thai statutory claim about numbering. |

### `INV-F-31` — Define storage constraints (`INV-M22`)

| Dimension | Finding |
|---|---|
| Trigger | Safety, compliance or capacity requirement. |
| Preconditions | Capability enabled. |
| Postconditions | Put-away decisions become constrained. |
| State transition | Created or changed. |
| Quantity impact | None. |
| Cost impact | None. |
| Document / event output | Storage category record (`CN-06`). |
| Audit evidence required | The constraint and its business or regulatory justification. Thai regulated-storage requirements are `HOLD / EVIDENCE REQUIRED` and route to the legal and Accounting-Tax tracks (`TH-HOLD-08` lineage). |

### `INV-F-32` — Suggest and override a put-away destination (`INV-M23`)

| Dimension | Finding |
|---|---|
| Trigger | Goods are received. |
| Preconditions | Put-away rules exist; storage constraints are satisfiable. |
| Postconditions | A destination is suggested; the operator accepts or overrides. |
| State transition | None on stock until the movement completes. |
| Quantity impact | Determines where quantity lands, not how much. |
| Cost impact | **Must be none** — a put-away must never move goods across a valuation boundary. `DEPENDENCY: ACCOUNTING COGS GAP` to confirm the boundary definition. |
| Document / event output | The destination on the movement. |
| Audit evidence required | Whether the suggestion was accepted or overridden, and by whom. R4 records the override rate as a genuine quality signal worth reporting, and the override itself as mandatory — in most Thai SMEs a wrong suggestion is worse than no suggestion. |

### `INV-F-33` — Assign or change a product category (`INV-M24`)

| Dimension | Finding |
|---|---|
| Trigger | Reporting reorganisation, or a costing policy decision. |
| Preconditions | Awareness that the category carries costing policy, not only grouping. |
| Postconditions | The costing behaviour of every product in the category changes. |
| State transition | Changed. |
| Quantity impact | None. |
| Cost impact | **The highest-blast-radius change in the module.** `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-01` NOT DECIDABLE. `L2-OBS` establishes that costing method and valuation mode are company-scoped properties of the category and that the reference system contains explicit handling for a product moving between categories with different methods, confirming the migration case is real. The evidence adds that a costing-method change does **not** retroactively rebase existing on-hand value, and that this is confirmed only for movement *away from* a standard-cost posture — the reverse and lateral directions remain a `HOLD`. R4 states these facts and makes no policy choice. |
| Document / event output | Category record (`CN-08`); valuation policy (`CN-09`). |
| Audit evidence required | Before and after method, effective date, approver, and the set of products affected. `GAP-FS-02` (is category acceptable as owner of both valuation policy and put-away behaviour, or must they be separated) is precondition-blocked on `JT-01`. |

### `INV-F-34` — Define a packaging (`INV-M26`)

| Dimension | Finding |
|---|---|
| Trigger | A new pack size is bought or sold. |
| Preconditions | Base unit defined. |
| Postconditions | Quantity translation becomes available on documents. |
| State transition | Created or changed. |
| Quantity impact | Indirect but real — a wrong contained quantity produces quantity errors that look like theft. |
| Cost impact | Quantity errors become valuation errors. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Packaging record (`CN-15`). |
| Audit evidence required | Before and after contained quantity, and the historical documents whose interpretation would change. R4 records that changing a contained quantity must not retroactively re-interpret history — the same non-retroactivity principle as `IV-11` for units. |

### `INV-F-35` — Set or maintain a reordering rule (`INV-M27`)

| Dimension | Finding |
|---|---|
| Trigger | Planning parameter decision, or periodic review. |
| Preconditions | Product and location exist. |
| Postconditions | Automatic supply proposals will be generated from these parameters. |
| State transition | Created, changed, suspended, resumed. |
| Quantity impact | None directly; determines future purchasing volume. |
| Cost impact | None directly; determines working capital. |
| Document / event output | Reordering rule record (`CN-20`). |
| Audit evidence required | Parameter values, who set them, and when they were last reviewed. Two R4 findings attach here. `R4-F-01`: the shortfall computation uses the greater of minimum and maximum, so an inverted entry is silently accepted. `R4-F-11`: uniqueness is enforced on (product, location, company) only, so overlapping rules at a parent and a child location are both permitted and both active, and each can raise supply for the same shortfall. Together these make this the highest-value configuration-control target in the module. |

### `INV-F-36` — Define barcode interpretation (`INV-M28`)

| Dimension | Finding |
|---|---|
| Trigger | Scanning is introduced, or a supplier's structured barcodes must be read. |
| Preconditions | Capability enabled; the nomenclature is assigned to the company. |
| Postconditions | All future scans are interpreted by these rules. |
| State transition | Created or changed. |
| Quantity impact | **Direct.** A structured barcode can carry an embedded quantity or weight. |
| Cost impact | A misread quantity becomes a valuation error. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Nomenclature record (`CN-16`). |
| Audit evidence required | Which nomenclature was in force at scan time. `R4-F-12`: a misinterpreted structured barcode produces a plausible but wrong quantity **silently**, which is a worse failure than a rejected scan. R4 records a scan-interpretation confirmation step as a design requirement. |

### `INV-F-37` — Define or change a unit conversion (`INV-M29`)

| Dimension | Finding |
|---|---|
| Trigger | A new trade unit is needed, or a factor was entered wrongly. |
| Preconditions | The unit belongs to one convertible category. |
| Postconditions | Conversion behaviour changes on all future documents. |
| State transition | Created or changed. |
| Quantity impact | **Direct and systemic.** |
| Cost impact | Conversion rounding directly changes valued quantity. `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Unit and category records (`CN-14`). |
| Audit evidence required | `IV-11` — a factor change must never alter historical quantity. `L2-OBS` confirms cross-category conversion is refused outright, which is correct and transferable. `R4-F-13`: the default rounding direction is **upward**, so repeated conversion inflates quantity monotonically and silently. R4 requires the rounding direction to be an explicit, per-category, versioned decision rather than an inherited implicit default. |

---

## 6. Cross-Cutting Functions

### `INV-F-38` — Enforce the period guard (all operational menus)

| Dimension | Finding |
|---|---|
| Trigger | Any function attempting to record a fact with an effective date. |
| Preconditions | A lock date supplied by Accounting (`HO-16`). |
| Postconditions | The fact is accepted, refused, or accepted under a recorded exception. |
| State transition | None on stock. |
| Quantity impact | Gates all of them. |
| Cost impact | `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-12` (period lock policy and exception granting) is in the lane that may be scoped now, but `JT-06` (late supplier bill after close) is gated and the evidence records that the reference system has **no documented prior-period attribution mechanism at all**, making `JT-06` largely original design work. |
| Document / event output | An exception record where an exception is granted. |
| Audit evidence required | `IV-07`: the movement date is in an open period unless a recorded exception exists with a named grantor, a written reason and an expiry. The v1.0 design position — a native guard at both entry and validation, with the global unaudited bypass **rejected as unauditable** — is treated as fixed and is not re-litigated by R4. `RISK-G1G2G3` (`G-1`, `G-2`, `G-3`) remain carried. |

### `INV-F-39` — Emit a fact to Accounting (all value-bearing functions)

| Dimension | Finding |
|---|---|
| Trigger | Any function whose completion produces a financially material fact. |
| Preconditions | All sixteen mandatory handoff data elements are known and evidence-backed, per the Boss-approved Minimum Handoff Data Contract. |
| Postconditions | Accounting has received a complete, idempotent, traceable fact. |
| State transition | Fact emitted; disposition recorded. |
| Quantity impact | None. |
| Cost impact | Inventory emits; Accounting decides. |
| Document / event output | Valuation fact (`CN-31`). |
| Audit evidence required | `RC-09` — every valuation fact received and dispositioned by Accounting each period. The full sixteen-element treatment is in `05_L4_CROSS_MODULE_DEPENDENCY_MAP.md` §4. R4's material observation is that **two of the sixteen elements cannot currently be supplied by Inventory at all**: a deterministic idempotency identity (`RISK-C02` / `IV-06`, no stable identity exists) and a migration or replay batch identity (`GAP-FS-08`, the provenance reference does not exist and must be originated). Both are Lane A — not COGS-gated — so they are actionable now and are R4's highest-leverage non-blocked recommendations. |

### `INV-F-40` — Correct a completed fact (all operational menus)

| Dimension | Finding |
|---|---|
| Trigger | An error is discovered after completion. |
| Preconditions | `P-02` / `IV-05` — the original is immutable. |
| Postconditions | A reversing fact exists, linked to the original, plus a corrected fact where appropriate. |
| State transition | New facts; the original unchanged. |
| Quantity impact | Net of the reversal and the correction. |
| Cost impact | `DEPENDENCY: ACCOUNTING COGS GAP`. |
| Document / event output | Reversal and correction facts with explicit linkage. |
| Audit evidence required | Original identity, reversal identity, correction identity, reason, approver, and both dates. The handoff contract requires the reversal-to-original link explicitly; a scenario cannot be treated as proven where that link cannot be made. |

### `INV-F-41` — Establish opening balances at cutover (`INV-M02`, migration)

| Dimension | Finding |
|---|---|
| Trigger | Go-live. |
| Preconditions | A certified opening position agreed with the accountant. |
| Postconditions | Stock exists in SMEsPlus with a stated origin. |
| State transition | — → opening balance established. |
| Quantity impact | **Yes — the entire starting position.** |
| Cost impact | **Yes.** `DEPENDENCY: ACCOUNTING COGS GAP` — `JT-11` / `G-5` / `GAP-FS-09` (opening balance certification). |
| Document / event output | Opening balance (`CN-33`); provenance reference (`CN-36`). |
| Audit evidence required | `RC-08` — the opening balance agrees with the accountant's opening trial balance, with **human certification**, once, at cutover. Prior evidence describes this as the single highest fabrication-risk point in the whole Inventory scope, because no reference mechanism exists to copy. R4 confirms it is unresolved and that `GAP-FS-08` (the provenance reference does not exist) is its precondition. |

---

## 7. L3 Coverage Result

| Measure | Result |
|---|---:|
| Functions given full eight-dimension L3 treatment | 41 of 41 |
| Functions with a quantity impact | 17 |
| Functions with a cost impact | 24 |
| Functions carrying `DEPENDENCY: ACCOUNTING COGS GAP` | 24 |
| Functions where **no reference pattern exists** and SMEsPlus must originate the design | 4 — `INV-F-13`, `INV-F-38` (late-period attribution aspect), `INV-F-39` (idempotency and provenance elements), `INV-F-41` |
| Functions where the reference pattern exists but is recorded as **unsafe to inherit** | 5 — `INV-F-03`/`INV-F-04` (count as balance attribute, no approval state), `INV-F-12` (no approval state), `INV-F-14` (three incompatible residual behaviours, one a failure mode), `INV-F-17` (asymmetric reclassification) |
| Functions closed by this session | **0** |

---

## 8. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
