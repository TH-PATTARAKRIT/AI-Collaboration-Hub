# BUSINESS_RULE_CATALOG.md

**Document ID:** SMEPLUS-26-07-05-001-BRC
**Phase:** 2.5 – Knowledge Consolidation & Enterprise Analysis
**Prepared by:** Claude, acting as Business Architect / Knowledge Engineer
**Date:** 2026-07-05

## Purpose
Extract business concepts only (no source code) for every Business Rule already documented in the repository, organized by category (Validation, Posting, Approval, Accounting, Workflow), each traced to its Functional Requirement and evidence path.

## Dependencies
`01_SaaS_Foundation/FDS/Domains/*.md`, `17_Functional_Specification_Factory/02_Purchase/Purchase Module Business Rules v0.1.pdf`, `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md`.

## Source Evidence / Confidence Level
SaaS Foundation rules: Medium confidence (Draft status, not yet Boss-approved, but internally consistent). Purchase module rules: High confidence (each rule is pre-mapped to an FR ID and the module has undergone Evidence Matching against real source code and the DB dump).

## Known Gaps
Rule text for domains beyond Purchase (e.g. Accounting, Sales, Inventory as standalone modules) has not yet been authored anywhere in the repository — only the SaaS Foundation (platform-layer) rules and the Purchase module rules exist today. This is expected: SaaS Foundation and Purchase are the current Priority-1 focus.

## Recommended Next Step
As each subsequent module (Sales, Inventory proper, Accounting proper, HR) enters its Functional Specification Factory pass, its Business Rules should be appended to this catalog using the same Rule ID / Related FR / Category / Evidence Path structure.

## ⚠️ Clean Room Framing Notice (2026-07-06, per ADR-0006)

All "Evidence Path" citations to Odoo or OCA source files throughout this document (§A–§H) are
**concept origins** — where a business rule was observed and confirmed against real-world usage —
not implementation to be installed or copied. SMEsPlus's own implementation of every rule below is
independent design and build work in its own FastAPI/Next.js/SQLAlchemy stack
(`TECHNOLOGY_STACK_STANDARD.md`), still to be done in Phase 3/4. §H (Thai Withholding Tax) has been
explicitly reworded to concept-first language; §A–§G were already stated as business rules rather
than implementation descriptions and did not require rewording, but are covered by this notice for
clarity.

---

## A. Workflow Rules — SaaS Foundation (Platform Layer)

| Rule ID | Rule | Domain | Related FD/FR | Evidence Path |
|---|---|---|---|---|
| BR-TEN-001 | A user belongs to exactly one tenant; cross-tenant accounts are not permitted in v1 | Tenant | FD-001/002 | `FDS/Domains/FDS_TENANT.md` |
| BR-TEN-002 | Suspended tenants retain read/export access but lose write access until reinstated | Tenant | FD-029 | `FDS/Domains/FDS_TENANT.md` |
| BR-TEN-003 | Terminated tenants' data is retained per data-retention policy before permanent deletion (duration pending Legal/Compliance input) | Tenant | FD-030 | `FDS/Domains/FDS_TENANT.md` |
| BR-BRN-001 | A branch belongs to exactly one company | Branch | FD-004 | `FDS/Domains/FDS_BRANCH.md` |
| BR-BRN-002 | A user's default branch scoping determines their default record visibility | Branch | — | `FDS/Domains/FDS_BRANCH.md` |
| BR-DIV-001 | A division belongs to exactly one branch | Division | — | `FDS/Domains/FDS_DIVISION.md` |
| BR-DIV-002 | Division is optional; a branch may operate with zero divisions (simple case must not require division setup) | Division | — | `FDS/Domains/FDS_DIVISION.md` |
| BR-MOD-001 | A module cannot be enabled if its declared dependencies are not also enabled | Module | — | `FDS/Domains/FDS_MODULE.md` |
| BR-MOD-002 | Disabling a module hides its UI/menu but does not delete its data (supports re-enable) | Module | — | `FDS/Domains/FDS_MODULE.md` |
| BR-SUB-001 | A tenant has exactly one active Subscription Plan at a time | Subscription | FD-017 | `FDS/Domains/FDS_SUBSCRIPTION.md` |
| BR-SUB-002 | Downgrading a plan that disables a module already in use requires explicit confirmation and does not delete existing data for that module | Subscription | — | `FDS/Domains/FDS_SUBSCRIPTION.md` |
| BR-SM-001 | Plan code must be unique | Subscription/Module | — | `FDS/Domains/FDS_SUBSCRIPTION_MODULE.md` |
| BR-SM-002 | Module code must be unique | Subscription/Module | — | `FDS/Domains/FDS_SUBSCRIPTION_MODULE.md` |
| BR-SM-003 | Tenant can activate only modules included in its active plan | Subscription/Module | — | `FDS/Domains/FDS_SUBSCRIPTION_MODULE.md` |
| BR-SM-004 | Module dependency must be satisfied before activation | Subscription/Module | — | `FDS/Domains/FDS_SUBSCRIPTION_MODULE.md` |
| BR-SM-005 | A required module cannot be deactivated if used by an active dependent module | Subscription/Module | — | `FDS/Domains/FDS_SUBSCRIPTION_MODULE.md` |
| BR-SM-006 | Subscription history must be preserved | Subscription/Module | — | `FDS/Domains/FDS_SUBSCRIPTION_MODULE.md` |
| BR-SM-008 | A suspended tenant cannot activate modules | Subscription/Module | — | `FDS/Domains/FDS_SUBSCRIPTION_MODULE.md` |
| BR-NTF-001 | A notification belongs to a User | Notification | — | `FDS/Domains/FDS_NOTIFICATION.md` |
| BR-NTF-002 | A notification cannot cross a Tenant boundary | Notification | — | `FDS/Domains/FDS_NOTIFICATION.md` |
| BR-NTF-003 | An archived notification is still retained (not deleted) | Notification | — | `FDS/Domains/FDS_NOTIFICATION.md` |

