# BUSINESS_CAPABILITY_MAP.md

**Document ID:** SMEPLUS-26-07-05-001-BCM
**Phase:** 2.5 – Knowledge Consolidation & Enterprise Analysis
**Prepared by:** Claude, acting as Business Architect / Enterprise Architect
**Date:** 2026-07-05

## Purpose
Classify every capability already evidenced in the repository into Core, Supporting, Shared, or Platform, so the Architecture Team has a single capability map to design against in Phase 3.

## Dependencies
`MODULE_DEPENDENCY_MATRIX.md` (this package), `01_SaaS_Foundation/FDS/Domains/*.md`, `02_Functional_Design/02_Functional_Design/iTEST02_module_inventory.csv`, `00_Architecture_Office/Reference_Architecture/SMEPLUS-BUSINESS-CAPABILITY-MODEL-v0.1.md`, `MODULE_EXPANSION_PLAN.md`.

## Source Evidence
Capability groupings below reconcile three separate sources that already exist in the repository: (a) the SaaS Foundation FDS domain set, (b) the real Odoo module-group breakdown from the dump analysis, and (c) `MODULE_EXPANSION_PLAN.md`'s explicit "Foundation Reuse Rule" list, which states every business module must reuse the same Shared Foundation capabilities rather than rebuilding them.

## Confidence Level
High for the Platform and Shared tiers (explicit FDS + explicit Foundation Reuse Rule). High for which Odoo module groups exist (schema-evidenced). Medium for Core vs. Supporting classification of business modules, since only Purchase has completed evidence matching — Sales, Accounting, Inventory, HR, and Manufacturing classification here is based on stated project priority and process centrality, not yet on their own Evidence Matching pass.

## Known Gaps
`Other_Unclassified` (293 tables, the largest single group in the dump) cannot be capability-classified yet — see `OPEN_SOURCE_TO_SMESPLUS_GAP.md`.

**Update 2026-07-05:** Accounting/Finance capability scope has been formally narrowed to Thailand-only localization per **ADR-0004** (`00_Architecture_Office/ADR/ADR-0004-ACCOUNTING-THAILAND-LOCALIZATION-SCOPE.md`), Boss-approved. Standard Odoo accounting functionality remains fully in scope; only the localization layer is restricted.

## Recommended Next Step
Confirm Core/Supporting split with Boss before Phase 3 sprint planning, since capability tier typically drives investment priority.

---

## 1. Platform Capabilities

*Definition: capabilities every tenant and every module depends on to exist at all; not a business function in themselves.*

| Capability | Evidence | Status |
|---|---|---|
| Tenant Management | `FDS_TENANT.md` | Draft FDS; GAP in schema (no table above Company yet) |
| Company / Branch / Division Management | `FDS_COMPANY.md`, `FDS_BRANCH.md`, `FDS_DIVISION.md` | Draft FDS; Company confirmed in schema (`res_company`), Branch/Division are custom GAPs |
| Identity & Access Management (IAM) | `FDS_IAM.md` | Draft FDS; base auth confirmed in Odoo core (`res_users`/`res_groups`) |
| Role & Permission | `FDS_ROLE.md`, `FDS_ROLE_PERMISSION.md`, `FDS_PERMISSION.md` | Draft FDS; base RBAC MATCHED (FR-FD-002) via `res_groups`/`ir_model_access`/`ir_rule` |
| Subscription & Module Activation | `FDS_SUBSCRIPTION.md`, `FDS_SUBSCRIPTION_MODULE.md`, `FDS_MODULE.md` | Draft FDS; confirmed GAP — zero subscription/entitlement tables exist (FR-FD-003) |
| Configuration Center | `FDS_CONFIGURATION.md` | Draft FDS; GAP (custom key-value store, no existing evidence); flagged NEW pending PMO confirmation |
| Integration Foundation | `FDS_INTEGRATION.md` | Draft FDS; GAP — no dedicated integration/webhook table found |
| Security Foundation | `MODULE_EXPANSION_PLAN.md` ("Foundation Reuse Rule" — Security listed as shared) | Referenced but not yet detailed as its own FDS domain |

## 2. Shared Capabilities

*Definition: cross-cutting services consumed by every business module, reusable rather than rebuilt per module (explicit design intent per `FDS_APPROVAL.md` and `MODULE_EXPANSION_PLAN.md`).*

