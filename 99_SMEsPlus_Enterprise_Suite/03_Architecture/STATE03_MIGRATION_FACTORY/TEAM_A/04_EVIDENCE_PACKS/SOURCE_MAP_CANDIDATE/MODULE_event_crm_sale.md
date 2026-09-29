# Source Map (candidate) — `event_crm_sale`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `event_crm_sale` |
| Display name | Event CRM Sale |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d209239dfca2f544` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/event_crm_sale/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `event_crm`, `event_sale`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_event_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Events / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `event.registration`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `event.registration`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 17 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — event_crm_sale
Source revision: 19.0.post20260921 | Module: "Event CRM Sale" (event_crm_sale/__manifest__.py:5) | depends: event_crm, event_sale (:10) | auto_install true (:15) | LGPL-3 (:17)
Basis: static reading of manifest, model, view and the single test; parent event_crm lead-rule code read for context.

## A. Capabilities and optionality
- A1. Lets event lead rules create ONE CRM lead per sales order ("Per Order", B2B) instead of one per attendee, when registrations come from ticket sales. event_crm_sale/__manifest__.py:9; event_crm_sale/models/event_registration.py:12-18
- A2. The "Create: Per Attendee / Per Order" choice on the lead rule is hidden in event_crm and made visible by this module (list column and form group). event_crm/views/event_lead_rule_views.xml:24,50-51 ; event_crm_sale/views/event_lead_rule_views.xml:8-10,18-20
- A3. Automatic bridge when Event CRM and Event Sales are both installed. event_crm_sale/__manifest__.py:15

## B. Objects, relationships, lifecycle
- B1. Lead rule field "lead creation basis" (owner event_crm): per attendee (default) or per order; help text explains B2C vs B2B. event_crm/models/event_lead_rule.py:77-81
- B2. Grouping of registrations: registrations that belong to a sales order are grouped per order and per rule; for each group the module finds existing leads linked to the same rule and any registration of that order, so the rule updates that lead instead of creating another. event_crm_sale/models/event_registration.py:19-49
- B3. Registrations without a sales order fall back to the base grouping. event_crm_sale/models/event_registration.py:19-20
- B4. Only per-order rules use the grouping; per-attendee rules create one lead per matching registration. event_crm/models/event_lead_rule.py:173-181
- B5. When a group already has a lead the rule appends a "New registrations" description to it; otherwise a new lead is created. event_crm/models/event_lead_rule.py:184-186
- B6. Lifecycle trigger comes from the rule (attendees created / registered / attended) and the sales order confirmation that registers attendees. event_crm/models/event_lead_rule.py:82-85 . (TEST) An order with three tickets for two events produces two leads, one per event, after order confirmation. event_crm_sale/tests/test_event_crm_flow.py:11-45

## C. Validations, security, multi-company
- C1. No constraints, groups, ACLs, or rules in this module. event_crm_sale/ (file list)
- C2. Lead searching in batch is done without extra restriction here; visibility follows crm access. UNKNOWN — EVIDENCE INSUFFICIENT on company scoping of the search over registrations and leads (event_crm_sale/models/event_registration.py:24-31).

## D. Handoffs
- D1. Lead creation and lead content: crm / event_crm. Registration, ticket and order link: event_sale (sale_order_id on registration). event_sale/models/event_registration.py:12
- D2. No accounting, inventory, purchase or analytic logic.

## E. Configuration that changes outcomes
- E1. Lead rule "Create" basis (per attendee vs per order), trigger and registration filters. event_crm/models/event_lead_rule.py:77-85
- E2. Products of type service tracked as event tickets (test setup). event_crm_sale/tests/test_event_crm_flow.py:20-27

## F. Effective extension path (modules)
- Depended on by: test_event_full (manifest grep). Overrides _get_lead_grouping also defined in event_crm (grep).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: lead content (partner, description) when several partners share one order; behaviour on cancelled or refunded orders.

