# Source Map (candidate) — `fleet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `fleet` |
| Display name | Fleet |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ceb163617ae3a0c4` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/fleet/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`
- Direct dependents in 300-module list (3): `account_fleet`, `hr_fleet`, `stock_fleet`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Fleet / Manage your fleet and track car costs
- Inventory of user-facing artifacts (counts): menu items 21, views 28, window actions 5, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (14): `fleet.vehicle.send.mail` (Send mails to Drivers); `fleet.service.type` (Fleet Service Type); `fleet.vehicle.log.services` (Services for vehicles); `fleet.vehicle.state` (Vehicle Status); `fleet.vehicle.model` (Model of a vehicle); `fleet.vehicle.model.brand` (Brand of the vehicle); `fleet.vehicle.assignation.log` (Drivers history on a vehicle); `fleet.vehicle` (Vehicle); `fleet.vehicle.tag` (Vehicle Tag); `fleet.vehicle.log.contract` (Vehicle Contract); `fleet.vehicle.odometer` (Odometer log for a vehicle); `fleet.vehicle.model.category` (Category of the model); `fleet.vehicle.cost.report` (Fleet Analysis Report); `fleet.vehicle.odometer.report` (Fleet Odometer Analysis Report)
- Objects extended from other modules (6): `mail.composer.mixin`, `mail.thread`, `mail.activity.mixin`, `mail.activity.type`, `avatar.mixin`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `fleet.vehicle.log.services` ← Community: `account_fleet`, `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.assignation.log` ← Community: `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle` ← Community: `account_fleet`, `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.log.contract` ← Community: `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.odometer` ← Community: `hr_fleet`; open-license custom/third-party scanned: —
- `fleet.vehicle.model.category` ← Community: `stock_fleet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `mail.thread`, `mail.activity.mixin`, `mail.activity.type`, `avatar.mixin`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: `fleet.vehicle.log.services` → ['new', 'running', 'done', 'cancelled']; `fleet.vehicle.log.contract` → ['futur', 'open', 'expired', 'closed']
- Validation: 0 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Fleet: Generate contracts costs based on costs frequency every 1 days
- Security: groups declared 3 (`fleet_group_user`, `fleet_group_manager`, `base.default_user_group`); record rules 9 (of which company-scoped by text 5); access rows 24

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 55 of 55 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — fleet
Source revision: 19.0.post20260921 | Module: "Fleet" v0.1, category Human Resources/Fleet, application, LGPL-3 (fleet/__manifest__.py:4-7,51,58). Basis: static reading of models, security, cron/data, wizard, report, settings and tests (TEST).

## A. Capabilities and optionality
- A1. Vehicle fleet management: register cars and bikes, track drivers over time, odometer readings, service jobs, leasing/insurance contracts with expiry reminders, and cost analysis. fleet/__manifest__.py:9-25; fleet/models/fleet_vehicle.py:23-27
- A2. Optionality: standalone application, no auto_install; depends only on base and mail. Sample content (demo) is separate from real data. fleet/__manifest__.py:27-30,48,51
- A3. Real data seeded on install: 67 vehicle brands, four vehicle states (New Request, To Order, Registered, Downgraded), two contract types (Omnium, Leasing), a "Contract to Renew" activity type, a "Changed Driver" message type. fleet/data/fleet_cars_data.xml; fleet/data/fleet_data.xml:14-42; fleet/data/mail_activity_type_data.xml:4-9; fleet/data/mail_message_subtype_data.xml:4-10
- A4. Seeded only in demo data (so absent from a clean production database): the "Waiting List" state and the default service type used on new service jobs. fleet/data/fleet_demo.xml:24,54; fleet/models/fleet_vehicle_log_services.py:35; fleet/models/fleet_vehicle.py:372,416. Consequence for a clean database: the default service type is empty (raise-if-missing disabled) and waiting-list logic is skipped. UNKNOWN — EVIDENCE INSUFFICIENT whether other modules seed these.
- A5. Menus: Fleet (officers), Reporting and Configuration (administrators), settings entry (system administrators); service types, vehicle states, tags menus require developer mode. fleet/views/fleet_vehicle_model_views.xml:167-168; fleet/views/fleet_board_view.xml:105; fleet/views/res_config_settings_views.xml:33-35; fleet/views/fleet_vehicle_views.xml:505,551

## B. Objects, relationships, lifecycle
- B1. Brand -> Model -> Vehicle. Model defines type (car/bike), category, fuel, power, seats, emissions, range and a custom property list; vehicle copies these defaults from its model when model changes but each can be overridden. fleet/models/fleet_vehicle_model.py:32-71; fleet/models/fleet_vehicle.py:14-20,152-168
- B2. Vehicle: company, fleet manager, license plate, chassis number, driver, future driver, state, dates (order, registration, cancellation, first contract), odometer, values (catalog, purchase, residual), tags, custom properties; name is "brand/model/plate". fleet/models/fleet_vehicle.py:38-145,234-237
- B3. Driver history: an assignment log row (vehicle, driver, start date, end date) is created whenever a driver is set or changed; the previous driver triggers a to-do for the fleet manager (or the user) to enter the end date. fleet/models/fleet_vehicle.py:396-397,404-412,438-450; fleet/models/fleet_vehicle_assignation_log.py:12-15
- B4. Future driver / "plan to change car or bike": setting a future driver flags the other current vehicles of that driver and vehicle type as planned to change (unless the vehicle is in New Request or Waiting List); "accept driver change" swaps drivers, clears the flags. fleet/models/fleet_vehicle.py:368-392,414-429,452-466. (TEST) fleet/tests/test_access_rights.py:37-77
- B5. Odometer log: dated reading per vehicle; vehicle's "last odometer" is the maximum logged; writing a lower value than current is refused; setting the odometer value creates a log. fleet/models/fleet_vehicle_odometer.py:13-15; fleet/models/fleet_vehicle.py:247-264,401-402
- B6. Service log: vehicle, service type, cost, vendor, date, driver, odometer link, stage New/Running/Done/Cancelled. Emptying the odometer value is refused. fleet/models/fleet_vehicle_log_services.py:15-42,50-59
- B7. Contract log: vehicle, type, vendor, cost, start/expiry (default one year), recurring cost with frequency, included services, status New/Running/Expired/Cancelled; status follows dates automatically when dates are edited or by daily job. fleet/models/fleet_vehicle_log_contract.py:20-65,104-133
- B8. Archiving a vehicle archives its contracts and service logs. fleet/models/fleet_vehicle.py:431-433
- B9. Reminders on vehicle: "contract renewal due soon" (expiry within N days) and "overdue" (expired without a running/upcoming replacement); last contract status. fleet/models/fleet_vehicle.py:296-328,334-366. (TEST) fleet/tests/test_overdue.py:9-77

## C. Validations, automation, security, communication
- C1. Constraints: vehicle state names unique; tag names unique; category names unique. fleet/models/fleet_vehicle_state.py:16-19; fleet/models/fleet_vehicle_tag.py:14-17; fleet/models/fleet_vehicle_model_category.py:12-15
- C2. Daily job (named "Generate contracts costs", but it only manages contract status): creates a "Contract to Renew" to-do for the responsible user when a running contract expires within the alert window (once), then marks past-expiry contracts as expired, future-dated as new, and started ones as running. fleet/data/fleet_data.xml:4-12; fleet/models/fleet_vehicle_log_contract.py:135-168. No recurring-cost posting is performed in this module: UNKNOWN — EVIDENCE INSUFFICIENT whether other modules post costs.
- C3. Groups: "Officer: Manage all vehicles" (implies internal user) and "Administrator" (implies Officer); root and admin users are preset administrators. fleet/security/fleet_security.xml:8-20
- C4. Access: Officers read reference data (models, brands, categories, states, tags, service types) and service logs, fully edit vehicles, contracts, odometer, assignment logs; Administrators edit everything including reports and the send-mail wizard. fleet/security/ir.model.access.csv:2-25
- C5. Company scoping: global rules limit vehicles, contracts, services, odometer and the cost report to the user's allowed companies (or no company). Administrator rules grant unrestricted rights per model. fleet/security/fleet_security.xml:23-69
- C6. Fleet manager selection is limited to internal users of the vehicle's company who hold the officer group. fleet/models/fleet_vehicle.py:41-44
- C7. Email to drivers: administrator wizard posts a message on each vehicle addressed to its driver, optionally from a saved template; blocked if any driver has no email. fleet/wizard/fleet_vehicle_send_mail.py:29-57; fleet/security/ir.model.access.csv:24. Requires outgoing mail (mail).
- C8. Reports: cost analysis by month (services + contracts, split by cost type) and odometer analysis, both read-only database views; administrators only. fleet/report/fleet_report.py:9-27; fleet/report/odometer_report.py:9-11; fleet/security/ir.model.access.csv:23,25
- C9. Tracking on vehicle changes (plate, driver, state, CO2, values) with a dedicated "Changed Driver" notification type. fleet/models/fleet_vehicle.py:496-500

## D. Handoffs
- D1. Accounting bridge (auto-install with account): account_fleet. HR bridge (auto-install with hr, keeps driver history per employee; owns the alert-day parameter name): hr_fleet. Transport batches: stock_fleet. Manifests: account_fleet/__manifest__.py:8,16; hr_fleet/__manifest__.py:8,26; stock_fleet/__manifest__.py:8
- D2. Analytic name hook noted for accounting: fleet/models/fleet_vehicle.py:330-332
- D3. Messaging, to-dos, templates: mail. Partners as drivers and vendors: base (res.partner).

## E. Configuration that changes outcomes
- E1. Alert days before contract end (default 30), stored under the system parameter key hr_fleet.delay_alert_contract; editable in Fleet Settings by system administrators. fleet/models/res_config_settings.py:10; fleet/views/res_config_settings_views.xml:11-19
- E2. Odometer unit, power unit, range unit per vehicle; CO2 unit follows range unit. fleet/models/fleet_vehicle.py:92-103,143-145,239-245
- E3. Vehicle state list and default state "New Request". fleet/models/fleet_vehicle.py:30-32,78-81
- E4. Contract recurring-cost frequency default monthly. fleet/models/fleet_vehicle_log_contract.py:58-64

## F. Extension path
- account_fleet, hr_fleet, stock_fleet (Community). Other extenders outside Community tree: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: dashboard/kanban view behaviour and board layout (views not read line by line).
- UNKNOWN — EVIDENCE INSUFFICIENT: content of hr_fleet, account_fleet, stock_fleet beyond manifests.
- UNKNOWN — EVIDENCE INSUFFICIENT: cost-report figures for contracts with weekly frequency (query samples daily/monthly/yearly only; fleet/report/fleet_report.py).
- UNKNOWN — EVIDENCE INSUFFICIENT: the multi-company "visible to all" behaviour for vehicles without company beyond the rule domain (fleet/security/fleet_security.xml:46).

