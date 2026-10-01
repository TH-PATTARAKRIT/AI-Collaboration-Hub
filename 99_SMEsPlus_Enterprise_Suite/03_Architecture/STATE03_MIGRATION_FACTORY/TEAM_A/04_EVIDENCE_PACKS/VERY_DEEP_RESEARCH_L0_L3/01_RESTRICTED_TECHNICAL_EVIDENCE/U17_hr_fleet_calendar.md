# U17 hr_fleet_calendar — RESTRICTED TECHNICAL EVIDENCE

> **RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**
> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**

| Field | Value |
|---|---|
| Unit | U17 `hr_fleet_calendar` (VDR L2/L3 worker output) |
| Modules owned (33) | `hr`, `hr_attendance`, `hr_holidays`, `hr_holidays_attendance`, `hr_holidays_homeworking`, `hr_homeworking`, `hr_homeworking_calendar`, `hr_calendar`, `hr_hourly_cost`, `hr_org_chart`, `hr_presence`, `hr_work_entry`, `hr_work_entry_holidays`, `hr_skills`, `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`, `hr_recruitment`, `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_recruitment_survey`, `hr_gamification`, `hr_livechat`, `hr_maintenance`, `hr_fleet`, `fleet`, `maintenance`, `gamification`, `gamification_sale_crm`, `calendar`, `calendar_sms`, `mail_bot_hr`, `resource_mail` |
| Source revision | `19.0.post20260921` (Odoo 19 Community, `odoo/addons`) |
| Date | 2026-10-02 |
| Claim-ID prefix / Neutral prefix | `VDR-U17-C###` / `N-U17-###` |
| Method | static source read (pointers viewed; line numbers machine-checked against anchors) + read-only configuration queries on the restored DB (counts, flags, names of seeded configuration only). HR data is personal data: only structures, rules and counts are recorded, no values. No source modified, Odoo not started, no git state change. |
| Limits | No V-level, completeness, coverage %, Gate PASS or Clean-Room approval is asserted. Anything needing execution is flagged `RT`. See section 0.4 for what was not read. |

## 0. Scope notes

### 0.1 Function-ID mapping
No Function-ID in `EXISTING_FUNCTION_ID_INDEX_53.json` genuinely matches the HR, time-off, attendance, recruitment, fleet or calendar capabilities (the only HR-adjacent entry, `BRP-F04` work-centre allowed employees, concerns manufacturing and is not evidenced here). Every capability below is therefore **FUNCTION MAPPING REQUIRED**; no ID is invented.

### 0.2 Capability list (derived from manifests, models and security, not from files)
- CAP-U17-01 Employee master record and dated versions (`hr`, `hr_hourly_cost`)
- CAP-U17-02 Employee data access scoping, manager hierarchy and company boundaries (`hr`, `hr_org_chart`, `hr_attendance` kiosk exposure)
- CAP-U17-03 Time-off request lifecycle and approval (`hr_holidays`, `hr_work_entry_holidays`, `hr_holidays_attendance`)
- CAP-U17-04 Time-off allocations, accrual plans and balances (`hr_holidays`, `hr_holidays_attendance`)
- CAP-U17-05 Attendance recording, kiosk and overtime (`hr_attendance`, `hr_holidays_attendance`)
- CAP-U17-06 Work entry generation, conflict control and validation (`hr_work_entry`, `hr_work_entry_holidays`)
- CAP-U17-07 Recruitment pipeline (`hr_recruitment`, `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_recruitment_survey`)
- CAP-U17-08 Skills, resumes and certifications (`hr_skills`, `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`)
- CAP-U17-09 Fleet vehicles, contracts, services and driver assignment (`fleet`, `hr_fleet`)
- CAP-U17-10 Calendar events, attendees, invitations and reminders (`calendar`, `calendar_sms`, `hr_calendar`)
- Secondary coverage (lighter depth, no D1/D2/D3 table): presence, home-working, maintenance, gamification, bridges (`hr_presence`, `hr_homeworking`, `hr_homeworking_calendar`, `hr_holidays_homeworking`, `maintenance`, `hr_maintenance`, `gamification`, `hr_gamification`, `gamification_sale_crm`, `resource_mail`, `mail_bot_hr`, `hr_livechat`, `hr_org_chart` chart controller).

### 0.3 DISCOVERED SUPPORTING MODULES (read only as far as needed, outside the U17 assignment)
`resource` (calendar, leaves, resource mixin: `_get_work_days_data_batch`, `resource.calendar.leaves`), `mail` (activities, aliases, message_notify), `base` (`res.users`, `res.partner.bank`, `res.partner`, geocoder), `sms` (composer, templates), `survey` (user_input, invite), `event`, `website_slides` (completion hook, read only through bridges), `utm`, `phone_validation`, `web_hierarchy`, `barcodes`, `base_geolocalize`, `digest`, `mail_bot`, `im_livechat`, `sale_crm`. `hr_contract` has no directory in this edition (contract data lives in `hr.version` inside `hr`). The restored DB shows `hr_expense`, `google_calendar` and `microsoft_calendar` as installed; they sit outside this unit and were not read, so any extension they make to employees, leaves or events is not evidenced here.

### 0.4 What was NOT read (honest partial list)
- `hr` views, wizards `hr_contract_template_wizard` and `hr_bank_account_allocation_wizard`, mail activity plan models, work-location and contract-type models, and country data files.
- `hr_holidays` generate-multi wizards, summary report wizards, report models (`hr.leave.report`, `hr.leave.report.calendar`), dashboard methods, mandatory-day views, i18n, and tests (read only for one reference).
- `hr_attendance` reporting views and JS; `hr_attendance_overtime_rule` interval maths beyond the constructors and constraints (lines 168-735 skimmed by structure only).
- `hr_work_entry` calendar views, `hr_user_work_entry_employee` model and resource calendar overrides (`resource_calendar*.py`).
- `hr_recruitment` job-add and talent-pool wizards, `hr.job` computed counters, source/campaign models, mail templates; `website_hr_recruitment` (not assigned).
- `hr_skills` job-skill, level, resume-type, report models, CV wizard.
- `fleet` model/brand/category models, cost and odometer reports, send-mail wizard.
- `calendar` recurrence engine (`calendar_recurrence.py`, 643 lines), res.users/res.partner extensions and `calendar.filters`.
- `maintenance` equipment model and team aliasing; `gamification` badge, karma, rank and tracking models; `hr_org_chart` views.
- No runtime behaviour was observed anywhere in this unit.

### 0.5 Contradictions with prior evidence (`CONTRA`)
None found. The prior candidate source-map records for `hr`, `hr_holidays`, `hr_attendance`, `hr_work_entry`, `fleet`, `calendar`, `hr_skills`, `hr_homeworking`, `maintenance` state security counts (ACL 26/27/11/6/24/15/20/2/10, rules 13/26/10/3/9/4/11/2/8) that match the source and the restored DB. Two notes: (a) the prior records count the extension of `base.group_user` and a `base.default_user_group` pseudo-group as "declared groups", which explains 3 vs 2 for `hr`; the DB holds 2 groups for `hr`, 4 for `hr_attendance` and 4 for `hr_recruitment`; (b) the prior hr_holidays quirk about allocation approval tasks reading the leave validation setting is **confirmed** (VDR-U17-C476). New findings not in prior records are listed in section 0.6.

### 0.6 Findings of note (all pointer-backed in the claims table)
1. `hr` has no contract model in this edition: contract terms are dated `hr.version` records reached through `_inherits` (VDR-U17-C002, VDR-U17-C009).
2. HR officers lose write access to `hr.job` when `hr_recruitment` is installed because it redefines the `hr` ACL id (VDR-U17-C349).
3. Recruitment officers get a domain-true rule on all `mail.message` records (VDR-U17-C348).
4. The fleet cron named "Generate contracts costs based on costs frequency" only manages contract expiry and reminders (VDR-U17-C395, VDR-U17-C396); the assignment log end date is never set by code (VDR-U17-C399).
5. `hr_holidays_attendance` overrides a base method that does not exist (VDR-U17-C168).
6. Kiosk routes are token-authenticated public endpoints acting in sudo; three further public routes have no sudo and a settings route writes on the session user's company (VDR-U17-C267, VDR-U17-C269, VDR-U17-C270).
7. Approval and invitation acceptance work through GET links (VDR-U17-C159, VDR-U17-C425).
8. Home-working guard and weekly wizard have latent defects (VDR-U17-C456, VDR-U17-C455); presence cron evaluates only the running user's company (VDR-U17-C448).
9. `hr_work_entry` supports only the working-schedule source in this edition (VDR-U17-C292).
10. Employee records of companies outside the user's allowed companies remain visible to their manager and to themselves (VDR-U17-C087).

### 0.7 Config reconciliation (restored DB vs source; configuration rows only)
| Module | ACL src / DB | Rules src / DB | Groups src / DB | Crons src / DB | Note |
|---|---|---|---|---|---|
| hr | 26 / 26 | 13 / 13 | 2 / 2 | 2 / 2 | 1 employee, 1 version, 1 department, 0 jobs seeded/config rows |
| hr_attendance | 11 / 11 | 10 / 10 | 4 own + 1 `base.group_user` extension / 4 | 2 / 2 | 2 rulesets, 6 rules |
| hr_holidays | 27 / 27 | 26 / 26 | 3 / 3 | 2 / 2 | 73 leave types seeded, 0 leaves |
| hr_holidays_attendance | 1 / 1 | 0 / 0 | 0 / 0 | 0 / 0 | |
| hr_homeworking | 2 / 2 | 2 / 2 | 0 / 0 | 0 / 0 | |
| hr_homeworking_calendar | 1 / 1 | 2 / 2 | 0 / 0 | 0 / 0 | |
| hr_presence | 1 / 1 | 1 / 1 | 0 / 0 | 1 / 1 | |
| hr_work_entry | 6 / 6 | 3 / 3 | 0 / 0 | 1 / 1 | 118 types, 0 entries |
| hr_skills | 20 / 20 | 11 / 11 | 0 / 0 | 1 / 1 | 36 skills, 11 levels |
| hr_recruitment | 31 / 30 (one row redefines an `hr` ACL id) | 8 / 8 | 4 own + 1 extension / 4 | 0 / 0 | 6 stages |
| hr_recruitment_skills | 2 / 2 | 2 / 2 | 0 / 0 | 0 / 0 | |
| hr_recruitment_survey | 13 / 13 | 14 / 14 | 0 / 0 | 0 / 0 | |
| hr_gamification | 5 / 5 | 4 / 4 | 0 / 0 | 0 / 0 | |
| hr_fleet | 1 / 1 | 1 / 1 | 0 / 0 | 0 / 0 | |
| fleet | 24 / 24 | 9 / 9 | 2 / 2 | 1 / 1 | 4 states, 67 brands |
| maintenance | 10 / 10 | 8 / 8 | 1 / 1 | 0 / 0 | 4 stages, 1 team |
| gamification | 28 / 28 | 3 / 3 | 0 / 0 | 2 / 2 | |
| calendar | 15 / 15 | 4 / 4 | 0 / 0 | 1 / 1 | 7 alarms |
| other 14 assigned modules | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | no security data: `hr_holidays_homeworking`, `hr_calendar`, `hr_hourly_cost`, `hr_org_chart`, `hr_work_entry_holidays`, `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`, `hr_recruitment_sms`, `hr_livechat`, `hr_maintenance` (implies a group), `gamification_sale_crm`, `calendar_sms`, `mail_bot_hr`, `resource_mail` |

Automations 0, sequences 0 (source and DB, VDR-U17-C477); cron total 13 equal in source and DB (VDR-U17-C478). All 33 modules are `installed` in the restored DB.

## CAP-U17-01 Employee master record and dated versions

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1 (business purpose & process semantics):** maintain one record per person per company holding working relationship data (company, department, job, manager, coach, schedule, location, tags), private data and contract-like terms, with history kept as effective-dated versions; support user creation, departure registration and expiry reminders. Edition fact: no contract model; contract periods are runs of versions sharing contract dates.

**D2 (architecture / data / object relationships):** `hr.employee` `_inherits` `hr.version` through a non-stored computed `version_id` (VDR-U17-C002, VDR-U17-C003); `current_version_id` is stored and refreshed by cron (VDR-U17-C004, VDR-U17-C006); `resource.resource` carries name, active, user and calendar (VDR-U17-C035); `res.users` links through `employee_ids` and `employee_id` (company employee); `hr.department` tree with manager; `hr.job` per department and company; wizard `hr.departure.wizard`.

**D3 (source / technical / workflow logic):** create: per-company batch, user sync, work contact creation, department channel subscription, onboarding note (VDR-U17-C027, VDR-U17-C025, VDR-U17-C026, VDR-U17-C028, VDR-U17-C029); write: user and tz sync, one write onto the version with stamp, calendar follows current version, bank accounts follow work contact (VDR-U17-C030, VDR-U17-C031, VDR-U17-C033, VDR-U17-C034, VDR-U17-C032); `create_version` copies the version in force with sudo and syncs sibling contract dates (VDR-U17-C016, VDR-U17-C017, VDR-U17-C018, VDR-U17-C019); constraints on dates and uniqueness (VDR-U17-C009, VDR-U17-C010, VDR-U17-C011, VDR-U17-C012, VDR-U17-C013, VDR-U17-C014, VDR-U17-C015).

State diagram (list):
- employee active -> archived [action_archive, links cleared, departure wizard when single] VDR-U17-C037 VDR-U17-C038
- archived -> active [action_unarchive clears departure data] VDR-U17-C039
- version v1 -> version v2 [create_version at a later date, copy of version in force] VDR-U17-C016
- version future-dated -> current [daily cron or date reached] VDR-U17-C006
- contract none -> contract period [create_contract writes dates on a same-date version or creates one] VDR-U17-C020

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Create employee (with or without user) -> work contact, avatar, channels, onboarding note VDR-U17-C025 VDR-U17-C026 VDR-U17-C029; change role/schedule by a new version VDR-U17-C016; depart via wizard VDR-U17-C040 VDR-U17-C041 VDR-U17-C043. |
| 2 Reversal / cancel / negative path | Unarchive clears departure data VDR-U17-C039; last version cannot be deleted/archived/moved VDR-U17-C012 VDR-U17-C013; departure before contract start refused VDR-U17-C040. |
| 3 Multi-company / data-scope | Employee rows are per company and users are unique per company VDR-U17-C022; company change is warned against VDR-U17-C050; creation batched per company VDR-U17-C027; scope rules in CAP-U17-02. |
| 4 Side effects & cross-module triggers | Version changes cascade into leaves, work entries and overtime (CAP-U17-03, -05, -06); user creation side effects VDR-U17-C051; bank accounts re-pointed VDR-U17-C032; department manager cascade VDR-U17-C046. |
| 5 Configuration & optionality | Contract and permit notice periods VDR-U17-C049; onboarding plan note VDR-U17-C029; user-from-employee cost warning VDR-U17-C052; hourly cost optional VDR-U17-C084. |
| 6 Validation & constraints | VDR-U17-C021 VDR-U17-C022 VDR-U17-C023 VDR-U17-C024 VDR-U17-C011 VDR-U17-C045 VDR-U17-C047 VDR-U17-C048 VDR-U17-C044. |
| 7 Roles & permissions | Officer group CRUD, administrator for contract terms, system read-only (CAP-U17-02) VDR-U17-C057 VDR-U17-C068. |
| 8 Scheduled / automated behaviour | Current-version refresh and expiry notice crons VDR-U17-C006 VDR-U17-C049 VDR-U17-C008. |
| 9 Exception & failure behaviour | Bulk user creation reports skipped employees instead of failing VDR-U17-C051; version creation requires date_version (VDR-U17-C016); departure wizard raises on date error VDR-U17-C040. |
| 10 Accounting, stock, audit, security & compliance | Last-modified stamp and tracked fields on versions VDR-U17-C033; bank accounts and payment-trust flag follow the contact VDR-U17-C032; personal data separated by groups (CAP-U17-02); no accounting posting in this capability. |

**DB reconciliation (restored DB, configuration only):** VDR-U17-C089 VDR-U17-C088 VDR-U17-C008. 1 employee row, 1 version row, 1 department; 12 contract types, 3 departure reasons, 3 work locations, 2 activity plans and 5 plan templates are seeded configuration. Company country is TH. Counts only; no personal values were read.

**Unknown / Runtime list:** VDR-U17-C054 (contract templates, payroll structures, localisation); behaviour of `_inherits` with multi-version selection in the web client (`RT`); onboarding plan wizard behaviour (`RT`).

## CAP-U17-02 Employee data access scoping, manager hierarchy and company boundaries

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** publish a directory to every internal user while confining private, banking, identification and pay data to HR; keep managers and employees able to see their own chain even across companies; offer an org chart.

**D2:** `hr.employee` (private, ACL officer) and `hr.employee.public` (SQL view over employee plus current version, ACL internal user) VDR-U17-C057 VDR-U17-C059 VDR-U17-C060 VDR-U17-C061; groups `group_hr_user` and `group_hr_manager` VDR-U17-C055 VDR-U17-C056; global rules per model VDR-U17-C070 VDR-U17-C071 VDR-U17-C072 VDR-U17-C073 VDR-U17-C074; field-level groups VDR-U17-C067 VDR-U17-C068 VDR-U17-C069; hierarchy `parent_id`, `child_ids`, `coach_id`; org chart `subordinate_ids`.

**D3:** private model methods `search_fetch`, `fetch`, `_search`, `get_view(s)` and `_check_access` detect missing read access and redirect to the public model, copying cache values or raising for private fields VDR-U17-C063 VDR-U17-C064 VDR-U17-C065 VDR-U17-C066 VDR-U17-C078; `hr.mixin` injects a sentinel context for many2many writes VDR-U17-C077; users edit own data through whitelisted self-service fields and HR responsible is notified VDR-U17-C075 VDR-U17-C076; org chart controller uses the public model, with sudo only for job and ancestor walk VDR-U17-C082 VDR-U17-C083 VDR-U17-C080.

State diagram (list):
- user without private read -> served from public view [search, fetch, get_view] VDR-U17-C065
- public request for private field -> AccessError VDR-U17-C064
- employee visible [company in allowed set OR manager OR own manager OR own record] VDR-U17-C070

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Employee opens directory and profile via public model VDR-U17-C059 VDR-U17-C065; HR officer opens private form VDR-U17-C057. |
| 2 Reversal / cancel / negative path | Private field request by non-HR raises VDR-U17-C064; private views refused with redirect VDR-U17-C066. |
| 3 Multi-company / data-scope | Four-branch rule on employee and public model VDR-U17-C070 VDR-U17-C071; leakage for managers/own record VDR-U17-C087; versions by `company_ids` VDR-U17-C073; org chart passes allowed companies in context VDR-U17-C082. |
| 4 Side effects & cross-module triggers | Sentinel context for relations VDR-U17-C077 VDR-U17-C078; org chart and presence read public fields VDR-U17-C082; recruitment, holidays, attendance, fleet, skills each extend both models. |
| 5 Configuration & optionality | `hr_org_chart` and `hr_hourly_cost` optional VDR-U17-C083 VDR-U17-C084; groups per field decide visibility VDR-U17-C067. |
| 6 Validation & constraints | No state machine; field groups and rules are the constraints VDR-U17-C068 VDR-U17-C074. |
| 7 Roles & permissions | VDR-U17-C055 VDR-U17-C056 VDR-U17-C057 VDR-U17-C058 VDR-U17-C059 VDR-U17-C074 VDR-U17-C073; DB confirms ACL names and a single global employee rule VDR-U17-C088. |
| 8 Scheduled / automated behaviour | None specific. |
| 9 Exception & failure behaviour | AccessError path VDR-U17-C064; org chart returns empty structures when read is denied VDR-U17-C082. |
| 10 Accounting, stock, audit, security & compliance | Bank accounts hidden from non-HR VDR-U17-C074; kiosk uses elevated reads of PIN and badge VDR-U17-C086; self-service edits notify HR VDR-U17-C076. |

**DB reconciliation:** VDR-U17-C088: hr.employee has one global rule with the four-way domain, hr.employee.public one, hr.version two, hr.department two, hr.job five (hr 1 plus recruitment); ACL names match source; group members: HR administrator group has the 2 seeded users.

**Unknown / Runtime list:** VDR-U17-C090; `hr.employee.public` view and cache hack behaviour under the web client (`RT`); effect of `bypass_search_access` on current_version_id for odd domains (`RT`).

