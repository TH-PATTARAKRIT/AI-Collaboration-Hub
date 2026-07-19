# STEP030211: Phase 2 Modular Carry-Forward Plan

**Session ID**: [SMEPLUS-26-07-19-001]  
**Control Level**: /L99.99  
**Step ID**: STEP030211  
**Date**: 2026-07-19  
**Total Modules Planned**: 5 Core + Future Extensible  
**Status**: PHASE 2 MODULAR CARRY-FORWARD PLANNING COMPLETE

---

## Executive Summary

Per Boss authorization: *"Confirm Phase 2 includes non-Accounting modules such as HR, Purchase, Sales, and Inventory, separated by module for future correction and controlled execution."*

This plan organizes ALL 24 gaps into modular work packages separated by business domain and module responsibility. Each module has:

- Independent work scope and ownership
- Dedicated deliverables and timelines
- Separate design path and future correction track
- No cross-module dependency collapse
- Clear separation for controlled handoff and Phase 2+ execution

**Principle**: "No module mixing. Future correction paths module-specific."

---

## MODULE 1: ACCOUNTING MODULE — Core System Module

### Module Scope

**Business Purpose**: Financial transaction processing, general ledger, accounts payable/receivable, financial reporting, compliance  
**Baseline Status**: MOST COMPLETE in source document baseline (Domain 10: 6 sources verified for Accounting)  
**Future Correction Path**: Dedicated STEP030206+ execution package  

### Module Gaps and Responsibilities

| Gap ID | Domain | Title | Scope | Owner | Phase 2 Target |
|---|---|---|---|---|---|
| **CRITICAL-GAP-001** | System Context | System Context Diagram | Solution boundary and Accounting subsystem context | Enterprise Architecture AI | STEP030205 Week 1-2 |
| **CRITICAL-GAP-002** | API Architecture | API Contract Specifications | Accounting APIs, GL APIs, reporting APIs | Integration Architecture AI | STEP030205 Week 2-3 |
| **CRITICAL-GAP-003** | API Security | API Security Architecture | Accounting data access controls, audit APIs | Security Architecture AI | STEP030205 Week 3-4 |
| **HIGH-GAP-004** | Data Isolation | Multi-Tenant Data Isolation | Accounting data isolation by tenant | Data Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-009** | RBAC | Access Control Matrix | GL clerk, manager, auditor roles | Security Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-010** | Governance | Data Ownership | GL ownership, finance data stewardship | Data Architecture AI | STEP030205 Week 1-2 |
| **HIGH-GAP-020** | ADR | Technology Stack | Accounting module tech decisions | Architecture Decision AI | STEP030205 Week 1-2 |
| **MEDIUM-GAP-015** | Infrastructure | Infrastructure Architecture | Accounting compute/storage requirements | Infrastructure Architecture AI | STEP030205 Week 4-5 |
| **MEDIUM-GAP-016** | Deployment | CI/CD Pipeline | Accounting module deployment stages | DevOps Architecture AI | STEP030205 Week 4-5 |
| **MEDIUM-GAP-017** | Observability | Observability Architecture | GL transaction logging/monitoring | Observability Architecture AI | STEP030205 Week 5-6 |
| **MEDIUM-GAP-018** | Backup/Recovery | Backup Strategy | GL backup and RTO/RPO requirements | DR Architecture AI | STEP030205 Week 5-6 |

### Module Dependencies

**External Dependencies**:
- GAP-001: None
- GAP-002: Requires GAP-001 (system context)
- GAP-003: Requires GAP-002 (API specs)
- All module gaps: Require foundational identity/access models (GAP-008)

**Internal Dependencies** (within Accounting module):
- Minimal — mostly independent design tracks
- RBAC (GAP-009) depends on Identity Model (GAP-008)

### Module Deliverables for Gate C

**Required for Gate C Passage**:
1. System Context Diagram v1.0 (GAP-001) ✓
2. Accounting APIs OpenAPI Spec v1.0 (GAP-002 — Accounting subset) ✓
3. API Security Architecture v1.0 (GAP-003) ✓
4. Data Isolation Strategy v1.0 (GAP-004) ✓
5. RBAC Matrix v1.0 — Finance roles (GAP-009) ✓

