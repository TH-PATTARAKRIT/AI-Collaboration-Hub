# SMEsPlus Technology Stack Standard

**Version:** 1.0  
**Status:** Approved Baseline  
**Architecture:** Open ERP-first Enterprise SaaS Platform  
**Target:** Claude Code / ChatGPT / Development Team  
**Last Updated:** 2026-07-06

---

## 1. Purpose

This document defines the official technology stack for the SMEsPlus Enterprise Suite.

SMEsPlus is designed as an Open ERP-first Enterprise SaaS Platform, combining enterprise best practices inspired by leading ERP solutions while maintaining a clean-room architecture and vendor-independent implementation.

This document is the single source of truth for all AI assistants, architects, developers, and engineering teams.

All implementation must follow this standard unless an Architecture Review formally approves a deviation.

---

## 2. Core Architecture Principles

- Open ERP-first
- SaaS-first
- API-first
- Multi-tenant by design
- Clean-room implementation
- Security by design
- Enterprise-grade control
- Audit-first
- Event-driven where required
- Modular business architecture
- No vendor lock-in

---

## 3. Frontend Stack

| Layer | Standard Technology | Notes |
|---|---|---|
| Frontend Framework | Next.js 15 | Main frontend framework |
| UI Library | React 19 | Component-based UI |
| Language | TypeScript 5 | Required for type safety |
| Styling | Tailwind CSS 4 | Standard styling framework |
| Component Library | shadcn/ui | Enterprise component baseline |
| Icons | Lucide React | Standard icon library |
| State Management | Zustand | Lightweight state management |
| Form Handling | React Hook Form | Standard form library |
| Validation | Zod | Schema validation |
| Data Fetching | TanStack Query | Server-state management |
| Table/Grid | TanStack Table | Standard data table |
| Charts | Recharts | Dashboard and reporting charts |
| Drag and Drop | dnd-kit | Workflow and layout interaction |
| Date Library | Day.js | Date/time formatting |
| i18n | next-intl | Thai/English localization |

---

## 4. Backend API Stack

| Layer | Standard Technology | Notes |
|---|---|---|
| Backend Framework | FastAPI | Main API framework |
| Language | Python 3.12 | Standard backend language |
| API Style | REST API | Default API style |
| API Documentation | OpenAPI / Swagger | Required for API review |
| Request Validation | Pydantic v2 | Required |
| Dependency Injection | FastAPI Depends | Standard pattern |
| Authentication | JWT | Standard token authentication |
| Authorization | OAuth2 / OpenID Connect | Enterprise-ready authorization |
| Background Worker | Celery | Background job processing |
| Scheduler | Celery Beat | Scheduled jobs |

---

## 5. API Standard

Default API style: REST API.

Default content type: `application/json`.

Default authentication: Bearer Token.

Standard response format:

```json
{
  "success": true,
  "message": "",
  "data": {},
  "errors": []
}
```

Standard API examples:

```text
GET    /api/v1/customers
POST   /api/v1/customers
GET    /api/v1/products
POST   /api/v1/sales-orders
GET    /api/v1/vendors
```

API naming standard:

- Resource names must use kebab-case.
- API versioning must use `/api/v1/`.
- Business APIs must not expose database table names directly.
- All APIs must support tenant isolation.
- All write APIs must support audit logging.

---

## 6. Database Stack

| Layer | Standard Technology | Notes |
|---|---|---|
| Database | PostgreSQL 17 | Primary database |
| ORM | SQLAlchemy 2.x | Standard ORM |
| Migration | Alembic | Required for schema changes |
| Connection Pool | PgBouncer | Required for production readiness |
| Search | PostgreSQL Full Text Search | Default search option |
| JSON Support | JSONB | For controlled flexible attributes |
| ID Standard | UUID v7 | Preferred public identifier |

Database rules:

- Every business table must include tenant isolation fields.
- Every critical business table must include audit fields.
- Soft delete is required where business recovery is needed.
- PostgreSQL must not be exposed directly to the internet.
- Database schema changes must be performed through migrations only.

---

## 7. Cache and Queue

| Layer | Standard Technology | Notes |
|---|---|---|
| Cache | Redis 7 | API cache and session cache |
| Queue | Redis / Celery Broker | Background job queue |
| Rate Limit | Redis | API rate limit support |
| OTP / Token Cache | Redis | Time-based token storage |

---

## 8. Object Storage

