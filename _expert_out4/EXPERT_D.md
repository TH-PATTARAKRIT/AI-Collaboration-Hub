# AAS-03 EXPERT D — Lead Code & UI Architect
## Adversarial challenge of the frozen S18 findings brief
Date 2026-09-05. Read-only forensic work. No database written, no source modified, no Odoo server run.

Verdict vocabulary used: SUPPORTED / MISSING / RISKY / CHALLENGED / EVIDENCE REQUIRED NEXT.
No PASS/FAIL wording is used anywhere in this document.

---

# 0. HEADLINE

I was asked to find another population-selection defect. I found **four**, three of them
independent of each other, plus **two defects I committed myself inside this run and corrected**.

| # | Defect | Rung that failed | Effect on the brief |
|---|--------|------------------|---------------------|
| D-01 | Database-artefact census is FORMAT-bound and PATH-SET-bound | PATH SET + PATTERN | 17 artefacts seen; **27 exist**; 1 whole database (`pankhamhom`) invisible |
| D-02 | `S18-11` module-source census is PATH-SET-bound to the volume | PATH SET | "6 of 16 version-matching / 7 zero copies" is **11 of 16 / 3 zero**; the headline "No copy at 18.0.1.10.0" is **disproved** |
| D-03 | "16 installed custom modules" is a NAME-PATTERN population, not a not-core population | POPULATION | The real denominator is **56**, not 16; `accessories` (25 fields on `account.account`) was never in scope |
| D-04 | `S18-06` proves a FILENAME negative and reports it as a BEHAVIOUR negative | UNIT | v18 **does** override the bill-line account; it lives in `account_move.py`, targets `stock_input`, and is the exact mechanism `S18-05` says is unexecuted |
| E-01 | (mine) `--include=*.py` unquoted in zsh → 13 empty greps | executed-not-quoted | corrected in-run, §6 |
| E-02 | (mine) database identity read as "first uuid-shaped string in the file" | identity key | corrected in-run, §5 |

The brief's **conclusions largely survive**. Its **denominators do not**. Every headline number in
`S18-11` is wrong, and `S18-06`'s supporting claim is wrong in a way that removes the reader's
ability to connect `S18-05` to a mechanism.

---

# 1. D-01 — THE DATABASE-ARTEFACT CENSUS (PRIMARY ASSIGNMENT)

### Declared enumeration

* **POPULATION** — every artefact on this host that is, or contains, a PostgreSQL dump of an Odoo database.
* **UNIT** — one artefact file (not one database; not one directory).
* **PATTERN (two widths, executed, reconciled below)**
  * W-ext: filename glob `*.dump`
  * W-magic: first 4096 bytes read and classified — `PGDMP` (pg_dump custom/tar), `PK` + a root
    `dump.sql` member (Odoo web-backup ZIP), literal `PostgreSQL database dump` (plain SQL),
    `ustar` (tar), `\x1f\x8b` (gzip, then decompressed and re-sniffed).
* **PATH SET (three widths)**
  * P-brief: `$HOME` minus `~/Library` and `~/.Trash`, plus `/Volumes/iMacSys`, plus `/Volumes/ChatGPT Installer`
  * P-corrected: P-brief **plus** `~/Library/Mobile Documents` (iCloud Drive) **plus** `~/Library/CloudStorage` (Google Drive)
  * P-root: `/` minus OS-owned trees, `/Users` and `/Volumes` (those covered above)
* Size floor swept at **two widths**: ≥1 MiB (5,821 files) and ≥64 KiB (196,640 files).

### Commands

```
python3 magic_census.py 1048576   # -> SCANNED_FILES_GE_1048576_BYTES=5821
python3 magic_census.py 65536     # -> SCANNED_FILES_GE_65536_BYTES=196640
python3 magic_root.py             # -> ROOT_SCANNED=1018
diff <(grep '^PGDMP' magic_1MB.txt|cut -f3|sort) <(grep '^PGDMP' magic_64KB.txt|cut -f3|sort)
  -> IDENTICAL PGDMP SETS AT BOTH WIDTHS
```

### Reconciliation of the widths

| Enumeration | Result |
|---|---|
| W-ext × P-brief | **17** files |
| W-magic(PGDMP) × P-brief | **17** files |
| extension false positives | **0** |
| extension false negatives inside P-brief | **0** |
| W-magic(PGDMP) × P-corrected | **18** files |
| W-magic(all formats) × P-corrected | **27** artefacts |
| W-magic × P-root | 0 primary artefacts (only prior-session scratchpad extracts) |

