# P07 — WITHHOLDING TAX EVENT MODEL

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Statutory WHT Event Chain

| Link | Statutory content | Source |
|---|---|---|
| Source business event | Payment of assessable income under s.40 | `S-30` |
| Tax trigger | **The moment of payment.** "shall withhold income tax at every time of payment". For income brought into withholding by Director-General order, the same rule applies. | `S-30` `S-28` `S-29` |
| Tax base | The assessable income paid | `S-30` |
| Tax calculation | Rate by income category under s.40 and the applicable Ministerial Regulation / DG order | `S-28` `S-30`; rate-to-category mapping held at `P07-U-10` |
| Tax document | **Certificate in duplicate, each copy with the same contents, issued immediately every time tax is withheld** (non-employment income) | `S-31` |
| Tax accounting event | A liability to the Revenue Department arises at withholding | derived from `S-30` `S-32` |
| Journal | Not prescribed by the Revenue Code | — |
| Tax report | Return stating the tax withheld **of each person** deriving assessable income | `S-33` |
| Filing | Remit within **7 days**; PND3 for natural persons, PND53 for juristic persons | `S-32` `S-33` |

## 2. Implemented WHT Event Chain

The declared source set contains **two** withholding implementations. Both are installable
and both attach to the same payment registration point.

### 2.1 Framework A — vendor `l10n_account_withholding_tax`

| Link | Implementation |
|---|---|
| Trigger | Registration of a payment ("Allows to register withholding taxes during the payment of an invoice or bill") |
| Extension points | `account.payment`, `account.tax`, `account.payment.register`, payment receipt report |
| Thai reporting | none — it is a generic localisation framework, not bound to PND |

### 2.2 Framework B — third-party `l10n_th_withholding_tax` (SMEsPlus-refactored)

| Link | Implementation | Evidence |
|---|---|---|
| Master data | `account.withholding.tax`, synchronised from any `account.tax` flagged `wt_tax` | `models/account_withholding_tax.py`; `models/account.py:48-99` |
| Default selection | From the product (`wt_tax_id` on sales-side types, `supplier_wt_tax_id` on purchase-side types), else from the payment | `models/account_move.py:17-28` |
| Candidate filtering | By `partner_id.is_company` **and** by a case-insensitive substring test for `pnd3` / `pnd53` on the name of the **first tag of the first repartition line** | `models/account_move.py:66-83` |
| Trigger | Payment register wizard: the WHT is computed and **subtracted from the payment amount**, and the difference is handled as `reconcile` | `wizard/account_payment_register.py:38-72`, `:89-93` |
| Tax base | `wt_tax_id.amount / 100 × price_subtotal`, summed over the selected invoice lines, less WHT already posted against the same invoices | `wizard/account_payment_register.py:50-57` |
| Accounting event | A **payment-difference write-off line** carrying the WHT account and the WHT tax tags — not a tax line | `wizard/account_payment_register.py:16-26` |
| Document | `withholding.tax.cert` created by a user-initiated wizard | `l10n_th_withholding_tax_cert` |
| Report | PND3 / PND53 CSV via an override of the vendor handler; plus an independent XLSX/PDF/HTML WHT report over certificates | `models/tax_report_pnd.py`; `l10n_th_withholding_tax_report` |

## 3. The Reported Event Is Not the Withholding Event

This is the central finding of the WHT model and is stated with its full derivation.

The overridden PND query is a `UNION` of two branches over the report's date range and tag
domain (`l10n_th_withholding_tax/models/tax_report_pnd.py`):

| Branch | Rows selected | Base used | Date used |
|---|---|---|---|
| 1 (`:20-53`) | lines with a non-null `tax_line_id`, inner-joined to `account_tax` | `tax_base_amount` | the line's move date |
| 2 (`:55-92`) | lines with a non-null `wt_tax_id`, inner-joined through `account_withholding_tax` to `account_tax`, **restricted to `account_move_line.payment_id is null`** and `account_move_line__move_id.payment_state != 'not_paid'` | `price_subtotal` | the line's move date |

The withholding produced by Framework B is a **payment write-off line**. It therefore has:

- `tax_line_id` = null, so branch 1 excludes it (the join is an inner join); and
- `payment_id` populated, so branch 2 excludes it explicitly.

