# SMEsPlus Community19 — G05-G08 A1 Parallel Static Intake V1.00

**Date:** 2026-09-24  
**Mode:** A1 SOURCE EVIDENCE ONLY  
**Stations:** G05 INVENTORY / G06 MANUFACTURING / G07 PURCHASE / G08 SALES  
**Question Gate:** CLOSED — governed G05-G08 question-bank directories are not present in the current Community19 GMVQ root  
**Downstream:** NO A2 / NO Reconciliation / NO A3 / NO MASTER for these groups until the exact governed question batch is present, verified, and eligible/frozen  
**Formal Coverage:** NOT AUTHORIZED

## 1. Governance and roster control

Current Group Structure V2 evidence establishes these governed counts:

| Group | Name | Governed module count | A1 station status |
|---|---|---:|---|
| G05 | INVENTORY | 14 | ACTIVE — anchor extracted / roster reconciliation open / WAIT QUESTION |
| G06 | MANUFACTURING | 12 | ACTIVE — anchor extracted / roster reconciliation open / WAIT QUESTION |
| G07 | PURCHASE | 9 | ACTIVE — anchor extracted / roster reconciliation open / WAIT QUESTION |
| G08 | SALES | 31 | ACTIVE — anchor extracted / roster reconciliation open / WAIT QUESTION |

The measured Group Structure V2 mapping artifact is `GROUP_STRUCTURE_V2_CORE.tsv`, SHA-256 `203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`. The full TSV row set is not currently reachable through the connected evidence surfaces in this run. Therefore exact remaining technical membership is **not guessed**. Only verified source anchors are extracted below while canonical roster recovery remains open.

The current Community19 A1 index is a 247-module study scope. Module counts are planning/control counts only and are not a Canonical Function-ID denominator.

## 2. Source re-anchor status

The authoritative local Community19 package baseline (`19.0-20260921`) is not currently reachable through the authorized desktop source root. For reproducible static progress, this run re-anchored verified source anchors against public Odoo `19.0` LGPL source on GitHub.

This is valid A1 source/static evidence but **does not establish byte identity with the local `19.0-20260921` package**. Status remains:

`CURRENT-SOURCE PACKAGE RE-ANCHOR PENDING`

Source Presence != Runtime Reachability.

---

# 3. G05 INVENTORY — verified source anchor `stock`

## 3.1 Manifest / dependency / load surface

- Module: `stock` — Inventory, version `1.1`, LGPL-3.
- Direct dependencies: `product`, `barcodes_gs1_nomenclature`, `digest`.
- Static data surface includes Inventory security/ACL, stock data, sequences, traceability, mail templates, reports, menus, configuration and extensive wizards.
- Static UX surfaces include lots, scraps, quants, warehouses, move lines, moves, pickings, operation types, products, locations, orderpoints, storage categories, rules, packages and forecast views.
- Static test surfaces include tours and unit-test assets.
- Pre-init, post-init and uninstall hooks are declared.

## 3.2 Principal entities / identity / lifecycle

`stock.move` is a principal movement entity with explicit identity and handoff fields including company, product, source/destination/final location, picking, warehouse, stock rule, orderpoint, routes, owner, lot/serial references, packages and source document origin.

Static lifecycle:

`draft -> waiting / confirmed / partially_available / assigned -> done`

with `cancel` as cancellation state.

Additional static mechanisms:

- procurement mode: `make_to_stock` vs `make_to_order`;
- chained movements: original/destination move relationships;
- return lineage: origin-returned and returned-move relationships;
- cancellation propagation control;
- separate demand, moved quantity, forecast availability, forecast date and reservation date;
- inter-company final-location handling appears in destination computation.

## 3.3 Security / company isolation

- Inventory User and Administrator privileges are declared.
- Optional groups cover multi-location, multi-warehouse, lot/serial, packages, push/pull flows, owners, warnings, delivery signature and reception report.
- Record rules constrain picking, operation type, putaway, warehouses, moves, orderpoints, scrap and reports to active companies.
- Selected shared master/operational records allow `company_id=False`, including lots, locations, move lines, quants, stock rules, routes, packages and storage categories.

## 3.4 Gaps

- Remaining 13 G05 technical members are not asserted without canonical TSV row evidence.
- Inventory valuation/accounting is not inferred from `stock` alone; bridge modules such as stock/account extensions require explicit roster/source verification.
- Runtime reservation, negative-stock behavior, valuation and posting are not proven by A1.

