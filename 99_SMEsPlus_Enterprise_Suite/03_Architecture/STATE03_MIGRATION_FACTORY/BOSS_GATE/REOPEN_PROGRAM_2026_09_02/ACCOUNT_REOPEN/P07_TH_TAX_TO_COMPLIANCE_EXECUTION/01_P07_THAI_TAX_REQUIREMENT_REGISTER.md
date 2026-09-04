# P07 — THAI TAX REQUIREMENT REGISTER

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Scope basis: `13_P07_SOURCE_LINK_REGISTER.md`
Legal basis: `09_P07_STATUTORY_SOURCE_REGISTER.md`
Date: `2026-09-04`

## 1. How to Read This Register

Each requirement is stated **from the statute**, then assessed **against the declared
source set**. The two are never merged: the `Requirement` column may cite only `LAW`,
`REGULATION` or `RD-REQ` band sources; the `Observed in declared source set` column may
cite only reference-ERP evidence. No requirement in this register was inferred from
reference ERP configuration.

Status vocabulary (no `PASS` wording is used anywhere in this package):

| Status | Meaning |
|---|---|
| `MET-IN-SOURCE` | The declared source set contains a mechanism that satisfies the requirement, on source reading |
| `PARTIAL` | A mechanism exists but does not cover the requirement as stated |
| `DIVERGENT` | A mechanism exists and produces a result the requirement does not permit |
| `NOT FOUND IN SEARCHED SCOPE` | No mechanism selected by the declared patterns (negative-claim class `B`) |
| `HOLD` | The requirement itself is not yet legally established in this session |

## 2. VAT — Registration, Rate and Base

| ID | Requirement | Source | Observed in declared source set | Status | Finding |
|---|---|---|---|---|---|
| `R-V-01` | VAT is charged at a rate set by s.80 (10%), reducible by Royal Decree; the reduced rate currently in force is 7% and each reduction has a fixed expiry. | `S-06` `S-35` `P-09` | Localisation ships tax groups literally named `VAT 7%`, `WHT 1%`, `WHT 2%`, `WHT 3%`, `WHT 5%` (`l10n_th/data/template/account.tax.group-th.csv`). The SMEsPlus Sale/Purchase VAT report admits a row **only if** the raw value of the tax group's name equals the literal dict `{'en_US': 'VAT 7%'}` (`smesplus_account_reports/models/account_generic_tax_report.py:88`, comparing `atg.name` selected raw at `:45`). `account.tax.group.name` is `translate=True` (`account/models/account_tax.py:32`), so the stored value is a translation mapping, and the Thai template ships a `name@th_TH` value for that group. **On a deployment with Thai installed as a language the equality is false for every row and both statutory books return no data.** | `DIVERGENT` | `P07-F-01` |
| `R-V-02` | VAT is charged to the purchaser at the time the tax liability takes place. | `S-10` | Tax is computed on the accounting document; no separate charge event exists. | `MET-IN-SOURCE` | — |
| `R-V-03` | The tax base is the total value received or receivable, excluding the output tax. | `S-05` | Base amounts are taken from the repartition engine (`tdr.base_amount`) or from `price_subtotal`. | `MET-IN-SOURCE` | — |
| `R-V-04` | Zero-rated supplies (s.80/1) are a distinct class from exempt supplies (s.81). | `S-07` | The localisation ships `Output VAT 0%` and `Output VAT Exempted` as separate taxes, mapped to distinct report lines `2. Less sales subject to 0% tax rate` and `3. Less exempted sales` (`l10n_th/data/template/account.tax-th.csv`). The SMEsPlus "Zero" reports do **not** distinguish them: both are selected by `account_move_line__move_id.amount_tax = 0` (`account_generic_tax_report.py:279-280`, `:474-476`). | `PARTIAL` | `P07-F-05` |

