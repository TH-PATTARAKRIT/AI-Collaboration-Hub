# SAAS_ARCHITECTURE.md

# SMEsPlus Enterprise Suite - SaaS Architecture

**Version:** 1.0.0

**Status:** Architecture Gate (Draft → Pending Review)

**Document Type:** System Architecture - SaaS Deployment Model

**Effective Date:** 2026-07-01

**Authority:** ADR-0010 (SaaS First)

---

# SECTION 1: PURPOSE

This document defines the SaaS (Software-as-a-Service) architecture for SMEsPlus Enterprise Suite.

It establishes:
- Multi-tenant deployment model
- Tenant isolation strategy
- Performance optimization architecture (40% target vs Odoo)
- Scalability patterns
- Resource optimization
- Operational resilience

**Scope:** Covers layers 1-10 of the 11-layer architecture (UI through Infrastructure)

---

# SECTION 2: SAAS FIRST PRINCIPLE

## 2.1 Core Definition

**SaaS First** means:

```
Every architectural decision assumes SaaS deployment.
No single-tenant assumptions.
Multi-tenancy is not optional—it's built-in from Layer 1.
```

## 2.2 SaaS Architecture Requirements

SaaS architecture must provide:

- ✅ **Multi-Tenancy** - Multiple organizations in one deployment
- ✅ **Isolation** - Complete data and configuration isolation
- ✅ **Scalability** - Horizontal scaling for growing tenant base
- ✅ **Elasticity** - Auto-scaling resources per load
- ✅ **High Availability** - 99.9% uptime SLA minimum
- ✅ **Security** - Tenant data always protected
- ✅ **Performance** - Sub-second response times
- ✅ **Cost Efficiency** - Per-tenant cost optimization

---

# SECTION 3: DEPLOYMENT MODEL

## 3.1 SaaS Deployment Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Internet / Cloud                  │
├─────────────────────────────────────────────────────┤
│                  API Gateway                         │
│      (Load Balancing, Auth, Rate Limiting)          │
├─────────────────────────────────────────────────────┤
│        Application Server Pool (Horizontal)         │
│  ┌──────────────┬──────────────┬──────────────┐    │
│  │   Server 1   │   Server 2   │   Server N   │    │
│  │ (Stateless)  │ (Stateless)  │ (Stateless)  │    │
│  └──────────────┴──────────────┴──────────────┘    │
├─────────────────────────────────────────────────────┤
│              Shared Services Layer                   │
│  ┌──────────────┬──────────────┬──────────────┐    │
│  │  PostgreSQL  │     Redis    │   Message    │    │
│  │  (Cluster)   │   (Cache)    │   Queue      │    │
│  └──────────────┴──────────────┴──────────────┘    │
├─────────────────────────────────────────────────────┤
│             Storage Layer (Multi-Tenant)            │
│  ┌──────────────────────────────────────────────┐  │
│  │   S3/MinIO - Tenant-Aware Buckets            │  │
│  └──────────────────────────────────────────────┘  │
├─────────────────────────────────────────────────────┤
│          Infrastructure (Proxmox/Kubernetes)        │
│     (Containers, VMs, Monitoring, Backup)          │
└─────────────────────────────────────────────────────┘
```

## 3.2 Key Characteristics

| Layer | Deployment Pattern | Scaling Strategy |
|-------|-------------------|-----------------|
| **API Gateway** | Single (HA) | Vertical |
| **Application Servers** | Horizontal Pool | Horizontal Auto-Scale |
| **Databases** | Shared (Clustered) | Vertical (Archive old data) |
| **Cache** | Shared (Redis Cluster) | Horizontal |
| **Storage** | Tenant-Partitioned | Horizontal (Buckets) |
| **Infrastructure** | Container-based | Horizontal |

---

# SECTION 4: MULTI-TENANCY ARCHITECTURE

## 4.1 Shared Infrastructure, Isolated Data

```
SaaS Architecture = Shared Application + Isolated Tenant Data
```

### Pattern: Schema Isolation (PostgreSQL)

Each tenant gets:
- Dedicated schema in shared database
- Row-level security (RLS) policies
- Separate sequences for IDs
- Isolated audit trails

```sql
CREATE SCHEMA tenant_12345;
ALTER ROLE tenant_app SET search_path TO tenant_12345;

