# 05 — Inventory Process Flow Catalog v1.0

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V1-001` | Jira: `ERPPLUS-139`
Status: `SMEsPlus-OWNED PROCESS DESIGN — CANDIDATE — NOT APPROVED, NOT A SCREEN DESIGN`
Clean-room: Layer 1. Flows describe *what happens and who does it*, never how a screen works and never any reference-ERP mechanism.

---

## 1. Flow Index

| Flow | Name | Primary menus | Emits accounting facts |
|---|---|---|---|
| `FL-01` | Purchase receipt to stock | OP-03, CF-06, CF-08 | Yes |
| `FL-02` | Stock to customer delivery | OP-03, PR-03 | Yes |
| `FL-03` | Internal movement between places | OP-03, CF-03 | No |
| `FL-04` | Warehouse-to-warehouse resupply via transit | OP-03, CF-04 | No (unless cross-company) |
| `FL-05` | Customer return inbound | OP-03 | Yes |
| `FL-06` | Supplier return outbound | OP-03 | Yes |
| `FL-07` | Physical count and adjustment | OP-02 | Yes |
| `FL-08` | Scrap and disposal | OP-04 | Yes |
| `FL-09` | Replenishment planning | OP-01, OP-06, CF-12 | No |
| `FL-10` | Landed cost allocation | OP-05 | Yes (value only) |
| `FL-11` | Lot / serial traceability and expiry | PR-03 | No |
| `FL-12` | Period-end valuation and reconciliation | RP-05 | Joint |
| `FL-13` | Migration cutover and opening balance | OP-02, RP-03 | Joint |
| `FL-14` | Barcode-driven scan operations | CF-13, OP-03, OP-02 | Indirect |

---

## 2. Structural Basis of Every Flow

Every flow below is built from one primitive: **a movement fact from a source place to a destination place**. The five internal location roles used in these flows — main stock, receiving holding, quality check, shipping staging, packing — are **benchmark-derived and unvalidated**, described in prose rather than any path notation, and which of them Thai SME warehouses actually use, under what names, is `UNKNOWN / EVIDENCE REQUIRED` pending Thai field input. This restates the correction already applied on the authoritative containment branch and does not weaken it.

---

## 3. The Flows

### FL-01 — Purchase receipt to stock

**Trigger.** A purchase order is confirmed by the Purchase domain.

**Steps.**
1. Purchase hands over the expected receipt: product, quantity, expected date, supplier, price reference.
2. Inventory creates a receipt document of the warehouse's inbound document type, with the numbering series of that type.
3. Goods physically arrive. The receiver opens the document and enters or scans actual quantities, and lot or serial values where the product is tracked, and expiry dates where the product has an expiry policy.
4. Where the warehouse uses a two- or three-step receipt, goods first land in the receiving holding area and, if required, the quality-check area, before moving on to main stock; each step is its own movement.
5. Put-away suggests a destination place; the receiver may override with a recorded reason.
6. Quantity differences are resolved explicitly: short receipt creates a backorder or closes the line with a reason; over-receipt beyond tolerance requires approval.
7. The receiver validates. Movement facts become done and immutable.
8. Inventory returns received quantities to Purchase for matching, and emits a receipt valuation fact to Accounting.

**Exceptions.** Goods arrive without a purchase order; goods arrive damaged; supplier ships a different pack size; lot value duplicates an existing lot; the movement date falls in a closed period; the same document is validated twice.

**Controls.** Validator ≠ order approver; tolerance approval; period guard; duplicate-validation refusal; put-away override recorded.

---

### FL-02 — Stock to customer delivery

**Trigger.** A sales order is confirmed by the Sales domain.

**Steps.**
1. Sales hands over the demand: product, quantity, requested date, customer, destination, priority.
2. Inventory creates a delivery document and reserves stock according to the tenant's reservation policy.
3. Where the warehouse uses a two- or three-step delivery, the goods are picked to the packing area and then the shipping staging area before dispatch; each step is a movement.
4. For tracked products the system proposes lots oldest-expiry-first (or oldest-received-first where expiry is not tracked); an override requires a reason, and shipping an expired lot is blocked unless explicitly overridden and approved.
5. Short availability forces an explicit decision: partial ship with a backorder, or hold.
6. The operator validates the dispatch. Movement facts become done.
7. Inventory notifies Sales of delivered quantities and lots, and emits a cost-of-goods-sold fact to Accounting.

**Exceptions.** Reserved stock is physically missing; the customer refuses delivery at the door; the order is cancelled after picking; a serial is scanned that was already shipped.

**Controls.** Reservation cannot exceed available; expiry block; separation between picker and validator where tenant size allows; period guard. **Open:** whether cost of goods sold is recognised at dispatch or at invoice is a Joint Accounting ↔ Inventory decision, unresolved.

---

### FL-03 — Internal movement between places

**Trigger.** A supervisor moves goods within one warehouse — reorganising shelves, moving to a cold room, consolidating a part-used pallet.

**Steps.** Create an internal document → select source and destination places → confirm quantities and lots → validate → movement facts recorded.

**Exceptions.** Destination is a grouping node or a non-internal counterpart place (refused); destination is over capacity (advisory warning only); goods moved physically but never recorded, discovered later at count.

**Controls.** Both ends must be internal places of the same company. **Accounting impact: none** — this movement changes where stock is, not whether the company owns it.

---

### FL-04 — Warehouse-to-warehouse resupply via transit

**Trigger.** A branch warehouse falls below its reorder point, or a supervisor requests stock from the main warehouse.

**Steps.** Source warehouse issues to the in-transit place → goods physically travel → destination warehouse receives from in-transit → transit balance returns to zero.

**Exceptions.** Goods dispatched but never received — stranded transit, which must be aged and reported; quantity received differs from quantity sent; the transfer crosses a company boundary, in which case it is not one transfer but a sale and a purchase between two companies.

**Controls.** Transit is never allowed to age silently — an open transit report is mandatory; a cross-company transfer must be recognised as such and routed to the Joint Accounting ↔ Inventory design, because inter-company invoicing applies. **Carried gap:** the cross-company path was never traced end to end in the evidence chain (`GAP-FS-07`).

---

### FL-05 — Customer return inbound

**Trigger.** A customer returns goods.

**Steps.** A return document is created, referencing the original delivery where one exists → the return reason is recorded → goods are inspected on arrival → good stock returns to main stock; unusable stock goes to a quarantine place and then to `FL-08` → movement facts are emitted with a reference to the original delivery.

**Controls.** The return must carry a reason from a controlled list; inspection outcome is recorded per line; a return without an original delivery reference is permitted but flagged.

**Accounting-Control Impact.** A reversing valuation fact is emitted. **The cost basis of a returned item — the original issue cost, or the current cost — is a carried conflict (`C-03`) and is not resolved by this session.**

---

### FL-06 — Supplier return outbound

**Trigger.** Goods are rejected at inspection, or a supplier agrees to take goods back.

**Steps.** A return document referencing the original receipt → approval → goods move from their internal place to the supplier counterpart → Purchase is notified for credit note handling → a reversing receipt valuation fact is emitted.

**Controls.** Approval required; reason mandatory; the returned quantity may not exceed the received quantity net of prior returns.

---

### FL-07 — Physical count and adjustment

**Trigger.** A cycle-count schedule, a discovered discrepancy, a year-end count, or a migration cutover.

**Steps.**
1. Plan the count: scope, date, counters, and the freeze policy for the counted area.
2. Generate count sheets — on paper or on a scanner — showing what to count and, where policy requires a blind count, *not* showing the system quantity.
3. Count. Record counted quantity per product, place and lot.
4. Compare against the system position. Every difference above the recount threshold is recounted before it is accepted.
5. Submit for approval with a reason per difference.
6. On approval, each difference is applied as a movement between the counted place and the adjustment counterpart.
7. Publish the adjustment register entry and emit the gain or loss fact.

**Exceptions.** Goods are received or dispatched during the count; a count sheet is applied days late and no longer reflects reality; a difference is backdated into a closed period; a large difference is split into several small ones to avoid the escalation threshold.

**Controls.** Counter ≠ approver; stale counts expire and must be recounted rather than applied; value escalation thresholds with anti-splitting detection; period guard; witnessed count at year end. **Open:** which freeze policy Thai SMEs can actually operate — full stop, area freeze, snapshot with reconciliation, or no freeze with movement capture — is `UNVALIDATED - THAI USER REVIEW REQUIRED`. **The statutory expectations around a witnessed annual count are `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.**

