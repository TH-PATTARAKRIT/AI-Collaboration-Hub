# G01 PLATFORM_BASE — Module `onboarding` — Lane A Pass-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T1 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `onboarding` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0, commit `8d05257d83f9128953f580a066db67c48fcdb96f` (raw.githubusercontent fetch) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Handoff target | RED TEAM A1 only. No Lane B material consulted. No GMVQ QID answered (W1-B09 question batch on Question-Gate HOLD; Lane A not blocked). |

## 1. Evidence Pointer Table

| Path (addons/onboarding/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | eaa50cca7d2c90c315d667811d90e0da328fa884 | Identity, deps, data list, asset bundles |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Package import graph (models only) |
| `models/__init__.py` | 0e27595dad9c06d42f912e26af49eb37975f7368 | Model import list (4 files) |
| `models/onboarding_onboarding.py` | 9ed728d6cbc8b6f45b090222c8b6f54a3f2de0cb | Onboarding panel definition |
| `models/onboarding_onboarding_step.py` | 262186464fc868d9c5623f131e9832433cac3623 | Step definition + step validation entry points |
| `models/onboarding_progress.py` | 26dacc185dcd6533fc7212cf72021f5f06474595 | Panel progress tracker + state vocabulary |
| `models/onboarding_progress_step.py` | 311a0fef450dfadbe4f835e3fa4085b5813d1bce | Step progress tracker |
| `security/ir.model.access.csv` | f99bf429ceb2f8b24b2d247afc4e3c3cf5b351cc | ACL (12 rows) |
| `views/onboarding_views.xml` | 7688f73dda173608c7b8875d39f97cb7c8712044 | Backend list/form views, 2 window actions |
| `views/onboarding_menus.xml` | f036c70072cabf473f29c0dc1bb12e0a24dbe30f | 2 technical menus |
| `views/onboarding_templates.xml` | 58cd0c2d3307fa793e0feb3218e11c0b1eb009b5 | QWeb panel/container/step templates |
| `static/src/scss/onboarding.scss` | 767ca652b9ebc2d851745e1e0e1dce030add501a | Panel styling (surface only) |
| `static/src/scss/onboarding.variables.scss` | 7698cf85528be46f6b8a00f78e1e4f220188b98c | Style variables (surface only) |
| `static/src/scss/onboarding.variables.dark.scss` | 3736c78ab21c2ee89e11545de6295a59d9c0870f | Dark-mode variables (surface only) |
| `i18n/onboarding.pot` | e506e7cbfec073f6ed731b8a3e883f53b1c8ecfd | Translatable-string inventory (72 msgids) |
| `tests/__init__.py` | efa3fd7505243e1ade826239f04b39f82ed7e731 | Test import list |
| `tests/case.py` | 3fa1aa8f0d4c97bdd056407c9f2224101b5b2948 | Test assertion helpers (done-like state semantics) |
| `tests/common.py` | acd18d6ab1cbe233c2e1fad9b6752bce4d10ab7a | Test fixtures (onboardings/steps/companies) |
| `tests/test_onboarding.py` | 32649804ad896c28c186c369f7960d2a760bbe44 | Behavioural tests of state/company rules |
| `tests/test_onboarding_concurrency.py` | 801def35ee5074177f34f6372f95008b0ac71220 | Concurrent progress-creation uniqueness test |

Blob count: 20. Absences (404, not imported): `controllers/__init__.py`, `controllers/main.py`, `controllers/onboarding.py`, `data/` (no data file listed in manifest).

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. WHAT: a hidden-category "toolbox" providing generic, reusable setup-guidance panels and their completion tracking. Sole dependency: `web`. LGPL-3. [`__manifest__.py`]
2. WHY: other apps declare their own panels/steps and reuse this tracking engine; the module ships no panel content itself (no data file in manifest). [`__manifest__.py`]
3. Loads 4 data files: 3 view files + ACL. Backend asset bundle picks up the whole `static/src` tree; separate light/dark variable bundles. [`__manifest__.py`]

### 2.2 Data (models, fields, constraints)
4. Four persisted entities: panel definition, step definition, panel-progress tracker, step-progress tracker. [`models/__init__.py`]
5. Panel definition: translatable name, a one-word route key (required, globally unique — DB constraint), ordered many-to-many link to steps, completion message, name of a close-callback action, sequence. Computed (non-stored): per-company flag, current-context progress, current state, closed flag. [`onboarding_onboarding.py`]
6. Step definition: title/description/button/done texts (translatable), done icon, image + alt text, name of an "open" callback action, per-company flag (default ON), sequence; many-to-many back-link to panels (a step may be shared by several panels). Computed current step progress/state for the context company. [`onboarding_onboarding_step.py`]
7. Panel-progress tracker: stored computed state, closed flag, optional company (cascade delete), required panel link (cascade delete), many-to-many to step-progress records. Uniqueness: one tracker per (panel, company-or-none) via a functional unique index treating "no company" as a value. [`onboarding_progress.py`]
8. Step-progress tracker: state (default not_done), required step link (cascade), optional company (cascade), many-to-many back to panel trackers. Uniqueness: one per (step, company-or-none). [`onboarding_progress_step.py`]
9. Constraint: a step may not be linked to any panel unless its "open" callback name is set (validation error listing step titles). [`onboarding_onboarding_step.py`; confirmed by `test_onboarding.py`]

### 2.3 Business rules / states / exceptions
10. State vocabulary (shared by steps and panels): not_done, just_done, done; the rendering layer adds a fourth pseudo-state `closed` for panels. [`onboarding_progress.py`]
11. Step transition: validation moves only not_done → just_done; already-validated steps are ignored (idempotent, returns empty). Progress records are lazily created for the current context on validation. [`onboarding_progress_step.py`, `onboarding_onboarding_step.py`]
12. Validation by external reference: an entry point takes a step's external ID and reports one of three outcomes (not found / just done / was already done). Missing reference is a quiet outcome, not an error. [`onboarding_onboarding_step.py`]
13. just_done → done consolidation happens as a side effect of *reading* the panel state for rendering, so the "just done" celebration is shown once. WHY: one-shot UX feedback. RISK: a read path mutates state; concurrent/duplicate renders may consume the one-shot state. [`onboarding_progress.py` `_get_and_update_onboarding_state`; `test_onboarding.py`]
14. Panel completion rule: panel is done only when count of done-like step trackers equals count of the panel's steps; otherwise not_done. Panel reports just_done on the render in which the last step consolidates. [`onboarding_progress.py`]
15. Adding a step to a completed (even closed) panel resets it to not_done. [`onboarding_onboarding.py` write; `test_onboarding.py`]
16. Close / hide: close sets the tracker's closed flag; a toggle action flips it; a model-level entry point closes a panel by external ID and silently no-ops if missing. Closed state is per tracker (hence per company when per-company). [`onboarding_onboarding.py`, `onboarding_progress.py`; `test_onboarding.py` per-company test]
17. Company scoping: a panel becomes per-company once any linked step is per-company or any tracker has a company; this is sticky (not reverted when the per-company step is removed — explicit design note to avoid merging progress). Current progress is resolved as tracker with company = current company OR none. [`onboarding_onboarding.py`]
18. Changing a step's per-company flag deletes that step's existing progress, then panels needing it are rebuilt (global trackers deleted and recreated per-company). RISK: completion history is discarded on scope change. [`onboarding_onboarding_step.py` write; `onboarding_onboarding.py` refresh; `test_onboarding.py` to-company-change]
19. Shared steps: completing a step shared by two panels counts toward both. [`test_onboarding.py` shared-steps]
20. Concurrency: simultaneous first-time tracker creation → exactly one succeeds; the loser gets a DB uniqueness violation (not caught in model code). [`test_onboarding_concurrency.py`]
21. Company deletion cascades to trackers; the related test is explicitly skipped (other FK constraints may block company deletion). [`test_onboarding.py`]

### 2.4 Security
22. No groups defined; no record rules (no security XML). ACL: rows for "all" and `base.group_user` exist on all 4 models but grant no permission; only `base.group_system` has full CRUD. [`security/ir.model.access.csv`]
23. No explicit elevated-access calls in module model code. RISK/inference for A1: ordinary internal users hold no ACL on these models, so consumer modules' render/validate paths must run with elevated rights — to be verified in consumer modules (outside this module). [`models/*`, ACL]
24. No company record rule on trackers; company isolation is by compute/filter logic only (current company or none). [`onboarding_onboarding.py`, `onboarding_onboarding_step.py`]

### 2.5 UI surfaces
25. Routes: none declared in this module (no controllers package). [absence]
26. Backend: 2 window actions (panels, steps), 4 views (list+form each), 2 menus under a base-owned technical "User Interface" parent; list header "Toggle visibility" button. [`onboarding_views.xml`, `onboarding_menus.xml`]
27. QWeb templates: 3 (panel, container with hide-confirmation dialog and completion banner, step card). Step image served via generic image URL on the step model; buttons carry model/method callback names for client-side dispatch. [`onboarding_templates.xml`]
28. Static assets: 3 SCSS files confirmed; JS file count not determined (glob-included; no listing API). The .pot has no static-source string references (only 2 model-code refs + model field/term refs). [`__manifest__.py`, `i18n/onboarding.pot`]

### 2.6 Jobs / config
29. No cron, no config parameters, no settings view, no seeded data. [manifest data list]

## 3. Cross-module edges
- Depends on `web` (assets, backend). Menus parent in `base`; placeholder image and confetti image from `base` static. [`__manifest__.py`, `onboarding_menus.xml`, `onboarding_onboarding_step.py`, `onboarding_templates.xml`]
- Company link to `res.company` (cascade). [progress models]
- Tests import a helper from `mail` (test-time only; `mail` not a manifest dependency). [`test_onboarding.py`]
- Inbound: consumer apps supply panels, steps, open/close callback methods, and the render route — not visible in this module.

## 4. Evidence gaps / contradictions
- G-ONB-1 (contradiction/pointer): route-key field comment and a method docstring refer to an `/onboarding/<route_name>` route and an "onboarding controller", but this module has no controllers at the anchor. Route owner not located (likely a consumer/other module) — open for A1.
- G-ONB-2: onboarding JS file inventory and client-side behaviour (hide/close dispatch, reload-on-close) not enumerated.
- G-ONB-3: whether consumer render/validate paths elevate privileges (item 23) — outside module.

## 5. Limitations
Static source only; presence ≠ runtime reachability; no runtime proof, no Formal Coverage claim. Clean-room: neutral WHAT/WHY/RISK only; identifiers are pointers, not design recommendations.
