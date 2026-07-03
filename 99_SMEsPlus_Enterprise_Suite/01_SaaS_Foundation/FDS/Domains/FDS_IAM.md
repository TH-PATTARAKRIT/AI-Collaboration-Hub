# FDS\_IAM.md

Document ID: FDS-DOMAIN-IAM-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Identity & Access Management (IAM)

Target Path:

`01\_SaaS\_Foundation/FDS/Domains/FDS\_IAM.md`

---

# 1. Purpose

Identity & Access Management (IAM) เป็น Domain สำหรับการจัดการผู้ใช้งาน การยืนยันตัวตน (Authentication) และการควบคุมการเข้าถึงระบบ (Authorization)

Domain นี้เป็นพื้นฐานของทุก Module ภายใน SMEsPlus และทำงานร่วมกับ Role, Permission, Audit และ Tenant Isolation

---

# 2. Scope

## In Scope

- User Registration (Invitation)

- User Profile

- User Status

- Login

- Logout

- Refresh Token

- Change Password

- Reset Password

- Account Lock

- Session Management

- MFA Ready

- User Preference

## Out of Scope

- Social Login

- External Identity Provider (SSO)

- Biometric Authentication

---

# 3. Actors

| Actor | Description |

|--------|-------------|

| Platform Admin | ผู้ดูแลระบบแพลตฟอร์ม |

| Tenant Owner | เจ้าของ Tenant |

| Company Admin | ผู้ดูแลบริษัท |

| User | ผู้ใช้งานทั่วไป |

---

# 4. Functional Requirements

## FR-IAM-001 Login

System shall allow registered user to login.

Priority

Critical

Permission

Public

API

POST /auth/login

Screen

Login

Acceptance Criteria

- Email และ Password ถูกต้อง

- User Status = Active

- Tenant Status = Active

- Return Access Token

- Return Refresh Token

- Record Login Audit

---

## FR-IAM-002 Logout

API

POST /auth/logout

Acceptance Criteria

- Session Invalidated

- Refresh Token Revoked

- Audit Recorded

---

## FR-IAM-003 Refresh Token

API

POST /auth/refresh

Acceptance Criteria

- Refresh Token Valid

- Issue New Access Token

- Old Token Invalidated

---

## FR-IAM-004 Invite User

Permission

user.invite

API

POST /users/invite

Acceptance Criteria

- Email Required

- Role Required

- Invitation Expiration Configurable

---

## FR-IAM-005 Activate User

API

POST /users/activate

Acceptance Criteria

- Invitation Valid

- Password Created

- Status Active

---

## FR-IAM-006 Change Password

Permission

user.change\_password

API

PATCH /users/password

Acceptance Criteria

- Current Password Required

- New Password Policy Valid

- Audit Recorded

---

## FR-IAM-007 Reset Password

Permission

user.reset\_password

API

POST /users/reset-password

Acceptance Criteria

- Email Verified

- Reset Token Generated

- Expiration Enforced

---

## FR-IAM-008 Lock Account

Permission

system

Acceptance Criteria

- Lock after configurable failed attempts

- Automatic unlock supported

- Audit Recorded

---

## FR-IAM-009 User Profile

Permission

user.profile

Acceptance Criteria

- Update Name

- Update Phone

- Update Avatar

- Update Language

---

## FR-IAM-010 Session Management

Permission

Authenticated User

Acceptance Criteria

- View Active Sessions

- Revoke Session

- Automatic Expiration

---

# 5. Business Rules

| Rule ID | Description |

|----------|-------------|

| BR-IAM-001 | Email ต้องไม่ซ้ำภายใน Tenant |

| BR-IAM-002 | Password ต้องเป็นไปตาม Password Policy |

| BR-IAM-003 | User ต้องอยู่ภายใต้ Tenant เดียว |

| BR-IAM-004 | Locked User ไม่สามารถ Login |

| BR-IAM-005 | Suspended Tenant Login ไม่ได้ |

| BR-IAM-006 | Refresh Token ใช้ได้ครั้งเดียว |

---

# 6. User Stories

### US-IAM-001

As a User

I want to login securely

So that I can access SMEsPlus.

---

### US-IAM-002

As an Administrator

I want to invite new users

So that my organization can collaborate.

---

