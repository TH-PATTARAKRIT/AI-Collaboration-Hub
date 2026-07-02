# 04 — Non-Functional Requirements

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-004
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss

## 1. Purpose

ระบุข้อกำหนดที่ไม่ใช่ functional (NFR) ของ SaaS Foundation ซึ่งเป็น baseline สำหรับทุกโมดูลธุรกิจที่สร้างบนรากฐานนี้

## 2. Performance

| ID | Requirement | Target |
|---|---|---|
| NFR-PERF-01 | Response time สำหรับ API เรียก tenant/user context | ≤ 300ms (p95) |
| NFR-PERF-02 | Login/authentication flow | ≤ 1.5s end-to-end |
| NFR-PERF-03 | Module activation toggle เห็นผลใน UI | ≤ 5s |

## 3. Scalability

| ID | Requirement |
|---|---|
| NFR-SCALE-01 | ระบบต้องรองรับการเพิ่มจำนวน tenant โดยไม่ต้อง redesign schema |
| NFR-SCALE-02 | Shared database ต้องรองรับ tenant จำนวนมากโดย performance ไม่ลดลงอย่างมีนัยสำคัญต่อ tenant แต่ละราย (noisy neighbor control) |

## 4. Availability

| ID | Requirement | Target |
|---|---|---|
| NFR-AVAIL-01 | Foundation service uptime | ≥ 99.5% ต่อเดือน |
| NFR-AVAIL-02 | Planned maintenance ต้องแจ้งล่วงหน้าและไม่กระทบ tenant isolation |

## 5. Security (summary — รายละเอียดใน 08_SECURITY_REQUIREMENTS.md)

| ID | Requirement |
|---|---|
| NFR-SEC-01 | ข้อมูลระหว่าง tenant ต้อง isolate สมบูรณ์ (zero cross-tenant data leakage) |
| NFR-SEC-02 | Password และ credential ต้องจัดเก็บแบบ hashed/encrypted ตามมาตรฐานอุตสาหกรรม |
| NFR-SEC-03 | ทุก privileged action ต้องมี audit log ที่แก้ไขย้อนหลังไม่ได้ |

## 6. Auditability

| ID | Requirement |
|---|---|
| NFR-AUDIT-01 | ทุก decision, handoff, และ output ต้อง traceable ตาม AI Project Constitution ข้อ 9 |
| NFR-AUDIT-02 | การเปลี่ยนแปลง subscription/module activation ต้องเก็บ log พร้อม timestamp, actor, และ before/after state |

## 7. Localization

| ID | Requirement |
|---|---|
| NFR-LOC-01 | UI หลักต้องรองรับภาษาไทยเป็นค่าเริ่มต้น |
| NFR-LOC-02 | Foundation ต้องไม่ hardcode ข้อสมมติที่ผูกกับ locale ใด locale หนึ่ง ยกเว้นส่วนที่เกี่ยวข้องกับ `l10n_th` โดยตรง |

## 8. Maintainability

| ID | Requirement |
|---|---|
| NFR-MAINT-01 | Foundation service ต้องแยกเป็น module อิสระ ไม่ผูกแน่นกับโมดูลธุรกิจใด ๆ (modular monolith ตาม ADR-0004) |
| NFR-MAINT-02 | ทุก breaking change ต้องมี ADR ใหม่ตาม ARCHITECTURE_DECISION_LOG.md |

## 9. Compliance

| ID | Requirement |
|---|---|
| NFR-COMP-01 | ระบบต้องออกแบบให้รองรับข้อกำหนดกฎหมายไทยที่เกี่ยวข้องกับข้อมูลส่วนบุคคล (PDPA) |
| NFR-COMP-02 | Audit trail ต้องเก็บรักษาตามระยะเวลาที่กฎหมายไทยกำหนดสำหรับข้อมูลทางบัญชี/ธุรกิจ |

## 10. Related Documents

- `03_FUNCTIONAL_REQUIREMENTS.md`
- `08_SECURITY_REQUIREMENTS.md`
- `01_SaaS_Foundation/ARCHITECTURE_PRINCIPLES.md`

## 11. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial NFR draft | Functional Specification AI (Claude) |