**The extension was not the defect here.** Extension and content agree exactly, 17 = 17, inside the
brief's path set. That agreement is itself the evidence that the failure is elsewhere: the census is
wrong because of **PATH SET** and **FORMAT**, and a reviewer who only re-ran the extension test at a
second width would have concluded the census was sound.

### What the 10 missing artefacts are

Invisible to `*.dump`, because they are ZIP or plain-SQL Odoo backups:

```
/Users/admin/Downloads/BK12MAY26_2026-08-03_11-28-04.zip        dump.sql = 282,964,412 bytes  BK12MAY26 | 19.0+e | 251 modules
/Users/admin/Downloads/iEVING_2026-03-30_02-30-18.zip           dump.sql =  50,873,761 bytes  iEVING    | 19.0+e | 179 modules
/Volumes/iMacSys/95_BHPRO_PROJECT/DOCUMENT/iEVING_2026-03-31_06-48-41/dump.sql
                                                                62,458,228 bytes  iEVING    | 19.0+e | 216 modules
```

Invisible additionally because they sit under `~/Library` (pruned):

```
~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/pankhamhom_2026-01-21_06-39-19.dump  PGDMP 29,621,742
~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/pankhamhom_2026-01-21_06-37-17.zip   dump.sql 133,254,922 | pankhamhom | 18.0+e-20250223 | 478 modules
~/Library/.../Downloads/T805efaplus_2025-12-27_07-09-46.zip                T805efaplus | 18.0+e-20250223 | 123 modules
~/Library/.../Downloads/iMSCG_2026-02-27_04-25-59.zip                      iMSCG | 16.0+e | 244 modules
~/Library/.../Downloads/iMSCG_2026-03-04_05-02-51.zip                      iMSCG | 16.0+e | 244 modules
~/Library/.../Downloads/premiumflexiblepackaging-pfp-odoo-main-19975000_2025-12-25_123055_exact_fs.zip
~/Library/.../Downloads/premiumflexiblepackaging-pfp-odoo-staging-25566772_2025-12-26_145450_exact_fs.zip
```

The **largest single database artefact on this host** — a 283 MB `dump.sql` inside
`BK12MAY26_2026-08-03_11-28-04.zip`, an Odoo **19.0+e** database with a 251-module manifest — is
invisible to every enumeration the brief and its predecessors ran. The `.dump` of the same database,
taken 5h40m earlier the same day, was 35.6 MB compressed and *was* seen.

### Why `~/Library` is not a defensible exclusion

The session memory records a real cost — a `$HOME` sweep triggers a macOS permission-prompt storm
across ~855 app-data directories — and prunes `~/Library` for that reason. That reason has authority
over **app-support data**. It has **no authority** over `~/Library/Mobile Documents` (iCloud Drive)
and `~/Library/CloudStorage` (Google Drive), which are *user document stores that Apple and Google
happen to mount under Library*. Both were swept here with no prompt storm:
`ICLOUD_SCANNED_GE_64KB=1369`. The exclusion reason stopped the audit at a boundary it did not cover.

### Deployment identity — the brief's `S18-01` uuid re-derived, and the census extended

Keyed on `ir_config_parameter.key = 'database.uuid'` (not on file position — see E-02):

| artefact | database.uuid | web.base.url |
|---|---|---|
| **idemo18_uat_…20260830** | **551ab874-9acb-11f1-b150-6ec7a480be3d** | **https://occ.smeplus.cloud** |
| BK12MAY26_2026-08-03_05-48-30 | 66d1b52a-4dca-11f1-818f-820e2e6af5e0 | https://vsystem.ving.run |
| iEVING_2026-07-23_10-31-06 | 1f6338ae-2be1-11f1-9465-820e2e6af5e0 | http://103.13.28.67:8069 |
| iSMEs_2026-07-11_05-03-27 | 45a8e08e-5dcd-11ee-90f5-5242ea102159 | https://swr.smeplus.asia |
| iTEST02_2026-06-14 and 2026-07-14 | a1430edc-0033-11f1-97d1-026da7621cc9 (both) | https://t9x.efaplus.cloud |
| occ_sim_pre_perpetual | a6664233-9ef0-11f1-8169-eb09a489ce4b | http://localhost:18018 |
| pankhamhom_2026-01-21_06-39-19 | 4b766580-c84d-11f0-9b17-12a417459fd7 | https://t8z.efaplus.cloud |