## B. Approval Rules — SaaS Foundation

| Rule ID | Rule | Domain | Related FD/FR | Evidence Path |
|---|---|---|---|---|
| BR-ROL-001 | Role permission changes take effect immediately for new sessions; existing sessions may require re-authentication (exact behavior pending Architecture confirmation) | Role | — | `FDS/Domains/FDS_ROLE.md` |
| BR-ROL-002 | A user may be assigned more than one role; effective permissions are the union of all assigned roles | Role | — | `FDS/Domains/FDS_ROLE.md` |
| BR-RP-001 | Role name must be unique within a tenant | Role/Permission | — | `FDS/Domains/FDS_ROLE_PERMISSION.md` |
| BR-RP-002 | System roles cannot be deleted | Role/Permission | — | `FDS/Domains/FDS_ROLE_PERMISSION.md` |
| BR-RP-003 | Permission must be enforced by the backend (not the UI alone) | Role/Permission | — | `FDS/Domains/FDS_ROLE_PERMISSION.md` |
| BR-RP-004 | Frontend permission controls visibility only, not security | Role/Permission | — | `FDS/Domains/FDS_ROLE_PERMISSION.md` |
| BR-RP-005 | Every permission change must be audited | Role/Permission | — | `FDS/Domains/FDS_ROLE_PERMISSION.md` |
| BR-RP-006 | A user cannot assign a permission higher than their own authority | Role/Permission | — | `FDS/Domains/FDS_ROLE_PERMISSION.md` |
| BR-PRM-001 | Record-level rules (branch/division scoping) are enforced at the data-access layer, not only in the UI | Permission | — | `FDS/Domains/FDS_PERMISSION.md` |
| BR-PRM-002 | Permission changes are additive within a role; removing a permission from a role removes it from all users holding only that role | Permission | — | `FDS/Domains/FDS_PERMISSION.md` |

## C. Accounting / Financial Rules — Purchase Module (Vendor Bill Matching)

Evidence: `17_Functional_Specification_Factory/02_Purchase/Purchase Module Business Rules v0.1.pdf` §10.

| Rule ID | Rule | Related FR | Evidence Path |
|---|---|---|---|
| BR-PUR-080 | A Vendor Bill must reference a Purchase Order | FR-PUR-087 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-081 | System supports 2-Way Matching (PO ↔ Vendor Bill) | FR-PUR-089 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-082 | System supports 3-Way Matching (PO ↔ Goods Receipt ↔ Vendor Bill) | FR-PUR-090 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-083 | If a mismatch exceeds tolerance, a Matching Exception must be created | FR-PUR-093 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-084 | Only after matching passes may the bill be forwarded to Accounting | FR-PUR-095 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-041 | Prices must be normalized to a common currency before comparison | FR-PUR-045 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-042 | Net Price = Unit Price − Discount + Tax | FR-PUR-046 | Purchase Module Business Rules v0.1.pdf |

## D. Validation / Posting Rules — Purchase Module (Request → RFQ → PO)

