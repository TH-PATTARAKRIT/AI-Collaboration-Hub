# Source Map (candidate) — `sms_twilio`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sms_twilio` |
| Display name | Twilio SMS |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `076f7165af9d7b00` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sms_twilio/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `test_mail_sms`, `test_mass_mailing`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Send SMS messages using Twilio
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `sms.twilio.account.manage` (SMS Twilio Connection Wizard); `sms.twilio.number` (Twilio Number)
- Objects extended from other modules (6): `mail.notification`, `sms.composer`, `sms.sms`, `sms.tracker`, `res.company`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `mail.notification`, `sms.composer`, `sms.sms`, `sms.tracker`, `res.company`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 54 of 55 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sms_twilio
Source revision: 19.0.post20260921 | Module: "Twilio SMS" (sms_twilio/__manifest__.py:2) | LGPL-3 (:22) | category Hidden/Tools (:5)
Basis: static reading of all models, tools, controller, wizard, security, views; tests by title only.

## A. Capabilities and optionality
- A1. Lets a company send text messages through its own Twilio account instead of the Odoo-operated (IAP) SMS service. sms_twilio/__manifest__.py:6-10; sms_twilio/models/res_company.py:12-19,24-28
- A2. Optional add-on: depends only on sms; no auto_install key (sms itself is auto_install). sms_twilio/__manifest__.py:11-13; sms/__manifest__.py:45
- A3. Conditional on a per-company choice "Send via Odoo" (default) or "Send via Twilio". sms_twilio/models/res_company.py:12-19. With the Twilio choice the standard "buy credits" widget is hidden. sms_twilio/views/res_config_settings_views.xml:10-20
- A4. Includes: sender-number pool per company with country-based sender selection; delivery-status callback endpoint; test-message and number-reload wizard; failure categories for Twilio errors. sms_twilio/models/sms_twilio_number.py:4-20; sms_twilio/tools/sms_twilio.py:10-21; sms_twilio/controllers/controllers.py:33-64; sms_twilio/wizard/sms_twilio_account_manage.py:23-99

## B. Objects and lifecycle
- B1. New object "Twilio number" (company, sequence, number, country). Belongs to one company, removed when the company is removed. sms_twilio/models/sms_twilio_number.py:9-15
- B2. Transient "Twilio connection wizard" mirrors the company's provider/SID/token/numbers fields. sms_twilio/wizard/sms_twilio_account_manage.py:12-21
- B3. Extends: company (provider, SID, token, numbers), outgoing SMS (company, provider id of message, extra failure types), SMS tracker (Twilio message id, error mapping), notification failure types, SMS composer. sms_twilio/models/res_company.py:9-22; sms_twilio/models/sms_sms.py:6-18; sms_twilio/models/sms_tracker.py:15-26; sms_twilio/models/mail_notification.py:4-14; sms_twilio/models/sms_composer.py:4-16
- B4. Lifecycle of one message: queued in Odoo -> grouped by owning company -> sent one by one to Twilio (state "sent" and Twilio message id on success, otherwise a mapped failure state) -> Twilio calls back with later status -> tracker updated and the outgoing record marked for deletion. sms_twilio/models/sms_sms.py:57-72; sms_twilio/tools/sms_api.py:41-78; sms_twilio/controllers/controllers.py:50-62
- B5. Twilio status to Odoo state mapping: queued/accepted/scheduled -> outgoing; sending/receiving -> processing; sent/received -> pending; delivered -> sent; canceled -> canceled; failed/undelivered -> error. sms_twilio/controllers/controllers.py:9-26
- B6. Twilio error codes mapped to delivery-failure categories (account suspended -> expired; unreachable/unknown handset -> invalid destination; blocked/carrier violation -> rejected; landline -> not allowed; unknown -> not delivered). sms_twilio/models/sms_tracker.py:3-12

