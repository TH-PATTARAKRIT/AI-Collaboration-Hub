# STEP030204 — Domain Source Document Inventory

**Session ID:** SMEPLUS-26-07-17-001  
**Execution Date:** 2026-07-17  
**Owner:** PMO / Architecture Lead  
**Reviewer:** ChatGPT /L99.99  
**Status:** BASELINE ESTABLISHED  

---

## 1. Inventory Rules

This inventory records **authoritative source documents** that exist in the repository and provide evidence, requirements, or baseline material for each of the six approved Domains. 

**Criteria for inclusion:**
- Document exists in repository with committed evidence
- File path, version, and timestamp are recorded
- Owner/author and reviewer are identifiable
- Document status is clearly stated (Draft, Published, Superseded, etc.)
- Relevance to one or more of the six approved Domains is explicit

**Explicit exclusions:**
- Chat-only outputs (no repository evidence)
- Temporary/local-only work
- Unverified or speculative material
- Documents for domains outside the six approved

**Canonical terminology:**
- "Open ERP" (not "Odoo", "ERPNext", or other specific systems) for enterprise resource planning system references

---

## 2. Inventory by Domain

### **DOMAIN 2: Architecture Principles, Standards and Governance**

#### Source Documents

| # | Document Name | File Path | Version | Type | Owner | Date | Commit/PR | Evidence Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| D2-001 | SMEPLUS Enterprise Architecture Standards v0.1 | `00_Architecture_Office/Enterprise_Standards/SMEPLUS-ENTERPRISE-STANDARDS-v0.1.md` | v0.1 | Markdown + PDF | Architecture Office | 2026-07-10 | COMMITTED | PUBLISHED / BASELINE | Authoritative governance standards for Open ERP architecture |
| D2-002 | Architecture Review Gate v0.1 | `00_Architecture_Office/Review_Checklists/SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md` | v0.1 | Markdown + PDF | Architecture Office | 2026-07-10 | COMMITTED | PUBLISHED / BASELINE | Review gate criteria and checklist for architecture approval |
| D2-003 | SMEsPlus Clean Room Learning Directive v2.0 | `00_Architecture_Office/Governance/SMEsPlus_Clean_Room_Learning_Directive_v2.0.md` | v2.0 | Markdown | Architecture Office | 2026-07-10 | COMMITTED | PUBLISHED / BASELINE | Clean Room principle for architecture learning from existing systems |
| D2-004 | SMEsPlus Clean Room Engineering Directive v1.0 | `00_Architecture_Office/Governance/SMEsPlus_Clean_Room_Engineering_Directive_v1.0.md` | v1.0 | Markdown | Architecture Office | 2026-07-10 | COMMITTED | PUBLISHED / BASELINE | Clean Room engineering approach for designing new architecture |
| D2-005 | ADR-0006 Clean Room Learning Directive Policy A | `00_Architecture_Office/ADR/ADR-0006-CLEAN-ROOM-LEARNING-DIRECTIVE-V2-POLICY-A.md` | Final | Markdown | Architecture Office | 2026-07-10 | COMMITTED | PUBLISHED / APPROVED | Boss-approved clean room policy |
| D2-006 | ADR-0005 Clean Room Engineering Directive | `00_Architecture_Office/ADR/ADR-0005-CLEAN-ROOM-ENGINEERING-DIRECTIVE.md` | Final | Markdown | Architecture Office | 2026-07-10 | COMMITTED | PUBLISHED / APPROVED | Boss-approved engineering directive |
| D2-007 | Architecture Domain Owner Matrix | `03_Architecture/00_Architecture_Governance/ARCHITECTURE_DOMAIN_OWNER_MATRIX.md` | Active Assignment | Markdown | PMO Evidence AI Owner | 2026-07-10 | COMMITTED | ACTIVE / BASELINE | Governance matrix assigning domain ownership and review responsibility |
| D2-008 | Architecture Gate Model | `03_Architecture/00_Architecture_Governance/ARCHITECTURE_GATE_MODEL.md` | Controlled Baseline | Markdown | Architecture Governance AI Owner | 2026-07-10 | COMMITTED | PUBLISHED / BASELINE | Gate sequencing and approval model |
| D2-009 | STATE03 Architecture Scope V2 | `03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Controlled Baseline Draft | Markdown | Architecture Governance AI Owner | 2026-07-10 | COMMITTED | DRAFT / HOLD | Approved scope for State 03 architecture work |

**Domain 2 Inventory Summary:**
- **Total Documents:** 9 authoritative sources
- **Published/Approved:** 7
- **Draft/Hold:** 2
- **Evidence Status:** ✅ COMPLETE for domain governance structure

---

### **DOMAIN 4: System Context and Solution Architecture**

#### Source Documents

| # | Document Name | File Path | Version | Type | Owner | Date | Commit/PR | Evidence Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| D4-001 | SMEPLUS Functional Architecture Design PDF | `02_Functional_Design/SMEPLUS Functional Architecture Design.pdf` | v0.1 | PDF | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Functional design providing context for system architecture |
| D4-002 | SMEsPlus SaaS Foundation Functional Design Specification | `02_Functional_Design/SMEsPlus SaaS Foundation Functional Design Specification.pdf` | v0.1 | PDF | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | SaaS foundation context and requirements |
| D4-003 | SMEPLUS Business Capability Model v0.1 | `00_Architecture_Office/Reference_Architecture/SMEPLUS-BUSINESS-CAPABILITY-MODEL-v0.1.md` | v0.1 | Markdown + PDF | Architecture Office | 2026-07-10 | COMMITTED | PUBLISHED / BASELINE | Business context and capability mapping for solution design |
| D4-004 | iTEST02 Functional Design Index | `02_Functional_Design/02_Functional_Design/00_iTEST02_FUNCTIONAL_DESIGN_INDEX.md` | Final | Markdown | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Comprehensive index of iTEST02 functional baseline (1,395 tables, 5,141 FK) |
| D4-005 | STATE03 Architecture Scope V2 (partial) | `03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Controlled Baseline Draft | Markdown | Architecture Governance AI Owner | 2026-07-10 | COMMITTED | DRAFT / HOLD | Scope document includes system context requirements |
| D4-006 | Architecture Decision Records Index | `03_Architecture_Decisions/03_Architecture_Decisions/00_iTEST02_ADR_INDEX.md` | Draft for review | Markdown | ADR Governance AI Owner | 2026-07-02 | COMMITTED | DRAFT | ADR conversion from iTEST02 database analysis (6 ADRs) |

