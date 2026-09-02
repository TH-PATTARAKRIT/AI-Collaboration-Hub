# 05 — Menu C: Product Accounting (Income/Expense) Field Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: Evidence-only. Layer 2 controlled research evidence. No PASS/FINAL/APPROVED status is asserted anywhere in this file.

Governing prompt reference: §6 Menu C, §7 Field Evidence Sheet Format. Citation convention `CV-02` and file-status convention `CV-04` from `00_EXECUTION_CHECKPOINT_LOG.md` apply throughout. The reference ERP is never named by product; it is called "the reference ERP" or "the OpenSource reference ERP."

---

## 0. Scope, Menu Path, and a Tab-Boundary Version Delta Found Up Front

Observed menu path: **Product app / Inventory app → Products → Products → (open a product) → Accounting-relevant fields**.

A material structural finding, disclosed before the field-by-field register because it affects how every row below should be read: the governing prompt frames this menu as a single "Accounting Tab." Evidence gathered in this pass indicates the fields the prompt groups under that label are **not consistently co-located in one tab across versions**:

- Earlier-version evidence (`13.0`-era, secondary/community-sourced) describes Income Account and Expense Account as living on a distinct "Accounting" tab of the product form, with Customer/Sales-side tax fields appearing separately on the "General Information" tab and vendor/purchase-side tax fields on the "Purchase" tab.
- Later-version evidence (`17.0`/`18.0`-era) describes "Customer Taxes" and "Vendor Taxes" as living inside the "Sales" and "Purchase" tabs respectively, with no directly confirmed statement of where Income Account/Expense Account render in those same versions (most likely still under a "General Information"/"Accounting" grouping, but this was **not directly confirmed by a primary-documentation quote** in this pass).
- Field labels themselves also shifted: "Sales Taxes"/"Purchase Taxes" (older, and the labels the governing prompt uses) vs. "Customer Taxes"/"Vendor Taxes" (observed in later-version search evidence).

This is classified `PROVISIONAL / HOLD` as a named version-delta item rather than silently normalized. All fields below are therefore registered by **function**, with the "Menu Path" cell stating the best-evidenced tab location per version band and flagging where that location is unconfirmed.

Layer B (Thai evidence) is `N/A` in this file — see deliverable `24`. Cross-references: `JT-01`, `JT-02`, `JT-04` (this file is the second primary evidence surface for JT-04, alongside file `04`), `JT-05`/`C-03`. Foundational rule held throughout: Inventory emits facts; Accounting decides postings.

---

## 1. Field C-01 — Income Account (Product-Level)

| Attribute | Value |
|---|---|
| Menu Path | Product form, Accounting/General-Information grouping (exact tab boundary version-dependent — see §0). Confirmed path segment: Products → Products → open product → account-properties fields. |
| Field Label | "Income Account" |
| Purpose | Overrides, for this specific product only, the account credited for the tax-exclusive amount at customer invoice validation |
| Values / Options | Any account from the chart of accounts; blank is a valid state |
| Default | Blank at product creation — inherits the category's Income Account (file `04`, field `B-03`) when blank |
| Visibility | Present on the product form once accounting features are enabled for the user (same gate discussed in file `04`, field `B-00`) |
| Scope | Product (single product record), within the company context of the account selected |
| Inherits From | Product Category's Income Account (`B-03`), used only when this field is blank |
| Override Precedence | **Product wins over Category.** Directly evidenced: "products inherit their Income Account and Expense Account from their product category, but these accounts can be overridden on each product record," and "if there is an income/expense account defined in the accounting tab on the product, [the reference ERP] will use this account." A further fallback layer below Category — a Journal-level default — was reported in secondary/community evidence but not confirmed in official documentation; treated as `PROVISIONAL` (see §5 below for the full precedence discussion). |
| Transaction Consumer | Customer invoice validation (same event as category-level Income Account, per file `04` field `B-03`) |
| Periodic Behavior | Same trigger regardless of Periodic/Perpetual — Income Account resolution is orthogonal to the valuation-timing toggle |
| Perpetual Behavior | Same trigger as Periodic |
| Account Type Impact | Revenue/Income |
| Financial Statement Impact | P&L (revenue line) |
| Change Impact | Whether changing the product-level override after invoices have already posted against the old account affects those historical entries: **not found** — `HOLD / EVIDENCE REQUIRED`. Reference evidence strongly implies **future transactions only** are affected (accounts are resolved at the moment of the triggering transaction, not retroactively recalculated), but no documentation passage states this as an explicit guarantee — kept `PROVISIONAL`, not `VERIFIED`. |
| Version Delta | Override mechanism and direction (Product > Category) is stable across all versions with usable evidence; exact tab location is the version delta already flagged in §0 |
| Evidence | Reference ERP official documentation — get-started (income/expense account definitions) and community-corroborated product/category hierarchy evidence, versions 13.0–19.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for override direction and trigger event; `PROVISIONAL` for future-only-effect assumption and exact tab placement; `HOLD` for historical-transaction re-resolution mechanics |