## C. Validations, automation, security, external service
- C1. Account SID must be 34 characters, start with "AC", and be alphanumeric after the prefix; checked before every send and before reloading numbers. sms_twilio/models/res_company.py:30-36; sms_twilio/tools/sms_api.py:22; sms_twilio/wizard/sms_twilio_account_manage.py:25
- C2. Credential fields (SID, auth token) readable only by the system-administrator group at field level. sms_twilio/models/res_company.py:20-21. Sender-number and wizard models: full access for system administrators only (wizard cannot delete). sms_twilio/security/ir.model.access.csv:2-3
- C3. Outbound call to Twilio's public API per recipient with basic authentication, 5-second timeout; a network failure is logged and the message becomes a generic server error. sms_twilio/tools/sms_api.py:30-39,55-59
- C4. Delivery callback endpoint is public (no login) and accepts POST only; it rejects malformed identifiers, unknown statuses and any call whose Twilio signature (built from the company auth token, callback URL and posted values) does not match. sms_twilio/controllers/controllers.py:33-48,66-74; sms_twilio/tools/sms_twilio.py:29-42
- C5. Callback URL is derived from the company's base URL, so the server must be publicly reachable by Twilio; an incorrect URL is reported as a distinct failure. sms_twilio/tools/sms_twilio.py:24-26; sms_twilio/tools/sms_api.py:96-97,109
- C6. Company scoping: provider choice and Twilio account are per company; each message is routed by the company of the related record (message record company, else stored company, else current company). Different companies may use different Twilio accounts or the Odoo service in the same send run. sms_twilio/models/sms_sms.py:57-75; sms_twilio/models/sms_composer.py:7-16; (TEST) sms_twilio/tests/test_sms_twilio.py:87
- C7. Sender number selection: Twilio number whose country matches the destination country; else the first by sequence; if none configured, sending fails with "From number missing". sms_twilio/tools/sms_twilio.py:10-21; sms_twilio/tools/sms_api.py:25,90-91
- C8. Provider errors translated to user-facing failures: wrong number format, missing recipient, same from/to, missing from, unverified trial recipient, callback URL, authentication. sms_twilio/tools/sms_api.py:80-99,101-116
- C9. Batch size for Twilio sending: 10 per session by default (system parameter), versus 500 for the Odoo service. sms_twilio/models/sms_sms.py:77-81; sms/models/sms_sms.py:163-164
- C10. Neutralization (database copy) replaces every company's Twilio auth token with a dummy value. sms_twilio/data/neutralize.sql:1-2
- C11. Wizard "reload numbers" deletes the company's existing number list and re-creates it from the Twilio account's incoming numbers. sms_twilio/wizard/sms_twilio_account_manage.py:39-62. "Send test" sends a real message through the normal path. :74-99
- C12. Failure-type compatibility code silently refreshes selection values on read (stable-branch workaround with removal note). sms_twilio/models/sms_sms.py:29-52; sms_twilio/models/mail_notification.py:19-45

## D. Handoffs
- D1. SMS framework (queue, send loop, composer, tracker, base API, settings block): sms. sms/models/sms_sms.py:99-135,163-179,233; sms/models/res_company.py:9-12
- D2. Phone country detection: phone_validation. sms_twilio/tools/sms_twilio.py:7,14
- D3. Message-level company field: mail. mail/models/mail_message.py:117
- D4. Consumers of the SMS framework that will use Twilio transparently (no code change): modules that queue SMS through sms (e.g. calendar_sms, event_sms, crm_sms, sale_sms, stock_sms, project_sms trace notes exist) — the routing is by company, not by module. sms_twilio/models/sms_sms.py:57-72
- D5. Only test-only modules name sms_twilio in their manifests: test_mass_mailing, test_mail_sms. (grep of manifests)

## E. Configuration that changes outcomes
- E1. Company setting "SMS Provider" (default Odoo service). sms_twilio/models/res_company.py:18; sms_twilio/models/res_config_settings.py:7
- E2. Account SID, auth token, sender numbers (with countries). sms_twilio/models/res_company.py:20-22
- E3. System parameter for Twilio batch size (default 10). sms_twilio/models/sms_sms.py:80
- E4. Company base URL must be reachable from the internet for status callbacks. sms_twilio/tools/sms_twilio.py:25

## F. Extension path
- sms (framework), sms_twilio (this provider), phone_validation, mail. Other provider-style modules: UNKNOWN — EVIDENCE INSUFFICIENT (none found by grep of "twilio" outside this module and test modules).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: encryption of the auth token at rest (plain character field, sms_twilio/models/res_company.py:21).
- UNKNOWN — EVIDENCE INSUFFICIENT: how inbound (received) SMS are handled; only outbound status callbacks exist here.
- UNKNOWN — EVIDENCE INSUFFICIENT: cost, rate limits and carrier registration requirements (Twilio-side, not in source).
- UNKNOWN — EVIDENCE INSUFFICIENT: delivery when the callback signature check fails on an otherwise valid message (state stays as last known).