| `R-V-25` | **A supply does not require consideration.** Donation, scrapping, application of goods to a non-business purpose, stock shortfall and goods remaining on cessation are supplies; a fixed asset is "goods". | `S-36` `S-37` `P-11` | No deemed-supply mechanism, no output-tax event and no tax document for any no-consideration transfer was found. The disposal path produces no tax invoice. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-58` |
| `R-V-26` | **Hire purchase / instalment sale**: liability arises as each instalment falls due, and a tax invoice is required on every instalment due date. | `S-38` `P-12` | No instalment-driven tax point and no per-instalment document issuance was found. Compounds with `R-V-10` and `R-V-11`: there is no tax-invoice object to issue per instalment even if the tax point were correct. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-59` |

## 3. VAT — Tax Point and Period

| ID | Requirement | Source | Observed in declared source set | Status | Finding |
|---|---|---|---|---|---|
| `R-V-05` | Goods: tax point is delivery, or earlier of transfer of ownership / payment / tax-invoice issuance. | `S-01` | No tax-point determination logic selected by the declared patterns. The document's accounting date is used throughout. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-02` `P07-N-06` |
| `R-V-06` | Services: tax point is receipt of payment, or earlier of tax-invoice issuance / use of the service. | `S-02` | Same as `R-V-05`. There is no service-specific tax point. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-02` |
| `R-V-07` | A supply belongs to the **tax month of its tax point** for both the return (s.83) and the net computation (s.82/3). | `S-09` `S-15` `P-02` | A tax-point-bearing field exists (`account.move.tax_period`, `smesplus_tax_period_date/models/tax_period.py:23`) and is **displayed** on the Sale/Purchase VAT report (`account_generic_tax_report.py:38`, `:92-108`), but the report's period selection remains `strict_range` over the **accounting date** (`:26`). The predecessor implementation substituted `COALESCE(account_move_line__move_id.tax_period, account_move_line.date)` into the period predicate (`account_generic_tax_report.py_bkp:30`) and that substitution is absent from the current file. | `DIVERGENT` | `P07-F-02` |
| `R-V-08` | Importation: tax point is payment of import duty / entry at Customs. | `S-03` | Not selected by the declared patterns. | `NOT FOUND IN SEARCHED SCOPE` | `P07-N-07` |
| `R-V-09` | Special tax points set by Ministerial Regulation (incorporeal goods, vending machines, credit-card sales, certain contracts). | `S-04` | Not selected by the declared patterns. | `NOT FOUND IN SEARCHED SCOPE` | `P07-N-07` |

## 4. VAT — Documents

| ID | Requirement | Source | Observed in declared source set | Status | Finding |
|---|---|---|---|---|---|
| `R-V-10` | A tax invoice and its copy must be issued **immediately at the tax point**, for every supply. | `S-19` | The Thai print layout replaces the invoice title with the literal `Tax Invoice` (`l10n_th/views/report_invoice.xml:14-16`) and is selected when the company's fiscal country is TH (`l10n_th/models/account_move.py:7-11`). Issuance is therefore a print action on the accounting document; no issuance event, no issuance timestamp, no copy record. | `PARTIAL` | `P07-F-26` |
| `R-V-11` | The tax invoice must carry its **own serial number** (and book number, if any). | `S-20` | The number printed is the accounting document name. No tax-invoice sequence, and no book number, selected by the declared patterns. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-26` `P07-N-01` |
| `R-V-12` | The word "tax invoice" must appear in a prominent place; VAT must be shown clearly separated; the date of issuance must appear. | `S-20` | Title literal present; VAT separation and date are inherited from the base invoice layout. | `MET-IN-SOURCE` | — |
| `R-V-13` | Issuer and purchaser particulars including taxpayer identification number **and branch**. | `S-20` `P-10` | Purchaser tax ID and a branch string are printed (`l10n_th/views/report_invoice.xml:4-13`). The branch string is derived from `res.partner.company_registry` via `l10n_th_branch_name` (`l10n_th/models/res_partner.py:9-18`). A **different** Thai branch field, `res.partner.branch`, exists in the same source set (`l10n_th_partner/models/res_partner.py:15`), as does `res.company.branch` (`l10n_th_partner/models/res_company.py:9`). | `DIVERGENT` | `P07-F-06` |
| `R-V-14` | Abbreviated tax invoice (retail) is a distinct document class with VAT-inclusive pricing. | `S-22` | Not selected by the declared patterns as a document class. The vendor tax report anticipates partnerless supplies by substituting the caption `Selling goods or providing services` (`l10n_th_reports/models/tax_report_vat.py:153-154`), which is the abbreviated-invoice case; the SMEsPlus reports remove that path by inner-joining the partner at all three of their SQL sites (`account_generic_tax_report.py:55`, `:256`, `:427`), which serve all four handlers. | `DIVERGENT` | `P07-F-04` |
| `R-V-15` | Debit note: issued in the same tax month as the causing event (or the following month if necessary), referencing the **original tax invoice**. | `S-23` | No debit-note document class, and no original-tax-invoice reference field, selected by the declared patterns in the Thai tax modules. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-07` |
| `R-V-16` | Credit note: same timing rule, referencing the original tax invoice and stating the VAT credited. | `S-24` | Credit notes exist as reversal documents in the base application, but no Thai tax report in the declared set carries an original-tax-invoice reference column, and the SMEsPlus VAT reports net refunds by sign (`account_generic_tax_report.py:87`). | `PARTIAL` | `P07-F-07` |
| `R-V-17` | Records must be retained for at least 5 years. | `S-26` | Retention is a platform/operations concern; not selected by the declared patterns as a tax-specific control. | `NOT FOUND IN SEARCHED SCOPE` | — |

## 5. VAT — Statutory Reports and Return

| ID | Requirement | Source | Observed in declared source set | Status | Finding |
|---|---|---|---|---|---|
| `R-V-18` | An **Output Tax Report** and an **Input Tax Report** are mandatory books of record. | `S-25` `P-04` | Two implementations coexist for the same statutory books: the vendor `Sales Tax Report (xlsx)` / `Purchase Tax Report (xlsx)` (`l10n_th_reports/models/tax_report_vat.py:36-56`), overridden by `l10n_th_reports_ext/models/tax_report_vat.py:11`; and the SMEsPlus `Sale Vat Report` / `Purchase Vat Report` plus zero-rate variants (`smesplus_account_reports/data/generic_tax_report.xml`). | `PARTIAL` | `P07-C-01` |
| `R-V-19` | Entries must be made in those reports within **3 working days** of acquisition or disposition. | `S-25` | The reports are query-time renderings over the ledger; no entry-timeliness concept selected. | `NOT FOUND IN SEARCHED SCOPE` | — |
| `R-V-20` | The return is filed **per tax month** by the **15th of the following month**. | `S-15` `S-34` | The base set provides a filing framework with configurable periodicity, deadline delay and workflow states (`account_reports/models/account_return.py:59`, `:624`, `:2660`), provisioned by 118 localisation modules. Thailand binds **one** generically-named return type to the Thai tax report and configures none of those attributes (`l10n_th_reports/data/account_return_data.xml:4-8`). The 15th-of-the-following-month deadline is therefore not represented. | `PARTIAL` | `P07-F-37` |
| `R-V-21` | Filing and payment are made **separately by each place of business**, unless the Director-General approves consolidation. | `S-15` `S-34` `P-10` | The SMEsPlus tax reports set `filter_multi_company` to `tax_units` (`smesplus_account_reports/data/generic_tax_report.xml:5`), which is a company-grouping filter, not a place-of-business filter. Branch appears only as a **display column** sourced inconsistently (`R-V-13`). No branch-level filing unit, no branch-level return, and no branch-level segregation of the report population were selected. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-09` `P07-N-05` |
| `R-V-22` | Excess input tax may be carried forward or refunded. | `S-18` | **Implemented.** Line `10_EXCESS_CARRIED_FORWARD` combines an `external` engine expression (`formula: most_recent`, `date_scope: previous_return_period`) with a `tax_tags` expression, and lines 11 and 12 consume it (`l10n_th/data/account_tax_report_data.xml:144-196`). `U-12` is **CLOSED**. | `MET-IN-SOURCE`, conditional on `R-V-24` | — |
| `R-V-24` | The VAT taxable period **is the calendar month** (`S-15`, `S-34`). | `S-15` `S-34` | The Thai return type sets no periodicity, so the effective period falls back to a **company-level, user-editable setting** offering seven values, whose platform default is `monthly` (`account_reports/models/account_return.py:535`; `account_reports/models/res_company.py:20-25`). The statutory monthly period is therefore correct only by coincidence of a platform default, and is silently changeable per company. The same setting governs the `previous_return_period` scope that `R-V-22`'s carry-forward resolves against. | `DIVERGENT` | `P07-F-40` |
| `R-V-23` | Self-assessed VAT on payments to foreign service providers and unregistered temporary operators. | `S-17` | Not selected by the declared patterns in the Thai modules. | `NOT FOUND IN SEARCHED SCOPE` | `P07-N-08` |