**Domain 4 Inventory Summary:**
- **Total Documents:** 6 authoritative sources
- **Published/Approved:** 4
- **Draft/Hold:** 2
- **Evidence Status:** ⚠️ PARTIAL — System context requires detailed solution architecture documentation

---

### **DOMAIN 9: Application Architecture**

#### Source Documents

| # | Document Name | File Path | Version | Type | Owner | Date | Commit/PR | Evidence Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| D9-001 | SMEPLUS Enterprise Suite Functional Architecture Design | `02_Functional_Design/SMEPLUS Functional Architecture Design.pdf` | v0.1 | PDF | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Application layering and functional boundaries |
| D9-002 | ACC-001 Accounting Thailand Functional Design Specification Package | `02_Functional_Design/ACC-001 Accounting Thailand Functional Design Specification Package.md` | v1.0 | Markdown | Functional Architecture | 2026-07-10 | COMMITTED | PUBLISHED / BASELINE | Application module design for accounting domain |
| D9-003 | ACC-002 Functional Design Specification | `02_Functional_Design/ACC-002 Functional Design Specification.md` | v0.1 | Markdown | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Application module design document |
| D9-004 | ACC-003 Functional Design Specification | `02_Functional_Design/ACC-003 Functional Design Specification.md` | v0.1 | Markdown | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Application module design document |
| D9-005 | ACC-004 Functional Design Specification | `02_Functional_Design/ACC-004 Functional Design Specification.md` | v0.1 | Markdown | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Application module design document |
| D9-006 | ACC-005 Functional Design Specification | `02_Functional_Design/ACC-005 Functional Design Specification.md` | v0.1 | Markdown | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Application module design document |
| D9-007 | iTEST02 Functional Design Assumptions | `02_Functional_Design/02_Functional_Design/iTEST02_functional_design_assumptions.md` | Final | Markdown | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Application design assumptions from iTEST02 baseline |
| D9-008 | iTEST02 Functional Design Governance Flow Diagram | `02_Functional_Design/02_Functional_Design/iTEST02_functional_design_governance_flow_diagram.md` | Final | Markdown | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Application governance and workflow architecture |
| D9-009 | iTEST02 Data Governance Controls | `02_Functional_Design/02_Functional_Design/iTEST02_data_governance_controls.md` | Final | Markdown | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Application-level data governance requirements |
| D9-010 | iTEST02 Sensitive Data Risk Report | `02_Functional_Design/02_Functional_Design/iTEST02_sensitive_data_risk_report.md` | Final | Markdown | Security Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Application security and data protection requirements |

**Domain 9 Inventory Summary:**
- **Total Documents:** 10 authoritative sources
- **Published/Approved:** 10
- **Draft/Hold:** 0
- **Evidence Status:** ✅ COMPLETE — Comprehensive functional baseline for application architecture

---

### **DOMAIN 10: Module Architecture**

#### Source Documents

