# P06_CUSTOM_MODULE_DELTA.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Supplementary deliverable** — not on the original required list; produced because the custom-module evidence is material to P06 and would otherwise be distributed and lost.

**STANDING QUALIFICATION, APPLIES TO EVERY ROW:** four custom copies exist and **which is deployed is unknown to this session**. Version strings are reported per copy. Nothing here asserts deployed behaviour.

---

## 1. Copy denominator

**POPULATION:** the 18 modules in the P06 custom scope. **PATTERN:** existence of `<root>/<module>/__manifest__.py`, then the `version` line. **PATH SET, four roots with their depth-1 directory counts:**
- `CUST18` = `.../Odoo18/EXTRA MODULE/smeplus-custom/addons` — **65** modules
- `CUST14` = `.../Odoo14/addons` — **127** modules
- `T8MASTER` = `.../Odoo18/t8master/custom/addons` — **57** modules
- `MIGR18` = `.../CLAUDE AI/MIGRATION/ODOO18/18.0.4_smeplus_v2/addons` — **47** modules

**UNIT:** module directory per copy. `—` = NOT FOUND under that root.

| Module | CUST18 | CUST14 | T8MASTER | MIGR18 |
|---|---|---|---|---|
| account_payment_multi_deduction | 18.0.1.0.2 | 14.0.1.1.0 | 18.0.1.0.2 | — |
| full_payment_custom | **1.8** | — | **1.8** | — |
| dev_print_cheque | 18.0.1.3 | 14.0.1.0 | 18.0.1.3 | 18.0.1.3 |
| print_payment_remittance_adviec | 18.0.1.1 | 1.0.0 | 18.0.1.1 | 18.0.1.1 |
| scgl_purchase_advance_payment | **1.0.0** | — | **1.0.0** | **1.0.0** |
| hr_expense_petty_cash | 18.0.1.2 | 1.0.1 | 18.0.1.2 | 18.0.1.2 |
| cr_effective_date_entries | 18.0.0.0 | — | 18.0.0.0 | — |
| scgl_tax_period_date | 18.0.1.0 | — | 18.0.1.0 | 18.0.1.0 |
| automatic_invoice_and_post | 18.0.1.0.1 | — | — | — |
| cap_auto_invoice | 18.0 | — | — | — |
| l10n_th_withholding_tax | 18.0.1.4 | 14.0.1.0.1 | 18.0.1.4 | 18.0.1.4 |
| l10n_th_withholding_tax_multi | 18.0.1.0.2 | 1.0.0 | 18.0.1.0.2 | — |
| **cheque_control** | — | 1.0.1 | — | — |
| **post_dated_cheque_mgt_app** | — | 1.0.1 | — | — |
| **pdc_generate_cheque_reference** | — | 1.0.2 | — | — |
| **account_payment_return** | — | 14.0.1.0.4 | — | — |
| **om_account_bank_statement_import** | — | 14.0.3.0.0 | — | — |
| hr_expense_petty_cash_sequence | — | 1.0.0 | — | **18.0.1.0.2** |

**CMD-F-01 — The four copies are byte-identical at the Python layer for every in-scope module present in more than one.**
PATTERN `diff -rq` filtered to `.py`, for the 10 modules in both CUST18 and T8MASTER and the 6 in both CUST18 and MIGR18: **zero differing `.py` files.**
**Consequence: a code fingerprint cannot discriminate which copy is deployed.** The only discriminators are set membership — `automatic_invoice_and_post`, `cap_auto_invoice`, `account_payment_multi_deduction`, `l10n_th_withholding_tax_multi`, `cr_effective_date_entries` and `full_payment_custom` are absent from MIGR18; `hr_expense_petty_cash_sequence` is absent from CUST18 and T8MASTER.

**CMD-F-02 — Two modules carry no v18-prefixed version string in any copy** (`full_payment_custom` at `1.8`, `scgl_purchase_advance_payment` at `1.0.0`). Whether that reflects an un-versioned port or an unmigrated file is undetermined — no VCS history under the evidence roots.

