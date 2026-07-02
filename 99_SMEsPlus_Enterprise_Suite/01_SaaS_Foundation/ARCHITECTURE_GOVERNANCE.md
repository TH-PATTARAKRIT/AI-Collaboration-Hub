ARCHITECTURE_GOVERNANCE.md

Version: v1.0
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Target Path: 01_SaaS_Foundation/ARCHITECTURE_GOVERNANCE.md

## 1. Purpose

เอกสารนี้กำหนดกระบวนการกำกับดูแล (Architecture Governance) เพื่อให้การออกแบบ การพัฒนา และการเปลี่ยนแปลงสถาปัตยกรรมของ SMEsPlus มีมาตรฐานเดียวกัน สามารถตรวจสอบย้อนกลับได้ และลดความเสี่ยงจากการตัดสินใจที่ไม่สอดคล้องกัน

Architecture Governance ใช้กับทุกทีมที่มีผลต่อ Architecture ของระบบ

## 2. Objectives

Architecture Governance มีวัตถุประสงค์เพื่อ

- รักษา Architecture Baseline
- ป้องกันการเกิด Architecture Drift
- กำหนดกระบวนการอนุมัติการเปลี่ยนแปลง
- เพิ่ม Traceability ระหว่าง Requirement และ Implementation
- รักษา Security และ Tenant Isolation
- สนับสนุนการขยายระบบในอนาคต

## 3. Governance Scope

ใช้กับ

- Functional Architecture
- Software Design
- API Design
- Database Design
- Security Design
- Deployment Architecture
- DevOps
- Infrastructure
- Integration
- AI Services

## 4. Governance Roles

| Role | Responsibility |
|---|---|
| Product Owner | อนุมัติ Business Requirement และ Scope |
| Solution Architect | ออกแบบ Architecture และตรวจสอบความสอดคล้อง |
| Technical Lead | ตรวจสอบการออกแบบระดับ Implementation |
| Backend Lead | รับผิดชอบ Service, API และ Database |
| Frontend Lead | รับผิดชอบ UI Architecture และ UX Consistency |
| Security Lead | ตรวจสอบ Security, RBAC, ABAC และ Compliance |
| DevOps Lead | ตรวจสอบ Deployment และ Infrastructure |
| QA Lead | ตรวจสอบ Traceability และ Test Coverage |
| Architecture Review Board (ARB) | อนุมัติ Architecture Decision ที่มีผลกระทบระดับระบบ |

## 5. Governance Principles

ทุกการเปลี่ยนแปลงต้อง

- มีเหตุผลทางธุรกิจหรือเทคนิค
- มี ADR รองรับ (ถ้ามีผลต่อ Architecture)
- ไม่ละเมิด Architecture Principles
- ไม่ทำให้ Tenant Isolation ลดลง
- ไม่ลดระดับ Security
- มีผลกระทบที่ประเมินได้
- มีแผน Rollback หากจำเป็น

## 6. Change Classification

### Minor Change

ตัวอย่าง
- แก้ข้อความในเอกสาร
- ปรับชื่อฟิลด์ที่ไม่กระทบ API
- ปรับปรุงคำอธิบาย

**Approval:** Technical Lead

### Moderate Change

ตัวอย่าง
- เพิ่ม API
- เพิ่มตารางใหม่
- เพิ่มหน้าจอใหม่
- เพิ่ม Permission

**Approval:** Technical Lead + Solution Architect

### Major Change

ตัวอย่าง
- เปลี่ยน Database Strategy
- เปลี่ยน Authentication
- เปลี่ยน Multi-Tenant Model
- เปลี่ยน Deployment Architecture
- เปลี่ยน Security Model

**Approval:** Architecture Review Board (ARB) — ADR Required

## 7. Architecture Review Workflow

```text
Business Requirement
       │
       ▼
Functional Review
       │
       ▼
Architecture Review
       │
       ▼
ADR (ถ้าจำเป็น)
       │
       ▼
Solution Approval
       │
       ▼
SDS Update
       │
       ▼
API / Database / UI Update
       │
       ▼
QA Review
       │
       ▼
Implementation
```

## 8. Architecture Review Checklist

ทุก Review ต้องตอบคำถามต่อไปนี้

**Business**
- Requirement ชัดเจนหรือไม่
- อยู่ใน Scope หรือไม่

**SaaS**
- รองรับ Multi-Tenant หรือไม่
- Tenant Isolation ถูกต้องหรือไม่

**Security**
- Authentication ถูกต้องหรือไม่
- Authorization ถูกต้องหรือไม่
- Audit ครบหรือไม่

**API**
- Version หรือไม่
- Backward Compatible หรือไม่

**Database**
- Normalization เหมาะสมหรือไม่
- Index เพียงพอหรือไม่
- RLS ครบหรือไม่

**UI**
- Permission ถูกต้องหรือไม่
- Error State ครบหรือไม่

**QA**
- Test Case ครบหรือไม่
- UAT ครบหรือไม่

## 9. Required Deliverables

ก่อนเริ่ม Development ต้องมี

- Approved FDS
- Approved SDS
- Approved API Contract
- Approved ERD
- Approved Permission Matrix
- Approved Screen Specification
- Approved Test Strategy
- Updated Traceability Matrix

หากเอกสารข้อใดขาด ให้ถือว่ายังไม่ผ่าน Design Gate

## 10. Architecture Gates

**Gate A — Business Approval**
Output: Business Scope, Requirement

**Gate B — Architecture Approval**
Output: Architecture Documents, ADR

**Gate C — Design Approval**
Output: SDS, API, Database, UI

**Gate D — Development Ready**
Output: Sprint Backlog, Test Strategy, Development Readiness Checklist

**Gate E — Production Ready**
Output: UAT Passed, Security Review Passed, Performance Test Passed, Go-Live Checklist Completed

## 11. Document Governance

เอกสารทุกไฟล์ต้องมี

- Version
- Status
- Owner
- Reviewer
- Last Updated
- Related Documents
- Approval Status

## 12. Versioning Policy

ใช้ Semantic Versioning

- Major — เปลี่ยน Architecture หรือ Breaking Change
- Minor — เพิ่ม Capability โดยไม่ทำลายของเดิม
- Patch — แก้ไขเอกสารหรือข้อผิดพลาด

ตัวอย่าง: v1.0.0, v1.1.0, v1.1.1

## 13. Architecture Decision Requirement

ต้องสร้าง ADR เมื่อมีการเปลี่ยนแปลงเกี่ยวกับ

- Security
- Authentication
- Authorization
- Database Strategy
- Multi-Tenant
- Deployment
- Integration
- Event Model
- Public API
- Module Architecture

## 14. Compliance

Architecture Governance นี้เป็นข้อบังคับสำหรับเอกสารภายใต้

- FDS/
- SDS/
- API/
- DATABASE/
- SECURITY/
- UI/
- QA/
- DEVOPS/
- DEPLOYMENT/

## 15. Related Documents

- README.md
- DOCUMENT_MAP.md
- ARCHITECTURE_PRINCIPLES.md
- ARCHITECTURE_DECISION_LOG.md
- TRACEABILITY_MATRIX.md
- VERSION_HISTORY.md
- CHANGELOG.md
- ADR/*

## 16. Governance Success Criteria

Architecture Governance ถือว่าสำเร็จเมื่อ

- ทุก Requirement เชื่อมโยงถึง Test Case ได้
- ทุก Major Decision มี ADR
- ทุก Breaking Change ผ่าน ARB
- ทุก Release ผ่าน Architecture Gate
- ไม่พบ Architecture Drift ระหว่าง Design และ Implementation
