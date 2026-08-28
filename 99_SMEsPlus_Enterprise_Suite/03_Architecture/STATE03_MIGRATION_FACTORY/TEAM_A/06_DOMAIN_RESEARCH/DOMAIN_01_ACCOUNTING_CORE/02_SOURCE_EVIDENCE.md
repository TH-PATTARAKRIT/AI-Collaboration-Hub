> Domain: DOMAIN_01 — Accounting Core | Team A (Maker) | Session SMEPLUS-26-08-29-MIG-A-D01-ACCOUNTING-CONT-001
> Source path READ ONLY. No target design. No coding. Boss is sole Final Approver.
> STEP linkage: **TBD / BASELINE LINKAGE REQUIRED** — STEP0303R5 is prior governance/planning evidence only.

# 02 — SOURCE EVIDENCE

Read-only. All paths under `ACCOUNT/01 ACCOUNT/SOURCE CODE/01 ACCOUNT/account/models/`.

| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SE-01 | account_move.py | L129–133 | State selection: draft / posted / cancel |
| SE-02 | account_move.py | L142 | `move_type` — one model for all document types |
| SE-03 | account_move.py | L2765–2782 | `_check_balanced` — debit=credit asserted in application code; raises UserError |
| SE-04 | account_move.py | L2769 | `_disable_recursion(container, 'check_move_validity')` — the balance check is **suppressible** |
| SE-05 | account_move.py | L2784+ | `_get_unbalanced_moves` — comment notes computed stored fields cannot be assumed during create/write |
| SE-06 | account_move.py | L2825–2856 | `@api.constrains`: auto-post requires bill date; journal↔move_type agreement; tax country validation; invoice currency rate |
| SE-07 | account_move.py | L623, L631 | `reversed_entry_id` / `reversal_move_ids` — reversal as self-reference |
| SE-08 | account_move.py | L5433 | `_reverse_moves` |
| SE-09 | account_move.py | L5663, L5712 | Reversal auto-reconciles against the original when posting |
| SE-10 | account_move.py | L6019 / L5507 | `action_post` → `_post(soft=True)` |
| SE-11 | account_move.py | L6108, L6187 | `button_draft`, `button_cancel` |
| SE-12 | account_move.py | L6109 | Reset-to-draft guard: move must be in ('cancel','posted') |
| SE-13 | account_move.py | L326, L353, L938 | `highest_name`, `secure_sequence_number` (no-gap inalterability sequence), `_compute_name` |
| SE-14 | account_move.py | L600–612 | `payment_state` — separate from `state` |
| SE-15 | account_move_line.py | L59–61 | `company_currency_id` related+stored from move |
| SE-16 | account_move_line.py | L118–134 | Monetary fields declared against `company_currency_id` |
| SE-17 | account_account.py | L44–72 | `account_type` — 19-value enumeration |
| SE-18 | account_account.py | L73+ | `include_initial_balance`, `internal_group` (equity/asset/liability/…) |
| SE-19 | account_account.py | L39 | `code` — Char(64), computed+searchable+inverse |
| SE-20 | account_account.py | L89 | `reconcile` — per-account reconciliation flag |
| SE-21 | account_account.py | L1047 | Deprecation guarded against tax repartition usage |
| SE-22 | account_journal.py | L145 | `restrict_mode_hash_table` — opt-in hash chaining |
| SE-23 | account_journal.py | L794–800 | Hash mode cannot simply be switched off once entries are hashed |
| SE-24 | company.py | L60–68, L78–99 | Six lock-date fields incl. `hard_lock_date` |
| SE-25 | company.py | L110–113 | `user_*` computed lock-date variants (per-user effective locks) |
| SE-26 | account_lock_exception.py | L257–305 | Lock exceptions with audit-trail interrogation |
| SE-27 | models/ directory listing | — | 40 model files; core: account_account, account_journal, account_move, account_move_line, reconcile, analytic, chart_template |

**Not read (black-box, OEEL-1):** `account_accountant`, `account_reports`, `account_asset`,
`account_budget`, `accountant`. No source body of any OEEL-1/OPL-1 module was opened.

## ADDITIONAL ANCHORS — CORR-001 ROUND
| ID | File | Anchor | What it evidences |
|---|---|---|---|
| SE-28 | account_move_line.py | L463–466 | `_check_credit_debit` = `models.Constraint("CHECK(... OR credit * debit=0)")` — a real DB CHECK |
| SE-29 | account_move_line.py | L467–470 | `_check_amount_currency_balance_sign` — balance and amount_currency must agree in sign |
| SE-30 | account_move_line.py | L471–474 | `_check_accountable_required_fields` — account required on accountable lines |
| SE-31 | account_move_line.py | L475–478 | `_check_non_accountable_fields_null` — presentation lines carry no amounts |
| SE-32 | account_account.py | L1492–1493 | `_check_length_prefix` CHECK constraint |
| SE-33 | account_move.py | L69, L2807 | `BYPASS_LOCK_CHECK` sentinel and `bypass_lock_check` context — lock enforcement has an explicit escape |
| SE-34 | account_journal.py | L36, L293 | `_uniq_name`, `_code_company_uniq` — UNIQUE constraints via `models.Constraint` |

**Method note:** Odoo 19 declares database constraints through `models.Constraint(...)`, not the
legacy `_sql_constraints` list — a grep for `_sql_constraints` returns 0 in this module and would
wrongly suggest no DB constraints are declared. Recorded so the next reviewer does not repeat it.
