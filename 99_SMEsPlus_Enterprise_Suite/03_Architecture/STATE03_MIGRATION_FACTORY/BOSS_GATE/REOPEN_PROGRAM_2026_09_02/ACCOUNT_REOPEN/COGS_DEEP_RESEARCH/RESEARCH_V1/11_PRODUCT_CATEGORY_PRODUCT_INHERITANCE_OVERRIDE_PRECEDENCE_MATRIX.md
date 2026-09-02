# 11 — Product Category vs Product Inheritance / Override Precedence Matrix

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: General precedence mechanism verified against reference-ERP official documentation and cross-checked secondary sources; 12-case matrix built from that mechanism plus first-principles accounting-timing reasoning; several cases are `HOLD` pending file `04`/`05` field-level confirmation and Joint reconciliation — no case in this file is asserted as an SMEsPlus design decision.

---

## 0. Dependency and Reconciliation Disclosure (read first)

This file answers governing-prompt §11 in full — the mandatory 12-case precedence matrix. It is written to depend **conceptually**, not textually, on:

- `04_MENU_B_PRODUCT_CATEGORY_ACCOUNTING_FIELD_REGISTER.md` — the field-by-field Product Category form walk (Menu B), and
- `05_MENU_C_PRODUCT_ACCOUNTING_INCOME_EXPENSE_FIELD_REGISTER.md` — the field-by-field Product Accounting-tab walk (Menu C),

both of which were commissioned as parallel deliverables in this same session and were not available to read at the time this file was authored. Rather than guess their exact field-label wording, section numbering, or evidence-table phrasing, this file independently re-derives the **general resolution mechanism** (§1) from its own reference-ERP research, then builds the 12-case matrix (§2) on that independently-sourced mechanism. Where this file's account of a field (e.g., an exact label, a visibility condition, a default value) turns out to differ from what files `04`/`05` record, that is a discrepancy for the **coordinating session** to reconcile before the deliverable set is treated as internally consistent — this file does not have authority to overwrite `04`/`05`, and `04`/`05` do not have authority to silently overwrite this file. This disclosure is made explicitly per the task brief rather than left implicit.

This file also depends on file `06` (`06_MENU_D_COA_COGS_INVENTORY_ACCOUNT_TYPE_REGISTER.md`, same author/session) for account-type vocabulary (Current Assets, Expense, Cost of Revenue) used below; that dependency is internally consistent since both files were authored together in this session.

---

## 1. General Resolution Mechanism (Layer A, independently sourced)

### 1.1 The precedence chain

Reference-ERP official and secondary documentation, converged on a consistent three/four-level precedence chain for the **Income Account** and **Expense Account** fields specifically (the two fields governing-prompt §11 is concerned with):

1. **Product variant** — if the specific sellable/purchasable variant record carries its own Income/Expense Account value, it wins.
2. **Product template** — if the variant level is blank, the product (template) record's own Income/Expense Account value, set on the product's Accounting tab, wins.
3. **Product Category** — if both variant and product levels are blank, the Income/Expense Account configured on the product's assigned Product Category is used.
4. **Journal-level fallback** — secondary-source evidence (forum-level, not an official version-pinned documentation page) additionally describes a journal-level default account as a final fallback when even the category level is blank. This fourth level is recorded as `Layer A — SECONDARY SOURCE, PROVISIONAL` and should not be treated with the same evidentiary weight as levels 1–3, which are corroborated by official documentation language describing product-level fields as overriding category defaults.

**Evidence:** Reference ERP official documentation — Chart of accounts / product accounting configuration guidance, versions 17.0–19.0, retrieved 2026-09-02 (Income/Expense Account fields on product and category, override relationship); Reference ERP community documentation — product/category income-expense account default hierarchy discussion, retrieved 2026-09-02 (`SECONDARY SOURCE, PROVISIONAL`, journal-level fallback claim only). **Fact Status:** precedence levels 1–3 `VERIFIED` in direction (product overrides category) though the *variant-vs-template* two-way split within "product level" is `PROVISIONAL` — most single-variant products make this distinction moot, and this session's evidence does not cleanly separate variant-level override behavior from template-level override behavior with an official-doc-grade citation. Level 4 (journal fallback) is `PROVISIONAL`.

