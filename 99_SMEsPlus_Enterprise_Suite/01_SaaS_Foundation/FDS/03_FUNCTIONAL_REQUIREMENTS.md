# 03 — Functional Requirements

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-003
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss
Evidence Source: `12_Traceability/Requirement_Matrix/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX.md`

## 1. Purpose

ระบุ Functional Requirement (FR) ของโมดูล SaaS Foundation พร้อมสถานะ evidence จากรอบ Evidence Matching ที่ทำไปแล้ว ตาม ADR-0002 (Evidence-Driven Functional Specification)

## 2. Requirement Summary

| FR ID | Title | Priority | Evidence Status | Jira |
|---|---|---|---|---|
| FR-FD-001 | Tenant Management & Isolation | Must Have | PARTIAL | ERPPLUS-TBD |
| FR-FD-002 | User Role & Permission Management (RBAC) | Must Have | PARTIAL | ERPPLUS-TBD |
| FR-FD-003 | Subscription Package Management | Must Have | GAP | ERPPLUS-TBD |
| FR-FD-004 | Module Activation & Licensing | Must Have | PARTIAL | ERPPLUS-TBD |

> Jira key ต้องถูกเติมโดย PMO AI เมื่อสร้าง issue ใน project ERPPLUS จริง — ห้าม Claude Code AI สมมติเลข issue เอง

## 3. FR-FD-001 — Tenant Management & Isolation

**Description:** ระบบต้องสามารถสร้าง, จัดเก็บ, และแยก (isolate) ข้อมูลของแต่ละ tenant ออกจากกันอย่างสมบูรณ์ ไม่ว่าจะเป็นระดับ database row (RLS) หรือ schema

**Business Rule:**
- Tenant ID ต้องถูกผูกกับทุก record ที่เป็น tenant-scoped data
- ผู้ใช้ของ tenant หนึ่งต้องไม่สามารถ query หรือแก้ไขข้อมูลของ tenant อื่นได้ไม่ว่าด้วยวิธีใด
- การลบ tenant ต้องมีกระบวนการ soft-delete และ retention period ก่อน hard-delete

**Evidence Status:** PARTIAL — Odoo multi-company mechanism มีอยู่บางส่วน แต่ยังไม่มีหลักฐาน RLS policy ที่บังคับ tenant isolation ระดับ row สมบูรณ์ในฐานข้อมูล production ที่ตรวจสอบ

**Dependency:** ทุก FR อื่นในระบบต้องพึ่งพา FR-FD-001

## 4. FR-FD-002 — User Role & Permission Management (RBAC)

**Description:** ระบบต้องรองรับการกำหนด role และสิทธิ์ (permission) ให้กับผู้ใช้ในแต่ละ tenant โดยแยกอิสระต่อ tenant

**Business Rule:**
- Role มาตรฐานขั้นต่ำ: Tenant Admin, Manager, Standard User, Read-only User
- Permission ต้องกำหนดได้ทั้งระดับ module และระดับ field-level (สำหรับข้อมูลอ่อนไหว เช่น การเงิน)
- การเปลี่ยน role ต้องมี audit log

**Evidence Status:** PARTIAL — Odoo access rights / record rules มีกลไกพื้นฐานรองรับ แต่ยังไม่มีหลักฐานการ map role มาตรฐานของ SMEsPlus กับ Odoo groups อย่างเป็นทางการ

## 5. FR-FD-003 — Subscription Package Management

**Description:** ระบบต้องสามารถกำหนด subscription package/tier พร้อม feature flag ที่ผูกกับแต่ละ tier และจัดการวงจรชีวิตของ subscription ต่อ tenant (สมัคร, ต่ออายุ, อัปเกรด, ยกเลิก)

**Business Rule:**
- แต่ละ tenant ต้องมี subscription record ที่ active อย่างน้อย 1 รายการเสมอ เพื่อให้ระบบทราบว่าเปิดใช้โมดูลใดได้
- การหมดอายุ subscription ต้องปิดการเข้าถึงฟีเจอร์ตาม tier แบบ graceful (ไม่ลบข้อมูล)
- การอัปเกรด/ดาวน์เกรด tier ต้องปรับ module activation ให้สอดคล้องทันที

**Evidence Status:** GAP — ไม่พบ SubscriptionService, ตาราง `subscriptions`, `subscription_tiers`, หรือ `feature_flags` ใน source code หรือ database ที่ตรวจสอบ ต้อง design ใหม่ทั้งหมด

**Impact:** เป็น blocker ต่อ FR-FD-004 (Module Activation) — ต้อง design ก่อนเริ่ม build โมดูลธุรกิจอื่นที่ต้องอิงสิทธิ์ subscription

## 6. FR-FD-004 — Module Activation & Licensing

**Description:** ระบบต้องสามารถเปิด/ปิดการใช้งานโมดูลธุรกิจ (Accounting, Purchase, Inventory ฯลฯ) ต่อ tenant ตาม subscription package ที่ tenant นั้นสมัคร

**Business Rule:**
- โมดูลที่ไม่ได้อยู่ใน subscription tier ของ tenant ต้องไม่แสดงในเมนูและไม่สามารถเข้าถึงผ่าน API ได้
- การเปิดใช้งานโมดูลใหม่ต้องไม่กระทบข้อมูลของโมดูลอื่นที่เปิดใช้งานอยู่แล้ว
- ต้องมี log การเปิด/ปิดโมดูลต่อ tenant เพื่อการตรวจสอบย้อนหลัง

**Evidence Status:** PARTIAL — Odoo module installation mechanism (`ir.module.module`) รองรับการเปิด/ปิดโมดูลระดับ instance แต่ยังไม่มีหลักฐานการ enforce ระดับ tenant ภายใต้ shared database เดียวกัน

**Dependency:** ต้องพึ่งพา FR-FD-003 (Subscription) เพื่อทราบว่า tenant มีสิทธิ์เปิดโมดูลใดได้บ้าง

## 7. Requirement Traceability

FR ทั้งหมดในเอกสารนี้ต้องเชื่อมโยงกับ:
- ADR ที่เกี่ยวข้อง (ดู `05_DOMAIN_MODEL.md`, `08_SECURITY_REQUIREMENTS.md`)
- Acceptance Criteria (`10_ACCEPTANCE_CRITERIA.md`)
- Jira issue ใน project ERPPLUS (เติมโดย PMO AI)

## 8. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial FR set carried forward from Evidence Matching round | Functional Specification AI (Claude) |
