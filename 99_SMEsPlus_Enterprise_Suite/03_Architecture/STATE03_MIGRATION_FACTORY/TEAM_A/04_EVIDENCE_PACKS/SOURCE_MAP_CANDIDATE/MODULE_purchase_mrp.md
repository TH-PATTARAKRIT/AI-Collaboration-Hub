# Source Map (candidate) — `purchase_mrp`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_mrp` |
| Display name | Purchase and MRP Management |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c2a4a549ca4bff41` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_mrp/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp`, `purchase_stock`
- Direct dependents in 300-module list (1): `mrp_subcontracting_purchase`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / —
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (9): `purchase.order`, `purchase.order.line`, `stock.move`, `stock.rule`, `mrp.production`, `mrp.bom`, `mrp.bom.line`, `report.mrp.report_mo_overview`, `report.mrp.report_bom_structure`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `purchase.order`, `purchase.order.line`, `stock.move`, `stock.rule`, `mrp.production`, `mrp.bom`, `mrp.bom.line`, `report.mrp.report_mo_overview`, `report.mrp.report_bom_structure`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 41 of 41 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: purchase_mrp ("Purchase and MRP Management")
Source revision: 19.0.post20260921 (Odoo 19.0 Community). Pointers `module/path:LINE`; (TEST) = test-derived.
Manifest: bridge between manufacturing and purchasing; depends mrp + purchase_stock; `auto_install: True` (purchase_mrp/__manifest__.py:9-14,26,28). It is CORE whenever both apps and stock-purchase are present; there is no setting or group toggling it.

