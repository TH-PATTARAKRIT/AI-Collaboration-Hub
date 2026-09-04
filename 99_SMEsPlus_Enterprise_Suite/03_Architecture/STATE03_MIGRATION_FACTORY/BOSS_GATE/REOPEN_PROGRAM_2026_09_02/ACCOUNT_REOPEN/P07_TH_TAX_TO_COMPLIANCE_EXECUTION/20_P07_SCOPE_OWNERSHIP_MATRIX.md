# P07 — SCOPE OWNERSHIP MATRIX

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Issued under: `SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Rule Applied

The correction supersedes any blanket "Tenant Context + Company Context are mandatory for
every operation" wording. The canonical rule is **SCOPE-AWARE EVERYWHERE**: determine the
applicable scope first, then derive the context requirement.

| Scope | Tenant context | Company context |
|---|---|---|
| `PLATFORM` | not required | not required |
| `TENANT` | mandatory | not required unless the specific operation is company-scoped |
| `COMPANY` | mandatory | mandatory |

`MISSING REQUIRED SCOPE = DENY`. `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`.
`OWNERSHIP != AVAILABILITY`. Ownership, operational, financial and reference scope are
distinct and are answered separately below.

Definitions used: `TENANT` = security / customer boundary. `COMPANY` = legal / accounting
/ business boundary. Unrelated independent companies are separate tenants by default.

## 2. Method

For every material P07 object the eight correction questions are answered from business,
legal and accounting semantics plus source evidence. Where the answer cannot be
established from the declared source set the row records
`HOLD — SCOPE EVIDENCE REQUIRED` rather than assuming a scope.

Column key: `OWN` owning scope · `EXEC` scope that executes the operation ·
`ACCESS` scope that may read · `MUTATE` scope that may change · `REF` scope that may
reference · `FIN` creates a financial effect · `FIN-OWNER` company owning that effect.

## 3. Matrix — Statutory Reference Layer

| # | Object | OWN | EXEC | ACCESS | MUTATE | REF | FIN | FIN-OWNER | Observed placement | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Thai statutory rate and form catalogue (VAT 7 / 0 / exempt; WHT 1 / 2 / 3 / 5; PND form set; s.40 income-type list) | `PLATFORM` | `PLATFORM` | `PLATFORM` | `PLATFORM` | `TENANT`, `COMPANY` | no | — | Shipped as per-company template CSV applied at chart installation (`l10n_th/data/template/account.tax-th.csv`, `account.tax.group-th.csv`) and as a Python module constant for income types (`l10n_th_withholding_tax_cert/models/withholding_tax_cert.py:16-64`). | **OVER-INSTANTIATED.** A `PLATFORM` reference is materialised once per company and becomes independently mutable per company. Not a defect under the correction (physical singularity is not required) but it removes any single source of truth for the national catalogue. `P07-F-30` |
| 2 | Statutory report structure (PP30-shaped tax report; PND3; PND53 line and tag structure) | `PLATFORM` | `PLATFORM` | `PLATFORM` | `PLATFORM` | `COMPANY` | no | — | `account.report` records with `country_id = TH` (`l10n_th/data/account_tax_report_data.xml`). | **CORRECT.** Country-scoped platform reference; no tenant or company context required to exist. |
| 3 | Tax return type (`account.return.type` "Tax") | `PLATFORM` (definition) / `COMPANY` (obligation instance) | `COMPANY` | `COMPANY` | `PLATFORM` (definition) | — | no (definition) | — | One record bound to the Thai tax report (`l10n_th_reports/data/account_return_data.xml:4-8`). | **CONFLATED.** The filing *obligation* is `COMPANY`-scoped and, under `S-15`, place-of-business-scoped; only the *definition* is platform. No company- or branch-level obligation instance was selected. `P07-F-09` |

## 4. Matrix — Company Accounting Layer

| # | Object | OWN | EXEC | ACCESS | MUTATE | REF | FIN | FIN-OWNER | Observed placement | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 4 | `account.tax` instance with GL repartition | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | yes (via repartition) | the company owning the tax | Company-scoped in the base application. | **CORRECT.** |
| 5 | `account.tax.group` | `COMPANY` (instance) over a `PLATFORM` concept | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | indirect | — | Company instances named from the platform catalogue (`VAT 7%`, `WHT n%`). | **CORRECT as data**, but a `COMPANY`-mutable label is used by a report as a statutory selection predicate — see row 11 and `P07-F-01`. |
| 6 | `account.withholding.tax` | **split**: statutory half `PLATFORM`, GL binding `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | yes (write-off posting) | the company owning the payment | One model holding name / rate / form tags / `type` **and** `account_id` + `company_id` (`l10n_th_withholding_tax/models/account_withholding_tax.py:11-26`). | **SCOPE CONFLATION.** One record answers to two owners. Compounded by `company_id` being taken from the acting session rather than proven from the source tax (`l10n_th_withholding_tax/models/account.py:82-99`) — `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY` is not honoured. `P07-F-18` |
| 7 | `account.account.wt_account` flag | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | no (classifier) | — | `l10n_th_withholding_tax/models/account.py:12-16`. | **CORRECT.** |
| 8 | Tax accounting event (tax line / WHT write-off line on a posted move) | `COMPANY` | `COMPANY` | `COMPANY` | none once posted | `COMPANY` | yes | the company of the move | Base application. | **CORRECT.** |
| 9 | Tax point field (`account.move.tax_period`, `account.move.line.tax_period_date`) | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | determines the period of a financial effect | the company of the move | `smesplus_tax_period_date/models/tax_period.py:23`, `:36`. | **CORRECT scope, INERT function.** The line-level field is written only in `create` and read by nothing in the declared set; the header field is displayed but does not drive period selection. `P07-F-02` `P07-F-03` |
| 10 | Product withholding defaults (`product.template.wt_tax_id`, `supplier_wt_tax_id`) | `TENANT` (product master) referencing a `COMPANY`+`PLATFORM` object | `COMPANY` | `TENANT` | `TENANT` | `COMPANY` | no | — | `l10n_th_withholding_tax/models/product.py:9-10`. | **CROSS-SCOPE REFERENCE.** A tenant-scope master record points at row 6, whose company half is company-scoped. Because row 6 conflates two scopes, this reference cannot be validated. Dependent on resolving row 6. |

