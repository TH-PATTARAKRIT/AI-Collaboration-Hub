# SMEsPlus SaaS Foundation — Functional Design Specification

Document ID: FDS-FOUNDATION-001  
Version: v1.0.0  
Status: Draft for Review  
Owner: SMEsPlus Product & Architecture Team  
Scope: SaaS Foundation  
Target Path: `01_SaaS_Foundation/FDS/SMEPLUS-SAAS-FOUNDATION-FDS.md`

## 1. Purpose

เอกสารนี้เป็น Functional Design Specification หลักของ SMEsPlus SaaS Foundation ใช้เป็น Single Source of Truth สำหรับ requirement, business rule, user story, acceptance criteria และ traceability ของระบบ Foundation

## 2. Business Objective

SMEsPlus SaaS Foundation มีเป้าหมายเพื่อสร้างแกนกลางของระบบ SaaS ที่รองรับ:

- Multi-Tenant
- Company / Branch / Division Structure
- Identity & Access Management
- Role / Permission / Policy
- Subscription & Module Activation
- Approval Workflow
- Notification
- Integration
- Audit & Governance
- Reporting Foundation

## 3. Scope

### In Scope

- Tenant Management
- Company Management
- Branch Management
- Division Management
- User Management
- Role Management
- Permission Management
- Subscription Management
- Module Activation
- Approval Foundation
- Notification Foundation
- Audit Foundation
- Integration Foundation
- Report Foundation
- Configuration Foundation

### Out of Scope

- Full Accounting Module
- Full Inventory Module
- Full HR Module
- Full CRM Module
- Full POS Module
- Production Billing Gateway
- Customer Production Migration

## 4. Requirement ID Standard

| Prefix | Domain |
|---|---|
| FR-TEN | Tenant |
| FR-CMP | Company |
| FR-BRN | Branch |
| FR-DIV | Division |
| FR-IAM | Identity & Access |
| FR-ROL | Role |
| FR-PER | Permission |
| FR-SUB | Subscription |
| FR-MOD | Module Activation |
| FR-APR | Approval |
| FR-NTF | Notification |
| FR-AUD | Audit |
| FR-INT | Integration |
| FR-RPT | Reporting |
| FR-CFG | Configuration |

## 5. Core Functional Requirements

### FR-TEN-001 — Create Tenant

System shall allow Platform Admin to create a new tenant.

Actor: Platform Admin  
Priority: High  
Related Screen: Tenant Administration  
Related API: `POST /tenants`  
Related Table: `tenants`  
Permission: `tenant.create`

Acceptance Criteria:

- Given Platform Admin is authenticated
- When Platform Admin submits valid tenant information
- Then system creates tenant with unique tenant code
- And system writes audit log

---

### FR-TEN-002 — Suspend Tenant

System shall allow Platform Admin to suspend tenant access.

Actor: Platform Admin  
Priority: High  
Related Screen: Tenant Administration  
Related API: `PATCH /tenants/{tenant_id}/suspend`  
Related Table: `tenants`  
Permission: `tenant.suspend`

Acceptance Criteria:

- Given tenant exists
- When Platform Admin suspends tenant
- Then users under tenant cannot login
- And existing active sessions are invalidated
- And audit log is created

---

### FR-CMP-001 — Create Company

System shall allow Tenant Owner to create company under tenant.

Actor: Tenant Owner  
Priority: High  
Related Screen: Company Management  
Related API: `POST /companies`  
Related Table: `companies`  
Permission: `company.create`

Acceptance Criteria:

- Given Tenant Owner is authenticated
- When company information is submitted
- Then company is created under current tenant only
- And tenant isolation is enforced

---

### FR-BRN-001 — Create Branch

System shall allow Company Admin to create branch under company.

Actor: Company Admin  
Priority: High  
Related Screen: Branch Management  
Related API: `POST /branches`  
Related Table: `branches`  
Permission: `branch.create`

Acceptance Criteria:

- Given company exists under current tenant
- When branch data is submitted
- Then branch is created under selected company
- And branch code must be unique within company

---

### FR-IAM-001 — User Login

System shall allow user to login using email and password.

