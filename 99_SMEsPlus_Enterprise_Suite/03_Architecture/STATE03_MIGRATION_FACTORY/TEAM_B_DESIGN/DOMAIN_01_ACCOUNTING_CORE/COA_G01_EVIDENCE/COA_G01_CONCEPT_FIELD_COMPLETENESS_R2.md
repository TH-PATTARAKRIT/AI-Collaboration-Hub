# COA-G01 Round 2 — Account Concept Field Completeness (19 Active Account Types)

**CORR1 (2026-08-31): full rebuild.** The original version of this document merged `Evidence Character` and `Fact Status` into a single column (e.g. cells reading "Boss Ruling (target) + Source Observation (partial)" conflated a provenance classification with a truth-value classification), and omitted explicit per-row `Source`, `Source Evidence`, `System/control dependency`, `Base Kernel candidacy`, `Canonicalization relevance`, and `Clean-room status` fields (these were stated once as uniform notes rather than reconciled per concept). This rebuild restructures the document as one subsection per Account Type, with all 17 AS §8.7 fields stated explicitly and individually for every type, and `Evidence Character`/`Fact Status` kept as two distinct fields throughout.

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Reconcile all 17 mandatory concept fields (AS §8.7), each field explicit and non-merged, for each of the 19 Boss-approved active Account Types | Claude (session SMEPLUS-26-08-30-COA-G01R2-001, CORR1 pass) | `AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md`; Team A `02_SOURCE_EVIDENCE.md`, `06_BUSINESS_RULE_REGISTER.md`; `COA_STANDARD/` | 2026-08-31 | ChatGPT Independent Review (pending); Boss (pending) | See per-type sections | Closes AR record E-04; corrects CORR1 finding on Evidence Character/Fact Status merging |

**Allowed `Fact Status` values (AS §8.7, used verbatim below):** `VERIFIED FACT`, `SUPPORTED INFERENCE`, `ASSUMPTION`, `UNKNOWN`, `EVIDENCE_MISSING`, `CONFLICTING EVIDENCE`.
**Allowed `Evidence Character` values (AS §8.7, used verbatim below):** `Source Observation`, `Boss Ruling`, `Regulatory Verification`, `Real-User Validation`, `Unclassified / Missing`.
These are two independent axes: a fact can be a `Boss Ruling` with `Fact Status: VERIFIED FACT` (the ruling itself is verifiably on record) while a *different* claim about the same concept is a `Source Observation` with `Fact Status: SUPPORTED INFERENCE`. Cells below give both axes separately wherever a concept has more than one applicable claim.

---

## 1. Receivable

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17` (`account_account.py` L44–72, 19-value enum); `AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md`
- **Business Meaning:** Amounts owed to the business by customers
- **Thailand Relevance:** High — WHT-at-payment timing (finding S2) affects posting on settlement
- **Account Type:** Receivable (Asset)
- **Financial Class:** Asset
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Reconcile-eligible per the `reconcile` flag (Team A `SE-20`); matching mechanics beyond the flag's existence = `UNKNOWN` (AR record Q-07)
- **Tax relevance:** Indirect (VAT output timing, WHT certificates on collection)
- **Financial Statement relevance:** Balance Sheet — current asset
- **System/control dependency:** Type drives `include_initial_balance` / `internal_group` (Team A `SE-18`, `BR-15`, `BR-16`)
- **Base Kernel candidacy:** Not decided at this Gate — COA-G02 scope
- **Canonicalization relevance:** Template-entry concept layer only; not canonical by Account Code/Name (SI-05)
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` (the 19-type enum) + `Boss Ruling` (this type is in the active 19)
- **Fact Status:** `VERIFIED FACT` (both the source enum and the Boss ruling are independently on record)
- **Conflict / Gap / Unknown:** None
- **Clean-room status:** Clean — business meaning and type classification only; no vendor code/schema/field-name adopted as SMEsPlus architecture

## 2. Bank and Cash

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Cash and bank-held funds
- **Thailand Relevance:** High — PromptPay QR (Thai toolchain finding T-series), bank integration
- **Account Type:** Bank and Cash (Asset)
- **Financial Class:** Asset
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Reconcile-eligible; bank reconciliation is the canonical use of the `reconcile` flag
- **Tax relevance:** Indirect
- **Financial Statement relevance:** Balance Sheet — current asset
- **System/control dependency:** Same as Receivable (type-driven `include_initial_balance`/`internal_group`)
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** None
- **Clean-room status:** Clean

