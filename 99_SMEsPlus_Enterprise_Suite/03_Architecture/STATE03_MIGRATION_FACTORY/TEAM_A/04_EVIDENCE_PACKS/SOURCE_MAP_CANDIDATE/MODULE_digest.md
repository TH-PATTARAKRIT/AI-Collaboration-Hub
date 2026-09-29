# Source Map (candidate) — `digest`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `digest` |
| Display name | KPI Digests |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4e41053e52b9bc11` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/digest/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`, `portal`, `resource`
- Direct dependents in 300-module list (10): `account`, `base_automation`, `crm`, `hr`, `hr_recruitment`, `im_livechat`, `project`, `sale_management`, `stock`, `website`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `mass_mailing`, `point_of_sale`, `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing / —
- Inventory of user-facing artifacts (counts): menu items 2, views 7, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `digest.digest` (Digest); `digest.tip` (Digest Tips)
- Objects extended from other modules (2): `res.users`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `digest.digest` ← Community: `account`, `crm`, `hr_recruitment`, `im_livechat`, `point_of_sale`, `project`, `sale_management`, `website_sale`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `res.users`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: `digest.digest` → ['activated', 'deactivated']
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Digest Emails every 1 days
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 45 of 45 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — digest
Source revision: 19.0.post20260921 | Module: "KPI Digests" (digest/__manifest__.py:4) | category Marketing (:5) | LGPL-3 (:28)
Basis: static reading of models, controller, security, data, settings view; test titles.
## A. Capabilities and optionality
- A1. Sends periodic e-mails to internal users summarising key business figures (KPIs) over three time windows with change against the previous period, plus one product "tip". digest/models/digest.py:246-328,379-395
- A2. Optional add-on, not auto_install, not an application; depends on mail, portal, resource. digest/__manifest__.py:11-15
- A3. Base KPIs in this module: "Connected Users" and "Messages Sent" (comments/e-mails). Other modules add their own KPI switches to the same digest object (see D1). digest/models/digest.py:40-85
- A4. A default digest "Your Odoo Periodic Digest" (daily; KPIs: connected users, messages) is created once, with the administrator as recipient. digest/data/digest_tips_data.xml:4-10
- A5. Settings option "Digest Emails": when on, every newly created internal user is auto-subscribed to the chosen digest; seeded on with the default digest. digest/models/res_config_settings.py:9-10; digest/models/res_users.py:9-19; digest/data/res_config_settings_data.xml:3-10; digest/views/res_config_settings_views.xml:8-20
## B. Objects and lifecycle
- B1. Digest (digest.digest): name, recipients (internal users only), periodicity daily/weekly/monthly/quarterly, next mailing date, company, state Activated/Deactivated, KPI on/off flags. digest/models/digest.py:21-43
- B2. Tip (digest.tip): ordered hint text with an authorised group and the list of users who already received it. digest/models/digest_tip.py:7-22
- B3. Lifecycle: create (next date = today + periodicity if empty) -> scheduled run when next date reached and state Activated -> one e-mail per recipient -> next date pushed forward. digest/models/digest.py:91-97,140-157,226-232,367-377
- B4. Activate / Deactivate buttons and "Send Now" (manual send does not change periodicity). digest/models/digest.py:121-138; digest/views/digest_views.xml:23-30
- B5. Slow-down rule: on automatic sending, if none of the recipients logged in during the look-back window (2 days for daily, 7 days weekly, 1 month monthly, 3 months quarterly), periodicity is lowered one step (daily to weekly to monthly to quarterly) and recipients are told. digest/models/digest.py:147-157,346-351,451-478; (TEST) digest/tests/test_digest.py:183,224
- B6. Each recipient's e-mail is queued as an outgoing mail, deleted after sending, in the recipient's language. digest/models/digest.py:151-154,203-222
## C. Validations, automation, security, external service
- C1. Scheduled job "Digest Emails" runs daily (first run about 2 hours after install) as the system user; selects Activated digests due today or earlier; a mail-delivery failure is logged and skipped so the digest is retried at the next run. digest/data/ir_cron_data.xml:3-12; digest/models/digest.py:226-232
- C2. KPI windows: last 24 hours, last 7 days, last 30 days, each against the preceding equal window, in the company's working-calendar time zone when set. Percentage change is shown only when both values are non-zero. digest/models/digest.py:379-395,445-449
- C3. KPI values are computed as the recipient (their access rights and company); a KPI the recipient may not read is silently omitted from that person's mail. digest/models/digest.py:277-292,306-307
- C4. Company scoping: a digest with a company counts only that company's records; a digest without company uses the current company at computation. Sender address is the digest company's e-mail, else current user's, else the system user's. digest/models/digest.py:58-69,401-438,207-211
- C5. Access: internal users read digests and tips; the ERP-manager group has full rights on both. No record rules. digest/security/ir.model.access.csv:2-5. Recipient list, next date and manual send/activate controls are shown to system administrators only. digest/views/digest_views.xml:23-30,46,65
- C6. Tips are chosen among those the user has not received and whose authorised group the user belongs to (or no group); each send marks the tip as received (unless suppressed). digest/models/digest.py:309-328
- C7. Unsubscribe: every mail carries a signed link and one-click List-Unsubscribe header. A public POST endpoint (CSRF disabled deliberately) unsubscribes when the token matches; wrong token gives "not found". Legacy no-token form works only for logged-in internal users. digest/models/digest.py:195-218,234-240; digest/controllers/portal.py:14-60; (TEST) digest/tests/test_digest.py:320,338,365
- C8. Changing periodicity via e-mail link requires an ERP-manager login. digest/controllers/portal.py:62-73
- C9. Users can subscribe/unsubscribe themselves; only internal users are accepted; changes are done with elevated rights. digest/models/digest.py:103-119
- C10. External service: outbound e-mail only (mail server of the database); no third-party service. digest/models/digest.py:222
## D. Handoffs (KPI providers extend the digest; each owns its figures)
- D1. Accounting revenue: account. account/models/digest.py:11-12
- D2. CRM new leads / opportunities won: crm. crm/models/digest.py:11-14
- D3. Live chat happiness, conversations, response time: im_livechat. im_livechat/models/digest.py:10-15
- D4. New employees from recruitment: hr_recruitment. hr_recruitment/models/digest.py:11-12
- D5. POS sales: point_of_sale. point_of_sale/models/digest.py:11-12
- D6. Website shop sales: website_sale. website_sale/models/digest.py:10-11
- D7. All sales: sale_management. sale_management/models/digest.py:10-11
- D8. Open tasks: project. project/models/digest_digest.py:11-12
- D9. Mail rendering/queue: mail. digest/models/digest.py:162-193,222
## E. Configuration that changes outcomes
- E1. Digest periodicity, KPI switches, recipient list, activation state. digest/models/digest.py:28-43
- E2. Auto-subscribe of new internal users (two system parameters). digest/models/res_users.py:13-18
- E3. Company working-calendar time zone for KPI windows. digest/models/digest.py:381-383
- E4. Custom KPIs can be added by naming a switch field with the prefix kpi_, x_kpi_ or x_studio_kpi_ and providing a matching value field. digest/models/digest.py:54,441-443
## F. Extension path
- Modules extending digest.digest: account, crm, im_livechat, hr_recruitment, point_of_sale, project, sale_management, website_sale (grep). Modules only referring to it: mail (template rendering), mass_mailing, website, base (view handling).
## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: template visual layout details and the full tips catalogue (16 seeded records counted, texts not analysed).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when a recipient has no e-mail address.
- UNKNOWN — EVIDENCE INSUFFICIENT: delivery-authentication (DKIM) requirement for one-click unsubscribe to work in mail clients (comment only, digest/models/digest.py:213).

