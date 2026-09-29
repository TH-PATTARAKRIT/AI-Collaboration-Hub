# Source Map (candidate) — `website_project`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_project` |
| Display name | Online Task Submission |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `aa745c0af8c8434b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_project/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `project`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Add a task suggestion form to your website
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `website.page`, `project.task`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `website.page`, `project.task`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 29 of 30 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_project (Online Task Submission)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_project.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: creates tasks in the Project app from a form published on the website, built with the website form builder (website_project/__manifest__.py:7-10).

## A. Capabilities / functions
- Conditional: depends on website and project with `auto_install` (website_project/__manifest__.py:12,19); appears automatically when both are installed.
- Core: registers the task model as a website-form target "Create a Task", allowed for website submission, with the task description as the default text field (website_project/data/website_project_data.xml:3-8).
- Core: whitelists which task fields the public form may fill: name, customer name, phone, company name, description, project, task properties (website_project/data/website_project_data.xml:10-21).
- Core: form-builder preset for "Create a Task": full name, phone, email (custom), company, subject, question text, attachment, and a required project selector (non-template projects only); success page `/your-task-has-been-submitted` (website_project/static/src/js/website_project_editor.js:4-49).
- Core: "Task submitted" thank-you page, published but not indexed, showing the new task number and a link to the portal task for logged-in users when the project is visible to employees/portal (website_project/views/project_portal_project_task_template.xml:3-35).
- Core: that page is never cached (website_project/models/website_page.py:9-13).
- Core: portal task and project pages use the record name as additional page title (website_project/views/project_portal_project_task_template.xml:37-41; website_project/views/project_portal_project_project_template.xml:3-7).
- Two stored convenience fields on tasks: customer name and company name, mirrored from the contact but editable (website_project/models/project_task.py:8-9).

## B. Business objects, relationships, lifecycle
- Website submission -> task (project.task, owned by project) -> optional contact match by email -> comment logged on the task (website_project/controllers/main.py:12-45, 47-69).
- Contact resolution: a known website visitor's contact wins; else if the submitted email matches an existing contact, that contact is set (name/phone/company entries moved into the "other information" text rather than overwriting the contact); else the task is left without a contact and the email is stored as the requester email and copy address, with typed name/phone/company kept on the task (website_project/controllers/main.py:15-18, 49-68).
- Task description is rebuilt: the entered text, a heading "Other Information" with extra entries, and submission metadata; the same text is logged as a comment on the task (website_project/controllers/main.py:26-44). (TEST) resulting description content (website_project/tests/test_project_portal_access.py:37-59).
- Lifecycle after creation is entirely project's (stages, assignees). The form sets the assignees to empty so the automation bot is not auto-assigned (website_project/controllers/main.py:19-20).

## C. Validations, automation, security, multi-company
- Public visitors may submit (form endpoint is public); the task is created with elevated rights through the website form base controller (website_project/controllers/main.py:11-22; website/controllers/form.py:63,263). (TEST) a public user can submit a task (website_project/tests/test_project_portal_access.py:37-59).
- Only the whitelisted fields are accepted from a public submission (website_project/data/website_project_data.xml:10-21). The requester email is handled as a separate, non-whitelisted key added by this module's data extraction (website_project/controllers/main.py:49-51).
- Existing contacts are never renamed or altered by a submission (TEST) (website_project/tests/test_project_portal_access.py:61-82). A project's own contact is not changed (TEST) (website_project/tests/test_project_portal_access.py:82).
- Anti-spam: the standard website form captcha applies (website/controllers/form.py:31); no extra checks here.
- Which project a public visitor may target: the form field lists projects; whether hidden/private projects are excluded from public submission: UNKNOWN — EVIDENCE INSUFFICIENT.
- Portal comment posting by a portal user creates a message authored by that user (TEST) (website_project/tests/test_project_portal_access.py:14-34).
- No access-control rows or record rules of its own; company scoping follows the project's company. Multi-website behaviour: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- project (owner): task, project, portal pages, stages; website (owner): form controller, form builder, pages, visitors (website_project/controllers/main.py:7,15).
- mail: partner-from-email matching and chatter log (website_project/controllers/main.py:41,50).
- Project sharing/portal templates modified here belong to project (`project.portal_my_task`, `project.portal_my_project`) (website_project/views/project_portal_project_task_template.xml:37).

## E. Configuration / defaults that change outcomes
- Choice of project in the form and of visible fields is made in the page builder (website_project/static/src/js/website_project_editor.js:39-49).
- Portal link on the thank-you page depends on project privacy (employees or portal) and the visitor being logged in (website_project/views/project_portal_project_task_template.xml:16).

## F. Effective extension path (module names only)
- project.task extended by: hr_timesheet, project_hr_skills, project_sms, project_timesheet_holidays, project_todo, sale_project, sale_timesheet, website_project. website.page extended by: website, website_hr_recruitment, website_livechat, website_project, website_sale.
- Website form controller extended by: website_crm, website_crm_iap_reveal, website_hr_recruitment, website_mass_mailing, website_project, website_sale.

## G. Not verified
- Attachment handling and file limits: UNKNOWN — EVIDENCE INSUFFICIENT.
- Notification emails to project followers on submission: UNKNOWN — EVIDENCE INSUFFICIENT.

