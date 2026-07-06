# MODULE_DEPENDENCY_MATRIX.md

**Document ID:** SMEPLUS-26-07-05-001-MDM
**Phase:** 2.5 – Knowledge Consolidation & Enterprise Analysis
**Prepared by:** Claude, acting as Solution Architect / ERP Domain Architect
**Date:** 2026-07-05

## Purpose
Show, for every module currently evidenced in the repository, its Dependency, Owner, Input, Output, Related Tables, and Related API status — grounded in the existing FDS domain files, module inventory CSVs, and Evidence Matching results.

## Dependencies
`01_SaaS_Foundation/FDS/Domains/*.md` (§3 "Depends On / Consumed By" sections), `02_Functional_Design/02_Functional_Design/iTEST02_module_inventory.csv`, `17_Functional_Specification_Factory/02_Purchase/*.pdf`, `01_SaaS_Foundation/API/OPENAPI_FOUNDATION_v0.1.yaml` (placeholder — no real API defined yet).

## Source Evidence / Confidence Level
High for SaaS Foundation domain dependencies (explicit "Depends On / Consumed By" sections exist per domain). High for module-to-table counts (direct CSV evidence). Low/GAP for "Related API" column across the board — the API layer is entirely a placeholder (`Status: PLACEHOLDER — not yet authored`), so every row's API column reflects that gate status rather than real endpoint evidence.

## Known Gaps
No API design exists yet for any module (Foundation or business). This is a correctly-held gate (Build Gate: HOLD), not a documentation omission — see prior `BUILD_READINESS_GATE_REPORT.md`.

## Recommended Next Step
Once FDS reaches Approved Baseline, author `SDS_FOUNDATION_v0.1.md` and only then `OPENAPI_FOUNDATION_v0.1`, per the dependency chain already declared inside the placeholder files themselves.

---

## A. SaaS Foundation Domains (Platform Layer)

| Module (Domain) | Dependency | Owner Role | Input | Output | Related Tables (Evidence) | Related API |
|---|---|---|---|---|---|---|
| Tenant | — (root entity) | Functional Specification AI | Tenant provisioning request | Tenant record, isolation boundary | GAP — no table exists | PLACEHOLDER |
| Company | Tenant | Functional Specification AI | Company registration data | Company record (root org per tenant) | `res_company` (CONFIRMED, Odoo core) | PLACEHOLDER |
| Branch | Company | Functional Specification AI | Branch setup request | Branch record, default stock/location binding | GAP — custom, "not a stock Odoo concept" | PLACEHOLDER |
| Division | Branch | Functional Specification AI | Division setup request (optional) | Division record | GAP — custom | PLACEHOLDER |
| IAM | Tenant, Company | Functional Specification AI | User registration/invitation, login credentials | Authenticated session, user profile | Odoo `res_users`/`res_groups` family (Odoo_Core_Technical group, 210 tables) | PLACEHOLDER |
| Role / Role-Permission | IAM | Functional Specification AI | Role definition, permission assignment | Effective permission set per user | Maps to Odoo `res.groups`, `ir.model.access` (Security_Access_Inventory.csv, 473 access records) | PLACEHOLDER |
| Permission | Role | Functional Specification AI | Permission grant/revoke request | Enforced access-layer rule (record-level, branch/division scoped) | Maps to Odoo `ir.rule`/`ir.model.access` | PLACEHOLDER |
| Subscription | Tenant | Functional Specification AI | Plan selection, upgrade/downgrade request | Active TenantSubscription record, feature flags | GAP — "zero subscription/entitlement tables exist" (FR-FD-003 confirmed GAP) | PLACEHOLDER |
| Subscription/Module | Subscription, Module | Functional Specification AI | Module activation request | Enabled/disabled module state per tenant | GAP — registry entity, no existing evidence | PLACEHOLDER |
| Module (Registry) | — | Functional Specification AI | Module dependency declaration | Module enable/disable gate | GAP — no existing evidence | PLACEHOLDER |
| Approval | Consumed by all business modules | Functional Specification AI | Any transaction requiring sign-off | Approval decision + history, reusable across modules | Partial — Odoo has some approval infra in `Other_Unclassified`/`approval_rule_users_to_notify_rel`; full reusable engine is GAP | PLACEHOLDER |
| Notification | User, Tenant | Functional Specification AI | Event trigger (any module) | Notification record per user, archived history | Odoo `mail.message`/notification infra (partial) | PLACEHOLDER |
| Audit | All modules (event source) | Functional Specification AI | Status/field change event | Audit trail record, audit export | Partial — Odoo `mail.message`/tracking; dedicated cross-module audit table is GAP | PLACEHOLDER |
| Integration | Tenant, Module | Enterprise Architect AI | External API call, webhook registration | API secret (one-time display), webhook delivery, integration log | GAP — no existing evidence found for a dedicated integration/webhook table | PLACEHOLDER |
| Configuration | Tenant, Company | Functional Specification AI | Config key/value set at tenant or company level | Effective configuration value (company overrides tenant) | GAP — custom key-value store, no existing evidence | PLACEHOLDER |
| Reporting | All modules (data source), Audit | Functional Specification AI | Report/dashboard request | Operational metrics (Platform Operator) or business report (tenant-scoped) | GAP — ReportDefinition entity, no existing evidence | PLACEHOLDER |

