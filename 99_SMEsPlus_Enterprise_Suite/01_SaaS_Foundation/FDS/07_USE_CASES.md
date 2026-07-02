# 07 — Use Cases

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-007
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss

## 1. Purpose

ระบุ use case flow ระดับรายละเอียดสำหรับ FR หลักของ SaaS Foundation

## 2. UC-FD-001 — Provision New Tenant

**Related FR:** FR-FD-001
**Actor:** SMEsPlus Operations
**Precondition:** Operations staff ได้รับ order/สัญญาจากลูกค้าใหม่แล้ว

**Main Flow:**
1. Operations สร้าง Tenant record พร้อมข้อมูลองค์กร (ชื่อ, เลขผู้เสียภาษี, ที่อยู่)
2. ระบบสร้าง isolation boundary (RLS policy scope) สำหรับ tenant ใหม่
3. ระบบสร้าง Tenant Admin user คนแรกพร้อม role Tenant Admin
4. ระบบส่ง invitation email ให้ Tenant Admin ตั้งรหัสผ่าน
5. ระบบสร้าง default Subscription record สถานะ Pending Activation

**Alternate Flow:**
- 2a. หากการสร้าง isolation boundary ล้มเหลว ระบบต้อง rollback ทั้งหมดและแจ้ง error พร้อม log

**Postcondition:** Tenant ใหม่พร้อมใช้งานหลัง Tenant Admin ยืนยันบัญชีและ subscription active

## 3. UC-FD-002 — Assign Role to User

**Related FR:** FR-FD-002
**Actor:** Tenant Admin
**Precondition:** Tenant Admin login แล้วและมีสิทธิ์จัดการผู้ใช้

**Main Flow:**
1. Tenant Admin เปิดหน้าจัดการผู้ใช้
2. เลือกผู้ใช้ที่ต้องการเปลี่ยน role
3. เลือก role ใหม่จากรายการที่อนุญาต
4. ระบบตรวจสอบว่า Tenant Admin มีสิทธิ์มอบ role นั้นได้ (ไม่สามารถมอบสิทธิ์เกินกว่าที่ตนเองมี)
5. ระบบบันทึกการเปลี่ยนแปลงและเขียน AuditLog

**Alternate Flow:**
- 4a. หาก Tenant Admin พยายามมอบสิทธิ์เกินระดับตนเอง ระบบปฏิเสธและแสดง error

**Postcondition:** ผู้ใช้มี role ใหม่มีผลทันทีในการ login ครั้งถัดไป (หรือ session ปัจจุบันตาม NFR-PERF-03)

## 4. UC-FD-003 — Upgrade Subscription Tier

**Related FR:** FR-FD-003, FR-FD-004
**Actor:** Tenant Admin
**Precondition:** Tenant มี Subscription active อยู่แล้วในtier ปัจจุบัน

**Main Flow:**
1. Tenant Admin เปิดหน้า subscription management
2. ระบบแสดง tier ปัจจุบันและ tier ที่สามารถอัปเกรดได้
3. Tenant Admin เลือก tier ใหม่และยืนยัน
4. ระบบอัปเดต Subscription record เป็น tier ใหม่
5. ระบบเปิดใช้งาน Module ที่รวมอยู่ใน tier ใหม่โดยอัตโนมัติ (ตาม UC-FD-004)
6. ระบบเขียน AuditLog การเปลี่ยน tier

**Alternate Flow:**
- 3a. หากมีปัญหาการชำระเงิน ระบบต้องไม่ downgrade โมดูลที่ใช้งานอยู่ก่อนจนกว่าจะยืนยันสถานะ billing

**Postcondition:** Tenant เข้าถึงโมดูลใหม่ตาม tier ที่อัปเกรดได้ทันที

## 5. UC-FD-004 — Activate Module for Tenant

**Related FR:** FR-FD-004
**Actor:** System (triggered by Subscription change) หรือ SMEsPlus Operations (manual override)
**Precondition:** Tenant มี Subscription ที่รวม Module เป้าหมาย

**Main Flow:**
1. ระบบตรวจสอบว่า Module ที่จะเปิดอยู่ใน SubscriptionTier ของ tenant หรือไม่
2. ระบบสร้าง/อัปเดต ModuleActivation record เป็น Active
3. ระบบ enforce การเข้าถึงที่ API level (ไม่ใช่แค่ UI)
4. ระบบเขียน AuditLog การเปิดใช้งานโมดูล

**Alternate Flow:**
- 1a. หาก Module ไม่อยู่ใน tier ปัจจุบัน ระบบปฏิเสธการเปิดใช้งานและแจ้ง Tenant Admin ให้ upgrade tier ก่อน

**Postcondition:** โมดูลปรากฏในเมนูและ API ของ tenant ทันที

## 6. Related Documents

- `06_USER_STORIES.md`
- `03_FUNCTIONAL_REQUIREMENTS.md`
- `10_ACCEPTANCE_CRITERIA.md`

## 7. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial use case draft | Functional Specification AI (Claude) |
