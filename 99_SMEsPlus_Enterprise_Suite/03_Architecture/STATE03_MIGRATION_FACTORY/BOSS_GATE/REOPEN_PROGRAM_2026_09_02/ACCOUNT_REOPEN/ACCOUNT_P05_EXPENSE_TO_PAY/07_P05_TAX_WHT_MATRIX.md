# 07 — P05 TAX / WHT MATRIX

`LAYER 2 — AUDIT QUARANTINE`
**Statutory notice.** No authoritative Thai Revenue Code or RD filing source was available to this
session. Every statutory assertion below is marked `HOLD / EVIDENCE REQUIRED` and routed to the
Accounting-Tax track (`12 D-05`). Mechanical facts about the code are stated separately and carry
their own class. **A mechanical fact is never presented as a statutory conclusion.**

## 1. Headline

> **Two independent, mutually unaware Thai withholding-tax subsystems are present, and they fill the
> same statutory return from different data.** The enterprise PND CSV export joins on `tax_line_id`;
> the custom stack produces WHT as a payment **write-off line**, whose `tax_line_id` is `NULL`.
> The withholding therefore appears in the PND report's on-screen totals and **disappears from the
> PND3/PND53 CSV export**, with no error raised.

## 2. The Two Subsystems

| | Subsystem A — enterprise | Subsystem B — custom / OCA |
|---|---|---|
| Module | `ENT18/addons/l10n_th_reports` (`auto_install: True`, depends `l10n_th` + `account_reports`) | `CUSTOM/l10n_th_withholding_tax` (+ `_multi`, `_cert`, `_cert_form`, `_report`) |
| On-screen report | `engine=tax_tags` — sums move lines **by tag** (`ENT18/l10n_th/data/account_tax_report_data.xml:192, 203, 214, 250, 261, 272`) | its own PDF/TXT/XLSX reports |
| CSV export | `models/tax_report_pnd.py:29-64` — `JOIN account_tax tax ON tax.id = account_move_line.tax_line_id`, deriving `wht_amount` from `tax.amount × tax_base_amount / 100` | n/a |
| Branch identifier | `partner.company_registry` (`tax_report_pnd.py:41`) | `partner.branch` |
| WHT line produced | a genuine tax line | a payment **write-off line** — `tax_line_id` is `NULL` |

The custom write-off line **does** carry the matching `tax_tag_ids` (planted at
`CUSTOM/l10n_th_withholding_tax/wizard/account_payment_register.py:21-25`, sourced from
`models/account.py:53`). That is why it reaches the tag-based grid and not the join-based export.

> **`TX-01` FACT VERIFIED (mechanical), severity HIGH.** The divergence is verified from source by
> AAS-03 Expert 4. **Its statutory consequence is `HOLD / EVIDENCE REQUIRED`** — this package does not
> assert what the Revenue Department requires, only that two implementations of the same return
> disagree on their data source and on their branch field.

## 3. WHT Lifecycle Chain — Subsystem B