---

# 4. G06 MANUFACTURING — verified source anchor `mrp`

## 4.1 Manifest / dependency / load surface

- Module: `mrp` — Manufacturing, version `2.0`, LGPL-3.
- Direct dependencies: `product`, `stock`, `resource`.
- Static surfaces include MRP security/ACL, manufacturing data, mail templates, quantity-change, workcenter-block, insufficient-stock, backorder, consumption-warning, split and serial-number wizards.
- Views cover Manufacturing Orders, Work Orders, Workcenters, BoMs, routing, stock moves, orderpoints, warehouses, pickings, stock rules, unbuild, scrap and settings.
- Reports include BoM structure, MO overview, production/workorder templates and stock-related reports.
- Pre-init, post-init and uninstall hooks plus tours/unit tests are declared.

## 4.2 Principal entities / inheritance / lifecycle

- `mrp.production` is the Manufacturing Order entity.
- It inherits `mail.thread`, `mail.activity.mixin` and `product.catalog.mixin`.
- Core static links include product, BoM, component and finished-product locations, picking type, lots/serials, raw/finished/byproduct stock moves, workorders, scrap, unbuild, orderpoint and generated destination moves.
- `company_id` is required; many business links use `check_company=True`.

Static Manufacturing Order lifecycle:

`draft -> confirmed -> progress -> to_close -> done`

with `cancel` as cancellation state.

Separate readiness state:

`confirmed / assigned / waiting`

Consumption control is explicit as `flexible / warning / strict`.

## 4.3 Security / company isolation

- Manufacturing User and Administrator privileges are declared; Manufacturing User implies Inventory User.
- Optional groups cover workorder operations/routings, byproducts, unlocked-by-default, reception report and workorder dependencies.
- Record rules constrain Manufacturing Orders, unbuild, workorders and productivity to active companies.
- Workcenters, BoMs, BoM lines, byproducts and routing workcenters may also be shared with `company_id=False`.

## 4.4 Cross-module handoff and gaps

- `mrp` directly depends on `stock`; raw consumption and finished output are represented through stock moves.
- This is a verified static Manufacturing -> Inventory handoff surface, not runtime proof.
- Remaining 11 G06 technical members are not asserted without canonical TSV row evidence.
- Cost absorption/accounting effects, subcontracting, maintenance/repair ownership and optional bridges require exact roster verification before attribution to G06.

---

# 5. G07 PURCHASE — verified source anchor `purchase`

## 5.1 Manifest / dependency / load surface

- Module: `purchase` — Purchase, version `1.2`, LGPL-3.
- Direct dependency: `account`.
- Static surfaces include Purchase security/ACL, accounting move views, purchase data, scheduled reminder job, reports, Purchase/Bill matching/settings/product/vendor views, portal templates, RFQ/PO templates, analytic views, bill-to-PO wizard and tours.

## 5.2 Principal entity / inheritance / lifecycle

`purchase.order` inherits portal, product catalog, mail thread/activity and account document import capabilities.

Core static fields include vendor, vendor reference, source, order deadline, confirmation date, destination/dropship address, currency, fiscal position, tax country, payment terms, incoterm, buyer, company, invoice linkage/status and expected arrival.

Static lifecycle:

`draft (RFQ) -> sent -> to approve -> purchase`

with `cancel` as cancellation state.

Confirmed-order locking and vendor acknowledgement are explicit static concepts.

A company/product constraint rejects purchase lines whose product company is not accessible to the quotation company/branch context.

## 5.3 Background / portal / security

- Daily root-user cron `Purchase reminder` calls `_send_reminder_mail()`.
- Portal routes expose RFQs, Purchase Orders, document view/report, planned-date update and EDI download, with document-access checks on public order routes.
- Purchase User and Administrator privileges are declared.
- Multi-company rules constrain orders, lines and reports.
- Portal visibility is constrained to the commercial-partner subtree.
- Purchase-user accounting visibility is restricted to incoming vendor documents (`in_invoice`, `in_refund`, `in_receipt`).

## 5.4 Gaps

- Remaining 8 G07 technical members are not asserted without canonical TSV row evidence.
- Goods receipt/dropship/subcontracting stock execution must not be inferred from the base `purchase` module alone; bridge-module membership must be verified first.
- Runtime approval thresholds, receipt creation and posting are not proven by A1.

---

# 6. G08 SALES — verified source anchor `sale`