-- Row-level security enforces tenant isolation
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON users
  USING (tenant_id = current_setting('app.current_tenant_id')::integer);
```

### Tenant Context Propagation

Every request must include:

```
1. Tenant ID (from JWT or session)
2. User ID (authenticated)
3. Request timestamp
4. Request correlation ID
```

Application must:
- Set tenant context at database session start
- Enforce tenant context in every query
- Audit tenant context in logs
- Never bypass tenant filtering

## 4.2 Data Isolation Enforcement

**Backend Enforcement (Database Level):**

```
All queries must include: WHERE tenant_id = current_tenant()
All writes must include: tenant_id = current_tenant()
All deletes must include: WHERE tenant_id = current_tenant()
```

**Application Level Enforcement:**

```
1. Set PostgreSQL session variable: app.current_tenant_id
2. Apply tenant filtering to all queries
3. Log tenant context with every operation
4. Audit tenant boundary violations
```

**Frontend Cannot Enforce Isolation:**

- ❌ Frontend filtering alone is not sufficient
- ✅ Backend must enforce for every operation
- ❌ Never trust client-side permission checks
- ✅ Backend authorization is mandatory

---

# SECTION 5: PERFORMANCE ARCHITECTURE

## 5.1 40% Performance Target

**Objective:** Achieve 40% better performance than standard Odoo

**Baseline:** Odoo Community/Enterprise performance metrics
**Target:** SMEsPlus performance ≥ 140% of Odoo standard

### Performance Dimensions

| Metric | Odoo Baseline | SMEsPlus Target | Optimization |
|--------|---------------|-----------------|--------------|
| **Page Load** | 2-3 sec | <1.2 sec | API-first, lazy loading |
| **List Query** | 500-1000ms | <300ms | Indexed, denormalized views |
| **Create Record** | 800-1200ms | <500ms | Optimized save path |
| **Concurrent Users** | 100-200 | 500+ | Horizontal scaling |
| **Throughput** | 100 req/sec | 500+ req/sec | Optimized API |

## 5.2 Performance Optimization Strategies

### Database Optimization

```sql
-- 1. Strategic Indexing
CREATE INDEX idx_tenant_created ON records(tenant_id, created_date DESC);
CREATE INDEX idx_company_status ON records(tenant_id, company_id, status);

-- 2. Denormalized Views for Reporting
CREATE MATERIALIZED VIEW mv_sales_summary AS
SELECT tenant_id, company_id, SUM(amount) AS total_sales
FROM orders WHERE status = 'completed'
GROUP BY tenant_id, company_id;

-- 3. Partitioning by Tenant (High-Volume Tables)
CREATE TABLE orders (
  id BIGSERIAL, tenant_id INTEGER, amount DECIMAL, created_date DATE
) PARTITION BY RANGE (tenant_id);

-- 4. Connection Pooling
-- PgBouncer: min_pool_size = 10, max_pool_size = 100 per tenant
```

### Caching Strategy

```
Level 1: Redis Cache (Session, Config, Lookups)
  - TTL: 1 hour for config
  - TTL: 15 min for user sessions
  - Invalidate on: Write operations
  
Level 2: Browser Cache (Static Assets)
  - TTL: 24 hours
  - Cache-Control: public, max-age=86400
  
Level 3: Database Query Result Cache
  - Cached aggregations (refreshed hourly)
  - Tenant-specific counters
  - Invalidate: On any insert/update/delete
```

### API Optimization

```
1. Pagination: Mandatory limit (max 1000 per page)
2. Field Selection: Allow clients to select fields (not *)
3. Lazy Loading: Don't load relationships by default
4. Batch API: Support multiple operations in single request
5. Compression: gzip enabled, response size <1MB target
```

### Search Optimization

```
-- Elasticsearch for full-text search
-- Index: transactions, documents, audit logs
-- Queries: <100ms response time
-- Refresh: Batch indexing (once per 5 minutes)

