# Source Map (candidate) — `sale_stock_product_expiry`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_stock_product_expiry` |
| Display name | Sale Stock Product Expiry |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `1013c72b45e6f85f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_stock_product_expiry/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_stock`, `product_expiry`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `sale.order.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 11 of 11 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_stock_product_expiry
Source revision: 19.0.post20260921 | Module: "Sale Stock Product Expiry" (sale_stock_product_expiry/__manifest__.py:2) | depends: sale_stock, product_expiry (:6) | auto_install true (:8) | LGPL-3 (:9)
Basis: static reading of the manifest and the single model file; one test read (shape only, tour not opened).

## A. Capabilities and optionality
- A1. Makes the availability/forecast indicator on sales order lines show "fresh" stock, i.e. ignoring stock that will be removed for expiry before the promised date. sale_stock_product_expiry/__manifest__.py:4; sale_stock_product_expiry/models/sale_order_line.py:11-16
- A2. Automatic bridge; only matters for products with expiration dates enabled. sale_stock_product_expiry/__manifest__.py:8; sale_stock_product_expiry/models/sale_order_line.py:9,13
- A3. Frontend widget files and a tour are shipped in assets (widget code not analysed). sale_stock_product_expiry/__manifest__.py:11-18

## B. Objects, relationships, lifecycle
- B1. Sales line exposes whether its product uses expiration dates (read-only related flag). sale_stock_product_expiry/models/sale_order_line.py:9
- B2. Reading quantities for the line's forecast is done in a context asking for "fresh" forecast; for expiry-tracked products the "free quantity" figure is then re-read from the product for the warehouse (not restricted to the date). sale_stock_product_expiry/models/sale_order_line.py:11-16
- B3. In stock, when expiry-awareness is on, stock whose removal date is on or before a cut-off is counted as expired/not free; the cut-off is the forecast date when the "fresh" flag is set, otherwise the expiry date passed by the caller. stock/models/product.py:219-222 (owner stock)
- B4. (TEST) Two perishable products with three lots each and different customer lead times: forecast at the delivery date shows 200 for the shorter-lead product and 100 for the longer-lead one (lots expiring before the date are excluded). sale_stock_product_expiry/tests/test_perishable_qty_at_date.py:11-47
- B5. No state transitions of its own.

## C. Validations, security, multi-company
- C1. No constraints, groups, ACLs or record rules. sale_stock_product_expiry/ (file list)
- C2. Multi-company: none explicit. UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Expiry data (lots, expiration/removal times): product_expiry / stock. Forecast computation: sale_stock and stock. No accounting, purchase or analytic logic.

## E. Configuration that changes outcomes
- E1. Product "expiration date" setting and lot tracking with removal time. test_perishable_qty_at_date.py:11-21
- E2. Customer lead time on the product (delivery date) and warehouse. test_perishable_qty_at_date.py:19; sale_stock_product_expiry/models/sale_order_line.py:11

## F. Effective extension path (modules)
- Depended on by: none (grep of manifests). Overrides the quantity read hook defined in sale_stock's sale order line.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: exact JS widget behaviour and the tour; effect on reservation (only forecast display is touched).

