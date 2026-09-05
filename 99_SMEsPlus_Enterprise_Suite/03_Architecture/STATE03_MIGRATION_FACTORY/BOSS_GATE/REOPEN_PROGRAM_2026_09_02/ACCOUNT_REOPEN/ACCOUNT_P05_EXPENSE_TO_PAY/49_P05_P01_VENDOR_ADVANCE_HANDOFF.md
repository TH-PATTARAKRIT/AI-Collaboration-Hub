# 49 — P05 → P01 VENDOR ADVANCE HANDOFF

> **Title corrected (AAS-03 Challenge D, `V-3`).** This file was titled and filenamed
> "**CRITICAL**". That is a decision-force severity word carried at the package's most durable and
> most-quoted layer, while this document's own evidence classes the financial effect as
> **`C — NOT YET SEARCHED`** and states plainly that no double-billing has been observed. The caveat
> must survive everywhere the finding is stated, including the title — it did not. `RE-24`.

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

## 4. Questions Routed to P01

**P05 has no authority to require action of a peer process.** These are routed questions, not
instructions — corrected from an earlier imperative list (Challenge D `V-1`, `RE-25`).

1. Does P01 own vendor advances at all (`H-P01-5`)?
2. Do the 21 `iSMEs` wizard rows, read against their purchase orders and final bills, show any vendor
   billed twice? **This is the open question on which severity turns**, and the data sits inside P01's
   scope, not P05's.
3. What is the correct authorisation scope for advance billing (`H-P01-2`, `SC-02`)?
4. Fork or core (`H-P01-4`)?

## 5. Boundary

P05 asserts **no** P01 canonical behaviour, **no** vendor-advance accounting semantics, and **no**
financial loss. `PEER DEPENDENCY — P01. OPEN.` Last consumed P01 SHA: **none — P01 has published no
branch.**
