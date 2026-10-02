> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | AWT Backlog | Not executable in this container

# AWT BACKLOG — Gx6

### PCO-F03 / PCO-F04 — Stock Closing + accrual mechanism (formal confirmation of the resolution)

- **Criticality**: C1
- **Hypothesis to verify**: The full resolved model — no entry at movement, entry at invoice, period-end Stock Closing + accrual sweeps up the rest — holds exactly as documented.
- **Required environment**: Same as the combined Gx1/Gx2/Gx4/Gx5 valuation-timing session — this becomes the capstone test.
- **Configuration prerequisite**: A receipt and a delivery, each left uninvoiced past a simulated period boundary.
- **Runtime action**: Advance to period close with both movements uninvoiced; run the accrual-entry review screen; generate the Stock Closing entry; confirm the Balance Sheet reflects the movements' value via the accrual, then confirm the accrual reverses correctly once the real invoice/bill posts in the next period.
- **Expected observable result**: Full round-trip: accrual created → Balance Sheet complete → real invoice posts → accrual reverses → no double-counting.
- **Cross-module observation**: Run together with Gx1 `GRV-F04`, Gx2 `SDV-F05`, Gx4 `IAV-F03`, Gx5 `PDT-F01` tests in one combined session — this is now the unifying test for all of them.
- **Accounting/stock effect**: Primary target — this is the capstone test of the whole cross-Gx valuation-timing question.
- **Reversal scenario**: The accrual's own Reversal Date IS the reversal scenario.
- **Evidence required**: Full before/after/reversal journal entry trail.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Runtime confirmation of the full round-trip.

### PCO-F01 — Lock Dates

- **Hypothesis to verify, refined 2026-09-30 (source-code tier, Handoff `D-07`; further refined same day, `MODULE_account.md` S2-CANDIDATE independent re-trace)**: A Hard Lock genuinely blocks *editing* of a posted entry via a `UserError`, TEST-confirmed to have no exception/override of any kind; a *new* entry dated inside a lock window is instead silently rolled forward to the first open day at `_post` time — this is now understood as the actual per-post mechanism, not an unreconciled second path. **New, higher-priority sub-hypotheses**: (a) the `bypass_lock_check` context flag, if reachable from any UI action or installed module, would defeat the entire lock model — its reachability needs runtime/code-path confirmation before anything else in this backlog item; (b) lock dates are evaluated up the parent-company chain (Hard Lock = max across the chain) — needs confirmation in a real multi-company hierarchy; (c) Community's "only accountant may edit validated entries" rule resolves to "anyone" — confirm whether any installed module (Enterprise or custom) actually restricts this in practice.
- **Required environment**: Same, plus a Hard Lock date set in the past relative to a test entry; a parent/child company pair for (b); at least two user roles for (c).
- **Runtime action**: Attempt to create/modify an entry dated before the Hard Lock; separately, create a fresh entry dated inside the lock window and observe the silent date-shift; search the codebase/UI for any caller of `bypass_lock_check`; set a Hard Lock on a parent company and confirm it constrains the child; attempt to edit a "checked"/validated entry as a non-accountant user.
- **Expected observable result**: Blocked with no override for editing; an unexpected date auto-shift for new entries in the window; `bypass_lock_check` either unreachable (confirms the control is sound) or reachable from somewhere (a real finding); lock inheriting down to the child company; edit permission either genuinely open to "anyone" (confirms the Community gap) or restricted by an installed extension.
- **Evidence required**: UI/error behavior for all five sub-cases; a `bypass_lock_check` caller trace if runtime access allows a codebase-wide search instead.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: All of the above — `bypass_lock_check`'s reachability is now the single highest-priority item in this backlog entry.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 4 (all)
CAPSTONE TEST : PCO-F03/F04, unifying Gx1/Gx2/Gx4/Gx5/Gx6 valuation-timing findings into one AWT session
```
