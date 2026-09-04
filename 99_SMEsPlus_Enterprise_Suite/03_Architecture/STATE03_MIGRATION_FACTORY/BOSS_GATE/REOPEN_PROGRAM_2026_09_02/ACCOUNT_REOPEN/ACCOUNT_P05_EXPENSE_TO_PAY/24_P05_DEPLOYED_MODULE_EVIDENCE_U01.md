# 24 — P05 DEPLOYED MODULE EVIDENCE (`U-01`)

`LAYER 2 — AUDIT QUARANTINE`

## 1. Evidence Class and Method

`U-01` asked which modules are actually installed. The continuation directive required the **highest
available evidence class** and forbade inferring deployment from source directories.

**Evidence class obtained: `ir_module_module` table rows from real Odoo databases.** That is the
system's own installed-module registry — the authoritative record, one class above a manifest and two
above a directory listing.

**Method — read-only, no database touched.** The dumps are PostgreSQL custom-format archives read
**offline as files**. No server was started, no database created, no connection opened.

```bash
pg_restore --data-only --table=ir_module_module -f <out.sql> <dump>     # v1.14/v1.15 archives
/opt/homebrew/Cellar/postgresql@18/18.6/bin/pg_restore ...              # v1.16 archives
```

`pg_restore` requires `-f` (file or `-`); without it the command errors rather than writing anywhere.
No `-d` was ever supplied, which is the flag that would target a live database.

## 2. Registries Located

| # | Registry | Source | Odoo version | Modules known | Installed |
|---|---|---|---|---|---|
| `R-a` | `iSMEs` | `~/Downloads/iSMEs_2026-07-11_05-03-27.dump` (148 MB, owner `scgl`) | **16.0** | 1009 | 190 |
| `R-b` | `occ_sim_baseline` | `~/OCC_Odoo18_Simulation_Lab/snapshots/occ_sim_baseline.dump` | **18.0** | 707 | 41 |
| `R-c` | `iEVING` | `~/Downloads/iEVING_2026-07-23_10-31-06.dump` (24 MB) | **19.0** | 1504 | 232 |
| `R-d` | `BK12MAY26` | `~/Downloads/BK12MAY26_2026-08-03_05-48-30.dump` (34 MB, owner `efaplus`) | **19.0** | 1508 | 251 |
| `R-e` | `iTEST02` (Jun) | `~/Downloads/SOURCE CODE/iTEST02_2026-06-14_14-41-19.dump` | **19.0** | 1548 | 486 |
| `R-f` | `iTEST02` (Jul) | `~/Downloads/iTEST02_2026-07-14_16-34-51.dump` (61 MB) | **19.0** | 1559 | 453 |
| `R-g` | module export | `~/Downloads/Module (ir.module.module).xlsx` | **19.0** | 1441 rows | — |

Version is taken from the `base` module's `latest_version` in each registry, not from the file name.

## 3. P05 Module Install Matrix

`INST` = installed · `uninst` = present in the registry but not installed · `—` = **absent from the
registry entirely**, i.e. not on that deployment's `addons_path`.

