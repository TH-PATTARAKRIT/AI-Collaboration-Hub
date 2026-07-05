# TRACEABILITY_MATRIX.md

Version: v1.1
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Scope: `01_SaaS_Foundation`

---

# Purpose

Requirements Traceability Matrix (RTM) เป็นเอกสารสำหรับเชื่อมโยง Requirement ตั้งแต่ Business Requirement ไปจนถึง Production Deployment

วัตถุประสงค์

- ตรวจสอบย้อนกลับ (End-to-End Traceability)
- ลด Requirement ตกหล่น
- สนับสนุน Architecture Governance
- สนับสนุน PMO Gate Control
- สนับสนุน Audit
- รองรับ AI-assisted Engineering

Repository นี้ถือเป็น **Single Source of Truth** สำหรับการติดตาม Requirement

---

# Traceability Model

```text
Business Requirement
        │
        ▼
Business Process
        │
        ▼
Functional Design (FDS)
        │
        ▼
Software Design (SDS)
        │
        ▼
API Specification
        │
        ▼
Database Design
        │
        ▼
UX / Screen Specification
        │
        ▼
Source Code
        │
        ▼
Unit Test
        │
        ▼
Integration Test
        │
        ▼
User Acceptance Test
        │
        ▼
Release Readiness
        │
        ▼
Production Deployment
```

---

# Traceability Levels

| Level | Description |
|--------|-------------|
| L1 | Business Requirement |
| L2 | Business Process |
| L3 | Functional Design |
| L4 | Software Design |
| L5 | API |
| L6 | Database |
| L7 | UX |
| L8 | Source Code |
| L9 | Test |
| L10 | Deployment |

---

# Requirement Identifier Standard

| Prefix | Description |
|---------|-------------|
| BR | Business Requirement |
| BP | Business Process |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| SDS | Software Design |
| API | API Specification |
| DB | Database |
| UX | User Experience |
| SRC | Source Code |
| SEC | Security |
| TC | Test Case |
| UAT | User Acceptance Test |
| ADR | Architecture Decision |

Example

```
BR-001
 ↓
BP-001
 ↓
FR-001
 ↓
SDS-001
 ↓
API-001
 ↓
DB-001
 ↓
UX-001
 ↓
SRC-001
 ↓
TC-001
 ↓
UAT-001
```

---

# Foundation Traceability Matrix

| BR | FR | SDS | API | DB | UX | SRC | TC | UAT | Evidence |
|----|----|-----|-----|----|----|-----|----|-----|----------|
| BR-001 | FR-001 | SDS-TENANT | API-TENANT | DB-TENANT | UX-TENANT | SRC-TENANT | TC-001 | UAT-001 | Pending |
| BR-002 | FR-002 | SDS-COMPANY | API-COMPANY | DB-COMPANY | UX-COMPANY | SRC-COMPANY | TC-002 | UAT-002 | Pending |
| BR-003 | FR-003 | SDS-IAM | API-USERS | DB-USERS | UX-USERS | SRC-USERS | TC-003 | UAT-003 | Pending |
| BR-004 | FR-004 | SDS-MODULE | API-MODULE | DB-MODULE | UX-MODULE | SRC-MODULE | TC-004 | UAT-004 | Pending |
| BR-005 | FR-005 | SDS-APPROVAL | API-APPROVAL | DB-APPROVAL | UX-APPROVAL | SRC-APPROVAL | TC-005 | UAT-005 | Pending |

---

# Non-Functional Requirement Traceability

| NFR | Description | SDS | Test |
|------|-------------|------|------|
| NFR-001 | Performance | SDS-PERFORMANCE | LOAD TEST |
| NFR-002 | Availability | SDS-INFRA | HA TEST |
| NFR-003 | Security | SECURITY | PEN TEST |
| NFR-004 | Scalability | SDS-INFRA | STRESS TEST |
| NFR-005 | Backup & Recovery | DEPLOYMENT | RESTORE TEST |
| NFR-006 | Monitoring | DEVOPS | OBSERVABILITY TEST |

---

# Change Impact Analysis

เมื่อมีการเปลี่ยนแปลง Requirement

ต้องตรวจสอบผลกระทบอย่างน้อย

- Business Process
- FDS
- SDS
- API
- Database
- UX
- Source Code
- Security
- Test
- UAT
- Documentation
- Deployment

---

# Traceability Rules

- ทุก BR ต้องมี BP
- ทุก BP ต้องมี FR
- ทุก FR ต้องมี SDS
- ทุก SDS ต้องมี API
- ทุก API ต้องมี Database Design
- ทุก UX ต้องอ้างอิง FR
- ทุก Source Code ต้องอ้างอิง SDS
- ทุก Test ต้องอ้างอิง Requirement
- ทุก UAT ต้องอ้างอิง Test Case

หากไม่เป็นไปตามกฎ ให้ถือว่ายังไม่ผ่าน Design Review

---

# Evidence Rule

No Evidence = No Progress

ทุก Requirement ต้องมี

- Document Reference
- Source Reference
- Test Evidence
- Review Evidence
- Approval Evidence

ก่อนเข้าสู่ Build Gate

---

# PMO Gate Control

ทุก Requirement ต้องผ่าน

```text
Architecture Review
        ↓
Design Review
        ↓
Code Review
        ↓
QA Review
        ↓
UAT Approval
        ↓
Release Approval
        ↓
Production Approval
```

---

# AI Traceability

AI-generated artifacts ต้องสามารถตรวจสอบได้ว่า

- AI Platform
- Prompt Reference
- Human Reviewer
- Review Date
- Approval Status

ก่อนนำไปใช้งานจริง

---

# Coverage Metrics

| Metric | Target |
|---------|--------|
| Requirement Coverage | 100% |
| API Coverage | 100% |
| Database Coverage | 100% |
| UX Coverage | 100% |
| Source Code Coverage | 100% |
| Test Coverage | 100% |
| UAT Coverage | 100% |
| Traceability Coverage | 100% |

---

# Related Documents

- README.md
- DOCUMENT_MAP.md
- ARCHITECTURE_PRINCIPLES.md
- ARCHITECTURE_GOVERNANCE.md
- SMEPLUS-SAAS-FOUNDATION-FDS.md
- SDS_FOUNDATION.md
- OPENAPI_FOUNDATION.yaml
- ERD_FOUNDATION.md
- SCREEN_SPEC_FOUNDATION.md
- TEST_STRATEGY.md
- UAT_SCENARIOS.md
- ARCHITECTURE_DECISION_LOG.md

---

# Success Criteria

Requirements Traceability Matrix ถือว่าสมบูรณ์เมื่อ

- ไม่มี Requirement Orphan
- ไม่มี Source Code Orphan
- ไม่มี API Orphan
- ไม่มี Database Object Orphan
- ไม่มี UX Orphan
- ไม่มี Test Case Orphan
- ไม่มี UAT Orphan
- Coverage ทุกด้านเท่ากับ 100%
- ผ่าน PMO Gate Control
- ผ่าน Architecture Review
- มี Evidence ครบทุก Requirement