## 3. Current Assets

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling; Odoo18 workbook rows 32–36 (prepayment-named accounts observed under this type)
- **Business Meaning:** Short-term assets not otherwise classified
- **Thailand Relevance:** Medium
- **Account Type:** Current Assets (Asset)
- **Financial Class:** Asset
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not typically reconcile-flagged
- **Tax relevance:** Indirect
- **Financial Statement relevance:** Balance Sheet — current asset
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High (type existence); Medium (specific row classification, see conflict below)
- **Evidence Character:** `Source Observation` (type existence) + `Source Observation` (workbook row classification, rows 32–36)
- **Fact Status:** `VERIFIED FACT` (type exists) / `CONFLICTING EVIDENCE` (whether specific prepayment-named rows belong here or under `Prepayments`)
- **Conflict / Gap / Unknown:** `CF-G01-03` (carried) — source workbook classifies some prepayment-named accounts (rows 32–36) here rather than under `Prepayments`; routed to COA-G03/G04, not merged in this Gate
- **Clean-room status:** Clean

## 4. Non-current Assets

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Long-term assets not otherwise classified
- **Thailand Relevance:** Low
- **Account Type:** Non-current Assets (Asset)
- **Financial Class:** Asset
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not typically reconcile-flagged
- **Tax relevance:** Indirect
- **Financial Statement relevance:** Balance Sheet — non-current asset
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** None
- **Clean-room status:** Clean

## 5. Prepayments

- **Source:** `AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md` (target requirement); Odoo18 workbook rows 32–36 (partial source observation)
- **Source Evidence:** `AJ` ruling text; workbook rows 32–36 (typed `Current Assets` in the source, not `Prepayments` — see conflict)
- **Business Meaning:** Payments made in advance of expense recognition
- **Thailand Relevance:** Medium
- **Account Type:** Prepayments (Asset)
- **Financial Class:** Asset
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not typically reconcile-flagged
- **Tax relevance:** Indirect
- **Financial Statement relevance:** Balance Sheet — current/non-current asset
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** Medium — **Boss-required despite absence from the `l10n_th` template; only 5 workbook rows plausibly relate, and those are typed differently in-source**
- **Evidence Character:** `Boss Ruling` (the type is active/required) — this is distinct from the weaker `Source Observation` for the specific rows
- **Fact Status:** `VERIFIED FACT` (the Boss ruling that this type is active) — the claim "these specific source rows belong to this type" is `CONFLICTING EVIDENCE`, not `VERIFIED FACT`
- **Conflict / Gap / Unknown:** Source/target classification delta — prepayment-named source rows are typed `Current Assets`, not `Prepayments`; routed to COA-G03/G04
- **Clean-room status:** Clean — no vendor architecture adopted; Boss ruling is an independent target decision, not a copy of source structure

## 6. Fixed Assets

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Long-lived tangible/intangible assets
- **Thailand Relevance:** High — depreciation, asset register
- **Account Type:** Fixed Assets (Asset)
- **Financial Class:** Asset
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not reconcile-flagged; depreciation schedule is a distinct control (see `Depreciation` below)
- **Tax relevance:** Indirect (depreciation deductibility)
- **Financial Statement relevance:** Balance Sheet — non-current asset
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High (type existence); Medium (accumulated-depreciation row classification, see conflict)
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT` (type exists) / `CONFLICTING EVIDENCE` (accumulated-depreciation row typing — see `Depreciation` below)
- **Conflict / Gap / Unknown:** `CF-G01-02` (carried) — see `Depreciation` row for detail
- **Clean-room status:** Clean

## 7. Payable

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Amounts owed by the business to vendors
- **Thailand Relevance:** High — WHT-at-payment (S2), Tax Branch addressing (S5)
- **Account Type:** Payable (Liability)
- **Financial Class:** Liability
- **Normal Balance:** Credit
- **Reconciliation behaviour:** Reconcile-eligible
- **Tax relevance:** Indirect (WHT deduction at payment, VAT input timing)
- **Financial Statement relevance:** Balance Sheet — current liability
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** None
- **Clean-room status:** Clean

## 8. Credit Card

- **Source:** `AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md` (target requirement only)
- **Source Evidence:** `AJ` ruling text; **no workbook rows and no `l10n_th` template rows observed for this type**
- **Business Meaning:** Amounts owed on company credit facilities
- **Thailand Relevance:** Low
- **Account Type:** Credit Card (Liability)
- **Financial Class:** Liability
- **Normal Balance:** Credit
- **Reconciliation behaviour:** Reconcile-eligible (statement matching) — by accounting-domain convention, not observed in this source
- **Tax relevance:** Indirect
- **Financial Statement relevance:** Balance Sheet — current liability
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group` (by rule; not source-observed for this specific type)
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** Low — **no source-row evidence exists for this type at all**
- **Evidence Character:** `Boss Ruling` only — no `Source Observation` exists for this type
- **Fact Status:** `VERIFIED FACT` (the Boss ruling itself is on record) — but this must not be read as evidence the type is source-observed; it is not
- **Conflict / Gap / Unknown:** No source-observation evidence at all for this type; entirely a Boss-required target capability
- **Clean-room status:** Clean — no source structure to copy in the first place

