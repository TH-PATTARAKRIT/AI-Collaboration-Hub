# 01 — Document Control

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-001
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss
Target Path: `01_SaaS_Foundation/FDS/01_DOCUMENT_CONTROL.md`

## 1. Purpose

ระบุข้อมูลควบคุมเอกสาร (document control) สำหรับ FDS ชุด SaaS Foundation ทั้งหมด เพื่อให้ทุกไฟล์ในชุดนี้ traceable ในเรื่อง version, owner, reviewer, และ approval status ตาม AI Repository Contract (Evidence Rule)

## 2. Document Identification

| Field | Value |
|---|---|
| Document Set | SMEsPlus SaaS Foundation — Functional Design Specification |
| Document Set ID | SMEPLUS-SAAS-FOUNDATION-FDS |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `SMEsPlus` |
| Path | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/` |
| Module | SaaS Foundation (Priority 1) |
| Related ADR | ADR-0001, ADR-0002, ADR-0003, ADR-0006 |

## 3. Ownership and Review Chain

| Role | Responsibility |
|---|---|
| Functional Specification AI | authors FR, use cases, acceptance criteria |
| Enterprise Architect AI | reviews technical/architecture alignment |
| PMO AI | checks process compliance and evidence completeness |
| Technical Team AI | checks completeness against SDS/API/DB feasibility |
| Boss | final approval authority |

## 4. Status Definitions

| Status | Meaning |
|---|---|
| Draft | เขียนใหม่ ยังไม่ผ่าน review |
| In Review | อยู่ระหว่างการตรวจสอบโดย PMO AI / Enterprise Architect AI |
| Approved Baseline | ผ่านการอนุมัติจาก Boss แล้ว ใช้เป็น source of truth ได้ |
| Superseded | ถูกแทนที่ด้วยเวอร์ชันใหม่กว่า |
| Deprecated | เลิกใช้งาน |

## 5. Version Numbering Rule

- `v0.x` = Draft cycle, ยังไม่ approved
- `v1.0` = First approved baseline (ต้องได้ Boss approval)
- `v1.x` = Minor update ที่ไม่กระทบ scope หลัก
- `v2.0+` = Major revision ที่กระทบ FR scope หรือ breaking change

## 6. Evidence Requirement

ทุก Functional Requirement ในชุดนี้ต้องอ้างอิงหนึ่งในสามแหล่งต่อไปนี้ ก่อนจะถือว่ามี evidence ครบ:

1. Evidence Matching Matrix (`12_Traceability/Requirement_Matrix/`)
2. Source code / database evidence จาก `01_ACCOUNT.zip`, `02_OTHER.zip`, หรือ live database dump
3. Boss confirmation ที่บันทึกไว้เป็นลายลักษณ์อักษร (เช่น scope decision, out-of-scope ruling)

Requirement ที่ไม่มี evidence ต้องระบุสถานะเป็น **GAP** และไม่นับเป็น progress ตาม No Evidence = No Progress Rule

## 7. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial document control record | Functional Specification AI (Claude) |

## 8. Related Documents

- `SMEPLUS-SAAS-FOUNDATION-FDS.md` (Master Index)
- `01_SaaS_Foundation/DOCUMENT_MAP.md`
- `01_SaaS_Foundation/ARCHITECTURE_DECISION_LOG.md`
- `repository-contract/AI_REPOSITORY_CONTRACT.md`
