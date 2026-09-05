# P06_DEPLOYED_MODULE_REGISTRY_PROOF.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S09)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **THIS FILE CLOSES THE PACKAGE'S LONGEST-STANDING EVIDENCE GAP, AND IT OVERTURNS THREE PRIOR P06 CONCLUSIONS.** Registry evidence was obtained. `om_data_remove` is **installed**. And a remediation module written by this programme states that the destructive path was **exercised against a live database**.

---

## 1. Registry evidence obtained — an Odoo database backup

**DMR-F-01 — A complete Odoo database dump exists on the workstation and records the module as installed.**

`/Volumes/iMacSys/95_BHPRO_PROJECT/DOCUMENT/iEVING_2026-03-31_06-48-41/` — `dump.sql` (62,458,228 B) + `manifest.json` + `filestore/`, dated 2026-03-31.

`manifest.json`, parsed: `odoo_dump: 1` · `db_name: iEVING` · `version: 19.0+e` · `version_info: [19, 0, 0, 'final', 0, 'e']` · **216 modules** · and:
```
modules["om_data_remove"] == "19.0.1.1"
```

`dump.sql:155063`, the `ir_module_module` row:
```
936 … om_data_remove  Odoo Mates, Sunpop.cn  /om_data_remove/static/description/icon.png  installed  19.0.1.1  {"en_US": "Odoo 18 Remove Data"} … LGPL-3 … Settings/Remove Data
```

Supporting `ir_model_data` rows — `dump.sql:103137`, `:136251-136256`: the module record (2026-03-18), and its view, action and **menu** (2026-03-31). `dump.sql:163446` carries the view body: *"Data Cleaning (Be careful to do that!)"*.

**This is the only Odoo backup on the volume** — `find … -name "dump.sql"` → 1 hit.

**DMR-F-02 — And the module-registry export corroborates it.**
`~/Downloads/Module (ir.module.module).xlsx`, row 994:
```
['Odoo 18 Remove Data', 'Odoo Mates, Sunpop.cn', '', '19.0.1.1', 'Installed']
```
Round 3 read these exports and **did not find this row**, because it searched on the technical name `om_data_remove` while the export column carries the **display name**. The row was there.

---

## 2. FIRST-PARTY EVIDENCE THAT THE DESTRUCTIVE PATH WAS EXERCISED

**DMR-F-03 — A remediation module for `om_data_remove` sits inside the V18E core addons directory, and its manifest describes real damage.**

`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/om_data_remove_fix/__manifest__.py:1-5`:
```
'name': 'OM Data Remove Fix - Orphan Reference Cleaner',
'version': '18.0.1.0.0',
'summary': 'Fixes "Missing Record" errors caused by om_data_remove (orphan mail.message, '
           'mail.notification, mail.activity, bus.bus, ir.attachment, ir.model.data references)',
```
`:15-17`:
```
`om_data_remove` uses **raw SQL** (`DELETE FROM <table>`) to wipe transactional
data. Because the deletes bypass the ORM, none of the following references are
cleaned up:
```
`:26-30`:
```
    Missing Record
    Record does not exist or has been deleted.
    (Record: stock.picking(58,), User: 2)
```

It overrides the destructive primitive itself — `om_data_remove_fix/models/res_config_settings.py:65`: `def remove_data(self, o, s=None):`.

**And its bytecode shows genuine local compilation**: `orphan_cleaner.cpython-310.pyc` carries an embedded source mtime of `2026-05-27T01:27:38Z`, exactly matching its `.py` on disk, written two minutes later — the signature of a real import under CPython 3.10 in Asia/Bangkok.

**DMR-F-04 — Classification, stated carefully.** This is **`SUPPORTED INTERPRETATION`, not `FACT VERIFIED`, that the tool was fired.** A manifest docstring is a narrative claim, not a log. What is `FACT VERIFIED` is that **someone in this programme wrote, compiled and shipped a module whose stated purpose is to clean up after `om_data_remove` ran**, and quoted a specific user-facing error with a record id and a user id. **No `ir_logging` extract, no `odoo.log` and no journald artefact was located** to convert it.

**It is nonetheless the strongest evidence in the entire P06 package that a documented destructive path was used in anger.**

---

## 3. The copy denominator was wrong — 4 is 17

**DMR-F-05 — `find /Volumes/iMacSys -type d -name "om_data_remove"` returns 17 directories**, plus `om_data_remove.zip`, `om_data_remove_fix.zip` and a staging folder.

| Version band | Copies | Notable |
|---|---|---|
| `1.0.0` | CUST18, T8, CUST14, `ODOO 12/addons` | the four P06 examined + one |
| `18.0.1.1` | MIGR18, `18.0.5_account/extra addons`, `SMEsPlus18/02_base_Extramodule` | |
| **`19.0.1.1` / `19.0.1.2`** | **7 copies**, incl. `ODOO19/SMEsPlus-SMEsPlus_Extra19`, `ODOO19/efaplus-custom`, `MIGRATION/SMEsPlus19`, BHPRO ×2 | matches the installed version |
| `16.0.1.0.1` | `Odoo16/addons` | |

