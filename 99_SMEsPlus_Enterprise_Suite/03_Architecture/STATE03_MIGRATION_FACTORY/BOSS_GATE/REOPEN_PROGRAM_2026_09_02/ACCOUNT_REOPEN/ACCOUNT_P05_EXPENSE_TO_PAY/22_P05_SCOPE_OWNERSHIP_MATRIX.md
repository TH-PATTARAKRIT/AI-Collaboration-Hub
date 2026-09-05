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
| `res.partner` (employee contact / vendor) | **TENANT by default, COMPANY-restrictable** — it carries its own optional `company_id` (`res_partner.py:294`) | — | TENANT | TENANT | TENANT, **and core constrains such references with `check_company`** | No | n/a | TENANT-owned master data, optionally company-restricted | Tenant; Company **where the reference is company-constrained** |
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
| **Updated classification** | ~~WITHDRAWN as a scope defect.~~ **REINSTATED, NARROWED — the withdrawal was wrong.** See the correction block below. |
| **Architecture impact** | SMEsPlus must not add company constraints to tenant-scoped partner references; it must instead require **partner presence** where a payment asserts a partner type. |
| **Cross-process impact** | Same rule applies to P01 (vendor references) and P02 (customer references). Recorded as `PEER DEPENDENCY OPEN`. |
| **Evidence required** | None further. |

> ### `R-01` WITHDRAWAL OVERTURNED BY AAS-03 EXPERT 4 — REINSTATED, NARROWED
>
> The withdrawal rested on *"`res.partner` is TENANT-scoped, so requiring `check_company` on a
> reference to it is over-constraint."* **Both halves of that premise are refuted from source:**
>
> 1. **`res.partner` is not purely tenant-scoped.** It carries its own optional `company_id`
>    (`ENT18/base/models/res_partner.py:294`, with `_onchange_company_id` at `:549`). Odoo's own model
>    lets a partner be either shared (`company_id = False`) **or hard-restricted to one company**.
>    §2's row classifying it "TENANT — Tenant only" is therefore **incomplete**, and that
>    mischaracterisation is precisely what let the withdrawal through.
> 2. **Odoo core applies `check_company=True` to partner references for exactly this reason** — e.g.
>    `account.move.partner_id` (`account/models/account_move.py:372-380`). The
>    *"reference scope ≠ financial scope"* argument the withdrawal invented is **contradicted by the
>    platform's own design pattern**.
>
> **The narrowing Expert 4 also supplied, which corrects the original finding in the other direction:**
> because `account.move` and `account.move.line` set `_check_company_auto = True` and their
> `partner_id` carries `check_company=True`, a cross-company vendor **will** be caught when the move
> is created or posted — and `_check_company` runs inside `create()`/`write()`, so **`sudo()` does not
> bypass it**. The defect is therefore **late failure, not absence of any gate**: an invalid
> cross-company vendor can be saved on a draft or submitted expense and only errors at posting.
>
> **Restated finding (`R-01'`)** — *missing early `check_company` validation on the expense line's
> `vendor_id`; enforcement exists only downstream, at move creation/posting, via
> `account.move.partner_id`.* Class: **FACT VERIFIED**, class **A** within the files read.
> This also corrects `04 §4`'s phrasing "there is no gate at any layer" — there is one, it is just late.
> Row 30 of §2 is corrected to **"TENANT by default, COMPANY-restrictable via optional `company_id`"**.

### `R-02` — `petty.cash` has no `company_id`

| | |
|---|---|
| **Original finding** | `TZ-02`, framed as a multi-company/tenant isolation violation on the assumption that every object needs company context. |
| **Scope assumption used** | Blanket. |
| **Why the original framing was wrong** | It asserted the requirement rather than deriving it. |
| **Correct scope analysis** | `petty.cash` **is** COMPANY-scoped, derived and not assumed: its `petty_cash_balance` is Σ(debit−credit) of **posted journal lines** on a specific `account.account` (`petty_cash.py:38-49`). A GL account is COMPANY legal-accounting truth, and a float balance is a company's cash position. The object therefore *creates and reflects a financial effect owned by a single company*. Under `COMPANY SCOPE → Tenant Context MANDATORY, Company Context MANDATORY`, company context is **required and absent**. |
| **Updated classification** | **`TZ-02` UPHELD and strengthened** — derived from the object's own financial semantics rather than from a blanket rule. **Consequence (a) was corrected by AAS-03 Expert 2 and is not what the primary research claimed:** `_compute_petty_cash_balance` is **not** `sudo()`, so the core record rule `account.account_move_line_comp_rule` does company-filter it; the actual effect is that **the same float record reports a different balance to different users** depending on their allowed companies. The genuinely unscoped access is elsewhere — `hr_expense_petty_cash/models/account_move.py:24` does a **`sudo()`, unscoped, `limit=1`** search, so with the global `unique(partner_id)` **company B's vendor bills are gated by company A's float configuration**. Consequence (b) stands unchanged: `_sql_constraints unique(partner_id)` is global, so one partner cannot hold a float in two companies. |
| **Architecture impact** | The SMEsPlus float object must carry an explicit company, and its balance must be a company-scoped query. Ownership of the float (which tenant) and the financial effect (which company) are separate determinations. |
| **Cross-process impact** | P08/P09 cash management. `PEER DEPENDENCY OPEN`. |
| **Evidence required** | **SUPPLIED.** AAS-03 Expert 2 independently searched the whole custom tree (5087 files; patterns declared at `21 NC-05`) and found no other module touching `petty.cash`, no `ir.rule` for it, and zero `company_id`/`check_company` in the module — class **A** *within that root*. The claim is **not** upgraded beyond that root. |

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
