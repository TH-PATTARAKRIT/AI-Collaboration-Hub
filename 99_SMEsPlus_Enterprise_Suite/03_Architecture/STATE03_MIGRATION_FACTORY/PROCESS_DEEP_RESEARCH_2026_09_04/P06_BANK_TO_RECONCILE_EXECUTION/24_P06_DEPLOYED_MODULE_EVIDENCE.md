# P06_DEPLOYED_MODULE_EVIDENCE.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C04)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Purpose:** establish the highest available evidence for what banking/payment/reconciliation modules are **actually deployed**, before any absence claim is preserved.

---

## 1. Why this step is mandatory

`P06-F02` asserts that **0 of 12 custom modules touch `account.bank.statement`**. That negative was derived from **source trees**, not from an installed population. Under the negative-claim standard, absence from a source tree is not absence from a running system. This file tests whether an installed population is available.

---

## 2. Evidence located

Two module-registry exports exist on this workstation:

| Ref | File | Rows | Installed | Version line |
|---|---|---|---|---|
| **DM-A** | `~/Downloads/Module (ir.module.module).xlsx` | 1442 | **503** | `19.0.*` |
| **DM-B** | `~/Downloads/Module (ir.module.module) (1).xlsx` | 1434 | **253** | `saas~19.1.*` |

Both are `ir.module.module` list exports with columns `Module Name · Author · Website · Latest Version · Status`. Both were captured 2026-03-08.

---

## 3. Which system each export describes

**DME-F-01 — DM-A is an SCG Legacy–built database, and it carries BHPRO-specific modules.**
Installed rows authored by the project vendor include `PromptPay Invoice Report` (author `SCGL`), `Purchase Advance Payment` (`SCGL`), `Tax Period Date` (`SCGL`), `Equipment Sequence`, `Product Sequence`, `Custom Title and Favicon`, `Scgl Stock Lot/Serial Filter`, plus `Account ( Invoice & Bill ) - Discount Wizard Catalog` and `Purchase Order - Discount Wizard Catalog` (`MPP, SCGLegacy(Thailand) Co.,Ltd`).
It **also** carries `Purchase Extrension Module for BHPRO`, `19_bhpro_menu_general` and `19_bhpro_master`.
**DENOMINATOR:** POPULATION: 503 installed rows in DM-A. PATTERN: `bhpro|scgl|occ|smesplus|smeplus|ving|wcf` over module name + author. UNIT: row. **RESULT = 11.**
**Verdict: DM-A is the BHPRO client database built by the same vendor. It is NOT the SMEsPlus C1/C2 target.**

**DME-F-02 — DM-B is an unrelated Odoo Online database.**
253 installed rows; 251 authored by Odoo S.A., one by `Almacom`, one by `Odoo SA`. **Zero** project-identifying rows under the same pattern. Version line `saas~19.1.*` indicates Odoo Online.
**Verdict: DM-B is not attributable to this project.**

**DME-F-03 — Both exports are from the Odoo 19 line. P06's entire research target is the v18 line (`18.0+e.20250608`).**
DM-A installed versions all carry the prefix `19`; DM-B all carry `saas~19`.
**This is the single most consequential fact in this file.** There is a **generation gap** between the only available deployment evidence and the researched target. Raised as **`P06-B-44` — HOLD — DATABASE EVIDENCE REQUIRED**: the SMEsPlus target database has not been observed by any P06 session.

---

## 4. Classification of the P06 module population

Per the required scheme. **"INSTALLED VERIFIED" is reserved for the target system and no module qualifies**, because no target-system registry was located.

