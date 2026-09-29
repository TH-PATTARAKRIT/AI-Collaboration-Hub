# Source Map (candidate) — `maintenance`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `maintenance` |
| Display name | Maintenance |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `105af9b6ac7ff31c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/maintenance/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (2): `hr_maintenance`, `stock_maintenance`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (2): `equipment_sequence` — no-license, `product_stock_equipment` — no-license

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Maintenance / Track equipment and manage maintenance requests
- Inventory of user-facing artifacts (counts): menu items 17, views 25, window actions 14, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (6): `maintenance.stage` (Maintenance Stage); `maintenance.equipment.category` (Maintenance Equipment Category); `maintenance.mixin` (Maintenance Maintained Item); `maintenance.equipment` (Maintenance Equipment); `maintenance.request` (Maintenance Request); `maintenance.team` (Maintenance Teams)
- Objects extended from other modules (5): `mail.thread`, `mail.activity.mixin`, `mail.thread.cc`, `mail.alias.mixin`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 3 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `maintenance.equipment` ← Community: `hr_maintenance`, `stock_maintenance`; open-license custom/third-party scanned: —
- `maintenance.request` ← Community: `hr_maintenance`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `mail.activity.mixin`, `mail.thread.cc`, `mail.alias.mixin`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`group_equipment_manager`); record rules 8 (of which company-scoped by text 4); access rows 10

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 16 of 16 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: maintenance
Source revision: 19.0.post20260921 | Path base: odoo/addons | Method: static source read (no execution)

## A. Capabilities
- Equipment register plus maintenance-request pipeline; flagged as an application, depends only on mail (maintenance/__manifest__.py:7,10,25). Not auto_install. Optional application.
- Equipment: vendor, model, serial, cost, warranty and scrap dates, owner, assigned date, category-specific custom properties (maintenance/models/maintenance.py:130-146).
- Equipment categories with default responsible person and property definition (maintenance.py:23-47).
- Maintenance requests, corrective or preventive, with priority, scheduled start/end, duration, instructions (PDF / slide link / text) (maintenance.py:207-256).
- Recurring preventive requests: on completion a follow-up copy is made in the first stage, moved forward by the interval, repeating forever or until an end date (maintenance.py:244-256, 335-347). (TEST) maintenance/tests/test_maintenance.py:90 and :210.
- Reliability indicators per equipment: MTBF, MTTR, latest failure date, estimated next failure, computed only from done corrective requests (maintenance.py:94-101).
- Maintenance teams with e-mail alias that creates requests by mail (maintenance.py:404-407, 449-455); dashboard counters (429-442).
- Activity scheduling for the assignee when a scheduled date exists (maintenance.py:373-388).
- Cancel = archive flag on the request (also disables recurrence); reopen resets to first stage (maintenance.py:258-265; button labels views/maintenance_views.xml:87-88).
- Optional add-on switch "Custom Maintenance Worksheets" (module_maintenance_worksheet) shown in settings (maintenance/models/res_config_settings.py:10; views/res_config_settings_views.xml:12-17). The worksheet module itself was not found in this Community tree (UNKNOWN — EVIDENCE INSUFFICIENT).

## B. Objects, states and gates
- maintenance.stage (name, sequence, fold, "done" flag) is the request state list, not a fixed enum (maintenance.py:10-20). Seeded stages: New Request, In Progress, Repaired (done), Scrap (done) (maintenance/data/maintenance_data.xml:6-27, noupdate).
- maintenance.request -> equipment (restrict delete), team (required), stage, technician; category is stored from equipment (maintenance.py:214-234).
- Second, independent state: kanban state normal / blocked / ready; reset to "normal" on any stage change (maintenance.py:223-224, 332-333).
- Entering a done stage: close date set today; leaving a done stage: close date cleared; the request's pending activity is completed (maintenance.py:351-355). On create a done-stage record gets a close date and a non-done one has it cleared (322-325).
- Equipment archiving via active flag (maintenance.py:131); equipment cannot be deleted while requests point to it (ondelete restrict, line 216).
- Team default for a request: a team of the current company, else any team (maintenance.py:200-205); equipment's team overrides when set (293-299).
- Technician default comes from equipment technician, else category responsible (maintenance.py:301-307).
- Chatter subtypes: request created, status changed, equipment assigned, category-level followers (maintenance/data/mail_message_subtype_data.xml:5-40). Seed team "Internal Maintenance" (line 41-43). Activity type "Maintenance Request" (data/mail_activity_type_data.xml:5-10).

## C. Validations, security, multi-company
- Scheduled end may not precede scheduled start (maintenance.py:267-271); end defaults to start + 1 hour (273-276); repeat interval >= 1 (287-291); serial number must be unique across equipment (152-155).
- A category with equipment or requests cannot be deleted (maintenance.py:62-66).
- Groups: "Equipment Manager" (implies internal user) (maintenance/security/maintenance.xml:9-16). ACL: internal users read equipment/category/stage/team, full on requests; managers full (maintenance/security/ir.model.access.csv:2-10); managers also manage activity types (line 11).
- Record rules: internal users see requests they own, are assigned to, or follow; equipment they follow; managers see all (maintenance.xml:21-47).
- Multi-company rules on request, equipment, team, category (company in allowed companies or empty) (maintenance.xml:49-71). Model-level auto company check on request, equipment and mixin (maintenance.py:71,114,186); team and technician are cleared when they do not fit the record company (88-92, 293-307). (TEST) maintenance/tests/test_maintenance_multicompany.py:12.
- Menus: main entries for managers and internal users; configuration for managers; stage menu only in developer mode (maintenance_views.xml:936-1040).

## D. Handoffs (owner in brackets)
- Messaging and activities [mail]: threads, followers, activity scheduling/feedback, e-mail alias (maintenance.py:112,183,406).
- Employee/department equipment assignment [hr_maintenance]: extends equipment and request (hr_maintenance/models/equipment.py:7,82).
- Stock location / serial-number lookup [stock_maintenance]: extends equipment (stock_maintenance/models/maintenance.py:7).
- No accounting entry, purchase, or inventory move is created by this module; cost is an informational field (maintenance.py:140). No cron found in this module (skeleton crons empty).

## E. Configuration that changes outcomes
- Stage list with "done" flags (drives close date, MTBF/MTTR, recurrence, open counts): maintenance.py:20, 97, 335, 351.
- Request repeat settings (interval, unit, forever/until) and preventive type (maintenance.py:244-256, 309-313: recurrence auto-cleared unless preventive).
- Team alias and member list; category default responsible; equipment effective date (start of MTBF calculation, maintenance.py:76).
- Settings switch for worksheets (see A).

## F. Effective extension path (module names only)
- Extend maintenance.equipment: hr_maintenance, stock_maintenance. Extend maintenance.request: hr_maintenance. Depend on maintenance: hr_maintenance, stock_maintenance.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: menu entries OEE and Losses Analysis (views/maintenance_views.xml:988-1000) carry no action in this module; which module, if any, fills them was not established. A request-reporting menu does exist (maintenance_views.xml:1007-1010).
- UNKNOWN — EVIDENCE INSUFFICIENT: portal or website access to requests; e-mail alias security settings beyond defaults from mail.
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side calendar behaviour (only test files seen, maintenance/tests/test_calendar_with_recurrence.py:9,41).

