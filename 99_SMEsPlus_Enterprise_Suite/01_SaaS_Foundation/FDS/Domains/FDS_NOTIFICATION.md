# FDS\_NOTIFICATION.md

Document ID: FDS-DOMAIN-NOTIFICATION-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Notification

---

# 1. Purpose

Notification Domain เป็นบริการกลางสำหรับการแจ้งเตือนผู้ใช้งานของ SMEsPlus

รองรับการแจ้งเตือนจากทุก Module เช่น

- Approval

- User Invitation

- Subscription

- System Alert

- Security Event

- Business Event

---

# 2. Scope

## In Scope

- In-App Notification

- Email Notification

- Push Notification (Future Ready)

- Notification Template

- Notification Preference

- Read / Unread

- Archive Notification

## Out of Scope

- SMS Gateway

- LINE OA Integration

- Marketing Campaign

---

# 3. Actors

| Actor | Description |

|--------|-------------|

| User | ผู้ใช้งาน |

| System | ระบบ |

| Administrator | ผู้ดูแลระบบ |

---

# 4. Functional Requirements

## FR-NTF-001 Create Notification

API

POST /notifications

Acceptance Criteria

- Notification Created

- Notification Type Valid

- Audit Recorded

---

## FR-NTF-002 View Notification

API

GET /notifications

Acceptance Criteria

- Only Current User

- Pagination

- Filter Supported

---

## FR-NTF-003 Mark As Read

API

PATCH /notifications/{id}/read

Acceptance Criteria

- Status Updated

- Timestamp Recorded

---

## FR-NTF-004 Archive Notification

API

PATCH /notifications/{id}/archive

Acceptance Criteria

- Notification Hidden

- Audit Recorded

---

## FR-NTF-005 Notification Preference

API

PATCH /notification-preferences

Acceptance Criteria

- Email On/Off

- In-App On/Off

---

# 5. Business Rules

BR-NTF-001

Notification belongs to User

BR-NTF-002

Notification cannot cross Tenant

BR-NTF-003

Archived Notification still retained

---

# 6. Screen Mapping

UX-NTF-001 Notification Center

UX-NTF-002 Notification Preference

---

# 7. API Mapping

POST /notifications

GET /notifications

PATCH /notifications/{id}/read

PATCH /notifications/{id}/archive

PATCH /notification-preferences

---

# 8. Database

notifications

notification\_preferences

notification\_templates

---

# 9. Security

Tenant Isolation

RBAC

Audit

---

# 10. Status

Ready for SDS/API/DB