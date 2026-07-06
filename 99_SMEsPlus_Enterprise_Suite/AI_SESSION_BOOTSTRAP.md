# AI Session Bootstrap

**Version:** v1.1  
**Status:** Operational  
**Owner:** Repository Owner  
**Project:** SMEsPlus Enterprise Suite  
**Repository:** TH-PATTARAKRIT/AI-Collaboration-Hub  
**Branch:** SMEsPlus  
**Working Mode:** /L99  
**Last Updated:** 2026-07-06  

---

# Purpose

เอกสารนี้ใช้สำหรับเริ่มต้น AI Session ใหม่ เพื่อให้ AI ทุกตัวสามารถทำงานต่อจากสถานะปัจจุบันของโครงการได้ โดยไม่ต้องอธิบาย Project ซ้ำทุกครั้ง

This document is the bootstrap control file for every new AI session. It defines where to read first, how to resume work, and what rules must be followed before producing any deliverable.

---

# Repository Location

```text
Repository: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Working Folder: 99_SMEsPlus_Enterprise_Suite/
Working Mode: /L99
```

---

# Repository Principle

Repository Owner เป็นผู้กำหนดมาตรฐาน

AI เป็นผู้ปฏิบัติตามมาตรฐาน

ห้าม AI เปลี่ยน Repository Structure เว้นแต่ได้รับอนุมัติจาก Repository Owner / Boss

AI must not create a new framework, rename standards, move folders, or change repository structure without explicit approval.

---

# Source of Truth

อ่านตามลำดับนี้ทุกครั้งก่อนเริ่มงาน

1. `README.md`
2. `DOCUMENT_MAP.md` ถ้ามีอยู่ใน Repository
3. `AI_WORKING_INDEX.md`
4. Repository Structure
5. Current Module Documents
6. Existing Review Gate / Evidence Files

If any referenced file is missing, mark it as a gap. Do not invent its content.

---

# Working Rule

ก่อนเริ่มทุกงาน AI ต้องทำตามลำดับนี้

1. Read Repository
2. Reuse Existing
3. Gap Analysis
4. No Duplicate
5. Clean Room 100%
6. No Evidence = No Progress
7. Work from current state only
8. Do not redesign the framework
9. Do not create folders unless approved
10. Do not change naming standard unless approved

---

# AI Responsibilities

| AI Role | Responsibility |
|---|---|
| Functional Specification AI | Functional Specification, Business Rules, Workflow, Database Mapping, API Mapping, UI Mapping, Acceptance Criteria, Traceability |
| Claude AI | Repository Review, Evidence Matching, SaaS Alignment, Gap Review |
| Claude Code | Development after approved Build Gate only |
| ChatGPT / Liza | Architecture Governance, PMO Control, Cross-AI Review, Executive Summary, Evidence Gate Review |
| PMO AI | Gate Review, Evidence Register, Status Control |
| Repository Owner | Repository Standard |
| Boss | Final Approval |

---

# Resume Rule

เริ่มทำงานจาก `AI_WORKING_INDEX.md`

หากมี Work Package ที่สถานะต่อไปนี้ ให้ทำงานต่อทันทีจากสถานะเดิม

- Pending
- In Progress
- Review Required
- HOLD

ห้ามออกแบบ Framework ใหม่

ห้ามสร้าง Folder ใหม่

ห้ามเปลี่ยน Naming Standard

เว้นแต่ได้รับอนุมัติ

---

# Gate Control

ใช้สถานะ Gate ต่อไปนี้เท่านั้น

| Gate Status | Meaning |
|---|---|
| PASS | Evidence complete and approved |
| HOLD | Work cannot proceed until required evidence or approval is complete |
| FROZEN | Claimed progress is frozen because evidence is missing or conflicting |
| ROLLBACK | Work must be reverted or replaced |
| REVIEW REQUIRED | Output exists but must be reviewed before use |

Core rule:

```text
No Evidence = No Progress
```

---

# Clean Room Rule

AI may study concepts, business rules, workflows, structures, and patterns.

AI must not copy, clone, or reuse protected source code, proprietary implementation, naming, comments, or database-specific logic without approval.

Required sequence:

```text
Reference Study -> Generic Concept -> SMEsPlus Design -> New Implementation -> Evidence Review
```

---

# Deliverable Rule

ทุก Session ต้องมี Deliverable ที่สามารถ Commit เข้า Repository ได้

Deliverable ต้องมีอย่างน้อย

- File name
- Owner
- Version
- Status
- Purpose
- Evidence reference
- Gate impact
- Next action

ห้ามนับงานเป็น Progress หากไม่มีไฟล์หรือ Evidence ที่ตรวจสอบได้

---

# Session Naming Standard

ใช้รูปแบบนี้เท่านั้น

```text
[SMEPLUS-YY-MM-DD-XXX] Session Name
```

Example:

```text
[SMEPLUS-26-07-06-001] AI Session Bootstrap Update
```

---

# Working Order for New AI Session

1. Open this file
2. Open `README.md`
3. Open `AI_WORKING_INDEX.md`
4. Check pending or in-progress work packages
5. Confirm no duplicate document already exists
6. Produce only the required deliverable
7. Mark evidence and gate impact
8. Report status to Repository Owner / Boss

---

# Current Execution Boundary

Allowed:

- Documentation
- Functional specification
- Architecture review
- Evidence matching
- Repository review
- Gap analysis
- PMO gate review
- Clean-room blueprint creation

HOLD unless approved:

- Production use
- Direct customer demo from unapproved output
- Feature coding
- Merge / release
- Migration execution
- Copy / clone / direct reuse of protected source

---

# End
