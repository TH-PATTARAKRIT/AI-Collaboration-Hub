# G01 PLATFORM_BASE — `web_hierarchy` — Lane A Pass-1 Source Evidence

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T2 (refill) |
| Group | G01 PLATFORM_BASE |
| Module | `web_hierarchy` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/web_hierarchy/`) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Question bank | None module-specific yet; no QIDs answered (evidence only) |

## 1. Evidence Pointer Table

| Path (under `addons/web_hierarchy/`) | Git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | `4415a3857877d3c7bad740228d632aa1c78bb067` | Identity, deps, asset bundles |
| `__init__.py` | `d6210b1285d37ef0ef813097b4de4d889ad7012e` | Imports `models` only |
| `models/__init__.py` | `89107c88c34ba277c9f06b381359038ecbe092cf` | Imports 3 model files |
| `models/ir_actions.py` | `e95d2c87dd7989c17e11de87aa72d30acd3c4c4d` | Adds view mode to window-action view lines |
| `models/ir_ui_view.py` | `ce1d68e9a6948c85da5df8244bded7c5f6106550` | Registers view type + arch validation |
| `models/models.py` | `88136e7d2b2bd4545ef6c63e2d4d3ef8c56eeaca` | Generic server-side hierarchy read helper on abstract base |

Probed absences (404, not imported/listed — absence, not gap): `controllers/__init__.py`, `security/ir.model.access.csv`, `tests/__init__.py` (no Python tests).

## 2. Findings by Card Section

### 2.1 Manifest / deps / purpose
1. WHAT: Hidden-category technical module providing a new "hierarchy" (org-chart-style) view type. Depends only on `web`. No `data` list, no `auto_install` key, LGPL-3. (`__manifest__.py`)
2. WHAT: Assets load into the lazy backend bundle plus a separate dark-theme variables bundle and unit-test bundle. (`__manifest__.py`)

### 2.2 Data (models, fields, constraints)
3. WHAT: No new stored models or tables. Three inherit-only extensions: (a) the window-action view-line model gains a `hierarchy` view-mode option with cascade-on-uninstall semantics; (b) the UI view model gains a `hierarchy` view type; (c) the abstract base of all models gains a read helper `hierarchy_read`. (`models/ir_actions.py`, `models/ir_ui_view.py`, `models/models.py`)
4. WHY/RISK: Cascade-on-uninstall means action view lines of this mode are removed if the module is removed — configuration data loss on uninstall is by design. (`models/ir_actions.py`)
5. WHAT: No SQL constraints or Python `@constrains` defined.

### 2.3 Business rules / exceptions
6. WHAT (view validation): Root-node attributes are restricted to a fixed allow-list (styling/class, title, create/edit/delete toggles, `parent_field`, `child_field`, icon, draggable, default order). Unknown attributes raise a view error. Children of the root may only be field nodes or a single templates node; a second templates node or any other tag raises a view error. Validation is skipped when the node is flagged non-validating. (`models/ir_ui_view.py` `_validate_tag_hierarchy`)
7. WHAT: The hierarchy type is treated as a QWeb-based view type for arch processing, and advertises a default icon in view-info metadata. (`models/ir_ui_view.py`)
8. WHAT (parent/child requirement): Server-side validation does **not** make `parent_field` mandatory nor check that it names an existing many2one; it is only allowed. Any enforcement of presence/type lives outside Python (JS) — not verified in this pass. (`models/ir_ui_view.py`)
9. WHAT (read helper): `hierarchy_read(domain, specification, parent_field, child_field?, order?)`:
   - Forces the parent field (with its display name) into the read specification if absent.
   - Searches with the given domain/order; empty -> empty list.
   - Single-match mode: also pulls that record's parent (if any) plus the parent's other children or the record's own direct children (excluding itself) — i.e. a one-level "focus" neighbourhood.
   - Multi-match mode: returns exactly the matched set.
   - When no `child_field` is supplied, computes per-record child-id lists via a grouped read on the parent field and attaches them under a synthetic key; when `child_field` is supplied, child ids are expected from the caller's specification instead.
   (`models/models.py`)
10. RISK (cycles): No explicit cycle detection, depth limit, or recursion in the server helper — it only expands one level, so it cannot loop server-side; cycle integrity depends on the target model's own parent constraints (outside this module). Client-side traversal behaviour on cyclic data not assessed. (`models/models.py`)
11. RISK: Helper is defined on the abstract base, so it exists on every model; the `parent_field` argument is caller-supplied and not validated against the model's fields in this helper (an invalid name would error in the ORM layers). (`models/models.py`)

### 2.4 Security
12. WHAT: No groups, ACL files, record rules, or `sudo()` in module Python. The helper runs as the calling user; search, grouped read and web read all go through standard ORM access checks. (`models/models.py`; absence of `security/`)
13. RISK/UNKNOWN: Reachability of `hierarchy_read` from the client is via the generic model-method RPC dispatch owned by `web`/core — not declared here; source presence != runtime reachability.

### 2.5 UI surfaces
14. WHAT: No HTTP routes (no controllers package). UI surface is entirely JS/SCSS under `static/src/**` (lazy backend) plus `static/tests/**`; file counts not enumerable in this pass (see gaps).

### 2.6 Jobs / config
15. WHAT: No cron, no config parameters, no settings fields, no data files.

## 3. Cross-module Edges
- `web` (declared dependency; provides asset bundles and generic RPC dispatch).
- Core `ir.actions.act_window.view`, `ir.ui.view`, abstract `base` (inherit targets).
- Downstream consumers (e.g. HR org chart style views) likely declare hierarchy views; not enumerated here (outside module scope).

## 4. Evidence Gaps / Contradictions
- GAP-1: `static/src/**` and `static/tests/**` file lists not enumerable (directory listing API blocked; manifest uses globs). JS surface count unknown.
- GAP-2: Client-side enforcement of `parent_field` presence/type and cycle handling in JS not examined (out of Python scope).
- No contradictions observed.

## 5. Limitations
- Static source only at the anchor commit; no runtime proof, no Formal Coverage, no percentages.
- Clean-room: neutral WHAT/WHY/RISK abstractions only; identifiers are pointers, not design recommendations.
