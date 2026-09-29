# Source Map (candidate) — `purchase_requisition_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_requisition_stock` |
| Display name | Purchase Requisition Stock |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d1f03d5ed2e7d662` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_requisition_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `purchase_requisition`, `purchase_stock`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (7): `purchase.requisition.create.alternative`, `purchase.order`, `purchase.order.line`, `stock.rule`, `stock.move`, `purchase.requisition`, `purchase.requisition.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `purchase.requisition.create.alternative`, `purchase.order`, `purchase.order.line`, `stock.rule`, `stock.move`, `purchase.requisition`, `purchase.requisition.line`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 25 of 25 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: purchase_requisition_stock
Source revision: 19.0.post20260921 (Odoo 19.0 Community). Pointers `module/path:LINE`; (TEST) = test-derived.
Manifest: "Purchase Requisition Stock"; depends purchase_requisition + purchase_stock; `auto_install: True` (purchase_requisition_stock/__manifest__.py:5,9,17). Bridge; CORE whenever purchase agreements and stock-purchase are both installed. No setting or group toggles it.

## A. Capabilities
1. Warehouse and receiving operation type on a purchase agreement; operation type is mandatory and defaults to the first receipt type of a warehouse of the current company (warns via the warehouse-redirect warning if none) (purchase_requisition_stock/models/purchase_requisition.py:10-19). Field appears on the agreement form only with advanced-location group `stock.group_adv_location` and is read-only after draft (purchase_requisition_stock/views/purchase_requisition_views.xml:9-11). A default warehouse (the main demo/standard warehouse xml-id `stock.warehouse0`) is stored as a database default for new agreements (purchase_requisition_stock/data/purchase_requisition_stock_data.xml:4-7, noupdate).
2. Automatic replenishment (reordering rules, make-to-order buy rules) that picks blanket-order vendor prices: POs created by procurement carry the agreement, vendor reference = agreement name and agreement currency (purchase_requisition_stock/models/stock.py:10-17); procurements are grouped into one PO per agreement, never mixing agreements (:19-25). (TEST) two blanket orders on different MTO products produce two POs (purchase_requisition_stock/tests/test_purchase_requisition_stock.py:98-186); price selection between a normal vendor price and a blanket-order price follows vendor-price sequence (:11-96).
3. Downstream-move link on agreement lines, copied to the RFQ line so a demand can be traced through an agreement (purchase_requisition_stock/models/purchase_requisition.py:22-30).
4. Alternatives enriched with stock data: vendor on-time-delivery (OTD) percentage shown per alternative PO and per compare line (purchase_requisition_stock/models/purchase.py:10-18,30; views purchase_requisition_stock/views/purchase_views.xml:8-11,14-22; hidden when rate is negative, i.e. no history).
5. Creating an alternative RFQ copies operation type, stock references, and per-line downstream moves from the origin PO (purchase_requisition_stock/wizard/purchase_requisition_create_alternative.py:10-24).

## B. Objects, relationships, lifecycle
- Extends purchase.requisition (warehouse, operation type), purchase.requisition.line (downstream move), purchase.order / line (OTD fields; agreement onchange), stock.rule (PO preparation and grouping), stock.move (upstream-document resolution), create-alternative wizard.
- Choosing an agreement on a PO also sets the PO operation type from the agreement (purchase_requisition_stock/models/purchase.py:20-24).
- Upstream documents: for a stock move linked to agreement lines, the responsible party is the agreement and its buyer, ignoring agreements that are closed or cancelled; evaluated with elevated access so users without purchase rights can process the move (purchase_requisition_stock/models/stock.py:33-39).
- Lifecycle states are unchanged: agreement states in purchase_requisition (purchase_requisition/models/purchase_requisition.py:34-42), PO states in purchase (purchase/models/purchase_order.py:105-111), receipts in stock.
- Vendor price handoff: agreement-linked vendor prices are hidden from POs of other agreements but remain candidates when no order is given (procurement) (purchase_requisition/models/product.py:17-22); this module's stock rule then binds the resulting PO to that agreement (purchase_requisition_stock/models/stock.py:13-14).
- (TEST) alternative PO copies operation type, delivery address, product, quantity and is linked to origin (test_purchase_requisition_stock.py:188-233); the original PO ends cancelled when its alternatives are handled through the warning wizard (:188-233); in a two-step reception setup the confirmed alternative's receipt stays chained to the internal move and the original PO is cancelled (:235-302).

## C. Validations, automation, security, multi-company
- Only validation: operation type required on agreements (purchase_requisition_stock/models/purchase_requisition.py:17-19). Domains limit warehouse and operation type to the agreement's company (:16,19).
- Security: Stock Manager gets read and create (no write, no delete) on agreements and agreement lines (purchase_requisition_stock/security/ir.model.access.csv:2-3). Purchase-side rights and company record rules come from purchase_requisition (purchase_requisition/security/purchase_requisition_security.xml:4-14).
- Multi-company: default operation type search is restricted to the current company's warehouses (purchase_requisition_stock/models/purchase_requisition.py:11); PO operation type domain is owned by purchase_stock (purchase_stock/models/purchase_order.py:24).
- Automation: created through stock scheduler / reordering (TEST scheduler run creating the PO, :235-302); no cron defined in this module.

## D. Handoffs
- Inventory: receipts, routes, reordering owned by stock/purchase_stock (`_prepare_purchase_order` and `_make_po_get_domain` base: purchase_stock/models/stock_rule.py:326,358).
- Purchase: agreements and alternatives owned by purchase_requisition.
- Accounting: none in this module (bills/valuation via purchase_stock/account).
- Approval: none added; PO approval rules apply at PO confirmation (purchase/models/purchase_order.py:625-639,1251-1259).
- Vendor performance metric OTD comes from the vendor record (purchase_stock/models/purchase_order.py:34).

## E. Configuration that changes outcomes
- Warehouse/operation type on the agreement; vendor price sequence and minimum quantities (TEST :56-77); currency of agreement overrides PO currency when set (purchase_requisition_stock/models/stock.py:15-16); multi-step reception setting of the warehouse (TEST :235-302); group `stock.group_adv_location` for showing the field.

## F. Effective extension path
- Extends objects of purchase_requisition (requisition, line, wizard), purchase_stock (rule, PO, move). Other Community modules extending purchase.requisition / line: none besides this one; wizard extended also by purchase_requisition_sale. No Community module depends on purchase_requisition_stock.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: the test named for "group id" propagation (test_purchase_requisition_stock.py:304) was not read in depth; this revision's wizard carries stock references (`reference_ids`), not a procurement group.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when the default warehouse record is absent (data uses `stock.warehouse0`).
- UNKNOWN — EVIDENCE INSUFFICIENT: use of move_dest_id on agreement lines by any user-facing flow (only the field and copy are shown).