## A. Capabilities
1. Buying kits (bills of materials of type "phantom" i.e. Kit): received quantity of a kit PO line is derived from component receipts, counting returns only when flagged to refund (purchase_mrp/models/purchase.py:50-81). Kit quantity edits on a PO propagate to downstream demand (:105-121). (TEST) component moves follow the BoM and re-scale when the kit quantity changes 1 -> 2 (purchase_mrp/tests/test_purchase_mrp_flow.py:565-586); inter-company receipt of a kit updates received quantity (:1324-1356).
2. Cost share on BoM lines ("Cost Share (%)", meant for splitting a purchased kit's cost across components) (purchase_mrp/models/mrp_bom.py:33-39; column shown only for Kit BoMs, optional/hidden: purchase_mrp/views/mrp_bom_views.xml:8-10). Used to spread purchase price into component valuation, including bill-based adjustments and Anglo-Saxon entries (purchase_mrp/models/stock_move.py:19-58,72-86). Without any cost share set, cost is divided equally among components (purchase_mrp/models/mrp_bom.py:41-58; (TEST) equal split, test_purchase_mrp_flow.py:199-224).
3. Two-way traceability between purchase orders and manufacturing orders: counters and smart buttons on MO ("Purchases") and PO ("Manufacturing") (purchase_mrp/models/mrp_production.py:10-51; purchase_mrp/models/purchase.py:13-44; views purchase_mrp/views/mrp_production_views.xml:9-15, purchase_mrp/views/purchase_order_views.xml:8-14). CONDITIONAL on groups: purchase counter/button needs Purchase User, manufacturing counter/button needs MRP User (purchase_mrp/models/mrp_production.py:13; purchase_mrp/models/purchase.py:16; views as above).
4. Reporting hooks: BoM structure report shows "buy" route with vendor, lead time (vendor delay + rule delay + company purchase days) and minimum-quantity alert (purchase_mrp/report/mrp_report_bom_structure.py:10-48); MO overview lists PO lines in RFQ / RFQ sent / to-approve as extra replenishment, uses estimated vs expected receipt date depending on PO state, and PO-based cost with tax handling (purchase_mrp/report/mrp_report_mo_overview.py:10-100). Orderpoint list shows Route column by default (purchase_mrp/views/stock_orderpoint_views.xml:8-10).
5. Procurement-exception notification also reaches users of MOs in the procurement group (purchase_mrp/models/stock_rule.py:9-14).

## B. Objects, relationships, lifecycle
- Extends mrp.bom / mrp.bom.line (cost share), mrp.production (PO count/link), purchase.order and purchase.order.line (kit logic, MO link), stock.move (cost/valuation), stock.rule, and two reports.
- Relationship PO <-> MO: an MO's raw-material moves (and their origin moves) link to PO lines through "created purchase lines" (MTO buy of components) or the move's purchase line (purchase_mrp/models/mrp_production.py:46-50); a PO finds MOs through the downstream moves of its lines (purchase_mrp/models/purchase.py:23-24). Merging MO origin links keeps created purchase lines (purchase_mrp/models/mrp_production.py:52-63). Upstream document for chained procurements is the PO and its buyer (purchase_mrp/models/purchase.py:102-103).
- Receipt moves of a PO inherit the production group when all referenced moves share one (purchase_mrp/models/purchase.py:83-87); if the line comes from a sold kit, component receipt moves are tied to the kit's BoM lines (:88-99) — the kit-sold hook returns nothing here and is completed by `sale_purchase_stock` (purchase_mrp/models/purchase.py:123-124; sale_purchase_stock/models/purchase_order.py:32).
- No new states. PO states (RFQ, RFQ Sent, To Approve, Purchase Order, Cancelled) stay in purchase (purchase/models/purchase_order.py:105-111); MO/receipt lifecycle stays in mrp/stock. The MO overview treats a PO as "done" when PO state is purchase and all its moves are done or cancelled (purchase_mrp/report/mrp_report_mo_overview.py:76-79).
- (TEST) cancelling an MO with an MTO-purchased component (test_purchase_mrp_flow.py:1175) and MO overview with MTO purchase and backorders (:1121) are covered; outcomes not re-derived here.

## C. Validations, automation, security, multi-company
- Constraint: on BoM save, cost shares must be non-negative and, when any is set, sum to 100 (rounded to 2 digits) per variant, considering variant-skipped lines and zero-quantity lines; errors: "Components cost share have to be positive or equals to zero." and "The total cost share for a BoM's component have to be 100" (purchase_mrp/models/mrp_bom.py:11-23). (TEST) variants/optional lines and rounding to precision (purchase_mrp/tests/test_anglo_saxon_valuation.py:571, :878; test_purchase_mrp_flow.py:1216-1235 — names/setup only reviewed).
- Rounding: last line absorbs remainder so shares sum to 100 (purchase_mrp/models/mrp_bom.py:25-30).
- Valuation guard: Anglo-Saxon entry generation for a kit raises an error when the computed total valuation quantity is zero (purchase_mrp/models/stock_move.py:84-85).
- Security: adds read-only ACL so Purchase User can read BoMs and BoM lines (purchase_mrp/security/ir.model.access.csv:2-3); no record rules. Kit lookups are company-specific (`company_id` passed to BoM search, purchase_mrp/models/purchase.py:70-72,90; sudo lookup without company for quantity procurement at :111 — UNKNOWN — EVIDENCE INSUFFICIENT for cross-company effect).

## D. Handoffs (owner in brackets)
- Inventory: receipts, kit explosion, MTO/replenishment routes [stock, purchase_stock, mrp]; downstream demand adjustment [purchase_stock via `_get_move_dests_initial_demand`, purchase_stock/models/purchase_order_line.py:201].
- Accounting/valuation: cost ratio, value and quantity taken from vendor bills, and Anglo-Saxon price-difference logic for kits [purchase_stock/stock_account base: purchase_stock/models/stock_move.py:217-225, extended here purchase_mrp/models/stock_move.py:19-58,72-86]. (TEST) many valuation scenarios: FIFO/AVCO, multi-currency, nested kits, backorders, unbuild, lots (purchase_mrp/tests/test_anglo_saxon_valuation.py:11-1013; test names only reviewed).
- Approval: none added; PO approval thresholds remain in purchase (purchase/models/purchase_order.py:1251-1259).
- Cost share field is shared with by-product cost share on stock moves in mrp (mrp/models/stock_move.py:56-58); merged moves sum it (purchase_mrp/models/stock_move.py:66-70).

## E. Configuration that changes outcomes
- BoM type Kit and its cost shares; product cost method / valuation type (FIFO, AVCO, real-time) affect entries (TEST setup at test_purchase_mrp_flow.py:199-202); vendor lead times and company "days to purchase" in reports (purchase_mrp/report/mrp_report_bom_structure.py:20); MTO/Buy routes and vendor presence decide "buy" route display (:40-41).

## F. Effective extension path
- Modules depending on purchase_mrp: mrp_subcontracting_purchase.
- Other Community modules extending mrp.bom / mrp.bom.line: mrp_subcontracting, project_mrp, sale_mrp. Modules referencing cost share: mrp, mrp_account, mrp_landed_costs, sale_mrp_margin. Modules using created purchase lines: purchase_stock (owner), purchase_repair. `_get_mrp_productions` extended by mrp_subcontracting_purchase; kit-sold hook extended by sale_purchase_stock.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: exact valuation results per scenario (only test names/setups were reviewed, not every assertion).
- UNKNOWN — EVIDENCE INSUFFICIENT: portal/vendor-facing visibility of kit component moves.
- UNKNOWN — EVIDENCE INSUFFICIENT: cross-company effects of the sudo BoM lookup at purchase_mrp/models/purchase.py:111.

