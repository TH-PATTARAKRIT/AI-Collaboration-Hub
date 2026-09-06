# SMEsPlus Standard Product & Upward Mobility Policy

Project: SMEsPlus ENTERPRISE SUITE
Effective Date: 2026-09-06
Authority: Boss = Sole Final Approver
Status: BOSS APPROVED / EFFECTIVE

## 1. Purpose

Establish the mandatory commercial and architecture policy for SMEsPlus Standard and Enterprise deployment tiers, with emphasis on Thai SME affordability, operational simplicity, shared-resource scalability, product consistency, and controlled upward migration.

## 2. Two-Tier Product Model

SMEsPlus operates as one product, one clean-room codebase, and two deployment tiers:

### STANDARD
- Shared Resource
- Multi-tenant shared cells
- Cost optimized for Thai SMEs
- Can scale horizontally to many cells/servers without changing product semantics
- Standard tenants may be distributed across many Standard servers/cells as capacity requires

### ENTERPRISE
- Dedicated Resource
- Dedicated tenant environment/resources
- Higher isolation, performance and SLA capability
- Uses the same SMEsPlus Core, business semantics, accounting integrity, API contracts, security principles and upgrade architecture

## 3. One Product / No Core Fork

Mandatory invariant:

**ONE SMEPLUS PRODUCT — ONE CORE CODEBASE — MULTIPLE DEPLOYMENT CELLS**

Deployment may differ. Business semantics must not fork.

Standard and Enterprise must not become separate codebases.

## 4. Horizontal Standard Scaling

Standard is not one national server or one national database.

Standard may scale through many shared-resource cells/servers, for example Cell A, Cell B, Cell C ... Cell N.

Cell count is not an architectural problem as long as:
- Tenant identity remains independent from server/database/cell identity
- Routing/placement is controlled
- Capacity and noisy-neighbor risk are monitored
- Upgrade/version governance remains consistent
- Backup/restore boundaries remain controlled

Cell capacity must be evidence-driven, not frozen as a tenant-count constant.

## 5. Standard Product Governance

Standard is a product, not a customer-by-customer customization service.

Customer-specific requests must not directly alter Standard Core.

Every requested capability must be evaluated for:
- Broad business value
- ERP semantic correctness
- Cross-module impact
- Security/tenant impact
- Accounting/control impact
- Maintainability
- Testability
- Upgrade impact
- Operational cost
- Reusability across the Standard customer base

A request may be accepted into Standard only when the SMEs Team determines that it is materially useful, architecturally sound, maintainable, and beneficial beyond a single isolated customer need.

## 6. Coverage Principle

SMEsPlus Standard should be designed broadly enough to cover real SME operating needs without becoming uselessly bloated.

Mandatory principle:

**MORE CAPABILITY IS ACCEPTABLE WHEN IT IS USEFUL, CONTROLLED, MAINTAINABLE AND ACTUALLY APPLICABLE.**

**MORE CAPABILITY WITHOUT REAL USAGE, BUSINESS VALUE OR MAINTAINABILITY IS WASTE.**

The objective is not minimum feature count and not maximum feature count. The objective is high-value, reusable business coverage.

## 7. Configuration Before Customization

Before creating new code, SMEs Team must evaluate whether the requirement can be satisfied through:
- Configuration
- Policy
- Workflow setup
- Entitlement
- Master-data design
- Reporting
- Approved extension point

Custom Core changes are last resort and require controlled review.

## 8. Customer Request Governance

Customer request flow:

Customer Request
→ AGPO Intake / Prior Evidence / Delta Check
→ IEDA ERP Semantic Review where applicable
→ PEESA Architecture / Engineering / Product Impact Review where applicable
→ 9 Veto if material
→ Standard Product Value Assessment
→ ACCEPT / HOLD / REJECT / REWORK
→ AGPO Controlled Prompt if accepted
→ Authorized execution only after Gate

A single-customer request does not automatically become product scope.

Control may discover a Scope Gap, but it may not silently convert that Gap into Scope.

## 9. Standard → Enterprise Mobility

Normal supported commercial migration:

**STANDARD → ENTERPRISE = SUPPORTED UPGRADE PATH**

Migration should preserve tenant identity and business identity where technically feasible.

Tenant Identity ≠ Server Identity
Tenant Identity ≠ Database Identity
Tenant Identity ≠ Cell Identity

## 10. Enterprise → Standard Policy

Normal commercial downgrade is not offered:

**ENTERPRISE → STANDARD = NOT A NORMAL COMMERCIAL OFFERING**

Reason: dedicated-resource tenants may exceed Standard capacity, workload, extension, integration, SLA or operational assumptions and may negatively affect shared-resource tenants.

Architecture may remain technically reversible under controlled exception, but this is not a normal sales path.

Any Enterprise → Standard exception requires at minimum:
- Standard capacity fit
- workload/performance fit
- compatible feature/extension profile
- compatible integration profile
- acceptable security/SLA reduction
- absence or remediation of dedicated-only dependencies
- migration/reconciliation testing
- backup and rollback plan
- controlled technical review
- Boss approval

## 11. Anti Lock-In

Not offering Enterprise → Standard as a normal downgrade does not remove customer data portability rights.

Data export, controlled exit, auditability, backup/restore and contractual portability must remain separately governed.

## 12. Standard Quality Rule

Standard is not a low-quality product. It is a shared-resource deployment model.

Standard and Enterprise must preserve the same minimum integrity principles for:
- Tenant isolation
- Security
- Accounting correctness
- Transaction integrity
- Auditability
- Backup
- Restore
- Reconciliation
- Upgradeability

## 13. Source Code / Server Layer Direction

SMEsPlus may operate many Standard servers/cells using the same Core source-code line and controlled deployment architecture.

Infrastructure scaling must happen through the SaaS architecture/deployment layer, not through customer-specific Core source-code forks.

## 14. Decision Rules

- Shared by default for affordability.
- Dedicated by choice or requirement.
- Standard customer-specific Core customization is not a default offering.
- Standard capability requests enter controlled product governance.
- Useful breadth is encouraged; unused complexity is rejected.
- Architecture invariants are frozen before implementation mechanisms.
- No Evidence = No Verified Progress.
- Never Skip Gate.
- Boss remains sole Final Approver.

## 15. Final Operating Principle

**SMEsPlus Standard must remain commercially affordable for Thai SMEs, horizontally scalable across many shared-resource cells, functionally broad enough for real business operations, and protected from customer-by-customer Core customization.**

**SMEsPlus Enterprise provides dedicated resource isolation while preserving the same SMEsPlus Core.**

**Standard → Enterprise is the normal supported mobility path. Enterprise → Standard is not a standard commercial path and requires controlled exception approval.**
