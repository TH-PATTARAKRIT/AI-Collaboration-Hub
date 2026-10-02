# U51 — CRM, event, HR, gamification bridge modules (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U51
- Modules: crm_iap_mine, crm_mail_plugin, crm_sms, event_booth, event_crm_sale, event_product, event_sms, gamification_sale_crm, hr (remaining: hr_version, mail_activity_plan/template, discuss_channel, hr_work_location), hr_holidays_homeworking, hr_homeworking, hr_homeworking_calendar, hr_hourly_cost, hr_livechat, hr_maintenance, hr_recruitment_sms, hr_skills_event, hr_skills_slides, hr_skills_survey, hr_timesheet_attendance, html_builder (residual Python), iap_crm, iap_mail
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: Bridge/extension modules study. Core modules (crm, event, hr, gamification, iap) studied in U38/U40/U41; this unit covers only what each bridge adds. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U51-01 — IAP Lead Mining (crm_iap_mine)

### D1 — Model: crm.iap.lead.mining.request
The module introduces a dedicated wizard model for requesting lead generation from the IAP cloud service.

### D2 — Key constants and endpoint
- `DEFAULT_ENDPOINT = 'https://iap-services.odoo.com'` (crm_iap_mine/models/crm_iap_lead_mining_request.py:13)
- `MAX_LEAD = 200`, `MAX_CONTACT = 5`, `CREDIT_PER_COMPANY = 1`, `CREDIT_PER_CONTACT = 1` (lines 15–19)
- IAP endpoint: `/api/dnb/1/search_by_criteria` (line 267)

### D3 — Supporting lookup models
- `crm.iap.lead.industry` — industry tags with `reveal_ids` (comma-separated) used for filtering (crm_iap_mine/models/crm_iap_lead_industry.py:8–21)
- `crm.iap.lead.role` — contact role categories with `reveal_id` (crm_iap_mine/models/crm_iap_lead_role.py:8–19)
- `crm.iap.lead.seniority` — contact seniority with `reveal_id` (crm_iap_mine/models/crm_iap_lead_seniority.py:8–18)
- `crm.iap.lead.helpers` — service model with `lead_vals_from_response` helper (crm_iap_mine/models/crm_iap_lead_helpers.py:5)

### D4 — crm.lead extension
`crm.lead` gains `lead_mining_request_id` Many2one (crm_iap_mine/models/crm_lead.py:10) and `action_generate_leads` button method (line 15).

---

## CAP-U51-02 — CRM Mail Plugin Bridge (crm_mail_plugin)

### D1 — Controller extension
`MailPluginController` subclass adds `_fetch_partner_leads` and `_get_contact_data` overrides to inject CRM lead data into the mail plugin sidebar (crm_mail_plugin/controllers/mail_plugin.py:16–75).

### D2 — Deprecated legacy routes
`CrmClient` controller exposes legacy JSON-RPC routes for older plugin versions: `/mail_client_extension/log_single_mail_content`, `/mail_client_extension/lead/get_by_partner_id`, `/mail_client_extension/lead/create_from_partner`, `/mail_client_extension/lead/open` (crm_mail_plugin/controllers/crm_client.py:13–64).

### D3 — Lead creation route
`/mail_plugin/lead/create` (POST, auth=outlook) creates a `crm.lead` record from email subject and body, linked to a partner (crm_mail_plugin/controllers/crm_client.py:42–54).

### D4 — Model stub
`crm.lead._form_view_auto_fill` is a deprecated model method retained for old plugin compatibility (crm_mail_plugin/models/crm_lead.py:11–23).

---

## CAP-U51-03 — CRM SMS (crm_sms)

### D1 — No new models
`crm_sms` contains only a test file; no models Python file exists under `crm_sms/models/`. The module's Python surface is limited to `__init__.py` and `__manifest__.py`. All functional additions are in data/view XML. (Source: directory scan, crm_sms module tree.)

---

## CAP-U51-04 — Event Booth (event_booth)

### D1 — New model: event.booth
`event.booth` inherits `event.type.booth`, `mail.thread`, `mail.activity.mixin`. Fields: `event_id` (Many2one event.event, cascade), `partner_id`, `contact_name`, `contact_email`, `contact_phone`, `state` (available/unavailable), `is_available` (computed) (event_booth/models/event_booth.py:7–28).

### D2 — Booth template model: event.type.booth
`event.type.booth` holds `name`, `event_type_id`, `booth_category_id` and a whitelist method `_get_event_booth_fields_whitelist` returning `['name', 'booth_category_id']` (event_booth/models/event_type_booth.py:7–27).

### D3 — Booth category model: event.booth.category
Inherits `image.mixin`; fields: `active`, `name`, `sequence`, `description` (Html), `booth_ids` (event_booth/models/event_booth_category.py:7–18).

### D4 — event.event extension
`event.event` gains `event_booth_ids`, `event_booth_count`, `event_booth_count_available`, `event_booth_category_ids`, `event_booth_category_available_ids` computed fields. `_compute_event_booth_ids` synchronises booths from the event type template when `event_type_id` changes (event_booth/models/event_event.py:10–89).

### D5 — Confirmation flow
`EventBooth.action_confirm` writes `state='unavailable'` and `_post_confirmation_message` posts a chatter note using `event_booth.event_booth_booked_template` template (event_booth/models/event_booth.py:72–87).

---

## CAP-U51-05 — Event CRM Sale Bridge (event_crm_sale)

### D1 — Sale-order-based lead grouping override
`event.registration._get_lead_grouping` overrides the CRM lead grouping logic: registrations with a `sale_order_id` are grouped by that sale order, finding existing leads linked to the same order and rule before creating new ones (event_crm_sale/models/event_registration.py:12–48).

---

## CAP-U51-06 — Event Product Bridge (event_product)

### D1 — EventTypeTicket: product association
`event.type.ticket` inherits gains `product_id` (Many2one product.product, domain `service_tracking='event'`), `currency_id`, `price`, `price_reduce` fields. `_default_product_id` resolves to `event_product.product_product_event` (event_product/models/event_type_ticket.py:15–97).

### D2 — EventEventTicket: tax-inclusive prices
`event.event.ticket` adds `price_reduce_taxinc` and `price_incl` computed fields using `taxes_id.compute_all` (event_product/models/event_event_ticket.py:6–38).