| Stage | Mechanism | Citation |
|---|---|---|
| **Configure (1)** | `account.withholding.tax`: name, `account_id` (domain `wt_account=True`, `ondelete=restrict`), `type` (sale/purchase/none), `amount` (percent, plain Float), `tax_tag_ids`, `tax_id`, `active`, `company_id` (required) | `models/account_withholding_tax.py:7-32` |
| **Configure (2)** | Auto-derived from `account.tax` by `update_wt()`, called from `create` and from **every** `write` | `models/account.py:27-36, 38-64` |
| **Default per product** | `wt_tax_id` / `supplier_wt_tax_id` on the product template | `models/product.py:9-10` |
| **Carried on the bill** | `account.move.line.wt_tax_id`, computed from the product, `store=True, readonly=False`. **No GL line is produced when the bill posts.** | `models/account_move.py:23-42` |
| **Recognised** | **At payment registration only.** The payment amount is reduced by `Σ(rate/100 × price_subtotal)` less amounts already withheld, and the shortfall becomes a write-off line | `wizard/account_payment_register.py:38-72`; core `ENT18/account/wizard/account_payment_register.py:1018-1024` |
| **GL account** | `writeoff_account_id = wt_tax_id.account_id` — the account flagged `wt_account=True` | `wizard/account_payment_register.py:66`; `models/account.py:11-15` |
| **Certificate** | `create.withholding.tax.cert` wizard → `withholding.tax.cert._compute_wt_cert_data` picks the payment's move lines on a WT account and builds cert lines. **The base is reverse-derived from the tax amount** (`base = abs(balance)/wt_percent*100`), never read from `price_subtotal` | `l10n_th_withholding_tax_cert/wizard/create_withholding_tax_cert.py:60-108`; `models/withholding_tax_cert.py:206-245, 247-266, 268-280` |
| **Report** | Wizard → PDF/TXT via `_compute_results`; XLSX by a **separate inline path with a different domain** | `l10n_th_withholding_tax_report/models/report_withholding_tax.py:150-161`; `wizard/withholding_tax_report_wizard.py:66-224` |
| **Partial payment** | Already-withheld amounts are subtracted by walking `matched_payment_ids` | `wizard/account_payment_register.py:54-57` |
| **Reversal / cancellation** | **No hook exists.** | `21 NC-14`, class **A** |
| **Multi-tax bill** | `_multi` forces `reconcile_multi_deduct` and builds one `account.payment.deduction` per WHT line | `l10n_th_withholding_tax_multi/models/account_payment.py:11-25, 37-92` |

## 4. Reachability From the Expense Path

| Branch | WHT reachable? | Evidence |
|---|---|---|
| `own_account` (employee-paid) | **YES.** `action_register_payment` → `line_ids.action_register_payment()` sets `active_model='account.move.line'`; the bill is `move_type='in_invoice'` (`hr_expense_sheet.py:833`), so `_compute_wt_tax_id` takes the `in_invoice` branch and reads `product_id.supplier_wt_tax_id`. If the expense product carries that field, WHT applies — and every defect in §5 applies with it. | Expert 4 §4 |
| `company_account` | **NO.** That branch creates the entry and the payment directly inside `_do_create_moves`; there is no payment-register step, so nothing can attach a WHT write-off. `grep -rn "wt_tax\|withhold"` over `ENT18/addons/hr_expense` → 0 hits, class **A**. | Expert 4 §4; `21 NC-13` |
| Advance disbursement | **NO.** `tax_ids` is explicitly `[]`. | `advance_expense_request.py:255` |

> **`TX-02` FACT VERIFIED, severity HIGH.** WHT applicability is a function of the **payment-mode
> toggle**, not of the payee. A withholdable payment to a third party routed as a company-paid expense
> (a `vendor_id`-carrying line, `04 §4`) can never withhold; the same cost routed `own_account` can.

## 5. Defect Register — Subsystem B

