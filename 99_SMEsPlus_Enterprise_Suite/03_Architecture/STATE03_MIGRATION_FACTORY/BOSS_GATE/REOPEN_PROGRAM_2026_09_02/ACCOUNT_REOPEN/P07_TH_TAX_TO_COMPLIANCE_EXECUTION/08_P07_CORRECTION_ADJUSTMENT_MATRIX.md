# P07 — CORRECTION / ADJUSTMENT MATRIX

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Scope

Correction, cancellation, adjustment, refund, tax period and closed period, for VAT and
for withholding tax. Each row states the statutory treatment, the mechanism available in
the declared source set, and the residual.

## 2. VAT Corrections

| # | Case | Statutory treatment | Source | Mechanism in the declared source set | Residual |
|---|---|---|---|---|---|
| `A-01` | Price reduced after issuance (return of goods, discount, over-charge) | Issue a **credit note** referencing the original tax invoice; deduct output tax **in the tax month the note is issued**; recipient deducts input tax in the month received | `S-14` `S-24` | Accounting reversal or a customer credit note; no Thai note class; no original-invoice reference; placed by accounting date | Adjustment cannot be identified as an adjustment, cannot cite its original, and lands in the wrong month whenever the accounting date is aligned to the original rather than to the note |
| `A-02` | Price increased after issuance | Issue a **debit note**; include increased output tax in the month the note is issued | `S-13` `S-23` | No debit-note class selected by the declared patterns | Handled, if at all, as an additional invoice — which is a different document with a different statutory meaning |
| `A-03` | Tax invoice issued in error / cancelled | Governed by the substitute-invoice and cancellation rules | held at `P07-U-08` | No document object exists, so there is nothing to cancel; only the accounting entry can be reversed | Cannot be assessed until `P07-U-08` is closed |
| `A-04` | Wrong tax period | The supply belongs to the tax month of its tax point | `S-09` `S-15` | A tax period field exists on the move and does not drive selection (`P07-F-02`) | A user who corrects the tax period sees the correction on screen and not in the report |
| `A-05` | Input tax not claimed in the invoice month | Deferred claim, subject to the rule held at `P07-U-03` | `P07-U-03` | The tax period field is the intended mechanism and is inert | Cannot be evidenced as compliant until `P07-U-03` is closed |
| `A-06` | Excess input tax | Carry forward or claim refund; refund within 3 years of the filing date | `S-18` `S-34` | **Implemented**: line `10_EXCESS_CARRIED_FORWARD` uses an `external` carryover expression scoped to `previous_return_period`, plus a tax-tag expression; lines 11 and 12 consume it. `P07-U-12` **CLOSED**. | The carryover is only as sound as the period it looks back to, and that period comes from an editable company setting rather than from the statute (`P07-F-40`). No refund-claim representation was found — class `B`, boundary as `A-13`. |
| `A-07` | Report re-run after the period is closed | Not addressed by the Revenue Code; an internal control question | — | The reports are query-time renderings with no snapshot, no freeze, and no version | A report printed for filing and the same report re-printed later can differ with no trace. Recorded as `P07-F-36` |

## 3. Withholding Tax Corrections

| # | Case | Statutory treatment | Source | Mechanism | Residual |
|---|---|---|---|---|---|
| `A-08` | Certificate issued with wrong particulars | Reissue; the payee holds the original | `S-31` | `state` = `cancel` plus `ref_wt_cert_id` pointing at the superseded certificate (`withholding_tax_cert.py:90-102`) | **Adequate pattern.** Cancellation is by reference, not deletion. The residual is that unlink is nevertheless granted to the billing group (`P07-F-19`) |
| `A-09` | Withholding reversed because the payment is cancelled | The withholding never occurred | derived from `S-30` | The payment reversal reverses the write-off line; the PND override keys on the **invoice**, so the reversal is visible only through `payment_state` | If the reversal returns the invoice to `not_paid`, branch 2 stops reporting it — retroactively changing a previously filed period's content with no trace |
| `A-10` | Over-withheld or under-withheld amount corrected | Correct the remittance and the certificate | `S-32` `S-33` | The PND figure is recomputed from rate × base, so a corrected ledger amount does not change the PND figure at all | **The correction cannot reach the filing.** `W-C-03` |
| `A-11` | Withholding on a partial payment | Withhold on the amount paid | `S-30` | Full invoice withholding is reported on the first non-`not_paid` state | `W-C-02` |
| `A-12` | Certificate created for a withholding that is later found to belong to a different PND form | Reissue under the correct form | `S-33` | `income_tax_form` is readonly on the certificate and set at creation | Requires cancel-and-reissue; consistent with `A-08` |

## 4. Period and Closed Period

