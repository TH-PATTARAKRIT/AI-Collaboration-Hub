# 17 — Purchase Receipt / Vendor Bill Cost Flow

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE COMPLETE — PURCHASE-SIDE ARCHETYPES (LAYER A) — LAYER B THAI HOLD — CP-08 SUPPORT`

---

## 1. Purpose and Scope

This file is the dedicated account-flow proof (governing prompt §12 format) for the purchase-side cost lifecycle: purchase order confirmation → receipt validation → vendor bill posting → price variance → inventory capitalization — under both Periodic and Perpetual, including receipt-before-bill, bill-before-receipt, and same-period timing. It does not repeat the sales-side lifecycle (file `18`) or the full Periodic/Perpetual end-to-end models (files `12`/`13`); it narrows to the purchase side only, at archetype depth.

Every archetype below carries the four mandatory labels: `REFERENCE OBSERVATION`, `ACCOUNTING MEANING`, `THAI RULE STATUS`, `SMEPLUS CANDIDATE / HOLD`. No archetype prescribes a final SMEsPlus account code or journal structure — per the governing prompt's hard rule, these are candidate business-meaning descriptions only. The reference ERP is never named; it is referred to only as "the reference ERP," consistent with clean-room rule (no vendor/product token, no ORM/table identifier, no fenced code block — all account-flow patterns below are expressed as prose and tables).

---

## 2. Evidence Layer Discipline

Layer A = reference ERP official documentation, versions 13.0–19.0. Layer B = Thai statutory position, `HOLD / EVIDENCE REQUIRED` throughout (routed to file `24`). Layer C = SMEsPlus candidate business-meaning language only, never a final posting rule.

---

## 3. Archetype A — Purchase Order Confirmation (Commitment, Pre-Financial)

**REFERENCE OBSERVATION.** Confirming a purchase order is documented, across the material reviewed, as creating a procurement commitment and (where enabled) a scheduled receipt — it is not documented as generating a financial (Balance Sheet/P&L) journal entry in either valuation pattern. Financial effects begin at receipt (Perpetual) or at vendor-bill posting (Periodic), not at order confirmation.
— *Reference ERP official documentation — Inventory Valuation / Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02.* Fact Status: `PROVISIONAL` — absence-of-entry is inferred from the documented account-flow tables/descriptions beginning at receipt/bill, not from an explicit "no entry at order confirmation" statement located in this pass.

**ACCOUNTING MEANING.** Order confirmation is a **commitment fact**, not a cost-acquisition fact. It is identical in financial substance under both Periodic and Perpetual — no capitalization, no expense, in either pattern — because no title/risk/cost transfer or delivery has occurred yet.

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED` — Thai practice around off-balance-sheet purchase-commitment disclosure (if any, e.g., for material outstanding commitments) not verified here.

**SMEPLUS CANDIDATE / HOLD.** Candidate language only: a "purchase commitment fact" (vendor, product, quantity, agreed unit cost, expected receipt date) distinct from any later cost-acquisition or capitalization fact. No account implication. `HOLD.`

---

## 4. Archetype B — Receipt Validation / Inventory Capitalization

### 4.1 Under Perpetual

**REFERENCE OBSERVATION.** Documentation (and corroborating community technical material describing the same documented pattern) describes receipt under Perpetual as posting a debit to a Stock/Valuation-side account and a credit to an interim "Stock Input" account — described in the material reviewed as "Stock Interim (Received)" by default — representing a recognized inventory-asset increase and an offsetting vendor obligation **not yet recorded as a formal bill**.
— *Reference ERP official documentation — Inventory Valuation / Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02* (account-role descriptions: "Stock Input/Output: Intermediate accounts for perpetual method"); corroborated by community-sourced technical description of the same "Stock Interim (Received)" mechanic (secondary evidence only, not authoritative), retrieved 2026-09-02. Fact Status: `PROVISIONAL` — the account-role concept (an interim/received account bridging receipt and bill) is corroborated by two independent-source descriptions; the literal debit/credit account-name pairing is not independently confirmed against a single fetched raw documentation page and should be treated as pattern-level evidence, not a verified journal template.

