# P07 — DEPENDENCY REGISTER

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Technical Module Dependencies

| ID | Dependency | Kind | Status | Evidence |
|---|---|---|---|---|
| `P07-D-01` | `l10n_th_withholding_tax_multi` → `account_payment_multi_deduction` | declared, **unsatisfiable in the declared source set** | **BROKEN** | The dependency is declared at `l10n_th_withholding_tax_multi/__manifest__.py:12`; the module is absent from all three roots of the declared PATH SET. It exists elsewhere on the volume (v12, v14, v18 project sets, and a directory named `no_use` in one v19 build), so this is a set-composition problem, not a missing artefact. Multiple-withholding-taxes-per-payment is therefore not installable from the declared set. |
| `P07-D-02` | `l10n_th_reports_ext` → `l10n_th_partner` | **undeclared** | **BROKEN** | The module declares `depends: ['l10n_th_reports']` only (`__manifest__.py:13-15`) but reads `partner.branch`, defined at `l10n_th_partner/models/res_partner.py:15`. |
| `P07-D-03` | `l10n_th_reports_ext` → `partner_company_type` | **undeclared** | **BROKEN** | Same manifest; reads `partner.partner_company_type_id`, defined at `partner_company_type/models/res_partner.py:10`. |
| `P07-D-04` | `l10n_th_withholding_tax` → `l10n_th_reports` | declared | satisfied, but see `P07-D-07` | `__manifest__.py:11` |
| `P07-D-05` | `l10n_th_reports_ext` → `l10n_th` (transitively, for `l10n_th_branch_name`) | transitive via `l10n_th_reports` | satisfied | `l10n_th/models/res_partner.py:9` |
| `P07-D-06` | `smesplus_account_reports` → `smesplus_tax_period_date`, `account_reports` | declared | satisfied | `__manifest__.py:13-17` |
| `P07-D-07` | Thai statutory reporting → Enterprise-licensed components | **licence dependency** | **OPEN — routed, not adjudicated** | `l10n_th_reports` is licensed `OEEL-1` and defines the Thai tax report and PND handlers; `account_reports` is Enterprise. Two SMEsPlus modules declaring `LGPL-3` (`l10n_th_reports_ext`, `smesplus_account_reports`) inherit from them. Licensing competence sits outside this session. |
| `P07-D-08` | `bm_thai_rd_vat_company_search` → external Revenue Department VAT service | **external service dependency**, proprietary module (`OPL-1`, priced) | **OPEN** | `__manifest__.py`. Availability, rate limits, data-protection posture and tenant boundary of the egress were not assessed (`P07-U-15`). |
| `P07-D-09` | WHT certificate print → `l10n_th_amount_to_text` | declared | satisfied | `l10n_th_withholding_tax_cert_form/__manifest__.py:11` |
| `P07-D-10` | WHT report → `report_xlsx_helper`, `date_range`, `l10n_th_partner` | declared | satisfied | `l10n_th_withholding_tax_report/__manifest__.py:12-18` |
| `P07-D-26` | `l10n_th_withholding_tax` → `l10n_th_partner`, `partner_company_type` | **undeclared** | **BROKEN, and worse than `P07-D-02`** | The manifest declares `["account", "l10n_th_reports"]` (`__manifest__.py:9`), yet the PND override runs **raw SQL** against `partner.branch` (`models/tax_report_pnd.py:33`, `:68`) and `res_partner_company_type` (`:48`, `:50`, `:83`, `:85`). Raw SQL fails with a database error rather than an attribute error, and this is the module that **produces the PND3 and PND53 statutory returns**. Found by applying the `P07-D-02` check to the whole population instead of one module. `P07-F-54` |
| `P07-D-27` | Withholding path → its own test suites | declared by the modules | **NON-EXECUTABLE** | Both suites import symbols absent from this generation; one asserts an error from commented-out code. No regression coverage exists for the withholding path. `P07-F-55` |
| `P07-D-28` | `l10n_th_withholding_tax` (AGPL-3) → `l10n_th_reports` (`OEEL-1`) | declared | **LICENCE INVERSION — OPEN, routed** | A copyleft module hard-depending on an Enterprise-licensed module. Related to `P07-D-07`; competence sits outside this session. `P07-F-56` |
| `P07-D-29` | Thai amount-in-words on the s.50 bis certificate | two byte-identical modules in the same addons path | **NON-DETERMINISTIC** | `convert_amount_text_to_thai` and `l10n_th_amount_to_text` are byte-identical apart from one description asset, carry the same version string, and both override the same method. `P07-D-09` records this dependency as satisfied — it is satisfied twice. `P07-F-48` |