**Neither branch reports the line on which the tax was actually withheld and posted.**
What branch 2 reports instead is the **invoice** line that carried the withholding
default, dated by the **invoice's** accounting date, as soon as the invoice's payment
state is anything other than `not_paid`.

Consequences, each independently material:

| # | Consequence | Statutory rule contradicted |
|---|---|---|
| `W-C-01` | The PND period is driven by the invoice date, not the payment date. An invoice dated in one month and paid in the next is reported in the month **before** the withholding occurred, and never in the month it occurred. | `S-30` `S-32` `P-07` |
| `W-C-02` | `payment_state != 'not_paid'` is satisfied by `partial`, `in_payment`, `paid`, `reversed` and `blocked`. A **partial** payment therefore causes the **whole** invoice's withholding to be reported. | `S-30` |
| `W-C-03` | The reported amount is recomputed as `ABS(rate × price_subtotal / 100)` rather than read from the posted write-off line, so the filing figure and the ledger figure are two independent computations of one tax fact. | `ONE TAX FACT -> ONE ACCOUNTING EFFECT` |
| `W-C-04` | A payment made without an invoice, or a withholding entered manually as a journal entry with the correct tags, is reported by branch 1 only if it carries a real `tax_line_id`. The two ways of recording the same fact are reported by different branches with different bases. | `ONE CANONICAL TAX EVENT` |

The vendor handler that the override replaces has the same recomputation defect
(`l10n_th_reports/models/tax_report_pnd.py:46`) and, having only branch 1, reports
nothing at all for Framework B withholdings.

## 4. Classification Defects

| # | Defect | Evidence | Why it is wrong |
|---|---|---|---|
| `W-K-01` | Income type is derived from the **rate**: `CASE tax.amount WHEN -1 THEN 'Transportation' WHEN -2 THEN 'Advertising' WHEN -3 THEN 'Service' WHEN -5 THEN 'Rental' ELSE ''`. | both handlers, `:39-45` / `:74-80` | Rate is not category. The 3% rate covers several s.40 categories that file differently; every rate outside the four listed produces an empty income type, silently. |
| `W-K-02` | Condition of withholding is the literal `'1'`. | both handlers | The conditions in which the payer bears the tax cannot be expressed. Statutory code set held at `P07-U-09`. |
| `W-K-03` | PND3 vs PND53 is selected by `partner_id.is_company` plus a substring of a **translatable tag label**, read from the **first** element of two unordered collections. | `models/account_move.py:66-83` | `is_company` is a contact-structure flag, not a determination of legal personality; a contact child of a company has `is_company = False`. If the tag label is maintained in Thai, neither substring matches and the candidate list is empty. |
| `W-K-04` | The certificate model carries the full 16-value s.40 income-type selection, but the PND export does not read it. | `withholding_tax_cert.py:16-64` | The correct classification exists in the system and is not used by the statutory export. |
| `W-K-05` | The vendor handler passes a hard-coded title (`บริษัท`) for PND53; the override ignores that argument and derives the title from partner company-type master data. | `l10n_th_reports/models/tax_report_pnd.py:98` vs override `:24-26` | The override silently changes a statutory column's source; completeness now depends on master data that has no completeness control. |
| `W-K-06` | Form coverage is **provisioned inconsistently across the four layers**. See the provisioning matrix in §4.1. | `withholding_tax_cert.py:9-14`; `withholding_tax_report_wizard.py:22`; `l10n_th/data/template/account.account-th.csv:60-63`; `account.tax-th.csv` | A form can have a general-ledger account and no way to file it. |

### 4.1 Form Provisioning Matrix

Built by enumerating four layers independently. `POPULATION` = every PND form named
anywhere in the PATH SET; `PATTERN` = case-insensitive `pnd` over all file types
excluding `__pycache__`, `.po`, `.pot`; the token census returned
`pnd3` (105), `pnd53` (92), `pnd3a` (12), `pnd1` (10), `pnd 54` (1), and no `pnd2`.

