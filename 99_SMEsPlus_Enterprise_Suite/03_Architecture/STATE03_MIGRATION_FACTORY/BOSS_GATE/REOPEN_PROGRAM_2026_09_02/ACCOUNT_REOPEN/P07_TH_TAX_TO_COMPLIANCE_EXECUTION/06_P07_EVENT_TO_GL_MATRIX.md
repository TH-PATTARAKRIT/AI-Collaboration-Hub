# P07 — EVENT TO GL MATRIX

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Tax Account Population

Enumerated from the Thai chart template (`l10n_th/data/template/account.account-th.csv`).
`UNIT` = one account code. The description column is quoted from the template, **abridged
where marked with an ellipsis**; §4 turns on the two descriptions quoted there, which are
given in full.

| Code | Name | Type | Description as shipped |
|---|---|---|---|
| `114200` | Input VAT | `asset_current` | "Tax paid on purchases. Balance is transferred to VAT Payable/Receivable at month-end." |
| `114300` | WHT Creditable | `asset_current` | "Prepaid Tax: Income tax deducted by customers when paying you. Claimable against year-end CIT." |
| `114400` | VAT Receivable | `asset_receivable` | "Net tax refund due from the Revenue Dept (if Input VAT > Output VAT)." |
| `114401` | WHT Receivable | `asset_receivable` | "Tax Closing Account: Consolidated WHT tax credits transferred from daily accounts. To be claimed against annual Corporate Income Tax (P.N.D. 50)." |
| `114500` | Prepaid CIT (PND 51) | `asset_current` | "Prepaid Tax: Corporate Income Tax paid mid-year (Form PND 51). Creditable against annual tax." |
| `213200` | Output VAT | `liability_current` | "Net VAT liability (Output VAT - Input VAT) to be remitted to Revenue Dept (PP.30)." |
| `213300` | Tax Withheld - PND 1 | `liability_current` | "Tax deducted from Employee Salaries. Remit monthly via form PND 1." |
| `213301` | Tax Withheld - PND 3 | `liability_current` | "Tax deducted from Individual Suppliers. Remit monthly via form PND 3." |
| `213302` | Tax Withheld - PND 53 | `liability_current` | "Tax deducted from Juristic (Company) Suppliers. Remit monthly via form PND 53." |
| `213303` | Tax Withheld - PND 54 | `liability_current` | "Tax deducted from payments sent Overseas. Remit via form PND 54." |
| `213400` | VAT Payable | `liability_payable` | "VAT Payable: Tax collected from sales. To be remitted to Revenue Dept (PP.30)." |
| `213500` | WHT Payable | `liability_payable` | "Net WHT liability moved here from PND specific accounts at month-end for lump-sum payment to Revenue Dept." |

## 2. Event → Repartition → Account

Read from `l10n_th/data/template/account.tax-th.csv` (repartition rows) and
`account.tax.group-th.csv` (group settlement accounts).

| # | Tax event | Tax template | Doc type | Base tag | Tax tag | Posts to | Group settlement accounts |
|---|---|---|---|---|---|---|---|
| `G-01` | Output VAT 7% | `tax_output_vat` | invoice, refund | `1. Sales amount` | `5. Output tax` | `213200` | payable `213400`, receivable `114400` |
| `G-02` | Output VAT 0% (zero-rated) | `tax_output_vat_0` | invoice, refund | `1. Sales amount` **and** `2. Less sales subject to 0% tax rate` | `5. Output tax` | `213200` | blank in the template; **resolves at load to `WHT 1%`** — see §3A |
| `G-03` | Output VAT exempt | `tax_output_vat_exempted` | invoice, refund | `1. Sales amount` **and** `3. Less exempted sales` | `5. Output tax` | `213200` | blank in the template; **resolves at load to `WHT 1%`** — see §3A |
| `G-04` | Input VAT 7% | `tax_input_vat` | invoice, refund | `6. Purchase amount…` | `7. Input tax…` | `114200` | payable `213400`, receivable `114400` |
| `G-05` | Input VAT 0% | `tax_input_vat_0` | invoice, refund | `6. Purchase amount…` | `7. Input tax…` | `114200` | blank in the template; **resolves at load to `WHT 1%`** — see §3A |
| `G-06` | Input VAT exempt / non-claimable | `tax_input_vat_exempted` | invoice, refund | `6. Purchase amount…` | `7. Input tax…` | `114200` | blank in the template; **resolves at load to `WHT 1%`** — see §3A |
| `G-07` | WHT on purchases, juristic payee, 1 / 2 / 3 / 5% | `tax_wht_co_{1,2,3,5}` | invoice, refund | `Income PND53` | `PND53` | `213302` | payable `213500`, receivable `114401` |
| `G-08` | WHT on purchases, natural payee, 1 / 2 / 3 / 5% | `tax_wht_pers_{1,2,3,5}` | invoice, refund | `Income PND3` | `PND3` | `213301` | payable `213500`, receivable `114401` |
| `G-09` | WHT suffered on sales, 1 / 2 / 3 / 5% | `tax_wht_income_{1,2,3,5}` | invoice, refund | **empty** | **empty** | `114300` | payable `213500`, receivable `114401` |
| `G-10` | WHT booked through the payment register (third-party framework) | not a tax; a payment-difference write-off | — | — | tags copied from `account.withholding.tax.tax_tag_ids` | the withholding account on the WHT record | none — it is not a tax line |