### D3 — ProductTemplate: service_tracking extension
`product.template.service_tracking` gains `('event', 'Event Registration')` selection value, and `_service_tracking_blacklist` includes `'event'` (event_product/models/product_template.py:7–12).

### D4 — ProductProduct: constraint
`product.product` adds `event_ticket_ids` One2many and a constraint `_check_event_ticket_service_tracking` raising ValidationError if any product linked to event tickets does not have `service_tracking='event'` (event_product/models/product_product.py:6–18).

### D5 — EventRegistration: sale_status field
`event.registration` gains `sale_status` Selection (`to_pay`, `sold`, `free`) computed via `_compute_registration_status`; default is `free` when no order exists (event_product/models/event_registration.py:6–24).

### D6 — EventEvent: currency relay
`event.event` gains `currency_id` related to `company_id.currency_id` (event_product/models/event_event.py:7–9).

---

## CAP-U51-07 — Event SMS (event_sms)

### D1 — EventMail SMS notification type
`event.mail.notification_type` gains `('sms', 'SMS')` selection value. `template_ref` reference field gains `sms.template` option. `_execute_event_based_for_registrations` delegates to `_send_sms` when type is `sms` (event_sms/models/event_mail.py:4–30).

### D2 — EventMailRegistration: SMS dispatch
`event.mail.registration._execute_on_registrations` processes SMS schedulers by calling `scheduler._send_sms` on registration sets, then sets `mail_sent=True` (event_sms/models/event_mail_registration.py:7–15).

### D3 — EventTypeMail: same extension
`event.type.mail` gains the same SMS selection on `notification_type` and `template_ref` (event_sms/models/event_type_mail.py:4–13).

### D4 — SmsTemplate: event context filter
`sms.template._search` adds domain `model='event.registration'` when context key `filter_template_on_event` is set. `unlink` also cascade-deletes linked `event.mail` and `event.type.mail` records (event_sms/models/sms_template.py:10–28).

---

## CAP-U51-08 — Gamification Sale CRM (gamification_sale_crm)

### D1 — Data-only module
`gamification_sale_crm` contains no Python model files. It is a data-only bridge with `auto_install=True` that loads gamification goal/challenge XML data for `sale_crm`. Source: `__manifest__.py` (`data`, `demo` keys; no `models` directory) (gamification_sale_crm/__manifest__.py:1–14).

---

## CAP-U51-09 — HR module remaining files (hr)

### D1 — hr.version model
`hr.version` (`_name='hr.version'`) is a versioned contract/employee record model. Key fields include: `employee_id`, `date_version`, `wage`, `contract_date_start`, `contract_date_end`, `structure_type_id`, `resource_calendar_id`, `department_id`, `job_id`, `sex`, `marital`, `identification_id`, `ssnid`, `passport_id`, personal address fields, departure fields (hr/models/hr_version.py:34–200).

### D2 — hr.version constraint: no overlapping contracts
`_check_dates` enforces non-overlapping contract periods per employee, raising `ValidationError` (hr/models/hr_version.py:239–278).

### D3 — hr.version: template support
`get_values_from_contract_template` copies whitelisted fields (`job_id`, `department_id`, `contract_type_id`, `structure_type_id`, `wage`, `resource_calendar_id`, `hr_responsible_id`) from a template version (hr/models/hr_version.py:443–458).

### D4 — hr.version: UniqueIndex
`_check_unique_date_version` unique index `(employee_id, date_version) WHERE active = TRUE AND employee_id IS NOT NULL` (hr/models/hr_version.py:202–205).

### D5 — hr.work.location model
`hr.work.location` defines `name`, `company_id`, `location_type` (home/office/other), `address_id`, `location_number` (hr/models/hr_work_location.py:7–20).

### D6 — discuss.channel: department auto-subscription
`discuss.channel` gains `subscription_department_ids` Many2many `hr.department`. `_subscribe_users_automatically_get_members` adds all active department member user partners to the channel (hr/models/discuss_channel.py:10–35).

### D7 — mail.activity.plan: department assignment
`mail.activity.plan` gains `department_id` and `department_assignable` (computed True when `res_model='hr.employee'`). Constraint blocks HR-specific types on non-employee models (hr/models/mail_activity_plan.py:9–44).

### D8 — mail.activity.plan.template: HR responsible types
`mail.activity.plan.template.responsible_type` gains `('coach', 'Coach')`, `('manager', 'Manager')`, `('employee', 'Employee')` selection values. `_determine_responsible` resolves to the coach, manager, or employee user, with fallback traversal up the hierarchy (hr/models/mail_activity_plan_template.py:9–109).

---

## CAP-U51-10 — HR Holidays Homeworking (hr_holidays_homeworking)

### D1 — Presence icon override for holidays
`hr.employee._compute_presence_icon` override: when employee `is_absent`, sets `hr_icon_display` to `presence_holiday_absent` or `presence_holiday_present` depending on `hr_presence_state`; otherwise delegates to work location (hr_holidays_homeworking/models/hr_employee.py:4–18).

---

## CAP-U51-11 — HR Homeworking (hr_homeworking)

### D1 — DAYS constant and employee location model
`DAYS` list: `['monday_location_id', ..., 'sunday_location_id']` (7 elements) (hr_homeworking/models/hr_homeworking.py:5).

`hr.employee.location` model: `work_location_id`, `employee_id`, `date`, `day_week_string` (computed). Unique constraint: one location record per (employee_id, date) (hr_homeworking/models/hr_homeworking.py:8–28).

### D2 — hr.employee: day-of-week location fields
`hr.employee` gains seven Many2one fields `monday_location_id` ... `sunday_location_id` plus `exceptional_location_id` (computed) and `today_location_name` (hr_homeworking/models/hr_employee.py:11–25).

### D3 — Dynamic view architecture for day grouping
`hr.employee.get_views` replaces placeholder `today_location_name` in search/list view arch with the actual current-day field name at view-fetch time (hr_homeworking/models/hr_employee.py:34–42).

### D4 — Presence icon integration
`_compute_presence_icon` sets `hr_icon_display` to `presence_home`, `presence_office`, or `presence_other` based on `location_type` of the current day's or exceptional location (hr_homeworking/models/hr_employee.py:55–63).