### 1.2 What the precedence chain does NOT cover

The same chain is **not** established by this session's evidence to govern **Costing Method** or **Inventory Valuation (cadence)** the same way. Every source retrieved this session describes Costing Method and the Automated/Manual (or 19.0-era Periodic/Perpetual) valuation-cadence selector as fields that live **only on the Product Category** (and, for the cadence/accounting-package dimension, partly at company level — see file `06` §2.8), with **no product-level override field found**. This is a material asymmetry: **Income/Expense Account resolution is a three-level product>category cascade; Costing Method and Valuation Cadence resolution is a category-only (or category+company) assignment with no product-level override observed.** This asymmetry directly shapes Cases 11 and 12 below and is flagged as `HOLD — absence-of-evidence, not evidence-of-absence` since a product-level costing override was not proactively searched to exhaustion this session; the field-level walk in file `04` is the authoritative source to close this HOLD.

### 1.3 Timing/effective-dating mechanism (Layer A, inferred from general reference-ERP configuration behavior, not a single dedicated document)

No dedicated "effective-dating" or "historical override" field was found for Income/Expense Account changes at either category or product level. The observed mechanism in reference ERP-class systems generally, and not contradicted by anything retrieved this session, is: **a change to a category's or product's Income/Expense Account (or to which category a product belongs) takes effect for transactions created after the change; it does not retroactively rewrite the account already posted on historical journal entries.** This is stated here as a `PROVISIONAL, first-principles-consistent` inference rather than a directly quoted documentation fact, because no version-pinned documentation page explicitly describing "changing this field does not alter historical entries" was retrieved this session. It is nonetheless the basis for the Historical Effect / Future Effect columns throughout §2, and is flagged `HOLD — needs a direct citation` for anyone promoting this file's conclusions past Layer 2 controlled evidence.

### 1.4 Why "same account at both levels" and "different account at both levels" are not merely cosmetic

Even when category and product both carry a non-blank Income/Expense Account, the reference ERP's evaluation order is still "check product first" — a same-valued pair (Cases 3/5) produces an identical resolved account to a category-only configuration (Case 1/2) but is **not evidenced as behaviorally identical** in one respect: if the product-level value is later changed while the category stays fixed, a same-valued pair silently becomes a different-valued pair with no configuration change at the category level and no error/warning evidenced. This "silent divergence" risk is a material control point carried into Case 9 below.

---

## 2. The 12-Case Precedence Matrix

Each case is proven against: Resolved Configuration, Transaction(s) Affected, Periodic Outcome, Perpetual Outcome, Historical Effect, Future Effect, Required Approval/Audit Trail, Migration Implication. Fact Status is stated per case; Layer B is N/A/pointer-to-file-24 throughout per clean-room rule (repeated per-case only where a case has a materially distinct Thai-relevant angle worth flagging for file `24` to pick up).

### Case 1 — Category has Income Account; Product blank

- **Resolved configuration:** Category's Income Account is used for every product in that category that leaves its own Income Account blank (§1.1 level 3).
- **Transaction(s) affected:** Customer Invoice line revenue-account selection (and, per §1.1, any Sales Order accounting preview that reads the resolved account before invoicing).
- **Periodic outcome:** No difference from Perpetual for the Income Account resolution itself — Income Account resolution is a revenue-side mechanism and is not gated by the Periodic/Perpetual (COGS-timing) distinction, which governs the Expense Account/Stock accounts. Recorded as `VERIFIED — mechanism, not outcome-specific` since no evidence found this session ties Income Account resolution to valuation cadence.
- **Perpetual outcome:** Same as Periodic (see above).
- **Historical effect:** None — this is the baseline (no override present), not a change event.
- **Future effect:** If a product-level override is later added, that product's future invoices resolve to the new product-level account; already-posted invoices are unaffected (§1.3).
- **Required approval/audit trail:** None beyond ordinary category-configuration change control — this is the default state, not an exception requiring extra sign-off.
- **Migration implication:** A migrated product with no product-level override must migrate as "blank," not as a copy of the category's current value, so that future category-level account changes continue to cascade correctly; hard-coding the resolved value onto the product at migration time would silently freeze that product out of future category-level changes. Flagged as a concrete migration-design risk.
- **Fact Status:** VERIFIED (mechanism); the Periodic/Perpetual non-relevance claim is PROVISIONAL.

