# Source Map (candidate) — `project_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_sms` |
| Display name | Project - SMS |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d7c7b9ad2a6653c8` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Send text messages when project/task stage move
- Inventory of user-facing artifacts (counts): menu items 0, views 6, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `project.project.stage`, `project.task.type`, `project.task`, `project.project`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `project.project.stage`, `project.task.type`, `project.task`, `project.project`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 28 of 28 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — project_sms (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Sends an SMS to the customer automatically when a project or a task enters a stage that has an SMS template configured (project_sms/__manifest__.py:6-7; project_sms/models/project_stage.py:10-12; project_sms/models/project_task_type.py:10-12).
- Also offers a manual "Send SMS" bulk action on projects (list/kanban, project managers only) and on tasks (list/kanban/form) (project_sms/views/project_project_views.xml:3-16; project_sms/views/project_task_views.xml:3-15).
- Depends on project and sms; auto_install True, so installed automatically when both are present (project_sms/__manifest__.py:10, :19).
- Conditional: sending occurs only if a stage has a template AND the record has a customer (partner) (project_sms/models/project_project.py:12; project_sms/models/project_task.py:12).

## B. Business objects, relationships, lifecycle
- Project Stage and Task Stage each gain an optional SMS template link; project-stage templates are restricted to templates for projects, task-stage templates to templates for tasks (project_sms/models/project_stage.py:10-12; project_sms/models/project_task_type.py:10-12).
- Trigger points: on project creation and on task creation (initial stage counts) and whenever the stage value is written (project_sms/models/project_project.py:18-28; project_sms/models/project_task.py:18-30).
- Task templates (is_template records) never send SMS (project_sms/models/project_task.py:12).
- SMS goes to the record's customer partner and is logged on the record (message with template) (project_sms/models/project_project.py:13-16; project_sms/models/project_task.py:13-16).
- No state machine of its own; the stage sequence is owned by project.

## C. Validations, automation, security, multi-company
- Sending is executed with elevated rights because the SMS template model is protected; explicit code comment for tasks and sudo on projects (project_sms/models/project_task.py:27-29; project_sms/models/project_project.py:11). Message is posted with the caller's environment for projects (project_sms/models/project_project.py:13).
- Tests confirm that a portal user and a project user can change task stage and trigger the SMS template (TEST: project_sms/tests/test_project_sharing.py:38, :69).
- Access: project managers get full rights on SMS templates (project_sms/security/ir.model.access.csv:2), narrowed by a record rule to templates whose model is project task or project; read excluded from the rule (project_sms/security/project_sms_security.xml:3-9). Migration to version 1.1 rewrites the older rule domain (project_sms/upgrades/1.1/pre-migrate.py:4-13).
- Manual project SMS action restricted to project manager group (project_sms/views/project_project_views.xml:6).
- No cron. Multi-company: no company logic in this module — depends on base project/sms record rules; UNKNOWN — EVIDENCE INSUFFICIENT.
- Failure handling when customer has no mobile number/SMS credits: UNKNOWN — EVIDENCE INSUFFICIENT (sms module).

## D. Handoffs (module ownership)
- SMS composition, delivery, IAP credit, templates: sms. Project/stage/task records: project. Customer partner data: base. No accounting, inventory or sales handoff.

## E. Configuration/defaults that change outcomes
- Whether an SMS is sent depends solely on the stage's SMS template setting (project_sms/models/project_stage.py:10-12; project_sms/models/project_task_type.py:10-12).
- Template selector on stage form/list is optional-hidden in list, always in form (project_sms/views/project_stage_views.xml:9, :20). Bulk SMS composer defaults to mass mode with log kept (project_sms/views/project_project_views.xml:9-13).

## F. Extension path (grep of _inherit)
- Extends project.project, project.project.stage, project.task, project.task.type (project_sms/models/*.py). No other module manifest lists project_sms as a dependency (grep of manifests).

## G. Not verified
- Whether a repeated write of the same stage re-sends SMS: UNKNOWN — EVIDENCE INSUFFICIENT (code triggers whenever stage_id key is written).
- Task stage view integration (project_sms/views/project_task_type_views.xml): UNKNOWN — EVIDENCE INSUFFICIENT (not read).

