# Source Map (candidate) — `hr_recruitment`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_recruitment` |
| Display name | Recruitment |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6a0a55775393c793` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_recruitment/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `calendar`, `utm`, `attachment_indexation`, `web_tour`, `digest`
- Direct dependents in 300-module list (4): `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_recruitment_survey`, `website_hr_recruitment`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Recruitment / Track your recruitment pipeline
- Inventory of user-facing artifacts (counts): menu items 27, views 46, window actions 27, server actions 2, reports 0, mail templates 4, scheduled jobs 0, wizards 6, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (12): `applicant.send.mail` (Send mails to applicants); `job.add.applicants` (Add applicants to a job); `talent.pool.add.applicants` (Add applicants to talent pool); `applicant.get.refuse.reason` (Get Refuse Reason); `hr.recruitment.degree` (Applicant Degree); `hr.applicant.category` (Category of applicant); `hr.recruitment.stage` (Recruitment Stages); `hr.talent.pool` (Talent Pool); `hr.applicant` (Applicant); `hr.recruitment.source` (Source of Applicants); `hr.applicant.refuse.reason` (Refuse Reason of Applicant); `hr.job.platform` (Job Platforms)
- Objects extended from other modules (26): `mail.composer.mixin`, `mail.activity.schedule`, `digest.digest`, `mail.activity.plan`, `ir.attachment`, `hr.department`, `mail.alias.mixin`, `hr.job`, `mail.activity.mixin`, `utm.source`, `ir.ui.menu`, `calendar.event`, `res.company`, `hr.employee`, `mail.thread`, `res.users`, `res.config.settings`, `utm.campaign`, `mail.thread.cc`, `mail.thread.main.attachment`, `mail.thread.blacklist`, `mail.thread.phone`, `utm.mixin`, `mail.tracking.duration.mixin`, `utm.source.mixin` … (+1)
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.applicant` ← Community: `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_recruitment_survey`, `website_hr_recruitment`; open-license custom/third-party scanned: —
- `hr.recruitment.source` ← Community: `website_hr_recruitment`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `mail.activity.schedule`, `digest.digest`, `mail.activity.plan`, `ir.attachment`, `hr.department`, `mail.alias.mixin`, `hr.job`, `mail.activity.mixin`, `utm.source`, `ir.ui.menu`, `calendar.event`, `res.company`, `hr.employee`, `mail.thread`, `res.users`, `res.config.settings`, `utm.campaign`, `mail.thread.cc`, `mail.thread.main.attachment`, `mail.thread.blacklist`, `mail.thread.phone`, `utm.mixin`, `mail.tracking.duration.mixin`, `utm.source.mixin` … (+1)

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 4 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 6 (`group_hr_recruitment_interviewer`, `group_hr_recruitment_user`, `group_hr_recruitment_manager`, `group_applicant_cv_display`, `base.group_user`, `base.default_user_group`); record rules 8 (of which company-scoped by text 1); access rows 31

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