## CAP-U17-03 Time-off request lifecycle and approval

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** let employees request absences, route approval by type, protect balances, and reflect approved absence on the working calendar, calendar meetings, work entries and overtime; recompute when public holidays or schedules change; cancel or delete on departure.

**D2:** `hr.leave` (state, dates, durations, employee, type, approvers, meeting), `hr.leave.type` (validation, allocation need, units), `resource.calendar.leaves` (absence entries, `holiday_id`), `calendar.event`, `hr.holidays.cancel.leave` wizard, `hr.leave.mandatory.day`; bridges `hr_work_entry_holidays` (work entry type per leave type, `leave_id` on entries) and `hr_holidays_attendance` (overtime deduction); employee extension `leave_manager_id`; groups responsible, officer, administrator.

**D3:** control flow: create -> `_check_validity` -> auto-approve or activities VDR-U17-C096 VDR-U17-C099 VDR-U17-C097 VDR-U17-C098; approve -> `validate1` or `_action_validate` -> resource leave and meeting VDR-U17-C109 VDR-U17-C110 VDR-U17-C111 VDR-U17-C125 VDR-U17-C127; refuse and cancel remove absence and meeting VDR-U17-C112 VDR-U17-C113 VDR-U17-C117 VDR-U17-C118 VDR-U17-C130; permission matrix VDR-U17-C119 VDR-U17-C120 VDR-U17-C121 VDR-U17-C124 VDR-U17-C123 VDR-U17-C122; inheritance chain: `hr.leave` base + `hr_work_entry_holidays` (validate, refuse, cancel hooks, `_error_checking` wrapper VDR-U17-C161 VDR-U17-C163 VDR-U17-C314 VDR-U17-C164) + `hr_holidays_attendance` (overtime deductible checks VDR-U17-C167 VDR-U17-C168).

State diagram (list):
- (new) -> confirm [create; type needs approval] VDR-U17-C098
- (new) -> validate [create; validation_type no_validation, automatic approval] VDR-U17-C097
- confirm -> validate1 [action_approve; validation_type both] VDR-U17-C109
- confirm -> validate [action_approve by approver or officer; other types] VDR-U17-C110
- validate1 -> validate [second approval by officer] VDR-U17-C111
- confirm|validate1|validate -> refuse [action_refuse] VDR-U17-C112
- confirm|validate1|validate|refuse -> cancel [own cancel wizard or system force cancel] VDR-U17-C120 VDR-U17-C117
- validate -> confirm [officer back to approval] VDR-U17-C121
- cancel -> (final) VDR-U17-C122

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Request created for own employee VDR-U17-C094, validated by type, approval stamps approver ids VDR-U17-C111, resource leave and optional meeting created VDR-U17-C125 VDR-U17-C127, work entries updated VDR-U17-C161. |
| 2 Reversal / cancel / negative path | Refuse VDR-U17-C112; user cancel with reason VDR-U17-C115 VDR-U17-C116; force cancel by cron or departure VDR-U17-C117 VDR-U17-C139 VDR-U17-C153; no reset VDR-U17-C123; delete rules VDR-U17-C133 VDR-U17-C134; copies refused VDR-U17-C135. |
| 3 Multi-company / data-scope | Global company rule on requests VDR-U17-C175; employee domain limits non-officers VDR-U17-C095; leave types scoped by company or country VDR-U17-C176; company country locked while country-specific leaves exist VDR-U17-C156. |
| 4 Side effects & cross-module triggers | Resource calendar leave VDR-U17-C126; meeting VDR-U17-C128 VDR-U17-C129; work entry conflict handling VDR-U17-C161 VDR-U17-C162 VDR-U17-C163 VDR-U17-C165; overtime VDR-U17-C167; public holiday recomputation VDR-U17-C147 VDR-U17-C150; schedule change VDR-U17-C151 VDR-U17-C152. |
| 5 Configuration & optionality | Per-type switches VDR-U17-C093 VDR-U17-C092; mandatory days VDR-U17-C104 VDR-U17-C105; negative cap VDR-U17-C103; approver group auto-grant VDR-U17-C144. |
| 6 Validation & constraints | VDR-U17-C101 VDR-U17-C102 VDR-U17-C103 VDR-U17-C104 VDR-U17-C106 VDR-U17-C107 VDR-U17-C108 VDR-U17-C158 VDR-U17-C157. |
| 7 Roles & permissions | ACL base.group_user full CRUD with record rules VDR-U17-C169 VDR-U17-C170 VDR-U17-C171 VDR-U17-C172 VDR-U17-C173 VDR-U17-C174; write guards VDR-U17-C131 VDR-U17-C132. |
| 8 Scheduled / automated behaviour | Daily cancel of uncovered accrual leaves VDR-U17-C138 VDR-U17-C139; approval activities VDR-U17-C137. |
| 9 Exception & failure behaviour | Approval link swallows exceptions VDR-U17-C160; schedule-change errors become a review message VDR-U17-C151; leaves failing validity after holiday change are refused VDR-U17-C148; zero-day approval blocked VDR-U17-C108. |
| 10 Accounting, stock, audit, security & compliance | State changes tracked (`tracking=True` on state) and approver ids recorded VDR-U17-C111; unpaid and accrual flags travel to the calendar leave VDR-U17-C126; state-changing GET links VDR-U17-C159; validated work entries lock cancellation VDR-U17-C164. No accounting posting in these modules (payroll not installed). |

**DB reconciliation (restored DB, configuration only):** VDR-U17-C177. Source 26 rules and 27 ACL equal DB; groups 3; crons 2 active. Because the company country is TH only the six country-less leave types are visible by the type rule; 0 leaves exist.

**Unknown / Runtime list:** VDR-U17-C178; duration numbers for flexible, hourly and half-day cases (`RT`); notification mail delivery (`RT`); interplay with external calendar sync modules present in the DB (`RT`); real behaviour of `action_reset_confirm` (VDR-U17-C168, `RT` if any caller exists in enterprise code).

## CAP-U17-04 Time-off allocations, accrual plans and balances

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** grant entitlements, optionally accruing over time, and enforce balance policy including carry-over, caps and expiry; convert extra hours to time-off pools when enabled.

**D2:** `hr.leave.allocation` (state, type, plan, `nextcall`/`lastcall`, carry-over fields), `hr.leave.accrual.plan` with `hr.leave.accrual.level`, `hr.leave.type` (allocation switches), balance engine `hr.employee._get_consumed_leaves` and `hr.leave.type.get_allocation_data`; bridge `hr_holidays_attendance` (worked-hours frequency, overtime pool).

**D3:** cron `_update_accrual` selects due allocations VDR-U17-C193 -> `_process_accrual_plans` first-run init VDR-U17-C194, replay loop VDR-U17-C195, level choice VDR-U17-C203, amount VDR-U17-C196 VDR-U17-C197 VDR-U17-C198, caps VDR-U17-C199, carry-over VDR-U17-C200 VDR-U17-C201 VDR-U17-C202; approvals mirror requests VDR-U17-C183 VDR-U17-C184 VDR-U17-C185 VDR-U17-C186 VDR-U17-C187 VDR-U17-C188 VDR-U17-C189; inheritance: base + `hr_holidays_attendance` overrides of `_get_accrual_plan_level_work_entry_prorata`, `get_allocation_data`, create/write checks VDR-U17-C216 VDR-U17-C220 VDR-U17-C219.

State diagram (list):
- (new) -> confirm [create] VDR-U17-C183
- (new) -> validate [create; allocation validation no_validation] VDR-U17-C184
- confirm -> validate1 [approve; both] VDR-U17-C185
- validate1|confirm -> validate [validate] VDR-U17-C186
- confirm|validate1|validate -> refuse [action_refuse] VDR-U17-C187
- accrual validate: nextcall due -> nextcall advanced [daily cron or on-demand preview] VDR-U17-C193 VDR-U17-C195

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Officer creates accrual allocation -> approved -> cron adds days per level VDR-U17-C194 VDR-U17-C195; employee requests time off against balance VDR-U17-C212 VDR-U17-C213. |
| 2 Reversal / cancel / negative path | Refuse VDR-U17-C187; delete only confirm/refuse without taken time VDR-U17-C191 VDR-U17-C192; reduce below taken refused VDR-U17-C190; accrual cannot be edited retroactively VDR-U17-C194. |
| 3 Multi-company / data-scope | Allocation rules and company rule VDR-U17-C221; plan multi-company rule; type visibility VDR-U17-C176. |
| 4 Side effects & cross-module triggers | Manager/department sync VDR-U17-C214; schedule change recompute VDR-U17-C215; overtime pool VDR-U17-C218 VDR-U17-C220; invalid-leave cancel cron (CAP-U17-03) VDR-U17-C138. |
| 5 Configuration & optionality | Plan options VDR-U17-C204 VDR-U17-C205; per-level caps and carry-over VDR-U17-C199 VDR-U17-C201; overtime deduction per type VDR-U17-C218. |
| 6 Validation & constraints | VDR-U17-C181 VDR-U17-C182 VDR-U17-C206 VDR-U17-C207 VDR-U17-C208 VDR-U17-C209 VDR-U17-C210 VDR-U17-C211 VDR-U17-C217. |
| 7 Roles & permissions | VDR-U17-C221 VDR-U17-C222 VDR-U17-C188 VDR-U17-C169. |
| 8 Scheduled / automated behaviour | VDR-U17-C193 VDR-U17-C223. |
| 9 Exception & failure behaviour | Overtime shortage raises VDR-U17-C219; first-run informational log VDR-U17-C194; allocation approval task decided by the leave validation setting VDR-U17-C476. |
| 10 Accounting, stock, audit, security & compliance | Balance integrity (excess tracking) VDR-U17-C213; tracked fields on allocation and approvers VDR-U17-C186; no financial posting; unpaid flag carried to calendar (CAP-U17-03). |

**DB reconciliation:** VDR-U17-C223; 0 allocations and 0 accrual plans; 27 ACL and 26 rules shared with CAP-U17-03.

**Unknown / Runtime list:** VDR-U17-C224; accrual replay performance for long histories (`RT`); interaction of `precomputed_allocations` context (`RT`).

## CAP-U17-05 Attendance recording, kiosk and overtime

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** capture check-in/out (web, systray, kiosk, badge), compute worked hours and overtime by rules, optionally auto-close and flag absences, and expose approval of extra hours.

**D2:** `hr.attendance`, `hr.attendance.overtime.line`, `hr.attendance.overtime.ruleset` and `.rule`, version field `ruleset_id`, company flags, groups own-reader, officer, user, manager; controllers for kiosk and systray; bridge `hr_holidays_attendance` (compensable flag, leave-triggered recompute).

**D3:** `_attendance_action_change` toggles VDR-U17-C233 VDR-U17-C234; create/write/unlink call `_update_overtime` VDR-U17-C237 VDR-U17-C238 VDR-U17-C239 VDR-U17-C240; rules produce vals VDR-U17-C251 VDR-U17-C247 VDR-U17-C248; crons VDR-U17-C254 VDR-U17-C255 VDR-U17-C256 VDR-U17-C257; kiosk routes VDR-U17-C266 VDR-U17-C267 VDR-U17-C268.

State diagram (list):
- no attendance -> open [check in] VDR-U17-C233
- open -> closed [check out, auto check-out cron, or employee archived] VDR-U17-C233 VDR-U17-C255 VDR-U17-C235
- overtime line (new) -> approved [company validation automatic] VDR-U17-C243
- overtime line (new) -> to_approve [company validation by manager] VDR-U17-C243
- to_approve -> approved|refused [officer action] VDR-U17-C245

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Check in/out VDR-U17-C233; worked hours VDR-U17-C230; overtime lines created VDR-U17-C237 VDR-U17-C251. |
| 2 Reversal / cancel / negative path | Error on missing check-in VDR-U17-C234; refusal of overtime VDR-U17-C245; regeneration keeps manual lines VDR-U17-C238; copy refused VDR-U17-C232. |
| 3 Multi-company / data-scope | Global company rules VDR-U17-C262; kiosk token per company VDR-U17-C266 VDR-U17-C274; systray uses active company VDR-U17-C272. |
| 4 Side effects & cross-module triggers | Presence state VDR-U17-C278; calendar leaves recompute overtime VDR-U17-C276; overtime pool for time off (CAP-U17-04) VDR-U17-C218; officer group auto-assignment VDR-U17-C259 VDR-U17-C260. |
| 5 Configuration & optionality | Company flags VDR-U17-C275 VDR-U17-C258; ruleset on version VDR-U17-C252; rule kinds VDR-U17-C249; combination mode VDR-U17-C246. |
| 6 Validation & constraints | VDR-U17-C227 VDR-U17-C228 VDR-U17-C229 VDR-U17-C244 VDR-U17-C250. |
| 7 Roles & permissions | VDR-U17-C261 VDR-U17-C263 VDR-U17-C264 VDR-U17-C265 VDR-U17-C241. |
| 8 Scheduled / automated behaviour | VDR-U17-C254 VDR-U17-C256 VDR-U17-C258. |
| 9 Exception & failure behaviour | Geocoding failure -> Unknown VDR-U17-C273; public-route behaviours VDR-U17-C269 VDR-U17-C270; auto check-out note VDR-U17-C255. |
| 10 Accounting, stock, audit, security & compliance | Evidence value limited: records editable by attendance officers; technical attendances VDR-U17-C257; kiosk bearer secret VDR-U17-C266 VDR-U17-C267; device data (IP, browser, coordinates) is personal data VDR-U17-C273; rates feed payroll (not installed) VDR-U17-C247. |

**DB reconciliation:** VDR-U17-C258: both crons active at 4 hours; company flags auto check-out, absence management, device tracking, systray on (config); 2 rulesets with 2 and 4 rules (6 total); source 11 ACL and 10 rules equal DB; 0 attendances.

**Unknown / Runtime list:** VDR-U17-C279; external geocoding latency and failure (`RT`); kiosk behaviour of the three non-sudo public routes (`RT`); barcode scanning hardware (`RT`).

## CAP-U17-06 Work entry generation, conflict control and validation

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** turn schedules, public holidays and approved time off into dated work entries per version, detect conflicts and let HR validate entries for payroll.

**D2:** `hr.work.entry` (date, duration, type, state, version), `hr.work.entry.type`, `hr.version` extensions (`date_generated_from/to`, `work_entry_source`, `last_generation_date`), regeneration wizard, bridge `hr_work_entry_holidays` (`leave_id`, type mapping).

**D3:** cron `_cron_generate_missing_work_entries` -> `generate_work_entries` -> `_generate_work_entries` -> `_get_work_entries_values` -> postprocess -> create -> `_check_if_error` VDR-U17-C302 VDR-U17-C293 VDR-U17-C294 VDR-U17-C295 VDR-U17-C297 VDR-U17-C298 VDR-U17-C283; validation VDR-U17-C282; errors VDR-U17-C284 VDR-U17-C285 VDR-U17-C286; leave integration VDR-U17-C311 VDR-U17-C312.

State diagram (list):
- (new) -> draft [generation] VDR-U17-C287
- draft -> conflict [duration above 24h per day, undefined type, leave outside schedule, day already validated] VDR-U17-C283
- conflict -> draft [cause removed, `_reset_conflicting_state`] VDR-U17-C289
- draft -> validated [action_validate with no errors] VDR-U17-C282
- draft|conflict -> cancelled [active false] VDR-U17-C288
- cancelled -> draft [active true] VDR-U17-C288

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Cron generates entries from calendar VDR-U17-C302 VDR-U17-C294; HR validates VDR-U17-C282. |
| 2 Reversal / cancel / negative path | Cancel/reactivate VDR-U17-C288; cannot delete validated VDR-U17-C290; regeneration excludes validated employees VDR-U17-C304; split VDR-U17-C291. |
| 3 Multi-company / data-scope | Company rule VDR-U17-C309; generation per company and timezone VDR-U17-C293; cron batch per company VDR-U17-C302. |
| 4 Side effects & cross-module triggers | Time off creates leave entries VDR-U17-C161 VDR-U17-C162; cancelling an entry refuses the time off VDR-U17-C165; schedule change recompute VDR-U17-C300; version create resets bounds VDR-U17-C310. |
| 5 Configuration & optionality | Single source VDR-U17-C292; types and codes VDR-U17-C305 VDR-U17-C307; bypass-code priority VDR-U17-C311. |
| 6 Validation & constraints | VDR-U17-C281 VDR-U17-C306 VDR-U17-C305 VDR-U17-C299. |
| 7 Roles & permissions | VDR-U17-C308 VDR-U17-C309. |
| 8 Scheduled / automated behaviour | VDR-U17-C302 VDR-U17-C303. |
| 9 Exception & failure behaviour | Missing timezone error VDR-U17-C299; conflict states instead of exceptions VDR-U17-C283; cron retriggers itself VDR-U17-C302. |
| 10 Accounting, stock, audit, security & compliance | Validated entries are the payroll handoff; generation as superuser VDR-U17-C293; amount_rate copied at creation VDR-U17-C287; no journal entries in these modules. |

**DB reconciliation:** VDR-U17-C303; 6 ACL, 3 rules, 1 cron equal source; 0 entries.

**Unknown / Runtime list:** VDR-U17-C316; flexible-calendar generation maths (`RT`); performance of mass regeneration (`RT`).

## CAP-U17-07 Recruitment pipeline

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** track applications per job through stages to hire or refusal, hand off to an employee, support email intake, SMS, surveys and skill matching.

**D2:** `hr.applicant` (stage, status, job, recruiter, interviewers, talent pool), `hr.job` (alias, planned recruits), `hr.recruitment.stage`, `hr.applicant.refuse.reason`, `hr.talent.pool`, `hr.job.platform`; wizard `applicant.get.refuse.reason`; bridges `hr_recruitment_skills` (`hr.applicant.skill`), `_sms`, `_survey` (`survey.user_input.applicant_id`); no `hr.candidate` model in this edition.

**D3:** stage compute and date_closed VDR-U17-C318 VDR-U17-C320; write-side effects VDR-U17-C324 VDR-U17-C321; create side effects VDR-U17-C323 VDR-U17-C325; refuse wizard VDR-U17-C339 VDR-U17-C340 VDR-U17-C341; reset VDR-U17-C342; hire handoff VDR-U17-C335 VDR-U17-C336 VDR-U17-C338 VDR-U17-C353; mail intake VDR-U17-C332 VDR-U17-C333 VDR-U17-C334.

State diagram (list):
- (new) -> ongoing in first stage [create or mail intake] VDR-U17-C318 VDR-U17-C332
- ongoing stage n -> stage n+1 [stage write; kanban state reset] VDR-U17-C324
- any non-hired stage -> hired stage [date_closed set; job planned recruits decremented] VDR-U17-C320 VDR-U17-C321
- ongoing -> refused/archived [refuse wizard] VDR-U17-C339
- refused|archived -> ongoing first stage [reset or unarchive] VDR-U17-C342
- hired -> employee [create_employee_from_applicant] VDR-U17-C335

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Intake -> stages -> hired stage -> employee VDR-U17-C332 VDR-U17-C320 VDR-U17-C335. |
| 2 Reversal / cancel / negative path | Refuse with reason and optional mail VDR-U17-C339 VDR-U17-C340; duplicates VDR-U17-C341; reset VDR-U17-C342; moving out of hired restores planned recruits VDR-U17-C321. |
| 3 Multi-company / data-scope | Global company rule VDR-U17-C347; applicant company computed from job/department VDR-U17-C318. |
| 4 Side effects & cross-module triggers | Interviewer group management VDR-U17-C326 VDR-U17-C327; employee creation VDR-U17-C338; skills copy VDR-U17-C353; survey invite and bot message VDR-U17-C356 VDR-U17-C357; SMS VDR-U17-C355. |
| 5 Configuration & optionality | Stage fields VDR-U17-C343; platforms and aliases VDR-U17-C333 VDR-U17-C334; survey type VDR-U17-C359. |
| 6 Validation & constraints | VDR-U17-C328 VDR-U17-C331 VDR-U17-C344 VDR-U17-C047 VDR-U17-C048. |
| 7 Roles & permissions | VDR-U17-C345 VDR-U17-C346 VDR-U17-C350 VDR-U17-C349 VDR-U17-C348 VDR-U17-C337 VDR-U17-C358 VDR-U17-C354. |
| 8 Scheduled / automated behaviour | None in recruitment itself (no cron). |
| 9 Exception & failure behaviour | Missing sender or recipient email blocks mail option VDR-U17-C340; missing name blocks employee creation VDR-U17-C335; interviewer denied VDR-U17-C337. |
| 10 Accounting, stock, audit, security & compliance | Applicant personal data and salary fields restricted by group (`groups` on salary fields, line 94-97 of the applicant model); chatter visibility to officers VDR-U17-C348; attachments copied to employee VDR-U17-C335; GDPR retention not implemented in the studied modules (no purge job found). |

