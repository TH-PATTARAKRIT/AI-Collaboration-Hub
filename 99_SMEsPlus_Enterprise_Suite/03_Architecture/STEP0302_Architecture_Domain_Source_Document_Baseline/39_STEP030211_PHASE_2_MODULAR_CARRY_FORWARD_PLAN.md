# STEP030211: Phase 2 Modular Carry-Forward Plan

**Session ID**: [SMEPLUS-26-07-19-001]  
**Control Level**: /L99.99  
**Step ID**: STEP030211  
**Date**: 2026-07-19  
**Status**: PHASE 2 MODULAR CARRY-FORWARD PLAN PREPARED  
**Principle**: Module-Separated Execution with Controlled Future Correction Paths

---

## 1. Executive Summary

Per Boss authorization in STEP030211, Phase 2 planning includes non-Accounting modules (HR, Purchase, Sales, Inventory) in addition to Accounting, but **modules remain separated by module group** for future correction and controlled execution. This plan outlines:

- Module group organization structure
- Functional design carry-forward per module
- Future correction and enhancement paths per module
- Module ownership and accountability
- Controlled module separation strategy

**Core Principle**: No module mixing. Each module maintains independent correction and enhancement track.

---

## 2. Phase 2 Module Group Organization

### Module Groups Defined

| Module Group | Status | FDS Phase | Owner Responsibility | Correction Track |
|--------------|--------|-----------|---------------------|------------------|
| **Accounting** | Core Module | Phase 2 FDS | Accounting Functional Lead | ACC-001 (existing) + Phase 2 enhancements |
| **HR** | Expansion Module | Phase 2 FDS (Non-Core) | HR Functional Lead | HR-001 (future) |
| **Purchase** | Expansion Module | Phase 2 FDS (Non-Core) | Purchase Functional Lead | PUR-001 (future) |
| **Sales** | Expansion Module | Phase 2 FDS (Non-Core) | Sales Functional Lead | SAL-001 (future) |
| **Inventory** | Expansion Module | Phase 2 FDS (Non-Core) | Inventory Functional Lead | INV-001 (future) |
| **Future Expansion Modules** | TBD | Phase 2+ | TBD | TBD (future) |

### Module Group Separation Strategy

**Mandatory Separation Rules**:

1. **No Cross-Module Data Dependencies**: Each module defines data ownership and scopes independently (per GAP-010)
2. **No Cross-Module Functional Dependencies**: Functional Design proceeds per-module with clear interface specifications
3. **No Module Collapsing**: Non-Accounting modules remain separate throughout Phase 2; NO attempt to merge into Accounting
4. **Independent Review**: Each module undergoes separate functional design review and owner sign-off
5. **Separate Correction Channels**: Each module maintains independent correction register and enhancement backlog

---

## 3. Accounting Module — Phase 2 Carry-Forward Plan

### Accounting Module Scope (CORE MODULE)

**Module Status**: Core functional domain for Open ERP  
**Functional Lead**: Accounting Functional Lead (TBD)  
**Current Phase**: Phase 2 Functional Design Specification (FDS)  
**Correction Track**: ACC (established batch: ACC-001, ACC-002, etc.)

### Accounting FDS Carry-Forward Items

