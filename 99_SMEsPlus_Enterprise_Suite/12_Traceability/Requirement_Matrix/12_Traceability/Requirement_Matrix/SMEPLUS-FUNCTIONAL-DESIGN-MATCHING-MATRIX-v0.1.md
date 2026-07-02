# SMEPLUS Functional Design Matching Matrix v0.1

**Document ID**: SMEPLUS-FDMM-v0.1  
**Status**: Draft for Claude + ChatGPT Review  
**Created**: 2026-07-02  
**Purpose**: Match Functional Specification with Source Code, Database, Module Architecture, Jira, Claude Task, and UAT Evidence  
**Owner**: Functional Specification AI + Enterprise Architect AI  
**Reviewers**: Claude Code AI, Database Design AI, QA UAT AI  

---

## 📋 Document Overview

This matrix provides **complete traceability** from Functional Requirement through to User Acceptance Testing, ensuring every requirement has:
- ✅ Business Rule definition
- ✅ Source code/ORM evidence
- ✅ Database/table mapping
- ✅ Screen/API specification
- ✅ Jira issue tracking
- ✅ Claude automation task
- ✅ UAT test case
- ✅ Gate approval status

---

## 🔄 Matching Rule (Complete Chain)

```
Functional Requirement (FR-*)
    ↓
Business Rule (BR-*)
    ↓
Business Process (BP-*)
    ↓
Module Responsibility
    ↓
Source Code Evidence (Class/ORM)
    ↓
Database Evidence (Table/Column)
    ↓
Screen/API Specification
    ↓
Jira Issue (ERPPLUS-*)
    ↓
Claude Automation Task
    ↓
UAT Test Case (UAT-*)
    ↓
Review Gate (Gate Result)
    ↓
Status: MATCHED ✅
```

---

## 📊 Matching Status Legend

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| **MATCHED** | ✅ All evidence found & verified | No action - ready for gate |
| **PARTIAL** | ⚠️ Some evidence found, gaps remain | Investigation & evidence collection |
| **GAP** | ❌ No evidence found | Design & implementation required |
| **NEW** | 🆕 New requirement not in current design | New design + development |
| **RETIRE** | 🗑️ Requirement obsolete/superseded | Remove from active tracking |
| **REVIEW** | 🔍 Needs expert review | Expert decision required |

---

## 🏢 SaaS Foundation Requirements

### **FR-FD-001: Tenant Management**

| Field | Value |
|-------|-------|
| **FR ID** | FR-FD-001 |
| **Function Name** | Tenant Management & Isolation |
| **Module** | SaaS Foundation |
| **BP ID** | N/A (Foundation) |
| **Business Rule** | BR-FD-TEN-001: Each tenant data must be isolated at database level |
| | BR-FD-TEN-002: Tenant context must be passed in every API call |
| | BR-FD-TEN-003: Tenant identification via subdomain or header |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | 🔍 PENDING | Need: TenantMiddleware, TenantContext, TenantIsolation class | 14_Claude_Execution/Task_Prompts/ |
| **Database** | 🔍 PENDING | Need: tenant_id in all tables, tenant isolation policies | 03_Data_Model_Overview.md (partial) |
| **Screen/API** | ⚠️ PARTIAL | API-FD-001: POST /api/tenants (create) | 01_System_OVERVIEW.md |
| | | SCR-FD-001: Tenant Management Dashboard | Design needed |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-91: Implement TenantMiddleware | |
| **Claude Task** | 🔍 PENDING | CTK-FD-001: Generate TenantContext with isolation | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-FD-001: Verify tenant A cannot see tenant B data | 08_Testing_Evidence/ |

**Status**: ⚠️ **PARTIAL**  
**Action**: 
1. Match TenantMiddleware to codebase (if exists)
2. Verify database tenant isolation policies
3. Create Jira ERPPLUS-91 for gaps

---

### **FR-FD-002: User Role & Permission Management**