## 6.1 Manifest / dependency / load surface

- Module: `sale` — Sales, version `1.2`, LGPL-3.
- Direct dependencies: `sales_team`, `account_payment`, `utm`.
- Static surfaces include ACL/groups/rules, invoice and sales reports, sequences, mail/template/subtype data, scheduled jobs, configuration, advance invoice, mass cancel, payment-link, discount and settings wizards, sale/order-line/account/team/activity/payment/product/partner/portal/UTM views, plus backend/frontend/tour/unit-test assets.
- Post-init hook is declared.

## 6.2 Principal entity / inheritance / lifecycle

`sale.order` inherits portal, product catalog, mail thread/activity, UTM and account document import capabilities.

Company checking is enabled automatically. A static SQL constraint requires a confirmation date for confirmed Sales Orders.

Static lifecycle:

`draft (Quotation) -> sent -> sale`

with `cancel` as cancellation state.

Core static surfaces include customer, invoice address, delivery address, company, salesperson/team, journal, fiscal position, payment terms/method, pricelist, currency/rate, order lines, tax/amounts, invoice linkage/status, signature, online payment/prepayment and UTM attribution.

## 6.3 Background / portal / security

- Daily root-user scheduled jobs exist for sending ready invoices and pending Sales emails; both are inactive by default in source data.
- Portal routes expose quotations, orders and public token-protected order pages; portal domains constrain records by the user's commercial-partner subtree and business state.
- Sales order, order line and analysis rules are multi-company constrained.
- Salesperson-level personal/all rules are explicit for orders, lines, reports and outbound invoices.
- Wizard ownership and Sales Manager activity-plan rules are explicit.

## 6.4 Gaps

- Remaining 30 G08 technical members are not asserted without canonical TSV row evidence.
- `sale` itself does not prove warehouse delivery execution; Sales -> Inventory, Sales -> Project and Sales -> Manufacturing bridges require exact governed membership and separate source extraction.
- Runtime signature, payment, invoicing and delivery behavior is not proven by A1.

---

# 7. Cross-station static reconciliation

| Handoff | Static evidence in this run | A1 conclusion |
|---|---|---|
| G06 Manufacturing -> G05 Inventory | `mrp` directly depends on `stock`; MO links raw/finished/byproduct stock moves | VERIFIED STATIC HANDOFF SURFACE |
| G07 Purchase -> Accounting | `purchase` directly depends on `account`; PO links supplier bills and tax/payment configuration | VERIFIED STATIC HANDOFF SURFACE |
| G08 Sales -> Accounting/Payment | `sale` depends on `account_payment`; SO links journal, invoices and payment transactions | VERIFIED STATIC HANDOFF SURFACE |
| G08 Sales -> G05 Inventory | Base `sale` source does not itself establish the complete delivery bridge | BRIDGE MODULE ROSTER/SOURCE REQUIRED |
| G07 Purchase -> G05 Inventory | Base `purchase` source does not itself establish the complete receipt bridge | BRIDGE MODULE ROSTER/SOURCE REQUIRED |
| G06 Manufacturing -> Accounting | Not established by base `mrp` alone | BRIDGE MODULE ROSTER/SOURCE REQUIRED |

A material control finding is therefore retained: business lifecycles cross module boundaries. Missing extension/bridge roster evidence must remain explicit rather than being replaced by inferred ownership.

# 8. Question Gate and downstream disposition

Current Community19 GMVQ root contains `G01_PLATFORM_BASE` plus governance/order documents, but no governed G05, G06, G07 or G08 question-bank directory. Example/historical question text is not a frozen eligible bank.

Therefore:

| Group | A1 | Question Gate | A2 | Reconciliation | A3 | MASTER |
|---|---|---|---|---|---|---|
| G05 | ACTIVE | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| G06 | ACTIVE | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| G07 | ACTIVE | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| G08 | ACTIVE | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |

No question set was invented in this run.

# 9. Evidence-state conclusion

- Verified delta exists for all four stations at the source/static anchor level.
- Exact full roster for each group remains open because the canonical TSV rows are not currently accessible.
- Local package re-anchor remains pending.
- Runtime/configuration proof was not executed.
- Formal Coverage remains prohibited until the Canonical Function-ID denominator is Boss-frozen.

**Disposition:** `A1 ACTIVE / VERIFIED STATIC DELTA / WAIT QUESTION / NO DOWNSTREAM EXECUTION`.
