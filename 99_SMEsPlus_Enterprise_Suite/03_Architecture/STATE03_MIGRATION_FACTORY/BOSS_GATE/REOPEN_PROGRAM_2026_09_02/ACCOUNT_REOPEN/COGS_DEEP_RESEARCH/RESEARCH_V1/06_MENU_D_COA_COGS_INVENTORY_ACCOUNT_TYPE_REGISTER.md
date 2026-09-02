# 06 — Menu D: Accounting -> Configuration -> Chart of Accounts — COGS / Inventory Account-Type Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: Layer A account-type taxonomy verified against official reference-ERP documentation for versions 13.0/15.0/17.0/18.0/19.0; a material 19.0 account-model redesign identified; Layer B Thai statutory mapping explicitly out of scope here (pointer to file 24); no journal entries or SMEsPlus account codes are prescribed.

---

## 0. Scope, Method, and Evidence-Layer Discipline

This file answers governing-prompt §6 Menu D and feeds the §7 field-evidence discipline for the **account-type** dimension only (not the category/product field-assignment dimension, which is files `04`/`05`/`11`). It records, per `CV-02` (see `00_EXECUTION_CHECKPOINT_LOG.md`), what account **types** the reference ERP's own chart-of-accounts taxonomy offers, which of those types are actually consumed somewhere in the COGS/inventory lifecycle, and how the taxonomy itself changed across versions 13.0–19.0.

Three evidence layers are held apart throughout, per governing prompt §3 and the clean-room rules:

- **Layer A — Reference ERP observed behavior.** Cited as `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02`. Where a claim came only from secondary community sources (forum posts, third-party blogs) rather than the vendor's own version-pinned documentation pages, it is marked `Layer A — SECONDARY SOURCE, PROVISIONAL` and should not be treated as equivalent-strength evidence to a direct official-doc citation.
- **Layer B — Thai statutory/tax/audit account classification.** **N/A in this file.** This file does not classify any account against the Thai Chart of Accounts, TFRS for NPAEs, or Revenue Department requirements. Thai statutory account classification is file `24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md`'s exclusive job. Any apparent similarity between a reference-ERP account-type label (e.g. "Cost of Revenue") and a Thai statement caption is coincidental terminology overlap, not a classification finding, and must not be read as one.
- **Layer C — SMEsPlus clean-room candidate.** Marked `CANDIDATE` (non-binding directional note) or `HOLD/JOINT` (requires Joint Team decision, cross-referenced to `JT-01/02/08/09`) only. No SMEsPlus account code, account list, or posting rule is prescribed in this file, per governing prompt §12's instruction not to prescribe final account codes/journal structure in this research session.

Foundational rule carried from the governing prompt into every row below: **Inventory emits facts; Accounting decides postings. Inventory never selects an account.** Everything in this file describes accounts as the reference ERP's *Accounting* configuration surface presents them — never as something Inventory chooses at runtime.

---

## 1. Full Reference-ERP Account-Type Taxonomy (Layer A)

The Chart of Accounts screen (`Accounting -> Configuration -> Chart of Accounts`) assigns every account exactly one **Account Type**, which drives (a) Balance Sheet vs Profit & Loss placement, (b) whether the account is reconcilable, (c) whether it can be selected as a "current assets"-class or "current liabilities"-class default, and (d) which configuration pickers (e.g. product category Income/Expense/Stock account fields) will surface it as a valid choice. This is a closed, version-stable list; it did not gain or lose members across 13.0–19.0, though later versions added a documentation section explaining the list more thoroughly.