## 5. Matrix — Statutory Document and Reporting Layer

| # | Object | OWN | EXEC | ACCESS | MUTATE | REF | FIN | FIN-OWNER | Observed placement | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 11 | Sale / Purchase VAT statutory report (s.87 books) | `COMPANY`, and under `S-15` place-of-business within the company | `COMPANY` | `COMPANY` | n/a | — | reports a financial effect | the filing company | `smesplus_account_reports` handlers; `filter_multi_company` = `tax_units`. | **UNDER-SCOPED.** Executes at company or cross-company tax-unit level; the statutory unit is the place of business. Row inclusion additionally depends on a `COMPANY`-mutable label (row 5). `P07-F-01` `P07-F-09` |
| 12 | PND3 / PND53 export | `COMPANY` | `COMPANY` | `COMPANY` | n/a | — | reports a financial effect | the withholding company | `l10n_th_reports/models/tax_report_pnd.py`, overridden by `l10n_th_withholding_tax/models/tax_report_pnd.py`. | **CORRECT scope.** Defects are event-model defects, not scope defects — `P07-F-10` … `P07-F-14`. |
| 13 | Withholding tax certificate (s.50 bis) + lines | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` until issued | `TENANT` (the payee holds a copy) | evidences a financial effect | the withholding company | `withholding_tax_cert.py:148-155` (header), `:403-405` (line, related). Record rules present for both. | **OWNERSHIP CORRECT, ACCESS OVER-BROAD.** Unlink granted to the billing group; the creation wizard and the report model granted to every internal user. Access scope exceeds object scope. `P07-F-19` |
| 14 | Tax invoice as a document | `COMPANY` | `COMPANY` | `COMPANY` | none once issued | `TENANT` (customer copy) | evidences a financial effect | the issuing company | Print title substitution only (`l10n_th/views/report_invoice.xml:14-16`). | **NOT MODELLED AS AN OBJECT.** With no document object there is nothing to scope, number, or make immutable. `P07-F-26` |
| 15 | WHT report wizard / `withholding.tax.report` | `COMPANY` | `COMPANY` | granted to `base.group_user` | — | — | no | — | `l10n_th_withholding_tax_report/security/ir.model.access.csv`; company domain limited to `allowed_company_ids` (`wizard/withholding_tax_report_wizard.py:39-43`). | **MIXED.** Company selection is correctly bounded to allowed companies; model access is granted to all internal users. |

## 6. Matrix — Identity and Boundary Layer

| # | Object | OWN | EXEC | ACCESS | MUTATE | REF | FIN | FIN-OWNER | Observed placement | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| 16 | Counterparty tax identity (`res.partner.vat`, `res.partner.branch`, `partner_company_type_id`) | `TENANT` | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | `l10n_th_partner/models/res_partner.py:15`; `partner_company_type/models/res_partner.py:10`. | **CORRECT.** Customer/vendor master is a tenant-scope security and data boundary; companies within the tenant reference it. |
| 17 | Filing entity identity (`res.company.vat`, `res.company.branch`) | `COMPANY` | `COMPANY` | `COMPANY` | `COMPANY` | — | no | — | `l10n_th_partner/models/res_company.py:9`. | **CORRECT but UNUSED.** No statutory report in the declared set reads `res.company.branch`; the reports print the company's *partner* branch string derived from `company_registry`. `P07-F-06` |
| 18 | Derived branch label (`res.partner.l10n_th_branch_name` from `company_registry`) | `TENANT` (derived from row 16) | — | `TENANT` | derived | `COMPANY` | no | — | `l10n_th/models/res_partner.py:9-18`. | **SCOPE COLLISION.** Three representations of "Thai branch" exist across two scopes and are used interchangeably by the statutory reports. `P07-F-06` |
| 19 | Tax unit grouping (`filter_multi_company` = `tax_units`) | `TENANT` grouping of `COMPANY` objects | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | aggregates financial effects across companies | the unit's `main_company_id`, described in the model as the one actually reporting and paying the taxes | The Thai VAT reports opt into the mechanism (`smesplus_account_reports/data/generic_tax_report.xml:5`, `:75`). The mechanism is `account.tax.unit` (`account_reports/models/account_tax.py:9`), carrying its own `vat`, a `country_id`, member `company_ids` and a `main_company_id`. | **NO TENANT BOUNDARY IN THE MODEL.** Its constraints are country, shared main currency, at most one unit per company per country, and a two-company minimum (`:118-142`) — none of them a tenant constraint. Its fiscal-position synchronisation and its `unlink` both operate over `self.env['res.company'].search([])`, an unbounded company search (`:106-117`). Containment, if any, comes entirely from ambient record rules on `res.company`, not from this model. `P07-F-39`; `P07-U-14` narrowed. |
| 20 | Partner enrichment from the Revenue Department VAT service | `TENANT` (writes tenant master data) via a `PLATFORM` external service | `TENANT` | `TENANT` | `TENANT` | `COMPANY` | no | — | `bm_thai_rd_vat_company_search` (proprietary, `OPL-1`). | **SCOPE CORRECT, EGRESS UNASSESSED.** An external call carrying taxpayer identifiers; the tenant boundary of that egress was not examined in this session. `P07-U-15` |

## 7. Findings Produced by the Scope Analysis

| ID | Statement | Class |
|---|---|---|
| `P07-F-18` (revised) | `account.withholding.tax` conflates a `PLATFORM` statutory reference with a `COMPANY` financial binding in one record, and its company ownership is taken from the acting session rather than proven from the source tax. | scope conflation + unproven ownership |
| `P07-F-30` (new) | The Thai statutory catalogue, a `PLATFORM` reference, is instantiated per company and is independently mutable there; one of those mutable labels is used as a statutory report predicate. | scope over-instantiation |
| `P07-F-06` (re-scoped) | "Thai branch" exists in three representations spanning `TENANT` and `COMPANY` scope and is used interchangeably by statutory reports; the `COMPANY`-scope filing attribute is read by none of them. | scope collision |
| `P07-F-39` (new) | The cross-company tax-unit mechanism the Thai VAT reports opt into carries **no tenant constraint of its own**, and two of its operations walk an unbounded `res.company` search. | scope boundary absent from the mechanism |
| `P07-U-14` (narrowed) | Whether ambient record rules on `res.company` contain that grouping within one tenant was not established. The question is no longer whether P07 defines a tenant construct — it defines none and needs none of its own — but what contains an unbounded company search. | `HOLD — SCOPE EVIDENCE REQUIRED` |
| `P07-U-15` (new) | Egress of taxpayer identifiers to an external Revenue Department service was not scope-assessed. | `NOT YET SEARCHED` |

## 8. What This Matrix Does Not Claim

- It does **not** claim that tenant or company context is required for platform reference
  data. Rows 1–3 explicitly require neither.
- It does **not** convert the absence of a tenant construct in the P07 population into a
  claim that SMEsPlus has no tenant construct. The claim is bounded to the P07 module
  population and the declared patterns — negative-claim class `B`, recorded as
  `P07-N-09` in `11_P07_CONTRADICTION_REGISTER.md` §5.
- It does **not** claim that the tax-unit mechanism requires Thai fiscal-position master
  data. That inference was drawn and then **discarded**: the mechanism creates its own
  fiscal positions and the code states they carry no taxes
  (`account_reports/models/account_tax.py:79-84`, docstring). `P07-F-38` and `P07-F-39`
  are independent findings, not one finding counted twice.
- It does **not** adjudicate scope for objects owned by P01, P02, P05, P06, P08 or P10.
  Those are `PEER DEPENDENCY OPEN` in `12_P07_DEPENDENCY_REGISTER.md` §4.