Actor: User  
Priority: Critical  
Related Screen: Login  
Related API: `POST /auth/login`  
Related Table: `users`  
Permission: Public

Acceptance Criteria:

- Given user account exists and is active
- When valid credential is submitted
- Then system returns access token and refresh token
- And tenant context is included

---

### FR-IAM-002 — Invite User

System shall allow Admin to invite user into tenant.

Actor: Tenant Owner / Company Admin  
Priority: High  
Related Screen: User Management  
Related API: `POST /users/invite`  
Related Table: `users`  
Permission: `user.invite`

Acceptance Criteria:

- Given inviter has permission
- When email and role are submitted
- Then invitation is created
- And user status is `invited`
- And notification is sent

---

### FR-ROL-001 — Create Role

System shall allow authorized admin to create role.

Actor: Tenant Owner  
Priority: High  
Related Screen: Role Management  
Related API: `POST /roles`  
Related Table: `roles`  
Permission: `role.create`

Acceptance Criteria:

- Given Tenant Owner is authenticated
- When role name and scope are submitted
- Then role is created
- And role belongs to current tenant only

---

### FR-PER-001 — Assign Permission to Role

System shall allow admin to assign permissions to role.

Actor: Tenant Owner  
Priority: High  
Related Screen: Permission Matrix  
Related API: `POST /roles/{role_id}/permissions`  
Related Table: `role_permissions`  
Permission: `permission.assign`

Acceptance Criteria:

- Given role exists
- When permission list is submitted
- Then permissions are assigned
- And audit log is created

---

### FR-SUB-001 — Assign Plan to Tenant

System shall allow Platform Admin to assign subscription plan to tenant.

Actor: Platform Admin  
Priority: High  
Related Screen: Tenant Administration  
Related API: `POST /tenants/{tenant_id}/plan`  
Related Table: `subscriptions`  
Permission: `subscription.assign`

Acceptance Criteria:

- Given tenant exists
- When plan is assigned
- Then tenant receives plan entitlement
- And module availability is updated

---

### FR-MOD-001 — Activate Module

System shall allow Tenant Owner to activate eligible module.

Actor: Tenant Owner  
Priority: High  
Related Screen: Module Activation  
Related API: `POST /tenant-modules/activate`  
Related Table: `tenant_module_activations`  
Permission: `module.activate`

Acceptance Criteria:

- Given tenant has eligible plan
- When module activation is requested
- Then system validates dependency
- And activates module
- And records audit log

---

### FR-APR-001 — Create Approval Request

System shall allow user to submit approval request.

Actor: User  
Priority: Medium  
Related Screen: Approval Inbox  
Related API: `POST /approval-requests`  
Related Table: `approval_requests`  
Permission: `approval.request.create`

Acceptance Criteria:

- Given approval workflow exists
- When request is submitted
- Then approval request is created
- And approver receives notification

---

### FR-APR-002 — Approve or Reject Request

System shall allow approver to approve or reject request.

Actor: Approver  
Priority: High  
Related Screen: Approval Inbox  
Related API: `POST /approval-requests/{id}/decision`  
Related Table: `approval_requests`  
Permission: `approval.decision`

Acceptance Criteria:

- Given approval request is pending
- When approver approves or rejects
- Then request status is updated
- And action is immutable
- And audit log is created

---

### FR-NTF-001 — View Notifications

System shall allow user to view own notifications.

Actor: User  
Priority: Medium  
Related Screen: Notification Center  
Related API: `GET /notifications`  
Related Table: `notifications`  
Permission: `notification.read`

Acceptance Criteria:

- Given user is authenticated
- When user opens notification list
- Then only own notifications are displayed

---

### FR-AUD-001 — Search Audit Log

System shall allow Auditor to search audit logs.

Actor: Auditor  
Priority: Critical  
Related Screen: Audit & Governance  
Related API: `GET /audit-logs`  
Related Table: `audit_logs`  
Permission: `audit.read`

Acceptance Criteria:

- Given auditor has permission
- When filters are submitted
- Then audit logs within authorized scope are returned
- And audit logs cannot be modified or deleted

---

### FR-INT-001 — Create API Client

