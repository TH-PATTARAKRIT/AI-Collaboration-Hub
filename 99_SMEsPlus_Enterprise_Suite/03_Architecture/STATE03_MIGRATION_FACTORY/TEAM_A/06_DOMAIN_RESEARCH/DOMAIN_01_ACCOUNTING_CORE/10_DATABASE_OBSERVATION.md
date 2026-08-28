# 10 — DATABASE OBSERVATION (A5)

Method: **read-only**. No production DB accessed. No destructive command. No restore performed.
No raw business data, customer data or credentials recorded or committed.

## TOOLCHAIN STATUS — RESOLVED THIS ROUND (CORR-01)
```
DB_RESTORE_TOOLCHAIN = OBTAINED (controlled ephemeral)
EVIDENCE LEVEL       = DIRECTLY RE-VERIFIED (metadata only)
```
The existing container runtime was started under control, an official `postgres:18` image was
used (PG16 had returned `unsupported version (1.16) in file header` — directly verified), and
`pg_restore -l` was executed **offline (`--network none`) against a read-only mount**.
Listing only: no restore, no database created, no server started, no row read.
The staged dump copy was deleted and its directory removed; the runtime was stopped.

## DIRECTLY VERIFIED
Archive: created 2026-06-14 14:41:20 UTC · db `iTEST02` · **28,648 TOC entries** · gzip ·
CUSTOM · dump version 1.16-0 · from PostgreSQL **18.4** · owner role `efaplus`.

Object census: FK CONSTRAINT 5,141 · SEQUENCE 2,871 · TABLE 2,763 · CONSTRAINT 1,860 ·
INDEX 1,808 · TABLE DATA 1,395 · DEFAULT 888 · VIEW 36 · RULE 9 · EXTENSION 6 ·
**TRIGGER 0**.

Accounting core objects, constraints, CHECK constraints, lock objects, currency and company
boundary objects: all confirmed present. Detail in DATABASE_OBJECT_INVENTORY.md and
DATABASE_RELATIONSHIP_REGISTER.md.

## RECONCILIATION WITH PRIOR EVIDENCE
Tables 1,395 and FK 5,141 **confirmed identical** to the prior approved inventory.
CHECK constraints: prior inventory reported none and **could not represent them**; direct
observation finds them present. Triggers and rules: **newly established**, not previously captured.

## MONETARY COLUMN TYPES — VERIFIED
`debit`, `credit`, `balance`, `amount_currency` are all `numeric`. Exact decimal, not float.

## DENORMALIZATION OBSERVED
`account_move_line.parent_state` duplicates header state onto every line — derived data with a
consistency obligation.