| Account Type | Statement Placement | Reconcilable by Default | Observed in COGS/Inventory Lifecycle |
|---|---|---|---|
| Receivable | Balance Sheet (Asset) | Yes | No — customer AR only |
| Bank and Cash | Balance Sheet (Asset) | No | No |
| Current Assets | Balance Sheet (Asset) | Configurable | **Yes** — Stock Valuation Account, Stock Input/Output (interim) accounts |
| Non-current Assets | Balance Sheet (Asset) | Configurable | No (not observed assigned to any inventory/COGS field) |
| Prepayments | Balance Sheet (Asset) | Configurable | No |
| Fixed Assets | Balance Sheet (Asset) | Configurable | Only indirectly — manufacturing equipment depreciation is out of COGS-account scope; not a stock/valuation account choice |
| Payable | Balance Sheet (Liability) | Yes | No — vendor AP only |
| Credit Card | Balance Sheet (Liability) | No | No |
| Current Liabilities | Balance Sheet (Liability) | Configurable | No |
| Non-current Liabilities | Balance Sheet (Liability) | Configurable | No |
| Equity | Balance Sheet (Equity) | No | No |
| Current Year Earnings | Balance Sheet (Equity) | No | No |
| Income | Profit & Loss (Income) | No | **Boundary-adjacent** — Income Account is the product/category revenue-side field; not itself a COGS account, but resolved by the same category/product mechanism (see file `11`) |
| Other Income | Profit & Loss (Income) | No | Not observed populated by inventory events in Layer A; theoretically available for non-operating inventory-related credits (e.g. found-stock write-up) but no direct doc evidence of default use — `HOLD` |
| Expense | Profit & Loss (Expense) | No | **Yes** — Expense Account (COGS-carrying field), Price Difference Account, Inventory Loss Account, Cost of Production Account, and (in Continental Periodic mode) the Variation Account |
| Depreciation | Profit & Loss (Expense) | No | Not observed used for inventory/COGS accounts |
| Cost of Revenue | Profit & Loss (Expense, sub-classified) | No | **Yes** — the documentation-recommended type for the Expense Account when it is meant to read as COGS specifically, distinct from general operating Expense |
| Off-Balance Sheet | Off-Balance Sheet (memo only) | No | Not observed used for inventory/COGS in Layer A; reference ERP uses Off-Balance Sheet for items like third-party-owned goods held in the company's warehouses (consignment-type tracking), which is adjacent to but not proven to be part of the standard COGS/valuation flow — `HOLD, evidence not pursued further this session` |

**Evidence:** Reference ERP official documentation — Chart of Accounts account-type list and Balance-Sheet/Profit-and-Loss grouping, version 18.0, retrieved 2026-09-02. Cross-checked for stability against version 13.0 and 14.0 chart-of-accounts documentation pages (same account-type set observed; no deletions/additions found). **Fact Status: VERIFIED** for the taxonomy list itself; **PROVISIONAL** for the "Off-Balance Sheet unused in COGS flow" negative claim, since a negative (absence of a documented use) is weaker evidence than a positive citation.

---

## 2. Inventory/COGS-Relevant Account Types — Deep Register

Each entry below follows: Purpose / Where Assigned / What Posts To It / Statement Placement / Version Delta / Evidence / Layer B / Layer C.

### 2.1 Current Assets — Stock Valuation Account (a.k.a. "Valuation Account" in 19.0 terminology)

