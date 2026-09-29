# Source Map (candidate) — `base_import_module`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_import_module` |
| Display name | Base import module |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d822629a1d8b83c1` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_import_module/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 1, views 5, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `base.import.module` (Import Module)
- Objects extended from other modules (4): `base.module.uninstall`, `ir.http`, `ir.ui.view`, `ir.module.module`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `base.module.uninstall`, `ir.http`, `ir.ui.view`, `ir.module.module`

## 6. Actions / states / validation / automation / security
- State fields found: `base.import.module` → ['init', 'done']
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 53 of 53 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_import_module
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Lets an authorized administrator upload a ZIP containing a "data module" (data XML/CSV/SQL files, static assets, translation files, no Python code) and register it as an installed app (base_import_module/__manifest__.py:5-11; base_import_module/models/ir_module.py:104-322,324-390).
- Also lets administrators browse and install "industry" data modules from the vendor's public app site (apps.odoo.com), including dependency and demo-data guidance (base_import_module/models/ir_module.py:32,409-419,532-586).
- Conditional: depends only on web; installs automatically; category Hidden/Tools (base_import_module/__manifest__.py:12-15).
- Menu "Import Module" is visible only to users in the technical-features (debug) group under the Apps management menu (base_import_module/views/base_import_module_view.xml:39-45). Upload wizard has "Force init" (debug group only) and "Load demo data" options (base_import_module/views/base_import_module_view.xml:12-14).
- Additional upload route for scripted use: POST with login and password plus the file (base_import_module/controllers/main.py:10-24).

## B. Business objects, relationships, lifecycle
- Import wizard (temporary): module ZIP file, status (init/done), messages, force flag, demo flag, dependency text (base_import_module/models/base_import_module.py:7-17).
- Extends the installed-module registry record with: "imported" flag and module type (official apps or industries; default official) (base_import_module/models/ir_module.py:39-43).
- Lifecycle: upload -> validate ZIP/manifests -> order modules by declared dependencies -> per module: register as installed (imported=true) -> load data files -> store static files as public attachments -> store translation files as attachments -> create asset records from manifest -> reload translations -> update module metadata (base_import_module/models/ir_module.py:145-316,379-384).
- Re-import of a module already known: update mode by default, "init" mode when force is set (base_import_module/models/ir_module.py:145-148). New module: init mode (base_import_module/models/ir_module.py:149-152). (TEST) import then update behavior is covered (base_import_module/tests/test_import_module.py:340).
- Uninstall: imported modules are deleted from the registry entirely because they cannot be reinstalled; the uninstall confirmation lists imported modules (base_import_module/models/ir_module.py:392-407; base_import_module/wizard/base_module_uninstall.py:9-10). (TEST) after uninstall the attachment, asset and their external ids are gone (base_import_module/tests/test_import_module.py:286-338).
- Imported modules are excluded from normal module loading and cannot be upgraded (state reverted to installed) (base_import_module/models/ir_module.py:50-52,526-530; base_import_module/views/ir_module_views.xml:19-21,63-65).

## C. Validations, automation, security, credentials
- Access: import wizard model granted to system administrators only (read/write/create, no delete) (base_import_module/security/ir.model.access.csv:2). Import routine itself refuses non-administrators (base_import_module/models/ir_module.py:325-327); the industry install button also denies non-administrators (base_import_module/models/ir_module.py:532-534).
- Scripted upload route: no platform auth (auth none), CSRF off, session not saved; it authenticates the supplied username/password, and requires an administrator; MFA-pending logins are rejected; any failure returns HTTP 500 with the message (base_import_module/controllers/main.py:10-24). Credential implication: administrator password is sent in a form field by the caller.
- ZIP checks: must be a ZIP; no member larger than 100 MB; each top-level folder must contain a manifest; unknown dependencies abort with a list (base_import_module/models/ir_module.py:33,330-337,362-368,133-139). (TEST) invalid manifest raises a user error (base_import_module/tests/test_import_module.py:144-154).
- Only manifest-declared data files with extensions XML/CSV/SQL are loaded; others skipped with a log; only useful files (data, static, translations) are extracted (base_import_module/models/ir_module.py:163-167,353-377). (TEST) data not in manifest is ignored; unexpected extension skipped (base_import_module/tests/test_import_module.py:199-236); extraction limited to useful files (base_import_module/tests/test_import_module.py:237).
- Asset paths with wildcards are rejected (base_import_module/models/ir_module.py:265-268). (TEST) rejected (base_import_module/tests/test_import_module.py:156-170).
- Studio-created customizations require the Studio app to be installed (base_import_module/models/ir_module.py:142-143,726-755).
- Missing dependencies that exist in the system are installed automatically before import (base_import_module/models/ir_module.py:140-141). (TEST) modules with dependencies (base_import_module/tests/test_import_module.py:408-450).
- Privilege note: import runs elevated (base_import_module/models/ir_module.py:384) and loaded data files can create or modify any record; static files become public attachments (base_import_module/models/ir_module.py:205-207).
- Imported-module views are validated as custom views for their models (base_import_module/models/ir_ui_view.py:11-29).
- Errors are wrapped with full trace text shown to the administrator (base_import_module/models/ir_module.py:385-389).
- External service: outbound calls to the vendor app site for industry lists, category list and module download, 5-second timeout, no credentials sent; failures give user-facing messages (base_import_module/models/ir_module.py:497-524,536-563). Company scoping: none.

## D. Handoffs to other modules
- Module registry, dependency handling, install/uninstall buttons, apps list: base module (extended at base_import_module/models/ir_module.py:36-37; views inherit base at base_import_module/views/ir_module_views.xml:7,37,51,71).
- Views, assets, attachments, translations tables: base (ir.ui.view, ir.asset, ir.attachment) (base_import_module/models/ir_module.py:208-212,293).
- Website-specific handling: the website module (context reset only) (base_import_module/models/ir_module.py:105-111). Studio: web_studio app (not in Community tree) (base_import_module/models/ir_module.py:142). Knowledge welcome article: knowledge app if present (base_import_module/models/ir_module.py:307-313).
- Web client translations for imported modules are served from stored attachments (base_import_module/models/ir_http.py:13-22).
- Lines-of-code accounting exclusion for imported modules: cloc tooling (TEST) (base_import_module/tests/test_cloc.py:36-288).

## E. Configuration/defaults that change outcomes
- Force init (debug only) and Load demo data flags; demo data is loaded only when requested (base_import_module/models/ir_module.py:130-131,159-161; base_import_module/views/base_import_module_view.xml:13-14). The dependency note warns not to load demo in production (base_import_module/models/ir_module.py:582-585).
- Industry-mode context flag marks module type as industries (base_import_module/models/ir_module.py:128-129,558).
- Vendor app URL and major version determine what is offered (base_import_module/models/ir_module.py:32,449,515).

## F. Effective extension path
- Modules overriding the uninstall wizard display list or the translation-serving hook (base_import_module/wizard/base_module_uninstall.py:9; base_import_module/models/ir_http.py:13). Bridge modules (website, knowledge) are referenced only by presence checks (base_import_module/models/ir_module.py:205,307).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: exact list of records that data files in an arbitrary ZIP may touch (depends on uploaded content).
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side list-view behavior for the industries browser (JS in static/src not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: rate limiting or lockout for the password-based upload route.

