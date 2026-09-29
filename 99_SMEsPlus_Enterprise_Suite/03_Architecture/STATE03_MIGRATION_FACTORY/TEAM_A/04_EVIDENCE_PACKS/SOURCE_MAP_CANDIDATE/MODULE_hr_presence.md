# Source Map (candidate) — `hr_presence`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_presence` |
| Display name | Employee Presence Control |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2f920b5b0761df9c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_presence/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `hr_holidays`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / —
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 5, reports 0, mail templates 1, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (6): `hr.employee.public`, `res.company`, `hr.employee`, `res.config.settings`, `res.users.log`, `ir.websocket`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.employee.public`, `res.company`, `hr.employee`, `res.config.settings`, `res.users.log`, `ir.websocket`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: HR Presence: cron every 1 hours
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 43 of 44 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_presence (Employee Presence Control)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_presence.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests (none exist in this module).
Note: not an auto-install bridge (no auto_install key, hr_presence/__manifest__.py:3-35); it is an optional module toggled from HR settings (hr/views/res_config_settings_views.xml:38, 47 reference `module_hr_presence`). It bridges hr, hr_holidays and sms (hr_presence/__manifest__.py:18).

## A. Capabilities / functions
- Detects whether employees are actually at work, using company-selected signals: IP address of the session, number of emails sent today, plus (from hr) login status (hr_presence/__manifest__.py:7-16; hr/models/res_company.py:9-15).
- Lets HR managers act on unjustified absences: mark present/absent, add a log note, send an SMS, or create an "Unplanned Absence" time off for one or several employees (hr_presence/views/hr_employee_views.xml:18-76; hr_presence/models/hr_employee.py:79-132).
- Adds search filters "Absent", "Off-Hours" and group-by "Presence/Absence" (grouping for HR managers only) (hr_presence/views/hr_employee_views.xml:8-14).
- Provides a mail template "Unexpected Absence" and an SMS template "Presence Reminder" (hr_presence/data/mail_template_data.xml:4-22; hr_presence/data/sms_data.xml:4-8).
- Conditional: the automatic checks only run when the company enables email- or IP-based control; otherwise presence is left to the base logic (hr_presence/models/hr_employee.py:182-183, 45, 61). Enabling either switch in settings triggers an immediate check (hr_presence/models/res_config_settings.py:7-12).

## B. Business objects, relationships, lifecycle
- Employee gets flags: email-sent today, IP-connected today, manually set present, manually set presence, and a stored display state (Off-Hours / Present / Absent) (hr_presence/models/hr_employee.py:16-27). Public employee record mirrors them (hr_presence/models/hr_employee_public.py:9-17).
- Login log gets an IP address field (hr_presence/models/res_users_log.py:9); an IP record is created at most once per user/IP/day when an internal user's session reports presence (hr_presence/models/ir_websocket.py:14-31).
- Company stores the timestamp of the last presence computation (hr_presence/models/res_company.py:10).
- Lifecycle: hourly job resets the flags for the company's employees, evaluates IP, then email (only those not already confirmed), stamps the compute time, and copies the resulting state into the stored display state (hr_presence/data/ir_cron.xml:4-13; hr_presence/models/hr_employee.py:29-77).
- State rule: manual override wins; else if control is on and the employee is working now and flagged (email/IP/manual) -> present; if working now, absent per time off and not flagged -> absent; else off-hours (hr_presence/models/hr_employee.py:172-192). The "present" branch also requires the last computation to be from the same calendar day (hr_presence/models/hr_employee.py:184-186).
- Setting the stored state to present through a write also flags manual presence (hr_presence/models/hr_employee.py:107-110).

## C. Validations, automation, security, multi-company
- Only HR managers may set present/absent, send SMS or add the log note; others get a rights error (hr_presence/models/hr_employee.py:93-94, 139-140, 163-164). The "Create a Time Off" action has no such explicit check in this module: UNKNOWN — EVIDENCE INSUFFICIENT for who can use it beyond leave rights.
- Automation: hourly scheduled job run as the system user, always recreated on upgrade check (forcecreate), loaded once (noupdate) (hr_presence/data/ir_cron.xml:3-13).
- Security: HR managers get full rights on SMS templates (hr_presence/security/ir.model.access.csv:2), restricted by a rule so create/edit/delete applies only to templates whose target is employees; read is not limited by the rule (hr_presence/security/sms_security.xml:3-9).
- Company scoping: the job checks employees of the current company only (hr_presence/models/hr_employee.py:31-32); thresholds and IP list are per company (hr/models/res_company.py:9-15). Because the job uses the environment company, behaviour across multiple companies in one run: UNKNOWN — EVIDENCE INSUFFICIENT.
- Email-based check counts messages authored by the employee's partner since start of day against the company threshold (hr_presence/models/hr_employee.py:61-72).

## D. Handoffs to other modules
- hr: owns employee, presence state base logic, working-now list, company presence switches and threshold/IP settings (hr/models/hr_employee.py:102, 847; hr/models/res_company.py:9-15).
- hr_holidays: owns the "absent today" flag and time-off / multi-employee leave generation wizard (hr_presence/models/hr_employee.py:117, 188).
- sms: owns SMS composer and templates (hr_presence/models/hr_employee.py:143, 156; hr_presence/security/sms_security.xml:5).
- mail / bus (websocket): message counts and session presence pings (hr_presence/models/hr_employee.py:65; hr_presence/models/ir_websocket.py:12-15).
- Front-end: list/form views and action menus expose the presence actions (hr_presence/static/src/ files listed under hr_presence/static/src/views and search).

## E. Configuration / defaults that change outcomes
- Company switches: based on user status (default on), emails sent (threshold count), IP address (list of valid IPs), attendances (hr/models/res_company.py:9-15). This module handles IP and email; the attendance and login variants live elsewhere (hr/models/hr_employee.py:880).
- SMS action uses the module's SMS template when found; otherwise falls back to a built-in message text (hr_presence/models/hr_employee.py:145-151). Observation: the code looks up template id `sms_template_presence` while the shipped data defines `sms_template_data_hr_presence` (hr_presence/data/sms_data.xml:4); a search of the Community tree found no record with the looked-up id, so the fallback text may apply: UNKNOWN — EVIDENCE INSUFFICIENT on runtime outcome.
- The mail template is described as sent manually; no code in this module sends it: UNKNOWN — EVIDENCE INSUFFICIENT (hr_presence/data/mail_template_data.xml:12).
- SMS is composed in mass mode with log kept, using the employee's mobile number (hr_presence/models/hr_employee.py:143).

## F. Effective extension path
- Modules involved: hr (presence base), hr_holidays (absence), sms, mail/bus. Extension via presence state computation, the hourly check, server actions bound to employee views.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: accuracy of IP detection behind proxies; only the remote address is used (hr_presence/models/ir_websocket.py:22).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end view behaviour (static JS not read in detail).
- UNKNOWN — EVIDENCE INSUFFICIENT: privacy/legal aspects of monitoring.

