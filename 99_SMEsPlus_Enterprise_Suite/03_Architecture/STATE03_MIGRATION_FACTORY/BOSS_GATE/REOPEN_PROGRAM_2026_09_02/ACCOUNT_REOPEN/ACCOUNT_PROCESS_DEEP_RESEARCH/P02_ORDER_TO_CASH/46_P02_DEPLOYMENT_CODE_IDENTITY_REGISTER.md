# 46 — P02 DEPLOYMENT CODE IDENTITY REGISTER

*(mandated semantic name `32_P02_DEPLOYMENT_CODE_IDENTITY_REGISTER.md`; 32 taken, next free number used per §15.)*

`LAYER 2 — AUDIT QUARANTINE.` **CP-04.** Baseline `aca211e`.

**Purpose: bound the claim.** Where code identity is unresolved, benchmark source behaviour must **not**
be converted into deployed behaviour. Only the five statuses mandated by §8 are used.

**Keyed on LINEAGE, not uuid** (`44`, as amended by `P02-F-45a`). Where a lineage carries several uuids
the row says so; where one uuid covers several live instances the row says that too.

---

> ## ⚠ CORRECTION BANNER — `C-54`, `C-55` (AAS-03 Expert 1, CONFIRMED)
>
> **`C-54` — this register declares lineage keying and delivers uuid keying.** The header says *"Keyed on
> LINEAGE, not uuid"*, and the table below then lists **`1f6338ae` iEVING and `66d1b52a` BK12MAY26 as two
> separate rows** — the exact pair `45` §5 confirmed as **one lineage** by the founding-company test.
> The 11 rows are 11 of the 17 **uuids**. **The identity model published in this round is not applied by
> the register published in this round** — the defect class this round exists to close, reproduced inside
> it. **Read the table as uuid-keyed until rebuilt** (next action 2 in the resume state).
> Consequence: the merged lineage is **one** row, so the register's transactional denominator is
> **10 lineages with data, not 11 uuids**.
>
> **`C-55` — the v16 caveat is not applied to the deployment that carries the headline.** `45a8e08e`
> (`iSMEs`) is **16.0** and supplies **447,384 of 493,277 marker-capable journal lines = 90.7%** of the
> zero-COGS evidence. This host holds **59 module directories for 16.0 against 797 for 18.0**, so its
> **standard** source is effectively unreadable. Its status below reads `PARTIAL MATCH`; the caveat
> immediately above says 16.0 rows should read `SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED`. **Corrected
> status for `45a8e08e`: `STANDARD SOURCE UNREADABLE`.**
>
> **This is the largest unstated gap in the round.** The custom-module gap in `§2` concerns `odoo_cff`,
> which `C-43` had **already excluded** from the marker-capable denominator. The gap that bites is this
> one: **90.7% of the headline evidence comes from a generation whose standard source cannot be read at
> all**, so no source-derived P02 negative transfers to it.

