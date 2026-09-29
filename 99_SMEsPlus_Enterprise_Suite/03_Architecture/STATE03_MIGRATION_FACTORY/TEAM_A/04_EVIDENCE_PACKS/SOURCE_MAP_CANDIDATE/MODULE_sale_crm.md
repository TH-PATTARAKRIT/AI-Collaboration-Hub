# Source Map (candidate) — `sale_crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_crm` |
| Display name | Opportunity to Quotation |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `50c4b28997e01d17` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_crm/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `crm`
- Direct dependents in 300-module list (1): `gamification_sale_crm`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_crm_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 1, views 4, window actions 4, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `crm.quotation.partner` (Create new or use existing Customer on new Quotation)
- Objects extended from other modules (3): `crm.team`, `sale.order`, `crm.lead`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `crm.team`, `sale.order`, `crm.lead`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 39 of 39 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_crm
Source revision: 19.0.post20260921 | Module: "Opportunity to Quotation" (sale_crm/__manifest__.py:5) | depends: sale, crm (:19) | License LGPL-3 (:31)
Basis: static reading of 3 model files, 1 wizard, security, views; 4 test files scanned (test names/assertions).

## A. Capabilities and optionality
- A1. Lets a salesperson create quotations directly from a CRM opportunity, see the opportunity's quotations and confirmed orders as counters, and have the opportunity's expected revenue lifted when a linked order is confirmed. sale_crm/models/crm_lead.py:10-13,35-66,103-110; sale_crm/views/crm_lead_views.xml:9-30
- A2. Conditional: bridge module, installed automatically when sale and crm are both present. sale_crm/__manifest__.py:28
- A3. Uninstall side effect: all sales teams that do not use opportunities are switched back to using them. sale_crm/__init__.py:7-9; sale_crm/__manifest__.py:29
- A4. Sales team form: the "opportunities" block is made visible; the team dashboard button becomes "Sales Analysis" (inside the Sales app) and opens the sales analysis report. sale_crm/views/crm_team_views.xml:10; sale_crm/models/crm_team.py:9-18
- A5. Sale order form gets an "Opportunity" field with creation defaults (campaign, medium, source, partner, company, and tags for salespeople). sale_crm/views/sale_order_views.xml:13-35
- A6. Lead merge summary lists the sale orders of merged leads. sale_crm/data/crm_lead_merge_template.xml:4-16; sale_crm/models/crm_lead.py:97-101 (TEST: tests/test_crm_lead_merge.py:12-33)

## B. Business objects, relationships, lifecycle
- B1. Sale order (sale.order, owner sale) gets an optional link to one opportunity (must be an opportunity, not a raw lead; company empty or equal to the order's company; company check on). sale_crm/models/sale_order.py:10-12
- B2. Opportunity (crm.lead, owner crm) gets its list of orders and three derived numbers: quotation count (draft or sent), sale-order count (anything not draft/sent/cancelled), and sum of untaxed totals of those orders converted into the company currency at each order's date. sale_crm/models/crm_lead.py:15-27,68-75
- B3. "New Quotation" button (opportunities only, hidden for lost/inactive): if the opportunity has no customer, a wizard asks to create a new customer / link an existing one / proceed without a customer; if it has a customer, a quotation is opened directly. sale_crm/models/crm_lead.py:29-39; sale_crm/wizard/crm_opportunity_to_quotation.py:35-52; sale_crm/views/crm_lead_views.xml:10-12 (TEST: tests/test_crm_lead_convert_quotation.py:20-119)
- B4. Wizard default: if a matching customer is found for the lead, choice defaults to "link existing", else "create". sale_crm/wizard/crm_opportunity_to_quotation.py:27-31 (TEST: tests/test_crm_lead_convert_quotation.py:24-35,58-59,90)
- B5. New quotation is pre-filled from the opportunity: customer, campaign, medium, source, origin (opportunity name), company, tags, team, salesperson. sale_crm/models/crm_lead.py:77-95
- B6. Revenue lift on confirmation: expected revenue is raised to the order's untaxed total only if it is currently lower and the order currency equals the opportunity company's currency; a note is logged. sale_crm/models/sale_order.py:14-18; sale_crm/models/crm_lead.py:103-110 (TEST: tests/test_sale_crm.py:7-60 - other-currency order leaves 0; same-currency order sets 200)
- B7. Confirmation runs with the default tag context removed to avoid tags leaking into follow-on records. sale_crm/models/sale_order.py:15
- B8. Opportunity won/lost stage is NOT changed by order confirmation in this module. The manifest text says the case is closed after generating the order, but no such closing was found in code. sale_crm/__manifest__.py:8-15; sale_crm/models/sale_order.py:14-18. UNKNOWN — EVIDENCE INSUFFICIENT for any closing done elsewhere (crm).

## C. Validations, security, multi-company
- C1. Wizard refuses to run unless launched from a lead. sale_crm/wizard/crm_opportunity_to_quotation.py:16-18
- C2. Access: wizard usable by salespersons (read/write/create, no delete); no other access rows, no record rules. sale_crm/security/ir.model.access.csv:2
- C3. Multi-company: opportunity link restricted to same-company or company-less opportunities; new quotation defaults to the lead's company, else the current company; revenue conversion uses each order's company. sale_crm/models/sale_order.py:11-12; sale_crm/models/crm_lead.py:22,88

## D. Handoffs
- D1. Quotation lifecycle, confirmation, invoicing, delivery: sale (and downstream). CRM stages, probability, won/lost: crm.
- D2. Only crm-side money effect is expected revenue on the opportunity; no accounting or inventory posting here. sale_crm/models/crm_lead.py:103-110
- D3. Sales analysis report from team dashboard: sale. sale_crm/models/crm_team.py:17
- D4. Partner creation/assignment from a lead: crm (`_handle_partner_assignment`, `_find_matching_partner`). sale_crm/wizard/crm_opportunity_to_quotation.py:27,49,51

## E. Configuration/defaults that change outcomes
- E1. Company currency of the opportunity vs order currency decides whether revenue is lifted (B6). (TEST) tests/test_sale_crm.py:53-60
- E2. Wizard choice "do not link to a customer" leaves the lead without a customer and opens a quotation with no customer default. (TEST) tests/test_crm_lead_convert_quotation.py:110-119
- E3. Team option "use opportunities" is forced on when this module is uninstalled. sale_crm/__init__.py:7-9

## F. Effective extension path (grep of _inherit)
- F1. This module extends: crm.lead, crm.team, sale.order. sale_crm/models/crm_lead.py:8; crm_team.py:7; sale_order.py:8
- F2. Modules depending on sale_crm: gamification_sale_crm, test_crm_full.

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: what happens to the opportunity stage after a won order (crm-side automation not read).
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: partner-level order statistics test (tests/test_res_partner.py) belongs to a different override not in this module's models; not analysed.
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of revenue lift when the opportunity has no company set.