---

## 2. Modules that alter payment state, posting or reconciliation

**CMD-F-03 — `account_payment_multi_deduction` suppresses move synchronisation.**
`$CUST18/account_payment_multi_deduction/models/account_payment.py:55-58` and `:64-66`:
```
if any(rec.is_multi_deduction for rec in self):
    self = self.with_context(skip_account_move_synchronization=True)
```
in both `_synchronize_from_moves` and `write`. It feeds `write_off_line_vals` (`wizard/account_payment_register.py:104-108`) and adds a `payment_difference_handling` value `reconcile_multi_deduct` (`:13-18`).
Signature compatibility with the v18 core `_prepare_move_line_default_vals(self, write_off_line_vals=None, force_balance=None)` (`$V18E/account/models/account_payment.py:293`) is **confirmed present**, including `force_balance`.
**Assessment:** this is the deliberate mechanism for Thai multi-deduction settlement (WHT plus other deductions on one payment). Turning off move synchronisation is a defensible way to protect hand-built write-off lines from PSM-F-25's rewrite — but it means those payments are **outside** the synchronisation invariant the rest of the system relies on.

**CMD-F-04 — `hr_expense_petty_cash` writes payment state directly and gates posting.**
`$CUST18/hr_expense_petty_cash/models/hr_expense_sheet.py:117` — `payment.write({'move_id': move.id, 'state': 'in_process'})` — a direct state write, bypassing the action API (PSM-R-06 violation in the reference itself, since `state` is `readonly=False`).
`models/account_move.py:18-20` overrides `action_post` with `self._check_petty_cash_amount()`, plus an `@api.constrains` at `:22`.
Journal-item account and partner are rewritten at `models/hr_expense.py:76-77`.

**CMD-F-05 — `hr_expense_petty_cash` contains a duplicated, divergent, dead override.**
Two files in the same module both declare `_inherit = "account.move"` with an identically-signed `action_post` and an identical `is_petty_cash` field: `models/account_move.py:10-20` and `models/account_invoice.py:10-20`.
**Only one is imported** — `models/__init__.py:4-7` imports `account_move`, `hr_expense`, `hr_expense_sheet`, `petty_cash`; **`account_invoice` is absent.** So `account_invoice.py` is dead code in this copy (identical across all three v18 copies).
And the two versions **differ behaviourally**: `account_move.py:24` uses `self.env["petty.cash"].sudo()`, `account_invoice.py:24` does not; `account_invoice.py:113-114` clears `line_ids`/`invoice_line_ids` in the onchange where `account_move.py:115` has those lines commented out.
**Classification: CONFIRMED DEFECT — dead code carrying divergent behaviour.** A future `__init__` edit changes system behaviour without any code change. `P06-B-36`.

**CMD-F-06 — `cr_effective_date_entries` unposts, renames and reposts journal entries, and writes valuation records by raw SQL.**
`$CUST18/cr_effective_date_entries/wizard/effective_date.py:63-68`:
```
for acc_mv in accmoveObj if not invoice_ids else invoice_ids.ids:
    acc_mv.button_draft()
    acc_mv.name = False
    acc_mv.date = self.date
```
then `acc_mv.action_post()` at `:68`.
**`acc_mv.name = False` discards the existing sequence number before reposting.** The accounting date is forced to a user-entered wizard value (`:19`, defaulting to now) with **no period or lock validation inside this module**.
And `:76-77` bypasses the ORM entirely on valuation records:
```
self.env.cr.execute('update stock_valuation_layer set create_date=%s where id=%s', (self.date, val.id))
```
It also back-dates sale (`:46`) and purchase (`:55-56`) orders. A residual debug artifact remains at `:24` (`print('active_ids',active_ids)`).
**Exposure:** three `ir.actions.server` bindings on stock picking, sale order and purchase order (`views/effective_date_action.xml:6,18,30`), each gated on a single hidden group (`security/security.xml:3-6`). **There is no binding on `account.move` directly** — NOT FOUND in that view file.
**Assessment for P06.** `button_draft()` on a reconciled entry calls `remove_move_reconcile()` (attack A5), so **this module can silently destroy bank reconciliations as a side effect of an effective-date correction.** The lock-date protection that the reference attaches to the state write (`$V18E/account/models/account_move.py:3238-3241`) does fire within the same transaction, but the sequence-number clearing is not protected by it.
**Classification: CONFIRMED DEFECT for P06 reliance** — a module that resequences and re-dates posted entries is incompatible with any bank-reconciliation control that assumes entry immutability. `P06-B-37`.
**Scope note (CORR1):** the objects it mutates are COMPANY-scoped accounting truth; the group gating it is a hidden `res.groups` with no implied groups. This is a COMPANY-scope mutation control that is effectively a single checkbox on a user.

