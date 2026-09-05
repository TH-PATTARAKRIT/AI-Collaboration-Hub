# 31 — G02-P02 DEPLOYED-CODE IDENTITY REGISTER

`LAYER 2 — AUDIT QUARANTINE.` Task **C2**. Baseline `ff8be51`. **OLD SESSION CONTINUATION.**

The question is not *what does the standard root contain* but **what code can materially change the
behaviour of each deployed P02 process being used as evidence**.

---

## 1. Method And Its Controls

| Step | Executed |
|---|---|
| Installed modules per deployment | `ir_module_module` where `state='installed'`, offline `pg_restore`, column positions read from the `COPY` header **by name** |
| Standard-module set | Union of the module directories of four reference roots (v14 127, v16 59, v18 797, v19 1,427, +v19 enterprise 1,425) = **1,634 distinct standard names** |
| Source availability | Host-wide index of **every** directory containing `__manifest__.py` — **58,263 directories, 3,174 distinct module names** |
| Non-standard = | installed name **not** in the 1,634-name standard union |

**Denominator declaration.** POPULATION: the 11 deployed databases with journal lines > 0. PATTERN:
`state='installed'`. PATH SET: the four reference roots for "standard", the whole host for "source
available". UNIT: **one (database, module) pair** — not a module name, because the same name in two
deployments is two facts.

**Control on the standard set.** The v16 root contributes only 59 names and v14 only 127 — far short of
a full distribution. **The standard union is therefore a floor, and "non-standard" here means "not found
in the roots available on this host", not "not shipped by the vendor".** Modules flagged non-standard on
the two v16 and two v14 deployments are the least reliable rows in this register, and are marked
accordingly. This is stated because an under-sized standard set inflates the custom count, which would
overstate the finding.

---

## 2. Installed-Module Census

| uuid | gen | deployment | installed | non-standard | P02-relevant non-standard |
|---|---|---|---|---|---|
| `25e88cd4` | 14.0 | iErpOCC | 215 | 36 | **13** |
| `5d5164c4` | 14.0 | odoo_cff_golive_99 | 590 | 409 | **178** |
| `45a8e08e` | 16.0 | iSMEs | 190 | 13 | **7** |
| `a1cdeab8` | 16.0 | e8db984d-56e7-489f-80db-38c5c55320e2 | 244 | 25 | **9** |
| `1d1f5d3e` | 18.0 | iSMEs182 | 174 | 6 | **0** |
| `551ab874` | 18.0 | 4e640e74-6222-4a51-bbcb-4f91686fcc16 | 302 | 26 | **9** |
| `57d32e15` | 18.0 | premiumflexiblepackaging | 308 | 28 | **11** |
| `4b766580` | 18.0 | pankhamhom | 478 | 6 | **1** |
| `1f6338ae` | 19.0 | iEVING | 232 | 18 | **9** |
| `66d1b52a` | 19.0 | BK12MAY26 | 251 | 19 | **9** |
| `a1430edc` | 19.0 | iTEST02 | 486 | 34 | **12** |

**258 P02-relevant non-standard (database, module) pairs. 69 have readable source on this host; 189 do
not.** The classification vocabulary required by the prompt is applied per row in §4.

---

## 3. `P02-F-31a` — RE-23 Extended: The Override Gap Is Not One Deployment

`RE-23` recorded that `inherit_sales` and `inherit_inventory` are installed in `idemo18_uat` and exist
nowhere on this host. **They are installed in two deployments, on two different generations:**

| uuid | gen | deployment | modules | source |
|---|---|---|---|---|
| `551ab874` | 18.0 | idemo18_uat | `inherit_sales`, `inherit_inventory` | **SOURCE GAP** |
| `25e88cd4` | 14.0 | iErpOCC | `inherit_sales`, `inherit_inventory`, `inherit_log_occ` | **SOURCE GAP** |

By name these override the two modules P02 is entirely about. **Neither can be read.** No behavioural
conclusion is drawn from the names — that is the whole point of the gap.

## 4. `P02-F-31b` — The Largest Deployment By Volume Is The Least Readable

`odoo_cff_golive_99` (`5d5164c4`, 14.0) carries **1,708,287 journal lines — 67% of every line measured
in this package** — and **590 installed modules, of which 409 are non-standard**: 316 in a `cu_*`
family and 37 in a `cff_*` family. **Source is absent for essentially all of them.**

| Classification | Meaning here |
|---|---|
| `STANDARD SOURCE FACT` | holds for the standard modules of the generation, subject to §1's floor caveat |
| `DEPLOYED CODE VERIFIED` | the installed-module list is verified; **the code is not** |
| `DEPLOYED BEHAVIOUR VERIFIED` | **not available** for this deployment |
| `SOURCE GAP` | **409 modules**, including every `cu_account_*` module touching payment, deposit, WHT, taxation, exchange rate and reporting |

**Consequence, stated exactly.** Every source-derived P02 negative is **inapplicable** to this
deployment. What survives for it is only what was measured directly from its data: 1,708,287 journal
lines, **zero `cogs` markers** (injection-controlled), 434,152 valuation layers of which 382,163 carry
an accounting entry. **A measured fact needs no source; an explanatory fact does.**

## 5. `P02-F-31c` — A Readable Custom Set Exists, And It Touches P02 Directly

For `idemo18_uat` (`551ab874`), 15 `scgl_*` modules are installed and **11 are readable on this host**.
Four are P02-material by subject and are carried into `32` (C3):

| module | why it is P02-material | source |
|---|---|---|
| `scgl_product_category_company` | product category × company — the object carrying `property_valuation` and the three stock accounts, which is the whole of `P02-F-05` | READABLE |
| `scgl_occ_transportation_costs` | freight / delivery charges — **business scenario 7, currently an open gap in `24`** | READABLE |
| `scgl_date_range_auto_period` | automatic period assignment — bears on cut-off and the lock-date behaviour (`P02-F-08`) | READABLE |
| `scgl_account_coa_control` | chart-of-accounts control | READABLE |
| `scgl_delivery_cost`, `scgl_signature`, `scgl_signature_hr_expense` | delivery cost is P02-material by name | **SOURCE GAP** |

The lab additionally holds readable copies of `account_payment_multi_deduction`,
`l10n_th_withholding_tax`, `l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax_multi` and
`scgl_wht_control` — the payment-deduction and Thai WHT overrides the prompt names as high priority.

## 6. Disposition

| Class | Count | Note |
|---|---|---|
| `DEPLOYED CODE VERIFIED` (module list) | **11 of 11** deployments | every material deployment enumerated |
| `SOURCE GAP` (P02-relevant, non-standard) | **189** (database, module) pairs | no behavioural conclusion drawn |
| Readable custom, P02-relevant | **69** pairs / **46** distinct names | worked in `32` |
| `DEPLOYED BEHAVIOUR VERIFIED` | see `33` §3 | only the read-only runtime facts obtained from the live lab |

**`P02-F-31d` — the artefact rule from `30`.** This register reports **302** installed modules for
`551ab874` where `22` and `18` publish **361**. Both are correct: two artefacts of one `database.uuid`,
different snapshots. Per `P02-F-30a`, every figure here names the artefact it came from.