**S18-01's uuid is SUPPORTED.** The brief's "NOT among the five uuids in the P04 census" is
**RISKY**: the census it defers to had 5 uuids; 8 distinct uuids are directly readable from PGDMP
artefacts alone, and 27 artefacts / at least 10 distinct `db_name` values exist once format and path
set are corrected. The brief inherited a denominator it did not re-derive.

**Also SUPPORTED, and previously unproved:** `web.base.url.freeze = True`
(write_date 2026-08-25 17:17:00). The OCC identification in `S18-11` rests on a config parameter that
Odoo rewrites on login unless frozen. It is frozen. The identification holds — but the brief asserted
it from a mutable key without checking the freeze.

### Unreferenced evidence directly on the brief's subject

`~/OCC_Odoo18_Simulation_Lab/` holds **7 PGDMP snapshots of a database named `occ_sim`**, including
`evidence/perpetual_at_invoicing/occ_sim_pre_perpetual.dump` (2026-08-24, PG 16.15). The brief's
`S18-02` turns on the v18 `manual_periodic`/`real_time` labels versus v19's `Perpetual (at
invoicing)` relabel. A local lab snapshot named for exactly that transition exists and is not cited.
**EVIDENCE REQUIRED NEXT.**

---

# 2. D-02 — `S18-11` IS ITSELF PATH-SET-BOUND (the brief's own new finding is wrong)

### The brief's claim

> "Full-volume, pattern-scoped `find -type d -name <module>` + manifest version compare: **6 of 16
> have a version-matching source copy; 10 do not** (7 have zero copies by name anywhere; 3 exist only
> at other versions)."
> "`purchase_request` deployed at 18.0.1.10.0: 16 copies on the volume … **No copy at 18.0.1.10.0.**"

### My enumeration

* **POPULATION** — the 16 module names in `s18/custom_installed.txt` (the brief's own list).
* **UNIT** — (a) a directory named `<module>` containing `__manifest__.py`; (b) a ZIP member path
  `…/<module>/__manifest__.py`. Version read from the manifest by regex on both quote styles.
* **PATH SET** — width A: `$HOME` minus `~/Library`,`~/.Trash` + both volumes. Width B: A + ZIP
  members + `~/Library/Mobile Documents`. Width C: B + `~/Library/CloudStorage`.

```
python3 modcensus.py A   -> MODE=A  DIR_HITS=71  ZIP_HITS=0
python3 modcensus.py B   -> MODE=B  DIR_HITS=72  ZIP_HITS=87
```

### Result

| | brief | width A | width B | width C |
|---|---|---|---|---|
| version-matching copy exists | **6 / 16** | **11 / 16** | 11 / 16 | **11 / 16** |
| zero copies by name anywhere | **7** | **4** | 4 | **3** |
| copies only at other versions | **3** | 1 | 1 | 2 |
| `purchase_request` copies | 16 | 25 | 53 | 53 |
| `purchase_request` at 18.0.1.10.0 | **0 — "No copy"** | **1** | **2** | **2** |

**CHALLENGED — the headline of `S18-11` is disproved.** The version-matching `purchase_request`
source does exist:

```
/Users/admin/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request/__manifest__.py
7:    "version": "18.0.1.10.0",
    "name": "Purchase Request",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "depends": ["purchase", "product", "purchase_stock", "hr"],
