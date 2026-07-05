# FDS\_INTEGRATION.md

Document ID: FDS-DOMAIN-INTEGRATION-001

Version: v1.0.0

Status: Draft

Owner: SMEsPlus Product Team

Domain: Integration

Target Path:

`01\_SaaS\_Foundation/FDS/Domains/FDS\_INTEGRATION.md`

---

# 1. Purpose

Integration Domain เป็นศูนย์กลางสำหรับการเชื่อมต่อระบบภายนอกและระบบภายในของ SMEsPlus

รองรับแนวคิด API First และ Event Driven Architecture เพื่อให้ทุก Module สามารถเชื่อมต่อกันได้โดยไม่เกิดการผูกติด (Loose Coupling)

---

# 2. Scope

## In Scope

- API Client

- API Key

- Webhook

- Event Publishing

- Event Subscription

- Callback Endpoint

- Integration Log

- Retry Mechanism

## Out of Scope

- ESB

- Message Broker Cluster

- ETL Platform

- Enterprise iPaaS

---

# 3. Actors

| Actor | Description |

|--------|-------------|

| Platform Admin | จัดการ Integration |

| Tenant Owner | จัดการ API ขององค์กร |

| External System | ระบบภายนอก |

| Developer | ผู้พัฒนา Integration |

---

# 4. Functional Requirements

## FR-INT-001 Create API Client

Permission

integration.client.create

API

POST /api-clients

Acceptance Criteria

- Client ID Generated

- Client Secret Generated

- Secret Display Once

- Audit Recorded

---

## FR-INT-002 Regenerate Secret

Permission

integration.client.rotate

API

POST /api-clients/{id}/rotate-secret

Acceptance Criteria

- New Secret Generated

- Old Secret Revoked

- Audit Recorded

---

## FR-INT-003 Register Webhook

Permission

integration.webhook.create

API

POST /webhooks

Acceptance Criteria

- HTTPS Required

- Event Required

- Endpoint Validated

---

## FR-INT-004 Send Webhook

Acceptance Criteria

- Retry Supported

- Response Logged

- Failure Recorded

---

## FR-INT-005 View Integration Log

API

GET /integration/logs

Acceptance Criteria

- Filter Supported

- Pagination

- Export

---

## FR-INT-006 Disable API Client

Acceptance Criteria

- Client Disabled

- Token Revoked

- Audit Recorded

---

# 5. Business Rules

BR-INT-001

API Secret แสดงได้เพียงครั้งเดียว

BR-INT-002

Webhook ต้องเป็น HTTPS

BR-INT-003

ทุก Request ต้องผ่าน Authentication

BR-INT-004

Integration Log ต้องเก็บย้อนหลังได้

---

# 6. User Stories

US-INT-001

As Developer

I want API Client

So that I can connect my application.

---

US-INT-002

As Tenant Owner

I want Webhook

So that my system receives events automatically.

---

# 7. Screen Mapping

UX-INT-001 API Client

UX-INT-002 Webhook

UX-INT-003 Integration Log

---

# 8. API Mapping

POST /api-clients

POST /api-clients/{id}/rotate-secret

POST /webhooks

GET /integration/logs

---

# 9. Database Mapping

api\_clients

api\_keys

webhooks

integration\_logs

---

# 10. Security

OAuth2 Ready

JWT

HTTPS

API Key Rotation

Audit

---

# 11. Traceability

FR → SDS → API → DB → UX → QA

---

# 12. Status

Ready for

SDS

API

DB

SECURITY