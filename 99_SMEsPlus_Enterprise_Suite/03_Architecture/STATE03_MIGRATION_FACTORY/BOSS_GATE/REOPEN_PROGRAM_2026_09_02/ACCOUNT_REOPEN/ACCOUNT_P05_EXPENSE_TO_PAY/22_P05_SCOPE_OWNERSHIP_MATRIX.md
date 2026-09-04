# 22 — P05 SCOPE OWNERSHIP MATRIX

`LAYER 2 — AUDIT QUARANTINE`
Issued under `SMEPLUS-26-09-04-ACC-REV2-CORR1` (Scope-Aware Constitution Correction).
Supersedes, **for this package only**, any earlier wording implying blanket
"Tenant Context + Company Context mandatory for every operation".

## 1. Canonical Rule Applied

`SCOPE-AWARE EVERYWHERE.` Each object below is assessed on eight axes:
OWN / EXECUTE / ACCESS / MUTATE / REFERENCE / financial effect? / owning company of that effect /
data character (PLATFORM reference vs TENANT-owned vs COMPANY legal-accounting truth).

Context requirement follows the proven scope; it is **not** assumed.
`MISSING REQUIRED SCOPE = DENY`. `OWNERSHIP ≠ AVAILABILITY`.

## 2. P05 Object Scope Determination

| Object | Owns | Executes | Access | Mutate | Reference | Fin. effect | Company owning it | Data character | Required context |
|---|---|---|---|---|---|---|---|---|---|
| `hr.expense` (claim line) | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | **Yes** (via the sheet) | the line's `company_id` | COMPANY accounting truth | Tenant + Company |
| `hr.expense.sheet` (claim) | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | **Yes** | `company_id` (required, readonly) | COMPANY accounting truth | Tenant + Company |
| `account.move` / `account.move.line` | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | **Yes** | the move's `company_id` | COMPANY legal truth | Tenant + Company |
| `account.payment` | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | **Yes** | the payment's `company_id` | COMPANY legal truth | Tenant + Company |
| `petty.cash` (float master) | **COMPANY** | COMPANY | COMPANY | COMPANY | COMPANY | **Yes** — its balance is Σ posted GL lines on a company's account | undeterminable in the reference (no field) | COMPANY accounting truth | Tenant + Company |
| `advance.expense.request` | COMPANY | COMPANY | TENANT-visible, COMPANY-authoritative | COMPANY | COMPANY | **Yes** (posts a bill) | `company_id` (required) | COMPANY accounting truth | Tenant + Company |
| `advance.expense.request.line` | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | Yes (via parent) | related `company_id` | COMPANY | Tenant + Company |
| `account.withholding.tax` **(rate + form class)** | **PLATFORM candidate** | — | PLATFORM | PLATFORM | TENANT/COMPANY | No, by itself | n/a | statutory PLATFORM reference | Tenant **not** required for the rate |
| `account.withholding.tax` **(GL account mapping)** | **COMPANY** | COMPANY | COMPANY | COMPANY | COMPANY | Yes, when applied | the payment's company | COMPANY | Tenant + Company |
| `res.partner` (employee contact / vendor) | **TENANT** | — | TENANT | TENANT | TENANT | No | n/a | TENANT-owned master data | Tenant only |
| `res.partner.property_account_payable_id` | **COMPANY** (company-dependent property) | COMPANY | COMPANY | COMPANY | COMPANY | Yes, when applied | the reading company | COMPANY | Tenant + Company |
| `hr.employee` | **TENANT** (HR master) — but one record per company in the reference | TENANT | TENANT | TENANT | TENANT/COMPANY | No | n/a | TENANT-owned | Tenant only |
| `hr.employee.ae_approver` (advance approver) | **TENANT** policy, **COMPANY** effect | COMPANY | TENANT | TENANT | COMPANY | No directly | company of the request it gates | TENANT policy | Tenant; Company at execution |
| `product.product` / `product.template` used as an expense category | **TENANT** | — | TENANT | TENANT | TENANT | No | n/a | TENANT-owned catalogue | Tenant only |
| `product.property_account_expense_id` | **COMPANY** (company-dependent) | COMPANY | COMPANY | COMPANY | COMPANY | Yes, when applied | the reading company | COMPANY | Tenant + Company |
| `account.journal` | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | Yes | `company_id` | COMPANY | Tenant + Company |
| `account.payment.method.line` | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | Yes | journal's company | COMPANY | Tenant + Company |
| Approval **policy** (who may approve what) | **TENANT** | COMPANY | TENANT | TENANT | COMPANY | No | company of the gated event | TENANT-owned policy | Tenant; Company at execution |
| Expense **evidence** (receipt attachment) | TENANT | — | TENANT, restricted | TENANT | COMPANY | No | n/a | TENANT-owned document | Tenant only |
| Analytic plan / distribution model | **TENANT** (may be COMPANY-restricted) | COMPANY | TENANT | TENANT | COMPANY | No | n/a | TENANT-owned dimension | Tenant; Company where restricted |

