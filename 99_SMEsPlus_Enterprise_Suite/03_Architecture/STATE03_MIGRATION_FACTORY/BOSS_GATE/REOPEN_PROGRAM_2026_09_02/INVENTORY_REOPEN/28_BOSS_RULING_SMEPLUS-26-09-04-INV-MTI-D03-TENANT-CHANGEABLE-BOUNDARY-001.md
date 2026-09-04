# Boss Ruling — SMEPLUS-26-09-04-INV-MTI-D03-TENANT-CHANGEABLE-BOUNDARY-001

## 1. Ruling Identity

Project: SMEsPlus ENTERPRISE SUITE
Workstream: Inventory Deep Research R4 / Multi-Tenant Invariant Set
Decision ID: MTI-D-03
Decision Topic: Tenant-Changeable Boundary
Ruling Date: 2026-09-04
Ruling Authority: Boss
Status: BOSS RULED

## 2. Boss Ruling

Boss agrees with the AAS+ recommendation:

`Platform-owned Core + Tenant Config Overlay`

For the shared SaaS pool, the platform core remains centrally owned. Tenant/company-specific behavior must be expressed through controlled configuration and master data overlays only.

## 3. SaaS Pool Boundary

In the shared SaaS pool, customer-specific setup may include controlled Inventory master/configuration records such as:

- Warehouse
- Location
- Route
- Rule
- Operation Type
- Putaway Rule
- Reordering Rule
- Storage Category
- Product Category
- Unit of Measure Category
- Barcode Nomenclature
- Other approved Inventory configuration/master records

The shared SaaS pool must not allow customer-specific changes that fork platform source code, database schema, posting engine behavior, authorization engine behavior, immutable event logic, or cross-tenant isolation rules.

## 4. Private Company Option

If a customer has extensive or unusual requirements that cannot be safely handled inside the shared SaaS pool, the customer may be separated into a `Private Company` operating model within the system.

The Private Company option may be opened when required, but it must pass controlled governance before use.

Private Company is not a bypass for evidence, authorization, audit, tenant isolation, or Boss approval.

## 5. Binding Control Rules

1. Platform-owned core logic remains centrally controlled.
2. Tenant/company configuration must not modify platform source logic.
3. Tenant/company configuration must not weaken MTI-D-01 product isolation.
4. Tenant/company configuration must not weaken MTI-D-02 Company + Warehouse + Operation-Type authorization.
5. Shared SaaS pool customization must remain configuration-led, evidence-backed, reversible where applicable, and auditable.
6. Private Company separation requires explicit Gate record, evidence, and Boss ruling before downstream implementation.

## 6. Relationship To Prior MTI Rulings

This ruling must be read together with:

- MTI-D-01: Product Master Scope = Option B, tenant/company-scoped product identity
- MTI-D-02: Authorization Granularity = Company + Warehouse + Operation-Type
- MTI-D-03: Tenant-Changeable Boundary = Platform-owned Core + Tenant Config Overlay, with Private Company option for high-specificity customers

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

If any downstream design cannot preserve the Platform-owned Core + Tenant Config Overlay boundary, the related item must remain HOLD.
