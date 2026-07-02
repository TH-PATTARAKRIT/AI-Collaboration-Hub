# 08 — Security Requirements

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-008
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI (with Enterprise Architect AI input)
Reviewers: PMO AI, Enterprise Architect AI, Code Review AI
Approval: Pending Boss
Related ADR: ADR-0002 (Multi-Tenant), ADR-0006 (RBAC/ABAC/RLS), ADR-0007 (Audit by Design)

## 1. Purpose

ระบุข้อกำหนดความปลอดภัยของ SaaS Foundation ที่โมดูลธุรกิจอื่นทั้งหมดต้องพึ่งพา เอกสารนี้เป็น functional-level requirement — รายละเอียดเชิง architecture อยู่ใน `SECURITY/SECURITY_ARCHITECTURE.md`

## 2. Tenant Isolation

| ID | Requirement |
|---|---|
| SEC-FD-01 | ทุก query ต้อง scope ด้วย tenant context เสมอ ไม่มี default query ที่ข้าม tenant boundary ได้ |
| SEC-FD-02 | Row-Level Security (RLS) หรือกลไกเทียบเท่าต้องบังคับใช้ที่ระดับ database ไม่ใช่แค่ application layer |
| SEC-FD-03 | Background job / batch process ต้องระบุ tenant context ชัดเจน ห้าม process ข้าม tenant ในรอบเดียวโดยไม่มี explicit isolation |

## 3. Authentication

| ID | Requirement |
|---|---|
| SEC-FD-04 | รองรับ authentication ด้วย username/password ขั้นต่ำ พร้อมช่องทางขยายสำหรับ MFA ในอนาคต |
| SEC-FD-05 | Password ต้องจัดเก็บแบบ hashed (ไม่เก็บ plaintext) |
| SEC-FD-06 | Session/token ต้องมี expiry และรองรับการ revoke ทันทีเมื่อ role หรือ subscription เปลี่ยน |

## 4. Authorization (RBAC/ABAC)

| ID | Requirement |
|---|---|
| SEC-FD-07 | ทุก API endpoint ต้องตรวจสอบ permission ก่อนประมวลผล ไม่พึ่งพา UI-level restriction เพียงอย่างเดียว |
| SEC-FD-08 | Permission check ต้องพิจารณาทั้ง Role (RBAC) และ attribute เช่น module activation status ของ tenant (ABAC) |
| SEC-FD-09 | Tenant Admin ไม่สามารถมอบสิทธิ์ที่สูงกว่าที่ตนเองมีให้ user อื่นได้ |

## 5. Audit and Logging

| ID | Requirement |
|---|---|
| SEC-FD-10 | ทุกการเปลี่ยนแปลง role, permission, subscription, module activation ต้องเขียน AuditLog แบบ append-only |
| SEC-FD-11 | AuditLog ต้องเก็บ actor, timestamp, before/after state, และ tenant context |
| SEC-FD-12 | AuditLog ห้ามถูกแก้ไขหรือลบโดยผู้ใช้ทั่วไป แม้จะเป็น Tenant Admin |

## 6. Data Protection

| ID | Requirement |
|---|---|
| SEC-FD-13 | ข้อมูลอ่อนไหว (เช่น ข้อมูลบัญชี, ข้อมูลส่วนบุคคล) ต้อง encrypt at rest ตามความเหมาะสม |
| SEC-FD-14 | การส่งข้อมูลระหว่าง client และ server ต้องผ่าน TLS เท่านั้น |

## 7. Threat Considerations (ระดับ Functional)

| Threat | Mitigation Requirement |
|---|---|
| Cross-tenant data leakage ผ่าน API parameter manipulation | SEC-FD-01, SEC-FD-02, SEC-FD-07 |
| Privilege escalation ผ่านการมอบ role เกินสิทธิ์ | SEC-FD-09 |
| Audit trail tampering | SEC-FD-12 |
| Session hijacking หลัง role/subscription เปลี่ยน | SEC-FD-06 |

## 8. Related Documents

- `03_FUNCTIONAL_REQUIREMENTS.md`
- `SECURITY/SECURITY_ARCHITECTURE.md`
- `SECURITY/TENANT_ISOLATION.md`
- `SECURITY/PERMISSION_MATRIX.md`

## 9. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial security requirements draft | Functional Specification AI (Claude) |
