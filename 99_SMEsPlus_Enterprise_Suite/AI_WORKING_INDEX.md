# AI_WORKING_INDEX.md

**Version:** v1.1  
**Status:** Working Artifact  
**Owner:** SMEsPlus PMO / Repository Owner  
**Last Updated:** 2026-07-07T01:31:49+07:00  
**Control Level:** L99

---

# Purpose

เอกสารนี้ใช้เป็น AI Working Artifact สำหรับติดตามสถานะการทำงานของ AI ภายในโครงการ SMEsPlus Enterprise Suite

ใช้ติดตาม

- Work package เสร็จหรือยัง
- Claude Review แล้วหรือยัง
- Evidence ครบหรือยัง
- Gate ผ่านหรือยัง

> ไฟล์นี้เป็น Working Artifact ของ AI ไม่ใช่มาตรฐานหลักของโครงการ

---

# Working Principle

- Repository Owner เป็นผู้กำหนดมาตรฐาน
- AI เป็นผู้ปฏิบัติตามมาตรฐาน
- AI จะไม่เสนอเปลี่ยนโครงสร้างหลักของ Repository
- AI จะเสนอเฉพาะเครื่องมือหรือไฟล์ช่วยงานที่ไม่กระทบมาตรฐานหลัก
- การเปลี่ยนแปลงโครงสร้างหลักต้องได้รับการอนุมัติจาก Boss
- No Evidence = No Progress
- No Gate Approval = No Move Forward

---

# AI Role

| AI | Responsibility |
|---|---|
| Functional Specification AI | Business Functional Specification |
| Claude AI | Repository Review, Evidence Matching, SaaS Alignment |
| ChatGPT (Liza) | Architecture Governance, PMO, Cross-AI Review, Evidence Gate Review |
| Claude Code | Coding หลังผ่าน Build Gate เท่านั้น |
| Repository Owner | Repository Standard |
| Boss | Final Approval |

---

# AI Working Index

| ID | Work Package | Responsible AI | Status | Claude Review | Evidence | Gate Impact | Next Action |
|---|---|---|---|---|---|---|---|
| EWP-000 | AI Collaboration Standard | Liza / PMO AI | In Progress | Required | Partial | Governance Gate | Verify latest governance standard |
| EWP-001 | Functional Specification Standard | Functional AI | Review Required | Required | Partial | FDS Gate | Validate FDS Factory pipeline |
| EWP-002 | Repository Audit | Claude AI / Liza | PASS WITH CONTROL | Required | Partial | Repository Gate | Continue duplicate-folder monitoring |
| EWP-003 | SaaS Alignment | Claude AI / Enterprise Architect AI | Review Required | Required | Partial | Architecture / FDS Gate | Review ACC-001 against SaaS Foundation |
| EWP-004 | Traceability Review | Liza / PMO AI | HOLD | Required | Partial | Traceability Gate | Verify ACC-001 matrix rows before MATCHED |
| ACC-001 | Accounting Thailand Functional Design Specification | Functional Specification AI | Draft Completed / Review Required | Pending | Partial | FDS / Evidence / Traceability Gate | Claude Review + PMO Evidence Review + Accounting Review required |

---

# Status Definition

- Not Started
- Pending
- In Progress
- Draft Completed
- Review Required
- PASS WITH CONTROL
- Approved
- HOLD
- Archived

---

# Evidence Definition

- None
- Pending
- Partial
- Complete
- Verified
- Conflict
- Archived

---

# Gate Impact

- Governance Gate
- Repository Gate
- Architecture Gate
- FDS Gate
- SDS Gate
- API / DB / UX Gate
- Traceability Gate
- QA / UAT Gate
- Build Gate
- Production Gate

---

# Current L99 Control Status

```text
ACC-001 FDS Gate = REVIEW REQUIRED
ACC-001 Evidence Gate = PARTIAL / HOLD
ACC-001 Traceability Gate = PARTIAL / HOLD
ACC-001 Build Gate = HOLD
ACC-001 Production Gate = HOLD
```

---

# Working Artifact Rule

ไฟล์นี้ใช้สำหรับติดตามการทำงานของ AI เท่านั้น

ไม่ใช้แทน

- README.md
- DOCUMENT_MAP.md
- TRACEABILITY_MATRIX.md
- ARCHITECTURE_GOVERNANCE.md
- FUNCTIONAL_SPECIFICATION_STANDARD.md
- WORK_PACKAGE_REGISTER.md

หากข้อมูลขัดแย้งกัน ให้ยึดเอกสารมาตรฐานหลักเป็น Source of Truth

---

# Executive Note

Repository Owner กำหนดมาตรฐาน

AI ปฏิบัติตามมาตรฐาน

PMO / Liza ตรวจสอบ Gate

Boss เป็นผู้อนุมัติสุดท้าย

---

# End
