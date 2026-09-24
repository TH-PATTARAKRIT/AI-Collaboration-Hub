# SMEsPlus Community19 — G05-G08 RED TEAM A1 Static Delta R4

**Date:** 2026-09-25 (Asia/Bangkok)  
**Lane:** A1 Source Evidence only  
**Stations:** G05 INVENTORY / G06 MANUFACTURING / G07 PURCHASE / G08 SALES  
**Question Gate:** WAIT QUESTION for all four stations  
**Downstream:** NO A2 / NO Reconciliation / NO A3 / NO MASTER  
**Formal Coverage:** PROHIBITED until Canonical Function-ID denominator is Boss-frozen

## 1. Roster reconciliation delta

The governed group counts remain G05=14, G06=12, G07=9, G08=31. The controlled mapping pointer remains `GROUP_STRUCTURE_V2_CORE.tsv`, SHA-256 `203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`.

This run independently checked the current `SMEsPlus` branch recursive Git tree. The row-level `GROUP_STRUCTURE_V2_CORE.tsv` is not present in that branch. The Community19 root contains the A1 lane, GMVQ lane, and Community Master Register manifest/hash only; the referenced workbook itself is not stored there. Google Drive exact-name search for `SMEsPlus_Odoo19_Community_Master_Register_V1.00` returned no accessible result. The authorized desktop source device was unavailable during the roster-recovery attempt. Therefore exact remaining technical membership is still OPEN and no module name is inferred.

`CURRENT-SOURCE PACKAGE RE-ANCHOR PENDING`

## 2. Question Gate re-check

The current governed GitHub `COMMUNITY19/GMVQ` root still contains only `G01_PLATFORM_BASE/` plus the standing/overnight GMVQ governance documents. There is no governed/frozen G05, G06, G07 or G08 question-bank directory. Each station therefore remains `A1 ACTIVE -> WAIT QUESTION`. No QID was authored or answered.

## 3. G05 INVENTORY — static UI/controller/test surface delta

Verified Odoo 19.0 public source anchors:

- `addons/stock/views/stock_picking_views.xml` — blob `15133fbc2c3b37542c958c96d8e3066a822504e5`
- `addons/stock/views/stock_quant_views.xml` — blob `6e7ac080fd557ff55e67120b334a6c7d6ad4ef57`
- `addons/stock/views/stock_menu_views.xml` — blob `6eeabeeddb8612ee5d5a4a32c4c41af84f003b7d`
- `addons/stock/controllers/main.py` — blob `96a289c690e7744d3150b4991296bc80e928e9f6`

Static evidence exposes transfer actions including reserve/unreserve, confirm, validate, print, return, cancel, scrap, package/reception/traceability actions and detailed operations. Inventory adjustment surfaces expose apply/reset/clear/count/relocate/history/orderpoint actions. Menus explicitly expose warehouse management, transfers, adjustments, procurement, configuration and inventory control. The stock-owned HTTP surface includes `/stock/<string:output_format>/<string:report_name>` with authenticated user access. The `stock/tests` directory contains 28 Python test modules (excluding `__init__.py`), including multicompany, procurement-rule, inventory, quant, stock-flow, lot, orderpoint, return-picking and warehouse tests.

A1 limit: static buttons/routes/tests prove source surfaces only; they do not prove runtime visibility, authorization, configuration or successful execution.

## 4. G06 MANUFACTURING — static UI/test surface delta

Verified Odoo 19.0 public source anchors:

- `addons/mrp/views/mrp_production_views.xml` — blob `97f55f955cc49daef24b6bb0dd1db1adeb80cdf0`
- `addons/mrp/views/mrp_workorder_views.xml` — blob `1ef4363f4864fa081e24d55456a443a17afe0edc`
- `addons/mrp/views/mrp_views_menus.xml` — blob `6b0a9e934195fbedbc028a022dd51459878edd98`

