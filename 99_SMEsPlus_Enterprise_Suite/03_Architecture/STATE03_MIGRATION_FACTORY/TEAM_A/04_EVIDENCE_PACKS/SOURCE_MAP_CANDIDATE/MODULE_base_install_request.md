# Source Map (candidate) — `base_install_request`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_install_request` |
| Display name | Base - Module Install Request |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e9a7ff25e7943193` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_install_request/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 1, server actions 0, reports 0, mail templates 1, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `base.module.install.request` (Module Activation Request); `base.module.install.review` (Module Activation Review)
- Objects extended from other modules (1): `ir.module.module`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.module.module`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 6

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 25 of 25 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — base_install_request
Source revision: 19.0.post20260921 | Module: "Base - Module Install Request", category Hidden, LGPL-3 (base_install_request/__manifest__.py:5-6,21). Basis: static reading; no tests in this module.

## A. Capabilities and optionality
- A1. Lets an ordinary internal user ask administrators to activate (install) an app that is not yet installed, with a free-text justification. base_install_request/__manifest__.py:8-11; base_install_request/wizard/base_module_install_request.py:8-20
- A2. Lets an administrator, from the emailed link, review which apps would be installed and confirm the installation in one step. base_install_request/wizard/base_module_install_request.py:47-87; base_install_request/wizard/base_module_install_request_views.xml:23-45
- A3. Conditional: auto_install on, depends only on mail; present on any database that has mail. base_install_request/__manifest__.py:7,12
- A4. Optional start-up behaviour: after installation, if the server was started with the "default productivity apps" option, it also installs HR, Mass Mailing, Project and Survey (plus Enterprise-only appointment, knowledge, planning, sign if present) when they are uninstalled. base_install_request/__init__.py:10-21; base_install_request/__manifest__.py:22

## B. Objects and lifecycle
- B1. Two temporary (wizard) records only, no permanent business data: an "activation request" (module, requesting user, recipients, message) and an "activation review" (module, dependent apps list). base_install_request/wizard/base_module_install_request.py:8-20,47-59
- B2. Flow: user sees a "Request Access" button on an uninstalled app card -> request form with recipients (all system administrators) and reason -> one email per administrator with a "Review Request" link -> administrator opens review screen -> "Install App" performs immediate installation and returns to home. base_install_request/views/ir_module_module_views.xml:9; base_install_request/wizard/base_module_install_request.py:24-44,81-87; base_install_request/data/mail_template_data.xml:23
- B3. Review lists the chosen module and any of its prerequisite modules flagged as applications; it refuses if nothing chosen or the module is already installed. base_install_request/wizard/base_module_install_request.py:70-79

## C. Validations, security, external effects
- C1. Request button is shown only if the app is uninstalled, is not a paid/"to buy" app, and the viewer is not a system administrator. base_install_request/views/ir_module_module_views.xml:9
- C2. Access: internal users may create request wizards (no delete); only system administrators may use the review wizard; internal users additionally get read-only access to module catalogue, category, dependency and exclusion records so the app cards can display. base_install_request/security/ir.model.access.csv:2-7
- C3. The module removes all group restrictions from the "Apps" management menu entry (base.menu_management), so it is not limited to administrators. base_install_request/views/ir_module_module_views.xml:14-16. The exact resulting audience is UNKNOWN — EVIDENCE INSUFFICIENT (base menu definition not read).
- C4. Recipients are computed as every user in the administrator group, regardless of company. base_install_request/wizard/base_module_install_request.py:22-25
- C5. Emails are sent immediately (not queued), from the requester's address, in each recipient's language, and auto-deleted after sending. base_install_request/wizard/base_module_install_request.py:32-35; base_install_request/data/mail_template_data.xml:9,34-35
- C6. Installing an app is a heavy, database-wide action; the administrator screen is the only place that runs it here. Outgoing mail server is required for the request to reach anyone (mail infrastructure owned by mail). UNKNOWN — EVIDENCE INSUFFICIENT what happens if mail sending fails.
- C7. No tests. No company scoping in this module.

## D. Handoffs
- D1. Module catalogue, installation engine, Apps menu: base. base_install_request/models/ir_module_module.py:8-19; base_install_request/views/ir_module_module_views.xml:6,14
- D2. Email template, layout and delivery: mail. base_install_request/wizard/base_module_install_request.py:28-35
- D3. Auto-installed productivity apps (only under start-up option): hr, mass_mailing, project, survey (Community). base_install_request/__init__.py:16

## E. Configuration that changes outcomes
- E1. Server option "default productivity apps" triggers A4 at install time only. base_install_request/__init__.py:11-12
- E2. Requester's company colors (secondary/primary email colors) style the email button. base_install_request/data/mail_template_data.xml:23

## F. Extension path
- Only base (ir.module.module) and mail (templates) are touched. Modules that reference this module: UNKNOWN — EVIDENCE INSUFFICIENT (no dependents searched beyond its own directory; one grep found none referencing the review action).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the request wizard is reachable from screens other than the app card view.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when multiple requests for the same module are sent (no de-duplication found).
- UNKNOWN — EVIDENCE INSUFFICIENT: Enterprise app availability (not in Community tree).

