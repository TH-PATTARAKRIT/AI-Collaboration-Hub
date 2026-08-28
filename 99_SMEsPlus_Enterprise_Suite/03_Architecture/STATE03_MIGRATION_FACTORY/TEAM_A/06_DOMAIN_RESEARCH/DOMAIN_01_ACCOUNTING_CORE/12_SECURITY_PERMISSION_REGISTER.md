> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 12 — SECURITY / PERMISSION REGISTER

Scope note: full security model belongs to a separate domain. Only accounting-core-coupled
observations are recorded here.

| ID | Observation | Evidence |
|---|---|---|
| SEC-01 | Lock dates have **per-user computed variants** (`user_fiscalyear_lock_date`, `user_tax_lock_date`, `user_sale_lock_date`, `user_purchase_lock_date`) — the effective lock depends on who is acting | SE-25 |
| SEC-02 | Lock exceptions are records with an audit-trail interrogation path (`action_show_audit_trail_during_exception`) — overrides are meant to be reviewable | SE-26 |
| SEC-03 | Disabling journal hash mode is guarded, not merely permissioned | SE-23 |
| SEC-04 | Account deprecation is guarded by usage, not by role | SE-21 |
| SEC-05 | Security/access inventory for the wider system exists in prior evidence (473 records) but was **not** re-derived for this domain | prior evidence P5 |

**Not researched here:** record rules, group definitions, field-level access, multi-company
access rules. Deferred to the security domain.

**Clean-room note:** no credentials, tokens or access data were read, recorded or committed.