## 6. Withholding Tax

| ID | Requirement | Source | Observed in declared source set | Status | Finding |
|---|---|---|---|---|---|
| `R-W-01` | Tax is withheld **at every time of payment**. | `S-30` `P-07` | Withholding is applied through the payment register as a payment-difference write-off (`l10n_th_withholding_tax/wizard/account_payment_register.py:16-26`, `:38-72`). The **event location is correct**. | `MET-IN-SOURCE` | — |
| `R-W-02` | The amount withheld is the amount that must be remitted and reported. | `S-32` `S-33` | Both PND exports **recompute** the amount as `ABS(rate × base / 100)` in SQL rather than reading the posted amount (`l10n_th_reports/models/tax_report_pnd.py:46`; `l10n_th_withholding_tax/models/tax_report_pnd.py:37`, `:72`). | `DIVERGENT` | `P07-F-10` |
| `R-W-03` | Reporting is **per payee per payment**. | `S-33` `P-08` | The override's second UNION branch reports the **invoice** line, gated on `account_move_line__move_id.payment_state != 'not_paid'` and `account_move_line.payment_id is null`, dated by the **invoice** accounting date (`l10n_th_withholding_tax/models/tax_report_pnd.py:55-92`). The payment write-off line — the actual withholding — is excluded from both branches. | `DIVERGENT` | `P07-F-11` |
| `R-W-04` | A partial payment withholds on the amount paid. | `S-30` | The wizard computes the WHT of the **whole** selected invoice lines, less previously posted WHT (`account_payment_register.py:50-57`). The PND branch then reports the whole invoice once `payment_state != 'not_paid'`, a set that includes `partial` and `in_payment` (base selection at `account/models/account_move.py:48-56`). | `DIVERGENT` | `P07-F-12` |
| `R-W-05` | Remittance is due **within 7 days**; PND returns are filed for the month of payment. | `S-32` | No remittance-deadline object, and no PND filing period object, selected. The period comes from the report date filter. | `NOT FOUND IN SEARCHED SCOPE` | `P07-F-11` |
| `R-W-06` | A **certificate in duplicate** must be issued **immediately every time tax is withheld** (non-employment income). | `S-31` | A certificate model exists with a creation wizard and print form (`l10n_th_withholding_tax_cert`). Issuance is user-initiated, not event-driven; no duplicate-copy record; number and date are computed (`withholding_tax_cert.py:77-89`, `:238`). | `PARTIAL` | `U-13` |
| `R-W-07` | The certificate and the PND schedule must state the **income type** under s.40 and the **condition of withholding**. | `S-31` `S-33` | Income type on the PND export is derived from the tax **rate** by a four-value `CASE` (`-1` Transportation, `-2` Advertising, `-3` Service, `-5` Rental; every other rate yields an empty string) in both handlers. Condition is the hard-coded literal `'1'` in both handlers. The certificate model itself carries a full 16-value s.40 income-type selection (`withholding_tax_cert.py:16-64`) which the PND export does not use. | `DIVERGENT` | `P07-F-13` `P07-F-14` |
| `R-W-08` | PND3 applies to payments to natural persons; PND53 to juristic persons. | `S-30` `S-33`; rejected contrary source in `09 §5` | Form selection is driven by `partner_id.is_company` combined with a case-insensitive **substring** test (`'pnd3'` / `'pnd53'`) against the **name of the first tag of the first repartition line** of each candidate tax (`l10n_th_withholding_tax/models/account_move.py:66-83`). Tag name is a translatable label; the tag collection is unordered. | `DIVERGENT` | `P07-F-15` |
| `R-W-09` | Every WHT form the entity is liable for must be producible. | `S-33` | Handlers exist for PND3 and PND53 only. The certificate model offers `pnd1`, `pnd3`, `pnd3a`, `pnd53`; the WHT report wizard narrows the selection to `pnd3` and `pnd53` only (`l10n_th_withholding_tax_report/wizard/withholding_tax_report_wizard.py:22`). PND 2 is not provisioned at any layer; PND 54 **is** provisioned in the chart of accounts (`213303`, with the remittance form named in its description) and at no other layer. Four-layer provisioning matrix at `03 §4.1`; negative-claim classes at `P07-N-11`. | `PARTIAL` | `P07-F-21` `W-K-07` |
| `R-W-10` | One withholding is one tax fact. | Constitution: `ONE TAX FACT -> ONE CANONICAL TAX EVENT -> ONE ACCOUNTING EFFECT` | Two withholding frameworks are simultaneously installable in the declared set: the vendor `l10n_account_withholding_tax` ("Withholding Tax on Payment") and the third-party `l10n_th_withholding_tax`. Both attach to the payment register. No guard preventing both from applying to one economic event was selected. | `DIVERGENT` | `P07-F-16` |