| Form | GL account in the Thai chart | Tax template | PND report handler | Certificate type | Report wizard selection |
|---|---|---|---|---|---|
| PND 1 (employment) | `213300 Tax Withheld - PND 1` | none | none | `pnd1` | no |
| PND 2 (s.40(3)(4)) | none | none | none | none | no |
| PND 3 (natural persons) | `213301 Tax Withheld - PND 3` | `tax_wht_pers_{1,2,3,5}` → tag `PND3` | yes | `pnd3` | yes |
| PND 3a | none | none | none | `pnd3a` | no |
| PND 53 (juristic persons) | `213302 Tax Withheld - PND 53` | `tax_wht_co_{1,2,3,5}` → tag `PND53` | yes | `pnd53` | yes |
| PND 54 (payments abroad) | `213303 Tax Withheld - PND 54` — description: "Tax deducted from payments sent Overseas. Remit via form PND 54." | none | none | none | no |
| Income-side WHT (tax withheld **from us** by customers) | `114300 WHT Creditable` | `tax_wht_income_{1,2,3,5}` | — | — | — |

Two results follow, both material:

- `W-K-07` — **PND 54 is provisioned in the chart of accounts and nowhere else.** The
  localisation names the obligation, states the remittance form in the account
  description in both languages, and supplies no tax, no tag, no handler, no certificate
  type and no wizard entry. A posting can be made to the account; it can never be filed
  from the system. The same shape applies to PND 1 (account, certificate type, no tax and
  no handler) and to PND 3a (certificate type only).
- `W-K-08` — **The income-side withholding taxes carry no tax tags at all.** Every
  `tax_wht_income_*` template row has an empty base tag and an empty tax tag and posts to
  `114300 WHT Creditable`. Both PND handlers select on membership of the income /
  remittance / surcharge tag set, so these lines are selected by nothing. Furthermore the
  synchroniser copies the repartition tags into `account.withholding.tax.tax_tag_ids`
  (`l10n_th_withholding_tax/models/account.py:76`, `:86`), and the payment register writes
  exactly those tags onto the write-off line
  (`wizard/account_payment_register.py:22-25`); for the income side that set is empty.
  **Withholding suffered on the sales side is therefore recorded in the ledger and
  reported by no tax report in the declared source set.**

### 4.2 Why the Classification Has to Read Strings

`W-K-03` is not an isolated coding choice. All twelve WHT templates share four tax groups
named `WHT 1%`, `WHT 2%`, `WHT 3%`, `WHT 5%` (`account.tax.group-th.csv`), so the tax
group encodes only the **rate**. The only carrier of the form classification anywhere in
the data model is the **literal text of the repartition tag** — `PND3`, `PND53`,
`Income PND3`, `Income PND53`. There is no typed attribute for "which PND form does this
withholding belong to". The runtime substring test is the consequence of a missing
attribute, not merely a careless predicate; any remedy that only hardens the predicate
leaves the model defect in place.

## 5. Calculation and Currency

| # | Observation | Evidence |
|---|---|---|
| `W-M-01` | The WHT amount is computed as a float division with no explicit rounding to the currency's decimal places, then subtracted from the payment amount. | `wizard/account_payment_register.py:50-60` |
| `W-M-02` | `price_subtotal` is in the **document** currency; `self.amount` is in the **payment** currency. No conversion is applied between them. | same |
| `W-M-03` | Recomputation is suppressed after the first pass by a transient flag, so a later change of payment date or currency does not recompute the withholding. | `wizard/account_payment_register.py:28`, `:38-41`, `:70` |
| `W-M-04` | **The "less withholding already posted" subtraction cannot subtract.** The expression is `amount_wt -= sum(debit) - sum(credit)` over payment lines carrying `wt_tax_id`. On a vendor payment the withholding write-off is a **credit**, so `debit - credit` is ≤ 0 for any line subset containing it, and `-=` of a non-positive number never reduces `amount_wt`. If `wt_tax_id` lands on every line of the balanced payment entry — which `models/account_move.py:25-26` makes likely, since the compute falls through to `rec.payment_id.wt_tax_id` for **every** line of an `entry` move — the expression is exactly zero. Either way a second partial payment re-withholds the full invoice amount. An earlier draft described this loop as if it netted. | `wizard/account_payment_register.py:54-57`; corrected during independent challenge |

## 6. Two Frameworks, One Fact

| Aspect | Framework A (vendor) | Framework B (third-party) |
|---|---|---|
| Model | withholding taxes as `account.tax` extensions | a separate `account.withholding.tax` catalogue mirroring `account.tax` |
| Accounting effect | real tax lines via `_prepare_tax_lines` (`l10n_account_withholding_tax/models/account_withholding_line.py:379-385`) | payment-difference write-off |
| Own numbering | a per-withholding sequence (`account_withholding_line.py:371-372`) | none — the certificate reuses the journal entry number (`withholding_tax_cert.py:252`) |
| Thai statutory output | none | PND3 / PND53 / certificate |
| Reaches a Thai database | only by deliberate install: no `auto_install`, and the only manifests depending on it are `l10n_kh`, `l10n_ph`, `l10n_sa_withholding_tax`, `l10n_lk` and `l10n_account_withholding_tax_pos` — **no Thai module** | installed as part of the Thai extra set |

