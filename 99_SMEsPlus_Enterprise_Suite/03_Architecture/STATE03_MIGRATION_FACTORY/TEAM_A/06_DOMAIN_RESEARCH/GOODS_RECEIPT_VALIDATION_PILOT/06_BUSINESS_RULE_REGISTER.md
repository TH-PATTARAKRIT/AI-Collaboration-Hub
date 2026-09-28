> Domain: GOODS_RECEIPT_VALIDATION_PILOT | Business Trace (Master Prompt §3, §6.3) | Documentation-Tier | Allowed output language only: WHAT / WHY / BUSINESS RULE / STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT / RISK / UNKNOWN

# 06 — BUSINESS RULE REGISTER (Business Trace per Function)

Evidence tier for every row below: **Documentation Evidence** (Odoo 19 official documentation, retrieved via search this session). See `19_PROVENANCE_REGISTER.md` for exact URLs. None of this is Source or Runtime Evidence.

---

### GRV-F01 — Receipt routing configuration

- **WHAT**: A warehouse may be configured to receive goods in one, two, or three physical steps between the vendor and stock.
- **WHY**: Different warehouses need different controls before stock becomes usable — e.g. a cold-storage or quality-sensitive operation wants an intermediate holding/inspection step before goods count as available stock.
- **BUSINESS RULE**: The number of steps is a warehouse-level configuration choice, not a per-transaction choice.
- **STATE**: Configuration is set once and applies to subsequent receipts at that warehouse until changed.
- **DATA CONCEPT**: A receipt is a movement instruction between named location roles (vendor location → intermediate input/quality location(s) → internal stock location).
- **CONTROL**: Enabling multi-step routing is itself gated behind a platform/module-level feature toggle.
- **DEPENDENCY**: GRV-F02 (physical execution) behaves differently depending on this configuration.
- **EVENT**: None documented at this evidence tier beyond "configuration changed."
- **RISK**: Misconfigured routing could let goods post as available stock before an intended inspection step — a control-design consideration for SMEsPlus, not a copied mechanism.
- **UNKNOWN**: Whether the step count can be overridden per-transaction or per-vendor is not evidenced this round — `RUNTIME/SOURCE VERIFICATION REQUIRED`.

---

### GRV-F02 — Physical receipt execution

- **WHAT**: A user confirms ("validates") that a quantity of goods has physically arrived, moving that quantity from a vendor-owned location into a stock-owned (or intermediate) location.
- **WHY**: The business needs a single, deliberate act that converts "expected" goods into "on-hand" stock, so downstream functions (availability, valuation, billing) have a trustworthy trigger.
- **BUSINESS RULE**: Validation is a discrete, user- or system-triggered action; it is not implied by the mere existence of a purchase order.
- **STATE**: Draft/expected → (in-progress, if multi-step) → done. A "done" receipt is the Stock Truth fact.
- **DATA CONCEPT**: The receipt record carries an ordered/expected quantity and a received/actual quantity, which may differ.
- **CONTROL**: Only a validated (done) receipt is treated as an authoritative movement; unvalidated records carry no stock or financial effect.
- **DEPENDENCY**: Feeds GRV-F04 (valuation) and GRV-F06 (bill control) once done.
- **EVENT**: "Receipt validated" is the material business event this pilot treats as the trigger point.
- **RISK**: A validated receipt with an incorrect quantity propagates an incorrect Stock Truth fact into valuation and billing.
- **UNKNOWN**: Exact system-level guard conditions (e.g. can a receipt be validated twice, what prevents double-processing) — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

---

### GRV-F03 — Partial receipt / backorder handling

- **WHAT**: When the received quantity is less than the ordered/expected quantity, the shortfall can be recorded as a separate, linked follow-up movement (a "backorder") rather than being silently lost or blocking the whole receipt.
- **WHY**: Real-world deliveries are frequently partial; the business needs to accept and value what did arrive without waiting for the rest, while not losing track of the remainder.
- **BUSINESS RULE**: Per documentation, creating the backorder follows from a user action (editing the received quantity, then validating) — it is not described as a silent, no-action-required automatic split.
- **STATE**: Original receipt → done (for the received portion) + a new linked record in draft/expected state for the remaining quantity.
- **DATA CONCEPT**: Backorder record retains a link/provenance back to the originating receipt and purchase order.
- **CONTROL**: The user can also explicitly split a line, provided the split quantity does not exceed the demand quantity.
- **DEPENDENCY**: GRV-F04/F06 must treat the partial "done" quantity as the valid financial-control input, not the original ordered quantity — this directly conditions GRV-F06's "received quantities" bill-control policy (see below).
- **EVENT**: "Backorder created."
- **RISK**: If a design silently assumes ordered quantity == received quantity, partial receipts will cause valuation and bill-control errors.
- **UNKNOWN**: Whether a backorder can itself be partially received again (recursive backorder), and any limit on repeated splits — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