| Module | iSMEs v16 | OCCsim v18 | iEVING v19 | BK12 v19 | iTEST02-Jun v19 | iTEST02-Jul v19 | Findings gated |
|---|---|---|---|---|---|---|---|
| `hr_expense` | INST | uninst | INST | INST | INST | INST | `F-01`,`F-19`..`F-28`,`E1-01`,`E1-05`..`E1-14` |
| `hr_expense_extract` | uninst | — | uninst | uninst | **INST** | **INST** | `E1-02` / `TZ-10` |
| `hr_expense_predict_product` | INST | — | INST | INST | INST | INST | — |
| `sale_expense` | INST | uninst | INST | INST | INST | INST | `E1-15`, `U-05` |
| `project_hr_expense` | uninst | uninst | uninst | uninst | INST | INST | — |
| `hr_payroll_expense` | uninst | — | uninst | uninst | **INST** | **INST** | `E1-03` / `TZ-11` |
| `documents_hr_expense` | — | — | uninst | uninst | INST | INST | — |
| `account` | INST | INST | INST | INST | INST | INST | core |
| `account_payment` | INST | uninst | INST | INST | INST | INST | core |
| `account_disallowed_expenses` | uninst | — | — | — | — | — | `TX-24` |
| `account_reports` | INST | — | INST | INST | INST | INST | — |
| `l10n_th` | INST | INST | INST | INST | INST | INST | — |
| `l10n_th_reports` | — | — | **INST** | **INST** | **INST** | **INST** | `TX-01` subsystem A |
| **`hr_expense_petty_cash`** | uninst | — | — | — | — | — | **`TZ-01`, `TZ-02`, `EX-04`, `E2-01`..`E2-05`** |
| `hr_expense_sequence` | uninst | — | — | — | — | — | `E2-04`, `E2-05` |
| **`scgl_advance_expense_request`** | — | — | uninst | uninst | uninst | uninst | **`F-07`, `GL-04`, `GL-05`, `TZ-07`, `TZ-08`, `E3-01`..`E3-11`** |
| **`scgl_purchase_advance_payment`** | **INST** | — | **INST** | **INST** | **INST** | **INST** | **`E3-12`, `E3-13`, `E3-14`, `E3-16`** |
| **`l10n_th_withholding_tax`** | **INST** | — | **INST** | **INST** | **INST** | **INST** | **`TX-03`,`TX-04`,`TX-08`..`TX-11`,`TX-17`,`TX-18`** |
| `l10n_th_withholding_tax_multi` | — | — | uninst | uninst | uninst | uninst | `TX-05` |
| **`l10n_th_withholding_tax_cert`** | **INST** | — | **INST** | **INST** | **INST** | **INST** | **`TX-12`,`TX-13`,`TX-14`,`TX-20`** |
| `l10n_th_withholding_tax_cert_form` | INST | — | INST | INST | INST | INST | `TX-19` |
| `l10n_th_withholding_tax_report` | INST | — | INST | INST | INST | INST | `TX-15`, `TX-16` |
| `account_payment_multi_deduction` | — | — | uninst | uninst | **INST** | **INST** | `TX-06` |
| `multi_level_approval` | — | — | INST | uninst | uninst | INST | `U-06` |
| `full_payment_custom` | — | — | — | — | — | — | `TX-22` |
| `print_payment_remittance_adviec` | uninst | — | uninst | uninst | uninst | uninst | `TX-21` |
| `print_voucher_request` | INST | — | uninst | uninst | INST | INST | — |
| `invoice_promptpay` | — | — | INST | INST | INST | INST | — |
| `purchase` | INST | uninst | INST | INST | INST | INST | `E3-12`..`E3-16` |

Corroborated by table presence: `petty_cash` and `advance_expense_request` **tables do not exist** in
any dump examined, while `purchase_advance_payment_bill`, `account_withholding_tax`,
`withholding_tax_cert` and `withholding_tax_cert_line` do.

## 4. What This Evidence Does **Not** Prove — read before using §3

> **No Odoo 18 database containing the P05 surface exists in the available evidence.**

The P05 source research was conducted against `odoo-18.0+e.20250608`. Of the seven registries: one is
v16, four are v19, one is a v19 spreadsheet export, and the **only** v18 database (`R-b`) is a
41-module Community sandbox in which `hr_expense` is *uninstalled* and **not one** of the P05 custom
modules is even present.

Therefore, with classes per the Negative Claim Control:

| Claim | Class |
|---|---|
| "In these six registries, `hr_expense_petty_cash` is installed in none." | **A** — verified absence within the stated registries |
| "`hr_expense_petty_cash` is not installed in the SMEsPlus v18 target." | **D — UNKNOWN.** No v18 P05 deployment was found. **This is not upgraded.** |
| "The deployed estate installs the Thai WHT stack and the purchase-advance module." | **A** within the five real business databases |
| "Module install state is uniform across the estate." | **E — CONTRADICTED.** It varies materially: `hr_expense_extract`, `hr_payroll_expense` and `account_payment_multi_deduction` are installed in the two `iTEST02` registries and in none of the others; `multi_level_approval` is installed in two of five. |

The `odoo.conf` at `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo.conf` names `db_name = smesplus_th`
with `addons_path = /opt/odoo/custom/smesplus_th_base,/opt/odoo/addons,/opt/odoo/enterprise`.
**No dump of `smesplus_th` was found.** That configuration file also states, in its own header, that
`addons_archive` must not be on the `addons_path` — which independently corroborates `21 NC-02`'s
treatment of the archive as non-deployed.

## 5. Disposition

| Aspect | Disposition |
|---|---|
| Module state of the **deployed estate** | **RESOLVED — EVIDENCE VERIFIED** (six registries, class A within them) |
| Module state of the **v18 target platform** | **HOLD — DATABASE EVIDENCE REQUIRED.** Specific ask: a dump or an `ir_module_module` export of `smesplus_th`, or of any Odoo 18 database carrying the P05 custom modules. |
| `U-01` overall | **PARTIALLY RESOLVED.** No longer a blanket unknown; the residue is precisely named. |

## 6. Consequence for Finding Severity

Reclassification is applied in `26` and `28`. In summary: the two most severe findings in the package
(`TZ-01` petty cash, and the entire employee-advance chain) are **not reachable in any evidenced
deployment**, while the purchase-advance and Thai WHT findings are **live in five of five** real
business databases. This inverts the package's severity ranking — see `37 §2`.