### US-IAM-003

As a User

I want to change my password

So that my account remains secure.

---

# 7. Use Cases

## UC-IAM-001 Login

Main Flow

1. Open Login Screen

2. Enter Email

3. Enter Password

4. Validate Credential

5. Create Session

6. Return JWT

7. Redirect Dashboard

Alternative Flow

- Wrong Password

- Locked Account

- Suspended Tenant

---

## UC-IAM-002 Reset Password

Main Flow

1. Request Reset

2. Receive Email

3. Open Reset Link

4. Enter New Password

5. Password Updated

---

# 8. Screen Mapping

| Screen | Description |

|---------|-------------|

| UX-IAM-001 | Login |

| UX-IAM-002 | Forgot Password |

| UX-IAM-003 | Reset Password |

| UX-IAM-004 | User Profile |

| UX-IAM-005 | Session Management |

---

# 9. API Mapping

| Requirement | API |

|-------------|-----|

| FR-IAM-001 | POST /auth/login |

| FR-IAM-002 | POST /auth/logout |

| FR-IAM-003 | POST /auth/refresh |

| FR-IAM-004 | POST /users/invite |

| FR-IAM-005 | POST /users/activate |

| FR-IAM-006 | PATCH /users/password |

| FR-IAM-007 | POST /users/reset-password |

| FR-IAM-008 | PATCH /users/lock |

| FR-IAM-009 | PATCH /users/profile |

| FR-IAM-010 | GET /sessions |

---

# 10. Database Mapping

| Requirement | Table |

|-------------|-------|

| Login | users |

| Session | user\_sessions |

| Invitation | user\_invitations |

| Password Reset | password\_reset\_tokens |

| Audit | audit\_logs |

---

# 11. Security Requirements

- JWT Authentication

- Refresh Token Rotation

- Password Hashing (Argon2id หรือ bcrypt)

- HTTPS Only

- Secure Cookie Support

- MFA Ready

- Session Timeout

- Account Lock Policy

- Password Complexity Policy

---

# 12. Audit Requirements

Audit Required

- Login

- Logout

- Password Change

- Password Reset

- Account Lock

- Invitation

- Profile Update

---

# 13. Traceability

| FR | SDS | API | DB | UX | QA |

|----|-----|-----|----|----|----|

| FR-IAM-001 | SDS-IAM-001 | API-AUTH-001 | DB-USERS | UX-IAM-001 | TC-IAM-001 |

| FR-IAM-002 | SDS-IAM-002 | API-AUTH-002 | DB-SESSIONS | UX-IAM-001 | TC-IAM-002 |

| FR-IAM-003 | SDS-IAM-003 | API-AUTH-003 | DB-SESSIONS | UX-IAM-001 | TC-IAM-003 |

| FR-IAM-004 | SDS-IAM-004 | API-USER-001 | DB-INVITATION | UX-IAM-004 | TC-IAM-004 |

| FR-IAM-005 | SDS-IAM-005 | API-USER-002 | DB-USERS | UX-IAM-004 | TC-IAM-005 |

| FR-IAM-006 | SDS-IAM-006 | API-USER-003 | DB-USERS | UX-IAM-004 | TC-IAM-006 |

| FR-IAM-007 | SDS-IAM-007 | API-USER-004 | DB-RESET | UX-IAM-003 | TC-IAM-007 |

| FR-IAM-008 | SDS-IAM-008 | API-USER-005 | DB-USERS | UX-IAM-004 | TC-IAM-008 |

| FR-IAM-009 | SDS-IAM-009 | API-USER-006 | DB-USERS | UX-IAM-004 | TC-IAM-009 |

| FR-IAM-010 | SDS-IAM-010 | API-SESSION-001 | DB-SESSIONS | UX-IAM-005 | TC-IAM-010 |

---

# 14. Risks

| Risk | Impact | Mitigation |

|------|---------|------------|

| Credential Theft | Critical | MFA Ready, Strong Password Policy |

| Brute Force Attack | High | Account Lock + Rate Limiting |

| Session Hijacking | High | Refresh Token Rotation |

| Unauthorized Access | Critical | RBAC + Tenant Isolation |

---

# 15. Status

Ready for

- SDS

- API

- DB

- SECURITY

- UX

- QA