**CMD-F-07 — Two auto-posting modules create and post invoices on non-accounting triggers.**
`$CUST18/automatic_invoice_and_post/models/stock_picking.py:33,45,56-60` — posts an invoice on **delivery validation**.
`$CUST18/cap_auto_invoice/models/sale_order.py:9,13,20-22` — posts an invoice on **sale-order confirmation**.
Two concrete hazards, both quoted:
- **`automatic_invoice_and_post`**: the gate at `:51` is `if auto_validate_invoice:` on the raw result of `ir.config_parameter.get_param(...)` (`:46-48`). `get_param` returns a **string**, and the string `"False"` is truthy in Python. **NOT FOUND: any `in ('True','1')` normalisation anywhere in the module.** The disjunct at `:53` (`or not self.sale_id.invoice_ids`) also fires when the picking has no linked SO invoices at all.
- **`cap_auto_invoice`**: `action_confirm` is a multi-record method, but the body reads `self.require_payment` and `self.order_line` without `ensure_one()` (`:15`), and `int(inv.get('res_id'))` (`:21`) assumes a single returned invoice. **`ensure_one` NOT FOUND in the module.** No idempotency guard against an existing invoice — PATTERN `invoice_ids|invoice_status|invoice_count` over `models/sale_order.py`: **0 hits.**
**Assessment for P06:** these are the upstream half of the duplicate-posting attack surface. They increase the population of posted invoices that P06 must then settle, and neither carries an idempotency guard. `P06-B-38`.

**CMD-F-08 — `scgl_tax_period_date` overrides `create` with the wrong decorator.**
`$CUST18/scgl_tax_period_date/models/tax_period.py:9-15` uses `@api.model` on an `account.move` `create` override, while the v18 core declares `@api.model_create_multi` (`$V18E/account/models/account_move.py:3183-3184`). It then writes `tax_period_date` onto tax lines inside `create` (`:12-14`).
**Recorded as an evidenced incompatibility, not adjudicated** — whether the ORM tolerates it in practice was not tested. `P06-OQ-70`, Class D.

**CMD-F-09 — The Thai withholding-tax modules mutate the settlement amount directly.**
`$CUST18/l10n_th_withholding_tax/wizard/account_payment_register.py:60` — `self.amount -= amount_wt`, computed at `:50-52` from `wt_tax_id.amount / 100 * price_subtotal`.
It carries its **own** double-payment guard on the WHT portion (`:54-57`), netting off already-posted WHT from prior payments, and an idempotency latch (`amount_wt_computed`, `:28,39-41,70`). It forces `payment_difference_handling = 'reconcile'` (`:89-93`).
`l10n_th_withholding_tax_multi` joins it to `account_payment_multi_deduction` (`__manifest__.py:11`) and builds per-line deductions (`models/account_payment.py:37,53-54,72-81`), blocking manual line entry (`:110`).
**Three code-quality observations, recorded as evidence:**
- `models/account_move.py:22` — `Many2many("account.withholding.tax", 'WT Tax ids', ...)`: the second positional argument of `Many2many` is `relation`, not a label.
- `models/account_move.py:52-57` — `_compute_wht_amount` assigns to the recordset (`self.wht_amount = ...`) inside a `for rec in self:` loop.
- `wizard/account_payment_register.py:74-87` — a `default_get` override whose entire body except the `super()` call is commented out; the disabled block (`:80-86`) would have blocked multi-move registration when WHT is present. **That guard is currently inert.**
- `l10n_th_withholding_tax_multi/models/account_payment.py:14-17,23` — `lines` is assigned only inside `if`/`elif` on `active_model` and referenced unbound at `:23` if neither branch is taken.
**Statutory correctness of Thai WHT is explicitly NOT adjudicated here — HOLD / EVIDENCE REQUIRED, routed to the Accounting-Tax track.** What is adjudicated is that these modules **change the amount that settles**, which places them squarely inside P06's boundary. `P06-B-13`.