GET /elasticsearch/transactions/_search
{
  "query": {
    "bool": {
      "must": [
        {"term": {"tenant_id": 12345}},
        {"match": {"description": "payment"}}
      ]
    }
  },
  "size": 50
}
```

---

# SECTION 6: COMPARISON WITH ODOO

## 6.1 Architectural Advantages

| Aspect | Odoo | SMEsPlus | Advantage |
|--------|------|----------|-----------|
| **Architecture** | Monolithic | 11-Layer Modular | Flexibility |
| **Multi-Tenancy** | Add-on module | Built-in | Native support |
| **API** | REST (added) | API-first | Better integration |
| **Database** | PostgreSQL | PostgreSQL + Optimized | Performance |
| **Scaling** | Vertical | Horizontal | Cost efficiency |
| **Customization** | Code modification | Configuration | Maintainability |
| **Performance** | 2-3 sec page load | <1.2 sec | 40% faster |
| **Concurrent Users** | 100-200 typical | 500+ typical | Scalability |

## 6.2 Performance Improvements

### Query Performance

**Odoo Approach:**
```python
# Odoo loads related records eagerly
orders = self.env['sale.order'].search([('state', '=', 'done')])
# Result: N+1 queries (slow)
```

**SMEsPlus Approach:**
```sql
-- Single optimized query with proper joins
SELECT o.id, o.name, c.name AS company_name, SUM(l.qty) AS total_qty
FROM orders o
JOIN companies c ON o.company_id = c.id
JOIN order_lines l ON o.id = l.order_id
WHERE o.tenant_id = $1 AND o.status = 'completed'
GROUP BY o.id, c.name
ORDER BY o.created_date DESC
LIMIT 100;
-- Result: Single query, <50ms response
```

### Customization Approach

**Odoo:**
- Extend Python classes
- Override methods
- Risk of conflicts
- Difficult to maintain

**SMEsPlus:**
- Configuration-based
- Business rules in database
- Audit trail of changes
- Easy to maintain and roll back

---

# SECTION 7: THAI MARKET CUSTOMIZATION

## 7.1 Thai-Specific Requirements

### Accounting Standards (Thai DART)

```
SMEsPlus Requirements:
- Chart of Accounts: Thai Accounting Standards
- Journal Entries: Bilingual support (Thai/English)
- Financial Reports: Thai Revenue Department format
- Tax Reporting: Thai tax forms and calculations
- Currency: Thai Baht (THB) as default, multi-currency support
- Fiscal Year: Calendar year (January-December)
```

### Thai Tax Compliance

```
1. VAT (Value Added Tax)
   - Standard rate: 7%
   - Reduced rate: 0% (exports, certain goods)
   - Reverse charge: Foreign services
   - VAT Invoice: Special format required

2. Corporate Income Tax
   - Standard rate: 20%
   - Filing deadline: 180 days after fiscal year-end
   - Installment payments: 4 times per year

3. Withholding Tax
   - Various rates by transaction type
   - Contractor: 3-5% withholding
   - Interest: 15% withholding
   - Dividends: 10% withholding
```

### Thai Localization Database

```
Localization data stored in SMEsPlus:
- Tax codes and rates (auto-updated)
- Statutory forms (Thai-language templates)
- Bank account formats
- Business registration numbers
- Government reporting formats
```

## 7.2 Multi-Entity Support (Thai-Specific)

Thai business structure often requires:

```
1. Company (Main legal entity)
   - Single tax ID
   - One VAT registration

2. Branches (Multiple operating locations)
   - Same company
   - Separate operations
   - Branch-level reporting

3. Divisions (Functional units)
   - Cost centers
   - Profit centers
   - Service departments

SMEsPlus Requirement:
- Company-level isolation
- Branch-level operations
- Division-level reporting
- Cross-entity consolidation
```

---

# SECTION 8: API-FIRST ARCHITECTURE

## 8.1 API Design Principle

```
Every business capability must be accessible through API.
UI calls API. Integrations call API. Internal services call API.
```

### API Gateway Pattern

```
Client → API Gateway → Service Router → Business Logic

API Gateway provides:
- Authentication & Authorization
- Rate limiting (per tenant)
- Request validation
- Response standardization
- API versioning
- Request logging
```

### API Versioning Strategy

```
/api/v1/orders         → Current production API
/api/v2/orders         → New API (parallel deployment)
/api/v1-deprecated/... → Legacy (sunset period)

