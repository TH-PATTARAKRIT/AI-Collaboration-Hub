# SMEPLUS Functional Design Matching Matrix v0.2 (Reconciled)

**Document ID**: SMEPLUS-FDMM-v0.2
**Supersedes**: SMEPLUS-FDMM-v0.1 (2026-07-02, Functional Specification AI + Enterprise Architect AI)
**Status**: Draft — Evidence Verified (this version fills v0.1's "🔍 PENDING" evidence with real source/DB findings)
**Reconciled by**: Claude (Lead Enterprise Solution Architect and Source Code Analyst role)
**Reconciliation date**: 2026-07-02
**Owner**: Functional Specification AI + Enterprise Architect AI (content ownership unchanged)
**Reviewers**: PMO AI, Database Design AI, QA UAT AI

---

## Why this version exists

v0.1 defined a strong FR/BR/Jira structure (FR-FD-001–004, FR-PUR-001–006, FR-INV-001, FR-ACC-001, mapped to ERPPLUS-91–102) but its **evidence columns were placeholders** ("🔍 PENDING", "Need: <ClassName>") — the technical verification against real source code and the database had not been done yet; the document explicitly asked "Claude" to do this next.

Independently, Claude ran three rounds of Evidence Matching (2026-07-02) directly against `01_ACCOUNT.zip`, `02_OTHER.zip` (Odoo source, extracted), and `iTEST02_2026-06-14_14-41-19.dump` (live PostgreSQL dump, read via embedded DDL since `pg_restore` could not open the v1.16-format dump). Those results are recorded in `07_Output_From_AI/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX.md` (business-process level) using different ID scheme (FD-001–030, PUR-001–030, from the separate `SMEPLUS Enterprise Functional Requirement Catalog v0.1.pdf`).

**This v0.2 merges the two**: it keeps v0.1's FR-ID/Jira structure (since ERPPLUS-91–102 tickets already reference it) and replaces the placeholder evidence with the verified findings. Where v0.1 assumed a generic microservice architecture (`TenantMiddleware`, `RFQService`, `ThreeWayMatchEngine` as named classes), this version corrects that to the actual system: **the live product is Odoo**, and the equivalent capability lives in Odoo ORM models, not custom-named services. This correction matters for anyone estimating story points from v0.1's "Need: XyzService" language — the SP estimates for anything marked MATCHED below should be revisited.

Cross-reference note: FR-ID below ↔ Claude's evidence ID:
- FR-FD-001 (Tenant Isolation) ↔ FD-005 (Multi-Company)
- FR-FD-002 (RBAC) ↔ FD-008/FD-009/FD-010
- FR-FD-003 (Subscription) ↔ FD-013–FD-016
- FR-FD-004 (Module Activation) ↔ FD-017/FD-018
- FR-PUR-001 (PR Creation) ↔ PUR-001–003
- FR-PUR-002 (RFQ) ↔ PUR-008–011
- FR-PUR-003 (Quote Tracking) ↔ PUR-012–016
- FR-PUR-004 (Comparison) ↔ PUR-017–018
- FR-PUR-005 (Vendor Selection & Approval) ↔ PUR-019–023 **and the OUT-OF-SCOPE level1/level2 approval extension — see note below**
- FR-PUR-006 (PO Generation) ↔ PUR-024–026
- FR-INV-001 (Goods Receipt) ↔ PUR-027–028
- FR-ACC-001 (Vendor Bill / 3-way match) ↔ PUR-029–030

---

## SaaS Foundation Requirements

### FR-FD-001: Tenant Management & Isolation
**v0.1 status**: PARTIAL (evidence PENDING)
**v0.2 verified evidence**:
- Database: `public.res_company` (native Odoo multi-company), `company_id` FK confirmed on `purchase_order` and other transactional tables. `ir_rule` provides record-level company isolation.
- Source: `base` module (`res_company.py`, `res_users.py`), standard Odoo core.
- **What's real vs. what v0.1 assumed**: There is no `TenantMiddleware`/`TenantContext` class and no dedicated `tenant_id` column — Odoo's isolation unit is `company_id`, not a "Tenant" wrapping multiple companies. A true multi-tenant layer (one Tenant → many Companies, as the SaaS product requires) **does not exist yet**.
**v0.2 status**: **PARTIAL** (mechanism exists at Company level; Tenant-grouping layer above it is a genuine gap)
**Revised Jira note for ERPPLUS-91**: Scope should be "design Tenant→Company grouping layer on top of existing `res_company`/`ir_rule`", not "verify TenantMiddleware" (no such class exists to verify).

### FR-FD-002: User Role & Permission Management (RBAC)
**v0.1 status**: PARTIAL (evidence PENDING)
**v0.2 verified evidence**:
- Database/Source: `res_groups`, `res_users`, `ir_model_access` (model-level ACL), `ir_rule` (record-level ACL) — all confirmed, standard Odoo RBAC.
- **Correction**: No `role_hierarchy` table exists as such; Odoo's hierarchy is expressed via group implication (`res_groups` → `implied_ids`), not a separate table. "Super Admin > Tenant Admin > Module Owner > User" as named tiers is a SaaS-product concept layered on top of groups, not present today.
**v0.2 status**: **MATCHED** for the base RBAC mechanism; **PARTIAL** for the specific 4-tier hierarchy naming v0.1 specifies.
**Revised Jira note for ERPPLUS-92**: Reframe as "map the 4-tier SaaS role hierarchy onto Odoo `res_groups` implication chains", not "implement role_hierarchy table" (base RBAC needs no new implementation).

### FR-FD-003: Subscription Package Management
**v0.1 status**: GAP — confirmed correct.
**v0.2 verified evidence**: Explicit search of the 1,395-table schema found **zero** `subscription_*`, `saas_*`, `tenant_*`, or `feature_flag*` tables. `sale_subscription` exists but is a customer-facing recurring-billing app (for SMEsPlus's own customers to bill), not an internal tenant-entitlement system — do not conflate the two when scoping ERPPLUS-93.
**v0.2 status**: **GAP, confirmed** (matches Claude's independent FD-013–FD-016 GAP finding). No change to priority/SP estimate needed — v0.1 was already correct here.

### FR-FD-004: Module Activation & Licensing
**v0.1 status**: PARTIAL (evidence PENDING)
**v0.2 verified evidence**:
- Source: Odoo's own module system (`ir_module_module`, manifest `depends` list) provides install/uninstall and automatic dependency resolution — confirmed.
- **Correction**: No `ModuleRegistry`/`tenant_modules`/`module_status` tables exist for **subscription-gated** activation. Odoo's module toggle is global-per-database, not per-tenant-within-a-shared-database.
**v0.2 status**: **PARTIAL** — base module toggle mechanism MATCHED; subscription-gating layer is GAP (depends on FR-FD-003 landing first).
**Revised Jira note for ERPPLUS-94**: Scope is "gate Odoo's existing module install/uninstall behind the (not-yet-built) subscription entitlement check", not "create ModuleRegistry from scratch".

---

## Purchase Module Requirements

### FR-PUR-001: Purchase Request Creation
**v0.1 status**: PARTIAL, noted `purchase_order` table with columns `pr_number, status, created_date, amount_total` (evidence PENDING/assumed).
**v0.2 verified evidence**: **Correction** — v0.1's evidence row conflated PR with PO. The real objects are separate:
- `public.purchase_order` — standard Odoo PO/RFQ object (`state`, no `pr_number` column — that column does not exist in the real schema).
- `public.purchase_request` — a **separate table**, confirmed via dump to be the standard **OCA `purchase_request`** community module (fields: `requested_by`, `picking_type_id`, `estimated_cost`, `is_name_editable`, `urgency_level`, `revise_count`, `origin`, `reason` — all with genuine descriptive column comments, i.e. professionally authored, not Studio-generated). This module's source is not present in the two zips provided to Claude, meaning it needs to be pulled from wherever it was installed from (likely the `efaplus` implementation-partner relationship — see Purchase evidence matrix Round 2), not written from scratch.
- `public.purchase_requisition` (and 4 related tables) — also confirmed present in both source and DB; this is the RFQ/PO-alternatives aggregation object, separate again from `purchase_request`.
**v0.2 status**: **MATCHED** (the base capability exists as a known open-source module; action is "source the module", not "build PurchaseRequestService")
**Revised Jira note for ERPPLUS-95**: Should be re-scoped from "Create PurchaseRequestService" (net-new build, 21 SP) to "source/install missing OCA `purchase_request` module + confirm field mapping against SMEsPlus PR business rules" — likely far less than 21 SP once the module is in hand.

### FR-PUR-002: RFQ (Request for Quotation) Management — multi-vendor tendering
**v0.1 status**: GAP — confirmed correct, and this is the most consequential finding in the whole matrix.
**v0.2 verified evidence**: Standard Odoo `purchase_order` in draft state functions as a single-vendor RFQ (one PO record = one vendor). No `rfq_header`/`rfq_line`/`rfq_vendor`/`rfq_response` tables of any kind exist in the schema. Multi-vendor tendering (inviting several vendors under one RFQ event and tracking responses) genuinely does not exist — confirms v0.1's GAP classification and its CRITICAL/55-SP estimate is a reasonable order of magnitude.
**v0.2 status**: **GAP, confirmed, no change.**

### FR-PUR-003: Vendor Response & Quote Tracking
**v0.1 status**: NEW — confirmed correct. No `quote_responses` table found in schema; confirms GAP.
**v0.2 status**: **GAP (labelled NEW in v0.1), confirmed, no change.** Depends on FR-PUR-002 landing first (same dependency v0.1 already noted).

### FR-PUR-004: Vendor Comparison & Analysis
**v0.1 status**: NEW — confirmed correct. No comparison/scoring table found.
**v0.2 status**: **GAP (labelled NEW in v0.1), confirmed, no change.**

### FR-PUR-005: Vendor Selection & Approval
**v0.1 status**: PARTIAL, noted generic `approval_workflows` table (evidence PENDING for vendor-specific mapping).
**v0.2 verified evidence — two things layered together, must be separated:**
1. **Vendor Selection object itself** (buyer picks a winning vendor among several RFQ responses, with mandatory justification if not lowest price, then routes for approval): **GAP** — no such object exists; standard Odoo just lets a buyer manually confirm one RFQ into a PO with no formal "selection" or "justification" step.
2. **A live, in-production two-level (`level1`/`level2`) approval extension on `purchase_order` and `purchase_request`** (custom fields `level1_user_id`, `level2_user_id`, `x_review_result`, `reject_reason`, etc., plus dedicated `purchase_order_level_reject`/`purchase_request_level_reject` tables) — this genuinely exists in the live database. **Boss confirmed 2026-07-02 this is a custom add-on module developed outside SMEsPlus scope and excluded it from the Functional Requirement Catalog matching effort.** ERPPLUS-99 should **not** be scoped against these fields — they are out of scope, not a gap to close.
**v0.2 status**: **GAP** for the in-scope Vendor Selection capability (item 1). Item 2 is **OUT OF SCOPE**, not tracked here.
**Revised Jira note for ERPPLUS-99**: Re-scope to "design Vendor Selection object (winner pick + justification + approval) from scratch" — do not reference or attempt to reuse the excluded `level1/level2` fields.

### FR-PUR-006: Purchase Order Generation from RFQ
**v0.1 status**: PARTIAL, noted `purchase_order` table (evidence PENDING for `POGenerationService`).
**v0.2 verified evidence**: Standard Odoo RFQ→PO confirmation (`button_confirm` on `purchase.order`) is the real mechanism — confirmed present and functioning; no separate `POGenerationService` class exists because none is needed, this is native Odoo behavior. **However**, this confirmation is **not currently gated** by any Vendor Selection approval step (since that object doesn't exist — see FR-PUR-005), so a PO can be confirmed today without the formal selection/approval SMEsPlus wants.
**v0.2 status**: **MATCHED** for the base RFQ→PO mechanism; **GAP** for the "PO cannot be created without an approved Vendor Selection" business rule.
**Revised Jira note for ERPPLUS-100**: Base PO generation needs no new service (remove/reduce SP). Real remaining work is the *gate*: block `button_confirm` until Vendor Selection (FR-PUR-005) is approved — much smaller scope than "auto-generate PO from scratch".

---

## Inventory Module Requirements

### FR-INV-001: Goods Receipt & Stock Update
**v0.1 status**: PARTIAL, noted `stock_picking`/`stock_movement` tables (evidence PENDING for `GoodsReceiptService`).
**v0.2 verified evidence**: Confirmed via Module Architecture doc and DB: receiving flow (`Receipt, Putaway, Picking`) and PO Lifecycle (`Goods Receipt → Inventory updated`) are native Odoo `stock` module behavior. Partial-quantity receipt is standard `stock.move` behavior. No separate `GoodsReceiptService` class exists or is needed.
**v0.2 status**: **MATCHED** at process level (native Odoo). **Note**: the specific rule "forbid over-receipt beyond PO qty unless approved" (tolerance/exception control) is **not confirmed** — likely GAP, needs field-level verification.
**Revised Jira note for ERPPLUS-101**: Reduce scope from "create GoodsReceiptService" to "add over-receipt tolerance/exception rule on top of existing native receiving flow" — much smaller than a from-scratch service.

---

## Accounting Module Requirements

### FR-ACC-001: Vendor Bill Processing (3-Way Match)
**v0.1 status**: PARTIAL, noted `account_move` table (evidence PENDING for `ThreeWayMatchEngine`).
**v0.2 verified evidence**: **Explicitly confirmed twice** in the Learning Analysis package: "3-way Matching: Matching PO, Receipt, and Invoice" (Module Architecture doc) and "Matching → 3-way match (PO ↔ Receipt ↔ Invoice)" (Data Model doc, Invoice Lifecycle section). This is native Odoo `account` module functionality — no separate `ThreeWayMatchEngine` class exists because none is needed.
**v0.2 status**: **MATCHED.** This is the strongest, most confidently-verified item in the whole matrix.
**Revised Jira note for ERPPLUS-102**: Reduce scope significantly — remove "Implement ThreeWayMatchEngine" subtask entirely (already exists and works). Remaining real work, if any, is the **tolerance/exception threshold** when a bill amount exceeds a configurable variance from the matched PO/Receipt (not confirmed either way — needs field-level check, not a full engine build).

---

## Revised Gap Summary (v0.2)

| FR ID | v0.1 status | v0.2 status | Direction of change |
|---|---|---|---|
| FR-FD-001 | PARTIAL | PARTIAL | Same tier, but real blocker identified (Tenant≠Company) |
| FR-FD-002 | PARTIAL | MATCHED (base) / PARTIAL (SaaS tiering) | **Improved** — base RBAC needs no new build |
| FR-FD-003 | GAP | GAP | Confirmed, unchanged |
| FR-FD-004 | PARTIAL | PARTIAL | Same tier, scope corrected (gate, not build) |
| FR-PUR-001 | PARTIAL | MATCHED | **Improved** — module exists, needs sourcing not building |
| FR-PUR-002 | GAP | GAP | Confirmed, unchanged (still the biggest real gap) |
| FR-PUR-003 | NEW | GAP (=NEW) | Confirmed, unchanged |
| FR-PUR-004 | NEW | GAP (=NEW) | Confirmed, unchanged |
| FR-PUR-005 | PARTIAL | GAP (in-scope part) / OUT OF SCOPE (excluded part) | Clarified — Boss removed the level1/2 approval fields from scope entirely |
| FR-PUR-006 | PARTIAL | MATCHED (base) / GAP (approval gate) | **Improved** — base mechanism needs no new build |
| FR-INV-001 | PARTIAL | MATCHED (base) / GAP (tolerance rule) | **Improved** — base mechanism needs no new build |
| FR-ACC-001 | PARTIAL | MATCHED | **Improved** — fully working already, biggest SP-estimate reduction |

**Net effect on the 289 SP / 9–10 week estimate in v0.1**: Five of twelve items (FR-FD-002, FR-PUR-001, FR-PUR-006, FR-INV-001, FR-ACC-001) turn out to need far less work than a from-scratch service build, because the underlying Odoo mechanism already exists and works. The two genuinely hard items (FR-PUR-002 RFQ tendering, and the now-clarified FR-PUR-005 Vendor Selection) remain the real critical path. **Recommend**: Enterprise Architect AI / PMO AI re-estimate story points for ERPPLUS-92, 95, 100, 101, 102 downward before sprint planning; ERPPLUS-96 (RFQ, 55 SP) and the re-scoped ERPPLUS-99 (Vendor Selection) remain the priority build items.

---

## Evidence chain disclosure (per ADR-0002)

Evidence for this reconciliation came from: `01_ACCOUNT.zip`, `02_OTHER.zip` (Odoo source, partially extracted: base, purchase, purchase_stock, purchase_requisition, approvals, approvals_purchase, l10n_th, product, stock, mail), and `iTEST02_2026-06-14_14-41-19.dump` read via `strings`/`grep` against embedded `CREATE TABLE`/`COMMENT ON COLUMN`/`COPY` statements (full `pg_restore` was not possible — dump format v1.16 exceeds the v16.14 client available in this environment). This is primary evidence (direct read of source/DB), not a summary of someone else's documentation. Full detail and the underlying Round 1–3 findings: `07_Output_From_AI/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX.md`, `SMEPLUS-GAP-ANALYSIS.md`, `SMEPLUS-IMPLEMENTATION-ROADMAP.md`, `SMEPLUS-CLAUDE-IMPLEMENTATION-BACKLOG.md` (also mirrored to Google Drive `99_SMEsPlus_Enterprise_Suite/07_Output_From_AI/`).