## 9. Current Liabilities

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling; Odoo18 workbook rows 42–46, 388 (tax-related sub-accounts observed under this generic type)
- **Business Meaning:** Short-term obligations not otherwise classified
- **Thailand Relevance:** Medium (generic) / High (for the embedded tax sub-accounts)
- **Account Type:** Current Liabilities (Liability)
- **Financial Class:** Liability
- **Normal Balance:** Credit
- **Reconciliation behaviour:** Not typically reconcile-flagged
- **Tax relevance:** Indirect at the type level; **direct** for the embedded WHT/prepaid-CIT/input-VAT/VAT-suspense rows
- **Financial Statement relevance:** Balance Sheet — current liability
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** Tax-relevant sub-accounts (WHT, prepaid CIT, input VAT/VAT suspense) currently sit under this generic type in the source workbook — routed to COA-G06, not reclassified here
- **Clean-room status:** Clean

## 10. Non-current Liabilities

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Long-term obligations not otherwise classified
- **Thailand Relevance:** Low
- **Account Type:** Non-current Liabilities (Liability)
- **Financial Class:** Liability
- **Normal Balance:** Credit
- **Reconciliation behaviour:** Not typically reconcile-flagged
- **Tax relevance:** Indirect
- **Financial Statement relevance:** Balance Sheet — non-current liability
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** None
- **Clean-room status:** Clean

