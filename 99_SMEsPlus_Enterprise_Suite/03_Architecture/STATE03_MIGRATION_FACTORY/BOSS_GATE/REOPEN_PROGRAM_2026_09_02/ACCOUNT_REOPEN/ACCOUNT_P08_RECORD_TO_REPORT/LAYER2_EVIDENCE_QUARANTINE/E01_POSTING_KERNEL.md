# E01 — POSTING KERNEL (LAYER 2 — AUDIT QUARANTINE)

**Boss / PMO / AI-Audit only.** Reference-source citations. Not for downstream packages.

REF18 = `.../SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` · CORE = `.../odoo-18.0+e.20250608/odoo`

## Dispatch and context
| Ref | Citation |
|---|---|
| `EV-KRN-01` | `CORE/api.py:512 call_kw` · `:529 context = kwargs.pop('context', None) or {}` · `:530 recs = recs.with_context(context)` — client context applied wholesale |
| `EV-KRN-02` | `CORE/service/model.py:71-72` dispatch → `call_kw`; no context allowlist found (searched `api.py`, `service/model.py`, `http.py`) |

## Balance
| Ref | Citation |
|---|---|
| `EV-KRN-03` | `account/models/account_move.py:2330 _check_balanced` · `:2334 _disable_recursion(container,'check_move_validity',default=True,target=False)` |
| `EV-KRN-04` | `account/models/account_move.py:5940-5961 _disable_recursion` — `current_val = self.env.context.get(key, default)`; `disabled = current_val == target` |
| `EV-KRN-05` | `account/models/account_move.py:2355-2375 _get_unbalanced_moves` — SQL groups by move, `HAVING ROUND(SUM(line.balance), currency.decimal_places) != 0`; `amount_currency` never summed |
| `EV-KRN-06` | product consumers of the suppression key: `point_of_sale/models/pos_session.py:439,442,985` |

## Posted-record protection
| Ref | Citation |
|---|---|
| `EV-KRN-07` | `account/models/account_move.py:3244-3248 unmodifiable_fields` = invoice_line_ids, line_ids, invoice_date, date, partner_id, invoice_payment_term_id, currency_id, fiscal_position_id, invoice_cash_rounding_id |
| `EV-KRN-08` | `account/models/account_move.py:3249` — guard skipped on `skip_readonly_check`; product consumers `account/models/account_bank_statement_line.py:441,483,803,845`; `account_accountant/models/account_move.py:130`; `account_accountant/models/bank_rec_widget.py:1411,1458` |
| `EV-KRN-09` | `account/models/account_move.py:83 BYPASS_LOCK_CHECK = object()` · `:2377-2379` identity comparison · only non-test users `account/models/partner.py:804-805` |
| `EV-KRN-10` | `account/models/account_move.py:3168-3174 _stolen_move`, used `:3192` (create) and `:3260` (write) — line re-parenting |
| `EV-KRN-11` | `account/models/account_move.py:3184-3186 create` refuses `state == 'posted'` |

## Seal
| Ref | Citation |
|---|---|
| `EV-KRN-12` | `account/models/account_move.py:46 MAX_HASH_VERSION = 4` |
| `EV-KRN-13` | `account/models/account_move.py:3832-3839 _get_integrity_hash_fields` — v1: date, journal_id, company_id; v2-4: name, date, journal_id, company_id; version read from `self._context.get('hash_version', MAX_HASH_VERSION)` at `:3834` |
| `EV-KRN-14` | `account/models/account_move_line.py:3283-3290` — v1: debit, credit, account_id, partner_id; v2-4: + name; version read at `:3285` |
| `EV-KRN-15` | write guards `account/models/account_move.py:3208-3214`; `account/models/account_move_line.py:1554-1563` |
| `EV-KRN-16` | `account/models/account_move.py:318 secure_sequence_number` — declared, no production writer found in REF18 ∪ `addons_archive` |

## Numbering and deletion
| Ref | Citation |
|---|---|
| `EV-KRN-17` | `account/models/account_move.py:713-715 _sql_constraints unique_name` (empty SQL body) · `:730-735 _auto_init` `CREATE UNIQUE INDEX account_move_unique_name ON account_move(name, journal_id) WHERE (state='posted' AND name != '/')` |
| `EV-KRN-18` | `account/models/account_move_line.py:429-448` — `check_credit_debit` (`credit*debit=0`), `check_amount_currency_balance_sign` |
| `EV-KRN-19` | `account/wizard/account_resequence.py:12` model · `:155-171 resequence()` — `moves_to_rename.name = False`, flush, reassign; only guard `:157-159` refuses date reordering on hash-restricted journals |
| `EV-KRN-20` | `account/models/account_move.py:3329-3345 _unlink_forbid_parts_of_chain` · `:3347-3358 _unlink_account_audit_trail_except_once_post` · `:3360-3368 unlink` (`_logger.info` only) · `:3305-3308` dead `if not ...: pass` branch |
| `EV-KRN-21` | `account/models/company.py:257 check_account_audit_trail` — no `default=` |
| `EV-KRN-22` | `account/models/account_move_line.py:1669` line-level delete guard, bypassed by `force_delete`; product users `account/models/account_bank_statement_line.py:451,483`; `account_accountant/models/bank_rec_widget.py:1410`; `account_asset/models/account_asset.py:957` |
| `EV-KRN-23` | `account/models/account_move_line.py:33-41` `move_id ondelete="cascade"`; `:93-104` `account_id ondelete="cascade"`; guard `account/models/account_account.py:1095` declared `@api.ondelete(at_uninstall=False)` |

## Control-account gating
| Ref | Citation |
|---|---|
| `EV-KRN-24` | `account/models/account_move_line.py:1243-1256 _check_payable_receivable` — both branches gated on `is_sale_document` / `is_purchase_document`; a `move_type='entry'` move satisfies neither |
| `EV-KRN-25` | `account/models/account_move_line.py:1204-1229 _check_constrains_account_id_journal_id` — bare `continue` at `:1221` for the journal's default/suspense account |

## Correction-by-new-entry (positive pattern)
| Ref | Citation |
|---|---|
| `EV-KRN-26` | `account/wizard/account_automatic_entry_wizard.py:19` actions · `:403-461 _do_action_change_period` · `:462-500 _do_action_change_account` — creates and posts new moves, uses `_get_lock_safe_date`, reconciles, posts chatter both sides |
