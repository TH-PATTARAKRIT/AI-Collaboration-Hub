# 06 — User Stories

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-006
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Pending Boss

## 1. Purpose

ระบุ user story ต่อ persona สำหรับ SaaS Foundation เพื่อเชื่อมโยง FR กับความต้องการเชิงผู้ใช้งานจริง

## 2. Personas

| Persona | Description |
|---|---|
| Tenant Admin | ผู้ดูแลระบบขององค์กรลูกค้า จัดการผู้ใช้และ subscription ของ tenant ตนเอง |
| Standard User | พนักงานทั่วไปที่ใช้งานโมดูลธุรกิจตามสิทธิ์ที่ได้รับ |
| SMEsPlus Operations | ทีมงานฝั่ง SMEsPlus ที่ดูแล tenant provisioning และ billing |

## 3. Stories — FR-FD-001 (Tenant Management & Isolation)

- **US-FD-001-01**: As a SMEsPlus Operations staff, I want to provision a new tenant with an isolated data space, so that a new customer can start using the system without seeing any other tenant's data.
- **US-FD-001-02**: As a Tenant Admin, I want to be certain that my organization's data can never be viewed by another tenant, so that I can trust the platform with sensitive business data.

## 4. Stories — FR-FD-002 (RBAC)

- **US-FD-002-01**: As a Tenant Admin, I want to assign roles (Manager, Standard User, Read-only) to my employees, so that each person only sees what their job requires.
- **US-FD-002-02**: As a Standard User, I want to be blocked from actions outside my role, so that I cannot accidentally modify data I'm not authorized to touch.
- **US-FD-002-03**: As a Tenant Admin, I want to see an audit trail of role changes, so that I can review who granted access and when.

## 5. Stories — FR-FD-003 (Subscription Package Management)

- **US-FD-003-01**: As a Tenant Admin, I want to see which subscription tier my organization is on and what modules it includes, so that I know what I'm paying for.
- **US-FD-003-02**: As a Tenant Admin, I want to upgrade my subscription tier, so that I can unlock additional modules as my business grows.
- **US-FD-003-03**: As SMEsPlus Operations, I want subscriptions to gracefully expire (not delete data) when unpaid, so that customers can renew without data loss.

## 6. Stories — FR-FD-004 (Module Activation & Licensing)

- **US-FD-004-01**: As a Tenant Admin, I want to see only the modules included in my subscription tier in my navigation menu, so that I'm not confused by features I can't use.
- **US-FD-004-02**: As SMEsPlus Operations, I want module activation to be enforced at the API level, not just hidden in the UI, so that tenants cannot bypass licensing by calling the API directly.

## 7. Traceability

| Story ID | FR ID |
|---|---|
| US-FD-001-01, US-FD-001-02 | FR-FD-001 |
| US-FD-002-01, US-FD-002-02, US-FD-002-03 | FR-FD-002 |
| US-FD-003-01, US-FD-003-02, US-FD-003-03 | FR-FD-003 |
| US-FD-004-01, US-FD-004-02 | FR-FD-004 |

## 8. Related Documents

- `03_FUNCTIONAL_REQUIREMENTS.md`
- `07_USE_CASES.md`

## 9. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial user stories draft | Functional Specification AI (Claude) |