| ID | Severity | Defect | Evidence |
|---|---|---|---|
| `TX-03` | **HIGH** | **Changing the payment date silently drops the entire withholding tax.** `amount_wt_computed` latches, and the latched branch returns `super()._compute_amount()`, which **restores the full gross residual**. `payment_difference` then rounds to ~0, so `_create_payment_vals_from_wizard` appends **no write-off line**. Full gross is paid, no WHT journal line exists, and there is nothing for a certificate to be built from. *The primary research called this a caching nuisance; Expert 4 established it is a settlement-integrity defect.* | `wizard/account_payment_register.py:28, 39-41, 70`; core `ENT18/account/wizard/account_payment_register.py:722-729, 691-699, 812-823, 985, 1002-1024` |
| `TX-04` | **HIGH** | **Companion defect, opposite direction.** On a manual downward amount edit, `custom_user_amount` stops the recompute but `wt_tax_id` remains set, so `payment_difference_handling` stays `'reconcile'` and `writeoff_account_id` stays the **WHT account**. Core then writes the *entire* payment difference — the unpaid **principal** — to the withholding-tax GL account. `grep -n "payment_difference"` over that file → **0 occurrences**; nothing checks that the difference equals the computed WHT. Class **A**. | same file; `21 NC-16` |
| `TX-05` | **HIGH** | **Installing `l10n_th_withholding_tax_multi` breaks the single-WHT case.** `models/account_payment.py:11-25` calls `super()._compute_payment_difference_handling()` (which sets `'reconcile'`) and then **unconditionally overwrites** it at `:19-22` with `'reconcile' if early_payment_discount_mode else 'open'`; the `'reconcile_multi_deduct'` rescue at `:23-25` fires only when there is **more than one** WHT tax. For exactly one, the field lands on `'open'` and core skips the write-off — while `self.amount` has **already** been reduced by the WHT. Net: vendor underpaid, bill left partially open, **no WHT line and therefore no certificate source**. | `l10n_th_withholding_tax_multi/models/account_payment.py:11-25`; base `wizard/account_payment_register.py:60, 89-93` |
| `TX-06` | **HIGH** | **Multi-tax WHT is UI-only.** `_update_vals_multi_deduction` is reachable only from an `@api.onchange` (`account_payment_multi_deduction/wizard/account_payment_register.py:51-63`). Any programmatic payment creation — import, API, scheduled job, another module — never fires it, so `deduction_ids` stays empty and `_check_deduction_amount` raises. | `:51-63, 65-80` |
| `TX-07` | MEDIUM | `UnboundLocalError` in a stored-field compute: `lines` is bound only inside `if/elif` on `active_model`, then read unconditionally. And `payment_vals["write_off_line_vals"][0]` is indexed unconditionally where core can leave that list empty → `IndexError`. | `l10n_th_withholding_tax_multi/models/account_payment.py:14-17, 23`; `account_payment_multi_deduction/wizard/account_payment_register.py:96-98` |
| `TX-08` | **HIGH** | **`wht_amount` is corrupted across a recompute batch, and it drives a printed settlement document.** `self.wht_amount = amount_wt` inside `for rec in self` writes the **last** record's value to **every** record in the batch — confirmed against the ORM: `Field.compute_value` protects the whole batch and `Field.__set__` then performs a pure cache write across all protected records, with no `ensure_one` and no exception. The field is `store=True`, so the wrong value is **persisted**. It is then read three times by the vendor remittance advice to compute the **net amount printed**. | `models/account_move.py:48, 50-58`; `ENT18/fields.py:1382-1398, 1440-1487`; `print_payment_remittance_adviec/report/print_payment_remittance_report/body.xml:184, 187, 207` |
| `TX-09` | MEDIUM | `wht_amount` has **no currency field** and is computed from `price_subtotal` (invoice currency). The remittance advice's running total (`body.xml:187`) sums it across invoices of potentially different currencies into one printed figure. It is also the **whole-invoice** WHT, not the amount withheld on *this* payment — so on a partial settlement the advice, the GL and the certificate are three unreconciled numbers. | as cited |
| `TX-10` | **HIGH** | **The receipt move types are inverted, and the inversion is operative.** `_compute_wt_tax_id:35` groups `in_receipt` with the sale-side fields; `:37` groups `out_receipt` with the supplier-side fields. Core is unambiguous: `in_receipt` = "Purchase Receipt", `out_receipt` = "Sales Receipt" (`ENT18/account/models/account_move.py:157-174`), corroborated by `get_purchase_types`/`get_sale_types` (`:5537-5542`), `get_outbound_types`/`get_inbound_types` (`:5551-5556`) and `TYPE_REVERSE_MAP` (`:63-72`). **There is no reason it is written that way.** | as cited |
| `TX-11` | MEDIUM | **The contradiction is wired into one widget.** `views/account_move_view.xml:11-12, 18-19` binds `wt_tax_id`'s domain to `wt_tax_ids`, which `get_wt_domain` classifies **correctly** (`:13-16`) while `_compute_wt_tax_id` supplies the default **incorrectly**. On an `in_receipt` the computed default can therefore be outside its own domain — and Odoo domains are client-side, so the out-of-domain default is **stored, not rejected**. Provenance: the inversion is in the git **baseline**; `get_wt_domain` is a **local uncommitted addition**. The contradiction was introduced by the local edit. | Expert 4 §1 |
| `TX-12` | **HIGH** | **No reversal or cancellation hook exists in any WHT module.** Declared boundary: the six WHT/deduction modules; pattern `grep -rn "def action_draft\|def action_cancel\|def button_cancel\|def button_draft\|_reverse_moves\|def unlink\|def action_reverse" --include='*.py'` → only the certificate's own buttons. Class **A**. Core `account.payment.action_cancel`/`action_draft` therefore proceed unguarded on a payment whose certificate is `done`; only `unlink` is blocked, by `ondelete="restrict"`. A `done` — potentially already-filed — certificate can outlive a cancelled WHT journal line, with `ref_move_line_id` silently dangling. | `21 NC-14`; `withholding_tax_cert.py:110, 282, 296, 340-345` |
| `TX-13` | **HIGH** | **Duplicate certificates for one payment are creatable.** The "one certificate" control is a Many2one `domain` — client-side only — and the creation wizard sets the value through **context**, bypassing it, with no check for an existing non-cancelled certificate. `wt_cert_cancel` is used **nowhere** as a constraint or cancellation guard (11 hits, all definition/compute/domain/`invisible="1"`), class **A**. Combined with `TX-12`, a payment can carry N `done` certificates and then be cancelled with all of them standing. | `withholding_tax_cert.py:108-109, 123-124`; `wizard/create_withholding_tax_cert.py:88`; `21 NC-15` |
| `TX-14` | **HIGH** | **A stored compute writes non-computed fields as a side effect, destroying the PND classification.** `_compute_wt_cert_data` is `@api.depends("payment_id","move_id")` but also assigns `ref_wt_cert_id`, `income_tax_form` and `wt_line` — none computed — so `Field.__set__` takes the unprotected branch and issues a **real `write()` inside a compute**. Their source is the **context**, which is empty outside the creation wizard. Any recompute (a `payment_id`/`move_id` write, or a forced recompute at upgrade) resets `income_tax_form` to `False`, clears `ref_wt_cert_id` and rebuilds `wt_line` — destroying the form classification and the substitution chain that `action_done` depends on. | `withholding_tax_cert.py:206-245, 286-294`; `ENT18/fields.py:1382-1417` |
| `TX-15` | MEDIUM | **The XLSX report ignores the company filter the PDF/TXT report applies.** The XLSX domain omits `company_partner_id`, which the PDF/TXT domain includes; the record rule only limits to *allowed* companies. Two exports of "the same" statutory report return different populations. Same method can raise `AttributeError` on a certificate with no date. The module also carries **two different filename codes for one form** (`pnd3 → "PND03"` vs `pnd3 → "P03"`), and offers only `pnd3`/`pnd53` while the certificate supports `pnd1`/`pnd3a` — certificates on those forms are unreportable and would `KeyError`. | `wizard/withholding_tax_report_wizard.py:12, 14, 22, 66, 162, 179, 209-215, 227`; `models/report_withholding_tax.py:9, 110-112, 154-160` |
| `TX-16` | MEDIUM | **Cancelled certificates are emitted into the statutory text and XLSX files as blanked rows** — both domains filter `state != 'draft'`, so cancelled rows are included, and `_create_text` blanks name/address/base/amount while still emitting the sequence number, VAT, rate and date. Whether that matches the RD's void-row convention: `HOLD / EVIDENCE REQUIRED`. Adjacent verified defect: `text = ""` is reset **inside** the document loop while `return text` sits outside — only the last document's text is returned, and `NameError` if the set is empty. | `models/report_withholding_tax.py:36-83, 159`; `wizard/…:162` |
| `TX-17` | MEDIUM | **`update_wt` mis-assigns company and can duplicate WHT records across companies.** It searches with **no company domain**, so the global rule filters to *allowed* companies and a record belonging to a company outside that set is invisible — and a **second** record is created for the same tax. `l_vals` **never copies `rec.company_id`**, so the new record inherits the *acting user's* company, not the tax's. It also raises `UserError` from inside `account.tax.write()`, so **any** write to a `wt_tax`-flagged tax whose repartition account lacks `wt_account` fails, including writes from unrelated flows. *This is why the ACL and company rule being present (`P05-F-30`) is true but insufficient — the rule is what creates the duplicate.* | `models/account.py:38-64, 48-49, 60, 62, 69` |
| `TX-18` | MEDIUM | `self.show_payment_difference = True` is **discarded** — the field is a non-stored compute with no inverse, so the write is dropped. Visibility is governed entirely by core, which additionally requires `payment_method_line_id.payment_account_id`. Where the outstanding-payments account is unconfigured, **the amount is silently reduced by the WHT while the difference section stays hidden.** | `wizard/account_payment_register.py:62`; `ENT18/account/wizard/account_payment_register.py:152, 311-318`; `ENT18/fields.py:1414-1417` |
| `TX-19` | MEDIUM | **Two report hooks are dead.** `report.withholding_tax_pdf` never resolves, because `ir.actions.report` looks up `report.%s % report_name` and `report_name` is the fully-qualified `l10n_th_withholding_tax_cert_form.withholding_tax_pdf`. And `render_qweb_text` overrides a method core does not have (core defines `_render_qweb_text`), so the PND text file's `.strip()` and entity-conversion cleanup **never runs** and the exported file retains qweb-escaped entities and surrounding whitespace. Statutory acceptability: `HOLD / EVIDENCE REQUIRED`. | `l10n_th_withholding_tax_cert_form/reports/withholding_report_pdf.py:8, 13-15`; `ENT18/base/models/ir_actions_report.py:1076, 1094`; `l10n_th_withholding_tax_report/models/ir_actions_report.py:22-30, 33-42` |
| `TX-20` | MEDIUM | **Seven certificate fields are permanently locked while the views present them as editable in draft.** Eight `states=` declarations were commented out with **no `readonly=False`** added in their place; the views still declare `readonly="state!='draft'"`. Code defect class **A**; rendered UI outcome class **D** (not executed). Related: `payment_date` is a **local** addition defaulting to `context_today`, and the certificate `date` is set from it — so the certificate is dated **today**, not the payment's own date. Whether the certificate date drives the filing period: `HOLD / EVIDENCE REQUIRED`. | `withholding_tax_cert.py:78, 87, 107, 114-115, 122, 142, 171, 178, 187, 237`; `views/withholding_tax_cert.xml:38, 42, 52, 58, 59, 68, 73` |
| `TX-21` | MEDIUM | **The remittance-advice module loads none of its Python and omits the dependency supplying the field it prints.** Both imports in `__init__.py` are commented out; the AbstractModel's `_name` belongs to a *different* module (copy-paste). The manifest declares `depends: ['account']` while the template reads `inv.wht_amount`, defined in `l10n_th_withholding_tax` — **a missing dependency**, so load order is not guaranteed and the report fails outright without that module. | `print_payment_remittance_adviec/module/__init__.py:3-4`; `module/report_designer.py:8-9`; `__manifest__.py:12`; `report/.../body.xml:184, 187, 207` |
| `TX-22` | LOW-MED | `full_payment_custom` adds `is_report_designer` to **`account.payment`** rather than `ir.actions.report` (the class is named `IrActionsReport` but `_inherit = 'account.payment'`). The payment voucher prints **gross with no withholding disclosure** — `grep -nEi "wt_tax\|wht\|withhold"` over that module's reports → 0 hits, class **A**. | `full_payment_custom/module/ir_action_report.py:6-8, 7, 12`; `21 NC-17` |
| `TX-23` | LOW | Local edits left three shadow copies of report source in-tree (`… copy.py` with a space in the filename, `.py_bkp`, `_backup.py`, plus two `… copy.js`), dropped the report context (`context` assigned and never used), and commented out the XLSX AbstractModel's import while an `ir.actions.report` record still points at it. The visible Export XLSX button does **not** use it — verified, not assumed — so this is dead configuration, not a broken button. | `l10n_th_withholding_tax_report`, git diff; `report/__init__.py:2`; `models/report_withholding_tax.py:116-117, 122, 127`; `data/report_data.xml:37-46` |

