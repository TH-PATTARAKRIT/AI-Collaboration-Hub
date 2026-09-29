# Source Map (candidate) — `google_calendar`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `google_calendar` |
| Display name | Google Calendar |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `1ef0f2d49fd67528` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/google_calendar/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `google_account`, `calendar`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity / —
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 2, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `google.calendar.account.reset` (Google Calendar Account Reset); `google.calendar.sync` (Synchronize a record with Google Calendar)
- Objects extended from other modules (7): `calendar.alarm_manager`, `calendar.attendee`, `res.users.settings`, `calendar.event`, `res.users`, `res.config.settings`, `calendar.recurrence`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `calendar.alarm_manager`, `calendar.attendee`, `res.users.settings`, `calendar.event`, `res.users`, `res.config.settings`, `calendar.recurrence`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Google Calendar: synchronization every 12 hours
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 55 of 55 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — google_calendar
Source revision: 19.0.post20260921 | Module: "Google Calendar" v1.0, category Productivity, LGPL-3 (google_calendar/__manifest__.py:4-6,27). Basis: static reading of manifest, sync models, service wrapper, wizard, cron, controller; test file names noted (TEST).

## A. Capabilities and optionality
- A1. Two-way synchronization of a user's Odoo meetings (and recurring series) with their primary Google Calendar: create, change, cancel, attendee responses, reminders, privacy, busy/free, video-call link. google_calendar/models/calendar.py:46-49,141-199,302-377; google_calendar/models/google_sync.py:132-152,158-211
- A2. Optionality: not automatic; installed from Calendar Settings ("Google Calendar" switch, then save and configure) or by the provider wizard; depends on google_account and calendar. google_calendar/__manifest__.py:7; calendar/views/res_config_settings_views.xml:14-19; calendar/wizard/calendar_provider_config.py:45-58
- A3. Conditional on credentials: sync works only if the company has entered a Google client ID and secret (system parameters) and each user has completed Google consent; otherwise the calendar screen reports "need config from admin" or "need authorization". google_calendar/models/res_config_settings.py:9-12; google_calendar/controllers/main.py:26-44; google_calendar/models/res_users.py:182-204
- A4. Scheduled job "Google Calendar: synchronization" runs every 12 hours for users that have a token and have not stopped sync. google_calendar/data/google_calendar_data.xml:4-19; google_calendar/models/res_users.py:140-157

## B. Objects, relationships, lifecycle
- B1. Extends calendar events and recurrences (owner: calendar) with a Google id, a "needs sync" flag, and a "guests cannot modify" flag; adds Google Meet as a video-call source. google_calendar/models/calendar.py:21-25; google_calendar/models/google_sync.py:61-63
- B2. Per-user connection data (refresh token, access token and validity, next-sync token, last calendar id, "sync stopped" flag) is stored on user settings, readable by system administrators only and excluded from client session info. google_calendar/models/res_users_settings.py:16-35
- B3. Sync status per user: active, paused (system parameter google_calendar_sync_paused), stopped (user flag). Pausing blocks all Odoo-to-Google pushes. google_calendar/models/res_users.py:33-42,175-179; google_calendar/models/google_sync.py:72,92,143
- B4. Odoo -> Google: changes to name, description, dates, attendees, reminders, location, privacy, active, busy/free, video link flag the event; a request is sent after the database commit so only committed changes reach Google. google_calendar/models/calendar.py:46-49; google_calendar/models/google_sync.py:24-50,65-77,262-317
- B5. Google -> Odoo: new Google events create Odoo events; cancelled ones are removed or archived; conflicts use "last updated wins" comparing Google update time with Odoo write date; birthday events are ignored; unknown attendees become contacts by email match. google_calendar/models/google_sync.py:172-211; google_calendar/models/res_users.py:88-92; google_calendar/models/calendar.py:202-246
- B6. First (full) sync is limited to a window of 365 days back and forward (parameter google_calendar.sync.range_days) and to 200 records per pass; later syncs use Google's incremental token, falling back to full sync when Google says the token is invalid. google_calendar/utils/google_calendar.py:37-47,51-53; google_calendar/models/calendar.py:126-138; google_calendar/models/google_sync.py:328-332; google_calendar/models/res_users.py:120-131
- B7. Deleting a synced event in Odoo archives it so the deletion can propagate to Google, then the local record disappears on the next sync. google_calendar/models/google_sync.py:110-125
- B8. Account reset wizard (system administrators): choose to leave, delete in Google, delete in Odoo, or both for the user's own events; and whether the next sync covers all events or only new ones; tokens are cleared. google_calendar/wizard/reset_account.py:14-67; google_calendar/security/ir.model.access.csv:2