| FDS Item | Domain | Description | Carry-Forward Status | Phase 2 Work | Deliverable |
|----------|--------|-------------|---------------------|------------|------------|
| Accounting Core Flows | Financial Operations | Chart of Accounts, GL Posting, Journal Entry, Period Close, Financial Reporting flows | CARRY-FORWARD | Complete detailed functional flows and validation rules | ACC_Accounting_Core_Flows_FDS_v1.0 |
| Multi-Currency | Financial Operations | Multi-currency transactions, exchange rate management, revaluation, settlement | CARRY-FORWARD | Define currency handling, rate sources, revaluation rules | ACC_Multi-Currency_Design_v1.0 |
| Multi-Entity | Financial Operations | Consolidated reporting, inter-company transactions, elimination rules | CARRY-FORWARD | Define consolidation logic and inter-company process | ACC_Multi-Entity_Design_v1.0 |
| Tax Compliance | Financial Operations | Tax calculation, tax returns, compliance reporting by jurisdiction | CARRY-FORWARD | Define tax engine and jurisdiction-specific rules | ACC_Tax_Design_v1.0 |
| Audit Trail | Compliance | Complete audit logging for all financial transactions and adjustments | CARRY-FORWARD | Define audit data capture and reporting requirements | ACC_Audit_Trail_Design_v1.0 |
| Reconciliation | Financial Operations | Bank reconciliation, GL reconciliation, inter-company reconciliation | CARRY-FORWARD | Define reconciliation matching logic and workflows | ACC_Reconciliation_Design_v1.0 |
| Budget and Forecast | Financial Operations | Budget entry, variance analysis, forecast vs. actual | CARRY-FORWARD | Define budget models and variance reporting | ACC_Budget_Design_v1.0 |
| Cost Allocation | Financial Operations | Cost center allocation, job costing, project accounting | CARRY-FORWARD | Define allocation rules and cost accounting models | ACC_Cost_Allocation_Design_v1.0 |

### Accounting Module Future Correction Path

**Correction Track**: ACC-00X (existing and new)

**Correction Categories**:
- ACC-Conformance: Alignment with Open ERP standards and architecture
- ACC-Enhancement: Feature additions and optimization
- ACC-Performance: Accounting module performance tuning
- ACC-Integration: Cross-module integration with other functional domains
- ACC-Compliance: Regulatory and audit requirement updates

**Module Ownership**: Sole responsibility of Accounting Functional Lead; no other module may claim Accounting functional ownership.

---

## 4. HR Module — Phase 2 Carry-Forward Plan

### HR Module Scope (EXPANSION MODULE)

**Module Status**: Expansion module planned for Open ERP Phase 2+  
**Functional Lead**: HR Functional Lead (TBD)  
**Current Phase**: Phase 2 Functional Design Specification (Non-Core)  
**Correction Track**: HR-001 (to be established)

### HR FDS Carry-Forward Items

| FDS Item | Domain | Description | Carry-Forward Status | Phase 2 Work | Deliverable |
|----------|--------|-------------|---------------------|------------|------------|
| Organization Structure | HR Admin | Organization hierarchy, reporting lines, cost centers | CARRY-FORWARD | Define org structure modeling and hierarchy rules | HR_Org_Structure_Design_v1.0 |
| Employee Management | HR Admin | Employee master, personal information, employment contracts | CARRY-FORWARD | Define employee data model and change tracking | HR_Employee_Management_Design_v1.0 |
| Recruitment | HR Operations | Job requisitions, candidate tracking, offer management | CARRY-FORWARD | Define recruitment workflow and candidate lifecycle | HR_Recruitment_Design_v1.0 |
| Compensation | HR Operations | Salary structures, pay grades, benefit administration | CARRY-FORWARD | Define compensation models and benefits allocation | HR_Compensation_Design_v1.0 |
| Time and Attendance | HR Operations | Time tracking, attendance, overtime, leave management | CARRY-FORWARD | Define time tracking and leave accrual models | HR_Time_Attendance_Design_v1.0 |
| Performance Management | HR Operations | Performance reviews, goal setting, appraisals | CARRY-FORWARD | Define performance evaluation workflows | HR_Performance_Design_v1.0 |
| Learning and Development | HR Operations | Training programs, skill tracking, certifications | CARRY-FORWARD | Define L&D program management | HR_Learning_Design_v1.0 |

### HR Module Future Correction Path

**Correction Track**: HR-00X (to be established)

**Correction Categories**:
- HR-Conformance: Alignment with Open ERP standards
- HR-Enhancement: Feature additions and module expansion
- HR-Integration: HR to other modules (Accounting payroll integration, etc.)
- HR-Compliance: Labor law and compliance requirements

**Module Ownership**: Sole responsibility of HR Functional Lead; HR functional decisions do NOT overlap with Accounting or other modules.

**Future Expansion**: HR module may expand to include additional modules (Payroll, Workforce Planning) in future phases, each maintaining separate correction tracks.