## 6. Non-Deductible / Disallowed Expense

Declared search: `grep -rlEi 'disallowed' <root> --include='*.py' --include='*.xml' --include='*.csv'`
over `ENT18/addons`, `ENT18/addons_archive`, `CUSTOM`.

| Question | Answer | Class |
|---|---|---|
| Model | `account.disallowed.expenses.category` (name, globally-`UNIQUE` code, company, accounts, current rate) and `account.disallowed.expenses.rate` (rate, `date_from`, category, company) | FACT VERIFIED |
| Percentage mechanism | Time-sliced by `date_from`, latest-effective-wins, via raw SQL `first_value(rate) OVER (PARTITION BY category_id ORDER BY date_from DESC) WHERE date_from < CURRENT_DATE` | FACT VERIFIED |
| Attachment point | `account.account.disallowed_expenses_category_id` (`check_company=True`); an **onchange** clears it for non-income/expense groups — so programmatic writes are unguarded | FACT VERIFIED |
| **Does it touch the GL?** | **No. It is report-only.** The handler inherits `account.report.custom.handler` and performs a read-only SQL aggregation `SUM(aml.balance * rate.rate) / 100`. `grep -n "def create\|def write\|def _post\|account.move.line'].create\|_prepare_.*_line"` over the module → no write path to any journal. **It posts nothing, adjusts nothing and blocks nothing.** | Class **A** |
| **Any connection to the expense path?** | **None.** `grep -rn "disallowed"` over `ENT18/addons/hr_expense` and `hr_expense_extract` → 0 hits. | Class **A** |
| Extension family | `account_disallowed_expenses_fleet`, `l10n_be_disallowed_expenses`, `l10n_be_account_disallowed_expenses_fleet` (+2 `__dup_` copies) exist **only in `addons_archive`** — Belgian and fleet-oriented, none Thai, none expense-report-oriented | Class **B** |
| In `CUSTOM` | 0 files | Class **B** — spellings `non_deductible`, `add_back` and Thai-language tokens **not searched**, class **C** for those |

