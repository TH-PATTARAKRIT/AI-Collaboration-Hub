# U181 — Event Management, Registration, Ticketing, Communication Chain
**Unit:** U181 | **Group:** G14 | **Priority:** P2 | **Status:** NOT_STUDIED → COMPLETE
**Source Base:** `odoo-19.0.post20260921/odoo/addons/event/`
**Research Date:** 2026-10-02

---

## VDR CLAIMS TABLE (9-Column)

| # | Claim | Model | Field / Method | File : Lines | Verified | Gate | Notes | Neutral Ref |
|---|-------|-------|----------------|-------------|----------|------|-------|-------------|
| C1 | `event.event` core date and stage fields exist | `event.event` | `date_begin`, `date_end`, `stage_id`, `organizer_id` | `event_event.py:107-164` | CONFIRMED | G-OK | `date_begin`/`date_end` required Datetime; `stage_id` Many2one event.stage copy=False default=first; `organizer_id` check_company=True default=company.partner_id | An event record holds two required date-time boundaries, a pipeline stage, and a responsible partner scoped to the active company |
| C2 | `event.registration` state machine has 4 states | `event.registration` | `state` Selection | `event_registration.py:69-79` | CONFIRMED | G-OK | States: draft (Unconfirmed), open (Registered), done (Attended), cancel (Cancelled). Default=open. Action methods: action_set_draft, action_confirm, action_set_done, action_cancel | A registration moves through four lifecycle states from pending through attended or cancelled |
| C3 | `event.registration` is linked to a partner | `event.registration` | `partner_id` | `event_registration.py:49` | CONFIRMED | G-OK | Many2one res.partner, tracking=1, index='btree_not_null', optional (not required) | Each registration optionally references a contact record for the attendee |
| C4 | `event.event.ticket` provides named registration types with seat limits | `event.event.ticket` | `name`, `seats_max`, `seats_limited`, `start_sale_datetime`, `end_sale_datetime`, `sale_available` | `event_ticket.py:8-196` | CONFIRMED | G-OK | Inherits `event.type.ticket`. No price in base module (price added by `event_sale` addon). `sale_available` = is_launched AND NOT is_expired AND NOT is_sold_out | A ticket record defines a category of registration with optional seat cap and sale window |
| C5 | Registration confirmation email uses `event.mail` with after_sub trigger, NOT `mail_template_id` on stage | `event.mail` | `interval_type='after_sub'`, `template_ref` | `event_mail.py:41-50`, `event_registration.py:345-382` | CONFIRMED | G-OK | `event.stage` has NO `mail_template_id` in Odoo 19 Community. Communication configured on `event.mail` (One2many on event) with `template_ref` Reference field and `interval_type='after_sub'`. `_update_mail_schedulers()` on registration create/confirm triggers schedulers | Communication templates are attached to event-level mail schedulers, not to pipeline stages |
| C6 | `event.stage` has sequence, fold, and pipe_end — no mail_template_id | `event.stage` | `sequence`, `fold`, `pipe_end` | `event_stage.py:7-19` | CONFIRMED | G-OK | `fold` = Folded in Kanban (not `pipe_funnel`). `pipe_end` = End Stage, auto-moves finished events here. NO `mail_template_id` on stage in Odoo 19 Community | A pipeline stage carries a display order, a kanban fold flag, and an end-of-life marker |
| C7 | Capacity management via `seats_max`, `seats_taken` computed, and constraint `_check_seats_availability` | `event.event`, `event.registration` | `seats_max`, `seats_taken`, `_verify_seats_availability()`, `_check_seats_availability` | `event_event.py:111-129,685-761`, `event_registration.py:97-107` | CONFIRMED | G-OK | `seats_taken` = seats_reserved + seats_used (computed in `_compute_seats()`). `_verify_seats_availability()` on event.event raises ValidationError if overflow. `_check_seats_availability` is `@api.constrains` on event.registration | Seat usage is derived from active open/done registrations; overflow raises a validation error at write time |
| C8 | `event.tag` and `event.tag.category` provide hierarchical event classification | `event.tag`, `event.tag.category` | `name`, `category_id`, `color`, `sequence` | `event_tag.py:9-42` | CONFIRMED | G-OK | `event.tag` has name, sequence, category_id (required Many2one, cascade), color (integer 1-11). `event.tag.category` has name, sequence, tag_ids | Tags are grouped under named categories and carry a colour index for visual classification |
| C9 | `event.event._close_registration()` does NOT exist; done state triggered by `action_set_done()` | `event.registration`, `event.event` | `action_set_done()`, `_gc_mark_events_done()` | `event_registration.py:314-316`, `event_event.py:878-886` | NOT_FOUND (renamed/absent) | G-DEVIATE | No `_close_registration()` method anywhere in event module. Registration `done` set via `action_set_done()` (writes state='done'). Barcode kiosk `register_attendee()` calls it. `_gc_mark_events_done` @autovacuum on event.event moves ended events to pipe_end stage. | Registration attendance is confirmed by an explicit state transition method; a background vacuum moves finished events into the pipeline end stage |
| C10 | `event.event` is company-scoped via non-required `company_id` field | `event.event` | `company_id` | `event_event.py:81-84` | CONFIRMED | G-OK | Many2one res.company, `required=False`, default=env.company. organizer_id has `check_company=True`. Registration inherits company_id via `related='event_id.company_id'` | Events belong to a company by default but the constraint is optional, allowing cross-company scenarios |
| C11 | `website_published` is NOT in base `event` module — belongs to `website_event` addon | `event.event` (base) | `website_published` absent | `event_event.py` (entire file), `website_event/models/event_event.py:52` | G-DEVIATE | G-DEVIATE | Base `event` module has no `website_published` field. Added by `website_event` addon which inherits event.event and mixes in `website.published.mixin`. Base module depends only on barcodes, base_setup, mail, phone_validation, portal, utm | Website publication status is an optional capability added by a separate website integration module |