## 11. Equity

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Owners' residual claim
- **Thailand Relevance:** Medium
- **Account Type:** Equity (Equity)
- **Financial Class:** Equity
- **Normal Balance:** Credit
- **Reconciliation behaviour:** Not reconcile-flagged
- **Tax relevance:** Direct in principle (statutory capital/reserve requirements are Thailand company-law dependent) — not researched this Gate
- **Financial Statement relevance:** Balance Sheet — equity
- **System/control dependency:** Type-driven `include_initial_balance`/`internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High (type existence); none (statutory capital/reserve rules)
- **Evidence Character:** `Source Observation` + `Boss Ruling` (type); `Unclassified / Missing` (statutory capital/reserve rules)
- **Fact Status:** `VERIFIED FACT` (type exists) / `UNKNOWN` (Thai statutory capital/reserve requirements)
- **Conflict / Gap / Unknown:** Thai statutory capital/reserve requirements not researched at this Gate — `UNKNOWN`, routed to COA-G06
- **Clean-room status:** Clean

## 12. Current Year Earnings

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`, `SE-18` (`include_initial_balance` carry-forward semantics); `AJ` ruling; Odoo18 workbook row 385
- **Business Meaning:** Current fiscal-year profit/loss carry, distinct from prior-year Retained Earnings
- **Thailand Relevance:** High — must not double-count with Retained Earnings (a finding independently raised and closed in Team B's `M-AUD-08` corrective round, per `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md` §5 audit chronology)
- **Account Type:** Current Year Earnings (Equity / result carry)
- **Financial Class:** Equity (result carry)
- **Normal Balance:** Credit for profit; may debit for loss
- **Reconciliation behaviour:** Not reconcile-flagged; closes to Equity at year-end (`SE-18` semantics)
- **Tax relevance:** Indirect (CIT computed on net result)
- **Financial Statement relevance:** Balance Sheet equity; links to P&L
- **System/control dependency:** `include_initial_balance` carry-forward mechanics
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Must remain distinct from ordinary Income/Expense and from Retained Earnings — reaffirmed, not re-litigated, this session
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** None (the double-counting risk was a Team B design-audit finding, already closed — see cross-reference above; not an open COA-G01 conflict)
- **Clean-room status:** Clean

## 13. Income

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Revenue from ordinary operations
- **Thailand Relevance:** High — VAT output tax point
- **Account Type:** Income (P&L)
- **Financial Class:** P&L (income)
- **Normal Balance:** Credit
- **Reconciliation behaviour:** Not reconcile-flagged
- **Tax relevance:** Direct — VAT output
- **Financial Statement relevance:** Profit & Loss
- **System/control dependency:** Type-driven `internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** None
- **Clean-room status:** Clean

## 14. Other Income

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Non-operating income
- **Thailand Relevance:** Low
- **Account Type:** Other Income (P&L)
- **Financial Class:** P&L (income)
- **Normal Balance:** Credit
- **Reconciliation behaviour:** Not reconcile-flagged
- **Tax relevance:** Direct — VAT/CIT treatment may differ from ordinary Income
- **Financial Statement relevance:** Profit & Loss
- **System/control dependency:** Type-driven `internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High (type existence); none (differential VAT/CIT treatment)
- **Evidence Character:** `Source Observation` + `Boss Ruling` (type); `Unclassified / Missing` (differential tax treatment)
- **Fact Status:** `VERIFIED FACT` (type exists) / `UNKNOWN` (differential VAT/CIT treatment vs. ordinary Income)
- **Conflict / Gap / Unknown:** Differential VAT/CIT treatment not researched this Gate — `UNKNOWN`, routed to COA-G06
- **Clean-room status:** Clean

## 15. Expenses

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling
- **Business Meaning:** Ordinary operating expense
- **Thailand Relevance:** High — deductibility, WHT-at-payment on many expense categories
- **Account Type:** Expenses (P&L)
- **Financial Class:** P&L (expense)
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not reconcile-flagged
- **Tax relevance:** Direct — CIT deductibility, WHT withholding obligation
- **Financial Statement relevance:** Profit & Loss
- **System/control dependency:** Type-driven `internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High
- **Evidence Character:** `Source Observation` + `Boss Ruling`
- **Fact Status:** `VERIFIED FACT`
- **Conflict / Gap / Unknown:** None
- **Clean-room status:** Clean

## 16. Other Expenses

- **Source:** `AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md` (target requirement); thin source observation
- **Source Evidence:** `AJ` ruling text; **no workbook rows distinctly separate this from ordinary `Expenses`**
- **Business Meaning:** Non-operating expense
- **Thailand Relevance:** Medium — Boss-required despite absence from the `l10n_th` template
- **Account Type:** Other Expenses (P&L)
- **Financial Class:** P&L (expense)
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not reconcile-flagged
- **Tax relevance:** Direct — non-deductible-expense rules are a named TB-05/COA-G06 dependency
- **Financial Statement relevance:** Profit & Loss
- **System/control dependency:** Type-driven `internal_group` (by rule, not source-observed for this specific type)
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** Medium
- **Evidence Character:** `Boss Ruling` (type active) — no distinct `Source Observation` separates this from `Expenses`
- **Fact Status:** `VERIFIED FACT` (the Boss ruling) / `UNKNOWN` (whether any specific source row belongs here rather than under `Expenses`)
- **Conflict / Gap / Unknown:** No workbook rows distinctly separate this type from ordinary `Expenses` — routed to COA-G03/G04
- **Clean-room status:** Clean

## 17. Depreciation

- **Source:** Core Accounting source `account_type` enumeration; Odoo18 workbook rows 71–74 and later accumulated-depreciation rows
- **Source Evidence:** Team A `SE-17`; `AJ` ruling; workbook rows 71, 74 (typed `Depreciation`) vs. 72–73 and most later accumulated-depreciation rows (typed `Fixed Assets`)
- **Business Meaning:** Periodic allocation of fixed-asset cost
- **Thailand Relevance:** Medium
- **Account Type:** Depreciation (P&L expense classification)
- **Financial Class:** P&L (expense), feeds Fixed Assets accumulated balance
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not reconcile-flagged
- **Tax relevance:** Direct — CIT depreciation-rate rules (Revenue Department)
- **Financial Statement relevance:** Profit & Loss; balance-sheet contra-asset linkage
- **System/control dependency:** Type-driven `internal_group`
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** Medium — inconsistent source classification (see conflict)
- **Evidence Character:** `Source Observation` (both the `Depreciation`-typed and `Fixed Assets`-typed accumulated-depreciation rows are directly observed, and they disagree)
- **Fact Status:** `CONFLICTING EVIDENCE` — the two groups of source rows are genuinely inconsistent with each other, not merely incomplete
- **Conflict / Gap / Unknown:** `CF-G01-02` (carried, reconfirmed) — accumulated-depreciation rows are inconsistently typed `Depreciation` (rows 71, 74) vs. `Fixed Assets` (rows 72–73 and most later rows) in the 389-row workbook; a genuine source-quality issue, not resolved by this session, routed to COA-G03/G05 for business-meaning-based reclassification
- **Clean-room status:** Clean — the conflict is a source-data-quality observation, not an architecture-copying issue

## 18. Cost of Revenue

- **Source:** Core Accounting source `account_type` enumeration
- **Source Evidence:** Team A `SE-17`; `AJ` ruling; Team A `INT-05` (inventory-valuation coupling, `14_INTEGRATION_REGISTER.md`)
- **Business Meaning:** Direct cost attributable to revenue generation
- **Thailand Relevance:** Medium — inventory valuation linkage
- **Account Type:** Cost of Revenue (P&L)
- **Financial Class:** P&L (cost)
- **Normal Balance:** Debit
- **Reconciliation behaviour:** Not reconcile-flagged
- **Tax relevance:** Direct — COGS deductibility
- **Financial Statement relevance:** Profit & Loss
- **System/control dependency:** Type-driven `internal_group`; inventory-valuation coupling (`INT-05`) — existence known, mechanism not researched
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only
- **Evidence strength:** High (type existence); low (inventory-valuation interaction mechanism)
- **Evidence Character:** `Source Observation` + `Boss Ruling` (type); `Unclassified / Missing` (inventory-valuation coupling mechanism — Team A's own statement: "no research performed on the deferred side")
- **Fact Status:** `VERIFIED FACT` (type exists) / `UNKNOWN` (inventory-valuation interaction beyond the fact that a coupling point exists)
- **Conflict / Gap / Unknown:** Inventory-valuation coupling is Team A `INT-05`; treat COGS/inventory interaction as `UNKNOWN` beyond existence of the coupling
- **Clean-room status:** Clean

## 19. Off-Balance Sheet

- **Source:** `AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md` (target requirement); minimal source observation
- **Source Evidence:** `AJ` ruling text; session-prompt §7 (excluded from ordinary totals by default); **no substantive workbook or `l10n_th` row evidence identified**
- **Business Meaning:** Tracking of items outside the entity's recognized financial position (e.g. guarantees, consignment, commitments)
- **Thailand Relevance:** Medium — Boss-controlled special rule; excluded from ordinary totals by default
- **Account Type:** Off-Balance Sheet (Memorandum)
- **Financial Class:** Memorandum — outside ordinary BS/P&L totals
- **Normal Balance:** Controlled memorandum treatment, not a simple debit/credit generalization
- **Reconciliation behaviour:** Not reconcile-flagged in the ordinary sense; requires its own control model (COA-G05/G07)
- **Tax relevance:** Indirect, context-dependent
- **Financial Statement relevance:** Reported separately from ordinary BS/P&L by default (Boss ruling)
- **System/control dependency:** Full control-model design deferred to COA-G05/COA-G07
- **Base Kernel candidacy:** Not decided at this Gate
- **Canonicalization relevance:** Template-entry concept layer only; full layering deferred
- **Evidence strength:** Medium — Boss-required active capability; weakest source-observation depth of the 19 types
- **Evidence Character:** `Boss Ruling` — essentially no independent `Source Observation` exists for this type
- **Fact Status:** `VERIFIED FACT` (the Boss ruling that this type is active and excluded from ordinary totals by default) — the underlying control model itself is `UNKNOWN` (not yet designed)
- **Conflict / Gap / Unknown:** Full control-model design deferred to COA-G05/COA-G07; this Gate only confirms the type is active and excluded from ordinary totals by default
- **Clean-room status:** Clean — no source structure exists to copy

---

## Explicit statement on evidence-strength floor

Three types — **Credit Card, Other Expenses, Off-Balance Sheet** — carry no or minimal direct source-row observation and exist in the 19-type target baseline purely by `Boss Ruling` `Evidence Character`, with `Fact Status: VERIFIED FACT` applying only to the ruling itself, not to any claim that the type is source-observed. This is not a defect: `l10n_th`/workbook omission was already ruled non-prohibitive by the `AJ` ruling. It is recorded explicitly here, with Evidence Character and Fact Status kept separate throughout, so COA-G02/G03 do not mistake "Boss-required, thin evidence" for "fully source-verified" when selecting kernel candidates.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
