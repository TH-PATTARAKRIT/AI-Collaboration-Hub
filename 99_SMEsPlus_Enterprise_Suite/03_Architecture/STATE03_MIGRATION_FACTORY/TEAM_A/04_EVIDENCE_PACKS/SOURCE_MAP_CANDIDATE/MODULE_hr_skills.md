# Source Map (candidate) — `hr_skills`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_skills` |
| Display name | Skills Management |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f6a8579e869c5832` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_skills/` |
| auto_install / application | True / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr`
- Direct dependents in 300-module list (5): `hr_recruitment_skills`, `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`, `project_hr_skills`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Manage skills, knowledge and resume of your employees
- Inventory of user-facing artifacts (counts): menu items 9, views 36, window actions 8, server actions 2, reports 1, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

## 4. Business objects (neutral names) and configuration
- Objects introduced (10): `hr.employee.cv.wizard` (Print Resume); `hr.skill.type` (Skill Type); `hr.job.skill` (Skills for job positions); `hr.resume.line.type` (Type of a resume line); `hr.individual.skill.mixin` (Skill level); `hr.resume.line` (Resume line of an employee); `hr.skill` (Skill); `hr.employee.skill` (Skill level for employee); `hr.skill.level` (Skill Level); `report.hr_skills.report_employee_cv` (Employee Resume)
- Objects extended from other modules (4): `hr.employee.public`, `hr.job`, `hr.employee`, `resource.resource`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.individual.skill.mixin` ← Community: `hr_recruitment_skills`; open-license custom/third-party scanned: —
- `hr.resume.line` ← Community: `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `hr.employee.public`, `hr.job`, `hr.employee`, `resource.resource`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 5 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Skills: Add an activity to employees with missing or expiring certifications every 1 days
- Security: groups declared 0 (—); record rules 11 (of which company-scoped by text 1); access rows 20

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

