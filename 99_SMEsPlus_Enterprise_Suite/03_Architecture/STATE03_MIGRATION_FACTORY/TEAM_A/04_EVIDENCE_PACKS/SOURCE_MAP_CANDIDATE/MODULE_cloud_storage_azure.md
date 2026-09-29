# Source Map (candidate) — `cloud_storage_azure`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `cloud_storage_azure` |
| Display name | Cloud Storage Azure |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `20617485d86bd06d` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/cloud_storage_azure/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `cloud_storage`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Technical Settings / Store chatter attachments in the Azure cloud
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 47 of 47 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — cloud_storage_azure
Source revision: 19.0.post20260921 | Module: "Cloud Storage Azure" (cloud_storage_azure/__manifest__.py:4) | LGPL-3 (:14)
Basis: static reading of models, utils, settings view, neutralize script, uninstall hook, and test file names/titles.

## A. Capabilities and optionality
- A1. Adds Microsoft Azure Blob Storage as one selectable provider for storing new chatter/web-client attachments outside the database and local file store. cloud_storage_azure/__manifest__.py:5; cloud_storage_azure/models/res_config_settings.py:23
- A2. Optional add-on (not auto_install, not an application); depends only on the provider-neutral module cloud_storage. cloud_storage_azure/__manifest__.py:8
- A3. Conditional behaviour: every override acts only when the stored provider setting equals "azure"; otherwise it defers to the next provider. cloud_storage_azure/models/ir_attachment.py:91,97,115; cloud_storage_azure/models/res_config_settings.py:47,60,85
- A4. Files are uploaded by the user's browser directly to Azure using a short-lived signed link issued by Odoo; downloads are served by redirecting the reader to a short-lived signed read link. cloud_storage_azure/models/ir_attachment.py:96-128; cloud_storage/models/ir_attachment.py:24-34
- A5. Ships an offline clean-up script (not part of the running application) that lists blobs, compares them with Odoo attachment URLs and deletes unused ones. cloud_storage_azure/utils/cleanup_cloud_storage_azure.py:10-31

## B. Objects and lifecycle
- B1. No new business model. Extends the attachment record (owner of the type "cloud storage": cloud_storage) and the settings wizard. cloud_storage_azure/models/ir_attachment.py:62-63; cloud_storage_azure/models/res_config_settings.py:21; cloud_storage/models/ir_attachment.py:19-22
- B2. Lifecycle of one attachment: created normally -> flagged as cloud attachment (content cleared, type switched, blob address stored) -> browser uploads to Azure -> later reads use signed read links. cloud_storage/models/ir_attachment.py:36-48; cloud_storage/controllers/attachment.py:12-32
- B3. Blob address is built from account name, container name and a unique path "attachment id / random id / file name". cloud_storage_azure/models/ir_attachment.py:79-83; cloud_storage/models/ir_attachment.py:69-75
- B4. Stored address must match the Azure pattern (account 3-24 lowercase letters/digits; container 3-63 lowercase letters/digits/hyphens, no leading hyphen; blob path); otherwise a validation error is raised on use. cloud_storage_azure/models/ir_attachment.py:65-77; (TEST) cloud_storage_azure/tests/test_cloud_storage_azure.py:167-214

