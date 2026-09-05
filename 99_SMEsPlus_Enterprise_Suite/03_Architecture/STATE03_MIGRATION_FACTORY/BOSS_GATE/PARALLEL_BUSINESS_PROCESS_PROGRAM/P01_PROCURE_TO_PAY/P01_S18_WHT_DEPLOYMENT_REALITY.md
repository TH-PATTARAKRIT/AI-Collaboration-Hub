# P01 — SERIES-18 WITHHOLDING-TAX DEPLOYMENT REALITY

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Bounded to database `551ab874-9acb-11f1-b150-6ec7a480be3d` (`idemo18_uat`) @ 2026-08-30.

> **NO STATUTORY CONCLUSION IS DRAWN IN THIS DOCUMENT.**
> Thai withholding-tax and PND questions belong to peer process **P07**. Source behaviour is not
> statutory truth. Every question of compliance below is recorded as
> `HOLD — STATUTORY EVIDENCE REQUIRED` and routed to P07. P01 does not overrule P07.

**MECHANISM EXISTENCE and MECHANISM REACHABILITY are kept strictly separate** — §2 and §3
respectively — because conflating them is what produced `ERR-P01-12` and `ERR-P01-18`.

---

## 1. THE ATTRIBUTION P01 HAD WRONG — `ERR-P01-33`

P01 has recorded this deployment's withholding mechanism as belonging to **`l10n_th 18.0.2.0`**.

**`l10n_th` contains no withholding-tax code.** Across the 798 modules of the declared core root, a
search for `withholding.tax.cert` and for `account.withholding.tax` returns **zero** hits.
`l10n_th` is 17 files — chart of accounts, EMV QR, report layouts, bank and partner extensions,
author *Almacom*.

Ownership resolved from `ir_model_data` where `model = 'ir.model'`, i.e. from the deployment
itself rather than from a manifest:

| Model | Owning module | Installed version |
|---|---|---|
| `account.withholding.tax` | `l10n_th_withholding_tax` | **18.0.1.4** (Ecosoft, OCA) |
| `withholding.tax.cert`, `.line`, `create.withholding.tax.cert` | `l10n_th_withholding_tax_cert` | **18.0.1.3** (Ecosoft, OCA, SCG) |
| `report.withholding.tax.pdf` | `l10n_th_withholding_tax_cert_form` | **18.0.1.0.2** |
| `withholding.tax.report`, `.wizard` | `l10n_th_withholding_tax_report` | **18.0.1.0.1** |
| `l10n_th_withholding_tax_multi` | — | **UNINSTALLED** |

**All four have version-matching source inside the declared path set `R4`.** P01 could not see them
because its custom-module population was a **name pattern** (`scgl_*` + `purchase_request`), not a
membership test — see `P01_POPULATION_SELECTION_METHOD_AUDIT.md §4A`.

**Consequence:** the deployed withholding mechanism is a **known OCA/Ecosoft stack with readable,
version-matched source** — not an opaque localisation module, and not the series-16 custom wizard
P01 analysed in earlier rounds.

---

## 2. MECHANISM EXISTENCE — what the deployed code provides

Read from the version-matched source in `R4`:

1. **`account.withholding.tax`** — a rate record. `account_id` is domained
   `[('wt_account','=',True)]`; `type` is sale/purchase/none; `amount` is a percentage; carries
   `tax_tag_ids` and `company_id`.
2. **`account.move.line.wt_tax_id`** — the withholding rate is carried on the **vendor bill line**.
3. **`account.payment.register`** — on registering payment from bill lines it computes
   `amount_wt = Σ(wt_tax_id.amount / 100 × price_subtotal)`, reduces the payment `amount`, forces
   `payment_difference_handling = 'reconcile'`, sets `writeoff_account_id = wt_tax_id.account_id`,
   and stamps the withholding tax tags on the write-off line.
4. **`account.payment.wt_tax_id`** — documented in the source as *"Optional hidden field to keep
   wt_tax. Useful for case 1 tax only"*.
5. **`withholding.tax.cert` + `.line`**, produced by the `create.withholding.tax.cert` wizard.
6. **`l10n_th_withholding_tax_multi` is UNINSTALLED** → **one withholding rate per payment.**

### 2.1 A second implementation exists on this host and is not deployed here

