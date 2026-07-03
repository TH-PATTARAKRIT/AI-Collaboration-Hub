# FDS — Audit

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-AUD
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Audit: the immutable change log covering every governed action across Foundation and
downstream modules. Directly supports Constitution Section 9 (Auditability) and ADR-0002 evidence
principles.

## 2. Scope
In Scope: audit log capture, audit trail viewer, audit export.
Out of Scope: module-specific compliance reporting (see FDS_REPORTING.md).

## 3. Depends On / Consumed By
Depends On: IAM
Consumed By: Reporting, QA UAT AI (evidence verification), Compliance

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| AUD-001 | Platform shall log all create/update/delete actions on governed models | FD-015 | PARTIAL |
| AUD-002 | Platform shall provide an audit trail viewer per record | FD-016 | PARTIAL |

## 5. Business Rules
BR-AUD-001: Every create/update/delete on a governed model produces an audit log entry with actor,
timestamp, and before/after values.
BR-AUD-002: Audit log entries are immutable — no update/delete through normal application paths.
BR-AUD-003: Approval decisions are captured as first-class audit events (see FDS_APPROVAL.md
section 10), not only as a status field change.

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| AuditLogEntry | id, actor_id, model, record_id, action, before, after, timestamp | Maps to Odoo mail.tracking pattern + custom extension |

## 7. Process / State Flow
N/A — append-only log, no lifecycle states.

## 8. Permission Notes
Admin, Compliance, and scoped Platform Operator can view audit trail; Branch Manager sees
branch-scoped audit entries only; Staff has no audit access.

## 9. Notification Events
None directly.

## 10. Audit Events
N/A (this domain is the audit mechanism itself)

## 11. Acceptance Criteria
AC-AUD-001: Given a governed record is updated, when the audit trail is viewed, then the change
shows actor, timestamp, and before/after values.

## 12. Open Items
- Confirm audit data retention duration aligned with tenant data retention policy (see
  FDS_TENANT.md BR-TEN-003) — pending Legal/Compliance confirmation.
- Confirm exact list of "governed models" requiring audit capture (currently PARTIAL evidence).

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | Odoo mail.tracking pattern (PARTIAL) + custom audit extension (GAP) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
