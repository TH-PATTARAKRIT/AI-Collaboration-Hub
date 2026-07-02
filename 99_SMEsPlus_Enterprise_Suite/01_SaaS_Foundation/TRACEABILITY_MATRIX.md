TRACEABILITY_MATRIX.md

Version: v1.0.0
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Target Path: 01_SaaS_Foundation/TRACEABILITY_MATRIX.md

## 1. Purpose

Requirements Traceability Matrix (RTM) เป็นเอกสารที่ใช้เชื่อมโยงข้อกำหนดทางธุรกิจ (Business Requirements) ไปจนถึงการทดสอบและการนำระบบขึ้นใช้งาน เพื่อให้สามารถตรวจสอบย้อนกลับ (Traceability) ได้ตลอดวงจรการพัฒนา

วัตถุประสงค์หลักคือ

- ยืนยันว่าทุก Requirement ได้รับการออกแบบ
- ยืนยันว่าทุก Requirement ได้รับการพัฒนา
- ยืนยันว่าทุก Requirement ได้รับการทดสอบ
- ลดความเสี่ยงจาก Requirement ตกหล่น
- สนับสนุนการตรวจสอบ (Audit) และ Governance

## 2. Traceability Model

```text
Business Requirement
       │
       ▼
Functional Requirement (FDS)
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
UI / Screen Specification
       │
       ▼
Implementation
       │
       ▼
Unit Test
       │
       ▼
Integration Test
       │
       ▼
UAT
       │
       ▼
Deployment Checklist
```

## 3. Traceability Levels

| Level | Description |
|---|---|
| L1 | Business Requirement |
| L2 | Functional Requirement |
| L3 | Software Design |
| L4 | API |
| L5 | Database |
| L6 | UI |
| L7 | Test |
| L8 | Release |

## 4. Requirement Identifier Standard

| Prefix | Description |
|---|---|
| BR | Business Requirement |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| SDS | Software Design |
| API | API Specification |
| DB | Database |
| UI | Screen |
| SEC | Security |
| TC | Test Case |
| UAT | User Acceptance Test |
| ADR | Architecture Decision |

ตัวอย่าง: `BR-001 → FR-001 → SDS-001 → API-001 → DB-001 → UI-001 → TC-001 → UAT-001`

## 5. Foundation Traceability Matrix

| BR | Title | FR | SDS | API | DB | UI | SEC | TC |
|---|---|---|---|---|---|---|---|---|
| BR-001 | Tenant Management | FR-001 | SDS-TENANT | API-TENANT | DB-TENANT | UI-TENANT | SEC-001 | TC-001 |
| BR-002 | Company Management | FR-002 | SDS-COMPANY | API-COMPANY | DB-COMPANY | UI-COMPANY | SEC-002 | TC-002 |
| BR-003 | User Management | FR-003 | SDS-IAM | API-USERS | DB-USERS | UI-USERS | SEC-003 | TC-003 |
| BR-004 | Module Activation | FR-004 | SDS-MODULE | API-MODULE | DB-MODULE | UI-MODULE | SEC-004 | TC-004 |
| BR-005 | Approval | FR-005 | SDS-APPROVAL | API-APPROVAL | DB-APPROVAL | UI-APPROVAL | SEC-005 | TC-005 |
| BR-006 | Notification | FR-006 | SDS-NOTIFICATION | API-NOTIFICATION | DB-NOTIFICATION | UI-NOTIFICATION | SEC-006 | TC-006 |
| BR-007 | Audit | FR-007 | SDS-AUDIT | API-AUDIT | DB-AUDIT | UI-AUDIT | SEC-007 | TC-007 |
| BR-008 | Integration | FR-008 | SDS-INTEGRATION | API-INTEGRATION | DB-INTEGRATION | UI-INTEGRATION | SEC-008 | TC-008 |

> **Evidence Note:** Each cell references a document/component ID that must exist as real evidence (e.g. `SDS-TENANT` section, `API-TENANT` endpoint group, `DB-TENANT` table set) before the row can be marked complete. IDs listed here are the target identifiers to be produced by FDS/SDS/API/DATABASE/UI/SECURITY/QA work, not yet confirmed as built.

## 6. Change Impact Analysis

เมื่อมีการเปลี่ยน Requirement ต้องตรวจสอบผลกระทบอย่างน้อยในหัวข้อ:

- FDS
- SDS
- API
- Database
- UI
- Security
- Test Cases
- UAT
- Documentation
- Deployment

ห้ามเปลี่ยน Requirement โดยไม่อัปเดต RTM

## 7. Traceability Rules

- ทุก BR ต้องมี FR อย่างน้อย 1 รายการ
- ทุก FR ต้องมี SDS รองรับ
- ทุก API ต้องอ้างอิง FR
- ทุก Database Object ต้องอ้างอิง SDS
- ทุก Screen ต้องอ้างอิง FR
- ทุก Test Case ต้องอ้างอิง Requirement
- ทุก UAT ต้องอ้างอิง Test Case

หากไม่เป็นไปตามกฎ ให้ถือว่าเอกสารยังไม่ผ่าน Design Review

## 8. Coverage Metrics

ต้องติดตามตัวชี้วัดต่อไปนี้

| Metric | Target |
|---|---|
| Requirement Coverage | 100% |
| API Coverage | 100% |
| Database Coverage | 100% |
| Screen Coverage | 100% |
| Test Coverage | 100% |
| UAT Coverage | 100% |
| Traceability Coverage | 100% |

## 9. Review Checklist

ก่อนอนุมัติ Release ต้องยืนยันว่า

- ไม่มี Requirement ที่ไม่มี Test
- ไม่มี API ที่ไม่มี Requirement
- ไม่มี Screen ที่ไม่มี Requirement
- ไม่มี Database Table ที่ไม่มี Design
- ไม่มี ADR ที่ขัดกับ Architecture Principles

## 10. Related Documents

- README.md
- DOCUMENT_MAP.md
- SMEPLUS-SAAS-FOUNDATION-FDS.md
- SDS_FOUNDATION.md
- OPENAPI_FOUNDATION.yaml
- ERD_FOUNDATION.md
- SCREEN_SPEC_FOUNDATION.md
- TEST_STRATEGY.md
- UAT_SCENARIOS.md
- ARCHITECTURE_DECISION_LOG.md

## 11. Success Criteria

Requirements Traceability Matrix ถือว่าสมบูรณ์เมื่อ

- Requirement ทุกข้อสามารถตรวจสอบย้อนกลับได้จนถึง UAT
- Coverage ทุกหมวดเป็น 100%
- ไม่มี Requirement Orphan
- ไม่มี Test Case Orphan
- ไม่มี API Orphan
- ไม่มี Database Object Orphan