## 7. Scope Ownership (Platform / Tenant / Company)

Revised under `SMEPLUS-26-09-04-ACC-REV2-CORR1` (Scope-Aware Constitution Correction).
The superseded wording of this section asserted a blanket company-ownership requirement
for tax master data. That is over-constrained. The canonical rule is **scope-aware
everywhere**: scope is determined first, then the context requirement follows. Full
per-object analysis is in `20_P07_SCOPE_OWNERSHIP_MATRIX.md`; the revalidation record is
in `15_P07_REVISION_LOG.md` §3.

| ID | Requirement | Source | Observed in declared source set | Status | Finding |
|---|---|---|---|---|---|
| `R-B-01` | An object that mixes a `PLATFORM`-scope statutory reference with a `COMPANY`-scope financial binding cannot be correctly scoped, because one record would have to answer to two owners. | `SMEPLUS-26-09-04-ACC-REV2-CORR1` §3-§4; `S-28` `S-30` | `account.withholding.tax` carries, in one record, the **statutory reference** (name, rate, income category, form tags) and the **company financial binding** (`account_id`, a GL account restricted to accounts flagged as withholding accounts) — `l10n_th_withholding_tax/models/account_withholding_tax.py:11-26`. The statutory half is `PLATFORM` by semantics (the Thai rate and form catalogue is national, identical for every tenant); the GL half is `COMPANY`. | `DIVERGENT` | `P07-F-18` |
| `R-B-02` | Where an object is `COMPANY`-scoped, the owning company must be **derived from the object's own lineage**, not from the acting session. | `SMEPLUS-26-09-04-ACC-REV2-CORR1` §2 (`REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`) | `company_id` is required with `default=lambda self: self.env.company`, and the synchroniser that creates these records from `account.tax` does **not** pass `company_id` (`l10n_th_withholding_tax/models/account.py:82-99`). Ownership is therefore taken from the acting user's active company rather than proven from the source tax. The record rule that follows (`security/security.xml`) filters on that unproven value. | `DIVERGENT` | `P07-F-18` |
| `R-B-03` | A statutory document carrying a financial effect is `COMPANY`-scoped, and must not be deletable by an ordinary operational role. | `S-26`; `EC-04`; correction §4 q.6-7 | The s.50 bis certificate is correctly `COMPANY`-scoped (`company_id` required, record rule present, line-level company related from the header — `withholding_tax_cert.py:148-155`, `:403-405`). The **access** control is not consistent with that scope: full create/write/**unlink** is granted to the billing group, and the certificate-creation wizard and the WHT report model are granted to `base.group_user` (`l10n_th_withholding_tax_cert/security/ir.model.access.csv`, `l10n_th_withholding_tax_report/security/ir.model.access.csv`). Ownership scope is correct; **access scope** is wider than the object's scope. | `DIVERGENT` | `P07-F-19` |
| `R-B-04` | A filing unit (place of business) is a `COMPANY`-scope legal boundary, distinct from a counterparty branch attribute, which is `TENANT`-scope master data. | `S-15` `P-10`; correction §3 (`TENANT = security/customer boundary`, `COMPANY = legal/accounting boundary`) | The declared set carries `res.company.branch` (`l10n_th_partner/models/res_company.py:9`) — a `COMPANY`-scope filing attribute — and `res.partner.branch` (`:15`) — a `TENANT`-scope counterparty attribute — and a third derived string `l10n_th_branch_name` computed from `res.partner.company_registry` (`l10n_th/models/res_partner.py:9-18`). The statutory reports print the counterparty attribute and the derived string; **no report reads the company-scope filing attribute**. The two scopes are used interchangeably. | `DIVERGENT` | `P07-F-06` `P07-F-09` |
| `R-B-05` | A tax-reporting grouping that spans companies must be proven not to span tenants. | Correction §3 (`UNRELATED INDEPENDENT COMPANIES = SEPARATE TENANTS BY DEFAULT`) | The SMEsPlus VAT reports declare `filter_multi_company` = `tax_units` (`smesplus_account_reports/data/generic_tax_report.xml:5`, `:75`), a cross-company grouping used to produce one tax figure from several companies. The mechanism behind that filter is `account.tax.unit` (`account_reports/models/account_tax.py:9`), whose constraints are country, shared main currency, one unit per company per country and a two-company minimum (`:118-142`) — **no tenant constraint** — and whose fiscal-position sync and `unlink` walk `self.env['res.company'].search([])` (`:106-117`). Containment depends entirely on ambient record rules, which were not established here. | `DIVERGENT`, with `HOLD — SCOPE EVIDENCE REQUIRED` on containment | `P07-F-39` `P07-U-14` |
| `R-B-06` | The Thai statutory catalogue (rates, form types, income categories, report structure) is `PLATFORM` reference data and does not require tenant or company context to exist. | Correction §2, §5 (`Platform Tax Reference -> PLATFORM candidate`) | The catalogue is shipped as company-instantiated template data (`l10n_th/data/template/*.csv` applied per company on chart installation) and as report definition records. Instantiating the national catalogue **per company** is a defensible implementation of a `PLATFORM` reference, but it makes every company's copy independently editable, so the platform reference has no single source of truth. This is recorded as a scope-design observation, not a defect, because the correction does not require platform data to be physically singular. | `PARTIAL` | `P07-F-30` |

## 8. Requirement Coverage Summary

| Status | Count |
|---|---|
| `MET-IN-SOURCE` | 4 |
| `PARTIAL` | 10 |
| `DIVERGENT` | 13 |
| `NOT FOUND IN SEARCHED SCOPE` | 9 |
| `HOLD` | 1 (`R-B-05`, scope evidence); 6 legal questions held in `09 §4` |
| **Total requirements registered** | **37** |

No requirement is recorded as satisfied on the strength of a reference-ERP default.

Section 7 was revised in place under `SMEPLUS-26-09-04-ACC-REV2-CORR1`; the superseded
wording and the reason it was over-constrained are preserved in `15_P07_REVISION_LOG.md` §3.
