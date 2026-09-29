# Source Map (candidate) — `hr_fleet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_fleet` |
| Display name | Fleet History |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `02b269c24bb6bb37` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_fleet/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `fleet`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / Get history of driven cars by employees
- Inventory of user-facing artifacts (counts): menu items 0, views 16, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (10): `hr.departure.wizard`, `fleet.vehicle.log.services`, `mail.activity.plan.template`, `ir.attachment`, `fleet.vehicle.assignation.log`, `fleet.vehicle`, `hr.employee`, `hr.employee.public`, `fleet.vehicle.log.contract`, `fleet.vehicle.odometer`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.departure.wizard`, `fleet.vehicle.log.services`, `mail.activity.plan.template`, `ir.attachment`, `fleet.vehicle.assignation.log`, `fleet.vehicle`, `hr.employee`, `hr.employee.public`, `fleet.vehicle.log.contract`, `fleet.vehicle.odometer`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 32 of 34 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_fleet (Fleet History)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/hr_fleet.json. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities / functions
- Bridge that turns the fleet's "driver" (a contact) into a real employee link, so vehicles, service logs, contracts, odometer readings and assignment history can be seen per employee ("Fleet History": history of driven cars by employees) (hr_fleet/__manifest__.py:4-8).
- Conditional: auto-installs when hr and fleet are both present; not an application (hr_fleet/__manifest__.py:8,26).
- Employee record: "Cars" history button, private/company plate search, and mobility card number (hr_fleet/models/employee.py:11-17,19-29,31-42).
- Vehicle record: employee-driver and future-employee-driver fields kept in sync with the fleet's driver/future-driver contacts (hr_fleet/models/fleet_vehicle.py:10-24,64-118).
- Assignment log: shows the employee behind each assignment and allows attaching documents to a log (hr_fleet/models/fleet_vehicle_assignation_log.py:9-40).
- Service log and contract log show the driver employee as purchaser (hr_fleet/models/fleet_vehicle_log_services.py:10-25; hr_fleet/models/fleet_vehicle_log_contract.py:10-13); odometer shows the driver employee read-only (hr_fleet/models/fleet_vehicle_odometer.py:10-13).
- Off-boarding: departure wizard option "Release Company Car" (default on only for fleet users) (hr_fleet/wizard/hr_departure_wizard.py:9-15) and a seeded off-boarding activity "Take Back Fleet" assigned to the vehicle's fleet manager (hr_fleet/data/hr_fleet_data.xml:5-9).

## B. Business objects, relationships, lifecycle
- Link rule: employee <-> vehicle goes through the employee's "work contact" (address book contact); the employee in the vehicle's company sharing that contact is chosen (hr_fleet/models/fleet_vehicle.py:26-38). If several employees match on write from contact side, no employee is set (only assigned when exactly one match) (hr_fleet/models/fleet_vehicle.py:71-81).
- Setting the employee on a vehicle sets the driver contact to that employee's work contact, and vice versa (hr_fleet/models/fleet_vehicle.py:64-100); same for the future driver (hr_fleet/models/fleet_vehicle.py:83-100). Fleet's own driver-change acceptance flow (future driver becomes driver) is owned by fleet; (TEST) after changing the employee's user (hence contact), accepting the driver change makes the new contact the driver (hr_fleet/tests/test_hr_fleet_driver.py:44-52).
- Changing the driver employee unsubscribes the previous driver (contact and user) from vehicle notifications (hr_fleet/models/fleet_vehicle.py:110-117).
- If an employee's work contact changes, the vehicle driver/future driver contacts follow (hr_fleet/models/employee.py:62-82).
- Mobility card is copied from the employee to vehicles they drive, recomputed when the card number changes (hr_fleet/models/fleet_vehicle.py:54-62; hr_fleet/models/employee.py:84-88).
- Departure release: on registering a departure with the option ticked, every open assignment of the leaving person (no end date, or ending after the departure date) is closed at the departure date, and vehicles where they are the driver lose the driver (hr_fleet/wizard/hr_departure_wizard.py:17-30). Future-driver assignments are not cleared here (no code for it).
- Fleet-manager off-boarding activity: the responsible is the manager of the employee's first vehicle; if the vehicle has no manager, the activity goes to the person scheduling it with a warning; if no vehicle, an error is shown (hr_fleet/models/mail_activity_plan_template.py:22-36); (TEST) (hr_fleet/tests/test_mail_activity_plan.py:39-80).

## C. Validations, automation, security, multi-company
- Block: an employee's work contact cannot be removed while a vehicle is linked to that employee (hr_fleet/models/employee.py:52-60).
- Fleet Manager responsible type only allowed on Employee plans (hr_fleet/models/mail_activity_plan_template.py:15-20).
- Multi-company: the driver employee is chosen per (contact, vehicle company); the employee field on vehicles is domain-limited to employees with no company or the vehicle's company (hr_fleet/models/fleet_vehicle.py:11-24,37); (TEST) same contact used by employees in two companies resolves to the employee of the vehicle's company (hr_fleet/tests/test_hr_fleet_driver.py:69-88).
- Access: HR Officers get read-only access to vehicles (hr_fleet/security/ir.model.access.csv:2), further limited by a record rule to vehicles that currently have (or will have) an employee driver, so officers see no unassigned vehicles (hr_fleet/security/hr_fleet_security.xml:4-13).
- Field-level privacy: number of cars only for Fleet Managers; vehicle list on employee for Fleet Managers and HR Officers; plate search for HR Officers; mobility card visible to Fleet Users, and read-only on the public employee card (hr_fleet/models/employee.py:11,14,16,17,95). Business implication: vehicle/plate details tied to individuals are not visible to ordinary employees.
- Some lookups use elevated rights to resolve employees from contacts, so assigning a driver does not require HR rights (hr_fleet/models/fleet_vehicle.py:68,76,87,95; hr_fleet/models/employee.py:55,71,85).

## D. Accounting / payroll / analytic handoffs
- None in this module. Vehicle costs (services, contracts) are fleet-owned; bills-to-vehicle linkage is in account_fleet; expense re-billing to vehicle, if any, UNKNOWN — EVIDENCE INSUFFICIENT.
- Payroll-related car benefit (company car in contract) is not here: UNKNOWN — EVIDENCE INSUFFICIENT (not in Community hr_fleet).

## E. Configuration / defaults that change outcomes
- "Release Company Car" default depends on the user holding fleet user rights (hr_fleet/wizard/hr_departure_wizard.py:9).
- Employee's work contact must exist for the link to work; a new employee with a user but no contact is not attached to unassigned cars (TEST: hr_fleet/tests/test_hr_fleet_driver.py:54-67).

## F. Effective extension path
- Extends: hr (employee, public employee, departure wizard, activity plan), fleet (vehicle, logs, odometer). Related: account_fleet (bills), hr_expense_... none confirmed.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: menu placement/visibility of views, demo data content, hr_fleet view attributes beyond model behaviours.

