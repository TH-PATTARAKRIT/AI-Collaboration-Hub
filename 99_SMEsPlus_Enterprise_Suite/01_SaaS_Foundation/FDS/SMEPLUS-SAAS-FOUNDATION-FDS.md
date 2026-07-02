# SMEsPlus SaaS Foundation — Functional Design Specification (Master Index)

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-000
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss
Target Path: `01_SaaS_Foundation/FDS/SMEPLUS-SAAS-FOUNDATION-FDS.md`
Related ADR: ADR-0001 (SaaS First), ADR-0002 (Multi-Tenant), ADR-0006 (RBAC/ABAC/RLS)
Related Requirement Source: `12_Traceability/Requirement_Matrix/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX.md`

## Purpose

เอกสารชุดนี้เป็น Functional Design Specification (FDS) ของโมดูล **SaaS Foundation** ซึ่งเป็นชั้นรากฐานของ SMEsPlus Enterprise Suite ครอบคลุมการจัดการ tenant, ผู้ใช้งาน, สิทธิ์การเข้าถึง, subscription และการเปิดใช้งานโมดูล

FDS ฉบับนี้เป็นเอกสารต้นทาง (source of truth) สำหรับ SDS, API, Database, Security, UI, QA และ DevOps ของ SaaS Foundation ตาม Dependency Rule ใน `DOCUMENT_MAP.md`:

```text
FDS → SDS → API / Database / UI / Security → QA → DevOps / Deployment
```

## Document Set

| # | Document | Purpose |
|---|---|---|
| 01 | `01_DOCUMENT_CONTROL.md` | version, ownership, approval, change history |
| 02 | `02_BUSINESS_CONTEXT.md` | business background, scope, stakeholders |
| 03 | `03_FUNCTIONAL_REQUIREMENTS.md` | FR-FD-001 to FR-FD-004 with evidence status |
| 04 | `04_NON_FUNCTIONAL_REQUIREMENTS.md` | performance, scalability, availability, security NFRs |
| 05 | `05_DOMAIN_MODEL.md` | core entities and relationships |
| 06 | `06_USER_STORIES.md` | user stories per persona |
| 07 | `07_USE_CASES.md` | detailed use case flows |
| 08 | `08_SECURITY_REQUIREMENTS.md` | tenant isolation, RBAC/ABAC, RLS requirements |
| 09 | `09_INTEGRATION_REQUIREMENTS.md` | internal/external integration points |
| 10 | `10_ACCEPTANCE_CRITERIA.md` | Given/When/Then acceptance criteria per FR |

## Evidence Baseline

การเขียน FR ในเอกสารชุดนี้อ้างอิงผลจาก Evidence Matching Round ที่ทำไปแล้วบน SaaS Foundation (FD-001 to FD-030) ตาม ADR-0002 (Evidence-Driven Functional Specification) และ ADR-0003 (As-Is Before To-Be) — ห้ามเขียน requirement ใหม่ที่ขัดแย้งกับผล evidence matching เดิมโดยไม่มีการ re-verify

| FR ID | Title | Evidence Status (last matching round) |
|---|---|---|
| FR-FD-001 | Tenant Management & Isolation | PARTIAL |
| FR-FD-002 | User Role & Permission Management (RBAC) | PARTIAL |
| FR-FD-003 | Subscription Package Management | GAP — no evidence, new build required |
| FR-FD-004 | Module Activation & Licensing | PARTIAL |

> Evidence status ต้องถูก re-verify ทุกครั้งที่มีการอัปเดต FR — ดู `03_FUNCTIONAL_REQUIREMENTS.md` ส่วน Evidence Reference

## Reading Order

1. `01_DOCUMENT_CONTROL.md`
2. `02_BUSINESS_CONTEXT.md`
3. `03_FUNCTIONAL_REQUIREMENTS.md`
4. `04_NON_FUNCTIONAL_REQUIREMENTS.md`
5. `05_DOMAIN_MODEL.md`
6. `06_USER_STORIES.md`
7. `07_USE_CASES.md`
8. `08_SECURITY_REQUIREMENTS.md`
9. `09_INTEGRATION_REQUIREMENTS.md`
10. `10_ACCEPTANCE_CRITERIA.md`

## Approval Rule

เอกสารทั้งชุดนี้ต้องผ่าน PMO AI (process/evidence check) และ Enterprise Architect AI (technical completeness) ก่อนเสนอ Boss อนุมัติเป็น Status: Approved Baseline

จนกว่าจะได้รับการอนุมัติ สถานะของทุกไฟล์ในชุดนี้คือ **Draft — In Review** และห้ามใช้เป็นฐานสำหรับ SDS/API/Database implementation

## Registry Note

โฟลเดอร์ `FDS/` และไฟล์ชุดนี้ต้องถูกบันทึกใน `repository-contract/FOLDER_REGISTRY.yaml` / `DOCUMENT_REGISTRY.yaml` และ `01_SaaS_Foundation/DOCUMENT_MAP.md` ต้องได้รับการอัปเดตให้ตรงกับรายการไฟล์จริงชุดนี้ (เดิม DOCUMENT_MAP.md ระบุไว้เพียง 2 ไฟล์: `SMEPLUS-SAAS-FOUNDATION-FDS.md`, `FDS_TEMPLATE.md`) — ตาม Approval Rule ของ DOCUMENT_MAP.md

## Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial draft of 10-file FDS structure created per Boss instruction | Functional Specification AI (Claude) |