| # | Question | Finding |
|---|---|---|
| `A-13` | Is there a tax period object distinct from the accounting period? | A **date field** exists (`account.move.tax_period`). No tax **period** object, period state, open/closed status or lock was found — class `B`, boundary: the 15 modules of `13 §5`; the base application's own period machinery was not re-enumerated. |
| `A-14` | Can a tax period be closed? | No tax-period close was selected by the declared patterns — class `B`, same boundary as `A-13`. The accounting lock dates of the base application are the only control, and they operate on the accounting date — which, given `P07-F-02`, is also what the tax reports select on. This is the one place where the accounting-date inversion is accidentally protective. |
| `A-15` | Can a posted tax fact be altered after filing? | Not through the tax layer: posted lines are immutable in the base application. But the **reported** figure can change without any ledger change, through `A-09` (payment state), through master-data change (`W-K-05` title source, `P07-F-06` branch source), and through a tax-group rename (`P07-F-01`). |
| `A-16` | Is there a filing record that fixes what was filed? | A filing framework exists in the base set (`account.return`, with state and deadline). Thailand registers **one generic return type** on it and configures no deadline and no workflow; PND3, PND53 and PND54 are not registered at all. See §5. |

`A-15` is the most serious item in this file. It was first recorded as a four-member
class; independent challenge confirmed all four and established that the class has **at
least seven** members, and that the two most severe were not among the original four.

| # | Ordinary, non-privileged action | What it silently rewrites in an already-filed report | Evidence |
|---|---|---|---|
| 1 | **Editing a tax's percentage** | The PND `Tax Rate`, `WHT Amount` **and** `Tax Type` columns of every previously filed row, because all three are computed from `tax.amount` on the live record at render time | `l10n_th_reports/models/tax_report_pnd.py:44-54`; override `:35-45`, `:70-80` |
| 2 | **Renaming a shared company-type record** | The `Title` column of every filed PND row for every partner of that legal form — one edit, many rows; the field is translatable and untracked | `partner_company_type/models/res_partner_company_type.py:12` |
| 3 | Renaming a tax group | Row inclusion in the two SMEsPlus VAT registers; `name` carries no `tracking` | `account_generic_tax_report.py:88`; `account/models/account_tax.py:32` |
| 4 | Changing a partner's company type | The PND `Title` column on **both** PND3 and PND53, **and** the partner's stored `name` — hence the `Contact Name` column and every re-rendered tax invoice | `l10n_th_withholding_tax/models/tax_report_pnd.py:24-26`, `:59-61`; `l10n_th_partner/models/res_partner.py:45-57` |
| 5 | Switching a partner from company to individual | Blanks `partner_company_type_id`, and with it the `Title` column of all prior filings | `l10n_th_partner/models/res_partner.py:59-64` |
| 6 | Changing a partner's branch or company registry | The branch column — sourced from four different places across four reports | `06 §1`; `P07-C-02` |
| 7 | Reversing a payment so an invoice returns to `not_paid` | The PND row disappears from any re-run | `l10n_th_withholding_tax/models/tax_report_pnd.py:92` |
| 8 | Re-parenting a partner | The `Title` column, via the parent fallback in the PND query | `tax_report_pnd.py:25`, `:49-50` |

Members 1 and 2 were added during independent challenge and are the most severe: member 1
rewrites monetary amounts and statutory classifications, and member 2 does so across every
partner sharing one master record.

`P07-F-36` is accordingly restated: **the reported figure is a render-time computation over
live master data, so no filed figure is reproducible.**

## 5. The Closing Segment — Framework Present, Thai Provisioning Minimal

An earlier draft of this file recorded the whole closing segment
(`Tax Report -> Filing / Adjustment / Close`) as absent. **That was wrong and is corrected
here.** The base set contains a full return-filing framework, and the defect is a Thai
provisioning gap on top of it, which is a materially different and more actionable finding.

### 5.1 What the framework provides

`account_reports/models/account_return.py` defines `account.return.type` (line 59),
`account.return` (line 624) and `account.return.check` (line 2660). The return type carries
`default_deadline_periodicity`, `deadline_periodicity`, `default_deadline_start_date`,
`deadline_days_delay`, `default_deadline_days_delay`, `states_workflow`,
`payment_partner_bank_id` and `country_id`. The return instance carries `state`,
`next_state` and a computed `date_deadline`, and is ordered by deadline.

Filing instances, filing states, statutory deadlines and compliance checks therefore
**exist** in the declared source set.

### 5.2 What Thailand provisions on it

`l10n_th_reports/data/account_return_data.xml` is ten lines long and defines exactly one
record:

    <record id="th_tax_return_type" model="account.return.type">
        <field name="name">Tax</field>
        <field name="report_id" ref="l10n_th.tax_report"/>
        <field name="country_id" ref="base.th" />
    </record>