| Rule ID | Rule | Related FR | Evidence Path |
|---|---|---|---|
| BR-PUR-001 | Purchase Request Number must be unique within a Company | FR-PUR-001 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-002 | Requester must be an Active user | FR-PUR-002 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-003 | Budget Reference must be an active/usable budget | FR-PUR-005 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-004 | A Draft Purchase Request can be edited | FR-PUR-007 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-005 | Once Submitted, a Purchase Request cannot be edited except via a Revision | FR-PUR-008 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-006 | A Purchase Request must pass the Approval Matrix | FR-PUR-009 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-020 | An RFQ can only be created from an Approved Purchase Request | FR-PUR-013 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-021 | An RFQ must reference at least one Purchase Request line | FR-PUR-016 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-022 | An RFQ must define a Response Deadline | FR-PUR-020 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-023 | One RFQ can invite multiple vendors | FR-PUR-021 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-030 | A Vendor Response must reference an RFQ | FR-PUR-028 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-032 | A submitted Vendor Response version cannot be edited | FR-PUR-032 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-034 | A Vendor Response must never be deleted | FR-PUR-034 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-050 | Vendor Selection must pass Approval | FR-PUR-054 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-051 | An Approved Vendor Response must be Locked | FR-PUR-057 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-053 | RFQ status changes to Awarded after Vendor Selection approval | FR-PUR-059 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-060 | A Purchase Order cannot be created without an Approved Vendor Selection | FR-PUR-060 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-062 | A PO exceeding its value threshold must pass Approval | FR-PUR-066 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-063 | Once Confirmed, key PO data cannot be edited except through Change Control | FR-PUR-067 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-070 | Goods Receipt must reference a Purchase Order | FR-PUR-071 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-071 | Partial Receipt is supported | FR-PUR-073 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-072 | Receiving more than ordered quantity requires approval | FR-PUR-074 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-073 | Inventory must be updated immediately after Receipt is confirmed | FR-PUR-079 | Purchase Module Business Rules v0.1.pdf |

## E. Approval Rules — Purchase Module

| Rule ID | Rule | Related FR | Evidence Path |
|---|---|---|---|
| BR-PUR-010 | Approver must be listed in the Approval Matrix | FR-PUR-010 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-011 | Approvers may not approve their own documents, where organizational policy requires it | FR-PUR-010 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-012 | Every comment must be recorded | FR-PUR-011 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-013 | Approval timeline entries cannot be retroactively edited | FR-PUR-012 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-040 | A Comparison Matrix must be built only from actual Vendor Responses | FR-PUR-043 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-043 | If the lowest-price vendor is not selected, a reason must be recorded | FR-PUR-051 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-044 | A manual override must record the approver and the reason | FR-PUR-052 | Purchase Module Business Rules v0.1.pdf |

## F. Security & Audit Rules — Purchase Module

| Rule ID | Rule | Related FR | Evidence Path |
|---|---|---|---|
| BR-PUR-090 | Access is controlled via Role-Based Access Control | FR-PUR-105 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-091 | An Auditor role has Read-only access | FR-PUR-111 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-092 | Data is segregated by Tenant, Company, and Branch | FR-PUR-117 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-100 | Every status change must generate an Audit Trail entry | FR-PUR-116 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-101 | Attachments and evidence must be retained | FR-PUR-112 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-102 | Comment threads cannot be retroactively deleted | FR-PUR-113 | Purchase Module Business Rules v0.1.pdf |
| BR-PUR-103 | Notifications must record their send history | FR-PUR-114 | Purchase Module Business Rules v0.1.pdf |
| BR-INT-001 | An API secret can be displayed only once, at creation | Integration | `FDS/Domains/FDS_INTEGRATION.md` |
| BR-INT-002 | Webhooks must use HTTPS | Integration | `FDS/Domains/FDS_INTEGRATION.md` |
| BR-INT-003 | Every request must pass Authentication | Integration | `FDS/Domains/FDS_INTEGRATION.md` |
| BR-INT-004 | Integration logs must be retained and retrievable historically | Integration | `FDS/Domains/FDS_INTEGRATION.md` |
| BR-CFG-001 | Company-level configuration overrides tenant-level default when both are set | Configuration | `FDS/Domains/FDS_CONFIGURATION.md` |
| BR-CFG-002 | Configuration is data-model-neutral — locale/format choice does not change stored data types | Configuration | `FDS/Domains/FDS_CONFIGURATION.md` |
| BR-REP-001 | The Platform Operator health dashboard must never surface tenant business data — operational metrics only | Reporting | `FDS/Domains/FDS_REPORTING.md` |
| BR-REP-002 | Audit export respects the same access scoping as the audit trail viewer | Reporting | `FDS/Domains/FDS_REPORTING.md` |

