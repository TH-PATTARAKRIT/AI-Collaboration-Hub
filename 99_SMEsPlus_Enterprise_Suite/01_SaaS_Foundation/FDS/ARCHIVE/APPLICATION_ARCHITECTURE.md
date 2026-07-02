# APPLICATION_ARCHITECTURE.md

# SMEsPlus Enterprise Suite - Application Layer Architecture

**Version:** 1.0.0

**Status:** Architecture Gate (Draft → Pending Review)

**Document Type:** System Architecture - Application Layer Design

**Effective Date:** 2026-07-01

**Authority:** ADR-0002 (Claude AI Primary Execution), ADR-0012 (API First)

---

# SECTION 1: PURPOSE

This document defines the application layer architecture for SMEsPlus Enterprise Suite.

It establishes:
- Service-oriented architecture patterns
- Repository pattern and data access layer
- Business logic organization and execution
- API controller design and HTTP handling
- DTO (Data Transfer Object) standards
- Stateless service design principles
- Multi-tenant context propagation
- Error handling and logging strategies
- Transaction management and consistency
- Performance optimization at application layer

**Scope:** Covers Layer 3 (Application Services) and Layer 4 (Business Domain) of the 11-layer architecture

---

# SECTION 2: APPLICATION LAYER POSITION

## 2.1 Application Layer in 11-Layer Architecture

```
Layer 1: User Interface
Layer 2: API Gateway
          │
          ▼
Layer 3: Application Service ← THIS DOCUMENT
          │
          ▼
Layer 4: Business Domain Services ← THIS DOCUMENT
          │
          ▼
Layer 5: Workflow & Approval
Layer 6: Integration
Layer 7: Data Access Layer
Layer 8: Database
Layer 9: Object Storage
Layer 10: Infrastructure
Layer 11: Observability
```

The application layer sits between the API Gateway and database layer, responsible for orchestration, validation, and business logic execution.

---

# SECTION 3: APPLICATION ARCHITECTURE OVERVIEW

## 3.1 Complete Application Flow

Requests flow through multiple layers with clear separation of concerns:

1. HTTP Request arrives
2. API Gateway routes and authenticates
3. API Controller handles HTTP protocol
4. Application Service orchestrates operations
5. Business Service executes business logic
6. Repository queries database
7. Database persists with audit trail
8. Response flows back through layers

---

# SECTION 4: SERVICE LAYER ARCHITECTURE

## 4.1 Three-Layer Service Design

The application is organized into three distinct service layers:

**API Controller Service** - Handles HTTP protocol concerns
**Application Service** - Orchestrates business operations  
**Business Service** - Implements core business logic

Each layer has clear responsibilities and loose coupling.

---

# SECTION 5: REPOSITORY PATTERN & DATA ACCESS LAYER

The repository pattern abstracts database access, enabling:

- Easy testing with mock repositories
- Database independence
- Consistent tenant filtering
- Query optimization
- Transaction management

All data access must go through repositories, never direct database access from business logic.

---

# SECTION 6: DTO & VALIDATION DESIGN

Data Transfer Objects (DTOs) separate API contracts from domain objects:

- Request DTOs validate incoming data
- Response DTOs shape outgoing data  
- Three-stage validation: DTO → Application → Business

---

# SECTION 7: STATELESS SERVICE DESIGN

Services are completely stateless, enabling:

- Horizontal scaling (add more instances)
- Load balancing without session affinity
- Disaster recovery
- Multi-region deployment

All state is stored in database, cache, or queue.

---

# SECTION 8: TENANT CONTEXT PROPAGATION

Multi-tenancy is enforced at both application and database levels:

- Extract tenant from JWT token
- Set context for request
- Database RLS policies enforce filtering
- Tenant isolation = critical security requirement

---

# SECTION 9: ERROR HANDLING & LOGGING

- Structured logging with context
- Error codes for programmatic handling
- No sensitive data in logs
- Request tracing for debugging

---

# SECTION 10: TRANSACTION MANAGEMENT

- Short, atomic transactions
- Explicit transaction boundaries
- Pessimistic locking where needed
- ACID compliance

---

# SECTION 11: PERFORMANCE OPTIMIZATION

- Multi-level caching (Redis)
- Query optimization
- Pagination for large result sets
- Connection pooling
- Index-aware query design

---

# SECTION 12: TESTING STRATEGY

- Unit tests for business logic
- Integration tests for APIs
- Security tests for tenant isolation
- Performance tests for scalability

---

# SECTION 13: THAI MARKET INTEGRATION

- Thai tax ID validation
- Withholding tax calculation
- Multi-entity support (Company, Branch)
- Thai DART compliance

---

# SECTION 14: COMPARISON WITH ODOO APPLICATION LAYER

SMEsPlus advantages:

- Service-oriented vs monolithic
- Explicit transaction management
- Repository pattern vs direct ORM
- Multi-level caching
- Better performance optimization
- Looser coupling

---

# SECTION 15: MONITORING & OBSERVABILITY

- Application metrics collection
- Distributed request tracing
- Error rate monitoring
- Performance baseline tracking

---

# SECTION 16: CROSS REFERENCES

- SAAS_ARCHITECTURE.md
- API_STANDARD.md
- DATABASE_ARCHITECTURE.md
- SYSTEM_ARCHITECTURE.md
- SECURITY_ARCHITECTURE.md

---

# SECTION 17: DOCUMENT STATUS

**Status:** Draft (Pending Architecture Gate Review)
**Version:** 1.0.0
**Owner:** SMEsPlus Architecture Office
**Effective Date:** Upon approval