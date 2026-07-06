# CANONICAL_DATA_MODEL.md

**Document ID:** SMEPLUS-26-07-05-001-CDM
**Phase:** 2.5 – Knowledge Consolidation & Enterprise Analysis
**Prepared by:** Claude, acting as Database Architect / Solution Designer
**Date:** 2026-07-05

## Purpose
Define the canonical entities requested for Phase 2.5 (Customer, Supplier, Company, Branch, Warehouse, Product, Inventory, Sales Order, Purchase Order, Invoice, Payment, Approval, Journal, Attachment, Audit) as **relationships only** — no column lists, no implementation, no source code. Every entity is grounded either in confirmed Odoo schema evidence or in the SMEsPlus SaaS Foundation FDS conceptual model; entities that exist only as a design intent (not yet in the schema) are marked **GAP**.

## Dependencies
`02_Functional_Design/02_Functional_Design/iTEST02_ERD_*.md`, `01_SaaS_Foundation/FDS/Domains/*.md`, `V2.0/.../Evidence_CSV/Dump_Table_Inventory.csv`.

## Source Evidence
Module-level ERDs extracted from the live PostgreSQL dump (`iTEST02_2026-06-14_14-41-19.dump`, 1,395 tables, 5,141 FK edges) plus the SaaS Foundation FDS conceptual data-entity tables ("Data Entities (Conceptual)" sections).

## Confidence Level
High for entities backed by direct schema evidence (Odoo core objects). Medium/GAP for SaaS Foundation platform-layer entities that are FDS-conceptual only (Tenant, Division, Module Registry, Subscription Plan) since these are Draft and not yet built.

## Known Gaps
See inline **GAP** markers per entity, and consolidated in §4.

## ⚠️ Clean Room Framing Notice (2026-07-06, per ADR-0006)

This document was originally written using Odoo's actual table/model names (`res_company`,
`account_move`, `sale_order`, `stock_move`, etc.) presented alongside the SMEsPlus canonical
entities, with wording like "maps to Odoo X — CONFIRMED." Per Boss's Clean Room Learning Directive
v2.0 (Policy A) and ADR-0006, this is reclassified: **the Odoo table/model names below are concept
origins only** — they show where an entity or relationship concept was observed and confirmed
against real usage, not a schema SMEsPlus adopts. SMEsPlus's actual schema is an independent
SQLAlchemy model design (per `TECHNOLOGY_STACK_STANDARD.md`), to be produced during Phase 3/4 SDS
work, informed by — but not copied from — the Odoo names retained below for traceability. Wherever
this document says a concept is "confirmed" or "MATCHED," read it as "the business need for this
entity/relationship is confirmed to be real and well-understood," not "this table is reused."

## Recommended Next Step
Database Design AI to formalize this canonical model into an ERD once FDS reaches Approved Baseline (per the existing blocker recorded in `SDS/ERD_FOUNDATION_v0.1.md`).

---

## 1. Platform / Foundation Layer (SMEsPlus-custom, above the Odoo base)

```
Tenant  [GAP — conceptual only, no table exists yet]
  └── Company [maps to Odoo res_company — CONFIRMED]
        └── Branch [SMEsPlus-custom entity — GAP, "not a stock Odoo concept" per FDS]
              └── Division [SMEsPlus-custom entity, optional — GAP]
```
- **Tenant → Company:** one Tenant has many Companies (conceptual; isolation boundary above Company). Evidence: `FDS_TENANT.md` §1 ("All Company, Branch, User, and business data ultimately belong to exactly one Tenant"). Evidence Matching confirms Company-level isolation exists in the real schema (`res_company`), but the Tenant-grouping layer above it does **not** exist yet (FR-FD-001 = PARTIAL, per `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md`).
- **Company → Branch:** one Company has many Branches; a Branch belongs to exactly one Company (BR-BRN-001). Evidence: `FDS_BRANCH.md`.
- **Branch → Division:** one Branch has zero or many Divisions; a Division belongs to exactly one Branch (BR-DIV-001, BR-DIV-002). Evidence: `FDS_DIVISION.md`.
- **Company/Branch → Warehouse:** a Branch has a default stock/location binding for Inventory (BRN-002 functional requirement). Evidence: `FDS_BRANCH.md` §2.

## 2. Party Entities

```
Customer/Supplier  →  maps to Odoo res_partner (single "partner" table for both roles, distinguished by flags)
```
- Odoo represents both **Customer** and **Supplier** as the same underlying partner concept (`res.partner`), differentiated by customer/vendor rank flags rather than separate tables. This is confirmed by the Sales/CRM and Inventory/Purchase ERDs, which both reference partner-linked foreign keys (`partner_id`) on `sale_order`, `purchase_order`, `crm_lead`, and `account_move`.
  Evidence: `iTEST02_ERD_Sales_CRM.md`, `iTEST02_ERD_Inventory_Purchase.md`, module inventory categories `Sales_CRM` (60 tables) and `Inventory_Purchase` (169 tables) in `iTEST02_module_inventory.csv`.
