# U181 — Event Module: Neutral Knowledge Reference
**Unit:** U181 | **Group:** G14 | **Level:** L3
**Research Date:** 2026-10-02

---

## WHAT THIS MODULE DOES

The `event` module in Odoo 19 Community manages the complete lifecycle of organised gatherings — conferences, trainings, exhibitions, meetups. It handles scheduling, attendee registration, capacity enforcement, ticket type definition, and automated communications.

---

## CORE CONCEPTS (Plain Language)

### Events
An event is a named activity with a start date, an end date, an optional venue, and an assigned responsible person. Events move through a configurable pipeline of stages (the same kanban board pattern used in CRM). Events can be single sessions or can hold multiple named time slots. Each event belongs to a company by default.

### Registrations
When someone signs up for an event they become an attendee through a registration record. A registration passes through four states:

- **Unconfirmed** (draft) — pending, not yet counted against seat limits
- **Registered** (open) — confirmed, counted against capacity
- **Attended** (done) — attendee physically checked in, recorded with a timestamp
- **Cancelled** — removed from active count

The system tracks the registered contact (partner) separately from the attendee name and email, allowing a single contact to book multiple seats.

### Tickets
Ticket types allow an event to offer different registration categories — for example a standard seat versus a VIP seat. Each ticket type has an optional maximum seat count and optional sale start/end windows. When `event_sale` is installed, tickets also carry a price. An attendee's registration is linked to one ticket type.

### Capacity
The system enforces seat limits at two levels: the overall event maximum and the per-ticket maximum. Available seats are computed dynamically from open and attended registrations. When limits are exceeded, a validation error is raised on save.

### Automated Communications
Events carry a list of scheduled communication items. Each item specifies a mail template, a trigger type, and a timing offset. Trigger types include:

- After each registration (immediate or near-immediate on subscribe)
- Before the event starts (X days/hours before)
- After the event starts
- Before the event ends
- After the event ends

When a new registration is confirmed, the system finds all schedulers with the "after each registration" trigger and sends the template to that attendee. Time-based communications are processed by a background cron job.

### Pipeline Stages
Stages define the kanban columns for the event board. A stage can be marked as the end stage, which causes the system to automatically move events there once their end date has passed (checked by a scheduled vacuum job). Stages can also be folded in the kanban view.

### Tags and Categories
Events can be tagged for classification. Tags are grouped under categories. Tags carry a colour index for visual display. Both models support translation.

### Multi-Slot Events
An event can be configured as multi-slot, where each slot has its own start/end time, seat limit, and communication schedule. Registrations for multi-slot events must specify a slot.

---

## INTEGRATION BOUNDARIES

| Extension | What It Adds |
|-----------|-------------|
| `event_sale` | Ticket price, link to sale order, revenue computation |
| `website_event` | Website publication, online registration flow, website_published flag |
| `website_event_sale` | Paid online registration via e-commerce |
| `event_booth` | Exhibitor booth management alongside sessions |
| `event_crm` | CRM lead generation from registrations |

---

## SME MIGRATION IMPLICATIONS

1. **Stage Configuration**: The base module has no mail template on stages. Communication templates live on the event's mail scheduler list. Any legacy system that attached confirmation templates to stages must be remapped to the `event.mail` scheduler model.

2. **Ticket Pricing**: Price is an optional addon concern. If the target deployment needs paid tickets, `event_sale` must be installed and sale order integration configured.

3. **Website Publishing**: `website_published` is not available without the `website_event` module. Online registration requires both `website` and `website_event`.

4. **Capacity Logic**: Seat limits are enforced at save time via a constraint. Overbooking (registrations exceeding the limit before the constraint fires) can occur in concurrent scenarios; the system detects this at write rather than reserving slots in a queue.

5. **Registration Attendance**: The "attended" state is set either manually by staff or automatically via the barcode kiosk registration desk. The kiosk scans a barcode and calls `register_attendee()` which transitions state to done.

6. **Multi-Company**: Events are company-filtered by default. The organiser contact is validated against the company (`check_company=True`). Cross-company event scenarios require explicit configuration or removal of the required company on the event.

7. **Multi-Slot**: The multi-slot feature is a Odoo 19 addition. Legacy single-session events migrate cleanly. Events with recurring sessions may need to be restructured as multi-slot events.