| Layer | Standard Technology | Notes |
|---|---|---|
| Object Storage | MinIO | S3-compatible storage |
| Use Cases | Documents, images, attachments, reports, exports, backups | Required for SaaS document storage |

Rules:

- Store files in object storage, not in the database.
- Store metadata in PostgreSQL.
- File access must be tenant-aware.
- Critical documents require immutable snapshot support.

---

## 9. Authentication and Authorization

Required standards:

- JWT
- OAuth2
- OpenID Connect
- MFA / TOTP
- Refresh token flow
- RBAC
- Permission matrix
- Tenant-aware access control
- Audit log for sensitive actions

---

## 10. SaaS and Multi-Tenant Architecture

Default model:

```text
Shared Application
Shared Database
Tenant ID Isolation
PostgreSQL Row-Level Security where required
```

Required SaaS controls:

- Tenant isolation
- Company/branch access control
- Role-based access control
- Permission matrix
- Approval engine
- Audit trail
- Immutable business events
- Source module execution
- Posting engine separation
- Document snapshot

---

## 11. Messaging and Event Processing

| Stage | Standard Technology | Notes |
|---|---|---|
| Initial Stage | Redis Streams | Lightweight event processing |
| Future Stage | RabbitMQ / Kafka | Requires Architecture Review |

Rules:

- Business events must be immutable.
- Event publishing must not replace transactional consistency.
- Critical events require retry and dead-letter handling.

---

## 12. Infrastructure Stack

| Layer | Standard Technology | Notes |
|---|---|---|
| Hosting | ReadyIDC | Private cloud hosting |
| Virtualization | Proxmox VE | VM management |
| Operating System | Debian 13 LTS | Standard Linux baseline |
| Container | Docker | Standard runtime package |
| Local Development | Docker Compose | Dev/Test environment |
| Reverse Proxy | Nginx | HTTP/HTTPS routing |
| SSL | Let's Encrypt | TLS certificates |
| Firewall | pfSense / OPNsense | Recommended firewall layer |
| VPN | WireGuard | Admin access control |
| Future Orchestration | Kubernetes | Reserved; requires Architecture Review |

---

## 13. Monitoring and Operations

| Layer | Standard Technology | Notes |
|---|---|---|
| Metrics | Prometheus | System and application metrics |
| Dashboard | Grafana | Monitoring dashboards |
| Logging | Loki | Log aggregation |
| Error Tracking | Sentry | Application error tracking |
| Uptime Monitoring | Uptime Kuma | Service availability monitoring |
| Health Endpoint | FastAPI Health Endpoint | Required for services |

---

## 14. DevOps and CI/CD

| Layer | Standard Technology | Notes |
|---|---|---|
| Version Control | GitHub | Source control |
| CI/CD | GitHub Actions | Build/test/deploy automation |
| Branch Strategy | Git Flow | Controlled development flow |
| Protected Branches | main, develop | Required |
| Pull Request | Mandatory | No direct production branch push |
| Code Review | Mandatory | Required before merge |
| Architecture Review | Mandatory for core changes | Required for platform and module architecture |

---

## 15. Testing Stack

| Layer | Standard Technology | Notes |
|---|---|---|
| Backend Unit Test | Pytest | Python unit testing |
| Frontend Unit Test | Vitest | Frontend unit testing |
| E2E Test | Playwright | Browser automation and UAT evidence |
| API Test | Bruno | API request testing |
| Load Test | k6 | Performance testing |

Minimum coverage target: 80% for critical modules.

---

## 16. Security Stack

| Layer | Standard Technology | Notes |
|---|---|---|
| Dependency Scan | Trivy | Container and dependency scan |
| Secret Scan | Gitleaks | Secret leakage detection |
| Python Lint | Ruff | Backend quality gate |
| Frontend Lint | ESLint | Frontend quality gate |
| Formatting | Prettier | Frontend formatting |
| Transport Security | HTTPS only | Required |
| Security Headers | Required | Required for web app |
| CORS | Explicit configuration | No wildcard in production |

Required protections:

- SQL injection protection
- XSS protection
- CSRF protection where applicable
- Tenant isolation testing
- Permission bypass testing
- Secret scanning before merge

---

## 17. Development Tools

| Category | Standard Tool |
|---|---|
| IDE | VS Code |
| AI Coding | Claude Code |
| Architecture Review | ChatGPT |
| Source Control | GitHub |
| Project Management | Jira |
| UI/UX Design | Figma |
| Documentation | Markdown |
| Knowledge Base | Confluence |
| Automation | Make |

