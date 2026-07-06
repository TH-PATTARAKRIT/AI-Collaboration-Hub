# FR_DETAIL_AUTHORIZATION.md

Version: v0.1
Status: Draft Baseline
Project: SMEsPlus Enterprise Suite
Mode: L99
Owner: Functional Specification AI
Updated: 2026-07-06

---

# Purpose

Detailed functional requirement decomposition for Authentication and Authorization.

Source file: MODULE_SPEC_AUTHORIZATION.md

---

# Functional Requirements

| FR ID | Requirement | Business Rule | Workflow | Evidence | Status |
|---|---|---|---|---|---|
| FR-AUTH-001 | User can login with valid credential | BR-AUTH-001 | WF-AUTH-001 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-002 | System rejects invalid credential | BR-AUTH-001 | WF-AUTH-001 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-003 | Disabled user cannot login | BR-AUTH-004 | WF-AUTH-001 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-004 | System creates user session after login | BR-AUTH-001 | WF-AUTH-001 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-005 | System validates session before protected action | BR-AUTH-002 | WF-AUTH-002 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-006 | System checks tenant scope before access | BR-AUTH-002 | WF-AUTH-002 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-007 | System checks organization scope before access | BR-AUTH-002 | WF-AUTH-002 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-008 | System checks role and permission before action | BR-AUTH-002 | WF-AUTH-002 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-009 | System records failed login attempt | BR-AUTH-003 | WF-AUTH-001 | MODULE_SPEC_AUTHORIZATION.md | NEW |
| FR-AUTH-010 | User can logout and terminate session | BR-AUTH-001 | WF-AUTH-003 | MODULE_SPEC_AUTHORIZATION.md | NEW |

---

# Data Mapping Baseline

- User entity
- Role entity
- Permission entity
- Tenant entity
- Organization entity
- Session entity
- Access audit entity

---

# API Mapping Baseline

- Login API
- Logout API
- Session validation API
- Permission check API
- Current user context API

---

# UI Mapping Baseline

- Login screen
- Logout action
- Access denied page
- Session expired page

---

# UAT Baseline

| UAT ID | Related FR | Scenario | Expected Result | Status |
|---|---|---|---|---|
| UAT-AUTH-001 | FR-AUTH-001 | Valid user login | Login succeeds | NEW |
| UAT-AUTH-002 | FR-AUTH-002 | Invalid login | Login rejected | NEW |
| UAT-AUTH-003 | FR-AUTH-003 | Disabled user login | Login blocked | NEW |
| UAT-AUTH-004 | FR-AUTH-008 | User opens unauthorized function | Access denied | NEW |

---

# Traceability

Link to TRACEABILITY_MATRIX.md during next traceability update.

---

# End