**CMD-F-10 — `full_payment_custom` declares a report class that inherits `account.payment`.**
`$CUST18/full_payment_custom/module/ir_action_report.py:6-8` — a class named `IrActionsReport` with `_inherit = 'account.payment'`, adding `is_report_designer` (`:8`). The sibling module `print_payment_remittance_adviec` declares the same class name with `_inherit = 'ir.actions.report'` (`module/ir_action_report.py:7-8`).
**The `is_report_designer` flag therefore lands on `account.payment` in one module and on `ir.actions.report` in the other.** Recorded as evidence. Neither module alters payment state, posting, reconciliation or the bank statement — PATTERN `def action_post|def action_draft|def action_cancel|reconcile|'state'|account\.bank\.statement` over both modules' `.py`: **0 hits.**

**CMD-F-11 — `dev_print_cheque` writes only module-added cheque metadata.**
`$CUST18/dev_print_cheque/wizard/dev_print_cheque_wizard.py:76-81` writes `cheque_no` and related fields onto the payment. PATTERN as above over its 8 `.py` files: **0 hits.** It adds a free-text `cheque_no` with **no state machine** — which is why the v14 `cheque_control` module existed on top of it.

---

## 3. The v14→v18 treasury regression

**CMD-F-12 — Five treasury modules present in v14 have no v18 counterpart.**
**DENOMINATOR:** PATH SET the three v18 custom roots (169 module directories total). **PATTERN A (directory):** `-iname "*cheque*" -o -iname "*check*" -o -iname "*pdc*" -o -iname "*payment_return*" -o -iname "*bank_statement*" -o -iname "*petty_cash*"` — hits only `dev_print_cheque`, `hr_expense_petty_cash`, `hr_expense_petty_cash_sequence`. **PATTERN B (model names, to catch renamed ports):** `grep -rln --include="*.py" "cheque\.code\|cheque\.generate\|pdc\.code\|account\.pdc\.payment\|payment\.return\|account\.bank\.statement\.import"` — **zero files in all three roots.**
**Class A within that declared scope.** The negative is pattern-bounded on model names, not on directory names alone — this is the specific control the enumeration-pattern-boundedness lesson requires.

| v14 module | What it did | v18 status |
|---|---|---|
| `cheque_control` | cheque-number lifecycle (`new`/`post`/`cancel`), hooking `action_post` and `action_cancel`, releasing the number after posting (`models/account_payment.py:10-31`) | **not migrated** |
| `post_dated_cheque_mgt_app` | a full parallel PDC payment engine — 16 `.py` files, delegated model, 6 wizards, states `draft/cancelled/returned/bounced/deposited/collect_cash`, and it redefines what "fully paid" means on `account.move` (`models/account_move.py:31-35`) | **not migrated** |
| `pdc_generate_cheque_reference` | PDC reference register with a duplicate guard (`models/pdc_inherit_register.py:26-33`) | **not migrated** |
| `account_payment_return` | returned/bounced items — breaks and re-makes reconciliations (`models/payment_return.py:246-249,214,277-278`), OCA, marked "Mature" | **not migrated** |
| `om_account_bank_statement_import` | v14 statement import; **note it was `auto_install: True`** | no custom counterpart; **core equivalents exist in `$V18E`** (`account_bank_statement_import{,_csv,_ofx,_qif,_camt}`, `account_bank_statement_extract`) |

