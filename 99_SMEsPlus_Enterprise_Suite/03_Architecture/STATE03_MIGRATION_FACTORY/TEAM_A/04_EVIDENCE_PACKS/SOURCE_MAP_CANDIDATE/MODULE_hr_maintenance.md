# Source Map (candidate) — `hr_maintenance`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_maintenance` |
| Display name | Maintenance - HR |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c04d249a1ebead1f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_maintenance/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `maintenance`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / Equipment, Assets, Internal Hardware, Allocation Tracking
- Inventory of user-facing artifacts (counts): menu items 0, views 10, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `hr.departure.wizard`, `maintenance.equipment`, `maintenance.request`, `hr.employee.public`, `hr.employee`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.departure.wizard`, `maintenance.equipment`, `maintenance.request`, `hr.employee.public`, `hr.employee`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`hr.group_hr_user`); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 38 of 39 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_maintenance (Maintenance - HR bridge)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_maintenance.json. Pointers are `module/path:LINE`; (TEST) = derived from tests. This module ships no tests.

## A. Capabilities / functions
- Bridge that lets company equipment be allocated to an employee or a department, ties maintenance requests to employees, and frees equipment when an employee leaves. Depends on hr and maintenance (hr_maintenance/__manifest__.py:10).
- Conditional-on-install: auto_install true (hr_maintenance/__manifest__.py:19), added automatically when both parents are present. Not an application; no settings.
- Equipment gains "Used By" (Department / Employee / Other, required, default Employee), an assigned employee, an assigned department and an assignment date (hr_maintenance/models/equipment.py:9-19). Form shows employee or department depending on the choice (hr_maintenance/views/maintenance_views.xml:86-88); list, kanban and search views show and group by employee/department and redefine "assigned"/"available" as having an employee or department (hr_maintenance/views/maintenance_views.xml:63-72, 98-104, 114-116).
- Maintenance requests gain an employee (defaults to the current user's employee) shown as "Created By" and used for the "My Maintenances" filter (hr_maintenance/models/equipment.py:84-87; hr_maintenance/views/maintenance_views.xml:10-18, 27-33).
- Employee form (officers/equipment managers) and employee public profile get an "Equipment" stat button (hr_maintenance/views/hr_views.xml:9-18, 27-37; counts hr_maintenance/models/hr_employee.py:7-13, hr_maintenance/models/hr_employee_public.py:9).
- Employee departure wizard gets an "Equipment" checkbox (default on) that clears the employee's equipment when the departure is registered (hr_maintenance/wizard/hr_departure_wizard.py:9-15; view hr_maintenance/wizard/hr_departure_wizard_views.xml:8-15; wizard base hr/wizard/hr_departure_wizard.py:7-9).
- Incoming-email requests: when the sender matches a user login, the request's employee is set (see C caveat) (hr_maintenance/models/equipment.py:115-126).

## B. Business objects, relationships, lifecycle
- Equipment -> Employee (many-to-one, tracked) and Equipment -> Department (many-to-one, tracked); Employee -> Equipment (one-to-many, officers only) (hr_maintenance/models/equipment.py:9-12; hr_maintenance/models/hr_employee.py:7).
- Maintenance request -> Employee (requester); equipment choice on a request is limited to equipment assigned to that employee or unassigned (hr_maintenance/models/equipment.py:87-89).
- Allocation lifecycle: choosing "Used By = Employee" clears the department; "Department" clears the employee; "Other" keeps whichever value is present; every recompute stamps today's date as the assignment date (hr_maintenance/models/equipment.py:30-42). Fields stay editable after computing (readonly false: :9-12, :19).
- Equipment owner (responsible user) is derived: the employee's user for employee allocation, the department manager's user for department allocation, otherwise the current user at compute time (hr_maintenance/models/equipment.py:21-28). For requests the owner is the requester's user only when the equipment is allocated to an employee, else empty (hr_maintenance/models/equipment.py:91-97).
- Departure: equipment is released only if the departure completes and the checkbox is on (hr_maintenance/wizard/hr_departure_wizard.py:12-14).
- Maintenance request stages (done flag, kanban state) belong to maintenance: stage has a "done" marker (maintenance/models/maintenance.py:20) and requests carry a stage and a kanban state (maintenance/models/maintenance.py:218-223).

## C. Validations, automation, security, multi-company
- Automation: assigning equipment to an employee or department subscribes the employee's user (and department manager's user) as followers, on create and on write (hr_maintenance/models/equipment.py:44-57, 59-72); assignment change posts with the "assigned" notification subtype (hr_maintenance/models/equipment.py:74-78). Requests subscribe the employee's user (hr_maintenance/models/equipment.py:99-113).
- Security escalation: HR Officers are made implied members of the Equipment Manager group, so HR officers can manage equipment (hr_maintenance/security/equipment.xml:3-6). Base ACL from maintenance: internal users read equipment, managers write (maintenance/security/ir.model.access.csv:2-3); requests are writable by all internal users (maintenance/security/ir.model.access.csv:4) but record rules limit users to requests they own, follow or are assigned; equipment is visible to followers only, managers see all (maintenance/security/maintenance.xml:21-31, 35-46). Consequence: the follower subscription above is what makes allocated equipment visible to the employee/department manager.
- Multi-company: rules from maintenance filter requests/equipment/teams/categories by company (maintenance/security/maintenance.xml:49-70). This module adds no company field or rule; the employee list button on the employee form respects the viewer's equipment rights (hr_maintenance/views/hr_views.xml:12 group restriction).
- Caveat on email-created requests: the employee is taken from the current session user's employee rather than the sender's, and only if a user login matches the sender address (hr_maintenance/models/equipment.py:120-125). Practical effect for inbound mail depends on which user context the mail gateway runs under: UNKNOWN — EVIDENCE INSUFFICIENT.
- Departure clears the equipment link via the employee's list; no guard against active maintenance requests (none found in the cited code).

## D. Accounting / payroll / analytic handoffs
- None. No asset accounting, depreciation, payroll or analytic link in this module. (Equipment cost/warranty data belongs to maintenance; asset accounting is not a Community bridge here: UNKNOWN — EVIDENCE INSUFFICIENT.)

## E. Configuration / defaults that change outcomes
- Default "Used By" is Employee (hr_maintenance/models/equipment.py:15-17).
- Departure wizard checkbox default on (hr_maintenance/wizard/hr_departure_wizard.py:9).
- Request employee default = current user's employee (hr_maintenance/models/equipment.py:84-87).
- Group implication is unconditional once installed (hr_maintenance/security/equipment.xml:5).

## F. Effective extension path (module names only)
- Extends: maintenance (equipment, request), hr (employee, public employee, departure wizard), views of maintenance/hr. Manifest dependents of hr_maintenance: none found.

## G. Not verified
- Whether re-computation on unrelated saves re-stamps assignment date beyond the changes of "Used By" (dependency is only on the Used By choice: hr_maintenance/models/equipment.py:30): UNKNOWN — EVIDENCE INSUFFICIENT for edge cases.
- Inbound e-mail employee attribution: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; nothing stated as a universal rule.

