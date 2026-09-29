# Source Map (candidate) — `project_purchase_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_purchase_stock` |
| Display name | Project - Purchase - Stock |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `b539e23b8d7158f9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_purchase_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project_purchase`, `project_stock`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `purchase.order`, `stock.rule`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `purchase.order`, `stock.rule`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 18 of 18 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_purchase_stock (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`; (TEST) = test-derived. Small glue module carrying the project reference from purchase orders to receipts and through replenishment.

## A. Capabilities and activation
- Adds a project link between purchase orders and the stock pickings they generate (project_purchase_stock/__manifest__.py:6). Depends on project_purchase and project_stock (project_purchase_stock/__manifest__.py:10); auto_install (project_purchase_stock/__manifest__.py:11).
- Upstream fields it relies on: project on purchase order (project_purchase/models/purchase_order.py:9) and project on stock picking (project_stock/models/stock_picking.py:9); both exclude project templates.

## B. Objects, relationships, lifecycle
- Receipt creation: when a purchase order with a project prepares its receipt, the picking gets the same project; no project means nothing added (project_purchase_stock/models/purchase_order.py:9-16).
- Replenishment: when a procurement carrying a project creates a purchase order, that order gets the project (project_purchase_stock/models/stock_rule.py:9-13). Procurement values can carry a project from a manufacturing order's group when it has exactly one MO (project_mrp/models/stock.py:19-23), when project_mrp is installed.
- Reuse of existing draft orders is now project-aware: an open purchase order is reused only when its project equals the procurement's project (including "none" matching only "none") (project_purchase_stock/models/stock_rule.py:15-18) (TEST: project_purchase_stock/tests/test_reordering_rule.py:11-66, covering no-project PO, project set on first PO leading to a new PO, and later no-project procurement reusing the second PO).
- Purchase lines in a project order receive the project's analytic accounts in their distribution (added on missing plans, or full project distribution when none) (project_purchase/models/purchase_order_line.py:9-30); this is owned by project_purchase, not this module.

## C. Validations, security, multi-company
- No constraints, groups, access files, or record rules in this module (directory holds only models and tests; manifest project_purchase_stock/__manifest__.py:3-12). Company scoping is inherited from purchase_stock replenishment; the extra matching term does not mention company (project_purchase_stock/models/stock_rule.py:15-18). Multi-company behaviour beyond that: UNKNOWN — EVIDENCE INSUFFICIENT

## D. Handoffs (owner)
- Purchase order and receipt documents: purchase / purchase_stock. Analytic cost attribution to the project: project_purchase and analytic/account (this module adds no accounting or valuation logic). Inventory valuation: stock_account. Sales: none.

## E. Configuration that changes outcomes
- Presence of a project on the purchase order or procurement values decides splitting of replenishment purchase orders (project_purchase_stock/models/stock_rule.py:17). Replenishment routes (MTO + Buy) as exercised by the test (project_purchase_stock/tests/test_reordering_rule.py:26-31).

## F. Extension path
- Extends purchase.order and stock.rule (project_purchase_stock/models/purchase_order.py:7; project_purchase_stock/models/stock_rule.py:7). No other module lists it as a dependency (manifest grep). Sibling project-glue modules that also pass a project through procurement: project_mrp, project_mrp_account (project_mrp/models/stock.py:19-23).

## G. Not verified
- How the project is set on procurement values for reordering rules or manual replenishment: UNKNOWN — EVIDENCE INSUFFICIENT
- Project profitability treatment of received goods: UNKNOWN — EVIDENCE INSUFFICIENT