## 2. Data and Configuration Dependencies

These are dependencies on **data**, not on modules, and they are the ones that make
statutory output fragile.

| ID | Dependent behaviour | Depends on | Failure mode if the dependency is not held |
|---|---|---|---|
| `P07-D-11` | Row inclusion in the SMEsPlus Sale/Purchase VAT reports | the tax group being named exactly `VAT 7%` in `en_US` | the statutory report silently returns no rows |
| `P07-D-12` | PND3 / PND53 candidate selection | the first tag of the first repartition line containing the substring `pnd3` / `pnd53`, in a translatable label | no withholding taxes are offered to the user |
| `P07-D-13` | PND income-type column | the tax rate being exactly −1, −2, −3 or −5 | the income type is emitted empty |
| `P07-D-14` | PND53 title column | partner company-type master data being populated | the title is emitted empty |
| `P07-D-15` | Branch column | `company_registry` in two reports, `branch` in two others | two statutory reports disagree about the same taxpayer's branch |
| `P07-D-16` | Sales-side WHT reporting | tags on `tax_wht_income_*`, which are empty as shipped | the fact is reported nowhere (`W-K-08`) |
| `P07-D-17` | Report period membership | the accounting date, not the tax point | facts fall in the wrong statutory month (`04 §5`) |
| `P07-D-25` | The VAT return period, and the `previous_return_period` scope of the excess-VAT carry-forward | a company-level periodicity setting with seven values, defaulting to monthly, asserted nowhere by the Thai localisation | a company set to any non-monthly value silently files on a non-statutory period and carries forward against the wrong prior period (`P07-F-40`) |

`P07-D-11` deserves separate emphasis: the VAT rate is a **Royal Decree reduction of a 10%
statutory rate, renewed annually with a fixed expiry** (`S-06`, `S-35`, `P-09`). The
current reduction runs to 30 September 2026 and a further extension to 30 September 2027
was approved by Cabinet on 27 July 2026 and confirmed by a Revenue Department notice on
2 August 2026 — so the rate is **not** about to lapse. The structural point stands
regardless of the current expiry date: a statutory report whose row predicate is the
literal string `VAT 7%` is coupled to a temporary instrument, and any future reversion to
the s.80 rate, or any renaming of the tax group, empties the report with no error.

## 3. Statutory Dependencies (HOLD)

Carried from `09 §4`. None is used to support a conclusion in this package.

| ID | Held question | Blocks |
|---|---|---|
| `U-03` | Instrument permitting a deferred input-tax claim | The legal grounding of the purchase-side tax period design (`TPR-05`) |
| `U-04` | Royal Decree number for the current 7% rate | Precise dating of `P07-D-11` |
| `U-07` | Prescribed format of the s.87 reports | Whether the reports are format-compliant, not merely arithmetically complete |
| `U-08` | Substitute tax invoice requirements | Whether `D-05` is a gap or a non-requirement |
| `U-09` | Statutory condition-of-withholding code set | Sizing of `W-K-02` |
| `U-10` | Authoritative s.40 income category → PND form → rate mapping | Specification of the replacement for `W-K-01` |

## 4. Peer Process Dependencies — `PEER DEPENDENCY OPEN`

Recorded under the Scope-Aware Correction §7. None stopped this session.