---

### GRV-F04 — Inventory valuation at receipt

> **RESOLUTION UPDATE (2026-09-28, Gx6).** The claim below (generic "perpetual valuation posts in real time whenever stock enters/leaves") is superseded by more specific, convergent evidence found in Gx2 and Gx6: **in Odoo 19, journal entries post at invoice/bill time, not at movement time; a month-end Stock Closing + accrual mechanism sweeps up anything not yet invoiced by period end.** This original text is kept as-is (not deleted) per this Deep Study's carry-forward discipline — treat the finding below as the *documentation-tier starting point* this Deep Study began from, and `PERIOD_CUTOFF_VALIDATION_PILOT/06_BUSINESS_RULE_REGISTER.md` `PCO-F03` as the current best understanding. AWT (queued, shared session) still formally confirms this at runtime.

- **WHAT**: A receipt may or may not immediately create an accounting-relevant value entry, depending on whether the business uses "automatic/perpetual" or "manual/periodic" valuation; where a value is computed, the costing method (documented: FIFO, AVCO, Standard-equivalent) determines the amount.
- **WHY**: Businesses differ in whether they want real-time financial visibility of stock movements (perpetual) versus a simpler periodic reconciliation done by the accounting team (periodic); costing method reflects different cost-accounting policies.
- **BUSINESS RULE**: Documentation states the default is manual/periodic valuation — i.e., **the accounting team, not the receipt action itself, posts the journal entry** under the default configuration. Automatic/perpetual valuation is an explicit configuration choice that makes the receipt itself create a real-time journal entry.
- **STATE**: Under FIFO, each incoming lot's value is tracked individually ("remaining units from each previous incoming move retain their own individual valuation") rather than being blended into a single average immediately.
- **DATA CONCEPT**: A received quantity carries a unit cost; under FIFO/AVCO that cost can later be explicitly adjusted ("Adjust Valuation" action) rather than being immutable.
- **CONTROL**: Whether a receipt has an immediate GL effect is entirely a configuration fact (valuation method), not a universal behavior — **a design must not assume perpetual valuation as the default**.
- **DEPENDENCY**: GRV-F05 (landed cost) and GRV-F06 (bill control) both interact with whichever valuation mode is active.
- **EVENT**: "Valuation posted" (perpetual mode) vs "no immediate financial event" (periodic mode, deferred to manual posting).
- **RISK**: A design that hard-codes "receipt = immediate GL entry" would be materially wrong for any business using the periodic/manual default.
- **UNKNOWN**: Exact account structure (stock valuation account, interim/clearing accounts) was not independently fetched this round (direct page fetch was blocked by network egress policy; only a search-engine summary was obtained) — `SOURCE VERIFICATION REQUIRED`, see GAP-GRV-04.

---

### GRV-F05 — Landed cost allocation onto received goods

- **WHAT**: Additional costs incurred to bring goods to a usable/sellable state (e.g. freight, duty) can be allocated onto the value of already-received stock, adjusting its recorded cost.
- **WHY**: The "true" cost of inventory is more than the vendor's unit price; businesses need this reflected in valuation and later COGS.
- **BUSINESS RULE (material finding — see CQS-GRV-03)**: Eligibility is gated by the **product's costing method** being FIFO or AVCO (documentation explicitly excludes a Standard-costing-method product category from this path) — **not** by whether valuation is automatic or manual. Documentation states landed cost "can be manual or automatic" valuation, "as long as the costing method is FIFO or AVCO."
- **STATE**: Original receipt valuation → landed-cost document applied → adjusted valuation.
- **DATA CONCEPT**: A landed-cost allocation references one or more prior receipts and distributes an additional amount across their valued quantities.
- **CONTROL**: The gating condition (costing method) is a product/category-level setting, checked at landed-cost application time, not at receipt time.
- **DEPENDENCY**: Depends on GRV-F04 having already established a per-lot valuation to adjust.
- **EVENT**: "Landed cost applied / valuation adjusted."
- **RISK**: A design assuming landed costs require perpetual valuation would incorrectly block a valid manual-valuation + FIFO/AVCO business from using this control.
- **UNKNOWN**: Exact allocation method across multiple receipt lines (by quantity, by value, by weight, etc.) — `SOURCE VERIFICATION REQUIRED`.

---

### GRV-F06 — Three-way match / bill control policy

