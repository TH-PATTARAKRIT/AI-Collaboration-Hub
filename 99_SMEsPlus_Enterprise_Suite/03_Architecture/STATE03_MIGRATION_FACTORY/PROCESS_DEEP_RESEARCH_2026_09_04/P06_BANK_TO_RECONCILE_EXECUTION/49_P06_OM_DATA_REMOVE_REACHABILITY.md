# P06_OM_DATA_REMOVE_REACHABILITY.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S06)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **NO DESTRUCTIVE PATH WAS EXECUTED AGAINST ANY DATABASE.** Reachability below is established from the source call graph, access configuration and module metadata only. Where runtime proof would be required, the item is held rather than asserted.

---

## 1. The reachability chain, link by link

| # | Link | Evidence | Blocks? |
|---|---|---|---|
| 1 | Module present on disk | 4 of 4 custom roots | no |
| 2 | Module **installed** in the target database | **UNKNOWN** — `P06-OQ-98`, no target registry | **this is the load-bearing unknown** |
| 3 | Model `res.config.settings` exists | always — core model | no |
| 4 | Method is public and undecorated | `remove_all`, `remove_account`, `remove_account_chart`, `remove_message` — no leading underscore, no `@api.private` | no |
| 5 | RPC route reachable | `/web/dataset/call_kw`, `auth="user"` | **any authenticated user** |
| 6 | Dispatch guard | `get_public_method` blocks only private/`@api.private` | no |
| 7 | `call_kw` access check | **none** — `browse(ids)` then invoke | no |
| 8 | Method body ORM check | **none** — raw SQL on `self._cr` | no |
| 9 | Postgres role permits `DELETE` | **NOT ASSESSED** — see §3 | possible, unverified |

**Links 3–8 are verified from source and none of them blocks.** Links 2 and 9 are the only candidate blockers, and both are deployment facts this session does not hold.

---

## 2. Two conditions decide everything

**REACH-F-01 — Condition A: is the module installed on the target?**
If **no**, the destructive path is not dispatchable there, and `B-50` is a **latent supply-chain risk** — a module sitting in the addons tree of four copies, one of them locally customised for this project's Thai withholding-tax certificates, available to be installed by anyone with module-install rights.
If **yes**, the path is live and every link in §1 applies.

**One `ir.module.module` export settles it.** This is `L1` in the leverage graph and the highest-value artefact in the whole package.

**REACH-F-02 — Condition B: does the database role permit `DELETE` on those tables?**
Odoo conventionally runs as the owner of its own schema, in which case `DELETE` is permitted. If a deployment has separated roles, Postgres would refuse — **and the exception would be swallowed to a `_logger.warning` in the v18 copies** (`44_` OMD-F-06), so the operator would see the button appear to succeed while nothing was deleted.
**This is a real mitigation worth checking rather than assuming, and it is uncommon in practice.** **HOLD — DEPLOYMENT EVIDENCE REQUIRED.**

---

## 3. What the compiled bytecode does and does not show

`__pycache__` directories exist in three of four copies:

| Copy | Bytecode | Implies |
|---|---|---|
| CUST18 | `cpython-313` | imported under Python 3.13 |
| CUST14 | `cpython-37`, `cpython-38` | imported under 3.7 **and** 3.8 |
| MIGR18 | `cpython-310` | imported under 3.10 |
| T8MASTER | **none** | never imported from this path |

> **WITHDRAWN AT THE SUPPLEMENTAL ROUND — REV-E-15.** The reading below is superseded. A PEP-552 header decode shows every embedded source mtime is **2022 or 2024**, years before the 2026 file mtimes, and one CUST14 `.pyc` encodes a source size matching no file on the volume. **These `__pycache__` directories were shipped inside vendor archives and copied with the source. None evidences a local import.** The only genuine local compilation on the workstation belongs to `om_data_remove_fix` (CPython 3.10, 2026-05-27, embedded mtime matching its source exactly). **The installation question is answered by registry evidence instead — see `58_`: the module is `installed` on the `iEVING` Odoo 19 database.**

