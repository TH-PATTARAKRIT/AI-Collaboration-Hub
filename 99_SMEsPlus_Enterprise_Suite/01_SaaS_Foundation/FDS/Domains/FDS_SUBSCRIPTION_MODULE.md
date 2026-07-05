# FDS\_SUBSCRIPTION\_MODULE.md

Document ID: FDS-DOMAIN-SUBSCRIPTION-MODULE-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Subscription & Module Activation

Target Path: `01\_SaaS\_Foundation/FDS/Domains/FDS\_SUBSCRIPTION\_MODULE.md`

## 1. Purpose

Subscription & Module Activation Domain ใช้กำหนดแพ็กเกจการใช้งาน แผนบริการ สิทธิ์การเข้าถึง Module และการเปิดใช้งาน Module ให้กับ Tenant

Domain นี้ช่วยให้ SMEsPlus สามารถควบคุมการใช้งานระบบตาม Plan และรองรับการขยาย Module ในอนาคตโดยไม่ต้องแก้ไขโค้ดหลัก

## 2. Scope

### In Scope

- Plan Management

- Module Catalog

- Plan Module Mapping

- Tenant Subscription

- Module Activation

- Module Deactivation

- Module Dependency Validation

- Usage Limit Overview

- Subscription Status

### Out of Scope

- Payment Gateway

- Invoice Billing

- Credit Card Processing

- Marketplace Purchase Flow

- Revenue Recognition

## 3. Actors

| Actor | Description |

|---|---|

| Platform Admin | จัดการ Plan, Module และ Subscription |

| Tenant Owner | ดู Plan และเปิดใช้ Module ที่ได้รับสิทธิ์ |

| Auditor | ตรวจสอบประวัติการเปลี่ยนแปลง Subscription และ Module |

## 4. Functional Requirements

### FR-SM-001 — Create Plan

System shall allow Platform Admin to create subscription plan.

Priority: High

Permission: `plan.create`

Screen: Plan Management

API: `POST /plans`

DB: `plans`

Acceptance Criteria:

- Plan code is required

- Plan name is required

- Duplicate plan code is not allowed

- Plan status defaults to `active`

- Audit log is recorded

---

### FR-SM-002 — View Plan List

System shall allow Platform Admin to view available plans.

Priority: Medium

Permission: `plan.read`

Screen: Plan Management

API: `GET /plans`

DB: `plans`

Acceptance Criteria:

- Pagination is supported

- Filter by status is supported

- Plan module count is displayed

---

### FR-SM-003 — Create Module

System shall allow Platform Admin to create module catalog item.

Priority: High

Permission: `module.create`

Screen: Module Catalog

API: `POST /modules`

DB: `modules`

Acceptance Criteria:

- Module code is required

- Module name is required

- Duplicate module code is not allowed

- Module status defaults to `active`

- Audit log is recorded

---

### FR-SM-004 — Map Module to Plan

System shall allow Platform Admin to map modules to subscription plan.

Priority: High

Permission: `plan.module.assign`

Screen: Plan Management

API: `POST /plans/{plan\_id}/modules`

DB: `plan\_modules`

Acceptance Criteria:

- Plan must exist

- Module must exist

- Duplicate mapping is not allowed

- Audit log is recorded

---

### FR-SM-005 — Assign Subscription to Tenant

System shall allow Platform Admin to assign subscription plan to tenant.

Priority: High

Permission: `subscription.assign`

Screen: Tenant Administration

API: `POST /tenants/{tenant\_id}/subscription`

DB: `subscriptions`

Acceptance Criteria:

- Tenant must exist

- Plan must exist

- Subscription status becomes `active`

- Existing subscription history is preserved

- Audit log is recorded

---

### FR-SM-006 — View Tenant Subscription

System shall allow Tenant Owner to view current subscription.

Priority: Medium

Permission: `subscription.read`

Screen: Subscription Overview

API: `GET /tenant/subscription`

DB: `subscriptions`, `plans`

Acceptance Criteria:

- Only current tenant subscription is displayed

- Plan name and status are displayed

- Available modules are displayed