| Field | Value |
|-------|-------|
| **FR ID** | FR-FD-002 |
| **Function Name** | User Role-Based Access Control (RBAC) |
| **Module** | SaaS Foundation |
| **BP ID** | N/A (Foundation) |
| **Business Rule** | BR-FD-IAM-001: Each user has role(s) in tenant context |
| | BR-FD-IAM-002: Permissions checked at API & screen level |
| | BR-FD-IAM-003: Role hierarchy: Super Admin > Tenant Admin > Module Owner > User |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | 🔍 PENDING | Need: RoleMiddleware, PermissionDecorator, RoleHierarchy | 14_Claude_Execution/Task_Prompts/ |
| **Database** | ⚠️ PARTIAL | Tables: users, roles, permissions, user_roles | 03_Data_Model_Overview.md |
| | | Need: role_hierarchy table |
| **Screen/API** | ⚠️ PARTIAL | API-FD-005: GET /api/users/{id}/permissions | 01_System_Overview.md |
| | | SCR-FD-003: User Permission Management | Design needed |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-92: Implement role hierarchy | |
| **Claude Task** | 🔍 PENDING | CTK-FD-002: Generate permission checking logic | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-FD-005: Verify User cannot access Admin screen | 08_Testing_Evidence/ |

**Status**: ⚠️ **PARTIAL**  
**Action**:
1. Verify role_hierarchy implementation
2. Validate permission decorator pattern
3. Create Jira ERPPLUS-92 for missing role hierarchy

---

### **FR-FD-003: Subscription Package Management**

| Field | Value |
|-------|-------|
| **FR ID** | FR-FD-003 |
| **Function Name** | Subscription Packages & Activation |
| **Module** | SaaS Foundation |
| **BP ID** | N/A (Foundation) |
| **Business Rule** | BR-FD-SUB-001: Each tenant has active subscription |
| | BR-FD-SUB-002: Features activated based on subscription tier |
| | BR-FD-SUB-003: Billing period tracked separately |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ❌ GAP | Need: SubscriptionService, FeatureFlag, BillingEngine | New |
| **Database** | ❌ GAP | Tables: subscriptions, subscription_tiers, feature_flags | Design needed |
| **Screen/API** | 🔍 PENDING | API-FD-007: POST /api/subscriptions/upgrade | Design needed |
| | | SCR-FD-004: Subscription Management Portal | Design needed |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-93: Design Subscription service | |
| **Claude Task** | 🔍 PENDING | CTK-FD-003: Generate subscription logic | |
| **UAT Test Case** | 🔍 PENDING | UAT-FD-009: Verify features visible per tier | 08_Testing_Evidence/ |

**Status**: ❌ **GAP**  
**Action**:
1. Design SubscriptionService architecture
2. Design subscription database schema
3. Create Jira ERPPLUS-93 with full requirements

---

### **FR-FD-004: Module Activation & Licensing**

| Field | Value |
|-------|-------|
| **FR ID** | FR-FD-004 |
| **Function Name** | Module Activation by Subscription |
| **Module** | SaaS Foundation |
| **BP ID** | N/A (Foundation) |
| **Business Rule** | BR-FD-MOD-001: Module visibility based on subscription |
| | BR-FD-MOD-002: Module can be enabled/disabled per tenant |
| | BR-FD-MOD-003: Menu & API endpoints filtered by active modules |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ⚠️ PARTIAL | Need: ModuleRegistry, ModuleActivation, FeatureGuard | 14_Claude_Execution/Task_Prompts/ |
| **Database** | ⚠️ PARTIAL | Tables: tenant_modules, module_status | Partial in 03_Data_Model_Overview.md |
| **Screen/API** | ⚠️ PARTIAL | API-FD-009: GET /api/modules/active (filters by tenant) | 01_System_Overview.md |
| | | SCR-FD-005: Module Dashboard | Design needed |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-94: Module activation flow | |
| **Claude Task** | 🔍 PENDING | CTK-FD-004: Generate module filtering logic | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-FD-007: Verify inactive modules hidden from menu | 08_Testing_Evidence/ |

