# Source Map (candidate) — `event_sms`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event_sms` |
| Display name | SMS on Events |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `62a993a90eb5f25e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event_sms/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `event`, `sms`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_event_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `event.mail`, `event.type.mail`, `sms.template`, `event.mail.registration`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `event.mail`, `event.type.mail`, `sms.template`, `event.mail.registration`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 28 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: event_sms (SMS on Events)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/event_sms.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge that lets event communications be sent as text messages (SMS) in addition to emails; depends on event and sms only (event_sms/__manifest__.py:9).
- Conditional: installs automatically when both event and sms are present (event_sms/__manifest__.py:16); not an application in its own right.
- Adds "SMS" as a second channel option on event communication schedulers, both on live events and on event-type templates, and lets the template choice point to an SMS template (event_sms/models/event_mail.py:7-8; event_sms/models/event_type_mail.py:7-8).
- The channel is inferred from the chosen template: picking an SMS template makes the scheduler an SMS scheduler; otherwise it stays an email scheduler (event_sms/models/event_mail.py:10-13; base behaviour event/models/event_mail.py:104-108).
- Ships two seeded SMS templates aimed at event registrations: a registration confirmation and a reminder ("Ready for ... starts at ... See you there") (event_sms/data/sms_data.xml:4-15). Seeded once (noupdate) so later edits by the company are kept (event_sms/data/sms_data.xml:2).
- Static assets: a customised template picker widget in the backend (event_sms/__manifest__.py:17-21).

## B. Business objects, relationships, lifecycle
- Reuses the event communication scheduler (trigger: after each registration, before/after event start, before/after event end; unit and number of hours/days/weeks/months) (event/models/event_mail.py:36-52); this module adds only the channel and template kind.
- For an SMS scheduler, sending targets the registrations of the event and goes through the generic mass-SMS composer with logging kept on each registration record, sending queued rather than forced immediately (event_sms/models/event_mail.py:20-25; sms/models/mail_thread.py:55-77).
- Per-registration executions (after-registration trigger): SMS schedulers mark each registration's communication line as sent; non-SMS lines fall through to the standard email path (event_sms/models/event_mail_registration.py:7-15).
- Event-based (one-shot) executions: the SMS is sent then the standard path continues (event_sms/models/event_mail.py:15-18).
- Lifecycle status/timing (scheduled/running/sent/error/cancelled, done flag, sent counter) is owned by the event module, not this one (event/models/event_mail.py:54-66).
- Timing gate (owned by event): a one-shot before-event-type scheduler is skipped once the event is over; already-done schedulers are skipped (event/models/event_mail.py:117-123).
- (TEST) After-registration SMS is sent automatically to each new registrant's phone and the scheduler counts 3 done for 3 registrations; a before-event reminder fires when executed at its scheduled date and marks the scheduler done (event_sms/tests/test_sms_schedule.py:61-107).

## C. Validations, automation, security, multi-company
- Deleting an SMS template automatically deletes every event / event-type scheduler that referenced it (so no scheduler is left with a missing template) (event_sms/models/sms_template.py:23-28); (TEST) confirmed for the after-registration scheduler (event_sms/tests/test_sms_schedule.py:109-113). Deletion of the schedulers is performed with elevated rights, so a user deleting a template does not need rights on the schedulers.
- Template picker filtering: when the event form asks for it via a context flag, only SMS templates written for event registrations are offered (event_sms/models/sms_template.py:10-21).
- Access: Event Managers get full create/read/update/delete on SMS templates (event_sms/security/ir.model.access.csv:2) but a record rule restricts their write/create/delete to templates whose target is an event or an event registration; read is not restricted by that rule (event_sms/security/sms_security.xml:3-9). Implication: event managers cannot modify SMS templates of other business areas but the rule sets read unrestricted at this level (final read visibility depends on other rules in the sms module: UNKNOWN — EVIDENCE INSUFFICIENT).
- Data sent: the recipient's phone number and event details (name, dates, address) are placed into the SMS text (event_sms/data/sms_data.xml:7-14); the send relies on the SMS gateway configured in the sms module (delivery, credits: UNKNOWN — EVIDENCE INSUFFICIENT for this module).
- Multi-company: no company rule or company field is defined here; scoping follows the event and sms modules (UNKNOWN — EVIDENCE INSUFFICIENT).

## D. Accounting / payroll / analytic handoffs
- None. No accounting, payroll or analytic objects are touched (event_sms/__manifest__.py:9). SMS credit purchase/billing belongs to the IAP/sms layer (UNKNOWN — EVIDENCE INSUFFICIENT in this module).

## E. Configuration / defaults that change outcomes
- Which channel is used depends entirely on the template kind picked on the scheduler; no settings screen or system parameter is added by this module (event_sms/models/event_mail.py:10-13).
- Trigger, unit and number are inherited event defaults (default unit hours, default trigger before event) (event/models/event_mail.py:36-47).
- Multi-slot events: the base scheduler handles slot-based execution separately (event/models/event_mail.py:114-116); whether the SMS path applies to slot-based sending is UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path
- Extends: event (schedulers, event-type templates, registrations), sms (templates). Modules relying on the mass-SMS channel: sms.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: opt-out handling, phone-number validation failures, delivery status tracking on the registration.