**Supporting Deliverables**:
- Technology Stack ADR v1.0 (GAP-020)
- Infrastructure Design v1.0 — Accounting requirements (GAP-015)

### Module Timeline — Phase 2

| Week | Activity | Owner | Deliverable |
|---|---|---|---|
| Week 1-2 | GAP-001, GAP-010, GAP-020 | Enterprise Architecture AI + Decision AI | Context diagram, data ownership, tech decisions |
| Week 2-3 | GAP-002 (Accounting), GAP-004, GAP-009 | Integration + Data + Security AI | API specs, isolation strategy, RBAC |
| Week 3-4 | GAP-003, GAP-008 refinement | Security AI + Identity AI | API security, IAM Accounting integration |
| Week 4-5 | GAP-015, GAP-016 | Infrastructure + DevOps AI | Infrastructure, CI/CD pipeline |
| Week 5-6 | GAP-017, GAP-018 | Observability + DR AI | Monitoring, backup strategy |

### Module Future Correction Path

**Module Gate C Readiness**:
- ✓ All CRITICAL gaps completed and reviewed
- ✓ All HIGH gaps completed and reviewed
- ✓ ChatGPT L99 independent review passed
- ✓ Boss Gate C passage decision for Accounting module

**Module Gate D Readiness** (Post-Build Phase):
- Implementation verification (coding phase)
- Integration testing for Accounting module
- Security/compliance testing
- Production readiness review

**Correction Trigger**: If Gate C review finds Accounting-specific gaps or rework, correction executes as dedicated STEP030206+ or STEP030207 execution package (module-specific, not architecture-wide).

---

## MODULE 2: HR MODULE — Business Process Module

### Module Scope

**Business Purpose**: Employee records, payroll, benefits, org structure, performance management  
**Baseline Status**: PARTIAL in source document baseline (Domain 10: 1 source; Domain 9: deferred to Phase 2)  
**Future Correction Path**: Dedicated STEP030206+ execution package  

### Module Gaps and Responsibilities

| Gap ID | Domain | Title | Scope | Owner | Phase 2 Target |
|---|---|---|---|---|---|
| **CRITICAL-GAP-001** | System Context | System Context Diagram | HR subsystem boundary and integrations | Enterprise Architecture AI | STEP030205 Week 1-2 |
| **CRITICAL-GAP-002** | API Architecture | API Contract Specifications | HR APIs, payroll APIs, org APIs | Integration Architecture AI | STEP030205 Week 2-3 |
| **CRITICAL-GAP-003** | API Security | API Security Architecture | HR data access, payroll security | Security Architecture AI | STEP030205 Week 3-4 |
| **HIGH-GAP-005** | Integration | Event Architecture | Employee events (hire/terminate/transfer) | Integration Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-006** | Integration | Integration Points | Payroll system integration, benefits integration | Integration Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-008** | IAM | Identity and Access Model | Employee directory, federated identity | Identity Architecture AI | STEP030205 Week 1-2 |
| **HIGH-GAP-009** | RBAC | Access Control Matrix | HR admin, manager, employee roles | Security Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-014** | Security | Security NFR | Employee data encryption, audit requirements | Security Architecture AI | STEP030205 Week 3-4 |
| **MEDIUM-GAP-015** | Infrastructure | Infrastructure Architecture | HR compute/storage, payroll processing | Infrastructure Architecture AI | STEP030205 Week 4-5 |
| **MEDIUM-GAP-019** | DR | Disaster Recovery Plan | HR data DR, payroll continuity | DR Architecture AI | STEP030205 Week 6 |
| **MEDIUM-GAP-021** | ADR | Data Model | Employee data model, benefits data model | Architecture Decision AI | STEP030205 Week 2-3 |

### Module Dependencies

**External Dependencies**:
- All HR gaps require GAP-001 (system context)
- GAP-002, GAP-003: Depend on system context
- GAP-008, GAP-009: Cross-module IAM dependencies

**Internal Dependencies** (within HR module):
- Event architecture (GAP-005) enables integration design (GAP-006)
- Identity model (GAP-008) foundational for RBAC (GAP-009)