**Status**: ⚠️ **PARTIAL**  
**Action**:
1. Verify ModuleRegistry implementation
2. Confirm tenant_modules table structure
3. Create Jira ERPPLUS-94 for activation flow

---

## 🛒 Purchase Module Requirements

### **FR-PUR-001: Purchase Request Creation**

| Field | Value |
|-------|-------|
| **FR ID** | FR-PUR-001 |
| **Function Name** | Create Purchase Request (PR) |
| **Module** | Purchase (BP-003 Procure-to-Pay) |
| **BP ID** | BP-003 |
| **Business Rule** | BR-PUR-001: PR created from approved requisition |
| | BR-PUR-002: PR must have valid line items with quantities |
| | BR-PUR-003: PR status progression: Draft → Submitted → Approved |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | 🔍 PENDING | Need: PurchaseRequestService, PurchaseRequestORM | 10_Modules/Purchase/ |
| **Database** | ⚠️ PARTIAL | Table: purchase_order (ORM) | 03_Data_Model_Overview.md |
| | | Columns: pr_number, status, created_date, amount_total |
| **Screen/API** | ⚠️ PARTIAL | API-FD-101: POST /api/purchase-requests | Design |
| | | SCR-PUR-001: PR Creation Form | Design needed |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-95: PR creation service | |
| **Claude Task** | 🔍 PENDING | CTK-PUR-001: Generate PR creation logic | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-PUR-001: Create PR from requisition | 08_Testing_Evidence/ |

**Status**: ⚠️ **PARTIAL**  
**Action**:
1. Verify PurchaseRequestService exists
2. Map PR database fields to schema
3. Create Jira ERPPLUS-95

---

### **FR-PUR-002: RFQ (Request for Quotation) Management**

| Field | Value |
|-------|-------|
| **FR ID** | FR-PUR-002 |
| **Function Name** | Create & Send RFQ to Vendors |
| **Module** | Purchase (BP-003) |
| **BP ID** | BP-003 |
| **Business Rule** | BR-PUR-201: RFQ created from PR line items |
| | BR-PUR-202: RFQ sent to selected vendors (multi-vendor) |
| | BR-PUR-203: RFQ has quote deadline & response tracking |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ❌ GAP | Need: RFQService, RFQTemplate, VendorNotificationService | New design |
| **Database** | ❌ GAP | Tables: rfq_header, rfq_line, rfq_vendor, rfq_response | Design needed |
| **Screen/API** | ❌ GAP | API-FD-102: POST /api/rfq (create RFQ) | Design needed |
| | | API-FD-103: POST /api/rfq/{id}/send (send to vendors) | Design needed |
| | | SCR-PUR-002: RFQ Management Dashboard | Design needed |
| **Jira Issue** | ❌ GAP | Create: ERPPLUS-96: Design & build RFQ service | |
| **Claude Task** | ❌ GAP | CTK-PUR-002: Generate RFQ logic | |
| **UAT Test Case** | ❌ GAP | UAT-PUR-004: Create RFQ & send to 3 vendors | Needs design |

**Status**: ❌ **GAP**  
**Action** (HIGH PRIORITY):
1. Design RFQService architecture
2. Design RFQ database schema (rfq_header, rfq_line, rfq_vendor)
3. Design vendor notification flow
4. Create Jira ERPPLUS-96 with detailed requirements

---

### **FR-PUR-003: Vendor Response & Quote Tracking**

