# Source Map (candidate) — `account_edi`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_edi` |
| Display name | Import/Export Invoices From XML/PDF |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `dfb575cda9be9f1f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_edi/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `l10n_eg_edi_eta`, `l10n_es_edi_sii`, `l10n_in_edi`, `l10n_sa_edi`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 0, views 8, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `account.edi.format` (EDI format); `account.edi.document` (Electronic Document for an account.move)
- Objects extended from other modules (6): `account.resequence.wizard`, `account.move`, `ir.actions.report`, `ir.attachment`, `account.move.send`, `account.journal`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `account.edi.format` ← Community: `l10n_eg_edi_eta`, `l10n_es_edi_sii`, `l10n_sa_edi`, `l10n_sa_edi_pos`; open-license custom/third-party scanned: —
- `account.edi.document` ← Community: `l10n_sa_edi`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `account.resequence.wizard`, `account.move`, `ir.actions.report`, `ir.attachment`, `account.move.send`, `account.journal`

## 6. Actions / states / validation / automation / security
- State fields found: `account.edi.document` → ['to_send', 'sent', 'to_cancel', 'cancelled']
- Validation: 0 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: EDI: Perform web services operations every 1 days
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 54 of 55 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — account_edi
Source revision: 19.0.post20260921 | Module: "Import/Export Invoices From XML/PDF" (account_edi/__manifest__.py:3) | depends: account (:15) | License LGPL-3 (:25)
Basis: static reading; tests read by name/assertion outline. Base framework for country e-invoicing formats; it defines no concrete format by itself (format hooks return empty/neutral defaults, account_edi/models/account_edi_format.py:58-106). Not auto_install.

## A. Capabilities and optionality
- A1. Framework that lets an "EDI format" be attached to sales journals; on posting, each enabled format produces an electronic document record per invoice which is processed (generated / transmitted / cancelled) by the format's own logic. account_edi/models/account_move.py:233-265; account_edi/models/account_edi_format.py:58-69
- A2. Two processing modes: synchronous formats (no web service) are processed immediately at posting; web-service formats are queued and processed by a scheduled job or manually ("Process now"). account_edi/models/account_move.py:262-265; account_edi/models/account_edi_document.py:200-234; account_edi/views/account_move_views.xml:108-112
- A3. Cancellation flow for already-sent documents: request cancellation, abandon the request, or force-cancel the invoice while a request is pending. account_edi/models/account_move.py:267-274,307-341; account_edi/views/account_move_views.xml:88-123
- A4. Error visibility on the invoice (banner with Info/Warning/Error levels, retry, list of failing documents). account_edi/models/account_move.py:62-88; account_edi/views/account_move_views.xml:5-10,105-139
- A5. Sending: EDI attachments are added to outgoing invoice e-mail / send-and-print; sale documents' PDF may embed format-specific attachments. account_edi/models/account_move_send.py:14-18; account_edi/models/account_move.py:380-390; account_edi/models/ir_actions_report.py:12-47
- A6. Format hooks a concrete format supplies: applicability/actions, whether it needs web services, journal compatibility, default-enablement, configuration checks, PDF preparation. account_edi/models/account_edi_format.py:58-119
- A7. Optional: installed as dependency of localisations (manifests depending on account_edi: l10n_eg_edi_eta, l10n_es_edi_sii, l10n_in_edi, l10n_sa_edi; l10n_sa_edi_pos indirectly). The scheduled job ships inactive and is activated when a format needing web services is created. account_edi/data/cron.xml:2-9; account_edi/models/account_edi_format.py:40-42
- A8. Vendor-bill import test relates to partner lookup by tax id (TEST) account_edi/tests/test_import_vendor_bill.py:9-21 (the function under test lives outside this module).

## B. Objects, relationships, lifecycle
- B1. EDI format (account.edi.format): name + unique code. account_edi/models/account_edi_format.py:11-17
- B2. EDI document (account.edi.document): one per (format, invoice), deleted with the invoice; holds generated attachment (system-admin readable), state, last error, blocking level. account_edi/models/account_edi_document.py:19-43
- B3. Document states: To Send -> Sent; Sent -> To Cancel -> Cancelled. account_edi/models/account_edi_document.py:26
- B4. Creation/re-arm: at invoice posting a document is created (or reset to To Send, attachment cleared) for every journal format that says it applies; configuration errors from the format abort posting with a message. account_edi/models/account_move.py:238-261
- B5. Job building: documents in To Send / To Cancel that are not blocked by an Error are grouped into jobs by format, state, company and an optional format-supplied key (else one per invoice). account_edi/models/account_edi_document.py:67-100 (TEST: account_edi/tests/test_edi.py:34-60)
- B6. Job result: success -> Sent (error cleared); failure -> error text and blocking level stored (default level Error). Error-level documents are excluded from later automatic processing until retried. account_edi/models/account_edi_document.py:121-131,81,245 (TEST: test_edi.py:62-76 warning documents remain To Send and succeed on retry)
- B7. Cancel result: success -> Cancelled and attachment removed; if the invoice is posted and no web-service document remains uncancelled, invoice is reset to draft and cancelled. account_edi/models/account_edi_document.py:137-173
- B8. Invoice aggregate state "Electronic invoicing" (stored) is derived only from web-service documents. account_edi/models/account_move.py:42-55
- B9. Invoice cancel/draft: cancelling an invoice marks unsent documents Cancelled, sent ones To Cancel; reset-to-draft deletes To-Send documents and clears errors. account_edi/models/account_move.py:275-305
- B10. Mail readiness: an invoice with a document still To Send is not "ready to be sent". account_edi/models/account_move.py:222-231 (TEST: test_edi.py:165-173)

## C. Validations, security, multi-company
- C1. Uniqueness of format code and of one document per format per invoice. account_edi/models/account_edi_format.py:14-17; account_edi/models/account_edi_document.py:40-43
- C2. Reset to draft is blocked (with pointer to "Request EDI Cancellation") when a web-service document is Sent/To Cancel and the format supports cancel; the Reset button is also hidden. account_edi/models/account_move.py:102-119,287-299
- C3. A journal cannot drop a format while unsynchronised web-service documents exist; non-web-service documents pending are deleted instead. account_edi/models/account_journal.py:24-44
- C4. Journal format selection is auto-computed (compatible + enabled-by-default + protected in-use) depending on journal type and company fiscal country. account_edi/models/account_journal.py:46-83
- C5. Attachments of web-service documents (government-sent) cannot be deleted. account_edi/models/ir_attachment.py:10-16
- C6. Invoices with a sent web-service document cannot be resequenced. account_edi/wizard/account_resequence.py:8-22
- C7. Concurrency: web-service processing locks documents, invoice and attachments; if already locked it skips (cron) or errors ("being sent by another process") for manual processing with no commit. account_edi/models/account_edi_document.py:217-230
- C8. Jobs must be single-format, single-company, single-state (guards). account_edi/models/account_edi_document.py:184-187
- C9. Access: all internal users read format and document; invoicing group (account.group_account_invoice) has full rights. account_edi/security/ir.model.access.csv:2-5. No record rules or company scoping defined in this module (UNKNOWN — EVIDENCE INSUFFICIENT on isolation, relies on invoice access and account's rules).
- C10. Cancel-request also checks fiscal lock dates. account_edi/models/account_move.py:307-312

## D. Handoffs
- D1. Posting, draft, cancel, sequence, mail-send: account (hooks extended: post, cancel, draft, ready-to-send, send extra attachments). account_edi/models/account_move.py:233,275,291,222; account_edi/models/account_move_send.py:14
- D2. Scheduled job "EDI: Perform web services operations": daily interval, 20 jobs per run, re-triggers itself if jobs remain; triggered also after posting/cancelling. account_edi/data/cron.xml:3-9; account_edi/models/account_edi_document.py:237-251; account_edi/models/account_move.py:264-265,283
- D3. Format implementation, transmission to tax authorities, and legal semantics: owned by dependent localisation modules (see F). account_edi/models/account_edi_format.py:58-69
- D4. Tax details helper for formats: wrapper over account's aggregated-taxes helper. account_edi/models/account_move.py:155-220
- D5. Attachment/main-attachment handling: the EDI XML is prevented from becoming the invoice's main attachment (mail/attachment viewer). account_edi/models/account_move.py:349-353
- D6. Audit: chatter messages for cancellation requested / called off / forced. account_edi/models/account_move.py:272,323,339
- D7. Note: account_edi_ubl_cii is a different (newer) path for UBL/CII generation and also extends invoice sending; not part of this module.

## E. Configuration that changes outcomes
- E1. Journal EDI formats (checkbox list, shown only if compatible formats exist). account_edi/views/account_journal_views.xml:9-15
- E2. Format's needs-web-services / default-enabled / journal-compatibility (default: sales journals only). account_edi/models/account_edi_format.py:71-97
- E3. Cron active flag (default inactive) and batch size 20. account_edi/data/cron.xml:6-9
- E4. Context flag to skip the cron trigger on posting. account_edi/models/account_move.py:263
- E5. Developer-mode-only filters and EDI document list on the invoice. account_edi/views/account_move_views.xml:74-77,150

## F. Extension path (module names only)
- account.edi.format: l10n_eg_edi_eta, l10n_es_edi_sii, l10n_sa_edi, l10n_sa_edi_pos.
- account.edi.document: l10n_sa_edi.
- Modules referencing edi_state / edi_document_ids: account_edi, l10n_eg_edi_eta, l10n_es_edi_sii, l10n_gr_edi, l10n_gr_edi_e_invoo, l10n_hu_edi, l10n_it_edi, l10n_jo_edi, l10n_jo_edi_pos, l10n_my_edi, l10n_my_edi_pos, l10n_ro_edi, l10n_rs_edi, l10n_sa_edi, l10n_sa_edi_pos, l10n_tw_edi_ecpay (name overlap only; some may use their own fields).
- account.journal: account, account_check_printing, account_debit_note, account_edi, account_payment, account_peppol and many l10n_*. account.move.send: many (account_edi_ubl_cii, account_peppol, l10n_* EDI modules, snailmail_account). account.resequence.wizard: account_edi, l10n_es_edi_sii, l10n_lk_invoice. ir.actions.report: account, account_edi, account_edi_ubl_cii, sale, purchase, stock and others.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how many current localisations still use this legacy framework versus their own field-based flow (only manifest dependencies and name-grep were checked).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the vendor-bill import path (no import code in this module; test only references partner lookup).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the cron is activated in databases where formats are created by demo/localisation data (activation logic is at format creation, account_edi/models/account_edi_format.py:40-42).

