# SOURCE_TO_BUSINESS_MAPPING.md

**Document ID:** SMEPLUS-26-07-05-001-STBM
**Phase:** 2.5 – Knowledge Consolidation & Enterprise Analysis
**Prepared by:** Claude, acting as ERP Domain Architect / Solution Designer
**Date:** 2026-07-05

## Purpose
Map Source Module (real Odoo module, as evidenced in the source-code and database analysis) → Business Process → Business Capability → Target SMEsPlus Module, so Phase 3 design work can trace every SMEsPlus module back to concrete source evidence.

## Dependencies
`V2.0/.../Evidence_CSV/Module_Inventory.csv`, `02_Functional_Design/02_Functional_Design/iTEST02_module_inventory.csv`, `BUSINESS_CAPABILITY_MAP.md` (this package), `17_Functional_Specification_Factory/02_Purchase/*`.

## Source Evidence
`Module_Inventory.csv` (1,436 module records with `category` column drawn from real Odoo app categories) cross-referenced with the module-group table counts in `iTEST02_module_inventory.csv`.

## Confidence Level
High for source module → Odoo category (direct CSV evidence). Medium for Business Process and Target SMEsPlus Module columns where FDS does not yet exist for that module (marked GAP in the Gap Analysis).

## Known Gaps
Only the Purchase (Procure-to-Pay) row has a fully-evidenced Business Process breakdown; all other rows show the process at category level only, pending each module's own Functional Specification Factory pass.

## Recommended Next Step
Use this mapping as the starting index for each subsequent module's Functional Specification Factory folder (`17_Functional_Specification_Factory/<NN>_<Module>/`), mirroring the structure already established for `01_SaaS_Foundation` and `02_Purchase`.

---

| Source Module (Odoo category, evidence) | Business Process | Business Capability | Target SMEsPlus Module |
|---|---|---|---|
| `Accounting/Accounting` (91 modules), `Accounting/Localizations/*` (232 modules), `Accounting/Payment Providers` (20 modules) | General Ledger, AR/AP posting, Tax/Withholding, Payment reconciliation | Accounting / Finance (Core) | Accounting/Finance module — **standard functions in scope; localization restricted to Thailand only (`l10n_th`, `l10n_th_reports`) per ADR-0004, 2026-07-05. The other 521 country-localization modules (of 523 total `l10n_*` modules evidenced) are explicitly OUT OF SCOPE.** |
| `account_3way_match` (Supply Chain/Purchase) | Vendor Bill 2-way/3-way matching | Procure-to-Pay (Core) — confirmed MATCHED (FR-ACC-001) | Purchase module (Vendor Bill Matching step) |
| Purchase-related zip content (`01_ACCOUNT.zip`) + OCA `purchase_request` | Purchase Request → RFQ → PO → Goods Receipt → Vendor Bill | Procure-to-Pay (Core) | Purchase module (fully evidenced, `17_Functional_Specification_Factory/02_Purchase/`) |
| `Supply Chain/Inventory` (27 direct modules; 169-table Inventory_Purchase group overall) | Stock move, warehouse/location management, reorder rules | Inventory / Stock Management (Core) | Inventory module |
| `Sales/Sales` (58 modules) | Quotation, sales order confirmation, delivery, invoicing | Order-to-Cash (Core) | Sales module |
| `Sales/Point of Sale` (54 modules) | In-person/retail sale transaction | Order-to-Cash (Core, retail variant) | Sales module (POS sub-capability) — **GAP: not yet scoped whether POS is in SMEsPlus v1** |
| CRM tables within `Sales_CRM` group (60 tables total) | Lead capture, opportunity tracking, lead-to-order conversion | CRM (Core) | CRM module |
| `Human Resources` (57 modules), `Human Resources/Payroll` (45 modules) | Employee master data, attendance, leave, payroll run, recruitment, appraisal | HR & Payroll (Supporting) | HR module |
| Manufacturing/Maintenance tables (`Manufacturing_Maintenance` group, 109 tables — incl. Fleet, Maintenance Equipment) | BOM, production/work orders, equipment maintenance, fleet management | Manufacturing & Maintenance (Supporting) | Manufacturing module |
| `Services/Helpdesk` (22 modules), `Services/Project` (21 modules) | Ticket management, project/task tracking, time logging, appointment booking | Project / Service (Supporting) | Project/Helpdesk module |
| `Website/Website` (46 modules) + eCommerce-related tables | Online storefront, live chat, online course delivery | Website / eCommerce (Supporting) | Website/eCommerce module |
| `Productivity/Dashboard` (27 modules) | KPI dashboard composition | Reporting (Shared) | Executive Dashboard / Reporting capability |
| `Marketing/Events` (24 modules) | Event registration, campaign tracking (UTM) | Marketing (not yet classified — likely Supporting) | **GAP — no target SMEsPlus module named yet** |
| AI_Knowledge group (22 tables: `ai_agent`, `ai_embedding`, `chatbot_*`, `digest_digest`) | Chatbot scripting, document embedding, digest email composition | AI & Knowledge (Supporting) | AI Integration capability (Claude/ChatGPT collaboration layer, per constitution) |
| `Odoo_Core_Technical` (210 tables: auth, automation, barcode, import/export) | Authentication, session, automation rule execution, data import/export | IAM / Platform (Platform) | SaaS Foundation — IAM domain |
| `Hidden`, `Hidden/Tests`, `Hidden/Tools` (144 modules combined) | Internal Odoo framework testing/tooling — not a business process | N/A (technical/internal) | Not applicable — excluded from business capability scope |
| `Other_Unclassified` (293 tables — largest group) | Unknown — spans asset management, applicant workflows, approval infra fragments per sample inspection | **GAP — cannot classify without further review** | **GAP — pending classification pass before assigning to any target module** |

---

## Reconciliation Note

This mapping intentionally does **not** use `16_Learning_Analysis/02_MODULE_ARCHITECTURE.md`'s 10-module list as a source, because that document's module boundaries (CRM, Sales, Purchase, Inventory, Manufacturing, Accounting, HR, Project/Helpdesk, Documents & Approval, Executive Dashboard) do not cite any Odoo category or table evidence and could not be reconciled against the real `Module_Inventory.csv` categories during this consolidation pass (see `KNOWLEDGE_CONSOLIDATION_REPORT.md` §4, GAP-KC-01). Where the two lists happen to agree (e.g., both name "HR," "Sales," "Purchase"), that is because these are common ERP capability names, not because `16_Learning_Analysis` was used as corroborating evidence.
