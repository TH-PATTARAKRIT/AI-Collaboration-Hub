# 04 — Menu B: Product Category Accounting Field Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: Evidence-only. Layer 2 controlled research evidence. No PASS/FINAL/APPROVED status is asserted anywhere in this file.

Governing prompt reference: §6 Menu B, §7 Field Evidence Sheet Format. Citation convention `CV-02` and file-status convention `CV-04` from `00_EXECUTION_CHECKPOINT_LOG.md` apply throughout. The reference ERP is never named by product; it is called "the reference ERP" or "the OpenSource reference ERP."

---

## 0. Scope and Menu Path Observed

Observed menu path (consistent across all researched versions unless flagged): **Inventory app → Configuration → Product Categories**, opening the category form's Accounting / Inventory Valuation section (this section is itself gated by an account-features visibility toggle — see field `B-00` below).

Version set researched: `13.0`, `14.0`, `15.0`, `saas-16.4`, `17.0`, `18.0`, `19.0`. Evidence density is uneven across this set (some versions returned usable page content on direct fetch; others required corroborating search-index extraction of the same official documentation source — both are treated as Layer A evidence under `CV-02`, with the weaker-sourced items marked `PROVISIONAL` rather than `VERIFIED`).

Layer B (Thai evidence) is `N/A` in this file by design — Thai statutory mapping belongs to deliverable `24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md`. Nothing in this file should be read as a Thai requirement.

Cross-references: `JT-01` (valuation policy ownership — this whole menu is the primary evidence surface for JT-01), `JT-02` (costing methods — field `B-01`), `JT-04` (COGS recognition timing — fields `B-04`, `B-08`), `JT-05`/`C-03` (return cost basis touching Income/Expense resolution — noted where relevant). Foundational rule held throughout: Inventory emits facts; Accounting decides postings. Nothing below should be read as assigning SMEsPlus posting ownership — it records only what the reference ERP does.

---

## 1. Field B-00 — Visibility Gate on the Accounting / Inventory Valuation Section Itself

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories (Account Properties / Inventory Valuation section) |
| Field Label | Section is not itself a field; its visibility is controlled by a user-level "Show Accounting Features" preference and by whether accounting/invoicing is installed |
| Purpose | Gates whether Income Account, Expense Account, and the Inventory Valuation sub-fields render on the category form at all |
| Values / Options | Shown / Hidden |
| Default | Hidden until the accounting-features preference is enabled for the current user (observed explicitly discussed for a `19.0` Community Edition case) |
| Visibility | Conditional — requires Settings → Users → (user) → "Show Accounting Features" enabled, in addition to an accounting/invoicing app being installed |
| Scope | User preference (not company, not category) |
| Inherits From | N/A |
| Override Precedence | N/A |
| Transaction Consumer | None directly — this is a UI-rendering gate, not a posting field |
| Periodic Behavior | Same gate applies regardless of Periodic/Perpetual selection |
| Perpetual Behavior | Same gate applies regardless of Periodic/Perpetual selection |
| Account Type Impact | None (UI-only) |
| Financial Statement Impact | None directly |
| Change Impact | N/A |
| Version Delta | Explicitly confirmed as a live pain point in `19.0` Community Edition forum evidence ("Account Properties group missing on product categories" → resolved by enabling the user preference). Whether this same gate condition existed identically in `13.0`–`17.0` is `PROVISIONAL` — earlier-version documentation describes the fields as present without discussing the toggle, which is not proof the toggle was absent, only that it was not the documentation's focus. |
| Evidence | Reference ERP official documentation and community support evidence — product category account properties visibility, versions 13.0–19.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for 19.0 Community Edition; `PROVISIONAL` for whether the identical gate mechanism existed in 13.0–17.0 |

Layer C: `CANDIDATE` — SMEsPlus should decide explicitly whether Income/Expense/Valuation account configuration is (a) always visible to any user with category-edit rights, or (b) gated behind a separate accounting-feature toggle as the reference does. The reference's gate is a UI/permission convenience, not an accounting rule, and must not be copied as architecture without a deliberate SMEsPlus permission-model decision. `HOLD` pending that decision.

---