## C. Validations, automation, security, external service
- C1. Only the organizer may push changes for events they own; attendees' response changes are synchronized using the organizer's connection; Google refuses non-organizer edits (403), which is logged and posted as a note on the event, and the event is not retried until updated. google_calendar/models/calendar_attendee.py:30-40; google_calendar/models/google_sync.py:213-260
- C2. If the event's Google settings say guests cannot modify, non-organizers are blocked from editing synced fields with a validation error. google_calendar/models/calendar.py:103-117
- C3. Events are inserted into Google only by the organizer's account (blocked when the sender is not the organizer). google_calendar/models/calendar.py:396-399; google_calendar/models/google_sync.py:147-150
- C4. Invitation emails from Odoo are suppressed when the organizer's Google sync is active and valid (Google sends invites instead); email reminders skip events that have a Google id. google_calendar/models/calendar.py:119-124; google_calendar/models/calendar_alarm_manager.py:10-15
- C5. Token failure (invalid grant / invalid client) clears the stored refresh token and tells the user to check credentials. google_calendar/models/res_users_settings.py:52-71
- C6. Concurrency: sync skips a user whose record is locked by another sync. google_calendar/models/res_users.py:113-118
- C7. External service and credentials: Google Calendar API (primary calendar), full read/write calendar permission, offline access with forced consent; client secret held as a system parameter shared by the whole database; user tokens stored in the database. google_calendar/utils/google_calendar.py:32,118-137; google_account/models/google_service.py:22-44
- C8. When credentials are missing, the shortcut to general settings is offered only to ERP managers (other users get the status message only). google_calendar/utils/google_calendar.py:139-140; google_calendar/controllers/main.py:26-36
- C9. Access rows: only the reset wizard (system administrators) is defined here; other data follows calendar rules. Company scoping: UNKNOWN — EVIDENCE INSUFFICIENT.
- C10. (TEST) Extensive suites for Google-to-Odoo, Odoo-to-Google, mail suppression and token access: google_calendar/tests/test_sync_google2odoo.py; google_calendar/tests/test_sync_odoo2google.py; google_calendar/tests/test_sync_odoo2google_mail.py; google_calendar/tests/test_token_access.py (file-level pointers only, not read in detail).

## D. Handoffs
- D1. Events, recurrences, attendees, reminders, privacy: calendar. Google OAuth endpoints and request layer: google_account. Settings host: base_setup via calendar. google_calendar/__manifest__.py:7; google_calendar/controllers/main.py:5-7
- D2. The parallel provider for Outlook: microsoft_calendar (independent; both can coexist per calendar module design). calendar/wizard/calendar_provider_config.py:12-14
- D3. Contact creation from attendee emails: mail thread partner lookup (mail). google_calendar/models/google_sync.py:348-356

## E. Configuration that changes outcomes
- E1. google_calendar_client_id / _client_secret (enable feature), google_calendar_sync_paused (pause all pushes), google_calendar.sync.range_days (full-sync window, default 365). google_calendar/models/res_config_settings.py:9-12; google_calendar/utils/google_calendar.py:42
- E2. Per-user "sync stopped" flag; per-event "guests can modify". google_calendar/models/res_users_settings.py:22; google_calendar/models/calendar.py:23-24

## F. Extension path
- calendar (events/recurrence/attendee/alarm manager/users); google_account; extension hooks such as invitation-blocked and event-user methods are declared for overriding. google_calendar/models/google_sync.py:392-407

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: Google API quotas, verification of the tenant's Google app, and Google-side sharing rules (external).
- UNKNOWN — EVIDENCE INSUFFICIENT: recurrence-rule conversion rules in detail (models/calendar_recurrence_rule.py only partly read).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end sync dialogs (static assets not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour with multiple companies in one database sharing one Google client id.