**CMD-F-13 — `cheque_control`'s v14 signature is already incompatible with v18.**
`$CUST14/cheque_control/wizard/account_payment_register.py:13` — `_create_payment_vals_from_wizard(self)` takes no `batch_result`; the v18 core signature is `_create_payment_vals_from_wizard(self, batch_result)` (`$V18E/account/wizard/account_payment_register.py:968`). A port is not a copy.

**CMD-F-14 — `hr_expense_petty_cash_sequence` was version-bumped to v18 with an unchanged body.**
The MIGR18 manifest reads `18.0.1.0.2` (`__manifest__.py:6`) while `models/hr_expense_sheet.py` is **byte-identical** to the v14 file (21 lines each). Two concrete v18 incompatibilities in that unchanged body:
1. `@api.model def create(self, vals)` (`:10-11`) against the v18 batch convention.
2. It writes a field `number` (`:20`) which is **NOT FOUND** on v18 core `hr.expense.sheet` — PATTERN `number = fields|'number'` over `$V18E/hr_expense/models/hr_expense_sheet.py`: **0 hits.**
**A version string was raised without a migration.** `P06-B-39`.

---

## 4. Consolidated touchpoint matrix (CUST18 copy)

**POPULATION:** the 12 CUST18 modules in scope. **PATTERN:** `def action_post|def action_draft|def button_draft|def action_cancel|def reconcile\(|js_assign_outstanding_line|_reconcile_plan|account\.bank\.statement|'state': 'posted'|'state': 'in_process'|matched_payment_ids|def _synchronize|def _prepare_move_line_default_vals|def _create_payment_vals_from_wizard|def _create_payments`, `/tests/` excluded. **UNIT:** module.

| Module | Payment state | Move posting | Reconciliation / write-off | Bank statement |
|---|---|---|---|---|
| account_payment_multi_deduction | suppresses sync | via `_prepare_move_line_default_vals` | **yes** | NOT FOUND |
| full_payment_custom | field only | NOT FOUND | NOT FOUND | NOT FOUND |
| dev_print_cheque | metadata only | NOT FOUND | NOT FOUND | NOT FOUND |
| print_payment_remittance_adviec | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| scgl_purchase_advance_payment | NOT FOUND | creates a **draft** move via `sudo()` | NOT FOUND | NOT FOUND |
| hr_expense_petty_cash | **direct state write** | **`action_post` gate** | NOT FOUND | NOT FOUND |
| cr_effective_date_entries | NOT FOUND | **draft + re-post + name clear** | NOT FOUND | NOT FOUND |
| scgl_tax_period_date | NOT FOUND | writes aml in `create` | NOT FOUND | NOT FOUND |
| automatic_invoice_and_post | NOT FOUND | **posts on picking validate** | NOT FOUND | NOT FOUND |
| cap_auto_invoice | NOT FOUND | **posts on SO confirm** | NOT FOUND | NOT FOUND |
| l10n_th_withholding_tax | reads only | NOT FOUND | **mutates the settled amount** | NOT FOUND |
| l10n_th_withholding_tax_multi | reads only | NOT FOUND | **builds deduction lines** | NOT FOUND |

**CMD-F-15 — Not one custom module in the P06 scope touches the bank statement.** All twelve return NOT FOUND for `account.bank.statement`. **Class A within the declared pattern and path set.**
**Consequence:** every custom extension in this estate operates on the **payment** side of P06 and none on the **bank** side. The bank-event and reconciliation halves of the process run entirely on unmodified reference behaviour — which is exactly where the seven confirmed attack defects live.