## 2. Field B-01 — Costing Method

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form |
| Field Label | "Costing Method" |
| Purpose | Determines how the reference ERP computes and updates the unit cost used for inventory valuation of every product in the category |
| Values / Options | "Standard Price"; "Average Cost" (AVCO); "First In First Out" (FIFO) — consistently observed as the three selectable options across `13.0` through `19.0` |
| Default | "Standard Price" |
| Visibility | Always visible once the section itself is visible (see `B-00`) |
| Scope | Product Category (all products assigned to the category inherit the method; a per-product costing-method override was not found in any researched version and is treated as `NOT PRESENT` unless later evidence contradicts this) |
| Inherits From | N/A — this is a category-owned, not inherited, field |
| Override Precedence | N/A at category level; product-level override `NOT OBSERVED` |
| Transaction Consumer | Every stock-in/stock-out valuation event: receipts, deliveries, manufacturing consumption/output, inventory adjustments, and — for Standard Price specifically — vendor bill price-variance handling (`B-06`) |
| Periodic Behavior | Costing Method still determines the unit cost figure used at period-end stock valuation/closing even though no automatic entry fires per transaction |
| Perpetual Behavior | Costing Method determines the unit cost figure used at each automatic journal entry generated per stock move |
| Account Type Impact | Indirect — selects which downstream account behavior applies (notably, Standard Price is a precondition for the Price Difference Account, `B-08`) |
| Financial Statement Impact | Both — directly shapes Balance Sheet inventory carrying value and, through cost release, P&L cost recognition |
| Change Impact | Documentation explicitly warns that "changing the costing method greatly impacts inventory valuation" and recommends accountant consultation before changing it; the exact mechanics of what happens to *existing on-hand stock value* at the moment of a method change (automatic revaluation vs. no change until next movement) were **not found** in the fetched documentation excerpts — `HOLD / EVIDENCE REQUIRED` |
| Version Delta | Option set and default (Standard Price) are stable `13.0`→`19.0` in every version successfully retrieved. No version was found that added, removed, or renamed a costing-method option. |
| Evidence | Reference ERP official documentation — inventory valuation configuration / automatic inventory valuation, versions 13.0, 15.0, saas-16.4, 17.0, 18.0, 19.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for option set/default; `HOLD` for existing-stock conversion mechanics |

Layer C: `CANDIDATE` — treat "Costing Method" as a JT-02 input, not a settled SMEsPlus decision. The HOLD on existing-stock conversion mechanics is material: SMEsPlus must not assume the reference silently revalues stock on a method change; evidence says only that it is risky, not what actually happens numerically.

---

## 3. Field B-02 — Inventory Valuation (Manual/Periodic vs Automated/Perpetual)

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form, Inventory Valuation sub-section |
| Field Label | "Inventory Valuation" |
| Purpose | Selects whether stock movements generate real-time accounting journal entries or whether valuation is reconciled periodically by manual entry |
| Values / Options | "Manual" and "Automated" in the naming used by `13.0`–`18.0` documentation. `19.0` documentation additionally frames the same choice using "Perpetual (at invoicing)" and "Periodic (at closing)" language layered onto the Manual/Automated toggle — this is a **terminology-level version delta**, treated as `PROVISIONAL` because it was observed via a single documentation-derived summary rather than a directly quoted field label from a `19.0` page fetch |
| Default | "Manual" |
| Visibility | Always visible once the section is visible (`B-00`) |
| Scope | Product Category |
| Inherits From | N/A |
| Override Precedence | N/A — no product-level override of this field was found |
| Transaction Consumer | All physical stock movements (receipts, deliveries, transfers, adjustments, manufacturing) when Automated; period-end manual journal entry only when Manual |
| Periodic Behavior | "Manual" is the reference's own name for what this programme calls Periodic: "the accounting team posts journal entries based on physical inventory of the company, and warehouse employees take the time to count the stock" — no automatic entry at the moment of any stock move |
| Perpetual Behavior | "Automated" is the reference's own name for Perpetual: "when a product enters or leaves your stock, an accounting entry will be automatically created… your accounting books are always up-to-date" |
| Account Type Impact | Directly gates whether Stock Valuation, Stock Journal, Stock Input, and Stock Output accounts (`B-05`–`B-07`) are even used/visible |
| Financial Statement Impact | Both — timing of Balance Sheet inventory updates and P&L cost recognition differ materially between the two modes (full lifecycle detail is out of scope for this file; see files `12`/`13`/`14`) |
| Change Impact | Not found in fetched evidence what happens to historical, already-posted transactions if a category is switched from Manual to Automated (or back) mid-stream — `HOLD / EVIDENCE REQUIRED` |
| Version Delta | `19.0` documentation contains a materially important and only partially corroborated claim: that the Perpetual method "impacts the stock valuation account at the invoice level" rather than at each stock movement, described as a "significant shift" introduced in version 19. This directly contradicts the interim-account mechanism observed and well-corroborated for `13.0`–`18.0` (see `B-06`/`B-07`, where the stock/inventory asset value moves at the delivery/receipt event, and only the P&L expense recognition waits for invoice). This is flagged `CONFLICTING` and must not be silently resolved — it is material to `JT-04`. |
| Evidence | Reference ERP official documentation — inventory valuation configuration, versions 13.0, 15.0, saas-16.4, 17.0, 18.0, retrieved 2026-09-02; version 19.0 valuation cheat sheet and get-started page, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for the Manual/Automated mechanism and default in 13.0–18.0; `CONFLICTING` for the precise 19.0 timing claim — requires direct field-level re-verification against a live 19.0 instance or a fuller documentation fetch before any SMEsPlus candidate relies on it |

