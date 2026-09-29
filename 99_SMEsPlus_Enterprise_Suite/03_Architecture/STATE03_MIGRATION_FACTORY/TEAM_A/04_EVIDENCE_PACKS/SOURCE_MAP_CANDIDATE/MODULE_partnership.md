# Source Map (candidate) — `partnership`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `partnership` |
| Display name | Partnership / Membership |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e3bfd515df5f5c64` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/partnership/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `crm`, `sale`
- Direct dependents in 300-module list (1): `website_crm_partner_assign`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/CRM / —
- Inventory of user-facing artifacts (counts): menu items 1, views 9, window actions 3, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `res.partner.grade` (Partner Grade)
- Objects extended from other modules (6): `product.pricelist`, `sale.order`, `product.template`, `res.company`, `res.config.settings`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `res.partner.grade` ← Community: `website_crm_partner_assign`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `product.pricelist`, `sale.order`, `product.template`, `res.company`, `res.config.settings`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 36 of 37 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — partnership
Source revision: 19.0.post20260921 | Module: "Partnership / Membership" (partnership/__manifest__.py:3) | depends: crm, sale (:12) | License LGPL-3 (:24)
Basis: static reading of 6 model files, security, seed data, menus/settings views; 1 test file (3 tests) read.

## A. Capabilities and optionality
- A1. Lets a business define membership/partner "levels" (grades), optionally linked to a pricelist, sell a level as a service product, and have the buyer automatically receive the level (and pricelist) when the sale is confirmed. partnership/models/res_partner_grade.py:7-15; partnership/models/product_template.py:9-12; partnership/models/sale_order.py:27-36 (TEST: tests/test_partnership.py:13-24)
- A2. Optional module (no auto_install key); switched on from CRM settings via the "Membership / Partnership" toggle. manifest has no auto_install key (partnership/__manifest__.py:2-25); crm/models/res_config_settings.py:18; crm/views/res_config_settings_views.xml:35
- A3. Company-level label for affiliates (default "Members"), editable in settings, which renames the configuration menu and appears on pricelist/grade counters. partnership/models/res_company.py:9-12; partnership/models/res_config_settings.py:9-15; partnership/views/partnership_menu.xml:3-7
- A4. Seed levels shipped: Gold, Silver, Bronze. partnership/data/res_partner_grade_data.xml:3-14
- A5. Product form exposes the "Membership / Partnership" service option and an "Assigned Level" field when selected. partnership/views/product_template_views.xml:8-13
- A6. Partner list/search: filters and group-by for level and pricelist; smart counters of partners per level and per pricelist. partnership/views/res_partner_views.xml:3-47; partnership/models/product_pricelist.py:9-20; partnership/models/res_partner_grade.py:16-27

## B. Business objects, relationships, lifecycle
- B1. Level (res.partner.grade, new, owner partnership): name, order, active flag, company, optional default pricelist. partnership/models/res_partner_grade.py:7-17
- B2. Partner (res.partner, owner base) gets a tracked level; kanban-style grouping shows all levels. partnership/models/res_partner.py:10
- B3. Product (product.template, owner product/sale) gets service-tracking option "partnership" (falls back to default if module removed) and a level. partnership/models/product_template.py:9-12
- B4. Sale order (sale.order, owner sale) computes an "assigned level" from the first partnership-type line's product. partnership/models/sale_order.py:10,21-25
- B5. Lifecycle: on confirmation of the order, the commercial (top-level) partner of the customer receives the level. partnership/models/sale_order.py:27-36 (TEST: tests/test_partnership.py:14-18)
- B6. Assigning a level to a partner also stamps the level's default pricelist as the partner's specific pricelist. partnership/models/res_partner.py:12-24 (TEST: tests/test_partnership.py:19-23)
- B7. Partnership products are counted as saleable service types. partnership/models/product_template.py:14-16 (TEST: tests/test_partnership.py:38-49)
- B8. No un-assignment: nothing in the module removes or downgrades a level on cancel, refund or expiry. UNKNOWN — EVIDENCE INSUFFICIENT beyond absence in this module (no membership period/expiry field found).

## C. Validations, security, multi-company
- C1. Conflicting products: an order may not hold partnership products that assign different levels; the check runs whenever order lines change (message wording speaks of confirmation). partnership/models/sale_order.py:12-19 (TEST: tests/test_partnership.py:26-36)
- C2. Conflicting pricelists: when a level with a default pricelist is set on a partner and a different pricelist is supplied in the same write, the write is refused; otherwise the level's pricelist is applied. partnership/models/res_partner.py:13-24
- C3. Access on levels: all internal users read; sales salespersons read/write/create (no delete); sales managers and system administrators full. partnership/security/ir.model.access.csv:2-5
- C4. No record rules. Level has a company field defaulting to the current company but no rule restricting by company in this module. partnership/models/res_partner_grade.py:14; partnership/security/ir.model.access.csv (only access rows). Multi-company enforcement: UNKNOWN — EVIDENCE INSUFFICIENT.
- C5. Confirm-time assignment writes the level on the commercial partner as the confirming user, without sudo. partnership/models/sale_order.py:36

## D. Handoffs
- D1. Quotation, confirmation, invoicing: sale / account. This module only reacts after confirmation.
- D2. Pricing effect: pricelist owned by product; module only sets the partner's specific pricelist. partnership/models/res_partner.py:23
- D3. No accounting, inventory or analytic posting. (none found in module)
- D4. Website portal/"partner assign" use of levels: website_crm_partner_assign (F2), not read.

## E. Configuration/defaults that change outcomes
- E1. Level default pricelist decides whether buying a level changes the customer's pricing. partnership/models/res_partner_grade.py:15
- E2. Product "service tracking = partnership" plus an assigned level on the product is what triggers assignment; product without a level assigns nothing (level empty). partnership/models/sale_order.py:24-25,34-35
- E3. Company label setting (default "Members"). partnership/models/res_company.py:9-12

## F. Effective extension path (grep of _inherit)
- F1. This module extends: product.pricelist, product.template, res.company, res.config.settings, res.partner, sale.order. partnership/models/*.py
- F2. Module depending on partnership: website_crm_partner_assign (reverse dependency index).

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: no expiry, renewal or invoice-payment gating of membership found; whether payment is required before level assignment is not addressed (assignment is on order confirmation only).
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: partner form placement of the level field (partner view not fully read).
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: multi-company behaviour (C4).