| Field | Value |
|-------|-------|
| **FR ID** | FR-PUR-003 |
| **Function Name** | Receive & Track Vendor Quotations |
| **Module** | Purchase (BP-003) |
| **BP ID** | BP-003 |
| **Business Rule** | BR-PUR-301: Vendor quotations mapped to RFQ |
| | BR-PUR-302: Quote tracking: Pending → Received → Evaluated |
| | BR-PUR-303: Automatic reminder if quote not received by deadline |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ❌ NEW | Need: QuoteReceiptService, DeadlineReminderJob | New |
| **Database** | ❌ NEW | Table: quote_responses (vendor_id, rfq_id, quote_date, price) | New |
| **Screen/API** | ❌ NEW | API-FD-104: POST /api/quotes (receive quote) | New |
| | | SCR-PUR-003: Quote Comparison Dashboard | New |
| **Jira Issue** | ❌ NEW | Create: ERPPLUS-97: Quote receipt & tracking | |
| **Claude Task** | ❌ NEW | CTK-PUR-003: Generate quote logic | |
| **UAT Test Case** | ❌ NEW | UAT-PUR-007: Receive quotes, verify deadline reminders | New |

**Status**: 🆕 **NEW**  
**Action** (HIGH PRIORITY):
1. Design quote receipt & tracking mechanism
2. Design reminder notification system
3. Create Jira ERPPLUS-97 with UX mockups

---

### **FR-PUR-004: Vendor Comparison & Analysis**

| Field | Value |
|-------|-------|
| **FR ID** | FR-PUR-004 |
| **Function Name** | Compare Vendor Quotes & Select Best |
| **Module** | Purchase (BP-003) |
| **BP ID** | BP-003 |
| **Business Rule** | BR-PUR-401: Price comparison (unit price, total, terms) |
| | BR-PUR-402: Quality metrics (delivery time, past performance) |
| | BR-PUR-403: Comparison report auto-generated |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ❌ NEW | Need: ComparisonEngine, ScoringAlgorithm, ReportGenerator | New |
| **Database** | ❌ NEW | Table: quote_comparison_scoring | New |
| **Screen/API** | ❌ NEW | API-FD-105: GET /api/rfq/{id}/comparison (analysis) | New |
| | | SCR-PUR-004: Comparison Dashboard with charts | New |
| **Jira Issue** | ❌ NEW | Create: ERPPLUS-98: Vendor comparison logic | |
| **Claude Task** | ❌ NEW | CTK-PUR-004: Generate comparison engine | |
| **UAT Test Case** | ❌ NEW | UAT-PUR-010: Compare 3 vendors, verify scoring | New |

**Status**: 🆕 **NEW**  
**Action** (MEDIUM PRIORITY):
1. Define comparison scoring algorithm
2. Design dashboard UI with charts
3. Create Jira ERPPLUS-98

---

### **FR-PUR-005: Vendor Selection & Approval**

| Field | Value |
|-------|-------|
| **FR ID** | FR-PUR-005 |
| **Function Name** | Select Winning Vendor & Route for Approval |
| **Module** | Purchase (BP-003) |
| **BP ID** | BP-003 |
| **Business Rule** | BR-PUR-501: Manager selects vendor & submits for approval |
| | BR-PUR-502: Approval workflow: Dept Head → Finance → Director |
| | BR-PUR-503: Rejection reverts to selection, allows new choice |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ⚠️ PARTIAL | Need: ApprovalWorkflow (generic exists) | 02_MODULE_ARCHITECTURE.md |
| **Database** | ⚠️ PARTIAL | Table: approval_workflows (generic entity) | 03_DATA_MODEL_OVERVIEW.md |
| | | Need: vendor_selection_approvals mapping |
| **Screen/API** | ⚠️ PARTIAL | API-FD-106: POST /api/vendor-selection/approve | Design |
| | | SCR-PUR-005: Approval Inbox & History | Design |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-99: Vendor approval workflow | |
| **Claude Task** | 🔍 PENDING | CTK-PUR-005: Generate approval logic | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-PUR-012: Test approval routing & rejection | Design |

**Status**: ⚠️ **PARTIAL**  
**Action**:
1. Confirm generic approval workflow supports vendor selection
2. Design vendor_selection_approvals mapping
3. Create Jira ERPPLUS-99

---

### **FR-PUR-006: Purchase Order Generation from RFQ**