`scgl_wht_control` ("SCGL WHT Control") has source at two locations, one of them an entire project
tree at `/Volumes/iMacSys/97_OCC_PROJECT_WHT_CONTROL/`. It **does not appear in
`ir_module_module` at all** — not installed, not uninstalled, never on this deployment's addons
path.

**CLASSIFICATION: EXISTS — NOT DEPLOYED.** Recorded so that no future round reads its source and
attributes its behaviour to this deployment. That is exactly `ERR-P01-13`.

### 2.2 Whether P01's series-16 finding concerns this same family — NOT DECIDED

P01's earlier withholding finding (*repeated full base per partial payment, never prorated*) was
read from a 69-line series-16 custom wizard. Series-16 copies of **these same OCA modules** also
exist on this host (`l10n_th_withholding_tax` 16.0.1.0.1,
`l10n_th_withholding_tax_cert` 14.0.1.0.0), so that finding may concern an **earlier version of
this same family** rather than a bespoke wizard.

**NOT DECIDABLE from this evidence base.** Settling it requires reading the earlier round's
**register and status field**, not its summary. Recorded as an open action; **no transfer of the
series-16 finding to this deployment is made or implied.**

---

## 3. MECHANISM REACHABILITY — measured, and kept separate from §2

**The certificate layer is populated. The tax-application layer has never run on a payment.**

### 3.1 Payments

`account_payment`, 3,508 rows (field count uniform at 35 across all rows):

| Measure | Value |
|---|---|
| `partner_type` | supplier **1,183** · customer 2,325 |
| `state` | paid 3,504 · in_process 4 |
| By company | 1 → 1,899 · 2 → 1,609 · **3 and 4 → zero** |
| **`wt_tax_id` non-null** | **0 of 3,508**, and **0 of the 1,183 supplier payments** |
| `is_multi_deduction` true | 0 of 3,508 — consistent with the multi module being uninstalled |
| `wt_cert_cancel` true | 3,181 of 3,508 → **327 payments hold a live certificate** |

### 3.2 Bill lines

`account_move_line.wt_tax_id` non-null: **4 of 40,353**.
*Positive controls in the same pass:* `purchase_line_id` 2,606 · `product_id` 7,963 ·
`payment_id` 7,430 — and two further real zeros in adjacent columns (`expense_id` 0,
`vehicle_id` 0), which is what distinguishes a measured zero from a parse failure.

All four are vendor-bill expense lines dated in the **last week of the dataset** (2026-08-25 to
08-30), in AP journals, at rates 1% and 3%. **None reached a payment.**

### 3.3 Rate records and certificates

`account.withholding.tax` — **40 rows**, all `type = 'purchase'`; rates 1 / 2 / 3 / 5 %;
16 active, 24 inactive; by company 8 / 16 / 8 / 8; accounts all `232000 Withholding Tax`.

`withholding.tax.cert` — **332 rows**: done 327, cancel 3, draft 2. `income_tax_form`
**pnd53 205 · pnd3 125 · null 2**. `tax_payer` = withholding on all 332. Companies 1 → 193,
2 → 139. `payment_id` non-null on 327, **327 distinct** — exactly `3,508 − 3,181`.

> **The certificate register was bulk-loaded, not produced by operation.** Business dates spread
> across eight months (2026-01-03 → 2026-08-29); **creation timestamps confined to 2026-08-25
> 20:42 → 2026-08-29 07:48**; **328 of 332 created under uid 1 (`__system__`)** and carrying
> `occ_mig` migration external IDs. Four were created by real users.

`withholding.tax.cert.line` — 348 rows. `wt_cert_income_type` '5' 332, '6' 16.
Rates: 3% 217 · 1% 97 · 5% 32 · 0% 2. **Σ base ฿10,755,666.83 · Σ amount ฿160,338.51**
(done ฿158,483.71 = co1 ฿94,020.37 + co2 ฿64,463.34; cancel ฿1,383.80; draft ฿21.00).
`ref_move_line_id` non-null on **1 of 348**. One line's `cert_id` has no matching certificate
(฿450.00). One line of 348 fails `|base × pct/100 − amount| ≤ 0.01`.

**CLASSIFICATION: INSTALLED · CONFIGURED · the certificate layer EXERCISED (by migration, not by
operation) · the payment-time tax-application layer NOT EXERCISED — 0 of 3,508.**

