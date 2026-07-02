VERSION_HISTORY.md

Document ID: GOV-008
Version: v1.0.0
Status: Approved
Owner: SMEsPlus Product & Architecture Team
Reviewer: Architecture Review Board (ARB)
Approver: Chief Solution Architect
Classification: Governance
Target Path: 01_SaaS_Foundation/VERSION_HISTORY.md

**Related Documents:** README.md, CHANGELOG.md, ARCHITECTURE_GOVERNANCE.md, ARCHITECTURE_DECISION_LOG.md

## 1. Purpose

เอกสารนี้ใช้เป็นประวัติ Version ของเอกสารทั้งหมดภายใต้ `01_SaaS_Foundation`

มีวัตถุประสงค์เพื่อ

- ติดตามวิวัฒนาการของเอกสาร
- ระบุ Baseline ที่ได้รับอนุมัติ
- สนับสนุน Audit และ Compliance
- สนับสนุนการ Rollback หากจำเป็น

## 2. Versioning Policy

ใช้ Semantic Versioning

| Version | Meaning |
|---|---|
| Major | เปลี่ยน Architecture หรือ Breaking Change |
| Minor | เพิ่มความสามารถโดยไม่กระทบของเดิม |
| Patch | แก้ไขเอกสาร คำอธิบาย หรือข้อผิดพลาด |

ตัวอย่าง: v1.0.0, v1.1.0, v1.1.1, v2.0.0

## 3. Foundation Baselines

| Baseline | Description | Status |
|---|---|---|
| Foundation v1.0 | Initial SaaS Foundation | Approved |
| Foundation v1.1 | Governance Improvement | Planned |
| Foundation v1.2 | SDS Expansion | Planned |
| Foundation v2.0 | Enterprise Modules | Planned |

## 4. Document Version Register

| Document | Current Version | Status |
|---|---|---|
| README | v1.0.0 | Approved |
| DOCUMENT_MAP | v1.0.0 | Approved |
| GLOSSARY | v1.0.0 | Approved |
| ARCHITECTURE_PRINCIPLES | v1.0.0 | Approved |
| ARCHITECTURE_GOVERNANCE | v1.0.0 | Approved |
| ARCHITECTURE_DECISION_LOG | v1.0.0 | Approved |
| TRACEABILITY_MATRIX | v1.0.0 | Approved |
| VERSION_HISTORY | v1.0.0 | Approved |
| CHANGELOG | v1.0.0 | Pending |

## 5. Version Lifecycle

```text
Draft
  │
  ▼
Review
  │
  ▼
Approved
  │
  ▼
Published
  │
  ▼
Deprecated
  │
  ▼
Archived
```

## 6. Version Control Rules

- ทุกการแก้ไขต้องเพิ่มรายการใน `CHANGELOG.md`
- Major Version ต้องมี ADR หากเป็นการเปลี่ยนสถาปัตยกรรม
- เอกสารที่ถูกแทนที่ต้องคงไว้เพื่ออ้างอิงจนกว่าจะครบระยะเวลาการเก็บรักษาที่กำหนด

## 7. Review Schedule

| Document Type | Review Frequency |
|---|---|
| Governance | ทุก 6 เดือน |
| FDS | ทุก Release |
| SDS | ทุก Release |
| API | ทุก Sprint ที่มีการเปลี่ยนแปลง |
| Database | ทุก Sprint ที่มี Migration |
| Security | ทุก Quarter |
| QA | ทุก Release |

## 8. Success Criteria

ถือว่า Version Management สมบูรณ์เมื่อ

- ทุกเอกสารมี Version
- ทุก Version มีประวัติการเปลี่ยนแปลง
- ทุก Major Version ผ่านการอนุมัติ
- CHANGELOG และ VERSION_HISTORY สอดคล้องกัน