### D5 — hr.employee.public: day location fields mirrored
`hr.employee.public` exposes all seven day location fields and `today_location_name` (hr_homeworking/models/hr_employee_public.py:7–14).

### D6 — res.users: location field sync
`res.users` gains seven related day-location Many2one fields delegated to `employee_id`. `_get_employee_fields_to_sync`, `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS` include `DAYS` (hr_homeworking/models/res_users.py:10–27).

### D7 — im_status: location suffix
`res.users._compute_im_status` appends location type prefix (`home_`, `office_`, `other_`) to IM status string when a location type is set (hr_homeworking/models/res_users.py:29–38). [RT: the resulting combined status value is consumed by the frontend — exact rendering is runtime-dependent.]

### D8 — hr.work.location: deletion guard
`hr.work.location._unlink_except_used_by_employee` prevents deletion of locations used in any day-of-week field or exceptional location record (hr_homeworking/models/hr_work_location.py:12–19).

---

## CAP-U51-12 — HR Homeworking Calendar (hr_homeworking_calendar)

### D1 — _get_worklocation method
`hr.employee._get_worklocation(start_date, end_date)` builds a dict keyed by employee id with all seven day-location values plus an `exceptions` sub-dict of date-keyed exceptional locations from `hr.employee.location` records in the period (hr_homeworking_calendar/models/hr_employee.py:14–50).

### D2 — res.partner bridge
`res.partner.get_worklocation` finds the employee linked to partner's `work_contact_id` within current company and delegates to `_get_worklocation` (hr_homeworking_calendar/models/res_partner.py:9–13).

### D3 — Wizard: homework.location.wizard
`homework.location.wizard` (`_name='homework.location.wizard'`) supports setting a location either as a one-off exception (creates/updates `hr.employee.location`) or as a weekly default (writes the day-of-week field on the user). The `weekly` boolean determines which path is taken (hr_homeworking_calendar/wizard/homework_location_wizard.py:8–61).

---

## CAP-U51-13 — HR Hourly Cost (hr_hourly_cost)

### D1 — hourly_cost field
`hr.employee.hourly_cost` Monetary field, `groups='hr.group_hr_user'`, `default=0.0`, `tracking=True` (hr_hourly_cost/models/hr_employee.py:9–10).

---

## CAP-U51-14 — HR Livechat (hr_livechat)

### D1 — Data-only module
`hr_livechat` contains no Python model files (only `__init__.py` and `__manifest__.py`). Functional additions are in XML views/data. (Source: directory scan — no `models/` directory present.)

---

## CAP-U51-15 — HR Maintenance (hr_maintenance)

### D1 — maintenance.equipment: employee/department assignment
`maintenance.equipment` gains `employee_id`, `department_id`, `equipment_assign_to` (department/employee/other), `owner_user_id`, `assign_date` fields. On create/write, the employee or department manager user is subscribed to the equipment record via `message_subscribe` (hr_maintenance/models/equipment.py:6–78).

### D2 — maintenance.request: employee link
`maintenance.request` gains `employee_id` (defaulting to `env.user.employee_id`) and filtered `equipment_id` domain. Creates message subscription for the employee user on create/write (hr_maintenance/models/equipment.py:81–127).

### D3 — hr.employee: equipment count
`hr.employee` gains `equipment_ids` One2many and `equipment_count` Integer computed field (hr_maintenance/models/hr_employee.py:7–13).

### D4 — hr.employee.public: equipment count relay
`hr.employee.public.equipment_count` is related to `employee_id.equipment_count` (hr_maintenance/models/hr_employee_public.py:9).

### D5 — hr.departure.wizard: free equipment option
`hr.departure.wizard` gains `unassign_equipment` Boolean (default True). On `action_register_departure`, clears `equipment_ids` on the employees if flag is set (hr_maintenance/wizard/hr_departure_wizard.py:7–15).

---

## CAP-U51-16 — HR Recruitment SMS (hr_recruitment_sms)

### D1 — action_send_sms on applicant
`hr.applicant.action_send_sms` opens the SMS composer wizard in mass-composition mode for selected applicants (hr_recruitment_sms/models/hr_applicant.py:9–16).

---

## CAP-U51-17 — HR Skills Event (hr_skills_event)

### D1 — hr.resume.line: onsite course type
`hr.resume.line` gains `event_id` Many2one `event.event` (stored, computed, indexed), `course_type` selection extension `('onsite', 'Onsite')`. Color is `#714a66` for onsite lines (hr_skills_event/models/hr_resume_line.py:7–36).

### D2 — event.event: auto-register employee
`event.event.create` override: when context key `hr_skills_event_add_employee` is set, the current (or context-specified) employee's `work_contact_id` partner is auto-registered as an attendee (hr_skills_event/models/event_event.py:9–25).

---

## CAP-U51-18 — HR Skills Slides (hr_skills_slides)

### D1 — hr.resume.line: eLearning course type
`hr.resume.line` gains `channel_id` Many2one `slide.channel` (stored, computed, indexed), `course_url` (related), `duration` Integer (computed from `channel_id.total_time`), `course_type` extension `('elearning', 'eLearning')`. Color is `#00a5b7` (hr_skills_slides/models/hr_resume_line.py:7–41).

### D2 — slide.channel.partner: auto-create resume line on completion
`_post_completion_update_hook` override: on completion of a `slide.channel` by a partner linked to an employee, creates a `hr.resume.line` of type `training` with `course_type='elearning'` if none exists for that (employee, channel) pair (hr_skills_slides/models/slide_channel.py:12–53).

### D3 — Chatter notifications
`SlideChannel._action_add_members` and `_remove_membership` post messages on the employee's chatter with course enrollment/departure events (hr_skills_slides/models/slide_channel.py:70–106).

### D4 — hr.employee: subscribed_courses computed
`hr.employee.subscribed_courses` Many2many related to `user_partner_id.slide_channel_ids`, with `courses_completion_text` and `has_subscribed_courses` computed fields (hr_skills_slides/models/hr_employee.py:10–27).

---

## CAP-U51-19 — HR Skills Survey (hr_skills_survey)