---

## 5. Purchase Module — Phase 2 Carry-Forward Plan

### Purchase Module Scope (EXPANSION MODULE)

**Module Status**: Expansion module planned for Open ERP Phase 2+  
**Functional Lead**: Purchase Functional Lead (TBD)  
**Current Phase**: Phase 2 Functional Design Specification (Non-Core)  
**Correction Track**: PUR-001 (to be established)

### Purchase FDS Carry-Forward Items

| FDS Item | Domain | Description | Carry-Forward Status | Phase 2 Work | Deliverable |
|----------|--------|-------------|---------------------|------------|------------|
| Purchase Requisition | Procurement | Purchase requests, approval workflows, requisition management | CARRY-FORWARD | Define requisition lifecycle and approval rules | PUR_Requisition_Design_v1.0 |
| Vendor Management | Procurement | Vendor master, vendor qualification, vendor performance | CARRY-FORWARD | Define vendor data model and qualification criteria | PUR_Vendor_Management_Design_v1.0 |
| Purchase Order | Procurement | PO creation, receipt, three-way matching, invoice matching | CARRY-FORWARD | Define PO lifecycle and matching algorithms | PUR_PurchaseOrder_Design_v1.0 |
| Supplier Invoice | Procurement | Invoice receipt, validation, matching to PO and receipt | CARRY-FORWARD | Define invoice processing and payment terms | PUR_Supplier_Invoice_Design_v1.0 |
| Supplier Performance | Procurement | On-time delivery tracking, quality metrics, cost analysis | CARRY-FORWARD | Define supplier scorecards and KPI tracking | PUR_Supplier_Performance_Design_v1.0 |
| Contract Management | Procurement | Supplier contracts, terms, rate cards, compliance tracking | CARRY-FORWARD | Define contract lifecycle management | PUR_Contract_Management_Design_v1.0 |

### Purchase Module Future Correction Path

**Correction Track**: PUR-00X (to be established)

**Correction Categories**:
- PUR-Conformance: Alignment with Open ERP standards
- PUR-Enhancement: Feature additions and optimization
- PUR-Integration: Integration with Inventory, Accounting, and Finance modules
- PUR-Compliance: Supplier and regulatory compliance

**Module Ownership**: Sole responsibility of Purchase Functional Lead; Purchase functional decisions are independent of Sales, Inventory, and Accounting scope.

---

## 6. Sales Module — Phase 2 Carry-Forward Plan

### Sales Module Scope (EXPANSION MODULE)

**Module Status**: Expansion module planned for Open ERP Phase 2+  
**Functional Lead**: Sales Functional Lead (TBD)  
**Current Phase**: Phase 2 Functional Design Specification (Non-Core)  
**Correction Track**: SAL-001 (to be established)

### Sales FDS Carry-Forward Items

| FDS Item | Domain | Description | Carry-Forward Status | Phase 2 Work | Deliverable |
|----------|--------|-------------|---------------------|------------|------------|
| Sales Quote | Sales Operations | Quote creation, approval, expiration management | CARRY-FORWARD | Define quote lifecycle and approval workflows | SAL_Quote_Design_v1.0 |
| Sales Order | Sales Operations | Order entry, order confirmation, fulfillment tracking | CARRY-FORWARD | Define order lifecycle and fulfillment rules | SAL_Order_Design_v1.0 |
| Customer Management | Sales Operations | Customer master, contact management, hierarchy | CARRY-FORWARD | Define customer data model and segmentation | SAL_Customer_Management_Design_v1.0 |
| Pricing | Sales Operations | Price lists, discounts, promotions, volume pricing | CARRY-FORWARD | Define pricing engine and promotion rules | SAL_Pricing_Design_v1.0 |
| Sales Pipeline | Sales Operations | Opportunity tracking, forecasting, pipeline management | CARRY-FORWARD | Define opportunity lifecycle and forecast models | SAL_Pipeline_Design_v1.0 |
| Fulfillment | Sales Operations | Picking, packing, shipping integration, delivery tracking | CARRY-FORWARD | Define fulfillment workflow and shipping integration | SAL_Fulfillment_Design_v1.0 |
| Billing | Sales Operations | Invoice generation, billing terms, revenue recognition | CARRY-FORWARD | Define billing workflow and revenue rules | SAL_Billing_Design_v1.0 |

