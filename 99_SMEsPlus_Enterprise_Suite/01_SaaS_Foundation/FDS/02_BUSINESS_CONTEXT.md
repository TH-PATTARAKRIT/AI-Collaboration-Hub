# 02 — Business Context

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-002
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss

## 1. Business Background

SMEsPlus Enterprise Suite เป็น SaaS ERP สำหรับตลาด SME ในประเทศไทยโดยเฉพาะ สร้างบน Odoo foundation พร้อม enterprise-control feature เพิ่มเติม จำหน่ายเฉพาะในประเทศไทย รูปแบบ deployment เป็น SaaS (multi-tenant)

จาก 14 module group ทั้งหมด มีเพียงกลุ่ม Accounting เท่านั้นที่ต้องการ localization เฉพาะประเทศไทย (`l10n_th`, `l10n_th_reports`) ส่วนอีก 13 กลุ่มใช้ standard Odoo functionality

**SaaS Foundation** คือชั้นรากฐานที่ทุกโมดูลธุรกิจ (Accounting, Purchase, Inventory, Sales, CRM ฯลฯ) ต้องพึ่งพา ได้แก่ tenant management, user/role management, subscription, และ module activation

## 2. Module Priority Context

| Priority | Modules |
|---|---|
| 1 | SaaS Foundation, Accounting, Purchase, Inventory |
| 2 | Sales, CRM, Product |
| 3 | Manufacturing, HR, Payroll |
| 4 | Remaining modules |

SaaS Foundation อยู่ใน Priority 1 เนื่องจากทุกโมดูลอื่นต้องพึ่งพา tenant isolation, RBAC และ subscription control ของ SaaS Foundation ก่อนจึงจะ deploy ได้

## 3. Business Goals

1. รองรับ multi-tenant SaaS ที่แยก data ระหว่าง tenant อย่างสมบูรณ์ (tenant isolation)
2. ควบคุมสิทธิ์การเข้าถึงตาม role และ subscription tier ของแต่ละ tenant
3. เปิด/ปิดการใช้งานโมดูลธุรกิจตาม subscription package ที่ tenant สมัคร
4. รองรับการขยายตัวของจำนวน tenant โดยไม่กระทบ performance หรือความปลอดภัยของ tenant อื่น

## 4. Stakeholders

| Stakeholder | Interest |
|---|---|
| Boss (Project Owner) | final approval, business direction |
| SME Customer (Tenant Admin) | สมัครใช้งาน, จัดการผู้ใช้ในองค์กรตนเอง |
| SME End User | ใช้งานโมดูลธุรกิจภายใต้สิทธิ์ที่ได้รับ |
| SMEsPlus Operations Team | ดูแล tenant provisioning, billing, support |
| Enterprise Architect AI | ควบคุม architecture ให้สอดคล้อง ADR |
| QA UAT AI | ตรวจสอบว่า foundation ทำงานถูกต้องก่อนปล่อยโมดูลอื่น |

## 5. In Scope

- Tenant registration, provisioning, and isolation
- User authentication and role-based access control (RBAC)
- Subscription package definition and management
- Module activation/deactivation per tenant per subscription
- Foundation-level audit logging

## 6. Out of Scope (for this FDS)

- Business logic ของแต่ละโมดูล (Accounting, Purchase ฯลฯ) — อยู่ใน FDS ของโมดูลนั้น ๆ
- Custom purchase approval extension (`purchase_request_level_reject` ฯลฯ) ที่มาจาก implementation partner `efaplus` — ถูกจัดเป็น Out of Scope / Retired ตามผล Evidence Matching
- Payment gateway integration รายละเอียด (อยู่ใน Integration FDS ของ Billing เมื่อมีการกำหนด scope)

## 7. Assumptions

- Odoo core version และ community module ที่ใช้เป็น foundation มี license ที่เหมาะสมสำหรับใช้เชิงพาณิชย์ในไทย
- Tenant ทั้งหมดใช้ shared database with row-level isolation (RLS) ตาม ADR-0002 / ADR-0006 เว้นแต่มีการเปลี่ยน decision
- ภาษาหลักของ UI คือภาษาไทย โดยมี English เป็นภาษารอง

## 8. Constraints

- ต้อง sold และ deploy เฉพาะตลาดไทยเท่านั้น
- ต้องปฏิบัติตาม No Evidence = No Progress ตลอดทุก state ของ AIOS 12-state framework
- Custom module ใด ๆ ที่พบใน production database แต่ไม่มี source ใน repository ต้องถูกสืบทวนแหล่งที่มาก่อนนำมานับเป็น scope (ดู TASK-005)

## 9. Related Documents

- `SMEPLUS-SAAS-FOUNDATION-FDS.md`
- `12_Traceability/Requirement_Matrix/SMEPLUS-GAP-ANALYSIS.md`
- `01_SaaS_Foundation/ARCHITECTURE_PRINCIPLES.md`

## 10. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial business context draft | Functional Specification AI (Claude) |