- **Purpose (Layer A):** Holds the current book value of on-hand physical inventory as an asset. This is the account that, summed across all products, is expected to reconcile to the Inventory Valuation report (Menu E, file `07`).
- **Where assigned:** Product Category form, "Account Stock Properties" section (visible only when the category's Inventory Valuation field is set to `Automated` in 13.0–18.0 terminology, or when a valuation account is configured under the restructured 19.0 model — see §3 below). Not overridable at the individual product level in any version researched; the category is the sole assignment point observed.
- **What posts to it:** Debited on incoming stock moves that increase valued on-hand quantity (goods receipt matched to a valuation layer); credited on outgoing stock moves that decrease valued on-hand quantity (delivery, consumption, write-off routed through it). Exact debit/credit archetypes are out of this file's scope (see file `12` §12 COGS Recognition/Account Flow Proof); this file only proves the account **type** and **assignment surface**.
- **Statement Placement:** Balance Sheet, Current Assets.
- **Version Delta:** Present under this account type across all versions researched (13.0 through 19.0). In 18.0 and earlier it is one of four category-level accounts (Stock Valuation / Stock Input / Stock Output / Price Difference). In 19.0 the reference ERP's own documentation states the accounting-model was restructured ("Discover why we changed" note observed in the 19.0 cheat-sheet page); the 19.0 cheat sheet refers to a "Stock Account" on the category and a "Stock Variation" account, which appear to be a renamed/consolidated presentation of the same Current-Assets valuation concept rather than a new account type — `PROVISIONAL, requires direct field-level confirmation in file 04's Menu B evidence` since this file's brief is account **types**, not the category form field-by-field walk.
- **Evidence:** Reference ERP official documentation — Automatic inventory valuation configuration, version 18.0, retrieved 2026-09-02; Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02; Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02.
- **Layer B:** N/A — pointer to file `24`. Whether a Thai-compliant chart of accounts would name/number this account differently, or whether Thai practice requires a more granular Current-Assets subdivision (e.g. separate raw-material vs finished-goods inventory asset accounts) is a statutory-evidence question, not answered here.
- **Layer C:** `CANDIDATE` — a single "Inventory Asset" Current-Assets-type account per valuation pool is a directionally reasonable SMEsPlus starting point, cross-referenced to `JT-01` (valuation policy ownership) since the granularity/segmentation of this account is itself a Joint decision, not an Accounting-only or Inventory-only one.

### 2.2 Current Assets — Stock Input Account / Stock Output Account (interim / "Stock Interim (Received/Delivered)")

- **Purpose (Layer A):** These are **interim clearing accounts**, not final valuation or expense accounts. The Stock Input Account is debited when goods physically enter stock and credited when the matching vendor bill posts (or an equivalent clearing event occurs); the Stock Output Account is debited when the matching customer invoice posts (or equivalent) and was credited when goods physically left stock. Their function is to bridge the timing gap between a *physical* stock movement and its *financial* (bill/invoice) counterpart so that the Stock Valuation Account and vendor/customer AP/AR never touch each other directly.
- **Where assigned:** Product Category "Account Stock Properties" section, same visibility gate as §2.1. Confirmed present as distinct fields labeled "Stock Input Account" and "Stock Output Account" in 13.0 through 18.0 documentation.
- **What posts to it:** Physical receipt/delivery stock-move journal entries and their offsetting vendor-bill / customer-invoice journal entries. This is the mechanical account pair that makes Anglo-Saxon Perpetual accounting possible without waiting for the bill/invoice to know the physical movement's value.
- **Statement Placement:** Balance Sheet, Current Assets. **Evidence caution:** an earlier automated-fetch pass against the 19.0 documentation initially returned a summary claiming these were typed as "Cost of Revenue"; a direct, targeted re-fetch of the 18.0 official configuration page returned "Current Assets classification" with an explicit quote. The 18.0 direct citation is treated as the reliable Layer A fact; the earlier "Cost of Revenue" claim is discarded as a fetch-summarization artifact, not evidence, and is recorded here only so a later reviewer does not re-introduce it as if it were unverified-but-plausible. **Fact Status: VERIFIED (Current Assets)** for 13.0–18.0; **HOLD** for whether the 19.0 restructured model keeps a directly analogous pair of accounts under the same type, pending file `04`'s field-level Menu B walk.
- **Version Delta:** Stable as a named, distinct field pair from 13.0 through 18.0. In 19.0, the cheat-sheet page's abbreviated matrix language ("Stock Account," "Stock Variation," "Expense/Cost of Goods Sold") does not clearly retain a visibly separate Input/Output pair in the excerpts retrieved this session — `HOLD, needs direct 19.0 category-form field enumeration, not pursued further in this account-type-focused file`.
- **Evidence:** Reference ERP official documentation — Automatic inventory valuation configuration, version 18.0, retrieved 2026-09-02 (direct quote: Stock Input/Output "Current Assets classification"); Reference ERP official documentation — Inventory valuation configuration, version 13.0, retrieved 2026-09-02 (field pair present, account type not independently re-confirmed for 13.0 in this pass — `PROVISIONAL` for 13.0 specifically).
- **Layer B:** N/A — pointer to file `24`. Thai practice's tolerance for interim/clearing "goods received not invoiced" and "goods delivered not invoiced" style accounts (a GRNI/GDNI-equivalent concept) is a statutory-evidence and audit-practice question for file `24`, not resolved here.
- **Layer C:** `HOLD/JOINT` — whether SMEsPlus needs an interim clearing-account pair at all depends on `JT-01` (who owns valuation timing) and `JT-08` (landed-cost eligibility/posting, since landed cost commonly lands in the same interim window). No candidate is offered until those are resolved.

### 2.3 Expense / Cost of Revenue — Expense Account (the COGS-carrying field)

- **Purpose (Layer A):** This is the field the reference ERP's own documentation explicitly recommends be typed as **Expenses** or **Cost of Revenue** — the two account types the vendor's own guidance treats as functionally interchangeable placements for what a reader would call "COGS," with a documented preference: under Automated/Perpetual Anglo-Saxon valuation, "Expenses" or "Cost of Revenue" type is directed; under Manual/Periodic valuation, the same field is instead pointed at the **Stock Valuation** account (i.e., in Periodic mode this field is redirected to a Current-Assets-type account rather than an Expense/Cost-of-Revenue-type account — see §2.1 and the Periodic/Perpetual distinction in file `12`/`13`).
- **Where assigned:** Product Category form (default) and Product form Accounting tab (override) — see file `11` for the full precedence proof. Same field, different scope levels.
- **What posts to it:** Under Perpetual/Anglo-Saxon Automated valuation: the customer-invoice-triggered (or delivery-triggered, version-dependent — see file `13`) recognition of cost against the matched Stock Output/interim account. Under Continental/Periodic: the vendor-bill-triggered recognition of purchase cost as expense, later trued up by the closing/variation entry.
- **Statement Placement:** Profit & Loss. The choice between "Expenses" and "Cost of Revenue" account type is a **presentation-line** choice, not a different accounting mechanism — both types post to P&L, but "Cost of Revenue" typically renders on a P&L layout as a distinct sub-total line ahead of gross-profit computation, while generic "Expenses" typically renders further down among operating expenses. The reference ERP's own P&L report layout groups by account type, so this choice materially affects where "COGS" appears relative to a Gross Profit subtotal.
- **Version Delta:** The dual-typing guidance ("Expenses or Cost of Revenue" for automated; "Stock Valuation" for manual) is confirmed present in both the 17.0 and 18.0 documentation passes this session. No evidence found this session that this dual-typing rule changed materially through 19.0, though the 19.0 restructuring (§3) changes the surrounding field names.
- **Evidence:** Reference ERP official documentation — Automatic inventory valuation configuration, version 17.0, retrieved 2026-09-02 (quote: "set the Expense Account to an Expenses or a Cost of Revenue type ... for manual valuation method, set the Expense Account to Stock Valuation"); Reference ERP official documentation — Automatic inventory valuation configuration, version 18.0, retrieved 2026-09-02 (independent confirmation).
- **Layer B:** N/A — pointer to file `24`. Whether Thai statutory/statement presentation requires (or merely permits) a distinct "Cost of Sales"/"COGS" caption ahead of a Gross Profit subtotal, as opposed to folding cost of goods into undifferentiated expenses, is a Thai financial-statement-presentation question for file `24`.
- **Layer C:** `CANDIDATE` — a dedicated Cost-of-Revenue-type "COGS" account, separate from general operating Expense-type accounts, is directionally consistent with standard gross-profit P&L presentation and is offered as a non-binding candidate; final account taxonomy remains `HOLD/JOINT` per `JT-01`/`JT-02` (costing methods materially affect what "the" COGS figure even means before an account structure can be finalized around it).

### 2.4 Expense — Price Difference Account

- **Purpose (Layer A):** Captures the variance between a product's **Standard Price** (the costing-method basis) and the actual price billed by the vendor, when the reference ERP's own documentation states this account is used **specifically and only** in the combination of Perpetual (at-invoicing / Automated) valuation **with** Standard Price costing. It is not used under FIFO or AVCO costing per the documentation retrieved.
- **Where assigned:** Product Category "Account Stock Properties" section, alongside the accounts in §2.1/§2.2.
- **What posts to it:** The delta between the vendor bill's actual unit price and the product's configured Standard Price, at bill-posting time, so that the Stock Valuation Account keeps moving strictly at Standard Price while the P&L absorbs the day-to-day purchase-price variance.
- **Statement Placement:** Profit & Loss (Expense). Can carry a debit or credit balance depending on whether actual cost ran above or below standard.
- **Version Delta:** Present and documented consistently 13.0 through 19.0 in every version-specific page fetched this session, though the 19.0 cheat-sheet's abbreviated account list did not explicitly re-list it by name in the excerpt retrieved — `HOLD, minor, likely a fetch-excerpt gap rather than a real removal, not to be treated as evidence of removal`.
- **Evidence:** Reference ERP official documentation — Inventory valuation configuration, version 13.0, retrieved 2026-09-02; Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (quote: "records the difference between the product's standard price ... and the actual billed price").
- **Layer B:** N/A — pointer to file `24`. Purchase-price-variance treatment under Thai cost-accounting practice (whether it must be allocated back into inventory/COGS at period end versus left as a standalone P&L variance line) is a Thai-evidence question, explicitly flagged for file `24` and cross-referenced to `JT-02` (costing methods) since Standard Costing itself is a `JT-02` open item.
- **Layer C:** `HOLD/JOINT` — no SMEsPlus candidate offered; entirely conditioned on whether Standard Costing is even adopted as an SMEsPlus-approved costing method (`JT-02`).

### 2.5 Expense — Inventory Loss Account

- **Purpose (Layer A):** Tracks shrinkage, damage, scrap, or other non-sale reductions in inventory quantity, when routed through a dedicated **location** (the reference ERP's model attaches this account to a "Virtual Locations/Inventory Loss" type location rather than to the product category directly).
- **Where assigned:** Location record (not product category, not product), specifically a location typed for inventory adjustments/loss. The 19.0 documentation explicitly recommends this be configured "for tracking inventory shrinkage" and separately notes it is "recommended for Anglo-Saxon accounting."
- **What posts to it:** Inventory Adjustment transactions where the counterpart is not a normal customer/vendor stock move but a scrap/loss/adjustment-to-loss-location move.
- **Statement Placement:** Profit & Loss (Expense) — distinct from the Expense Account (§2.3) that carries ordinary-course COGS. This is a structural, evidence-backed confirmation of the governing prompt's core premise (§2/§14): **not every inventory-value decrease is COGS** — the reference ERP itself routes loss/shrinkage to a different account than sale-driven cost release, when configured to do so.
- **Version Delta:** Explicitly named and typed in the 19.0 documentation retrieved this session ("Inventory Loss Account ... Expense"). Earlier-version (13.0–18.0) documentation pages fetched this session did not surface this as a separately named category-adjacent account in the same terms — it may have existed under a different label/location-based mechanism in earlier versions rather than being a new addition; this session's evidence is **insufficient to state whether this is a 19.0 addition or a 19.0 rename/surfacing of pre-existing location-based behavior** — `HOLD, version-origin unresolved`.
- **Evidence:** Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02.
- **Layer B:** N/A — pointer to file `24`. Whether Thai tax rules require documentary substantiation (e.g., destruction witnessed/reported to Revenue Department) before a scrap/loss can be deducted as an expense, and whether that requirement should gate the SMEsPlus equivalent of this account, is squarely a file `24` matter, cross-referenced to governing-prompt §10 scenario 23.
- **Layer C:** `CANDIDATE` — a dedicated non-COGS "Inventory Loss/Shrinkage" Expense-type account, distinct from the ordinary COGS account, is offered as a directionally sound candidate precisely because it operationalizes the "not every decrease is COGS" boundary rule; still `HOLD` on exact SMEsPlus account taxonomy pending `JT-01`.

### 2.6 Expense — Cost of Production Account (WIP/manufacturing-adjacent concept)

- **Purpose (Layer A):** Set on **production locations** to capture manufacturing-related cost flow (raw-material consumption into a manufacturing order and/or finished-goods output valuation routing), per the 19.0 documentation.
- **Where assigned:** Location record (production-type location), analogous in mechanism to §2.5's location-based Inventory Loss Account rather than to the product category form.
- **What posts to it:** Manufacturing consumption/output stock moves that pass through a production location, as distinct from ordinary purchase-receipt/sales-delivery moves.
- **Statement Placement:** Profit & Loss (Expense), per the 19.0 documentation's typing.
- **Version Delta / Scope caution:** The reference ERP's Manufacturing app is a **separate application** from core Inventory/Accounting, and a true Work-in-Process **asset** account (as opposed to a P&L Cost-of-Production expense pass-through) is governed primarily by Manufacturing-app costing configuration, which this Menu-D chart-of-accounts pass did not exhaustively research. This file records only the account-type fact observed for the "Cost of Production Account" label; the deeper WIP lifecycle (raw material -> WIP -> finished goods -> COGS) is governing-prompt §10 scenarios 27–29 and deliverable `22_MANUFACTURING_RM_WIP_FG_COGS_RESEARCH.md`'s job, not this file's. **Explicitly marked `HOLD — WIP asset-account concept not proven in this pass`**; only the Expense-type "Cost of Production Account" is `VERIFIED` as to type/location-assignment.
- **Evidence:** Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02.
- **Layer B:** N/A — pointer to file `24`. Thai TFRS/TFRS-for-NPAEs treatment of WIP as a distinct inventory sub-class (raw materials / WIP / finished goods) is a statutory-evidence question deferred entirely to file `24` and file `22`.
- **Layer C:** `HOLD/JOINT` — cross-referenced to `JT-09` (WIP recognition), which this file's evidence does not resolve.

### 2.7 Income — Income Account (boundary note only)

- **Purpose (Layer A):** Revenue-side counterpart field, resolved by the identical category/product precedence mechanism as the Expense Account (file `11`). It is **not** a COGS or inventory-valuation account and is included here only to establish the boundary: the reference ERP's product/category "Accounting" configuration surface controls both revenue (Income Account) and cost (Expense Account) recognition through the same override mechanism, which is why Menu D (accounts) and Menu B/C (category/product field assignment, files `04`/`05`) must be read together, and why file `11`'s precedence proof applies symmetrically to both fields even though this file's material focus is the Expense/COGS side.
- **Statement Placement:** Profit & Loss (Income).
- **Evidence:** Reference ERP official documentation — Chart of accounts, version 18.0, retrieved 2026-09-02 (Income account-type definition); cross-referenced against the Income/Expense Account override mechanism reported in file `11`.
- **Layer B / Layer C:** N/A to this file — revenue-account statutory/candidate treatment is outside COGS/inventory scope entirely.

### 2.8 Continental-Periodic-only — Variation Account

- **Purpose (Layer A):** Used specifically in **Continental accounting under Periodic valuation**, where the reference ERP's own 19.0 documentation types it as an **Expense** account for capturing the stock-variation entry generated at closing (the balancing entry between opening inventory + purchases and physically counted/valued closing inventory — see governing-prompt §14's Periodic COGS identity). Under **Anglo-Saxon Perpetual**, the analogous variation concept is instead recommended as a **Current Asset** (interim-tracking-preferred) or, optionally, an Expense account — i.e., the same conceptual "variation" role changes **account type** depending on which accounting model (Continental vs Anglo-Saxon) and which valuation cadence (Periodic vs Perpetual) is in force. This is a materially important, evidence-backed finding: **the same business concept (stock variation) does not have one fixed account type in the reference ERP — its type is a function of the accounting-model/valuation-cadence combination**, which is a direct instance of the governing prompt's "no hidden timing assumption" hard rule made concrete at the account-type level.
- **Where assigned:** Category-level ("Stock Valuation Account"/"Variation Account" fields, per the 19.0 restructured labels) combined with the company-level Continental/Anglo-Saxon accounting-package setting, which is set once per company and not overridable per category in the evidence retrieved this session — `PROVISIONAL, company-level exclusivity not independently re-confirmed this pass, cross-reference file 03/25`.
- **What posts to it:** The stock-closing/variation journal entry described structurally in file `08` (Menu F) and file `12`/`14` (Periodic model / comparison matrix); this file records only the account-type behavior.
- **Statement Placement:** Either Balance Sheet (Current Assets, Anglo-Saxon-preferred interim treatment) or Profit & Loss (Expense, Continental / Anglo-Saxon-optional treatment) — **dual placement is itself the evidence-backed fact**, not an inconsistency to be resolved by this file.
- **Version Delta:** This dual-typing description was retrieved specifically from 19.0 documentation. Earlier versions (13.0–18.0) documentation retrieved this session described a Continental-vs-Anglo-Saxon distinction in *recognition timing* but did not surface an explicit account-type table for a named "Variation Account" as cleanly as the 19.0 material did — `HOLD, whether this is a 19.0-only explicit naming of a previously implicit mechanic, or a genuine new field, is unresolved` pending file `04`'s field-level walk of the category form across versions.
- **Evidence:** Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02.
- **Layer B:** N/A — pointer to file `24`.
- **Layer C:** `HOLD/JOINT` — cross-referenced to `JT-01` (valuation policy ownership, since Continental vs Anglo-Saxon is itself a policy choice with account-type consequences) and `JT-09` (WIP/variation-adjacent recognition boundary).

---

## 3. Version-Delta Register — Menu D Specific

| Version Band | Observed State | Evidence | Fact Status |
|---|---|---|---|
| 13.0 | Category-level four-account model (Stock Valuation / Stock Input / Stock Output / Price Difference) fully present; "Manual"/"Automated" terminology for valuation cadence; Continental vs Anglo-Saxon timing distinction documented in prose, not as an explicit per-account type table. | Reference ERP official documentation — Inventory valuation configuration, version 13.0, retrieved 2026-09-02 | VERIFIED (four-account model, terminology); PROVISIONAL (absence of explicit account-type table — negative evidence) |
| 14.0–15.0 | Same four-account model confirmed present under equivalent documentation structure (menu path renamed from "management/reporting" to a stable sub-path across these releases, not a functional account-type change). | Reference ERP official documentation — Chart of accounts / Inventory valuation configuration, versions 14.0/15.0, retrieved 2026-09-02 | VERIFIED (structural continuity) |
| saas-16.4 / 17.0 | Same four-account model; explicit dual-typing rule for the Expense Account ("Expenses or Cost of Revenue" for Automated; "Stock Valuation" for Manual) directly quoted from official documentation. | Reference ERP official documentation — Automatic inventory valuation configuration, versions saas-16.4/17.0, retrieved 2026-09-02 | VERIFIED |
| 18.0 | Same four-account model; Stock Input/Output explicitly reconfirmed as **Current Assets** type via direct quote; menu path relocated to `inventory/product_management/inventory_valuation/` (a navigation change, not an account-type change — cross-reference file `03`/`04` for the full menu-path delta). | Reference ERP official documentation — Automatic inventory valuation configuration, version 18.0, retrieved 2026-09-02 | VERIFIED |
| 19.0 | **Material redesign.** Valuation-cadence field labels changed from "Manual"/"Automated" to **"Periodic (at closing)"** / **"Perpetual (at invoicing)"**. Account model re-described using terms "Valuation Account," "Variation Account," "Stock Input Account" (Cost-of-Revenue-typed per one fetch — **unreliable, see §2.2 caution**), "Price Difference Account" (Expense), plus two account concepts not seen clearly named in earlier-version documentation retrieved this session: "Inventory Loss Account" (Expense, location-based) and "Cost of Production Account" (Expense, location-based). The reference ERP's own documentation explicitly signals this as an intentional change (a "Discover why we changed" cross-reference was observed in the 19.0 cheat-sheet page), meaning **this is a vendor-acknowledged behavioral break, not an inference by this research** — the exact scope and mechanics of the break are not fully characterized by this file's evidence and require a dedicated re-pass in file `04` (category field enumeration) and file `14` (Periodic vs Perpetual comparison) before being treated as closed. | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02; Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02 | VERIFIED (that a change occurred, and its direction); HOLD (full field-by-field before/after mapping) |

**Explicit instruction to downstream files:** Do not silently carry the 13.0–18.0 four-account model (Stock Valuation / Stock Input / Stock Output / Price Difference) into a 19.0-scoped conclusion, and do not silently carry 19.0's "Periodic (at closing)/Perpetual (at invoicing)" terminology backward onto 13.0–18.0's "Manual"/"Automated" terminology. They are evidenced as materially different labelings of a related but not proven-identical mechanism. This is the governing prompt's §5 version-delta rule applied concretely.

---

## 4. Explicit Separation — Observed Reference Account-Type Taxonomy vs Thai Statutory COA Classification

Per governing-prompt Menu D instruction ("Do not infer Thai COA classification from the reference. Map observed behavior separately from Thai authoritative requirements") and the clean-room rule against inferring Thai classification from reference-ERP behavior:

- **What this file established (Layer A only):** The reference ERP offers a fixed, closed set of account types (§1); a specific subset of those types is actually consumed by COGS/inventory-lifecycle account fields (§2); and that subset's field-to-type mapping changed materially at version 19.0 (§3).
- **What this file explicitly did NOT do:** Assign, imply, or recommend a Thai statutory account code (e.g., a PP.30/Revenue-Department-style chart position), a Thai financial-statement caption, or a Thai audit-classification for any account described above. No mapping of "Cost of Revenue" (reference-ERP type) to any specific Thai P&L line is made or implied by this file.
- **Required next step (not performed here):** File `24_THAI_ACCOUNTING_TAX_STATUTORY_EVIDENCE_REGISTER.md` must independently establish, from authoritative Thai sources only, what account classification and statement-presentation requirements actually apply, and only the Joint Team may then decide whether/how the reference-ERP taxonomy in §1–§3 informs (never dictates) an SMEsPlus candidate chart of accounts.
- **Standing HOLD:** Every Layer C candidate note in §2 above is non-binding and explicitly conditioned on file `24` and Joint (`JT-01`/`JT-02`/`JT-08`/`JT-09`) resolution. None constitutes a Chart-of-Accounts decision.

---

## 5. Cross-Reference to Open Joint Decisions

| Joint ID | Topic | Relevance surfaced in this file |
|---|---|---|
| `JT-01` | Valuation policy ownership | §2.1 (valuation-account granularity), §2.8 (Continental/Anglo-Saxon as a policy choice with account-type consequences) |
| `JT-02` | Costing methods | §2.4 (Price Difference Account exists only under Standard Costing + Perpetual), §2.6 (Cost of Production Account boundary with `JT-09`) |
| `JT-08` | Landed-cost eligibility/posting | §2.2 (interim Stock Input/Output accounts are the mechanical landing zone for landed-cost timing questions — proof deferred to file `21`) |
| `JT-09` | WIP recognition | §2.6, §2.8 |

---

## 6. Material Open HOLD Items From This File

1. **19.0 account-model field-by-field mapping is incomplete** (§3) — the single most material open item in this file: whether "Stock Input Account" retains a distinct identity and a Current-Assets type in 19.0, or has been functionally absorbed into "Valuation Account"/"Variation Account," is unresolved and materially affects any future SMEsPlus account-taxonomy candidate that wants to target the reference ERP's current (19.0) rather than legacy (13.0–18.0) model.
2. Origin of the "Inventory Loss Account" and "Cost of Production Account" as either 19.0-new or 19.0-renamed-and-surfaced is unresolved (§2.5, §2.6).
3. Whether the Continental/Anglo-Saxon accounting-package setting is strictly company-level-exclusive (no per-category override) is `PROVISIONAL`, not independently re-verified this pass (§2.8).
4. Off-Balance-Sheet account type's role (if any) in consignment/third-party-owned-stock COGS scenarios is `HOLD`, not pursued (§1).

No PASS, FINAL, or account-taxonomy authorization is declared by this file.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
