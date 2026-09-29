# Source Map (candidate) — `microsoft_calendar`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `microsoft_calendar` |
| Display name | Outlook Calendar |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `aca770e40ecca90b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/microsoft_calendar/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `microsoft_account`, `calendar`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity / —
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 1, wizards 2, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `microsoft.calendar.account.reset` (Microsoft Calendar Account Reset); `microsoft.calendar.sync` (Synchronize a record with Microsoft Calendar)
- Objects extended from other modules (7): `calendar.alarm_manager`, `calendar.attendee`, `res.users.settings`, `calendar.event`, `res.users`, `res.config.settings`, `calendar.recurrence`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `calendar.alarm_manager`, `calendar.attendee`, `res.users.settings`, `calendar.event`, `res.users`, `res.config.settings`, `calendar.recurrence`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Outlook: synchronization every 12 hours
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 61 of 61 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — microsoft_calendar
Source revision: 19.0.post20260921 | Module: "Outlook Calendar" v1.0, category Productivity, LGPL-3 (microsoft_calendar/__manifest__.py:4-6,28). Basis: static reading of sync models, service wrapper, reset wizard, cron, controller; test file names noted (TEST).

## A. Capabilities and optionality
- A1. Synchronization of a user's Odoo meetings with their Outlook / Microsoft 365 calendar through Microsoft Graph: create, change, delete, attendee responses, reminders, privacy, busy/free, video link. microsoft_calendar/models/calendar.py:47-51; microsoft_calendar/models/microsoft_sync.py:67-103,129-158; microsoft_calendar/utils/microsoft_calendar.py:101-200
- A2. Optionality: not automatic; installed from Calendar Settings ("Outlook Calendar" switch, then save and configure) or by the provider wizard; depends on microsoft_account and calendar. microsoft_calendar/__manifest__.py:7; calendar/views/res_config_settings_views.xml:11-13; calendar/wizard/calendar_provider_config.py:45-58
- A3. Conditional on credentials: sync requires a company Microsoft client ID and secret (system parameters) and per-user consent; otherwise the calendar reports "need config from admin" or "need authorization". microsoft_calendar/models/res_config_settings.py:9-12; microsoft_calendar/controllers/main.py:23-41; microsoft_calendar/models/res_users.py:161-170
- A4. Scheduled job "Outlook: synchronization" every 12 hours for users with a refresh token who have not stopped sync. microsoft_calendar/data/microsoft_calendar_data.xml:4-14; microsoft_calendar/models/res_users.py:116-127
- A5. Installation creates a random database-wide identifier (microsoft_guid parameter) if absent. microsoft_calendar/__init__.py:8-17

## B. Objects, relationships, lifecycle
- B1. Extends events and recurrences (owner: calendar) with Outlook ids (event id, universal id, series master id) and a separate "needs sync" flag. microsoft_calendar/models/microsoft_sync.py:60-65; microsoft_calendar/models/calendar.py:41
- B2. Token fields (refresh/access/validity) live on the user via microsoft_account and are administrator-only; sync token, "stopped" flag and last sync date live on user settings, administrator-only and excluded from session info. microsoft_account/models/res_users.py:13-14; microsoft_calendar/models/res_users_settings.py:10-22
- B3. Sync status per user: active, paused (system parameter microsoft_calendar_sync_paused), or stopped (user flag). Paused blocks Odoo-to-Outlook pushes. microsoft_calendar/models/res_users.py:71-80,141-145; microsoft_calendar/models/microsoft_sync.py:74,97,117
- B4. Odoo -> Outlook: changes to name, description, dates, organizer, privacy, attendees, reminders, location, busy/free, active, video link flag the event; requests go out after the database commit. microsoft_calendar/models/calendar.py:47-51; microsoft_calendar/models/microsoft_sync.py:23-49,378-432
- B5. Outlook -> Odoo: uses Microsoft's incremental change feed; series masters trigger a second read of occurrences; new items create events/recurrences (max 720 occurrences), cancelled ones are removed, others are updated when Outlook's last-modified time is not older than Odoo's write date ("last modified wins"). microsoft_calendar/utils/microsoft_calendar.py:101-150; microsoft_calendar/models/microsoft_sync.py:21,165-360
- B6. First sync window: 365 days back and 730 days forward by default (parameter microsoft_calendar.sync.range_days); Odoo-to-Outlook side uses a symmetric window and only events created after the first synchronization date, and only records written after the user's last sync (5-minute tolerance), to avoid mass invitations for old events. microsoft_calendar/utils/microsoft_calendar.py:66-72; microsoft_calendar/models/calendar.py:286-309; microsoft_calendar/models/microsoft_sync.py:517-530; microsoft_calendar/models/res_users.py:186-205
- B7. Optional lower bound (microsoft_calendar.sync.lower_bound_range) to stop re-updating old events in Odoo unless the time difference is over 1 hour. microsoft_calendar/models/microsoft_sync.py:326-347,362-376
- B8. Changing an event's organizer recreates the event under the new organizer and deactivates the old one. microsoft_calendar/models/calendar.py:240-249
- B9. Account reset wizard (system administrators): leave, delete in Outlook, in Odoo or both; next sync all or new only; recurring events are not touched in Outlook "to prevent spam"; tokens and sync token are cleared. microsoft_calendar/wizard/reset_account.py:13-55; microsoft_calendar/security/ir.model.access.csv:2

## C. Validations, automation, security, external service
- C1. Recurring events cannot be created, updated, deleted or archived from Odoo while sync is active for a synced series; the user is told to do it in Outlook (Outlook limitation). microsoft_calendar/models/calendar.py:76-82,148-165,167-181,230-238,279-284
- C2. Moving one occurrence past the neighbouring occurrences is refused. microsoft_calendar/models/calendar.py:114-133
- C3. Every attendee must have an email address or sync is blocked with an error listing up to 50 events; sync stays blocked until events are fixed or archived. microsoft_calendar/models/calendar.py:642-661
- C4. A different organizer is allowed only if that organizer has Outlook sync active and is among attendees (or the current user has no sync). microsoft_calendar/models/calendar.py:99-112
- C5. Attendee replies (accept/decline/maybe) are sent to Outlook only by non-organizer attendees; recurring events reject the reply. microsoft_calendar/models/calendar_attendee.py:29-37
- C6. Insertion into Outlook is blocked when the sender is not the event owner. microsoft_calendar/models/calendar.py:708-711; microsoft_calendar/models/microsoft_sync.py:147-148
- C7. Odoo invitation emails are suppressed for events already synced or pending sync (Outlook sends its own); Odoo email reminders skip events that have an Outlook id. microsoft_calendar/models/calendar.py:68-74; microsoft_calendar/models/calendar_alarm_manager.py:10-15
- C8. Token failure (invalid grant/client) clears refresh and sync tokens and tells the user to check credentials. microsoft_calendar/models/res_users.py:51-69
- C9. External service and credentials: Microsoft identity platform (default common tenant, overridable by microsoft_account.auth_endpoint / token_endpoint) and Microsoft Graph (graph.microsoft.com); calendar read-write permission with offline access; client secret is a database-wide system parameter; request timeout 5 seconds by default, overridable by microsoft_calendar.graph_timeout. microsoft_account/models/microsoft_service.py:17-19,43-57; microsoft_calendar/utils/microsoft_calendar.py:205-206; microsoft_calendar/models/microsoft_sync.py:473-483
- C10. Access rows: only the reset wizard (system administrators); other data follows calendar rules. Company scoping: UNKNOWN — EVIDENCE INSUFFICIENT.
- C11. (TEST) Suites for create, update, delete, answer, service and event conversion behaviours: microsoft_calendar/tests/test_create_events.py; microsoft_calendar/tests/test_update_events.py; microsoft_calendar/tests/test_delete_events.py; microsoft_calendar/tests/test_answer_events.py; microsoft_calendar/tests/test_microsoft_service.py; microsoft_calendar/tests/test_microsoft_event.py (file-level pointers only, not read in detail).

## D. Handoffs
- D1. Events, recurrences, attendees, alarms, privacy: calendar. OAuth endpoints, token storage and request layer: microsoft_account. Settings host: base_setup via calendar. microsoft_calendar/__manifest__.py:7
- D2. Parallel provider for Google: google_calendar. Mail-server OAuth for Outlook mail is a different module: microsoft_outlook (separate credentials: microsoft_outlook_client_id vs microsoft_calendar_client_id). microsoft_outlook/models/res_config_settings.py:10; microsoft_calendar/models/res_config_settings.py:9
- D3. Appointment app (Enterprise) referenced in a calendar override comment only: calendar/models/calendar_event.py:475-478.

## E. Configuration that changes outcomes
- E1. microsoft_calendar_client_id / _client_secret; microsoft_calendar_sync_paused; microsoft_calendar.sync.range_days; microsoft_calendar.sync.lower_bound_range; microsoft_calendar.sync.first_synchronization_date (set automatically); microsoft_calendar.graph_timeout. microsoft_calendar/models/res_config_settings.py:9-12; microsoft_calendar/models/calendar.py:288-307; microsoft_calendar/models/res_users.py:186-205
- E2. Per-user "sync stopped" flag; stopping clears the last sync date. microsoft_calendar/models/res_users.py:129-139

## F. Extension path
- calendar (event/recurrence/attendee/alarm manager/users); microsoft_account; hooks for organizer validation are noted as overridable elsewhere. calendar/models/calendar_event.py:475-479

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: conversion of recurrence rules between Outlook and Odoo (models/calendar_recurrence_rule.py and utils/microsoft_event.py only partly read).
- UNKNOWN — EVIDENCE INSUFFICIENT: Microsoft app registration, tenant restrictions, throttling and Graph limits (external).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end sync dialogs (static assets not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: company isolation with several companies sharing one client ID.

