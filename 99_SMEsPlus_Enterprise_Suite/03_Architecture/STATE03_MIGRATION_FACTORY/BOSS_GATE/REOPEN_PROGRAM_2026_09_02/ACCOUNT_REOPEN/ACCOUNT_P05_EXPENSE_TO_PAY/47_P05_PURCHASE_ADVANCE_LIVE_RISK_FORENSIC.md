# 47 — P05 PURCHASE ADVANCE LIVE RISK FORENSIC

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E07`

## 1. Installation — Round 2's claim NARROWED

Round 2: *"`scgl_purchase_advance_payment` is installed in all four distinct databases evidenced."*

Re-verified across seven registries:

| Registry | State | Version |
|---|---|---|
| `iSMEs` v16 | **INSTALLED** | `16.0.1.0.0` |
| **`idemo18_uat` v18 (target)** | **`uninstalled`** | — |
| `occ_sim` v18 | absent | — |
| `iEVING` v19 | **INSTALLED** | `19.0.1.0.0` |
| `BK12MAY26` v19 | **INSTALLED** | `19.0.1.0.0` |
| `iTEST02` v19 | **INSTALLED** | `19.0.1.0.0` |
| `pankhamhom` | not read | class `C` |

**Corrected: installed in four of six read registries — and NOT on the v18 target platform.**
Round 2's "all four distinct databases" was true of the set it had; it is **not** true of the
population once the v18 target is included. `RE-22`.

## 2. Data Population

| Registry | `purchase_advance_payment_bill` rows |
|---|---|
| `iSMEs` v16 | **21** |
| `iEVING`, `BK12MAY26` | 0 |
| `iTEST02` | 0 |
| `idemo18_uat` | table absent (module uninstalled) |

> **Material qualification of Round 2's severity.** The wizard has been **used 21 times, in one
> database, at v16**. In the three v19 databases it is installed and **never used**. On the v18 target
> it is not installed. The exposure is **installed-and-reachable in four registries, exercised in one**.

## 3. The Two Reported Defects — re-derived, not inherited

### `A` — vendor down payment never deducted from the final bill

Source re-derivation stands (`30 §1 H-P01-1`): `deduct_down_payments` has four references in the
custom tree and its **only consumer is commented out** (`wizard/purchase_advance.py:178`); the live
branch calls `purchase_order_ids.action_create_invoice()` (`:179`), a core action with no knowledge of
the flag. Class **A** over the custom tree for the *source* defect.

**Database corroboration attempted and NOT obtained.** With 21 wizard rows in `iSMEs` v16 only, and no
extraction performed of the resulting bills against their purchase orders, the *accounting* effect —
whether a vendor was actually billed twice — is **`C` — NOT YET SEARCHED**. It is **not** asserted.

> **This is the correction that matters most for P01's benefit.** Round 2 routed this as a live
> duplicate-payment exposure "in all four real business databases". The defensible statement is:
> **the source defect is verified; the module is installed in four registries; it has been exercised
> 21 times in one; and no observed double-billing has been demonstrated.** P01 should receive the
> verified source defect and the exercise count, not an asserted financial loss.

### `B` — `sudo()` vendor-bill creation

Source facts re-derived: `security/ir.model.access.csv:2` grants full CRUD on
`purchase.advance.payment.bill` to `base.group_user`; `_create_bill` creates the `account.move` with
`.sudo()` (`wizard/purchase_advance.py:203`). Class **A** over the module.

**Authorisation classification — `PARTIAL AUTHORIZATION`, not `SUDO BYPASS VERIFIED`.** See `48`.

## 4. Exposure Class

| Defect | Class |
|---|---|
| `A` source defect | **LIVE — CONFIGURED / REACHABLE** in four registries; **not** on the v18 target |
| `A` financial effect | **NOT OBSERVED** — class `C` |
| `B` source defect | **LIVE — CONFIGURED / REACHABLE** in the same four |
| `B` authorisation effect | **PARTIAL** — see `48` |

## 5. Ownership

`scgl_purchase_advance_payment` depends on `purchase`. **P01 owns Procure-to-Pay.** P05 discovered,
verified and documents; **P05 does not define vendor-advance accounting semantics, does not close
P01 architecture, and does not decide whether this is a defect in P01's model.** Routed at `49`.