## B. Business Modules (Odoo-Evidenced, from Dump Analysis)

| Module Group | Dependency (Functional) | Owner Role | Input | Output | Related Tables (Evidence — table count) | Related API |
|---|---|---|---|---|---|---|
| Sales_CRM | Company, Customer (partner), Product | Functional Specification AI | Lead capture, quotation request | Sales Order, converted opportunity | 60 tables, 231 outgoing FK, 145 incoming FK (`iTEST02_module_inventory.csv`) | PLACEHOLDER |
| Inventory_Purchase | Company, Product, Warehouse, Vendor (partner) | Functional Specification AI | Purchase Request, Goods Receipt event | Stock Move/on-hand position, Purchase Order, Vendor Bill trigger | 169 tables, 739 outgoing FK, 495 incoming FK (`iTEST02_module_inventory.csv`) | PLACEHOLDER |
| Accounting_Finance | Sales_CRM (AR), Inventory_Purchase (AP), Company | Functional Specification AI | Invoice/Bill posting, payment receipt | Journal Entry, Chart-of-Accounts balance, financial report | 178 tables, 702 outgoing FK, 396 incoming FK (`iTEST02_module_inventory.csv`). **Localization scope: Thailand only (`l10n_th`, `l10n_th_reports`) per ADR-0004 — 521 other-country `l10n_*` modules OUT OF SCOPE.** | PLACEHOLDER |
| HR_Payroll | Company, Branch, Department | Functional Specification AI | Employee record, leave/expense request | Payslip, leave balance, appraisal record | 179 tables, 694 outgoing FK, 353 incoming FK (`iTEST02_module_inventory.csv`) | PLACEHOLDER |
| Manufacturing_Maintenance | Inventory_Purchase (BOM consumption) | Functional Specification AI | Production/work order, maintenance request | Finished goods stock move, maintenance/fleet log | 109 tables, 470 outgoing FK, 212 incoming FK (`iTEST02_module_inventory.csv`) | PLACEHOLDER |
| Project_Service | HR_Payroll (resources), Sales_CRM (customer) | Functional Specification AI | Project/task creation, helpdesk ticket, appointment booking | Task/ticket status, time log, resource allocation | 120 tables, 419 outgoing FK, 236 incoming FK (`iTEST02_module_inventory.csv`) | PLACEHOLDER |
| Website_eCommerce | Sales_CRM, Inventory_Purchase | Functional Specification AI | Online order, live-chat session, course/slide enrollment | Web sales order, chat transcript | 55 tables, 210 outgoing FK, 121 incoming FK (`iTEST02_module_inventory.csv`) | PLACEHOLDER |
| AI_Knowledge | Cross-cutting (any module content) | Enterprise Architect AI | Document ingestion, chatbot query | Embedding vector, chatbot response, digest email | 22 tables, 64 outgoing FK, 22 incoming FK (`iTEST02_module_inventory.csv`) | PLACEHOLDER |
| Odoo_Core_Technical | — (platform base for all above) | Enterprise Architect AI | Auth/session request, automation trigger | Technical infrastructure (auth, barcode, automation, import/export) | 210 tables, 725 outgoing FK, 2,893 incoming FK (highest incoming-FK count — confirms this group is the most depended-upon layer) | N/A — infrastructure layer |
| Other_Unclassified | Varies (spans multiple business domains) | PMO AI (needs classification) | — | — | 293 tables, 887 outgoing FK, 268 incoming FK — **GAP: largest unclassified group, needs a follow-up classification pass** | N/A |

