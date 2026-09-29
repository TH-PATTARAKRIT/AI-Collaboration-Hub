# Source Map (candidate) — `iap_mail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `iap_mail` |
| Display name | IAP / Mail |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4dce5a25f1c7a1ad` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/iap_mail/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `iap`, `mail`
- Direct dependents in 300-module list (7): `crm_iap_enrich`, `crm_iap_mine`, `iap_crm`, `partner_autocomplete`, `sms`, `snailmail`, `website_crm_iap_reveal`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Bridge between IAP and mail
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `iap.account`, `mail.thread`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `iap.account`, `mail.thread`

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

# Source Map trace note — iap_mail
Source revision: 19.0.post20260921 | Module: "IAP / Mail", category Hidden/Tools, LGPL-3 (iap_mail/__manifest__.py:6,9,31). Basis: static reading of module and of the iap parent model for context; no tests in this module.

## A. Capabilities and optionality
- A1. Bridge between the paid-service credit system (IAP) and the mail/chatter system. It adds change history and a discussion panel to IAP accounts, live pop-up notices to the user (success, error, out-of-credit), and reusable message templates for company-enrichment results. iap_mail/models/iap_account.py:8-40; iap_mail/views/iap_views.xml:9-11; iap_mail/data/mail_templates.xml:4,119
- A2. Conditional: auto_install on with dependencies iap and mail; present whenever both are installed. iap_mail/__manifest__.py:11-16
- A3. No menus, settings or groups of its own.

## B. Objects and relationships
- B1. Extends the IAP account (owner: iap) so it becomes a discussion-enabled record. Tracked fields: linked companies, email-alert threshold, email-alert recipients. iap_mail/models/iap_account.py:8-13
- B2. IAP account (owner: iap): service, token, companies, remote-read balance, alert threshold/recipients, state (banned / registered / unregistered). iap/models/iap_account.py:23-42
- B3. Notifications are transient: pushed to the current user's browser session only; nothing stored. iap_mail/models/iap_account.py:24-40; iap_mail/static/src/js/services/iap_notification_service.js:10-17
- B4. Out-of-credit notice carries a link to buy credits for the named service. iap_mail/models/iap_account.py:34-39

## C. Validations, security, external effects
- C1. Validations on threshold/recipients live in iap: threshold must not be negative; every alert recipient must have an email address. iap/models/iap_account.py:45-53
- C2. Security is inherited from iap: system administrators full rights; internal users read and create only; a company rule restricts accounts to those with no company or the user's allowed companies. iap/security/ir.model.access.csv:2-3; iap/security/ir_rule.xml:6-8. The token field is readable only by administrators. iap/models/iap_account.py:31-32
- C3. External service: editing threshold/recipients sends them to the IAP server; opening an account fetches balance/state from it (skipped in tests). Failures are logged, not raised. iap/models/iap_account.py:56-82,84-100. Credential implication: the account token is the authentication key for the paid service and is transmitted to the IAP endpoint (default iap.odoo.com). iap/models/iap_account.py:15,29-33
- C4. Tracking means threshold/recipient/company changes are logged on the account's chatter (mail behaviour, not re-verified here). iap_mail/models/iap_account.py:11-13

## D. Handoffs
- D1. Company enrichment message templates are rendered by partner_autocomplete (company data by DnB) and by crm_iap_enrich / mail_plugin (enrich_company). partner_autocomplete/models/res_partner.py:231,251; crm_iap_enrich/models/crm_lead.py:199; mail_plugin/controllers/mail_plugin.py:122,381
- D2. Notification senders: crm_iap_enrich (no-credit, error, success on lead enrichment) and sms (success after account code). crm_iap_enrich/models/crm_lead.py:92,98,104; sms/wizard/sms_account_code.py:21
- D3. Account, service catalog, endpoint, credits URL: iap. Chatter and messaging: mail.

## E. Configuration that changes outcomes
- E1. Alert threshold of zero hides/does not require recipients in the form; a positive threshold makes recipients required. iap/views/iap_views.xml:30-33
- E2. IAP endpoint override: UNKNOWN — EVIDENCE INSUFFICIENT (helper iap_tools.iap_get_endpoint not read).

## F. Extension path
- Modules calling into it: crm_iap_enrich, sms, partner_autocomplete, mail_plugin. Parent: iap.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which other IAP-consuming modules (e.g. SMS credit) rely on the alert email flow beyond the two callers listed.
- UNKNOWN — EVIDENCE INSUFFICIENT: contents of the enrichment templates (long HTML, only structure sampled).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether user-visible pop-ups reach users who are not connected (bus delivery, mail/bus modules not read).

