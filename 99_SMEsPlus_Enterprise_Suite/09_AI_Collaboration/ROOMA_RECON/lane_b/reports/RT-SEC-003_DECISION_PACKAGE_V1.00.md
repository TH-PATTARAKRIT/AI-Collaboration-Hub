# RT-SEC-003 — DECISION PACKAGE V1.00
**SMEsPlus Enterprise Suite · ROOM A · Lane B (Gemini) · RED TEAM**
Prepared 2026-09-26 · Asia/Bangkok · Status: **PREPARED ONLY — READY FOR BOSS DECISION**
Author: RED TEAM (Lane B audit session) · Reconciler/Approver: not the author

> Every number below was measured on the live study server on 26 Sep, as `roomb_observer` (uid 5),
> read-only. Scripts and raw outputs are in `~/ROOMB_WORKSPACE/reports/` and `ops/`. Nothing was changed.

---

## 1. The finding, restated

`roomb_observer` holds **7 shared groups** (Sales User: All Documents · Accounting/Invoicing ·
Purchase User · Inventory User · Employees/Officer: Manage all employees · Show Full Accounting
Features · Role/User) plus the dedicated **group 120** (BOSSDEC-002 A). Batch W1-STD was collected
under these rights. Open question from the handover: *are these rights wider than a real user, and
must the excess be removed?*

## 2. What the measurements changed — the question has two sides, not one

| Measure (26 Sep, exact) | Value | Evidence |
|---|---|---|
| Menus in the system (census denominator) | **681 menus · 492 leaf screens · 30 sections** | `batches/W1-SCREENS/MENU_TREE.json`, tree hash `c5d68d14…` |
| Menus the observer actually sees in the UI (`load_menus`) | **163 menus · 108 leaf screens · 18 sections** | `reports/RT-SEC-003_ui_visible_observer.json` |
| Share of leaf screens reachable by menu with today's rights | **108 / 492 = 22 %** | same |
| Sections invisible to the observer (12) | Attendances · Fleet · Link Tracker · Live Chat · Manufacturing · Project · Recruitment · Settings · Surveys · Tests · Timesheets · eLearning | same |
| Leaves gated by `Role / Administrator` (base.group_system) alone | **95 (all of Settings) + ~1 per section** | `reports/RT-SEC-003_groups_needed.json` |

**Side 1 — realism (the original concern).** Rights wider than a plain user distort only
*permission-behaviour* observations. Boss ruled 26 Sep that Lane B collects results and does not
answer questions, and permission questions left Lane B (RT-LANEB-015). This side is therefore
**largely retired** for the census model.

**Side 2 — coverage (new).** For a census, today's rights are **too narrow**: 78 % of leaf screens
are unreachable through the menu. Gemini's Stage 2 would honestly report `REACHED: no` for most
of the denominator. This side is the one that now needs a decision.

**Correction to the census label (RT-LANEB-017, new).** `census_menu_tree.py` prints
"681 menus visible to this account". Measured: the RPC `search` returns all 681 menus to the
observer with or without `ir.ui.menu.full_list` — it is the **full system surface**, not what the
account sees. The number is right as a denominator; the label is wrong. Fix is one string.

## 3. Model estimates for reduced profiles (upper bounds — calibrated, use with care)

`ops/rtsec003_menu_impact_estimate.py` models menu-group visibility only (it cannot see
`ir.model.access`, so it overstates). Calibration: for the current profile it predicted ≤201 menus /
≤129 leaves; measured 163 / 108. Treat every estimate as **"no more than"**.

| Profile | Direct groups | Menus ≤ | Leaf screens ≤ | Sections lost vs today |
|---|---:|---:|---:|---|
| A  current 8 groups | 8 | 201 (measured 163) | 129 (measured 108) | — |
| B  Role/User + group 120 only | 2 | 89 | 54 | CRM · Events · Inventory · Invoicing · Purchase · Repairs |
| C  drop HR-Officer + Full-Accounting | 6 | 172 | 112 | none |
| D  drop Full-Accounting only | 7 | 188 | 123 | none |

Reading: removing the two "elevated" groups (C) costs ~15 % of what the observer sees today and
retires Side 1 entirely; it does nothing for Side 2.

## 4. Which groups gate the hidden screens (measured)

Per section, the groups the observer does **not** hold that gate its hidden leaf screens
(full table: `reports/RT-SEC-003_groups_needed.json`):

| Section | leaves | in UI | gating group(s) not held |
|---|---:|---:|---|
| Settings | 95 | 0 | Access Rights · **Role / Administrator** |
| Invoicing | 41 | 17 | Accounting / Administrator [20] · Analytic Accounting [4] |
| Inventory | 37 | 14 | Inventory / Administrator [37] |
| Sales | 32 | 8 | Sales / Administrator [24] |
| Website | 31 | 13 | Role / Administrator [15] · Website / Editor and Designer [8] |
| CRM | 25 | 10 | Sales / Administrator [25] |
| Employees | 23 | 8 | Employees / Administrator [23] |
| Recruitment | 19 | 0 | Recruitment / Officer [19] · Interviewer [19] |
| Live Chat | 16 | 0 | Live Chat / User [16] |
| Project | 15 | 0 | Project / User [15] · Administrator [15] |
| Fleet · Manufacturing | 14 · 14 | 0 · 0 | Fleet / Officer: Manage all vehicles · Manufacturing / User |
| Time Off · eLearning · Events | 14 · 13 · 13 | 4 · 0 · 2 | Time Off / Administrator · eLearning / Officer · Events / User |
| Purchase · Contacts · Maintenance | 12 · 10 · 10 | 6 · 1 · 7 | Purchase / Administrator · Contact / Creation · (Role/Admin ×1) |
| Attendances · Timesheets | 9 · 9 | 0 · 0 | Officer: Manage attendances · Timesheets / User: all timesheets |
| Repairs · Expenses · Surveys · Link Tracker · Calendar | 5 · 6 · 5 · 4 · 3 | 1 · 3 · 0 · 0 · 1 | Inventory/Admin · Expenses/Admin · Surveys/User · — · Role/Admin |