---

## 4. WHERE WITHHOLDING ACTUALLY REACHES THE LEDGER — AND IT IS NOT THE MODULE'S ROUTE

Journal items on the withholding accounts:

| Account | Company | Items | Debit | Credit | Carrying a `payment_id` |
|---|---|---|---|---|---|
| 179 `232000 Withholding Tax` | 1 | 206 | ฿85,988.54 | ฿94,704.16 | 192 |
| 65 `232000 Withholding Tax` | 2 | 152 | ฿56,582.89 | ฿64,715.51 | 138 |
| 103 (co 3), 141 (co 4) | 3, 4 | **0** | | | |

Journal split of those 358 items: **330 in bank journals** (KAS2 co1 191, KAS1 co2 132, SIC1 5,
SCB1 1, BKK3 1) and 28 in AP journals. All 358 are `posted`.

**Three separable observations:**

1. **The applied-withholding route is not the module's route.** If
   `account.payment.register` had produced these, the payments would carry `wt_tax_id`.
   **Zero of 3,508 do.** The amounts were entered by some other path — a bank-side write-off, a
   manual entry, or the migration.
2. **The PND-specific liability accounts carry nothing.** `214001 / 214002 / 214003`
   (ภาษีหัก ณ ที่จ่ายค้างจ่าย ภ.ง.ด.1 / ภ.ง.ด.3 / ภ.ง.ด.53) exist in **all four** charts and hold
   **zero** items — while the certificate register classifies **330 of 332** certificates as pnd3
   or pnd53. **The form classification lives only in the certificate register, never in the ledger.**
3. **Register and ledger do not tie.**

   | | Amount |
   |---|---|
   | Certificate lines, state done | ฿158,483.71 (co1 ฿94,020.37 + co2 ฿64,463.34) |
   | GL gross credits, accounts 179 + 65 | ฿159,419.67 (co1 ฿94,704.16 + co2 ฿64,715.51) |
   | **Difference** | **฿935.96 — 0.59%** (co1 ฿683.79 + co2 ฿252.17) |

   Both figures are **enumerated from rows**, not re-derived from a stated total.

---

## 5. ROUTED TO P07 — `HOLD — STATUTORY EVIDENCE REQUIRED`

P01 measures; **P07 decides**. Three questions, stated as questions:

1. Does a withholding credit posted to a **generic `232000` account** rather than to the
   **PND-keyed liability accounts** satisfy Thai filing requirements?
2. Does a certificate register whose lines carry a reference to their originating journal item on
   **1 of 348** meet the record-keeping standard?
3. Is the **฿935.96 (0.59%)** register-to-ledger difference material?

**P01 does not answer any of these, and nothing in this document should be read as an answer.**

---

## 6. CLASSIFICATION SUMMARY

| Item | Classification |
|---|---|
| `l10n_th` supplies the withholding mechanism | **FALSE — CORRECTED, `ERR-P01-33`.** Zero WHT code in `l10n_th` |
| Four OCA/Ecosoft modules supply it, with version-matched source in `R4` | **FACT VERIFIED** |
| `l10n_th_withholding_tax_multi` uninstalled → one rate per payment | **FACT VERIFIED** |
| `scgl_wht_control` | **EXISTS — NOT DEPLOYED** (absent from `ir_module_module` entirely) |
| P01's series-16 withholding finding applies here | **NOT DECIDABLE** — may concern an earlier version of this same OCA family; **no transfer made** |
| Certificate layer exercised | **FACT VERIFIED — 332 certificates, but bulk-loaded** (328 under `__system__` with migration xmlids in a five-day window) |
| Payment-time tax application exercised | **NOT EXERCISED — 0 of 3,508 payments carry `wt_tax_id`** |
| Bill-line withholding exercised | **4 of 40,353 lines**, all in the last week, none reaching a payment |
| Withholding reaches the GL by some other route | **FACT VERIFIED** — 358 items, 330 raised in bank journals |
| PND-keyed liability accounts | **zero items in all four companies — FACT VERIFIED** |
| Register-to-ledger difference ฿935.96 | **FACT VERIFIED**, both sides enumerated |
| Whether any of this is compliant | **HOLD — STATUTORY EVIDENCE REQUIRED → P07** |
