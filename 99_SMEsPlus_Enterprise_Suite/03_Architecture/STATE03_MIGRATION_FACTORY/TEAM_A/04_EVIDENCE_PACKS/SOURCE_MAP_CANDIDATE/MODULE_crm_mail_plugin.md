# Source Map (candidate) — `crm_mail_plugin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `crm_mail_plugin` |
| Display name | CRM Mail Plugin |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `1ef47b64a749afce` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/crm_mail_plugin/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `crm`, `mail_plugin`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Turn emails received in your mailbox into leads and log their content as internal notes.
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 1, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 4
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `crm.lead`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `crm.lead`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 28 of 29 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: crm_mail_plugin (CRM Mail Plugin)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/crm_mail_plugin.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge between the mailbox add-in (mail_plugin) and CRM: turn a received email into a lead and log email content as an internal note (crm_mail_plugin/__manifest__.py:9, 12-15).
- Conditional: `auto_install` true; activates when crm and mail_plugin are both present (crm_mail_plugin/__manifest__.py:21).
- Core current endpoint: create a lead from a contact plus email subject and body; lead title is the plain-text subject, description is the body, linked to the chosen contact (crm_mail_plugin/controllers/crm_client.py:42-54).
- Contact panel in the add-in shows the contact's leads (up to a page size, default 5) with revenue, probability and, if recurring revenue is enabled for the user, recurring revenue and plan (crm_mail_plugin/controllers/mail_plugin.py:16-52, 31, 43-48).
- Email content may be logged as a note on leads; lead model is added to the list of allowed logging targets (crm_mail_plugin/controllers/mail_plugin.py:71-75). Logging itself is owned by mail_plugin (mail_plugin/controllers/mail_plugin.py:250-270).
- Add-in translation set is extended with this module's terms (crm_mail_plugin/controllers/mail_plugin.py:77-81).
- Legacy (deprecated since 14.3, kept for old add-in versions): log a message on a lead, list leads by partner, redirect to a prefilled lead form, open a lead in edit mode (crm_mail_plugin/controllers/crm_client.py:13-40, 56-64; crm_mail_plugin/models/crm_lead.py:10-23; crm_mail_plugin/views/crm_mail_plugin_lead.xml:3-9; crm_mail_plugin/views/crm_lead_views.xml:3-9).

## B. Business objects, relationships, lifecycle
- Lead (crm) -> Contact (many-to-one, set at creation from the add-in) (crm_mail_plugin/controllers/crm_client.py:48-52).
- Email -> internal note on lead (chatter message), optional attachments (mail_plugin/controllers/mail_plugin.py:250-270).
- Lifecycle: leads are created with only name, contact and description; stage, team, salesperson come from crm defaults: UNKNOWN — EVIDENCE INSUFFICIENT for exact defaults.
- Missing contact: request returns a "partner_not_found" error rather than creating a lead (crm_mail_plugin/controllers/crm_client.py:44-46).

## C. Validations, automation, security, multi-company
- Authentication: add-in routes use an "outlook" auth mode based on a per-user access key with the plugin scope; requests then run as that user (mail_plugin/models/ir_http.py:14-30). Lead routes in this module reuse it (crm_mail_plugin/controllers/crm_client.py:42).
- Feature gating: leads section and logging target appear only if the user can create leads; otherwise the add-in behaves as if CRM were absent (crm_mail_plugin/controllers/mail_plugin.py:56-63, 71-74, 77-80). (TEST) leads section absent for a user without lead access, present after granting the "all leads" sales group; only that contact's leads returned (crm_mail_plugin/tests/test_crm_mail_plugin.py:11-41).
- Logging on a model outside the allowed list is refused (mail_plugin/controllers/mail_plugin.py:260-261).
- Multi-company: lead is created under the contact's company, not the user's default company, so a contact in another allowed company yields a lead in that company (crm_mail_plugin/controllers/crm_client.py:48). (TEST) confirmed (crm_mail_plugin/tests/test_crm_mail_plugin.py:44-89).
- Listing partner leads uses the caller's normal record access; salesperson-only visibility follows crm rules (crm_mail_plugin/controllers/mail_plugin.py:29-30). Exact rule content: UNKNOWN — EVIDENCE INSUFFICIENT (crm security not read).
- Legacy routes by partner/lead id apply no extra check beyond the caller's rights (crm_mail_plugin/controllers/crm_client.py:29-30).
- The module declares no groups, access entries or record rules of its own (skeleton "groups": [], "rules": []).

## D. Handoffs to other modules
- mail_plugin: owns auth, contact lookup/creation, company enrichment, message logging (mail_plugin/controllers/mail_plugin.py:21-270).
- crm: owns lead object, rights, revenue and recurring fields (crm_mail_plugin/controllers/mail_plugin.py:29, 31).
- res.partner contacts: created/enriched by mail_plugin, consumed here.
- No accounting, sale, analytic or timesheet handoff.

## E. Configuration / defaults that change outcomes
- Recurring-revenue group of the calling user decides whether recurring fields appear in the contact panel (crm_mail_plugin/controllers/mail_plugin.py:31).
- Default page size of leads: 5 (crm_mail_plugin/controllers/mail_plugin.py:16).
- Add-in access key must exist per user: UNKNOWN — EVIDENCE INSUFFICIENT for provisioning steps.

## F. Effective extension path
- Extends mail_plugin's controller (crm_mail_plugin/controllers/mail_plugin.py:14) and crm lead model. Modules: mail_plugin, crm.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: duplicate-lead prevention, attachment handling into leads, lead assignment on creation.
- UNKNOWN — EVIDENCE INSUFFICIENT: external mailbox vendor integration behaviour (outside this module).

