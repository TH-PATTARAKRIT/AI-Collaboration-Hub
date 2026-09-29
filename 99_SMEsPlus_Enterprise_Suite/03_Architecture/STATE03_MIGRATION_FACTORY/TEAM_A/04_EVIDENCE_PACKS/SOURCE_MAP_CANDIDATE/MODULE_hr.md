# Source Map (candidate) — `hr`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr` |
| Display name | Employees |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `bf7754f632dd6a72` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `digest`, `phone_validation`, `resource_mail`, `web`
- Direct dependents in 300-module list (17): `hr_attendance`, `hr_calendar`, `hr_expense`, `hr_fleet`, `hr_gamification`, `hr_holidays`, `hr_homeworking`, `hr_hourly_cost`, `hr_livechat`, `hr_maintenance`, `hr_org_chart`, `hr_presence` … (+5)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `pos_hr`
- Custom / third-party modules that declare a dependency (name — license only) (11): `purchase_request_level_approve` — LGPL-3, `product_brand_sale` — AGPL-3, `19_contact_reference_sequence` — OPL-1, `purchase_request_level_approve_po` — LGPL-3, `19_bhpro_master_data` — OPL-1, `multi_level_approval_hr` — OPL-1, `base_location` — AGPL-3, `sale_order_level_approve` — LGPL-3, `purchase_request` — LGPL-3, `product_stock_equipment` — no-license, `contact_reference_sequence` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Centralize employee information
- Inventory of user-facing artifacts (counts): menu items 18, views 56, window actions 20, server actions 3, reports 1, mail templates 0, scheduled jobs 2, wizards 6, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (15): `hr.version.wizard` (Contract Template Wizard); `hr.departure.wizard` (Departure Wizard); `hr.bank.account.allocation.wizard.line` (Bank Account Allocation Line (Wizard)); `hr.bank.account.allocation.wizard` (Bank Account Allocation Wizard); `hr.departure.reason` (Departure Reason); `hr.contract.type` (Contract Type); `hr.version` (Version); `hr.employee.public` (Public Employee); `hr.work.location` (Work Location); `hr.employee.category` (Employee Category); `hr.department` (Department); `hr.job` (Job Position); `hr.payroll.structure.type` (Salary Structure Type); `hr.employee` (Employee); `hr.manager.department.report` (Hr Manager Department Report)
- Objects extended from other modules (20): `mail.activity.schedule`, `discuss.channel`, `mail.thread`, `mail.activity.mixin`, `mail.activity.plan`, `resource.calendar`, `base`, `mail.activity.plan.template`, `resource.calendar.leaves`, `resource.resource`, `ir.ui.menu`, `res.partner.bank`, `res.company`, `mail.thread.main.attachment`, `resource.mixin`, `avatar.mixin`, `mail.alias`, `res.users`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.departure.wizard` ← Community: `hr_fleet`, `hr_holidays`, `hr_maintenance`; open-license custom/third-party scanned: —
- `hr.version` ← Community: `hr_attendance`, `hr_holidays`, `hr_work_entry`, `hr_work_entry_holidays`, `l10n_fr_hr_work_entry_holidays`; open-license custom/third-party scanned: —
- `hr.employee.public` ← Community: `hr_attendance`, `hr_expense`, `hr_fleet`, `hr_gamification`, `hr_holidays`, `hr_homeworking`, `hr_maintenance`, `hr_org_chart`, `hr_presence`, `hr_skills` … (+2); open-license custom/third-party scanned: `base_location`, `purchase_request`, `purchase_request_level_approve`
- `hr.work.location` ← Community: `hr_homeworking`; open-license custom/third-party scanned: —
- `hr.department` ← Community: `hr_expense`, `hr_holidays`, `hr_recruitment`, `website_hr_recruitment`; open-license custom/third-party scanned: —
- `hr.job` ← Community: `hr_recruitment`, `hr_recruitment_skills`, `hr_recruitment_survey`, `hr_skills`, `website_hr_recruitment`; open-license custom/third-party scanned: —
- `hr.employee` ← Community: `hr_attendance`, `hr_expense`, `hr_fleet`, `hr_gamification`, `hr_holidays`, `hr_holidays_attendance`, `hr_holidays_homeworking`, `hr_homeworking`, `hr_homeworking_calendar`, `hr_hourly_cost` … (+12); open-license custom/third-party scanned: `base_location`, `product_brand_sale`, `purchase_request`, `purchase_request_level_approve`, `scgl_advance_expense_request`, `scgl_timesheet_grid`, `smesplus_advance_expense_request`
- `hr.manager.department.report` ← Community: `hr_holidays`, `hr_timesheet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.activity.schedule`, `discuss.channel`, `mail.thread`, `mail.activity.mixin`, `mail.activity.plan`, `resource.calendar`, `base`, `mail.activity.plan.template`, `resource.calendar.leaves`, `resource.resource`, `ir.ui.menu`, `res.partner.bank`, `res.company`, `mail.thread.main.attachment`, `resource.mixin`, `avatar.mixin`, `mail.alias`, `res.users`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 9 declarative constraint method(s), 6 database-level uniqueness/check declaration(s) (declared in code)
- Automation: HR Employee: Notify Expiring Contract or Work Permit every 1 days; HR Employee: Update Current Version every 1 days
- Security: groups declared 3 (`group_hr_user`, `group_hr_manager`, `base.default_user_group`); record rules 13 (of which company-scoped by text 5); access rows 26

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 72 of 76 source pointers resolve to an existing file and in-range line (4 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr (Employees)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/hr.json. Pointers `module/path:LINE`; (TEST) = test-derived.
Privacy note: this module holds the most sensitive personal data in the suite; the access notes below describe business-level visibility only.

## A. Capabilities / functions
- Application "Employees": central employee directory (identity, work info, manager/coach, department, job, work location, working hours), private/personal data, departure recording, onboarding/offboarding plans, presence status, company-wide employee settings (skeleton summary "Centralize employee information"; hr/models/hr_employee.py:26-52).
- Depends on base_setup, digest, phone_validation, resource_mail, web (skeleton depends); application=true; no auto_install. Core: employee, department, job position, work location, tags, departure reasons, contract types, activity plans, employee versions. Optional via company settings: advanced presence control (module hr_presence), skills (hr_skills), attendance-based presence (hr_attendance) (hr/models/res_config_settings.py:10-19).
- Structural change in this revision: the employee no longer carries contract data directly. Job, department, work address, working hours, employment type, private address/family data, contract dates and wage live on dated "versions" of the employee; the employee record reads/writes through its current version (hr/models/hr_employee.py:31-52,255-274,1427-1487). "Contract" is not a separate object: it is a period (start/end dates) shared by consecutive versions; salary structure type and wage are on versions (hr/models/hr_version.py:171-190,239-278).
- Public directory: every internal user sees a limited "public employee" card (name, job, department, work contact info, work location, manager-visible presence) instead of the full record (hr/models/hr_employee_public.py:10-60; skeleton access row for base.group_user read-only).
- Scheduled: daily notice of contracts and work permits about to expire (company notice periods default 7 and 60 days) and daily refresh of each employee's "current version" (hr/data/hr_data.xml:154-172; hr/models/res_company.py:15-16; hr/models/hr_employee.py:1177-1209,528-546).
- Onboarding and Offboarding plans (seeded activity plans) can be launched per employee, with responsible resolved to coach, manager or employee user, walking up the manager chain if a person has no user (hr/data/hr_data.xml:9-55; hr/models/mail_activity_plan_template.py:24-120). Employee creation posts a note suggesting an onboarding plan (hr/models/hr_employee.py:1414-1423).
- Departments auto-subscribe their members to selected discussion channels (hr/models/discuss_channel.py:11-35; hr/models/hr_employee.py:1404-1410,1462-1467).

## B. Business objects, relationships, lifecycle
- Employee: resource (name, calendar, time zone, active flag), optional user (one user per employee per company), company (required), work contact (a contact record), manager (parent) and coach (defaults to manager), department, job, tags, badge id and PIN (for kiosk/POS) (hr/models/hr_employee.py:56-118,195-213,246-253). Each employee always has at least one active version (hr/models/hr_version.py:294-300,302-311; (TEST) hr/tests/test_hr_employee.py:31).
- Version: dated snapshot of employee attributes with an effective date; unique per employee per date among active ones; the version in force today is the "current" version, refreshed daily (hr/models/hr_version.py:197-207,393-410; hr/models/hr_employee.py:528-546); (TEST) (hr/tests/test_hr_version.py:376-397). Creating a new version copies the version in force at that date and applies the changes; contract dates are carried and synchronised across versions of the same contract (hr/models/hr_employee.py:571-643; hr/models/hr_version.py:302-365); (TEST) (hr/tests/test_hr_version.py:146-350).
- Contract rules: at most one contract period running at a time per employee (overlap blocked); an end date requires a start date; start not after end; a new contract requires the previous one to be closed first (hr/models/hr_version.py:197-206,239-283); (TEST) (hr/tests/test_hr_version.py:17-95). A single-version employee's version date follows the contract start (hr/models/hr_version.py:322-333; (TEST) hr/tests/test_hr_version.py:819).
- Contract template: values can be pre-filled from a template (whitelist of copied fields) via wizard or on creation (hr/models/hr_version.py:285-293,443-460; hr/wizard/hr_contract_template_wizard.py).
- Employee <-> user: linking a user copies user picture, time zone and contact into the employee; conversely user name/email/picture/time zone changes flow into the linked employees (hr/models/hr_employee.py:1340-1349; hr/models/res_users.py:195-240); creating a user with "create employee" creates the employee (hr/models/res_users.py:164-181). Actions to create users from employees exist (hr/models/hr_employee.py:980-1100). (TEST) (hr/tests/test_hr_employee.py:121-146,229-272,321-465).
- Work contact: created automatically if missing; work phone/email mirror the contact only when that contact belongs to a single employee (hr/models/hr_employee.py:801-846); contacts linked to employees cannot be deleted, only archived (hr/models/res_partner.py:71-82).
- Department: hierarchy (no cycles), manager, company inherited from parent; changing the manager moves the manager relation of members who reported to the old manager (hr/models/hr_department.py:115-147).
- Job position: unique per department and company; target recruitment >= 0; forecast = current + target (hr/models/hr_job.py:35-58).
- Departure: archiving one employee opens the departure wizard (reason, date, description, optional contract end date, optional removal of related user); confirmed departure records reason/date on the employee, can end the current contract on the departure date, and can archive the linked user only if all that user's employees are covered (hr/models/hr_employee.py:1508-1537; hr/wizard/hr_departure_wizard.py:61-125); the wizard's own archiving of employees/users happens only under a termination context, otherwise the employee was already archived by the archive action that opened it (hr/wizard/hr_departure_wizard.py:96-112); departure date cannot precede the current contract start (hr/wizard/hr_departure_wizard.py:74-78). Archiving clears manager/coach links pointing to the archived person and other modules add theirs (hr/models/hr_employee.py:1493-1531). Unarchiving clears departure data (hr/models/hr_employee.py:1499-1506). (TEST) (hr/tests/test_hr_employee.py:507-526).
- Bank accounts and salary split: employees can hold several bank accounts; each has a percentage or fixed amount and a sequence, kept in a salary distribution structure; percentages must total exactly 100; a bank account can be marked trusted for outgoing payments; changing the work contact detaches trust and moves the accounts (hr/models/hr_employee.py:137-160,289-352,1429-1443,1925-1975; hr/wizard/hr_bank_account_wizard.py:40-63).
- Presence status: present (system login, optionally email or IP or attendance per company setting), absent, off-hours, archived; other modules (attendance, time off) refine it (hr/models/hr_employee.py:847-906; hr/models/res_company.py:12-14).

## C. Validations, automation, security, multi-company
- Badge id unique and alphanumeric up to 18 characters; PIN digits only; user unique per company; salary distribution rules above (hr/models/hr_employee.py:246-252,333-352,1305-1317).
- Groups: "Officer: Manage all employees" (HR Officer, implies internal user) and "Administrator" (HR Manager, root and admin) (hr/security/hr_security.xml:10-25).
- Model-level access: only HR Officers (and read-only system administrators) can read the full employee record; all internal users read the limited public card; departments, jobs, tags readable by everyone, editable by officers; work locations editable by administrators; versions by officers and administrators; contract types, departure reasons by officers; activity plans/templates and payroll structure types by administrators (skeleton access rows; hr/security/ir.model.access.csv).
- Business-level visibility of sensitive fields: on the employee record all personal data (private address/phone/email, birthday, place of birth, nationality, ID/passport/social security numbers, marital status, spouse, children, emergency contact, visa and work permit, bank accounts, licence and ID copies, car plate, departure reasons, badge/PIN) is restricted to HR Officers; contract dates, wage, salary structure and contract type are restricted to HR Administrators (hr/models/hr_employee.py:127-176,181-193,210-217; hr/models/hr_version.py:63-190). Birthday can be shown to all employees only if HR ticks a per-employee flag (hr/models/hr_employee.py:134-136,940-946). Non-officers reading employees are served from the public card; requests for private fields raise access errors (hr/models/hr_employee.py:1109-1176,1232-1267). (TEST) (hr/tests/test_self_user_access.py:131-206; hr/tests/test_payroll_fields_access.py:10-101).
- Record rules on employees and public cards: visible if in the user's selected companies (or no company), or if the user is that employee, that employee's manager, or the manager of the viewer (so an employee can always see their manager and reports across companies) (hr/security/hr_security.xml:28-54); (TEST) (hr/tests/test_multi_company.py:83-100). Departments and jobs scoped by company; versions by company plus full access for HR Administrators; contract types, departure reasons, payroll structure types by country of the user's companies (hr/security/hr_security.xml:39-60,76-122).
- Employee bank accounts (contacts of employees) are hidden from normal internal users and fully visible to HR Officers (hr/security/hr_security.xml:62-74).
- Self-service: any user can edit a limited list of own contact/personal fields (private address, private phone/email, emergency contact, bank accounts of user, work phone/email, job title, work location, badge, PIN, visa expiry, notes), and readable own employee links, from "My Preferences"; edits by users to such fields notify the employee's HR Responsible (hr/models/res_users.py:14-54,120-127,195-240). Which fields a user can see in their own preferences is elevated for that one screen only (hr/models/res_users.py:143-158).
- Changing an employee's company shows a warning recommending a new employee instead, to avoid losing contracts/leaves (hr/models/hr_employee.py:1539-1544).
- The many-to-many-to-employee assignment now needs read access on employees; the module supplies a helper so other users' assignments keep working (hr/models/hr_mixin.py:9-30; hr/models/hr_employee.py:1149-1157).
- Automation on create: work contact, generated avatar, department channel subscription, onboarding suggestion (hr/models/hr_employee.py:1381-1425).

## D. Accounting / payroll / analytic handoffs
- No accounting entries. Payroll is not in Community: the module stores wage, salary structure type (with default working schedule by country), HR Responsible, bank accounts and salary distribution for consumption by a payroll module (UNKNOWN — EVIDENCE INSUFFICIENT: consumer not in this tree; hr/models/hr_payroll_structure_type.py skeleton fields; hr/models/hr_version.py:178-190,535-550). Work entries/time valuation: hr_work_entry and hr_work_entry_holidays (dependants present in tree; not read).
- Expense reimbursement partner and bank are read from employee work contact and primary bank account by hr_expense (see hr_expense note).
- Employee cost per hour: hr_hourly_cost (dependant present; not read).

## E. Configuration / defaults that change outcomes
- Company: default working hours; contract expiry notice 7 days; work permit notice 60 days; presence control by login (default on), email count, IP list, attendance (hr/models/res_company.py:12-16; hr/models/res_config_settings.py:7-19).
- Seeded data (noupdate): one department, Onboarding/Offboarding plans, departure reasons Fired/Resigned/Retired (protected from deletion), permanent/temporary contract types, and employee tags (hr/data/hr_data.xml:5-80; hr/models/hr_departure_reason.py:8-30).
- Version defaults: employee type "employee", marital "single", distance unit km, HR Responsible defaults to the creating user (hr/models/hr_version.py:107-113,127-133,192-195).
- Company-level custom employee properties definition (hr/models/res_company.py:14).

## F. Effective extension path
- Direct dependants include: hr_attendance, hr_holidays, hr_expense, hr_fleet, hr_gamification, hr_calendar, hr_presence, hr_homeworking, hr_hourly_cost, hr_livechat, hr_org_chart, hr_recruitment, hr_timesheet, hr_maintenance, hr_skills, hr_work_entry, pos_hr, mail_bot_hr (manifest grep of `'hr'`).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: views and menus, badge report, employee import templates, digest tips, scenario data, user-creation-from-employee notification edge cases, frontend JS.

