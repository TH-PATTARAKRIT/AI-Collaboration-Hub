# FDS\_ROLE\_PERMISSION.md

Document ID: FDS-DOMAIN-ROLE-PERMISSION-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Role & Permission

Target Path: `01\_SaaS\_Foundation/FDS/Domains/FDS\_ROLE\_PERMISSION.md`

## 1. Purpose

Role & Permission Domain ใช้กำหนดสิทธิ์การใช้งานระบบ SMEsPlus โดยควบคุมว่า User แต่ละคนสามารถเข้าถึงเมนู ข้อมูล และ Action ใดได้บ้าง

ระบบต้องรองรับ RBAC เป็นหลัก และเตรียมรองรับ ABAC สำหรับเงื่อนไขเพิ่มเติม เช่น Tenant, Company, Branch และ Module Scope

## 2. Scope

### In Scope

- Role Management

- Permission Management

- Assign Role to User

- Assign Permission to Role

- Scope-based Access

- Permission Audit

- Default Role Template

### Out of Scope

- External IAM Provider

- Advanced Policy Engine

- Custom Script-based Permission

## 3. Actors

| Actor | Description |

|---|---|

| Platform Admin | จัดการสิทธิ์ระดับ Platform |

| Tenant Owner | จัดการ Role ภายใน Tenant |

| Company Admin | จัดการ User Role ภายใน Company |

| Auditor | ตรวจสอบประวัติการเปลี่ยนแปลงสิทธิ์ |

## 4. Functional Requirements

### FR-RP-001 — Create Role

System shall allow Tenant Owner to create role.

Priority: High

Permission: `role.create`

Screen: User & Role Management

API: `POST /roles`

DB: `roles`

Acceptance Criteria:

- Role name is required

- Role belongs to current tenant

- Duplicate role name in same tenant is not allowed

- Audit log is recorded

---

### FR-RP-002 — View Role List

System shall allow authorized user to view role list.

Priority: High

Permission: `role.read`

API: `GET /roles`

DB: `roles`

Acceptance Criteria:

- Only roles within current tenant are shown

- Search and filter are supported

- Pagination is supported

---

### FR-RP-003 — Update Role

System shall allow Tenant Owner to update role information.

Priority: Medium

Permission: `role.update`

API: `PATCH /roles/{role\_id}`

DB: `roles`

Acceptance Criteria:

- Role exists under current tenant

- Role name can be updated

- System roles cannot be modified unless allowed

- Audit log is recorded

---

### FR-RP-004 — Delete Role

System shall allow Tenant Owner to delete unused role.

Priority: Medium

Permission: `role.delete`

API: `DELETE /roles/{role\_id}`

DB: `roles`

Acceptance Criteria:

- Role must not be assigned to active users

- System role cannot be deleted

- Soft delete is applied

- Audit log is recorded

---

### FR-RP-005 — Assign Permission to Role

System shall allow Tenant Owner to assign permissions to role.

Priority: High

Permission: `permission.assign`

API: `POST /roles/{role\_id}/permissions`

DB: `role\_permissions`

Acceptance Criteria:

- Role exists within current tenant

- Permission code must be valid

- Permission assignment is saved

- Audit log is recorded

---

### FR-RP-006 — Assign Role to User

System shall allow admin to assign role to user.

Priority: High

Permission: `user.role.assign`

API: `POST /users/{user\_id}/roles`

DB: `user\_role\_assignments`

Acceptance Criteria:

- User exists under current tenant

- Role exists under current tenant

- Scope must be valid

- Audit log is recorded

---

### FR-RP-007 — View Permission Matrix

System shall allow admin to view permission matrix.

Priority: Medium

Permission: `permission.read`

API: `GET /permissions/matrix`

DB: `permissions`, `role\_permissions`

Acceptance Criteria:

- Permissions are grouped by module

- Role-permission status is displayed

- Read-only users cannot modify matrix

---

### FR-RP-008 — Permission Audit

System shall record all permission changes.

Priority: Critical

Permission: `audit.read`

API: `GET /audit-logs?resource=permission`

DB: `audit\_logs`

Acceptance Criteria:

- Role creation is audited

- Permission assignment is audited

- Role assignment is audited

- Actor and timestamp are recorded

## 5. Business Rules

| Rule ID | Rule |

|---|---|

| BR-RP-001 | Role name must be unique within tenant |

| BR-RP-002 | System roles cannot be deleted |

| BR-RP-003 | User permission must be enforced by backend |

| BR-RP-004 | Frontend permission only controls visibility, not security |

| BR-RP-005 | Permission change must be audited |

