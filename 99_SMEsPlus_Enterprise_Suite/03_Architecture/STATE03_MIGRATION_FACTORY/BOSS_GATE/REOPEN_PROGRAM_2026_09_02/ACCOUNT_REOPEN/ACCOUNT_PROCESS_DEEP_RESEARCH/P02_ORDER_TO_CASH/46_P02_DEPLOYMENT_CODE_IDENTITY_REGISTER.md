# 46 — P02 DEPLOYMENT CODE IDENTITY REGISTER

*(mandated semantic name `32_P02_DEPLOYMENT_CODE_IDENTITY_REGISTER.md`; 32 taken, next free number used per §15.)*

`LAYER 2 — AUDIT QUARANTINE.` **CP-04.** Baseline `aca211e`.

**Purpose: bound the claim.** Where code identity is unresolved, benchmark source behaviour must **not**
be converted into deployed behaviour. Only the five statuses mandated by §8 are used.

**Keyed on LINEAGE, not uuid** (`44`, as amended by `P02-F-45a`). Where a lineage carries several uuids
the row says so; where one uuid covers several live instances the row says that too.

---

## 1. Register

| Lineage (founding company / label) | Gen | Installed | Non-standard | P02-relevant non-standard | with readable source | **STATUS** |
|---|---|---|---|---|---|---|
| `1d1f5d3e` iSMEs182 | 18.0 | 174 | 6 | 0 | 0 | **PARTIAL MATCH** — no P02-relevant custom module |
| `1f6338ae` iEVING | 19.0 | 232 | 18 | 9 | 7 | **SOURCE MISSING** (2 of 9) |
| `25e88cd4` iErpOCC | 14.0 | 215 | 36 | 13 | 7 | **SOURCE MISSING** (6 of 13) |
| `45a8e08e` iSMEs | 16.0 | 190 | 13 | 7 | 7 | **PARTIAL MATCH** — all P02-relevant custom source readable |
| `4b766580` pankhamhom | 18.0 | 478 | 6 | 1 | 1 | **PARTIAL MATCH** — all P02-relevant custom source readable |
| `551ab874` 4e640e74-6222-4a51-bbcb-4f | 18.0 | 302 | 26 | 9 | 4 | **SOURCE MISSING** (5 of 9) |
| `57d32e15` premiumflexiblepackaging | 18.0 | 308 | 28 | 11 | 1 | **SOURCE MISSING** (10 of 11) |
| `5d5164c4` odoo_cff_golive_99 | 14.0 | 590 | 409 | 178 | 14 | **DEPLOYED CODE IDENTITY UNRESOLVED** |
| `66d1b52a` BK12MAY26 | 19.0 | 251 | 19 | 9 | 7 | **SOURCE MISSING** (2 of 9) |
| `a1430edc` iTEST02 | 19.0 | 486 | 34 | 12 | 12 | **PARTIAL MATCH** — all P02-relevant custom source readable |
| `a1cdeab8` e8db984d-56e7-489f-80db-38 | 16.0 | 244 | 25 | 9 | 9 | **PARTIAL MATCH** — all P02-relevant custom source readable |

> **CAVEAT ON THE "readable source" COLUMN — it is a NAME match, not a CODE match.** A module counts as
> having readable source if its **name** appears as a directory anywhere in the host's 3,174-name module
> index. That index spans **all** generations, so a 16.0 deployment's module can be "found" as an 18.0
> directory of the same name. **This package has already recorded that a name does not identify code**;
> the column is therefore an **upper bound on availability**, never evidence of a match. It is the reason
> no row reads `MATCH VERIFIED`, and the reason the 16.0 rows in particular should be read as
> `SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED` rather than as `PARTIAL MATCH` — the v16 reference root on
> this host contributes only 59 module directories, far short of a distribution.

**`MATCH VERIFIED` is used for no deployment.** Nothing in this estate proves that the code running a
deployment is the code read on this host. The nearest is `PARTIAL MATCH`, and that only where no
P02-relevant custom module is installed or all such source is readable.

## 2. `P02-F-46a` — The Volume Is Concentrated Where The Code Is Least Known

`odoo_cff_golive_99` carries **1,708,287 journal lines — the single largest deployment in the
population — and 178 P02-relevant non-standard modules of which only 14 have readable source.** It is
the one row that earns `DEPLOYED CODE IDENTITY UNRESOLVED` outright.

**Consequence, stated exactly:** every source-derived P02 negative is **inapplicable** to it. What
survives for that deployment is only what was measured from its own data — and after `C-43`, even its
zero-`cogs` measurement is a **schema fact**, since 14.0 does not carry `cogs` in the field's selection.
**For this deployment P02 has neither a source basis nor a behavioural marker.**

## 3. `P02-F-46b` — Two Deployments Have No P02-Relevant Custom Code At All

`iSMEs182` (18.0) and, at the P02 surface, `pankhamhom` (18.0, 1 module) are the only rows where the
standard-source reading transfers with little qualification. **Both are small** — 22 and 25 confirmed
sale lines. **The deployments P02 can reason about are the ones with almost no data; the deployments
with data are the ones it cannot read.**

## 4. Live Deployment Instances — Code Identity Is Known Here And Nowhere Else

| container | databases | gen | code identity |
|---|---|---|---|
| `occ-odoo18-db` | 7, one lineage (`a6664233`) | 18.0 | **MATCH VERIFIED for the standard stack** — modules and versions readable directly from the running instances; **differing module state across the seven** |
| `bhpro92-db` | `bhpro92_test`, `bhpro_tracking_test_20260901` | **19.0** | **MATCH VERIFIED** — `stock_account`/`sale_stock` installed, `anglo_saxon_accounting = true` on the second |

**These are the only `MATCH VERIFIED` rows in the package — and all nine are transaction-empty.**
Code identity and business evidence are, in this estate, **mutually exclusive**.

## 5. Bound

The census reads `ir_module_module` from **one artefact per lineage**. Per `44` §1.2 a snapshot is not a
lineage: `551ab874` reports **302** modules here and **361** in `22`, from two artefacts of the same
lineage. **Every row above names the artefact it came from in the underlying data, and none of these
counts is a property of the lineage.**
