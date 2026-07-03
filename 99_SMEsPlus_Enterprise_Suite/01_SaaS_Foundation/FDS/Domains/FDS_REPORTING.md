# FDS — Reporting

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-REP
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines cross-domain Foundation-level reporting: user activity, approval cycle time, audit export,
and platform-operational health — distinct from module-specific business reports (financial
statements, inventory valuation, etc.), which are owned by their respective module FDS packages.

## 2. Scope
In Scope: tenant-level activity summary, approval cycle-time report, audit export, platform health
dashboard (Platform Operator only, no tenant business data).
Out of Scope: module-specific financial/operational reports.

## 3. Depends On / Consumed By
Depends On: Audit, Approval
Consumed By: Admin/Compliance UI, Platform Operator console

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| REP-001 | Platform shall provide a tenant-level user activity summary | New — not in FD-001..030 | GAP — NEW |
| REP-002 | Platform shall provide an approval-cycle-time report | New | GAP — NEW |
| REP-003 | Platform shall provide an audit export (CSV/PDF) | New | GAP — NEW |
| REP-004 | Platform Operator shall have a cross-tenant health dashboard, scoped to operational data only | New | GAP — NEW |

## 5. Business Rules
BR-REP-001: Platform Operator health dashboard must never surface tenant business data content —
operational metrics only (uptime, active tenant count, ticket volume).
BR-REP-002: Audit export respects the same access scoping as the audit trail viewer (see
FDS_AUDIT.md section 8).

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| ReportDefinition | id, report_type, scope | GAP — no existing evidence |

## 7. Process / State Flow
N/A — reporting is query/export driven, not lifecycle-driven.

## 8. Permission Notes
See FDS_AUDIT.md section 8 for audit-export access scoping; activity summary follows the same
role-based visibility as the underlying Audit domain.

## 9. Notification Events
None directly.

## 10. Audit Events
- report.exported (actor, report_type, timestamp) — exporting audit data is itself an audited action.

## 11. Acceptance Criteria
AC-REP-001: Given a Compliance user requests an audit export, when the export completes, then it
contains only records that user is authorized to view per their role scoping.

## 12. Open Items
- All four requirements in this domain are flagged NEW (not present in original FD-001–030 set) —
  requires PMO AI confirmation before addition to the Matching Matrix as tracked requirements.

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | No confirmed source — GAP / NEW |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