---

## 2. Field C-02 — Expense Account (Product-Level)

| Attribute | Value |
|---|---|
| Menu Path | Same grouping as `C-01`, adjacent field |
| Field Label | "Expense Account" |
| Purpose | Overrides, for this specific product only, the account used for the cost side of the product's lifecycle — subject to the same Continental/Anglo-Saxon and Periodic/Perpetual dependency documented at category level in file `04`, field `B-04` |
| Values / Options | Any account from the chart of accounts; blank is a valid state |
| Default | Blank at product creation — inherits the category's Expense Account when blank |
| Visibility | Present once accounting features are enabled (same gate as `C-01`) |
| Scope | Product |
| Inherits From | Product Category's Expense Account (`B-04`) |
| Override Precedence | **Product wins over Category**, identically to Income Account — directly evidenced by the same source passage covering both fields together. This override is a single mechanism, not two independent ones: "if you want to set different Income/Expense accounts for a product than its product category accounts, you can open the product and in the Accounting tab set the accounts, which will override the category accounts when selling/purchasing this product." |
| Transaction Consumer | **Same event dependency as category-level Expense Account** (file `04`, field `B-04`): vendor bill validation under Continental; two-stage delivery-then-invoice clearing under Anglo-Saxon Automated (Perpetual); capitalized-until-close under Anglo-Saxon Manual (Periodic). The product-level override does not change *which event* consumes the account — it only changes *which account value* that event uses. |
| Periodic Behavior | Same as category-level `B-04` Periodic row: not expensed at transaction moment; held as asset value until period-end closing/variation entry |
| Perpetual Behavior | Same as category-level `B-04` Perpetual row: physical/asset-side value moves at delivery; P&L expense (COGS) recognized when clearing against the corresponding customer invoice — with the same `CONFLICTING` version-19.0 caveat carried over from file `04` |
| Account Type Impact | Same configuration-dependent type rule as `B-04` (Expenses/Cost of Revenue vs. Stock Valuation/Current Assets, depending on Anglo-Saxon/Continental and Manual/Automated) |
| Financial Statement Impact | Both — transiently Balance Sheet, ultimately P&L, same as `B-04` |
| Change Impact | Same `HOLD` as `C-01` — historical-transaction re-resolution effect not found |
| Version Delta | Same `CONFLICTING` 19.0 item inherited from `B-02`/`B-04` |
| Evidence | Reference ERP official documentation — get-started and inventory valuation configuration pages, versions 13.0–19.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for override direction; inherits `PROVISIONAL`/`CONFLICTING` status from `B-04` for the underlying event-timing mechanics |

---

## 3. Field C-03 — Sales Taxes / Customer Taxes