| Field | Value |
|-------|-------|
| **FR ID** | FR-PUR-006 |
| **Function Name** | Auto-Generate PO from Approved RFQ |
| **Module** | Purchase (BP-003) |
| **BP ID** | BP-003 |
| **Business Rule** | BR-PUR-601: PO created from RFQ after vendor approval |
| | BR-PUR-602: PO line items from RFQ line items |
| | BR-PUR-603: Vendor payment terms & shipping copied to PO |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ⚠️ PARTIAL | Need: POGenerationService | 10_Modules/Purchase/ |
| **Database** | ⚠️ PARTIAL | Table: purchase_order | 03_DATA_MODEL_OVERVIEW.md |
| | | Columns: po_number, rfq_id, vendor_id, po_date, total_amount |
| **Screen/API** | ⚠️ PARTIAL | API-FD-107: POST /api/purchase-orders (auto-generate) | Design |
| | | SCR-PUR-006: PO Creation & Preview | Design |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-100: PO generation service | |
| **Claude Task** | 🔍 PENDING | CTK-PUR-006: Generate PO creation logic | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-PUR-014: Auto-generate PO from approved RFQ | Design |

**Status**: ⚠️ **PARTIAL**  
**Action**:
1. Verify POGenerationService implementation
2. Map RFQ-to-PO field mappings
3. Create Jira ERPPLUS-100

---

## 📦 Inventory Module Requirements

### **FR-INV-001: Goods Receipt & Stock Update**

| Field | Value |
|-------|-------|
| **FR ID** | FR-INV-001 |
| **Function Name** | Receive Goods & Update Inventory |
| **Module** | Inventory (BP-004) |
| **BP ID** | BP-004 |
| **Business Rule** | BR-INV-001: Goods receipt created from PO |
| | BR-INV-002: Stock levels auto-updated upon receipt |
| | BR-INV-003: Quality inspection flagged if needed |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ⚠️ PARTIAL | Need: GoodsReceiptService | 10_Modules/Inventory/ |
| **Database** | ⚠️ PARTIAL | Table: stock_picking | 03_DATA_MODEL_OVERVIEW.md |
| | | Table: stock_movement | 03_DATA_MODEL_OVERVIEW.md |
| **Screen/API** | ⚠️ PARTIAL | API-FD-201: POST /api/goods-receipt | Design |
| | | SCR-INV-001: GR Creation & Scanning | Design |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-101: Goods receipt service | |
| **Claude Task** | 🔍 PENDING | CTK-INV-001: Generate GR logic | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-INV-001: Receive goods, verify stock update | Design |

**Status**: ⚠️ **PARTIAL**  
**Action**:
1. Verify GoodsReceiptService implementation
2. Validate stock_picking and stock_movement table usage
3. Create Jira ERPPLUS-101

---

## 💰 Accounting Module Requirements

### **FR-ACC-001: Vendor Bill Processing**

| Field | Value |
|-------|-------|
| **FR ID** | FR-ACC-001 |
| **Function Name** | Receive & Process Vendor Invoice |
| **Module** | Accounting (BP-006) |
| **BP ID** | BP-006 |
| **Business Rule** | BR-ACC-001: Bill matched to PO (3-way match) |
| | BR-ACC-002: GL entries created for AP & expense |
| | BR-ACC-003: Payment terms applied, due date calculated |

**Evidence Collection:**

| Type | Status | Evidence | Location |
|------|--------|----------|----------|
| **Source Code** | ⚠️ PARTIAL | Need: VendorBillService, ThreeWayMatchEngine | 10_Modules/Accounting/ |
| **Database** | ⚠️ PARTIAL | Table: account_move | 03_DATA_MODEL_OVERVIEW.md |
| | | Columns: invoice_number, po_id, vendor_id, bill_date, amount, due_date |
| **Screen/API** | ⚠️ PARTIAL | API-FD-301: POST /api/vendor-bills | Design |
| | | SCR-ACC-001: Invoice Entry & Matching | Design |
| **Jira Issue** | 🔍 PENDING | Create: ERPPLUS-102: Vendor bill processing | |
| **Claude Task** | 🔍 PENDING | CTK-ACC-001: Generate bill logic | |
| **UAT Test Case** | ⚠️ PARTIAL | UAT-ACC-001: 3-way match & GL creation | Design |