> **`TX-24`** There is **no non-deductible-expense treatment anywhere in the expense-to-pay path.**
> The module provides a *reporting* percentage by GL account and is unconnected to `hr.expense`, to WHT
> and to the ledger. Whether a Thai add-back obligation requires more: `HOLD / EVIDENCE REQUIRED`.

## 7. VAT / Recoverable Tax

| Fact | Evidence | Class |
|---|---|---|
| Purchase taxes on an expense line are **always** forced price-included, in both the tax-detail path and the totals computation. A price-excluded VAT configuration is silently reinterpreted. | `hr_expense/models/account_move.py:78-83`; `account_move_line.py:24-27`; the field help says so openly at `hr_expense.py:198` | FACT VERIFIED |
| Cash-basis tax tags are included only on the company-paid branch | `hr_expense.py:906` (`include_caba_tags=self.payment_mode == 'company_account'`) | FACT VERIFIED |
| The advance disbursement strips all taxes | `advance_expense_request.py:255` | FACT VERIFIED |

## 8. What SMEsPlus Must Decide

| ID | Decision |
|---|---|
| `BD-05` | Which WHT subsystem is authoritative? Both are present; they disagree on data source and branch field (`TX-01`). |
| `BD-06` | Must WHT be recognised at bill posting (as an accrued withholding liability) rather than only at payment? The reference recognises nothing until settlement. |
| `BD-07` | Must WHT applicability follow the **payee**, not the payment-mode toggle (`TX-02`)? |
| `BD-08` | Is a non-deductible / add-back mechanism in scope for SMEsPlus, given the reference supplies only a report (`TX-24`)? |
