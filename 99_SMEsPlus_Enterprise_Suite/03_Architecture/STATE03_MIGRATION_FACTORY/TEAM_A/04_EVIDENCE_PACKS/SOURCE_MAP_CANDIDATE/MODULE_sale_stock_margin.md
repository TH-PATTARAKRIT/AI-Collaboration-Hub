# Source Map (candidate) — `sale_stock_margin`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_stock_margin` |
| Display name | Sale Stock Margin |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f207178f455e2971` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_stock_margin/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_stock`, `sale_margin`
- Direct dependents in 300-module list (1): `sale_mrp_margin`
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 19 of 19 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_stock_margin
Source revision: 19.0.post20260921 | Module: "Sale Stock Margin" (sale_stock_margin/__manifest__.py:3) | depends: sale_stock, sale_margin (:7) | auto_install true (:9) | LGPL-3 (:11)
Basis: static reading of the single model file; test names and selected tests read.

## A. Capabilities and optionality
- A1. Once goods are delivered, the line "cost" used for margin is replaced by the actual valued cost of the delivery instead of the product's planned standard cost. sale_stock_margin/__manifest__.py:5; sale_stock_margin/models/sale_order_line.py:10-35
- A2. Automatic bridge: installs itself whenever Sales Stock and Sales Margin are both installed. sale_stock_margin/__manifest__.py:7,9

## B. Objects, relationships, lifecycle
- B1. No new objects/fields; overrides how the line's cost is computed. Recomputed when the line's stock moves, their valuation, or the transfer state change. sale_stock_margin/models/sale_order_line.py:10
- B2. Lines with no valued (non-cancelled, non-draft) moves keep the base rule (product standard cost). sale_stock_margin/models/sale_order_line.py:16-17 ; has_valued_move_ids true when any move is neither cancelled nor draft: sale_stock/models/sale_order_line.py:464-467
- B3. If the product category uses a costing method other than standard: cost = weighted mix of (delivered quantity x delivery unit cost) and (undelivered remainder x current product cost); with nothing delivered yet the current product cost is used. sale_stock_margin/models/sale_order_line.py:18-31
- B4. Under standard costing the existing cost is not overwritten (planned cost stays) unless the line was added from a delivery with zero ordered quantity, in which case base computation applies. sale_stock_margin/models/sale_order_line.py:18,32-35; (TEST) sale_stock_margin/tests/test_sale_stock_margin.py:367-393
- B5. Delivery unit cost = weighted average of dropshipped moves (their valuation) and regular outgoing moves (normal move price); if no valued quantity, falls back to the move price. stock_account/models/stock_move.py:699-711 (owner stock_account)
- B6. Cost is converted to the line unit of measure and to the sales line currency. sale_stock_margin/models/sale_order_line.py:27-31; (TEST) test_sale_stock_margin.py:218-241 (multi-currency), 468-485 (different UoM)
- B7. (TEST) Average-cost (AVCO) products: cost reflects delivered moves, service lines in the same order do not change it, zero-quantity lines and returns handled. test_sale_stock_margin.py:187-217,486-633
- B8. (TEST) Dropshipped FIFO product: until the dropship transfer is validated the cost is the product's standard cost; after validation it is the purchase order unit price. test_sale_stock_margin.py:634-669

## C. Validations, security, multi-company
- C1. No constraints, groups or rules added. Cost fields remain internal-user only (from sale_margin). sale_margin/models/sale_order_line.py:18
- C2. Multi-company: computation runs in the line's company context. sale_stock_margin/models/sale_order_line.py:14. (TEST) confirming an order of company B while logged in company A computes from B's data. test_sale_stock_margin.py:242-302
- C3. UNKNOWN — EVIDENCE INSUFFICIENT on behaviour of returns to non-customer locations for FIFO beyond the AVCO tests listed.

## D. Handoffs
- D1. Inventory valuation of delivery moves: stock_account (unit cost of done moves). sale_stock_margin/models/sale_order_line.py:21
- D2. Purchase price for dropship: from the purchase order via stock_account/stock_dropshipping valuation; this module only reads it. (TEST) test_sale_stock_margin.py:634-669
- D3. Kit and manufactured-product refinements: sale_mrp / sale_mrp_margin. (TEST) sale_mrp_margin/tests/test_sale_mrp_flow.py:283-332
- D4. No accounting entries are created here.

## E. Configuration that changes outcomes
- E1. Product category costing method (standard vs average/FIFO). sale_stock_margin/models/sale_order_line.py:18
- E2. Product standard cost and cost currency (fallback and remainder share). sale_stock_margin/models/sale_order_line.py:23,26
- E3. Whether delivery has been validated (state of transfer). sale_stock_margin/models/sale_order_line.py:10,21

## F. Effective extension path (modules)
- Depended on by: sale_mrp_margin (manifest). Base cost logic overridden here originates in sale_margin; also overridden in sale_expense_margin and sale_timesheet_margin.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how a partial delivery combined with mixed UoM and returns behaves under FIFO with lots (only test names read).

