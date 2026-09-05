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

## 4. WHY THIS DELIVERABLE IS SHORT, AND SAYING SO

The prompt asked for a full advance → partial payment → WHT → reconciliation → final deduction → residual
lineage. **This round reached the populations and not the lineage.**

The reconciliation join (22,468 payments against 447,384 journal items and two reconcile tables) is the
largest remaining piece of executable work in this package, and it was **not** attempted rather than
attempted and estimated. Stating that plainly is preferable to a settlement narrative built on counts.

**It is recorded as the NEXT EXACT ACTION in `P01_AUTO_RESUME_STATE.md`.**
