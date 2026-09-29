# Source Map (candidate) — `cloud_storage_google`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `cloud_storage_google` |
| Display name | Cloud Storage Google |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `03581866647985cc` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/cloud_storage_google/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `cloud_storage`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Technical Settings / Store chatter attachments in the Google cloud
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `ir.attachment`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.attachment`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 42 of 42 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — cloud_storage_google
Source revision: 19.0.post20260921 | Module: "Cloud Storage Google" (cloud_storage_google/__manifest__.py:4) | LGPL-3 (:25)
Basis: static reading of models, utils, settings view, neutralize script, uninstall hook, test titles.

## A. Capabilities and optionality
- A1. Adds Google Cloud Storage as a selectable provider for new chatter/web-client attachments. cloud_storage_google/__manifest__.py:5; cloud_storage_google/models/res_config_settings.py:25
- A2. Optional (no auto_install); depends on cloud_storage; requires the external Python library google-auth. cloud_storage_google/__manifest__.py:8,12-17
- A3. Conditional: overrides apply only when provider setting equals "google". cloud_storage_google/models/ir_attachment.py:58,64,80; cloud_storage_google/models/res_config_settings.py:57,100,109
- A4. Direct browser-to-bucket upload through a signed PUT link; reading through a signed GET link (redirect). cloud_storage_google/models/ir_attachment.py:63-88; cloud_storage/models/ir_attachment.py:24-34
- A5. Small backend style file only. cloud_storage_google/__manifest__.py:18-22; cloud_storage_google/static/src/scss/cloud_storage_google.scss:1
- A6. Ships an offline script for removing unused blobs (not part of the running application). cloud_storage_google/utils/cleanup_cloud_storage_google.py:1

## B. Objects and lifecycle
- B1. No new model; extends attachment and settings wizard (attachment type "cloud storage" is owned by cloud_storage). cloud_storage_google/models/ir_attachment.py:31-32; cloud_storage/models/ir_attachment.py:19-22
- B2. Blob address = bucket name + unique path (attachment id / random id / file name). cloud_storage_google/models/ir_attachment.py:44-46; cloud_storage/models/ir_attachment.py:69-75
- B3. Stored address must match the Google pattern (storage.googleapis.com/bucket/blob) else validation error. cloud_storage_google/models/ir_attachment.py:33-42
- B4. Lifecycle same as generic cloud attachment: flagged after creation, content cleared, browser uploads, later reads by signed link. cloud_storage/models/ir_attachment.py:36-48

## C. Validations, automation, security, external service
- C1. Credentials: a Google service-account key in JSON is uploaded as a file on the settings screen and stored as text in a system parameter together with the bucket name. cloud_storage_google/models/res_config_settings.py:27-40,49-53; cloud_storage_google/views/settings.xml:14-20
- C2. Configuration is treated as incomplete unless both bucket and key are present; base module then refuses to enable. cloud_storage_google/models/res_config_settings.py:98-106; cloud_storage/models/res_config_settings.py:77-79
- C3. On changed configuration a live self-test runs: upload empty blob, read it back, then the module writes CORS rules on the bucket (any origin, GET and PUT) using full-control scope; each failure raises a validation error. cloud_storage_google/models/res_config_settings.py:55-96. Consequence: the service account needs bucket-metadata write permission, and the bucket becomes readable/writable by signed links from any web origin.
- C4. Signed link lifetimes: 300 s for both upload and read by default. cloud_storage/models/ir_attachment.py:16-17,87-91; cloud_storage_google/models/ir_attachment.py:67,84
- C5. Parsed credential object is cached per database in memory and reloaded when the stored key text changes. cloud_storage_google/models/ir_attachment.py:15-28
- C6. Outbound calls use 5-second timeouts. cloud_storage_google/models/res_config_settings.py:68,74,94
- C7. Provider switch or module removal blocked while any attachment still has a Google address. cloud_storage_google/models/res_config_settings.py:108-122; cloud_storage_google/__init__.py:6-10; (TEST) cloud_storage_google/tests/test_cloud_storage_google.py:50-59
- C8. Uninstall removes bucket and key parameters; neutralization deletes the same two parameters. cloud_storage_google/__init__.py:11-14; cloud_storage_google/data/neutralize.sql:1-4; (TEST) cloud_storage_google/tests/test_cloud_storage_google.py:61-67
- C9. No security groups, record rules or company scoping defined in this module. cloud_storage_google/__manifest__.py:9-11
- C10. Observation: the failure message for the read-permission check builds its text from the upload response rather than the read response. cloud_storage_google/models/res_config_settings.py:76. Practical effect — UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Provider-neutral engine (settings block, min file size, session info, upload endpoint, unsupported models): cloud_storage. cloud_storage/models/ir_http.py:8-16; cloud_storage/controllers/attachment.py:9-32
- D2. Bulk move of existing local files: cloud_storage_migration. cloud_storage_migration/models/ir_attachment.py:24-44
- D3. Signed-link tests (TEST): cloud_storage_google/tests/test_cloud_storage_google.py:37; upload endpoint test (TEST): cloud_storage_google/tests/test_cloud_storage_google_attachment_controller.py:12

## E. Configuration
- E1. Provider = google; bucket name; service-account key file; minimum file size (default 20,000,000 bytes). cloud_storage_google/models/res_config_settings.py:27-40; cloud_storage/models/res_config_settings.py:6,28-37
- E2. Changing bucket while old blobs exist requires the service account to keep access to the old bucket (module instruction). cloud_storage_google/models/res_config_settings.py:18-22

## F. Extension path
- cloud_storage (base), cloud_storage_google, cloud_storage_azure, cloud_storage_migration.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which groups can view or edit the service-account key text on the settings screen; whether the key is masked.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether wildcard-origin CORS is acceptable for a given deployment (policy decision, not shown in source).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the offline clean-up script beyond its header (cloud_storage_google/utils/cleanup_cloud_storage_google.py not read in full).

