# Source Map (candidate) — `transifex`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `transifex` |
| Display name | Transifex integration |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `860e8c215cc15c8a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/transifex/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `web`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Add a link to edit a translation in Transifex
- Inventory of user-facing artifacts (counts): menu items 1, views 2, window actions 0, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `transifex.code.translation` (Code Translation); `transifex.translation` (Transifex Translation)
- Objects extended from other modules (1): `base`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `base`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Transifex: Reload code translations every ? ?
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 30 of 30 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: transifex
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Adds "contribute a translation" links pointing to the vendor's public Transifex translation project, for both record-level (database-stored) translations and program-text ("code") translations (transifex/__manifest__.py:7,13-14; transifex/models/models.py:10-48; transifex/models/transifex_code_translation.py:19-20).
- Optional, not auto-installing; depends on base and web; category Hidden/Tools (transifex/__manifest__.py:8,35).
- Limited scope by design: only standard modules published in the vendor project are linked; custom modules are not, and the target language must be active on the Transifex project (transifex/__manifest__.py:16-21).
- Adds a "Transifex Code Translations" screen under the translation menu, for system administrators (transifex/views/code_translation_views.xml:38-45).

## B. Business objects, relationships, lifecycle
- Code Translation cache (persistent, no audit columns): source text, translation value, module, language, computed Transifex link (transifex/models/transifex_code_translation.py:10-20).
- Loading: cache is filled from installed modules' program-text translations for each installed non-English language; already-loaded (module, language) pairs are skipped; a table lock prevents concurrent loads (returns false if locked) (transifex/models/transifex_code_translation.py:29-57).
- Opening the screen triggers a load first (transifex/models/transifex_code_translation.py:59-66). A full reload deletes all rows and reloads (transifex/models/transifex_code_translation.py:68-71).
- Scheduled reload every 7 days by an automatic job (transifex/data/transifex_data.xml:9-16).
- Record-level links: for a record with an external id belonging to a module that was loaded in this session, each translation row gets its module and a Transifex link (transifex/models/models.py:36-48).
- Link building: needs the project URL parameter, installed languages with ISO codes, and a module-to-project map read from Transifex configuration files found beside addon paths; skips English, empty source, unknown language or unmapped module; link contains language, module and the first 50 characters of the source term (transifex/models/transifex_translation.py:17-44,46-85).

## C. Validations, automation, security, credentials
- Security: code translation model readable by system administrators only, no write/create/delete rights via access list; the screen action is restricted to the system administration group (transifex/security/ir.model.access.csv:2; transifex/views/code_translation_views.xml:41). Loading/reload writes are done with elevated rights (transifex/models/transifex_code_translation.py:52) and reload is a scheduled job (transifex/data/transifex_data.xml:9-16).
- Company scoping: none; translations are global.
- External-service implication: no outbound calls by the server; it only builds links that a person opens in a browser. Default project URL is https://app.transifex.com/odoo (transifex/data/transifex_data.xml:4-7). No credentials.
- If the project URL is emptied, no links are produced (transifex/models/transifex_translation.py:55-57).
- Record-level link enrichment is skipped for records without an external id or whose module is not among modules initialized in this run (transifex/models/models.py:37-43).

## D. Handoffs to other modules
- Translation infrastructure (record-level and program-text translation loading, languages): base (transifex/models/models.py:36; transifex/models/transifex_code_translation.py:7,50).
- Translation dialog UI: web client (transifex/static/src/views/fields/translation_dialog.xml, listed in transifex/__manifest__.py:30). Its behavior: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration/defaults that change outcomes
- System parameter "transifex.project_url" (preset; editable) (transifex/data/transifex_data.xml:4-7; transifex/models/transifex_translation.py:55).
- Weekly reload interval (transifex/data/transifex_data.xml:14-15).
- Presence of Transifex config files in the addon locations determines which modules get links (transifex/models/transifex_translation.py:29-44). In a deployment without those files the mapping is empty and no links appear (transifex/models/transifex_translation.py:66-67).

## F. Effective extension path
- Modules using the record translation query API inherit the enriched output automatically through the shared base hook (transifex/models/models.py:7-8,36). No other extension path identified.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: contents of the front-end list controller ("reload code translations" button).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether Transifex configuration files exist in this distribution tree (not inspected; outside module scope).

