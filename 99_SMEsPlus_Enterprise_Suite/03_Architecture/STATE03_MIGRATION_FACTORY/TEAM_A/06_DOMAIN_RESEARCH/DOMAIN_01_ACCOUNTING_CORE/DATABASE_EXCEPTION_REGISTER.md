# DATABASE EXCEPTION REGISTER — DOMAIN_01 (CORRECTED, CORR-01)

Round: SMEPLUS-26-08-29-MIG-A-D01-CORR-001 | Supersedes the prior version of this file.

## STATUS CHANGE
```
PRIOR:  A5 = HOLD — pg_restore could not run
NOW:    A5 = DIRECT OBSERVATION OBTAINED
```

| ID | Exception | Resolution this round |
|---|---|---|
| DBX-01 | No local PostgreSQL client | **STILL TRUE** — `pg_restore`/`psql` absent from host |
| DBX-02 | Container runtime down | **RESOLVED** — existing Colima runtime started under control, used, then **stopped**, returning the host to its prior state |
| DBX-03 | Version mismatch PG16 vs PG18 archive | **VERIFIED, THEN RESOLVED** — PG16 `pg_restore` returned `unsupported version (1.16) in file header`; official `postgres:18` image obtained and used |
| DBX-04 | Ephemeral dump copy | **CLOSED** — staged to a host-mounted path solely for read-only listing; **deleted, and the directory removed**, verified |
| DBX-05 | Snapshot not production-representative | **STILL TRUE** — see DATABASE_DATA_PROFILE |
| DBX-06 | "Zero CHECK constraints" (prior claim) | **RETRACTED — SEE BELOW. This was an evidence-scope artefact, not a database fact.** |

## DBX-06 — RETRACTION AND CORRECTION (material)
The prior round concluded, from the approved `Dump_Constraint_Inventory.csv`, that the core
accounting tables carried **zero CHECK constraints**, and inferred that no database mechanism
enforced accounting invariants.

**That inference was unsafe and is retracted.** Two independent checks disprove it:

1. **The inventory cannot represent CHECK constraints at all.** Across all 1,395 tables it
   contains only three constraint types — FOREIGN KEY (5,141), PRIMARY KEY (1,392),
   UNIQUE (149). Zero CHECK rows anywhere. Absence was a property of the *instrument*, not the
   database.
2. **Direct observation proves CHECK constraints exist.** `pg_restore -l` on the dump lists
   four CHECK constraints on `account_move_line`:
   `account_move_line_check_credit_debit`, `_check_amount_currency_balance_sign`,
   `_check_accountable_required_fields`, `_check_non_accountable_fields_null`.
   Their definitions are visible in readable source (`account_move_line.py:463–476`).

**Method lesson recorded:** absence in a derived inventory is not absence in the system.
Any future "X does not exist" finding must first establish that the instrument could have
shown X.

## CONTROLLED ENVIRONMENT RECORD
| Item | Value |
|---|---|
| Runtime | Existing Colima/Docker on host; started for this task, **stopped afterwards** |
| Image | `postgres:18` (official), obtained for archive-version compatibility |
| Network during inspection | `--network none` — inspection ran fully offline |
| Mount | read-only (`:ro`) |
| Operation | `pg_restore -l` **listing only** — no restore, no database created, no server started |
| Data extracted | TOC **metadata only** — object names and types. **No business data, no row values, no customer data, no credentials** |
| Cleanup | dump copy deleted; ephemeral directory removed; both verified |
| Source path | untouched — verified unmodified |
