# Source Map (candidate) — `calendar_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `calendar_sms` |
| Display name | Calendar - SMS |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `b1c7f50b9e76a444` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/calendar_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `calendar`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Calendar / Send text messages as event reminders
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `calendar.alarm_manager`, `calendar.event`, `calendar.alarm`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `calendar.alarm_manager`, `calendar.event`, `calendar.alarm`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 36 of 36 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — calendar_sms
Source revision: 19.0.post20260921 | Module: "Calendar - SMS" (calendar_sms/__manifest__.py:5) | LGPL-3 (:17)
Basis: static reading of all models, views, data; tests by title.

## A. Capabilities and optionality
- A1. Adds text-message reminders to calendar events and a manual "send SMS to attendees" action. calendar_sms/__manifest__.py:7; calendar_sms/models/calendar_alarm_manager.py:11-24; calendar_sms/models/calendar_event.py:28-43
- A2. Bridge module: auto_install, depends on calendar and sms, so it appears automatically when both are installed. calendar_sms/__manifest__.py:10,15
- A3. Conditional: reminders are sent only for alarms whose type is "SMS Text Message"; e-mail/notification alarms are handled by calendar unchanged. calendar_sms/models/calendar_alarm.py:10-12; calendar_sms/models/calendar_alarm_manager.py:14-15

## B. Objects and lifecycle
- B1. No new model. Adds an alarm type "SMS" and an SMS-template link to the reminder definition (calendar.alarm); adds reminder-sending and manual-send behaviour to the event. calendar_sms/models/calendar_alarm.py:8-17; calendar_sms/models/calendar_event.py:8-43
- B2. Template choice: an SMS-type alarm without a template gets the shipped default template "Calendar Event: Reminder"; non-SMS alarms have the link cleared. The link is required on the form when type is SMS. calendar_sms/models/calendar_alarm.py:19-25; calendar_sms/views/calendar_views.xml:10; calendar_sms/data/sms_data.xml:4-8
- B3. Lifecycle: the scheduled reminder job (owned by calendar) runs -> after e-mail/notification alarms, this module selects events due for SMS alarms -> sends SMS -> re-arms recurring-event alarms. calendar/data/calendar_cron.xml:5-9; calendar_sms/models/calendar_alarm_manager.py:14-24; calendar/models/calendar_event.py:1249-1265
- B4. Removing the SMS alarm type falls back to the default alarm type. calendar_sms/models/calendar_alarm.py:12

## C. Validations, automation, security, external service
- C1. Recipients: event participants who have a valid sanitized phone number and have not declined; the event's responsible user is excluded unless the alarm has "Notify Responsible" on. calendar_sms/models/calendar_event.py:12-20; (TEST) calendar_sms/tests/test_calendar_sms.py:102-106
- C2. Text used: alarm's SMS template, else a fallback sentence with event name and display time. calendar_sms/models/calendar_event.py:21-26
- C3. Messages are sent immediately, not queued for later. calendar_sms/models/calendar_event.py:25
- C4. Manual send: refused with an error if the event has no attendees; otherwise opens the SMS composer in mass mode on the attendees with logging kept. calendar_sms/models/calendar_event.py:28-43. The event form button is hidden when the user cannot edit the event. calendar_sms/views/calendar_views.xml:34
- C5. Event form phone widget's inline SMS option is disabled in favour of the button. calendar_sms/views/calendar_views.xml:36-38
- C6. Test (TEST): two events with 1-hour and 24-hour alarms send exactly the matching template to the matching partners. calendar_sms/tests/test_calendar_sms.py:108-123
- C7. Security groups, record rules, access files: none added by this module (no security data in manifest). calendar_sms/__manifest__.py:11-14
- C8. External-service implication: delivery uses whatever SMS provider the sending company has configured in sms (Odoo credit service or another provider such as sms_twilio); credit or credentials problems appear as SMS failures, not calendar errors. calendar_sms/models/calendar_event.py:21-26; sms_twilio/models/sms_sms.py:57-72

## D. Handoffs
- D1. Calendar events, alarms, reminder job, attendee states: calendar. calendar/models/calendar_alarm_manager.py:143,182; calendar/models/calendar_alarm.py:14,29
- D2. Sending, templates, composer, provider selection and failure tracking: sms. calendar_sms/models/calendar_event.py:21,34; calendar_sms/data/sms_data.xml:4
- D3. Phone sanitization used to filter recipients: partner phone fields (owner: phone_validation via sms chain). calendar_sms/models/calendar_event.py:17 — owner file not read; UNKNOWN — EVIDENCE INSUFFICIENT for exact owner file.

## E. Configuration that changes outcomes
- E1. Per reminder: type SMS, timing, "Notify Responsible", chosen SMS template. calendar/models/calendar_alarm.py:29; calendar_sms/models/calendar_alarm.py:13-17
- E2. The shipped template text can be edited without code (loaded once; not overwritten on update). calendar_sms/data/sms_data.xml:3

## F. Extension path
- calendar (base object), sms (delivery), calendar_sms (bridge). Further overriders of the reminder job: UNKNOWN — EVIDENCE INSUFFICIENT (not searched).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: what happens to attendees without a phone number (they are skipped silently by the filter; no notification found in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: timezone used in the shipped template beyond the expression referencing the partner's timezone (calendar_sms/data/sms_data.xml:7).
- UNKNOWN — EVIDENCE INSUFFICIENT: the exact selection window for "due" alarms (implemented in calendar, not read in detail).

