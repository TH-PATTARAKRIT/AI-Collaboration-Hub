> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 16 — EDGE CASE REGISTER

| ID | Edge case | Why it matters | Evidence |
|---|---|---|---|
| EC-01 | **Unbalanced entry persisted** | Entry-level balance is application-only and suppressible (BR-01/02); no DB mechanism can catch it — row-level CHECKs cannot aggregate and there are **0 triggers**. Whether it has actually happened in the snapshot is EVIDENCE_MISSING | SE-03, SE-04, CF-01 |
| EC-02 | Computed stored fields unreliable mid-write | Source comment explicitly warns `_get_unbalanced_moves` cannot assume computed stored fields during create/write | SE-05 |
| EC-03 | Posted entry reset to draft | History is mutable by design; a posted, numbered entry can return to editable | SE-11, SE-12 |
| EC-04 | Cancelled entry resurrected | `button_draft` accepts `cancel` as a source state | SE-12 |
| EC-05 | Reversal treated as a state | There is no `reversed` state; migration logic keying on status will mis-handle reversals | SE-07 |
| EC-06 | Reversal not reconciled | Auto-reconciliation happens on posting a *draft* reversal of a *posted* original; other paths may leave them unmatched | SE-09 |
| EC-07 | Journal without hash protection | Entries carry no `inalterable_hash`; tamper evidence absent for that journal | SE-22 |
| EC-08 | Hash mode disabled after use | Guarded, but the guard is application-level | SE-23 |
| EC-09 | Six locks disagreeing | Fiscal-year, tax, sale, purchase and hard locks can hold different dates simultaneously; per-user variants add another axis | SE-24, SE-25 |
| EC-10 | Lock exception window | A time-boxed exception permits writes into an otherwise locked period | SE-26 |
| EC-11 | `hard_lock_date` semantics | Distinct from the other locks; must not be modelled as "just another lock" | SE-24 |
| EC-12 | Denormalized `parent_state` drift | Line state can, in principle, disagree with header state | DB |
| EC-13 | Three monetary columns, two degrees of freedom | debit/credit/balance can disagree if written independently | DB, MM-02 |
| EC-14 | System-generated lines | Tax/rounding/payment-term lines coexist with user lines in one entry | AU-08 |
| EC-15 | Account deprecated while in use | Guarded only against tax repartition, not against all usage | SE-21 |
| EC-16 | Line with both debit and credit | **Prevented at database level** by `check_credit_debit` — a genuine DB guarantee | SE-28 |
| EC-17 | Currency amount sign disagreeing with balance | **Prevented at database level** by `check_amount_currency_balance_sign` | SE-29 |
| EC-18 | Lock bypassed via context sentinel | `BYPASS_LOCK_CHECK` / `bypass_lock_check` provides an explicit escape from lock enforcement | SE-33 |
