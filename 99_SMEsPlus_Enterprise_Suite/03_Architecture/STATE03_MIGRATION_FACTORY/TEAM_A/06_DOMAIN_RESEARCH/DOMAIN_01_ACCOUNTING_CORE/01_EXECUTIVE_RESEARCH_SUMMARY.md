> Domain: DOMAIN_01 — Accounting Core | Team A (Maker) | Session SMEPLUS-26-08-29-MIG-A-D01-ACCOUNTING-CONT-001
> Source path READ ONLY. No target design. No coding. Boss is sole Final Approver.
> STEP linkage: **TBD / BASELINE LINKAGE REQUIRED** — STEP0303R5 is prior governance/planning evidence only.

# 01 — EXECUTIVE RESEARCH SUMMARY

## What Accounting Core IS in the reference system
A single generic journal-entry model. One header object (`account.move`) and one line object
(`account.move.line`) carry **every** financial document — journal entries, customer invoices,
vendor bills, credit notes and reversals are all the same two tables differentiated by a type
field and a journal. Accounts are a flat coded list typed by a 19-value enumeration; journals
classify and control entries; a three-state lifecycle governs posting.

## The six critical findings (canonical — see CRITICAL_FINDING_REGISTER.md)
Registered critical findings: **6**. Neutralization records: **5** (N-02 covers CF-04 and CF-06).

**CF-01 — Entry-level balance has no database enforcement. [CORRECTED THIS ROUND]**
`Σdebit = Σcredit` is asserted only by `_check_balanced` (`account_move.py:2765`), which is
wrapped in `_disable_recursion(..., 'check_move_validity')` and can be switched off.
Direct `pg_restore -l` observation now establishes *why* no database backstop exists: the four
CHECK constraints that do exist on `account_move_line` are **row-level** (credit×debit=0, sign
agreement, required account, empty presentation lines) and cannot express an aggregate across
an entry, and the database contains **zero triggers**.
*The prior round's reasoning — "the inventory shows zero CHECK constraints" — was unsafe and is
retracted; that inventory cannot represent CHECK constraints at all. The conclusion survives on
stronger evidence.* Data-level balance remains **EVIDENCE_MISSING**.

**CF-02 — Tamper evidence is opt-in per journal** (`restrict_mode_hash_table`).

**CF-03 — Period control is six lock-date fields** plus per-user computed variants, a
lock-exception object, and a `BYPASS_LOCK_CHECK` context escape.

**CF-04 — Reversal is a relationship, not a state** (`reversed_entry_id`); states are only
draft / posted / cancel.

**CF-05 — Money is exact decimal** (`numeric`) end to end.

**CF-06 — Posted history is mutable** — `button_draft` accepts `posted` and `cancel`.
Independent triangulation shows SAP Business One *prevents* this, so it is vendor-specific
divergence, not industry norm.

## Evidence position
`account` is LGPL-3 and was read at source level. Enterprise accounting modules
(`account_accountant`, `account_reports`, `account_asset`, `account_budget`, `accountant`) are
OEEL-1 and were **not read** — metadata only.
Database evidence is now **DIRECTLY RE-VERIFIED** via offline `pg_restore -l` (28,648 TOC
entries). Row-level behaviour remains unobserved: no restore was performed and the snapshot is
a configuration/UAT database.
External triangulation is **PARTIALLY CLOSED** — 3 of 9 targets triangulated against real
public sources; Thai statutory questions remain open.
