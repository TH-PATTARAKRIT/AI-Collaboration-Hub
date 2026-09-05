# 46 — P05 EMPLOYEE ADVANCE DEPLOYMENT RECLASSIFICATION

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E06`

## 1. Verification of the Denominator

Round 2 claimed `scgl_advance_expense_request` is installed in none of six registries. **Re-verified
against seven registries, now including the v18 target:**

| Registry | State |
|---|---|
| `iSMEs` v16 | absent from registry |
| **`idemo18_uat` v18** | **`uninstalled`** |
| `occ_sim` v18 | absent |
| `iEVING` v19 | `uninstalled` |
| `BK12MAY26` v19 | `uninstalled` |
| `iTEST02` v19 | `uninstalled` |
| `pankhamhom` | **NOT YET READ — class `C`** |

**UPHELD and strengthened.** The module is installed in **none** of the six read registries, including
the v18 target where the rest of the P05 surface *is* installed. Class **A** within those six;
class **C** for `pankhamhom`. Corroborated structurally: the `advance_expense_request` table does not
exist in any dump examined.

## 2. Is There Another Employee-Advance Implementation?

Declared search over the `idemo18_uat` installed set (361 modules), pattern
`advance|imprest|employee[ _-]?loan`:

| Hit | Assessment |
|---|---|
| `sale_advance_payment_inv` (core) | **customer** down payment — out of P05 scope |
| `account_payment_multi_deduction` | payment deduction, not an advance |
| `scgl_purchase_advance_payment` | **`uninstalled` on v18** — vendor advance, P01 territory |

**No employee-advance implementation is installed on the target platform.** Class **A** within that
registry.

> **Consequence for `DUP-03`.** Round 1 called the advance-vs-claim duplicate "structural, because the
> two systems share no code path". On the target platform the exposure is not merely structural but
> **vacuous** — there is no advance system deployed at all. The finding is preserved as a source and
> design fact; its operational reach is nil.

## 3. Reclassification

| Finding | Was | Now |
|---|---|---|
| `F-07` advance expensed at disbursement | `LATENT` | **`LATENT — MODULE NOT INSTALLED`**, verified across six registries incl. v18 |
| `GL-04`, `GL-05` clearing account collapse | `LATENT` | same |
| `TZ-05` raw `state='cancel'` write | `LATENT` (P05 trigger) | same — **but the underlying core gap `TZ-08` is platform-level and belongs to P08** |
| `TZ-07`, `TZ-13` clearing defects | `LATENT` | same |
| `E3-01`..`E3-11` | `LATENT` | same |

## 4. Design Weight — the axis that matters

Per `26 §2` (Expert 1's accepted challenge), `LATENT` does **not** mean *less relevant* for a
clean-room build decision. SMEsPlus has not built employee advances. These findings are a documented
catalogue of how a reference implementation got it wrong — **expense recognised at disbursement with
no receivable, a clearing entry that can net to zero on the same bank account while reporting the
advance cleared, and a non-accounting document able to force-cancel a posted entry.** Their value is
in what SMEsPlus declines to inherit, and that value is undiminished by the module being uninstalled.

`17 §6 DI-01` (*an advance creates an asset, never an expense*) stands unchanged and remains
Boss-decidable now.