- **WHAT**: A vendor bill can be gated so that it is only created/payable in reference to quantities actually received (as opposed to quantities merely ordered), and an explicit three-way-matching feature layers a "should this be paid" signal on top.
- **WHY**: Prevents paying for goods not yet received and provides a documented audit signal when a bill's content no longer matches what was actually ordered/received.
- **BUSINESS RULE**: Bill Control Policy has (at least) two documented modes — "ordered quantities" (bill draftable immediately on PO confirmation) and "received quantities" (bill draftable only once some/all quantity is received). Three-way matching is explicitly documented as **only functioning when the policy is set to "received quantities."**
- **STATE**: Vendor bill carries a `Should Be Paid` field, defaulting to `Yes` when validly created against received quantity; editing a draft bill's quantity/price/products after creation moves this field to `Exception` rather than blocking the edit.
- **DATA CONCEPT**: The bill's "should be paid" status is a **derived signal**, distinct from the bill's own draft/posted/paid lifecycle state.
- **CONTROL**: Per documentation, this is described as a soft, informational control — "Odoo notices the discrepancy, but does not block the changes or display an error message." This is a material control-design nuance: **it is not evidenced as a hard payment block.**
- **DEPENDENCY**: Directly depends on GRV-F02/F03's received-quantity fact; only meaningful under the "received quantities" Bill Control Policy.
- **EVENT**: "Bill exception flagged" (informational, not blocking, per documentation).
- **RISK**: A design assuming three-way matching is a hard block on payment (rather than an informational flag per the documentation) would overstate the strength of this control — must be confirmed against runtime before being relied on as a hard control in any target design.
- **UNKNOWN**: Whether a downstream payment-execution step enforces a hard check on this flag (as opposed to the bill-editing step described) is not evidenced — `RUNTIME VERIFICATION REQUIRED`, see CQS-GRV-04.

---

### GRV-F07 — Reversal / return of received goods

> **Evidence added 2026-09-28 (continuous execution, closing the documentation half of `GAP-GRV-06`).** Odoo's documentation does not have a page dedicated to "return goods to vendor" distinct from the sales-side one — the mechanism is the same generic **Reverse Transfer** applied to a validated receipt instead of a validated delivery, mirrored on the financial side by a **Vendor Refund / Vendor Credit Note** instead of a Customer Credit Note. This symmetry with `SALES_DELIVERY_VALIDATION_PILOT` SDV-F06/F07 is itself the finding.

- **WHAT**: Before a vendor bill is validated for the returned quantity, a return to the vendor is processed via Reverse Transfer on the original receipt. After a vendor bill has been validated, the bill cannot be edited — a Vendor Refund / Vendor Credit Note is the documented instrument for the financial correction.
- **WHY**: Same rationale as the sales-side mirror: once a financial document is validated it must not be silently edited, so a dedicated reversal instrument exists for both directions of trade.
- **BUSINESS RULE**: A credit/debit note is documented as "the only legal method for canceling, refunding, or modifying a validated invoice" — stated in the customer-invoice context, structurally symmetric with the vendor-bill side, where the vendor bill's own "Credit Note" button and the "Vendors → Refunds" list are the documented equivalent instrument.
- **STATE**: Validated receipt (pre-bill) → Reverse Transfer → validated → PO's received-quantity reduced. Validated receipt + validated bill (post-bill) → Reverse Transfer (stock) + Vendor Refund/Credit Note (financial), both required.
- **DATA CONCEPT**: Symmetric with `SDV-F06`/`SDV-F07` — two separate instruments (one Stock Truth, one Financial Truth), not a single combined "undo."
- **CONTROL**: The financial correction instrument (Vendor Refund/Credit Note) is distinct from, and does not by itself imply, the stock-level reversal — both must be done for a post-bill return.
- **DEPENDENCY**: Depends on `GRV-F02` (the original receipt) and, for the post-bill case, `GRV-F06` (three-way match / bill control) having already run.
- **EVENT**: "Return validated" (stock) + "Vendor refund/credit note issued" (financial, post-bill case only).
- **RISK**: A design providing only inventory-level reversal for post-bill vendor returns would be incomplete, exactly as flagged for the sales side in `SDV-F07`.
- **UNKNOWN**: Whether "Purchase matching" (the OCR-digitized-bill-to-PO matching feature documented for ordinary vendor bills) plays any role in reconciling a returned quantity against a partially-matched bill — not evidenced this round; whether the vendor refund amount auto-derives from the original bill/valuation or requires manual entry (mirrors `GAP-SDV-05`) — `SOURCE/RUNTIME VERIFICATION REQUIRED`.
