# 45 — P05 PETTY CASH DEPLOYMENT RECLASSIFICATION

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E05`

> ## HEADLINE: `TZ-01` IS CONTRADICTED BY PRODUCTION DATA ON THE TARGET PLATFORM

## 1. What Was Claimed, Across Two Rounds

| Round | Claim |
|---|---|
| `P05#02` | **`TZ-01`** — *"Petty-cash spending never credits the petty-cash account. The float balance is permanently overstated and its control is a one-way ratchet."* Upheld on four independent source lines and promoted to `FACT VERIFIED`. |
| `P05#03` | Reclassified **`LATENT`** — *"`hr_expense_petty_cash` is installed in none of the six registries."* |

**Both are now wrong**, and in opposite directions.

## 2. Deployment Reality

`idemo18_uat` (Odoo **18.0**, the target platform, 4 companies):

| Fact | Value |
|---|---|
| `hr_expense_petty_cash` | **INSTALLED**, version `18.0.1.2` |
| `petty_cash` holder records | **8** (3 active, 5 archived), limits 5,000–50,000 |
| `hr_expense` rows | **993** |
| — `payment_mode = 'petty_cash'` | **634 (63.8%)** |
| — `payment_mode = 'company_account'` | 357 |
| — `payment_mode = 'own_account'` | **2** |
| Expenses with `petty_cash_id` set | 660 |
| Expense sheets | 979, of which **934 `done`** |

> **Petty cash is not a marginal feature on the target platform. It is the dominant expense
> mechanism — 634 of 993 claims — while the employee-reimbursement path that P05 traced in most
> depth is used exactly twice.** The prior rounds' emphasis was inverted relative to real usage.

## 3. The Decisive GL Test — `TZ-01` Contradicted

Traced: petty-cash expense → sheet → `account_move` (via `expense_sheet_id`) → `account_move_line`,
taking every credit line (`balance < 0`).

| Credit account | `account_type` | Lines | Is it a `petty_cash.account_id`? |
|---|---|---|---|
| `204` | `asset_cash` | **275** | **YES** |
| `336` | `asset_cash` | **111** | **YES** |
| `339` | `asset_cash` | 1 | no (adjacent cash account) |

**386 of 387 credit lines land on a petty cash account**, carrying the **holder's** `partner_id`
(1838, 2016 — matching `petty_cash.partner_id`). Not one lands on an employee payable.

> **`TZ-01` is class `E — CONTRADICTED` as an operational claim.** The accounting outcome in the
> deployed v18 system is **correct**: petty-cash spending credits the petty cash account. The claim
> that it "never" does is false, and the float is **not** overstated by this mechanism.

## 4. Why the Source Analysis Reached the Opposite Conclusion

The source facts remain true and were re-verified: `_get_account_move_line_values` occurs **0 times**
in the v18 Enterprise tree, and the module's tests are a non-executing v14 artefact. Those are class
**A** statements about **the source copy at `smeplus-custom/addons`**.

But the deployed entries do not match that copy's code path either:

| Observation | Implication |
|---|---|
| Moves are `move_type = 'entry'` on **general** journals 45/46 | not the `own_account` branch, which produces `in_invoice` |
| `origin_payment_id` is **null on all 387** | not the `company_account` branch, which creates a payment |
| Credit account is `petty_cash.account_id` (204/336), **not** the petty cash journal's default (205/337) | something reads the holder's account explicitly |

**Conclusion: the deployed `hr_expense_petty_cash` is not the source copy that was analysed**, despite
both carrying version string `18.0.1.2`. Project memory warned that three near-identical custom copies
exist at differing version strings and that which is deployed is unknown — that warning is now
**realised**, not hypothetical.

> **This is the structural finding of this continuation, and it is larger than `TZ-01`:**
> **every source-only P05 finding rests on a code copy that is not demonstrably the deployed code.**
> Recorded as `U-16`; it bounds `10`, `05`, `07` and every `LATENT` classification in `26`.

## 5. What Survives, and It Is Not Small

The GL redirection works. Two findings survive the contradiction and are **newly measured**:

| ID | Finding | Evidence | Class |
|---|---|---|---|
| **`PC-01`** | **238 of 625 petty-cash sheets (38.1%) have no linked journal entry — and 206 of those are state `done`.** A third of the petty-cash population reports fully processed with no traceable accounting entry attached. | 625 petty-cash sheets; 387 with a move (all `done`); 238 without (206 `done`, 23 `approve`, 8 `submit`, 1 `draft`) | **FACT VERIFIED** (v18 target) |
| `PC-02` | `TZ-02` cross-company leak **NOT OBSERVED**: account 336 is posted to only by company 2, account 204 only by company 1. Multiple holders share an account (1612/1769/10156 → 336; 1499/2016 → 204), but each partner appears once, so the global `unique(partner_id)` constraint is not exercised. | 4 companies present | `TZ-02` → **`B` — NOT OBSERVED IN SEARCHED SCOPE.** Source defect stands; consequence not realised here. |

`PC-01` is the same audit-trail defect as `SR-07`, now measured at production scale on the target
platform: whether by the severing paths (`expense_sheet_id` nulled) or by entries never created, **a
`done` sheet is not a guarantee that a traceable entry exists.** Its cause is `NOT YET SEARCHED`
(class **C**) and is carried as `U-17`.

## 6. Reclassification

| Item | Was | Now |
|---|---|---|
| `TZ-01` operational claim | `FACT VERIFIED` → `LATENT` | **`E` — CONTRADICTED. Withdrawn.** |
| `TZ-01` source observations | `FACT VERIFIED` | **Upheld for the analysed source copy only**, bounded by `U-16` |
| `TZ-02` | `LATENT` | **`B` — source defect stands, consequence not observed** |
| **`PC-01`** *(new)* | — | **LIVE — OBSERVED**, 38.1% of the petty-cash population |
| Petty cash overall | "headline defect" | **The GL works. The audit trail is the defect.** |

## 7. Does Another Installed Module Provide Petty-Cash Behaviour?

Declared search over the `idemo18_uat` installed set (361 modules), pattern
`petty|imprest|cash[ _-]?float|revolving`: only `hr_expense_petty_cash`. **Class `A` within that
registry.** No competing implementation. The behaviour observed is that module's.
