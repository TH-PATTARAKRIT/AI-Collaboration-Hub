# Source Map (candidate) — `hr_recruitment_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_recruitment_sms` |
| Display name | Recruitment - SMS |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a4ad0411b42f3d57` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_recruitment_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_recruitment`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Recruitment / Mass mailing sms to job applicants
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `hr.applicant`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.applicant`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 13 of 14 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_recruitment_sms (Recruitment - SMS)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_recruitment_sms.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests (none exist in this module).

## A. Capabilities / functions
- Bridge between Recruitment and SMS: adds a "Send SMS" action to applicants, for mass texting from list or kanban selections (hr_recruitment_sms/__manifest__.py:5-6, 8; hr_recruitment_sms/views/hr_applicant_views.xml:3-11).
- Depends on hr_recruitment and sms; `auto_install` true (hr_recruitment_sms/__manifest__.py:8, 12).
- The action is bound to the applicant model in list and kanban views only, not the form (hr_recruitment_sms/views/hr_applicant_views.xml:7-8); sequence 2 orders it in the menu (hr_recruitment_sms/views/hr_applicant_views.xml:6).
- Opens the standard SMS composer in mass mode with the selected applicants as recipients and "keep a log on each record" turned on (hr_recruitment_sms/models/hr_applicant.py:9-16).
- No new fields, models, data, menus, settings or security in this module.

## B. Business objects, relationships, lifecycle
- Object touched: applicant (owned by hr_recruitment) and SMS composer (owned by sms) (hr_recruitment_sms/models/hr_applicant.py:7, 10).
- Phone number used is the applicant's contact phone; applicant model uses the phone mixin and declares that field as the SMS number field (hr_recruitment/models/hr_applicant.py:30, 598-601).
- Lifecycle: no state gating in this module (e.g. archived/refused applicants are not excluded by this code): UNKNOWN — EVIDENCE INSUFFICIENT for behaviour on refused or archived records.
- Logging: each sent message is recorded on the applicant's chatter because mass logging is enabled by default (hr_recruitment_sms/models/hr_applicant.py:13).

## C. Validations, automation, security, multi-company
- No validations, automation, groups or record rules here (manifest data lists only the view file, hr_recruitment_sms/__manifest__.py:9-11).
- Rights follow recruitment (who sees applicants) and sms (who may compose/send): UNKNOWN — EVIDENCE INSUFFICIENT for the resulting group requirement.
- Opt-out / blacklist handling and invalid-number handling are owned by sms and the phone mixin: UNKNOWN — EVIDENCE INSUFFICIENT.
- Company scoping: none added.

## D. Handoffs to other modules
- hr_recruitment: owns applicants and their phone field (hr_recruitment/models/hr_applicant.py:598-601).
- sms: owns composer, templates, sending, credits/gateway (hr_recruitment_sms/models/hr_applicant.py:10).

## E. Configuration / defaults that change outcomes
- Default composition mode "mass"; log kept on records (hr_recruitment_sms/models/hr_applicant.py:12-13).
- Delivery depends on SMS gateway configuration and credits: UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path
- Modules involved: hr_recruitment, sms. Extension via the composer action and the applicant phone-number field list.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the composer allows template selection for the applicant model (template ownership in sms).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for applicants without phone number.