Backward Compatibility:
- Additive changes: No version bump
- Breaking changes: New version required
- Deprecation period: Minimum 6 months
```

### Rate Limiting (Per Tenant)

```
Standard Plan:
  - 100 requests/second per tenant
  - 1,000 requests/minute burst
  - 10MB response payload limit

Premium Plan:
  - 1,000 requests/second per tenant
  - 10,000 requests/minute burst
  - 100MB response payload limit
```

---

# SECTION 9: SECURITY ARCHITECTURE

## 9.1 Security Layers

### Layer 1: Network (API Gateway)
```
- HTTPS/TLS 1.3 only
- WAF (Web Application Firewall)
- DDoS protection
- IP whitelisting (enterprise)
```

### Layer 2: Authentication
```
- OAuth 2.0 for integrations
- JWT tokens (15-minute expiry)
- MFA support (TOTP)
- Session management
```

### Layer 3: Authorization
```
- Role-based access control (RBAC)
- Row-level security (RLS) by tenant
- Attribute-based access control (ABAC)
- Resource-level permissions
```

### Layer 4: Data Protection
```
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- Sensitive data masking in logs
- Audit trail of all access
```

## 9.2 Tenant Data Protection

**Critical Rule:**

```
TENANT BOUNDARY VIOLATION = CRITICAL DEFECT

Every access must verify:
1. Authenticated user
2. User belongs to tenant
3. Resource belongs to tenant
4. Tenant isolation enforced at database level
```

---

# SECTION 10: RELIABILITY ARCHITECTURE

## 10.1 High Availability Design

```
┌─────────────────────────────────────────┐
│         Load Balancer (HA)              │
│    (Active-Passive failover)            │
├─────────────────────────────────────────┤
│    Application Server Cluster           │
│  - Minimum 3 instances (horizontal)    │
│  - Health checks: 5-second interval     │
│  - Auto-restart on failure              │
├─────────────────────────────────────────┤
│    Database Cluster (Primary + Replicas)│
│  - Synchronous replication              │
│  - Automatic failover                   │
│  - Backup: Every 6 hours                │
├─────────────────────────────────────────┤
│    Message Queue (HA)                   │
│  - At-least-once delivery               │
│  - Durable persistence                  │
│  - Consumer groups                      │
└─────────────────────────────────────────┘
```

## 10.2 Disaster Recovery

**RTO (Recovery Time Objective):** <1 hour
**RPO (Recovery Point Objective):** <15 minutes

```
Backup Strategy:
- Continuous replication to standby
- Daily snapshots (kept 30 days)
- Weekly archives (kept 1 year)
- Cross-region backup (every 24 hours)

Failover Procedure:
1. Detect primary failure
2. Promote replica to primary (automated)
3. Update DNS records (5-minute TTL)
4. Notify operations team
5. Complete: <5 minutes
```

---

# SECTION 11: INFRASTRUCTURE REQUIREMENTS

## 11.1 Minimum Infrastructure

```
Development Environment:
- 4 vCPU, 8 GB RAM, 100 GB storage
- Single application server
- PostgreSQL 14+
- Redis cache
- MinIO for storage

Production Environment (Minimum):
- API Gateway: 2 vCPU, 4 GB RAM
- App Servers (3×): 4 vCPU each, 8 GB RAM each
- Database: 8 vCPU, 32 GB RAM, 500 GB SSD
- Redis: 2 vCPU, 8 GB RAM
- MinIO: 2 nodes, 4 TB storage each
- Monitoring: 2 vCPU, 4 GB RAM
```

## 11.2 Scaling Limits (Single Cluster)

```
Tenant Capacity per Cluster:
- Small: 10-50 tenants (under 100 users each)
- Medium: 50-500 tenants (under 500 users each)
- Large: 500+ tenants (architecture review required)

When to scale:
- CPU utilization >80% sustained
- Memory utilization >85% sustained
- Database query time >500ms (p99)
- Add new cluster, shard by tenant_id ranges
```

---

# SECTION 12: MONITORING & OBSERVABILITY

## 12.1 Key Metrics

```
Application Metrics:
- Request rate (req/sec)
- Response time (p50, p95, p99)
- Error rate (%)
- Cache hit rate (%)
- API endpoint latency (per endpoint)

