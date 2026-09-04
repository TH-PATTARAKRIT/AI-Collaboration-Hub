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
| `A-03` | Tax invoice issued in error / cancelled | Governed by the substitute-invoice and cancellation rules | held at `U-08` | No document object exists, so there is nothing to cancel; only the accounting entry can be reversed | Cannot be assessed until `U-08` is closed |
| `A-04` | Wrong tax period | The supply belongs to the tax month of its tax point | `S-09` `S-15` | A tax period field exists on the move and does not drive selection (`P07-F-02`) | A user who corrects the tax period sees the correction on screen and not in the report |
| `A-05` | Input tax not claimed in the invoice month | Deferred claim, subject to the rule held at `U-03` | `U-03` | The tax period field is the intended mechanism and is inert | Cannot be evidenced as compliant until `U-03` is closed |
| `A-06` | Excess input tax | Carry forward or claim refund; refund within 3 years of the filing date | `S-18` `S-34` | Report line `10. Excess tax payment carried forward from last period` exists in the report structure; its population mechanism was not traced | `P07-U-12` |
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

`A-15` is the most serious item in this file. Four independent, ordinary,
non-privileged actions change the content of a **previously filed statutory report** while
leaving the ledger untouched and leaving no trace:

1. renaming a tax group (`RPT-06`/`RPT-08` row inclusion),
2. changing a partner's company type (PND53 title column),
3. changing a partner's branch or company registry (branch column, sourced differently in
   different reports),
4. reversing a payment so an invoice returns to `not_paid` (PND row disappears).

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
Belgium, taken as one comparison point, registers separate return types for the VAT
return, the VAT listing and the EC sales list, and sets `default_deadline_periodicity`,
`states_workflow`, `auto_generate` and the tax authority's bank account.

| Thai statutory return | Registered as a return type | Deadline configured | Workflow configured |
|---|---|---|---|
| ภ.พ.30 (VAT, 15th of following month, `S-15`) | yes, as the generic name `Tax` | **no** | **no** |
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
| Filing state | yes (`state`, `next_state`, `states_workflow`) | not configured |
| Statutory deadline | yes (`date_deadline`, periodicity, days delay) | not configured |
| Compliance check | yes (`account.return.check`) | none |
| Filed-figure snapshot | not established in this session | — |
| Adjustment as a first-class fact | no | no |
| Original-document reference on an adjustment | no | no |
| Tax period state / close | not found in the tax layer; accounting lock dates are the only control (`A-14`) | — |

`P07-N-15` is accordingly **withdrawn** as originally stated and replaced by `P07-F-37`.
The withdrawal is recorded in `15_P07_REVISION_LOG.md` §4. `P07-U-19` is narrowed to: the
filed-figure snapshot and re-run behaviour of `account.return` were not examined.
