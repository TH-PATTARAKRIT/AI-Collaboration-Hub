# Boss Ruling — SMEPLUS-26-09-04-INV-MTI-D02-AUTHORIZATION-GRANULARITY-001

## 1. Ruling Identity

Project: SMEsPlus ENTERPRISE SUITE
Workstream: Inventory Deep Research R4 / Multi-Tenant Invariant Set
Decision ID: MTI-D-02
Decision Topic: Authorization Granularity
Ruling Date: 2026-09-04
Ruling Authority: Boss
Status: BOSS RULED

## 2. Boss Ruling

Boss approves MTI-D-02 as:

`Company + Warehouse + Operation-Type`

This is the required authorization granularity for Inventory-side SaaS isolation and operational control.

## 3. Binding Interpretation

Inventory permission and execution context must be controlled by all applicable dimensions below:

1. Tenant / Company context
2. Warehouse context
3. Operation-Type context

A user, role, automation, report, import, API, scheduler, or handoff may not rely on company-only authorization when warehouse-level and operation-type-level restriction is required by the business action.

## 4. Core Control Rules

1. A tenant/company must never see, select, search, report, infer, or operate another tenant/company's inventory records.
2. A user authorized for one warehouse is not automatically authorized for every warehouse in the same company.
3. A user authorized for one operation type is not automatically authorized for every operation type in the same warehouse.
4. Operation Type does not replace Company or Warehouse context.
5. Warehouse does not replace Company context.
6. Company context does not replace Tenant isolation.
7. Inventory reports, valuation views, replenishment views, adjustments, transfers, scrap, landed cost flows, scheduler actions, and stock movement history must preserve the same authorization context.
8. Background jobs and system automation must carry explicit tenant/company/warehouse/operation-type context when executing inventory actions.

## 5. Domain Examples

Examples of operation-type-specific authorization include, but are not limited to:

- Receipt
- Delivery
- Internal Transfer
- Inventory Adjustment
- Scrap
- Replenishment
- Landed Cost review/action
- Scheduler-controlled replenishment or reservation actions

## 6. Relationship To MTI-D-01

This ruling must be read together with MTI-D-01:

- MTI-D-01: Product Master Scope = Option B, tenant/company-scoped product identity
- MTI-D-02: Authorization Granularity = Company + Warehouse + Operation-Type

Together, these rulings mean product identity and inventory operations must remain isolated by tenant/company, then further constrained by warehouse and operation type where actions require operational control.

## 7. Non-Authorization

This ruling is not an authorization for:

- Development
- Team B coding
- Team C build
- Merge to canonical branch
- Production release
- Final Gate PASS

## 8. Downstream Instruction

All downstream Inventory v2.0, R4 blocker remediation, AAS+, PMO, design, and proof prompts must carry this ruling verbatim or cite this file directly.

If any downstream design cannot prove Company + Warehouse + Operation-Type enforcement, the item must remain HOLD.
