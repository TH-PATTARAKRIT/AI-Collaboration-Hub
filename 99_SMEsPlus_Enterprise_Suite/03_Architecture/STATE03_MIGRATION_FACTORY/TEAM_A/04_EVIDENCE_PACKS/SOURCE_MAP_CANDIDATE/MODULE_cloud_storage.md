# Source Map (candidate) — `cloud_storage`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `cloud_storage` |
| Display name | Cloud Storage |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `59937d6e43db233c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/cloud_storage/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `mail`
- Direct dependents in 300-module list (3): `cloud_storage_azure`, `cloud_storage_google`, `cloud_storage_migration`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Technical Settings / Store chatter attachments in the cloud
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `ir.http`, `ir.attachment`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `ir.attachment`, `res.config.settings`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 35 of 35 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — cloud_storage
Source revision: 19.0.post20260921 | Module: "Cloud Storage" v1.0, category Technical Settings, LGPL-3 (cloud_storage/__manifest__.py:4-7,22). Basis: static reading; one unit test read (TEST). This module is a framework only; the actual provider logic lives in sibling modules.

## A. Capabilities and optionality
- A1. Lets large chatter attachments be kept in an external cloud bucket instead of the Odoo database/filestore: the browser uploads directly to the cloud using a time-limited link the server issues, and downloads are redirected to a time-limited cloud link. cloud_storage/__manifest__.py:5; cloud_storage/controllers/attachment.py:28-32; cloud_storage/models/ir_attachment.py:24-33
- A2. Optionality: NOT automatic. No auto_install; depends on base_setup and mail. It does nothing useful alone: the provider choice list is empty and the storage-specific steps are declared but unimplemented (raise "not implemented"). cloud_storage/__manifest__.py:8; cloud_storage/models/res_config_settings.py:22-26; cloud_storage/models/ir_attachment.py:78-85,93-105,107-123
- A3. Conditional on a provider being selected in Settings (system parameter cloud_storage_provider); without it, uploads flagged as cloud are refused. cloud_storage/models/ir_attachment.py:39-40; cloud_storage/controllers/attachment.py:14-17
- A4. Settings section "Cloud Storage" placed after Integrations: provider choice and minimum file size in MB. cloud_storage/views/settings.xml:9-18

## B. Objects and lifecycle
- B1. No new model. Adds a new attachment storage type "Cloud Storage" to attachments; if the type is removed the attachment falls back to a plain URL type. cloud_storage/models/ir_attachment.py:19-22
- B2. Upload lifecycle: client requests an upload through the chatter upload route -> server creates the attachment normally -> attachment is flipped to cloud type with its content cleared and a cloud blob address stored (mimetype preserved) -> server returns upload instructions -> browser sends the file to the cloud. cloud_storage/controllers/attachment.py:19-32; cloud_storage/models/ir_attachment.py:36-48; (TEST) cloud_storage/tests/test_ir_attachment.py:8-27
- B3. Download lifecycle: request for a cloud attachment becomes a redirect to a signed link, cached until 10 seconds before expiry; only when a full provider configuration exists. cloud_storage/models/ir_attachment.py:24-33
- B4. Migration back to local: fetch the file from the cloud (10-second timeout), then store as ordinary binary and drop the URL. cloud_storage/models/ir_attachment.py:50-67
- B5. Blob naming: "<attachment id>/<random uuid>/<file name>". cloud_storage/models/ir_attachment.py:69-75
- B6. Default validity of upload and download links: 300 seconds each; download validity can be overridden by context. cloud_storage/models/ir_attachment.py:16-17,87-91

## C. Validations, security, external service
- C1. Switching provider is guarded: existing cloud-stored attachments are not fetchable after a change; provider modules are expected to block switching/uninstall when attachments exist (hook is empty here). cloud_storage/models/res_config_settings.py:10-18,55-60,73-74
- C2. Saving Settings with a provider chosen but no complete configuration is rejected ("configure before enabling"). cloud_storage/models/res_config_settings.py:77-79
- C3. Models excluded from cloud storage (their code reads attachment content): those inheriting the main-attachment mixin, and documents-related models if that app exists; the list is sent to the browser. cloud_storage/models/ir_attachment.py:125-132; cloud_storage/models/ir_http.py:10-16
- C4. Threshold: the client uses cloud upload only for files above the minimum size; default 20 MB; stored as a system parameter. cloud_storage/models/res_config_settings.py:6,28-37,66,75; cloud_storage/models/ir_http.py:13-15. It is described as a soft limit for the web client. cloud_storage/models/res_config_settings.py:17-18
- C5. Security and company scoping are inherited: this module adds no access file, groups or rules (no security folder). Upload rights follow the mail attachment route it extends. UNKNOWN — EVIDENCE INSUFFICIENT for who may request cloud upload beyond the base route rules.
- C6. External-service implications: needs a cloud account and credentials configured in a provider module (not here); public clients receive direct cloud links. Credentials location: UNKNOWN — EVIDENCE INSUFFICIENT for this module (see provider modules).

## D. Handoffs
- D1. Chatter attachment route and main-attachment registration: mail. cloud_storage/controllers/attachment.py:5-9; mail/controllers/attachment.py:83; mail/models/ir_attachment.py:45-49
- D2. Settings screen host: base_setup. cloud_storage/views/settings.xml:7
- D3. Providers and migration (each depends on cloud_storage): cloud_storage_azure, cloud_storage_google, cloud_storage_migration. cloud_storage_azure/__manifest__.py:8; cloud_storage_google/__manifest__.py:8; cloud_storage_migration/__manifest__.py:8

## E. Configuration that changes outcomes
- E1. cloud_storage_provider (empty = feature off); cloud_storage_min_file_size (bytes, default 20,000,000). cloud_storage/models/res_config_settings.py:25,35-36
- E2. Link lifetimes (E: 300 s defaults). cloud_storage/models/ir_attachment.py:16-17

## F. Extension path
- cloud_storage_azure, cloud_storage_google (provider implementations), cloud_storage_migration (bulk migration, cron and report model present).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: provider-specific behaviour (not read; belongs to sibling modules).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end upload logic (static JS not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether portal/guest users can trigger cloud uploads (decorator adds guest context, cloud_storage/controllers/attachment.py:11; rights not traced).

