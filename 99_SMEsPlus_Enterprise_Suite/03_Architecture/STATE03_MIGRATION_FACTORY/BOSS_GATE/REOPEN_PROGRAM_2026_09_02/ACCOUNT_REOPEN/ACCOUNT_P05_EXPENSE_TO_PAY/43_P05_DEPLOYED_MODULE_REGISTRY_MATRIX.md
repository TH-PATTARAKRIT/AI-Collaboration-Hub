# 43 — P05 DEPLOYED MODULE REGISTRY MATRIX

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E03`
Supersedes `24 §3`. `24` is retained as audit lineage; its conclusions are **corrected here**.

## 1. Registries Read

Seven distinct database identities, all `ir_module_module` read offline.

| ID | Database | Odoo version | Modules | Installed | Companies |
|---|---|---|---|---|---|
| `R-1` | `iSMEs` | **16.0** | 1009 | 190 | 1 |
| `R-2` | **`idemo18_uat`** | **18.0** | **1369** | **361** | **4** |
| `R-3` | `occ_sim` | 18.0 | 707 | 41 | — |
| `R-4` | `iEVING` | 19.0 | 1504 | 232 | — |
| `R-5` | `BK12MAY26` | 19.0 | 1508 | 251 | — |
| `R-6` | `iTEST02` | 19.0 | 1559 | 453 | — |
| `R-7` | `pankhamhom` | *not yet read* | — | — | — |

`R-7` is `NOT YET SEARCHED — class C`; it is a 28 MB readable archive located by the exhaustive
search and not consumed within this continuation's budget. Declared, not concealed.

## 2. P05 Module Matrix

`INST` installed · `uninst` present but not installed · `—` absent from the registry.

| Module | `iSMEs` v16 | **`idemo18_uat` v18** | `occ_sim` v18 | `iEVING` v19 | `BK12` v19 | `iTEST02` v19 |
|---|---|---|---|---|---|---|
| `hr_expense` | INST | **INST 18.0.2.0** | uninst | INST | INST | INST |
| `hr_expense_extract` | uninst | **INST 18.0.1.0** | — | uninst | uninst | INST |
| `sale_expense` | INST | **INST** | uninst | INST | INST | INST |
| `hr_payroll_expense` | uninst | uninst | — | uninst | uninst | INST |
| **`hr_expense_petty_cash`** | uninst | **INST 18.0.1.2** | — | — | — | — |
| `hr_expense_sequence` | uninst | uninst | — | — | — | — |
| **`scgl_advance_expense_request`** | — | **uninst** | — | uninst | uninst | uninst |
| **`scgl_purchase_advance_payment`** | INST | **uninst** | — | INST | INST | INST |
| `l10n_th` | INST | **INST 18.0.2.0** | INST | INST | INST | INST |
| `l10n_th_reports` | — | **INST 18.0.1.0** | — | INST | INST | INST |
| `l10n_th_withholding_tax` | INST | **INST 18.0.1.4** | — | INST | INST | INST |
| `l10n_th_withholding_tax_multi` | — | uninst | — | uninst | uninst | uninst |
| `l10n_th_withholding_tax_cert` | INST | **INST 18.0.1.3** | — | INST | INST | INST |
| `l10n_th_withholding_tax_cert_form` | INST | **INST** | — | INST | INST | INST |
| `l10n_th_withholding_tax_report` | INST | **INST** | — | INST | INST | INST |
| `account_payment_multi_deduction` | — | **INST 18.0.1.0.2** | — | uninst | uninst | INST |
| `account_disallowed_expenses` | uninst | **INST 18.0.1.0** | — | — | — | — |
| `multi_level_approval` | — | uninst | — | INST | uninst | INST |
| `purchase` | INST | **INST** | uninst | INST | INST | INST |
| **`scgl_signature_hr_expense`** | — | **INST** | — | — | — | — |
| `scgl_multi_approve_core` | — | **INST** | — | — | — | — |

## 3. Corrections to `24`

| `24` claim | Status now |
|---|---|
| "No Odoo 18 database carrying the P05 surface exists in the available evidence" | **`E` — CONTRADICTED.** `idemo18_uat` is v18 and carries the whole P05 surface. `RE-20`. |
| "`hr_expense_petty_cash` is installed in none of the six registries" | **`E` — CONTRADICTED.** Installed at `18.0.1.2` on the v18 target. `RE-21`. |
| "`scgl_advance_expense_request` is installed in none" | **UPHELD** — `uninst` or absent in all seven registries, now including v18. Strengthened, not weakened. |
| "`scgl_purchase_advance_payment` is live in all four distinct databases" | **NARROWED.** It is `uninst` on the v18 target. Live in `iSMEs` v16, `iEVING`, `BK12`, `iTEST02` — **four of six read registries, but not the v18 one.** `RE-22`. |
| "Six registries" as the population | **`E`** — the population is nine identities, seven readable, one unread (`R-7`). |

## 4. New Module Surface Never Analysed

`idemo18_uat` carries **`scgl_signature_hr_expense`** (installed) — a custom module that extends the
expense surface and appears in **no** prior P05 analysis. Also installed: `scgl_multi_approve_core`,
`scgl_multi_approve_purchase_request`, `scgl_account_coa_control`, `scgl_date_range_auto_period`.

**Class `C` — NOT YET SEARCHED.** This is a material population gap: the P05 source analysis was
bounded to `smeplus-custom/addons`, and at least one installed expense-affecting module on the target
platform is outside everything examined. Recorded as gating unknown **`U-15`**.

## 5. Deployment Reality vs Source Copy

`idemo18_uat` runs `hr_expense_petty_cash 18.0.1.2` — the same version string as the source copy read
at `smeplus-custom/addons`. **But the deployed behaviour does not match that source** (`45 §3`).
Therefore: **the source copy analysed is not demonstrably the deployed code.** Every source-only P05
finding inherits this caveat. Recorded as **`U-16`**.