### 6.1 `P07-F-16` Restated — a Guard Exists, and It Is Worse Than None

An earlier statement of this finding said no guard prevents both frameworks from applying
to one payment. **That was wrong, and the truth is more serious.** A guard exists in the
base application:

    # We don't support to combine 'write_off_lines' and 'withholding_lines' together ...
    if withholding_lines and write_off_lines:
        write_off_lines = []
        write_off_amount_currency = 0.0
        write_off_balance = 0.0

`account/models/account_payment.py:341-345`. Both frameworks converge here: the vendor path
supplies `withholding_lines` through `_prepare_move_withholding_lines`
(`account_payment.py:283-285`, extended at
`l10n_account_withholding_tax/models/account_payment.py:102-107`), while the Thai path
arrives as `write_off_line_vals`.

So if both are active on one payment, the Thai withholding line is **silently discarded** —
while the payment amount has *already* been reduced by the Thai wizard
(`wizard/account_payment_register.py:60`). The result is a payment that is short by the
withholding amount with no corresponding withholding entry, and no error.

The corrected finding has two limbs:

- **Posting layer:** an undocumented silent-discard guard, which converts a
  double-recognition risk into a **silent under-recognition** defect. Worse than the
  absence originally reported, and of a different kind.
- **Reporting layer:** **no guard.** The vendor path produces real tax lines, so it lands in
  PND branch 1, while the same invoice can already be reported by branch 2 — genuine
  double counting in the statutory return. This limb of the original finding survives.

Mitigating the exposure: the vendor module is not auto-installed and no Thai module depends
on it, so it reaches a Thai database only by deliberate installation. `P07-F-16` is
therefore **conditional on a configuration choice**, not a defect of the shipped Thai set.
Carried into `11_P07_CONTRADICTION_REGISTER.md` in the restated form.

## 7. Provisioning and Installability of the Withholding Path

Added after independent challenge. These findings change how the rest of this file should
be read: the path analysed above is, on a fresh install of the declared source set,
**not operable at all**.

| ID | Finding | Evidence |
|---|---|---|
| `P07-F-51` | **The withholding path is inert on a fresh install.** `account.account-th.csv` has no column for the withholding-account flag, and the flag is set nowhere in the declared set except a test fixture (`l10n_th_withholding_tax/tests/account_withholding_tax_test.xml:6`) and a form default. With no account flagged: the withholding account field's domain `[('wt_account','=',True)]` is empty (`models/account_withholding_tax.py:15`), the certificate wizard's required account field has an empty domain (`create_withholding_tax_cert.py:14-20`), and ticking the withholding flag on any shipped `tax_wht_*` raises `UserError` (`models/account.py:78-81`). §2.2's "synchronised from any tax flagged `wt_tax`" is therefore conditional on a provisioning step the declared set does not perform. | `models/account.py:78-81`; `data/account.account-th.csv` |
| `P07-F-52` | The withholding wizard reads `payment.move_line_ids` (`wizard/account_payment_register.py:56`), a field defined **only** in the certificate module (`l10n_th_withholding_tax_cert/models/account_payment.py:23`), on which the withholding module does not depend (`__manifest__.py:9` = `["account", "l10n_th_reports"]`). Installing the withholding module alone raises on any payment against a line carrying a withholding tax. | `wizard/account_payment_register.py:56`; `__manifest__.py:9` |
| `P07-F-55` | Neither withholding test suite can execute. Both import `SavepointCase` from `odoo.tests.common` (`tests/test_withholding_tax.py:5`; `tests/test_wt_cert.py:7`); the declared set contains only `SavepointCaseWithUserDemo`. `test_wt_cert.py:6` imports `get_resource_path`, which has zero occurrences in the declared set. Further v13/v14 API appears throughout (`user_type_id`, `"type"` on the move, `browse_ref` called on the class). `test_withholding_tax.py:132-136` asserts an error raised by code that is commented out (`wizard/account_payment_register.py:76-86`). **There is no regression coverage for the withholding path in either direction** — nothing in the tests contradicts this file's findings, and nothing verifies them. | `tests/test_withholding_tax.py:5`; `tests/test_wt_cert.py:6-7` |
| `P07-F-57` | Latent index error: the candidate filter reads `invoice_repartition_line_ids[0].tag_ids[0].name` (`models/account_move.py:70`, `:79`) while guarding only on the union `invoice_repartition_line_ids.tag_ids`. A purchase tax tagged on the tax line but not the base line raises. Latent because the shipped Thai chart tags base lines. | `models/account_move.py:70`, `:79` |