Layer C: `HOLD` on the 19.0 timing claim specifically. This is the single most material open item in this file — see closing summary.

---

## 4. Field B-03 — Income Account

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form, Account Properties |
| Field Label | "Income Account" |
| Purpose | Names the account credited for the tax-exclusive amount when a customer invoice referencing a product in this category is validated |
| Values / Options | Any account of a revenue-appropriate type from the chart of accounts (exact type constraint not confirmed — `HOLD`) |
| Default | Not observed to have a reference-wide hard default distinct from whatever the company's chart-of-accounts template seeded; some community evidence indicates a technical configuration-parameter default exists, but this was not confirmed against official documentation — `PROVISIONAL` |
| Visibility | Always visible once the section is visible (`B-00`) |
| Scope | Product Category, itself scoped by company through the account being a company-owned chart-of-accounts entry (see `B-10`) |
| Inherits From | N/A at category level — this is the category's own source-of-default for the product level (see file `05`, field `C-01`) |
| Override Precedence | Category value is the fallback used only when the product-level Income Account is blank (proven in file `05`) |
| Transaction Consumer | Customer invoice validation — confirmed directly: "the Income Account will be used when validating a customer invoice, which means it will hold the details of invoiced amount (without tax)" |
| Periodic Behavior | Same trigger (customer invoice validation) — Income Account recognition is not itself gated by the Periodic/Perpetual valuation toggle, because it is a revenue-side account, not an inventory-cost-side account |
| Perpetual Behavior | Same trigger as Periodic — confirmed no divergence in the evidence found; Income Account resolution appears orthogonal to `B-02` |
| Account Type Impact | Revenue / Income |
| Financial Statement Impact | P&L (revenue line) |
| Change Impact | Effect on already-posted historical invoices when the category's Income Account is changed later was **not found** — `HOLD / EVIDENCE REQUIRED` |
| Version Delta | No option/behavior delta found across `13.0`–`19.0`; mechanism described consistently |
| Evidence | Reference ERP official documentation — get-started / chart of accounts and inventory valuation configuration pages, versions 13.0–19.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for the trigger mechanism; `HOLD` for default-value mechanics and historical-change effect |

Layer C: `CANDIDATE` semantics only — "Income Account resolves at invoice validation" is a reference observation, not a pre-approved SMEsPlus rule. SMEsPlus must independently decide whether revenue-account resolution timing is invoice-based, delivery-based, or order-based, consistent with JT-04 scope (which is framed around COGS/expense timing but the same discipline applies to revenue timing).

---