**Status**: ⚠️ **PARTIAL**  
**Action**:
1. Verify ThreeWayMatchEngine implementation
2. Confirm GL entry creation logic
3. Create Jira ERPPLUS-102

---

## 📈 Gap Analysis Summary

### **Critical Gaps (MUST IMPLEMENT)**

| Gap ID | Requirement | Module | Priority | Owner |
|--------|-------------|--------|----------|-------|
| **GAP-001** | FR-FD-003: Subscription Service | SaaS Foundation | CRITICAL | Enterprise Architect AI |
| **GAP-002** | FR-PUR-002: RFQ Management | Purchase | CRITICAL | Functional Specification AI |
| **GAP-003** | FR-PUR-003: Quote Tracking | Purchase | CRITICAL | Functional Specification AI |
| **GAP-004** | FR-PUR-004: Vendor Comparison | Purchase | HIGH | Functional Specification AI |

### **Partial Gaps (REQUIRE VERIFICATION)**

| Gap ID | Requirement | Module | Action |
|--------|-------------|--------|--------|
| **PGAP-001** | FR-FD-001: Tenant Isolation | SaaS Foundation | Verify TenantMiddleware |
| **PGAP-002** | FR-FD-002: RBAC Implementation | SaaS Foundation | Verify role hierarchy |
| **PGAP-003** | FR-FD-004: Module Activation | SaaS Foundation | Verify ModuleRegistry |
| **PGAP-004** | FR-PUR-001: PR Creation | Purchase | Verify PurchaseRequestService |
| **PGAP-005** | FR-PUR-005: Approval Workflow | Purchase | Confirm generic workflow fit |
| **PGAP-006** | FR-PUR-006: PO Generation | Purchase | Verify POGenerationService |
| **PGAP-007** | FR-INV-001: Goods Receipt | Inventory | Verify GoodsReceiptService |
| **PGAP-008** | FR-ACC-001: Vendor Bill | Accounting | Verify ThreeWayMatchEngine |

---

## 🎯 Jira Task Recommendations

### **Create These Issues in ERPPLUS Project**

