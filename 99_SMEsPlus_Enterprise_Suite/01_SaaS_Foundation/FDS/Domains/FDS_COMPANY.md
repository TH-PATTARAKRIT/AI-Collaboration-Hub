# FDS\_COMPANY.md

Document ID: FDS-DOMAIN-COMPANY-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Company Management

Target Path:

`01\_SaaS\_Foundation/FDS/Domains/FDS\_COMPANY.md`

---

# 1. Purpose

Company Management เป็น Domain สำหรับจัดการโครงสร้างองค์กรภายใต้ Tenant

โดย Company เป็น Root Organization ของแต่ละ Tenant และสามารถมี Branch รวมถึงหน่วยงานภายในได้

---

# 2. Scope

## In Scope

- Create Company

- Update Company

- View Company

- Disable Company

- Enable Company

- Company Profile

- Company Logo

- Company Address

- Tax Information

- Default Settings

## Out of Scope

- Accounting

- Financial Statement

- Tax Calculation

- Payroll

---

# 3. Actors

| Actor | Description |

|--------|-------------|

| Tenant Owner | เจ้าของ Tenant |

| Company Admin | ผู้ดูแลบริษัท |

| Auditor | ผู้ตรวจสอบข้อมูล |

---

# 4. Functional Requirements

## FR-CMP-001 Create Company

System shall allow Tenant Owner to create company.

Priority

High

Permission

company.create

Screen

Company Management

API

POST /companies

Database

companies

Acceptance Criteria

- Company Name Required

- Company Code Unique in Tenant

- Company belongs to Current Tenant

- Audit Log Generated

---

## FR-CMP-002 View Company

System shall allow authorized user to view company list.

Permission

company.read

API

GET /companies

Acceptance Criteria

- Pagination Supported

- Search Supported

- Filter Supported

---

## FR-CMP-003 Update Company

Permission

company.update

API

PATCH /companies/{company\_id}

Acceptance Criteria

- Update Company Profile

- Update Address

- Update Contact

- Audit Log Generated

---

## FR-CMP-004 Disable Company

Permission

company.disable

API

PATCH /companies/{company\_id}/disable

Acceptance Criteria

- Company Status = Disabled

- User cannot create new transaction

- Audit Generated

---

## FR-CMP-005 Enable Company

Permission

company.enable

API

PATCH /companies/{company\_id}/enable

Acceptance Criteria

- Company Status = Active

- Company Ready to Use

- Audit Generated

---

## FR-CMP-006 Company Settings

Permission

company.settings

API

GET /companies/{company\_id}/settings

PATCH /companies/{company\_id}/settings

Acceptance Criteria

- Update Default Language

- Update Time Zone

- Update Currency

- Update Logo

---

# 5. Business Rules

| Rule | Description |

|-------|-------------|

| BR-CMP-001 | Company Code Unique in Tenant |

| BR-CMP-002 | Company belongs to one Tenant |

| BR-CMP-003 | Disabled Company cannot create new business transaction |

| BR-CMP-004 | Company deletion is not allowed if business data exists |

| BR-CMP-005 | Company configuration change must be audited |

---

# 6. User Stories

## US-CMP-001

As a Tenant Owner

I want to create company

So that my organization can use SMEsPlus.

---

## US-CMP-002

As Company Admin

I want to edit company information

So that organization information is always correct.

---

## US-CMP-003

As Auditor

I want to review company changes

So that configuration changes can be verified.

---

# 7. Use Cases

## UC-CMP-001 Create Company

Main Flow

1. Open Company Management

2. Click Create Company

3. Enter Company Information

4. Save

5. Validate

6. Create Company

7. Audit Log

Alternative Flow

- Duplicate Company Code

- Missing Required Fields

---

## UC-CMP-002 Disable Company

1. Select Company

2. Click Disable

3. Confirm

4. System Disable

5. Audit Log

---

# 8. Screen Mapping

| Screen ID | Screen |

|------------|---------------------|

| UX-CMP-001 | Company Dashboard |

| UX-CMP-002 | Company Form |

| UX-CMP-003 | Company Settings |

---

# 9. API Mapping

| Requirement | API |

|-------------|---------------------------|

| FR-CMP-001 | POST /companies |

| FR-CMP-002 | GET /companies |

| FR-CMP-003 | PATCH /companies/{id} |

| FR-CMP-004 | PATCH /companies/{id}/disable |

| FR-CMP-005 | PATCH /companies/{id}/enable |

| FR-CMP-006 | GET/PATCH /companies/{id}/settings |

---

# 10. Database Mapping

| Requirement | Table |

|-------------|----------------|

| FR-CMP-001 | companies |

| FR-CMP-002 | companies |

| FR-CMP-003 | companies |

| FR-CMP-004 | companies |

| FR-CMP-005 | companies |

| FR-CMP-006 | company\_settings |

---

# 11. Security Requirements

- Company belongs to Tenant

- Cross Tenant Access Prohibited

- Backend Authorization Required

- Audit Required

- Soft Delete Only

---

# 12. Audit Requirements

Audit Required

- Company Create

- Company Update

- Company Disable

- Company Enable

- Company Setting Update

Audit Fields

- company\_id

- tenant\_id

- actor\_id

- action

- request\_id

- ip\_address

- created\_at

---

# 13. Traceability

| FR | SDS | API | DB | UX | QA |

|----|-----|-----|----|----|----|

| FR-CMP-001 | SDS-CMP-001 | API-CMP-001 | DB-COMPANY | UX-CMP-001 | TC-CMP-001 |

| FR-CMP-002 | SDS-CMP-002 | API-CMP-002 | DB-COMPANY | UX-CMP-001 | TC-CMP-002 |

| FR-CMP-003 | SDS-CMP-003 | API-CMP-003 | DB-COMPANY | UX-CMP-002 | TC-CMP-003 |

| FR-CMP-004 | SDS-CMP-004 | API-CMP-004 | DB-COMPANY | UX-CMP-003 | TC-CMP-004 |

| FR-CMP-005 | SDS-CMP-005 | API-CMP-005 | DB-COMPANY | UX-CMP-003 | TC-CMP-005 |

| FR-CMP-006 | SDS-CMP-006 | API-CMP-006 | DB-COMPANY-SETTINGS | UX-CMP-003 | TC-CMP-006 |

---

# 14. Risks

| Risk | Impact | Mitigation |

|------|---------|------------|

| Duplicate Company Code | High | Unique Validation |

| Wrong Tenant Assignment | Critical | Tenant Isolation Validation |

| Unauthorized Configuration Change | High | RBAC + Audit |

| Invalid Company Status | Medium | Workflow Validation |

---

# 15. Future Enhancement

Planned Features

- Multiple Business Units

- Company Branding Theme

- Company Document Templates

- Fiscal Calendar

- Localized Business Configuration

---

# 16. Status

Ready for

- SDS

- API

- DB

- UX

- QA