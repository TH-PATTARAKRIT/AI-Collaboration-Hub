# TRACEABILITY_MATRIX.md

**Version:** v1.0  
**Status:** Operational Baseline  
**Owner:** Functional Specification AI / SMEsPlus PMO  
**Project:** SMEsPlus Enterprise Suite  
**Branch:** SMEsPlus  
**Last Updated:** 2026-07-06

---

# Purpose

เอกสารนี้ใช้ควบคุม Traceability ของ Functional Specification ตั้งแต่ Requirement ถึง Evidence และ Gate Result

This matrix links functional requirements to business rules, workflows, data mapping, API mapping, UI mapping, acceptance criteria, evidence, and gate result.

---

# Traceability Rule

ทุก Functional Requirement ต้องมีการเชื่อมโยงอย่างน้อย

```text
Functional Requirement
-> Business Rule
-> Business Process / Workflow
-> Module
-> Database Mapping
-> API / Event Mapping
-> UI Mapping
-> Acceptance Criteria
-> Evidence
-> Gate Result
```

No Evidence = No Progress

---

# Status Definition

| Status | Meaning |
|---|---|
| NEW | New requirement, not yet reviewed |
| MATCHED | Evidence and mapping are complete |
| PARTIAL | Some evidence exists but mapping is incomplete |
| GAP | Missing required evidence or mapping |
| HOLD | Cannot proceed until owner resolves issue |
| RETIRE | Requirement should not continue |
| APPROVED | Reviewed and accepted by authorized owner |

---

# Matrix

| FR ID | Function | Module | Business Rule ID | Workflow ID | DB Mapping | API/Event Mapping | UI Mapping | Acceptance Criteria | Evidence Location | Owner | Reviewer | Gate Result | Status | Next Action |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-000 | AI Session Bootstrap Control | Repository Governance | BR-000 | WF-000 | N/A | N/A | N/A | AI can resume from repository source of truth | `AI_SESSION_BOOTSTRAP.md` | PMO AI / Liza | Repository Owner | REVIEW REQUIRED | PARTIAL | Link to work package and role directory |
| FR-001 | Functional Specification Bootstrap | Functional Design | BR-001 | WF-001 | Pending | Pending | Pending | Functional AI can start FDS without repeated explanation | Pending | Functional Specification AI | PMO AI | HOLD | NEW | Create first functional work package |

---

# Evidence Requirement

Evidence must include

- File path or link
- Owner
- Timestamp
- Reviewer or verifier
- Status
- Gate impact

If evidence is missing, mark status as `GAP` or `HOLD`.

---

# Functional Specification Use

Functional Specification AI must update this matrix when producing or reviewing

- Functional Specification
- Business Rules
- Workflow
- Database Mapping
- API Mapping
- UI Mapping
- Acceptance Criteria
- UAT / QA input

---

# End
