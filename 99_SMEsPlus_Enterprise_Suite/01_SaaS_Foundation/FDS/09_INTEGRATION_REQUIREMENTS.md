# 09 — Integration Requirements

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-009
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss

## 1. Purpose

ระบุจุดเชื่อมต่อ (integration point) ที่ SaaS Foundation ต้องมี ทั้งภายในระบบ (โมดูลธุรกิจอื่น) และภายนอก (third-party) เอกสารนี้เป็น functional-level เท่านั้น รายละเอียด contract อยู่ใน `API/`

## 2. Internal Integration (Foundation → Business Modules)

| ID | Integration | Description |
|---|---|---|
| INT-FD-01 | Tenant Context Propagation | ทุกโมดูลธุรกิจ (Accounting, Purchase, Inventory ฯลฯ) ต้องรับ tenant context จาก Foundation ผ่าน request header/token — ห้าม module ธุรกิจ resolve tenant เอง |
| INT-FD-02 | Permission Check API | โมดูลธุรกิจต้องเรียก Foundation permission check ก่อนอนุญาต action ที่มีผลต่อข้อมูล |
| INT-FD-03 | Module Activation Status | โมดูลธุรกิจต้อง query สถานะ ModuleActivation ของตนเองจาก Foundation ก่อนให้บริการ ไม่ hardcode ว่าตนเอง "เปิดใช้งานเสมอ" |
| INT-FD-04 | Audit Event Emission | เหตุการณ์สำคัญของโมดูลธุรกิจ (เช่น อนุมัติเอกสาร) ควรส่ง event เข้า AuditLog ผ่าน Foundation event catalog |

## 3. External Integration (Foundation → Third-Party)

| ID | Integration | Description | Status |
|---|---|---|---|
| INT-FD-05 | Billing / Payment Gateway | สำหรับการต่ออายุ/อัปเกรด subscription | Scope not yet defined — pending separate FDS |
| INT-FD-06 | Email/Notification Provider | สำหรับ tenant provisioning invitation, subscription expiry warning | Scope not yet defined |
| INT-FD-07 | Identity Provider (optional, future) | สำหรับ SSO ในอนาคต | Out of scope for v1.0 |

## 4. Evidence Note

รายการ Integration ข้อ 2 (Internal) อ้างอิงจากโครงสร้าง modular monolith ตาม ADR-0004 — ยังไม่มีหลักฐาน implementation จริงของ Tenant Context Propagation mechanism ใน source code ที่ตรวจสอบ ต้องถูก design ใหม่ร่วมกับ SDS

รายการข้อ 3 (External) ยังไม่มี scope ที่ Boss ยืนยัน — ต้องเปิด FDS แยกเมื่อมีการตัดสินใจ vendor/mechanism

## 5. Related Documents

- `03_FUNCTIONAL_REQUIREMENTS.md`
- `API/API_GUIDELINE.md`
- `API/EVENT_CATALOG.md`

## 6. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial integration requirements draft | Functional Specification AI (Claude) |