### Module Deliverables for Gate C

**Required for Gate C Passage**:
1. System Context Diagram v1.0 (GAP-001) ✓
2. HR APIs OpenAPI Spec v1.0 (GAP-002 — HR subset) ✓
3. API Security Architecture v1.0 (GAP-003) ✓
4. Identity Architecture v1.0 (GAP-008) ✓
5. RBAC Matrix v1.0 — HR roles (GAP-009) ✓

**Supporting Deliverables**:
- Event Architecture Design v1.0 (GAP-005)
- Integration Patterns Guide v1.0 (GAP-006)
- Data Model ADR v1.0 (GAP-021)

### Module Timeline — Phase 2

| Week | Activity | Owner | Deliverable |
|---|---|---|---|
| Week 1-2 | GAP-001, GAP-008 | Enterprise Architecture AI, Identity AI | Context diagram, identity architecture |
| Week 2-3 | GAP-002, GAP-005, GAP-006, GAP-009, GAP-021 | Integration + Security AI + Decision AI | APIs, events, integration, RBAC, data model |
| Week 3-4 | GAP-003, GAP-014 | Security AI | API security, security NFR |
| Week 4-5 | GAP-015 | Infrastructure AI | Infrastructure |
| Week 6 | GAP-019 | DR AI | DR plan |

### Module Future Correction Path

**Correction Trigger**: HR-specific gaps or rework → STEP030206+ execution (module-scoped).  
**No Accounting Module Mixing**: HR design path independent from Accounting module path.

---

## MODULE 3: PURCHASE MODULE — Business Process Module

### Module Scope

**Business Purpose**: Vendor management, purchase orders, procurement, receipt, invoice matching  
**Baseline Status**: DEFERRED in baseline (Domain 9/10: not yet detailed)  
**Future Correction Path**: Dedicated STEP030206+ execution package  

### Module Gaps and Responsibilities

| Gap ID | Domain | Title | Scope | Owner | Phase 2 Target |
|---|---|---|---|---|---|
| **CRITICAL-GAP-001** | System Context | System Context Diagram | Purchase subsystem boundary | Enterprise Architecture AI | STEP030205 Week 1-2 |
| **CRITICAL-GAP-002** | API Architecture | API Contract Specifications | Purchase APIs, vendor APIs | Integration Architecture AI | STEP030205 Week 2-3 |
| **CRITICAL-GAP-003** | API Security | API Security Architecture | Purchase data access controls | Security Architecture AI | STEP030205 Week 3-4 |
| **HIGH-GAP-005** | Integration | Event Architecture | PO events, receipt events, invoice events | Integration Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-006** | Integration | Integration Points | Vendor system integration, logistics integration | Integration Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-009** | RBAC | Access Control Matrix | Procurement officer, manager, approver roles | Security Architecture AI | STEP030205 Week 2-3 |
| **MEDIUM-GAP-015** | Infrastructure | Infrastructure Architecture | Purchase processing infrastructure | Infrastructure Architecture AI | STEP030205 Week 4-5 |
| **MEDIUM-GAP-021** | ADR | Data Model | PO data model, vendor data model | Architecture Decision AI | STEP030205 Week 2-3 |
| **MEDIUM-GAP-022** | ADR | Communication Pattern | Purchase process messaging pattern | Architecture Decision AI | STEP030205 Week 3-4 |

### Module Dependencies

**External Dependencies**:
- All Purchase gaps require foundational architecture (GAP-001, GAP-008)

### Module Deliverables for Gate C

**Required for Gate C Passage**:
1. System Context Diagram v1.0 (GAP-001) ✓
2. Purchase APIs OpenAPI Spec v1.0 (GAP-002) ✓
3. API Security Architecture v1.0 (GAP-003) ✓
4. RBAC Matrix v1.0 — Procurement roles (GAP-009) ✓

### Module Future Correction Path

**No Mixing with Accounting or HR**: Purchase module design and corrections execute independently.

---

## MODULE 4: SALES MODULE — Business Process Module

### Module Scope

