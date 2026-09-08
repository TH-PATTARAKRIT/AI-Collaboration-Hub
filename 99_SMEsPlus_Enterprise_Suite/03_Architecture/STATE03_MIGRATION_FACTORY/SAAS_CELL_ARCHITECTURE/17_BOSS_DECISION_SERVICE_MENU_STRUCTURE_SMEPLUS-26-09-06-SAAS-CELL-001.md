# BOSS DECISION — SERVICE MENU STRUCTURE

Session: SMEPLUS-26-09-06-SAAS-CELL-001
Date: 2026-09-08
Status: APPROVED DIRECTION / DETAIL DESIGN PENDING
Boss: Sole Final Approver

## 1. Approved Naming

- Canonical English / Default UI: `Service`
- Thai controlled localization: `บริการ`

## 2. Approved Scope

Service means customer-facing service operations. It is not internal equipment maintenance.

Approved candidate submenu structure:

1. Service Requests
2. Service Orders
3. Scheduling & Dispatch
4. Field Service
5. Service Contracts
6. Warranty & Entitlements
7. Customer Equipment
8. Parts & Materials
9. Service Billing
10. SLA & Escalations
11. Service Knowledge
12. Reports

## 3. Semantic Boundaries

- `Maintenance` = internal operational maintenance of company-used equipment.
- `Service` = service delivered to customers.
- `Service Request` = customer or internal service demand/request.
- `Service Order` = authorized service execution order.
- `Work Order` remains reserved for Manufacturing execution.

## 4. Cross-Domain Traceability

Service must remain traceable to Sales, Equipment, Inventory, Purchase, Quality, Accounting/Invoicing and Finance where applicable.

Reference lifecycle:

`Customer / Product / Warranty -> Service Request -> Service Order -> Scheduling / Field Service -> Parts / Labor / External Service -> Billing Request -> Accounting/Invoicing -> Finance Settlement -> Reports`

## 5. Shared Source-of-Truth Rules

- Parts inventory comes from Inventory source facts.
- External service cost comes from Purchase/AP source facts.
- Service determines billable facts; Accounting/Invoicing creates the accounting/legal invoice.
- Service reports must reconcile to source transactions and preserve drill-down lineage.

Principle:

`Different Reports, Same Business Facts.`

## 6. Customer Equipment

Customer Equipment is an operational identity under the broader Equipment concept, with ownership classification such as company-owned, customer-owned, rental, leased or third-party.

## 7. Knowledge Boundary

Service Knowledge may capture troubleshooting and verified service resolutions. Promotion into the enterprise Knowledge of Truth requires controlled verification and approval.

## 8. Governance

This approval does not authorize Team C implementation or production deployment.

No Evidence = No Progress.
Never Skip Gate.
Boss remains sole Final Approver.