## 3. Revalidation of Findings Affected by the Superseded Assumption

Per correction §6, only findings **materially affected** by the incorrect Tenant+Company-everywhere
assumption are revalidated. All other evidence, source links, contradictions and lineage are preserved
unchanged.

### `R-01` — `hr.expense.vendor_id` has no `check_company`

| | |
|---|---|
| **Original finding** | `04 §6` recorded `vendor_id` as "Unconstrained" because it lacks `check_company`. |
| **Scope assumption used** | Blanket: every reference must be company-constrained. |
| **Why over-constrained** | `res.partner` is **TENANT-scoped** master data (§2). `REFERENCE SCOPE ≠ FINANCIAL SCOPE`. A company-owned entry legitimately *references* a tenant-owned partner. Requiring company context on the reference itself is over-constraint. |
| **Correct scope analysis** | The financial effect is owned by the move's company; the partner reference is tenant-scoped. Absence of `check_company` on `vendor_id` is **not** a scope defect. |
| **Updated classification** | **WITHDRAWN as a scope defect.** The *separate* finding at `04 §4` — that `vendor_id` is optional while `partner_type` is hard-coded `'supplier'`, producing a supplier payment with no partner — **stands unchanged**, as it is an identity-completeness defect, not a scope defect. |
| **Architecture impact** | SMEsPlus must not add company constraints to tenant-scoped partner references; it must instead require **partner presence** where a payment asserts a partner type. |
| **Cross-process impact** | Same rule applies to P01 (vendor references) and P02 (customer references). Recorded as `PEER DEPENDENCY OPEN`. |
| **Evidence required** | None further. |

### `R-02` — `petty.cash` has no `company_id`

| | |
|---|---|
| **Original finding** | `TZ-02`, framed as a multi-company/tenant isolation violation on the assumption that every object needs company context. |
| **Scope assumption used** | Blanket. |
| **Why the original framing was wrong** | It asserted the requirement rather than deriving it. |
| **Correct scope analysis** | `petty.cash` **is** COMPANY-scoped, derived and not assumed: its `petty_cash_balance` is Σ(debit−credit) of **posted journal lines** on a specific `account.account` (`petty_cash.py:38-49`). A GL account is COMPANY legal-accounting truth, and a float balance is a company's cash position. The object therefore *creates and reflects a financial effect owned by a single company*. Under `COMPANY SCOPE → Tenant Context MANDATORY, Company Context MANDATORY`, company context is **required and absent**. |
| **Updated classification** | **`TZ-02` UPHELD and strengthened** — it is now derived from the object's own financial semantics rather than from a blanket rule. Two concrete consequences, both structural: (a) `_compute_petty_cash_balance` searches `account.move.line` with **no company domain**, so in a multi-company database one holder's float balance aggregates every company's postings; (b) `_sql_constraints unique(partner_id)` is **globally** unique, so one partner cannot hold a float in two companies. |
| **Architecture impact** | The SMEsPlus float object must carry an explicit company, and its balance must be a company-scoped query. Ownership of the float (which tenant) and the financial effect (which company) are separate determinations. |
| **Cross-process impact** | P08/P09 cash management. `PEER DEPENDENCY OPEN`. |
| **Evidence required** | Expert 2 tasked to search the whole custom tree for any other module adding company scoping to `petty.cash` (`16 §4`, `21 NC-05`). Until that returns, the absence is class **B**, not class **A**. |

### `R-03` — `account.withholding.tax.company_id` is required

