> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 07 — STATE / EVENT REGISTER

## Entry lifecycle — three states only
```
        ┌───────────────── button_draft ──────────────────┐
        │                                                 │
     [draft] ── action_post ──> [posted] ── button_cancel ──> [cancel]
        ▲                                                     │
        └───────────────── button_draft ──────────────────────┘
```
| State | Meaning | Evidence |
|---|---|---|
| draft | Editable, not in the ledger | SE-01 |
| posted | Committed to the ledger, numbered | SE-01, SE-10 |
| cancel | Voided but retained | SE-01, SE-11 |

**There is no `reversed` state.** Reversal is a relationship (`reversed_entry_id`) to a
separate move. Treating "reversed" as a status is a migration trap. Evidence: SE-07..09.

## Second, independent status
`payment_state` (draft/posted/cancel among others) is maintained separately from `state` —
a document has both a *ledger* status and a *settlement* status. Evidence: SE-14.

## Denormalized state copy
`account_move_line.parent_state` mirrors the header state onto every line. It is derived data
with a consistency obligation, not an independent fact. Evidence: DB relationship register.

## Events observed
| Event | Trigger | Consequence |
|---|---|---|
| EV-01 Entry created | create | Balance asserted; draft |
| EV-02 Entry posted | action_post | Name assigned; state posted; parent_state propagated; hash/secure sequence advanced where enabled |
| EV-03 Entry reset | button_draft | Returns to editable; history mutated |
| EV-04 Entry cancelled | button_cancel | Voided, retained |
| EV-05 Reversal posted | post of reversal | Auto-reconciled against the original (SE-09) |
| EV-06 Reconciliation completed | matching | partial rows grouped into a full reconcile |
| EV-07 Lock date set | company config | Prior-period entry attempts refused |
| EV-08 Lock exception granted | account.lock.exception | Narrow, time-boxed, audit-interrogable override |