| Module | Source trees | DM-A (BHPRO, v19) | Classification **for the P06 target** |
|---|---|---|---|
| `account_bank_statement_import` | V18E | **Installed** | **UNKNOWN** |
| `..._camt` | V18E | **Installed** | **UNKNOWN** |
| `..._csv` | V18E | **Installed** | **UNKNOWN** |
| `..._ofx` | V18E | **Installed** | **UNKNOWN** |
| `..._qif` | V18E | **not in installed set** | **UNKNOWN** |
| `account_bank_statement_extract` | V18E | not in DM-A; **Installed in DM-B** | **UNKNOWN** |
| `account_online_synchronization` | V18E | **Installed** | **UNKNOWN** |
| `account_payment` | V18E | **Installed** | **UNKNOWN** |
| `payment` (Payment Engine) | V18E | **Installed** | **UNKNOWN** |
| `account_check_printing` | V18E | not in installed set | **UNKNOWN** |
| `account_batch_payment` | V18E | not in installed set | **UNKNOWN** |
| `account_accountant_batch_payment` | V18E | not in installed set | **UNKNOWN** |
| `account_payment_multi_deduction` | CUST18/CUST14/T8 | **Installed** (`19.0.1.0.2`) | **UNKNOWN** |
| `dev_print_cheque` | all four | **Installed** (`19.0.1.3`) | **UNKNOWN** |
| `invoice_promptpay` | CUST18/CUST14 | **Installed** (`19.0.1.0`) | **UNKNOWN** |
| `scgl_purchase_advance_payment` | CUST18/T8/MIGR | **Installed** (`19.0.1.0.0`) | **UNKNOWN** |
| `scgl_tax_period_date` | CUST18/T8/MIGR | **Installed** (`19.0.0.1`) | **UNKNOWN** |
| `l10n_th_withholding_tax` (+cert, +report) | CUST18/CUST14 | **Installed** | **UNKNOWN** |
| `payment_2c2p` | CUST18/CUST14 | not in installed set | **UNKNOWN** |
| `cheque_control` | CUST14 only | not in installed set | **SOURCE ONLY** |
| `post_dated_cheque_mgt_app` | CUST14 only | not in installed set | **SOURCE ONLY** |
| `pdc_generate_cheque_reference` | CUST14 only | not in installed set | **SOURCE ONLY** |
| `account_payment_return` | CUST14 only | not in installed set | **SOURCE ONLY** |
| `om_account_bank_statement_import` | CUST14 only | not in installed set | **SOURCE ONLY** |
| `cr_effective_date_entries` | CUST18/T8 | not in installed set | **UNKNOWN** |
| `full_payment_custom` | CUST18/T8 | not in installed set | **UNKNOWN** |
| `hr_expense_petty_cash` | all four | not in installed set | **UNKNOWN** |

**DENOMINATOR for the "not in installed set" cells:** POPULATION: the 503 installed rows of DM-A. PATTERN: `bank|payment|cheque|check|recon|pdc|statement|cash|promptpay|2c2p|withhold|petty|deduct|effective_date|advance|iso20022|l10n_th` over the Module Name column. UNIT: row. **This matches on the human-readable module *title*, not the technical name** — a module whose title does not contain a pattern word would be missed. **Class B, not Class A.**

---

## 5. What this does and does not do to `P06-F02`

**DME-F-04 — `P06-F02` is NOT upgraded, and it is NOT withdrawn.**
- It cannot be upgraded to "installed verified": no target-system registry exists.
- It is not withdrawn: the source-tree evidence stands exactly as stated, and it remains the correct statement of what the *code* does.
- **Its boundary is now sharper:** *"0 of 12 custom modules in the P06 scope, as read from the declared source copies, contain any reference to `account.bank.statement`."* That is what was established and all that was established.
- **Status: HOLD — DATABASE EVIDENCE REQUIRED** for any deployment-level claim.

**DME-F-05 — The available evidence nonetheless narrows one thing usefully.**
In a database built by the same vendor for a comparable Thai client, the installed P06-relevant set is **payment-side custom modules on top of stock reference bank modules**: multi-deduction, cheque printing, PromptPay, purchase advance, Thai WHT — with **no cheque-control, no post-dated-cheque, no returned-payment, and no batch-payment module installed**.
That is **corroborating, not confirming**. It is consistent with `P06-F02` and with the v14→v18 regression finding, and it is recorded as **SUPPORTED INTERPRETATION**, never as FACT VERIFIED for the target.

**DME-F-06 — One observation for P07, outside P06's scope but material.**
DM-B (Odoo 19 SaaS) shows a **native** `Withholding Tax on Payment` module installed. If the target generation moves to 19, a platform-native WHT-on-payment capability would sit alongside the custom Thai WHT modules that P06 found mutating the settled amount. **Routed to P07 as a peer note. P06 does not adjudicate it.**

---

## 6. Exact evidence required to close `P06-B-44`

One artefact would close it: an `ir.module.module` export **from the SMEsPlus target database** (the C1/C2 system evidenced in runtime extract S-04), containing `name`, `state` and `latest_version`. Failing that, the server `addons_path` plus the module registry table.

Until then, every deployment statement in the P06 package remains **UNKNOWN**, and this file is the record of why.

---

# End