---

## 18. AI Collaboration Standard

### Claude Code

Claude Code is responsible for:

- Backend implementation
- Frontend implementation
- API implementation
- Unit tests
- Refactoring
- Bug fixes
- Code documentation

Claude Code must not:

- Change architecture without approval
- Introduce a new framework without Architecture Review
- Remove tenant isolation
- Bypass authentication or authorization
- Copy protected source code into SMEsPlus
- Merge or release without gate approval

### ChatGPT

ChatGPT is responsible for:

- SaaS architecture
- Functional specification
- Database design review
- Technical review
- Code review guidance
- Governance control
- Security review
- Evidence gate reporting

### Make

Make is responsible for:

- Workflow automation
- Jira integration
- GitHub integration
- Email/Slack notification
- Evidence automation where approved

---

## 19. Recommended Repository Structure

```text
99_SMEsPlus_Enterprise_Suite/
├── 00_PROJECT_STANDARD/
│   ├── TECHNOLOGY_STACK_STANDARD.md
│   ├── CODING_STANDARD.md
│   ├── SECURITY_STANDARD.md
│   ├── API_STANDARD.md
│   ├── DATABASE_STANDARD.md
│   └── UI_UX_STANDARD.md
├── 01_SaaS_Foundation/
├── 02_Functional_Design/
├── 03_Database_Design/
├── 04_API_Design/
├── 05_Frontend_Design/
├── 06_Engineering/
├── 07_Infrastructure/
├── 08_QA_UAT/
└── 09_AI_Collaboration/
```

---

## 20. Coding Standards

Required principles:

- Clean Architecture
- SOLID principles
- DRY
- KISS
- RESTful API
- Repository pattern where appropriate
- Dependency injection
- Domain-driven boundaries
- Type safety
- Secure by default
- Tenant-aware code
- Audit-aware code

---

## 21. Naming Standards

| Area | Standard |
|---|---|
| Frontend Components | PascalCase |
| Backend Functions | snake_case |
| Database Tables | snake_case |
| API Resources | kebab-case |
| Environment Variables | UPPER_CASE |
| Branch Names | feature/ERPPLUS-000-description |
| Pull Requests | ERPPLUS-000: short description |

---

## 22. Version Policy

Use Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

Examples:

```text
v1.0.0
v1.1.0
v1.1.5
v2.0.0
```

---

## 23. Future Technologies Reserved for Review

The following technologies are not approved by default and require Architecture Review before adoption:

- GraphQL
- gRPC
- Kubernetes
- Apache Kafka
- OpenSearch
- ClickHouse
- Vector Database
- AI Agent Framework
- Microservice split beyond approved boundaries

---

## 24. Mandatory Technology Decision Rules

The following technologies are mandatory for the current baseline unless formally approved otherwise:

- Next.js
- React
- TypeScript
- Tailwind CSS
- FastAPI
- Python
- REST API
- PostgreSQL
- SQLAlchemy
- Alembic
- Redis
- MinIO
- Docker
- Nginx
- Proxmox
- GitHub
- Jira
- Figma
- Claude Code
- ChatGPT
- Make

No alternative framework may be introduced without Architecture Review.

---

## 25. Terminology Standard

Use **Open ERP** for all SMEsPlus architecture, design, standards, and functional documents.

Do not use a specific ERP product name as the general architecture term.

Allowed exceptions:

- When referring to a specific product, source, API, ORM, license, or documentation by its legal/product name.
- When recording evidence from external reference systems.
- When performing clean-room learning or fit/gap review where the original product name is required for traceability.

Required replacement rule:

| Avoid | Use |
|---|---|
| Odoo-first | Open ERP-first |
| Odoo Architecture | Open ERP Architecture |
| Odoo Module | Open ERP Module |
| Odoo Standard | Open ERP Standard |
| Odoo Database | Open ERP Database |
| Odoo Integration | Open ERP Integration |
| Odoo Localization | Open ERP Thai Localization |

---

## 26. Executive Summary

This document is the official Technology Stack baseline for the SMEsPlus Enterprise Suite.

All implementation, documentation, architecture, coding, testing, deployment, and AI-generated artifacts must comply with this standard.

Any deviation requires Architecture Review and formal approval.

**End of Document**
