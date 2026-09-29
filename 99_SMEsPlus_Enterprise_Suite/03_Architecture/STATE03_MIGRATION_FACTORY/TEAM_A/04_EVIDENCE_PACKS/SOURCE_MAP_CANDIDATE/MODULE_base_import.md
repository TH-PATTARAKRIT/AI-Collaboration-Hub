# Source Map (candidate) — `base_import`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_import` |
| Display name | Base import |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4af989c1e8d6dc8a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_import/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_import_export`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `base_import.mapping` (Base Import Mapping); `base_import.import` (Base Import)
- Objects extended from other modules (2): `base`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `base`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 45 of 45 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_import
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Server-side file import for any business model: user uploads a file, the system previews it, suggests a column-to-field mapping, does a trial run, then a real run (base_import/models/base_import.py:130-176; base_import/__manifest__.py:3-23).
- Stated design goals: keep the import logic on the server so it can be automated without the web client, allow other front-ends, and let administrators omit the feature by not installing the module (base_import/__manifest__.py:7-22).
- Conditional: depends on web only, installs automatically, category Hidden/Tools (base_import/__manifest__.py:24-28).
- Accepted formats: CSV, ODS, XLS, XLSX; anything else is rejected with an "unsupported format" message (base_import/models/base_import.py:45-50,421). Excel reading needs an Excel-reader library on the host; a missing library yields a "requires module" message (base_import/models/base_import.py:405-420).
- UI entry: an "Import records" item appears in the list/kanban gear menu on regular window actions, hidden on small screens, and hidden when the view disables import or create (base_import/static/src/import_records/import_records.js:39-48).
- Model-specific downloadable templates are supported through an overridable hook that returns none by default (base_import/models/base_import.py:85-93); sample CSVs ship in base_import/static/csv (skeleton listing).

## B. Business objects, relationships, lifecycle
- Import job (temporary record, kept up to 12 hours): target model name, uploaded file, file name, file type (base_import/models/base_import.py:177-189).
- Saved column mapping (persistent): target model, external column label, chosen field; used to pre-fill mappings on later imports from the same third-party system (base_import/models/base_import.py:96-113).
- Lifecycle: create job (client) -> upload file via web route that writes file into the job (base_import/controllers/main.py:13-24; base_import/static/src/import_model.js:237-243) -> preview/mapping suggestion -> optional dry run -> real run in batches -> mapping saved on success (base_import/models/base_import.py:1004-1125,1435-1539).
- Importable fields exclude system columns and read-only fields; relational fields expose external-ID and database-ID sub-choices; one-to-many fields recurse up to 3 levels; dynamic property fields are included when the user can read their definitions (base_import/models/base_import.py:34,270-350,285-288).

## C. Validations, automation, security, credentials
- Preview: empty/corrupt file rejected; row length must match header length; at least one column must be mapped (base_import/models/base_import.py:1023-1024,1146-1147,1158-1165).
- Encoding auto-detected unless chosen; decoding failure gives a specific message; delimiter guessed among comma, semicolon, tab, space, pipe, unit-separator; text delimiter must be one character (base_import/models/base_import.py:545-588).
- Mapping suggestion order: previously saved mapping, exact match on technical name/label/translated label, then fuzzy match under a distance threshold of 0.2 (base_import/models/base_import.py:139-152,184).
- Value parsing: dates/datetimes by chosen or detected format with line-specific error text; floats tolerate currency symbols and separators; error cells in spreadsheets are rejected (base_import/models/base_import.py:1210-1260,1315-1345,456-463,492-495).
- Duplicate mapping of several columns onto one text/char/html/many2many field concatenates values (space, newline, line-break tag, comma) (base_import/models/base_import.py:52-57,1565-1650).
- Fallback values for boolean/selection mismatches: user can choose a replacement or skip (base_import/models/base_import.py:1652-1719).
- Image/binary fields: value may be a URL or base64 data; invalid data is rejected. URL fetch is limited to users passing a hook that by default allows only the administrator group (base_import/models/base_import.py:116-127,1289-1311). URL downloads honor configured URL pattern, maximum size and timeout, and verify the file is a usable image (base_import/models/base_import.py:1357-1383). Business note: URL import can consume worker capacity (docstring: base_import/models/base_import.py:120-121).
- Dry run vs real run: both run in a database savepoint; dry run rolls back and resets caches; a real run rolls back on blocking errors and returns structured messages (base_import/models/base_import.py:1462-1501). Loading is delegated to the target model's standard load routine, so target-model constraints apply (base_import/models/base_import.py:1488).
- Import context flags set for the loader: import file flag, name-create-enabled fields, set-empty fields, skipped records, row limit (base_import/models/base_import.py:1480-1487).
- Security: all internal users (base.group_user) may read/write/create mapping and import jobs; import-job delete not granted; a rule limits import jobs to the record creator (base_import/security/ir.model.access.csv:2-3; base_import/security/base_import_security.xml:3-7). Whether a user may create records in the target model is enforced by that model's own access rights: UNKNOWN — EVIDENCE INSUFFICIENT within this module.
- Company scoping: none defined for mappings (mappings are shared across companies; base_import/models/base_import.py:108-113).
- Upload route uses the caller's session; job id supplied by client and access limited by the creator-only rule (base_import/controllers/main.py:13-24; base_import/security/base_import_security.xml:6).

## D. Handoffs to other modules
- Record creation/update, required-field, unique-key and business-rule enforcement: the target model's owning module through the generic load routine (base_import/models/base_import.py:1488).
- Import-menu display: web client search/cog menu framework (base_import/static/src/import_records/import_records.js:1-8).
- Model-specific import templates: any module overriding the template hook (base_import/models/base_import.py:85-93). Which modules do so: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration/defaults that change outcomes
- Client defaults: batch size 2000 rows; tracking (change logging) disabled during import (base_import/static/src/import_model.js:111-113,125-128). Preview shows the first 10 lines (base_import/models/base_import.py:1004).
- Server configuration for URL import: URL pattern, max bytes, timeout (base_import/models/base_import.py:1357-1361).
- Upload size limit taken from session setting (base_import/static/src/import_model.js:130).
- User's language date format is tried first for date detection (base_import/models/base_import.py:700-706).
- Debug-feature group users additionally see database-ID choice on one-to-many fields (base_import/models/base_import.py:344-347).
- Batch resume: interrupted/partial import returns a next-row position so the user can resume (base_import/models/base_import.py:1532-1535; base_import/static/src/import_model.js:294-300).

## F. Effective extension path
- Override the remote-URL permission hook on Users to widen/narrow who may import images by URL (base_import/models/base_import.py:119-127).
- Override the template hook on any model to publish templates (base_import/models/base_import.py:85-93).
- Additional file readers can be added by defining a reader named after the file type (base_import/models/base_import.py:402-404).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: automated test coverage on the server side (no Python tests directory in this module; only JS tests at base_import/static/tests).
- UNKNOWN — EVIDENCE INSUFFICIENT: exact error text and behavior of the target model's load routine (outside module).
- UNKNOWN — EVIDENCE INSUFFICIENT: how the import job's temporary records are purged beyond the 12-hour setting.