| ID | Peer | Open item | P07 impact if unresolved |
|---|---|---|---|
| `P07-D-18` | P01 | Tax point and typed vendor legal personality on the bill line | PND form determination stays heuristic |
| `P07-D-19` | P02 | Tax point, delivery event, tax-invoice document identity | Goods tax point remains undeterminable |
| `P07-D-20` | P05 | Input-tax deductibility classification on expense lines | `S-11` cannot be evidenced |
| `P07-D-21` | P06 | Payment date as the withholding anchor, allocation, reversal linkage, FX policy | `W-C-01`, `W-C-02`, `W-M-02` cannot be closed by P07 alone |
| `P07-D-22` | P08 | Tax settlement mechanism; acceptance that a tax fact and its accounting entry may fall in different periods; tax-period state | `O-03` ownership cannot be restored to P07 |
| `P07-D-23` | P10 | Rule that deferral affects recognition timing only, never tax-period membership | Risk of a second, competing period attribute |
| `P07-D-24` | P11 | What contains the unbounded `res.company` search inside the cross-company tax-unit mechanism, given that the mechanism carries no tenant constraint (`P07-F-39`) | `P07-U-14` stays `HOLD — SCOPE EVIDENCE REQUIRED`; the Thai VAT reports opt into this mechanism by configuration |

## 5. Provisioning Gaps Against a Measured Peer Baseline

Two P07 capabilities are unprovisioned for Thailand on frameworks that the declared source
set already contains and that most peer localisations use. Both were found by enumerating
the peer population rather than by inspecting Thailand alone.

| ID | Capability | Framework present | Thai provisioning | Peer baseline in `02 OTHER` |
|---|---|---|---|---|
| `P07-F-37` | Return filing: instance, state, statutory deadline, compliance check | `account.return`, `account.return.type`, `account.return.check` with `deadline_periodicity`, `deadline_days_delay`, `states_workflow`, `payment_partner_bank_id` | **one** return type named `Tax`, no deadline, no workflow; PND3/PND53/PND54 not registered | **118** modules ship `account.return.type` data |
| `P07-F-38` | Fiscal position / tax mapping — named explicitly in the session directive | `account.fiscal.position` template loading, and a `fiscal_position_ids` column in the tax template format | **none.** `l10n_th/data/template/` contains four files and no fiscal position template; every `fiscal_position_ids` cell in `account.tax-th.csv` is empty. Further, `filter_fiscal_position` is **commented out on all four** SMEsPlus statutory VAT reports (`smesplus_account_reports/data/generic_tax_report.xml:6`, `:76`, `:139`, `:212`) — tax mapping was not merely unprovisioned, it was explicitly disabled on the s.87 registers | **94** of the **126** directories that ship a chart of accounts — see the correction below |

`P07-F-38` means there is no Thai tax mapping for export customers, non-VAT-registered
vendors, exempt or promoted entities, or overseas payees — the last being exactly the
PND 54 case that has a general-ledger account and nothing else (`03 §4.1`).

**Denominator correction.** The first issue of this finding reported "113 of 138". Both
numbers were defective and the defect was found by independent challenge:

| | First issue | Corrected |
|---|---|---|
| Numerator UNIT | **files** matching `account.fiscal.position-*.csv` (113) | **directories** shipping at least one (94). Nineteen modules ship two each, so the file count silently over-counts modules. |
| Denominator | 138, from a `find -type d -name template` that double-counts | **126** — the directories that ship an `account.tax-*.csv`, i.e. that define a chart at all. This is the only denominator with a stated definition. |
| Ratio | 113 of 138 (82%) | **94 of 126 (75%)** |

The UNIT was switched between numerator and denominator mid-count. That is precisely the
`UNIT` clause of the project's Denominator Completeness Rule, failing inside the finding
whose own closing note congratulated this session for catching a `-maxdepth` error in the
same enumeration. **The substantive conclusion is unchanged — Thailand ships none, and
three-quarters of chart-shipping peers ship one — but the ratio as first published was
wrong, and it had already propagated into the Layer-1 handoff file.** Recorded as
`REV-E-13`; the earlier `-maxdepth 3` error is `REV-E-04`.

Enumeration commands, both stated so the count can be reproduced:

    find "<02 OTHER>" -maxdepth 4 -name 'account.fiscal.position-*.csv' \
      | sed 's|.*/02 OTHER/||; s|/.*||' | sort -u | wc -l      -> 94
    find "<02 OTHER>" -maxdepth 4 -name 'account.tax-*.csv' \
      | sed 's|.*/02 OTHER/||; s|/.*||' | sort -u | wc -l      -> 126