**DB reconciliation:** VDR-U17-C351; hr.job ACL id redefined VDR-U17-C349.

**Unknown / Runtime list:** VDR-U17-C360; SMS gateway VDR-U17-C355 (`RT`); inbound mail gateway behaviour (`RT`).

## CAP-U17-08 Skills, resumes and certifications

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** maintain employee skills and resume lines with validity, auto-add training and certifications from events, courses and surveys, and remind about missing or expiring certifications.

**D2:** `hr.skill.type`, `hr.skill`, `hr.skill.level`, `hr.employee.skill` and `hr.applicant.skill` via `hr.individual.skill.mixin`, `hr.resume.line` and types, bridges `hr_skills_event`, `_slides`, `_survey`.

**D3:** mixin constraints and expiry VDR-U17-C361 VDR-U17-C362 VDR-U17-C363 VDR-U17-C364 VDR-U17-C365; current-skill filter VDR-U17-C366; cron VDR-U17-C369 VDR-U17-C370; bridge hooks VDR-U17-C375 VDR-U17-C376 VDR-U17-C377 VDR-U17-C378.

State diagram (list):
- skill active (valid_to empty or future) -> ended [removal sets valid_to yesterday] VDR-U17-C365
- skill (recent) -> deleted [created yesterday or later, or already ended] VDR-U17-C365
- certification valid -> expiring [within three months] -> expired VDR-U17-C378

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Employee or HR adds a skill; completion hooks add resume lines VDR-U17-C376 VDR-U17-C377 VDR-U17-C375. |
| 2 Reversal / cancel / negative path | Removal archives instead of deleting VDR-U17-C365; edits replaced by new records VDR-U17-C361. |
| 3 Multi-company / data-scope | Reports have company rule VDR-U17-C373; resume/skill read-all rules have no company scope VDR-U17-C371. |
| 4 Side effects & cross-module triggers | Event registration VDR-U17-C375; elevated writes VDR-U17-C379; applicant skills copy on hire VDR-U17-C353. |
| 5 Configuration & optionality | Certification skill types; validity months on surveys VDR-U17-C377; bridges auto-install. |
| 6 Validation & constraints | VDR-U17-C363 VDR-U17-C364 VDR-U17-C367 VDR-U17-C368. |
| 7 Roles & permissions | VDR-U17-C371 VDR-U17-C372 VDR-U17-C373 VDR-U17-C374. |
| 8 Scheduled / automated behaviour | VDR-U17-C369 VDR-U17-C380. |
| 9 Exception & failure behaviour | Overlap collisions raise a validation error listing conflicts VDR-U17-C362; cron skips employees with no responsible VDR-U17-C370. |
| 10 Accounting, stock, audit, security & compliance | History preserved for audit VDR-U17-C361; resumes visible company-wide VDR-U17-C371; certificate files stored on resume lines. |

**DB reconciliation:** VDR-U17-C380.

**Unknown / Runtime list:** VDR-U17-C381; survey/slides completion callbacks at runtime (`RT`).

## CAP-U17-09 Fleet vehicles, contracts, services and driver assignment

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** register vehicles and models, log odometers, services and contracts, track drivers and their history, and alert on contract renewal; bridge drivers to employees.

**D2:** `fleet.vehicle`, `.model`, `.model.brand`, `.state`, `.log.contract`, `.log.services`, `.odometer`, `.assignation.log`, `.service.type`; `hr_fleet` fields `driver_employee_id`, `future_driver_employee_id`, `mobility_card`; groups fleet officer and administrator.

**D3:** odometer VDR-U17-C384 VDR-U17-C385 VDR-U17-C386; driver change VDR-U17-C387 VDR-U17-C388 VDR-U17-C389 VDR-U17-C390; contracts VDR-U17-C392 VDR-U17-C393 VDR-U17-C394 VDR-U17-C395; bridge VDR-U17-C405 VDR-U17-C406 VDR-U17-C407 VDR-U17-C408.

State diagram (list):
- contract futur -> open [start date reached] VDR-U17-C394
- contract open -> expired [expiration passed] VDR-U17-C394
- contract any -> closed [action_close] VDR-U17-C393
- service new -> running -> done|cancelled VDR-U17-C401
- vehicle state: configurable list, default New Request VDR-U17-C382

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Register vehicle, assign driver, log odometer, track contract VDR-U17-C387 VDR-U17-C385 VDR-U17-C394. |
| 2 Reversal / cancel / negative path | Lower odometer refused VDR-U17-C386; archive cascades VDR-U17-C391; contract closed state VDR-U17-C392. |
| 3 Multi-company / data-scope | Company rules VDR-U17-C403; driver employee computed within vehicle company VDR-U17-C406. |
| 4 Side effects & cross-module triggers | Driver activity VDR-U17-C388; employee/driver sync VDR-U17-C405 VDR-U17-C408; plan template responsible VDR-U17-C411. |
| 5 Configuration & optionality | Delay parameter VDR-U17-C397; states and service types configurable. |
| 6 Validation & constraints | VDR-U17-C383 VDR-U17-C386 VDR-U17-C400 VDR-U17-C407. |
| 7 Roles & permissions | VDR-U17-C402 VDR-U17-C404 VDR-U17-C409 VDR-U17-C410. |
| 8 Scheduled / automated behaviour | VDR-U17-C394 VDR-U17-C395. |
| 9 Exception & failure behaviour | Constraint errors; no cost generation despite the cron name VDR-U17-C396; open-ended assignment history VDR-U17-C399. |
| 10 Accounting, stock, audit, security & compliance | Contract amounts stored but no posting in these modules VDR-U17-C396; driver identity linked to employee; history log for audit VDR-U17-C387. |

**DB reconciliation:** VDR-U17-C412; `hr_fleet.delay_alert_contract` parameter present.

**Unknown / Runtime list:** VDR-U17-C413; mail send wizard (`RT`).

## CAP-U17-10 Calendar events, attendees, invitations and reminders

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

**D1:** schedule meetings with attendees, invitations, accept/decline, privacy masking and reminders; HR bridge flags attendees outside working time; SMS reminders optional.

**D2:** `calendar.event`, `.attendee`, `.alarm`, `.recurrence`, `calendar.alarm_manager` (abstract), cron `Calendar: Event Reminder`, auth method `calendar`, controllers; bridges `hr_calendar`, `calendar_sms`; consumers `hr_holidays`, `hr_recruitment`.

**D3:** create -> attendees -> invitations -> alarms VDR-U17-C426 VDR-U17-C427 VDR-U17-C436; write -> change notification and alarm rebuild VDR-U17-C432 VDR-U17-C433 VDR-U17-C434; reminders VDR-U17-C437 VDR-U17-C438 VDR-U17-C439; privacy VDR-U17-C415 VDR-U17-C414 VDR-U17-C416; SMS override chain: `calendar.alarm_manager._send_reminder` base + `calendar_sms` VDR-U17-C441.

State diagram (list):
- attendee needsAction -> accepted [organiser default or accept link] VDR-U17-C419 VDR-U17-C425
- attendee needsAction|accepted -> declined [decline link or action] VDR-U17-C421
- accepted -> needsAction [organiser reset after time change by another user] VDR-U17-C433
- event active -> archived [archive or recurrence exception handling] VDR-U17-C434

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Create event with partners -> invitations with ICS -> reminders VDR-U17-C426 VDR-U17-C429 VDR-U17-C438. |
| 2 Reversal / cancel / negative path | Decline VDR-U17-C421; private-event write denial VDR-U17-C416; attendee copy refused VDR-U17-C422. |
| 3 Multi-company / data-scope | Employees see all events by rule, masked in code VDR-U17-C417 VDR-U17-C414; portal limited VDR-U17-C418; no company rule exists. |
| 4 Side effects & cross-module triggers | Leave meetings and interview meetings reuse events (CAP-U17-03, -07); availability bridge VDR-U17-C444 VDR-U17-C445 VDR-U17-C446. |
| 5 Configuration & optionality | Alarm types VDR-U17-C435 VDR-U17-C440; mail block parameter VDR-U17-C428; default privacy parameter (VDR-U17-C439). |
| 6 Validation & constraints | VDR-U17-C420 VDR-U17-C422 VDR-U17-C434. |
| 7 Roles & permissions | VDR-U17-C417 VDR-U17-C418 VDR-U17-C423 VDR-U17-C424; ACLs 15 rows (source = DB). |
| 8 Scheduled / automated behaviour | VDR-U17-C436 VDR-U17-C437 VDR-U17-C439. |
| 9 Exception & failure behaviour | Past alarms skipped by design VDR-U17-C436; force-send limit VDR-U17-C431; SMS failures not handled in this module VDR-U17-C440. |
| 10 Accounting, stock, audit, security & compliance | Token links act in sudo VDR-U17-C425; invitation mail contains personal data of attendees; private masking is code-level, not rule-level VDR-U17-C417. |

**DB reconciliation:** VDR-U17-C439.

**Unknown / Runtime list:** VDR-U17-C447; recurrence engine rules (not read); SMS gateway (`RT`); mail queue delivery (`RT`).

## Secondary coverage — presence, home-working, maintenance, gamification and bridges

**Scope:** lighter depth; each statement is pointer-backed.
- Presence: VDR-U17-C448 VDR-U17-C449 VDR-U17-C450 VDR-U17-C451 VDR-U17-C452.
- Home-working: VDR-U17-C453 VDR-U17-C454 VDR-U17-C455 VDR-U17-C456 VDR-U17-C457 VDR-U17-C458.
- Maintenance: VDR-U17-C459 VDR-U17-C460 VDR-U17-C461 VDR-U17-C462.
- Gamification: VDR-U17-C463 VDR-U17-C464 VDR-U17-C465 VDR-U17-C466 VDR-U17-C467 VDR-U17-C468 VDR-U17-C469.
- Bridges: VDR-U17-C470 VDR-U17-C471 VDR-U17-C472 VDR-U17-C473 VDR-U17-C474; organisation chart in CAP-U17-02.
- Unknown: VDR-U17-C475.