```
Priority: CRITICAL
==============================

ERPPLUS-91: TenantMiddleware Implementation & Verification
Description: Verify or implement tenant isolation middleware
  - Subtask 1: Code review existing TenantMiddleware
  - Subtask 2: Verify tenant_id passed in all API calls
  - Subtask 3: Verify DB-level row security policies
  - Subtask 4: Create test suite for isolation
Type: Task | Story Points: 13 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-92: RBAC Role Hierarchy Implementation
Description: Implement role-based access control with hierarchy
  - Subtask 1: Design role_hierarchy table
  - Subtask 2: Implement RoleHierarchy service
  - Subtask 3: Create PermissionDecorator for API endpoints
  - Subtask 4: Add role checking to all screens
Type: Task | Story Points: 21 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-93: Subscription Service Architecture & Implementation
Description: Design and build complete subscription management
  - Subtask 1: Design SubscriptionService architecture
  - Subtask 2: Create subscription database schema
  - Subtask 3: Implement subscription APIs (create/upgrade/cancel)
  - Subtask 4: Implement feature flag system
  - Subtask 5: Create subscription UI screens
Type: Story | Story Points: 34 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-94: Module Activation & Feature Gating
Description: Implement module activation per subscription
  - Subtask 1: Create ModuleRegistry service
  - Subtask 2: Implement module filtering in API responses
  - Subtask 3: Implement module hiding in UI menu
  - Subtask 4: Create module status management UI
Type: Story | Story Points: 21 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-95: Purchase Request (PR) Service Implementation
Description: Implement PR creation from requisitions
  - Subtask 1: Create PurchaseRequestService
  - Subtask 2: Create PR creation API (POST /api/purchase-requests)
  - Subtask 3: Create PR UI screens
  - Subtask 4: Implement PR workflow (Draft → Submitted → Approved)
Type: Story | Story Points: 21 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-96: RFQ (Request for Quotation) Service - CRITICAL
Description: Implement complete RFQ management system
  - Subtask 1: Design RFQ data model (rfq_header, rfq_line, rfq_vendor)
  - Subtask 2: Create RFQService (create, send, track)
  - Subtask 3: Create vendor notification system
  - Subtask 4: Create RFQ UI dashboard
  - Subtask 5: Implement RFQ deadline & reminder logic
  - Subtask 6: Create RFQ APIs
Type: Story | Story Points: 55 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-97: Quote Receipt & Tracking System - CRITICAL
Description: Implement vendor quote receipt and tracking
  - Subtask 1: Design quote_responses table
  - Subtask 2: Create QuoteReceiptService
  - Subtask 3: Implement automatic deadline reminders
  - Subtask 4: Create quote tracking dashboard
  - Subtask 5: Create quote receipt APIs
Type: Story | Story Points: 34 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-98: Vendor Quote Comparison Engine - CRITICAL
Description: Implement quote comparison and scoring
  - Subtask 1: Design comparison scoring algorithm
  - Subtask 2: Create ComparisonEngine service
  - Subtask 3: Create comparison dashboard with charts
  - Subtask 4: Implement auto-report generation
Type: Story | Story Points: 34 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-99: Vendor Selection & Approval Workflow
Description: Implement vendor selection approval routing
  - Subtask 1: Design vendor_selection_approvals mapping
  - Subtask 2: Implement approval workflow routing
  - Subtask 3: Create approval inbox UI
  - Subtask 4: Test rejection and resubmission flow
Type: Story | Story Points: 21 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-100: Purchase Order (PO) Auto-Generation
Description: Auto-generate PO from approved RFQ
  - Subtask 1: Create POGenerationService
  - Subtask 2: Map RFQ-to-PO field transformations
  - Subtask 3: Create PO generation trigger
  - Subtask 4: Create PO preview UI
Type: Story | Story Points: 21 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-101: Goods Receipt (GR) & Stock Update
Description: Implement goods receipt and inventory update
  - Subtask 1: Create GoodsReceiptService
  - Subtask 2: Implement stock_movement auto-creation
  - Subtask 3: Create GR scanning UI
  - Subtask 4: Implement quality inspection flags
Type: Story | Story Points: 21 | Sprint: ERPPLUS-87 (Phase 2)

ERPPLUS-102: Vendor Bill Processing & 3-Way Match
Description: Implement vendor invoice receipt and GL posting
  - Subtask 1: Create VendorBillService
  - Subtask 2: Implement ThreeWayMatchEngine (PO ↔ GR ↔ Invoice)
  - Subtask 3: Implement GL entry auto-creation
  - Subtask 4: Create bill matching UI
Type: Story | Story Points: 34 | Sprint: ERPPLUS-87 (Phase 2)
```

---

## 🔍 Claude Matching Requirements

### **Claude Must Read These References:**

1. **Learning Materials** (new):
   - `16_Learning_Analysis/00_LEARNING_INDEX.md` ← START HERE
   - `16_Learning_Analysis/01_SYSTEM_OVERVIEW.md` ← Architecture context
   - `16_Learning_Analysis/02_MODULE_ARCHITECTURE.md` ← Module responsibilities
   - `16_Learning_Analysis/03_DATA_MODEL_OVERVIEW.md` ← Database schema

2. **Foundation Documentation:**
   - `01_SaaS_Foundation/FDS/SMEPLUS-SAAS-FOUNDATION-FDS-v0.1.md` ← Foundation requirements
   - `10_Modules/Purchase/ (if available)` ← Purchase module design

3. **Existing Evidence:**
   - `12_Traceability/Requirement_Matrix/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX-v0.1.md` ← This file
   - `02_Functional_Design/ (if available)` ← Functional specs

### **Claude Output Required:**

