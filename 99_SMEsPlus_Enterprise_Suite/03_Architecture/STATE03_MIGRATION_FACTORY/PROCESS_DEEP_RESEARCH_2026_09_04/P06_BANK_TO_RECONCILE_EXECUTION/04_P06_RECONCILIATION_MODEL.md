# P06_RECONCILIATION_MODEL.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. What reconciliation *is* in the reference implementation

**RM-F-01 — Validating a bank match does not reconcile the suspense line. It deletes and re-creates every line of the statement entry.**
`$V18E/account_accountant/models/bank_rec_widget.py:1409-1413`:
```
move_ctx = move.with_context(force_delete=True, skip_readonly_check=True,)
move_ctx.write({'line_ids': [Command.clear()] + line_ids_create_command_list})
```
`force_delete=True` bypasses the normal `_check_reconciliation` protection; `skip_readonly_check=True` bypasses field protection.
**This is the single most important structural fact about the reconciliation engine.** A bank match is not a *link* between two existing records — it is a **destruction and reconstruction of a posted journal entry**. Everything else in this file follows from it: the audit trail of what was matched to what, and what the entry looked like before, does not survive the operation. Only the resulting partials do.

**RM-F-02 — The commit is a `_reconcile_plan` with recursive exchange differences disabled.**
`$V18E/account_accountant/models/bank_rec_widget.py:1443-1447`:
```
self.env['account.move.line'].with_context(no_exchange_difference_no_recursive=True)._reconcile_plan([
    (line + counterpart).with_prefetch(all_line_ids) for line, counterpart in lines])
```
Exchange-difference moves are pre-created *before* the reconciliation (`:1440`) and back-linked onto the partials afterwards (`:1450-1455`), and their amounts are "squashed" into the counterpart line before the aml is created (`:1386-1388`).

**RM-F-03 — Pairing is by sequence index, not by record id.**
`$V18E/account_accountant/models/bank_rec_widget.py:1377-1378` builds `to_reconcile` as `(len(line_ids_create_command_list) + 1, line.source_aml_id)`, resolved after re-creation via `sequence2lines = move_ctx.line_ids.grouped('sequence')` (`:1416-1420`). The correspondence between a widget row and the journal item it becomes is positional.

---

## 2. The widget state machine

**RM-F-04 — The widget model is not persisted at all.**
`$V18E/account_accountant/models/bank_rec_widget.py:20-21` — `_auto = False` / `_table_query = "0"`. There is no stored record of a reconciliation session, who ran it, what candidates were offered, or what was rejected.

**RM-F-05 — Three states, driven entirely by the presence of the suspense account.**
`$V18E/account_accountant/models/bank_rec_widget.py:99-101` — `invalid`, `valid`, `reconciled`. Transition logic at `:201-208`:
```
elif wizard.st_line_id.is_reconciled: wizard.state = 'reconciled'
... if suspense_account in wizard.line_ids.account_id: wizard.state = 'invalid' else: wizard.state = 'valid'
```
**"Valid" means "the suspense account no longer appears on any line."** It does not mean the match is correct, that the counterparty is right, or that the amounts correspond to anything real. A write-off to any account satisfies it.

**RM-F-06 — Eight line flags.**
`$V18E/account_accountant/models/bank_rec_widget_line.py:25-32` — `liquidity, new_aml, aml, exchange_diff, tax_line, manual, early_payment, auto_balance`. **DENOMINATOR:** POPULATION: the `flag` selection tuples. UNIT: value. **COUNT = 8.**
- `auto_balance` is the residual plug; **editing it silently converts it to `manual`** (`bank_rec_widget.py:389-392`). The distinction between "the system plugged this" and "a human decided this" is erased by the act of touching it.
- `auto_balance` is dropped and re-created on every rebalance so it is always last (`:479-482`).

**RM-F-07 — "To check" is the inverse of `account.move.checked`, and selecting a reconcile model can silently clear it.**
`$V18E/account_accountant/models/bank_rec_widget.py:1484-1487` — `_action_to_check` sets `move.checked = False` **then validates**. `:1573-1575` — merely selecting a reconcile model with `to_check` set writes `self.st_line_id.move_id.checked = False`. `:1525-1529` — `_js_action_set_as_checked` only flips the flag; it validates nothing.
**"Checked" is therefore not a review control.** It is a display flag that any of three unrelated actions can set or clear.