| Attribute | Value |
|---|---|
| Menu Path | Product form — "General Information" or "Sales" tab depending on version band (see §0); **not** confirmed to be co-located with Income/Expense Account in every version |
| Field Label | "Sales Taxes" (older-version evidence) / "Customer Taxes" (later-version evidence) — treated as the same functional field under two label generations |
| Purpose | Sets the default tax(es) applied to sale transaction lines for this product |
| Values / Options | Zero, one, or multiple tax records from the company's tax configuration |
| Default | Not confirmed against official documentation whether a reference-wide default exists (e.g., a company-level default tax) versus the field starting blank — `HOLD` |
| Visibility | Present when the product is sellable / the Sales app or sales capability is enabled on the product (evidenced indirectly: "the Invoicing Policy field... only appears when the Sales app is installed and the product has the Sales checkbox enabled" — the same enabling condition is presumed, not confirmed, to gate the Customer/Sales Taxes field; `PROVISIONAL`) |
| Scope | Product |
| Inherits From | **Not confirmed as inheriting from Product Category.** This is a material and explicit contrast with Income/Expense Account: no documentation passage found in this pass states that tax defaults flow from category to product the way Income/Expense Account do. Absent that confirmation, this field is treated as product-own-value, not category-inherited — `HOLD / EVIDENCE REQUIRED` if SMEsPlus later needs to confirm or refute category-level tax inheritance in the reference. |
| Override Precedence | Documentation states: "product tax having the highest priority at the time of sales and purchase" — implying taxes resolved from the product record take precedence over some other (unspecified in the fetched excerpt) source, most likely a Fiscal Position or company default, consistent with the separate Fiscal Position tax/account mapping mechanism the reference also documents. The exact precedence order between product-level tax, Fiscal Position mapping, and any company-level default is `HOLD` — not fully traced in this pass. |
| Transaction Consumer | Sales order and/or customer invoice line creation — "product taxes are automatically shown in sale orders or purchase orders when created" |
| Periodic Behavior | Not differentiated by Periodic/Perpetual — tax determination is a revenue/AR-side and statutory-compliance concern, not an inventory-valuation-timing concern |
| Perpetual Behavior | Same as Periodic |
| Account Type Impact | N/A directly (tax fields select tax records, not accounts) — though tax records themselves reference tax-payable/receivable accounts, which is a separate configuration surface not covered by this file |
| Financial Statement Impact | Balance Sheet (tax liability) and disclosure, not P&L revenue/COGS directly |
| Change Impact | Not found |
| Version Delta | Label change ("Sales Taxes" → "Customer Taxes") flagged as a named, not-fully-version-pinned delta; exact version at which the rename occurred was **not isolated** in this pass — `HOLD` |
| Evidence | Reference ERP official documentation and community-corroborated evidence — tax configuration and product tab structure, versions 13.0, 16.0, 17.0, 18.0, retrieved 2026-09-02 |
| Fact Status | `PROVISIONAL` throughout — this field's evidence is weaker than `C-01`/`C-02` because no single fetched page gave a full authoritative description of default sourcing, inheritance, and precedence together |

---

## 4. Field C-04 — Purchase Taxes / Vendor Taxes

