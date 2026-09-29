# Source Map (candidate) — `attachment_indexation`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `attachment_indexation` |
| Display name | Attachments List and Document Indexation |
| Manifest version | 2.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2509ff7520bb12b4` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/attachment_indexation/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (1): `hr_recruitment`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `ir.attachment`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.attachment`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 23 of 23 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: attachment_indexation
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Extracts searchable text from uploaded files so attachment content can be indexed. Supported types: Word (docx), PowerPoint (pptx), Excel (xlsx), OpenDocument (text/spreadsheet), and PDF (attachment_indexation/__manifest__.py:8-11; attachment_indexation/models/ir_attachment.py:20).
- Optional and conditional: depends on web only, no auto-install flag (attachment_indexation/__manifest__.py:15). Category Hidden/Tools (attachment_indexation/__manifest__.py:6).
- Conditional on external libraries: PDF indexing needs the PDF-text library; if missing, a warning is logged and PDFs are not indexed (attachment_indexation/models/ir_attachment.py:16-18,220-229). Spreadsheet (xlsx) indexing needs the spreadsheet-reading library; if missing it yields empty text (attachment_indexation/models/ir_attachment.py:106-111).
- The manifest description also mentions showing attachments on top of forms; no code for that exists in this module (attachment_indexation/__manifest__.py:10; module has only the attachment model extension: attachment_indexation/__init__.py:4): UNKNOWN — EVIDENCE INSUFFICIENT for who provides it.

## B. Business objects, relationships, lifecycle
- Extends the generic Attachment record only; it adds no new objects or fields (attachment_indexation/models/ir_attachment.py:67-68).
- Lifecycle: when an attachment's content is stored, the index routine tries each file type in order (docx, pptx, xlsx, opendoc, pdf) and takes the first non-empty text, else falls back to the base behavior (attachment_indexation/models/ir_attachment.py:254-267).
- A one-entry cache keyed by content checksum avoids repeated extraction; copying an attachment seeds the cache with its existing index text (attachment_indexation/models/ir_attachment.py:23,256-259,268-275).

## C. Validations, automation, security, credentials
- Failures are swallowed: unreadable, corrupt or oversized structures give empty index text rather than errors (attachment_indexation/models/ir_attachment.py:81-82,133-134,209-210,251-252).
- PDF gate: content must begin with the PDF signature (attachment_indexation/models/ir_attachment.py:217-218).
- Spreadsheet-like documents are rendered as comma-separated rows prefixed with the sheet name; blank rows skipped (attachment_indexation/models/ir_attachment.py:121-137,172-190).
- Repeated empty rows/columns in OpenDocument spreadsheets are capped (100 columns, 50 rows) (attachment_indexation/models/ir_attachment.py:144,157,174).
- Text cleanup removes NUL characters and collapses whitespace (attachment_indexation/models/ir_attachment.py:35-55,264).
- No groups, access rules, or company scoping defined; inherits attachment permissions from base: UNKNOWN — EVIDENCE INSUFFICIENT.
- No credentials or external services; extraction runs locally in-process. Privacy implication: document text becomes stored index content on the attachment (attachment_indexation/models/ir_attachment.py:263-269).
- (TEST) A sample PDF yields the exact text "TestContent!!" (attachment_indexation/tests/test_indexation.py:19-24); skipped if the PDF library is absent (attachment_indexation/tests/test_indexation.py:19).

## D. Handoffs to other modules
- Attachment storage and base indexing default (plain text types) are owned by base (attachment_indexation/models/ir_attachment.py:267 calls the parent behavior).
- Any search or document features consuming the index text: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration/defaults that change outcomes
- Presence of the PDF and spreadsheet libraries on the host controls whether those types are indexed (attachment_indexation/models/ir_attachment.py:16-18,106-111).
- Type order is fixed (attachment_indexation/models/ir_attachment.py:20,261).

## F. Effective extension path
- Additional file types can be added by extending the attachment model's index step; the mechanism is the shared index hook (attachment_indexation/models/ir_attachment.py:254-267). No dependents identified in this scope.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: size limits on documents indexed, and the trigger conditions in the base module deciding when indexing is invoked.
- UNKNOWN — EVIDENCE INSUFFICIENT: the "attachments shown at the top of forms" claim.