**RM-F-08 — Reset is blocked on hashed lines but redirected to the destructive path.**
`$V18E/account_accountant/models/bank_rec_widget.py:1507-1515` raises *"You can't hit the reset button on a secured bank transaction."*; `:1517` otherwise delegates to `st_line.action_undo_reconciliation()`.

---

## 3. Matching rules — how a candidate is chosen

**RM-F-09 — Three rule types; evaluation order is `sequence, id`; the first rule producing candidates wins.**
`$V18E/account/models/account_reconcile_model.py:192-194` — `writeoff_button`, `writeoff_suggestion`, `invoice_matching`. `_order = 'sequence, id'` (`:178`).
`$V18E/account_accountant/models/account_reconcile_model.py:76-86` — `if res: return {**res, 'model': rec_model,}`. The in-code note at `:360-362` is explicit: *"the algorithm stops when a rule returns some candidates."*
`writeoff_button` models are excluded from automatic application (`:60`).
**Consequence:** rule ordering is business logic. A rule inserted at a lower sequence silently suppresses every rule below it for the transactions it matches, with no record on the statement line of which rules were skipped.

**RM-F-10 — Text matching is case-insensitive, anchored, and reads three specific fields.**
`$V18E/account_accountant/models/account_reconcile_model.py:117-124` maps rule fields to `st_line.payment_ref`, `move.narration`, `st_line.transaction_type`. `match_regex` uses `re.match` — **anchored at string start, not a search**. A reference appearing mid-narrative will not match a regex rule.
`match_text_location_*` (`$V18E/account/models/account_reconcile_model.py:219-233`) maps to `payment_ref` / `narration` / `ref`; **only `label` defaults to True.**
Token significance is hard-coded: `$V18E/account_accountant/models/account_reconcile_model.py:176` — `significant_token_size = 4`.

**RM-F-11 — The candidate query tokenises by stripping all non-digits in the database.**
`$V18E/account_accountant/models/account_reconcile_model.py:264-270`:
```
REGEXP_SPLIT_TO_ARRAY(SUBSTRING(REGEXP_REPLACE(%(field)s, '[^0-9\s]', '', 'g'), '\S(?:.*\S)*'), '\s+')
```
Six UNION-ALL sub-queries maximum: 3 text columns × 2 token strategies (`:253-257`, `:276-280`). Ranking is `COUNT(*) DESC` on token hits, then maturity/date/id (`:295-302`).
**Consequence for Thai practice:** a numeric-token match means the system matched *digit runs*, not references. Invoice numbers, tax IDs, dates and amounts all reduce to digit runs. A four-digit token is enough to link a bank line to an invoice.

**RM-F-12 — Default lookback is 18 months.** `$V18E/account/models/account_reconcile_model.py:320-325`.

**RM-F-13 — Textual hits may auto-reconcile; amount-only fallback may not.**
`$V18E/account_accountant/models/account_reconcile_model.py:310-313` returns `allow_auto_reconcile: True`; the amount-only fallback at `:351-354` returns `False`. The partner-less fallback matches on an **exact rounded residual** (`:333-335,342`).

**RM-F-14 — If a text-location toggle is on and the text query finds nothing, the rule aborts rather than falling back to amounts.**
`$V18E/account_accountant/models/account_reconcile_model.py:314-317`.

**RM-F-15 — Auto-reconcile requires three simultaneous conditions.**
`$V18E/account_accountant/models/account_reconcile_model.py:416-417` — `'allow_auto_reconcile' in status`, `candidate_vals['allow_auto_reconcile']`, and `self.auto_reconcile`. The field is labelled "Auto-validate" (`$V18E/account/models/account_reconcile_model.py:196-197`).

---

## 4. Payment tolerance — where a shortfall silently closes an invoice

**RM-F-16 — Tolerance defaults ON with a percentage type.**
`$V18E/account/models/account_reconcile_model.py:284-302` — `allow_payment_tolerance` default `True`, `payment_tolerance_type` default `percentage`, help text *"Difference accepted in case of underpayment."*

**RM-F-17 — Turning tolerance OFF removes the check entirely and permits both write-off and auto-reconcile.**
`$V18E/account_accountant/models/account_reconcile_model.py:520-521`:
```
if not self.allow_payment_tolerance: return {'allow_write_off', 'allow_auto_reconcile'}
```
**This is a control-inversion.** A field named "Payment Tolerance", switched *off*, does not tighten the control — it accepts an **arbitrary** shortfall and permits automatic validation. The safe setting is `allow_payment_tolerance = True` with `payment_tolerance_param = 0`, which rejects (`:548-549`). An operator reading the label would reasonably conclude the opposite.

