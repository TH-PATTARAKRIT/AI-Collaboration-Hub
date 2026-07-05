# DOCUMENT_MAP.md

Version: v1.1
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Scope: `01_SaaS_Foundation`

---

# Purpose

เอกสารนี้เป็น **Document Navigation Guide** สำหรับ `01_SaaS_Foundation`

ใช้เป็นแผนที่นำทางเอกสารทั้งหมดของโครงการ เพื่อให้ทุกทีมเข้าใจว่า

- เอกสารแต่ละไฟล์มีหน้าที่อะไร
- ควรอ่านลำดับใด
- ความสัมพันธ์ระหว่างเอกสาร
- Dependency ระหว่างเอกสาร
- Traceability ของ Architecture

Document Map นี้ถือเป็น **Single Source of Truth** สำหรับการนำทางเอกสารภายใน Foundation

---

# AI Collaboration

Repository นี้รองรับการทำงานร่วมกันระหว่างทีมพัฒนาและ AI

รองรับ

- ChatGPT
- Claude Code
- GitHub Copilot
- Future AI Agents

AI ทุกตัวต้องอ้างอิง Repository นี้เป็นมาตรฐานเดียวกัน

AI-generated outputs ต้องสอดคล้องกับ

- Architecture Principles
- Architecture Governance
- Traceability Matrix
- Security Standards
- Repository Structure

---

# Canonical Document Flow

```text
Business Vision
        ↓
Architecture Principles
        ↓
Architecture Decision Records (ADR)
        ↓
Functional Design Specification (FDS)
        ↓
Software Design Specification (SDS)
        ↓
API
DB
Security
UX
        ↓
Development
        ↓
QA
        ↓
Deployment
```

---

# Document Groups

## 1. Foundation Governance

| Document | Purpose |
|----------|---------|
| README.md | Entry Point |
| DOCUMENT_MAP.md | Document Navigation |
| GLOSSARY.md | Common Terminology |
| ARCHITECTURE_PRINCIPLES.md | Design Principles |
| ARCHITECTURE_GOVERNANCE.md | Governance Process |
| ARCHITECTURE_DECISION_LOG.md | Architecture Decisions |
| TRACEABILITY_MATRIX.md | Requirement Traceability |
| VERSION_HISTORY.md | Version Control |
| CHANGELOG.md | Change History |

---

## 2. Architecture Decision Records

Folder

```
ADR/
```

Purpose

Architecture Decision Records

ตัวอย่าง

- ADR_TEMPLATE.md
- ADR-0001-SaaS-First.md
- ADR-0002-Multi-Tenant.md
- ADR-0003-API-First.md
- ADR-0004-Modular-Monolith.md
- ADR-0005-PostgreSQL.md
- ADR-0006-RBAC-ABAC-RLS.md
- ADR-0007-Audit-By-Design.md
- ADR-0008-Kubernetes-Deployment.md

---

## 3. Functional Design

Folder

```
FDS/
```

Main Documents

- SMEPLUS-SAAS-FOUNDATION-FDS.md
- FDS_TEMPLATE.md

---

## 4. Software Design

Folder

```
SDS/
```

Main Documents

- SDS_FOUNDATION.md
- DOMAIN_MODEL.md
- SERVICE_CATALOG.md

---

## 5. API

Folder

```
API/
```

Main Documents

- OPENAPI_FOUNDATION.yaml
- API_GUIDELINE.md
- ERROR_CODE_STANDARD.md
- PAGINATION_STANDARD.md
- EVENT_CATALOG.md

---

## 6. Database

Folder

```
DB/
```

Main Documents

- ERD_FOUNDATION.md
- DATA_DICTIONARY.md
- DATABASE_STANDARDS.md

Migration

- 001_initial_schema.sql
- 002_rls_policy.sql
- 003_seed_data.sql

---

## 7. Security

Folder

```
SECURITY/
```

Main Documents

- SECURITY_ARCHITECTURE.md
- PERMISSION_MATRIX.md
- TENANT_ISOLATION.md
- SECURITY_CHECKLIST.md

---

## 8. UX

Folder

```
UX/
```

Main Documents

- SCREEN_SPEC_FOUNDATION.md
- UI_GUIDELINE.md
- FIGMA_MAPPING.md
- USER_FLOW.md

---

## 9. QA

Folder

```
QA/
```

Main Documents

- TEST_STRATEGY.md
- TEST_CASES.md
- TEST_DATA.md
- UAT_SCENARIOS.md

---

## 10. DevOps

Folder

```
DEVOPS/
```

Main Documents

- CI_CD.md
- DOCKER.md
- KUBERNETES.md
- ENVIRONMENT.md

---

## 11. Deployment

Folder

```
DEPLOYMENT/
```

Main Documents

- MIGRATION_PLAN.md
- DEPLOYMENT_READINESS_CHECKLIST.md
- GO_LIVE_CHECKLIST.md

---

# Recommended Reading Order

## Executive / PM

1. README.md
2. DOCUMENT_MAP.md
3. ARCHITECTURE_PRINCIPLES.md
4. FDS/
5. TRACEABILITY_MATRIX.md
6. DEPLOYMENT/

---

## Architect

1. README.md
2. Principles
3. Governance
4. ADR
5. FDS
6. SDS
7. API
8. DB
9. SECURITY

---

## Backend

1. SDS
2. API
3. DB
4. SECURITY

---

## Frontend

1. UX
2. API
3. SECURITY

---

## QA

1. FDS
2. TRACEABILITY_MATRIX
3. TEST_STRATEGY
4. TEST_CASES
5. UAT

---

## DevOps

1. DEVOPS
2. DEPLOYMENT

---

# Dependency Rule

```text
README
        ↓
Architecture Principles
        ↓
Architecture Governance
        ↓
ADR
        ↓
FDS
        ↓
SDS
        ↓
API
DB
SECURITY
UX
        ↓
Development
        ↓
QA
        ↓
Deployment
```

---

# Maintenance Rule

เมื่อมีการเปลี่ยนแปลง

- Requirement
- Architecture
- API
- Database
- UX
- Security

ต้องอัปเดต

- CHANGELOG.md
- VERSION_HISTORY.md
- TRACEABILITY_MATRIX.md
- เอกสารต้นทาง
- เอกสารปลายทางที่ได้รับผลกระทบ

---

# Approval Rule

Document Map นี้ต้องได้รับการปรับปรุงทุกครั้งที่

- เพิ่มเอกสาร
- ลบเอกสาร
- เปลี่ยนชื่อเอกสาร
- เปลี่ยนโครงสร้าง Repository

เพื่อให้ Repository มี Document Navigation ที่ถูกต้องอยู่เสมอ

---

# Executive Note

Document Map นี้เป็นจุดเริ่มต้นของการเรียนรู้ Repository ทั้งหมด

ทุกทีม รวมถึง AI ต้องอ้างอิงลำดับเอกสารตาม Document Map นี้ เพื่อให้การออกแบบ การพัฒนา การทดสอบ และการ Deploy เป็นไปในมาตรฐานเดียวกัน