**ACCOUNTING MEANING.** This is the direct answer to "when is purchase cost first capitalized" under Perpetual: **at receipt validation**, the moment physical stock enters, cost is recognized as an asset — before any vendor bill exists. The interim account exists precisely to hold the "goods received, not yet invoiced" position as a visible, named balance rather than an invisible gap discovered only at period end (contrast with the Periodic pattern's documented absence of an equivalent mechanism — file `12` §6).

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED` — whether Thai practice/tax rules require a distinct "goods received not invoiced" liability presentation, or permit it collapsed into trade payables, is not verified here.

**SMEPLUS CANDIDATE / HOLD.** Candidate language only: a "receipt-triggered capitalization fact," carrying quantity, unit cost basis (from the purchase order/expected cost, since no bill exists yet), location, and a reference back to the purchase commitment fact (§3). Whether SMEsPlus adopts a visible interim-liability concept analogous to what is documented here, or a different mechanism, is unresolved. `HOLD — JT-01 / JT-06.`

### 4.2 Under Periodic

**REFERENCE OBSERVATION.** As established in file `12` §4.3, receipt under Periodic is documented as a physical/quantity-only event with no confirmed dedicated financial entry at the moment of receipt; no interim "received not invoiced" account was confirmed as part of the Periodic pattern in the material reviewed.
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02.* Fact Status: `PROVISIONAL`.

**ACCOUNTING MEANING.** Under Periodic, receipt validation does **not** capitalize cost. Capitalization (in the sense of an asset-side figure) only emerges as a derived by-product of the closing entry (file `12` §4.7–§4.8), and even then indirectly, via the physical count feeding the Variation Account — not as a discrete "this receipt is now an asset" posting.

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED`.

**SMEPLUS CANDIDATE / HOLD.** `HOLD` — same receipt quantity fact as Perpetual (§4.1) can be emitted by Inventory in both patterns; what differs is purely what Accounting chooses to do with it, consistent with "Inventory emits facts, Accounting decides postings." No candidate posting difference is prescribed here.

---

## 5. Archetype C — Vendor Bill Posting

### 5.1 Under Perpetual

**REFERENCE OBSERVATION.** Documentation and corroborating material describe vendor-bill posting under Perpetual as clearing the interim "Stock Interim (Received)" balance created at receipt (§4.1): the bill posts a debit to the interim account (offsetting the receipt-time credit) and a credit to Accounts Payable, at the vendor-bill amount.
— Community-sourced technical description of the interim-account clearing mechanic (secondary evidence, corroborating an account-role pattern also referenced in official Valuation Cheat Sheet material), retrieved 2026-09-02; *Reference ERP official documentation — Valuation Cheat Sheet, version 19.0, retrieved 2026-09-02* (general account-role framing). Fact Status: `PROVISIONAL`.

**ACCOUNTING MEANING.** The vendor bill under Perpetual is a **settlement/clearing event**, not a fresh capitalization event — capitalization already happened at receipt (§4.1). The bill's role is to convert the informal "received, not billed" position into a formal payable and to true up cost if the bill amount differs from the receipt-time cost basis (§6).

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED`.

**SMEPLUS CANDIDATE / HOLD.** Candidate language only: a "vendor bill posting fact" that references the receipt-triggered capitalization fact (§4.1) it is clearing, carrying the final invoiced amount, tax treatment, and any variance. `HOLD — JT-06.`

### 5.2 Under Periodic

**REFERENCE OBSERVATION.** As established in file `12` §4.2, the vendor bill under Periodic is documented as posting an ordinary expense-by-nature entry; it is the point at which cost first becomes financially visible at all under Periodic (no prior receipt-time entry exists to clear).
— *Reference ERP official documentation — Inventory Valuation, version 19.0, retrieved 2026-09-02.* Fact Status: `PROVISIONAL`.

**ACCOUNTING MEANING.** Under Periodic, the vendor bill is the **primary, first cost-acquisition event**, not a clearing event — there is nothing to clear because receipt created no financial entry (§4.2). This is the structural inverse of the Perpetual pattern's roles for the same two events.

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED`.

**SMEPLUS CANDIDATE / HOLD.** `HOLD.`

---

## 6. Archetype D — Price Variance (Purchase Order / Receipt Cost vs. Vendor Bill Cost)

**REFERENCE OBSERVATION.** Documentation and corroborating material describe a dedicated **Price Difference Account**, stated to apply specifically under the Perpetual/Anglo-Saxon-labelled pattern, used to absorb the variance when the vendor-bill amount differs from the cost basis already recognized at receipt. Two distinct variance mechanics are described depending on costing method: with FIFO or average costing, the variance is measured against "the PO price at the time the goods were received"; with standard costing, the variance is measured against "the standard cost." The account is documented as configured at the product-category level (with product-level override available, consistent with the general category/product inheritance pattern), defaulting to blank, with official guidance recommending an expense-type account be set. Community-sourced material also notes this account was removed from a later major version and subsequently reinstated, indicating version instability in its availability.
— *Reference ERP official documentation — Average Price on Returned Goods, version 19.0, retrieved 2026-09-02* (Price Difference Account role and costing-method-dependent variance basis); corroborated by community-sourced material on category-level configuration and the removal/reinstatement history (secondary evidence, version-instability corroboration only), retrieved 2026-09-02. Fact Status: `PROVISIONAL` for the mechanic description; `PROVISIONAL — VERSION DELTA FLAGGED` for the removal/reinstatement claim (secondary-sourced only, exact version numbers of removal and reinstatement not independently confirmed against an official changelog in this pass).

**ACCOUNTING MEANING.** This is the direct answer to "vendor bill price differs from cost": under Perpetual, the variance between what was capitalized at receipt (§4.1, using PO/expected cost or standard cost) and what the vendor actually billed is **not silently absorbed into the Inventory Asset figure** — it is routed to a separate, named variance account, keeping the Inventory Asset carrying value aligned to a consistent costing policy (PO/receipt cost, or standard cost) rather than fluctuating with every vendor's actual invoiced price. Under standard costing specifically, this is the textbook "purchase price variance" pattern; under FIFO/average costing, it is a narrower "did the bill match what we already recorded at receipt" true-up.

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED` — Thai tax/statutory treatment of purchase price variance (expensed immediately vs. allocated back into inventory cost) is not verified here; this is a materially significant Layer B question because it directly affects taxable cost of sales. Routed to file `24` with elevated priority.

**SMEPLUS CANDIDATE / HOLD.** Candidate language only: a "purchase price variance fact," carrying the receipt-time cost basis, the final billed cost, the delta, and the costing method in force at the time, without prescribing whether SMEsPlus routes the delta to a variance account, restates the Inventory Asset, or allocates it back across remaining on-hand quantity. This last point (immediate variance recognition vs. inventory-cost restatement) is explicitly `HOLD — JT-02 / JT-06`, and is flagged as a genuine open design fork, not a detail.

**Periodic note.** No equivalent named Price-Difference mechanism was confirmed for the Periodic pattern in the material reviewed — under Periodic, a bill-vs-PO price difference is simply part of whatever amount posts as the period's purchase expense-by-nature (file `12` §4.2); it has no separate visibility until the close absorbs the net effect into the Variation Account. This asymmetry (named variance account under Perpetual; no confirmed equivalent under Periodic) is itself a material finding, consistent with file `12` §6's receipt/bill-gap asymmetry finding. `HOLD.`

---

## 7. Timing Matrix — Receipt-Before-Bill / Bill-Before-Receipt / Same-Period

| Scenario | Perpetual (Layer A observation) | Periodic (Layer A observation) | Fact Status |
|---|---|---|---|
| **Receipt before bill** (most common) | Receipt capitalizes cost immediately via the interim account (§4.1). Inventory Asset and the interim liability are both live before any bill exists. When the bill later posts, it clears the interim balance and posts any price variance (§6). Inventory Asset is correct (at receipt-time cost basis) even while unbilled. | Receipt has no confirmed financial entry (§4.2). No interim liability is visible. The unbilled-but-received position exists only physically until either (a) the bill eventually posts (making it a same-period or later-period purchase expense) or (b) a close occurs first, in which case the physical count includes stock the financial ledger does not yet reflect — absorbed into the Variation Account (file `12` §6). | `PROVISIONAL` |
| **Bill before receipt** (e.g., prepayment, drop-ship timing, advance billing) | Not directly confirmed in the material reviewed for this pass. By structural inference from the documented interim-account mechanic (§4.1/§5.1), a bill with no prior receipt would have no interim receipt-side balance to clear — implying either the bill posts against a different (non-interim) payable/prepayment treatment, or the system defers full recognition until receipt occurs. **This is not confirmed and is flagged `HOLD`, not assumed.** | Bill posts its expense-by-nature entry regardless of physical receipt status (file `12` §4.2/§5 row 7) — the Periodic pattern's documented behavior is that the financial (bill) and physical (receipt) sides are independent, so a bill-before-receipt case behaves, financially, no differently from a normal bill posting; the physical-side gap is only surfaced at the next physical count/close. | `HOLD` (Perpetual sub-case); `PROVISIONAL` (Periodic sub-case) |
| **Same period (receipt and bill both occur before close, ordinary case)** | Interim account opens and clears within the same period; any price variance posts within the period (§6). Inventory Asset reflects final, bill-trued-up cost by period end. | Both receipt (no entry) and bill (expense-by-nature entry) occur within the period; at close, the physical count and the accumulated purchase-expense total (which now includes this bill) are reconciled together — ordinary case, lowest evidence risk. | `PROVISIONAL` |

**Cross-cutting observation.** The **bill-before-receipt** sub-case under Perpetual is the weakest evidence point in this file — it was not directly documented in the material reviewed, only inferred by structural symmetry with the receipt-before-bill case. This should not be treated as confirmed reference-ERP behavior. It is listed explicitly in §10 as a material HOLD requiring a dedicated follow-up fetch (e.g., against a page specifically describing prepayment or bill-only purchase flows) before any SMEsPlus candidate is drafted for that sub-case.

---

## 8. Archetype E — Landed Cost Interaction With Purchase-Side Capitalization (Brief Cross-Reference)

**REFERENCE OBSERVATION.** Documentation describes a landed-cost mechanism that adds shipment, insurance, customs-duty, and similar costs to a product's valuation after the original purchase-order cost, via a dedicated landed-cost record that can be generated from a vendor bill and allocated across the affected receipt lines using a selectable method (equal split, by quantity, by current cost, by weight, or by volume); the landed-cost record is validated separately and posts its own accounting entry.
— *Reference ERP official documentation — Landed Costs, version 19.0 (also present at versions 14.0 through 18.0 per documentation index), retrieved 2026-09-02.* Fact Status: `VERIFIED` for the existence and general mechanic; `HOLD` for the specific journal/account treatment when landed cost arrives after partial or full sale of the affected units (full treatment is file `21`'s scope, not duplicated here).

**ACCOUNTING MEANING.** Landed cost is a **second, later capitalization event** layered onto the original receipt-time capitalization (§4.1) or the original bill-time expense (§5.2), depending on valuation pattern. It is evidence that "purchase cost" is not always a single, atomic event even within the purchase-side lifecycle — a receipt can be capitalized once at receipt, trued up again at bill (§6), and adjusted a third time by landed cost, all for the same physical unit.

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED` — Thai treatment of import duty, freight capitalization, and recoverable VAT distinction (explicitly named in governing prompt §13) is a materially significant Layer B question not resolved here. Routed to file `24` and file `21`.

**SMEPLUS CANDIDATE / HOLD.** `HOLD` — full candidate treatment deferred to file `21` to avoid duplicating scope.

---

## 9. Archetype F — Closing-Time Treatment of Unbilled Receipts / Unreceived Bills (Purchase-Side Accrual Question)

**REFERENCE OBSERVATION.** No single confirmed documentation passage in the material reviewed states, in exact terms, how the reference ERP treats a still-open interim "received, not billed" balance (Perpetual pattern, §4.1) at period close, nor how Periodic's absorbed-into-Variation-Account treatment (file `12` §4.8) is distinguished from an ordinary period-end accrual in statutory reporting terms.
Fact Status: `HOLD` — this is a genuine evidence gap, not a paraphrase-risk item.

**ACCOUNTING MEANING.** Both patterns leave an open question at closing time about "goods received not invoiced" (a standard accrual concept in general accounting practice, sometimes abbreviated in professional literature, though no such abbreviation is used here per clean-room rule): whether it remains a live, unreversed interim balance carried into the next period (Perpetual) or is folded into a single period variation figure that does not separately name the unbilled-receipt component (Periodic). Both are plausible readings of what has been confirmed; neither is confirmed as the actual behavior.

**THAI RULE STATUS.** `HOLD / EVIDENCE REQUIRED` — Thai period cut-off and physical-stock-evidence requirements (governing prompt §13) directly bear on this question and are not resolved here.

**SMEPLUS CANDIDATE / HOLD.** Candidate language only: SMEsPlus should treat "does an open receipt-not-billed position survive a period close as a visible balance, or does it get absorbed and lose its identity" as an explicit design question for `JT-06`/`JT-07`, not something to inherit implicitly from either reference pattern. `HOLD — JT-06 / JT-07.`

---

## 10. Consolidated Material HOLD List (This File)

1. `HOLD — MOST MATERIAL.` Bill-before-receipt under Perpetual is not directly documented in the material reviewed; only inferred by structural symmetry (§7). No SMEsPlus candidate should be drafted for this sub-case without a dedicated follow-up fetch against a page specifically addressing prepayment/bill-only purchase flows.
2. `HOLD.` Price Difference Account removal-and-reinstatement version history is secondary-sourced only; exact version numbers not confirmed against an official changelog (§6).
3. `HOLD.` No confirmed Periodic-pattern equivalent to the Perpetual interim "received, not billed" account exists in the material reviewed — asymmetry noted but not resolved (§4.2, §6, §9).
4. `HOLD.` Purchase price variance's ultimate tax/statutory treatment in Thailand (immediate expense vs. inventory-cost allocation) — elevated priority, directly affects taxable cost of sales (§6).
5. `HOLD.` Closing-time survival/absorption of an open unbilled-receipt balance is not confirmed for either pattern (§9).
6. `HOLD.` All Layer B (Thai) rows throughout; routed to file `24`.

---

## 11. Cross-Reference to Open Joint Decisions

| Joint ID | Relevance in this file |
|---|---|
| `JT-01` | Category/product ownership of the Price Difference Account and interim-account configuration (§4.1, §6) feeds valuation-policy-ownership evidence; not resolved here. |
| `JT-02` | Costing-method-dependent variance basis (FIFO/average vs. standard) directly shapes what "price variance" even means (§6); full costing-method proof remains file `15`'s scope. |
| `JT-06` | Directly and repeatedly fed by this file — late supplier bill after receipt (§5.1, §9) and bill-before-receipt (§7) are core `JT-06` evidence inputs. Not closed here. |
| `JT-07` | Fed by §9 — whether the purchase-side accrual position survives close as a visible balance is a period-close design input. Not closed here. |

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