```
plus the same tree inside `/Users/admin/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36.zip`.

It is in **`$HOME/Downloads`**. The brief searched "the volume". A path set stated as *"full-volume"*
sounds exhaustive and is a scope stated as a description: it names a storage device, not a boundary
over the artefacts.

Version-matching copies now located for 11 of 16, including four the brief placed in its
"zero copies anywhere" bucket:

```
purchase_request                    18.0.1.10.0  /Users/admin/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request
scgl_account_coa_control            18.0.1.0.1   /Users/admin/Downloads/OCC/scgl_account_coa_control
scgl_chatter_compact                18.0.1.1.0   /Users/admin/Downloads/OCC/scgl_chatter_compact
scgl_custom_title_and_favicon       18.0.0.0.2   /Users/admin/Desktop/SMEsPlus/SMEsPlus-SMEsPlus_Extra_18/1800030 Custom_title_and Favicon/scgl_custom_title_and_favicon
scgl_date_range_auto_period         18.0.1.0.0   /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/scgl_date_range_auto_period
scgl_document_terms_conditions      18.0.1.0.0   /Users/admin/Downloads/scgl_document_terms_conditions
scgl_multi_approve_core             18.0.0.3.1   /Users/admin/OCC_Odoo18_Simulation_Lab/addons/scgl_multi_approve_core
scgl_multi_approve_purchase_request 18.0.1.0.0   /Users/admin/Desktop/PURCHASE REQUEST/scgl_multi_approve_purchase_request
scgl_occ_transportation_costs       18.0.1.0.0   /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/scgl_occ_transportation_costs
scgl_product_category_company       18.0.1.5.0   /Users/admin/Projects/pcat_runtime/scgl_product_category_company
scgl_uom_archive                    18.0.1.0.0   /Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/scgl_uom_archive
```

### A second, independent unit failure inside the same enumeration

`find -type d -name <module>` cannot see a module packaged as an archive. Width B added 87 ZIP-member
hits. There is an entire vendor library the directory unit is blind to:
`~/Library/Mobile Documents/com~apple~CloudDocs/Downloads/18000 EXTRA MODULE/` — 59 numbered
directories, many holding the module only as a `.zip`
(`scgl_custom_title_and_favicon_v18.2.zip`, `purchase_request.zip`, `scgl_account_reports ( V18.0.1.3 - Feb05 ).zip`, …).

And a third: `~/Library/CloudStorage/GoogleDrive-scgl.thailand@gmail.com/…/00 ADISAK/local-addons/`
holds `scgl_stock_fleet` and `scgl_occ_transportation_costs` with real `__manifest__.py` files —
`scgl_stock_fleet` is one of the four modules I had called "no copy" at widths A and B. My own zero
was path-set-bound too, one rung further out.

### Negative control (the residual zero set)

```
scgl_delivery_cost         dirs=0  name-matches anywhere=0
scgl_signature             dirs=0  name-matches=6 (all are scgl_jasper_api/models/scgl_signature_image.py — a different module)
scgl_signature_hr_expense  dirs=0  name-matches=0
POSITIVE CONTROL, same finder: scgl_uom_archive -> 1
```

**Three modules, not seven, have no source anywhere in the corrected path set.**

---

# 3. D-03 — "16 INSTALLED CUSTOM MODULES" IS A NAME-PATTERN POPULATION

The brief's population is `scgl_*` plus `purchase_request`. That is an author-chosen name pattern, not
a criterion. I re-derived the population at two independent widths.

**Width 1 — by author** (`ir_module_module.author` not in {Odoo S.A., Odoo SA, odoo, Odoo PS}):
`NON_ODOO_AUTHORED_INSTALLED = 53` of 361 installed.

**Width 2 — by core-tree membership** (installed name absent from the union of six series-18 core
addons trees; `UNION_CORE_MODULE_NAMES=1535`; positive control: `'account' in core -> True`,
`'stock_account' -> True`): `NOT_IN_ANY_CORE_TREE = 55`.

**The two widths disagree, and each has a demonstrated failure mode:**

* Width 1 **drops `scgl_product_category_company`** — the module `S18-12` is entirely about — because
  its manifest declares `author = 'Odoo S.A.'`. Author is not an identity.
* Width 2 **drops `l10n_th`** — deployed at 18.0.2.0 by author *Almacom*, i.e. a third-party module
  occupying a core module's name. Name is not an identity either.
* Width 2 finds two more that width 1 misses: **`construction`**, **`journal_entries_report`**.

**Reconciled population: 56 non-core installed modules. The brief scoped 16.**

### What was outside the brief's 16 and should not have been

| module | deployed | evidence (from `ir_model_data` + `ir_model_fields` in the archive) |
|---|---|---|
| **`accessories`** | 18.0.0.1 | 47 ir_model_data rows; **25 fields added to `account.account`**, 1 to `account.move.line` (`seq`), 2 `ir.model.inherit` rows. It is a **declared dependency of `scgl_account_coa_control`** and is `installed`. |
| `account_invoice_fixed_discount` | 18.0.1.0.0 | adds `account.move.line.discount_fixed` (monetary). v18 `_get_gross_unit_price` branches on `self.discount`. |
| `full_summarize_bills` | 18.0.0.3 | adds `account.move.no`; a vendor-bill summarisation report |
| `om_data_remove` | 18.0.1.0.0 | see §7 — destructive data-removal module, installed |
| `inherit_inventory`, `inherit_sales` | 18.0.0.1 | 1 `ir.ui.view` row each and nothing else; **view-layer only** — a bounded positive |
| `stock_card_report` | 18.0.1.0.0 | inventory-card reporting; 40 fields, all on its own wizard/report models |
| `delivery_cement_truck` | 18.0.0.0 | author NULL; 6 fields, all on `sale.order` |
| `tracking_customer` | 18.0.1.0.0 | 24 fields on `res.partner`/`res.users` only |
| `scgl_signature` | 18.0.1.0.0 | **8 fields on `account.move`** (`signature`, `digital_sign`, `sign_by`, `sign_on`, `show_sign_bill`, …) + 8 on `account.bank.statement.line`. No source copy exists; the field list is the bound. |
| `scgl_delivery_cost` | 18.0.1.0.0 | 2 fields on `stock.picking` (`delivery_cost_id`, `delivery_price`). No source copy exists. |

`S18-12` closes with "This module does NOT touch `property_valuation` or any `property_stock_*`
field — checked explicitly, **because a category customisation is the one thing that could have
falsified S18-02**." The check was correct and the reasoning was correct — but it was run against
1 of 56 candidates.

**Note on method.** `ir_model_fields` has **no `modules` column** in the extracted schema
(`COPY public.ir_model_fields (id, relation_field_id, model_id, …)` — 46 columns, none named
`modules`). My first attempt at this table returned a clean `0 fields` for all nine modules. That zero
was a tool failure indistinguishable from a real result. The figures above come from `ir_model_data`
(`IR_MODEL_DATA_ROWS=225529`), joined to `ir_model_fields.id`, with positive controls
`distinct modules in ir_model_data = 356` and `rows for module 'stock_account' = 168`.

---

# 4. D-04 — `S18-06`: A FILENAME NEGATIVE REPORTED AS A BEHAVIOUR NEGATIVE

### The brief's claim

> "v19 `R3:stock_account/models/account_move_line.py:13-24` `_compute_account_id` sets the bill line
> to `accounts['stock_valuation']` … **v18 `stock_account/models/` contains no `account_move_line.py`
> at all** (directory listed: 15 files, none named that)."
> Section heading: "**Bill-line account override is v19-only**".

### The file fact — SUPPORTED

```
ls -1 "…/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/stock_account/models/"  -> 15 files, no account_move_line.py
```
Generalised, pattern-scoped, over every `stock_account` tree on the host, series taken from the
enclosing `odoo/release.py` `version_info`:

```
(series, has stock_account/models/account_move_line.py)
  ('14','no_aml') 1   ('16','no_aml') 2   ('17','no_aml') 2
  ('18','no_aml') 15  ('19','HAS_AML') 8
  (None, …) 44  <- coverage gap, see below
