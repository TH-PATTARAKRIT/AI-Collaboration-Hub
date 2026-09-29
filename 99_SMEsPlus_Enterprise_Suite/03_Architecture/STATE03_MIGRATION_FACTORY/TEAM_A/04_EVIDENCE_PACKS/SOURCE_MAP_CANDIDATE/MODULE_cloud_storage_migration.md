# Source Map (candidate) — `cloud_storage_migration`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `cloud_storage_migration` |
| Display name | Cloud Storage Migration |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `42dcf7cc2824d9e4` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/cloud_storage_migration/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `cloud_storage`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Technical Settings / Migrate local attachments to cloud storage
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `cloud.storage.migration.report` (Cloud Storage Migration Report)
- Objects extended from other modules (2): `ir.attachment`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.attachment`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Migrate Local Attachment Binaries to Cloud Storage every 9999 months
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 35 of 35 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — cloud_storage_migration
Source revision: 19.0.post20260921 | Module: "Cloud Storage Migration" (cloud_storage_migration/__manifest__.py:4) | LGPL-3 (:17)
Basis: static reading of models, cron/seed data, access file, settings view; two setting tests by title.
## A. Capabilities and optionality
- A1. Moves existing locally stored attachment files to the configured cloud provider in the background, per selected business model. cloud_storage_migration/__manifest__.py:5; cloud_storage_migration/models/ir_attachment.py:24-44,46-186
- A2. Optional add-on (no auto_install); depends only on cloud_storage, and needs a provider module (cloud_storage_azure or cloud_storage_google) to be usable. cloud_storage_migration/__manifest__.py:8; cloud_storage_migration/models/ir_attachment.py:54-55
- A3. Not automatic: the cron is seeded with a next run about 9999 days ahead and a 9999-month interval; it is intended to be triggered manually from the settings screen ("Cron Job" button). cloud_storage_migration/data/ir_cron.xml:10-12; cloud_storage_migration/views/res_config_settings.xml:22-27
- A4. Provides a read-only report of stored binary attachments per business model (count, total and largest size, split into message attachments and all attachments) plus flags showing which models are scheduled. cloud_storage_migration/models/cloud_storage_migration_report.py:9-28,30-66,82-92
## B. Objects and lifecycle
- B1. New reporting model (database view, no stored rows): cloud.storage.migration.report. cloud_storage_migration/models/cloud_storage_migration_report.py:9-13. Counts only local binary attachments linked to a record, excluding field-bound ones. :56-60
- B2. Per-attachment lifecycle: local file -> address generated -> file streamed to provider using the provider's upload link -> record switched to cloud type and local content dropped. cloud_storage_migration/models/ir_attachment.py:24-44
- B3. Progress is a "last processed attachment id" cursor kept in a system parameter compared with a "highest attachment id at start" parameter, shown as a progress bar. cloud_storage_migration/models/cloud_storage_migration_report.py:94-98; cloud_storage_migration/data/data.xml:26-30
- B4. Selection of what to migrate: two comma-separated model-name lists ("message attachments only" and "all attachments"), edited as tags on the settings screen. cloud_storage_migration/models/res_config_settings.py:13-34,42-62; cloud_storage_migration/views/res_config_settings.xml:38-46
## C. Validations, automation, security, external service
- C1. Preconditions raised as errors: no provider configured; no model selected. cloud_storage_migration/models/ir_attachment.py:54-55,66-67
- C2. Eligibility filter (all must hold): local binary with stored file and no URL; linked to a record; not field-bound; model in selected list (message-list models additionally require the attachment be attached to a message); model not in cloud_storage's unsupported list; size between minimum file size and max file size; created more than 7 days ago; not used by a Documents record when that app exists. cloud_storage_migration/models/ir_attachment.py:100-145
- C3. Guardrails: a batch stops after the time budget (half of server real-time limit) or when total size would reach the batch cap; oversize single file is skipped; the cron re-triggers itself until finished. cloud_storage_migration/models/ir_attachment.py:79-91,161-167,182-186
- C4. Failure handling: cursor is committed before each upload so a file is never uploaded twice on timeout; a failed file is logged, rolled back and skipped (it is not retried in the same run). cloud_storage_migration/models/ir_attachment.py:171-180
- C5. Upload timeout per file: 10 s connect, 30 s transfer. cloud_storage_migration/models/ir_attachment.py:37
- C6. Access: report model readable only by the system administrators group; no write/create/delete. cloud_storage_migration/security/ir.model.access.csv:2. Cron entry point additionally requires admin access (decorator). cloud_storage_migration/models/ir_attachment.py:46. Cron runs as the root/system user. cloud_storage_migration/data/ir_cron.xml:9
- C7. No record rules or company scoping in this module; the attachment query is not company-filtered. cloud_storage_migration/models/ir_attachment.py:108-131
- C8. External-service implication: the server itself reads local files and pushes them to the provider (bandwidth/credentials of the server); the provider's credentials belong to the provider module. cloud_storage_migration/models/ir_attachment.py:30-37
- C9. Tests (TEST): removing a model from the tag lists updates the stored setting. cloud_storage_migration/tests/test_res_config_settings.py:29,45
## D. Handoffs
- D1. Provider settings, upload-link generation, unsupported-model list: cloud_storage, cloud_storage_azure, cloud_storage_google. cloud_storage/models/ir_attachment.py:125-132; cloud_storage_azure/models/ir_attachment.py:114-128; cloud_storage_google/models/ir_attachment.py:79-88
- D2. Documents app (not in this addons list) is honoured through an existence check, no direct dependency. cloud_storage_migration/models/ir_attachment.py:100-105
- D3. Reverse move (cloud to local) is owned by cloud_storage. cloud_storage/models/ir_attachment.py:50-67
## E. Configuration defaults that change outcomes
- E1. Seeded once (no-update): max file size 1,000,000,000 bytes; max batch total 1,000,000,000 bytes; both model lists empty; cursor 0. cloud_storage_migration/data/data.xml:4-30
- E2. Code fallbacks if parameters missing: max file 10^9, max batch 10^10 (10 GB, differs from the 1 GB seed). cloud_storage_migration/models/ir_attachment.py:60-61
- E3. Minimum size uses cloud_storage's parameter (default 20 MB). cloud_storage_migration/models/ir_attachment.py:15,59
- E4. Other parameters are reachable through the "Parameters" button. cloud_storage_migration/models/res_config_settings.py:64-79
## F. Extension path
- cloud_storage, cloud_storage_azure, cloud_storage_google (provider hooks). No other Community module names cloud_storage in a manifest.
## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether recent (under 7 days) attachments are ever migrated by another path.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when the provider is switched mid-migration beyond the module's own instruction (cloud_storage/models/res_config_settings.py:11-16).
- UNKNOWN — EVIDENCE INSUFFICIENT: the exact meaning of the cursor when the selected model list changes between runs.