> **`C-83` — THE "readable source" COLUMN DOES NOT REPRODUCE FOR THE TWO 16.0 LINEAGES, AND THE STATUS
> FIELD STILL SAYS `PARTIAL MATCH`.** An independent sweep (population: directories containing
> `__manifest__.py`/`__openerp__.py`; unit: basename; path set: `/Volumes/iMacSys` + `$HOME` + `/Volumes/iMac`)
> returned **0 for all ten** module names underlying the 16 `SOURCE-ON-HOST` rows of `45a8e08e` and
> `a1cdeab8`, while positive controls fired in the same run (`account` 74, `stock_account` 72,
> `scgl_account_coa_control` 6) and a negative control returned 0. **23% of the 69-module "readable
> source" total is unreproducible**, and there is **no 16.0 or 14.0 core distribution anywhere on this
> host**. The caveat below already said these rows should read `SOURCE AVAILABLE BUT NOT PROVEN
> DEPLOYED`; **the table kept printing `PARTIAL MATCH`. A correction in prose that never reaches the
> status column is the "audit your disposition table" defect — peers cite the field, not the paragraph.**
> **Both 16.0 rows are hereby `SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED`.**
>
> **`C-84` — this file contradicts itself.** §1 states *"`MATCH VERIFIED` is used for no deployment"*;
> §4 then prints **`MATCH VERIFIED`** for two containers. §4's basis is `ir_module_module` name+version
> read from a running instance — the identification method this register elsewhere rules insufficient.
> **§1 is scoped to archived lineages; §4's rows are downgraded to `SOURCE AVAILABLE BUT NOT PROVEN
> DEPLOYED`, and are in any case not re-verifiable — the container runtime is down (`C-78`).**
>
> **`C-85` — there is no module-version dimension at all.** Every row of the census for one database
> carries **one identical version string**, which is the database's **`base`** version, not the module's:
> the 16.0 artefact shows `base 16.0.1.3` while `account` is `16.0.1.2` and `stock_account` is `16.0.1.1`.
> **The census cannot compare even module versions, let alone code.** No row may be graded above
> `SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED` until `ir_module_module.latest_version` is extracted
> per module — it is present in every artefact.


> ## ✅ MAJOR REVERSAL — `C-86`. THE REFERENCE DISTRIBUTIONS EXIST. `C-55` IS WITHDRAWN.
>
> Every sweep in this programme pruned `~/Library` (adopted from the TCC prompt-storm lesson). **Full
> Odoo reference distributions for 14, 15, 16, 17, 18 and 19 sit inside it**, at
> `~/Library/CloudStorage/GoogleDrive-…/00 SW_SOURCE CODE/`:
>
> | distribution | module directories |
> |---|---|
> | **14 ODOO 14 ENTERPRISE** | **796** |
> | **16 ODOO 16 ENTERPRISE** | **950** |
> | 15 / 17 / 18 / 19 | present |
>
> Verified to contain `account`, `stock_account`, `sale_stock` — the exact modules P02 needs.
>
> **What this withdraws:**
> - **`C-55` — WITHDRAWN.** *"90.7% of the headline evidence comes from a generation whose standard
>   source cannot be read at all"* is **false**. A **950-module 16.0 Enterprise distribution** is on this
>   host. The "59 module directories" figure came from `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/addons`,
>   a **custom** directory mistaken for the distribution.
> - **`46` §2 / `C-43` side-note — "no 14.0 root exists on this host": false** (796 dirs).
> - **`31` §1's "the standard union is a floor"** — the floor was drawn far too low.
> - **Expert 4's `CH-4`** ("0 for all ten module names; no 16.0 or 14.0 core distribution anywhere") —
>   **refuted**; its sweep pruned `Library` too.
>
> **Quantified effect — the custom-module counts across the package were OVERSTATED.** Standard union
> rebuilt: **1,634 → 1,932 names**. Non-standard installed modules re-derived:
>
> | lineage | gen | published | **corrected** |
> |---|---|---|---|
> | `45a8e08e` **iSMEs** | 16.0 | 13 | **1** |
> | `a1cdeab8` | 16.0 | 25 | **3** |
> | `25e88cd4` iErpOCC | 14.0 | 36 | **23** |
> | `5d5164c4` odoo_cff | 14.0 | 409 | **380** |
> | **total rows** | | **620** | **540** |
>
> **The deployment carrying 90.7% of the marker-capable evidence runs ONE non-standard module, and its
> standard source is readable.** That is a materially **stronger** position than the package claimed.
>
> **How it was missed.** A blanket prune, adopted for a good reason (a TCC prompt storm), was never
> declared as an evidence-affecting exclusion and was inherited by **three P02 sweeps and two independent
> experts**. *Shared blind-spot agreement*, recurring — and this time the shared blind spot was one the
> package had itself written into its method.

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

**CORRECTED (`C-55`).** The original sentence — *"`iSMEs182` and `pankhamhom` are the only rows where the standard-source reading transfers"* — is **false on this register's own table**: `45a8e08e` and `a1cdeab8` are also `PARTIAL MATCH`, and `45a8e08e` carries 447,384 lines. The accurate statement is narrower and worse: **`iSMEs` has data *and* a nominally-readable custom set, but is 16.0, for which no standard distribution exists on this host.** **Both are small** — 22 and 25 confirmed
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
