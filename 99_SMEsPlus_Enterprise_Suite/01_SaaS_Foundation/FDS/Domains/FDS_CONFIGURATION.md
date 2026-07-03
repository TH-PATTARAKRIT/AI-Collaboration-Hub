# FDS — Configuration

Document ID: SMEPLUS-FDS-SAAS-FOUNDATION-CFG
Version: 1.0.0
Status: Draft
Owner Role: Functional Specification AI
Reviewers: PMO AI, Enterprise Architect AI
Approval: Boss

## 1. Purpose
Defines Configuration: tenant- and company-level configuration values (locale, date/number format,
default currency, notification preferences default, password policy default) that other domains
read but don't own.

## 2. Scope
In Scope: tenant/company configuration key-value store, configuration inheritance (tenant default ->
company override).
Out of Scope: module-specific settings (e.g. Accounting chart-of-accounts defaults — owned by
Accounting FDS).

## 3. Depends On / Consumed By
Depends On: Tenant, Company
Consumed By: IAM (password policy), Notification (default channel prefs), all modules (locale/format)

## 4. Functional Requirements
| ID | Requirement | Related FD-ID | Evidence Status |
|---|---|---|---|
| CFG-001 | Platform shall support tenant-level default configuration with company-level override | New — not in FD-001..030 | GAP — NEW |
| CFG-002 | Platform shall support Thai and English locale configuration (presentation layer) | Related to NFR-007 | MATCHED (Odoo i18n) |

## 5. Business Rules
BR-CFG-001: Company-level configuration overrides tenant-level default when both are set; if
company-level is unset, tenant-level default applies.
BR-CFG-002: Configuration is data-model-neutral — locale/format choice does not change underlying
stored data types (see 07_CONSTRAINTS equivalent: localization is presentation-layer only).

## 6. Data Entities (Conceptual)
| Entity | Key Attributes | Notes |
|---|---|---|
| TenantConfiguration | tenant_id, key, value | GAP — custom key-value store |
| CompanyConfiguration | company_id, key, value | Override layer |

## 7. Process / State Flow
N/A — configuration entity, no lifecycle states.

## 8. Permission Notes
Only Admin/Tenant Owner can change tenant-level defaults; Admin can set company-level overrides.

## 9. Notification Events
- configuration.changed (informational, low priority)

## 10. Audit Events
- configuration.changed (actor, key, old_value, new_value) — required for password-policy and
  security-relevant keys at minimum.

## 11. Acceptance Criteria
AC-CFG-001: Given a tenant sets a default password policy and one company overrides it, when a user
under that company logs in, then the company-level policy applies, not the tenant default.

## 12. Open Items
- CFG-001 flagged NEW — requires PMO AI confirmation before addition to the Matching Matrix.
- Confirm which specific keys need audit capture (BR relevant vs. purely cosmetic settings).

## 13. Evidence Record
| Field | Value |
|---|---|
| Owner | Functional Specification AI |
| Source | Odoo i18n (locale, MATCHED) + custom config store (GAP/NEW) |
| Timestamp | 2026-07-03 |
| Repository | TH-PATTARAKRIT/AI-Collaboration-Hub |
| Folder | 99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/FDS/Domains |
| Reviewer | Pending |
| Status | Draft |
