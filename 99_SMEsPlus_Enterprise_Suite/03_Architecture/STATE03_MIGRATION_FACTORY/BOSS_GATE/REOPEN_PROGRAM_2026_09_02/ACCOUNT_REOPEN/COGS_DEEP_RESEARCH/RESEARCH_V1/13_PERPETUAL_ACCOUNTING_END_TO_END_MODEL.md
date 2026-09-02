# 13 — Perpetual Accounting End-to-End Model

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `PERPETUAL MODEL CONSTRUCTED FROM LAYER A EVIDENCE — CP-06 (file 13 of 2) — NOT A DESIGN FREEZE`

---

## 1. Purpose and Boundary

This file builds the Perpetual accounting lifecycle required by governing prompt §8.2:

`Opening Inventory -> Purchase / Receipt / Vendor Bill -> Inventory Asset -> Sale / Delivery / Customer Invoice -> COGS Recognition -> Returns/Reversals -> Period Close/Reconciliation`

and answers, explicitly and separately, every §8.2 research question. It does not compare Perpetual against Periodic (that is file `14`'s job) and it does not select a final SMEsPlus posting design (`SMEPLUS CANDIDATE` cells below are candidates only, per `CV-04`/§12).

Foundational rule carried into every section below: **Inventory emits facts; Accounting decides postings.** Nowhere in this file does "the reference ERP does X" become "SMEsPlus Inventory must do X." Reference behavior is Layer A evidence about one external system's implementation choice, transformed per governing prompt §3 into neutral business meaning before any SMEsPlus candidate is proposed.

---

## 2. Evidence Base (Layer A citations used in this file)

| ID | Citation |
|---|---|
| `EV-13-01` | Reference ERP official documentation — Inventory valuation (Accounting standards, Configuration, Valuation methods, Variation account, Accrual entries, Upgrade process for Anglo-Saxon Perpetual), version 19.0, retrieved 2026-09-02 |
| `EV-13-02` | Reference ERP official documentation — Valuation cheat sheet (Inventory vs Accounting, Accounting Methods, Changes in version 19), version 19.0, retrieved 2026-09-02 |
| `EV-13-03` | Reference ERP official documentation — Automatic inventory valuation (Types of accounting, Expense account, Stock input/output), version 17.0, retrieved 2026-09-02 |
| `EV-13-04` | Reference ERP official documentation — Using inventory valuation (Receive a product, Deliver a product, Inventory valuation journal entries), version 17.0, retrieved 2026-09-02 |
| `EV-13-05` | Reference ERP official documentation — Automatic inventory valuation (Costing method, Types of accounting), version 18.0, retrieved 2026-09-02 |

`EV-13-01`/`EV-13-02` are version-19-only pages (the version-19 cheat-sheet page carries an explicit banner stating it applies to version 19 or later of the reference ERP only — vendor name scrubbed per `CV-01`, version number retained as required by `CV-02`). `EV-13-03`/`EV-13-04`/`EV-13-05` describe the pre-19 architecture. Both eras are carried below as **two distinct Perpetual regimes**, not silently merged, per governing prompt §5 version-delta rule.

---

## 3. The Single Most Material Version Delta in This File

Before the lifecycle can be described, one fact must be stated plainly because it invalidates any single unqualified answer to "when does Perpetual recognize COGS":

> "Before [major version 19], the Perpetual accounting method was implemented by posting real-time accounting entries at each stock movement... Since [version 19], the Perpetual method impacts the stock valuation account at the invoice level." — `EV-13-02`

This is not a cosmetic label change. It is a change in **which physical event triggers a financial journal entry** under the same policy name ("Perpetual"). The reference ERP's own comparison table (`EV-13-02`) states directly:

| Dimension | Pre-19 Regime | Version-19+ Regime |
|---|---|---|
| Perpetual Entries | "Invoices + every moves" | "Invoices + one closing" |
| Accounting valuation | "Requires inventory" (accounting reads inventory-layer values) | "Accounting only" (accounting valuation is self-contained) |
| Periodic + Anglo-Saxon combination | "Not supported" | "Fully supported" |
| Perpetual Continental / Anglo-Saxon closing | "Manual closing" | Automated (closing entry mechanism applies uniformly) |
| General ledger volume | "More journal entries" | "Fewer journal entries" |

**Fact Status: `VERIFIED`** (direct quotation, `EV-13-02`). Every answer in §7 below is therefore given twice — once for the pre-19 regime, once for the version-19+ regime — rather than once with an implicit version assumption. This directly satisfies governing prompt §5's instruction not to "silently carry an old Automatic/Manual valuation interpretation into a newer Periodic/Perpetual model, or vice versa."

Terminology note (`Fact Status: VERIFIED`, `EV-13-01`/`EV-13-03`): the pre-19 field pairing was **Perpetual (Automatic)** vs **Periodic (Manual)**, set primarily at product-category level (`Inventory Valuation = Automated`). The version-19+ field pairing is **Perpetual (at invoicing)** vs **Periodic (at closing)**, set at company level (`Accounting -> Configuration -> Settings -> Inventory Valuation`), with category/product override still available per `EV-13-01` ("Default accounts, inventory valuation methods, and costing methods can be overridden by setting them on the product category form"). Whether the pre-19 category-level `Automated`/`Manual` labels still exist as-is on the category form after the version-19 change, or whether the category form was collapsed into the company-level setting only, is **`UNKNOWN / HOLD`** — no version-19 category-form field list was independently confirmed in this pass (routed to file `04`).

---

## 4. Perpetual Lifecycle — Pre-19 Regime ("real-time at every stock movement")

### 4.1 Opening Inventory
An opening quantity/value exists on-hand before this lifecycle's first researched event. Per file `01` §3.1, this value must arrive as an Inventory-emitted fact (opening valuation fact, `HX-24` in the Inventory package); this file does not re-derive how that fact is produced (out of Accounting-side scope) — it only receives it as the starting Inventory Asset balance. Migration/opening-balance replay integrity is file `26`'s subject, not this file's.

### 4.2 Purchase / Receipt / Vendor Bill
`Fact Status: VERIFIED` (`EV-13-03`, `EV-13-04`).

- A Purchase Order by itself creates no valuation/accounting entry (order documents are not stock movements).
- **Physical receipt** (goods arrive into stock) is the event that creates the first journal entry: "each new stock move layer (SVL)... generates a journal entry" (`EV-13-03`), observed in practice tied to the receipt document reference (e.g., a `WH/IN/*` reference), not to the vendor bill document (`EV-13-04`).
- At receipt, the counterpart side of the entry is **not** the final Payable/Expense account directly — it is the **Stock Input Account**, described as: "counterpart journal items for all incoming stock moves will be posted in this account... unless there is a specific valuation account set on the source location" (`EV-13-03`).
- The **Vendor Bill**, when it later posts, is the event that clears/balances the Stock Input interim account against Accounts Payable (Anglo-Saxon: "receiving products and billing vendors balance the Stock Input account", `EV-13-03`).

**REFERENCE OBSERVATION**: Receipt posts Stock Valuation (debit, increasing the asset) against Stock Input (credit, interim). Vendor Bill posts Stock Input (debit, clearing the interim) against Accounts Payable (credit).
**ACCOUNTING MEANING**: the reference ERP treats the *physical* receipt event as the moment the Inventory Asset increases, and treats the *billing* event as the moment the obligation to a vendor is recognized — the interim account exists specifically to hold the gap between "goods are physically in" and "vendor has billed us for them," so neither event is silently dropped and neither is double-counted.
**THAI RULE STATUS**: `HOLD` (routed to file `24` per Hard Rule "Reference behavior is evidence, not target architecture" — a Thai-authoritative position on when a purchase obligation and the related asset are each recognized is not established in this file).
**SMEPLUS CANDIDATE / HOLD**: `HOLD` — whether SMEsPlus adopts a receipt-vs-bill interim account at all is `JT-06` (late supplier bill) territory, not decided here.

### 4.3 Inventory Asset
`Fact Status: VERIFIED` (`EV-13-03`).
The account carrying the Inventory Asset in this regime is the **Stock Valuation Account**: "when automated inventory valuation is enabled on a product, this account will hold the current value of the products" (`EV-13-03`). It is updated at every physical stock move (receipt increases it, delivery decreases it), independent of billing/invoicing status — this is the direct consequence of "real-time... at each stock movement" (`EV-13-02`, describing what pre-19 did). Costing method (Standard / AVCO / FIFO) determines the **unit cost** applied at each move; see §8.

### 4.4 Sale / Delivery / Customer Invoice
`Fact Status: VERIFIED` with one internal documentation tension flagged as `Fact Status: PROVISIONAL` (see below).

- **Delivery** (goods leave stock) is a stock move like receipt, and per §4.2's mechanism it generates a journal entry crediting Stock Valuation. The counterpart is the **Stock Output Account**: "counterpart journal items for all outgoing stock moves will be posted in this account... unless there is a specific valuation account set on the destination location" (`EV-13-03`).
- Under **Anglo-Saxon** accounting specifically, Stock Input and Stock Output are configured as *different* current-asset accounts, and the documentation states: "delivering products and invoicing the customer balance the Stock Output account" (`EV-13-03`) — i.e., the Stock Output interim balance is only fully cleared once the customer invoice posts.
- The Expense Account field itself (the account ultimately meant to carry P&L cost) is configured, for Anglo-Saxon + Automated, as an "Expenses or a Cost of Revenue type (e.g. Cost of Production, Cost of Goods Sold, etc.)" (`EV-13-03`) — a genuine P&L account, distinct from the Stock Output current-asset interim account.

**Internal documentation tension (`Fact Status: PROVISIONAL`, flagged not resolved by direct quotation):** the same page states in one place that "the costs of goods sold (COGS) are reported when products are sold or delivered" and in the very next sentence that "the cost of a good is only recorded as an expense when a customer is invoiced for a product" (`EV-13-03`). These two sentences are not self-consistent read literally. The most defensible synthesis, built only from the account-role definitions quoted above (not from a separately observed worked example, which this pass did not independently trace through the live UI):

**REFERENCE OBSERVATION**: Delivery moves value out of Stock Valuation into the interim Stock Output account (a current asset), not directly into the Expense/COGS account. Customer Invoice is the event the documentation identifies as jointly balancing (clearing) that Stock Output interim account.
**ACCOUNTING MEANING**: physical delivery changes *which asset account* holds the value (Stock Valuation -> Stock Output interim); it does not by itself post to the Profit & Loss expense/COGS account. The P&L expense recognition is structurally completed only when the interim account is cleared — and the documentation names invoicing, not delivery, as the clearing event for Anglo-Saxon Stock Output. This reading is consistent with, not contradictory to, the Anglo-Saxon "costs of goods sold... reported when products are sold or delivered" language if that phrase is read as describing the *trigger for the interim stock-side entry*, while the *Expense-account debit* specifically waits for invoicing. **This resolution is a synthesis by this research pass, not a directly observed worked journal-entry trace** — it is offered as `PROVISIONAL`, not `VERIFIED`, and a direct UI/journal trace (posting a real delivery, then a real invoice, and reading the two generated entries) is the concrete follow-up action needed to move it to `VERIFIED`. No dollar-figure example is fabricated here per the Hard Rule "No fabricated journal entry."
**THAI RULE STATUS**: `HOLD`.
**SMEPLUS CANDIDATE / HOLD**: `HOLD` — this is exactly the shape of question `JT-04` ("COGS recognition timing — dispatch vs invoice") already exists to resolve; this file supplies it as evidence, not as a decision.

### 4.5 Returns / Reversals
`Fact Status: HOLD — not independently traced in this pass.` The Menu-A/Menu-G/Menu-19 evidence files (routed: file `19`) carry the dedicated return-to-original-cost-basis proof. This file records only the structural implication of §4.2–4.4: because the pre-19 regime posts a real journal entry at every stock movement, a return (a reverse stock movement) would, by the same "every move gets an entry" rule (`EV-13-02`), generate its own reversing entry at the moment of the physical return movement, symmetrically to the original movement's interim-account mechanics. Whether the reference ERP re-uses the *original* cost layer (FIFO-specific concern) or applies a new average/standard cost at return time is `HOLD`, cross-referenced to `JT-05`/`C-03`.

### 4.6 Period Close / Reconciliation Under Pre-19 Perpetual
`Fact Status: VERIFIED` (`EV-13-02` "Manual closing" cells for pre-19 Perpetual Continental/Anglo-Saxon).
Even in the pre-19 "real-time at every movement" regime, a closing step still existed and was **manual** — the version-19+ comparison table's own baseline states pre-19 Perpetual closing was "Manual closing" for both Continental and Anglo-Saxon (`EV-13-02`). This means real-time movement-level posting did not eliminate the need for a period-end reconciliation step even before version 19; it only reduced what that step had to correct for, since most value had already moved account-to-account in real time. What exactly the manual close corrected for pre-19 (e.g., un-invoiced Stock Output balances, un-billed Stock Input balances) is `HOLD` — not independently traced to a pre-19 "Inventory Valuation report" worked example in this pass.

---

## 5. Perpetual Lifecycle — Version-19+ Regime ("Perpetual at invoicing")

### 5.1 Opening Inventory
Unchanged in kind from §4.1 — an opening fact is received, not re-derived, by the Accounting side.

### 5.2 Purchase / Receipt / Vendor Bill
`Fact Status: VERIFIED` (`EV-13-01`, `EV-13-02`).

- The **Inventory app** ("stock" layer) still tracks physical receipt in real time — this did not change: "The Inventory app keeps track of the inventory value in real time as you receive and deliver goods" (`EV-13-02`). What changed is whether that physical event, by itself, produces an **accounting** journal entry.
- Per the Accounting-vs-Inventory responsibility table (`EV-13-02`): Receipt = Inventory only (`✓` under Inventory, `/` — not applicable — under Accounting). Vendor Bill = Accounting only (`✓` under Accounting, `/` under Inventory).
- Under the Periodic/Perpetual definitions restated for version 19+: "Perpetual: Post vendor bills as assets (stock valuation), report expenses when goods are sold (cost of goods sold)" (`EV-13-02`) — the **Vendor Bill**, not the physical receipt, is the accounting-recognized event that increases the Inventory Asset (Stock Valuation) account under Perpetual.
- Stock Input/Output interim accounts as a named account pair are **retired** in this regime: "In [version] 19, the stock input/output accounts are no longer used" (`EV-13-01`). The gap between physical receipt and vendor bill is instead covered by (a) the **Variation account**, described as a buffer, and (b) explicit **accrual entries** against a "Bill to Receive"/"GRNI"-type report line (`EV-13-01`).

**REFERENCE OBSERVATION**: Under version-19+ Perpetual, the Vendor Bill posting is the accounting-recognized trigger that debits the Stock Valuation (asset) account; the physical receipt by itself does not.
**ACCOUNTING MEANING**: the reference ERP has moved the "which physical/financial event moves the Inventory Asset account" boundary. Physical truth (goods are in the warehouse) and financial truth (the asset is recorded) are allowed to diverge until a bill posts or until the periodic closing/accrual mechanism catches the gap — a materially different posture from the pre-19 "every move is instantly financial" model.
**THAI RULE STATUS**: `HOLD`.
**SMEPLUS CANDIDATE / HOLD**: `HOLD` — squarely `JT-03` (continuous vs periodic valuation *timing*) and `JT-06` (late supplier bill) territory.

### 5.3 Inventory Asset
`Fact Status: VERIFIED` (`EV-13-01`).
Carried on the **Valuation Account**: "the asset account used to record the financial value of physical stock" (`EV-13-01`), company-configured, overridable per category. Under version-19+ Perpetual it is populated by Vendor Bill (purchase side, §5.2) and reduced by Customer Invoice (sale side, §5.4) — **not** by the underlying stock-move layer directly, except to the extent the **stock closing process** (§5.6) catches up un-invoiced/un-billed movement.

### 5.4 Sale / Delivery / Customer Invoice
`Fact Status: VERIFIED` (`EV-13-01`, `EV-13-02`) — this is the least ambiguous evidence in this file.

Direct quotation: "Perpetual (at invoicing): Inventory valuation is updated when bills or invoices are posted. The expense account (COGS) is debited when invoices are posted." (`EV-13-01`).

**REFERENCE OBSERVATION**: Under version-19+ Perpetual, the Customer Invoice posting — not the delivery — is the documented, unambiguous trigger that debits the Expense/COGS account. The Accounting-vs-Inventory table confirms Delivery = Inventory-only event, Customer Invoice = Accounting-only event (`EV-13-02`).
**ACCOUNTING MEANING**: the version-19+ regime removes the ambiguity that §4.4 flagged as `PROVISIONAL` for the pre-19 regime — it makes the invoice, explicitly and by name, the sole accounting-recognized COGS trigger, with delivery relegated to a physical-only (Inventory-layer) event that the accounting layer only reconciles at closing.
**THAI RULE STATUS**: `HOLD` — a Thai-authoritative view on whether "cost recognized as expense when related revenue is recognized" (the matching-principle language governing prompt §13 asks this file's Thai track to test) aligns with an invoice-triggered COGS event, or requires a delivery/transfer-of-control-triggered event instead, is not established here; routed to file `24`.
**SMEPLUS CANDIDATE / HOLD**: `HOLD` — this is `JT-04`'s central question, now evidenced with a directly quotable, unambiguous reference behavior rather than the pre-19 tension. The evidence itself does not resolve `JT-04`; it sharpens what `JT-04` must decide for SMEsPlus (dispatch-triggered vs invoice-triggered vs a hybrid using SMEsPlus's own interim mechanism).

### 5.5 Returns / Reversals
`Fact Status: HOLD` — not independently traced for the version-19+ regime in this pass; routed to file `19`. Structural implication carried forward: because version-19+ Perpetual ties COGS to the invoice event rather than the movement event, a **credit note** (the invoice-side reversal) is the more likely candidate trigger for a COGS reversal than the physical goods-return movement alone — but this is `PROVISIONAL`, not independently confirmed against a worked credit-note trace.

### 5.6 Period Close / Reconciliation Under Version-19+ Perpetual
`Fact Status: VERIFIED` (`EV-13-01`).
Even though Perpetual is "at invoicing," period close is **not eliminated** — it is redefined. The **Stock Closing entry** process is explicitly still present and still runs under Perpetual, described as reconciling "for deliveries and receipts, even if there is no invoice or vendor bill yet" (`EV-13-01`, describing Perpetual (at invoicing) combined with the stock closing process). The **Inventory Valuation report** shows: Initial Balance, Inventory Loss (Periodic-only), Cost of Production (Periodic-only, and even then "not commonly used" for Continental Periodic per the same source), Stock Variation (difference between posted value and stock-layer value), and Ending Stock (`EV-13-01`). Clicking "Generate Entry" then "Post" creates the Stock Closing entry updating Stock Valuation and Stock Variation in the general ledger (`EV-13-01`). Separately, **Accrual entries** (`Bill to Receive`, `Invoices To Be Issued`, `Billed Not Received`, `Invoiced Not Delivered` review lines) exist specifically because "revenue and expenses are recognized when goods or services are delivered or received, not when invoiced," and under Anglo-Saxon Perpetual these accrual entries also redistribute the Variation buffer account balance into named accounts ("Bill to Receive" / "GRNI") (`EV-13-01`).

**This directly answers §8.2's "what does period close still do under Perpetual"**: it (a) still generates a genuine Stock Closing journal entry against the Variation buffer account for any physical movement not yet matched by a bill/invoice, and (b) still requires optional accrual entries to align expense/revenue timing with delivery/receipt timing rather than invoice timing, for financial-statement-accuracy purposes — i.e., "Perpetual" does not mean "close does nothing"; it means the close's job narrows from "the primary posting mechanism" (Periodic) to "a gap-filler for what invoicing hasn't yet caught" (Perpetual).

---

## 6. Interim / Variation Control Mechanism — Both Regimes Compared

`Fact Status: VERIFIED` for both cells, `EV-13-01`/`EV-13-03`.

| | Pre-19 Regime | Version-19+ Regime |
|---|---|---|
| Named mechanism | Stock Input Account / Stock Output Account (per product category, current-asset type) | Variation Account (single buffer, current-asset or expense type depending on standard) + Accrual entries (Bill to Receive / GRNI / Invoices To Be Issued / Invoiced Not Delivered) |
| Granularity | Per stock move (one interim posting per receipt, one per delivery) | Aggregated at closing (one Stock Closing entry covering the period's un-invoiced/un-billed gap), with optional accrual entries for specific pending documents |
| Anglo-Saxon config | Stock Input ≠ Stock Output (two distinct current-asset accounts) | Variation account = "Current asset account (recommended for interim tracking) or expense account (optional)" (`EV-13-01`) |
| Continental config | Stock Input = Stock Output (one shared current-asset account) | Variation account = "Expense account (specific for variation recording)" (`EV-13-01`) |
| Migration note | N/A (native regime) | Explicit "Upgrade process for Anglo-Saxon Perpetual" documented: non-zero Stock Interim balances must be journaled into Stock Valuation before/after upgrade, via either a server action or a manual journal entry, then a new "inventory variation entry" moves the increase into the new Variation account (`EV-13-01`) |

**ACCOUNTING MEANING**: both regimes solve the same underlying problem — physical movement and financial recognition do not always happen at the same instant, so an interim/buffer account exists to hold the difference without either fabricating revenue/expense early or losing track of physical value that has moved. The regimes differ in *when* that buffer is cleared: pre-19 clears it move-by-move as bills/invoices arrive; version-19+ clears it in aggregate at closing/accrual time. This is the direct evidentiary answer to §8.2's "what interim/variation control exists when physical and financial timing differ."
**SMEPLUS CANDIDATE / HOLD**: `HOLD` — both mechanisms are candidate shapes for whatever SMEsPlus's own interim-timing control ends up being; neither is adopted here.

---

## 7. Direct Answers to Governing Prompt §8.2 Questions

| # | Question | Answer (version-qualified) | Fact Status |
|---|---|---|---|
| 1 | Which event updates Inventory Asset? | Pre-19: physical **receipt** (real-time stock move). Version-19+: **Vendor Bill** posting (with the closing process catching un-billed receipts). | `VERIFIED` both regimes (§4.3, §5.3) |
| 2 | Which event recognizes COGS? | Pre-19: structurally ambiguous in the source text itself — physical **delivery** moves value out of Stock Valuation into an interim Stock Output account, but the Expense/COGS P&L account debit is best evidenced as completed at **Customer Invoice** (interim-clearing event). Version-19+: unambiguously **Customer Invoice** ("the expense account (COGS) is debited when invoices are posted"). | Pre-19: `PROVISIONAL`. Version-19+: `VERIFIED` (§4.4, §5.4) |
| 3 | Is COGS triggered by delivery, invoice, or another event — does this vary by version/standard? | Yes, it materially varies by version (see row 2) and by standard: Continental Periodic debits an expense-by-nature account at **vendor bill** time regardless of sale timing (file `12`'s subject), which is a third pattern outside this file's Perpetual scope entirely. | `VERIFIED` (delta itself), `PROVISIONAL` (pre-19 exact trigger) |
| 4 | What interim/variation control exists when physical and financial timing differ? | Pre-19: Stock Input/Stock Output accounts, per move. Version-19+: Variation account (buffer) plus accrual entries (Bill to Receive/GRNI, Invoices To Be Issued, Invoiced Not Delivered, Billed Not Received). | `VERIFIED` (§6) |
| 5 | What happens to partial receipt/delivery? | `HOLD` — not independently traced in this pass. The stock-move-layer (SVL) generation logic ("each new stock move layer... generates a journal entry", `EV-13-03`) implies each partial movement is its own layer/event, so a partial receipt would post its own partial-value entry rather than waiting for full PO completion — but this inference was not confirmed against a worked partial-receipt example. Routed to file `17` (purchase-side) and file `18` (sales-side, partial delivery/backorder, this file's companion). | `HOLD` |
| 6 | What happens when vendor bill price differs from valuation cost? | `PROVISIONAL` — the **Price Difference Account** exists specifically for this: "records the difference between the product's standard price... and the actual billed price" (`EV-13-01`), but this is documented only for the **Standard Price** costing method under version-19+ Perpetual ("When using the Perpetual (at invoicing) valuation method with the Standard Price costing method, a Price Difference Account can be set"). Behavior under AVCO/FIFO, and under the pre-19 regime specifically, is `HOLD`. | Standard-cost/version-19+: `PROVISIONAL`. Other cost methods/pre-19: `HOLD` |
| 7 | What happens when landed cost arrives after some stock has been sold? | `HOLD` — a landed-cost-specific documentation page was targeted in this pass but did not resolve to independently fetchable, quotable primary text; this file does not fabricate a mechanism. Routed to file `21` as a dedicated open item, cross-referenced `JT-08`. | `HOLD` |
| 8 | How are returns reversed to the original cost basis? | `HOLD` — not independently traced for either regime in this pass beyond the structural inference in §4.5/§5.5. Routed to file `19`, cross-referenced `JT-05`/`C-03`. | `HOLD` |
| 9 | What does period close still do under Perpetual? | It still generates a genuine Stock Closing journal entry for the un-invoiced/un-billed gap, and (version-19+) still needs optional accrual entries for delivery/receipt-vs-invoice timing alignment; period close is a gap-filler under Perpetual, not the primary posting mechanism it is under Periodic. | `VERIFIED` (§5.6) |

No cell above is left blank; every unresolved item carries an explicit `HOLD`/`PROVISIONAL` status and a routing target rather than a guessed answer, per the Hard Rule "Do not manufacture certainty."

---

## 8. Costing Method Interaction (Perpetual-Specific Notes)

`Fact Status: VERIFIED` (`EV-13-03`/`EV-13-05`, worked numeric tables reproduced structurally, not verbatim, to avoid unnecessary reproduction of a long source table; the arithmetic pattern is restated in neutral form).

- **Standard Price**: unit cost is fixed on the product form; a receipt at a different purchase price does not change the Inventory Asset unit cost — the delta is a candidate case for the Price Difference Account (§7 row 6, version-19+ Perpetual + Standard only, `PROVISIONAL`).
- **Average Cost (AVCO)**: unit cost recalculates on every receipt as `(prior inventory value + incoming value) / new quantity on hand`; deliveries use the current average at the moment of delivery, regardless of original purchase price. This is stated as "dynamic" in the source (`EV-13-03`).
- **FIFO**: each receipt retains its own cost layer; a delivery consumes the oldest layer(s) first, and a delivery spanning multiple layers produces a **blended** unit cost for that delivery (the source's worked example shows a 10-unit delivery consuming 8 units at one cost and 2 units at another, producing a mixed delivery value) (`EV-13-03`).

**ACCOUNTING MEANING**: costing method changes *how much* value moves at each event, not *which event* moves it — the version-delta in §3 (which event triggers a financial entry) is orthogonal to which costing method is chosen. A change of costing method is separately flagged in the source as leaving already-received stock at its prior value while only new-forward movement uses the new method (`EV-13-03`: "products already in stock... do not change value; rather, the existing units keep their value, and any product moves from then on affect the average cost").
**SMEPLUS CANDIDATE / HOLD**: `HOLD` — routed to file `15` for the dedicated costing-method matrix; this file records only the Perpetual-specific interaction.

---

## 9. Open Joint Decisions This File Feeds (Not Closes)

| ID | This file's contribution |
|---|---|
| `JT-03` | Direct evidence that "Perpetual" is not one fixed timing model across reference versions — it is at minimum two materially different timing models sharing one name (§3, §5). |
| `JT-04` | The pre-19 vs version-19+ COGS-trigger contrast (§7 row 2/3) is the single most load-bearing evidence this file contributes to `JT-04`. |
| `JT-05`/`C-03` | Not resolved here; §4.5/§5.5 record only the structural expectation that a return event must exist somewhere in the timing model, without evidencing the cost-basis mechanics. |
| `JT-06` | The interim-account mechanism (§6) is the reference-side evidence base for how a late vendor bill is *structurally* absorbed without corrupting the Inventory Asset balance already recognized from receipt (pre-19) or without prematurely recognizing an asset before the bill exists (version-19+). |
| `JT-08` | Landed cost explicitly `HOLD` (§7 row 7) — this file does not claim evidence it does not have. |

---

## 10. Material Unknowns Carried Out of This File

1. Version-19+ product-category-level field continuity (`Automated`/`Manual` labels) — `HOLD`, routed file `04`.
2. Exact mechanics of partial receipt/delivery under both regimes — `HOLD`, routed files `17`/`18`.
3. Price Difference Account behavior outside Standard-cost + version-19+ Perpetual — `HOLD`, routed file `21`.
4. Landed cost after partial/full sale — `HOLD`, routed file `21`.
5. Return-to-original-cost-basis mechanics under both regimes — `HOLD`, routed file `19`.
6. The pre-19 delivery-vs-invoice COGS tension (§4.4) remains `PROVISIONAL`, not `VERIFIED` — closing it requires a direct worked-journal-entry trace against a live or archived pre-19 instance, which this research pass (external documentation only, per governing prompt §3's Layer A boundary) could not perform.

None of the above is treated as resolved. Each is carried forward exactly as `HOLD`/`PROVISIONAL`, per the Hard Rule "No Evidence = No Progress."

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