---

### FR-SM-007 — Activate Module

System shall allow Tenant Owner to activate eligible module.

Priority: High

Permission: `module.activate`

Screen: Module Activation

API: `POST /tenant-modules/activate`

DB: `tenant\_module\_activations`

Acceptance Criteria:

- Tenant must have active subscription

- Module must be included in tenant plan

- Module dependency must be validated

- Activation status becomes `active`

- Audit log is recorded

---

### FR-SM-008 — Deactivate Module

System shall allow Tenant Owner to deactivate module when allowed.

Priority: Medium

Permission: `module.deactivate`

Screen: Module Activation

API: `POST /tenant-modules/deactivate`

DB: `tenant\_module\_activations`

Acceptance Criteria:

- Module must be active

- Module must not be required by another active module

- Deactivation status becomes `inactive`

- Audit log is recorded

---

### FR-SM-009 — Validate Module Dependency

System shall validate module dependency before activation or deactivation.

Priority: High

Permission: System

Screen: Module Activation

API: Internal validation

DB: `module\_dependencies`

Acceptance Criteria:

- Required dependency must be active before activation

- Dependent module must be handled before deactivation

- Validation error must be user-readable

---

### FR-SM-010 — View Usage Limit

System shall allow authorized user to view usage limits by plan.

Priority: Medium

Permission: `subscription.usage.read`

Screen: Subscription Overview

API: `GET /tenant/subscription/usage`

DB: `subscription\_usage`

Acceptance Criteria:

- Usage is scoped to current tenant

- Current usage and limit are displayed

- Warning is shown when usage approaches limit

## 5. Business Rules

| Rule ID | Rule |

|---|---|

| BR-SM-001 | Plan code must be unique |

| BR-SM-002 | Module code must be unique |

| BR-SM-003 | Tenant can activate only modules included in active plan |

| BR-SM-004 | Module dependency must be satisfied before activation |

| BR-SM-005 | Required module cannot be deactivated if used by active dependent module |

| BR-SM-006 | Subscription history must be preserved |

| BR-SM-007 | Subscription and module changes must be audited |

| BR-SM-008 | Suspended tenant cannot activate modules |

## 6. User Stories

### US-SM-001

As a Platform Admin,

I want to create subscription plans,

So that tenants can be assigned to appropriate service packages.

### US-SM-002

As a Platform Admin,

I want to manage module catalog,

So that SMEsPlus can control which capabilities are available.

### US-SM-003

As a Tenant Owner,

I want to activate eligible modules,

So that my organization can use purchased capabilities.

### US-SM-004

As an Auditor,

I want to review subscription and module activation history,

So that changes can be verified.

## 7. Use Cases

### UC-SM-001 — Assign Subscription to Tenant

1. Platform Admin opens Tenant Administration

2. Selects tenant

3. Opens Subscription section

4. Selects plan

5. Confirms assignment

6. System validates tenant and plan

7. System creates active subscription

8. System updates available modules

9. System records audit log

Exception Flow:

- Tenant not found

- Plan inactive

- Unauthorized actor

---

### UC-SM-002 — Activate Module

1. Tenant Owner opens Module Activation

2. Selects available module

3. Clicks Activate

4. System validates subscription

5. System validates plan entitlement

6. System validates dependency

7. System activates module

8. System records audit log

Exception Flow:

- Module not included in plan

- Missing dependency

- Tenant suspended

---

### UC-SM-003 — Deactivate Module

1. Tenant Owner opens Module Activation

2. Selects active module

3. Clicks Deactivate

4. System validates dependency impact

5. System asks for confirmation

6. System deactivates module

7. System records audit log

Exception Flow:

- Module required by another active module

- Unauthorized actor

## 8. Screen Mapping

| Screen ID | Screen |

|---|---|

| UX-SM-001 | Plan Management |

| UX-SM-002 | Module Catalog |

| UX-SM-003 | Subscription Overview |

| UX-SM-004 | Module Activation |

| UX-SM-005 | Usage Limit Overview |

## 9. API Mapping

| Requirement | API |

|---|---|