---

### FL-08 — Scrap and disposal

**Trigger.** Damage, expiry, loss, or a failed inspection.

**Steps.** Identify and quarantine → raise a scrap request with reason and evidence → approve, escalating by value, with a witness where a formal destruction procedure applies → move from the internal place to the loss counterpart → record physical disposal → publish the scrap register entry with its evidence pack → emit the loss fact.

**Exceptions.** Theft concealed as damage; sellable goods scrapped to clear space; disposal recorded with no evidence; scrap dated into a closed period.

**Controls.** Requester ≠ approver; controlled reason list; value escalation; evidence attachment; witness record; period guard; scrap trend by reason monitored as a fraud indicator. **The Thai tax treatment of scrapped goods and the destruction procedure required to support it are `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.**

---

### FL-09 — Replenishment planning

**Trigger.** The scheduled planning run, a sales order confirmation, or a manual "plan now".

**Steps.** For each active rule, compute the forecast position → compare to the minimum → propose a quantity that restores the maximum, rounded to the supplier's multiple → attach an explanation → present for review → the buyer confirms, edits or rejects with a reason → confirmed proposals become purchase, manufacturing or transfer documents in their owning domain.

**Exceptions.** A retried run creates a second proposal for the same shortfall; the forecast ignores demand that is not yet confirmed; the minimum is expressed in one unit and read in another; a rule points at an archived product.

**Controls.** Demand identity makes the run idempotent (`C-02`, Boss decision); confirming a proposal is not order approval; every run is logged, including empty runs; explanations are mandatory.

---

### FL-10 — Landed cost allocation

**Trigger.** A freight, duty, insurance or broker bill is posted by Accounting and relates to received goods.

**Steps.** Accounting hands over the cost bill with its cost type → the user selects the target receipts → enters cost lines → chooses an allocation basis per line (value, quantity, weight, volume, or explicit) → reviews the computed allocation → validates → the cost basis of the affected receipt lines increases and value-change facts are emitted.

**Exceptions.** Some or all of the goods have already been sold, so there is no remaining stock to carry the cost; the same bill is allocated twice; the products use a costing method for which a retrospective cost change is not meaningful; the bill arrives after the period is closed.

**Controls.** Accounting approval; one allocation per bill per receipt line; explicit handling — never silent — where goods are already sold; period guard. **Open (Joint):** eligibility rules and posting structure. **`HOLD / EVIDENCE REQUIRED` (Accounting-Tax track):** Thai import duty and import VAT treatment, including whether recoverable input VAT must be excluded from landed cost.

---

### FL-11 — Lot / serial traceability and expiry

**Trigger.** A recall notice, a customer complaint, a warranty claim, or a scheduled expiry review.

**Steps.**
- *Forward trace:* from a lot, list every delivery that contained it and every customer who received it.
- *Backward trace:* from a customer document or a serial, identify the receipt, the supplier, and the batch.
- *Expiry review:* list lots reaching their expiry horizon, with quantity and place, so the business can sell them first, discount them, or scrap them.

**Controls.** Traceability must be answerable within the tenant's own data with no manual reconstruction; serial uniqueness is enforced at the data layer; expiry alerts have a configurable horizon; shipping an expired lot is blocked absent an approved override.

---

### FL-12 — Period-end valuation and reconciliation

**Trigger.** Accounting closes a period.

**Steps.** Accounting supplies the lock date → Inventory refuses new movements dated into the locked period except through a recorded exception → Inventory computes the valuation as of the period end under the stated policy → Inventory presents the movement of value for the period (opening, receipts, issues, adjustments, scrap, landed cost, closing) → Accounting compares to the ledger and works the reconciling items → Accounting posts and closes.

**Exceptions.** A supplier bill arrives after the close and changes a cost basis inside the closed period; an adjustment is approved after the cut-off; the valuation figure is not reproducible when re-run.

**Controls.** Native Inventory period guard, independent of any accounting bridge; the costing policy and its version are printed on the report; the figure is reproducible; the export is acceptance-tested. **Blocking (Joint):** the ownership of valuation policy, the design of the close, and the treatment of late bills are unresolved and this flow cannot be finalised without them.

---

### FL-13 — Migration cutover and opening balance

**Trigger.** A tenant goes live.

**Steps.** Load master data with a provenance reference from every legacy record to its SMEsPlus record → load either the full movement history or a certified opening balance plus history from the cutover date → replay history with a stable identity so a re-run duplicates nothing → produce the opening balance as a count-and-adjustment against a zero start, so that cutover stock enters through the same audited path as any other adjustment → certify the opening quantity and value against the accountant's opening trial balance, with a human sign-off.

**Exceptions.** Legacy records that violate a SMEsPlus invariant (a service item holding stock, a duplicate serial, a unit with no group); a replay that runs twice; an opening value that does not agree with the ledger.

**Controls.** Provenance is mandatory and does not exist today — it must be designed as a first-class migration component (`GAP-FS-08`); the opening balance requires human certification (`G-5`); reconciliation reports run before, and again after, cutover.

---

### FL-14 — Barcode-driven scan operations

**Trigger.** A worker scans a label during receiving, picking, counting or put-away.

**Steps.** The scan is matched against the configured formats in priority order → the first match resolves the product, variant, pack, batch or embedded quantity → the resolved value is applied to the document line in context → an unmatched scan is refused with a readable message.

**Exceptions.** Overlapping formats resolve the same label two ways; a weight-embedded label is read as a plain article code; a pack label is applied as a single unit.

**Controls.** Overlapping patterns are detected at configuration time; unmatched scans are logged and reviewed; the resolved interpretation is shown to the worker before it is committed.

---

## 4. Exception Grammar (applies across all flows)

| Exception class | Rule |
|---|---|
| Quantity short | Always an explicit decision — backorder or close with reason. Never silent. |
| Quantity over | Tolerance-checked; beyond tolerance requires approval. |
| Wrong identity (lot, serial, variant) | Refused at entry where detectable; corrected by reversal where discovered later. |
| Timing (closed period) | Refused natively by Inventory; exception path names grantor, reason and expiry. |
| Duplication (retry, double-validate, double-allocate) | Prevented by a stable identity, never repaired after the fact. |
| Physical reality differs from the record | Recorded as a count and adjustment with a reason, never as a silent edit. |
| Automatic decision the user disagrees with | Overridable, with the override and its reason recorded. |

---

## 5. UAT-Ready Business Scenarios

Each scenario below is written so that a Thai SME user could execute it and judge the result without reading any design document. All are `UNVALIDATED - THAI USER REVIEW REQUIRED` until a real Thai user has walked them.

| # | Scenario | Expected outcome |
|---|---|---|
| `UAT-01` | Receive 100 pieces against a purchase order for 120, in one step. | Receipt of 100 done; backorder of 20 created; on-hand +100; one receipt valuation fact. |
| `UAT-02` | Receive 10 cartons of an item defined as 12 pieces per carton. | On-hand increases by 120 pieces; the document shows 10 cartons handled; no second conversion applied. |
| `UAT-03` | Receive a batch-tracked item with an expiry date, then try to ship an expired batch. | Receipt records batch and expiry; shipment of the expired batch is blocked and requires an approved override. |
| `UAT-04` | Deliver 5 of an item with 3 available. | Short availability forces an explicit partial-or-hold decision; no negative on-hand is created silently. |
| `UAT-05` | Move 20 pieces from the main stock area to a cold room. | On-hand per place changes; total on-hand unchanged; no accounting fact emitted. |
| `UAT-06` | Send 50 pieces from the main warehouse to a branch warehouse. | Transit shows 50 in flight; branch receipt clears transit to zero; no valuation fact for a same-company move. |
| `UAT-07` | Count a shelf, find 3 fewer than the system says, and approve the difference. | Adjustment applied as a movement with a reason and an approver; register entry created; loss fact emitted; counter could not self-approve. |
| `UAT-08` | Attempt to backdate that adjustment into last month, which is closed. | Refused, with a readable message and a named exception path. |
| `UAT-09` | Scrap 2 damaged pieces with photographic evidence, above the escalation threshold. | Escalated to the higher approver; scrap register entry with evidence; loss fact emitted. |
| `UAT-10` | Let a reorder rule with a minimum of 50 fire when the forecast is 12. | One proposal, with a readable explanation; re-running the planning task creates no second proposal. |
| `UAT-11` | Allocate a freight bill across two receipts by value. | Allocation statement shows the basis and the amount per line; cost basis increases; value-change facts emitted; a second allocation of the same bill is refused. |
| `UAT-12` | Run the valuation report for last month, twice. | Identical figures both times; the costing policy and version are printed on the report; the export opens correctly. |
| `UAT-13` | Trace a batch from receipt to every customer who received it. | Complete forward trace with no manual reconstruction. |
| `UAT-14` | Scan a pack label at the receiving dock. | The pack is resolved, the base quantity is computed once, and the interpretation is shown before it is committed. |
| `UAT-15` | Attempt to archive a storage place that still holds stock. | Refused, naming what is blocking it. |
| `UAT-16` | Change a unit conversion factor and re-run last month's stock card. | Historical quantities are unchanged; the new factor applies only from its effective date. |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