---

## ARCHITECTURE SUMMARY

### Module Dependencies
- **Core `event` module** depends on: `barcodes`, `base_setup`, `mail`, `phone_validation`, `portal`, `utm`
- No dependency on `website`, `sale`, or `account` in base

### Model Inventory
| Model | Description |
|-------|-------------|
| `event.event` | Master event record; date range, stage, organizer, seats, tickets, mailing |
| `event.stage` | Kanban pipeline stage; sequence, fold, pipe_end |
| `event.registration` | Attendee registration; state machine, partner link, barcode |
| `event.event.ticket` | Named ticket type per event; seat cap, sale window |
| `event.type` | Event template/category |
| `event.type.ticket` | Ticket template (parent of event.event.ticket) |
| `event.mail` | Automated mailing scheduler; interval_type, template_ref |
| `event.mail.registration` | Per-registration tracking of scheduled mails |
| `event.mail.slot` | Slot-specific mail tracking for multi-slot events |
| `event.slot` | Time slot within a multi-slot event |
| `event.tag` | Classification tag |
| `event.tag.category` | Tag grouping |
| `event.question` | Custom attendee question |
| `event.registration.answer` | Attendee's answer to a question |

### Communication Chain (L3)
1. Event created → `event_mail_ids` One2many populated from event type or defaults
2. `event.mail` records carry `interval_type` and `template_ref`
3. On registration create/confirm: `_update_mail_schedulers()` searches `interval_type='after_sub'` schedulers and calls `execute()` immediately (or triggers cron if async)
4. `_execute_attendee_based()` generates `event.mail.registration` records and sends via `mail.compose.message` in mass_mail mode
5. Event-based communications (before/after event) run via `event_mail_scheduler` cron, calling `schedule_communications()` → `execute()` → `_execute_event_based()`
6. Author resolved from: organizer_id email → company email → user email → base user

### Capacity Management Chain
- `seats_max` (Integer) on event.event and event.event.ticket
- `_compute_seats()` raw SQL: groups event_registration by event_id+state WHERE state IN ('open','done') AND active=true
- `seats_taken = seats_reserved + seats_used`
- `seats_available = seats_max - seats_taken` (0 if seats_max=0 = unlimited)
- `@api.constrains` `_check_seats_availability` on event.registration fires on create/write of active+open/done records
- `event.event._verify_seats_availability()` raises ValidationError on overflow
- `event_registrations_sold_out` computed Boolean for UI and website display

### Key Design Deviations from Research Scope
| Scope Claim | Actual in Odoo 19 Community |
|-------------|----------------------------|
| `mail_template_id` on `event.stage` | Removed; communication now on `event.mail` model with `template_ref` Reference field |
| `pipe_funnel` on `event.stage` | Field is named `fold` (Folded in Kanban); `pipe_end` is separate End Stage marker |
| `event.event._close_registration()` | Method does not exist; replaced by `action_set_done()` + `_gc_mark_events_done()` autovacuum |
| `seats_availability` computed field | Actual field is `seats_available`; additional: `seats_taken`, `seats_reserved`, `seats_used` |
| `website_published` on event.event (base) | Added only by `website_event` optional addon |
| Ticket `price` | Not in base `event`; added by `event_sale` addon via `event_type_ticket` extension |

---

## SOURCE FILE EVIDENCE INDEX
| File | Purpose | Key Items |
|------|---------|-----------|
| `event/models/event_event.py` | Core event model | date_begin/end, stage_id, organizer_id, company_id, seats_*, _compute_seats, _verify_seats_availability, _gc_mark_events_done |
| `event/models/event_registration.py` | Registration model | state selection, partner_id, _check_seats_availability constraint, action_set_done, _update_mail_schedulers |
| `event/models/event_stage.py` | Stage model | sequence, fold, pipe_end (no mail_template_id) |
| `event/models/event_ticket.py` | Ticket model | event.event.ticket, seats_*, sale_available, is_launched, is_expired, is_sold_out |
| `event/models/event_type_ticket.py` | Ticket template | name, seats_max, seats_limited (no price) |
| `event/models/event_mail.py` | Mail scheduler | interval_type, template_ref, _execute_attendee_based, _send_mail, schedule_communications |
| `event/models/event_tag.py` | Tag and category | event.tag, event.tag.category |
| `event/__manifest__.py` | Dependencies | barcodes, base_setup, mail, phone_validation, portal, utm |
| `website_event/models/event_event.py:52` | Website extension | website_published field (NOT in base) |