Two facts follow. (1) **Settings (95 leaves = 19 % of the denominator) is reachable only with
`Role / Administrator`** — the role that can install and uninstall modules, i.e. move the frozen
baseline. (2) Every other section opens with an **app-level** Administrator/Officer/User group,
none of which can touch the module set.

## 5. Options

| | Option | Consequence | Risk | Cost | Schedule | Reversible |
|---|---|---|---|---|---|---|
| **A** | Keep `roomb_observer` as is; census covers ≤108/492 by menu; rest recorded `REACHED: no`; RT-SEC-003 closed as *risk accepted* | Stage 2 stalls at 22 % — an honest but nearly useless census | low | 0 | none | yes |
| **B** | Strip to Role/User + group 120 | ≤54 leaves; kills the census; also breaks W1-STD S6 continuity | — | low | none | yes |
| **C** | Widen `roomb_observer` with every app Administrator group (no Role/Administrator) | coverage → ≤397/492; but the **same account writes** S6 transactions — a wide, write-capable AI-driven account; W1-STD collected under a profile that no longer exists → must be re-run | med-high | 1 odoo-shell script | +1 day | yes, but evidence trail muddied |
| **D** ★ | **Two accounts, separated duties**: keep `roomb_observer` as the narrow **S6 transaction** account (writes only in company 2); create **`roomb_census`** — wide **read-by-procedure** account with the app-level groups of §4, **never** Role/Administrator, Access Rights or Technical | census → ≤397/492 (≤333 if deferred sections excluded); W1-STD untouched; Settings excluded from UI census, feature switches captured via `res.config.settings` metadata (S2, reachable since BOSSDEC-002 A) | medium — Odoo rights are additive, so `roomb_census` *can* write inside its apps; held by controls below | 1 odoo-shell script, grant-script pattern (backup · before · apply · after · rollback) | unblocks Stage 2 same day | yes — deactivate the account |
| E | Give the census account Role/Administrator to reach Settings | closes the last 95 leaves | **high — the account could move the frozen baseline**; contradicts Lane B prohibition 5 | — | — | — |

**Controls that make D acceptable (Odoo cannot make a wide account read-only by groups alone):**
1. `roomb_census` is used **only** by the deterministic census scripts (`census_menu_tree.py`,
   `census_screens.py`) — GET navigation and screenshots; the scripts contain no write call.
2. Gemini keeps the **one-command rule** (`GEMINI_TASK.md`): it never holds a shell beyond that command.
3. **Detective audit after every census batch** (read-only): search key models for
   `create_uid` / `write_uid` = census uid; expected 0. Result goes in the batch report. Any hit = batch VOID.
4. Installed-set hash before and after every batch (existing safety trip; the account cannot change it anyway
   without Role/Administrator).
5. Password lives only in `credentials/roomb_census.env` (mode 600); never in a task file.

## 6. Recommendation

**Option D.** It is the only option that raises coverage without touching the account whose
evidence already exists, and it converts RT-SEC-003 from "remove rights" into a **separation of
duties** design: one account observes widely and writes nothing; the other writes narrowly and
observes little. The Side-1 concern on `roomb_observer` (groups 90, 29) is **deferred** until the
module-specific question sets say what S6 transactions actually need — removing them now would be
a change without a requirement behind it.

## 7. Decisions requested from Boss

| ID | Decision | Options |
|---|---|---|
| **BOSSDEC-003 A** | Adopt the two-account model (Option D) | D ★ / A / C |
| **BOSSDEC-003 B** | Census group set for `roomb_census`: all app-level groups in §4, **excluding** Role/Administrator, Access Rights, Technical | approve list / amend |
| **BOSSDEC-003 C** | Deferred sections (Website · eLearning · Live Chat · Link Tracker) — include in census with `SCOPE: NEXT_PHASE_SECTION`, or exclude by withholding their groups | include+flag / exclude |
| **BOSSDEC-003 D** | Settings (95 leaves): exclude from UI census; cover feature switches via S2 metadata | approve / Boss captures Settings personally, once |
| **BOSSDEC-003 E** | `roomb_observer` groups 90 + 29: defer to MVQ (recommended) or remove now (profile C) | defer ★ / remove |
| ack | RT-LANEB-016 (gate fix, applied 26 Sep) — close · RT-LANEB-017 (census label) — open, one-string fix | — |

```
Governance: PREPARED ONLY. Not Boss Final Approval. Author ≠ approver.
No change was made to any account, group or access rule while preparing this package.
```