Database Metrics:
- Query time (p50, p95, p99)
- Connection pool usage (%)
- Slow queries (>100ms)
- Transaction throughput (tx/sec)
- Table sizes and growth

Infrastructure Metrics:
- CPU utilization (%)
- Memory utilization (%)
- Disk I/O (MB/sec)
- Network I/O (Mbps)
- Container restarts (count)

Business Metrics:
- Active users (per tenant)
- Transactions per hour
- Document storage used (per tenant)
- API usage (per tenant)
```

## 12.2 Alerting

```
Critical Alerts (< 5 minute response):
- Database down
- API Gateway unavailable
- Memory exhausted
- Disk full
- Tenant isolation breach

Warning Alerts (< 30 minute response):
- High error rate (> 1%)
- Response time degradation (> 2x baseline)
- Connection pool near exhaustion
- Cache hit rate drop
- Slow query detected
```

---

# SECTION 13: COST OPTIMIZATION

## 13.1 SaaS Cost Model

```
Infrastructure Cost Drivers:
1. Storage per tenant (per GB per month)
2. Compute per concurrent user (per vCPU-hour)
3. Network egress (per GB)
4. Backup (per GB retained)
5. Support (per support tier)

Cost Optimization:
- Shared infrastructure (amortized across tenants)
- Tenant-based resource quotas
- Archive old data (reduce storage)
- Connection pooling (reduce compute)
- Batch operations (reduce API calls)
```

## 13.2 Revenue Model Alignment

```
Typical SaaS Pricing:
- Startup Tier: $299-499/month
- Business Tier: $999-1999/month
- Enterprise Tier: Custom pricing

Cost Structure Target:
- Infrastructure: 20-30% of revenue
- Operations: 15-20% of revenue
- Development: 25-35% of revenue
- Profit margin: 15-25% (mature)
```

---

# SECTION 14: CROSS-REFERENCES

### Related Architecture Documents

- **SYSTEM_ARCHITECTURE.md** - 11-layer model (foundational)
- **APPLICATION_ARCHITECTURE.md** - Application layer detail
- **MULTI_TENANT_ARCHITECTURE.md** - Tenant isolation patterns
- **DATABASE_ARCHITECTURE.md** - PostgreSQL optimization
- **SECURITY_ARCHITECTURE.md** - Security controls
- **DEPLOYMENT_ARCHITECTURE.md** - Infrastructure and deployment

### Related Standards

- **PROJECT_CONSTITUTION.md** - Governance framework
- **EVIDENCE_RULE.md** - Evidence standards
- **GATE_CONTROL.md** - Architecture Gate requirements
- **ADR-0010** - SaaS First (decision authority)
- **ADR-0011** - Multi-Tenant by Design

---

# SECTION 15: DOCUMENT STATUS

**Document Owner:** SMEsPlus Architecture Office

**Document Version:** 1.0.0

**Status:** Draft (Pending Architecture Gate Review)

**Effective Date:** Upon approval

**Created:** 2026-07-01

**Last Updated:** 2026-07-01

**Gate:** Architecture Gate (Gate 3)

**Evidence Path:** `/02_Architecture/SAAS_ARCHITECTURE.md`

**Related Jira Issue:** ERPPLUS-[TBD] (Priority 2 - Architecture)

---

# IMPLEMENTATION CHECKLIST

**Architect Review:**
- [ ] Verify SaaS principles
- [ ] Confirm multi-tenancy design
- [ ] Validate performance targets
- [ ] Review security architecture
- [ ] Approve infrastructure requirements

**Security Review:**
- [ ] Tenant isolation enforcement
- [ ] Data protection measures
- [ ] API authentication/authorization
- [ ] Audit logging completeness

**Operations Review:**
- [ ] Infrastructure capacity
- [ ] Monitoring and alerting
- [ ] Backup and recovery
- [ ] Disaster recovery testing

**Final Approval:**
- [ ] Architecture Office sign-off
- [ ] Record in ADR (if required)
- [ ] Update DECISION_LOG.md

---

**END OF SAAS_ARCHITECTURE.md**

**This document is subject to the Architecture Gate review process (Gate 3 of 9)**