**RM-F-18 — Overpayment skips the tolerance check and permits auto-reconcile.**
`$V18E/account_accountant/models/account_reconcile_model.py:542-545` — in-code comment: *"the payment amount is higher than the sum of invoices … don't check the tolerance and don't try to generate any write-off."*

**RM-F-19 — Shipped defaults are safe; the exposure is a configuration change with no approval gate.**
`$V18E/account/models/chart_template.py:1116-1135` seeds `reconcile_perfect_match` with `auto_reconcile: True` and `payment_tolerance_param: 0`, and `reconcile_partial_underpaid` with `auto_reconcile: False` and `allow_payment_tolerance: False`. So out of the box a shortfall is rejected.
**The three tolerance fields carry `tracking=True` (`account_reconcile_model.py:286,293,301`) and nothing else.** NOT FOUND: any approval, limit or group restriction on changing them — PATTERN `writeoff.*(limit|approv)|(limit|approv).*writeoff` over `$V18E/account` + `$V18E/account_accountant`, py+xml: **0 hits**. **Class A within that declared scope.**
**Consequence:** the difference between "every shortfall is rejected" and "every shortfall under N percent silently closes the invoice" is one number, changed by anyone with accounting-manager rights, logged only in a chatter entry.

---

## 5. Reconciliation primitives and their guards

**RM-F-20 — `reconcile()` and `remove_move_reconcile()` are both one-line wrappers.**
`$V18E/account/models/account_move_line.py:3074-3076` and `:3078-3080`:
```
def remove_move_reconcile(self):
    """ Undo a reconciliation """
    (self.matched_debit_ids + self.matched_credit_ids).unlink()
```
**Undoing a reconciliation performs no checks of any kind.**

**RM-F-21 — The exigibility guards, and exactly what they permit.**
`$V18E/account/models/account_move_line.py:2326-2346`, invoked once per plan node (`:2435-2437`):
| Guard | Line | What it actually tests |
|---|---|---|
| already reconciled | 2326 | `aml.reconciled`, i.e. **residual is zero** — not "a partial exists" |
| posted only | 2328 | `parent_state != 'posted'` |
| same account | 2330-2335 | reads the account **through `shadowed_aml_values`**, so a caller supplying a shadow map legitimately reconciles across different real accounts |
| same company | 2336-2340 | **`len(self.company_id.root_id) > 1`** — root, not company |
| account reconcilable | 2341-2346 | with an explicit exemption for `asset_cash` / `liability_credit_card` |

**RM-F-22 — The company guard is root-scoped. Sibling branch companies reconcile freely.**
This is the load-bearing finding for the cross-company attack. See the Duplicate/Match Attack file, A4.

**RM-F-23 — There is no currency guard; the optimiser splits instead of rejecting.**
`$V18E/account/models/account_move_line.py:2393-2401`.

**RM-F-24 — `_reconciled_by_number` expands the full-reconcile batch beyond the explicit plan.**
`$V18E/account/models/account_move_line.py:2571-2577`. The set of lines affected by a reconciliation is therefore not the set the operator selected.

**RM-F-25 — `full_reconcile_id` is written by raw SQL, bypassing the ORM `write()` and therefore its lock-date checks.**
`$V18E/account/models/account_full_reconcile.py:52-57` — `self.env.cr.execute_values("""UPDATE account_move_line line SET full_reconcile_id = source.full_id ...`.

**RM-F-26 — An import path silently flips an account's `reconcile` configuration.**
`$V18E/account/models/account_move_line.py:3106-3110`:
```
if not account.reconcile: _logger.info("%s has reconciled lines, changing the config", account.display_name)
account.reconcile = True
```
A chart-of-accounts setting is changed by a data operation, recorded only in a log line.

**RM-F-27 — Partner and account may be changed across a whole matched set.**
`$V18E/account/models/account_move_line.py:1596-1598` — in-code comment: *"allow changing the partner or/and the account on all the lines of a reconciliation together"*. The counterparty of a settled item is editable after settlement.

---

## 6. Lock dates and reconciliation — the asymmetry

