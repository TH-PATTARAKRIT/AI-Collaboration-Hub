# DOCUMENT_MAP.md

**Version:** v1.0  
**Status:** Operational  
**Owner:** Repository Owner / SMEsPlus PMO  
**Project:** SMEsPlus Enterprise Suite  
**Branch:** SMEsPlus  
**Working Folder:** `99_SMEsPlus_Enterprise_Suite/`  
**Last Updated:** 2026-07-06

---

# Purpose

เอกสารนี้เป็นแผนที่เอกสารหลักของโครงการ SMEsPlus Enterprise Suite เพื่อให้ Functional Specification AI, Claude AI, Claude Code, PMO AI และ ChatGPT/Liza อ่านเอกสารตามลำดับเดียวกันก่อนเริ่มงาน

This file defines the official document map for AI session bootstrap, functional specification work, evidence control, and repository governance.

---

# Reading Order

AI ทุกตัวต้องอ่านตามลำดับนี้ก่อนเริ่มงาน

1. `README.md`
2. `AI_SESSION_BOOTSTRAP.md`
3. `DOCUMENT_MAP.md`
4. `AI_WORKING_INDEX.md`
5. `WORK_PACKAGE_REGISTER.md`
6. `AI_ROLE_DIRECTORY.md`
7. `BOOT_SEQUENCE.md`
8. `TRACEABILITY_MATRIX.md`
9. Folder-specific README or current module document
10. Evidence / Review Gate files related to the work package

---

# Core Control Documents

| File | Purpose | Owner | Required Before Work |
|---|---|---|---|
| `README.md` | Repository overview and folder structure | Repository Owner | Yes |
| `AI_SESSION_BOOTSTRAP.md` | New AI session startup control | Repository Owner / PMO AI | Yes |
| `DOCUMENT_MAP.md` | Document reading map | PMO AI | Yes |
| `AI_WORKING_INDEX.md` | Current AI work status | PMO AI / Liza | Yes |
| `WORK_PACKAGE_REGISTER.md` | Work package register and status | PMO AI | Yes |
| `AI_ROLE_DIRECTORY.md` | AI role responsibility map | Repository Owner / PMO AI | Yes |
| `BOOT_SEQUENCE.md` | Step-by-step startup process | PMO AI | Yes |
| `TRACEABILITY_MATRIX.md` | Requirement-to-evidence mapping | Functional Specification AI / PMO AI | Yes for functional work |

---

# Functional Specification Document Set

Functional Specification AI ต้องเริ่มจากเอกสารเหล่านี้

| Document | Target Folder | Purpose | Status |
|---|---|---|---|
| Functional Specification | `02_Functional_Design/` | Business function detail | To be produced |
| Business Rules | `02_Functional_Design/` | Rule definition and exceptions | To be produced |
| Workflow | `02_Functional_Design/` | Process flow and BPMN input | To be produced |
| Database Mapping | `02_Functional_Design/` | Table/entity mapping | To be produced |
| API Mapping | `02_Functional_Design/` | API/event/service mapping | To be produced |
| UI Mapping | `02_Functional_Design/` | Screen/menu/action mapping | To be produced |
| Acceptance Criteria | `02_Functional_Design/` | Pass/fail criteria | To be produced |
| Traceability | `TRACEABILITY_MATRIX.md` | FR to evidence mapping | Operational baseline |

---

# Repository Folder Map

| Folder | Primary Use | Owner |
|---|---|---|
| `00_Project_Governance/` | Governance, constitution, approvals | PMO AI |
| `01_AI_Handoff/` | AI handoff records and role transitions | Integration AI / PMO AI |
| `02_Functional_Design/` | Functional specs, workflows, acceptance criteria | Functional Specification AI |
| `03_Architecture_Decisions/` | Architecture decisions and ADRs | Enterprise Architect AI |
| `04_Review_Gates/` | Gate criteria and approval records | PMO AI / Review AI |
| `05_Prompts/` | Approved prompts and guardrails | PMO AI |
| `06_Templates/` | Document templates | PMO AI |
| `07_Output_From_AI/` | AI outputs after review | PMO AI |
| `08_Testing_Evidence/` | Test/UAT evidence | QA/UAT AI |
| `09_Security_Clean_Room/` | Clean-room and security evidence | AI Governance / Security AI |
| `11_Diagrams/` | Flowcharts, mindmaps, architecture visuals | Architecture / Functional AI |

---

# No Duplicate Rule

ก่อนสร้างเอกสารใหม่ AI ต้องตรวจสอบว่าเอกสารหรือหัวข้อเดียวกันมีอยู่แล้วหรือไม่

If an existing file covers the same purpose, update or reference the existing file instead of creating a duplicate.

---

# Gap Handling Rule

ถ้าเอกสารที่อ้างถึงยังไม่มี ให้บันทึกเป็น Gap ใน `WORK_PACKAGE_REGISTER.md` หรือรายงานสถานะ ไม่ให้สมมติว่าเอกสารนั้นมีอยู่จริง

---

# End
