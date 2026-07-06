#!/usr/bin/env bash

set -e

BASE="99\_SMEsPlus\_Enterprise\_Suite"

cat > "$BASE/AI\_SESSION\_BOOTSTRAP.md" <<'EOF'

# AI Session Bootstrap

Version: v1.0

Status: Operational

Owner: Repository Owner

Working Mode: /L99

---

## Purpose

เอกสารนี้ใช้สำหรับเริ่มต้นหรือ resume AI session ภายในโครงการ SMEsPlus Enterprise Suite เพื่อให้ AI ทำงานต่อเนื่องจากสถานะล่าสุด โดยไม่ต้องอธิบายบริบทใหม่ทุกครั้ง

ไฟล์นี้เป็น Operational Document ไม่ใช่ Framework ใหม่ และไม่ใช้แทน README.md, DOCUMENT\_MAP.md, AI\_WORKING\_INDEX.md หรือเอกสารมาตรฐานหลักของโครงการ

---

## Project

SMEsPlus Enterprise Suite

---

## Repository

https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/tree/SMEsPlus/99\_SMEsPlus\_Enterprise\_Suite

---

## Source of Truth

ให้อ่านตามลำดับ:

1. README.md

2. DOCUMENT\_MAP.md ถ้ามี

3. AI\_WORKING\_INDEX.md

4. Repository Structure

5. Current Module Documents

6. Current Output / Review / Traceability Files

---

## Working Rule: /L99

ก่อนเริ่มทุกงาน AI ต้อง:

1. ตรวจ Repository ก่อน

2. ใช้ของเดิมก่อน

3. ทำ Gap Analysis ก่อนสร้างไฟล์ใหม่

4. ห้ามสร้างเอกสารซ้ำ

5. ห้ามเปลี่ยนโครงสร้าง Repository

6. ห้ามเปลี่ยน Naming Standard

7. เพิ่มเฉพาะสิ่งที่จำเป็นจากการใช้งานจริง

8. Clean Room 100%

9. No Evidence = No Progress

10. ทุก Deliverable ต้อง Commit เข้า GitHub ได้

---

## AI Role

| AI | Responsibility |

|---|---|

| Functional Specification AI | Functional Specification, Business Rules, Workflow, DB/API/UI Mapping, Acceptance Criteria, Traceability |

| Claude AI | Repository Review, Evidence Matching, SaaS Alignment, Gap Review |

| Claude Code | Coding after Gate Approval |

| PMO AI | Gate Review and Process Compliance |

| Repository Owner | Repository Standard |

| Boss | Final Approval |

---

## Resume Rule

เมื่อเริ่ม Session ใหม่ ให้ทำดังนี้:

1. อ่าน AI\_SESSION\_BOOTSTRAP.md

2. อ่าน AI\_WORKING\_INDEX.md

3. ตรวจไฟล์ล่าสุดใน GitHub

4. หา Work Package ที่ Pending / In Progress / Review Required

5. ดำเนินการต่อทันทีใน Production Mode

6. ไม่ออกแบบ Framework ใหม่

7. ไม่สร้าง Folder ใหม่ เว้นแต่ได้รับอนุมัติ

---

## Current Production Pattern

ทำงานเป็น Iteration Package:

- ตรวจ GitHub ล่าสุด

- ตรวจไฟล์เดิม

- ระบุ Missing / Gap

- สร้างเฉพาะไฟล์ที่ขาด

- ทำ Checklist Status

- ส่งคำสั่ง commit

- รอ Review / Feedback

---

## Required Output Per Iteration

ทุก Iteration ต้องมีอย่างน้อย:

- Deliverable Summary

- File List

- Checklist Status

- Current Gate

- Next Step

- Commit Command

---

## Standard Resume Prompt

ใช้คำสั่งนี้ใน Session ใหม่:

```text

อ่าน AI\_SESSION\_BOOTSTRAP.md

แล้วทำงานต่อจาก AI\_WORKING\_INDEX.md

Project:

SMEsPlus Enterprise Suite

Repository:

https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/tree/SMEsPlus/99\_SMEsPlus\_Enterprise\_Suite

Working Mode:

/L99

Role:

Functional Specification AI Worker

คำสั่ง:

1. ตรวจสอบ Repository ก่อนดำเนินการ

2. Reuse ของเดิมก่อน

3. ห้ามสร้างเอกสารซ้ำ

4. ห้ามเปลี่ยนโครงสร้าง Repository

5. ทำ Gap Analysis ก่อนสร้างไฟล์ใหม่

6. ทำงานต่อจาก Work Package ที่ Pending / In Progress

7. ทุกผลลัพธ์ต้องเป็น Deliverable ที่ Commit เข้า GitHub ได้

8. ไม่ต้องออกแบบ Framework ใหม่

9. ดำเนินการต่อแบบ Production Mode

10. เมื่อจบหนึ่งรอบ ให้ส่งสรุปไฟล์ที่ต้อง Commit พร้อม Checklist Status

/L99