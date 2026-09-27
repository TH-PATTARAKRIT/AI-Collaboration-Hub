# G01 PLATFORM_BASE — Module `html_builder` — Lane A Pass-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T1 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `html_builder` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0, commit `8d05257d83f9128953f580a066db67c48fcdb96f` (raw.githubusercontent fetch) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (server-side Python scope per brief; client-side JS behaviour intentionally not analysed — see §5) |
| Handoff target | RED TEAM A1 only. No Lane B material consulted. No GMVQ QID answered (W1-B06 question batch on Question-Gate HOLD; Lane A not blocked). |

## 1. Evidence Pointer Table

| Path (addons/html_builder/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | f55fb07044ff6db8e5aee583226f781f3575b498 | Identity, deps, asset bundle definitions |
| `__init__.py` | e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 | Package init — empty file (0 bytes): imports nothing |
| `tests/__init__.py` | 171a01d1dcfcea9b4b4774f1ba1b86d2d303fec7 | Test import list (1 module) |
| `tests/test_html_builder_assets_bundle.py` | 7792507bfa3f17176bed0e978a7b85a5673ae8c0 | Post-install bundle-composition test |
| `i18n/html_builder.pot` | dd82b4946129d8d1368c4c4ae89b22781912d2a9 | Translatable-string inventory (528 msgids; source refs) |
| `static/src/builder.js` | 8ff24b4cfbd9ad95f500d0f2bcda16b00c943e61 | Existence probe of main client component (surface count only; not analysed) |

Blob count: 6. Absences (404; consistent with empty `__init__.py`): `models/__init__.py`, `controllers/__init__.py`, `controllers/main.py`, `views/templates.xml`.

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. WHAT: a generic, reusable client-side HTML page/content builder. Manifest description names its intended consumers as the website builder and the mass-mailing editor. [`__manifest__.py`]
2. Dependencies: `base`, `html_editor`, `mail`. A manifest comment states the `mail` dependency exists only to access a JS mail-model helper (i.e., a technical, not functional, coupling). [`__manifest__.py`]
3. Category "Uncategorized", version 0.1, LGPL-3; no `installable`/`application`/`auto_install` keys set (framework defaults apply). [`__manifest__.py`]
4. No `data` key: the module loads no XML/CSV data, views, menus, actions, or ACL. [`__manifest__.py`]

### 2.2 Data (models, fields, constraints)
5. No server-side models, fields, or DB constraints: `__init__.py` is empty and no `models` package exists at the anchor. [`__init__.py`; absences]

### 2.3 Business rules / states / exceptions
6. No server-side business rules, states, or exceptions. All builder behaviour is client-side (out of this pass's scope by brief). [`__init__.py`; `__manifest__.py`]
7. One server-side guard exists only as a test: the lazily loaded builder bundle must not contain edit-mode-only SCSS (those are routed to the in-iframe bundle instead). WHY: separate styling of editor chrome vs. edited content. RISK: mis-globbing would leak edit styles into the builder shell — guarded by test only, not runtime. [`tests/test_html_builder_assets_bundle.py`; `__manifest__.py` remove directives]

### 2.4 Security
8. No groups, ACL, record rules, or elevated-access calls in this module (no Python code, no security files). Access control for any persistence triggered through the builder must therefore live in consumer/dependency modules (e.g., `html_editor`, website, mass mailing) — not verified here. [absences]

### 2.5 UI surfaces
9. Routes: none (no controllers). [absences]
10. Asset bundles: 7 bundle entries in manifest — 3 bundles newly defined by this module (the lazily loaded builder bundle, the in-builder-iframe bundle, the add-snippet dialog iframe bundle) and 4 contributions to existing web bundles (primary variables, frontend background styling, web dark-mode, unit tests). Builder bundle is documented as lazy-loaded when the editor is ready. [`__manifest__.py`]
11. Surface count (lower bound, from .pot source references): 79 distinct `static/src` files carrying translatable strings — 32 JS, 47 XML templates — grouped under core (incl. anchor, building blocks), plugins (incl. background, background options, font, image, shape), sidebar, snippets, utils. 528 translatable message IDs. No Python source refs in .pot. [`i18n/html_builder.pot`]
12. Frontend footprint: a background SCSS is injected into the public frontend bundle, so a styling surface exists on public pages even outside edit mode. [`__manifest__.py`]

### 2.6 Jobs / config
13. No cron, config parameters, settings, or seed data. [`__manifest__.py`; absences]

## 3. Cross-module edges
- Outbound: `html_editor` (editor core; manifest pulls its SCSS and ChatGPT/link plugin styles into builder bundles), `web` (bootstrap variables, fonts, helper bundles, frontend helpers), `mail` (JS helper only, per manifest comment), `base`. [`__manifest__.py`]
- Inbound (declared intent only): website builder and mass-mailing editor. Not verified from those modules in this pass.
- Test infrastructure: relies on the framework QWeb asset-bundle resolver. [`tests/test_html_builder_assets_bundle.py`]

## 4. Evidence gaps / contradictions
- G-HB-1: JS/XML client behaviour (plugins, save paths, any RPC calls it issues to other modules' endpoints) not analysed — excluded by brief ("server-side Python only"). Any persistence/route used by the builder belongs to other modules and is unverified.
- G-HB-2: full static file inventory unknown (no listing API); 79 is a lower bound from .pot references only.
- G-HB-3: manifest description claims consumers (website, mass mailing); inbound dependency not confirmed from consumer manifests in this pass.
- No contradictions found.

## 5. Limitations
Static source only; presence ≠ runtime reachability; no runtime proof, no Formal Coverage claim. Server-side scope: module has zero executable Python outside one test, so card sections 2.2–2.4 are documented absences, not gaps. Clean-room: neutral WHAT/WHY/RISK only; identifiers are pointers, not design recommendations.