### Sales Module Future Correction Path

**Correction Track**: SAL-00X (to be established)

**Correction Categories**:
- SAL-Conformance: Alignment with Open ERP standards
- SAL-Enhancement: Feature additions and sales automation
- SAL-Integration: Integration with Inventory, Accounting, and Shipping modules
- SAL-Compliance: Sales compliance and revenue recognition

**Module Ownership**: Sole responsibility of Sales Functional Lead; Sales functional decisions are independent of Purchase, Inventory, and Accounting scope.

---

## 7. Inventory Module — Phase 2 Carry-Forward Plan

### Inventory Module Scope (EXPANSION MODULE)

**Module Status**: Expansion module planned for Open ERP Phase 2+  
**Functional Lead**: Inventory Functional Lead (TBD)  
**Current Phase**: Phase 2 Functional Design Specification (Non-Core)  
**Correction Track**: INV-001 (to be established)

### Inventory FDS Carry-Forward Items

| FDS Item | Domain | Description | Carry-Forward Status | Phase 2 Work | Deliverable |
|----------|--------|-------------|---------------------|------------|------------|
| Inventory Master | Inventory Operations | Item master, units of measure, item hierarchies | CARRY-FORWARD | Define item data model and classification | INV_Item_Master_Design_v1.0 |
| Warehouse Setup | Inventory Operations | Warehouse locations, bins, putaway rules, picking rules | CARRY-FORWARD | Define warehouse topology and routing logic | INV_Warehouse_Setup_Design_v1.0 |
| Stock Transactions | Inventory Operations | Receipts, issues, transfers, adjustments | CARRY-FORWARD | Define inventory transaction processing | INV_Stock_Transactions_Design_v1.0 |
| Inventory Valuation | Inventory Operations | Costing methods (FIFO, LIFO, weighted average), revaluation | CARRY-FORWARD | Define costing engine and revaluation logic | INV_Valuation_Design_v1.0 |
| Cycle Counting | Inventory Operations | Physical counts, variance reconciliation, count procedures | CARRY-FORWARD | Define counting workflows and reconciliation | INV_Cycle_Counting_Design_v1.0 |
| Safety Stock | Inventory Operations | Reorder points, safety stock calculations, shortage alerts | CARRY-FORWARD | Define safety stock models and alert rules | INV_Safety_Stock_Design_v1.0 |
| Demand Planning | Inventory Operations | Forecasting, seasonal adjustments, replenishment planning | CARRY-FORWARD | Define demand models and replenishment algorithms | INV_Demand_Planning_Design_v1.0 |

### Inventory Module Future Correction Path

**Correction Track**: INV-00X (to be established)

**Correction Categories**:
- INV-Conformance: Alignment with Open ERP standards
- INV-Enhancement: Feature additions and inventory optimization
- INV-Integration: Integration with Purchase, Sales, and Accounting modules
- INV-Compliance: Compliance and audit trail requirements

**Module Ownership**: Sole responsibility of Inventory Functional Lead; Inventory functional decisions are independent of other functional domains.

---

## 8. Future Expansion Modules (Placeholder)

### Future Module Discovery Process

During Phase 2, the following modules may be identified as future expansion opportunities:

| Potential Future Module | Initial Scope | Status | TBD |
|------------------------|---------------|--------|-----|
| Payroll | Salary processing, tax withholding, statutory reporting | FUTURE | Correction track: PAY-001 (future) |
| Fixed Assets | Asset acquisition, depreciation, disposal, tracking | FUTURE | Correction track: FA-001 (future) |
| Supplier CRM | Supplier engagement, collaboration, performance | FUTURE | Correction track: SCST-001 (future) |
| Project Management | Project planning, resource allocation, project costing | FUTURE | Correction track: PROJ-001 (future) |
| Quality Management | Quality inspections, defect tracking, compliance | FUTURE | Correction track: QM-001 (future) |