Static MO actions include plan/unplan, reserve/unreserve, confirm, start, cancel, mark done, unbuild, scrap, split, merge, lock/unlock, produce, serial allocation, BoM generation/update and overview/report actions. Workorder surfaces expose start, pause/pending, finish and scrap/wizard actions. Menus expose manufacturing, planning, BoM, reporting and configuration. No `addons/mrp/controllers` directory is present at the public 19.0 module path; this is a path-level static finding only, not a claim that Manufacturing has no externally reachable behavior through dependencies. The `mrp/tests` directory contains 22 Python test modules, including BoM, backorder, multicompany, procurement, traceability, unbuild and multistep-manufacturing tests.

## 5. G07 PURCHASE — static UI/controller/test surface delta

Verified Odoo 19.0 public source anchors:

- `addons/purchase/views/purchase_views.xml` — blob `b9e6edb600509e0ff97866e18d533fef26d1ad36`
- `addons/purchase/controllers/portal.py` — blob `874e5e519a8ac786521b7dc7024b4600dfd8889c`

Static actions expose RFQ send, confirm, approve, acknowledge, draft/reset, print quotation/PO, cancel, lock/unlock, bill matching, vendor-bill view, comparison, catalog and invoice creation. Purchase menus expose suppliers, products, RFQs, purchase orders and configuration surfaces. Portal routes include `/my/rfq`, `/my/purchase`, purchase-order detail/update and EDI download endpoints; access semantics are explicitly declared in source per route. The `purchase/tests` directory contains 11 Python test modules, including access-rights, purchase flow, invoices, downpayment, catalog and reports.

## 6. G08 SALES — static UI/controller/test surface delta

Verified Odoo 19.0 public source anchors:

- `addons/sale/views/sale_order_views.xml` — blob `a1295bbf53fea8980f44e3241db9c178dd87ed23`
- `addons/sale/views/sale_menus.xml` — blob `c0374876006c434971e16b1ba29f89ff4c644ebb`
- `addons/sale/controllers/portal.py` — blob `181e72142b45849d356c98a877e4a03165617b0f`
- `addons/sale/controllers/product_configurator.py` — blob `238c0cea049869cb78a49e95f88ae6f1f6101918`
- `addons/sale/controllers/combo_configurator.py` — blob `79a35961a70a83a6cb9e99ec2b2fa9391d279d8a`

Static Sales actions expose quotation send, confirm, cancel, draft, lock/unlock, payment capture/void, preview, invoice view, price/tax update, catalog and discount/down-payment actions. Menus expose quotations, orders, invoicing, products, pricelists, reporting, configuration and payment surfaces. Portal routes include `/my/quotes`, `/my/orders`, order detail, accept, decline, document download, EDI download and transaction endpoints. Authenticated JSON-RPC configurator surfaces include `/sale/product_configurator/get_values`, `/sale/combo_configurator/get_data` and `/sale/combo_configurator/get_price`; the inspected configurator routes declare user authentication and read-only semantics where shown in source. The `sale/tests` directory contains 32 Python test modules, including access-rights, credit-limit, payment-flow, sale-order, invoicing, tax/downpayment and controller tests.

## 7. RED TEAM disposition

The A1 surface map is materially deeper for all four verified anchors: source now covers model/lifecycle evidence from prior rounds plus explicit UI actions/menus, module-owned controller surfaces and test-evidence inventory. This increases static understanding only; it does not establish Runtime Reachability.

| Station | Current state | Blocking gate |
|---|---|---|
| G05 INVENTORY | A1 ACTIVE — deeper static delta verified | WAIT QUESTION + exact roster |
| G06 MANUFACTURING | A1 ACTIVE — deeper static delta verified | WAIT QUESTION + exact roster |
| G07 PURCHASE | A1 ACTIVE — deeper static delta verified | WAIT QUESTION + exact roster |
| G08 SALES | A1 ACTIVE — deeper static delta verified | WAIT QUESTION + exact roster |

No Evidence = No Progress. Source Presence != Runtime Reachability. No Formal Coverage or Research-Complete claim is made.
