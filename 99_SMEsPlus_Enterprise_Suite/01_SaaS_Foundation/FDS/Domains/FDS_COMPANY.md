# FDS — Company

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-CMP
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Company: a legal entity within a Tenant. A Tenant may own multiple Companies (holding
structure); each Company has its own fiscal year, currency, and books.

## 2. Scope
In Scope: company profile, fiscal year/currency configuration, multi-company support within a tenant.
Out of Scope: Accounting-specific ledger configuration (see Accounting FDS package), Branch detail
(see FDS_BRANCH.md).

## 3. Depends On / Consumed By
Depends On: Tenant
Consumed By: Branch, Configuration, Accounting, Purchase, Inventory (via company_id scoping)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| CMP-001 | Platform shall support multiple companies per tenant | FD-003 | MATCHED (Odoo res.company) |
| CMP-002 | Platform shall support company-level currency and fiscal year configuration | FD-022 | See Matching Matrix |

## 5. Business Rules
BR-CMP-001: A company belongs to exactly one tenant.
BR-CMP-002: Fiscal year and currency are set at company creation and changed only through a
controlled process (not freely editable after transactions exist).

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| Company | id, tenant_id, name, currency, fiscal_year_start | Maps to Odoo res.company, extended with tenant_id |

## 7. Process / State Flow
Company Created -> Active -> (rare) Archived — company archival is out of scope for v1; not a
formal lifecycle requirement yet.

## 8. Permission Notes
Only Tenant Owner / Admin can create or edit Company records.

## 9. Notification Events
- company.created

## 10. Audit Events
- company.created, company.updated (fiscal_year/currency changes flagged as sensitive)

## 11. Acceptance Criteria
AC-CMP-001: Given a tenant creates a second company, when the user switches company context, then
only that company's data is shown.

## 12. Open Items
- Confirm whether company archival/deactivation is needed for v1 or deferred.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | Odoo res.company (standard, MATCHED) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