## C. Validations, automation, security, external service
- C1. Saving settings with the provider chosen but any of the five Azure values missing yields an empty configuration, which the base module rejects ("configure before enabling"). cloud_storage_azure/models/res_config_settings.py:49-56; cloud_storage/models/res_config_settings.py:77-79
- C2. On saving changed credentials the module performs a live self-test: uploads an empty test blob, then reads it back; each failure raises a validation error with Azure's response text. cloud_storage_azure/models/res_config_settings.py:58-82; cloud_storage/models/res_config_settings.py:80-81
- C3. Credentials: tenant id, client id, client secret, account name, container name are stored as system parameters (plain text values), edited only through the settings screen. cloud_storage_azure/models/res_config_settings.py:25-40. The client secret is exchanged with Microsoft's login service for a token and then a "user delegation key" (7-day validity) that signs the links. cloud_storage_azure/utils/cloud_storage_azure_utils.py:331-393; cloud_storage_azure/models/ir_attachment.py:44
- C4. Delegation key is cached per database in server memory, refreshed when less than one day remains, and an authentication failure is cached too, so repeated failures do not re-call Azure until settings change or the "invalidate cached key" option is saved. cloud_storage_azure/models/ir_attachment.py:13-59; cloud_storage_azure/models/res_config_settings.py:41-43,100-105
- C5. Signed link lifetimes: upload link 300 s, read link 300 s by default (overridable by context). Upload link grants create-only; read link grants read-only. cloud_storage/models/ir_attachment.py:16-17,87-91; cloud_storage_azure/models/ir_attachment.py:100-119
- C6. Outbound calls use 5-second timeouts. cloud_storage_azure/utils/cloud_storage_azure_utils.py:356,374; cloud_storage_azure/models/res_config_settings.py:73,80
- C7. Switching provider or removing the module is blocked while any attachment still points to an Azure address. cloud_storage_azure/models/res_config_settings.py:84-98; cloud_storage_azure/__init__.py:6-10; (TEST) cloud_storage_azure/tests/test_cloud_storage_azure.py:332-341
- C8. Uninstall removes the five credential parameters and clears the provider setting. cloud_storage_azure/__init__.py:11-17; (TEST) cloud_storage_azure/tests/test_cloud_storage_azure.py:343-351
- C9. Database neutralization (test/copy of a production database) deletes the five credential parameters so a copy cannot reach the production container. cloud_storage_azure/data/neutralize.sql:1-7
- C10. Security groups / record rules / company scoping: none defined by this module (no security folder in manifest). cloud_storage_azure/__manifest__.py:9-11. Settings screen access follows the general settings wizard (owner: base_setup) — UNKNOWN — EVIDENCE INSUFFICIENT for the exact group.
- C11. Observation: in the non-Azure branch of the configuration getter the parent method is returned without being called. cloud_storage_azure/models/res_config_settings.py:48. Effect when another provider is active — UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Provider-neutral engine (attachment type, upload endpoint, min file size, unsupported-model list, settings block): cloud_storage. cloud_storage/models/ir_attachment.py:19-48,125-132; cloud_storage/controllers/attachment.py:9-32; cloud_storage/models/res_config_settings.py:22-37
- D2. Bulk move of existing local files: cloud_storage_migration (uses the upload link this module issues). cloud_storage_migration/models/ir_attachment.py:31-32
- D3. Outgoing email conversion of cloud attachments into links: (TEST) cloud_storage_azure/tests/test_cloud_storage_azure.py:325-330 (mail module owns the conversion; code not read) — UNKNOWN — EVIDENCE INSUFFICIENT for the owning file.

## E. Configuration that changes outcomes
- E1. Provider selection (must be "azure"); five Azure values; minimum file size (default 20,000,000 bytes) below which the browser keeps using normal storage. cloud_storage/models/res_config_settings.py:6,22-37; cloud_storage/models/ir_http.py:12-16
- E2. Changing account or container while old blobs are in use requires the app registration to keep access to the old containers (stated in the module's own instructions). cloud_storage_azure/models/res_config_settings.py:12-16

## F. Extension path
- Modules extending attachment cloud behaviour: cloud_storage (base), cloud_storage_azure, cloud_storage_google, cloud_storage_migration. (grep of "cloud_storage" in manifests found only these four.)

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which user groups may open the settings screen and edit credentials.
- UNKNOWN — EVIDENCE INSUFFICIENT: encryption/masking of the client secret in the parameter store or UI (field is a plain text field, cloud_storage_azure/views/settings.xml:23-24; no masking option seen).
- UNKNOWN — EVIDENCE INSUFFICIENT: actual Azure-side permissions/CORS required beyond the self-test in C2 (no CORS setup in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: attachments of models that read their own file content are excluded via cloud_storage's unsupported list; the complete list was not enumerated.