### Case 2 — Category has Expense Account; Product blank

- **Resolved configuration:** Category's Expense Account is used for every product in the category that leaves its own Expense Account blank.
- **Transaction(s) affected:** Whichever transaction the resolved Expense Account is actually consumed by — and here **Periodic vs Perpetual materially changes what "the Expense Account" even means**, per file `06` §2.3: under Perpetual/Automated valuation, the resolved Expense Account is Expense/Cost-of-Revenue-typed and is posted at the customer-invoice (or delivery, version-dependent) event; under Periodic/Manual valuation, the same field is redirected to the Stock Valuation (Current Assets) account and the category's nominal "Expense Account" value is not the one actually driving COGS presentation — COGS instead emerges from the period-close variation entry (file `12`).
- **Periodic outcome:** The category-level Expense Account field is present but its accounting role is structurally different (redirected to Stock Valuation per file `06` §2.3) — COGS is not recognized transaction-by-transaction via this field under Periodic.
- **Perpetual outcome:** The category-level Expense Account field directly drives per-transaction COGS recognition timing (at invoice or delivery, per file `13`).
- **Historical effect:** None (baseline state).
- **Future effect:** Same reasoning as Case 1, mirrored for Expense.
- **Required approval/audit trail:** None beyond ordinary configuration change control.
- **Migration implication:** Same "leave blank, do not hard-code" principle as Case 1; additionally, migration tooling must know **which valuation cadence** is active per company/category before it can even correctly interpret what the category's Expense Account field means (Case 2's Periodic/Perpetual divergence is structural, not cosmetic) — this is a direct dependency on `JT-01`.
- **Fact Status:** VERIFIED (the Periodic/Perpetual structural divergence, sourced from file `06` §2.3's directly quoted documentation).

### Case 3 — Category and Product have the same Income Account

- **Resolved configuration:** Product-level value wins per §1.1 level 2, but since it is numerically identical to the category's, the resolved account is indistinguishable from Case 1's outcome for as long as both remain equal.
- **Transaction(s) affected:** Same as Case 1.
- **Periodic / Perpetual outcome:** Same as Case 1 (Income Account resolution is cadence-independent per current evidence).
- **Historical effect:** None.
- **Future effect:** **Materially different from Case 1's future-effect story.** Because the product now carries an explicit (non-blank) value, a future category-level change does **not** cascade to this product — the product is now "pinned." This is the silent-divergence risk flagged in §1.4: an administrator who changes the category's Income Account expecting it to apply company-wide will not realize this specific product is excluded, because at the moment of the category change the two values still look "the same" in any report that only shows resolved (not raw per-level) values.
- **Required approval/audit trail:** `HOLD/CANDIDATE` — this file recommends (Layer C, non-binding) that any SMEsPlus configuration UI surface a visible distinction between "inherited from category" and "explicitly set, currently equal to category" states, precisely because the reference-ERP-observed mechanism does not appear to make this distinction visible to an administrator, which is a control gap worth surfacing to the Joint Team.
- **Migration implication:** A product migrated with an explicit (even if equal-valued) Income Account will **not** track future category changes; a product migrated blank will. Migration tooling must make this choice deliberately per product, not by copying the resolved value uniformly.
- **Fact Status:** VERIFIED (precedence direction); the "silent divergence / no visible distinction" claim is PROVISIONAL — not disproven by any evidence found, but also not exhaustively confirmed by inspecting the actual list-view/form-view UI this session.

### Case 4 — Category and Product have different Income Accounts

- **Resolved configuration:** Product-level value wins outright (§1.1 level 2 over level 3); the category's Income Account is not used for this product at all while the override stands.
- **Transaction(s) affected:** Same as Case 1, but every invoice line for this specific product/variant posts revenue to the product-level account, not the category account — meaning products within the same category can legitimately post revenue to different Income accounts, which has direct P&L-grouping/reporting consequences (revenue-by-category reporting that assumes "one account per category" would be wrong for this product).
- **Periodic / Perpetual outcome:** Same mechanism regardless of cadence (Income side is cadence-independent per current evidence, as in Case 1).
- **Historical effect:** None from the override's mere existence; see Case 9 for the mid-period-change scenario specifically.
- **Future effect:** All future transactions for this product use the product-level account until/unless the override is removed.
- **Required approval/audit trail:** `HOLD/CANDIDATE` — a deliberate, category-diverging override is exactly the kind of configuration event this session's evidence suggests deserves an audit-trail entry (who set it, when, why) beyond ordinary field-change logging, because it silently defeats category-level reporting assumptions; no evidence this session shows the reference ERP itself imposes any such approval gate (it is a plain field edit) — flagged as a candidate SMEsPlus control, not an observed reference behavior.
- **Migration implication:** Migration must preserve the override explicitly (cannot be treated as "noise" and dropped to category default) since it reflects a deliberate business decision already in force.
- **Fact Status:** VERIFIED (precedence direction and reporting-consequence reasoning); audit-trail candidate is Layer C only.

### Case 5 — Category and Product have the same Expense Account

- **Resolved configuration:** Product-level value wins per precedence but is numerically equal to category's — mirrors Case 3's mechanism exactly, applied to Expense Account.
- **Transaction(s) affected / Periodic / Perpetual outcome:** Same structural Periodic/Perpetual divergence as Case 2 (the field's role differs by cadence), with the added Case-3-style "pinning" risk: future category-level Expense Account changes will not cascade to this product once it carries an explicit value, even if that value currently matches.
- **Historical / Future effect:** Same reasoning as Case 3, applied to COGS-side accounts — with higher materiality than the Income-side equivalent, because an Expense Account "pinning" gap directly affects a P&L cost line and, under Perpetual, directly affects transaction-by-transaction COGS, not just a revenue-classification nuance.
- **Required approval/audit trail:** `HOLD/CANDIDATE`, same reasoning as Case 3, elevated in priority given COGS materiality.
- **Migration implication:** Same as Case 3, with the added instruction that migration tooling must record, per product, whether an Expense Account value is "inherited-equal" or "explicit-equal," because a downstream COGS-account restructuring project (post-migration) needs to know which products would actually be affected by a category-level account change and which are pinned.
- **Fact Status:** VERIFIED (mechanism); PROVISIONAL (visibility-gap claim, as in Case 3).

### Case 6 — Category and Product have different Expense Accounts

- **Resolved configuration:** Product-level Expense Account wins outright; mirrors Case 4's mechanism.
- **Transaction(s) affected:** Same transaction set as Case 2, but resolved per-product; this is the case most directly responsible for governing-prompt §6 Menu C's mandatory question ("When does the Product-level Income/Expense account override the Product Category default, and which business event uses the resolved account under Periodic and under Perpetual accounting?") — the answer, per file `06` §2.3 and this file's §1.1/§1.2, is: **the override always wins at resolution time regardless of cadence; what changes by cadence is which business event (vendor bill under Periodic-style redirection to Stock Valuation, vs. customer invoice/delivery under Perpetual) actually consumes the resolved account, and what account-type role that field plays once resolved.**
- **Historical effect:** None from mere existence (see Case 9 for the change-mid-period scenario).
- **Future effect:** All future COGS-relevant transactions for this product use its own Expense Account.
- **Required approval/audit trail:** `HOLD/CANDIDATE`, same reasoning as Case 4, COGS-elevated as in Case 5.
- **Migration implication:** Must preserve the override explicitly; additionally, because this changes which P&L account absorbs this product's cost of sales, a migrated multi-product category with mixed overrides requires migration tooling to reconcile at the **product** level, not assume category-level COGS reporting is complete without enumerating every product's resolved (not nominal-category) account.
- **Fact Status:** VERIFIED (precedence direction and event-vs-account distinction, both traceable to file `06` §2.3's directly-quoted evidence).

### Case 7 — Product changes category before any transaction

- **Resolved configuration:** Immediately upon category reassignment, and before any transaction exists for the product, the product's resolved Income/Expense Account recalculates against the **new** category (if the product itself has no override) — there is no transaction history to reconcile against, so this is the cleanest possible case.
- **Transaction(s) affected:** None yet — this case is about configuration state prior to any posting.
- **Periodic / Perpetual outcome:** No outcome divergence — no transactions exist yet to be timed differently.
- **Historical effect:** None (no history exists).
- **Future effect:** All future transactions resolve against the new category (subject to any product-level override still standing, unaffected by the category change per §1.1's precedence — an override does not get cleared by a category reassignment; this is `PROVISIONAL`, inferred from the general independence of the two fields rather than a directly observed "category change clears override" test).
- **Required approval/audit trail:** `CANDIDATE` — even with zero transaction risk, a category reassignment changes which Costing Method and Valuation Cadence govern the product going forward (§1.2), which is exactly the kind of change governing-prompt §11 flags as needing proof of effect — recommend (non-binding) that SMEsPlus log category-reassignment events regardless of transaction history, because the *next* transaction's cost-recognition behavior depends on it.
- **Migration implication:** Pre-transaction category assignment is the easiest migration case — no historical-value reconciliation is needed; migration tooling should still capture the assignment as a discrete, dated event for audit-trail completeness even though no COGS math is at stake yet.
- **Fact Status:** VERIFIED (no-history-to-reconcile logic); PROVISIONAL (override survives category-reassignment claim).

### Case 8 — Product changes category with existing stock

- **Resolved configuration:** Same mechanical account-resolution recalculation as Case 7, but now against a product that already carries on-hand quantity/value under the **old** category's Costing Method and Valuation Account.
- **Transaction(s) affected:** Every future stock move for this product now targets the new category's Stock Valuation/Input/Output/Expense accounts (subject to override), while the **existing on-hand value** was built up under the old category's accounts. No evidence retrieved this session shows the reference ERP automatically re-values or transfers existing on-hand stock's accumulated value from the old category's Stock Valuation Account to the new category's Stock Valuation Account upon reassignment — this is a `HOLD, material, not directly tested this session` with high real-world risk: if no automatic transfer/re-class journal entry is generated, existing stock value remains sitting in the old category's Valuation Account while new movements post against the new category's accounts, producing an un-reconciled split.
- **Periodic outcome:** Under Periodic, the discrepancy (if any) would only surface at the next stock-closing event, potentially making it harder to detect early.
- **Perpetual outcome:** Under Perpetual, the discrepancy (if any) would be visible sooner, at the next stock move, as a Stock Valuation Account balance that no longer reconciles cleanly by category-grouped report.
- **Historical effect:** Historical (pre-reassignment) transactions are not evidenced to be rewritten — they remain posted against the old category's resolved accounts, consistent with §1.3.
- **Future effect:** Future transactions use the new category's resolved accounts.
- **Required approval/audit trail:** `HOLD/CANDIDATE, elevated priority` — this is the single most operationally risky case in this matrix given the un-tested automatic-revaluation question; recommend this be escalated as a named open question for the Joint Team (`JT-01`) rather than left as an ordinary configuration change, and that no SMEsPlus design assume a "safe" default here without a dedicated proof pass (candidate follow-up: a targeted reference-ERP test-instance walkthrough, out of scope for this documentation-only research session).
- **Migration implication:** Migration replay logic (governing-prompt §10 scenario 31) must not assume category reassignment with existing stock is a no-op; it is a candidate source of un-reconciled inventory-value/account-value splits and should be enumerated as its own migration test case.
- **Fact Status:** HOLD — this is the most material unresolved item in this file; see §4.

### Case 9 — Product accounting override changes mid-period

- **Resolved configuration:** From the moment the product-level Income/Expense Account field is edited, every **subsequent** transaction resolves against the new value; the precedence mechanism itself (§1.1) is unaffected by *when in a period* the change happens — it is a point-in-time field read, not a period-aware calculation.
- **Transaction(s) affected:** Transactions created/posted after the change use the new account; transactions already posted before the change keep their original posted account (§1.3) — meaning a **single accounting period can contain transactions for the same product posted to two different accounts**, purely as a function of when within the period the override was edited.
- **Periodic outcome:** Under Periodic valuation, since COGS is not recognized transaction-by-transaction but derived at closing (file `06` §2.3, file `12`), a mid-period Expense Account override change has **muted** in-period effect on the COGS figure itself (which is computed from opening/closing inventory and net purchases, not by summing per-transaction Expense-Account postings) — but it still affects which account any Income-side or directly-posted entries land in during the period, and it affects which account the eventual closing/variation entry references going forward.
- **Perpetual outcome:** Under Perpetual, since COGS is recognized transaction-by-transaction, a mid-period change produces a genuinely **split COGS presentation within one period** — part of the period's cost-of-sales for this product sits in the old Expense Account, part in the new one. This is a materially different outcome from Periodic and is exactly the kind of "hidden timing assumption" the governing prompt's hard rules forbid glossing over.
- **Historical effect:** None on already-posted entries (per §1.3, PROVISIONAL).
- **Future effect:** All transactions after the change date use the new account.
- **Required approval/audit trail:** `CANDIDATE, high priority` — recommend SMEsPlus require an explicit reason/approval and a system-logged effective-timestamp for any mid-period Income/Expense Account override change on a product, precisely because the reference-ERP-observed mechanism applies the change silently and immediately with no period-boundary awareness; this is offered as a control candidate, not observed reference behavior (the reference ERP is not evidenced to impose any such gate itself).
- **Migration implication:** If historical data being migrated contains evidence of a mid-period override change (i.e., the same product's transactions in one legacy period reference two different accounts), migration tooling must preserve that split rather than "normalizing" it to a single account, or it will misstate historical COGS-by-account reporting.
- **Fact Status:** VERIFIED (mechanism, and the Periodic-muted vs Perpetual-split outcome divergence, both derived directly from file `06`'s account-role findings); PROVISIONAL (no-retroactive-rewrite assumption underlying "historical effect: none," per §1.3).

### Case 10 — Company A and Company B use different policies/accounts

- **Resolved configuration:** The reference ERP's multi-company model scopes Chart of Accounts, and therefore Income/Expense Account values, per company — a Product Category record, and the accounts it references, are evidenced (via the general multi-company chart-of-accounts architecture referenced in file `06` and standard reference-ERP multi-company documentation patterns) to be company-specific or company-filtered, meaning "the same" category name in two companies does not guarantee "the same" resolved account, and a product shared/visible across companies (where the reference ERP supports that) would need company-context-aware resolution at the point of transaction, not merely category/product-level resolution.
- **Transaction(s) affected:** Every transaction is created within a company context; resolution (§1.1) is evidenced to run within that company's chart of accounts, not globally.
- **Periodic outcome / Perpetual outcome:** Each company independently chooses Periodic vs Perpetual and Continental vs Anglo-Saxon (file `06` §2.8) — there is no evidence this session that these are forced to be uniform across companies in a multi-company deployment, meaning **Company A could run Perpetual/Anglo-Saxon while Company B runs Periodic/Continental on the same reference-ERP instance**, with a shared product master resolving to structurally different account *types* (not just different account records) per company.
- **Historical effect:** Historical transactions remain scoped to the company (and its then-current accounts/policy) they were posted in.
- **Future effect:** Future transactions in each company continue to resolve independently per that company's category/product/account configuration.
- **Required approval/audit trail:** `HOLD/JOINT` — cross-referenced to `JT-01` and the Joint controls' inter-company scope generally; whether SMEsPlus permits per-company policy divergence at all (as opposed to enforcing a group-wide standard) is a Joint/governance decision this file cannot make.
- **Migration implication:** Migration tooling must be company-scoped at every resolution step; a "global" product-to-account mapping table would be structurally wrong if any two companies in scope run different Periodic/Perpetual or Continental/Anglo-Saxon policies. This directly affects governing-prompt §10 scenario 26 (inter-company transfer) and deliverable `25_MULTI_COMPANY_TENANT_POLICY_ISOLATION_REGISTER.md`, cross-referenced here rather than re-derived.
- **Fact Status:** PROVISIONAL — this session did not fetch a dedicated multi-company chart-of-accounts documentation page; the claim is architecturally consistent with everything else evidenced (company-scoped accounts, category-only-not-cross-company valuation settings) but is not independently, directly cited. Flagged `HOLD — needs a dedicated multi-company documentation citation` before being relied upon past this research file.

### Case 11 — Category valuation method differs from company default, where reference version permits override

- **Resolved configuration:** Per §1.2, this session's evidence describes Valuation Cadence (Automated/Manual, or 19.0's Periodic/Perpetual) as a **per-category** field, with the company-level Settings screen (Menu A, file `03`) contributing overall accounting-package context (Continental/Anglo-Saxon, default journal) rather than a single overridable "company default cadence" that categories then diverge from. In other words, this session's evidence does **not** clearly establish that a "company default" *for cadence specifically* exists as a distinct concept from "whatever each category is individually configured to" — every category's Automated/Manual (or Periodic/Perpetual) selector is evidenced as independently set, not inherited-then-overridden.
- **Transaction(s) affected:** Every stock-move/bill/invoice transaction for every product in the category, since valuation cadence directly determines which account (Stock Valuation vs Expense/Cost-of-Revenue) and which event carries COGS timing (file `06` §2.3, file `13`).
- **Periodic outcome / Perpetual outcome:** By construction, this case is precisely "category runs one cadence while some other reference point (company-level or another category) runs the other" — the outcome is the full Periodic vs Perpetual divergence documented in files `12`/`13`/`14`, scoped to just this category's products while the rest of the company/other categories behave per their own independent setting.
- **Historical effect:** Transactions posted before a category's cadence setting changed remain governed by the cadence in force at posting time (`PROVISIONAL`, same reasoning as §1.3, not directly re-tested for the cadence field specifically).
- **Future effect:** Transactions after a cadence change follow the new cadence — and changing a category's valuation cadence is evidenced elsewhere (file `06` §2.1/§2.3) to be a materially disruptive change (it redirects which account type multiple fields resolve to), not a cosmetic toggle.
- **Required approval/audit trail:** `HOLD/JOINT` — cross-referenced to `JT-01`; whether SMEsPlus even permits category-level cadence divergence within one company (as opposed to enforcing one cadence company-wide) is an open Joint question this file surfaces but does not answer.
- **Migration implication:** Migration tooling cannot assume a single company-wide cadence; it must read cadence per category (and reconcile against file `06`'s account-type findings per category) before it can correctly map historical postings.
- **Fact Status:** HOLD — the premise of this case ("company default" that a category can diverge from) is not cleanly evidenced as a real configuration concept in the reference ERP; this file records the best-available reading (cadence is category-scoped, full stop, with company-level settings providing package-level context rather than a per-category-overridable default) and flags the case's framing itself as needing file `03`/`04` confirmation.

### Case 12 — Category costing method differs from company default, where reference version permits override

- **Resolved configuration:** Same structural finding as Case 11, applied to Costing Method (Standard/AVCO/FIFO): this session's evidence describes Costing Method as configured **per Product Category** with no company-wide "default that categories override" concept independently confirmed — each category's Costing Method field is its own setting.
- **Transaction(s) affected:** Every receipt/issue cost-layer calculation for every product in the category (file `09`/`15`'s job to detail the cost-layer mechanics; this file only proves the assignment-precedence dimension).
- **Periodic outcome / Perpetual outcome:** Costing Method interacts with cadence but is evidenced as a logically separate axis (file `06` §2.4's Price-Difference-Account finding — Standard Costing plus Perpetual specifically — is itself proof that Costing Method and Cadence are two independent configuration dimensions that combine, not one field). A category running FIFO under Perpetual behaves differently in cost-layer terms than a category running Standard under Perpetual, independent of the Periodic/Perpetual question addressed in Case 11.
- **Historical effect:** A costing-method change on a category with existing valued stock is a recognized hard problem in cost-accounting generally (existing FIFO layers or a prior Standard Price must be reconciled against the new method's opening basis) — no reference-ERP-specific mechanism for this transition was found/tested this session; this is `HOLD`, cross-referenced to governing-prompt §9's costing-method-change research questions and deliverable `15_COSTING_METHOD_DEEP_RESEARCH_MATRIX.md`, which owns this in full detail. This file only flags that the precedence question ("which costing method applies, category's or some default") is answered (category, full stop, per current evidence) while the transition mechanics remain that other file's job.
- **Future effect:** Future receipts/issues use the new costing method's cost-layer logic.
- **Required approval/audit trail:** `HOLD/JOINT` — cross-referenced to `JT-02` (costing methods is a named open Joint decision), which directly owns whether/how a costing-method change is even permitted, let alone how it is approved and logged.
- **Migration implication:** Same category-scoped-not-company-default reasoning as Case 11; additionally, migration replay (governing-prompt §10 scenario 31) must capture the costing method **in force at the time of each historical transaction** per category, not assume a single method for the whole migration window, since categories are independently configurable and could plausibly have changed method historically.
- **Fact Status:** HOLD — same framing caveat as Case 11 (the "company default that a category overrides" premise is not cleanly evidenced), plus a further HOLD on transition mechanics deferred to file `15`.

---

## 3. Summary Table

| # | Case | Resolved winner | Materiality | Fact Status |
|---|---|---|---|---|
| 1 | Category Income, product blank | Category | Low (baseline) | VERIFIED |
| 2 | Category Expense, product blank | Category, but role redirects by cadence | Medium — Periodic/Perpetual structural divergence | VERIFIED |
| 3 | Same Income Account both levels | Product (silent pin) | Medium — future-cascade risk | VERIFIED / PROVISIONAL (visibility gap) |
| 4 | Different Income Accounts | Product | Medium — reporting-grouping risk | VERIFIED |
| 5 | Same Expense Account both levels | Product (silent pin) | High — COGS pinning risk | VERIFIED / PROVISIONAL |
| 6 | Different Expense Accounts | Product | High — direct COGS/event-timing proof case | VERIFIED |
| 7 | Category change, no transactions yet | New category (subject to override) | Low | VERIFIED / PROVISIONAL (override survival) |
| 8 | Category change, existing stock | New category going forward; old value's fate UNRESOLVED | **Highest in this file** | HOLD |
| 9 | Mid-period override change | New account from change point forward | High — Periodic-muted vs Perpetual-split | VERIFIED / PROVISIONAL |
| 10 | Company A vs Company B differ | Company-scoped independently | High — multi-company/inter-company | PROVISIONAL |
| 11 | Category cadence vs "company default" | Category-scoped (premise itself HOLD) | High | HOLD |
| 12 | Category costing method vs "company default" | Category-scoped (premise itself HOLD); transition mechanics deferred to file 15 | High | HOLD |

---

## 4. Single Most Material Open Item

**Case 8 (product changes category with existing stock)** is the most material unresolved item in this file: this session found no evidence, either confirming or ruling out, that the reference ERP automatically transfers/re-classes an existing product's accumulated Stock Valuation Account balance when its Product Category is reassigned. If no such automatic transfer occurs, every historical migration and every live category-reassignment operation risks leaving stranded, un-reconciled value in the old category's Valuation Account while new activity posts to the new category's accounts — directly threatening the governing prompt's Cross-System Reconciliation identity (§14) and the `JT-01` valuation-policy-ownership decision. This is escalated as a named open question, not resolved by this file, and should not be assumed either way by any downstream SMEsPlus design work.

---

## 5. Cross-Reference to Open Joint Decisions

| Joint ID | Cases where surfaced |
|---|---|
| `JT-01` (valuation policy ownership) | 8, 10, 11 |
| `JT-02` (costing methods) | 12 |
| `JT-08` (landed-cost eligibility/posting) | Not directly surfaced by this file's 12 cases; cross-referenced only via file `06` §2.2 |
| `JT-09` (WIP recognition) | Not directly surfaced by this file's 12 cases; cross-referenced only via file `06` §2.6/§2.8 |

Foundational rule reaffirmed: **Inventory emits facts; Accounting decides postings.** Every precedence resolution in this file is an Accounting-configuration-surface mechanism (category/product/company fields); nowhere in this file does Inventory select or influence which account a transaction resolves to.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
