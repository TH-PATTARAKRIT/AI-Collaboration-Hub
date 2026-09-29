# Source Map (candidate) — `board`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `board` |
| Display name | Dashboards |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `96066050abb40eb6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/board/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `mis_builder` — AGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Productivity / Build your own dashboards
- Inventory of user-facing artifacts (counts): menu items 1, views 1, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `board.board` (Board)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 29 of 30 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: board (Dashboards / "My Dashboard")

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/board.json. Pointers are `module/path:LINE`; (TEST) = derived from tests (front-end unit tests exist under board/static/tests per manifest, not read: board/__manifest__.py:27-29).

## A. Capabilities / functions
- Lets each user build a personal dashboard ("My Dashboard") from saved list/graph/pivot/etc. views that they pin from any screen (board/__manifest__.py:11-14; entry point board/controllers/main.py:11-12).
- Optional: no auto_install and no application flag; installed on request. Depends only on spreadsheet_dashboard (board/__manifest__.py:16), which supplies the parent Dashboards menu.
- Adds a "My Dashboard" menu under the Dashboards root (board/views/board_views.xml:31-36) opening a form-type screen that the web client renders as a board (board/models/board.py:51-53; action board/views/board_views.xml:19-26). The toolbar is disabled in that action (board/views/board_views.xml:23).
- "Add to dashboard" service: given an action, filter, context and view mode from the caller, the service inserts a new tile at the top of the first column of the requesting user's own copy of the dashboard (board/controllers/main.py:14-41). The tile stores the view type, title, the filter and the context; the multi-company selection is deliberately dropped from the saved context so the tile is not permanently filtered to the companies active at pin time (board/controllers/main.py:24-27).
- Returns failure (false) if the dashboard action or its column is missing or the action id is empty (board/controllers/main.py:16, 23, 44).

## B. Business objects, relationships, lifecycle
- Virtual "board" model: no table and no stored records; create does nothing (board/models/board.py:8-10, 18-20). It exists only to carry the form layout.
- Personalisation object: a per-user customised copy of the base layout, stored as a user-specific view override (board/models/board.py:31; created board/controllers/main.py:37-41). Lookup is by current user and base view; if one exists the user's layout replaces the shipped layout when the screen opens (board/models/board.py:31-34).
- Base layout is a two-column-ratio board with one empty column, shipped as "no update" data so administrator edits survive upgrades (board/views/board_views.xml:3-16, style 2-1 at :10).
- Each pin creates a new override record rather than modifying the previous one (board/controllers/main.py:37); which of several overrides wins when a user has more than one: the lookup takes the first match only (board/models/board.py:31 limit 1) and ordering was not verified: UNKNOWN — EVIDENCE INSUFFICIENT.
- Lifecycle: pin -> tile appears -> user may rearrange/remove tiles via the client (client code not read: UNKNOWN — EVIDENCE INSUFFICIENT).

## C. Validations, automation, security, multi-company
- Tiles whose action is marked invisible (i.e. not permitted for the user) are stripped out when the layout is served (board/models/board.py:42-48).
- Access: all internal users have read-only access to the virtual board model (board/security/ir.model.access.csv:2). Personalisation records are written with elevated rights inside the controller (board/controllers/main.py:14, 37), because the underlying custom-view model is otherwise limited to system administrators (base/security/ir.model.access.csv:38). Route requires a logged-in user (board/controllers/main.py:11).
- Per-user scoping: layout lookup and creation are keyed on the current user (board/models/board.py:31; board/controllers/main.py:38). No record rules or company field in the module.
- Content of each tile is executed with the viewer's normal rights when the tile is rendered (standard client behaviour; not shown in this module: UNKNOWN — EVIDENCE INSUFFICIENT).

## D. Accounting / payroll / analytic handoffs
- None. It reuses whatever models the pinned actions point to; no financial ownership.

## E. Configuration / defaults that change outcomes
- Default layout style and column count from the shipped view (board/views/board_views.xml:10-11). Administrators may change the base view; per-user overrides continue to take precedence.
- Menu position: sequence 100 under the Dashboards root (board/views/board_views.xml:36).
- Multi-company: tiles do not remember the company selection (board/controllers/main.py:24-27).

## F. Effective extension path (module names only)
- Depends on: spreadsheet_dashboard. Extends: the web client (front-end assets in board/static/src per board/__manifest__.py:22-26), base custom-view model. Manifest dependents of board: none found. It coexists with spreadsheet dashboards (spreadsheet_dashboard, spreadsheet_dashboard_* modules) under the same root menu.

## G. Not verified
- Front-end behaviour (drag/drop, removal, layout switching): UNKNOWN — EVIDENCE INSUFFICIENT.
- Which override wins when several exist for one user: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; not asserted as universal.

