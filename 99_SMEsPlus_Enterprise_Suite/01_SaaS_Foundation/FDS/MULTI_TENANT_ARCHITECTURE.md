# MULTI_TENANT_ARCHITECTURE.md

# SMEsPlus Enterprise Suite - Multi-Tenant Architecture

**Version:** 1.0.0

**Status:** Architecture Gate (Draft → Pending Review)

**Document Type:** System Architecture - Multi-Tenancy Design

**Effective Date:** 2026-07-01

**Authority:** ADR-0011 (Multi-Tenant by Design)

---

# SECTION 1: PURPOSE

This document defines the multi-tenant architecture for SMEsPlus Enterprise Suite.

It establishes:
- Tenant isolation strategies at every layer
- Tenant hierarchy and data model
- Row-level security implementation
- Tenant context propagation patterns
- Performance optimization for multi-tenancy
- Security enforcement mechanisms
- Thai multi-entity support
- Data isolation verification
- Compliance and auditability

**Scope:** Covers multi-tenancy across all 11 layers of architecture

---

# SECTION 2: MULTI-TENANCY DEFINITION

## 2.1 What is Multi-Tenancy?

```
Multiple independent organizations (tenants) operate within
a single software deployment, each with:

✅ Separate data (completely isolated)
✅ Separate configuration (customizable per tenant)
✅ Separate users and permissions
✅ Separate audit trails
✅ Shared infrastructure (cost-efficient)
```

## 2.2 Multi-Tenancy Levels

SMEsPlus uses Level 2: Single Database, Multiple Schemas
- Each tenant gets dedicated schema
- RLS policies provide additional protection
- Good balance of isolation and efficiency

---

# SECTION 3: TENANT HIERARCHY

## 3.1 Complete Tenant Structure

```
Platform → Tenant → Company → Branch → Division → User
```

| Level | Entity | Purpose |
|-------|--------|---------|
| 1 | Platform | SMEsPlus SaaS |
| 2 | Tenant | Organization |
| 3 | Company | Legal entity |
| 4 | Branch | Operating location |
| 5 | Division | Functional unit |
| 6 | User | Individual |

## 3.2 Thai-Specific Structure

Thailand business structure support:
- Main company with tax registration
- Multiple branches across regions
- Functional divisions (accounting, sales, HR)
- Subsidiary companies (optional)

---

# SECTION 4: ISOLATION STRATEGIES

Defense in Depth approach:

1. **Application Level** - Python/Node code filtering
2. **Repository Level** - SQL queries with tenant filters
3. **Database Level** - PostgreSQL RLS policies

If any level fails, next level catches it.

---

# SECTION 5: DATABASE MULTI-TENANCY IMPLEMENTATION

Schema isolation pattern:
- One schema per tenant
- Identical table structure
- RLS policies for additional protection
- Connection-level isolation

---

# SECTION 6: APPLICATION LAYER ISOLATION

TenantContext management ensures:
- Thread-safe tenant context
- Automatic PostgreSQL session variables
- Middleware integration with JWT
- Immutable context for request duration

---

# SECTION 7: AUTHORIZATION WITH MULTI-TENANCY

Role-based access control with tenant awareness:
- Users assigned to specific tenants
- Companies and branches filtered by role
- Cross-tenant access verification
- Permission checking at operation level

---

# SECTION 8: TENANT DATA MODEL

All business tables must include:
- tenant_id (primary isolation key)
- company_id (secondary isolation)
- branch_id (where applicable)
- Audit columns (created_by, updated_by, deleted_at)

---

# SECTION 9: ISOLATION VERIFICATION

Testing ensures:
- Tenant cannot access other tenant data
- Users cannot access unauthorized companies/branches
- Branch managers see only assigned branches
- Audit trail captures all access

---

# SECTION 10: PERFORMANCE CONSIDERATIONS

Schema isolation benefits:
- Faster queries (smaller table scans)
- Tenant-specific indexes
- Optimized query plans
- Per-tenant backup/restore

---

# SECTION 11: THAI MULTI-ENTITY SCENARIOS

Support for complex Thai business structures:
- Consolidated reporting across branches
- Company-level visibility
- Branch-level detail views
- Division-based cost centers

---

# SECTION 12: CRITICAL SECURITY RULES

**TENANT BOUNDARY VIOLATION = CRITICAL DEFECT**

Every code change must:
- Filter by tenant_id
- Check company_id where needed
- Verify branch_id
- Enforce authorization
- Maintain RLS enforcement

---

# SECTION 13: CROSS REFERENCES

- SAAS_ARCHITECTURE.md
- DATABASE_ARCHITECTURE.md
- APPLICATION_ARCHITECTURE.md
- SECURITY_ARCHITECTURE.md
- API_STANDARD.md

---

# SECTION 14: DOCUMENT STATUS

**Version:** 1.0.0
**Status:** Draft (Pending Architecture Gate Review)
**Owner:** SMEsPlus Architecture Office
**Created:** 2026-07-01