**Business Purpose**: Customers, sales orders, pricing, billing, revenue recognition  
**Baseline Status**: DEFERRED in baseline (Domain 9/10: not yet detailed)  
**Future Correction Path**: Dedicated STEP030206+ execution package  

### Module Gaps and Responsibilities

| Gap ID | Domain | Title | Scope | Owner | Phase 2 Target |
|---|---|---|---|---|---|
| **CRITICAL-GAP-001** | System Context | System Context Diagram | Sales subsystem boundary | Enterprise Architecture AI | STEP030205 Week 1-2 |
| **CRITICAL-GAP-002** | API Architecture | API Contract Specifications | Sales APIs, customer APIs, billing APIs | Integration Architecture AI | STEP030205 Week 2-3 |
| **CRITICAL-GAP-003** | API Security | API Security Architecture | Sales data access controls | Security Architecture AI | STEP030205 Week 3-4 |
| **HIGH-GAP-005** | Integration | Event Architecture | SO events, fulfillment events, billing events | Integration Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-009** | RBAC | Access Control Matrix | Sales rep, manager, billing roles | Security Architecture AI | STEP030205 Week 2-3 |
| **MEDIUM-GAP-015** | Infrastructure | Infrastructure Architecture | Sales order processing infrastructure | Infrastructure Architecture AI | STEP030205 Week 4-5 |
| **MEDIUM-GAP-021** | ADR | Data Model | Sales order data model, customer data model | Architecture Decision AI | STEP030205 Week 2-3 |

### Module Dependencies

**External Dependencies**:
- All Sales gaps require foundational architecture (GAP-001, GAP-008)

### Module Deliverables for Gate C

**Required for Gate C Passage**:
1. System Context Diagram v1.0 (GAP-001) ✓
2. Sales APIs OpenAPI Spec v1.0 (GAP-002) ✓
3. API Security Architecture v1.0 (GAP-003) ✓
4. RBAC Matrix v1.0 — Sales roles (GAP-009) ✓

---

## MODULE 5: INVENTORY MODULE — Business Process Module

### Module Scope

**Business Purpose**: Stock management, warehouse operations, inventory tracking, stock movements  
**Baseline Status**: DEFERRED in baseline (Domain 9/10: not yet detailed)  
**Future Correction Path**: Dedicated STEP030206+ execution package  

### Module Gaps and Responsibilities

| Gap ID | Domain | Title | Scope | Owner | Phase 2 Target |
|---|---|---|---|---|---|
| **CRITICAL-GAP-001** | System Context | System Context Diagram | Inventory subsystem boundary | Enterprise Architecture AI | STEP030205 Week 1-2 |
| **CRITICAL-GAP-002** | API Architecture | API Contract Specifications | Inventory APIs, stock APIs | Integration Architecture AI | STEP030205 Week 2-3 |
| **CRITICAL-GAP-003** | API Security | API Security Architecture | Inventory data access controls | Security Architecture AI | STEP030205 Week 3-4 |
| **HIGH-GAP-005** | Integration | Event Architecture | Stock move events, receipt events | Integration Architecture AI | STEP030205 Week 2-3 |
| **HIGH-GAP-009** | RBAC | Access Control Matrix | Warehouse operator, manager, auditor roles | Security Architecture AI | STEP030205 Week 2-3 |
| **MEDIUM-GAP-015** | Infrastructure | Infrastructure Architecture | Inventory processing infrastructure | Infrastructure Architecture AI | STEP030205 Week 4-5 |

### Module Dependencies

**External Dependencies**:
- All Inventory gaps require foundational architecture (GAP-001, GAP-008)

### Module Deliverables for Gate C

**Required for Gate C Passage**:
1. System Context Diagram v1.0 (GAP-001) ✓
2. Inventory APIs OpenAPI Spec v1.0 (GAP-002) ✓
3. API Security Architecture v1.0 (GAP-003) ✓
4. RBAC Matrix v1.0 — Warehouse roles (GAP-009) ✓

---

## CROSS-CUTTING ARCHITECTURE (Non-Module-Specific Gaps)

### Gaps Applicable to All Modules

These gaps are **foundational** and apply across all modules but are designed once (not per module):

