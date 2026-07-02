# 05 — Domain Model

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-005
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss

## 1. Purpose

ระบุ core entity และความสัมพันธ์ระดับ conceptual ของ SaaS Foundation เพื่อเป็นฐานให้ SDS (`SDS/DOMAIN_MODEL.md`) และ Database (`DATABASE/ERD_FOUNDATION.md`) นำไปออกแบบรายละเอียดต่อ

> เอกสารนี้เป็น conceptual model เท่านั้น ไม่ใช่ ERD ระดับ physical schema — physical design อยู่ใน `DATABASE/`

## 2. Core Entities

| Entity | Description | Related FR |
|---|---|---|
| Tenant | หน่วยองค์กรลูกค้าหนึ่งรายที่สมัครใช้ SMEsPlus | FR-FD-001 |
| User | ผู้ใช้งานที่ผูกกับ tenant หนึ่งราย | FR-FD-002 |
| Role | ชุดสิทธิ์มาตรฐาน (Tenant Admin, Manager, Standard User, Read-only) | FR-FD-002 |
| Permission | สิทธิ์ระดับ module/field ที่ผูกกับ Role | FR-FD-002 |
| Subscription | บันทึกการสมัครใช้งาน tier ของ tenant | FR-FD-003 |
| SubscriptionTier | นิยาม feature flag และโมดูลที่รวมอยู่ในแต่ละ tier | FR-FD-003 |
| Module | โมดูลธุรกิจที่สามารถเปิด/ปิดได้ต่อ tenant | FR-FD-004 |
| ModuleActivation | บันทึกสถานะการเปิดใช้งานโมดูลต่อ tenant | FR-FD-004 |
| AuditLog | บันทึกเหตุการณ์สำคัญทุกรายการที่เกี่ยวกับ security/subscription/module | NFR-AUDIT-01/02 |

## 3. Entity Relationships (Conceptual)

```text
Tenant (1) ──── (N) User
Tenant (1) ──── (N) Subscription
Tenant (1) ──── (N) ModuleActivation

User (N) ──── (1) Role
Role (N) ──── (N) Permission

Subscription (N) ──── (1) SubscriptionTier
SubscriptionTier (1) ──── (N) Module   [modules included in tier]

ModuleActivation (N) ──── (1) Module
ModuleActivation (N) ──── (1) Tenant

AuditLog (N) ──── (1) Tenant
AuditLog (N) ──── (0..1) User          [actor, nullable for system events]
```

## 4. Entity Notes

**Tenant**
- Primary isolation boundary ของทั้งระบบ
- ทุก entity อื่นที่เป็น tenant-scoped ต้องมี foreign key อ้างอิง Tenant โดยตรงหรือโดยอ้อม

**User**
- ผูกกับ Tenant เดียวเท่านั้นในเวอร์ชันแรก (ไม่รองรับ multi-tenant user ในระยะแรก เว้นแต่มี ADR ใหม่)

**Role / Permission**
- Role เป็น template สิทธิ์ระดับ tenant สามารถ customize เพิ่มเติมได้ในระดับ tenant แต่ role มาตรฐาน 4 แบบต้องมีเสมอ

**Subscription / SubscriptionTier**
- SubscriptionTier เป็น master data ระดับ system (ไม่ผูก tenant) — Subscription คือ instance ที่ tenant สมัครใช้ tier นั้น
- Subscription ต้องมี state: Active, Expired, Cancelled, Pending Renewal

**Module / ModuleActivation**
- Module เป็น master data ระดับ system ที่ registry ไว้ (Accounting, Purchase, Inventory ฯลฯ)
- ModuleActivation คือความสัมพันธ์ many-to-many ระหว่าง Tenant และ Module พร้อมสถานะ (Active/Inactive) และ timestamp

**AuditLog**
- Append-only, ห้ามแก้ไขหรือลบย้อนหลัง

## 5. Open Design Questions (สำหรับ SDS/Database ตัดสินใจต่อ)

1. Tenant isolation จะใช้ Row-Level Security (RLS) เพียงอย่างเดียว หรือใช้ schema-per-tenant สำหรับ tenant ขนาดใหญ่ — ต้องมี ADR
2. Role customization ระดับ tenant จะเก็บเป็น override หรือ full copy ของ Role template
3. SubscriptionTier เปลี่ยนแปลง (เพิ่ม/ลด module) มีผลย้อนหลังกับ Subscription ที่ active อยู่หรือไม่

## 6. Related Documents

- `03_FUNCTIONAL_REQUIREMENTS.md`
- `SDS/DOMAIN_MODEL.md` (physical/service-level detail)
- `DATABASE/ERD_FOUNDATION.md`

## 7. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial conceptual domain model | Functional Specification AI (Claude) |