## 3. Findings from the Mapping

| # | Finding | Consequence |
|---|---|---|
| `GL-01` | `G-09` carries **no tags on either side**. | Sales-side withholding posts to `114300` and is selected by no tax report in the declared set. Both **PND** handlers select on tag membership, so they miss it; the third WHT report selects on certificate lines rather than tags (`l10n_th_withholding_tax_report/models/report_withholding_tax.py:152-155`) and misses it for a different reason — no certificate exists for sales-side withholding. An earlier draft said "every PND handler selects on tag membership", which was true, and generalised it to every WHT report, which was not. `W-K-08`. Class `A` within the 15-module population. |
| `GL-02` | `G-02`, `G-03`, `G-05`, `G-06` carry a **blank** tax group in the template — and therefore do **not** end up group-less. See §3A. | They cannot satisfy the SMEsPlus report predicate at `:88` (`P07-F-01`), so zero-rated and exempt supplies are excluded from the main statutory VAT reports; and they are classified into a **withholding** tax group, which is a posting-path consequence, not only a reporting one. |
| `GL-03` | `G-10` produces an accounting effect that is **not a tax line**: no `tax_line_id`, no `tax_base_amount`, only manually-copied tags. | The vendor PND handler, which inner-joins on `tax_line_id`, cannot see it at all; the override sees the invoice instead of it (`W-C-01`…`W-C-04`). One economic event, two incompatible ledger shapes. |
| `GL-04` | `G-07` and `G-08` post the withholding as a **tax on the invoice**, while `G-10` posts it as a **write-off on the payment**. Both are available and both are configured by the same localisation. | A tenant that configures WHT as an invoice tax and a tenant that uses the payment register produce different ledgers, different tax-line shapes, and different report behaviour for the same statute. Neither path is declared canonical. |
| `GL-05` | Every WHT template is `type_tax_use = purchase` except `tax_wht_income_*`, which is `sale`; the *rate* is identical across the three families and the *tax group* is shared (`WHT 1%`…`WHT 5%`). | The tax group encodes rate only. For the two purchase families, form classification exists **only** as the literal text of the repartition tag, which is why the runtime classifier must read strings (`03 §4.2`). For the income family it does not exist in any form, because that family carries no tag at all (`GL-01`) — an earlier draft's "solely" covered the first case and silently mis-stated the second. |

## 3A. Where the Blank Tax Group Actually Resolves — `P07-F-42`

An earlier draft of this file recorded the four zero-rated and exempt VAT taxes as having
**no tax group**. That is true of the CSV and **false of the resulting records**, and the
correction matters because it moves the finding from the reporting path to the posting
path. Two independent reviewers reached this conclusion separately; the chain below is the
one that was traced end to end.

| Step | Evidence | Result |
|---|---|---|
| 1 | `account/models/chart_template.py:1332` — `_parse_csv` builds values with `... if key != 'id' and value and (...)` | an **empty** CSV cell is omitted from the vals dict, not set to `False` |
| 2 | `account/models/account_tax.py:156-161` — `tax_group_id` is `compute='_compute_tax_group_id', store=True, readonly=False, required=True, precompute=True` | a stored, required field with a precompute |
| 3 | ORM `_add_precomputed_values` fires a precompute exactly when the field name is **absent** from vals | step 1 guarantees absence, so the compute runs |
| 4 | `account/models/account_tax.py:274-291` — the compute assigns `search([<company domain>, ('country_id','=',country.id)], limit=1)` | first matching Thai group wins |
| 5 | `account/models/account_tax.py:28` `_order = 'sequence asc, id'`; `:33` `sequence` defaults to 10 for every group | ordering collapses to lowest id |
| 6 | `chart_template.py` loads `account.tax.group` before `account.tax`, in CSV row order; `account.tax.group-th.csv` order is `tax_group_1, tax_group_2, tax_group_3, tax_group_5, tax_group_vat_7` | lowest id is `tax_group_1` = **`WHT 1%`** |
| 7 | `account.tax.group-th.csv` — `tax_group_1` carries `tax_payable_account_id = 213500 WHT Payable`, `tax_receivable_account_id = 114401 WHT Receivable` | the settlement accounts are the **withholding** control accounts |

**`P07-F-42` — Thailand's zero-rated and exempt VAT taxes are classified into the
withholding tax group `WHT 1%`, and therefore settle against the withholding control
accounts rather than the VAT ones.** Two consequences follow, and the second is the more
serious because it is not a reporting artefact:

1. In the invoice tax-totals block, a 0% or exempt VAT line is grouped and labelled
   `WHT 1%`.
2. The tax-closing entry, whose counterpart is the group's `tax_payable_account_id`
   (`account/models/account_tax.py:35-39`), routes zero-rated and exempt VAT to
   `213500` / `114401` — the accounts the chart reserves for withholding tax settlement
   (`06 §1`).