**Additional hits outside the declared population**, surfaced by the same grep and recorded for completeness without analysis:
- `$CUST18/scgl_advance_expense_request/wizard/advance_request_reconcile.py:44` — `js_assign_outstanding_line`
- `$CUST18/import_bridge_axis/wizard/import_invoice_wizard.py:230,244` — `'state': 'posted'`
- `$CUST18/om_data_remove/models/model.py:82,168,207` — direct `account.bank.statement` / `account.bank.statement.line` access
**The third of these is material to P06 and was outside the declared module population.** A data-removal module with direct bank-statement access bears on attack A7. Raised as `P06-OQ-71` for a follow-on pass — and recorded as a live example of why an author-chosen module list is not a denominator.

---

## Blockers raised

| ID | Blocker |
|---|---|
| P06-B-36 | `hr_expense_petty_cash` carries a duplicated, behaviourally divergent, unimported `account.move` override. |
| P06-B-37 | `cr_effective_date_entries` unposts, resequences and re-dates posted entries, and writes valuation rows by raw SQL — incompatible with any reconciliation control assuming entry immutability. |
| P06-B-38 | Two auto-posting modules post invoices on non-accounting triggers, one with a truthy-string configuration gate and one with no `ensure_one()` and no idempotency guard. |
| P06-B-39 | `hr_expense_petty_cash_sequence` was version-stamped v18 with an unchanged v14 body, writing a field NOT FOUND on v18 core `hr.expense.sheet` (PATTERN `number = fields|'number'` over `$V18E/hr_expense/models/hr_expense_sheet.py`, 0 hits — Class A within that file's scope). |
| P06-B-34 | Post-dated cheque handling was not migrated. |
| P06-B-35 | Returned/bounced-payment handling was not migrated. |

## Open items

| ID | Item | Class |
|---|---|---|
| P06-OQ-52 | Which copy is deployed. Requires server config and the module registry; the copies are byte-identical at the Python layer. | D |
| P06-OQ-70 | Whether the `@api.model` `create` override in `scgl_tax_period_date` is tolerated by the v18 ORM. | D |
| P06-OQ-71 | `om_data_remove` has direct bank-statement access and was outside the declared population. | C |
| P06-OQ-72 | Access-rule exposure for `cheque.setting`, `petty.cash`, `effective_date.entries.wiz`, `account.payment.deduction` was not audited. | C |
| P06-OQ-73 | `print_payment_remittance_adviec` declares an abstract report named for a **different** module (`print_voucher_request`); whether the two collide was not assessed. | C |
| P06-OQ-74 | `dev_purchase_down_payment` (v14) may be the antecedent of `scgl_purchase_advance_payment`; not compared. | C |

---

# End

---

# APPENDIX A — TARGETED CONTINUATION FINDINGS (2026-09-04)

Added by `[SMEPLUS-26-09-04-ACC-P06-B2R-TARGETED-EVIDENCE-CLOSURE-001]`, closing `P06-OQ-71` and `P06-OQ-81`. The body above is unchanged.

## A.1 — `om_data_remove`: unconditional ledger deletion with no server-side authorisation

`P06-OQ-71` asked what this module does with its direct bank-statement access. The answer is more serious than the question anticipated.

**CMD-F-16 — The module performs unfiltered, ORM-bypassing, auto-committing `DELETE FROM` on the core accounting tables.**
`$CUST18/om_data_remove/models/model.py:18-27`:
```
sql = "delete from %s" % t_name
...
    self._cr.execute(sql)
    self._cr.commit()
```
**No `WHERE` clause.** Therefore no company filter, no date filter, no state filter and no lock-date check. Exceptions are swallowed at `:28-29` (`except Exception as e: _logger.warning(...)`).

**Tables reached, by method:**
- `remove_account()` — `account.bank.statement.line` (`:168`), `account.payment` (`:169`), `account.partial.reconcile` (`:172`), `account.move.line` (`:173`), `account.move` (`:175`), `payment.transaction` (`:167`)
- `remove_account_chart()` — `account.bank.statement` (`:207`), `account.payment` (`:205`)
- `remove_message()` — `mail.message`, `mail.followers`, `mail.activity` (`:326-330`)
- `remove_all()` (`:334-348`) chains all three: **one button destroys the ledger and the chatter that would evidence it.**

**CMD-F-17 — And it rewinds the document-number sequences.**
`:189-194` resets `ir.sequence.number_next = 1` for `BNK1/%`, `CSH1/%`, `INV/%`, `EXCH/%`, `MISC/%`. **Previously-used document numbers become re-issuable.** Combined with CMD-F-16 this is the complete removal of the audit trail *and* of the evidence that numbers were ever used.

**CMD-F-18 — Server-side authorisation: NOT FOUND.**
PATH SET `$CUST18/om_data_remove`, 4 source files, `models/model.py` (368 lines) read in full. **No `security/` directory and no `ir.model.access.csv`** (`find` returns neither). No `has_group` or `_is_admin` call anywhere in the module. The manifest declares no security file (`__manifest__.py:12-14`).
The only two controls are presentational: a `groups="base.group_system"` attribute on the **menu item** (`views/view.xml:113-119`) and a client-side `confirm=` string on each button (`views/view.xml:20`).
**The methods are plain `type="object"` handlers on `res.config.settings`, a `TransientModel` with a broad default ACL.** A menu `groups=` attribute controls menu visibility, not method invocation.
**Classification: CONFIRMED DEFECT.** Raised as **`P06-B-50`**.

**CMD-F-19 — It is present in all four custom roots** (`$CUST18`, `$CUST14`, `$T8MASTER`, `$MIGR18`), verified by `ls -d`. This is not an isolated copy.

**Assessment for P06.** This single module defeats attack A7's premise. The prior round analysed statement-line deletion through the ORM `unlink()` path and its `force_delete` bypass. **This module does not use that path at all** — it deletes the rows directly and commits. Every control discussed in A7 and A8 — audit-trail retention, `_check_reconciliation`, lock dates, the inalterability hash — is inapplicable, because none of them is in the code path.

## A.2 — The custom approval estate does not cover settlement

`P06-OQ-81` asked whether the custom approval modules supply the write-off control that `P06-B-22` says is missing. **They do not.**

**CMD-F-20 — Zero coverage of settlement objects.**
**DENOMINATOR:** POPULATION: 3 modules (`multi_level_approval`, `multi_level_approval_configuration`, `multi_level_approval_hr`), 46 tracked `.py`/`.xml`/`.csv` files. PATTERN: `account\.payment|account\.move|writeoff|write_off|reconcile`. UNIT: matching line. **RESULT = 0.**
The 11 `limit` hits are all ORM `search(..., limit=N)` keyword arguments.

**CMD-F-21 — The only enforcement hook is a `write`-time state-field gate, and it exempts administrators.**
`$CUST18/multi_level_approval_configuration/models/base_model.py:12-16`:
```
_inherit = 'base'
def write(self, vals):
    self.env['multi.approval.type'].check_rule(self, vals)
```
`check_rule` — `models/multi_approval_type.py:692-712`:
```
if self.env.user._is_admin() or self._context.get('run_python_code'):
    return True
...
    if approval_type.state_field and approval_type.state_field in vals:
        raise UserError(self._make_err_msg())
```
It blocks **writes that touch a configured state field** on models an administrator has manually configured. It does not cover `create` or `unlink`, and reconciliation does not proceed through a state-field `write` at all.

**CMD-F-22 — There is no amount, threshold or limit concept.**
`amount_opt` (`multi_level_approval/models/multi_approval_type.py:60-64`) is a Selection controlling **whether an Amount box is required on the request form**. `amount` (`models/multi_approval.py:93`) is a `fields.Float` on the request document. **No numeric comparison, no `threshold`, no `limit` field.** The only routing input is a free-text `domain` evaluated by `safe_eval` (`multi_approval_type.py:42,164`) — i.e. an amount rule is runtime data a user types, not shipped behaviour.

**CMD-F-23 — And the approval gate can disable itself.**
The approve/refuse hooks execute **stored Python source** (`approve_python_code` / `refuse_python_code`) through `safe_eval(..., mode="exec")` with `env` and `record` in scope (`multi_approval_type.py:657-667`), and set `run_python_code: 1` in the context (`:616`) — **which is precisely the flag that makes `check_rule` return `True` unconditionally (`:692`)**.
`action_configure` (`:525-552`) likewise generates a computed field's Python body as a string (`get_compute_val`, `:274-278`) and execs it.
**Classification: CONFIRMED DEFECT.** An approval framework whose own execution path carries the flag that bypasses it is not a control. Raised as **`P06-B-51`**.

**CMD-F-24 — Meanwhile the custom estate's actual write-off producer has a blanket ACL.**
`$CUST18/account_payment_multi_deduction/security/ir.model.access.csv:2`:
```
access_account_payment_deduction,account.payment.deduction,model_account_payment_deduction,account.group_account_invoice,1,1,1,1
```
**Any Invoicing user, full create/read/write/unlink.** Its only validation is an arithmetic identity, not a ceiling — `wizard/account_payment_register.py:78-80`: `raise UserError(_("The total deduction should be %s") % rec.payment_difference)`. The `groups=` attributes in its views cover analytic-distribution columns, not the deduction amount.
Raised as **`P06-B-52`**.

**Effect on `P06-B-22`:** the blocker was downgraded to Class B at the prior round's challenge precisely because this estate had not been searched. **It has now been searched, and the negative is restored to Class A within the enlarged declared scope** (`$V18E/account` + `$V18E/account_accountant` + the three custom approval modules). **There is no approval or amount control over settlement write-offs anywhere in the searched estate.**

## A.3 — `BYPASS_LOCK_CHECK` in the custom trees: NOT FOUND

`P06-OQ-21`. **DENOMINATOR:** PATH SET all four custom roots; POPULATION **19,982 files** (`find -type f`: 5,087 + 8,795 + 3,599 + 2,501); PATTERN `BYPASS_LOCK_CHECK|bypass_lock_check`, `grep -rIn -E`, all file types. **RESULT = 0 lines.**
Widened confirmation: `bypass[_ ]?lock` case-insensitive → **0 lines**. A broader `bypass` scan returns 20 files, none lock-related.
**Class A within that declared scope.** Combined with the prior round's `$V18E` search (2 callers, both in `account/models/partner.py`, partner merge), the sentinel originates and is used only in the reference core.
**`P06-OQ-21` — CLOSED — SOURCE EVIDENCE VERIFIED.**
*Residual scope note: the Odoo core `odoo/` package outside `addons/` was not searched. That is a framework path, not an addon path, and no custom code lives there — but the boundary is declared rather than assumed.*

## A.4 — Blockers and open items arising from this appendix

| ID | Item |
|---|---|
| `P06-B-50` | `om_data_remove` deletes bank statements, payments, moves, partials and chatter by unconditional SQL, then rewinds sequences, with no server-side authorisation. Present in all four custom roots. |
| `P06-B-51` | The custom approval framework's execution path sets the very context flag that disables its own gate. |
| `P06-B-52` | The custom write-off producer is granted full CRUD to any Invoicing user with no amount ceiling. |
| `P06-OQ-21` | **CLOSED** |
| `P06-OQ-71` | **CLOSED** — and it produced `P06-B-50` |
| `P06-OQ-81` | **CLOSED** — and it restored `P06-B-22` to Class A |
| `P06-OQ-91` | **NEW** — whether any `multi.approval.type` record is configured against a settlement model is a **database** question (`model_id` is runtime-populated; no data record ships in any manifest). **HOLD — DATABASE EVIDENCE REQUIRED.** |

---

# End of Appendix A
