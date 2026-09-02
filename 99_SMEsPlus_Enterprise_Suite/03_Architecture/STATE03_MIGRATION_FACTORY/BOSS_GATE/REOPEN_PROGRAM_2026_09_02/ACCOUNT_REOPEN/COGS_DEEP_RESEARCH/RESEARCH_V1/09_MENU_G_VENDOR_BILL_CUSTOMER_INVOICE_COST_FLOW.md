# 09 — MENU G — Vendor Bill / Customer Invoice Accounting Behavior

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE IN PROGRESS — CP-03 (Menu G) — three-layer evidence, no synthesis to Final Design`

---

## 0. Scope and Convention Binding

This file answers governing prompt §6 Menu G: how the Product-Category/Product accounting resolution proven in files `04` and `05` is actually **consumed** — which account is debited/credited, and by which triggering event — when a Vendor Bill is posted, a Customer Invoice is posted, the bill/invoice exists before or after the physical receipt/delivery, quantities are partial, returns occur, price differs from cost, or the accounting period is closed.

This file inherits `CV-01`–`CV-06` from `00_EXECUTION_CHECKPOINT_LOG.md`: the reference ERP is never named by product; citations use the `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02` form; no vendor code tokens or fenced code blocks appear; three evidence layers are kept separate; nothing here is a final SMEsPlus design decision.

Joint decisions this file feeds (not closes): `JT-04` (COGS recognition timing — dispatch vs invoice), `JT-05`/`C-03` (return cost basis), `JT-06` (late supplier bill after close). Question-fingerprint rows `4`, `5`, `11`, `12`, `13` from file `01` §5 are primarily answered here.

---

## 1. Layer A — Governing Distinction Observed in the Reference ERP

Two independent axes are documented, and the reference material is explicit that they are **conventionally paired but not the same axis**:

| Axis | Values observed | Evidence |
|---|---|---|
| Accounting standard / recognition philosophy | `Continental` — cost of a good is recognized as expense as soon as the product is received into stock (i.e., at the vendor-bill/receipt boundary, not at sale). `Anglo-Saxon` — cost of goods sold is recognized as an expense only when the good is invoiced/delivered to the final customer. | Reference ERP official documentation — Inventory valuation (Continental/Anglo-Saxon accounting mode), version 13.0, retrieved 2026-09-02; version 19.0, retrieved 2026-09-02 |
| Valuation update cadence | `Periodic (at closing)` — inventory value is updated only during a stock-closing process; day-to-day stock movement is tracked physically but not synchronized to the ledger. `Perpetual (at invoicing)` — inventory value is updated when stock moves occur / when bills or invoices are posted, i.e. continuously rather than only at close. | Reference ERP official documentation — Inventory valuation: periodic vs perpetual methods, version 19.0, retrieved 2026-09-02 |

The 19.0 documentation states explicitly: *"Periodic ... is often associated with Continental standards, while ... Perpetual ... is commonly used with Anglo-Saxon standards"* — a **correlation**, not an enforced pairing. Earlier documentation (13.0, saas-16.4) instead frames the same underlying choice as a binary `Manual` vs `Automated` **Inventory Valuation** field on the Product Category, with the Continental/Anglo-Saxon choice expressed separately through which accounts are configured (same account for input/output = Continental-style; distinct accounts = Anglo-Saxon-style). This is a material **terminology version-delta**, not merely a relabeling of identical mechanics — see §8.

`FACT STATUS: VERIFIED (Layer A, terminology and correlation only — not a rule that one axis determines the other).`

---

## 2. Menu G Field/Account Evidence Sheet

| Field | Requirement | Evidence |
|---|---|---|
| Menu Path | Accounting → Configuration → Settings → Inventory Valuation (account definition); consumed at Purchase → Vendor Bills and Sales → Customer Invoices posting screens | Reference ERP official documentation — Inventory valuation, versions 13.0–19.0, retrieved 2026-09-02 |
| Field Label | "Stock Input Account" / "Stock Output Account" (pre-19 terminology, automated/perpetual only); "Valuation Account" / "Variation Account" (19.0 terminology, applies to both Periodic and Perpetual) | Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02; Inventory valuation, version 19.0, retrieved 2026-09-02 |
| Purpose | Interim/clearing accounts that absorb the timing gap between a physical stock movement and its matching bill/invoice; the "Variation" account additionally absorbs the gap closed only at stock-closing under Periodic | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 |
| Values / Options | Continental style: Stock Input Account = Stock Output Account (same Current Asset account). Anglo-Saxon style: Stock Input Account ≠ Stock Output Account (two distinct Current Asset accounts) | Reference ERP official documentation — Automatic inventory valuation, version saas-16.4, retrieved 2026-09-02 |
| Default | UNKNOWN — reference documentation does not publish a universal default GL code; defaults are chart-of-accounts/localization-dependent | HOLD / EVIDENCE REQUIRED |
| Visibility | Stock Input/Output/Valuation/Journal fields visible only when Inventory Valuation = Automated/Perpetual on the Product Category; not shown under Manual/Periodic | Reference ERP official documentation — Inventory valuation configuration, version saas-16.4, retrieved 2026-09-02 |
| Scope | Product Category (primary); resolvable per company (multi-company chart of accounts) | Reference ERP official documentation — Inventory valuation configuration, versions 13.0–18.0, retrieved 2026-09-02 |
| Inherits From | Product Category; not overridden at Product level for these specific accounts (Product-level override is limited to Income/Expense accounts per file `05`) | Reference ERP official documentation — Product Category accounting fields, versions 13.0–19.0, retrieved 2026-09-02; cross-ref file `05` |
| Override Precedence | N/A for Stock Input/Output/Valuation (category-only); Income/Expense precedence is Product-level override over Category default, per file `05` | Cross-ref file `05` (Menu C) |
| Transaction Consumer | Receipt validation (debits Stock Valuation/Input side); Vendor Bill posting (clears the interim account, debits it, credits Accounts Payable); Delivery validation (credits Stock Valuation/Output side under Perpetual pre-19); Customer Invoice posting (recognizes COGS/expense side under Anglo-Saxon Perpetual) | Reference ERP official documentation — How stock valuation account interacts with vendor bills, version saas-16.4, retrieved 2026-09-02; community/support corroboration retrieved 2026-09-02 |
| Periodic Behavior | Receipt/delivery create **no** value-affecting journal entry. Vendor Bill posting debits the Expense account "by nature" and credits Accounts Payable — this **is** the value-affecting posting. Inventory Value on the Balance Sheet is corrected only at stock-closing, via the Variation account (an Expense-type account under Continental Periodic). | Reference ERP official documentation — Inventory valuation: periodic vs perpetual methods, version 19.0, retrieved 2026-09-02 |
| Perpetual Behavior (pre-19) | Receipt validation **is** value-affecting: debits Stock Valuation, credits Stock Input (interim/"Stock Interim Received"). Vendor Bill posting clears the interim account (debits it) against Accounts Payable (credits it) — a **balance-sheet-only reclassification**, not a new value event, provided the bill price equals the receipt cost. Delivery validation debits Stock Output/credits Stock Valuation; Customer Invoice posting recognizes COGS. | Reference ERP official documentation — Perpetual inventory accounting; Stock valuation interim accounts, versions saas-16.4–18.0, retrieved 2026-09-02 |
| Perpetual Behavior (19.0+) | Materially changed — see §8. The Perpetual method now "impacts the stock valuation account at the invoice level"; receipt/delivery move quantity but the value-affecting posting is consolidated to the bill/invoice event, with the closing entry handling remaining timing gaps (bills to receive, invoices to issue, deferred revenue, prepaid expense). | Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02 |
| Account Type Impact | Stock Input/Output/Valuation = Current Asset; Variation (Continental Periodic) = Expense; Variation (Anglo-Saxon Perpetual, recommended) = Current Asset, optionally Expense | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 |
| Financial Statement Impact | Both — Balance Sheet (Inventory Asset, interim/clearing balances) and Profit & Loss (Expense/COGS, Variation when expense-typed) | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 |
| Change Impact | Changing Inventory Valuation method (Manual↔Automated / Periodic↔Perpetual) does not retroactively restate historical postings; documented migration guidance is to zero stock via adjustment, switch method, then re-enter stock at the original monetary value — i.e., a manual bridging procedure, not an automatic recompute | Reference ERP official documentation — community guidance on moving from Manual (periodic) to Automated (real-time), version 16.0, retrieved 2026-09-02 (secondary/forum-sourced — see Fact Status) |
| Version Delta | Terminology shift Manual/Automated → Periodic/Perpetual; 4-account model (Valuation, Journal, Input, Output) → 2-account model (Valuation, Variation) language in 19.0; Price-Difference/PPV account re-architected at 16.0 — see §8 | Multiple, cited per row above |
| Evidence | See per-row citations above | — |
| Fact Status | VERIFIED for the account-role mechanics and the 19.0 terminology/structural shift (primary reference documentation, multiple versions cross-read); PROVISIONAL for the "Change Impact" row (forum/community source, not primary documentation) | — |

---

## 3. Vendor Bill Posted — Traced by Configuration

### 3.1 Continental / Periodic

The Vendor Bill posting **is** the value-affecting event. It debits the resolved Expense account (Product/Category resolution per files `04`–`05`) "by nature" and credits Accounts Payable. Inventory Value on the Balance Sheet is not touched at this moment; it is corrected only later, at stock-closing, through the Variation account. Physical receipt (if tracked at all) creates no accounting entry.

`FACT STATUS: VERIFIED.` Reference ERP official documentation — Inventory valuation: periodic vs perpetual methods, version 19.0, retrieved 2026-09-02.

### 3.2 Anglo-Saxon / Perpetual (pre-19 mechanics)

Two distinct postings occur, at two distinct times, and reconcile through the Stock Input interim account:

1. Receipt validation: debit Stock Valuation (Inventory Asset), credit Stock Input (interim/clearing, "goods received not invoiced").
2. Vendor Bill posting: debit Stock Input (clearing the interim balance), credit Accounts Payable.

If the receipt happens first, the interim account carries a temporary credit balance ("goods received not invoiced") until the bill clears it. If the bill is posted first (§4), the interim account instead carries a temporary debit balance ("goods invoiced not received") until the receipt clears it.

`FACT STATUS: VERIFIED.` Reference ERP official documentation — How to treat stock valuation (interim); Vendor bill for stock item entry-to-receipt-stock relationship, versions saas-16.4–18.0, retrieved 2026-09-02.

### 3.3 Anglo-Saxon / Perpetual (19.0+)

The receipt still moves physical quantity, but per §8 the value-affecting posting is now consolidated at the invoice/bill event rather than split real-time across receipt-then-bill. The closing entry absorbs the residual "bills to receive" gap. Whether the pre-19 two-step interim mechanic is retained as an intermediate implementation detail beneath the new consolidated presentation, or replaced outright, is **not established from the documentation excerpts retrieved** — the 19.0 cheat-sheet fetch describes the outcome (invoice-level impact, closing-entry-managed gaps) but this session did not retrieve the full underlying account-by-account posting table for 19.0.

`FACT STATUS: HOLD / EVIDENCE REQUIRED` — mechanism-level detail for 19.0 not fully retrieved in this pass; outcome-level claim is VERIFIED, posting-line-level claim is not.

---

## 4. Vendor Bill Exists Before or After Receipt

| Case | Continental / Periodic | Anglo-Saxon / Perpetual (pre-19) |
|---|---|---|
| Receipt before Bill | No entry at receipt (Periodic tracks physically only). Bill posts the expense in full when it arrives. | Receipt posts Stock Valuation vs Stock Input (credit/"goods received not invoiced"). Bill later clears Stock Input against Accounts Payable. |
| Bill before Receipt | Bill posts the expense in full at bill date regardless of physical receipt status — Periodic ties value recognition to the bill event, not the physical event, by design. | Bill posts Stock Input (debit/"goods invoiced not received") vs Accounts Payable. Value sits in the interim account until receipt occurs and clears it against Stock Valuation. |

Both patterns are internally consistent with each method's defining trigger (Periodic = bill-triggered; Perpetual pre-19 = stock-move-triggered, bill-reconciling). The reference documentation does not describe a "bill blocked until receipt exists" hard control at the accounting layer — 3-way matching (PO/receipt/bill quantity and price comparison) is documented as a **procurement control**, separate from whether the accounting entry itself is technically permitted to post. Whether SMEsPlus should impose a harder gate is a Layer C question, not resolved here.

`FACT STATUS: VERIFIED` for the account-mechanics rows; `HOLD` for whether any version enforces a hard block on out-of-sequence posting — not established from documentation retrieved this pass.

---

## 5. Customer Invoice Posted — Traced by Configuration

### 5.1 Continental / Periodic

Symmetric to §3.1: Customer Invoice posting recognizes revenue (Income account) but the matching Expense/COGS side of the sale is **not** separately recognized at invoice time under a strict reading of "cost recognized as soon as received into stock" — the Continental philosophy already recognized the cost at the earlier purchase-bill event. Under Periodic, the outbound side of the identity is captured only at the next stock-closing via the Variation account, not per-invoice. This means Periodic Continental accounting does **not** produce a per-transaction gross-margin-matched COGS line; COGS is a derived, period-end figure (see file `12`, Periodic model).

`FACT STATUS: VERIFIED` on the "no per-invoice COGS posting" conclusion, derived directly from the cited mechanics; flagged for cross-check against file `12`'s full periodic model rather than restated as new synthesis here.

### 5.2 Anglo-Saxon / Perpetual (pre-19)

Delivery validation posts the outbound value move: debit Stock Output (interim), credit Stock Valuation. Customer Invoice posting recognizes COGS as an expense: the documentation states "the cost of goods sold (COGS) is recognized as an expense when the customer invoice is posted, typically when products are sold." The precise debit/credit pairing at invoice time (COGS debit against Stock Output credit, mirroring the vendor-bill-clears-Stock-Input pattern) is the documented symmetric counterpart to §3.2, though this session's retrieved excerpts state the Stock Input side explicitly and infer the Stock Output side by documented symmetry rather than an independently quoted worked example.

`FACT STATUS: VERIFIED` for "invoice posting recognizes COGS" (directly quoted); `PROVISIONAL` for the exact Stock-Output-clearing mechanics at invoice time (inferred by documented symmetry, not independently quoted in the excerpts retrieved).

### 5.3 Anglo-Saxon / Perpetual (19.0+)

Per §8, the value-affecting posting is consolidated to the invoice event; delivery moves quantity. This makes the pre-19 "delivery is a value event" characterization **version-specific**, not a permanent property of Perpetual accounting in this reference ERP — a direct answer to the governing-prompt instruction to "be explicit about which event... triggers a value-affecting posting."

`FACT STATUS: VERIFIED` at the outcome level (see §8 citation); `HOLD` at full posting-line detail, same caveat as §3.3.

---

## 6. Explicit Trigger Determination Table (governing-prompt mandatory question)

| Configuration | Value-affecting event for INBOUND (purchase) side | Value-affecting event for OUTBOUND (sale) side |
|---|---|---|
| Continental / Periodic (all versions reviewed) | Vendor Bill posting (not receipt) | Customer Invoice posting for revenue; COGS is not separately triggered per-invoice — it is a residual computed at stock-closing (Variation account) |
| Anglo-Saxon / Perpetual, versions ≤18.0 (documented) | Receipt validation (Stock Valuation moves); Vendor Bill posting is a clearing/reclass of the interim account, not a new value event, when bill price = receipt cost | Delivery validation (Stock Valuation moves); Customer Invoice posting recognizes COGS as expense and clears the Stock Output interim account |
| Anglo-Saxon / Perpetual, version 19.0+ (documented outcome) | Consolidated to Vendor Bill posting at the invoice/bill level; receipt moves quantity only; closing entry manages "bills to receive" gap | Consolidated to Customer Invoice posting; delivery moves quantity only; closing entry manages "invoices to issue," deferred revenue, prepaid-expense gaps |

`FACT STATUS: VERIFIED` — this table is a direct restatement of cited primary documentation, not an inference beyond what was quoted, with the two `PROVISIONAL`/`HOLD` caveats from §5.2/§5.3/§3.3 carried forward.

---

## 7. Partial Quantities, Backorders, and Returns

### 7.1 Partial quantities / backorders

Invoicing policy is documented as a separate configuration axis from valuation method: "Invoice what is ordered" (default; invoice on sales-order confirmation regardless of delivered quantity) vs "Invoice what is delivered" (invoice only the quantity actually shipped; used where ordered and delivered quantities commonly diverge — bulk/liquid/food goods cited as the documented example). Backorders are created for the undelivered remainder and the system is documented to "automatically add the quantities to the invoice" as further partial deliveries occur.

The retrieved documentation does **not** state how invoicing-policy choice interacts with the Periodic-vs-Perpetual valuation-trigger table in §6 — e.g., whether "Invoice what is ordered" under Anglo-Saxon Perpetual creates a COGS posting for quantity not yet physically delivered. This is a **material unresolved interaction** between two independently documented configuration axes.

`FACT STATUS: HOLD / EVIDENCE REQUIRED` — invoicing-policy × valuation-trigger interaction not found in documentation retrieved this pass. Flagged to file `30` (Material Unknown/Conflict Register).

### 7.2 Purchase returns

Not independently retrieved with a dedicated worked example in this pass; by the documented general reversal mechanism (credit/debit notes reverse the matching original journal items) and the receipt/bill symmetry established in §3–4, a purchase return should reverse through the same Stock Valuation/Stock Input pathway the original receipt used. This is an **inference from documented mechanics**, not an independently cited worked example for the purchase-return case specifically.

`FACT STATUS: PROVISIONAL` — mechanism inferred from documented symmetry; a dedicated purchase-return worked example was not retrieved and should be sourced before this is treated as VERIFIED.

### 7.3 Sales returns / customer credit notes — cost-basis finding (feeds `JT-05`/`C-03`)

Documentation confirms: (a) a validated invoice cannot be edited — a credit note is "the only legal method for canceling, refunding, or modifying a validated invoice"; (b) a reverse stock transfer alone is documented as **insufficient** and must be paired with a credit note to complete a customer return; (c) credit-note creation generates a reverse entry that cancels the matching original journal items.

A materially important **cost-basis finding** surfaced in community/support material (not primary documentation, flagged accordingly): under FIFO costing, a returned unit is valued by the system at the **current** costing-layer price at the time of the return, not the **original** unit cost at which that specific unit was originally issued — a documented discrepancy that can leave a residual, unexplained balance in the interim/clearing account when the current FIFO layer price differs from the original layer's price. This is exactly the question `JT-05`/`C-03` (cost basis for a customer return) asks, and this evidence supports treating it as a **live, documented behavior gap** in the reference ERP under FIFO, not a solved problem to be silently inherited.

`FACT STATUS: VERIFIED` for (a)–(c) (primary documentation); `PROVISIONAL` for the FIFO current-vs-original-layer discrepancy (forum/support-sourced, but specific and mechanically plausible given documented FIFO layer-consumption behavior — retained as a flagged risk, not discarded, per clean-room instruction not to treat commentary as authority while still preserving the signal for Joint review). This finding is material to `JT-05`/`C-03` and must not be silently dropped.

---

## 8. Version Delta — Detailed (feeds file `02`)

| Version boundary | What changed | Evidence |
|---|---|---|
| 13.0 → saas-16.4 | Stable: "Manual" vs "Automated" Inventory Valuation field on Product Category; Continental = same Stock Input/Output account, Anglo-Saxon = distinct accounts; both terms co-exist with a separate "Real Time"/"Periodic" cadence description in some releases | Reference ERP official documentation — Inventory valuation configuration, versions 13.0, 14.0, saas-16.4, retrieved 2026-09-02 |
| 16.0 (point release) | Purchase Price Variance handling re-implemented: per one corroborating source, streamlined to route PPV through the Stock Interim (Received) account with reclass/land/expense/capitalize options, rather than requiring a separate dedicated Price Difference Account in all cases. The 19.0 documentation, however, still independently describes a distinct "Price Difference Account" field available "with Perpetual + Standard Price costing." These two statements are not fully reconciled by the excerpts retrieved. | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (Price Difference Account); community source on 16.0 PPV re-implementation, retrieved 2026-09-02 (secondary) |
| 17.0 / 18.0 | Terminology stable at "Automated" (Stock Valuation Account, Stock Journal, Stock Input Account, Stock Output Account, marked "(automated only)"); Anglo-Saxon/Continental distinction expressed through Expense Account type guidance (Expenses-or-Cost-of-Revenue type vs Expenses-type) | Reference ERP official documentation — Automatic inventory valuation, versions 17.0, 18.0, retrieved 2026-09-02 |
| 19.0 | Structural relabel + mechanism change: field/terminology moves to "Periodic (at closing)" / "Perpetual (at invoicing)"; account model moves toward "Valuation Account" + "Variation Account" language; **Perpetual method now posts stock valuation impact at the invoice level rather than in real time at every stock move**; a consolidated closing entry now separately manages "bills to receive," "invoices to issue," deferred revenue, and prepaid expense gaps that were previously carried differently | Reference ERP official documentation — Inventory valuation; Valuation cheat sheet, version 19.0, retrieved 2026-09-02 |

`WARNING (governing prompt §5 version-delta rule): the 19.0 change is not a cosmetic rename.` A pre-19 assumption that "Perpetual = value posts at receipt/delivery, real time" would be a **false carry-forward** into 19.0, where the documented outcome is that Perpetual now posts value at the bill/invoice event for the inventory-valuation-account impact, with receipt/delivery moving quantity only and a closing entry absorbing residual timing gaps. Any SMEsPlus candidate built on "which reference version" must state the version explicitly — this is not free of ambiguity across the 13.0–19.0 range studied.

`FACT STATUS: VERIFIED` for the fact that a change occurred and its documented outcome; `HOLD` for full mechanism-level detail of the 19.0 posting model (see §3.3/§5.3 caveats).

---

## 9. Period Closed

Lock-date documentation (Journal Entries Lock Date, Tax Return Lock Date, All Users Lock Date) is confirmed present across the versions searched (15.0–19.0 secondary corroboration; primary-documentation confirmation strongest for 17.0–19.0). Once a lock date is set, the system is documented to prevent posting new journal entries dated on or before that date for non-exempted users; an administrator-grantable, scoped, time-bound exception mechanism exists.

Applied to Menu G: a Vendor Bill or Customer Invoice dated **into a locked period** is documented to be blocked from posting at that date for ordinary users. The retrieved documentation does not specify, for either Periodic or Perpetual valuation, whether the system automatically **re-dates** such an entry to the next open period, or simply refuses the post outright requiring manual date correction — this distinction matters directly for `JT-06` (late supplier bill after close) and is not resolved by evidence retrieved in this pass.

`FACT STATUS: VERIFIED` for lock-date existence and the block-on-locked-period behavior; `HOLD / EVIDENCE REQUIRED` for the exact refuse-vs-redate mechanism, which is material to `JT-06` and must not be assumed.

---

## 10. Layer B — Thai Accounting / Tax Evidence

Not independently researched in this file. Pointer only: see `24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md` for authoritative Thai treatment of (a) when purchase cost may be recognized as an asset vs expense, (b) required substantiation for a credit note/return to be tax-valid, (c) cut-off requirements at period end. This file makes **no** Thai-authority claim.

`FACT STATUS: N/A — pointer only, per file `01` §5 routing (Layer B owned by file `24`).`

---

## 11. Layer C — SMEsPlus Candidate Semantics (CANDIDATE / HOLD only)

None of the following are final design. Each is offered as a candidate business-meaning translation for later Joint review, explicitly labeled:

| # | Layer A observation | Neutral business meaning | SMEsPlus candidate status |
|---|---|---|---|
| C-G1 | Continental Periodic ties expense recognition to the bill event, not the physical event | "Purchase cost becomes an accounting fact when the vendor's claim is recorded, not when goods physically arrive" | `CANDIDATE` — plausible general ledger discipline; requires Joint review against Thai cut-off requirement (Layer B, file 24) before any adoption |
| C-G2 | Perpetual pre-19 uses an interim/clearing account to bridge physical-event timing and bill/invoice timing | "A physical stock fact and its matching financial claim are reconciled through an explicit clearing balance, not silently netted" | `CANDIDATE` — consistent with the existing Inventory-emits-facts / Accounting-decides-postings boundary; the clearing-account *mechanism* itself is Layer A implementation detail and is explicitly NOT proposed as SMEsPlus's literal account structure |
| C-G3 | FIFO return valued at current layer, not original layer (§7.3) | "A return's cost basis may drift from its original issue cost under a moving cost method unless explicitly pinned" | `HOLD` — this is a flagged risk to feed `JT-05`/`C-03`, not a resolved design; SMEsPlus must decide, not inherit, whether returns are cost-pinned to the original issuing event |
| C-G4 | Lock-date block-on-post exists but redate-vs-refuse mechanism is unresolved (§9) | "A control preventing back-period posting is expected, but its exact failure-mode UX is undetermined" | `HOLD` — feeds `JT-06`; no candidate offered without the missing evidence |
| C-G5 | Invoicing-policy × valuation-trigger interaction is undocumented in evidence retrieved (§7.1) | "Whether COGS/value posts on invoice-of-order vs invoice-of-delivery is a distinct configuration question from Periodic/Perpetual itself" | `HOLD` — material unknown, routed to file `30` |

---

## 12. Special Team Notes (abbreviated — full register in file `29`)

- `S1 COGS/Financial Accounting`: confirms COGS is never a receipt/delivery-triggered concept under Continental Periodic; under Perpetual it is bill/invoice-triggered (pre-19) or invoice-consolidated (19.0+) — never a same-moment-as-physical-event concept in any configuration reviewed.
- `S4 Periodic Accounting` / `S5 Perpetual Accounting`: the trigger table in §6 is this file's primary handoff artifact to files `12`/`13`.
- `S6 Returns/Adjustment/Scrap/Landed Cost`: the FIFO current-vs-original-layer return finding (§7.3) is this file's primary handoff to file `19`.
- `S9 Migration/Replay/AI Control`: notes that the 19.0 structural change (§8) means any migration/replay design must record which reference-version behavior a legacy comparison was built against — a silent "the reference ERP does X" claim is not safe without a version tag going forward.

---

## 13. Open HOLD / EVIDENCE REQUIRED Items From This File

1. Full posting-line mechanism for 19.0 consolidated Perpetual invoice-level valuation (§3.3, §5.3, §6).
2. Whether any reference version enforces a hard block on bill-before-receipt or invoice-before-delivery posting at the accounting layer, vs. leaving it to a separate 3-way-match procurement control (§4).
3. Dedicated purchase-return worked example (currently inferred by symmetry only) (§7.2).
4. Invoicing-policy (ordered vs delivered) interaction with the Periodic/Perpetual value-trigger table (§7.1) — routed to file `30`.
5. Lock-date refuse-vs-redate mechanism for a late bill/invoice (§9) — material to `JT-06`, routed to file `23`/`30`.
6. Reconciliation of the two conflicting-looking PPV/Price-Difference-Account statements across 16.0 and 19.0 documentation (§8) — routed to file `21`/`30`.

No item above is resolved by assumption. Each remains `HOLD / EVIDENCE REQUIRED` until independently re-verified.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