### D1 — hr.resume.line: certification fields
`hr.resume.line` gains `survey_id` Many2one `survey.survey`, `department_id` (related, stored), `expiration_status` Selection (expired/expiring/valid) computed from `date_end` with 3-month warning window (hr_skills_survey/models/hr_resume_line.py:8–27).

### D2 — survey.survey: certification validity
`survey.survey.certification_validity_months` Integer field (default 0 = never expires) (hr_skills_survey/models/survey_survey.py:9–13).

### D3 — survey.user_input: auto-create resume line on certification
`survey.user_input._mark_done` override: on a successful certification attempt, creates or updates a `hr.resume.line` of type `certification` for each linked employee, computing `date_end = date_start + validity_months` (hr_skills_survey/models/survey_user.py:13–55).

---

## CAP-U51-20 — HR Timesheet Attendance (hr_timesheet_attendance)

### D1 — SQL view report model
`hr.timesheet.attendance.report` is a read-only SQL view model (`_auto=False`). Fields: `employee_id`, `date`, `total_timesheet`, `total_attendance`, `total_difference`, `timesheets_cost`, `attendance_cost`, `cost_difference`, `company_id` (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:7–19).

### D2 — SQL definition
`init()` creates the view as a UNION ALL of attendance rows (from `hr_attendance`) and timesheet rows (from `account_analytic_line` where `project_id IS NOT NULL`), joined with `hr_employee.hourly_cost`. Cost fields are `hours * hourly_cost` (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:22–72).

### D3 — Menu access gate
`ir.ui.menu._load_menus_blacklist` hides the attendance-timesheet report menu for users without `hr_timesheet.group_hr_timesheet_user` (hr_timesheet_attendance/models/ir_ui_menu.py:9–13).

---

## CAP-U51-21 — HTML Builder (html_builder — residual Python)

### D1 — No Python models
The `html_builder` module at this revision contains no Python model files. The `models/` directory does not exist. Python is limited to `__init__.py`, `__manifest__.py`, and a test file for asset bundle tests. All logic is JavaScript/SCSS. (Source: directory scan — no models under html_builder.)

---

## CAP-U51-22 — IAP CRM (iap_crm)

### D1 — reveal_id field on crm.lead
`crm.lead.reveal_id` Char field with `index='btree_not_null'` — stores the IAP reveal technical identifier (DUNS or clearbit_id) from lead mining (iap_crm/models/crm_lead.py:10–11).

### D2 — Merge support
`crm.lead._merge_get_fields` appends `reveal_id` so it is preserved during lead merges (iap_crm/models/crm_lead.py:12–13).

---

## CAP-U51-23 — IAP Mail (iap_mail)

### D1 — iap.account: mail.thread mixin
`iap.account` inherits `mail.thread` and gains `company_ids` (tracking), `warning_threshold` Float, `warning_user_ids` Many2many `res.users` (tracking) (iap_mail/models/iap_account.py:6–13).

