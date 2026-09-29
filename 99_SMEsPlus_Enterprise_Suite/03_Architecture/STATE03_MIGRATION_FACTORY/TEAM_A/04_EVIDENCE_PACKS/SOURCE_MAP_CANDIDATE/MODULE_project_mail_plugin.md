# Source Map (candidate) — `project_mail_plugin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_mail_plugin` |
| Display name | Project Mail Plugin |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e606f9cd9dab0b27` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_mail_plugin/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project`, `mail_plugin`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Integrate your inbox with projects
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 3
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
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 17 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — project_mail_plugin (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Lets users of the external mail add-in (Outlook-style mailbox plugin) turn an email into a project task and log email content as internal notes on tasks (project_mail_plugin/__manifest__.py:9-10).
- Depends on project and mail_plugin; auto_install is True, so it installs automatically when both are present (project_mail_plugin/__manifest__.py:15-20).
- Conditional exposure: the "tasks" section is sent to the add-in only if the current user may create tasks; otherwise it behaves as if project were not installed (project_mail_plugin/controllers/mail_plugin.py:22-29).
- Provides an action that opens a task form in edit mode, used by the plugin to redirect the user after creation (project_mail_plugin/views/project_task_views.xml:3-9).

## B. Business objects, relationships, lifecycle
- No new stored objects or models; only web endpoints and one window action (module listing: controllers, views, tests only).
- Contact panel data: for a known partner, up to 5 of that partner's tasks (id, name, project name), limited to tasks whose project the user can read; also a flag telling whether the user may create projects. For no partner, an empty task list (project_mail_plugin/controllers/mail_plugin.py:31-47).
- Project search: name contains search term, limit default 5; returns id, name, customer name, company (project_mail_plugin/controllers/project_client.py:7-23).
- Task creation from email: requires an existing partner and existing project (otherwise returns an error code); subject becomes the task name (fallback "Task for <partner>"), email body becomes the description, the requesting user is assigned; created in the partner's company context (project_mail_plugin/controllers/project_client.py:25-45).
- Project creation from the plugin: creates a project with only a name (project_mail_plugin/controllers/project_client.py:47-50).
- Logging of email content is allowed for the task model when the user can create tasks; plugin translations for this module are whitelisted under the same condition (project_mail_plugin/controllers/mail_plugin.py:51-61).

## C. Validations, automation, security, multi-company
- Endpoints use the plugin-specific authentication mode (auth 'outlook') and permissive cross-origin access (project_mail_plugin/controllers/project_client.py:7, :25, :47).
- Project search reads with the caller's rights; result fields are then read with elevated rights (project_mail_plugin/controllers/project_client.py:13, :22) — visibility of project/partner names is therefore not limited by record rules after the search.
- Task and project creation run under the caller's rights, so ordinary create access rules of project apply (project_mail_plugin/controllers/project_client.py:37, :49). Existence checks do not test read access to the chosen project/partner: UNKNOWN — EVIDENCE INSUFFICIENT on further limits.
- Multi-company: task created with the partner's company context; project search returns each project's company id (project_mail_plugin/controllers/project_client.py:20, :37).
- No access CSV, record rules or crons in this module.

## D. Handoffs (module ownership)
- Task/project records, stages, access: project. Mailbox add-in protocol, contact data, note logging whitelist, authentication mode: mail_plugin. Partner records: base/contacts. No accounting, inventory or sales handoff.

## E. Configuration/defaults that change outcomes
- Default result limit 5 for project search and partner tasks (project_mail_plugin/controllers/project_client.py:8; project_mail_plugin/controllers/mail_plugin.py:35).
- User language affects returned project names (TEST: project_mail_plugin/tests/test_controller.py:11-51).
- Which project a task lands in is chosen by the plugin user; no default project logic here.

## F. Extension path (grep of _inherit)
- Controller override of mail_plugin.MailPluginController (project_mail_plugin/controllers/mail_plugin.py:13). No model _inherit. No other module manifest lists project_mail_plugin as a dependency (grep of manifests).

## G. Not verified
- Add-in (client side) behaviour and what fields the add-in shows: UNKNOWN — EVIDENCE INSUFFICIENT.
- How mail_plugin authentication maps API keys to users: UNKNOWN — EVIDENCE INSUFFICIENT (mail_plugin not read).

