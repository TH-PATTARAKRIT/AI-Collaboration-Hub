# Source Map (candidate) — `crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `crm` |
| Display name | CRM |
| Manifest version | 1.9 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2a7b1a3c1390eccd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/crm/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `sales_team`, `mail`, `calendar`, `resource`, `utm`, `web_tour`, `contacts`, `digest`, `phone_validation`
- Direct dependents in 300-module list (11): `crm_livechat`, `crm_mail_plugin`, `crm_sms`, `event_crm`, `iap_crm`, `partnership`, `sale_crm`, `survey_crm`, `website_crm`, `website_crm_partner_assign`, `website_crm_sms`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `mass_mailing_crm`, `test_crm_full`, `test_discuss_full`, `test_main_flows`
- Custom / third-party modules that declare a dependency (name — license only) (1): `social_hub` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Track leads and close opportunities
- Inventory of user-facing artifacts (counts): menu items 26, views 55, window actions 33, server actions 2, reports 0, mail templates 1, scheduled jobs 2, wizards 6, web routes 3
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (12): `crm.lead.pls.update` (Update the probabilities); `crm.lead2opportunity.partner` (Convert Lead to Opportunity (not in mass)); `crm.lead.lost` (Get Lost Reason); `crm.lead2opportunity.partner.mass` (Convert Lead to Opportunity (in mass)); `crm.merge.opportunity` (Merge Opportunities); `crm.lost.reason` (Opp. Lost Reason); `crm.lead.scoring.frequency` (Lead Scoring Frequency); `crm.lead.scoring.frequency.field` (Fields that can be used for predictive lead scoring computation); `crm.recurring.plan` (CRM Recurring revenue plans); `crm.stage` (CRM Stages); `crm.lead` (Lead); `crm.activity.report` (CRM Activity Analysis)
- Objects extended from other modules (18): `digest.digest`, `mail.alias.mixin`, `crm.team`, `crm.team.member`, `calendar.event`, `utm.campaign`, `mail.activity`, `ir.config_parameter`, `res.users`, `res.config.settings`, `mail.thread.cc`, `mail.thread.blacklist`, `mail.thread.phone`, `mail.activity.mixin`, `utm.mixin`, `format.address.mixin`, `mail.tracking.duration.mixin`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `crm.lead` ← Community: `crm_iap_enrich`, `crm_iap_mine`, `crm_livechat`, `crm_mail_plugin`, `event_crm`, `iap_crm`, `mass_mailing_crm`, `sale_crm`, `survey_crm`, `website_crm` … (+3); open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `digest.digest`, `mail.alias.mixin`, `crm.team`, `crm.team.member`, `calendar.event`, `utm.campaign`, `mail.activity`, `ir.config_parameter`, `res.users`, `res.config.settings`, `mail.thread.cc`, `mail.thread.blacklist`, `mail.thread.phone`, `mail.activity.mixin`, `utm.mixin`, `format.address.mixin`, `mail.tracking.duration.mixin`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 4 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Predictive Lead Scoring: Recompute Automated Probabilities every 1 days; CRM: Lead Assignment every 1 days
- Security: groups declared 2 (`group_use_lead`, `group_use_recurring_revenues`); record rules 8 (of which company-scoped by text 2); access rows 32

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

