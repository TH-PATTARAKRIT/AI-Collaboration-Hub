# Source Map (candidate) — `survey`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `survey` |
| Display name | Surveys |
| Manifest version | 3.7 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `639e58b8349cc66a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/survey/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `auth_signup`, `http_routing`, `mail`, `web_tour`, `gamification`
- Direct dependents in 300-module list (4): `hr_recruitment_survey`, `hr_skills_survey`, `survey_crm`, `website_slides_survey`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Surveys / Send your surveys or share them live.
- Inventory of user-facing artifacts (counts): menu items 7, views 23, window actions 6, server actions 1, reports 1, mail templates 2, scheduled jobs 0, wizards 1, web routes 22
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (6): `survey.invite` (Survey Invitation Wizard); `survey.survey` (Survey); `survey.question` (Survey Question); `survey.question.answer` (Survey Label); `survey.user_input` (Survey User Input); `survey.user_input.line` (Survey User Input Line)
- Objects extended from other modules (8): `mail.composer.mixin`, `res.lang`, `ir.http`, `gamification.badge`, `mail.thread`, `mail.activity.mixin`, `gamification.challenge`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `survey.invite` ← Community: `hr_recruitment_survey`; open-license custom/third-party scanned: —
- `survey.survey` ← Community: `hr_recruitment_survey`, `hr_skills_survey`, `survey_crm`, `website_slides_survey`; open-license custom/third-party scanned: —
- `survey.question` ← Community: `survey_crm`; open-license custom/third-party scanned: —
- `survey.question.answer` ← Community: `survey_crm`; open-license custom/third-party scanned: —
- `survey.user_input` ← Community: `hr_recruitment_survey`, `hr_skills_survey`, `survey_crm`, `website_slides_survey`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `res.lang`, `ir.http`, `gamification.badge`, `mail.thread`, `mail.activity.mixin`, `gamification.challenge`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `survey.user_input` → ['new', 'in_progress', 'done']
- Validation: 5 declarative constraint method(s), 21 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`base.default_user_group`); record rules 12 (of which company-scoped by text 0); access rows 22

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