## G. Future Rule Classification (Per ADR / Architecture Office Note)

Per the Purchase Module Business Rules document's own closing note, every rule above is intended to be further classified in the next pass into: Validation Rule, Calculation Rule, Workflow Rule, Security Rule, Integration Rule, Compliance Rule — and cross-linked to API design, Database Constraints, and UAT. This reclassification has **not yet occurred** (GAP — see `OPEN_SOURCE_TO_SMESPLUS_GAP.md`).
Evidence: `Purchase Module Business Rules v0.1.pdf` §13, "Architecture Office Note."

---

## H. Thai Withholding Tax Certificate — Business Rules (Independent SMEsPlus Requirements; Concept Origin Noted Per ADR-0006)

**⚠️ Reclassified 2026-07-06 per ADR-0006 (Clean Room Policy A):** the rules below are stated as
independent SMEsPlus business requirements. The OCA `l10n_th_withholding_tax*` suite (`Archive.zip`,
provided by Boss 2026-07-05) is cited only as the **concept origin** — i.e. where the business
requirement was observed and confirmed against real usage — never as the source of the rule's
wording or as code to be installed. SMEsPlus's own FastAPI/SQLAlchemy implementation of these rules
is independent design work, not yet done (Phase 3/4). See `OPEN_SOURCE_TO_SMESPLUS_GAP.md` §1 and
§8, and `ADR-0004` Addendum 3.

| Rule ID | SMEsPlus Business Requirement | Concept Origin (reference only, not implementation) |
|---|---|---|
| BR-WHT-001 | A withholding-tax certificate line's tax amount must reconcile with base amount × tax percentage (within the tenant's currency precision); the system must reject any certificate line where these three values are inconsistent. | Concept observed in a reference Thai WHT implementation's line-validation logic |
| BR-WHT-002 | A withholding-tax certificate must follow a controlled lifecycle: Draft (editable) → Done (finalized, issued to the payee) → Cancelled. | Concept observed in a reference Thai WHT implementation's document state model |
| BR-WHT-003 | If a certificate is superseded by a corrected replacement, the original must be automatically cancelled and the system must record which certificate replaced it, for audit purposes. | Concept observed in a reference Thai WHT implementation's substitution/correction handling |
| BR-WHT-004 | A withholding-tax certificate must be creatable from the context of either a vendor bill/journal entry or a payment transaction — both are valid triggers for issuing a certificate to a payee. | Concept observed in a reference Thai WHT implementation's certificate-creation entry points |
| BR-WHT-005 | The system must determine the correct Thai Revenue Department income-tax form type (e.g. the individual vs. juristic-person WHT form categories) from the nature of the underlying transaction, rather than requiring the user to select it manually every time. | Concept observed in a reference Thai WHT implementation's form-type auto-detection logic |
| BR-WHT-006 | The printed/issued certificate must itemize the statutory deduction categories required on a Thai WHT certificate (pension/welfare fund, social security fund, provident fund), each shown explicitly even when zero. | Concept observed in a reference Thai WHT implementation's certificate print layout |
| BR-WHT-007 | SMEsPlus's WHT certificate feature must not depend on any Odoo Enterprise-licensed component; certificate/report output must be achievable entirely within SMEsPlus's own independent stack. | Business/licensing constraint reinforced by observing that even the reference implementation deliberately avoided its platform's Enterprise-only reporting dependency |

---



| Category | Rule Count Catalogued |
|---|---:|
| SaaS Foundation — Workflow | 20 |
| SaaS Foundation — Approval/Permission | 10 |
| Purchase — Validation/Posting | 22 |
| Purchase — Approval | 7 |
| Purchase — Accounting/Financial | 7 |
| Purchase/Foundation — Security & Audit | 12 |
| Thai Withholding Tax Certificate (source-verified 2026-07-05) | 7 |
| **Total rules catalogued in this pass** | **85** |

This is a subset of the full evidence base — the source PostgreSQL dump analysis independently identified **4,377 business methods** at the code level (`Business_Rule_Method_Inventory.csv`), of which only the Purchase and SaaS Foundation domains have been distilled into named, FR-traced business rules so far. The remaining modules (Accounting proper, Sales, Inventory, Manufacturing, HR/Payroll) are **GAP** for rule extraction until their own Functional Specification Factory passes occur.
