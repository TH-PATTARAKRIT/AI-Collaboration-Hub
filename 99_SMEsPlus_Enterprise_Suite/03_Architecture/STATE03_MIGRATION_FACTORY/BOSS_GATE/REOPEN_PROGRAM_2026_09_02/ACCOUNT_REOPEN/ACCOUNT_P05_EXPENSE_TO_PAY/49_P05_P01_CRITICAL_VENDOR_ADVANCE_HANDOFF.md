# 49 — P05 → P01 CRITICAL VENDOR ADVANCE HANDOFF

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E08`
**P05 discovered, verified and routes. P05 does not adjudicate P01 architecture.**

## 1. Corrected Framing — read before the evidence

Round 2 routed this as *"live in all four real business databases"* with an asserted duplicate-payment
loss. **This continuation narrows it on three counts, and P01 should work from the narrowed version:**

1. The module is **not installed on the v18 target platform** (`idemo18_uat`).
2. It is installed in **four of six** read registries — `iSMEs` v16, `iEVING`, `BK12MAY26`, `iTEST02`.
3. It has been **exercised 21 times, in `iSMEs` v16 only**; zero rows in the three v19 databases.
   **No double-billing has been observed.** The source defect is verified; the financial effect is not.

## 2. Evidence

| Item | Finding | Class |
|---|---|---|
| `H-P01-1` | **Vendor down payments are never deducted from the final bill.** `deduct_down_payments` has four references; its only consumer is **commented out** (`wizard/purchase_advance.py:178`); the live branch calls core `action_create_invoice()` (`:179`), which knows nothing of the flag. | **A** over the custom tree (source) |
| `H-P01-1a` | **Financial effect NOT demonstrated.** No extraction of the 21 wizard rows against their purchase orders and resulting bills was performed. | **C — NOT YET SEARCHED** |
| `H-P01-2` | **`sudo()` vendor-bill creation.** ACL grants full CRUD to `base.group_user`; `_create_bill` elevates. Classification: **`PARTIAL AUTHORIZATION`** — the `account.move` ACL gate is bypassed; `_check_company`, balance and lock controls are not. Wizard reachability by a non-purchasing user: class **C**. | **A** (source) / **C** (reach) |
| `H-P01-3` | Percentage down payment computed on the wrong base with the **customer** tax field (`taxes_id`, not `supplier_taxes_id`); `all([])` is `True`, so the percentage applies to tax-**inclusive** `amount_total`. | **A** |
| `H-P01-4` | Forks a native v18/v19 feature (`is_downpayment`, `_create_downpayments`); its button replacement covers 2 of 4 core buttons, so the two list-header "Create Bills" buttons bypass the wizard. | **A** |
| `H-P01-5` | **Ownership question P05 will not answer:** does P01 own vendor advances? | OPEN |
| `H-P01-6` | An expense line can name a `vendor_id` and post to vendor-facing accounts with no purchase document. Cross-company vendors are caught, but **late** — at move creation/posting, not at capture (`22 R-01'`). | **A** |

## 3. Affected Population

| Database | Version | Installed | Wizard rows |
|---|---|---|---|
| `iSMEs` | 16.0 | yes | **21** |
| `iEVING` | 19.0 | yes | 0 |
| `BK12MAY26` | 19.0 | yes | 0 |
| `iTEST02` | 19.0 | yes | 0 |
| **`idemo18_uat`** | **18.0** | **no** | n/a |

## 4. Required P01 Follow-up

1. Determine whether P01 owns vendor advances at all (`H-P01-5`).
2. Extract the 21 `iSMEs` wizard rows against their purchase orders and final bills, and establish
   whether any vendor was billed twice. **This is the open question that decides severity**, and it
   sits inside P01's data scope.
3. Decide the authorisation scope for advance billing (`H-P01-2`, `SC-02`).
4. Decide fork-vs-core (`H-P01-4`).

## 5. Boundary

P05 asserts **no** P01 canonical behaviour, **no** vendor-advance accounting semantics, and **no**
financial loss. `PEER DEPENDENCY — P01. OPEN.` Last consumed P01 SHA: **none — P01 has published no
branch.**