**RM-F-28 — Reconciling and un-reconciling are NOT lock-date gated.**
**DENOMINATOR:** PATTERN `lock_date|_check_fiscal_lock_dates|hard_lock|_validate_locks`. PATH SET: `account/models/account_move_line.py`, `account/models/account_partial_reconcile.py`, `account/models/account_full_reconcile.py`, `account_accountant/models/bank_rec_widget.py`, `account_accountant/wizard/account_reconcile_wizard.py`, `account_accountant/wizard/account_auto_reconcile_wizard.py`. UNIT: lock-date call inside a reconcile primitive.
**RESULT: zero lock-date calls inside `reconcile()`, `_reconcile_plan`, `_reconcile_plan_with_sync`, `_optimize_reconciliation_plan`, `_check_amls_exigibility_for_reconciliation`, `_create_reconciliation_partials`, `AccountPartialReconcile.create/unlink`, or `AccountFullReconcile.create`.** `account_full_reconcile.py` and `bank_rec_widget.py` return **0 hits for the whole file**. **Class A within that declared scope.**
Mechanically this holds because reconciliation writes `account.partial.reconcile` rows and updates `full_reconcile_id` by raw SQL (RM-F-25), so `AccountMoveLine.write`'s lock check is never reached. The protected-field lists confirm it: `$V18E/account/models/account_move_line.py:3368-3374` — `fiscal_fnames` contains `balance, tax_line_id, tax_ids, tax_tag_ids, account_id, journal_id, amount_currency, currency_id, partner_id`. **`amount_residual`, `full_reconcile_id`, `matching_number` and `reconciled` are all absent.**

**RM-F-29 — Where a lock date is consulted on this path, it SHIFTS the date rather than refusing.**
`$V18E/account_accountant/wizard/account_reconcile_wizard.py:492-496` — `if lock_dates: return lock_dates[-1][0] + timedelta(days=1)`, applied at `:602` and `:645`. The user sees a message, not a block (`:426-429`): *"The date you set violates the lock date … It will be overriden by the following date."*
Same pattern for cash-basis reversal dating (`$V18E/account/models/account_partial_reconcile.py:513-514`) and for reversal moves (`$V18E/account/models/account_move.py:5669-5674`).

**RM-F-30 — The one place a lock date DOES block is an emergent side effect, not a designed control.**
Because `_action_validate` clears `move.line_ids` (RM-F-01), aml `unlink()` runs, and `$V18E/account/models/account_move_line.py:1700-1703` calls `_check_fiscal_lock_dates()` on posted moves. So **validating a bank transaction dated in a locked period is blocked, while reconciling or un-reconciling pre-existing items in a locked period is not.**
And the check is scoped to the **statement line's own move** — the counterpart invoice, whose residual and payment status are being retroactively changed, is never date-checked.
**Confidence: medium-high.** The blocking depends on the ORM routing `Command.clear()` to `AccountMoveLine.unlink()` under `force_delete=True`; the lock check at `:1703` is not gated by `force_delete`, but this was read, not executed. Carried as `P06-OQ-20` — **a control that exists by accident should not be relied on until it is tested.**

**RM-F-31 — Locking a period is guarded against unreconciled statement lines; nothing re-asserts it afterwards.**
`$V18E/account/models/company.py:519-528` raises a `RedirectWarning`: *"There are still unreconciled bank statement lines in the period you want to lock."* A one-time gate at lock time only.

**RM-F-32 — A named lock bypass sentinel exists.**
`$V18E/account/models/account_move.py:83` — `BYPASS_LOCK_CHECK = object()`, honoured at `:2378`. Callers in `$V18E` excluding tests: **2**, both in `$V18E/account/models/partner.py:804-805` (partner merge). **Any custom module importing this sentinel disables lock enforcement wholesale.** The SMEsPlus custom addon trees were **not searched for it** — Class C, carried as `P06-OQ-21`.

---

## 7. Automatic reconciliation at scale

**RM-F-33 — The auto-reconcile wizard has exactly one date guard, and it is an upper bound only.**
`$V18E/account_accountant/wizard/account_auto_reconcile_wizard.py:22-23` — `to_date` required, defaults to today; `from_date` optional. Applied at `:98-99` as `('date', '>=', self.from_date or date.min)`. **With `from_date` blank the wizard operates over all history back to `date.min`.** NOT FOUND: any lock-date check in this wizard (PATTERN `lock_date|hard_lock|_check_fiscal`, that file, 0 hits).
Two modes: `one_to_one` ("Perfect Match") and `zero_balance` ("Clear Account") (`:38-39`).