**REACH-F-03 — Bytecode proves IMPORT, not INSTALLATION, and it is weak evidence in both directions.**
Python writes a `.pyc` when a module is imported. Odoo imports every module found on the `addons_path` during registry construction **whether or not it is installed in the database**, so bytecode is consistent with the module merely being *visible* to a server that started up.
**It does establish one thing:** three of the four copies have at some point been on an `addons_path` of a running interpreter. **It establishes nothing about which database, which server, or whether the module was ever installed or invoked.**
**Timestamps are filesystem metadata, not audit evidence, and are not used here.**

The absence of bytecode in T8MASTER is equally weak — a copy may have been cleaned, or copied after import.

---

## 4. Reachability by caller class

| Caller | Reaches the destructive method? | Basis |
|---|---|---|
| Administrator via the menu | **yes** | menu `groups="base.group_system"` renders; button issues the RPC |
| Administrator via RPC | **yes** | trivially |
| **Ordinary authenticated user via RPC** | **yes on the source chain** — no link in §1 blocks them | links 5–8; **runtime unverified** |
| Ordinary user via the UI | **no** | the menu is not rendered for them — **and this is not a control**, only an absence of convenience |
| Unauthenticated caller | **no** | `auth="user"` requires a session |
| Portal / public user | **needs assessment** — they hold a session. Whether portal users can reach `/web/dataset/call_kw` for an arbitrary model was **not traced**. Recorded as `P06-OQ-101` |

**REACH-F-04 — The gap between "administrator via the menu" and "ordinary user via RPC" is the entire finding.** The first is the intended use of a database-cleanup tool. The second is what the code permits.

---

## 5. Classification

> **UPGRADED AT THE SUPPLEMENTAL ROUND.** Registry evidence was subsequently obtained (`58_`): `om_data_remove` is recorded `installed`, version `19.0.1.1`, in the `iEVING` database dump (`dump.sql:155063`, `manifest.json` `version: 19.0+e`), and a matching `Installed` row appears in a module-registry export. **Condition A of §2 is answered — the module IS installed somewhere.** Whether it is installed on the *SMEsPlus target* remains open.
> **Revised classification: `REACHABLE — DEPLOYMENT VERIFIED` on a v19 database not confirmed to be the SMEsPlus target.** The source-chain classification below stands as the v18 analysis.

**DESTRUCTIVE REACHABILITY (v18 source analysis): `SOURCE-REACHABLE / RUNTIME UNVERIFIED`.**

Stated precisely: **every link in the dispatch chain from an authenticated HTTP session to the unfiltered `DELETE FROM` is present and verified in source, and no link was found that performs an authorisation check.** No execution was attempted, so the chain is not runtime-verified; and two deployment conditions — module installation and database-role permissions — are unknown and could each independently make the path unreachable on a given system.

**This is deliberately the weaker of the two available classifications.** `REACHABLE — VERIFIED` would require execution, and execution against a real database is prohibited and would in any case be the wrong way to establish this.

---

## 6. What would move the classification

| To reach | Requires |
|---|---|
| `REACHABLE ONLY WITH SPECIFIC PRIVILEGE` | evidence that some link does check a group — **none found**; would overturn §1 |
| `UNREACHABLE — VERIFIED` | proof the module is not installed on the target **and** cannot be installed |
| `REACHABLE — VERIFIED` | a controlled, isolated, non-production fixture — **not attempted, and not proposed**; the source evidence is sufficient for a design decision and execution would add risk without adding information |
| `CONFIGURATION-DEPENDENT` | this is arguably already true via Condition A; it is folded into the source-reachable classification rather than used to soften it |

---

## 7. Open items

| ID | Item | Class |
|---|---|---|
| `P06-OQ-98` | Is the module installed on the target? | **HOLD — DEPLOYMENT REGISTRY EVIDENCE REQUIRED** |
| `P06-OQ-101` | Can a portal user reach `/web/dataset/call_kw` for an arbitrary model? Not traced. | C |
| `P06-OQ-102` | Does the deployed Postgres role permit `DELETE` on the accounting tables? | **HOLD — DEPLOYMENT EVIDENCE REQUIRED** |