## Runtime / AWT-required list (`RT`)
VDR-U17-C258 crons and kiosk behaviour; VDR-U17-C273 geocoding; VDR-U17-C269 and VDR-U17-C270 public-route behaviour; VDR-U17-C355, VDR-U17-C440, VDR-U17-C441, VDR-U17-C442, VDR-U17-C443, VDR-U17-C451 SMS gateway; VDR-U17-C431 mail sending; VDR-U17-C224; VDR-U17-C279; VDR-U17-C090; VDR-U17-C447.

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U17-C001 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:39 | _name = 'hr.employee' | FACT | always | — | hr.employee is the employee model; it mixes in mail thread, activity, resource and avatar behaviour | N-U17-001 |
| VDR-U17-C002 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:45 | 'hr.version': 'version_id' | FACT | always | — | hr.employee delegation-inherits hr.version through version_id, so contract-like fields are read and written on a version record | N-U17-002 |
| VDR-U17-C003 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:50 | compute='_compute_version_id' | FACT | always | — | version_id is a non-stored computed field (compute_sudo, groups hr.group_hr_user) resolved from context key version_id or current_version_id | N-U17-002 |
| VDR-U17-C004 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:531 | date_version', '<=', fields.Date.today() | FACT | always | — | _compute_current_version_id picks the version with the latest date_version not after today, ordered date_version desc, limit 1 | N-U17-002 |
| VDR-U17-C005 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:538 | elif employee.version_ids | FACT | always | — | When no version is dated on or before today the first version of the employee becomes current | N-U17-002 |
| VDR-U17-C006 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:544 | _cron_update_current_version_id | FACT | always | — | A cron method recomputes current_version_id for all employees; this is how a future-dated version becomes current | N-U17-002 |
| VDR-U17-C007 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:507 | context.get('version_id' | FACT | always | — | A version_id context key selects an explicit version for the employee when that version belongs to the employee | N-U17-010 |
| VDR-U17-C008 | FUNCTION MAPPING REQUIRED | hr/data/hr_data.xml:163 | ir_cron_data_employee_update_current_version | OBSERVATION | restored DB | — | DB shows cron HR Employee: Update Current Version active, interval 1 day; HR Employee: Notify Expiring Contract or Work Permit also active at 1 day | N-U17-002 |
| VDR-U17-C009 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:202 | _check_unique_date_version | FACT | always | — | Unique index on (employee_id, date_version) where active and employee_id not null | N-U17-008 |
| VDR-U17-C010 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:197 | _check_contract_start_date_defined | FACT | always | — | SQL check: contract_date_end may be set only if contract_date_start is set | N-U17-008 |
| VDR-U17-C011 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:271 | already has a contract running | FACT | always | — | _check_dates raises when an active version's contract period overlaps another contract period of the same employee; start after end raises as well | N-U17-008 |
| VDR-U17-C012 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:299 | must always have at least one active version | FACT | always | — | Deleting the last version of an employee is refused by an ondelete guard | N-U17-007 |
| VDR-U17-C013 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:309 | Cannot archive all the active versions | FACT | always | — | write refuses archiving all versions of an employee; line 306 refuses unassigning all versions | N-U17-007 |
| VDR-U17-C014 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:316 | different contracts at once | FACT | always | — | Changing contract dates on versions that belong to different contract periods in one write is refused | N-U17-009 |
| VDR-U17-C015 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:325 | "date_version": vals["contract_date_start"] | FACT | always | — | When the employee has only one version, setting contract_date_start also moves date_version to that date | N-U17-009 |
| VDR-U17-C016 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:571 | def create_version | FACT | always | — | create_version(values) requires date_version, reuses the version in force at that date as the copy source and returns the existing version when the date matches | N-U17-009 |
| VDR-U17-C017 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:586 | if version_to_copy.date_version == date | FACT | always | — | Same-date request returns the existing version unchanged | N-U17-009 |
| VDR-U17-C018 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:630 | version_to_copy.sudo().copy_data()[0] | FACT | always | — | The copy source is read with sudo so users lacking field access can still create a version; requested changes are written afterwards without sudo | N-U17-009 |
| VDR-U17-C019 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:600 | sync_contract_dates=True | FACT | always | — | When contract end changes at version creation, sibling versions of the same contract are synchronised with sudo | N-U17-009 |
| VDR-U17-C020 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:645 | def create_contract | FACT | always | — | create_contract writes contract dates on a same-date version, else creates a version; end date is the day before the next contract start | N-U17-003 |
| VDR-U17-C021 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:248 | The Badge ID must be unique | FACT | always | — | SQL unique(barcode) on employees | N-U17-011 |
| VDR-U17-C022 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:252 | A user cannot be linked to multiple employees | FACT | always | — | SQL unique(user_id, company_id) | N-U17-011 |
| VDR-U17-C023 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1309 | The PIN must be a sequence of digits | FACT | always | — | Constraint on pin | N-U17-011 |
| VDR-U17-C024 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1316 | alphanumeric without any accents | FACT | always | — | Constraint: barcode matches ^[A-Za-z0-9]+$ and length at most 18 | N-U17-011 |
| VDR-U17-C025 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1386 | vals.update(self._sync_user | FACT | always | — | create with user_id copies work contact, picture and tz from the user and takes the user's name when name is missing | N-U17-004 |
| VDR-U17-C026 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1402 | _create_work_contacts | FACT | always | — | After create, employees without work_contact_id get contacts created with sudo | N-U17-014 |
| VDR-U17-C027 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1396 | super(HrEmployee, self.with_company(company)) | FACT | always | — | create is batched per company so the underlying version gets the right company in context | N-U17-010 |
| VDR-U17-C028 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1412 | _subscribe_users_automatically | FACT | always | — | Creating an employee in a department re-evaluates department-based automatic channel subscriptions | N-U17-017 |
| VDR-U17-C029 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1421 | onboarding plan | FACT | always | — | A log note with a link to the onboarding plan wizard is posted on every created employee | N-U17-017 |
| VDR-U17-C030 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1433 | vals.update(self._sync_user(user | FACT | always | — | write with user_id re-syncs contact, picture and tz and removes the work contact from other employees of that partner | N-U17-004 |
| VDR-U17-C031 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1443 | users_to_update.write({'tz' | FACT | always | — | Employee timezone changes are pushed to the linked user when the user's company matches | N-U17-004 |
| VDR-U17-C032 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1459 | bank_account.allow_out_payment = False | FACT | always | — | Changing work_contact_id re-points bank accounts to the new contact and clears allow_out_payment on moved accounts | N-U17-014 |
| VDR-U17-C033 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1468 | last_modified_uid | FACT | always | — | Version-held values are written in one call on version_id with last_modified_date and last_modified_uid, and a log note names the version | N-U17-010 |
| VDR-U17-C034 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1465 | self.resource_id.calendar_id = new_version.resource_calendar_id | FACT | always | — | When current_version_id changes the resource calendar follows the new version | N-U17-018 |
| VDR-U17-C035 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:84 | related='resource_id.name' | FACT | always | — | Employee name, active and user_id are related fields stored via the resource record | N-U17-018 |
| VDR-U17-C036 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1491 | return resources.unlink() | FACT | always | — | Deleting an employee deletes the linked resource | N-U17-018 |
| VDR-U17-C037 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1494 | return ['parent_id', 'coach_id'] | FACT | always | — | On archive, parent_id and coach_id on other employees pointing to the archived employee are emptied; modules can add fields through the two hook methods | N-U17-012 |
| VDR-U17-C038 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1530 | Register Departure | FACT | single employee archived without no_wizard context | — | Archiving exactly one employee returns the Register Departure wizard action | N-U17-005 |
| VDR-U17-C039 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1502 | 'departure_reason_id': False | FACT | always | — | Unarchive clears departure reason, description and date | N-U17-016 |
| VDR-U17-C040 | FUNCTION MAPPING REQUIRED | hr/wizard/hr_departure_wizard.py:78 | Departure date can't be earlier | FACT | always | — | The wizard refuses a departure date before the contract start of any current version | N-U17-013 |
| VDR-U17-C041 | FUNCTION MAPPING REQUIRED | hr/wizard/hr_departure_wizard.py:117 | active_versions.write({'contract_date_end' | FACT | set_date_end checked (default for HR officers) | — | Departure optionally writes contract_date_end on current versions that have a contract start | N-U17-005 |
| VDR-U17-C042 | FUNCTION MAPPING REQUIRED | hr/wizard/hr_departure_wizard.py:92 | related_employees_count.get(user, 0) | FACT | remove_related_user checked | — | A user is archived only when all its employees are in the wizard; others are reported as not archived | N-U17-013 |
| VDR-U17-C043 | FUNCTION MAPPING REQUIRED | hr/wizard/hr_departure_wizard.py:105 | archived_employees.with_context(no_wizard=True) | FACT | employee_termination context | — | Employees are archived (and users archived) only when the context key employee_termination is set | N-U17-005 |
| VDR-U17-C044 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:195 | default=lambda self: self.env.user | FACT | always | — | hr_responsible_id is required, defaults to the current user and is limited to non-share users with the HR officer group in the version's company | N-U17-015 |
| VDR-U17-C045 | FUNCTION MAPPING REQUIRED | hr/models/hr_department.py:118 | You cannot create recursive departments | FACT | always | — | Constraint on parent_id cycles | N-U17-019 |
| VDR-U17-C046 | FUNCTION MAPPING REQUIRED | hr/models/hr_department.py:139 | def _update_employee_manager | FACT | manager_id written | — | Changing a department manager re-points employees of that department whose parent was the old manager | N-U17-012 |
| VDR-U17-C047 | FUNCTION MAPPING REQUIRED | hr/models/hr_job.py:42 | _name_company_uniq | FACT | always | — | unique(name, company_id, department_id) on hr.job | N-U17-019 |
| VDR-U17-C048 | FUNCTION MAPPING REQUIRED | hr/models/hr_job.py:46 | _no_of_recruitment_positive | FACT | always | — | CHECK(no_of_recruitment >= 0) | N-U17-019 |
| VDR-U17-C049 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1187 | contract_expiration_notice_period | FACT | cron | — | The notice cron schedules to-do activities for contract end and work permit expiry that fall exactly at today plus the company's notice period, for the HR responsible or the cron user | N-U17-017 |
| VDR-U17-C050 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1543 | To avoid multi company issues | FACT | onchange | — | Onchange of company on an existing employee shows a warning recommending a new employee in the other company | N-U17-020 |
| VDR-U17-C051 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1050 | users_without_emails.append(employee.name) | FACT | always | — | Bulk user creation skips employees with an existing user, missing or invalid work email, email already used by a user, or duplicated among the selection, and reports each group | N-U17-020 |
| VDR-U17-C052 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1004 | Adding new users may increase your subscription cost | FACT | always | — | A redirect warning precedes bulk user creation and mentions the default user template rights | N-U17-017 |
| VDR-U17-C053 | FUNCTION MAPPING REQUIRED | hr/models/res_users.py:170 | create_employee_id | FACT | always | — | Creating a user with create_employee or create_employee_id creates or links an employee | N-U17-004 |
| VDR-U17-C054 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | — | Contract templates wizard, payroll structure types and country-specific HR extensions not read; read hr/wizard/hr_contract_template_wizard.py and l10n HR modules to resolve | N-U17-021 |
| VDR-U17-C055 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:10 | group_hr_user | FACT | always | — | Group Officer: Manage all employees implies base.group_user | N-U17-023 |
| VDR-U17-C056 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:18 | group_hr_manager | FACT | always | — | Group Administrator implies the officer group; root and admin users are members | N-U17-023 |
| VDR-U17-C057 | FUNCTION MAPPING REQUIRED | hr/security/ir.model.access.csv:4 | access_hr_employee_user | FACT | always | — | ACL on hr.employee: officer group has full CRUD | N-U17-023 |
| VDR-U17-C058 | FUNCTION MAPPING REQUIRED | hr/security/ir.model.access.csv:5 | access_hr_employee_system_user | FACT | always | — | ACL: base.group_system read only on hr.employee | N-U17-023 |
| VDR-U17-C059 | FUNCTION MAPPING REQUIRED | hr/security/ir.model.access.csv:6 | access_hr_employee_public_user | FACT | always | — | ACL: base.group_user read only on hr.employee.public; no ACL gives base.group_user access to hr.employee | N-U17-022 |
| VDR-U17-C060 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee_public.py:14 | _auto = False | FACT | always | — | hr.employee.public is a database view model, not a table | N-U17-022 |
| VDR-U17-C061 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee_public.py:200 | ON v.id = e.current_version_id | FACT | always | — | The view joins hr_employee to the current hr_version and selects stored public fields | N-U17-022 |
| VDR-U17-C062 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee_public.py:189 | version_fields[name].store | FACT | always | — | _get_fields takes a column from hr_version when the field is a stored version field, else from hr_employee | N-U17-022 |
| VDR-U17-C063 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1113 | HACK: retrieve publicly available values | FACT | user lacks read on hr.employee | — | search_fetch and fetch fall back to hr.employee.public and copy values into the private model cache | N-U17-025 |
| VDR-U17-C064 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1164 | not available for employee public profiles | FACT | user lacks read on hr.employee | — | Requesting a field that is absent from the public model raises AccessError | N-U17-025 |
| VDR-U17-C065 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1241 | if self.browse().has_access('read') or bypass_access | FACT | user lacks read on hr.employee | — | _search is served by hr.employee.public and the ids are re-browsed on hr.employee | N-U17-025 |
| VDR-U17-C066 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1224 | We can redirect you to the public employee list | FACT | user lacks read on hr.employee | — | get_views raises RedirectWarning to the public employee list instead of building private views | N-U17-025 |
| VDR-U17-C067 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:129 | Private Phone | FACT | always | — | Private contact, birthday, bank, permit, visa, emergency, barcode, pin and ID scan fields carry groups hr.group_hr_user | N-U17-026 |
| VDR-U17-C068 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:184 | contract_wage | FACT | always | — | Contract dates, wage, structure type and contract type on the employee carry groups hr.group_hr_manager | N-U17-026 |
| VDR-U17-C069 | FUNCTION MAPPING REQUIRED | hr/models/hr_version.py:78 | SSN No | FACT | always | — | ssnid and passport fields on hr.version carry groups hr.group_hr_user | N-U17-026 |
| VDR-U17-C070 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:31 | ('parent_id.user_id', '=', user.id) | FACT | always | — | Global rule on hr.employee: company in company_ids or False, or manager user is the user, or id is the user's employee's parent, or user is the employee's user | N-U17-027 |
| VDR-U17-C071 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:48 | ('parent_id.user_id', '=', user.id) | FACT | always | — | The same four-way domain applies to hr.employee.public | N-U17-027 |
| VDR-U17-C072 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:42 | company_ids + [False] | FACT | always | — | Departments and jobs are scoped by company_ids plus no-company records | N-U17-027 |
| VDR-U17-C073 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:114 | [('company_id', 'in', company_ids)] | FACT | always | — | hr.version is scoped by company_ids; the HR administrator group has a second rule with domain true | N-U17-028 |
| VDR-U17-C074 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:64 | [('partner_id.employee_ids', '=', False)] | FACT | always | — | Internal users cannot access bank accounts of partners that have employees; HR officers get an unrestricted rule | N-U17-029 |
| VDR-U17-C075 | FUNCTION MAPPING REQUIRED | hr/models/res_users.py:121 | HR_WRITABLE_FIELDS | FACT | always | — | SELF_READABLE_FIELDS and SELF_WRITEABLE_FIELDS include a list of private contact, emergency, bank, barcode, pin and work fields so users can edit their own data on preferences | N-U17-030 |
| VDR-U17-C076 | FUNCTION MAPPING REQUIRED | hr/models/res_users.py:222 | Personal information update | FACT | user writes employee-related fields | — | A message is notified to the version's HR responsible listing modified fields | N-U17-030 |
| VDR-U17-C077 | FUNCTION MAPPING REQUIRED | hr/models/hr_mixin.py:20 | _allow_read_hr_employee | FACT | models using hr.mixin | — | hr.mixin passes a sentinel context so many2many links to hr.employee work for users without read access | N-U17-034 |
| VDR-U17-C078 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:1154 | _allow_read_hr_employee | FACT | sentinel in context | — | _check_access returns for read when the sentinel is present | N-U17-034 |
| VDR-U17-C079 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee_public.py:115 | child_of | FACT | always | — | is_manager is true for employees in the child_of tree of the user's employee | N-U17-031 |
| VDR-U17-C080 | FUNCTION MAPPING REQUIRED | hr_org_chart/models/hr_org_chart_mixin.py:24 | the CEO is manager of everyone | FACT | hr_org_chart installed | — | _get_subordinates excludes already-visited parents so a cyclic hierarchy terminates | N-U17-031 |
| VDR-U17-C081 | FUNCTION MAPPING REQUIRED | hr_org_chart/models/hr_org_chart_mixin.py:49 | subordinates = self.env.user.employee_id.subordinate_ids | FACT | hr_org_chart installed | — | is_subordinate is computed against the current user's employee | N-U17-031 |
| VDR-U17-C082 | FUNCTION MAPPING REQUIRED | hr_org_chart/controllers/hr_org_chart.py:21 | request.env['hr.employee.public'] | FACT | hr_org_chart installed | — | The org chart controller uses hr.employee.public, checks read access per employee, then reads job and ancestors with sudo | N-U17-031 |
| VDR-U17-C083 | FUNCTION MAPPING REQUIRED | hr_org_chart/controllers/hr_org_chart.py:10 | _managers_level = 5 | FACT | hr_org_chart installed | — | Manager chain is limited to five levels by default | N-U17-031 |
| VDR-U17-C084 | FUNCTION MAPPING REQUIRED | hr_hourly_cost/models/hr_employee.py:9 | hourly_cost = fields.Monetary | FACT | hr_hourly_cost installed | — | hourly_cost on hr.employee carries groups hr.group_hr_user and is tracked | N-U17-033 |
| VDR-U17-C085 | FUNCTION MAPPING REQUIRED | hr/models/resource.py:41 | public_employees | FACT | non HR user | — | resource avatar for non-HR users is read from hr.employee.public | N-U17-024 |
| VDR-U17-C086 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:208 | employee.pin == pin_code | INFERENCE | kiosk request | — | Kiosk routes use sudo() on hr.employee and read private fields (pin, barcode) with elevated rights; see CAP-U17-05 | N-U17-036 |
| VDR-U17-C087 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:33 | ('parent_id.user_id', '=', user.id) | INFERENCE | multi-company | — | Because the manager and own-record branches are OR-ed with the company branch, an employee of a company outside company_ids stays visible to the manager user and to the employee's own user | N-U17-035 |
| VDR-U17-C088 | FUNCTION MAPPING REQUIRED | hr/security/ir.model.access.csv:2 | access_hr_employee_category_user | OBSERVATION | restored DB | — | DB holds 26 hr ACL rows (source csv 26), 13 hr rules (source 13), 2 groups (source 2); hr.employee has one global rule with 4-way domain; hr.job ACL access_hr_job_user is overridden by hr_recruitment so officer group has read only while recruitment officers have full CRUD | N-U17-023 |
| VDR-U17-C089 | FUNCTION MAPPING REQUIRED | hr/data/hr_data.xml:154 | ir_cron_data_employee_notify_expiring_contract_work_permit | OBSERVATION | restored DB | — | DB holds 1 employee, 1 version, 1 department, 0 jobs, 12 contract types, 3 departure reasons, 3 work locations; HR administrator group has 2 members (counts only) | N-U17-001 |
| VDR-U17-C090 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Portal or external access to employee records and multi-company switching behaviour in the web client not exercised; runtime test required | N-U17-037 |
| VDR-U17-C091 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:132 | ('validate1', 'Second Approval') | FACT | always | — | hr.leave.state selection is confirm (To Approve), refuse, validate1 (Second Approval), validate (Approved), cancel; default confirm | N-U17-055 |
| VDR-U17-C092 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_type.py:88 | ('no_validation', 'None needed') | FACT | always | — | leave_validation_type selection no_validation, hr, manager, both; default hr | N-U17-039 |
| VDR-U17-C093 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_type.py:92 | requires_allocation = fields.Boolean(default=True | FACT | always | — | Type switches: requires_allocation (default true), employee_requests, request_unit day/half_day/hour, unpaid, include_public_holidays_in_duration, support_document, allow_request_on_top, allows_negative with max_allowed_negative, create_calendar_meeting | N-U17-039 |
| VDR-U17-C094 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:155 | default=lambda self: self.env.user.employee_id | FACT | always | — | employee_id is required, restrict on delete and defaults to the current user's employee | N-U17-042 |
| VDR-U17-C095 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:515 | has_group('hr_holidays.group_hr_holidays_user') | FACT | always | — | Non-officers can pick only employees whose user is themselves or whose leave_manager_id is themselves, among active employees of their companies | N-U17-042 |
| VDR-U17-C096 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:938 | There is no employee set on the time off | FACT | always | — | create raises UserError when employee_id is missing | N-U17-042 |
| VDR-U17-C097 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:960 | The time off has been automatically approved | FACT | validation_type no_validation and not leave_fast_create | — | create calls action_approve in sudo, subscribes the responsible and posts a comment | N-U17-042 |
| VDR-U17-C098 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:962 | holiday_sudo.activity_update() | FACT | other validation types, not import | — | create schedules approval activities through activity_update | N-U17-042 |
| VDR-U17-C099 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:943 | holidays._check_validity() | FACT | always | — | create runs _compute_duration and _check_validity right after super().create | N-U17-044 |
| VDR-U17-C100 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:344 | An employee already booked time off which overlaps | FACT | type allow_request_on_top false | — | _compute_dashboard_warning_message lists overlapping requests not cancelled or refused for the same employee | N-U17-043 |
| VDR-U17-C101 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:796 | raise ValidationError(holiday.dashboard_warning_message) | FACT | state not refuse or cancel | — | _check_date turns the warning into a blocking ValidationError unless leave_skip_date_check context | N-U17-043 |
| VDR-U17-C102 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:822 | You do not have any allocation for this time off type | FACT | requires_allocation true | — | _check_validity refuses a request when max_leaves is zero | N-U17-044 |
| VDR-U17-C103 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:824 | < -max_excess | FACT | allows_negative | — | With a negative cap the request is refused when virtual_remaining_leaves falls below minus max_allowed_negative | N-U17-044 |
| VDR-U17-C104 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:847 | You are not allowed to request time off on a Mandatory Day | FACT | user not in time off officer group | — | Non-officers cannot book a mandatory day | N-U17-045 |
| VDR-U17-C105 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:563 | ('department_ids', 'parent_of', department_ids) | FACT | always | — | Mandatory days match by company, optional calendar, optional department (parent_of) and job | N-U17-045 |
| VDR-U17-C106 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:804 | This modification is not allowed in the current state | FACT | state validate1 or validate | — | Changing dates or employee of an approved or second-approval request raises unless leave_skip_state_check | N-U17-050 |
| VDR-U17-C107 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:445 | A leave cannot be set across multiple versions | FACT | always | — | _check_contracts raises when versions overlapping the request have more than one resource_calendar | N-U17-046 |
| VDR-U17-C108 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1282 | are not supposed to work during that period | FACT | validation | — | _action_validate raises when a request has employee and zero days; hr_work_entry_holidays exempts three work entry codes | N-U17-046 |
| VDR-U17-C109 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1199 | leave_to_approve.write({'state': 'validate1' | FACT | validation_type both | — | action_approve moves both-type requests to validate1 with first_approver_id, others go to _action_validate | N-U17-047 |
| VDR-U17-C110 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1284 | self.write({'state': 'validate'}) | FACT | always | — | _action_validate writes state validate and the approver ids then creates resource leaves | N-U17-040 |
| VDR-U17-C111 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1295 | leaves_second_approver.write | FACT | always | — | second_approver_id is set for both-type requests, else first_approver_id | N-U17-047 |
| VDR-U17-C112 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1306 | must be confirmed or validated in order to refuse | FACT | always | — | action_refuse accepts confirm, validate, validate1 only | N-U17-055 |
| VDR-U17-C113 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1313 | self.mapped('meeting_id').write({'active': False}) | FACT | always | — | Refuse archives the calendar meeting and cleans approval activities | N-U17-048 |
| VDR-U17-C114 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1332 | Refused Time Off | FACT | both validated or manager validated | — | _notify_manager notifies the leave manager that an approved request was refused | N-U17-048 |
| VDR-U17-C115 | FUNCTION MAPPING REQUIRED | hr_holidays/wizard/hr_holidays_cancel_leave.py:14 | self.leave_id._action_user_cancel(self.reason) | FACT | always | — | The cancel wizard passes an optional reason to _action_user_cancel | N-U17-048 |
| VDR-U17-C116 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1345 | This time off cannot be cancelled | FACT | always | — | _action_user_cancel requires can_cancel | N-U17-047 |
| VDR-U17-C117 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1393 | leave_sudo.state = "cancel" | FACT | always | — | _force_cancel sets state cancel in sudo, posts the reason and notifies responsibles by validation type and state | N-U17-048 |
| VDR-U17-C118 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1398 | self.meeting_id.active = False | FACT | always | — | _post_leave_cancel archives the meeting and removes the resource calendar leave | N-U17-048 |
| VDR-U17-C119 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1412 | def _get_next_states_by_state | FACT | always | — | _get_next_states_by_state builds the transition matrix from validation type, officer, own-leave and approver status | N-U17-047 |
| VDR-U17-C120 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1430 | is_own_leave and (not is_in_past or is_officer) | FACT | always | — | Employees may cancel own validate1, validate and refuse requests unless in the past (officers always) | N-U17-047 |
| VDR-U17-C121 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1441 | state_result['validate1'].update | FACT | officer | — | Officers can move between confirm, validate1, validate, refuse and cancel states in most directions | N-U17-047 |
| VDR-U17-C122 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1476 | A cancelled leave cannot be modified | FACT | non-superuser | — | _check_approval_update refuses any change from cancel | N-U17-055 |
| VDR-U17-C123 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1482 | reset a leave | FACT | target state confirm not allowed by matrix | — | Plain users cannot reset; message says to cancel or delete and create another | N-U17-047 |
| VDR-U17-C124 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1474 | State Approve is only used for leave needed 2 approvals | FACT | always | — | validate1 target is refused unless validation_type is both | N-U17-047 |
| VDR-U17-C125 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1099 | holidays._create_resource_leave() | FACT | on validation | — | _validate_leave_request creates sudo resource.calendar.leaves for each approved leave | N-U17-040 |
| VDR-U17-C126 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1059 | 'holiday_id': self.id | FACT | always | — | The resource leave links holiday_id, resource, calendar, time_type and elligible_for_accrual_rate | N-U17-040 |
| VDR-U17-C127 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1100 | create_calendar_meeting | FACT | type flag true | — | A calendar.event is created in sudo per approved leave of those types | N-U17-040 |
| VDR-U17-C128 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1160 | 'privacy': 'confidential' | FACT | always | — | Leave meeting values set privacy confidential, attendee is the user's partner or the work contact | N-U17-040 |
| VDR-U17-C129 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1111 | no_mail_to_attendees=True | FACT | always | — | Meetings are created without invitation mail and without video call | N-U17-040 |
| VDR-U17-C130 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:978 | validated_leaves._remove_resource_leave() | FACT | state moves away from validate | — | write removes the resource leave of leaves leaving validate state; date changes on validated leaves amend it | N-U17-048 |
| VDR-U17-C131 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:971 | must have manager rights to modify/validate a time off that already begun | FACT | non-officer, leave started | — | Non-officer who is not leave manager cannot write a started leave | N-U17-050 |
| VDR-U17-C132 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:973 | Only a manager can modify a canceled leave | FACT | non-officer | — | Cancelled leaves are editable by officers only | N-U17-050 |
| VDR-U17-C133 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1016 | can only be deleted by Administrators | FACT | always | — | Ondelete guard: non-officers only confirm, validate1 or cancel and not in the past; officers non-admin only cancel or confirm | N-U17-049 |
| VDR-U17-C134 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1025 | in the past | FACT | non-officer | — | Deleting a leave that started before today is refused for non-officers | N-U17-049 |
| VDR-U17-C135 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1042 | A time off cannot be duplicated | FACT | state not cancel or refuse | — | copy_data refuses duplicates of active leaves | N-U17-050 |
| VDR-U17-C136 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1539 | def _get_responsible_for_approval | FACT | always | — | Responsible is leave_manager_id, else the manager's user, else the type's responsible_ids (manager or both-at-confirm), or the type's responsible_ids for hr and second step | N-U17-042 |
| VDR-U17-C137 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1566 | mail_act_leave_approval | FACT | always | — | activity_update creates approval or second-approval activities with deadline date_from minus activity delay and clears them on validate, refuse or cancel | N-U17-042 |
| VDR-U17-C138 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1683 | inspected_date = fields.Date.today() + timedelta(days=31) | FACT | cron | — | _cancel_invalid_leaves inspects confirm, validate1, validate leaves starting in the next 31 days that use accrual types | N-U17-054 |
| VDR-U17-C139 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1704 | the accruated amount is insufficient for that duration | FACT | cron | — | Leaves with zero max_leaves or excess above the allowed negative are force-cancelled with a note | N-U17-054 |
| VDR-U17-C140 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:679 | days = ceil(days) | FACT | request unit day | — | Day-unit types round durations up | N-U17-038 |
| VDR-U17-C141 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:624 | is_fully_flexible | FACT | flexible employee | — | Flexible employees use real elapsed hours minus public holidays | N-U17-038 |
| VDR-U17-C142 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:598 | include_public_holidays_in_duration | FACT | always | — | Public-holiday inclusion is per type and selects compute_leaves in the work-time computation | N-U17-038 |
| VDR-U17-C143 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_employee.py:162 | def _compute_leave_manager | FACT | always | — | leave_manager_id is computed from parent_id.user_id and follows the manager when it was equal to the previous manager | N-U17-058 |
| VDR-U17-C144 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_employee.py:230 | leave_manager.sudo().write({'group_ids' | FACT | write with leave_manager_id | — | Naming a leave manager adds the user to the Time Off Responsible group in sudo | N-U17-058 |
| VDR-U17-C145 | FUNCTION MAPPING REQUIRED | hr_holidays/models/res_users.py:63 | Command.unlink(self.env.ref(approver_group).id) | FACT | user no longer leave manager | — | _clean_leave_responsible_users removes the group from users who no longer approve anyone | N-U17-058 |
| VDR-U17-C146 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_employee.py:276 | ['leave_manager_id'] | FACT | always | — | Archiving an employee empties leave_manager_id on other employees pointing to that user | N-U17-058 |
| VDR-U17-C147 | FUNCTION MAPPING REQUIRED | hr_holidays/models/resource.py:56 | def _reevaluate_leaves | FACT | public holiday create write unlink | — | Recomputes number_of_days of overlapping leaves, re-checks validity and refunds or charges days with a note | N-U17-052 |
| VDR-U17-C148 | FUNCTION MAPPING REQUIRED | hr_holidays/models/resource.py:90 | has been set to refused | FACT | allocation insufficient after change | — | Leaves failing validity after a public holiday change are refused via action_refuse | N-U17-052 |
| VDR-U17-C149 | FUNCTION MAPPING REQUIRED | hr_holidays/models/resource.py:37 | Two public holidays cannot overlap | FACT | always | — | Constraint on company-level resource leaves with same company and calendar | N-U17-052 |
| VDR-U17-C150 | FUNCTION MAPPING REQUIRED | hr_holidays/models/resource.py:147 | self._reevaluate_leaves(time_domain_dict) | FACT | always | — | create, write and unlink on resource.calendar.leaves all call _reevaluate_leaves | N-U17-052 |
| VDR-U17-C151 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_version.py:61 | Changing the contract on this employee changes their working schedule | FACT | schedule or contract date change | — | hr.version create and write re-split overlapping leaves and raise a ValidationError when balances no longer cover recalculated durations | N-U17-052 |
| VDR-U17-C152 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_employee.py:250 | Changing this working schedule results in the affected employee | FACT | resource_calendar_id written | — | Employee schedule write re-computes future leaves and revalidates approved ones | N-U17-052 |
| VDR-U17-C153 | FUNCTION MAPPING REQUIRED | hr_holidays/wizard/hr_departure_wizard.py:40 | leaves_to_cancel._force_cancel(cancel_msg | FACT | departure registered | — | Approved or second-approval future leaves are force-cancelled without notifying responsibles | N-U17-053 |
| VDR-U17-C154 | FUNCTION MAPPING REQUIRED | hr_holidays/wizard/hr_departure_wizard.py:43 | leaves_to_delete.with_context(leave_skip_state_check=True).unlink() | FACT | departure registered | — | Other future leaves are deleted | N-U17-053 |
| VDR-U17-C155 | FUNCTION MAPPING REQUIRED | hr_holidays/wizard/hr_departure_wizard.py:23 | _split_leaves | FACT | departure registered | — | Leaves spanning the departure date are split at the day after departure | N-U17-053 |
| VDR-U17-C156 | FUNCTION MAPPING REQUIRED | hr_holidays/models/res_company.py:22 | The company country cannot be changed while time off | FACT | not in tests | — | Company country change is refused while leaves or allocations with another country exist | N-U17-059 |
| VDR-U17-C157 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_type.py:251 | cannot be changed once leaves of that type have been taken | FACT | not install mode | — | requires_allocation cannot change when any leave of the type exists | N-U17-059 |
| VDR-U17-C158 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:236 | The start date must be before or equal to the end date | FACT | always | — | SQL checks date_from <= date_to, request dates ordered and number_of_days >= 0 | N-U17-059 |
| VDR-U17-C159 | FUNCTION MAPPING REQUIRED | hr_holidays/controllers/main.py:10 | /leave/approve | FACT | always | — | Routes /leave/approve, /leave/validate, /leave/refuse, /allocation/validate, /allocation/refuse are auth user, GET, and call action_approve or action_refuse after a token check | N-U17-051 |
| VDR-U17-C160 | FUNCTION MAPPING REQUIRED | hr_holidays/controllers/main.py:16 | except Exception | FACT | always | — | Any exception on approval is swallowed and the user is redirected to the generic fallback | N-U17-060 |
| VDR-U17-C161 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_leave.py:129 | self.sudo()._cancel_work_entry_conflict() | FACT | hr_work_entry_holidays installed | — | Validating a leave creates leave work entries and archives overlapping non-validated entries that are inside the leave | N-U17-057 |
| VDR-U17-C162 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_leave.py:87 | included.filtered(lambda entry: entry.state != 'validated').write({'active': False}) | FACT | hr_work_entry_holidays installed | — | Entries wholly inside the leave are deactivated | N-U17-057 |
| VDR-U17-C163 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_leave.py:138 | self._regen_work_entries() | FACT | hr_work_entry_holidays installed | — | Refuse, return to approval and user cancel regenerate attendance work entries for the dates of the leave entries | N-U17-057 |
| VDR-U17-C164 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_leave.py:175 | leave.can_cancel = leave.id not in leave_ids | FACT | hr_work_entry_holidays installed | — | can_cancel is false when a validated work entry references the leave | N-U17-057 |
| VDR-U17-C165 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_work_entry.py:17 | filtered(lambda l: l.state != 'refuse').action_refuse() | FACT | hr_work_entry_holidays installed | — | Cancelling a leave work entry refuses its leave | N-U17-115 |
| VDR-U17-C166 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_leave.py:125 | 'LEAVE110', 'LEAVE210', 'LEAVE280' | FACT | hr_work_entry_holidays installed | — | Leaves whose type maps to these work entry codes are exempt from the zero-day validation block | N-U17-046 |
| VDR-U17-C167 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_leave.py:53 | You do not have enough extra hours to request this leave | FACT | type overtime_deductible and no allocation | — | Create, write and approve check the compensable overtime balance | N-U17-057 |
| VDR-U17-C168 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_leave.py:58 | super().action_reset_confirm() | INFERENCE | hr_holidays_attendance installed | — | action_reset_confirm calls super but grep over odoo/addons finds no other definition or caller of this method, so invoking it would fail with AttributeError | N-U17-061 |
| VDR-U17-C169 | FUNCTION MAPPING REQUIRED | hr_holidays/security/ir.model.access.csv:4 | access_hr_holidays_employee_request | FACT | always | — | ACL gives base.group_user full CRUD on hr.leave and hr.leave.allocation; limits come from record rules | N-U17-049 |
| VDR-U17-C170 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:37 | [('employee_id.user_id', '=', user.id)] | FACT | always | — | Internal users read own leaves | N-U17-047 |
| VDR-U17-C171 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:51 | ('state', 'not in', ['validate', 'validate1']) | FACT | always | — | Internal users create or edit own leaves not yet approved, or leaves of employees they approve for types with manager, both or no validation | N-U17-047 |
| VDR-U17-C172 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:64 | ['confirm', 'validate1'] | FACT | always | — | Internal users delete own leaves only in confirm or validate1 | N-U17-049 |
| VDR-U17-C173 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:76 | ('employee_id.leave_manager_id', '=', user.id) | FACT | always | — | Responsible group reads leaves of employees where it is the leave manager | N-U17-047 |
| VDR-U17-C174 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:102 | [(1, '=', 1)] | FACT | always | — | Officer group reads all; write rule excludes own validated leaves; Administrator has an all-access rule | N-U17-047 |
| VDR-U17-C175 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:136 | [('company_id', 'in', company_ids)] | FACT | always | — | Global company rule on hr.leave | N-U17-059 |
| VDR-U17-C176 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:264 | ('country_id', 'in', user.env.companies.country_id.ids + [False]) | FACT | always | — | Leave types are visible when their company is allowed, or when company is empty and country is empty or among the user's companies' countries | N-U17-039 |
| VDR-U17-C177 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:259 | hr_holidays_status_rule_multi_company | OBSERVATION | restored DB | — | DB: company country TH; 73 time off types seeded, six have no country and the rest are tied to other countries so only the six are visible to a TH company; 0 leaves; 26 holiday rules (source 26), 27 ACL (source 27), 3 groups, 2 crons active | N-U17-039 |
| VDR-U17-C178 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Generate-multiple wizards, inbound email handling and external calendar sync for time off not read in depth; read hr_holidays/wizard and run tests | N-U17-062 |
| VDR-U17-C179 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:61 | ('validate1', 'Second Approval') | FACT | always | — | hr.leave.allocation.state selection confirm, refuse, validate1, validate; default confirm; no cancel state | N-U17-076 |
| VDR-U17-C180 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:119 | ('accrual', 'Accrual Allocation') | FACT | always | — | allocation_type regular or accrual, accrual_plan_id inverse sets the type | N-U17-063 |
| VDR-U17-C181 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:133 | allocation_type='regular' | FACT | always | — | SQL check: regular allocations need number_of_days > 0 | N-U17-068 |
| VDR-U17-C182 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:140 | must be anterior to the End Date | FACT | always | — | date_from after date_to raises UserError | N-U17-068 |
| VDR-U17-C183 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:815 | Incorrect state for new allocation | FACT | always | — | create refuses any state other than confirm | N-U17-067 |
| VDR-U17-C184 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:833 | allocation.action_approve() | FACT | allocation_validation_type no_validation | — | create approves automatically | N-U17-067 |
| VDR-U17-C185 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:911 | allocation_to_approve.write({'state': 'validate1' | FACT | always | — | action_approve writes validate1 with approver_id or calls _action_validate when can_validate | N-U17-067 |
| VDR-U17-C186 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:922 | 'second_approver_id': current_employee.id | FACT | always | — | _action_validate stamps approver and second approver | N-U17-067 |
| VDR-U17-C187 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:932 | must be confirmed, second approval or validated in order to refuse | FACT | always | — | action_refuse allowed from confirm, validate1, validate | N-U17-076 |
| VDR-U17-C188 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:951 | Only a time off Administrator can approve/refuse their own requests | FACT | type needs validation, user not administrator | — | An employee cannot approve or refuse own allocation unless administrator | N-U17-067 |
| VDR-U17-C189 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:746 | state_result['confirm'].add('validate') | FACT | no_validation | — | _get_next_states_by_state allows confirm to validate for no_validation types and mirrors the leave matrix otherwise | N-U17-067 |
| VDR-U17-C190 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:869 | You cannot reduce the duration below the duration of leaves already taken | FACT | number_of_days changed | — | write compares excess before and after and raises unless within negative cap | N-U17-068 |
| VDR-U17-C191 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:880 | You cannot delete an allocation request which is in %s state | FACT | not allocation_skip_state_check | — | Only confirm or refuse allocations can be deleted | N-U17-069 |
| VDR-U17-C192 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:885 | which has some validated leaves | FACT | requires_allocation type | — | Allocations with leaves_taken > 0 cannot be deleted | N-U17-069 |
| VDR-U17-C193 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:683 | ('allocation_type', '=', 'accrual'), ('state', '=', 'validate') | FACT | cron | — | _update_accrual selects validate accrual allocations with plan and employee, not past date_to, whose nextcall is empty or due, and runs _process_accrual_plans | N-U17-070 |
| VDR-U17-C194 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:472 | This allocation have already ran once | FACT | first run when nextcall empty | — | First run initialises lastcall and nextcall (adjusted for carry-over and level transition) and logs a message that later configuration changes will not alter allocated days | N-U17-070 |
| VDR-U17-C195 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:508 | while allocation.nextcall <= date_to | FACT | always | — | Missed periods are replayed in a loop until nextcall passes today | N-U17-070 |
| VDR-U17-C196 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:437 | period_prorata | FACT | partial period and not worked-time plan | — | Partial periods are prorated by call days over period days | N-U17-071 |
| VDR-U17-C197 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:432 | added_value / self.employee_id._get_hours_per_day | FACT | level in hours | — | Hour amounts are converted to days with the employee's hours per day | N-U17-071 |
| VDR-U17-C198 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:411 | if level.frequency in level._get_hourly_frequencies() | FACT | hourly frequency or worked-time plan | — | Prorata uses worked hours, eligible leave hours and non-eligible leave hours from the calendar | N-U17-071 |
| VDR-U17-C199 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:341 | maximum_leave_yearly | FACT | cap flags on level | — | Yearly cap uses yearly_accrued_amount; balance cap uses leaves_taken plus maximum_leave | N-U17-072 |
| VDR-U17-C200 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:322 | carryover_time == 'year_start' | FACT | always | — | Carry-over date is start of year, allocation anniversary or custom day and month | N-U17-073 |
| VDR-U17-C201 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:584 | allocation_max_days | FACT | carry-over date reached | — | Unused time is lost or limited to postpone_max_days; sets expiring_carryover_days | N-U17-073 |
| VDR-U17-C202 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:563 | expiring_days = max(0, allocation.expiring_carryover_days - leaves_taken) | FACT | accrual_validity on level | — | Only unused expiring days are removed on the expiration date | N-U17-073 |
| VDR-U17-C203 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:366 | date > self.date_from + get_timedelta(level.start_count, level.start_type) | FACT | always | — | Level chosen by elapsed time since date_from; transition immediately or end_of_accrual | N-U17-074 |
| VDR-U17-C204 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_accrual_plan.py:26 | transition_mode | FACT | always | — | Plan fields: transition_mode, accrued_gain_time start or end, is_based_on_worked_time, carryover_date year_start, allocation or other | N-U17-064 |
| VDR-U17-C205 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_accrual_plan_level.py:49 | ('bimonthly', 'Twice a month') | FACT | always | — | Level frequency hourly, daily, weekly, bimonthly, monthly, biyearly, yearly | N-U17-064 |
| VDR-U17-C206 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_accrual_plan_level.py:150 | You can not start an accrual in the past | FACT | always | — | SQL: start_count > 0 only with milestone after; creation needs start_count 0 | N-U17-075 |
| VDR-U17-C207 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_accrual_plan_level.py:154 | You must give a rate greater than 0 | FACT | always | — | added_value must be greater than zero | N-U17-075 |
| VDR-U17-C208 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_accrual_plan_level.py:158 | You cannot have a maximum quantity to carryover set to 0 | FACT | always | — | SQL checks on postpone_max_days, accrual validity count and yearly cap amount | N-U17-075 |
| VDR-U17-C209 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_accrual_plan.py:167 | linked to an existing allocation | FACT | always | — | A plan used by non-cancelled allocations cannot be deleted | N-U17-075 |
| VDR-U17-C210 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_type.py:131 | The maximum excess amount should be greater than 0 | FACT | always | — | SQL check NOT allows_negative OR max_allowed_negative > 0 | N-U17-080 |
| VDR-U17-C211 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_type.py:174 | You cannot allow requests on top of leaves of type 'Absence' | FACT | always | — | allow_request_on_top is forbidden for time_type leave; worked-time types must be eligible for accrual | N-U17-080 |
| VDR-U17-C212 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_type.py:235 | alloc.allocation_type == 'accrual' | FACT | always | — | has_valid_allocation is true for types without allocation need, or when an accrual or positive-balance allocation covers the dates | N-U17-065 |
| VDR-U17-C213 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_employee.py:415 | def _get_consumed_leaves | FACT | always | — | _get_consumed_leaves distributes confirm, validate1 and validate leaves over validated allocations and returns per-allocation and excess data | N-U17-065 |
| VDR-U17-C214 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_employee.py:272 | allocations.write(hr_vals) | FACT | parent or department changed | — | Manager and department changes are written to allocations in confirm state and to future or pending leaves | N-U17-079 |
| VDR-U17-C215 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_version.py:100 | Hour-based allocations store their duration | FACT | schedule change | — | number_of_days is recomputed from number_of_hours_display when the schedule changes | N-U17-078 |
| VDR-U17-C216 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_leave_allocation.py:68 | level.frequency != 'worked_hours' | FACT | hr_holidays_attendance installed | — | worked_hours frequency sums attendance worked hours in the window | N-U17-077 |
| VDR-U17-C217 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_leave_accrual_plan_level.py:21 | You can't base accrued time on hours worked | FACT | accrued_gain_time start | — | worked_hours frequency is refused when accrual is at period start | N-U17-075 |
| VDR-U17-C218 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_employee.py:14 | ('compensable_as_leave', '=', True) | FACT | hr_holidays_attendance installed | — | Deductible pool = approved compensable overtime minus non-cancelled overtime-deductible leave hours minus overtime-deductible allocation hours | N-U17-077 |
| VDR-U17-C219 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_leave_allocation.py:64 | The employee does not have enough overtime hours | FACT | overtime_deductible type | — | Allocation create and write verify the pool is not negative | N-U17-081 |
| VDR-U17-C220 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_leave_type.py:60 | 'overtime_deductible': True | FACT | type overtime_deductible without allocation need | — | get_allocation_data appends a synthetic balance from the overtime pool | N-U17-077 |
| VDR-U17-C221 | FUNCTION MAPPING REQUIRED | hr_holidays/security/hr_holidays_security.xml:153 | ('employee_id.leave_manager_id', '=', user.id) | FACT | always | — | Allocation rules: employees read own or managed allocations, write only own in confirm; officers read all; administrator all; company rule includes type company | N-U17-067 |
| VDR-U17-C222 | FUNCTION MAPPING REQUIRED | hr_holidays/security/ir.model.access.csv:20 | access_hr_leave_accrual_plan_user | FACT | always | — | Accrual plan and level ACL: officer read only, administrator full | N-U17-064 |
| VDR-U17-C223 | FUNCTION MAPPING REQUIRED | hr_holidays/data/ir_cron_data.xml:8 | model._update_accrual() | OBSERVATION | restored DB | — | DB: accrual cron active daily; 0 allocations and 0 accrual plans; 6 cron-owned time off types visible to the TH company | N-U17-070 |
| VDR-U17-C224 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Numeric results of accrual cases (proration, caps, carry-over) cannot be asserted without execution | N-U17-082 |
| VDR-U17-C225 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:28 | _name = 'hr.attendance' | FACT | always | — | hr.attendance records employee_id, check_in, check_out, worked_hours, overtime_hours, overtime_status, validated_overtime_hours, geolocation and in or out mode | N-U17-083 |
| VDR-U17-C226 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:77 | ('auto_check_out', 'Automatic Check-Out') | FACT | always | — | in_mode is kiosk, systray, manual or technical; out_mode additionally auto_check_out | N-U17-083 |
| VDR-U17-C227 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:203 | cannot be earlier than | FACT | always | — | Constraint: check_out before check_in is refused | N-U17-087 |
| VDR-U17-C228 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:220 | the employee was already checked in on | FACT | always | — | _check_validity refuses a new attendance overlapping the previous one of the same employee | N-U17-087 |
| VDR-U17-C229 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:232 | hasn't checked out since | FACT | attendance without check_out | — | Only one open attendance per employee | N-U17-087 |
| VDR-U17-C230 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:192 | if not resource._is_flexible() | FACT | always | — | Lunch intervals are subtracted unless the resource is flexible; flexible hours are the plain difference | N-U17-088 |
| VDR-U17-C231 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:90 | tz = timezone(attendance.employee_id._get_tz()) | FACT | always | — | Attendance date is the check_in converted to the employee's timezone | N-U17-088 |
| VDR-U17-C232 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:398 | You cannot duplicate an attendance | FACT | always | — | copy is refused | N-U17-087 |
| VDR-U17-C233 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_employee.py:208 | def _attendance_action_change | FACT | always | — | Check in creates an attendance; check out writes check_out on the open one with optional in or out geo values | N-U17-089 |
| VDR-U17-C234 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_employee.py:241 | could not find corresponding check in | FACT | attendance_state checked_in but no open record | — | UserError asks to contact HR | N-U17-089 |
| VDR-U17-C235 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_employee.py:89 | open_attendances.write | FACT | employee archived | — | action_archive closes open attendances at now in sudo | N-U17-090 |
| VDR-U17-C236 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_employee.py:206 | 'checked_in' or 'checked_out' | FACT | always | — | attendance_state derives from last_attendance_id (latest check_in not after now) | N-U17-089 |
| VDR-U17-C237 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:373 | res._update_overtime() | FACT | always | — | create, write of employee, check_in or check_out, and unlink all regenerate overtime lines for the affected dates | N-U17-091 |
| VDR-U17-C238 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:330 | manual_overtimes | FACT | regeneration | — | Lines whose manual_duration differs from duration or whose status is to_approve are remembered and recreated with status to_approve | N-U17-091 |
| VDR-U17-C239 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:331 | all_overtime_lines.unlink() | FACT | regeneration | — | Existing lines in the affected domain are deleted before recreation | N-U17-091 |
| VDR-U17-C240 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:280 | rule.quantity_period == 'week' | FACT | weekly rules | — | The regeneration domain widens to Monday–Sunday when any rule is weekly or flexible schedule caps hours weekly | N-U17-091 |
| VDR-U17-C241 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:381 | Do not have access, user cannot edit the attendances that are not their own | FACT | employee_id in vals | — | Reassigning an attendance requires own employee, attendance administrator or attendance approver of the target | N-U17-094 |
| VDR-U17-C242 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:112 | ot.status == 'refused' | FACT | always | — | overtime_status is approved when all linked lines approved, refused when all refused, else to_approve | N-U17-092 |
| VDR-U17-C243 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime.py:65 | attendance_overtime_validation == 'by_manager' | FACT | always | — | New lines are to_approve when company validation is by_manager, else approved | N-U17-092 |
| VDR-U17-C244 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime.py:57 | CHECK (time_stop > time_start) | FACT | always | — | Overtime line stop must be after start | N-U17-101 |
| VDR-U17-C245 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime.py:86 | self.write({'status': 'approved'}) | FACT | always | — | action_approve and action_refuse write status and recompute the attendance status and validated hours | N-U17-092 |
| VDR-U17-C246 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime_ruleset.py:18 | rate_combination_mode | FACT | always | — | Ruleset combines rule rates by max or sum | N-U17-092 |
| VDR-U17-C247 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime_rule.py:777 | combined_rate = max_rate_rule.amount_rate | FACT | ruleset max mode | — | _extra_overtime_vals takes the highest paid rule rate in max mode, 1 plus the sum of extra rates in sum mode, 0 when no rule is paid | N-U17-092 |
| VDR-U17-C248 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_attendance_overtime_rule.py:22 | combined_rate += sum(r.amount_rate | FACT | hr_holidays_attendance installed | — | In sum mode compensable rules add their whole rate instead of the extra part and expose compensable_as_leave | N-U17-084 |
| VDR-U17-C249 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime_rule.py:79 | ('quantity', "Quantity") | FACT | always | — | base_off quantity or timing; timing_type work_days, non_work_days, leave, schedule | N-U17-084 |
| VDR-U17-C250 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime_rule.py:152 | the usual amount of work hours is not specified | FACT | always | — | Quantity rules need expected hours or contract hours and a period; schedule timing rules need a calendar; timing start in 0–24 | N-U17-101 |
| VDR-U17-C251 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime_rule.py:736 | _add_overtime_val | FACT | always | — | Overtime and undertime intervals are converted to lines per day and rule set, with duration rounded to four decimals | N-U17-084 |
| VDR-U17-C252 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_version.py:22 | hr_attendance_default_ruleset | FACT | always | — | hr.version.ruleset_id (group hr_manager) defaults to the Default Ruleset | N-U17-084 |
| VDR-U17-C253 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime_ruleset.py:50 | action_regenerate_overtimes | FACT | manual action | — | Regenerates overtime for attendances of versions using the ruleset | N-U17-091 |
| VDR-U17-C254 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:608 | employee_id.company_id.auto_check_out | FACT | cron | — | _cron_auto_check_out inspects open attendances of companies with auto_check_out and non-flexible calendars | N-U17-093 |
| VDR-U17-C255 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:649 | max_tol | FACT | cron | — | Closes when current plus previous worked hours minus tolerance exceed expected hours of the day; sets out_mode auto_check_out and posts a note | N-U17-093 |
| VDR-U17-C256 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:665 | absence_management | FACT | cron | — | _cron_absence_detection creates one-second technical attendances yesterday for non-flexible employees with a contract start and no overtime line | N-U17-085 |
| VDR-U17-C257 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:693 | unjustified absence | FACT | cron | — | Technical attendances without overtime are deleted again; others get an explanatory note | N-U17-085 |
| VDR-U17-C258 | FUNCTION MAPPING REQUIRED | hr_attendance/data/hr_attendance_data.xml:8 | model._cron_auto_check_out() | OBSERVATION | restored DB | — | DB shows both attendance crons active at 4 hours; company flags in the DB: auto check-out, absence management, device tracking and systray check-in are on; kiosk mode barcode and manual with PIN; overtime validation automatic; display of extra hours on; default ruleset has 2 rules, UAE ruleset 4, 6 rules total | N-U17-098 |
| VDR-U17-C259 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_employee.py:63 | officer_group.sudo().write({'user_ids' | FACT | attendance_manager_id set | — | Naming an attendance approver adds the user to the attendance officer group; removing clears it when no longer approver | N-U17-094 |
| VDR-U17-C260 | FUNCTION MAPPING REQUIRED | hr_attendance/models/res_users.py:15 | group_hr_attendance_officer | FACT | approver removed | — | _clean_attendance_officers removes the officer group from users who approve nobody | N-U17-094 |
| VDR-U17-C261 | FUNCTION MAPPING REQUIRED | hr_attendance/security/hr_attendance_security.xml:15 | group_hr_attendance_own_reader | FACT | always | — | base.group_user implies the own-reader group; groups officer, user (all attendances) and manager are layered | N-U17-086 |
| VDR-U17-C262 | FUNCTION MAPPING REQUIRED | hr_attendance/security/hr_attendance_security.xml:47 | ('employee_id.company_id', 'in', company_ids) | FACT | always | — | Global company rule on attendances and overtime lines | N-U17-086 |
| VDR-U17-C263 | FUNCTION MAPPING REQUIRED | hr_attendance/security/hr_attendance_security.xml:64 | ('employee_id.attendance_manager_id', '=', user.id) | FACT | always | — | Attendance officers read and write only attendances of employees they approve | N-U17-086 |
| VDR-U17-C264 | FUNCTION MAPPING REQUIRED | hr_attendance/security/hr_attendance_security.xml:81 | [('employee_id.user_id', '=', user.id)] | FACT | always | — | Own-reader sees own attendances read-only | N-U17-086 |
| VDR-U17-C265 | FUNCTION MAPPING REQUIRED | hr_attendance/security/ir.model.access.csv:6 | access_hr_attendance_overtime_rule_admin | FACT | always | — | Overtime rules and rulesets are writable by attendance administrators only; HR administrators read both; attendance officers read rules only | N-U17-086 |
| VDR-U17-C266 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:17 | attendance_kiosk_key', '=', token | FACT | always | — | Kiosk company is identified by a uuid token stored on the company | N-U17-095 |
| VDR-U17-C267 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:197 | request.env['hr.employee'].sudo().search([('barcode', '=', barcode) | FACT | valid token | — | Barcode scan route is auth public, finds employee by barcode within the company with sudo and toggles attendance | N-U17-095 |
| VDR-U17-C268 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:208 | (employee.pin == pin_code) | FACT | valid token | — | Manual selection toggles attendance with sudo; PIN is compared only when kiosk PIN is enabled | N-U17-095 |
| VDR-U17-C269 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:119 | employee.write({'barcode': badge}) | INFERENCE | auth public route | RT | set_badge, create_employee and get_employees_without_badge are auth public and use request.env without sudo, so success depends on the ACL of the calling session user; with a true public user they would be refused | N-U17-102 |
| VDR-U17-C270 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:270 | request.env.user.company_id.attendance_kiosk_mode = mode | INFERENCE | auth public route | RT | set_attendance_settings validates the token company but writes the mode on the session user's company | N-U17-102 |
| VDR-U17-C271 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:86 | hr_attendance.group_hr_attendance_user | FACT | always | — | The kiosk menu redirect requires the attendance user group and logs out a password-protected session before showing the kiosk | N-U17-095 |
| VDR-U17-C272 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:241 | systray_check_in_out | FACT | always | — | Systray check in or out is auth user and acts on the user's employee of the active company | N-U17-083 |
| VDR-U17-C273 | FUNCTION MAPPING REQUIRED | hr_attendance/controllers/main.py:63 | request.env['base.geocoder']._get_localisation(latitude, longitude) | FACT | device_tracking_enabled | RT | Location label comes from base.geocoder; UserError or RequestException yield Unknown; IP, browser and coordinates are stored | N-U17-096 |
| VDR-U17-C274 | FUNCTION MAPPING REQUIRED | hr_attendance/models/res_company.py:32 | attendance_kiosk_key | FACT | always | — | attendance_kiosk_key defaults to uuid4 hex, not copied, readable by attendance user group | N-U17-102 |
| VDR-U17-C275 | FUNCTION MAPPING REQUIRED | hr_attendance/models/res_company.py:36 | attendance_overtime_validation | FACT | always | — | Company flags: kiosk mode and barcode source, kiosk PIN, systray, overtime validation, auto check-out with tolerance, absence management, device tracking, display of extra hours | N-U17-098 |
| VDR-U17-C276 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/resource_calendar_leaves.py:54 | _update_attendances_overtime | FACT | hr_holidays_attendance installed | — | Creating, changing or deleting calendar leaves recomputes overtime of attendances in the affected window | N-U17-099 |
| VDR-U17-C277 | FUNCTION MAPPING REQUIRED | hr_holidays_attendance/models/hr_attendance_overtime.py:10 | compensable_as_leave | FACT | hr_holidays_attendance installed | — | Overtime lines gain compensable_as_leave, fed by the rule flag | N-U17-084 |
| VDR-U17-C278 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_employee.py:290 | attendance_state == "checked_in" | FACT | always | — | Attendance has second priority after login in the presence state: checked in is present; checked out during working hours is absent | N-U17-100 |
| VDR-U17-C279 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | Exact overtime splitting for mixed quantity and timing rules and the legal value of kiosk evidence require execution tests and local counsel | N-U17-104 |
| VDR-U17-C280 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:41 | ('conflict', 'In Conflict') | FACT | always | — | hr.work.entry state draft, conflict, validated (In Payslip), cancelled; fields employee, version, date, duration, type, amount_rate | N-U17-117 |
| VDR-U17-C281 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:59 | Duration must be positive and cannot exceed 24 hours | FACT | always | — | Constraint on duration | N-U17-108 |
| VDR-U17-C282 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:117 | if not work_entries._check_if_error() | FACT | always | — | action_validate writes validated only when no error check fires | N-U17-109 |
| VDR-U17-C283 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:142 | undefined_type.write({'state': 'conflict'}) | FACT | always | — | _check_if_error marks undefined type, over-24h days, leave entries outside schedule and entries on already validated days as conflict | N-U17-109 |
| VDR-U17-C284 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:163 | HAVING 0 >= SUM(duration) OR SUM(duration) > 24 | FACT | always | — | SQL finds employee-days whose active entries sum above 24 hours | N-U17-108 |
| VDR-U17-C285 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:198 | calendar.flexible_hours | FACT | always | — | Leave entries are checked against calendar attendance intervals; flexible or missing calendars are skipped | N-U17-109 |
| VDR-U17-C286 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:215 | validated_work_entries | FACT | always | — | Any non-validated entry on an employee-day that already has validated entries is a conflict | N-U17-109 |
| VDR-U17-C287 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:258 | work_entries._check_if_error() | FACT | always | — | create copies amount_rate from the type, sets company from the employee and runs the checks | N-U17-109 |
| VDR-U17-C288 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:271 | vals['state'] = 'draft' if vals['active'] else 'cancelled' | FACT | always | — | active and state are kept in step: cancelled means inactive, draft means active | N-U17-112 |
| VDR-U17-C289 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:317 | work_entries._reset_conflicting_state() | FACT | always | — | _error_checking resets conflict states in the date range before the write and rechecks after, unless hr_work_entry_no_check | N-U17-117 |
| VDR-U17-C290 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:282 | This work entry is validated | FACT | always | — | Validated entries cannot be deleted | N-U17-112 |
| VDR-U17-C291 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:125 | You can't split a work entry with less than 1 hour | FACT | always | — | action_split needs duration of at least one hour and a smaller split duration, then copies the entry | N-U17-114 |
| VDR-U17-C292 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:27 | ('calendar', 'Working Schedule') | FACT | always | — | work_entry_source selection has the single value calendar; help text mentions attendances and planning, not available in this edition | N-U17-118 |
| VDR-U17-C293 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:416 | with_user(SUPERUSER_ID) | FACT | always | — | generate_work_entries groups versions by company and timezone and runs generation as superuser | N-U17-122 |
| VDR-U17-C294 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:475 | last_generated_from = min(version.date_generated_from, version_stop) | FACT | not forced | — | Only ranges outside date_generated_from..date_generated_to are generated and the bounds are extended | N-U17-110 |
| VDR-U17-C295 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:463 | domain_to_nullify | FACT | force | — | Forced generation deactivates non-validated entries in range before regenerating | N-U17-110 |
| VDR-U17-C296 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:444 | if not version.contract_date_start | FACT | always | — | Versions without a contract start are skipped | N-U17-110 |
| VDR-U17-C297 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:609 | Now merge similar work entries on the same day | FACT | always | — | Entries with same date, type, employee, version and company are merged and zero-duration entries dropped | N-U17-111 |
| VDR-U17-C298 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:543 | Handle multi-local-day spans | FACT | always | — | Intervals spanning local midnight are split per day in the version timezone | N-U17-111 |
| VDR-U17-C299 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:520 | Missing timezone for work entries generation | FACT | no timezone found | — | UserError when neither the version calendar, employee calendar nor company calendar gives a timezone | N-U17-122 |
| VDR-U17-C300 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:696 | ['resource_calendar_id', 'work_entry_source'] | FACT | always | — | Changing the calendar or source recomputes entries for the generated range; contract date changes call _remove_work_entries | N-U17-113 |
| VDR-U17-C301 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:682 | self._cancel_work_entries() | FACT | always | — | Deleting a version removes its non-validated entries in the version dates | N-U17-113 |
| VDR-U17-C302 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:719 | BATCH_SIZE = 100 | FACT | cron | — | _cron_generate_missing_work_entries handles current-month versions with open periods in batches of 100 of one company and retriggers itself | N-U17-106 |
| VDR-U17-C303 | FUNCTION MAPPING REQUIRED | hr_work_entry/data/ir_cron_data.xml:8 | model._cron_generate_missing_work_entries() | OBSERVATION | restored DB | — | DB: cron Generate Missing Work Entries active daily; 0 work entries; 118 work entry types (BE 32, CH 16, AU 15, HK 11, no country 9, others fewer); 6 ACL rows and 3 rules equal source | N-U17-106 |
| VDR-U17-C304 | FUNCTION MAPPING REQUIRED | hr_work_entry/wizard/hr_work_entry_regeneration_wizard.py:107 | No work entry can be regenerated in this range of dates and these employees | FACT | always | — | Regeneration needs generated bounds, a range inside them and at least one employee without validated entries; it calls generate_work_entries with force | N-U17-112 |
| VDR-U17-C305 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry_type.py:59 | The same code cannot be associated to multiple work entry types | FACT | always | — | Payroll code unique per country or global | N-U17-119 |
| VDR-U17-C306 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry_type.py:44 | You can't change the Country of this work entry type | FACT | not install mode | — | Country cannot change when entries use the type | N-U17-121 |
| VDR-U17-C307 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry_type.py:31 | amount_rate | FACT | always | — | Type fields: code, display code, external code, is_leave, is_work, amount_rate, is_extra_hours | N-U17-119 |
| VDR-U17-C308 | FUNCTION MAPPING REQUIRED | hr_work_entry/security/ir.model.access.csv:2 | access_hr_work_entry_officer | FACT | always | — | HR officers create, read and write entries but cannot delete; system group has full rights; entry types read for officers and full for HR administrators | N-U17-107 |
| VDR-U17-C309 | FUNCTION MAPPING REQUIRED | hr_work_entry/security/hr_work_entry_security.xml:23 | [('company_id', 'in', company_ids)] | FACT | always | — | Entries are scoped by company; types by country | N-U17-107 |
| VDR-U17-C310 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_employee.py:31 | 'date_generated_from': fields.Datetime.now() | FACT | always | — | Creating a version resets its generated bounds to today so history is not regenerated | N-U17-110 |
| VDR-U17-C311 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_version.py:53 | bypassing_rc_leave | FACT | hr_work_entry_holidays installed | — | Leave entry type is chosen: bypassing codes, then global leaves, then employee leaves | N-U17-116 |
| VDR-U17-C312 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_version.py:25 | result.append(('leave_id' | FACT | hr_work_entry_holidays installed | — | Leave entries carry leave_id of the covering time off | N-U17-115 |
| VDR-U17-C313 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_leave.py:12 | work_entry_type_id = fields.Many2one('hr.work.entry.type' | FACT | hr_work_entry_holidays installed | — | Time off types map to a work entry type and the resource leave inherits it | N-U17-115 |
| VDR-U17-C314 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_leave.py:105 | _error_checking(start=start | FACT | hr_work_entry_holidays installed | — | Leave create and write run inside the work entry error-checking context over the leave range plus one day | N-U17-115 |
| VDR-U17-C315 | FUNCTION MAPPING REQUIRED | hr_work_entry_holidays/models/hr_work_entry.py:22 | attendances.write({'leave_id': False}) | FACT | hr_work_entry_holidays installed | — | Resetting a conflict on attendance entries removes their leave link | N-U17-115 |
| VDR-U17-C316 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | — | Payroll consumption of validated entries and localisation types are outside this edition's module set; resolve by reading payroll and l10n modules if installed | N-U17-123 |
| VDR-U17-C317 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:24 | _name = 'hr.applicant' | FACT | always | — | hr.applicant is the application model (thread, CC, blacklist, phone, activity, UTM and duration-tracking mixins); there is no separate candidate model in this edition | N-U17-124 |
| VDR-U17-C318 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:589 | ('fold', '=', False) | FACT | job set and no stage | — | _compute_stage picks the lowest-sequence stage with no job restriction or restricted to the job and not folded | N-U17-128 |
| VDR-U17-C319 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_job.py:217 | def _get_first_stage | FACT | mail alias creation | — | _get_first_stage does not filter folded stages, unlike the applicant compute | N-U17-128 |
| VDR-U17-C320 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:606 | applicant.date_closed = fields.Datetime.now() | FACT | stage hired_stage | — | date_closed is set on entering a hired stage and cleared otherwise | N-U17-129 |
| VDR-U17-C321 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:669 | applicant.job_id.no_of_recruitment -= 1 | FACT | stage change to hired and from non-hired | — | Moving into a hired stage decrements the job's no_of_recruitment when positive; leaving increments | N-U17-129 |
| VDR-U17-C322 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:516 | applicant.application_status = 'refused' | FACT | always | — | application_status is refused if refuse_reason_id, archived if inactive, hired if date_closed, else ongoing | N-U17-130 |
| VDR-U17-C323 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:625 | vals['date_open'] = fields.Datetime.now() | FACT | user_id set | — | date_open is stamped when a recruiter is set; email_from is stripped | N-U17-124 |
| VDR-U17-C324 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:665 | vals['last_stage_id'] = applicant.stage_id.id | FACT | stage_id written | — | Stage change resets kanban_state to normal, stamps last stage update and stores last_stage_id | N-U17-128 |
| VDR-U17-C325 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:631 | _create_recruitment_interviewers | FACT | interviewers set | — | Interviewers are granted the interviewer group in sudo and notified except the acting user | N-U17-133 |
| VDR-U17-C326 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/res_users.py:16 | interviewers = self - recruitment_group.all_user_ids | FACT | always | — | Users who are not recruitment officers receive the interviewer group | N-U17-133 |
| VDR-U17-C327 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/res_users.py:34 | users_to_remove | FACT | interviewer removed | — | The interviewer group is removed when the user is interviewer on no job and no application and not an officer | N-U17-133 |
| VDR-U17-C328 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:152 | Talent must belong to at least one Talent Pool | FACT | always | — | A talent record needs at least one pool | N-U17-136 |
| VDR-U17-C329 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:635 | applicant.pool_applicant_id = applicant | FACT | talent_pool_ids set at create | — | A talent applicant becomes its own pool applicant | N-U17-136 |
| VDR-U17-C330 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:681 | applicant.pool_applicant_id.email_from = vals['email_from'] | FACT | linked applications | — | Email, phone, profile link and degree changes are mirrored to the pool applicant | N-U17-136 |
| VDR-U17-C331 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:714 | You cannot duplicate the talent(s) | FACT | always | — | Talents cannot be duplicated | N-U17-136 |
| VDR-U17-C332 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:953 | stage = job._get_first_stage() | FACT | inbound mail with job custom value | — | message_new gives the new applicant the first stage of the job; default_user_id is cleared so the gateway user does not become recruiter | N-U17-125 |
| VDR-U17-C333 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:960 | job_platform = self.env['hr.job.platform'] | FACT | sender matches platform email | — | Mail from a registered job platform takes the name from a regex on subject or body and email_from is dropped | N-U17-125 |
| VDR-U17-C334 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_job.py:276 | values['alias_model_id'] | FACT | always | — | Each job alias creates hr.applicant with defaults job, department, company and recruiter | N-U17-125 |
| VDR-U17-C335 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:1012 | Please provide an applicant name | FACT | always | — | create_employee_from_applicant requires a name, creates a partner if missing, creates the employee and copies attachments not already present | N-U17-134 |
| VDR-U17-C336 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:1036 | address_sudo = self.env['res.partner'].sudo().browse(address_id) | FACT | always | — | Employee values take private address, email, phone and language from the contact in sudo, job, department, company address and work email from the department company or applicant | N-U17-126 |
| VDR-U17-C337 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:1062 | You are not allowed to perform this action | FACT | interviewer without officer group | — | _check_interviewer_access blocks employee creation for pure interviewers | N-U17-133 |
| VDR-U17-C338 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_employee.py:23 | applicant_hired_template | FACT | employee created with applicants | — | A hired message is logged on the applicant when the employee is created | N-U17-134 |
| VDR-U17-C339 | FUNCTION MAPPING REQUIRED | hr_recruitment/wizard/applicant_refuse_reason.py:138 | 'active': False | FACT | always | — | action_refuse_reason_apply writes refuse_reason_id, active false and refuse_date; mail is queued after the write | N-U17-131 |
| VDR-U17-C340 | FUNCTION MAPPING REQUIRED | hr_recruitment/wizard/applicant_refuse_reason.py:117 | Unable to post message, please configure the sender's email address | FACT | send_mail | — | Sending requires the user's email and an email on each applicant or contact | N-U17-131 |
| VDR-U17-C341 | FUNCTION MAPPING REQUIRED | hr_recruitment/wizard/applicant_refuse_reason.py:130 | Refused automatically because this application has been identified as a duplicate | FACT | duplicates checked | — | Duplicates (same email, phone or LinkedIn) of non-closed applications are refused with a log message | N-U17-131 |
| VDR-U17-C342 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:1080 | Reinsert the applicant into the recruitment pipe | FACT | always | — | reset_applicant writes the first non-folded stage and clears refuse_reason_id; action_unarchive calls it | N-U17-132 |
| VDR-U17-C343 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_recruitment_stage.py:25 | hired_stage | FACT | always | — | Stage has job restriction, email template, fold, hired_stage, rotting threshold and kanban legends | N-U17-128 |
| VDR-U17-C344 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_recruitment_stage.py:52 | stage._origin.hired_stage and not stage.hired_stage | FACT | stage edited | — | A warning flag shows when a hired stage with applicants loses the flag | N-U17-142 |
| VDR-U17-C345 | FUNCTION MAPPING REQUIRED | hr_recruitment/security/hr_recruitment_security.xml:17 | group_hr_recruitment_interviewer | FACT | always | — | Groups Interviewer, Officer, Administrator and CV display; base.group_user implies CV display | N-U17-133 |
| VDR-U17-C346 | FUNCTION MAPPING REQUIRED | hr_recruitment/security/hr_recruitment_security.xml:54 | ('job_id.interviewer_ids', 'in', user.id) | FACT | always | — | Interviewers read and write only applications whose job or application lists them; no create or delete | N-U17-133 |
| VDR-U17-C347 | FUNCTION MAPPING REQUIRED | hr_recruitment/security/hr_recruitment_security.xml:14 | company_ids + [False] | FACT | always | — | Global company rule on applications | N-U17-135 |
| VDR-U17-C348 | FUNCTION MAPPING REQUIRED | hr_recruitment/security/hr_recruitment_security.xml:86 | model_id" ref="mail.model_mail_message | FACT | recruitment officer | — | Rule User: All Chatter gives recruitment officers domain true on mail.message | N-U17-143 |
| VDR-U17-C349 | FUNCTION MAPPING REQUIRED | hr_recruitment/security/ir.model.access.csv:4 | hr.access_hr_job_user | FACT | always | — | Recruitment redefines the hr module's hr.job ACL id so HR officers keep read only while recruitment officers have full CRUD on hr.job | N-U17-135 |
| VDR-U17-C350 | FUNCTION MAPPING REQUIRED | hr_recruitment/security/ir.model.access.csv:5 | access_hr_applicant_interviewer | FACT | always | — | ACL: interviewer read and write, officer full on hr.applicant; stages read for officers and full for administrators | N-U17-133 |
| VDR-U17-C351 | FUNCTION MAPPING REQUIRED | hr_recruitment/data/hr_recruitment_data.xml:68 | hired_stage | OBSERVATION | restored DB | — | DB: 6 stages (New to Contract Signed, last is hired and folded), 6 refuse reasons, 4 degrees, 3 job platforms, 4 tags, 0 applicants and 0 jobs; 30 ACL rows and 8 rules in recruitment match source (31 csv rows, one redefines an hr row), 4 groups | N-U17-124 |
| VDR-U17-C352 | FUNCTION MAPPING REQUIRED | hr_recruitment_skills/models/hr_applicant.py:72 | matching_score = round(applicant_total / job_total * 100) | FACT | hr_recruitment_skills installed | — | Matching score is applicant skill progress capped at twice the job level plus degree score, over the job's required total | N-U17-139 |
| VDR-U17-C353 | FUNCTION MAPPING REQUIRED | hr_recruitment_skills/models/hr_applicant.py:81 | vals["employee_skill_ids"] | FACT | hr_recruitment_skills installed | — | create_employee copies applicant skills to employee skills | N-U17-126 |
| VDR-U17-C354 | FUNCTION MAPPING REQUIRED | hr_recruitment_skills/security/hr_recruitment_skills_security.xml:9 | applicant_id.job_id.interviewer_ids | FACT | hr_recruitment_skills installed | — | Applicant skills follow the interviewer rule; officers see all | N-U17-133 |
| VDR-U17-C355 | FUNCTION MAPPING REQUIRED | hr_recruitment_sms/models/hr_applicant.py:12 | default_composition_mode | FACT | hr_recruitment_sms installed | RT | action_send_sms opens sms.composer in mass mode on the applications; delivery depends on the SMS gateway | N-U17-141 |
| VDR-U17-C356 | FUNCTION MAPPING REQUIRED | hr_recruitment_survey/models/hr_applicant.py:48 | self.survey_id.check_validity() | FACT | survey flow | — | action_send_survey creates a contact in sudo if missing, validates the survey and opens the invite wizard with a 15-day deadline | N-U17-140 |
| VDR-U17-C357 | FUNCTION MAPPING REQUIRED | hr_recruitment_survey/models/survey_user_input.py:13 | odoobot = self.env.ref('base.partner_root') | FACT | survey completed | — | Completion posts a message on the applicant authored by the bot partner | N-U17-140 |
| VDR-U17-C358 | FUNCTION MAPPING REQUIRED | hr_recruitment_survey/security/hr_recruitment_survey_security.xml:14 | survey_user_input_rule_recruitment_manager | FACT | hr_recruitment_survey installed | — | Recruitment administrators get full rules on recruitment-type surveys, questions and answers; officers and interviewers get scoped read | N-U17-135 |
| VDR-U17-C359 | FUNCTION MAPPING REQUIRED | hr_recruitment_survey/models/survey_survey.py:9 | ('recruitment', 'Recruitment') | FACT | hr_recruitment_survey installed | — | survey_type gains recruitment; allowed for interviewers and survey users | N-U17-138 |
| VDR-U17-C360 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | — | Website job publication, document digitisation and external job-board feeds not studied | N-U17-144 |
| VDR-U17-C361 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_individual_skill_mixin.py:73 | There can only be one active skill for each skill_id | FACT | always | — | The mixin documents regular skills: one active per skill, history by archiving, no edits; certifications: many with different validity ranges | N-U17-148 |
| VDR-U17-C362 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_individual_skill_mixin.py:68 | _check_not_overlapping_regular_skill | FACT | always | — | Constraint refuses skills overlapping or exactly matching existing ones for the same owner and skill | N-U17-148 |
| VDR-U17-C363 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_individual_skill_mixin.py:204 | valid stop date prior to their valid start date | FACT | always | — | valid_to before valid_from raises | N-U17-149 |
| VDR-U17-C364 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_individual_skill_mixin.py:210 | don't match | FACT | always | — | Skill must belong to the skill type; level must belong to the type | N-U17-149 |
| VDR-U17-C365 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_individual_skill_mixin.py:273 | individual_skill.valid_from >= yesterday | FACT | skill removal | — | _expire_individual_skills deletes skills created yesterday or later or already ended, archives others by setting valid_to yesterday unless that overlaps | N-U17-150 |
| VDR-U17-C366 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_employee_skill.py:25 | skill.skill_type_id.is_certification and not filtered_emp_skill | FACT | always | — | Current skills exclude ended ones; for certifications the latest expired one is kept visible | N-U17-154 |
| VDR-U17-C367 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_skill_type.py:34 | must contain at least one skill and one level | FACT | always | — | A skill type needs at least one skill and one level | N-U17-149 |
| VDR-U17-C368 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_resume_line.py:40 | CHECK ((date_start <= date_end OR date_end IS NULL)) | FACT | always | — | Resume line start must not follow end | N-U17-152 |
| VDR-U17-C369 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_employee.py:63 | three_months_later | FACT | cron | — | _add_certification_activity_to_employees schedules an upload-certification activity for employees whose job requires a certification they lack or that expires within three months | N-U17-151 |
| VDR-U17-C370 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_employee.py:122 | responsible = employee.user_id or employee.parent_id.user_id or job_id.user_id | FACT | cron | — | Responsible is the employee's user, else the manager's user, else the job recruiter; none means skipped | N-U17-151 |
| VDR-U17-C371 | FUNCTION MAPPING REQUIRED | hr_skills/security/hr_skills_security.xml:7 | Resume: employee: read all | FACT | always | — | All internal users read every resume line and employee skill (domain true) | N-U17-153 |
| VDR-U17-C372 | FUNCTION MAPPING REQUIRED | hr_skills/security/hr_skills_security.xml:24 | [('employee_id.user_id','=',user.id)] | FACT | always | — | Internal users create, edit and delete only their own resume lines and skills | N-U17-153 |
| VDR-U17-C373 | FUNCTION MAPPING REQUIRED | hr_skills/security/hr_skills_security.xml:64 | has_department_manager_access | FACT | always | — | Skill reports: HR officers all, managers by department, history by child_of the user's employees, plus company scope | N-U17-153 |
| VDR-U17-C374 | FUNCTION MAPPING REQUIRED | hr_skills/security/ir.model.access.csv:11 | access_hr_skill_employee | FACT | always | — | ACL base.group_user read and create (no write) on hr.skill | N-U17-157 |
| VDR-U17-C375 | FUNCTION MAPPING REQUIRED | hr_skills_event/models/event_event.py:15 | hr_skills_event_add_employee | FACT | hr_skills_event installed | — | Creating an onsite course event from the resume registers the employee's work contact | N-U17-146 |
| VDR-U17-C376 | FUNCTION MAPPING REQUIRED | hr_skills_slides/models/slide_channel.py:48 | 'course_type': 'elearning' | FACT | hr_skills_slides installed | — | Completing a course adds a training resume line in sudo once per channel | N-U17-146 |
| VDR-U17-C377 | FUNCTION MAPPING REQUIRED | hr_skills_survey/models/survey_user.py:21 | certification_user_inputs | FACT | hr_skills_survey installed | — | A passed certification survey writes or creates a resume line with date_end from certification_validity_months | N-U17-146 |
| VDR-U17-C378 | FUNCTION MAPPING REQUIRED | hr_skills_survey/models/hr_resume_line.py:25 | relativedelta(months=-3) | FACT | hr_skills_survey installed | — | expiration_status is expired, expiring within three months or valid | N-U17-152 |
| VDR-U17-C379 | FUNCTION MAPPING REQUIRED | hr_skills_slides/models/slide_channel.py:27 | HrResumeLine = self.env['hr.resume.line'].sudo() | FACT | hr_skills_slides installed | — | Resume automation writes with sudo | N-U17-156 |
| VDR-U17-C380 | FUNCTION MAPPING REQUIRED | hr_skills/security/ir.model.access.csv:2 | access_hr_resume_line | OBSERVATION | restored DB | — | DB: 36 skills, 11 levels, 2 skill types, 3 resume line types, 0 employee skills, 0 resume lines; certification cron active daily; ACL 20 and rules 11 equal source | N-U17-145 |
| VDR-U17-C381 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | — | Job-to-skill mapping and resume printing wizard not read in depth | N-U17-159 |
| VDR-U17-C382 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:31 | fleet_vehicle_state_new_request | FACT | always | — | New vehicles default to the seeded state New Request | N-U17-169 |
| VDR-U17-C383 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:61 | model_id = fields.Many2one('fleet.vehicle.model', 'Model' | FACT | always | — | model_id is required; company defaults to the current company | N-U17-173 |
| VDR-U17-C384 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:250 | order='value desc' | FACT | always | — | odometer is the highest logged value from fleet.vehicle.odometer | N-U17-163 |
| VDR-U17-C385 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:257 | self.env['fleet.vehicle.odometer'].create | FACT | odometer written | — | Inverse creates an odometer log dated today for the driver | N-U17-163 |
| VDR-U17-C386 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:402 | The odometer value cannot be lower than the previous one | FACT | odometer in vals | — | write refuses a lower value | N-U17-163 |
| VDR-U17-C387 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:407 | vehicle.create_driver_history(vals) | FACT | driver_id changes | — | A history line with date_start today is created | N-U17-164 |
| VDR-U17-C388 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:412 | Specify the End date of | FACT | previous driver existed | — | A to-do activity for the fleet manager or current user asks to set the end date | N-U17-164 |
| VDR-U17-C389 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:452 | def action_accept_driver_change | FACT | manual action | — | Future driver becomes driver, other vehicles of that type driven by that person lose the driver, change flags cleared | N-U17-164 |
| VDR-U17-C390 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:386 | plan_to_change_car = True | FACT | future driver set | — | Vehicles of the same type held by the future driver are flagged plan to change | N-U17-164 |
| VDR-U17-C391 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:432 | self.env['fleet.vehicle.log.contract'].search | FACT | vehicle archived | — | Contracts and services of the vehicle are deactivated | N-U17-165 |
| VDR-U17-C392 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_log_contract.py:48 | ('futur', 'New') | FACT | always | — | Contract state futur, open, expired, closed; recurring cost fields cost_generated and cost_frequency | N-U17-166 |
| VDR-U17-C393 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_log_contract.py:116 | future_contracts.action_draft() | FACT | start or expiry dates written | — | Writing dates sets the state by comparing with today; renewal activity is rescheduled | N-U17-166 |
| VDR-U17-C394 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_log_contract.py:143 | reminder_activity_type | FACT | cron | — | scheduler_manage_contract_expiration schedules renewal activities for open contracts expiring within the delay and with a responsible user, expires overdue, drafts future, opens started | N-U17-166 |
| VDR-U17-C395 | FUNCTION MAPPING REQUIRED | fleet/data/fleet_data.xml:8 | model.run_scheduler() | FACT | always | — | The cron named Generate contracts costs based on costs frequency calls run_scheduler, which only calls scheduler_manage_contract_expiration | N-U17-170 |
| VDR-U17-C396 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_log_contract.py:58 | cost_frequency = fields.Selection | INFERENCE | always | — | Searching fleet and hr_fleet models finds no code that creates cost lines from cost_generated or cost_frequency | N-U17-170 |
| VDR-U17-C397 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:299 | hr_fleet.delay_alert_contract | FACT | always | — | Renewal alert lead time is the system parameter hr_fleet.delay_alert_contract, default 30 days; DB has the parameter | N-U17-167 |
| VDR-U17-C398 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:322 | record.contract_renewal_overdue = diff_time < 0 | FACT | always | — | Overdue and due-soon flags derive from the latest expiration date of non-closed contracts | N-U17-167 |
| VDR-U17-C399 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_assignation_log.py:15 | date_end = fields.Date(string="End Date") | INFERENCE | always | — | date_end is a plain field; a search of fleet and hr_fleet models finds no code that sets it, so ending an assignment is manual | N-U17-173 |
| VDR-U17-C400 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_log_services.py:53 | Emptying the odometer value of a vehicle is not allowed | FACT | always | — | Service odometer inverse refuses empty value and creates an odometer log | N-U17-173 |
| VDR-U17-C401 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_log_services.py:39 | ('running', 'Running') | FACT | always | — | Service state new, running, done, cancelled | N-U17-169 |
| VDR-U17-C402 | FUNCTION MAPPING REQUIRED | fleet/security/fleet_security.xml:8 | fleet_group_user | FACT | always | — | Groups Officer and Administrator; Administrator has all-access rules on vehicles, contracts, services and odometer | N-U17-172 |
| VDR-U17-C403 | FUNCTION MAPPING REQUIRED | fleet/security/fleet_security.xml:46 | [('company_id', 'in', company_ids + [False])] | FACT | always | — | Company rules on vehicles, contracts, cost report, odometer and services | N-U17-172 |
| VDR-U17-C404 | FUNCTION MAPPING REQUIRED | fleet/security/ir.model.access.csv:8 | fleet_vehicle_log_services_access_right_user | FACT | always | — | Officers have read-only on services, models, brands, states and tags and full CRUD on vehicles, contracts and odometer; administrators manage configuration | N-U17-172 |
| VDR-U17-C405 | FUNCTION MAPPING REQUIRED | hr_fleet/models/fleet_vehicle.py:65 | def _update_create_write_vals | FACT | hr_fleet installed | — | Driver employee and driver partner stay synchronised in both directions; reverse lookup applies only when exactly one employee has that work contact | N-U17-161 |
| VDR-U17-C406 | FUNCTION MAPPING REQUIRED | hr_fleet/models/fleet_vehicle.py:37 | employees_by_partner_id_and_company_id.get | FACT | hr_fleet installed | — | driver_employee_id is the first employee of the same company whose work contact is the driver | N-U17-161 |
| VDR-U17-C407 | FUNCTION MAPPING REQUIRED | hr_fleet/models/employee.py:60 | Cannot remove address from employees with linked cars | FACT | hr_fleet installed | — | Constraint on work_contact_id | N-U17-168 |
| VDR-U17-C408 | FUNCTION MAPPING REQUIRED | hr_fleet/models/employee.py:77 | car_ids.filtered(lambda c: c.driver_employee_id.id == employee.id) | FACT | hr_fleet installed | — | Work contact change updates driver and future driver on vehicles in sudo | N-U17-168 |
| VDR-U17-C409 | FUNCTION MAPPING REQUIRED | hr_fleet/security/hr_fleet_security.xml:4 | Hr Officer read rights on vehicle with employees assigned | FACT | hr_fleet installed | — | HR officers get read on vehicles that have a driver employee or future driver employee | N-U17-161 |
| VDR-U17-C410 | FUNCTION MAPPING REQUIRED | hr_fleet/models/employee.py:17 | mobility_card | FACT | hr_fleet installed | — | mobility_card needs the fleet officer group; car_ids needs fleet administrator or HR officer group | N-U17-175 |
| VDR-U17-C411 | FUNCTION MAPPING REQUIRED | hr_fleet/models/mail_activity_plan_template.py:13 | ('fleet_manager', "Fleet Manager") | FACT | hr_fleet installed | — | Activity plan template can name the fleet manager as responsible, limited to employee plans | N-U17-171 |
| VDR-U17-C412 | FUNCTION MAPPING REQUIRED | fleet/data/fleet_data.xml:4 | ir_cron_contract_costs_generator | OBSERVATION | restored DB | — | DB: fleet cron active daily; 4 vehicle states, 2 service types, 67 brands, 0 vehicles; 24 ACL and 9 rules equal source; hr_fleet adds 1 ACL, 1 rule and 1 plan template | N-U17-160 |
| VDR-U17-C413 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | — | Cost generation, accounting links and any module that adds contract cost lines are outside the studied modules; read fleet_account if installed | N-U17-175 |
| VDR-U17-C414 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:760 | _('Busy') if field.name == 'name' | FACT | private event, user neither organiser nor attendee | — | _fetch_query replaces non-public fields of others' private events by Busy or false | N-U17-180 |
| VDR-U17-C415 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:892 | calendar_is_private = not self.privacy | FACT | always | — | An event is private when its privacy is private or empty with an organiser whose default privacy is private | N-U17-180 |
| VDR-U17-C416 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:886 | _make_access_error("write", event) | FACT | writing another organiser's private event | — | Write raises an access error | N-U17-180 |
| VDR-U17-C417 | FUNCTION MAPPING REQUIRED | calendar/security/calendar_security.xml:15 | All Calendar Event for employees | FACT | always | — | Rule gives base.group_user domain true on calendar.event; the private-event rule has perm_read false so reading is masked in code, not by rule | N-U17-180 |
| VDR-U17-C418 | FUNCTION MAPPING REQUIRED | calendar/security/calendar_security.xml:8 | [('partner_ids', 'in', user.partner_id.id)] | FACT | always | — | Portal sees only events listing their partner; calendar.attendee ACL for portal is all zero with a domain-true rule | N-U17-181 |
| VDR-U17-C419 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:63 | values['state'] = 'accepted' | FACT | attendee partner is the creating user | — | Organiser attendance defaults to accepted | N-U17-182 |
| VDR-U17-C420 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:70 | attendees.event_id.check_access('write') | FACT | always | — | Creating or writing attendees requires write access on the event | N-U17-182 |
| VDR-U17-C421 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:27 | ('accepted', 'Yes') | FACT | always | — | Attendee states accepted, declined, tentative, needsAction; do_accept and do_decline post a message | N-U17-188 |
| VDR-U17-C422 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:83 | You cannot duplicate a calendar attendee | FACT | always | — | Attendee copy refused | N-U17-191 |
| VDR-U17-C423 | FUNCTION MAPPING REQUIRED | calendar/models/ir_http.py:20 | Invalid Invitation Token | FACT | calendar auth routes | — | Auth method calendar finds the attendee by token and, for a signed-in user, requires the same partner | N-U17-183 |
| VDR-U17-C424 | FUNCTION MAPPING REQUIRED | calendar/models/ir_http.py:25 | Invitation cannot be forwarded via email | FACT | signed-in different user | — | Forwarded links are refused for a different logged-in user | N-U17-183 |
| VDR-U17-C425 | FUNCTION MAPPING REQUIRED | calendar/controllers/main.py:12 | /calendar/meeting/accept | FACT | always | — | Accept and decline routes are http GET-capable with auth calendar and act in sudo on the token's attendee | N-U17-192 |
| VDR-U17-C426 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:714 | events.attendee_ids._send_invitation_emails() | FACT | create | — | create sends invitations for every attendee | N-U17-184 |
| VDR-U17-C427 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:119 | attendee.event_id.start > now | FACT | always | — | Invitation emails only for events starting in the future | N-U17-184 |
| VDR-U17-C428 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:141 | calendar.block_mail | FACT | always | — | System parameter calendar.block_mail or context no_mail_to_attendees suppresses attendee mail | N-U17-184 |
| VDR-U17-C429 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:176 | invitation.ics | FACT | attendee has email | — | An ICS attachment is generated and the mail posted with message_notify in sudo | N-U17-177 |
| VDR-U17-C430 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:218 | partner_not_sender | FACT | always | — | The acting user is not notified unless notify_author | N-U17-184 |
| VDR-U17-C431 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:133 | mail.mail_force_send_limit | FACT | force_send | RT | Mails are sent after commit only if fewer than the force-send limit, else left to the queue | N-U17-184 |
| VDR-U17-C432 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:862 | calendar_template_meeting_changedate | FACT | start changed on a future event | — | Existing attendees get a change-date mail | N-U17-185 |
| VDR-U17-C433 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:848 | 'state': 'needsAction' | FACT | another user changed time fields | — | Organiser attendee state is reset to needsAction | N-U17-185 |
| VDR-U17-C434 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:776 | Unable to save the recurrence with | FACT | always | — | Recurrence fields need update of all or following events | N-U17-185 |
| VDR-U17-C435 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_alarm.py:15 | [('notification', 'Notification'), ('email', 'Email')] | FACT | always | — | Alarm types notification and email, duration with minutes, hours or days, optional mail template | N-U17-178 |
| VDR-U17-C436 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:1274 | cron._trigger(at=at) | FACT | alarm on event | — | _setup_alarms creates cron triggers at start minus alarm duration, skipping past alarms | N-U17-186 |
| VDR-U17-C437 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_alarm_manager.py:166 | event.start - CAST(alarm.duration | FACT | cron | — | Alarms due between lastcall (default one week ago) and now are selected in SQL | N-U17-186 |
| VDR-U17-C438 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_alarm_manager.py:194 | a.state != 'declined' | FACT | cron | — | _send_reminder notifies attendees not declined for events not yet ended with notify_author and re-arms recurring events | N-U17-186 |
| VDR-U17-C439 | FUNCTION MAPPING REQUIRED | calendar/data/calendar_cron.xml:9 | model._send_reminder() | OBSERVATION | restored DB | — | DB: cron Calendar: Event Reminder active daily plus on-demand triggers; 7 alarms seeded; 15 ACL and 4 rules equal source; system parameter calendar.default_privacy is public; 0 events | N-U17-186 |
| VDR-U17-C440 | FUNCTION MAPPING REQUIRED | calendar_sms/models/calendar_alarm.py:11 | ('sms', 'SMS Text Message') | FACT | calendar_sms installed | RT | Alarm type sms with an SMS template; delivery depends on the SMS gateway whose failure handling is not in this module | N-U17-189 |
| VDR-U17-C441 | FUNCTION MAPPING REQUIRED | calendar_sms/models/calendar_alarm_manager.py:23 | events._do_sms_reminder(alarm) | FACT | calendar_sms installed | RT | _send_reminder is overridden to send SMS after email reminders | N-U17-189 |
| VDR-U17-C442 | FUNCTION MAPPING REQUIRED | calendar_sms/models/calendar_event.py:17 | partner.phone_sanitized | FACT | calendar_sms installed | RT | SMS goes to attendees with a sanitized phone who have not declined, excluding the organiser unless notify_responsible; put_in_queue is false | N-U17-189 |
| VDR-U17-C443 | FUNCTION MAPPING REQUIRED | calendar_sms/models/calendar_event.py:38 | default_composition_mode | FACT | calendar_sms installed | RT | Bulk SMS action opens the composer in mass mode on attendees | N-U17-189 |
| VDR-U17-C444 | FUNCTION MAPPING REQUIRED | hr_calendar/models/calendar_event.py:28 | schedule_by_partner = event.partner_ids._get_schedule | FACT | hr_calendar installed | — | Attendees whose employee schedule does not cover the event interval are added to unavailable_partner_ids | N-U17-187 |
| VDR-U17-C445 | FUNCTION MAPPING REQUIRED | hr_calendar/models/calendar_event.py:63 | interval_by_event[event] = Intervals([]) | FACT | hr_calendar installed | — | All-day events on days when the company is closed have an empty interval | N-U17-187 |
| VDR-U17-C446 | FUNCTION MAPPING REQUIRED | hr_calendar/models/res_partner.py:23 | self.env['hr.employee'].sudo()._read_group | FACT | hr_calendar installed | — | Attendee employees are read with sudo | N-U17-187 |
| VDR-U17-C447 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | RT | External calendar synchronisation, appointment booking and delivery receipts not studied | N-U17-193 |
| VDR-U17-C448 | FUNCTION MAPPING REQUIRED | hr_presence/models/hr_employee.py:31 | company = self.env.company | FACT | cron | — | _check_presence evaluates employees of the running user's current company only | N-U17-199 |
| VDR-U17-C449 | FUNCTION MAPPING REQUIRED | hr_presence/models/hr_employee.py:93 | You don't have the right to do this | FACT | always | — | Manual presence marks, SMS and log notes need the HR administrator group | N-U17-199 |
| VDR-U17-C450 | FUNCTION MAPPING REQUIRED | hr_presence/models/hr_employee.py:178 | employee.manually_set_presence | FACT | email or IP control enabled | — | Presence state uses manual mark, then IP and email signals during working hours | N-U17-194 |
| VDR-U17-C451 | FUNCTION MAPPING REQUIRED | hr_presence/models/hr_employee.py:143 | default_composition_mode='mass' | FACT | hr_presence installed | RT | SMS to absentees uses the mass composer on mobile_phone | N-U17-194 |
| VDR-U17-C452 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:883 | if presence_status == "online" | FACT | hr_presence_control_login | — | Base presence is present when online, absent when offline during working time | N-U17-194 |
| VDR-U17-C453 | FUNCTION MAPPING REQUIRED | hr_homeworking/models/hr_homeworking.py:22 | Only one default work location and one exceptional work location per day per employee | FACT | hr_homeworking installed | — | unique(employee_id, date) on exceptional locations | N-U17-200 |
| VDR-U17-C454 | FUNCTION MAPPING REQUIRED | hr_homeworking/security/security.xml:5 | homeworking: own | FACT | hr_homeworking installed | — | Employees read and write only their own location records; HR officers all | N-U17-195 |
| VDR-U17-C455 | FUNCTION MAPPING REQUIRED | hr_homeworking_calendar/wizard/homework_location_wizard.py:42 | employee_id.sudo().user_id.write({ | INFERENCE | weekly flag | — | Weekly default is written through the employee's user; an employee without a user gets no change | N-U17-200 |
| VDR-U17-C456 | FUNCTION MAPPING REQUIRED | hr_homeworking/models/hr_work_location.py:14 | domains = [(day, 'in', self.ids) for day in DAYS] | INFERENCE | location deletion | — | The list is an implicit AND of seven conditions, so deletion is blocked only for employees using the location on all seven weekdays | N-U17-200 |
| VDR-U17-C457 | FUNCTION MAPPING REQUIRED | hr_holidays_homeworking/models/hr_employee.py:13 | presence_holiday_ | FACT | hr_holidays_homeworking installed | — | Absence outranks location in the presence icon | N-U17-195 |
| VDR-U17-C458 | FUNCTION MAPPING REQUIRED | hr_homeworking_calendar/models/hr_employee.py:14 | def _get_worklocation | FACT | hr_homeworking_calendar installed | — | Calendar bridge returns weekday locations plus dated exceptions per employee | N-U17-195 |
| VDR-U17-C459 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:343 | request.copy({ | FACT | preventive recurring request set to done stage | — | Next request is created at schedule date plus interval while repeat is forever or before the end date | N-U17-201 |
| VDR-U17-C460 | FUNCTION MAPPING REQUIRED | maintenance/security/maintenance.xml:21 | Users are allowed to access their own maintenance requests | FACT | always | — | Internal users see requests they own, follow or are assigned; equipment they follow; ACL gives them full CRUD on requests | N-U17-196 |
| VDR-U17-C461 | FUNCTION MAPPING REQUIRED | hr_maintenance/security/equipment.xml:5 | maintenance.group_equipment_manager | FACT | hr_maintenance installed | — | hr.group_hr_user implies the equipment manager group | N-U17-201 |
| VDR-U17-C462 | FUNCTION MAPPING REQUIRED | hr_maintenance/models/equipment.py:26 | equipment.owner_user_id = equipment.employee_id.user_id.id | FACT | hr_maintenance installed | — | Equipment owner follows the assigned employee or the department manager | N-U17-196 |
| VDR-U17-C463 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_goal.py:166 | safe_eval(code, cxt, mode="exec") | FACT | computation_mode python | — | Python goal definitions execute stored code with safe_eval | N-U17-202 |
| VDR-U17-C464 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_challenge.py:246 | planned_challenges.write({'state': 'inprogress'}) | FACT | cron | — | Daily cron starts planned challenges, closes ended ones and updates running ones | N-U17-202 |
| VDR-U17-C465 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_challenge.py:278 | JOIN mail_presence as mp ON mp.user_id = gg.user_id | FACT | cron | — | Only goals of users with recent presence are updated | N-U17-202 |
| VDR-U17-C466 | FUNCTION MAPPING REQUIRED | gamification/models/gamification_challenge.py:654 | def _check_challenge_reward | FACT | always | — | Rewards at period end or in real time when the user reached every goal | N-U17-202 |
| VDR-U17-C467 | FUNCTION MAPPING REQUIRED | gamification/security/gamification_security.xml:3 | User can only see his/her goals | FACT | always | — | Users see own goals or goals of ranking-visible challenges; managers all | N-U17-197 |
| VDR-U17-C468 | FUNCTION MAPPING REQUIRED | hr_gamification/security/gamification_security.xml:14 | Base group user granted badge write/unlink access | FACT | hr_gamification installed | — | Internal users edit and delete badge grants they created; HR officers all | N-U17-203 |
| VDR-U17-C469 | FUNCTION MAPPING REQUIRED | hr_gamification/models/hr_employee.py:26 | ('challenge_id.challenge_category', '=', 'hr') | FACT | hr_gamification installed | — | Employee goals are goals of the linked user in HR-category challenges | N-U17-203 |
| VDR-U17-C470 | FUNCTION MAPPING REQUIRED | resource_mail/models/resource_resource.py:14 | color = fields.Integer(default=_default_color) | FACT | resource_mail installed | — | Resource gets a random colour and the user's presence status | N-U17-198 |
| VDR-U17-C471 | FUNCTION MAPPING REQUIRED | mail_bot_hr/__manifest__.py:9 | 'depends': ['mail_bot', 'hr'] | FACT | always | — | mail_bot_hr is views only (no models) bridging the bot state into the HR user form | N-U17-198 |
| VDR-U17-C472 | FUNCTION MAPPING REQUIRED | hr_livechat/__manifest__.py:7 | 'depends': ['hr', 'im_livechat'] | FACT | always | — | hr_livechat is views only, adding employee context to live chat views | N-U17-198 |
| VDR-U17-C473 | FUNCTION MAPPING REQUIRED | gamification_sale_crm/__manifest__.py:7 | 'depends': ['gamification', 'sale_crm'] | FACT | always | — | gamification_sale_crm is example data (goal definitions and challenges) only | N-U17-198 |
| VDR-U17-C474 | FUNCTION MAPPING REQUIRED | hr_presence/__manifest__.py:18 | 'depends': ['hr', 'hr_holidays', 'sms'] | FACT | always | — | hr_presence has no auto_install and depends on hr_holidays and sms; hr_homeworking has no auto_install | N-U17-204 |
| VDR-U17-C475 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | — | — | Ancillary modules were read at lighter depth; maintenance teams and aliases, gamification badges and karma ranks, org chart views were not studied in depth | N-U17-207 |
| VDR-U17-C476 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_allocation.py:1051 | leave_validation_type != 'no_validation' | FACT | always | — | Allocation activity_update tests the type's leave_validation_type, not allocation_validation_type, when deciding whether to schedule approval tasks (confirms the quirk noted in the prior candidate map; not a contradiction) | N-U17-081 |
| VDR-U17-C477 | FUNCTION MAPPING REQUIRED | hr_holidays/tests/test_automatic_leave_dates.py:470 | base_automation is not a dependency of hr_holidays | OBSERVATION | restored DB | — | A search of the 33 assigned modules finds no shipped base.automation or ir.sequence data (only a test mentions base.automation); DB shows 0 automation and 0 sequence rows for them | N-U17-207 |
| VDR-U17-C478 | FUNCTION MAPPING REQUIRED | hr_holidays/data/ir_cron_data.xml:4 | hr_leave_allocation_cron_accrual | OBSERVATION | restored DB | — | Source declares 13 cron records in the assigned modules (hr 2, hr_attendance 2, hr_holidays 2, hr_presence 1, hr_work_entry 1, hr_skills 1, fleet 1, gamification 2, calendar 1); DB has the same 13, all active, owner set, priority 5 | N-U17-207 |
| VDR-U17-C479 | FUNCTION MAPPING REQUIRED | hr/models/hr_employee.py:559 | def _get_version | INFERENCE | always | — | _get_version(date) returns the version in force at a date and is called by leave accrual, attendance overtime and work entry code (see claims in CAP-U17-04, -05, -06), so history of terms is consumed by downstream processes | N-U17-006 |
| VDR-U17-C480 | FUNCTION MAPPING REQUIRED | hr/security/hr_security.xml:28 | hr_employee_comp_rule | INFERENCE | always | — | Access scoping is expressed only by ACL rows, global rules and field groups; no state field or workflow is involved | N-U17-032 |
| VDR-U17-C481 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave.py:1122 | has been accepted | INFERENCE | approval | — | Approval posts an acceptance message to the employee and creates the calendar absence, which shows the purpose of keeping availability consistent | N-U17-041 |
| VDR-U17-C482 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_type.py:47 | create_calendar_meeting | FACT | always | — | Per-type booleans create_calendar_meeting and support_document, plus request_unit and allows_negative, make the behaviours optional | N-U17-056 |
| VDR-U17-C483 | FUNCTION MAPPING REQUIRED | hr_holidays/models/hr_leave_accrual_plan_level.py:115 | action_with_unused_accruals = fields.Selection( | INFERENCE | always | — | Levels offer an unused-accrual action (lost or carry over) and a carry-over limit, which expresses use-it-or-lose-it policy | N-U17-066 |
| VDR-U17-C484 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance_overtime.py:19 | ('to_approve', "To Approve") | FACT | always | — | Overtime line status selection to_approve, approved, refused | N-U17-097 |
| VDR-U17-C485 | FUNCTION MAPPING REQUIRED | hr_attendance/models/hr_attendance.py:331 | all_overtime_lines.unlink() | INFERENCE | every attendance change | — | Each change deletes and recreates all overtime lines in the affected date domain, so cost grows with history in the range | N-U17-103 |
| VDR-U17-C486 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_work_entry.py:26 | version_id = fields.Many2one('hr.version' | FACT | always | — | A work entry belongs to an employee, a version, a date and a duration and has a type | N-U17-105 |
| VDR-U17-C487 | FUNCTION MAPPING REQUIRED | hr_work_entry/models/hr_version.py:178 | attendances_by_resource = self.sudo()._get_attendance_intervals | FACT | always | — | Generation reads calendar attendance intervals and resource calendar leaves for the period | N-U17-120 |
| VDR-U17-C488 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:1003 | def create_employee_from_applicant | INFERENCE | always | — | A single model carries the application from intake to the employee hand-off, giving one place to track the pipeline | N-U17-127 |
| VDR-U17-C489 | FUNCTION MAPPING REQUIRED | hr_recruitment/models/hr_applicant.py:111 | ('blocked', 'Blocked') | FACT | always | — | kanban_state normal, done, waiting, blocked is reset to normal on stage change; application_status is computed separately | N-U17-137 |
| VDR-U17-C490 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_skill_type.py:24 | is_certification = fields.Boolean | INFERENCE | always | — | A certification flag on skill types, validity dates on individual skills and the expiry cron serve staffing, training and compliance reminders | N-U17-147 |
| VDR-U17-C491 | FUNCTION MAPPING REQUIRED | hr_skills_event/__manifest__.py:21 | 'auto_install': True | FACT | always | — | hr_skills_event, hr_skills_slides and hr_skills_survey declare auto_install | N-U17-155 |
| VDR-U17-C492 | FUNCTION MAPPING REQUIRED | hr_skills/models/hr_resume_line.py:33 | certificate_file = fields.Binary | FACT | always | — | Resume lines store an optional certificate file that every internal user can read through the read-all rule | N-U17-158 |
| VDR-U17-C493 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle.py:24 | _name = 'fleet.vehicle' | INFERENCE | always | — | One vehicle record aggregates driver, odometer, services, contracts and assignment history | N-U17-162 |
| VDR-U17-C494 | FUNCTION MAPPING REQUIRED | fleet/models/fleet_vehicle_assignation_log.py:15 | date_end = fields.Date(string="End Date") | INFERENCE | always | — | Open-ended or overlapping assignment history is possible because the end date is never written by code; see fl_assign_end | N-U17-174 |
| VDR-U17-C495 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_event.py:71 | _name = 'calendar.event' | FACT | always | — | calendar.event holds organiser, partners, attendees, alarms, privacy, recurrence and links to a document via res_model and res_id | N-U17-176 |
| VDR-U17-C496 | FUNCTION MAPPING REQUIRED | hr_calendar/models/calendar_event.py:14 | _compute_unavailable_partner_ids | INFERENCE | hr_calendar installed | — | The HR bridge computes unavailable attendees from employee schedules to help scheduling | N-U17-179 |
| VDR-U17-C497 | FUNCTION MAPPING REQUIRED | calendar/models/calendar_attendee.py:209 | send_after_commit | FACT | force_send under limit | RT | Reminder and invitation mail is sent after commit or left to the mail queue, so delivery depends on the scheduler and queue | N-U17-190 |
| VDR-U17-C498 | FUNCTION MAPPING REQUIRED | hr_maintenance/__manifest__.py:10 | 'depends': ['hr', 'maintenance'] | FACT | always | — | hr_maintenance depends on hr and maintenance; hr_presence depends on hr, hr_holidays and sms; gamification bridges depend on sale_crm or hr | N-U17-205 |
| VDR-U17-C499 | FUNCTION MAPPING REQUIRED | hr_presence/models/hr_employee.py:31 | company = self.env.company | INFERENCE | cron | — | Presence control covers one company per run, so multi-company set-ups are partially covered | N-U17-206 |