| Capability | Evidence | Status |
|---|---|---|
| Approval Workflow (reusable engine) | `FDS_APPROVAL.md` | Draft FDS; explicitly designed to be reusable across all modules without a new workflow per module; partially GAP (engine itself not yet built) |
| Notification | `FDS_NOTIFICATION.md` | Draft FDS; belongs to User, cannot cross Tenant, archived items retained |
| Audit & Governance | `FDS_AUDIT.md` | Draft FDS; every module must send events to a central Audit Service; partial GAP (dedicated cross-module table not confirmed, though Odoo's native `mail.message`/tracking gives partial coverage) |
| Reporting (Operator + Tenant tiers) | `FDS_REPORTING.md` | Draft FDS; two distinct reporting surfaces — Platform Operator health dashboard (operational metrics only, must never show tenant business data, BR-REP-001) vs. tenant-scoped business reporting |
| Attachment / Evidence Retention | `CANONICAL_DATA_MODEL.md` §8, BR-PUR-101 | Confirmed via Odoo's generic `ir_attachment` mechanism, referenced across many modules |

## 3. Core Capabilities

*Definition: capabilities that directly execute SME's primary revenue and cost transactions — the reason the platform exists. Classification below follows the project's Priority-1/Priority-2 focus (SaaS Foundation, Accounting, Purchase, Inventory = Priority 1; Sales, CRM, Product = Priority 2) together with process centrality confirmed by the schema.*

| Capability | Evidence | Status | Notes |
|---|---|---|---|
| Procure-to-Pay (Purchase) | `17_Functional_Specification_Factory/02_Purchase/*`, `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` | Actively in Functional Design; fully evidence-matched | Only module with a complete end-to-end Evidence Matching pass; RFQ/Vendor Comparison/Vendor Selection are the confirmed real build gaps |
| Inventory / Stock Management | `iTEST02_ERD_Inventory_Purchase.md` | Schema-evidenced (169 tables); FDS not yet authored as standalone module | Goods Receipt (MATCHED base) already covered under Purchase's evidence-matching pass |
| Accounting / Finance | `iTEST02_ERD_Accounting_Finance.md` | Schema-evidenced (178 tables); Vendor Bill / 3-way match MATCHED (FR-ACC-001) | Largest table count among business modules. **Scope note (ADR-0004, 2026-07-05, Boss-approved): standard Odoo accounting functions retained in full; localization restricted to Thailand only (`l10n_th`, `l10n_th_reports`) — the other 521 country-localization modules present in the source (523 `l10n_*` modules total) are OUT OF SCOPE.** |
| Order-to-Cash (Sales) | `iTEST02_ERD_Sales_CRM.md` | Schema-evidenced (60 tables, shared with CRM); FDS not yet authored | Priority-2 per project sequencing |
| CRM (Lead/Opportunity Management) | `iTEST02_ERD_Sales_CRM.md` | Schema-evidenced (shared 60-table group with Sales); FDS not yet authored | Priority-2 |

## 4. Supporting Capabilities

*Definition: capabilities that are valuable but not the primary transaction engine — they extend or enrich core capabilities. Classification follows Priority-3/Priority-4 sequencing.*

| Capability | Evidence | Status |
|---|---|---|
| HR & Payroll | `iTEST02_ERD_HR_Payroll.md` (179 tables) | Schema-evidenced; Priority-3; FDS not yet authored |
| Manufacturing & Maintenance | `iTEST02_module_inventory.csv` (109 tables) | Schema-evidenced; Priority-3; FDS not yet authored |
| Project / Service (Helpdesk) | `iTEST02_module_inventory.csv` (120 tables) | Schema-evidenced; Priority-4; FDS not yet authored |
| Website / eCommerce | `iTEST02_module_inventory.csv` (55 tables) | Schema-evidenced; Priority-4; FDS not yet authored |
| AI & Knowledge (chatbot, embeddings, digest) | `iTEST02_module_inventory.csv` (22 tables) | Schema-evidenced; smallest group; Priority-4 |

## 5. Unclassified (Requires Follow-Up Before Phase 3)

| Group | Evidence | Issue |
|---|---|---|
| Other_Unclassified | `iTEST02_module_inventory.csv` (293 tables — the single largest group in the entire schema) | No capability tier can be assigned yet; sample tables span asset management, applicant workflows, approval infrastructure, and more, suggesting this group actually contains fragments of several capabilities above rather than one coherent new capability |
| Odoo_Core_Technical | `iTEST02_module_inventory.csv` (210 tables, 2,893 incoming FK — highest in the entire schema) | Not a business capability at all — this is technical infrastructure (auth, automation, barcode, import/export) that underlies every tier above; listed here for completeness, not for capability planning |

---

## Capability Tier Diagram (Text Form)

```
┌───────────────────────────── Core (revenue/cost engine) ─────────────────────────────┐
│  Procure-to-Pay (Purchase)  │  Inventory  │  Accounting  │  Order-to-Cash (Sales)  │ CRM │
└────────────────────────────────────────────────────────────────────────────────────────┘
                              ▲ consumed by / feeds into ▲
┌──────────────────────────── Supporting (extends core) ───────────────────────────────┐
│   HR & Payroll   │   Manufacturing & Maintenance   │  Project/Service  │  Website/eCommerce  │  AI & Knowledge  │
└────────────────────────────────────────────────────────────────────────────────────────┘
                              ▲ all of the above call down into ▲
┌────────────────────────────── Shared (cross-cutting services) ───────────────────────┐
│   Approval   │   Notification   │   Audit & Governance   │   Reporting   │   Attachment   │
└────────────────────────────────────────────────────────────────────────────────────────┘
                              ▲ all of the above run on top of ▲
┌────────────────────────────── Platform (existence layer) ────────────────────────────┐
│  Tenant  │  Company/Branch/Division  │  IAM  │  Role/Permission  │  Subscription/Module  │  Configuration  │  Integration  │  Security  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
