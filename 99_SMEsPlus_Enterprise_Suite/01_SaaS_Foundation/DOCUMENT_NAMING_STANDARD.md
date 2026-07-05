# DOCUMENT\_NAMING\_STANDARD.md

Version: 1.0

Status: Approved

Owner: SMEsPlus Architecture Board

Applies To: 01\_SaaS\_Foundation

Last Updated: 2026-07-05

---

# Document Naming & Repository Consistency Standard

## Purpose

กำหนดมาตรฐานการตั้งชื่อเอกสารและโครงสร้าง Repository ของ SMEsPlus Enterprise Suite เพื่อให้เอกสารมีความสอดคล้อง (Consistency) และเป็น Single Source of Truth สำหรับทีมงานและ AI ทุกระบบ

---

# Principle

การใช้ชื่อเต็ม (Full Name) หรือชื่อย่อ (Abbreviation)

\*\*ไม่ถือเป็นความแตกต่างเชิงสถาปัตยกรรม (Architecture Difference)\*\*

แต่ถือเป็น

> Documentation Consistency

ดังนั้น

- ไม่กระทบ Business Logic

- ไม่กระทบ SaaS Architecture

- ไม่กระทบ Source Code

- ไม่กระทบ Database Design

แต่ควรใช้ชื่อเดียวกันทั้ง Repository

---

# Naming Policy

สามารถใช้ชื่อย่อได้

ตัวอย่าง

| Full Name | Standard Repository Name |

|------------|--------------------------|

| DATABASE | DB |

| USER INTERFACE | UX |

| APPLICATION PROGRAMMING INTERFACE | API |

| SOFTWARE DESIGN SPECIFICATION | SDS |

| FUNCTIONAL DESIGN SPECIFICATION | FDS |

| QUALITY ASSURANCE | QA |

Repository จะใช้ชื่อย่อเป็นมาตรฐาน

```

DB

UX

API

FDS

SDS

QA

ADR

```

เพื่อให้

- Path สั้น

- อ่านง่าย

- ใช้กับ Script

- ใช้กับ AI

- ใช้กับ CI/CD

---

# Documentation Rule

README

Document Map

Architecture Index

Traceability Matrix

Folder Reference

ต้องอ้างอิงชื่อ Folder ให้ตรงกับ Repository จริง

ตัวอย่าง

ถูกต้อง

```

DB/

UX/

API/

```

ไม่ควรเขียน

```

DATABASE/

UI/

```

หาก Folder จริงไม่ได้ใช้ชื่อนั้น

---

# AI Compatibility

AI Agent

- Claude Code

- ChatGPT

- GitHub Copilot

- Automation Script

ควรอ้างอิง Path เดียวกันเสมอ

เพื่อลดความผิดพลาดในการค้นหาเอกสาร

---

# Repository Consistency Rule

Repository ถือเป็น Source of Truth

หากมีความแตกต่างระหว่าง

- README

- Document

- Folder

ให้ Folder Structure ใน Repository เป็นมาตรฐานอ้างอิง

และปรับเอกสารให้สอดคล้อง

---

# Impact Assessment

| Item | Impact |

|------|--------|

| SaaS Architecture | None |

| Functional Design | None |

| Software Design | None |

| Database Design | None |

| Security | None |

| DevOps | None |

| Documentation Consistency | Minor |

| AI Navigation | Improve |

---

# Executive Decision

Repository Folder Name

เป็นมาตรฐานกลางของโครงการ

การใช้ชื่อเต็มหรือชื่อย่อ

ถือว่าเป็น

\*\*Documentation Consistency Improvement\*\*

ไม่ใช่

Architecture Change

ไม่ต้องเปิด ADR ใหม่

ไม่กระทบ Build Gate

แต่ควรปรับปรุงเมื่อมีการแก้ไขเอกสารในรอบถัดไป

---

Approved By

SMEsPlus Architecture Board