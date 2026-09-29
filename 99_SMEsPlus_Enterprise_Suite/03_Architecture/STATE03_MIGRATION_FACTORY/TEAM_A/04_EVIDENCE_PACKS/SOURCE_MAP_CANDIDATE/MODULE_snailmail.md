# Source Map (candidate) — `snailmail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `snailmail` |
| Display name | Snail Mail |
| Manifest version | 0.4 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / BOSS-DECISION-PENDING (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e82e445314c97c39` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/snailmail/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `iap_mail`, `mail`
- Direct dependents in 300-module list (1): `snailmail_account`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 1, views 2, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `snailmail.letter` (Snailmail Letter)
- Objects extended from other modules (7): `mail.notification`, `ir.actions.report`, `mail.thread`, `res.company`, `res.config.settings`, `mail.message`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `mail.notification`, `ir.actions.report`, `mail.thread`, `res.company`, `res.config.settings`, `mail.message`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `snailmail.letter` → ['pending', 'sent', 'error', 'canceled']
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Snailmail: process letters queue every 24 hours
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 52 of 52 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — snailmail
Source revision: 19.0.post20260921 | Module: "Snail Mail" (snailmail/__manifest__.py:3) | category Hidden/Tools (:8)
Basis: static reading of manifest, all models, security, data, views; country_utils and static files not read in detail.

## A. Capabilities and optionality
- A1. Lets users send a document (typically an invoice or follow-up) as a printed letter by post, through the Odoo IAP snailmail service. snailmail/__manifest__.py:4-6; snailmail/data/iap_service_data.xml:4-9
- A2. Infrastructure module: auto_install, depends on iap_mail and mail. It does not by itself add a "send by post" button on accounting documents — that is done by snailmail_account. snailmail/__manifest__.py:10-13,21; snailmail_account/__manifest__.py:10; snailmail_account/models/account_move_send.py:46-66
- A3. Company-level print options: colour (default on), cover page (default off), both sides (default off); a layout-dependent rule forces cover page on for the "boxed", "bold" and "striped" report layouts. snailmail/models/res_company.py:10-12; snailmail/models/res_config_settings.py:9-30
- A4. Letters appear in a "Snailmail Letters" list under the Email technical menu. snailmail/views/snailmail_views.xml:51-60
- A5. Scheduled job "process letters queue" runs every 24 hours. snailmail/data/snailmail_data.xml:4-11

## B. Objects and lifecycle
- B1. New object Snailmail Letter: sender, source document (model + id), recipient partner, company, chosen report, generated PDF attachment, print options (colour/cover/duplex), state, error code, information text, address snapshot, related status message. snailmail/models/snailmail_letter.py:33-71
- B2. States: In Queue (pending, default), Sent, Error, Cancelled. snailmail/models/snailmail_letter.py:47-56
- B3. On creation: a chatter message of type "snailmail" ("Letter sent by post with Snailmail") is posted on the source document; the recipient address is copied onto the letter; a "snail"-type notification (already marked read, status ready) is created for the recipient. snailmail/models/snailmail_letter.py:80-114; snailmail/models/mail_message.py:12-14; snailmail/models/mail_notification.py:9-10
- B4. Address snapshot follows the partner until the letter is sent or cancelled: editing the partner's street/city/zip/state/country updates all unsent letters for that partner. snailmail/models/res_partner.py:12-26
- B5. Send path: address validity check (street, city, zip, country needed) -> PDF prepared (report rendered in English, A4, margins whitened, optional cover page) -> uploaded with account token and database id to the IAP snailmail endpoint -> per-document result written back to letter and notification. snailmail/models/snailmail_letter.py:369-372,399-457,151-193,516-567
- B6. Outcomes: success sets Sent with the provider's tracking id; failures set Error with a code; insufficient credit additionally raises a "no credit" notification to the user. snailmail/models/snailmail_letter.py:430-457
- B7. Manual actions: "Send Now" and "Cancel" on pending/error letters. Sending one letter runs immediately; several selected letters are only re-queued. snailmail/views/snailmail_views.xml:24-25; snailmail/models/snailmail_letter.py:460-476
- B8. Retry job: sends letters in Pending state and letters in Error whose code is trial, credit, attachment or missing-fields; stops at the first credit error and commits after every letter. snailmail/models/snailmail_letter.py:479-489

## C. Validations, automation, security, external service
- C1. Recipient must have a name (or parent company name) else the letter goes to Error "missing required fields". snailmail/models/snailmail_letter.py:229-236. Incomplete address goes to Error the same way. :369-391,492-495
- C2. Report must be A4; some modern layouts (bubble, wave, folder) are temporarily replaced by the standard layout while rendering. snailmail/models/snailmail_letter.py:172-188
- C3. Maximum 8 pages is stated in the error text; the check itself is done by the provider. snailmail/models/snailmail_letter.py:333-334 (message only)
- C4. Country coverage is decided by the provider: unsupported country returns "no price available". snailmail/models/snailmail_letter.py:326-327. Country names are printed in English from a built-in table. snailmail/models/res_partner.py:28-36
- C5. Germany-specific address formatting (single street line with "//" for second line) applied when rendering letters. snailmail/models/res_partner.py:38-50; snailmail/models/snailmail_letter.py:499-503
- C6. External service: endpoint default https://iap-snailmail.odoo.com (overridable by system parameter), timeout 30 s (overridable). Sent data: IAP account token, database UUID, sender and recipient addresses, company logo, the PDF, options (currency EUR). snailmail/models/snailmail_letter.py:19-21,202,227-228,265-267,297-306,392-395. Credits ("Stamps") are bought via IAP. snailmail/data/iap_service_data.xml:8
- C7. Access: every internal user may read, write and create letters (no delete); system administrators have full rights. snailmail/security/ir.model.access.csv:2-3
- C8. Attachment safety: creating or changing a letter requires read access to the chosen attachment; the letter itself exposes the PDF content to users who could not read the attachment directly. snailmail/models/snailmail_letter.py:118-124; (TEST) snailmail/tests/test_attachment_access.py:28-72
- C9. Company scoping: letter carries a company (default current, read-only); no record rule in this module; the return address is the letter company's partner. snailmail/models/snailmail_letter.py:41-42,255-262; snailmail/__manifest__.py:14-20. Multi-company visibility of letters — UNKNOWN — EVIDENCE INSUFFICIENT.
- C10. Batch cancel: cancelling the "snail" notification type cancels the current user's unsent letters for that model. snailmail/models/mail_thread.py:11-25
- C11. Failure categories added to notifications: credit, trial, price, fields, format, unknown. snailmail/models/mail_notification.py:11-18
- C12. When rendering for post the standard report is never reused from a stored attachment. snailmail/models/ir_actions_report.py:7-12

## D. Handoffs
- D1. Invoice/follow-up sending via post (partner preference "by Post", send-wizard method, letter creation, alerts for bad address, unlink of letters with the invoice): snailmail_account. snailmail_account/models/account_move_send.py:13-24,46-66; snailmail_account/models/res_partner.py:8; snailmail_account/models/account_move.py:8-13
- D2. Credits/account token/notifications: iap and iap_mail. snailmail/models/snailmail_letter.py:15,202,435-449
- D3. Chatter messages and notifications: mail. snailmail/models/mail_message.py:5; snailmail/models/mail_notification.py:6
- D4. Regional layouts adjusting recipient window for letters: l10n_din5008, l10n_ch (context flag "snailmail_layout"). l10n_din5008/report/din5008_report.xml:39; l10n_ch/models/ir_actions_report.py:77
- D5. No accounting entries are created by this module.

## E. Configuration that changes outcomes
- E1. Company: colour, cover page, both sides. snailmail/models/res_company.py:10-12
- E2. Report layout choice (forces cover page for some layouts; unsupported layouts replaced during rendering). snailmail/models/res_config_settings.py:15-30; snailmail/models/snailmail_letter.py:179-188
- E3. System parameters for endpoint and timeout. snailmail/models/snailmail_letter.py:396-397
- E4. IAP credit balance. snailmail/data/iap_service_data.xml:8-9

## F. Extension path
- mail, iap_mail (base), snailmail (engine), snailmail_account (invoice sending), l10n_din5008 and l10n_ch (layout adjustments). test_mail_full lists snailmail only as a commented-out entry. test_mail_full/__manifest__.py:18

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how the client-side (JavaScript) letter creation and resend UI work in the discuss/chatter (static/src not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: cost per letter, supported-country list beyond the built-in name table, and provider-side validation rules.
- UNKNOWN — EVIDENCE INSUFFICIENT: multi-company record visibility of letters.
- UNKNOWN — EVIDENCE INSUFFICIENT: retention of stored PDFs after sending (no cleanup found in this module).