```
**15 of 15 series-18 trees lack the file; 8 of 8 series-19 trees have it.** Clean separation, both
directions, no counterexample. The file claim is SUPPORTED and now generalised.

### The behaviour claim — CHALLENGED

v18 has a bill-line account override. It is in a different file:

`…/odoo-18.0+e.20250608/odoo/addons/stock_account/models/account_move.py`
```
253: class AccountMoveLine(models.Model):
254:     _inherit = 'account.move.line'
263:     def _compute_account_id(self):
264:         super()._compute_account_id()
265:         input_lines = self.filtered(lambda line: (
266:             line._eligible_for_cogs()
267:             and line.move_id.company_id.anglo_saxon_accounting
268:             and line.move_id.is_purchase_document()
269:         ))
270:         for line in input_lines:
271:             fiscal_position = line.move_id.fiscal_position_id
272:             accounts = line.with_company(line.company_id).product_id.product_tmpl_id.get_product_accounts(fiscal_pos=fiscal_position)
273:             if accounts['stock_input']:
274:                 line.account_id = accounts['stock_input']
276:     def _eligible_for_cogs(self):
278:         return self.product_id.is_storable and self.product_id.valuation == 'real_time'
```

So the equivalent behaviour in v18 **exists, is on the same model, is the same method name, and
targets `accounts['stock_input']`** — which is `property_stock_account_input_categ_id`, the exact
account `S18-05` reports as configured on 15 of 126 categories for all four companies and carrying
**0 journal items**. The brief separated the mechanism from its own finding by looking for a filename.

Generation diff, both directions:

| | v18 (`account_move.py:263`) | v19 (`account_move_line.py:13`) |
|---|---|---|
| target account | `accounts['stock_input']` (GRNI) | `accounts['stock_valuation']` |
| gate: `anglo_saxon_accounting` | **required** | **removed** |
| gate: valuation | `== 'real_time'` (inside `_eligible_for_cogs`) | `== 'real_time'` (inline) |
| gate: dropship | none | `_eligible_for_stock_account()` excludes dropshipped |

**The brief's conclusion still holds.** `_eligible_for_cogs` requires `valuation == 'real_time'`, and
`S18-02` proves every product in all four companies resolves to `manual_periodic`, so the v18 override
cannot fire here. And the predicate is invariant across builds: of the 15 series-18 trees, **14 carry
the byte-identical `_eligible_for_cogs` body** (`is_storable and valuation == 'real_time'`) and 1 has
no `account_move.py` at all (a partial copy). So the conclusion does not depend on which v18 tree was
read — even though **6 distinct contents of `account_move.py`** exist among those 15 trees.

**Restate `S18-06` as:** *v18 does override the bill-line account on purchase documents, to the stock
input (GRNI) account, and that override is inert here because it is gated on `real_time`; v19 moves
the override to a new file, retargets it from `stock_input` to `stock_valuation`, and drops the
anglo-saxon gate.* That third clause is a **migration exposure the brief does not carry**: in v19 the
override fires for companies 2, 3 and 4 (`anglo_saxon_accounting = FALSE`) where in v18 it could not.
**EVIDENCE REQUIRED NEXT.**

### Code identity — a labelled version accepted without content proof

The brief calls one tree "R1: v18". Manifest versions cannot discriminate: v18 core ships
`'version': '1.3'` for `account` and Odoo prefixes the series at install time, so R1's `1.3` and the
deployed `18.0.1.3` agree — as do at least **11 other trees on this host**. Content does discriminate:
**6 distinct `account_move.py` contents across 15 series-18 `stock_account` trees.** Two concrete
hazards found while testing this:

* `/Volumes/iMacSys/CLAUDE AI/MIGRATION/ODOO18/enterprise/addons/stock_account` — path says **ODOO18**,
  content is **v19**: it has `account_move_line.py`, `product_value.py`, and `product.py` matching
  `Perpetual` 3×.
* Two different trees both named `odoo-18.0.post20260605` carry `account/__manifest__.py` at **1.4**
  and **1.3** respectively. A build string does not identify code.

**Coverage assertion.** 44 of the 72 `stock_account` directories on this host could not be series-resolved. Almost all are
`.Encrypted` Google-Drive mirrors whose files are non-materialised cloud stubs (directories present,
`__manifest__.py` absent), plus one Claude-agent `icons_stage` artefact. This is stated as coverage,
not as a result.

---

# 5. E-02 — A DEFECT I COMMITTED AND CORRECTED (identity keyed on position)

My first attempt read each archive's `database.uuid` as *the first uuid-shaped string in the extracted
`ir_config_parameter` file*. For the subject archive that returned `58871b73-c444-4139-b613-ee19140f441f`
— a v4 uuid belonging to a different parameter — where the correct value keyed on
`ir_config_parameter.key = 'database.uuid'` is `551ab874-9acb-11f1-b150-6ec7a480be3d` (a v1 uuid).
The wrong value would have contradicted `S18-01` and I would have raised a false finding against the
brief. Corrected by parsing the `key` column with `pgc.load`; positive control printed:
`rows in subject ir_config_parameter = 56`, and the full key list.

**Rule this exercises:** an identifier read by position in a file is not an identifier. The uuid was
right there; the *key* was what made it an identity.

---

# 6. E-01 — A DEFECT I COMMITTED AND CORRECTED (unquoted glob)

```
grep -rhoE "_inherits?…" "$p" --include=*.py     # zsh: no matches found: --include=*.py
```
Thirteen modules returned an empty inheritance list. Had the shell not printed its own error the
output would have read as "no custom module inherits any accounting model". Re-run with
`--include='*.py'` and a positive control against core `stock_account` (which must return
`account.move account.move.line product.category …` and does).

---

# 7. FURTHER FINDINGS AGAINST THE BRIEF'S CONCLUSIONS

### 7.1 `S18-12` under-declares the module's own hook surface — CHALLENGED (partial)

The brief describes `scgl_product_category_company` 18.0.1.5.0 as adding
"`PurchaseOrder.button_confirm` → `_scgl_validate_product_company_scope` and an `@api.constrains` on
purchase order lines". AST enumeration of the version-matching source
(`/Users/admin/Projects/pcat_runtime/scgl_product_category_company`, `"version": "18.0.1.5.0"`)
gives the full surface:

```
product.category     15 methods incl. _search, 2 @api.constrains
product.template     11 methods incl. name_search, 2 @api.constrains
product.product      _scgl_assert_company_allowed, name_search
sale.order           _scgl_validate_product_company_scope, action_confirm
sale.order.line      @api.constrains('product_id','order_id')
purchase.order       _scgl_validate_product_company_scope, button_confirm
purchase.order.line  @api.constrains('product_id','order_id')
stock.move           @api.constrains('product_id','company_id')
stock.picking        _scgl_validate_product_company_scope, action_confirm, button_validate
account.move         _scgl_validate_product_company_scope, action_post      <-- not in the brief
account.move.line    @api.constrains('product_id','move_id')                <-- not in the brief
```

The guard also wraps **`account.move.action_post`** and constrains **`account.move.line`**. The
brief's vacuity finding is unchanged in direction — 110 of 126 categories still permit everything —
but its scope is understated: the same vacuous guard sits on every posting, every picking validation
and every sale confirmation, not only on PO confirmation.

### 7.2 `om_data_remove` is installed and references the valuation table — RISKY

`om_data_remove` 18.0.1.0.0 is `installed`. The only source copy located is version **19.0.1.1**
(`/Users/admin/Desktop/SMEsPlus/SMEsPlus-SMEsPlus_Extra19/om_data_remove`), so its content is
**not evidence about the deployed 18.0.1.0.0 module**. In that 19.0.1.1 copy:

```
models/model.py:24    sql = "delete from %s" % t_name
models/model.py:153   'stock.valuation.layer',
models/model.py:236   sql = "delete from ir_default where (field_id = %s or field_id = %s) and company_id=%d"
models/model.py:267   'property_stock_valuation_account_id': None,
```

`S18-03` and `S18-04` are counts over `stock_valuation_layer` **as it stands in the archive**. A module
that truncates that table by raw SQL, and separately deletes rows from `ir_default` — the exact table
`S18-02` reads valuation policy from — is installed in this deployment. Prior-session memory records
this module as installed and deleting the ledger unauthorised in another deployment (P06).

This does **not** disprove anything: raw `DELETE` leaves no trace, so absence of evidence of a purge
is expected either way. It bounds the claim: 47,801 layers and the single global
`ir_default` row for `property_valuation` are the post-hoc state of tables a resident, installed
module can silently empty. **EVIDENCE REQUIRED NEXT:** the deployed 18.0.1.0.0 source; and
`ir_logging` / `mail_message` around any invocation of its wizard.

### 7.3 `purchase_request` alters the receipt path `S18-07` counts over — RISKY

Version-matching source, AST-enumerated:
```
purchase.order       button_confirm, unlink, _purchase_request_confirm_message*
purchase.order.line  _prepare_stock_moves, write, update_service_allocations
stock.move           _prepare_merge_moves_distinct_fields, _merge_moves_fields,
                     _prepare_merge_move_sort_method, _action_cancel, copy_data, _check_company_purchase_request