No periodicity, no deadline delay, no workflow, no payment partner bank, no check.

### 5.3 The gap, measured

`POPULATION` = every module in `02 OTHER` shipping `account.return.type` data.
`PATTERN` = files containing `model="account.return.type"`. `RESULT` = **118 modules**.
Belgium, read in full as one comparison point, registers **five** return types (VAT, VAT
Listing, EC Sales List, corporate-tax advance payment, audit). An earlier draft claimed
Belgium's differentiator was that it sets the four deadline and workflow attributes; that
comparison does **not** hold — `be_vat_return_type` sets only `name`, `report_id`,
`country_id` and a payment bank account, so on that test Belgium's VAT return scores as
Thailand's does. The differentiators that do hold are **coverage** (five registered
returns against one) and **compliance checks**: Belgium ships
`l10n_be_reports/data/account_return_check_template.xml` and a return-type subclass in
`l10n_be_reports/models/account_return.py`; Thailand ships neither.

| Thai statutory return | Registered as a return type | Deadline configured | Workflow configured |
|---|---|---|---|
| ภ.พ.30 (VAT, 15th of following month, `S-15`) | yes, as the generic name `Tax` | **no — a generic computed deadline is shown instead** | inherited by computation, not set |
| ภ.ง.ด.3 (`S-33`) | **no** — exists only as a report with a CSV export button | no | no |
| ภ.ง.ด.53 (`S-33`) | **no** — same | no | no |
| ภ.ง.ด.54 | **no** — general-ledger account only (`03 §4.1`) | no | no |

`P07-F-37` — the Thai localisation registers 1 of its 4 principal statutory returns with
the filing framework the declared source set already provides, names it generically, and
configures none of the four deadline and workflow attributes the framework exposes. The
statutory deadlines established at `S-15` and `S-32` are therefore not represented anywhere
in the system.

### 5.4 Corrected element table

| Element | Framework provides | Thailand provisions |
|---|---|---|
| Filing instance | yes (`account.return`) | one generic type only |
| Filing state | yes (`state`, `next_state`, `states_workflow`) | **configured by computation, not by data.** `states_workflow` is computed (`account_return.py:82-93`), and because the Thai report's `root_report_id` is the generic tax report, `is_tax_return_type` is true and the workflow resolves to `generic_state_tax_report` (`:160-169`). `auto_generate` likewise computes true (`:154-156`), so Thai VAT returns **are** generated. An earlier draft recorded both as "not configured", which was wrong. |
| Statutory deadline | yes (`date_deadline`, periodicity, days delay) | **present but generic, which is worse than absent.** With `deadline_days_delay` unset, the deadline is `date_to + company.account_return_reminder_day` (`account_return.py:850-853`) — a company-wide reminder day presented to the user as the return's due date, bearing no relation to the 15th-of-the-following-month rule of `S-15`. |
| Compliance check | yes (`account.return.check`) | none |
| Filed-figure snapshot | not established in this session | — |
| Adjustment as a first-class fact | no | no |
| Original-document reference on an adjustment | no | no |
| Tax period state / close | not found in the tax layer; accounting lock dates are the only control (`A-14`) | — |

`P07-N-15` is accordingly **withdrawn** as originally stated and replaced by `P07-F-37`.
The withdrawal is recorded in `15_P07_REVISION_LOG.md` §4. `P07-U-19` is narrowed to: the
filed-figure snapshot and re-run behaviour of `account.return` were not examined.

## 6. Negative Claims Made in This File

Added after independent challenge, which established that this file and `06` asserted
system-wide negatives with no class and no boundary. Of the negatives that had been left
unregistered here, three were subsequently found to be wrong or over-stated (the two filing
rows corrected in §5.4, and the `A-13` mechanism description). No registered negative in
this package has yet failed. See `15 §4` `REV-E-10`.

| ID | Claim | Class | Boundary |
|---|---|---|---|
| `P07-N-20` | No Thai debit-note document class was found. | `B` | the 15 modules of `13 §5`; the base document typology was not re-enumerated |
| `P07-N-21` | No snapshot, freeze or version of a rendered statutory report was found. | `B` | the 15 modules of `13 §5`; the base `account.return` framework's own attachment behaviour was **not** examined (`P07-U-19`) |
| `P07-N-22` | No tax-period object, period state, open/closed status or lock was found in the tax layer. | `B` | as `P07-N-21`; the base application's accounting period machinery was not re-enumerated |
| `P07-N-23` | No representation of a refund claim under `S-18` / `S-34` was found. | `B` | the 15 modules of `13 §5` |
| `P07-N-24` | Posted accounting lines are immutable in the base application. | **positive claim, not a negative — and NOT verified in this session.** Recorded here because `A-15`'s framing leans on it. | `C — NOT YET SEARCHED`; carried as `P07-U-21` |