### D2 — Notification bus methods
`_send_success_notification`, `_send_error_notification`, `_send_no_credit_notification` push bus notifications via `env.user._bus_send('iap_notification', params)` (iap_mail/models/iap_account.py:16–40).

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U51-C001 | crm_iap_mine.constants | crm_iap_mine/models/crm_iap_lead_mining_request.py:13 | `DEFAULT_ENDPOINT = 'https://iap-services.odoo.com'` | FACT | — | — | Default IAP endpoint for lead mining is iap-services.odoo.com | N-U51-001 |
| VDR-U51-C002 | crm_iap_mine.constants | crm_iap_mine/models/crm_iap_lead_mining_request.py:15 | `MAX_LEAD = 200` | FACT | — | — | Maximum leads per mining request is 200 | N-U51-001 |
| VDR-U51-C003 | crm_iap_mine.constants | crm_iap_mine/models/crm_iap_lead_mining_request.py:17 | `MAX_CONTACT = 5` | FACT | — | — | Maximum contacts per company in mining request is 5 | N-U51-001 |
| VDR-U51-C004 | crm_iap_mine.constants | crm_iap_mine/models/crm_iap_lead_mining_request.py:18 | `CREDIT_PER_COMPANY = 1` | FACT | — | — | Each company discovery costs 1 IAP credit | N-U51-001 |
| VDR-U51-C005 | crm_iap_mine.model | crm_iap_mine/models/crm_iap_lead_mining_request.py:23 | `_name = 'crm.iap.lead.mining.request'` | FACT | — | — | Model name is crm.iap.lead.mining.request | N-U51-001 |
| VDR-U51-C006 | crm_iap_mine.state | crm_iap_mine/models/crm_iap_lead_mining_request.py:37 | `state = fields.Selection([('draft', 'Draft'), ('error', 'Error'), ('done', 'Done')]` | FACT | — | — | Mining request states are draft, error, done | N-U51-001 |
| VDR-U51-C007 | crm_iap_mine.search_type | crm_iap_mine/models/crm_iap_lead_mining_request.py:41 | `search_type = fields.Selection([('companies', 'Companies'), ('people', 'Companies and their Contacts')]` | FACT | — | — | Target can be companies only, or companies plus contacts | N-U51-001 |
| VDR-U51-C008 | crm_iap_mine.endpoint | crm_iap_mine/models/crm_iap_lead_mining_request.py:267 | endpoint = self.env['ir.config_parameter'].sudo | FACT | — | — | IAP call uses path /api/dnb/1/search_by_criteria | N-U51-001 |
| VDR-U51-C009 | crm_iap_mine.industry | crm_iap_mine/models/crm_iap_lead_industry.py:14 | `reveal_ids = fields.Char(required=True)` | FACT | — | — | Industry model stores reveal_ids as comma-separated string | N-U51-001 |
| VDR-U51-C010 | crm_iap_mine.role | crm_iap_mine/models/crm_iap_lead_role.py:13 | `reveal_id = fields.Char(required=True)` | FACT | — | — | Role model stores a single reveal_id string | N-U51-001 |
| VDR-U51-C011 | crm_iap_mine.lead_ext | crm_iap_mine/models/crm_lead.py:10 | lead_mining_request_id | FACT | — | — | crm.lead gains lead_mining_request_id with btree_not_null index | N-U51-001 |
| VDR-U51-C012 | crm_iap_mine.helpers | crm_iap_mine/models/crm_iap_lead_helpers.py:33 | `def lead_vals_from_response(self, lead_type, team_id, tag_ids, user_id, company_data, people_data):` | FACT | — | — | Helper maps IAP response company_data dict to crm.lead create vals | N-U51-001 |
| VDR-U51-C013 | crm_iap_mine.credit_error | crm_iap_mine/models/crm_iap_lead_mining_request.py:253 | `if response.get('credit_error'):` | FACT | — | — | Insufficient-credits condition sets error_type='credits' and state='error' | N-U51-001 |
| VDR-U51-C014 | crm_mail_plugin.fetch_leads | crm_mail_plugin/controllers/mail_plugin.py:16 | `def _fetch_partner_leads(self, partner, limit=5, offset=0):` | FACT | — | — | Mail plugin controller fetches up to 5 CRM leads per partner by default | N-U51-002 |
| VDR-U51-C015 | crm_mail_plugin.create | crm_mail_plugin/controllers/crm_client.py:42 | `@http.route('/mail_plugin/lead/create', type='jsonrpc', auth='outlook', cors="*")` | FACT | — | — | Route /mail_plugin/lead/create creates crm.lead from email subject/body | N-U51-002 |
| VDR-U51-C016 | crm_mail_plugin.whitelist | crm_mail_plugin/controllers/mail_plugin.py:71 | def _mail_content_logging_models_whitelist(self) | FACT | — | `crm.lead` create access | crm.lead is added to mail content logging whitelist when user can create leads | N-U51-002 |
| VDR-U51-C017 | event_booth.model | event_booth/models/event_booth.py:7 | `_name = 'event.booth'` | FACT | — | — | event.booth is the new booth instance model | N-U51-003 |
| VDR-U51-C018 | event_booth.state | event_booth/models/event_booth.py:24 | state = fields.Selection | FACT | — | — | Booth state is available or unavailable | N-U51-003 |
| VDR-U51-C019 | event_booth.confirm | event_booth/models/event_booth.py:82 | `def action_confirm(self, additional_values=None):` | FACT | — | — | action_confirm writes state=unavailable and posts confirmation message | N-U51-003 |
| VDR-U51-C020 | event_booth.category | event_booth/models/event_booth_category.py:7 | `_name = 'event.booth.category'` | FACT | — | — | event.booth.category holds booth type with image, name, sequence, description | N-U51-003 |
| VDR-U51-C021 | event_booth.type_template | event_booth/models/event_type_booth.py:8 | `_name = 'event.type.booth'` | FACT | — | — | event.type.booth is the template from which booths are copied on event creation | N-U51-003 |
| VDR-U51-C022 | event_booth.event_sync | event_booth/models/event_event.py:28 | `def _compute_event_booth_ids(self):` | FACT | — | — | Changing event_type_id removes available booths and re-creates from type templates | N-U51-003 |
| VDR-U51-C023 | event_booth.count | event_booth/models/event_event.py:16 | string='Total Booths | FACT | — | — | event.event computes total and available booth counts | N-U51-003 |
| VDR-U51-C024 | event_crm_sale.grouping | event_crm_sale/models/event_registration.py:12 | `def _get_lead_grouping(self, rules, rule_to_new_regs):` | FACT | — | — | Registrations with sale_order_id are grouped by sale order for CRM lead creation | N-U51-004 |
| VDR-U51-C025 | event_product.ticket_product | event_product/models/event_type_ticket.py:22 | domain=[("service_tracking | FACT | — | — | Event type ticket requires a product with service_tracking='event' | N-U51-005 |
| VDR-U51-C026 | event_product.default_product | event_product/models/event_type_ticket.py:16 | `return self.env.ref('event_product.product_product_event', raise_if_not_found=False)` | FACT | — | — | Default product for event tickets is the event_product.product_product_event record | N-U51-005 |
| VDR-U51-C027 | event_product.price_incl | event_product/models/event_event_ticket.py:13 | string='Price include | FACT | — | — | event.event.ticket exposes tax-inclusive price as price_incl | N-U51-005 |
| VDR-U51-C028 | event_product.service_tracking | event_product/models/product_template.py:7 | service_tracking | FACT | — | — | product.template.service_tracking gains 'event' option | N-U51-005 |
| VDR-U51-C029 | event_product.constraint | event_product/models/product_product.py:11 | `def _check_event_ticket_service_tracking(self):` | FACT | — | — | ValidationError raised if product linked to event ticket lacks service_tracking='event' | N-U51-005 |
| VDR-U51-C030 | event_product.sale_status | event_product/models/event_registration.py:7 | sale_status = fields.Selection | FACT | — | — | event.registration.sale_status default is 'free' when no order | N-U51-005 |
| VDR-U51-C031 | event_sms.notif_type | event_sms/models/event_mail.py:7 | `notification_type = fields.Selection(selection_add=[('sms', 'SMS')])` | FACT | — | — | event.mail gains SMS notification type | N-U51-006 |
| VDR-U51-C032 | event_sms.send | event_sms/models/event_mail.py:20 | `def _send_sms(self, registrations):` | FACT | — | — | _send_sms calls _message_sms_schedule_mass on registrations with mass_keep_log=True | N-U51-006 |
| VDR-U51-C033 | event_sms.template_cascade | event_sms/models/sms_template.py:24 | res = super().unlink() | FACT | — | — | Deleting sms.template cascade-deletes linked event.mail and event.type.mail records | N-U51-006 |
| VDR-U51-C034 | event_sms.context_filter | event_sms/models/sms_template.py:19 | `if self.env.context.get('filter_template_on_event'):` | FACT | — | — | context key filter_template_on_event restricts sms.template search to event.registration model | N-U51-006 |
| VDR-U51-C035 | gamification_sale_crm.data_only | gamification_sale_crm/__manifest__.py:7 | `'depends': ['gamification', 'sale_crm'],` | FACT | — | — | gamification_sale_crm has no Python models; pure data/XML module | N-U51-007 |
| VDR-U51-C036 | hr_version.model | hr/models/hr_version.py:34 | `_name = 'hr.version'` | FACT | — | — | hr.version is the versioned employee/contract record model | N-U51-008 |
| VDR-U51-C037 | hr_version.unique_index | hr/models/hr_version.py:202 | _check_unique_date_version = models.UniqueIndex | FACT | — | — | UniqueIndex prevents two active versions sharing the same date per employee | N-U51-008 |
| VDR-U51-C038 | hr_version.dates_compute | hr/models/hr_version.py:564 | `version.date_start = max(version.date_version, version.contract_date_start)` | FACT | — | — | date_start is max(date_version, contract_date_start); date_end bounded by next version | N-U51-008 |
| VDR-U51-C039 | hr_version.template_whitelist | hr/models/hr_version.py:446 | `return ['job_id', 'department_id', 'contract_type_id', 'structure_type_id', 'wage', 'resource_calendar_id', 'hr_responsible_id']` | FACT | — | — | Contract template copies exactly these 7 fields to the new version | N-U51-008 |
| VDR-U51-C040 | hr_version.unlink_guard | hr/models/hr_version.py:295 | def _unlink_except_last_version(self) | FACT | — | — | ValidationError prevents deleting the last active version of an employee | N-U51-008 |
| VDR-U51-C041 | hr_work_location.model | hr/models/hr_work_location.py:7 | `_name = 'hr.work.location'` | FACT | — | — | hr.work.location defines location type (home/office/other) and address | N-U51-008 |
| VDR-U51-C042 | hr_discuss.dept_subscribe | hr/models/discuss_channel.py:11 | subscription_department_ids = fields.Many2many | FACT | — | — | discuss.channel gains department auto-subscription | N-U51-008 |
| VDR-U51-C043 | hr_activity_plan.dept | hr/models/mail_activity_plan.py:11 | department_id = fields.Many2one | FACT | — | — | Activity plan gains department_id scoped to hr.employee plans | N-U51-008 |
| VDR-U51-C044 | hr_activity_template.responsible | hr/models/mail_activity_plan_template.py:11 | responsible_type | FACT | — | — | Activity plan template gains HR-specific responsible types | N-U51-008 |
| VDR-U51-C045 | hr_holidays_hw.presence | hr_holidays_homeworking/models/hr_employee.py:7 | def _compute_presence_icon(self) | FACT | — | — | Absent employees get presence_holiday_absent/present icon overriding work location | N-U51-009 |
| VDR-U51-C046 | hr_homeworking.days | hr_homeworking/models/hr_homeworking.py:5 | DAYS = ['monday_location_id | FACT | — | — | DAYS constant lists 7 day-of-week location field names | N-U51-010 |
| VDR-U51-C047 | hr_homeworking.location_model | hr_homeworking/models/hr_homeworking.py:8 | `_name = 'hr.employee.location'` | FACT | — | — | hr.employee.location records one-off exceptional day locations per employee | N-U51-010 |
| VDR-U51-C048 | hr_homeworking.unique | hr_homeworking/models/hr_homeworking.py:20 | _uniq_exceptional_per_day = models.Constraint | FACT | — | — | Only one exceptional location record per employee per date | N-U51-010 |
| VDR-U51-C049 | hr_homeworking.employee_fields | hr_homeworking/models/hr_employee.py:11 | `monday_location_id = fields.Many2one('hr.work.location', string='Monday')` | FACT | — | — | hr.employee gains per-day default location fields Monday–Sunday | N-U51-010 |
| VDR-U51-C050 | hr_homeworking.dynamic_view | hr_homeworking/models/hr_employee.py:34 | `def get_views(self, views, options=None):` | FACT | — | — | get_views replaces today_location_name placeholder with current weekday field at runtime | N-U51-010 |
| VDR-U51-C051 | hr_homeworking.presence_icon | hr_homeworking/models/hr_employee.py:62 | `employee.hr_icon_display = f'presence_{today_employee_location_id.location_type}'` | FACT | — | — | Presence icon prefix matches location_type (home/office/other) | N-U51-010 |
| VDR-U51-C052 | hr_homeworking.im_status | hr_homeworking/models/res_users.py:36 | `user.im_status = location_type + "_" + im_status` | FACT | — | RT | im_status string gets location_type prefix; frontend rendering is RT | N-U51-010 |
| VDR-U51-C053 | hr_homeworking.unlink_guard | hr_homeworking/models/hr_work_location.py:12 | `def _unlink_except_used_by_employee(self):` | FACT | — | — | Deleting a work location used in any employee day field or exception raises UserError | N-U51-010 |
| VDR-U51-C054 | hr_homeworking.self_fields | hr_homeworking/models/res_users.py:22 | `return super().SELF_READABLE_FIELDS + DAYS` | FACT | — | — | Users can read and write their own day-location fields via SELF_READABLE/WRITEABLE_FIELDS | N-U51-010 |
| VDR-U51-C055 | hr_hw_calendar.get_worklocation | hr_homeworking_calendar/models/hr_employee.py:14 | `def _get_worklocation(self, start_date, end_date):` | FACT | — | — | Returns dict of employee work locations per weekday plus exceptions within period | N-U51-011 |
| VDR-U51-C056 | hr_hw_calendar.partner | hr_homeworking_calendar/models/res_partner.py:9 | `def get_worklocation(self, start_date, end_date):` | FACT | — | — | res.partner.get_worklocation delegates to employee linked via work_contact_id | N-U51-011 |
| VDR-U51-C057 | hr_hw_calendar.wizard | hr_homeworking_calendar/wizard/homework_location_wizard.py:9 | `_name = 'homework.location.wizard'` | FACT | — | — | Wizard supports setting a location as weekly default or one-off exception | N-U51-011 |
| VDR-U51-C058 | hr_hw_calendar.wizard_weekly | hr_homeworking_calendar/wizard/homework_location_wizard.py:42 | employee_id.sudo().user_id.write | FACT | — | — | When weekly=True, writes day-of-week field on user and deletes any exception for that date | N-U51-011 |
| VDR-U51-C059 | hr_hourly_cost.field | hr_hourly_cost/models/hr_employee.py:9 | hourly_cost = fields.Monetary | FACT | — | — | hr.employee gains hourly_cost Monetary with tracking | N-U51-012 |
| VDR-U51-C060 | hr_maintenance.assign_to | hr_maintenance/models/equipment.py:12 | store=True, readonly | FACT | — | — | Equipment assignment target is department, employee, or other | N-U51-013 |
| VDR-U51-C061 | hr_maintenance.owner | hr_maintenance/models/equipment.py:18 | `owner_user_id = fields.Many2one(compute='_compute_owner', store=True)` | FACT | — | — | Equipment owner_user_id is employee's user (employee mode) or department manager's user | N-U51-013 |
| VDR-U51-C062 | hr_maintenance.subscribe | hr_maintenance/models/equipment.py:51 | if equipment.employee_id | FACT | — | — | Employee/manager partner is auto-subscribed to equipment chatter on create/assign | N-U51-013 |
| VDR-U51-C063 | hr_maintenance.request_employee | hr_maintenance/models/equipment.py:87 | `employee_id = fields.Many2one('hr.employee', string='Employee', default=_default_employee_get)` | FACT | — | — | maintenance.request defaults employee_id to current user's employee | N-U51-013 |
| VDR-U51-C064 | hr_maintenance.hr_employee_ext | hr_maintenance/models/hr_employee.py:7 | `equipment_ids = fields.One2many('maintenance.equipment', 'employee_id', groups="hr.group_hr_user")` | FACT | — | — | hr.employee gains equipment_ids One2many and equipment_count | N-U51-013 |
| VDR-U51-C065 | hr_maintenance.departure | hr_maintenance/wizard/hr_departure_wizard.py:9 | `unassign_equipment = fields.Boolean("Free Equiments", default=True` | FACT | — | — | Departure wizard offers unassign_equipment option defaulting to True | N-U51-013 |
| VDR-U51-C066 | hr_recruitment_sms.action | hr_recruitment_sms/models/hr_applicant.py:9 | `def action_send_sms(self):` | FACT | — | — | hr.applicant.action_send_sms opens SMS composer in mass mode | N-U51-014 |
| VDR-U51-C067 | hr_skills_event.resume_onsite | hr_skills_event/models/hr_resume_line.py:9 | event_id = fields.Many2one | FACT | — | — | hr.resume.line gains event_id for onsite course type | N-U51-015 |
| VDR-U51-C068 | hr_skills_event.course_type | hr_skills_event/models/hr_resume_line.py:15 | course_type = fields.Selection | FACT | — | — | hr.resume.line.course_type gains 'onsite' selection value | N-U51-015 |
| VDR-U51-C069 | hr_skills_event.color | hr_skills_event/models/hr_resume_line.py:35 | `resume_line.color = '#714a66'` | FACT | — | — | Onsite course resume lines use color #714a66 | N-U51-015 |
| VDR-U51-C070 | hr_skills_event.auto_register | hr_skills_event/models/event_event.py:16 | `if self.env.context.get('hr_skills_event_add_employee'):` | FACT | — | — | Context key hr_skills_event_add_employee triggers auto-registration of employee as attendee | N-U51-015 |
| VDR-U51-C071 | hr_skills_slides.resume_elearning | hr_skills_slides/models/hr_resume_line.py:10 | channel_id = fields.Many2one | FACT | — | — | hr.resume.line gains channel_id for eLearning course type | N-U51-016 |
| VDR-U51-C072 | hr_skills_slides.duration | hr_skills_slides/models/hr_resume_line.py:15 | `duration = fields.Integer(string="Duration", compute='_compute_duration', readonly=False, store=True)` | FACT | — | — | Resume line duration auto-computed from channel.total_time | N-U51-016 |
| VDR-U51-C073 | hr_skills_slides.auto_resume | hr_skills_slides/models/slide_channel.py:12 | `def _post_completion_update_hook(self, completed=True):` | FACT | — | — | On course completion, a hr.resume.line of type training/elearning is auto-created for the employee | N-U51-016 |
| VDR-U51-C074 | hr_skills_slides.color | hr_skills_slides/models/hr_resume_line.py:41 | `resume_line.color = '#00a5b7'` | FACT | — | — | eLearning course resume lines use color #00a5b7 | N-U51-016 |
| VDR-U51-C075 | hr_skills_slides.chatter | hr_skills_slides/models/slide_channel.py:75 | `channel._message_employee_chatter(` | FACT | — | — | Enrolling/leaving a course posts a chatter message on the employee record | N-U51-016 |
| VDR-U51-C076 | hr_skills_slides.employee_courses | hr_skills_slides/models/hr_employee.py:10 | `subscribed_courses = fields.Many2many('slide.channel', related='user_partner_id.slide_channel_ids')` | FACT | — | — | hr.employee.subscribed_courses is a related Many2many of slide channels | N-U51-016 |
| VDR-U51-C077 | hr_skills_survey.expiration | hr_skills_survey/models/hr_resume_line.py:13 | expiration_status = fields.Selection | FACT | — | — | hr.resume.line.expiration_status computes based on date_end with 3-month warning window | N-U51-017 |
| VDR-U51-C078 | hr_skills_survey.validity | hr_skills_survey/models/survey_survey.py:9 | certification_validity_months = fields.Integer | FACT | — | — | survey.survey gains certification_validity_months; 0 means never expires | N-U51-017 |
| VDR-U51-C079 | hr_skills_survey.mark_done | hr_skills_survey/models/survey_user.py:13 | `def _mark_done(self):` | FACT | — | — | On successful certification, hr.resume.line created/updated with date_end = date_start + validity_months | N-U51-017 |
| VDR-U51-C080 | hr_skills_survey.survey_id | hr_skills_survey/models/hr_resume_line.py:12 | `survey_id = fields.Many2one('survey.survey', string='Certification', readonly=True)` | FACT | — | — | hr.resume.line.survey_id links the line to its source certification survey | N-U51-017 |
| VDR-U51-C081 | hr_ts_att.report_model | hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:8 | `_name = 'hr.timesheet.attendance.report'` | FACT | — | — | hr.timesheet.attendance.report is a read-only SQL view model | N-U51-018 |
| VDR-U51-C082 | hr_ts_att.sql_union | hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:43 | CAST(hr_attendance.check_in | FACT | — | — | Report UNION ALLs attendance rows with timesheet rows filtered by project_id IS NOT NULL | N-U51-018 |
| VDR-U51-C083 | hr_ts_att.cost_formula | hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:33 | `NULLIF(sum(t.timesheet) * t.emp_cost, 0) as timesheets_cost` | FACT | — | — | Cost fields are hours * hourly_cost from hr_employee | N-U51-018 |
| VDR-U51-C084 | hr_ts_att.menu_gate | hr_timesheet_attendance/models/ir_ui_menu.py:11 | `if not self.env.user.has_group('hr_timesheet.group_hr_timesheet_user')` | FACT | — | — | Attendance-timesheet report menu is hidden for non-timesheet users | N-U51-018 |
| VDR-U51-C085 | html_builder.no_models | html_builder/__manifest__.py:1 | `'name': "HTML Builder"` | FACT | — | — | html_builder contains no Python model files in this revision; all logic is JavaScript/SCSS | N-U51-019 |
| VDR-U51-C086 | iap_crm.reveal_id | iap_crm/models/crm_lead.py:10 | `reveal_id = fields.Char(string='Reveal ID', index='btree_not_null')` | FACT | — | — | crm.lead.reveal_id is indexed with btree_not_null; stores DUNS or clearbit_id | N-U51-020 |
| VDR-U51-C087 | iap_crm.merge | iap_crm/models/crm_lead.py:12 | `return super()._merge_get_fields() + ['reveal_id']` | FACT | — | — | reveal_id is preserved during crm.lead merge operations | N-U51-020 |
| VDR-U51-C088 | iap_mail.mixin | iap_mail/models/iap_account.py:7 | `_inherit = ['iap.account', 'mail.thread']` | FACT | — | — | iap_mail adds mail.thread mixin to iap.account | N-U51-021 |
| VDR-U51-C089 | iap_mail.warning | iap_mail/models/iap_account.py:11 | `warning_threshold = fields.Float("Email Alert Threshold", tracking=True)` | FACT | — | — | iap.account gains warning_threshold and warning_user_ids for alert configuration | N-U51-021 |
| VDR-U51-C090 | iap_mail.bus_notify | iap_mail/models/iap_account.py:31 | `self.env.user._bus_send("iap_notification", params)` | FACT | — | RT | IAP notifications push via bus to current user; frontend consumption is RT | N-U51-021 |
| VDR-U51-C091 | iap_mail.no_credit | iap_mail/models/iap_account.py:34 | `def _send_no_credit_notification(self, service_name, title):` | FACT | — | — | _send_no_credit_notification sends bus message with get_credits_url link | N-U51-021 |
| VDR-U51-C092 | hr_homeworking.exceptional_loc | hr_homeworking/models/hr_employee.py:18 | exceptional_location_id = fields.Many2one | FACT | — | — | exceptional_location_id is today's non-weekly override location | N-U51-010 |
| VDR-U51-C093 | hr_homeworking.work_loc_type | hr_homeworking/models/hr_employee.py:73 | @api.depends(*DAYS, "exceptional_location_id") | FACT | — | — | work_location_type is computed from exceptional or day-of-week location | N-U51-010 |
| VDR-U51-C094 | event_booth.whitelist | event_booth/models/event_type_booth.py:26 | `return ['name', 'booth_category_id']` | FACT | — | — | Only name and booth_category_id are copied from type template to booth | N-U51-003 |
| VDR-U51-C095 | hr_version.flexible | hr/models/hr_version.py:436 | @api.depends('resource_calendar_id.flexi | FACT | — | — | Version is fully flexible when resource_calendar_id is not set | N-U51-008 |
| VDR-U51-C096 | hr_version.normalized_wage | hr/models/hr_version.py:475 | def _get_normalized_wage(self) | FACT | — | — | Without payroll, hourly wage is derived as monthly_wage * 12 / 52 / hours_per_week | N-U51-008 |
| VDR-U51-C097 | hr_homeworking_calendar.exception_struct | hr_homeworking_calendar/models/hr_employee.py:44 | employee_id = exception["employee_id"][0] | FACT | — | — | _get_worklocation exception entries include hr_employee_location_id, location_type, location_name, work_location_id | N-U51-011 |
| VDR-U51-C098 | hr_maintenance.message_new | hr_maintenance/models/equipment.py:116 | `def message_new(self, msg_dict, custom_values=None):` | FACT | — | — | maintenance.request.message_new auto-assigns employee from incoming email sender if user/employee match | N-U51-013 |
| VDR-U51-C099 | event_crm_sale.so_search | event_crm_sale/models/event_registration.py:22 | if so_registrations | FACT | — | — | _get_lead_grouping pre-fetches all registrations for those sale orders to populate cache | N-U51-004 |
| VDR-U51-C100 | hr_version.check_dates | hr/models/hr_version.py:239 | `@api.constrains('employee_id', 'contract_date_start', 'contract_date_end')` | FACT | — | — | _check_dates constraint validates no overlapping active contracts per employee | N-U51-008 |
| VDR-U51-C101 | iap_crm.lead_helpers_vals | crm_iap_mine/models/crm_iap_lead_helpers.py:44 | `'reveal_id': company_data.get('duns') or company_data.get('clearbit_id', ''),` | FACT | — | — | lead_vals_from_response prefers DUNS, falls back to clearbit_id for reveal_id | N-U51-001 |
| VDR-U51-C102 | hr_skills_survey.expiring_window | hr_skills_survey/models/hr_resume_line.py:25 | `elif line.date_end + relativedelta(months=-3) <= fields.Date.today():` | FACT | — | — | expiration_status='expiring' triggers when date_end is within 3 months from today | N-U51-017 |
| VDR-U51-C103 | hr_ts_att.timezone | hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:44 | at time zone 'utc | FACT | — | — | Attendance date is cast to employee's resource calendar timezone | N-U51-018 |
| VDR-U51-C104 | hr_discuss.constraint | hr/models/discuss_channel.py:16 | `failing_channels = self.sudo().filtered(lambda channel: channel.channel_type != 'channel' and channel.subscription_department_ids)` | FACT | — | — | Department subscription is only valid on channel_type='channel' discuss channels | N-U51-008 |
| VDR-U51-C105 | hr_version.salary_costs_factor | hr/models/hr_version.py:672 | `return 12.0` | FACT | — | — | _get_salary_costs_factor returns 12 (monthly to annual multiplier) | N-U51-008 |
