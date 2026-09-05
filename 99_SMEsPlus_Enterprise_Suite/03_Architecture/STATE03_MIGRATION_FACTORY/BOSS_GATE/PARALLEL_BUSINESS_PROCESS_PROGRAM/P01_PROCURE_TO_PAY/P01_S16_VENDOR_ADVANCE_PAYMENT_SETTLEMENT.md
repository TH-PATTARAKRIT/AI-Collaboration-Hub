# P01 — SERIES-16 VENDOR ADVANCE / PARTIAL PAYMENT / SETTLEMENT

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-05` · Deployment `45a8e08e`

---

## 1. POPULATION

| Object | Rows |
|---|---|
| `account_payment` | **22,468** — supplier **19,575** / customer 2,893 |
| Supplier payments carrying `wt_tax_id` | 4,941 (25.24%) |
| `account_partial_reconcile` | extracted, 8.49 MB |
| `account_full_reconcile` | extracted, 3.00 MB |
| `purchase_request` | **2,163** — approved 2,147 / to_approve 4 / draft 7 / rejected 5 |
| `scgl_purchase_advance_payment` | **installed** at 16.0.1.0.0; source located via the host index (18 exact-version copies) |

---

## 2. THE P05 DISAGREEMENT IS PRESERVED, NOT RESOLVED

P01 recorded in an earlier round, from source, that the vendor-advance module's
**"deduct down payments" control is inert** — the flag `deduct_down_payments` defaults to `True` and its only
code reference is a **commented-out line**.

**This round does not resolve that against the deployment**, and it does not withdraw it.

- The module **is installed here** at the version P01 read.
- Whether the deployment exercises the advance/down-payment path, and what the inert control costs in
  practice, **was not measured this round**. Reconciliation of `account_partial_reconcile` against
  down-payment lines is a substantial piece of work that was not reached.
- Peer **P05** owns expense-to-pay and has its own position on the same module.

**`Peer Position ≠ Peer Decision ≠ Boss Decision.`** P01 does not overrule P05 and does not adopt P05's
reading in place of its own measurement. The disagreement stands, both positions preserved.

**CLASSIFICATION: `UNRESOLVED — EVIDENCE REQUIRED`.** Recorded as blocker `S16-B-02`.

---

## 3. WHAT WAS ESTABLISHED

| Item | Evidence | Classification |
|---|---|---|
| Supplier payment volume | 19,575 | **FACT VERIFIED** |
| Withholding applies to a minority of supplier payments | 4,941 (25.24%) | **FACT VERIFIED** |
| Purchase requisition is heavily exercised | 2,163 requests, **2,147 approved** | **FACT VERIFIED** |
| The rejection path is used | 5 rejected | **FACT VERIFIED** |
| `scgl_purchase_advance_payment` installed | `ir_module_module` | **FACT VERIFIED** |
| Advance → bill deduction behaviour in this deployment | — | **NOT MEASURED** |
| Partial-payment withholding arithmetic | — | **NOT MEASURED**; assigned to AAS-03 Expert 3 |
| Residual payable after settlement | — | **NOT MEASURED** |

---

## 4. AP SETTLEMENT — MEASURED AFTER THE FIRST DRAFT OF THIS DOCUMENT

The reconciliation join recorded below as "not attempted" **was** attempted later in the same run, and it
returned. This section replaces that part of the gap; §5 states what still remains.

**POPULATION:** `account_move_line` rows on the **11** accounts of type `liability_payable` — **54,137 items**.
**POSITIVE CONTROL:** of the 52,996 items flagged `reconciled`, **0 carry a non-zero `amount_residual`** —
the field behaves, so a non-zero residual is a measurement rather than noise.

| Measure | Value |
|---|---|
| AP journal items | **54,137** |
| Reconciled | **52,996 — 97.89%** |
| Carrying `full_reconcile_id` | 52,966 |
| Carrying `matching_number` | 52,984 |
| **Open items** (unreconciled, non-zero residual) | **1,141** |
| Total open residual | **−฿103,516,686.24** |

**A 97.89% reconciliation rate is the healthiest settlement profile P01 has measured in any deployment.**

### 4.1 But the open residual is not one population

| Move state | Open items | Residual |
|---|---|---|
| **`posted`** | 539 | **−฿98,745,661.71** |
| **`cancel`** | **559** | **−฿18,153,699.21** |
| **`draft`** | 43 | **+฿13,382,674.68** |

**Roughly half of the open AP items sit on documents that are cancelled or still draft.**
The cancelled group is 559 items — `entry` 391, `in_invoice` 147, `in_refund` 21 — and **280 of them date
from 2023**.

### 4.2 What this does and does not mean

**It does not mean ฿18.15M is owed.** `amount_residual` is a stored computed value; on a cancelled document it
may simply be stale, and cancelled moves are normally excluded from payables reporting. **No claim is made that
these are live obligations.**

**What it does mean** is that the AP figure this deployment reports depends entirely on whether the reporting
layer filters by move state:

| Basis | Open AP |
|---|---|
| Posted only | **−฿98,745,661.71** |
| Posted + cancelled + draft | **−฿103,516,686.24** |

**A ฿4.77 million spread between two defensible readings of the same field**, with no lock date and no period
close to fix either. **Which basis any given report uses was not established**, and that is the question — not
the residual itself.

**CLASSIFICATION:** the counts and residuals are **FACT VERIFIED**, with a positive control.
Whether cancelled-document residuals reach any report is **UNRESOLVED — EVIDENCE REQUIRED**, and the
reporting judgement is **P08's**. Routed there and to **P11**.

---

## 5. WHY THE REST OF THIS DELIVERABLE IS SHORT, AND SAYING SO

The prompt asked for a full advance → partial payment → WHT → reconciliation → final deduction → residual
lineage. **This round reached the populations and not the lineage.**

The reconciliation join (22,468 payments against 447,384 journal items and two reconcile tables) is the
largest remaining piece of executable work in this package, and it was **not** attempted rather than
attempted and estimated. Stating that plainly is preferable to a settlement narrative built on counts.

**What §4 did NOT reach**, and what remains the next action: whether **advances are deducted from final
bills**, the **partial-payment withholding arithmetic** across the 4,941 supplier payments carrying
`wt_tax_id`, and the **residual payable after settlement per vendor**. The AP-level reconciliation is now
measured; the **advance-specific** lineage is not, and the P05 disagreement in §2 is untouched by §4.