| # | Document Name | File Path | Version | Type | Owner | Date | Commit/PR | Evidence Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| D10-001 | iTEST02 Module Inventory | `02_Functional_Design/02_Functional_Design/iTEST02_module_inventory.csv` | Final | CSV | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Authoritative inventory of Open ERP modules (1,395 tables mapped to modules) |
| D10-002 | iTEST02 Functional Design Index (module catalog) | `02_Functional_Design/02_Functional_Design/00_iTEST02_FUNCTIONAL_DESIGN_INDEX.md` | Final | Markdown | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Module catalog with boundary definitions |
| D10-003 | iTEST02 ERD Accounting Finance | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_Accounting_Finance.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Accounting module entity relationship design |
| D10-004 | iTEST02 ERD HR Payroll | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_HR_Payroll.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | HR/Payroll module entity relationship design |
| D10-005 | iTEST02 ERD Inventory Purchase | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_Inventory_Purchase.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Inventory/Purchase module entity relationship design |
| D10-006 | iTEST02 ERD Sales CRM | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_Sales_CRM.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Sales/CRM module entity relationship design |
| D10-007 | SMEsPlus SaaS Foundation Functional Design | `02_Functional_Design/SMEsPlus SaaS Foundation Functional Design Specification.pdf` | v0.1 | PDF | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Foundation module requirements and architecture |
| D10-008 | Purchase Module Functional Requirement Catalog | `17_Functional_Specification_Factory/02_Purchase/Purchase Module Functional Requirement Catalog v0.1.pdf` | v0.1 | PDF | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Purchase module requirements specification |
| D10-009 | module_tier_catalog.yml | `17_Functional_Specification_Factory/config/module_tier_catalog.yml` | v0.1 | YAML | Functional Architecture | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Module tier classification and dependency model |
| D10-010 | iTEST02 Module Owner Signoff Matrix | `04_Review_Gates/04_Review_Gates/iTEST02_module_owner_signoff_matrix.csv` | Final | CSV | Governance AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Module ownership assignment and review matrix |

**Domain 10 Inventory Summary:**
- **Total Documents:** 10 authoritative sources
- **Published/Approved:** 10
- **Draft/Hold:** 0
- **Evidence Status:** ✅ COMPLETE — Comprehensive module architecture baseline from iTEST02

---

### **DOMAIN 12: API and Integration Architecture**

#### Source Documents

| # | Document Name | File Path | Version | Type | Owner | Date | Commit/PR | Evidence Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| D12-001 | SMEPLUS API Mapping Standard | `99_SMEsPlus_Enterprise_Suite/API_MAPPING_STANDARD.md` | v0.1 | Markdown | Integration Architecture AI Owner | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Standard for API design and mapping across Open ERP modules |
| D12-002 | MODULE SPEC API GATEWAY | `99_SMEsPlus_Enterprise_Suite/MODULE_SPEC_API_GATEWAY.md` | v0.1 | Markdown | API Architecture AI Owner | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | API Gateway specification for integration point design |
| D12-003 | OPENAPI FOUNDATION v0.1.yaml | `01_SaaS_Foundation/API/OPENAPI_FOUNDATION_v0.1.yaml` | v0.1 | YAML | API Architecture AI Owner | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Foundation API specification in OpenAPI 3.0 format |
| D12-004 | iTEST02 ADR-002 Domain-based ERD and Migration Slicing | `03_Architecture_Decisions/03_Architecture_Decisions/iTEST02_ADR-002.md` | Final | Markdown | ADR Governance AI Owner | 2026-07-02 | COMMITTED | PUBLISHED | ADR for domain-based API boundary design |
| D12-005 | iTEST02 ADR-006 Integration and Event Architecture | `03_Architecture_Decisions/03_Architecture_Decisions/00_iTEST02_ADR_INDEX.md` (Integration reference) | Draft | Markdown | Event Architecture AI Owner | 2026-07-02 | COMMITTED | DRAFT | Reference to event architecture in ADR index |
| D12-006 | iTEST02 Sensitive Data Risk Report (API context) | `02_Functional_Design/02_Functional_Design/iTEST02_sensitive_data_risk_report.md` | Final | Markdown | Security Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED | API security and data exposure requirements |

**Domain 12 Inventory Summary:**
- **Total Documents:** 6 authoritative sources
- **Published/Approved:** 5
- **Draft/Hold:** 1
- **Evidence Status:** ⚠️ PARTIAL — API Gateway architecture is defined but requires detailed integration patterns documentation

---

### **DOMAIN 13: Data Flow and Event Architecture**

#### Source Documents