1. **Source Code Evidence**
   - For each FR, identify ORM classes, services, controllers
   - Reference exact file paths (e.g., `src/purchase/services/rfq.service.ts`)
   - Note if evidence exists or GAP

2. **Database Evidence**
   - For each FR, identify tables, columns, relationships
   - Reference schema definitions
   - Note if tables exist or need design

3. **Status Update**
   - Update MATCHED / PARTIAL / GAP / NEW / RETIRE status
   - Add action items for each gap

4. **Jira Task Generation**
   - Create Jira-formatted task list
   - Include acceptance criteria
   - Assign story points (T-shirt sizing: S=5, M=13, L=21, XL=34, XXL=55)

5. **Risk Assessment**
   - Identify critical path items (RFQ, Quotes, Comparison)
   - Highlight dependencies
   - Flag technical complexity

---

## ⚠️ Implementation Risk Assessment

### **Critical Path Items** 🔴

| Item | Risk | Impact | Mitigation |
|------|------|--------|-----------|
| RFQ System (FR-PUR-002) | HIGH | Blocks all vendor selection | Design first, build in Phase 2 Week 1 |
| Quote Tracking (FR-PUR-003) | HIGH | Blocks comparison & selection | Parallel development with RFQ |
| Comparison Engine (FR-PUR-004) | MEDIUM | Blocks vendor decision | Implement scoring early, refine later |

### **Dependency Chain** 🔗

```
Subscription (FR-FD-003)
    ↓
Module Activation (FR-FD-004)
    ↓
Purchase Request (FR-PUR-001)
    ↓
RFQ Management (FR-PUR-002)
    ↓
Quote Tracking (FR-PUR-003)
    ↓
Quote Comparison (FR-PUR-004)
    ↓
Vendor Approval (FR-PUR-005)
    ↓
PO Generation (FR-PUR-006)
    ↓
Goods Receipt (FR-INV-001)
    ↓
Vendor Bill (FR-ACC-001)
```

**CRITICAL**: Any gap in Subscription/RBAC delays entire purchase flow.

---

## 📊 Matrix Status Summary

| Category | Matched | Partial | Gap | New | Total | % Complete |
|----------|---------|---------|-----|-----|-------|------------|
| **SaaS Foundation** | 0 | 2 | 1 | 1 | 4 | 50% |
| **Purchase Module** | 0 | 3 | 1 | 2 | 6 | 50% |
| **Inventory Module** | 0 | 1 | 0 | 0 | 1 | 100% ⚠️ |
| **Accounting Module** | 0 | 1 | 0 | 0 | 1 | 100% ⚠️ |
| **TOTAL** | 0 | 7 | 2 | 3 | 12 | 58% |

**Note**: ⚠️ Inventory & Accounting show 100% but only have PARTIAL evidence - requires verification

---

## ✅ Next Steps

### **Immediate (Today 2026-07-02):**
1. ✅ Create this matching matrix
2. Share with Claude Code AI for evidence collection
3. Share with Database Design AI for schema verification
4. Share with Enterprise Architect AI for gap review

### **Phase 2 (2026-07-03 to 07):**
1. Claude fills Source Code Evidence for all items
2. Database Design AI fills Database Evidence
3. Resolve all PARTIAL gaps
4. Create Jira issues for all GAP & NEW items
5. Estimate story points

### **Phase 3 (2026-07-08):**
1. Code review for evidence verification
2. UAT test case mapping
3. Gate sign-off

---

## 📝 Document Control

| Field | Value |
|-------|-------|
| **Version** | 0.1 (Draft) |
| **Created** | 2026-07-02 |
| **Last Updated** | 2026-07-02 |
| **Owner** | Functional Specification AI |
| **Status** | Draft for Claude + ChatGPT Review |
| **Next Review** | 2026-07-03 (Post Phase 2 kick-off) |
| **Approval** | Pending - Technical Team AI |

---

**Document End**

🔄 **Ready for Claude matching analysis and ChatGPT review!**