**Process**: Any future modules identified during Phase 2 shall follow the same module separation pattern, with independent FDS, correction track, and ownership assignments.

---

## 9. Module Integration Points (Controlled Interfaces)

### Cross-Module Integration Requirements

While modules remain separated for correction and ownership, defined integration points are required:

| Integration | Source Module | Target Module | Integration Type | Phase 2 Work |
|-------------|---------------|--------------|------------------|------------|
| Payroll Accounting | HR (Payroll future) | Accounting | GL Account Posting | Define GL account rules and posting logic |
| Purchase-to-Pay | Purchase | Accounting | AP Invoice and GL Posting | Define GL account mapping and accrual rules |
| Order-to-Cash | Sales | Accounting | AR Invoice and GL Posting | Define GL account mapping and revenue rules |
| Inventory Valuation | Inventory | Accounting | COGS and Inventory GL | Define COGS calculation and GL posting |
| Asset Depreciation | Fixed Assets (future) | Accounting | Depreciation GL Posting | Define depreciation methods and GL posting |

**Integration Design Responsibility**: Each integration is designed with input from both modules; ownership remains with target module (e.g., Purchase-to-Pay interface owned by Accounting for GL posting rules).

---

## 10. Module Separation Governance

### Mandatory Module Separation Rules

1. **Functional Ownership**: Each module has sole functional lead assigned; NO shared module leads
2. **Data Model Separation**: Each module defines its own data model; shared entities (e.g., Customer, Item) have clear ownership rules
3. **Correction Track Separation**: Each module maintains independent correction register (ACC-00X, HR-00X, etc.)
4. **Feature Backlog Separation**: Future enhancements tracked separately per module
5. **FDS Approval Process**: Each module FDS reviewed and approved independently by module lead
6. **No Module Merging**: Non-Accounting modules will NOT be collapsed or merged with Accounting or other modules

### Violation Consequences

If module separation is violated:
- ✘ Cross-module dependencies introduced without Boss approval
- ✘ Modules merged without governance review
- ✘ Correction tracks mixed or consolidated

**Escalation**: Any violation must be escalated to Boss for resolution decision.

---

## 11. Phase 2 Module Execution Timeline

### Module Coordination Schedule

| Phase | Week | Accounting | HR | Purchase | Sales | Inventory | Notes |
|-------|------|-----------|----|---------|---------|-----------|----|
| Kickoff | 1 | FDS initiation | FDS initiation | FDS initiation | FDS initiation | FDS initiation | All modules start independently |
| Core Work | 2-4 | Core flows | Org structure | Vendor mgmt | Customer mgmt | Item master | Parallel module work |
| Integration | 3-4 | GL posting rules | Payroll accrual | AP accounts | AR accounts | COGS rules | Define cross-module GL rules |
| Review | 5 | Internal review | Internal review | Internal review | Internal review | Internal review | Module owner review |
| ChatGPT Review | 5-6 | L99 review | L99 review | L99 review | L99 review | L99 review | Independent review by ChatGPT L99 |
| Gate C Prep | 6 | Gate readiness | Gate readiness | Gate readiness | Gate readiness | Gate readiness | Prepare for Gate C assessment |

---

## 12. Document Control

| Property | Value |
|----------|-------|
| **Document ID** | 39_STEP030211_PHASE_2_MODULAR_CARRY_FORWARD_PLAN |
| **Classification** | /L99.99 |
| **Status** | COMPLETE — PHASE 2 MODULAR PLAN PREPARED |
| **Module Groups Defined** | 5 (Accounting, HR, Purchase, Sales, Inventory) + Future TBD |
| **Module Separation** | Mandatory per Boss authorization |

---

**STEP030211 PHASE 2 MODULAR CARRY-FORWARD — COMPLETE**

**Status**: Phase 2 modules separated by group; independent correction tracks established; no module mixing.

**Next Action**: Boss authorization for Phase 2 execution with module group separation maintained.

---

_Generated by Claude Code (Execution Agent) as part of STEP030211 execution_
