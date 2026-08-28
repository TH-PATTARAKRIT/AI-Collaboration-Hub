> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 06 — BUSINESS RULE REGISTER

| ID | Rule | Enforcement point | Strength | Evidence |
|---|---|---|---|---|
| BR-01 | An entry must balance: total debit = total credit | Application, `_check_balanced`, on create/write | **Application only** | SE-03 |
| BR-02 | The balance assertion can be suspended for a block of work | `_disable_recursion(..., 'check_move_validity')` | Deliberate bypass | SE-04 |
| **BR-03** | **No database mechanism enforces ENTRY-LEVEL balance** | — | **NONE** | **CORRECTED:** row-level CHECK constraints DO exist on account_move_line (SE-28..31) but cannot aggregate; database contains **0 triggers** (direct pg_restore -l). See CRITICAL_FINDING_REGISTER CF-01 |
| BR-04 | Journal must be compatible with the document type | `@api.constrains('journal_id','move_type')` | Application | SE-06 |
| BR-05 | Taxes must belong to the correct country for the fiscal position | `@api.constrains('line_ids','fiscal_position_id','company_id')` | Application | SE-06 |
| BR-06 | Invoice currency rate must be valid | `@api.constrains('invoice_currency_rate')` | Application | SE-06 |
| BR-07 | Auto-posted bills require a bill date | `@api.constrains('auto_post','invoice_date')` | Application | SE-06 |
| BR-08 | Reset to draft only from posted or cancelled | Guard in `button_draft` path | Application | SE-12 |
| BR-17 | A line may not carry both debit and credit (`credit * debit = 0`) | **DATABASE CHECK** | **Enforced in DB** | SE-28 |
| BR-18 | Balance and amount_currency must agree in sign | **DATABASE CHECK** | **Enforced in DB** | SE-29 |
| BR-19 | Accountable lines require an account | **DATABASE CHECK** | **Enforced in DB** | SE-30 |
| BR-20 | Presentation lines must carry no financial content | **DATABASE CHECK** | **Enforced in DB** | SE-31 |
| BR-21 | Lock enforcement can be bypassed via context sentinel | Application | Deliberate escape | SE-33 |
| BR-09 | Reconciliation permitted only on accounts flagged `reconcile` | Field-driven | Configuration | SE-20 |
| BR-10 | An account in use by tax repartition cannot be deprecated | Guard on write | Application | SE-21 |
| BR-11 | Hash protection cannot be silently disabled once entries are hashed | Guard on journal write | Application | SE-23 |
| BR-12 | Entries on/before an applicable lock date are refused | Company lock dates | Configuration | SE-24 |
| BR-13 | A lock may be overridden only through a time-boxed lock exception | `account.lock.exception` | Configuration + audit | SE-26 |
| BR-14 | `hard_lock_date` is not reversible in the way other locks are | Distinct field, separate semantics | Configuration | SE-24 |
| BR-15 | Every account carries a type from a fixed 19-value set | Required field, enumerated | Model | SE-17 |
| BR-16 | Account type determines whether balance is carried forward across years | `include_initial_balance` derived from type | Model | SE-18 |

## THE FINDING THAT DOMINATES THIS REGISTER — CORRECTED
The database **does** enforce accounting rules — four row-level CHECK constraints on
`account_move_line` (BR-17…BR-20), directly verified present in the dump.

What it does **not** enforce is the *entry-level* identity `Σdebit = Σcredit`, and direct
observation now shows why: a PostgreSQL CHECK constraint evaluates one row at a time and cannot
express an aggregate across an entry's sibling lines, and the database contains **zero
triggers**. The only remaining mechanism is application code, which is suppressible (BR-02).

**Retraction.** The prior round asserted "0 CHECK constraints" from a derived inventory that
cannot represent CHECK constraints. That reasoning is withdrawn. The conclusion stands on
better evidence, and is now stated with the correct scope: *entry-level* balance, not *all*
accounting rules.

**Migration relevance (principle candidate, not design):** migrated accounting entries must be
independently validated for debit/credit balance and not assumed valid merely because records
exist in the source database.