System shall allow admin to create API client.

Actor: Tenant Owner / Integration Admin  
Priority: Medium  
Related Screen: Integration Center  
Related API: `POST /api-clients`  
Related Table: `api_clients`  
Permission: `integration.client.create`

Acceptance Criteria:

- Given admin has permission
- When API client is created
- Then client ID and secret are generated
- And secret is shown only once

---

### FR-RPT-001 — Export Report

System shall allow authorized user to export report.

Actor: Authorized User  
Priority: Medium  
Related Screen: Reports  
Related API: `POST /reports/export`  
Related Table: report source tables  
Permission: `report.export`

Acceptance Criteria:

- Given user has report permission
- When export is requested
- Then report is generated within user scope
- And export action is logged

## 6. Non-Functional Requirements

### NFR-SEC-001 — Tenant Isolation

System must prevent access across tenants.

Acceptance Criteria:

- Backend enforces tenant context
- Database applies tenant filtering or RLS
- Tenant isolation test must pass before release

### NFR-PER-001 — API Performance

Core API response time should be under 500 ms for normal operations.

### NFR-AVA-001 — Availability

Target availability for foundation services is 99.9%.

### NFR-AUD-001 — Auditability

All critical actions must generate audit logs.

## 7. Business Rules

| Rule ID | Description |
|---|---|
| BR-001 | Tenant code must be unique |
| BR-002 | User email must be unique within tenant |
| BR-003 | Branch code must be unique within company |
| BR-004 | Suspended tenant users cannot login |
| BR-005 | Module activation must follow plan entitlement |
| BR-006 | Critical actions must be audited |
| BR-007 | Audit logs must be immutable |
| BR-008 | Permission must be enforced at backend |

## 8. Screen Inventory

| Screen ID | Screen |
|---|---|
| UI-001 | Dashboard |
| UI-002 | Tenant Administration |
| UI-003 | Company & Branch Management |
| UI-004 | User & Role Management |
| UI-005 | Module Activation |
| UI-006 | Configuration Center |
| UI-007 | Approval Inbox |
| UI-008 | Integration Center |
| UI-009 | Audit & Governance |
| UI-010 | Reports |

## 9. API Overview

| API Group | Purpose |
|---|---|
| Auth API | Login, refresh token, logout |
| Tenant API | Tenant management |
| Company API | Company and branch management |
| IAM API | User, role, permission |
| Module API | Module catalog and activation |
| Approval API | Approval workflow |
| Notification API | User notification |
| Audit API | Audit search |
| Integration API | API client and webhook |
| Report API | Report export |

## 10. Database Overview

Core tables:

- tenants
- companies
- branches
- divisions
- users
- roles
- permissions
- role_permissions
- user_role_assignments
- subscriptions
- plans
- modules
- tenant_module_activations
- approval_workflows
- approval_requests
- notifications
- api_clients
- webhooks
- audit_logs

## 11. Security Requirements

- Authentication required for protected APIs
- Authorization enforced by backend
- Tenant isolation enforced by application and database
- Audit log required for critical actions
- API secret must be shown once
- MFA-ready design required

## 12. Traceability

| Requirement | SDS | API | DB | UX | QA |
|---|---|---|---|---|---|
| FR-TEN-001 | SDS-TEN | API-TEN | DB-TENANTS | UI-002 | TC-TEN-001 |
| FR-CMP-001 | SDS-CMP | API-CMP | DB-COMPANIES | UI-003 | TC-CMP-001 |
| FR-IAM-001 | SDS-IAM | API-AUTH | DB-USERS | UI-LOGIN | TC-IAM-001 |
| FR-MOD-001 | SDS-MOD | API-MOD | DB-MODULES | UI-005 | TC-MOD-001 |
| FR-AUD-001 | SDS-AUD | API-AUD | DB-AUDIT | UI-009 | TC-AUD-001 |

## 13. Acceptance Summary

FDS is ready for SDS expansion when:

- All foundation domains have requirement IDs
- All critical requirements have acceptance criteria
- All requirements map to screen, API, database and QA
- Security and audit requirements are defined
- Business rules are approved
