# P04 — SCOPE / MULTI-COMPANY / ACCESS (CLOSURE VIEW)

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P04-11`. Extends `20` of the base package; **prior rows
stand.** Scope is determined **per object**, never blanket-enforced (`CORR1`).

---

## 1. Objects material to this closure

| Object | Scope | Evidence | Consistent? |
|---|---|---|---|
| `account.asset` (asset) | **COMPANY** | `company_id`; currency related from it | yes |
| `account.asset` (**model**, `state='model'`) | **COMPANY** | `model_id` domain `[('company_id','=',company_id)]` | yes — but see `P04-BD-09`: whether a depreciation policy template *should* be company-owned is an open Boss question |
| `account.asset.group` | **COMPANY**, weakly | a group with no company is visible to no one — `P04-B-28`, closed from source | yes |
| `maintenance.equipment` | **COMPANY** | reference model | yes |
| **`account.asset.name_asset`** (the custom link) | **UNCONSTRAINED** | **no company domain on the field**, unlike `model_id` which has one | **NO — asymmetric** |
| `account.analytic.account` | **COMPANY** + plan | reference | yes |
| Depreciation journal | **COMPANY** | `journal_id`, domain `type='general'` | yes |

## 2. The one inconsistency, stated as a bounded check rather than a claim

> **`P04-F-156`. Within one custom module the two Many2one fields that reach outside the asset
> disagree about company scope: `model_id` carries a company domain and `name_asset` carries
> none.** On the field evidence alone an asset in company A can reference equipment in
> company B.
>
> **What this does NOT establish.** A record rule on `maintenance.equipment` could still block
> it at read time. **Field domains and record rules are different instruments and this run
> examined only the first.** Registered as **`P04-B-54`** with the exact question — *does an
> `ir.rule` on `maintenance.equipment` restrict by company, and does it apply to the asset
> form's Many2one lookup?* — rather than published as a cross-company hole.
>
> Recorded this way deliberately: this package has twice published a boundary claim on one
> instrument and had to narrow it.

## 3. PLATFORM / TENANT / COMPANY determination

| Level | Objects |
|---|---|
| **PLATFORM** | module installation set (`equipment_sequence`, `product_stock_equipment`, `account_asset`); day-convention **implementation** |
| **TENANT** | none identified in this closure that is not also company-scoped |
| **COMPANY** | every object in §1; the day-convention **election** per asset; the account triple; the journal |

**No blanket tenant+company enforcement is asserted**, per `CORR1`.

## 4. Disposition

> **`CQ-P04-11` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for scope determination of
> every object material to this closure, with **one asymmetry found and routed as a bounded
> record-rule question (`P04-B-54`)** rather than asserted.
