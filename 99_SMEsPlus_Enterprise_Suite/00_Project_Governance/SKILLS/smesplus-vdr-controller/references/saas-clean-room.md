# SaaS Invariants and Clean-Room Rules

## Tenant and company model

- Tenant = one independent customer or one demonstrable corporate/economic group under common ownership/control/formally recognized group governance.
- Company = one legal/accounting/business entity inside the tenant.
- Unrelated independent companies default to separate tenants.
- Administrative convenience, business relationship, or common service provider does not justify a shared tenant.
- A user may hold memberships in multiple tenants, but runtime execution context must remain one explicit tenant context at a time.
- Lower-level relationships such as company, branch, warehouse, or location can never weaken tenant isolation.

Treat cross-tenant leakage as a critical / Zero-Tolerance defect.

## Clean-room model

SMEsPlus is a new SaaS ERP implementation. External ERP systems, source code, documents, databases, and reference systems may be used for learning, functional understanding, pattern identification, control analysis, gap analysis, and behavior verification.

Do not automatically reuse them as SMEsPlus source code, database schema, workflow clone, ORM clone, or proprietary implementation.

Use this transformation:

Reference Observation -> Generic Concept -> SMEsPlus Requirement -> SMEsPlus Independent Design.

When evidence is derived from a reference system, keep reference provenance separate from SMEsPlus implementation decisions.