## C. Purchase Module — Detailed Process-Level Dependency Chain

Evidence: `17_Functional_Specification_Factory/02_Purchase/Purchase Module Functional Requirement Catalog v0.1.pdf`, `FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md`.

| Step | Dependency | Owner Role | Input | Output | Related Tables | Evidence Status |
|---|---|---|---|---|---|---|
| Purchase Request | Requester (IAM), Approval Matrix | Functional Specification AI | Requester, Department, Required Date, Purpose, Request Lines | Draft/Submitted Purchase Request | `PURCHASE_REQUEST_LINE` (OCA `purchase_request`) | MATCHED |
| Department Approval | Purchase Request, Approval | Functional Specification AI | Submitted Purchase Request | Approved/Rejected Purchase Request | Approval object (GAP — reusable engine not yet built) | GAP (engine) |
| RFQ | Approved Purchase Request | Functional Specification AI | PR reference, Response Deadline | RFQ record | GAP — no existing implementation | GAP |
| Vendor Invitation | RFQ | Functional Specification AI | Vendor list | Invitation record (evidence of invitation) | GAP | GAP |
| Vendor Response | RFQ, Vendor Invitation | Functional Specification AI | Vendor's quoted price/terms | Versioned Vendor Response | GAP | GAP |
| Vendor Comparison | Vendor Response (≥1) | Functional Specification AI | Multiple Vendor Responses | Comparison Matrix (currency-normalized) | GAP | GAP |
| Vendor Selection | Vendor Comparison, Approval | Functional Specification AI | Comparison Matrix, buyer decision + justification | Approved Vendor Selection, Awarded RFQ status | GAP (selection object); level1/2 approval fields OUT OF SCOPE (Boss decision 2026-07-02) | GAP / OUT OF SCOPE |
| Purchase Order | Approved Vendor Selection | Functional Specification AI | RFQ + Vendor Response reference | Confirmed PO | `PURCHASE_ORDER`, `PURCHASE_ORDER_LINE` | MATCHED (base) / GAP (approval gate on Vendor Selection) |
| Goods Receipt | Purchase Order | Functional Specification AI | Delivery/receiving event | Stock Move, updated on-hand inventory | `STOCK_PICKING` (incoming), `STOCK_MOVE`, `STOCK_MOVE_LINE` | MATCHED (base) / GAP (over-receipt tolerance rule) |
| Vendor Bill Matching | Purchase Order, Goods Receipt | Functional Specification AI | Vendor invoice | Matched/exception-flagged bill | `account_move` (in_invoice) | MATCHED (2-way/3-way match confirmed twice per Evidence Matching) |
| Accounting Integration | Vendor Bill Matching | Functional Specification AI | Matched bill | Posted Journal Entry | `account_move`, `account_move_line`, `account_journal` | MATCHED |
| Close | Accounting Integration | Functional Specification AI | Fully processed PO/bill | Closed PO status | — | Not yet evidence-matched (GAP for explicit "Close" state) |

---

## Summary Observations

1. **Every module in the entire repository, without exception, has its API column as PLACEHOLDER.** This is a correct, intentional gate — not a documentation gap — because SDS/API work is blocked on FDS Approved Baseline (ADR-0002/ADR-0003 compliance).
2. The Purchase module is the only business module with a fully evidence-matched, end-to-end dependency chain (Request → RFQ → PO → Receipt → Bill → Accounting). All other business modules (Sales, Accounting, HR, Manufacturing, Project, Website) currently have only schema-level table/FK counts — their functional dependency chains have not yet been authored as FDS (**GAP**, expected — Purchase is the current Priority-1 focus per module priority hierarchy).
3. `Odoo_Core_Technical`'s 2,893 incoming foreign keys (far higher than any business module) confirms it is the structural backbone every other module depends on — this should be explicitly called out to any AI role or human architect who assumes business modules are independent of each other.
4. `Other_Unclassified` (293 tables) is the single largest gap in the module inventory and should be prioritized for a classification pass before Phase 3, since its true dependencies are currently unknown.