| Attribute | Value |
|---|---|
| Menu Path | Product form — "Purchase" tab (both older- and later-version evidence agree the vendor-side tax field lives on a Purchase-labeled tab, unlike the Sales-side field's less certain location) |
| Field Label | "Purchase Taxes" (older-version evidence) / "Vendor Taxes" (later-version evidence, and explicitly located "below Vendor Bills" in one version's forum evidence) |
| Purpose | Sets the default tax(es) applied to purchase transaction lines (vendor bill/purchase order lines) for this product |
| Values / Options | Zero, one, or multiple tax records |
| Default | Not confirmed — `HOLD`, same as `C-03` |
| Visibility | Present when the product is purchasable (Purchase capability enabled on the product) — same evidentiary strength/pattern as `C-03`, `PROVISIONAL` |
| Scope | Product |
| Inherits From | Not confirmed as category-inherited — same `HOLD` as `C-03` |
| Override Precedence | Same "product tax has highest priority" statement applies, sourced from the same combined sales/purchase tax passage; exact precedence against Fiscal Position is `HOLD`, same as `C-03` |
| Transaction Consumer | Purchase order and/or vendor bill line creation |
| Periodic Behavior | Not differentiated by Periodic/Perpetual |
| Perpetual Behavior | Not differentiated by Periodic/Perpetual |
| Account Type Impact | N/A directly (see `C-03` reasoning) |
| Financial Statement Impact | Balance Sheet (tax receivable/recoverable) — this is also the field most directly relevant to the governing prompt's later-file "landed cost / duty / recoverable VAT distinction" concern (§13), which is out of scope for this file beyond flagging the connection |
| Change Impact | Not found |
| Version Delta | Same label-generation delta as `C-03`, mirrored on the purchase side |
| Evidence | Reference ERP official documentation and community-corroborated evidence — tax configuration and product tab structure, versions 12.0, 13.0, 17.0, 18.0, retrieved 2026-09-02 |
| Fact Status | `PROVISIONAL`, same evidentiary caveat as `C-03` |

---

## 5. Field C-05 — Cost / Standard Price

| Attribute | Value |
|---|---|
| Menu Path | Product form, General Information tab (the "Cost" field sits alongside Sales Price, not inside the Accounting-labeled account-properties grouping) |
| Field Label | "Cost" (this is the field the governing prompt refers to as "Standard Cost where relevant") |
| Purpose | Records the unit cost used as the valuation basis when the product's category Costing Method (`B-01`) = Standard Price; also generally usable as a cost-reference figure regardless of costing method for margin/reporting purposes |
| Values / Options | Numeric monetary value |
| Default | Not confirmed as having a non-zero reference-wide default — `HOLD` |
| Visibility | Always visible on the product form's General Information tab |
| Scope | Product (not category — there is no category-level "Cost" figure; Costing Method at category level selects the *method*, while the *value* for Standard Price specifically is this product-level field) |
| Inherits From | N/A — product-owned value, not inherited |
| Override Precedence | N/A — single source of truth per product for this figure |
| Transaction Consumer | Every valuation event when Costing Method = Standard Price: receipts (valued at this figure regardless of actual purchase price), and the Price Difference Account mechanism (`B-08`) when the actual vendor bill price differs from this figure. Under AVCO or FIFO costing methods, this field is **not** the live valuation driver — those methods compute a dynamic average/layer cost instead, though the field may still display/store a reference value. This distinction was not fully re-confirmed by a direct documentation quote for what the field *displays* under AVCO/FIFO (e.g., whether it auto-updates to reflect the computed average) — `HOLD / EVIDENCE REQUIRED`. |
| Periodic Behavior | Same field/value used as the closing-valuation basis under Standard Price costing regardless of Manual/Automated |
| Perpetual Behavior | Same field/value used as the per-transaction valuation basis under Standard Price costing |
| Account Type Impact | Not an account itself; drives amounts posted to Stock Valuation and, on variance, Price Difference Account (`B-05`, `B-08`) |
| Financial Statement Impact | Balance Sheet (inventory carrying value under Standard Price) |
| Change Impact | Whether editing this field revalues existing on-hand stock or only affects future receipts: **not found** — `HOLD / EVIDENCE REQUIRED`. This is the product-level instance of the same consolidated existing-stock-change question raised in file `04` §12. |
| Version Delta | No delta found in field existence or general purpose across versions with usable evidence |
| Evidence | Reference ERP official documentation — product type/general information page, version 18.0, retrieved 2026-09-02; corroborating general knowledge of the Standard Price costing-method dependency established in file `04` field `B-01`/`B-08`, not independently re-fetched from a dedicated "Cost field" documentation page in this pass |
| Fact Status | `PROVISIONAL` — field existence and general role are well-corroborated indirectly through the costing-method evidence chain, but no single fetched page was found that documents the Cost field in isolation with full behavioral detail |

---

## 6. Field C-06 — Invoicing Policy

| Attribute | Value |
|---|---|
| Menu Path | Product form, Sales tab (explicitly **not** the Accounting-labeled grouping — flagged because the governing prompt lists this under "Accounting Tab" scope, but evidence places it on Sales) |
| Field Label | "Invoicing Policy" |
| Purpose | Determines whether a sales order line becomes invoiceable as soon as the order is confirmed, or only once the corresponding delivery is completed |
| Values / Options | "Ordered quantities" and "Delivered quantities" |
| Default | "Ordered quantities" ("Invoice what is ordered" is documented as "the default mode in the Sales app") |
| Visibility | "Only appears when the Sales app is installed and the product has the Sales checkbox enabled" |
| Scope | Product |
| Inherits From | N/A — no category-level equivalent found; this appears to be a product-only setting with no category default source, unlike Income/Expense Account |
| Override Precedence | N/A (single-source field) |
| Transaction Consumer | Sales order confirmation (Ordered quantities policy) or delivery completion (Delivered quantities policy) — gates *when a customer invoice can be created*, which is the same event `C-01`/`C-02` and file `04` field `B-04` identify as the trigger for Income Account credit and (under Anglo-Saxon Automated) Expense/COGS Account clearing |
| Periodic Behavior | Governs invoice creation timing regardless of the inventory-valuation Periodic/Perpetual toggle; the *interaction* is that under Anglo-Saxon Automated (Perpetual) valuation, this field indirectly controls **when COGS is recognized in the P&L**, because that recognition is invoice-triggered (per `B-04`). Under Periodic/Manual valuation, this field has no comparable COGS-timing effect, because Periodic COGS recognition is driven by the period-end closing calculation, not by any single invoice event. |
| Perpetual Behavior | Materially interacts with COGS timing as described above — this is a direct, evidenced mechanism by which a Sales-tab field (not an Accounting-tab field) governs financial recognition timing under Perpetual/Anglo-Saxon configuration, and is flagged as relevant to `JT-04` even though it sits outside the strict "Accounting tab" scope the governing prompt names |
| Account Type Impact | None directly |
| Financial Statement Impact | P&L timing (indirect, via the mechanism above) |
| Change Impact | Not found |
| Version Delta | No functional delta found; option set and default are stable across versions with usable evidence (`13.0` through `19.0` search evidence consistent) |
| Evidence | Reference ERP official documentation — invoicing policy pages, versions 13.0, 15.0, 16.0, saas-15.3, saas-18.2, 19.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for field mechanics and default; `PROVISIONAL` for the specific claim that this field is the *sole* gate on invoice-triggered COGS recognition under Perpetual (plausible and consistent with `B-04`, but not independently confirmed by a single documentation passage stating the connection explicitly) |

---

## 7. Mandatory Question — Product-Level Override and Business-Event Resolution Under Periodic vs. Perpetual

> **"When does the Product-level Income/Expense account override the Product Category default, and which business event uses the resolved account under Periodic and under Perpetual accounting?"**

**When the override applies:** The product-level Income Account and Expense Account fields override the category default whenever they are **not blank**. Resolution is evidenced as a strict two-level fallback, evaluated at the moment a transaction needs an account:

1. If the product's own Income/Expense Account field is set, that value is used.
2. Otherwise, the product's assigned Product Category's Income/Expense Account is used.

A commonly repeated community claim adds a third fallback level below Category — a Journal-configured default account — used only if both Product and Category are blank. This third level is `PROVISIONAL`: it is repeated across several independent forum threads but was **not confirmed against a primary official-documentation passage** in this research pass. It is recorded here because leaving it out entirely would understate what a blank-Category, blank-Product configuration actually does (community evidence, and one forum thread title itself, "please define income account for this product," suggests the reference can also simply **error/block posting** if no account resolves at all — implying the Journal fallback may be conditional or version-dependent rather than universal). This is classified `HOLD / EVIDENCE REQUIRED` — SMEsPlus must not assume a silent three-level fallback always succeeds; it may instead be a hard stop requiring explicit configuration, which is arguably the more control-conscious behavior and worth independently evaluating on its own merits regardless of what the reference does.

Separately, a **Fiscal Position** mechanism (tax and account mapping, documented as its own feature) can substitute a different account than the one resolved by the Product/Category/Journal chain above, for a given customer or vendor. The order in which Fiscal Position mapping is applied relative to the Product-level override — i.e., whether Fiscal Position can override even an explicit product-level Income/Expense Account, or only ever substitutes for the Category/Journal fallback levels — was **not confirmed** in this pass. `HOLD / EVIDENCE REQUIRED`.

**Which business event uses the resolved account, under each valuation mode:**

| Account | Periodic (Manual) — triggering event | Perpetual (Automated) — triggering event |
|---|---|---|
| Income Account (resolved Product > Category [> Journal, `PROVISIONAL`] [, subject to Fiscal Position, order `HOLD`]) | Customer invoice validation. Not differentiated by the valuation toggle — Income Account resolution and posting timing is identical whether the category uses Periodic or Perpetual inventory valuation, because Income Account sits on the revenue/AR side of the transaction, not the inventory-cost side. | Customer invoice validation — identical trigger and timing to Periodic. No evidence was found of any divergence. |
| Expense Account (resolved Product > Category [> Journal, `PROVISIONAL`] [, subject to Fiscal Position, order `HOLD`]) | Vendor bill validation, under Continental configuration (cost expensed by nature at purchase). Under Anglo-Saxon + Manual specifically, the resolved account is instead typed as a Stock Valuation/asset account and is **not** expensed at bill posting — it is capitalized and only becomes an expense figure through the period-end closing/stock-variation calculation (file `04`, field `B-04`; full lifecycle in files `12`/`17`). | Two-stage, Anglo-Saxon + Automated: the **inventory asset value** moves at the **delivery** event (debiting a Stock Interim/Output holding account, which is a different account from the resolved Expense Account itself), while the **resolved Expense Account is only actually debited (COGS recognized in the P&L) at customer invoice posting**, when that posting clears the Stock Interim (Delivered) holding balance. Under Continental + Automated, the resolved Expense Account is instead debited at vendor bill validation, matching the Continental/Manual trigger — the Automated/Manual toggle in Continental mode changes *whether other accounts (Stock Valuation etc.) also post automatically*, not *which event triggers the Expense Account itself*. **This entire Perpetual/Anglo-Saxon two-stage description carries the `CONFLICTING` status inherited from file `04` fields `B-02`/`B-04`** regarding a 19.0 documentation claim that Perpetual valuation was changed to "impact the stock valuation account at the invoice level" — if that claim is confirmed on independent re-verification, the delivery-triggered asset movement described here would need to be re-stated for 19.0 specifically. |

**Summary answer:** The override rule itself (Product beats Category when non-blank) is `VERIFIED` and is identical in mechanism for both Income and Expense Account, and identical in mechanism for both Periodic and Perpetual — the valuation-timing toggle does not change *whether* the override applies, only *what event(s) consume the resulting Expense Account value* once resolved. Income Account resolution-and-consumption is invoice-triggered in both modes. Expense Account resolution-and-consumption is genuinely different by mode: bill-triggered (Continental, both toggle states; Anglo-Saxon Manual capitalizes instead of expensing at bill) versus a delivery/invoice two-stage split (Anglo-Saxon Automated) — with the 19.0 status of that two-stage split under active `CONFLICTING` review.

---

## 8. Company Context

| Attribute | Value |
|---|---|
| Scope | The product record itself, and each account it can resolve to, sit within a company context in the same two-layer sense described in file `04` field `B-09`: the product/category configuration may be shared, while the specific account records resolved are company-owned chart-of-accounts entries. |
| Multi-company resolution mechanics | Not independently confirmed for the product level beyond what file `04` already flags as `HOLD` at the category level — this file does not add new evidence beyond that cross-reference. |
| Fact Status | `HOLD`, carried forward from file `04` field `B-09` |

---

## 9. Blank / Default Behavior — Consolidated

| Field | Behavior when blank at product level |
|---|---|
| Income Account | Falls back to Category value; if Category also blank, resolution outcome is `HOLD` (possible Journal fallback, `PROVISIONAL`, or a hard block requiring configuration, also `PROVISIONAL`) |
| Expense Account | Same fallback chain as Income Account |
| Sales/Customer Taxes | Not confirmed to have a category-level fallback at all (§`C-03`) — blank likely means no tax applied by default, but this was not confirmed against documentation — `HOLD` |
| Purchase/Vendor Taxes | Same `HOLD` as Sales/Customer Taxes |
| Cost | Not confirmed whether blank/zero has special valuation handling (e.g., a zero-cost warning or block) versus simply valuing at zero — `HOLD`; this connects to the governing-prompt's later negative/zero-cost exception coverage in deliverable `07` (Menu E) |
| Invoicing Policy | Not blank-able in the same sense — defaults to "Ordered quantities" rather than an empty state |

---

## 10. Precedence When Product and Category Differ

Directly evidenced and `VERIFIED`: when both Product and Category have a non-blank Income Account (or Expense Account) and they **differ**, the Product-level value is used, in full, for every transaction consuming that account, from the moment the product-level value is set onward. No partial-precedence, blending, or conditional-precedence mechanism was found — this is a simple override, not a merge.

What was **not found**: whether the reference surfaces any warning, audit-trail entry, or approval requirement when a product's account diverges from its category's account (i.e., whether divergence is a silently-allowed configuration state or a flagged one). `HOLD / EVIDENCE REQUIRED` — directly relevant to governing-prompt §11 items 3–6 (same/different Income/Expense Account cases) and to deliverable `11`'s required audit-trail column.

---

## 11. Effect on Historical vs. Future Transactions

Every account-resolution field in this file (`C-01`, `C-02`, and by extension `C-03`/`C-04` for taxes) shares the same unresolved question already raised at category level (file `04` §12): reference evidence consistently implies, but never explicitly states, that account/tax resolution happens **at the moment of the triggering transaction** (invoice validation, bill validation, order confirmation) and is therefore naturally future-only in effect — changing a product's override today should not, by the general mechanism described, alter the accounts already recorded on already-posted historical entries, because those entries are static journal records, not live references back to the product configuration. This inference is **architecturally reasonable and consistent with everything found**, but it is an inference, not a directly quoted documentation guarantee, and is therefore held at `PROVISIONAL` rather than `VERIFIED` throughout this file and file `04`.

---

## 12. Fact-Status Roll-Up for This File

| Fact Status | Count of fields/rows carrying this status |
|---|---|
| `VERIFIED` | 5 (C-01 override direction/trigger, C-02 override direction, C-06 field mechanics/default, §7 override-rule summary, §10 override-not-merge finding) |
| `PROVISIONAL` | 9 (C-01 future-only assumption/tab placement, C-02 inherited from B-04, C-03 default/visibility/precedence, C-04 same, C-05 field existence/AVCO-FIFO display, C-06 sole-gate claim, §7 Journal-fallback level, §11 historical/future inference) |
| `HOLD` | 8 material open items (C-01 historical re-resolution, C-03 category-inheritance, C-04 category-inheritance, C-05 existing-stock revaluation and blank/zero handling, §5 company context, §7 Fiscal Position ordering, §9 blank-tax/blank-cost outcomes, §10 divergence audit-trail) |
| `CONFLICTING` | 1 (inherited from file `04`: the 19.0 Perpetual/invoice-level timing claim, carried into §7's Expense Account resolution table) |

No field in this file is marked `PASS`, `FINAL`, or `APPROVED`. No blank material cell was left in any evidence table above.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
