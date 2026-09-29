# Source Map (candidate) — `event_crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event_crm` |
| Display name | Event CRM |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3942cbd0218aa2c7` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event_crm/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `event`, `crm`
- Direct dependents in 300-module list (1): `event_crm_sale`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `test_crm_full`, `test_event_full`, `website_event_crm`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / —
- Inventory of user-facing artifacts (counts): menu items 1, views 8, window actions 5, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `event.lead.request` (Event Lead Request); `event.lead.rule` (Event Lead Rules)
- Objects extended from other modules (4): `event.registration`, `event.event`, `crm.lead`, `event.question.answer`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `event.registration`, `event.event`, `crm.lead`, `event.question.answer`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Event CRM: Generate Leads based on Rules every 1 days
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 50 of 50 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — event_crm (Odoo 19 Community, revision 19.0.post20260921)

## A. Capabilities; core / optional / conditional
- Creates or updates CRM leads/opportunities from event registrations according to configurable "lead generation rules" (event_crm/__manifest__.py:9; event_crm/models/event_lead_rule.py:10-66).
- Bridge module: depends on event and crm (event_crm/__manifest__.py:10); auto_install is True, so it is installed automatically once both are present (event_crm/__manifest__.py:32). No settings toggle found in this module.
- Rule menu "Lead Generation" restricted to event managers (event_crm/views/event_lead_rule_views.xml:100-105). Lead type field is shown only with the "use leads" CRM group (event_crm/views/event_lead_rule_views.xml:71); the default lead type follows that group (event_crm/models/event_lead_rule.py:103-106).
- "Per Order" creation basis is documented as exposed in the interface only when event_sale or website_event is installed; behaviour itself lives here (event_crm/models/event_lead_rule.py:20-22, :77-81).

## B. Business objects, relationships, lifecycle
- Lead Rule (event.lead.rule): name, active flag, creation basis (per attendee / per order), trigger (on creation / on registration confirmed / on attended), optional event, optional event templates, optional company, optional registration filter, and lead defaults (type, sales team, salesperson, tags) (event_crm/models/event_lead_rule.py:71-111).
- Lead <-> Registration: many-to-many links; each lead also records its source event and the rule that created it (event_crm/models/crm_lead.py:10-15; event_crm/models/event_registration.py:14-16).
- Event Lead Request (technical batch record, one per event at a time) tracks progress of a background regeneration (event_crm/models/event_lead_request.py:16-32).
- Trigger lifecycle: registration create -> "create" rules; state written to open -> "confirm" rules; state written to done -> "done" rules (event_crm/models/event_registration.py:29-36, :64-68, :82-103).
- Registrations in draft or cancel state are excluded from manual/batch regeneration (event_crm/models/event_event.py:35-38; event_crm/models/event_lead_request.py:50-53).
- Rules do not duplicate: registrations already linked to a lead of the same rule are skipped (event_crm/models/event_lead_rule.py:151-161). All matching rules apply, so several leads can result from one registration (event_crm/models/event_lead_rule.py:62-65).
- Per-order rules group registrations by event and creation timestamp; a group creates one lead per event (event_crm/models/event_registration.py:316-320, :338-348; event_crm/models/event_lead_rule.py:192-194). Update of an existing group lead is stated as not supported for grouping (event_crm/models/event_registration.py:322-323).
- Later registration edits (partner, name, email, phone) propagate to linked leads; description gets an appended "Updated registrations" block (event_crm/models/event_registration.py:38-61, :105-169).
- Contact rule: a registration's partner is kept on an attendee lead only if its email and phone are consistent with the registration; otherwise the lead carries the raw contact details (event_crm/models/event_registration.py:199-258).

## C. Validations, automation, security, multi-company
- Rule filter conditions: active, optional domain filter, company must equal event/registration company when set, event OR event template must match when either is set (event_crm/models/event_lead_rule.py:202-229).
- Uniqueness: one generation request per event (event_crm/models/event_lead_request.py:29-32).
- Manual regeneration allowed only to event managers, else a user error (event_crm/models/event_event.py:32-33). Server action bound to events, restricted to event manager group (event_crm/data/ir_action_data.xml:4-13).
- Batch size 200 registrations; above that a background job is used, below it runs synchronously (event_crm/models/event_lead_request.py:22; event_crm/models/event_event.py:40-55).
- Scheduled job "Generate Leads based on Rules" daily, re-triggers itself until requests complete and removes finished requests (event_crm/data/ir_cron_data.xml:5-13; event_crm/models/event_lead_request.py:35-79).
- Rule execution runs with elevated privileges when fired from registration events (event_crm/models/event_registration.py:66,68,96,99,102).
- Access: rule model read-only for registration desk, event user, salesman groups; full for event manager; request model only for system admin (event_crm/security/ir.model.access.csv:2-6).
- Multi-company: record rule on lead rules for multi-company users, rules visible when company is in allowed companies or unset (event_crm/security/event_crm_security.xml:4-9).
- Lead/registration counters and links on events are gated by sales salesman or registration desk groups (event_crm/models/event_event.py:11-15; event_crm/models/crm_lead.py:12-19).
- Data import skips rule execution (event_crm/models/event_registration.py:72-80); context flag skip also exists (event_crm/models/event_registration.py:34).

## D. Handoffs (module ownership)
- Lead/opportunity records, teams, tags, merge: crm (event_crm/models/crm_lead.py:8). Merge carries over registration links and event/rule fields (event_crm/models/crm_lead.py:26-35), merge summary shows event info (event_crm/data/crm_lead_merge_template.xml:4-18).
- Events, registrations, questions: event. Question-answer button opens a pre-filled rule (event_crm/models/event_question_answer.py:7-20).
- Phone normalisation: phone_validation (event_crm/models/event_registration.py:8, :231-232).
- Sale-order based grouping: event_crm_sale (depends on event_crm, event_sale — event_crm_sale/__manifest__.py:10). Website flow: website_event_crm (website_event_crm/__manifest__.py:10). No accounting/inventory handoff in this module.

## E. Configuration that changes outcomes
- Rule trigger, creation basis, filter domain, company/event/template scoping, default type/team/salesperson/tags (event_crm/models/event_lead_rule.py:71-111).
- Selecting a sales team pre-fills the salesperson with the team leader in the form (event_crm/models/event_lead_rule.py:113-116).
- Lead campaign/source/medium taken from the first registration with a value (event_crm/models/event_registration.py:190-193).

## F. Extension path (grep of _inherit)
- event_crm_sale, website_event_crm (extend event.registration); event_crm itself extends crm.lead, event.event, event.registration, event.question.answer (event_crm/models/*.py). Other manifests referencing it: test_event_full, test_crm_full (test modules).

## G. Not verified
- Tests seen (TEST): batch regeneration flow with cron trigger (event_crm/tests/test_event_crm_flow.py:35-70); per-order create/update/duplicate cases (event_crm/tests/test_event_crm_flow.py:72-236); merge behaviour (event_crm/tests/test_crm_lead_merge.py:13-83).
- Exact per-order behaviour when event_sale groups by sale order: UNKNOWN — EVIDENCE INSUFFICIENT (outside this module).
- Rule menu placement/parent menu: UNKNOWN — EVIDENCE INSUFFICIENT (not fully inspected).