## 5. Field B-04 — Expense Account

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form, Account Properties |
| Field Label | "Expense Account" |
| Purpose | Names the account debited for the cost side of the product lifecycle — but which cost event actually debits it depends materially on the Periodic/Perpetual and Anglo-Saxon/Continental configuration (see below) |
| Values / Options | Any account from the chart of accounts; the *appropriate account type* differs by configuration mode (below) |
| Default | Not confirmed as reference-wide fixed default; company chart-of-accounts template dependent — `PROVISIONAL` |
| Visibility | Always visible once the section is visible (`B-00`) |
| Scope | Product Category |
| Inherits From | N/A at category level — source of default for product-level override (file `05`, field `C-02`) |
| Override Precedence | Category value is the fallback used only when product-level Expense Account is blank |
| Transaction Consumer | **Materially different depending on configuration** — this is the field most directly relevant to `JT-04`: <br>• Continental accounting (Manual or Automated): Expense Account is debited at **vendor bill validation** — "the Expense Account will be used when validating a vendor bill, which means it will hold the details of tax excluded amount in the vendor bill." <br>• Anglo-Saxon accounting, Manual (Periodic): Expense Account is set to a Stock Valuation / Current Assets type account, i.e. cost is capitalized, not expensed, until the periodic closing entry recognizes stock variation. <br>• Anglo-Saxon accounting, Automated (Perpetual): Expense Account is set to an Expenses/Cost of Revenue type account and is debited at the point the reference clears the Stock Interim (Delivered) holding account — evidenced as occurring at **customer invoice posting**, with the physical inventory-asset decrement itself already having occurred earlier at the **delivery** event (see `B-07`). This two-event split (asset decrement at delivery; P&L expense recognition at invoice) is the reference's actual COGS-timing mechanism and is a primary input to `JT-04`. |
| Periodic Behavior | Cost is not expensed at the transaction moment; carried as Stock Valuation/asset until closing entry converts opening+purchases−closing into a stock-variation/expense figure (full lifecycle in files `12`/`17`) |
| Perpetual Behavior | Two-stage: inventory asset moves at delivery; Expense (COGS) account is only debited when the corresponding customer invoice is posted, via the Stock Interim (Delivered) clearing mechanism |
| Account Type Impact | Expenses/Cost of Revenue (Anglo-Saxon Automated; Continental both modes) or Current Assets/Stock Valuation (Anglo-Saxon Manual) — the account **type expected in this field changes with configuration**, which is itself a material fact SMEsPlus must not flatten into a single universal "COGS account" assumption |
| Financial Statement Impact | Both — P&L (once recognized as expense) and, transiently, Balance Sheet (while held as Stock Valuation/interim) |
| Change Impact | Effect of changing this account after transactions already posted against the old account: **not found** — `HOLD / EVIDENCE REQUIRED` |
| Version Delta | Mechanism (bill-triggered under Continental; invoice-triggered COGS clearing under Anglo-Saxon Automated) is corroborated consistently for `13.0`–`18.0`. The `19.0` "Perpetual impacts stock valuation account at invoice level" claim (see `B-02`) would, if accurate, alter this description materially by moving the *asset*-side event to invoice as well, collapsing the current two-event split into one. This is flagged `CONFLICTING`, not adopted. |
| Evidence | Reference ERP official documentation — get-started (income/expense account definitions), inventory valuation configuration and automatic inventory valuation pages, versions 13.0–19.0; community/forum evidence on Stock Interim mechanics used only as corroborating secondary evidence, not as sole source, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for the Continental (bill-triggered) and Anglo-Saxon Manual (capitalize-until-close) mechanisms; `PROVISIONAL` for the precise Anglo-Saxon Automated two-event (delivery-then-invoice) mechanism, corroborated by a forum secondary source but not by a directly quoted official-documentation passage in this session's fetches; `CONFLICTING` for whether 19.0 changes this |

Layer C: `HOLD` — this field is the single richest source of JT-04 evidence in this file, and also the single most version-uncertain. SMEsPlus must not adopt "Expense Account = COGS, recognized at delivery" or "recognized at invoice" as a blanket rule without first resolving the 19.0 conflict and independently re-deriving the Anglo-Saxon Automated mechanism against a primary documentation quote (not only secondary/forum corroboration).

---