| # | Document Name | File Path | Version | Type | Owner | Date | Commit/PR | Evidence Status | Notes |
|---|---|---|---|---|---|---|---|---|---|
| D13-001 | iTEST02 Functional Design Assumptions (data flow context) | `02_Functional_Design/02_Functional_Design/iTEST02_functional_design_assumptions.md` | Final | Markdown | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Data flow and event assumptions from functional design |
| D13-002 | iTEST02 ERD Accounting Finance (data model) | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_Accounting_Finance.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Accounting data flow and relationships |
| D13-003 | iTEST02 ERD HR Payroll (data model) | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_HR_Payroll.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | HR/Payroll data flow and relationships |
| D13-004 | iTEST02 ERD Inventory Purchase (data model) | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_Inventory_Purchase.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Inventory/Purchase data flow and relationships |
| D13-005 | iTEST02 ERD Sales CRM (data model) | `02_Functional_Design/02_Functional_Design/iTEST02_ERD_Sales_CRM.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Sales/CRM data flow and relationships |
| D13-006 | iTEST02 Data Governance Controls | `02_Functional_Design/02_Functional_Design/iTEST02_data_governance_controls.md` | Final | Markdown | Data Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Data governance framework for data flow architecture |
| D13-007 | iTEST02 Functional Design Governance Flow Diagram | `02_Functional_Design/02_Functional_Design/iTEST02_functional_design_governance_flow_diagram.md` | Final | Markdown | Functional Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Process and data flow governance architecture |
| D13-008 | iTEST02 ADR-002 Domain-based Migration Slicing | `03_Architecture_Decisions/03_Architecture_Decisions/iTEST02_ADR-002.md` | Final | Markdown | ADR Governance AI Owner | 2026-07-02 | COMMITTED | PUBLISHED | ADR for data flow boundary and event slicing |
| D13-009 | OPENAPI FOUNDATION v0.1.yaml (event/webhook context) | `01_SaaS_Foundation/API/OPENAPI_FOUNDATION_v0.1.yaml` | v0.1 | YAML | API Architecture AI Owner | 2026-06-15 | COMMITTED | PUBLISHED / BASELINE | Foundation API includes event/webhook patterns |
| D13-010 | iTEST02 Sensitive Data Risk Report (data flow security) | `02_Functional_Design/02_Functional_Design/iTEST02_sensitive_data_risk_report.md` | Final | Markdown | Security Architecture AI Owner | 2026-06-28 | COMMITTED | PUBLISHED / BASELINE | Data flow security and privacy requirements |

**Domain 13 Inventory Summary:**
- **Total Documents:** 10 authoritative sources
- **Published/Approved:** 10
- **Draft/Hold:** 0
- **Evidence Status:** ✅ COMPLETE — Comprehensive data flow and event architecture baseline

---

## 3. Overall Inventory Summary

| Domain | Count | Published | Draft | Status |
|---|---|---|---|---|
| Domain 2 (Governance) | 9 | 7 | 2 | ✅ COMPLETE |
| Domain 4 (System Context) | 6 | 4 | 2 | ⚠️ PARTIAL |
| Domain 9 (Application) | 10 | 10 | 0 | ✅ COMPLETE |
| Domain 10 (Module) | 10 | 10 | 0 | ✅ COMPLETE |
| Domain 12 (API Integration) | 6 | 5 | 1 | ⚠️ PARTIAL |
| Domain 13 (Data Flow/Event) | 10 | 10 | 0 | ✅ COMPLETE |
| **TOTAL** | **51** | **46** | **5** | **BASELINE ESTABLISHED** |

---

## 4. Inventory Status Interpretation

**✅ Complete Domains (4 of 6):**
- Domain 2 (Governance): Full governance framework established
- Domain 9 (Application): Comprehensive functional and application architecture
- Domain 10 (Module): Complete module structure and ERD artifacts
- Domain 13 (Data Flow/Event): Complete data model and flow documentation

**⚠️ Partial Domains (2 of 6) — Require Follow-up:**
- Domain 4 (System Context): Functional basis exists but requires explicit system context and solution architecture documentation
- Domain 12 (API Integration): API standards and gateway defined but requires detailed integration patterns and service contracts

---

## 5. No Evidence = No Progress

**Sources NOT found in inventory (gaps for Domain 4 and 12):**
- Explicit System Context Diagram (currently in functional form)
- High-level Solution Architecture decision record
- Detailed API Integration Pattern Catalog
- Message/Event Broker Architecture specification
- Service Contract templates

These gaps are **recorded in the Conflict and Gap Register** (file 17).

---

**Inventory Completion:** CONFIRMED  
**Date:** 2026-07-17  
**Status:** READY FOR TRACEABILITY MATRIX

---

**Next Step:** Execute 16_STEP030204_SOURCE_TO_DOMAIN_TRACEABILITY_MATRIX.md
