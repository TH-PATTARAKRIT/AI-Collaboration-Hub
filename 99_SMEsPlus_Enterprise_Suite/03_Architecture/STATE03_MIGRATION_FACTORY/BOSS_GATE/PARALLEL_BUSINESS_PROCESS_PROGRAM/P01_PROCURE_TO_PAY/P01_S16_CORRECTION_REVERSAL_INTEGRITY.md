# P01 — SERIES-16 CORRECTION / CANCELLATION / REVERSAL INTEGRITY

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-07` · Deployment `45a8e08e`

---

## 1. WHAT CORRECTION LOOKS LIKE HERE

**POPULATION:** `account_move`, 183,590 rows.

| Mechanism | Count |
|---|---|
| Moves carrying `reversed_entry_id` — **immutable reversal** | **5,115** |
| — of which posted | 5,057 |
| — of which cancelled | 58 |
| — by type | `entry` 5,024 · `in_refund` 85 · `out_refund` 6 |
| Moves in state `cancel` | **1,866** — `entry` 1,687 · `in_invoice` 156 · `in_refund` 22 · `out_invoice` 1 |
| Moves in state `draft` | 12,581 |
| `account_move_reversal` (the wizard's own table) | **0 rows** |

**CLASSIFICATION: correction in this deployment is predominantly IMMUTABLE REVERSAL, not destructive delete.**
5,115 reversal pairs exist and both halves are retained. That is the healthiest correction profile P01 has
observed in any deployment in this estate.

The wizard table holding 0 rows is expected — `account.move.reversal` is a transient model; its emptiness is
**not** evidence that the wizard was unused, and it is not read as such.

---

## 2. THE DATE A REVERSAL CARRIES

| Relationship | Count |
|---|---|
| Reversal dated **the same day** as its original | 1,741 |
| Reversal dated **differently** | **3,374** |
| Original could not be resolved | **0** |

Day gap (reversal date − original date), over the 3,374:

| min | p50 | p90 | max |
|---|---|---|---|
| **−57** | +13 | +25 | **+211** |

- **2 reversals are dated BEFORE the entry they reverse.**
- **22 reversals are posted in a different month from the original.**

A reversal carrying its own later date is ordinary and correct. A reversal dated **before** its original is not,
and 22 cross-month reversals move an effect out of the period that recognised it.

**And nothing prevents either**, because §3.

---

## 3. NO PERIOD LOCK EXISTS

| Lock field (series-16 vocabulary) | Value |
|---|---|
| `period_lock_date` | **NULL** |
| `fiscalyear_lock_date` | **NULL** |
| `tax_lock_date` | **NULL** |
| `po_lock` | `edit` |

**The lock-field vocabulary is generation-specific.** Series 16 exposes three lock dates; series 18 exposes
five (`fiscalyear`, `tax`, `sale`, `purchase`, `hard`). A finding phrased in one generation's vocabulary
cannot be asserted of the other, and P01's period-lock findings are therefore stated per series.

**All three locks are unset in a deployment with 183,590 journal entries and 169,143 posted ones.**
P01's earlier source finding — that a lock *re-dates rather than refuses* — is **NOT REACHABLE here**: there is
no lock to defeat. The exposure is not a weak control; it is **no control**.

---

## 4. WHAT WAS NOT ESTABLISHED

- **What happens to `stock_valuation_layer` rows when a bill is reset to draft or cancelled.** Series-16
  `stock_account` deletes derived items on some paths; whether that leaves orphaned layers or orphaned journal
  items in this deployment was **assigned as a disproof task to AAS-03 Expert 2** and is not asserted here.
- **Whether `om_data_remove` — installed at `16.0.1.0.1`, and reported by peer P06 to delete ledger data
  without authorisation — has ever run in this database.** Assigned to AAS-03 Expert 4. **Not asserted.**
- The 1,866 cancelled moves were not traced to their downstream effects.

---

## 5. CLASSIFICATION

| Item | Classification |
|---|---|
| Correction is immutable reversal, not destructive delete | **FACT VERIFIED** for the 5,115 observed pairs |
| Both halves of every reversal are retained; 0 unresolvable originals | **FACT VERIFIED** |
| 2 reversals dated before their original | **FACT VERIFIED** |
| 22 reversals posted in a different month | **FACT VERIFIED** |
| No period lock of any kind is configured | **FACT VERIFIED** |
| P01's "lock re-dates rather than refuses" finding | **NOT REACHABLE — no lock configured** |
| Valuation-layer fate on bill cancellation | **UNRESOLVED — EVIDENCE REQUIRED** |
| Whether `om_data_remove` ran here | **UNRESOLVED — under challenge** |