**DMR-F-06 — And three copies are rebranded `SMEsPlus Remove Data`** — including **two under `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/`**, this programme's own account workspace.
**Classification: `SUPPORTED INTERPRETATION`, downgraded at challenge (E3-S-04).** The manifest `author` remains `Odoo Mates, Sunpop.cn` in every copy; only `name` changes. **That is equally consistent with white-labelling by whoever assembled the distribution, which may be the vendor rather than this programme.** The alternative is recorded, not disposed of — `P06-OQ-115`.

**Consequence:** the round-3 statement *"present in all four custom roots"* was true but **materially understated**. The module is present in **17** locations across four Odoo generations, has been **renamed to carry the project's own name**, and one copy has been **functionally extended for the project's Thai withholding-tax certificates** (`44_` OMD-F-02). **Recorded as REV-E-13.**

---

## 4. Deployment configuration — what was and was not found

**DMR-F-07 — Four config files exist; none places any `om_data_remove` copy on an `addons_path`.**
`find /Volumes/iMacSys -maxdepth 6 \( -name "odoo.conf" -o -name "odoo-server.conf" -o -name "docker-compose*.yml" -o -name "*.service" \)` → **4 hits**:
1. `CLAUDE AI/SMEsPlus18/odoo.conf:67` — `addons_path = /opt/odoo/custom/smesplus_th_base,/opt/odoo/addons,/opt/odoo/enterprise`. **Container paths that do not exist on this workstation**; header records `Build : 18.0+e.20250608` and `Maintainer: Claude AI`. An authored template, not a captured runtime config.
2. `CLAUDE AI/MIGRATION/SMEsPlus19/96_combined/odoo.conf` — v19 layout, *"Verified: 807 modules"*.
3–4. two `docker-compose` files with no `addons_path`.
**No `*.service` unit — NOT FOUND** in that scope.

**So: the module is proven installed on `iEVING` (v19), and the `addons_path` that loaded it is not recorded anywhere on this workstation.** `P06-OQ-98` moves from *"is it installed?"* — **answered, yes, somewhere** — to *"is it installed on the SMEsPlus target?"* — **still open**.

---

## 5. Classification

| Question | Round 3 | **Now** |
|---|---|---|
| Registry evidence obtained | **NO** | **YES — a database dump and a matching export row** |
| `om_data_remove` installed | UNKNOWN | **INSTALLED — VERIFIED on `iEVING`, Odoo 19.0+e, version 19.0.1.1** |
| Installed on the **SMEsPlus target** | UNKNOWN | **STILL UNKNOWN** — `iEVING` is a BHPRO-programme database |
| Destructive path exercised | not assessed | **SUPPORTED INTERPRETATION — yes**, per `om_data_remove_fix` |
| Copy count | 4 | **17** |
| Deployment `addons_path` | not searched | **NOT FOUND** |

**`P06-B-50` reachability is upgraded from `SOURCE-REACHABLE / RUNTIME UNVERIFIED` to `REACHABLE — DEPLOYMENT VERIFIED (on a v19 database that is not confirmed to be the SMEsPlus target)`.**

---

## 6. What this does to the leverage graph

Round 3 and `48_` both named the target module registry as the single highest-leverage artefact. **A registry has now been obtained — and it is not the target's.** The leverage claim survives but its object narrows:

> **The remaining artefact is an `ir.module.module` export from the SMEsPlus production or UAT database specifically** — the C1/C2 system evidenced in runtime extract S-04 — **not any Odoo database.**

**And one new query is now more valuable than that export.** The dump is on disk and readable. Querying `iEVING` for the orphan signature this analysis predicts — `account_full_reconcile` rows with zero surviving `account_partial_reconcile` children, `account_move_line.full_reconcile_id` pointing at them, and `matching_number` values violating the ORM constraint — **would convert "the tool was installed" into "the tool was fired, and here is the damage."** Recorded as `P06-OQ-112`, and it is the highest-value unrun query in the package.

---

## 7. Open items

| ID | Item | Class |
|---|---|---|
| `P06-OQ-98` | Installed on the **SMEsPlus target**? | **HOLD — DEPLOYMENT REGISTRY EVIDENCE REQUIRED** |
| `P06-OQ-112` | Query `iEVING`'s dump for the predicted orphan signature | **the highest-value unrun query** |
| `P06-OQ-113` | Which of the 17 copies any server loaded — no `addons_path` records it | D |
| `P06-OQ-114` | Execution proof: no `ir_logging`, `odoo.log` or journald artefact located | D |
| `P06-OQ-115` | Three copies are rebranded with the project's name; who did so and why is unrecorded | D |