### 7.1 The Derivation in §3 Rests on a File This Package Did Not Cite

§3 concludes that branch 2 reports the invoice line. That is only true because an
SMEsPlus-added ORM override injects the withholding tax's **base** repartition tags onto the
invoice base line: `l10n_th_withholding_tax/models/account_tax.py:7-22`
(`_add_accounting_data_to_base_line_tax_details`). The PND domain is membership of the
income / remittance / surcharge tags (`l10n_th_reports/models/tax_report_pnd.py:98`,
`:135`). Without that override the invoice line carries no matching tag and branch 2 returns
nothing.

The derivation in §3 is therefore **correct but was incompletely argued**: it omitted the
mechanism that makes its own subject reachable. Recorded because an argument that omits a
load-bearing link is not reproducible, even when its conclusion survives.

### 7.2 A Third Divergent Computation of the Same Amount

§3 `W-C-03` records two independent computations of one withholding fact. There is a
**third**: the certificate takes `abs(move_line.balance)` from the real write-off line
(`l10n_th_withholding_tax_cert/models/withholding_tax_cert.py:302-303`, selected by account
at `:309-320`). So one tax fact yields three computations drawn from two different source
lines — the ledger write-off, the recomputed PND figure, and the certificate figure. The
certificate is the only one of the three that reads the posted amount.

### 7.3 A Third Writer of Withholding Lines

`l10n_th_withholding_tax_multi` writes `wt_tax_id` and tax tags onto per-line deduction
entries (`models/account_payment.py:85-92`). Those lines carry a payment id and no tax line
id, so they are invisible to **both** PND branches for the same two reasons as the ordinary
write-off. The module is not installable from the declared set (`P07-F-20`), so this is a
latent third path rather than a live one.

## 8. Negative Claims Made in This File

| ID | Claim | Class | Boundary |
|---|---|---|---|
| `P07-N-10` | No guard preventing both withholding frameworks from applying to one payment was found. | `B — NOT FOUND IN SEARCHED SCOPE` | all Python and XML of modules 3, 7, 8, 10, 11 of `13 §5`, read in full for the WHT path |
| `P07-N-11` | No PND 54 **tax template, report handler, certificate type or wizard entry** was found, although a PND 54 **general-ledger account is present**. No PND 2 artefact of any kind was found. | PND 54: `A — VERIFIED ABSENCE WITHIN SCOPE` for the four reporting layers, `E — CONTRADICTED` for the chart layer, which does provision it. PND 2: `B — NOT FOUND IN SEARCHED SCOPE`. | PATH SET of `13 §2`; pattern `pnd` case-insensitive over all file types excluding `__pycache__`, `.po`, `.pot`; token census recorded in §4.1 |
| `P07-N-12` | No remittance-deadline or filing-period object for withholding tax was found. | `B — NOT FOUND IN SEARCHED SCOPE` | as above |
| `P07-N-13` | No mechanism implementing the month-end consolidation described in the chart (PND-specific accounts → `213500 WHT Payable`; daily WHT credits → `114401 WHT Receivable`) was traced. | `C — NOT YET SEARCHED` | The tax groups do set `tax_payable_account_id = 213500` and `tax_receivable_account_id = 114401`, so the base application's tax-closing path is the likely executor; that path was **not** examined in this session. Recorded as `P07-U-17`. |

**Note on a design that was inspected and found coherent, not defective:** the tax groups
name `213500 WHT Payable` / `114401 WHT Receivable` while the repartition lines post to
`213301` / `213302` / `114300`. This is not an inconsistency: the account descriptions
state the intended two-stage design — daily postings to form-specific accounts, month-end
consolidation to the settlement accounts. It is recorded here so that a later reviewer
does not re-raise it as a defect. What is **not** established is the executor of the
consolidation (`P07-N-13`).
