# STEP030204 Domain Source Document Inventory

**Prompt ID:** SMEPLUS-26-07-17-001  
**Status:** EVIDENCE INVENTORY — FORMAL BASELINE  
**Control Level:** /L99.99  
**Effective Date:** 2026-07-17  
**Data Collection Date:** 2026-07-17  

---

## Document Inventory Structure

All source documents are catalogued with:
- **File:** Absolute path in repository
- **Section:** Relevant section(s) within document
- **Source Path:** GitHub path for traceability
- **Version:** Document version or commit reference
- **Owner:** Author or accountable AI/human
- **Date:** Creation/approval date
- **Evidence:** Commit SHA, PR reference, or Jira ID
- **Status:** Verified / Draft / Superseded / Conflicting / Unverified

---

## DOMAIN 2: Architecture Principles, Standards and Governance

### 2.1 Governance Framework

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 2.1.1 | SMEPLUS Architecture Review Gate Standard | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Review_Checklists/SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md` | Enterprise Architecture | v0.1 | Unknown | DRAFT | Control gate definition |
| 2.1.2 | Architecture Review Gate | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/ARCHITECTURE_REVIEW_GATE.md` | Architecture Governance | Current | Unknown | VERIFIED | Gate model and criteria |
| 2.1.3 | Architecture Domain Owner Matrix | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/ARCHITECTURE_DOMAIN_OWNER_MATRIX.md` | PMO | Current | 2026-07-10 | ACTIVE | Governance control matrix |
| 2.1.4 | State 03 Architecture Scope V2 | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Enterprise Architecture | v2 | 2026-07-10 | CONTROLLED | Approved scope and conditions |

### 2.2 Governance Standards

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 2.2.1 | Architecture Document Template | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/ARCHITECTURE_DOCUMENT_TEMPLATE.md` | Architecture Governance | Current | Unknown | VERIFIED | Document control standard |
| 2.2.2 | Enterprise Standards | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Enterprise_Standards/SMEPLUS-ENTERPRISE-STANDARDS-v0.1.md` | Enterprise Governance | v0.1 | Unknown | DRAFT | Standards baseline |
| 2.2.3 | GitHub-Jira Sync Control | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/GITHUB_JIRA_SYNC_CONTROL.md` | PMO | Current | Unknown | VERIFIED | Integration control |

### 2.3 Design Principles and Directives

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 2.3.1 | Clean Room Learning Directive v2.0 | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/SMEsPlus_Clean_Room_Learning_Directive_v2.0.md` | Architecture Governance | v2.0 | Unknown | VERIFIED | Learning methodology |
| 2.3.2 | Clean Room Engineering Directive v1.0 | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/SMEsPlus_Clean_Room_Engineering_Directive_v1.0.md` | Architecture Governance | v1.0 | Unknown | VERIFIED | Engineering control |
| 2.3.3 | ADR-0005: Clean Room Engineering | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/ADR/ADR-0005-CLEAN-ROOM-ENGINEERING-DIRECTIVE.md` | Architecture Decision | v1 | Unknown | VERIFIED | Architecture decision record |
| 2.3.4 | ADR-0006: Clean Room Learning v2 | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/ADR/ADR-0006-CLEAN-ROOM-LEARNING-DIRECTIVE-V2-POLICY-A.md` | Architecture Decision | v2 | Unknown | VERIFIED | Policy architecture record |

### 2.4 Conflict and Assumption Register

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 2.4.1 | Authority Conflict Register | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/State_02_Governance/STATE02_AUTHORITY_CONFLICT_REGISTER_v1.1.md` | Governance Authority | v1.1 | Unknown | VERIFIED | Conflict tracking |

---

## DOMAIN 4: System Context and Solution Architecture

### 4.1 System Context and Boundaries

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 4.1.1 | Business Capability Model | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Reference_Architecture/SMEPLUS-BUSINESS-CAPABILITY-MODEL-v0.1.md` | Enterprise Architecture | v0.1 | Unknown | DRAFT | Business context definition |
| 4.1.2 | Architecture Scope V2 | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Enterprise Architecture | v2 | 2026-07-10 | CONTROLLED | Context and scope boundaries |
| 4.1.3 | Architecture Document Template | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/ARCHITECTURE_DOCUMENT_TEMPLATE.md` | Architecture Governance | Current | Unknown | VERIFIED | Template includes system context |

### 4.2 Solution Architecture

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 4.2.1 | Architecture Decisions (iTEST02 ADR Index) | `99_SMEsPlus_Enterprise_Suite/03_Architecture_Decisions/03_Architecture_Decisions/00_iTEST02_ADR_INDEX.md` | Architecture Decision | Current | Unknown | DRAFT | Solution decisions register |
| 4.2.2 | Technology Stack Standard | `99_SMEsPlus_Enterprise_Suite/00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md` | Architecture | Standard | Unknown | VERIFIED | Technology selection policy |

### 4.3 Reference Architecture

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 4.3.1 | Reference Architecture README | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Reference_Architecture/README.md` | Enterprise Architecture | Current | Unknown | DRAFT | Architecture reference framework |

---

## DOMAIN 9: Application Architecture

### 9.1 Application Structure and Decomposition

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 9.1.1 | SaaS Foundation UX - Module Activation | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/UX/ModuleActivation.md` | Application Architecture | Draft | Unknown | DRAFT | Application modularity concept |
| 9.1.2 | SaaS Foundation UX - Integration Center | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/UX/IntegrationCenter.md` | Application Architecture | Draft | Unknown | DRAFT | Application integration concept |
| 9.1.3 | SaaS Foundation UX - Audit Governance | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/UX/AuditGovernance.md` | Application Architecture | Draft | Unknown | DRAFT | Application audit and governance |
| 9.1.4 | Module Specification - API Gateway | `99_SMEsPlus_Enterprise_Suite/MODULE_SPEC_API_GATEWAY.md` | Application Architecture | v1 | Unknown | DRAFT | API Gateway application design |

### 9.2 Design Patterns

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 9.2.1 | Design Patterns README | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Design_Patterns/README.md` | Architecture Governance | Current | Unknown | DRAFT | Design pattern catalog |