Class and boundary: **source-derived through a complete seven-step chain, not executed**
until `REV-E-25`. **Now VERIFIED against a deployed database**: all four zero-rated and exempt taxes carry `tax_group_id 1` = `WHT 1%`, settling to accounts 64/19 against VAT's 63/18 (`22 §4.2`). The residual — record-creation order at template load — is resolved and **`P07-U-20` is CLOSED**. This is the strongest available class short of
execution, and it is materially stronger than the `D — UNKNOWN` at which this finding was
first recorded.

## 4. Chart Description Defect

The withholding accounts describe a coherent two-stage design: form-specific daily
accounts (`213301`, `213302`, `213303`) consolidated at month-end into `213500 WHT
Payable`. `114200 Input VAT` describes the same pattern for VAT: "Balance is transferred to
VAT Payable/Receivable at month-end."

The two VAT settlement accounts do not follow it:

| Account | Actual role, from the repartition and group data | Description as shipped | Assessment |
|---|---|---|---|
| `213200 Output VAT` | The **daily gross output VAT** account: every output repartition line posts here (`G-01`, `G-02`, `G-03`). | "**Net VAT liability (Output VAT - Input VAT)** to be remitted to Revenue Dept (PP.30)." | The description states a net-settlement role that the data contradicts. |
| `213400 VAT Payable` | The **month-end settlement** account: it is the tax group's `tax_payable_account_id`, the counterpart of `114200`'s stated month-end transfer. | "VAT Payable: **Tax collected from sales.** To be remitted to Revenue Dept (PP.30)." | The description states a daily-collection role that the data contradicts. |

`P07-F-34` — the two descriptions are transposed relative to the roles the repartition and
group data actually assign. This is a **documentation** defect, not a posting defect: the
postings themselves are consistent with the WHT pattern and with `114200`. It is material
because the account description is the only in-product statement of the design, an
accountant selecting an account manually reads it, and it is shipped in both English and
Thai.

## 5. Journal Effect by Scenario

Stated as the ledger shape each configuration produces, so that P08 can reconcile them.

| Scenario | Ledger shape | Tax-line shape | Visible to |
|---|---|---|---|
| Standard-rated sale | revenue credit, receivable debit, `213200` credit tagged `5. Output tax` | true tax line | all VAT reports |
| Zero-rated sale | revenue credit, receivable debit, `213200` credit of zero, base tagged `1.` and `2.`; **group resolves to `WHT 1%`, so the closing entry settles it against `213500`/`114401`** (`§3A`) | true tax line, zero amount | main SMEsPlus report: **no** (group is not `VAT 7%`); zero report: only if the **whole move** has `amount_tax = 0` |
| Standard-rated purchase | expense debit, payable credit, `114200` debit tagged `7. Input tax` | true tax line | all VAT reports |
| WHT via invoice tax (`G-07`/`G-08`) | expense debit, payable credit reduced, `213301`/`213302` credit tagged `PND3`/`PND53` | true tax line | vendor PND handler branch 1, and override branch 1 |
| WHT via payment register (`G-10`) | payable debit, bank credit, withholding-account credit carrying copied tags | **write-off line, not a tax line** | vendor PND handler: **no**; override: **no** (excluded by `payment_id is null`); the invoice line is reported in its place |
| WHT suffered on sales (`G-09`) | receivable credit reduced, `114300` debit, **no tags** | true tax line with empty tags | **no report** |

The last two rows are the P07 headline for the core accounting reconciliation: two of the
six tax-bearing ledger shapes produced by this localisation are invisible to the statutory
reporting layer, and a third is reported by proxy from a different document on a different
date.

## 6. Negative Claims Made in This File

Added after independent challenge, which established that this file and `08` carried
system-wide negatives with no class and no boundary while `02`, `03` and `05` registered
theirs. Every negative that had been left unregistered and was then tested was found to be
wrong or over-stated; every registered negative survived. That correlation is itself the
finding — see `15 §4` `REV-E-10`.

| ID | Claim | Class | Boundary |
|---|---|---|---|
| `P07-N-16` | The income-side withholding templates carry no tag on either repartition side. | `A — VERIFIED ABSENCE WITHIN SCOPE` | `l10n_th/data/template/account.tax-th.csv`, all 16 repartition rows of `tax_wht_income_{1,2,3,5}`, read individually |
| `P07-N-17` | No tax report in the 15-module population selects the income-side withholding fact. | `A` | the 15 modules of `13 §5`; both PND handlers select on tag membership, the WHT report selects on certificate lines and no certificate exists for the sales side |
| `P07-N-18` | Neither withholding ledger shape is declared canonical anywhere in the declared source set. | `B — NOT FOUND IN SEARCHED SCOPE` | PATH SET of `13 §2`; no design record, configuration flag or constraint expressing precedence was found |
| `P07-N-19` | The four zero-rated and exempt VAT taxes carry a blank tax-group cell in the template. | `A` | `account.tax-th.csv`, the four template rows. **This is a statement about the CSV only.** The resulting records are **not** group-less — see `§3A`. |