## 6. Field B-05 — Stock / Valuation Account

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form, Inventory Valuation sub-section |
| Field Label | "Stock Valuation Account" |
| Purpose | Holds the current book value of on-hand stock for products in the category |
| Values / Options | Any Current Asset type account |
| Default | Not confirmed as a fixed reference-wide default — company chart-of-accounts dependent |
| Visibility | Appears only when Inventory Valuation (`B-02`) = Automated |
| Scope | Product Category |
| Inherits From | N/A |
| Override Precedence | N/A — no product-level override observed |
| Transaction Consumer | Every automated stock-value-changing event once Automated is selected: receipts, deliveries, adjustments, manufacturing moves, landed cost allocation |
| Periodic Behavior | Not used for automatic postings under Manual (the analogous balance is instead reconciled manually at close) — but the underlying concept of "value of stock on hand" still exists as a reporting figure regardless of mode; only the *automatic posting* to this named account is Automated-only |
| Perpetual Behavior | Directly and continuously updated by automatic journal entries as stock moves |
| Account Type Impact | Current Asset |
| Financial Statement Impact | Balance Sheet |
| Change Impact | Effect of re-pointing this account after historical postings already exist against the old account: **not found** — `HOLD / EVIDENCE REQUIRED` |
| Version Delta | Consistently named and described `13.0`–`18.0`. Not independently re-confirmed for `19.0` beyond the general note that account fields remain configurable on the category form. |
| Evidence | Reference ERP official documentation — inventory valuation configuration, versions 13.0, 15.0, saas-16.4, 18.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` |

Layer C: `CANDIDATE` — the Stock/Valuation Account concept (an asset account tracking on-hand value) is a widely-expected accounting control and is expected to be relevant to SMEsPlus regardless of the reference's specific implementation; final SMEsPlus semantics are `HOLD` pending JT-01.

---

## 7. Field B-06 — Stock Journal

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form, Inventory Valuation sub-section |
| Field Label | "Stock Journal" |
| Purpose | Names the accounting journal into which automatic inventory-valuation journal entries are posted |
| Values / Options | Any journal of appropriate type configured in the company |
| Default | Not confirmed — `HOLD` |
| Visibility | Appears only when Inventory Valuation (`B-02`) = Automated |
| Scope | Product Category |
| Inherits From | N/A |
| Override Precedence | N/A |
| Transaction Consumer | Every automatic valuation entry (receipt, delivery, adjustment, manufacturing, landed cost) — this field only selects *where* the entry posts, not *which* accounts it touches |
| Periodic Behavior | Not applicable under Manual — no automatic entries are generated to route through a journal |
| Perpetual Behavior | Fully applicable — every automatic entry described under `B-04`/`B-05`/`B-07` posts into this journal |
| Account Type Impact | None directly (journal selection, not account selection) |
| Financial Statement Impact | Indirect (audit-trail/reporting grouping only) |
| Change Impact | Not found |
| Version Delta | No delta found across the versions with usable evidence |
| Evidence | Reference ERP official documentation — inventory valuation configuration, version 18.0, retrieved 2026-09-02 |
| Fact Status | `PROVISIONAL` — confirmed present in one version's fetched content; not independently cross-confirmed for every version in the required set |

Layer C: `N/A` — journal-routing is an implementation/reporting convenience, not a recognition-timing or classification decision; no SMEsPlus candidate implied.

---

## 8. Fields B-07a/B-07b — Stock Input Account and Stock Output Account (Interim / Variation Accounts)

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form, Inventory Valuation sub-section |
| Field Label | "Stock Input Account" and "Stock Output Account" (functionally the "Stock Interim (Received)" and "Stock Interim (Delivered)" holding accounts referenced in COGS-timing evidence) |
| Purpose | Hold, transiently, the value of goods that have physically moved but not yet been matched to a vendor bill (input/received side) or a customer invoice (output/delivered side) |
| Values / Options | Any account, typically Current Asset type |
| Default | Not confirmed — `HOLD` |
| Visibility | Appear only when Inventory Valuation (`B-02`) = Automated |
| Scope | Product Category |
| Inherits From | N/A |
| Override Precedence | A location-specific valuation account can override this category-level default for a given stock move, per documentation phrasing ("…unless there is a specific valuation account set on the source/destination location") — this is a `MENU H`-adjacent fact (location-level accounting control) noted here only as a boundary condition, not developed further in this file |
| Transaction Consumer | Stock Input Account: debited at goods receipt (before vendor bill), credited when the vendor bill is later posted. Stock Output Account: debited at goods delivery (before customer invoice), credited when the customer invoice is later posted and the matching Expense/COGS account is debited (see `B-04`) |
| Periodic Behavior | Not used — Manual valuation does not generate the receipt/delivery-triggered interim entries; the periodic model instead recognizes purchase cost by nature at bill posting and reconciles via a period-end stock-variation entry (full detail: files `12`/`17`) |
| Perpetual Behavior | Core mechanism of Perpetual/Automated valuation: these two accounts are exactly the "unbilled receipts" and "uninvoiced deliveries" holding points the governing prompt's Menu F/Scenario-30 language anticipates |
| Account Type Impact | Current Asset (interim/clearing) |
| Financial Statement Impact | Balance Sheet, transiently — documentation explicitly notes these require periodic reconciliation to a zero balance, implying a non-zero balance here is itself a control signal (unbilled receipts / uninvoiced deliveries), not necessarily an error |
| Change Impact | Not found |
| Version Delta | Anglo-Saxon configuration is described consistently `13.0`–`18.0` as setting Stock Input and Stock Output to two *different* Current Asset accounts; Continental configuration sets both to the *same* account. This distinction is corroborated by multiple independently-fetched version pages and is treated as `VERIFIED`. The `19.0` conflicting claim under `B-02`/`B-04` (invoice-level impact) would, if confirmed, change the *timing* but not necessarily the *account-pairing* rule described here — kept as a separate open item rather than assumed resolved. |
| Evidence | Reference ERP official documentation — inventory valuation configuration and automatic inventory valuation pages, versions 13.0, 15.0, saas-16.4, 18.0, retrieved 2026-09-02; community/forum secondary evidence on Stock Interim clearing mechanics, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for the Anglo-Saxon-distinct / Continental-shared account-pairing rule; `PROVISIONAL` for the exact debit/credit choreography (corroborated mainly by secondary forum evidence, not a directly quoted primary-documentation passage) |

Layer C: `HOLD` — this is the reference's concrete mechanism for exactly the "receipt before bill" / "bill before receipt" / "delivery before invoice" / "invoice before delivery" scenario family (governing prompt §10, scenarios 2–6, 12–14). It is highly relevant as *evidence of one possible design*, not as a template to copy; JT-04 and JT-05/C-03 must treat it as one data point.

---

## 9. Field B-08 — Price Difference Account

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories → category form, Inventory Valuation sub-section |
| Field Label | "Price Difference Account" |
| Purpose | Captures the variance between a product's Standard Price (or the price already recorded at receipt) and the price actually billed by the vendor |
| Values / Options | Any account, typically an Expense/variance-type account |
| Default | Not confirmed — `HOLD` |
| Visibility | Conditional — appears only when costing method (`B-01`) = Standard Price **and** Inventory Valuation (`B-02`) = Automated. Confirmed explicitly: "a Price Difference Account can be set for the Product Category" only "when using the Perpetual (at invoicing) valuation method with the Standard Price costing method." |
| Scope | Product Category |
| Inherits From | N/A |
| Override Precedence | N/A — no product-level override found |
| Transaction Consumer | Vendor bill validation, specifically only when the vendor bill's unit price differs from the price already used to value the receipt (Standard Cost, or the Purchase Order price at time of receipt) — documented worked example: goods received and valued at 25, vendor bill posted at 26, the 1-unit variance posts to this account so the bill entry balances against the value already recorded at receipt |
| Periodic Behavior | Not applicable — this account is explicitly gated on Automated valuation; under Manual/Periodic there is no per-transaction price-difference posting (variance is absorbed into the period-end stock-variation calculation instead) |
| Perpetual Behavior | Applies at vendor bill posting whenever billed price ≠ receipt/standard valuation price |
| Account Type Impact | Expense/variance |
| Financial Statement Impact | P&L (variance recognized as expense/income depending on direction) |
| Change Impact | Not found |
| Version Delta | One secondary source describes this mechanism as "re-implemented at version 16 with Standard Cost databases," streamlined to route through the Stock Input (Received) interim account's residual balance rather than posting to a dedicated account in the same way as earlier versions. This is a **material version-delta candidate** but is sourced from a single community thread, not a directly quoted official-documentation passage — `PROVISIONAL`, not `VERIFIED`. |
| Evidence | Reference ERP official documentation — inventory valuation configuration, version 18.0, retrieved 2026-09-02; community/forum secondary evidence on purchase-price-variance mechanics and the version-16 re-implementation, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for the field's existence, visibility gate, and general purpose; `PROVISIONAL` for the exact debit/credit mechanics and for the version-16 re-implementation claim |

Layer C: `HOLD` — directly relevant to governing-prompt Scenario 6 ("vendor bill price differs from receipt/valuation basis"). No SMEsPlus candidate is proposed here; this is evidence only.

---

## 10. Field B-09 — Category / Company Ownership and Scope

| Attribute | Value |
|---|---|
| Menu Path | Inventory → Configuration → Product Categories |
| Field Label | No explicit "Company" field was found on the standard category form in core documentation |
| Purpose | Determines whether a single category record is shared across all companies in a multi-company deployment, or restricted to one |
| Values / Options | N/A in core — multiple independent third-party/community extension modules exist specifically to *add* a company-restriction field to the category, which is itself evidence that core does not ship one |
| Default | Category records are, by default, global/shared across companies in core — evidenced indirectly by the existence and stated purpose of third-party "restrict category to one company" extensions ("leave the Company field empty to make the category shared globally… set it to a specific company to restrict it") |
| Visibility | N/A (no core field) |
| Scope | Global (category record) vs. Company (the accounts the category points to) — these are **two different scopes and must not be conflated**: the category itself is shared, but each Income/Expense/Stock account it references is a company-owned chart-of-accounts entry |
| Inherits From | N/A |
| Override Precedence | N/A |
| Transaction Consumer | N/A directly |
| Periodic Behavior | Not differentiated by this field |
| Perpetual Behavior | Not differentiated by this field |
| Account Type Impact | N/A |
| Financial Statement Impact | N/A directly, but material to multi-company correctness: if a shared category resolves to a company-owned account, and the transaction's company context does not match that account's company, evidence suggests this is exactly the class of error the "please define income account for this product" and "account issue… replaced" forum threads describe |
| Change Impact | N/A |
| Version Delta | Not found — no version was identified in this research pass that added a native company field to the category form |
| Evidence | Reference ERP community/marketplace evidence — multiple independent "product category company/multi-company" extension modules across versions 7.0–18.0, and forum threads on separating categories per company, retrieved 2026-09-02. This is **weaker than official documentation** and is disclosed as such. |
| Fact Status | `PROVISIONAL` — the "no native company field on category" conclusion rests on the *absence* of a documented field plus the *presence* of third-party modules filling that gap, which is reasonable but indirect evidence, not a directly quoted documentation statement that the field is absent. Whether the Income/Expense/Stock/Price-Difference account fields resolve as company-dependent values *on the same shared category record* (i.e., the same category shows different accounts depending on which company is active) was searched for directly and **not confirmed** against official documentation in this pass — `HOLD / EVIDENCE REQUIRED`. |

Layer C: `HOLD` — this is directly relevant to governing-prompt §11 item 10 ("Company A and Company B use different policies/accounts") and to `JT-01`/`JT-09`(multi-tenant). SMEsPlus must not assume the reference's category-sharing model (or its company-dependent account resolution, if that is confirmed later) is correct or required for a Thai multi-company SME context; this is flagged as the second most material open item in this file.

---

## 11. Field B-10 — Inheritance to Product (Summary Pointer)

| Attribute | Value |
|---|---|
| Menu Path | Product Category (source) → Product → Accounting tab (consumer) |
| Field Label | N/A — this is a relationship, not a field |
| Purpose | Establishes the category as the *default source* for Income Account and Expense Account at product level |
| Values / Options | N/A |
| Default | Category values are the default whenever the product-level field is blank |
| Visibility | N/A |
| Scope | Category → Product, one level of inheritance only (no evidence of a deeper hierarchy, e.g. parent-category → child-category inheritance of accounts specifically, though category-nesting itself exists for other purposes — `HOLD` on whether parent-category accounts cascade to child categories that leave their own account fields blank) |
| Inherits From | Product inherits from Category (proven); whether Category inherits from parent Category is `HOLD` |
| Override Precedence | Product > Category (fully detailed and evidenced in file `05`) |
| Transaction Consumer | See `B-03`/`B-04` |
| Periodic Behavior | Same inheritance rule applies regardless of Periodic/Perpetual — inheritance is a configuration-resolution concern, not a posting-timing concern |
| Perpetual Behavior | Same as Periodic |
| Account Type Impact | N/A (relationship, not an account) |
| Financial Statement Impact | N/A directly |
| Change Impact | Not found what happens to *already-resolved* historical transactions if the category default changes after a product previously left its own field blank and inherited the old value — `HOLD / EVIDENCE REQUIRED`, same open question as `B-03`/`B-04` |
| Version Delta | Inheritance direction (Category → Product, overridable) is stable and consistently described across all versions with usable evidence |
| Evidence | Reference ERP official documentation and corroborating community evidence — product/category income-expense account hierarchy, versions 13.0–19.0, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for Product > Category override direction; `HOLD` for parent/child category cascade and for historical-transaction re-resolution behavior |

Full precedence-matrix development (governing prompt §11's twelve numbered cases) belongs to deliverable `11_PRODUCT_CATEGORY_PRODUCT_INHERITANCE_OVERRIDE_PRECEDENCE_MATRIX.md`, not this file; this row exists only to close the Menu B field register per §7.

---

## 12. Effect of Changing Category or Policy on Existing Stock — Consolidated HOLD

Across every field above (`B-01` costing method change, `B-02` Manual↔Automated switch, `B-03`/`B-04` account re-pointing, `B-09` company/account resolution), the same category of question recurs: **what happens to inventory that already exists, and to transactions already posted, at the moment a category-level policy or account changes?**

No fetched documentation passage in this research pass directly answered this for any of the four cases. Community evidence repeatedly frames these changes as risky ("greatly impacts inventory valuation," "requires accountant consultation") but never states the actual mechanical outcome (automatic revaluation entry generated vs. silent divergence between recorded and recomputed value vs. change applying only prospectively to future moves).

This is classified `HOLD / EVIDENCE REQUIRED` as a single consolidated item rather than four separate weaker claims, because the underlying evidence gap is the same gap in each case: the reference's documentation describes *configuration*, not *migration/transition mechanics*. This maps directly onto governing-prompt §10 Scenario 31 (migration/opening inventory replay) and deliverable `26_MIGRATION_OPENING_COST_REPLAY_IDEMPOTENCY_REGISTER.md`; SMEsPlus must treat this as an open design question to be answered on SMEsPlus's own terms, not inferred from the reference.

---

## 13. Behavior by Periodic vs Perpetual — Category-Level Summary Table

| Field | Periodic (Manual) behavior at category level | Perpetual (Automated) behavior at category level |
|---|---|---|
| Costing Method | Same three options; drives period-end closing valuation figure | Same three options; drives per-transaction automatic entry value |
| Income Account | Used at customer invoice validation (unaffected by this toggle) | Used at customer invoice validation (unaffected by this toggle) |
| Expense Account | Debited at vendor bill (Continental) or held as Stock Valuation/asset until close (Anglo-Saxon) | Debited at customer invoice, clearing Stock Interim (Delivered), after asset already moved at delivery (Anglo-Saxon); at bill (Continental) |
| Stock Valuation Account | Not automatically posted; reconciled manually at close | Continuously updated by automatic entries |
| Stock Journal | Not used (no automatic entries to route) | Used for every automatic entry |
| Stock Input / Output Account | Not used — periodic model has no interim-clearing mechanism; uses a period-end stock-variation concept instead (Menu A/F territory) | Core mechanism — interim clearing for unbilled receipts / uninvoiced deliveries |
| Price Difference Account | Not applicable — gated on Automated | Applicable at vendor bill posting when billed price ≠ receipt/standard price |

This table is a cross-reference aid only; the authoritative Periodic and Perpetual end-to-end models are deliverables `12`/`17` and `13`/`18` respectively, and the formal comparison matrix is deliverable `14`.

---

## 14. Fact-Status Roll-Up for This File

| Fact Status | Count of fields/rows carrying this status |
|---|---|
| `VERIFIED` | 7 (B-00 partial, B-01 option set, B-03 trigger, B-04 Continental/Manual mechanism, B-07 account-pairing rule, B-08 existence/gate, B-10 override direction) |
| `PROVISIONAL` | 6 (B-00 pre-19.0 gate history, B-01 default value sourcing, B-04 Anglo-Saxon Automated exact choreography, B-06, B-07 exact debit/credit choreography, B-08 version-16 re-implementation, B-09 no-native-company-field conclusion) |
| `HOLD` | 5 material open items (B-01 existing-stock conversion, B-02 19.0 timing claim, B-04 19.0 conflict, B-09 company-dependent account resolution, §12 consolidated existing-stock/policy-change mechanics) |
| `CONFLICTING` | 2 (B-02 and B-04, both concerning the 19.0 "Perpetual impacts stock valuation at invoice level" claim) |

No field in this file is marked `PASS`, `FINAL`, or `APPROVED`. No blank material cell was left in any evidence table above; every unresolved item is explicitly marked `HOLD / EVIDENCE REQUIRED`, `PROVISIONAL`, or `CONFLICTING` with a stated reason.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
