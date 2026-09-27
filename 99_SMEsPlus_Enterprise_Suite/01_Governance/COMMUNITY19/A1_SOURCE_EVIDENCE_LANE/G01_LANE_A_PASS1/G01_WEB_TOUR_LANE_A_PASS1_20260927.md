# G01 PLATFORM_BASE — Module `web_tour` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T1 |
| Group | G01 PLATFORM_BASE |
| Module | `web_tour` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/web_tour/`) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Nothing here is runtime proof. Source presence does not show runtime reachability. No Formal Coverage is claimed. No GMVQ QIDs are answered.

## 1. Evidence Pointer Table

| Path (addons/web_tour/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 5945c1565cf76b2ec760a3c7a0e90e26e072b5f2 | Deps, data, asset bundles |
| `__init__.py` | 0650744f6bc69b9f0b865e8c7174c813a5f5995e | Package imports (models only) |
| `models/__init__.py` | 21a7f8bde633f7a64ad4d827a8a3b37dc3886fbe | Model imports |
| `models/tour.py` | 575bf0a5953a383c2733c7775ec699f6e73724ac | Tour and tour-step models |
| `models/res_users.py` | 9ab9decb169d9902b0a51494694447f972b5236d | Per-user onboarding flag |
| `models/ir_http.py` | 1e7889a99ee503313d0dc65c2ffe4ab89ac01df2 | Session info extension |
| `security/ir.model.access.csv` | 71ea4517ba59b0a592677b7cc6e6c3ccaec14619 | ACLs |
| `views/tour_views.xml` | c80188dc901a523a0ffb2ec0c3a78b33d828dc1b | Views, action, menu, server action |

Blobs cited: **8**. `controllers/__init__.py` returned HTTP 404 and is not cited (see gaps).

## 2. Findings by Card Section

### 2.1 Manifest / deps / purpose
1. WHAT: this module provides guided onboarding and test tours for the web client. It depends only on `web`, is `auto_install`, category Hidden, license LGPL-3. WHY: it provides in-app user guidance and scripted UI walkthroughs, and it serves as test infrastructure. RISK: the same step engine is used for user onboarding and for automated UI tests, which couples those two concerns. (`__manifest__.py`)
2. There are 2 data files (ACL, views). Assets are injected into `web.assets_backend`, `web.assets_frontend`, `web.assets_unit_tests` and `web.assets_tests`, and the module defines 4 bundles of its own (common, interactive, automatic, recorder). The recorder bundle is the in-UI tour authoring tool. JS was not studied. (`__manifest__.py`)

### 2.2 Data (models, inheritance, key fields, identity)
3. New model `web_tour.tour`. It holds a name (required), a starting URL (default `/odoo`), a computed sharing URL (base URL plus a tour query arg), a completion message (translatable HTML), a sequence, a `custom` flag, and a many2many of users who consumed the tour. Identity: a unique constraint on `name`. Order: sequence, name, id. (`models/tour.py`)
4. New model `web_tour.tour.step`. It holds a trigger (required), content, a tooltip position (bottom/top/right/left, default bottom), a `run` instruction and a sequence, plus a required link to the tour that cascades on delete and is indexed. (`models/tour.py`)
5. Extension of `res.users`: a stored, editable computed boolean `tour_enabled` (label "Onboarding"). It is computed at creation (it depends on `create_date`) and is true only for admin users when no module has demo data and no test is running. (`models/res_users.py`)

### 2.3 Business rules / states / lifecycle / exceptions
6. Current tour selection applies only when the user is internal and has tours enabled. It returns the first tour by order that is not `custom` and that the user has not consumed. (`models/tour.py`)
7. Consume: for an internal user, the named tour is linked to the user's consumed set (a sudo write), and then the next current tour is returned. RISK: tour progress is tracked per user with no per-company scope. (`models/tour.py`)
8. A user can toggle their own `tour_enabled` through a model method that writes under sudo on the current user only. (`models/res_users.py`)
9. Export: a tour can be serialized to a JS registry file, stored as an `ir.attachment` linked to the tour, and returned as a download URL action. (`models/tour.py`)
10. There is no workflow state machine. The only lifecycle is the per-user consumed/not-consumed status and the enabled flag. No explicit validation errors are raised besides the name uniqueness constraint.

### 2.4 Security
11. ACLs: `base.group_system` has full CRUD on tours and steps. `base.group_user` has read-only access to both. (`security/ir.model.access.csv`)
12. No record rules are declared. The sudo sites are the consumed-user link write, the user flag toggle, and a demo-module count query. (`models/tour.py`, `models/res_users.py`)
13. The tour/step JSON methods are public model methods whose visibility depends on the read ACL above. The `run` step field is a free-text instruction that the client executes. RISK: authoring is limited to the system group, which A1 should confirm. (`models/tour.py`, `security/ir.model.access.csv`)

### 2.5 UI surfaces (names only)
14. Views: `tour_form`, `tour_list`, `tour_search`. Window action: `tour_action`. Menu: `menu_tour_action` under `base.next_id_2` (a technical parent from `base`; no menu-level groups attribute was observed). Server action: `tour_export_js_action` bound to the tour form. (`views/tour_views.xml`)
15. The module has no HTTP controllers (only models are imported). Client access goes through the generic RPC layer of `web`.

### 2.6 Jobs / config / toggles / integrations
16. The module declares no crons and reads no config parameters. The feature toggle is the per-user `tour_enabled` flag. Its default depends on whether demo data is installed and on the test-mode flag. (`models/res_users.py`)
17. The session info payload is extended with `tour_enabled` and `current_tour`, which pushes onboarding state to the client at bootstrap. (`models/ir_http.py`)

## 3. Cross-module Edges
- Hard dependency: `web`. This module extends `ir.http.session_info` from `web` (session-info extension point) and appends to the `web.assets_*` bundles.
- Uses the `base` models `res.users`, `ir.module.module` (demo count), `ir.attachment` (export), and the menu parent `base.next_id_2`.
- Reverse extension point: other modules can register tours through the client registry category (name `web_tour.tours`, seen in the export content). The server-side `web_tour.tour` records are used for custom or recorded tours.
- The export download URL points to the `/web/content` route in `web`.

## 4. Evidence Gaps / Contradictions
- G-1: `controllers/__init__.py` returned 404. `__init__.py` imports only `models`, so this is consistent with the module having no controllers package. It is recorded as an absence and not as a failure.
- G-2: The JS client (tour service, pointer, recorder, automatic/interactive runners) was not studied, so step execution semantics and client-side guards are unevidenced.
- G-3: The contents of the view XML beyond record ids, the menu and the binding were not examined in depth.
- G-4: Tests and static assets were not reviewed.
- No contradictions were observed.

## 5. Limitations
Static source only, at a single commit. No runtime or DB observation was made. Findings are neutral abstractions and are not design recommendations.
