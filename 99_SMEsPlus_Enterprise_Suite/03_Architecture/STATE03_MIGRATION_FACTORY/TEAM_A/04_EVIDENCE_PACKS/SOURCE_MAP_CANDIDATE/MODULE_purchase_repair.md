# Source Map (candidate) — `purchase_repair`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_repair` |
| Display name | Purchase Repair |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `9ccb350064c06195` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_repair/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `repair`, `purchase_stock`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / Keep track of linked purchase and repair orders
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `purchase.order`, `repair.order`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `purchase.order`, `repair.order`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 22 of 22 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: purchase_repair
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Lets users see, from a repair order, the purchase orders that were generated to supply its parts, and from a purchase order, the repair orders that requested the goods. purchase_repair/__manifest__.py:5,10-14
- Conditional: auto-installs when repair and purchase_stock are both installed. purchase_repair/__manifest__.py:10,15
- Read-only traceability aid: adds counters and "open related" actions; no state changes, no accounting. purchase_repair/models/purchase_order.py:8-29; purchase_repair/models/repair_order.py:8-29

## B. Business objects and relationships
- Purchase order side: a count of source repairs = the repair orders reached through the purchase lines' downstream stock movements. purchase_repair/models/purchase_order.py:10-13
- Repair order side: a count of generated purchases = the purchase orders reached through the repair parts' "created purchase line" link. purchase_repair/models/repair_order.py:10-13
- Open-related actions: one result opens the record directly; several open a list; none returns an empty form action. purchase_repair/models/purchase_order.py:15-29; purchase_repair/models/repair_order.py:15-29
- Links themselves originate in purchase_stock (purchase lines keep downstream moves; stock moves keep created purchase lines). purchase_stock/models/purchase_order_line.py:30; purchase_stock/models/stock_move.py:18
- How the link comes to exist (TEST): a repair part on a product that has a make-to-order route on the repair operation and a "buy" route with a vendor; confirming the repair creates a purchase order whose line points back to the repair. purchase_repair/tests/test_repair_purchase_flow.py:15-58 (TEST)
- Lifecycle of both documents is unchanged and owned by repair (draft/confirmed/under repair/repaired/cancelled) and purchase. repair/models/repair.py:42-53
- Repair-order purchase button is hidden while the repair is in draft. purchase_repair/views/repair_views.xml:12

## C. Validations / security / multi-company
- No constraints. Visibility control by groups: purchase counter/button on the repair form needs purchase user (purchase.group_purchase_user); repair counter/button on the purchase form needs inventory user (stock.group_stock_user). purchase_repair/models/repair_order.py:8; purchase_repair/views/repair_views.xml:11; purchase_repair/models/purchase_order.py:8; purchase_repair/views/purchase_views.xml:11
- Company scoping inherited from record rules on the two parent objects (repair order rule: repair/security/repair_security.xml:5-9; purchase rules owned by purchase).

## D. Handoffs
- Procurement: repair parts drive a make-to-order procurement into purchase [stock rules owned by stock, purchase_stock]. repair/models/repair.py:629-631; repair/models/stock_warehouse.py:78-98
- Receipts, vendor bills and valuation of purchased parts stay in [purchase_stock / purchase / stock_account]; this module does not touch them.

## E. Configuration that changes outcomes
- Whether a repair part triggers a purchase depends on product routes (MTO + Buy), vendor list, and whether the MTO rule for the repair operation is set to make-to-order. purchase_repair/tests/test_repair_purchase_flow.py:23-42 (TEST)
- Warehouse-level "Repair MTO Rule" is created per warehouse by repair. repair/models/stock_warehouse.py:12-13,82-97

## F. Effective extension path
- purchase.order is extended by purchase_repair (among many other purchase-related modules). repair.order is extended by purchase_repair, mrp_repair, l10n_din5008_repair (from _inherit search; module names only).

## G. Not verified
- Behaviour when one purchase line is merged across several repairs or when a purchase order is merged/cancelled after link creation: UNKNOWN — EVIDENCE INSUFFICIENT
- Any access-right nuance if a user has purchase rights but not inventory rights (counter on purchase form is hidden by group, not tested): UNKNOWN — EVIDENCE INSUFFICIENT