| FR-SM-001 | `POST /plans` |

| FR-SM-002 | `GET /plans` |

| FR-SM-003 | `POST /modules` |

| FR-SM-004 | `POST /plans/{plan\_id}/modules` |

| FR-SM-005 | `POST /tenants/{tenant\_id}/subscription` |

| FR-SM-006 | `GET /tenant/subscription` |

| FR-SM-007 | `POST /tenant-modules/activate` |

| FR-SM-008 | `POST /tenant-modules/deactivate` |

| FR-SM-009 | Internal dependency validation |

| FR-SM-010 | `GET /tenant/subscription/usage` |

## 10. Database Mapping

| Requirement | Table |

|---|---|

| FR-SM-001 | `plans` |

| FR-SM-002 | `plans`, `plan\_modules` |

| FR-SM-003 | `modules` |

| FR-SM-004 | `plan\_modules` |

| FR-SM-005 | `subscriptions` |

| FR-SM-006 | `subscriptions`, `plans`, `modules` |

| FR-SM-007 | `tenant\_module\_activations` |

| FR-SM-008 | `tenant\_module\_activations` |

| FR-SM-009 | `module\_dependencies` |

| FR-SM-010 | `subscription\_usage` |

## 11. Security Requirements

- Only Platform Admin can create plans and modules

- Tenant Owner can activate only eligible modules

- Module activation must be scoped to current tenant

- Backend must enforce plan entitlement

- Frontend must not be trusted for entitlement validation

- Suspended tenant cannot change subscription or module state

## 12. Audit Requirements

Audit required for:

- Plan creation

- Plan update

- Module creation

- Plan-module mapping

- Subscription assignment

- Module activation

- Module deactivation

- Usage limit change

Audit fields:

- tenant\_id

- actor\_id

- action

- resource\_type

- resource\_id

- before\_value

- after\_value

- request\_id

- ip\_address

- created\_at

## 13. Traceability

| FR | SDS | API | DB | UX | QA |

|---|---|---|---|---|---|

| FR-SM-001 | SDS-SM-001 | API-PLAN-001 | DB-PLANS | UX-SM-001 | TC-SM-001 |

| FR-SM-002 | SDS-SM-002 | API-PLAN-002 | DB-PLANS | UX-SM-001 | TC-SM-002 |

| FR-SM-003 | SDS-SM-003 | API-MOD-001 | DB-MODULES | UX-SM-002 | TC-SM-003 |

| FR-SM-004 | SDS-SM-004 | API-PLAN-003 | DB-PLAN-MODULES | UX-SM-001 | TC-SM-004 |

| FR-SM-005 | SDS-SM-005 | API-SUB-001 | DB-SUBSCRIPTIONS | UX-SM-003 | TC-SM-005 |

| FR-SM-006 | SDS-SM-006 | API-SUB-002 | DB-SUBSCRIPTIONS | UX-SM-003 | TC-SM-006 |

| FR-SM-007 | SDS-SM-007 | API-MOD-002 | DB-TENANT-MODULES | UX-SM-004 | TC-SM-007 |

| FR-SM-008 | SDS-SM-008 | API-MOD-003 | DB-TENANT-MODULES | UX-SM-004 | TC-SM-008 |

| FR-SM-009 | SDS-SM-009 | API-MOD-004 | DB-MODULE-DEPENDENCIES | UX-SM-004 | TC-SM-009 |

| FR-SM-010 | SDS-SM-010 | API-SUB-003 | DB-SUBSCRIPTION-USAGE | UX-SM-005 | TC-SM-010 |

## 14. Risks

| Risk | Impact | Mitigation |

|---|---|---|

| Tenant activates unauthorized module | High | Backend entitlement validation |

| Dependency conflict | Medium | Dependency validation before change |

| Incorrect subscription assignment | High | Confirmation and audit |

| Usage limit mismatch | Medium | Centralized usage calculation |

| Billing expectation mismatch | Medium | Clearly mark billing gateway as out of scope |

## 15. Status

Ready for SDS, API, DB, SECURITY, UX and QA expansion.