# P07 — EVENT TO GL MATRIX

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Tax Account Population

Enumerated from the Thai chart template (`l10n_th/data/template/account.account-th.csv`).
`UNIT` = one account code. The description column is quoted from the template itself,
because §4 turns on it.

| Code | Name | Type | Description as shipped |
|---|---|---|---|
| `114200` | Input VAT | `asset_current` | "Tax paid on purchases. Balance is transferred to VAT Payable/Receivable at month-end." |
| `114300` | WHT Creditable | `asset_current` | "Prepaid Tax: Income tax deducted by customers when paying you. Claimable against year-end CIT." |
| `114400` | VAT Receivable | `asset_receivable` | "Net tax refund due from the Revenue Dept (if Input VAT > Output VAT)." |
| `114401` | WHT Receivable | `asset_receivable` | "Tax Closing Account: Consolidated WHT tax credits transferred from daily accounts." |
| `114500` | Prepaid CIT (PND 51) | `asset_current` | mid-year corporate income tax |
| `213200` | Output VAT | `liability_current` | "Net VAT liability (Output VAT - Input VAT) to be remitted to Revenue Dept (PP.30)." |
| `213300` | Tax Withheld - PND 1 | `liability_current` | "Tax deducted from Employee Salaries. Remit monthly via form PND 1." |
| `213301` | Tax Withheld - PND 3 | `liability_current` | "Tax deducted from Individual Suppliers. Remit monthly via form PND 3." |
| `213302` | Tax Withheld - PND 53 | `liability_current` | "Tax deducted from Juristic (Company) Suppliers. Remit monthly via form PND 53." |
| `213303` | Tax Withheld - PND 54 | `liability_current` | "Tax deducted from payments sent Overseas. Remit via form PND 54." |
| `213400` | VAT Payable | `liability_payable` | "VAT Payable: Tax collected from sales. To be remitted to Revenue Dept (PP.30)." |
| `213500` | WHT Payable | `liability_payable` | "Net WHT liability moved here from PND specific accounts at month-end for lump-sum payment." |

## 2. Event → Repartition → Account

Read from `l10n_th/data/template/account.tax-th.csv` (repartition rows) and
`account.tax.group-th.csv` (group settlement accounts).

| # | Tax event | Tax template | Doc type | Base tag | Tax tag | Posts to | Group settlement accounts |
|---|---|---|---|---|---|---|---|
| `G-01` | Output VAT 7% | `tax_output_vat` | invoice, refund | `1. Sales amount` | `5. Output tax` | `213200` | payable `213400`, receivable `114400` |
| `G-02` | Output VAT 0% (zero-rated) | `tax_output_vat_0` | invoice, refund | `1. Sales amount` **and** `2. Less sales subject to 0% tax rate` | `5. Output tax` | `213200` | **no tax group assigned in the template** |
| `G-03` | Output VAT exempt | `tax_output_vat_exempted` | invoice, refund | `1. Sales amount` **and** `3. Less exempted sales` | `5. Output tax` | `213200` | **no tax group assigned in the template** |
| `G-04` | Input VAT 7% | `tax_input_vat` | invoice, refund | `6. Purchase amount…` | `7. Input tax…` | `114200` | payable `213400`, receivable `114400` |
| `G-05` | Input VAT 0% | `tax_input_vat_0` | invoice, refund | `6. Purchase amount…` | `7. Input tax…` | `114200` | **none** |
| `G-06` | Input VAT exempt / non-claimable | `tax_input_vat_exempted` | invoice, refund | `6. Purchase amount…` | `7. Input tax…` | `114200` | **none** |
| `G-07` | WHT on purchases, juristic payee, 1 / 2 / 3 / 5% | `tax_wht_co_{1,2,3,5}` | invoice, refund | `Income PND53` | `PND53` | `213302` | payable `213500`, receivable `114401` |
| `G-08` | WHT on purchases, natural payee, 1 / 2 / 3 / 5% | `tax_wht_pers_{1,2,3,5}` | invoice, refund | `Income PND3` | `PND3` | `213301` | payable `213500`, receivable `114401` |
| `G-09` | WHT suffered on sales, 1 / 2 / 3 / 5% | `tax_wht_income_{1,2,3,5}` | invoice, refund | **empty** | **empty** | `114300` | payable `213500`, receivable `114401` |
| `G-10` | WHT booked through the payment register (third-party framework) | not a tax; a payment-difference write-off | — | — | tags copied from `account.withholding.tax.tax_tag_ids` | the withholding account on the WHT record | none — it is not a tax line |

## 3. Findings from the Mapping

| # | Finding | Consequence |
|---|---|---|
| `GL-01` | `G-09` carries **no tags on either side**. | Sales-side withholding posts to `114300` and is selected by no tax report, because every PND handler selects on tag membership. `W-K-08`. |
| `GL-02` | `G-02`, `G-03`, `G-05`, `G-06` carry **no tax group** in the template. | They cannot satisfy the SMEsPlus report predicate `group_name == {'en_US': 'VAT 7%'}` (`P07-F-01`), so zero-rated and exempt supplies are excluded from the main statutory VAT reports by two independent mechanisms. |
| `GL-03` | `G-10` produces an accounting effect that is **not a tax line**: no `tax_line_id`, no `tax_base_amount`, only manually-copied tags. | The vendor PND handler, which inner-joins on `tax_line_id`, cannot see it at all; the override sees the invoice instead of it (`W-C-01`…`W-C-04`). One economic event, two incompatible ledger shapes. |
| `GL-04` | `G-07` and `G-08` post the withholding as a **tax on the invoice**, while `G-10` posts it as a **write-off on the payment**. Both are available and both are configured by the same localisation. | A tenant that configures WHT as an invoice tax and a tenant that uses the payment register produce different ledgers, different tax-line shapes, and different report behaviour for the same statute. Neither path is declared canonical. |
| `GL-05` | Every WHT template is `type_tax_use = purchase` except `tax_wht_income_*`, which is `sale`; but the *rate* is identical across the three families and the *tax group* is shared (`WHT 1%`…`WHT 5%`). | The tax group encodes rate only. Form classification exists **solely** as the literal text of the repartition tag, which is why the runtime classifier must read strings (`03 §4.2`). |

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
| Zero-rated sale | revenue credit, receivable debit, `213200` credit of zero, base tagged `1.` and `2.` | true tax line, zero amount | main SMEsPlus report: **no** (no `VAT 7%` group); zero report: only if the **whole move** has `amount_tax = 0` |
| Standard-rated purchase | expense debit, payable credit, `114200` debit tagged `7. Input tax` | true tax line | all VAT reports |
| WHT via invoice tax (`G-07`/`G-08`) | expense debit, payable credit reduced, `213301`/`213302` credit tagged `PND3`/`PND53` | true tax line | vendor PND handler branch 1, and override branch 1 |
| WHT via payment register (`G-10`) | payable debit, bank credit, withholding-account credit carrying copied tags | **write-off line, not a tax line** | vendor PND handler: **no**; override: **no** (excluded by `payment_id is null`); the invoice line is reported in its place |
| WHT suffered on sales (`G-09`) | receivable credit reduced, `114300` debit, **no tags** | true tax line with empty tags | **no report** |

The last two rows are the P07 headline for the core accounting reconciliation: two of the
six tax-bearing ledger shapes produced by this localisation are invisible to the statutory
reporting layer, and a third is reported by proxy from a different document on a different
date.