stock.move.line      _action_done, allocate
stock.picking        _action_done
stock.rule           _run_buy, create_purchase_request, _prepare_purchase_request*
```
`S18-07`'s "3,158 [stock moves] linked to a purchase line" and "1,403 done purchase-linked moves" are
counted over a `stock_move` table whose **merge fields and merge sort key are overridden by an
installed module**. The counts are what the data says; their interpretation as a one-to-one
receipt population is not established. **EVIDENCE REQUIRED NEXT.**

### 7.4 Override-surface sweep of the non-core population — bounded negative

* **POPULATION** — the 53 author-derived non-core installed modules (scan run before the
  core-membership width was derived; `construction` and `journal_entries_report` are therefore NOT in
  this scan). Of the 53, **44 have at least one source directory** in the corrected path set and
  **32 have a version-exact copy**.
* **PATTERN** — `property_valuation | stock_input | stock_valuation | _compute_account_id |
  _eligible_for_cogs | _account_entry_move | get_product_accounts | anglo_saxon |
  stock\.valuation\.layer | _validate_accounting_entries | property_stock_account`
* **UNIT** — one file, `--include='*.py' --include='*.xml'`.
* **POSITIVE CONTROL** — same pattern set against core v18 `stock_account` returns 5 files.

**Result: exactly one module matches — `om_data_remove` (§7.2).** Nothing else in the located
non-core sources reads or writes the valuation-policy or GRNI-account path.

**This is a bounded negative, not a clearance.** It binds only to the 44 located sources, only 32 of
which are the deployed version; **9 of the 53 scanned have no source directory anywhere**
(`delivery_cement_truck, equipment_fleet, hr_payroll_other_input, inherit_inventory, inherit_sales,
scgl_delivery_cost, scgl_signature, scgl_signature_hr_expense, tracking_customer`). For all nine the
DB-side field bound in §3 shows none adds a field to
`product.category`, `product.template`, `stock.valuation.layer` or `account.move.line.account_id`.
`construction` and `journal_entries_report` were never in the scanned set and are **not bounded at
all** — EVIDENCE REQUIRED NEXT.

---

# 8. WHAT I DID NOT DISTURB

The following brief claims I re-derived or spot-checked and did not contradict:

* `S18-01` `database.uuid`, `web.base.url` — **SUPPORTED**, and `web.base.url.freeze = True` newly established.
* `S18-01` module counts — **SUPPORTED**: `ir_module_module` 1,369 rows; installed 361 / uninstalled 1,005 / uninstallable 3.
* `S18-06` "v18 `stock_account/models` has no `account_move_line.py`" as a **file** claim — **SUPPORTED** and generalised to 15/15 series-18 trees.
* `S18-02`'s dependence on the v18 `_eligible_for_cogs` predicate — **SUPPORTED and build-invariant** (14 of 15 byte-identical; 15th has no such file).
* `S18-13`'s lesson (a well-formed zero is not self-authenticating) — independently reproduced twice in this run, §3 and §6.

---

# 9. SUMMARY BY VERDICT

**SUPPORTED**
`S18-01` deployment identity (uuid, frozen base URL, module counts). `S18-06` as a file-layout claim,
generalised 15/15 vs 8/8. `S18-02`'s governing v18 predicate, invariant across 6 distinct v18 builds.

**CHALLENGED**
`S18-11` — every headline figure. 6→**11** version-matching; 7→**3** zero-copy; "No copy at
18.0.1.10.0" is **disproved** by `/Users/admin/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request`.
`S18-06`'s "v19-only" — v18 has the same override, on the same model, targeting `stock_input`.
"16 installed custom modules" — the population is **56**.

**MISSING**
Ten database artefacts, including the largest on the host (283 MB `dump.sql`, Odoo 19.0+e) and a whole
database (`pankhamhom`, two artefacts, 478-module manifest). The `occ_sim` simulation-lab snapshot set,
one of which is named for the exact v19 semantic transition `S18-02` turns on. `accessories` —
installed, 25 fields on `account.account`, a declared dependency of a module the brief did analyse.

**RISKY**
`om_data_remove` installed with raw-SQL deletion of `stock_valuation_layer` and `ir_default`, bounding
`S18-02`/`S18-03`/`S18-04` as post-hoc states. `purchase_request` overriding stock-move merge keys and
`_action_done`, bounding `S18-07`'s move population. `S18-12`'s hook surface understated by two models.
The v19 override dropping the `anglo_saxon_accounting` gate — companies 2, 3, 4 are `FALSE` today.

**EVIDENCE REQUIRED NEXT** (ranked)
1. Read `BK12MAY26_2026-08-03_11-28-04.zip::dump.sql` (283 MB, Odoo **19.0+e**). It is the only
   large v19 database artefact on this host and `S18-02`/`S18-06` are entirely about the v18→v19
   semantic change.
2. Deployed `om_data_remove` 18.0.1.0.0 source; then `ir_logging` around its wizard.
3. `occ_sim_pre_perpetual.dump` — a local snapshot named for the `Perpetual (at invoicing)` transition.
4. Bound `construction` and `journal_entries_report` via `ir_model_data`.
5. Re-run any inherited census (the "five uuids") against the 27-artefact / 10-database corrected set.

---

# 10. THE TRANSFERABLE RULE

Every defect in this report is one shape:

> **A negative about the evidence base was proved at a narrower boundary than the claim it was used
> to support, and the boundary was stated as a description rather than declared as a set.**

* "full-volume" described a *storage device*; the file was in `$HOME`. (D-02)
* "custom modules" described a *name prefix*; the population was *not-core*. (D-03)
* "no `account_move_line.py`" proved a *filename*; the claim was about *behaviour*. (D-04)
* "`~/Library` is app data" was true of app data and false of iCloud Drive and Google Drive. (D-01)

The counter-measure that actually worked in this run was not searching harder. It was **running each
enumeration at two widths and reconciling them** — and treating *agreement* as evidence
(17 = 17 on extension-vs-content; 15/15 vs 8/8 on the generation split; 14/15 byte-identical
predicates) exactly as seriously as disagreement. The extension test agreed at both widths and was
still built on the wrong path set. **Width agreement on one rung is not evidence about another rung.**
