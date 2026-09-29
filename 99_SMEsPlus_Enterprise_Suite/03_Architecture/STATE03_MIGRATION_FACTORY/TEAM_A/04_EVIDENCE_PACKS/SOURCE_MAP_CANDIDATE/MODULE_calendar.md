# Source Map (candidate) — `calendar`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `calendar` |
| Display name | Calendar |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `95e0c0f556661e6b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/calendar/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`
- Direct dependents in 300-module list (8): `calendar_sms`, `crm`, `google_calendar`, `hr_calendar`, `hr_holidays`, `hr_homeworking_calendar`, `hr_recruitment`, `microsoft_calendar`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Calendar / Schedule employees' meetings
- Inventory of user-facing artifacts (counts): menu items 8, views 18, window actions 5, server actions 0, reports 0, mail templates 5, scheduled jobs 1, wizards 3, web routes 10
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (9): `calendar.provider.config` (Calendar Provider Configuration Wizard); `calendar.popover.delete.wizard` (Calendar Popover Delete Wizard); `calendar.alarm_manager` (Event Alarm Manager); `calendar.attendee` (Calendar Attendee Information); `calendar.event.type` (Event Meeting Type); `calendar.recurrence` (Event Recurrence Rule); `calendar.event` (Calendar Event); `calendar.filters` (Calendar Filters); `calendar.alarm` (Event Alarm)
- Objects extended from other modules (11): `mail.activity.schedule`, `mail.composer.mixin`, `discuss.channel`, `ir.http`, `mail.activity.type`, `res.users.settings`, `mail.activity`, `mail.thread`, `res.users`, `mail.activity.mixin`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `calendar.alarm_manager` ← Community: `calendar_sms`, `google_calendar`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.attendee` ← Community: `google_calendar`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.recurrence` ← Community: `google_calendar`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.event` ← Community: `calendar_sms`, `crm`, `google_calendar`, `hr_calendar`, `hr_holidays`, `hr_recruitment`, `microsoft_calendar`; open-license custom/third-party scanned: —
- `calendar.alarm` ← Community: `calendar_sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.activity.schedule`, `mail.composer.mixin`, `discuss.channel`, `ir.http`, `mail.activity.type`, `res.users.settings`, `mail.activity`, `mail.thread`, `res.users`, `mail.activity.mixin`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Calendar: Event Reminder every 1 days
- Security: groups declared 0 (—); record rules 4 (of which company-scoped by text 0); access rows 15

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 59 of 59 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — calendar
Source revision: 19.0.post20260921 | Module: "Calendar" v1.1, category Productivity/Calendar, application, LGPL-3 (calendar/__manifest__.py:4-5,20,43,62). Basis: static reading of models, security, cron, controllers, wizards, seed data; test names read (TEST).

## A. Capabilities and optionality
- A1. Shared meeting calendar: events with attendees, invitations by email with an attached calendar file, accept/decline links, reminders (in-app pop-up and email), recurring events, all-day events, video-call links, privacy levels, and a "today's meetings" entry in the activity tray. calendar/__manifest__.py:10-18; calendar/models/calendar_event.py:131-262,1126-1160; calendar/models/res_users.py:157-178
- A2. Optionality: standalone application, no auto_install; depends on base and mail. Optional external synchronization is a separate switch in Calendar Settings (Google, Outlook) that installs the provider module. calendar/__manifest__.py:7; calendar/views/res_config_settings_views.xml:9-21; base_setup/models/res_config_settings.py:15-17
- A3. A wizard lets a system administrator install a provider module and store its client ID/secret and a "sync paused" flag without visiting general settings. calendar/wizard/calendar_provider_config.py:37-58
- A4. Seed data: five in-app reminders (15 min, 30 min, 1 h, 2 h, 1 day), two email reminders (3 h, 6 h), five email templates (invitation, date change, reminder, update, deletion), an "Invitation" message type, the Meeting activity type marked as category "meeting", and default privacy parameter "public". calendar/data/calendar_data.xml:4-52; calendar/data/mail_template_data.xml:4,119,243,348,443; calendar/data/mail_message_subtype_data.xml:4-10; calendar/data/mail_activity_type_data.xml:4-6

## B. Objects, relationships, lifecycle
- B1. Event: subject, organizer (default current user), start/stop or all-day dates, duration, location, video-call address, attendees (partners), reminders, tags, optional link to any business document (model + id), privacy, "show as" busy/available, notes. calendar/models/calendar_event.py:131-215
- B2. Attendee: one row per (event, partner) with response state Needs Action / Yes / No / Maybe and a private token; the organizer's own row starts accepted. calendar/models/calendar_attendee.py:34-46,59-63
- B3. Recurrence: rule (daily/weekly/monthly/yearly, interval, weekdays, count/end date/forever) that generates individual events; capped at 720 occurrences; edits can apply to this event, this and following, or all (all-events edit not allowed when dates or times change). calendar/models/calendar_recurrence.py:17,84-121,605-622; calendar/models/calendar_event.py:221-226,768-835
- B4. Event lifecycle: create -> attendee rows created, invitation emails sent for future events, reminder triggers scheduled; edit of time -> date-change email to existing attendees (future events only) and organizer status reset when someone else moves it; delete -> optional cancellation email via a wizard, or plain delete when a sync is active; archive hides. calendar/models/calendar_event.py:714,839-864,967-1006
- B5. Link with activities: creating an event from a document/activity creates a "meeting" activity on that document (unless model excluded); name, description, start and organizer stay synchronized both ways; feedback on completing the activity is appended to event notes. calendar/models/calendar_event.py:607-656,1215-1243; calendar/models/mail_activity.py:13-35,56-64
- B6. Video call: a Discuss-based link is generated with a per-event token; the chat channel is created on first join and attendees are added as members. calendar/models/calendar_event.py:563-577,787-794,1057-1078; calendar/controllers/main.py:104-114
- B7. Calendar filters per user (which attendees' calendars are shown) and event tags (unique name). calendar/models/calendar_filter.py:10-18; calendar/models/calendar_event_type.py:16-22

## C. Validations, automation, security, communication
- C1. End cannot be earlier than start (timed and all-day). calendar/models/calendar_event.py:451-473
- C2. Recurrence fields can be saved only with "this and following" or "all events" choice; monthly "by day" needs day 1-31 or weekday+position. calendar/models/calendar_event.py:775-776; calendar/models/calendar_recurrence.py:124-133
- C3. Reminder job (daily, run as root, also triggered at computed times): sends email reminders for alarms falling since last run to attendees who have not declined and only for events not yet ended; new reminders created after their time are skipped by design. calendar/data/calendar_cron.xml:4-14; calendar/models/calendar_alarm_manager.py:143-204
- C4. In-app reminders are pushed to internal users on the bus and polled by clients every few minutes; acknowledgement stored on the partner. calendar/models/calendar_alarm_manager.py:206-255; calendar/controllers/main.py:95-102
- C5. Groups/rights: internal users create/edit/delete events, attendees, alarms, filters, recurrences; portal users read only their own events (rule) and cannot access attendee rows directly; event types read-only for employees, editable by system administrators. calendar/security/ir.model.access.csv:2-16; calendar/security/calendar_security.xml:5-24
- C6. Privacy: an event is public, private, or internal-only, with a per-user default (public unless changed; system default parameter seeded as public). Non-participants see private events as "Busy" with details blanked; only organizer or attendees may edit; uninvited administrators cannot read or edit private events but can edit non-private ones; users cannot change another user's default privacy. calendar/models/calendar_event.py:146-155,312-322,876-915,742-766; calendar/models/res_users.py:49-71; calendar/security/calendar_security.xml:26-34. (TEST) calendar/tests/test_access_rights.py:42-345
- C7. Invitation links: accept/decline/view use the attendee token; a logged-in user whose partner differs from the attendee is refused ("cannot be forwarded"). Unauthenticated internal users are redirected to the form; outsiders see a simple page. calendar/models/ir_http.py:13-29; calendar/controllers/main.py:12-83
- C8. Mail suppression: system parameter calendar.block_mail or context flag stops all attendee emails; sender defaults to organizer; emails skip the acting user unless forced; large batches (over mail_force_send_limit, default 100) are queued not sent at once. calendar/models/calendar_attendee.py:97,133-146,207-209,211-219
- C9. Company scoping: no company field or multi-company rule on events; visibility is by attendee/organizer/privacy only. UNKNOWN — EVIDENCE INSUFFICIENT for tenant isolation across companies.
- C10. Attendee unavailability is computed from other "busy" events sharing partners and overlapping times. calendar/models/calendar_event.py:519-541; calendar/models/res_partner.py:112-128
- C11. Attendees cannot be duplicated; changing attendee state requires write access to the event. calendar/models/calendar_attendee.py:70-83

## D. Handoffs
- D1. Meeting scheduling from CRM, recruitment, HR time-off/work location, SMS reminders: crm, hr_recruitment, hr_holidays, hr_calendar, hr_homeworking_calendar, calendar_sms (dependents). crm/__manifest__.py, hr_recruitment/__manifest__.py, hr_holidays/__manifest__.py, hr_calendar/__manifest__.py, hr_homeworking_calendar/__manifest__.py, calendar_sms/__manifest__.py (each lists calendar in dependencies). Appointment app (Enterprise) is referenced only in comments: calendar/models/calendar_event.py:476-478; calendar/models/calendar_attendee.py:213-215.
- D2. External synchronization: google_calendar, microsoft_calendar. calendar/models/res_users.py:180-193
- D3. Messaging, activities, templates, discuss channels: mail. Partners/users: base.
- D4. Meetings per contact shown on partner: base partner via calendar. calendar/models/res_partner.py:13-23

## E. Configuration that changes outcomes
- E1. User calendar default privacy; system parameter calendar.default_privacy (initial default for new users). calendar/models/res_users.py:49-61; calendar/data/calendar_data.xml:49-52
- E2. Reminder set per event (in-app vs email; email template per reminder). calendar/models/calendar_alarm.py:14-49
- E3. Default event duration from stored defaults (fallback 1 hour). calendar/models/calendar_event.py:1785-1791
- E4. calendar.block_mail; mail.mail_force_send_limit. calendar/models/calendar_attendee.py:133,141
- E5. Provider credentials/paused flags for Google and Outlook sync (E of provider modules). calendar/wizard/calendar_provider_config.py:18-35

## F. Extension path
- google_calendar, microsoft_calendar (sync); crm, hr_recruitment, hr_holidays, hr_calendar, hr_homeworking_calendar, calendar_sms (dependents); test_discuss_full (tests).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end calendar view behaviour and pop-up scheduling (static JS not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: content of the five email templates (only ids read).
- UNKNOWN — EVIDENCE INSUFFICIENT: how dependents (crm, hr_*) use the calendar beyond their manifests.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether iCal generation works without the optional vobject library (module logs a warning and disables it: calendar/models/calendar_event.py:35-39).

