# DATABASE RELATIONSHIP REGISTER — DOMAIN_01 (CORRECTED, CORR-01)

Evidence level: **DIRECTLY RE-VERIFIED** (pg_restore -l, metadata only).

## STRUCTURAL CONSTRAINTS ON THE CORE PAIR — DIRECTLY OBSERVED
| Table | PRIMARY KEY | FK | CHECK |
|---|---|---:|---:|
| `account_move` | `account_move_pkey` | many (incl. company, currency, fiscal position, asset, campaign, create_uid) | **0 observed** |
| `account_move_line` | `account_move_line_pkey` | many | **4** |

### The four CHECK constraints on `account_move_line` — DIRECTLY VERIFIED
Present in the dump TOC; definitions readable in `account_move_line.py:463–476`.

| Constraint | Definition (from readable source) | What it guarantees |
|---|---|---|
| `check_credit_debit` | `CHECK(display_type IN ('line_section','line_subsection','line_note') OR credit * debit = 0)` | A posting line cannot carry **both** a debit and a credit — one side must be zero |
| `check_amount_currency_balance_sign` | `CHECK(... OR ((balance <= 0 AND amount_currency <= 0) OR (balance >= 0 AND amount_currency >= 0)))` | Company-currency balance and foreign-currency amount must **agree in sign** |
| `check_accountable_required_fields` | `CHECK(... OR account_id IS NOT NULL)` | A real posting line must have an account (**nullability evidence**) |
| `check_non_accountable_fields_null` | `CHECK(display_type NOT IN (...) OR (amount_currency = 0 AND debit = 0 AND credit = 0 AND account_id IS NULL))` | Presentation lines (sections/notes) must carry **no** financial content |

**Analytical point.** These are *row-level* guarantees. PostgreSQL CHECK constraints evaluate
one row at a time and cannot express an aggregate condition across the sibling rows of an
entry. Therefore no CHECK constraint can enforce `Σdebit = Σcredit` for a move — this is a
property of the constraint mechanism, not an omission by the vendor.

## TRIGGERS AND RULES — DIRECTLY VERIFIED
- **TRIGGER count across the entire database: 0.** No trigger enforces any accounting invariant.
- **RULE count: 9**, every one a view `_RETURN` rule (fleet_vehicle_cost_report,
  helpdesk_sla_report_analysis, helpdesk_ticket_report_analysis, hr_recruitment_report,
  hr_referral_reward_report, planning_analysis_report, report_project_task_user,
  report_project_task_user_fsm, vendor_delay_report). **None on an accounting table; none
  enforcing anything.**

## REFERENTIAL SHAPE
```
account_journal ─1:N─> account_move ─1:N─> account_move_line ─N:1─> account_account
res_company ─1:N─> account_journal / account_account / account_move   (company boundary)
account_move ─self─> reversed_entry_id                                 (reversal linkage)
account_partial_reconcile ─N:1─> account_full_reconcile
account_lock_exception ─N:1─> res_company
account_move ─N:1─> res_currency                                       (multi-currency boundary)
```
FK edges database-wide: **5,141** (directly confirmed, matching prior evidence exactly).

## DENORMALIZED COLUMNS (consistency obligations, not relationships)
`account_move_line.parent_state`, `.journal_id`, `.company_currency_id` — derived data.
Recompute on migration; do not carry as authority.
