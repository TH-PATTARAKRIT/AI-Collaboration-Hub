# Source Map (candidate) — `event`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event` |
| Display name | Events Organization |
| Manifest version | 1.9 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c5f4a2350dad4f4a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `barcodes`, `base_setup`, `mail`, `phone_validation`, `portal`, `utm`
- Direct dependents in 300-module list (5): `event_booth`, `event_crm`, `event_product`, `event_sms`, `hr_skills_event`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `mass_mailing_event`, `mass_mailing_event_sms`, `test_event_full`, `website_event`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / Trainings, Conferences, Meetings, Exhibitions, Registrations
- Inventory of user-facing artifacts (counts): menu items 12, views 49, window actions 15, server actions 0, reports 7, mail templates 3, scheduled jobs 1, wizards 1, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (16): `event.question` (Event Question); `event.mail` (Event Automated Mailing); `event.type` (Event Template); `event.stage` (Event Stage); `event.type.ticket` (Event Template Ticket); `event.slot` (Event Slot); `event.registration` (Event Registration); `event.registration.answer` (Event Registration Answer); `event.event` (Event); `event.type.mail` (Mail Scheduling on Event Category); `event.mail.slot` (Slot Mail Scheduler); `event.question.answer` (Event Question Answer); `event.tag.category` (Event Tag Category); `event.tag` (Event Tag); `event.event.ticket` (Event Ticket); `event.mail.registration` (Registration Mail Scheduler)
- Objects extended from other modules (5): `mail.thread`, `mail.activity.mixin`, `mail.template`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `event.question` ← Community: `pos_event`; open-license custom/third-party scanned: —
- `event.mail` ← Community: `event_sms`; open-license custom/third-party scanned: —
- `event.type` ← Community: `event_booth`, `website_event`, `website_event_booth`, `website_event_exhibitor`, `website_event_track`; open-license custom/third-party scanned: —
- `event.type.ticket` ← Community: `event_product`; open-license custom/third-party scanned: —
- `event.slot` ← Community: `pos_event`, `website_event`; open-license custom/third-party scanned: —
- `event.registration` ← Community: `event_crm`, `event_crm_sale`, `event_product`, `event_sale`, `mass_mailing_event`, `pos_event`, `pos_event_sale`, `website_event`, `website_event_crm`; open-license custom/third-party scanned: —
- `event.registration.answer` ← Community: `pos_event`; open-license custom/third-party scanned: —
- `event.event` ← Community: `event_booth`, `event_crm`, `event_product`, `event_sale`, `hr_skills_event`, `mass_mailing_event`, `mass_mailing_event_sms`, `mass_mailing_event_track`, `mass_mailing_event_track_sms`, `pos_event` … (+5); open-license custom/third-party scanned: —
- `event.type.mail` ← Community: `event_sms`; open-license custom/third-party scanned: —
- `event.question.answer` ← Community: `event_crm`, `pos_event`; open-license custom/third-party scanned: —
- `event.tag.category` ← Community: `website_event`; open-license custom/third-party scanned: —
- `event.tag` ← Community: `website_event`; open-license custom/third-party scanned: —
- `event.event.ticket` ← Community: `event_product`, `event_sale`, `pos_event`, `website_event_sale`; open-license custom/third-party scanned: —
- `event.mail.registration` ← Community: `event_sms`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `mail.activity.mixin`, `mail.template`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `event.registration` → ['draft', 'open', 'done', 'cancel']
- Validation: 10 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Event: Mail Scheduler every 24 hours
- Security: groups declared 4 (`group_event_registration_desk`, `group_event_user`, `group_event_manager`, `base.default_user_group`); record rules 3 (of which company-scoped by text 3); access rows 37

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 95 of 95 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — event
Source revision: 19.0.post20260921 | Module: "Events Organization" (event/__manifest__.py:3) | version 1.9 (:4) | category Marketing/Events (:6) | LGPL-3 (:79)
Basis: static reading of all models, security, cron, settings, controller and stage/question seed data; report and view XML by file name; tests by title. Not an application flag in the manifest (no `application` key), reached through the Events menu.
## A. Capabilities and optionality
- A1. Organise events (trainings, conferences, exhibitions): event records, ticket types, optional time slots, attendee registrations, registration questions, automated communications, attendee badges/tickets and a registration desk with barcode check-in. event/__manifest__.py:7-19; event/models/event_event.py:31-207; event/models/event_registration.py:13-90
- A2. Core in this module: events, templates (event types), stages, tags, tickets (no price), slots, registrations, questions/answers, mail schedulers, iCal file, tickets/badges PDF, kiosk check-in. event/models/event_type.py:5-56; event/models/event_stage.py:7-18; event/models/event_slot.py:15-45; event/controllers/main.py:15,32,84
- A3. Optional add-ons chosen from Events settings (each installs a module): tickets with sales (event_sale), tickets with PoS (pos_event), online ticketing (website_event_sale), tracks/agenda (website_event_track and live/quiz variants), advanced sponsors (website_event_exhibitor), booth management (event_booth). event/models/res_config_settings.py:22-31; event/views/res_config_settings_views.xml:13-45
- A4. Conditional: barcode scanning is on only if the "Use Event Barcode" setting is true. event/models/event_event.py:209-212; event/models/res_config_settings.py:28
- A5. Conditional: Google static map for venue only with both API key and secret configured; secret must be valid base64. event/models/res_partner.py:63-87; event/models/res_config_settings.py:13-21,58-76
- A6. Depends: barcodes, base_setup, mail, phone_validation, portal, utm; no auto_install. event/__manifest__.py:20
- A7. iCal file generation needs the optional Python library vobject (warning logged if missing). event/models/event_event.py:24-28
## B. Objects, relationships, lifecycle
- B1. Event (event.event): responsible user, organizer, venue, company, dates and display time zone, language for communications, stage and kanban status, seat limits, template, tickets, slots, mail schedule, questions, badge format/background, ticket instructions. event/models/event_event.py:73-207
- B2. Template (event.type) pre-fills tickets, mail schedule, tags, questions, seat limit, time zone, notes; re-applied when the template changes on an event. event/models/event_event.py:219-249,452-548; (TEST) event/tests/test_event_internals.py:110-384
- B3. Ticket (event.event.ticket): name, description, seat maximum (0 = unlimited), sale start/end, per-order limit, colour; belongs to one event; no price here (price/product come from event_product). event/models/event_ticket.py:13-50; event/models/event_type_ticket.py:9-36
- B4. Slot (event.slot): a date with start/end hour in the event time zone; converted to UTC datetimes; capacity is the event maximum per slot. event/models/event_slot.py:20-27,70-77,109-137; event/models/event_event.py:132-137
- B5. Registration (event.registration): event, optional slot and ticket, "booked by" partner, attendee name/email/phone/company, barcode, UTM origin, state, answers, properties. event/models/event_registration.py:34-90
- B6. Registration states: Unconfirmed (draft), Registered (open, default), Attended (done), Cancelled (cancel). Seats count only open and done. event/models/event_registration.py:69-79; event/models/event_event.py:258-283
- B7. State moves are explicit actions: set draft / confirm / mark attended / cancel; attended writes a log line and stamps attended date; confirming from draft/cancel re-arms scheduled emails. event/models/event_registration.py:159-166,284-296,308-319
- B8. Event stages: New, Booked, Announced, Ended (end stage, folded); events past their end date are moved automatically to the first end stage by the database clean-up routine. event/data/event_data.xml:5-26; event/models/event_event.py:794-803,879-886
- B9. Kanban status: In Progress / Ready / Blocked / Cancelled, reset to In Progress on stage change unless cancelled. event/models/event_event.py:101-106,557-561
- B10. Communication scheduler (event.mail) per event: trigger (after each registration, before/after start, before/after end), interval, mail template; per-attendee sub-records and per-slot sub-records track what was sent. event/models/event_mail.py:25-69; event/models/event_mail_registration.py:11-20; event/models/event_mail_slot.py
- B11. Questions (event.question) and suggested answers; default questions Name, Email (mandatory) and Phone are seeded; answers recorded per registration. event/models/event_question.py:7-34; event/data/event_question_data.xml:4-23; event/models/event_registration_answer.py:9-26
## C. Validations, constraints, automation
- C1. Event end cannot be before start; online URL must have scheme and host (https added if missing); slots must lie within event dates. event/models/event_event.py:586-628
- C2. Registration barcode unique. event/models/event_registration.py:92-95
- C3. Seat capacity is enforced on any registration that is (or becomes) open or attended: event, per-slot and per-ticket limits; shortage lists items and missing seats. event/models/event_registration.py:97-107; event/models/event_event.py:685-765; (TEST) event/tests/test_event_internals.py:682, event/tests/test_event_slot.py:164,232
- C4. With slots, the event seat maximum applies per slot, and slot is mandatory on registration; slot and ticket must belong to the chosen event. event/models/event_event.py:111-115; event/models/event_registration.py:200-210
- C5. Registration open = not cancelled, sale started, not ended, seats available, and a sellable ticket exists (if tickets are used). Sold out computed from event and ticket/slot availability. event/models/event_event.py:296-334,344-368
- C6. Ticket rules: sale end not before sale start; per-order limit cannot exceed ticket seats, must be between 0 and 30; ticket with registrations cannot be deleted. event/models/event_ticket.py:118-136,190-195; event/models/event_event.py:39
- C7. Slot rules: hours between 0:00 and 23:59, end after start; slot with registrations cannot be deleted. event/models/event_slot.py:47-68,139-144
- C8. Question rules: default question must be reusable; question type frozen once answered; answered questions/answers and default questions cannot be deleted (archive instead). event/models/event_question.py:36-75; event/models/event_question_answer.py:18-21
- C9. Phone numbers are normalised on create and on change using the attendee's, partner's, event's or company's country. event/models/event_registration.py:229-233,262-279
- C10. Attendee name/email/phone/company are filled from the booking partner's contact when empty. event/models/event_registration.py:122-157,212-220
- C11. Scheduler job "Event: Mail Scheduler" runs daily (first run 15 minutes after install) and is also triggered when scheduled dates change; runs as system user. event/data/ir_cron_data.xml:4-13; event/models/event_mail.py:83-85
- C12. Scheduler behaviour: skips archived or cancelled events; event-based mails are one-shot to registrations not in draft/cancel, in batches (default 50, up to 1000 per run, then re-triggers); "before start" mails are not sent once the event has ended; per-attendee mails go out right after registration unless the async parameter is set. event/models/event_mail.py:110-125,127-176,212-287,470-494; event/models/event_registration.py:345-382; (TEST) event/tests/test_event_mail_schedule.py:153,727,785,1023,1099
- C13. Failures: invalid or missing template is skipped with a log; other errors post a note on the event and notify organizer, event responsible and template author at most hourly. event/models/event_mail.py:330-359,403-459
- C14. Scheduled attendee mails ignore mail exclusion (opt-out) list because registering implies subscribing to event mails. event/models/event_mail_registration.py:35-45; (TEST) event/tests/test_event_mail_schedule.py:979
- C15. Deleting a mail template removes the schedulers using it. event/models/mail_template.py:23-28
- C16. Security groups (each implies the previous): Registration Desk (implies internal user), User, Administrator (includes admin users by default). event/security/event_security.xml:10-30
- C17. Access: Registration Desk reads events, tickets, slots, stages, tags, schedulers and can create/edit registrations and answers; User can create/edit events, tickets, slots, schedulers, questions and tags (tags: no delete); Administrator has full rights including templates and stages; no access without a group on registration/ticket/tag rows. event/security/ir.model.access.csv:2-38
- C18. Company scoping: multi-company rules on events, registrations and tickets (company_ids or no company). event/security/event_security.xml:35-48
- C19. Registration Desk users may post messages on events without write rights. event/models/event_event.py:673-679
- C20. Public ticket/badge download: access by signed hash over event and registration ids; wrong hash/missing data gives not found; PDF or responsive HTML. event/controllers/main.py:32-82; event/models/event_event.py:871-877
- C21. Check-in by barcode: unknown code -> invalid; cancelled, unconfirmed, finished event -> refused; different event -> needs manual confirmation; already attended -> flagged; otherwise set attended. event/models/event_registration.py:235-256
- C22. External services: optional Google Maps static image (key, secret in system parameters; map link validity is tested with a 2-second web request); outbound e-mail for communications. event/models/res_partner.py:32-55,63-87
## D. Handoffs (owner module per topic)
- D1. Ticket prices/products, "event" service type, invoicing link: event_product (auto_install; depends event, product, account). event_product/__manifest__.py:5,16; event_product/models/event_type_ticket.py:15-42
- D2. Sale order to registration: sale order line of event service creates registrations (one per unit; paid single-order registrations start Unconfirmed so attendee data can be completed; free ones start Registered); order cancellation cancels registrations; sale status Free/Sold: event_sale (auto_install; depends event_product, sale_management). event_sale/__manifest__.py:21,41; event_sale/models/sale_order_line.py:44-69; event_sale/models/event_registration.py:13-36
- D3. Online ticketing/cart with tickets and slots: website_event_sale. website_event_sale/models/sale_order.py:11-98
- D4. Public website event pages, publication, registration form, visibility: website_event. website_event/models/event_event.py:21-53
- D5. Point of sale tickets and registrations: pos_event (auto_install; depends point_of_sale, event_product). pos_event/__manifest__.py:8,22; pos_event/models/event_registration.py:37
- D6. Leads from attendees: event_crm (auto_install; rules choose per attendee or per order, and trigger at creation, registration or attendance). event_crm/__manifest__.py:10,32; event_crm/models/event_lead_rule.py:77-90
- D7. SMS communications: event_sms (adds SMS as a scheduler notification type). event_sms/models/event_mail.py:5-27
- D8. Mass mailing to attendees: mass_mailing_event (and mass_mailing_event_sms for SMS). mass_mailing_event/__manifest__.py:15
- D9. Booths: event_booth (and event_booth_sale for selling booths). event_booth/__manifest__.py:12
- D10. Employee resume lines from events: hr_skills_event. hr_skills_event/__manifest__.py:15
- D11. Communication engine, templates, composer, chatter: mail. event/models/event_mail.py:361-387
- D12. UTM origin on registrations: utm. event/models/event_registration.py:44-47
## E. Configuration and defaults that change outcomes
- E1. Default mail schedule on a new event without template: confirmation right after registration, reminder 1 hour before start, reminder 3 days before start (both use the reminder template). event/models/event_type.py:10-28
- E2. Default questions come from those flagged default (Name, Email, Phone). event/models/event_type.py:30-31
- E3. Event default dates: next half hour, lasting one day; organizer and venue default to the company partner; display time zone from template, else user, else UTC. event/models/event_event.py:41-50,85-88,169-171,409-415
- E4. Ticket default name "Registration"; seat limit 0 = unlimited; tickets copy from template only name, description, seats, sequence. event/models/event_type_ticket.py:11-13,36
- E5. System parameters: event.event_mail_async (scheduler mode), mail.batch_size, mail.render.cron.limit, event.use_event_barcode, Google Maps key/secret. event/models/event_registration.py:367; event/models/event_mail.py:139-144; event/models/event_event.py:210
- E6. Barcode nomenclature is company-level. event/models/res_config_settings.py:29
## F. Extension path (module names)
- Modules depending on event: event_crm, event_booth, event_sms, event_product, hr_skills_event, mass_mailing_event, mass_mailing_event_sms, website_event, test_event_full. Indirect: event_sale, website_event_sale, pos_event, event_booth_sale, website_event_booth, website_event_track (via event_product/website_event/event_booth).
## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: content and wording of the seeded e-mail templates and badge/ticket layouts (event/data/mail_template_data.xml, event/report/* not read beyond names).
- UNKNOWN — EVIDENCE INSUFFICIENT: kiosk/registration-desk front-end behaviour beyond the server methods (event/static/src not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: refunds, payment, invoicing and tax treatment of tickets (owned by event_sale/event_product; not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether portal/public users can see events without website_event (no portal access rows here).