- **Customer → Sales Order:** one Customer (partner) has many Sales Orders.
- **Supplier → Purchase Order:** one Supplier (partner) has many Purchase Orders.
- **Customer/Supplier → Invoice:** one partner has many Invoices/Bills (both directions unified in Odoo's `account_move`, distinguished by move type).

## 3. Product & Inventory Entities

```
Product (PRODUCT_TEMPLATE / PRODUCT_PRODUCT)
  └── Stock Move (STOCK_MOVE) ──> Stock Picking (STOCK_PICKING) ──> Picking Type (STOCK_PICKING_TYPE)
  └── Warehouse (STOCK_WAREHOUSE) ──> Location (STOCK_LOCATION)
  └── Lot/Serial (STOCK_LOT)
```
- **Product Template → Product (variant):** one Product Template has many Product (variant) records — confirmed Odoo pattern (`product_template` → `product_product`).
  Evidence: `iTEST02_ERD_Inventory_Purchase.md`.
- **Warehouse → Location:** one Warehouse has many Locations (`stock_warehouse` → `stock_location`).
- **Product → Stock Move → Inventory (on-hand position):** Inventory is not a single table but the aggregate of `stock_move` / `stock_move_line` transactions against `stock_location`, filtered by product and warehouse — confirmed via FK edges in `iTEST02_ERD_Inventory_Purchase.md` (`STOCK_MOVE`, `STOCK_MOVE_LINE`, `STOCK_LOCATION`, `STOCK_WAREHOUSE`).
- **Warehouse → Reorder Rule:** `STOCK_WAREHOUSE_ORDERPOINT` links Warehouse + Product to a reorder policy.
- **Purchase Request Line → Product:** `PURCHASE_REQUEST_LINE` (OCA `purchase_request` module — confirmed MATCHED, FR-PUR-001) references Product for quantity/UoM/estimated price, feeding into the Purchase Order flow (§5).

## 4. Sales Entities

```
Sales Order (SALE_ORDER)
  └── Sales Order Line (SALE_ORDER_LINE) ──> Product
  └── CRM Lead (CRM_LEAD) [pre-sales origin, optional]
        └── CRM Team (CRM_TEAM)
```
- **CRM Lead → Sales Order:** a Lead may convert into a Sales Order (Odoo `crm_lead` → `sale_order` conversion flow); this is optional, not mandatory.
  Evidence: `iTEST02_ERD_Sales_CRM.md`.
- **Sales Order → Sales Order Line → Product:** standard header/line pattern.
- **Sales Order → Invoice:** an approved/confirmed Sales Order generates one or more customer Invoices (`account_move`, move type = out_invoice), consistent with the Order-to-Cash description in Purchase's mirror-image Procure-to-Pay flow.

## 5. Purchase Entities (fully evidenced end-to-end; Priority-1 active design)

```
Purchase Request (custom/OCA purchase_request)
  └── Purchase Request Line ──> Product
  └── RFQ [GAP — no existing implementation]
        └── Vendor Invitation [GAP]
        └── Vendor Response [GAP]
              └── Vendor Comparison [GAP]
                    └── Vendor Selection [GAP — approval object; level1/level2 fields OUT OF SCOPE per Boss 2026-07-02]
                          └── Purchase Order (PURCHASE_ORDER)
                                └── Purchase Order Line (PURCHASE_ORDER_LINE) ──> Product
                                └── Goods Receipt (STOCK_PICKING, type=incoming) [MATCHED — base flow]
                                      └── Vendor Bill (account_move, move type=in_invoice) [MATCHED — 2-way/3-way match]
```
- Every arrow above is grounded either in confirmed schema evidence (Purchase Order, Purchase Order Line, Goods Receipt, Vendor Bill — all MATCHED/PARTIAL per Evidence Matching) or explicitly marked GAP where the Evidence Matching Matrix v0.2 found no implementation (RFQ, Vendor Invitation, Vendor Response, Vendor Comparison, Vendor Selection).
  Evidence: `iTEST02_ERD_Inventory_Purchase.md` (schema-level), `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` (evidence-matching verdicts), `Purchase Module Functional Requirement Catalog v0.1.pdf` (process flow).
- **Purchase Order → Goods Receipt:** one PO has many Goods Receipts (Partial Receipt supported, BR-PUR-071).
- **Purchase Order + Goods Receipt → Vendor Bill:** 3-way match (PO ↔ Receipt ↔ Bill), BR-PUR-082.

## 6. Accounting Entities

```
Journal (ACCOUNT_JOURNAL)
  └── Journal Entry / Move (ACCOUNT_MOVE)
        └── Move Line (ACCOUNT_MOVE_LINE) ──> Account (ACCOUNT_ACCOUNT)
  └── Payment (ACCOUNT_PAYMENT) ──> Move (reconciliation link)
Invoice = a specialized Account Move (move_type constrains it to a customer/vendor invoice or bill)
```
- **Journal → Move:** one Journal (e.g., Sales, Purchases, Bank, Cash) has many Moves. Evidence: `iTEST02_ERD_Accounting_Finance.md`.
- **Move → Move Line → Account:** standard double-entry pattern; each Move has multiple debit/credit lines, each posted against one Chart-of-Accounts Account.
- **Payment → Move:** a Payment reconciles against one or more Moves (`account_payment` → `account_move` via `move_id`), and payments may pair as internal transfers (`paired_internal_transfer_payment_id`).
- **Invoice** is not a separate canonical entity in the real schema — it is a Move with `move_type` constrained to `out_invoice`/`in_invoice` (customer invoice / vendor bill). This directly informs the Canonical Data Model: do not model "Invoice" as a standalone SMEsPlus entity; model it as a specialization of Journal Entry/Move, consistent with the underlying Odoo implementation this platform is being built on.

## 7. Approval Entity (cross-cutting, reusable workflow — SaaS Foundation layer)

```
Approval Workflow [SMEsPlus-custom reusable engine — Draft FDS, partially GAP]
  └── Approval Step
        └── Approver Assignment
  ← attaches to: Purchase Request, RFQ→PO chain, Vendor Selection, Leave Request, Document, (any module transaction)
```
- Approval is explicitly designed as a **cross-module, reusable object** — not owned by any single business module. Evidence: `FDS_APPROVAL.md` §1 ("ระบบต้องสามารถนำกลับไปใช้ซ้ำ (Reusable Workflow Engine) ได้โดยไม่ต้องพัฒนา Workflow ใหม่ในแต่ละ Module" — the system must be reusable without building a new workflow per module).
- **Approval → any transactional entity:** one-to-many; a single transaction (Purchase Request, Vendor Selection, PO, Leave Request, Document) can have many Approval Steps forming its approval history.

## 8. Journal, Attachment, Audit (Supporting / Cross-Cutting Entities)

```
Attachment  ← attaches to: any transactional entity (Purchase Request, RFQ, Vendor Response, PO, Document)
Audit Log   ← records: status changes and field changes across all modules
```
- **Attachment:** per BR-PUR-101, "Attachments and evidence must be retained" — Attachment is a supporting entity referenced by many transactional entities (many-to-one from Attachment's perspective, one-to-many from the transaction's perspective). Real schema evidence: Odoo's generic `ir_attachment` model is referenced across many FK edges in the dump (e.g. `fleet_vehicle_mail_compose_message_ir_attachments_rel`), confirming this is implemented as a shared, polymorphic-style attachment mechanism rather than per-module tables.
  Evidence: `iTEST02_module_inventory.csv` (Manufacturing_Maintenance sample tables reference `ir_attachments` relation tables).
- **Audit Log:** every module must send events to a central Audit Service (BR-PUR-100, "every status change must generate an Audit Trail entry"; `FDS_AUDIT.md` — "ทุก Module ต้องส่ง Event มายัง Audit Service"). This is currently a **GAP** at the platform layer (no confirmed dedicated audit-log table found in the Evidence Matching pass) but Odoo's native `mail.message`/tracking mechanism provides partial coverage already in the base schema.
  Evidence: `FDS_AUDIT.md`, `FDS_REPORTING.md` BR-REP-002 (audit export must respect the same access scoping as the audit trail viewer).

---

## 9. Consolidated Relationship Diagram (Text Form)

```
Tenant [GAP]
 └─ Company (res_company)
     └─ Branch [custom]
         └─ Division [custom, optional]
     └─ Customer/Supplier (res_partner)
         ├─ Sales Order → Sales Order Line → Product
         │        └─ Invoice (account_move, out_invoice)
         └─ Purchase Order → Purchase Order Line → Product
                  └─ Goods Receipt → Vendor Bill (account_move, in_invoice)
     └─ Product (product_template/product_product)
         └─ Warehouse → Location → Stock Move (Inventory position)
     └─ Journal → Move (Journal Entry) → Move Line → Account
         └─ Payment (reconciles to Move)
     └─ Approval Workflow (cross-cutting; attaches to any transaction above)
     └─ Attachment (cross-cutting; attaches to any transaction above)
     └─ Audit Log (cross-cutting; records changes across all of the above) [partial GAP]
```

## 10. Known Gaps (Entity-Level)

| Entity | Status | Reason |
|---|---|---|
| Tenant | GAP | Conceptual only; no table exists above Company (FR-FD-001 = PARTIAL) |
| Branch, Division | GAP (schema) / Defined (FDS) | Custom entities, fully specified in FDS but not yet built |
| RFQ, Vendor Invitation, Vendor Response, Vendor Comparison, Vendor Selection | GAP | Confirmed no existing implementation in the 1,395-table schema (Evidence Matching v0.2) |
| Subscription Plan, Module Registry | GAP | FDS-conceptual only, explicitly flagged "no existing evidence" in `FDS_SUBSCRIPTION.md`, `FDS_MODULE.md` |
| Audit Log (dedicated platform table) | Partial GAP | Odoo native `mail.message`/tracking gives partial coverage; no confirmed dedicated cross-module audit table |
| Invoice as standalone entity | Not a gap — modeling clarification | Should be modeled as a Move specialization, not a separate entity, to match the underlying Odoo implementation |
