# U207 Neutral Knowledge — Calendar: Events, Attendees, Alarms

**Unit**: U207  
**Module**: calendar (Community)  
**Gate**: GREEN  
**Claim count**: 20

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U207-C01 | FIELD-DEF | calendar/models/calendar_event.py:131 | name field declaration | FIELD | Always | STABLE | The meeting subject is a required character field on the event record | Event subject field requirement |
| U207-C02 | FIELD-DEF | calendar/models/calendar_event.py:176–178 | start field declaration | FIELD | Always | STABLE | The start moment is a required, indexed, change-tracked datetime field on every calendar event | Event start field tracking |
| U207-C03 | FIELD-DEF | calendar/models/calendar_event.py:156–162 | show_as field declaration | FIELD | Always | STABLE | The availability indicator selects between free and busy states; the default is busy | Free-busy availability indicator |
| U207-C04 | FIELD-DEF | calendar/models/calendar_event.py:146–150 | privacy field declaration | FIELD | Always | STABLE | The visibility field accepts three values: public, private, and confidential (internal-users only) | Event visibility options |
| U207-C05 | FIELD-DEF | calendar/models/calendar_attendee.py:26–31 | STATE_SELECTION constant | CONST | Always | STABLE | Attendee participation states are: accepted, declined, tentative, and needsAction | Participant response states |
| U207-C06 | METHOD | calendar/models/calendar_attendee.py:229–237 | do_accept method | METHOD | On attendee acceptance | STABLE | Accepting an invitation writes the accepted state and posts a chatter message on the event using the invitation subtype | Acceptance and chatter post |
| U207-C07 | METHOD | calendar/models/calendar_attendee.py:239–247 | do_decline method | METHOD | On attendee decline | STABLE | Declining an invitation writes the declined state and posts a chatter message on the event using the invitation subtype | Decline and chatter post |
| U207-C08 | METHOD | calendar/models/calendar_attendee.py:115–122 | _send_invitation_emails method | METHOD | When event start is in the future | STABLE | Invitation emails are sent only to attendees whose event has not yet started, using the meeting invitation mail template | Future-event invitation filter |
| U207-C09 | METHOD | calendar/models/calendar_attendee.py:124–209 | _notify_attendees method | METHOD | When mail template provided and block_mail config is false | STABLE | Attendee notification renders the template per attendee, attaches an iCalendar file, and sends via the event message notification path | Per-attendee notification with calendar attachment |
| U207-C10 | FIELD-DEF | calendar/models/calendar_alarm.py:14–16 | alarm_type field | FIELD | Always | MIGRATION-FLAG | The alarm type accepts only notification and email values in version 19; there is no SMS alarm type | Alarm type enumeration v19 |
| U207-C11 | METHOD | calendar/models/calendar_alarm.py:31–41 | _compute_duration_minutes method | METHOD | Always | STABLE | Alarm lead time converts duration and interval unit to minutes using multipliers of one for minutes, sixty for hours, and 1440 for days | Alarm duration normalization |
| U207-C12 | FIELD-DEF | calendar/models/calendar_event.py:217–219 | recurrency and recurrence_id fields | FIELD | When event is recurrent | STABLE | A recurrent event carries a boolean flag and a foreign key to a separate recurrence rule record | Recurrence linkage pattern |
| U207-C13 | FIELD-DEF | calendar/models/calendar_recurrence.py:104 | rrule stored field | FIELD | Always | STABLE | The recurrence rule string is stored on the recurrence record and recomputed whenever its constituent parameters change | Stored rule string computation |
| U207-C14 | METHOD | calendar/models/calendar_recurrence.py:584–627 | _get_rrule method | METHOD | On recurrence generation | STABLE | Occurrence generation enforces a hard cap of 720 events and a configurable year horizon (default 15 years) via a system parameter | Recurrence occurrence cap |
| U207-C15 | METHOD | calendar/models/calendar_recurrence.py:399–447 | _rrule_parse method | METHOD | On inverse rrule write | STABLE | Parsing an iCal rule string back to field values strips non-standard X-prefixed parameters before handing the string to the dateutil parser | Rule string parsing with extension stripping |
| U207-C16 | FIELD-DEF | calendar/models/mail_activity.py:13 | calendar_event_id on activity | FIELD | Always | STABLE | The activity model carries a cascading foreign key to a calendar event, enabling bidirectional linkage | Activity-to-event foreign key |
| U207-C17 | METHOD | calendar/models/mail_activity.py:15–35 | write override on activity | METHOD | When deadline changes on an activity with a linked event | STABLE | Changing the activity deadline shifts the linked calendar event start by the same day difference, guarded by a context flag to prevent update loops | Activity-event deadline synchronization |
| U207-C18 | METHOD | calendar/models/calendar_event.py:1215–1231 | _sync_activities method | METHOD | On event name, description, start, or user_id change | STABLE | Changing event name, description, start date, or organizer propagates those values to linked activities, guarded by a context flag to prevent reciprocal loops | Event-to-activity field propagation |
| U207-C19 | METHOD | calendar/models/calendar_event.py:888–894 | _check_private_event_conditions method | METHOD | For non-superuser reads | STABLE | An event is treated as private when its visibility is set to private, or when visibility is unset and the organizer default is private, and the current user is neither organizer nor invited attendee | Private event access condition |
| U207-C20 | MIGRATE | calendar/models/calendar_event.py — field absent | No recurrent_id field in v19 | MIGRATION-FLAG | Always | BREAKING | The field used in older versions to link individual recurrence occurrences to the base event is absent in version 19; the recurrence relationship is maintained solely through the recurrence rule foreign key and the follow-recurrence boolean | Recurrence field removal v19 |