---

## DOMAIN 10: Module Architecture

### 10.1 Module Definition and Boundaries

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 10.1.1 | Module Specification - API Gateway | `99_SMEsPlus_Enterprise_Suite/MODULE_SPEC_API_GATEWAY.md` | Module Architecture | v1 | Unknown | DRAFT | Gateway module specification |
| 10.1.2 | SaaS Foundation - Module Activation | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/UX/ModuleActivation.md` | Module Architecture | Draft | Unknown | DRAFT | Module activation pattern |

### 10.2 Module Dependencies

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 10.2.1 | Architecture Scope V2 (Modules section) | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Enterprise Architecture | v2 | 2026-07-10 | CONTROLLED | Module boundary analysis authorized |

---

## DOMAIN 12: API and Integration Architecture

### 12.1 API Strategy and Design

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 12.1.1 | API Mapping Standard | `99_SMEsPlus_Enterprise_Suite/API_MAPPING_STANDARD.md` | Integration Architecture | Standard | Unknown | VERIFIED | API mapping policy |
| 12.1.2 | Module Specification - API Gateway | `99_SMEsPlus_Enterprise_Suite/MODULE_SPEC_API_GATEWAY.md` | Integration Architecture | v1 | Unknown | DRAFT | API Gateway design |
| 12.1.3 | Architecture Scope V2 (API section) | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Enterprise Architecture | v2 | 2026-07-10 | CONTROLLED | API architecture concept authorized |

### 12.2 Integration Patterns

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 12.2.1 | SaaS Foundation UX - Integration Center | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/UX/IntegrationCenter.md` | Integration Architecture | Draft | Unknown | DRAFT | Integration pattern design |
| 12.2.2 | GitHub-Jira Sync Control | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/GITHUB_JIRA_SYNC_CONTROL.md` | PMO | Current | Unknown | VERIFIED | Integration governance |

---

## DOMAIN 13: Data Flow and Event Architecture

### 13.1 Data Flow Patterns

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 13.1.1 | Architecture Scope V2 (Data Flow section) | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Enterprise Architecture | v2 | 2026-07-10 | CONTROLLED | Data flow concept authorized |
| 13.1.2 | SaaS Foundation UX - Module Activation | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/UX/ModuleActivation.md` | Integration Architecture | Draft | Unknown | DRAFT | Module data flow pattern |

### 13.2 Event Architecture

| # | Document | File Path | Owner | Version | Date | Evidence Status | Notes |
|---|----------|-----------|-------|---------|------|-----------------|-------|
| 13.2.1 | Architecture Scope V2 (Event section) | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` | Enterprise Architecture | v2 | 2026-07-10 | CONTROLLED | Event architecture concept authorized |
| 13.2.2 | Integration Center (Events) | `99_SMEsPlus_Enterprise_Suite/01_SaaS_Foundation/UX/IntegrationCenter.md` | Integration Architecture | Draft | Unknown | DRAFT | Event integration pattern |

---

## Source Document Summary

| Status | Count | Details |
|--------|-------|---------|
| **VERIFIED** | 7 | Authoritative, approved governance documents |
| **CONTROLLED** | 4 | Baseline documents under active control |
| **ACTIVE** | 2 | Currently maintained and referenced |
| **DRAFT** | 17 | Preparation phase, not yet finalized |
| **UNVERIFIED** | 0 | No documents lack ownership/dating |
| **SUPERSEDED** | 0 | No obsolete versions identified yet |
| **CONFLICTING** | 0 | No contradictions identified yet |
| **MISSING** | Multiple | See GAP REGISTER (Document 17) |
| **TOTAL CATALOGUED** | 30 | Across six approved domains |

---

## Inventory Verification Rules

**A source document is AUTHORITATIVE when:**

1. ✓ File path is recorded in this inventory
2. ✓ Owner or author is identified
3. ✓ Version or commit reference is recorded
4. ✓ Creation/approval date is documented
5. ✓ GitHub evidence path is provided
6. ✓ Status is marked (Verified / Draft / Controlled / etc.)
7. ✓ Domain mapping is established in Traceability Matrix (Document 16)

**A source document is NOT AUTHORITATIVE when:**

- ✗ File path is unrecorded
- ✗ Author is unknown or undocumented
- ✗ Version is unmarked
- ✗ Date is missing
- ✗ Domain mapping is not established
- ✗ Status remains "Unknown" or "Unverified"

**Evidence Status Definitions:**

- **VERIFIED:** Document reviewed and approved by Owner
- **CONTROLLED:** Document is current baseline under active governance
- **ACTIVE:** Document is in use and maintained
- **DRAFT:** Document is preparation phase, not finalized
- **UNVERIFIED:** Document exists but status unknown
- **SUPERSEDED:** Document is obsolete, replaced by newer version
- **CONFLICTING:** Document contradicts other authoritative source

---

## Inventory Control

**Document:**  
`15_STEP030204_DOMAIN_SOURCE_DOCUMENT_INVENTORY.md`

**Status:** BASELINE INVENTORY COMPLETE  
**Owner:** PMO / Architecture Lead  
**Reviewer:** To be assigned  
**Approval:** Pending Boss review  
**Last Updated:** 2026-07-17  
**Commit:** [TO BE RECORDED]

**No Evidence = No Progress**
