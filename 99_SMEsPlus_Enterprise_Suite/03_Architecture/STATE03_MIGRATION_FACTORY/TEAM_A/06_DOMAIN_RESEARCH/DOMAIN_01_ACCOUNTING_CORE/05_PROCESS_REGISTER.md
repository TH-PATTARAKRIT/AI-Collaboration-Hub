> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 05 — PROCESS REGISTER

## PR-01 — Record a journal entry
Create header (journal, date, company) → add lines (account, debit/credit, optional
amount_currency and analytic) → balance asserted on write → entry sits in `draft`.
Evidence: SE-01, SE-03, SE-05.

## PR-02 — Post an entry
`action_post` → `_post(soft=True)` → name assigned from journal sequence (or gapless secure
sequence when the journal is hash-protected) → state becomes `posted` → `parent_state`
denormalized onto every line. Evidence: SE-10, SE-13, DB relationship register.

## PR-03 — Correct a posted entry (two routes observed)
Route A — **reset to draft**: `button_draft`, permitted from posted or cancel, then edit and
re-post. Route B — **reverse**: `_reverse_moves` creates an opposing entry linked by
`reversed_entry_id`; on posting it auto-reconciles against the original.
Route A mutates history; Route B preserves it. Both exist; nothing in the core forces Route B.
Evidence: SE-07..09, SE-11, SE-12.

## PR-04 — Cancel an entry
`button_cancel` → state `cancel`. Cancelled entries remain in the ledger and can be reset to
draft. Evidence: SE-11, SE-12.

## PR-05 — Reconcile items
Items on accounts flagged `reconcile` are matched; matches accumulate as
`account_partial_reconcile` rows and, when fully matched, group under `account_full_reconcile`.
Evidence: CAP-01, CAP-09, DB inventory.

## PR-06 — Close a period
A lock date is set on the company (fiscal year, tax, sale, purchase, or hard). Entries dated
on/before the applicable lock are refused. A time-boxed `account.lock.exception` can grant a
narrow override. Evidence: SE-24..26.

## PR-07 — Multi-company posting
Journal, account and move each carry company; lines carry company currency related from the
move. Entries do not span companies. Evidence: SE-15, CAP-11.

**Deferred processes (dependency only):** invoice/bill capture, payment matching, tax
computation and filing, depreciation posting, stock valuation posting, statutory reporting.
