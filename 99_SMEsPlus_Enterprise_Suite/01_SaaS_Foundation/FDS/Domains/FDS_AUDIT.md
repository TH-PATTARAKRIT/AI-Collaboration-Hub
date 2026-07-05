# FDS\_AUDIT.md

Document ID: FDS-DOMAIN-AUDIT-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Audit & Activity Logging

Target Path:

`01\_SaaS\_Foundation/FDS/Domains/FDS\_AUDIT.md`

---

# 1. Purpose

Audit Domain เป็นศูนย์กลางสำหรับจัดเก็บประวัติการทำงาน (Audit Trail)

ของทุก Module ภายใน SMEsPlus

Audit Log ใช้สำหรับ

- Security Investigation

- Compliance

- User Activity

- Data Change Tracking

- System Troubleshooting

ทุก Module ต้องส่ง Event มายัง Audit Service

---

# 2. Scope

## In Scope

- User Activity Log

- Data Change Log

- Login History

- Permission Change

- Configuration Change

- API Activity

- Search Audit

- Export Audit

## Out of Scope

- SIEM

- External Log Aggregator

- Infrastructure Monitoring

---

# 3. Actors

| Actor | Description |

|--------|-------------|

| Platform Admin | ตรวจสอบระบบ |

| Tenant Owner | ตรวจสอบข้อมูลของ Tenant |

| Auditor | ผู้ตรวจสอบ |

| System | ส่ง Audit Event |

---

# 4. Functional Requirements

## FR-AUD-001 Record Audit Log

API

POST /audit/events

Acceptance Criteria

- Event Recorded

- Timestamp Generated

- Immutable

---

## FR-AUD-002 Search Audit

API

GET /audit/events

Acceptance Criteria

- Filter by User

- Filter by Date

- Filter by Module

- Pagination

---

## FR-AUD-003 View Audit Detail

API

GET /audit/events/{id}

Acceptance Criteria

- Complete Event Detail

- Actor

- Resource

- Before Value

- After Value

---

## FR-AUD-004 Export Audit

API

POST /audit/export

Acceptance Criteria

- CSV

- Excel

- PDF

---

## FR-AUD-005 Login History

API

GET /audit/login-history

Acceptance Criteria

- Login

- Logout

- Failed Login

---

## FR-AUD-006 Configuration History

Acceptance Criteria

- Configuration Change

- Old Value

- New Value

---

# 5. Business Rules

BR-AUD-001

Audit Log cannot be edited

BR-AUD-002

Audit Log cannot be deleted

BR-AUD-003

Audit belongs to Tenant

BR-AUD-004

Critical Action must create Audit

---

# 6. User Stories

US-AUD-001

As Auditor

I want to search audit history

So that I can investigate incidents.

---

US-AUD-002

As Platform Admin

I want to export audit log

So that compliance reports can be generated.

---

# 7. Use Cases

UC-AUD-001 Search Audit

1 Search

2 Filter

3 View Detail

4 Export

---

UC-AUD-002 View Login History

1 Select User

2 View Login Timeline

3 View Failed Login

---

# 8. Screen Mapping

UX-AUD-001 Audit Dashboard

UX-AUD-002 Audit Detail

UX-AUD-003 Login History

---

# 9. API Mapping

POST /audit/events

GET /audit/events

GET /audit/events/{id}

POST /audit/export

GET /audit/login-history

---

# 10. Database Mapping

audit\_logs

audit\_changes

audit\_exports

login\_histories

---

# 11. Security

Read Only

RBAC

Tenant Isolation

Immutable

---

# 12. Audit Fields

audit\_id

tenant\_id

user\_id

action

resource

resource\_id

before\_value

after\_value

request\_id

ip\_address

user\_agent

created\_at

---

# 13. Traceability

FR → SDS → API → DB → UX → QA

---

# 14. Risks

Unauthorized Audit Access

Large Audit Volume

Long Retention

---

# 15. Status

Ready for

SDS

API

DB

SECURITY

QA