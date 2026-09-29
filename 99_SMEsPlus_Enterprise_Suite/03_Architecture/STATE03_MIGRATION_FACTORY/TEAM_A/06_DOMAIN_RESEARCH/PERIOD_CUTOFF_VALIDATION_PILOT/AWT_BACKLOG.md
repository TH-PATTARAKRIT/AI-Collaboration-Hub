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

- **Hypothesis to verify, refined 2026-09-30 (source-code tier, Handoff `D-07`)**: A Hard Lock genuinely blocks entry creation/modification before its date via a `UserError`, with no override found in source; a *new* entry dated inside a lock window is instead silently rolled forward to the first open day at create/post time (a second, distinct path from the hard block — both need runtime confirmation of exactly when each fires).
- **Required environment**: Same, plus a Hard Lock date set in the past relative to a test entry.
- **Runtime action**: Attempt to create/modify an entry dated before the Hard Lock; separately, attempt to create a fresh entry dated inside the lock window and observe whether it is blocked or silently date-shifted.
- **Expected observable result**: Blocked, with no visible override option — or, for the second case, an unexpected date auto-shift the user did not request.
- **Evidence required**: UI/error behavior for both paths.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Confirmation of "no override," which path fires when, and what happens if a genuine correction is needed after Hard Lock.

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 4 (all)
CAPSTONE TEST : PCO-F03/F04, unifying Gx1/Gx2/Gx4/Gx5/Gx6 valuation-timing findings into one AWT session
```