| Gap ID | Title | Scope | Owner | Module Applicability |
|---|---|---|---|---|
| **CRITICAL-GAP-001** | System Context Diagram | Entire system context; modules context contained within | Enterprise Architecture AI | ALL MODULES |
| **CRITICAL-GAP-002** | API Contract Specifications | Foundation; module-specific APIs derived from this | Integration Architecture AI | ALL MODULES |
| **CRITICAL-GAP-003** | API Security Architecture | Foundation; applied to all module APIs | Security Architecture AI | ALL MODULES |
| **HIGH-GAP-007** | Tenant Isolation Strategy | Foundation; applied to all modules | Multi-Tenant Architecture AI | ALL MODULES |
| **HIGH-GAP-008** | Identity Architecture | Foundation; federated identity for all modules | Identity Architecture AI | ALL MODULES |
| **HIGH-GAP-011** | Performance NFR | Foundation; applied to all modules | NFR Architecture AI | ALL MODULES |
| **HIGH-GAP-012** | Scalability NFR | Foundation; applied to all modules | NFR Architecture AI | ALL MODULES |
| **HIGH-GAP-013** | Availability NFR | Foundation; applied to all modules | NFR Architecture AI | ALL MODULES |

---

## MODULE SEPARATION and Future Correction Rules

### No Module Mixing Principle

✓ **Accounting module design** is independent; future Accounting corrections execute as dedicated package  
✓ **HR module design** is independent; future HR corrections execute as dedicated package  
✓ **Purchase module design** is independent; future Purchase corrections execute as dedicated package  
✓ **Sales module design** is independent; future Sales corrections execute as dedicated package  
✓ **Inventory module design** is independent; future Inventory corrections execute as dedicated package  
✓ **Cross-cutting architecture** (foundational gaps) is common to all; corrections executed separately from module-specific work  

### Future Correction Trigger and Execution

**Scenario**: Gate C review finds Accounting module design gap or rework required.

**Correction Path**:
1. Identify gap as **Accounting-module-specific** vs. **cross-cutting**
2. If Accounting-specific: Schedule STEP030206+ execution package for Accounting module only
3. Do NOT re-execute HR, Purchase, Sales, or Inventory modules
4. Correction applies to Accounting module future design phases and implementation

**Example**: If Accounting GL design requires API revision, correction executes as Accounting module STEP030206 (not system-wide). Other modules' designs remain unaffected and proceed independently.

---

## Phase 2 Modular Timeline — Complete

| Phase | Week | Activity | Modules | Status |
|---|---|---|---|---|
| **Foundation** | Week 1-2 | System Context (GAP-001), Identity Architecture (GAP-008), Foundational ADRs | ALL | Parallel |
| **Module Design** | Week 2-3 | Module-specific APIs, RBAC, data models, integration | Accounting, HR, Purchase, Sales, Inventory | Parallel |
| **API Security** | Week 3-4 | API Security, Security NFR, module security details | ALL | Parallel |
| **Infrastructure** | Week 4-5 | Infrastructure design, CI/CD pipeline, observability | ALL | Parallel |
| **Finalization** | Week 5-6 | Backup/DR, risk register, evidence completeness | ALL | Serial |
| **Review & Gate C** | Week 6 | ChatGPT L99 independent review, Boss Gate C decision | ALL | Serial |

---

## Document Control

- **Document ID**: 39_STEP030211_PHASE_2_MODULAR_CARRY_FORWARD_PLAN
- **Version**: 1.0
- **Created**: 2026-07-19
- **Controlled Status**: MODULAR PLANNING RECORD
- **Classification**: /L99.99
- **Authority**: Boss Authorization (module separation required)
- **Archive**: Part of STEP030211 package

---

**STATUS**: ✓ PHASE 2 MODULAR CARRY-FORWARD PLAN COMPLETE  
**MODULES**: Accounting | HR | Purchase | Sales | Inventory | Cross-Cutting  
**NO MODULE MIXING — SEPARATION MAINTAINED FOR FUTURE CORRECTION**  
**ห้ามข้าม GATE** (Do Not Skip Gate)
