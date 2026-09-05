# 51 — P05 → P07 TX-01 STATUTORY HANDOFF

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E12`
**P05 verifies source, database, and predicate divergence. P07 owns every statutory determination.
P05 declares no Thai compliance or non-compliance.**

## 1. Technical Evidence Delivered

| Element | Value |
|---|---|
| Two WHT subsystems installed together | `l10n_th_reports` (enterprise) **+** `l10n_th_withholding_tax*` (custom/OCA) |
| Registries where both are installed | `idemo18_uat` v18, `iEVING`, `BK12MAY26`, `iTEST02` — **4 of 6** |
| Screen predicate | `engine="tax_tags"` — sums by tag |
| CSV predicate | inner join on `account_move_line.tax_line_id` |
| Custom WHT line | carries the tags, **never** `tax_line_id` — structurally guaranteed |
| **v18 target population** | **358 of 358 lines (100.00%)** on WHT accounts carry no `tax_line_id` |
| v16 population | 5,426 of 5,863 (92.55%) |
| Branch identifier divergence | `partner.company_registry` (enterprise) vs `partner.branch` (custom) |

## 2. Unresolved Statutory Questions — P07's

1. Does the screen-vs-export divergence affect a **filed** return, and by what amount?
2. Which of the two subsystems is the **system of record** for PND3 / PND53?
3. Which branch identifier is correct for the return?
4. `iSMEs` v16 holds 13 `pnd1` certificates the report wizard cannot export — are `pnd1`
   certificates in scope for this filing?
5. Are cancelled certificates correctly emitted as blanked rows retaining sequence number, VAT id,
   rate and date?
6. Is a payment permitted **one certificate per payee** (21 such cases), and more than one per payee
   at **different rates** (8 cases)? One **exact duplicate** exists in 5,201 (`52`).
7. `1,417` certificates in `iSMEs` carry **no certificate number**, 1,414 of them `done`. Must a
   statutory certificate carry a unique identifier?
8. At v19 the statutory columns `date`, `income_tax_form`, `supplier_partner_id` became **nullable**.
   Is a certificate with no payee and no tax form admissible?
9. Are Thai WHT rates uniform across companies of one taxpayer? (Bears on `SC-01`; on v18 the config
   is **per-company, 4 accounts**, which contradicts the v16 single-account picture.)

## 3. Boundary

Every item above is `HOLD — STATUTORY EVIDENCE REQUIRED`. P05 supplies mechanics and populations only.
`PEER DEPENDENCY — P07. OPEN.` Last consumed P07 SHA: **none — P07 has published no branch.**