| BR-RP-006 | User cannot assign permission higher than own authority |

## 6. User Stories

### US-RP-001

As a Tenant Owner,

I want to create roles,

So that I can control user responsibilities.

### US-RP-002

As a Company Admin,

I want to assign roles to users,

So that users can access the correct functions.

### US-RP-003

As an Auditor,

I want to review permission changes,

So that access control can be verified.

## 7. Use Cases

### UC-RP-001 — Create Role

1. Tenant Owner opens Role Management

2. Clicks Create Role

3. Enters role name and scope

4. Saves role

5. System validates duplicate name

6. System creates role

7. System records audit log

Exception Flow:

- Duplicate role name

- Missing required field

- Unauthorized actor

---

### UC-RP-002 — Assign Permission

1. Tenant Owner opens Permission Matrix

2. Selects role

3. Selects permissions

4. Saves changes

5. System validates permission list

6. System updates role permissions

7. System records audit log

---

### UC-RP-003 — Assign Role to User

1. Admin opens User Detail

2. Selects Assign Role

3. Chooses role and scope

4. Saves assignment

5. System validates role and user scope

6. System records audit log

## 8. Screen Mapping

| Screen ID | Screen |

|---|---|

| UX-RP-001 | User & Role Management |

| UX-RP-002 | Role Form |

| UX-RP-003 | Permission Matrix |

| UX-RP-004 | User Role Assignment |

| UX-RP-005 | Permission Audit View |

## 9. API Mapping

| Requirement | API |

|---|---|

| FR-RP-001 | `POST /roles` |

| FR-RP-002 | `GET /roles` |

| FR-RP-003 | `PATCH /roles/{role\_id}` |

| FR-RP-004 | `DELETE /roles/{role\_id}` |

| FR-RP-005 | `POST /roles/{role\_id}/permissions` |

| FR-RP-006 | `POST /users/{user\_id}/roles` |

| FR-RP-007 | `GET /permissions/matrix` |

| FR-RP-008 | `GET /audit-logs` |

## 10. Database Mapping

| Requirement | Table |

|---|---|

| FR-RP-001 | `roles` |

| FR-RP-002 | `roles` |

| FR-RP-003 | `roles` |

| FR-RP-004 | `roles` |

| FR-RP-005 | `role\_permissions`, `permissions` |

| FR-RP-006 | `user\_role\_assignments`, `users`, `roles` |

| FR-RP-007 | `permissions`, `role\_permissions` |

| FR-RP-008 | `audit\_logs` |

## 11. Security Requirements

- Backend must enforce all permissions

- Tenant isolation is required for roles and assignments

- Admin cannot assign permissions beyond own authority

- Permission matrix must be read-only for unauthorized users

- Critical permission changes require audit log

## 12. Audit Requirements

Audit required for:

- Role create

- Role update

- Role delete

- Permission assignment

- Permission removal

- User role assignment

- User role removal

## 13. Traceability

| FR | SDS | API | DB | UX | QA |

|---|---|---|---|---|---|

| FR-RP-001 | SDS-RP-001 | API-RP-001 | DB-ROLES | UX-RP-002 | TC-RP-001 |

| FR-RP-002 | SDS-RP-002 | API-RP-002 | DB-ROLES | UX-RP-001 | TC-RP-002 |

| FR-RP-003 | SDS-RP-003 | API-RP-003 | DB-ROLES | UX-RP-002 | TC-RP-003 |

| FR-RP-004 | SDS-RP-004 | API-RP-004 | DB-ROLES | UX-RP-001 | TC-RP-004 |

| FR-RP-005 | SDS-RP-005 | API-RP-005 | DB-ROLE-PERMISSIONS | UX-RP-003 | TC-RP-005 |

| FR-RP-006 | SDS-RP-006 | API-RP-006 | DB-USER-ROLE | UX-RP-004 | TC-RP-006 |

| FR-RP-007 | SDS-RP-007 | API-RP-007 | DB-PERMISSIONS | UX-RP-003 | TC-RP-007 |

| FR-RP-008 | SDS-RP-008 | API-AUD-001 | DB-AUDIT | UX-RP-005 | TC-RP-008 |

## 14. Risks

| Risk | Impact | Mitigation |

|---|---|---|

| Unauthorized permission escalation | Critical | Backend enforcement and audit |

| Incorrect role assignment | High | Scope validation |

| System role deletion | High | Protect system roles |

| Permission drift | Medium | Periodic permission audit |

## 15. Status

Ready for SDS, API, DB, SECURITY, UX and QA expansion.