**RM-F-34 — The partner filter is silently ignored unless an account filter is also set.**
`$V18E/account_accountant/wizard/account_auto_reconcile_wizard.py:105-108` — the partner clause is nested inside `if self.account_ids:`. Selecting partners alone produces a run across **all** accounts. **Classification: CONFIRMED DEFECT.**

**RM-F-35 — The cron auto-reconciler swallows user errors at INFO level.**
`$V18E/account_accountant/models/account_bank_statement.py:145-159`:
```
if wizard.state == 'valid' and wizard.matching_rules_allow_auto_reconcile: wizard._action_validate()
except UserError as e: _logger.info("Failed to auto reconcile statement line %s due to user error: %s", ...)
```
**A lock-date or balance failure during automatic reconciliation produces a log line and nothing else** — no flag on the statement line, no queue, no operator notification. Scope: unreconciled lines created within the last 3 months, ordered by `cron_last_check` (`:103-108`), capped at 180 seconds (`account_reconcile_model.py:569-571`).
**Consequence:** silent partial completion is the normal failure mode of automatic reconciliation.

---

## 8. Manual reconcile wizard

**RM-F-36 — Up to two different accounts may be reconciled together, by materialising a transfer entry.**
`$V18E/account_accountant/wizard/account_reconcile_wizard.py:25-36` raises above two accounts and forces the second through `shadowed_aml_values`; `:658-667` creates a real transfer move first (`if do_transfer: transfer_move = self.create_transfer()`).
This is the sanctioned use of the shadow mechanism noted in RM-F-21.

**RM-F-37 — Reconcile-model autocomplete is restricted by raw SQL to models with exactly one line.**
`$V18E/account_accountant/wizard/account_reconcile_wizard.py:444-451` — `HAVING COUNT(account_reconcile_model.id) = 1`.

---

## 9. Target-design requirements

| ID | Requirement | Arises from |
|---|---|---|
| RM-R-01 | A reconciliation must be a **record**, not a rewrite. The pre-match state of the entry must survive the match. | RM-F-01 |
| RM-R-02 | A reconciliation session must be persisted: who, when, which candidates were offered, which were rejected and why. | RM-F-04 |
| RM-R-03 | "Valid" must mean *evidenced*, not *suspense-free*. | RM-F-05 |
| RM-R-04 | System-plugged and human-decided differences must remain distinguishable after editing. | RM-F-06 |
| RM-R-05 | Review status must be a controlled state with a reviewer identity, not a flag three unrelated actions can clear. | RM-F-07 |
| RM-R-06 | The matching rule that fired, and the rules it pre-empted, must be recorded on the match. | RM-F-09 |
| RM-R-07 | Tolerance semantics must be non-invertible: disabling a tolerance must never widen acceptance. | RM-F-17 |
| RM-R-08 | Changing a tolerance parameter must require approval and must be a controlled configuration change. | RM-F-19 |
| RM-R-09 | Breaking a reconciliation must be an authorised, logged, lock-date-aware operation. | RM-F-20, RM-F-28 |
| RM-R-10 | Company isolation must be tested at `company_id`, never at `root_id`, on every reconciliation path. | RM-F-22 |
| RM-R-11 | No accounting-relevant field may be written by raw SQL that bypasses the guard layer. | RM-F-25 |
| RM-R-12 | Chart-of-accounts configuration must never be mutated by a data operation. | RM-F-26 |
| RM-R-13 | Automatic reconciliation must have a bounded window on both ends and must surface every failure to an operator queue. | RM-F-33, RM-F-35 |
| RM-R-14 | A lock-date control must be explicit and must apply to **both** sides of a reconciliation. | RM-F-29, RM-F-30 |

## 10. Open items

| ID | Item | Class |
|---|---|---|
| P06-OQ-20 | RM-F-30's incidental lock block was read, not executed. Confirm by test before relying on it. | D |
| P06-OQ-21 | `BYPASS_LOCK_CHECK` was not searched for in the SMEsPlus custom addon trees. | C |
| P06-OQ-22 | `_get_default_amls_matching_domain` — the outermost filter on every candidate search — was not read in full. | C |
| P06-OQ-23 | `_prepare_reconciliation_single_partial` (~300 lines) was read only in part; the mixed-currency partial-split arithmetic is uncovered. | C |
| P06-OQ-24 | Concurrency: no pessimistic row lock was found on the reconcile path (PATTERN `FOR UPDATE|select_for_update|_lock`, 0 hits). Whether isolation alone serialises two concurrent validations is **not decidable from static evidence**. | D |

---

# End
