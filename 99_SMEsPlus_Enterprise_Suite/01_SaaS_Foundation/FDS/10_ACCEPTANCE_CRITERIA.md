# 10 — Acceptance Criteria

Document ID: SMEPLUS-SAAS-FOUNDATION-FDS-010
Version: v0.1
Status: Draft — In Review
Owner: Functional Specification AI (with QA UAT AI input)
Reviewers: PMO AI, QA UAT AI
Approval: Pending Boss

## 1. Purpose

ระบุ acceptance criteria แบบ Given/When/Then สำหรับแต่ละ FR เพื่อให้ QA UAT AI นำไปสร้าง test case และเป็นเกณฑ์ evidence ว่างานเสร็จสมบูรณ์ตาม Definition of Done

## 2. AC — FR-FD-001 (Tenant Management & Isolation)

**AC-FD-001-01**
Given a new tenant has been provisioned
When any user of Tenant A queries data
Then the result must never contain records belonging to Tenant B

**AC-FD-001-02**
Given a tenant provisioning request fails midway
When the system rolls back
Then no partial tenant record, user, or subscription remains in the database

## 3. AC — FR-FD-002 (RBAC)

**AC-FD-002-01**
Given a Tenant Admin assigns the "Read-only User" role to a user
When that user attempts to modify any record
Then the system rejects the action with an authorization error

**AC-FD-002-02**
Given a role change is made
When the change is saved
Then an AuditLog entry is created with actor, timestamp, and before/after role

## 4. AC — FR-FD-003 (Subscription Package Management)

**AC-FD-003-01**
Given a tenant's subscription expires
When the expiry date passes
Then the tenant's data remains intact but access to tier-restricted modules is blocked

**AC-FD-003-02**
Given a Tenant Admin upgrades to a higher tier
When the upgrade is confirmed
Then all modules included in the new tier become accessible without manual reactivation

## 5. AC — FR-FD-004 (Module Activation & Licensing)

**AC-FD-004-01**
Given a module is not included in a tenant's subscription tier
When a user of that tenant calls the module's API directly
Then the API returns an authorization error, not just a hidden UI element

**AC-FD-004-02**
Given a module is newly activated for a tenant
When the tenant's user refreshes their session
Then the module appears in navigation within the NFR-PERF-03 target time (≤ 5s)

## 6. Definition of Done (applies to all FR above)

โมดูล/ฟีเจอร์จะนับว่า "Done" ได้ก็ต่อเมื่อ:

1. Acceptance criteria ทั้งหมดของ FR นั้นผ่าน UAT
2. มี evidence (screenshot, log, test result) แนบใน `08_Testing_Evidence/`
3. Code review ผ่านตาม `CODE_REVIEW_PLAYBOOK.md` (เมื่อ playbook นี้ upload ครบ)
4. Security checklist ที่เกี่ยวข้องผ่านตาม `SECURITY/SECURITY_CHECKLIST.md`
5. PMO AI ยืนยัน evidence ครบตาม No Evidence = No Progress
6. Boss อนุมัติ

## 7. Related Documents

- `03_FUNCTIONAL_REQUIREMENTS.md`
- `07_USE_CASES.md`
- `08_Testing_Evidence/` (repository-level testing evidence folder)
- `QA/TEST_CASES.md`

## 8. Change History

| Date | Version | Change | Author |
|---|---|---|---|
| 2026-07-02 | v0.1 | Initial acceptance criteria draft | Functional Specification AI (Claude) |
