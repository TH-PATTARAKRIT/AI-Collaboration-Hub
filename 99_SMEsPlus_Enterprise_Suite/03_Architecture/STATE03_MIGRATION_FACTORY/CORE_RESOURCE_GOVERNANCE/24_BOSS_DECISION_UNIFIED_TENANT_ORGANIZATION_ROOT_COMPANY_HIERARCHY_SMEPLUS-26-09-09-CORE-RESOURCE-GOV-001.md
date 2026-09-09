# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# BOSS DECISION — Unified Tenant → Organization Root → Company Hierarchy

## Decision Status
APPROVED BY BOSS

## Decision
SMEsPlus shall use one consistent organizational hierarchy for every Tenant, regardless of whether the customer initially arrives as a single legal company or as a multi-company / holding / corporate group.

Canonical hierarchy:

`PLATFORM -> TENANT -> ORGANIZATION ROOT / GROUP -> COMPANY -> BRANCH`

Every Tenant MUST have an Organization Root / Group layer.

For a single-company customer:

`Tenant -> Organization Root -> Company`

For a multi-company / holding customer:

`Tenant -> Organization Root / Group -> Company A + Company B + Company C ...`

A real Holding Company, Parent Company, or other legal parent entity is optional business structure inside the Organization Root. SMEsPlus must not invent a fake legal holding company merely to satisfy the hierarchy.

## Rationale
The platform cannot know at tenant onboarding whether a customer will remain a single-company SME or later expand into multiple legal entities, subsidiaries, or a holding structure. A single canonical path avoids branch logic, reduces onboarding ambiguity, simplifies security and authorization design, and allows the customer to grow from one Company to many Companies without changing Tenant identity.

## Key Semantics
- Tenant = SaaS customer / security / isolation boundary.
- Organization Root / Group = canonical logical organization boundary inside the Tenant.
- Holding Company = optional real legal/entity relationship where applicable.
- Company = legal/accounting/business entity executing transactions.
- Branch = subordinate operating location/business unit where applicable.

## Growth Example
Initial state:

`Tenant T00500 -> Group ABC -> Company A`

Later growth:

`Tenant T00500 -> Group ABC -> Company A + Company B + Company C`

Later creation of a legal holding entity:

`Tenant T00500 -> Group ABC -> Holding Company ABC Holdings + Company A + Company B + Company C`

Tenant identity, package, wallet, audit lineage and infrastructure placement do not need to change merely because the customer adds Companies or creates a holding structure.

## Design Principle
> One canonical organizational path for every Tenant. Customer growth changes the organization below the Tenant, not the Tenant identity itself.

## Governance Impact
The SaaS Team must use this hierarchy as a Boss-approved business/identity invariant and must reconcile it with tenant isolation, company context, role/permission scope, package/resource governance, billing/wallet ownership, data architecture and Standard-to-Enterprise mobility.

This decision does NOT freeze physical infrastructure topology, database topology, Kubernetes topology, container-per-tenant, schema-per-tenant, or database-per-tenant mechanisms.

Boss remains sole Final Approver.
