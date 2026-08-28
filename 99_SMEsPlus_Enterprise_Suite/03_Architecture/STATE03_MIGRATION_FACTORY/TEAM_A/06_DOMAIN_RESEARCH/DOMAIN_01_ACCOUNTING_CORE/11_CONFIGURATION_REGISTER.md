> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 11 — CONFIGURATION REGISTER

Behaviour in this domain is heavily configuration-driven. Configuration is **data that changes
accounting outcomes**, so it must be treated as in-scope evidence, not environment noise.

| ID | Configuration | Level | Effect |
|---|---|---|---|
| CFG-01 | `restrict_mode_hash_table` | Journal | Turns tamper-evidence on. **Off by default** — a journal is only secure if configured so |
| CFG-02 | `restrictive_audit_trail` | Company | Tightens audit-trail behaviour |
| CFG-03 | `fiscalyear_lock_date` | Company | Blocks entries on/before the date |
| CFG-04 | `tax_lock_date` | Company | Blocks tax-relevant changes |
| CFG-05 | `sale_lock_date` | Company | Blocks sales-side entries |
| CFG-06 | `purchase_lock_date` | Company | Blocks purchase-side entries |
| CFG-07 | `hard_lock_date` | Company | Strongest lock; distinct semantics from the others |
| CFG-08 | `user_*` lock variants | Company/user | Computed per-user effective lock dates |
| CFG-09 | `account.lock.exception` | Record | Time-boxed override of a lock, with audit interrogation |
| CFG-10 | `reconcile` per account | Account | Enables matching |
| CFG-11 | `deprecated` per account | Account | Retires an account, guarded against tax usage |
| CFG-12 | `include_initial_balance` | Account (derived) | Year-end carry-forward behaviour |
| CFG-13 | Journal sequence prefix/number | Journal | Entry numbering shape |
| CFG-14 | Chart template | Company | Initial chart of accounts |

**Observation.** Five of the fourteen items above concern *period locking*. The reference
system expresses "the books are closed" through a combination of six fields, per-user computed
variants, and an exception object — not through one state.