| | |
|---|---|
| **Original finding** | Recorded in `04 §6` as "Constrained" — i.e. treated as correct because it had a company field and a company rule. |
| **Scope assumption used** | Blanket: company scoping is always right. |
| **Why it is over-constrained** | The object conflates two different scopes in one record. A Thai WHT **rate and form classification** is statutory — a `PLATFORM` reference candidate, identical for every tenant and every company. The **GL account** it posts to is `COMPANY` truth. By making the whole record COMPANY-scoped and `company_id` required (`account_withholding_tax.py:26`), the reference forces the statutory rate to be duplicated once per company, with no mechanism keeping the duplicates equal. |
| **Correct scope analysis** | Split the object: PLATFORM statutory reference (rate, form class, tag semantics) + COMPANY mapping (account, journal). |
| **Updated classification** | **NEW FINDING `SC-01`** — over-constrained scope in the reference; statutory reference data is company-duplicated. Severity MEDIUM, but HIGH for statutory correctness because divergence between per-company copies is undetectable. |
| **Architecture impact** | SMEsPlus must model statutory tax reference at PLATFORM scope. |
| **Cross-process impact** | P01, P02, P07 all consume tax reference. `PEER DEPENDENCY OPEN`. |
| **Evidence required** | The **statutory** assertion that Thai WHT rates are uniform across companies is `HOLD / EVIDENCE REQUIRED` — routed to the Accounting-Tax track. The **structural** assertion (one record conflates two scopes) is FACT VERIFIED from source and stands independently. |

### `R-04` — `advance.expense.request.assigned_to` resolves through a One2many

| | |
|---|---|
| **Original finding** | `P05-F-12`, framed as "cross-company approver leakage". |
| **Scope assumption used** | Blanket company enforcement on an approval field. |
| **Correct scope analysis** | Approval **policy** is TENANT-scoped (§2); the approval **execution** gates a COMPANY-owned financial effect. The defect is therefore not that the approver is not company-filtered — it is that **the executing scope is not determined at all**. `related="requested_by.employee_ids.ae_approver"` silently takes the first employee record; in a tenant with several companies the approver is drawn from an arbitrary company's HR record, with no assertion that it is the company owning the financial effect. |
| **Updated classification** | **UPHELD, re-derived.** Restated as: *the operation does not determine its executing scope before resolving its authoriser.* This is a `MISSING REQUIRED SCOPE = DENY` case that instead resolves silently. |
| **Architecture impact** | Authoriser resolution must take the financial effect's company as an explicit input. |
| **Cross-process impact** | Every approval in P01–P10. `PEER DEPENDENCY OPEN`. |

### `R-05` — `hr.expense.sheet.company_id` required + readonly, `_check_expense_lines_company`

| | |
|---|---|
| **Original finding** | Recorded as "Constrained" (correct). |
| **Revalidation** | Confirmed correct under scope-aware rules and **not** over-constrained: the claim carries a financial effect, so COMPANY scope is genuinely required. No change. |

### `R-06` — Findings NOT affected by the correction

The following are unaffected because they do not rest on any scope assumption. They are preserved
unchanged with their original evidence and lineage: `C-01` (payment guard comma), `EX-04`/`TZ-01`
(petty cash GL redirection), `EX-08` (direct `state` write), `GL-05` (line-0 account), `GL-06`
(missing currency on clearing lines), `P05-F-14` (inverted receipt mapping), `P05-F-15`
(`self` assignment in a loop), `RI-01`–`RI-07`, `SR-01`–`SR-07`, `AN-01`–`AN-06`.

## 4. Scope Determinations Still Open

| ID | Question | Disposition |
|---|---|---|
| `SO-01` | Is `hr.employee` TENANT-scoped with company-specific *contracts*, or genuinely one record per company? The reference implies the latter (`requested_by.employee_ids` is a One2many). This decides `R-04`'s remedy. | `HOLD — SCOPE EVIDENCE REQUIRED`; unaffected work continues |
| `SO-02` | Is an expense **category** (product) TENANT reference or COMPANY reference? Its expense account is company-dependent, which suggests TENANT object + COMPANY property — the split this package recommends for WHT (`SC-01`). | `HOLD — SCOPE EVIDENCE REQUIRED` |
| `SO-03` | Do unrelated independent companies in the current deployment share a tenant? Per the correction, unrelated independent companies are **separate tenants by default**. Not determinable from source. | `HOLD — SCOPE EVIDENCE REQUIRED`; depends on `U-01` |
| `SO-04` | Which scope owns an expense **evidence document** once it has been copied onto a company's journal entry (`hr_expense_sheet.py:838-841` copies attachments onto the move)? The document is duplicated across scopes by design. | `HOLD — SCOPE EVIDENCE REQUIRED` |

## 5. Peer Dependency Status

`PEER DEPENDENCY OPEN` — P01, P02, P03 sibling sessions were cloned from the same base commit
`88f52cd` and had produced no committed scope determination at the time this file was written.
P05 does **not** stop for them. P11 is to reconcile scope semantics across P01–P10 continuously;
the four cross-process items raised above (`R-01`, `R-02`, `R-03`, `R-04`) are the P05 contributions
to that reconciliation.
