# Source Map (candidate) — `crm_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `crm_sms` |
| Display name | SMS in CRM |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6fb9134bcabb54ee` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/crm_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `crm`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_crm_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / Add SMS capabilities to CRM
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 19 of 20 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: crm_sms (SMS in CRM)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/crm_sms.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge module: adds "send SMS" actions to CRM leads/opportunities; depends on crm and sms only (crm_sms/__manifest__.py:9).
- Conditional: `auto_install` true, so it activates automatically once both crm and sms are installed; not a standalone application (crm_sms/__manifest__.py:16).
- Two SMS composer actions bound to the lead model in the "Action" menu: one for list/kanban selections (bulk, "mass" mode, keeps a log on each lead) and one for the single-record form ("comment" mode on the open record) (crm_sms/views/crm_lead_views.xml:4-28).
- List view of opportunities gains an "SMS" button in the header and, next to the email-compose button, a per-row SMS button hidden for lost opportunities (crm_sms/views/crm_lead_views.xml:35-40).
- The reporting variant of the opportunity list has that per-row SMS button removed (crm_sms/views/crm_lead_views.xml:44-50).
- The module defines no Python models or fields of its own (crm_sms/__init__.py:1-2; skeleton "models": []). Phone handling on leads comes from crm's phone mixin (crm/models/crm_lead.py:90).

## B. Business objects, relationships, lifecycle
- Objects touched: lead/opportunity (owned by crm) and SMS composer (owned by sms). Composer receives the selected lead ids as default recipients (crm_sms/views/crm_lead_views.xml:12, 24).
- Lifecycle gate: per-row SMS button is not offered on lost opportunities (crm_sms/views/crm_lead_views.xml:39). Whether bulk or form actions also block lost leads: UNKNOWN — EVIDENCE INSUFFICIENT.
- (TEST) Clearing or changing a lead's phone keeps the sanitized number in step (empty phone gives empty sanitized number) (crm_sms/tests/test_crm_lead.py:11-26).

## C. Validations, automation, security, multi-company
- Sale managers get full create/edit/delete on SMS templates via an access entry (crm_sms/security/ir.model.access.csv:2), narrowed by a rule so that this extra power applies only to templates targeting leads or partners (crm_sms/security/sms_security.xml:3-9). The rule turns off the read perm, so it does not restrict reading (crm_sms/security/sms_security.xml:8).
- Baseline in sms: all internal users read templates only; system administrators have full rights (sms/security/ir.model.access.csv:5-6).
- Rule file is loaded once and not overwritten on upgrade (noupdate) (crm_sms/security/sms_security.xml:2).
- No company field or company rule added; multi-company scoping of leads follows crm and of templates follows sms: UNKNOWN — EVIDENCE INSUFFICIENT for combined behaviour.
- Consent / blacklist checks before sending: UNKNOWN — EVIDENCE INSUFFICIENT (handled, if at all, inside sms composer, not read here).

## D. Handoffs to other modules
- crm: owns leads, list views the buttons are injected into (crm_sms/views/crm_lead_views.xml:32, 46).
- sms: owns composer, templates, sending, credit/IAP gateway, template access baseline (sms/security/ir.model.access.csv:4-11).
- sales_team: owns the sale manager group used for template rights (crm_sms/security/ir.model.access.csv:2).
- No accounting, analytic, sale or timesheet handoff.

## E. Configuration / defaults that change outcomes
- Bulk action defaults to mass mode with logging on; form action defaults to single comment mode (crm_sms/views/crm_lead_views.xml:9-13, 22-25).
- Effective sending depends on sms gateway configuration and credits: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path
- Views extend crm's opportunity list views; rights extend sms templates. Modules involved: crm, sms, sales_team.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: composer validation, opt-out handling, error path for leads without phone.
- UNKNOWN — EVIDENCE INSUFFICIENT: any effect of the module on lead lifecycle beyond UI entry points.

