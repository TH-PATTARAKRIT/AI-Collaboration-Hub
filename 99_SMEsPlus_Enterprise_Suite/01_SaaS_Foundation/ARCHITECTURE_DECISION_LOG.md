ARCHITECTURE_DECISION_LOG.md

Version: v1.0.0
Status: Approved Baseline
Owner: SMEsPlus Product & Architecture Team
Target Path: 01_SaaS_Foundation/ARCHITECTURE_DECISION_LOG.md

## 1. Purpose

Architecture Decision Log (ADL) เป็นทะเบียนกลางของการตัดสินใจเชิงสถาปัตยกรรม (Architecture Decisions)

มีหน้าที่
- บันทึกการตัดสินใจ
- อ้างอิง ADR
- แสดงสถานะของแต่ละ Decision
- ป้องกันการตัดสินใจซ้ำ
- ช่วยตรวจสอบย้อนหลัง

เอกสารนี้เป็น Index ของ ADR ทั้งหมด รายละเอียดของแต่ละ Decision อยู่ในโฟลเดอร์ `ADR/`

## 2. Decision Lifecycle

ทุก Decision ต้องผ่านขั้นตอนดังนี้

```text
Proposed
   │
   ▼
Architecture Review
   │
   ▼
Approved
   │
   ▼
Implemented
   │
   ▼
Verified
   │
   ▼
Archived (ถ้ามีการแทนที่)
```

## 3. Decision Status

| Status | Meaning |
|---|---|
| Proposed | ยังไม่ได้ Review |
| Under Review | กำลังพิจารณา |
| Approved | ใช้งานเป็นมาตรฐาน |
| Implemented | นำไปใช้แล้ว |
| Deprecated | เลิกใช้ |
| Superseded | ถูกแทนที่โดย ADR ใหม่ |

## 4. Architecture Decision Register

| ADR | Title | Status | Owner | Related Documents |
|---|---|---|---|---|
| ADR-0001 | SaaS First Architecture | Approved | Solution Architect | Architecture Principles |
| ADR-0002 | Multi-Tenant by Design | Approved | Solution Architect | Security / Database |
| ADR-0003 | API First Development | Approved | Backend Lead | API Guideline |
| ADR-0004 | Modular Monolith for MVP | Approved | Architecture Board | SDS |
| ADR-0005 | PostgreSQL Primary Database | Approved | DBA Lead | Database Standards |
| ADR-0006 | RBAC + ABAC + RLS | Approved | Security Lead | Permission Matrix |
| ADR-0007 | Audit by Design | Approved | Security Lead | Audit Architecture |
| ADR-0008 | Kubernetes Deployment | Approved | DevOps Lead | Deployment |
| ADR-0009 | Redis Cache Layer | Approved | Backend Lead | Performance |
| ADR-0010 | Event Driven Integration | Approved | Integration Lead | Event Catalog |

> **Evidence Note:** This register lists the approved decisions. The underlying `ADR/ADR-XXXX-*.md` files (one per row, per the Decision Rule in Section 6) are the authoritative evidence and must exist before a row can be counted as complete progress, per the project's No Evidence = No Progress rule.

## 5. Decision Classification

**Business Decision** — เช่น SaaS Pricing, Subscription Plan Strategy

**Functional Decision** — เช่น Approval Flow, Module Activation, Notification Strategy

**Technical Decision** — เช่น Database, API, Cache, Queue, Logging

**Security Decision** — เช่น JWT, MFA, OAuth, Encryption

**Infrastructure Decision** — เช่น Kubernetes, Docker, GitHub Actions

## 6. Decision Rule

Architecture Decision ต้องมี

- Context
- Problem Statement
- Decision
- Alternatives
- Consequences
- Review Date

ห้ามสร้าง ADR ที่ไม่มีข้อมูลครบ

## 7. Review Frequency

Decision ต้อง Review อย่างน้อย

- ทุก Major Release
- หรือ เมื่อมี Breaking Change

## 8. Decision Priority

หากเกิด Conflict ให้ใช้ลำดับดังนี้

1. Security
2. Compliance
3. Tenant Isolation
4. Data Integrity
5. Availability
6. Performance
7. Cost

## 9. Required ADR

ก่อน Release Foundation ต้องมี ADR อย่างน้อย

- SaaS First
- Multi Tenant
- API First
- Security
- Database
- Deployment
- Audit
- Integration

## 10. Related Documents

- README.md
- DOCUMENT_MAP.md
- ARCHITECTURE_PRINCIPLES.md
- ARCHITECTURE_GOVERNANCE.md
- ADR/*
- TRACEABILITY_MATRIX.md
- CHANGELOG.md
- VERSION_HISTORY.md

## 11. Success Criteria

Architecture Decision Log ถือว่าสมบูรณ์เมื่อ

- ทุก Major Decision มี ADR
- ไม่มี ADR ซ้ำ
- ทุก ADR เชื่อมโยงเอกสารที่เกี่ยวข้อง
- ทุก Breaking Change มี ADR ใหม่
- ADR ทุกฉบับมีสถานะชัดเจน
