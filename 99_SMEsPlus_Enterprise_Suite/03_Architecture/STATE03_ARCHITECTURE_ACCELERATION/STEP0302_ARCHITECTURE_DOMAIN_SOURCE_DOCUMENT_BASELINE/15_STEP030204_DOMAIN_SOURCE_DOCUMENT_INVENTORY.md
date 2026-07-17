# [SMEPLUS-26-07-17-001] STEP030204 Domain Source Document Inventory

**Document ID:** STEP030204_DOMAIN_SOURCE_DOCUMENT_INVENTORY  
**Session ID:** SMEPLUS-26-07-17-001  
**Status:** EXECUTION  
**Control Level:** /L99.99  
**Inventory Date:** 2026-07-17  
**Execution Agent:** Claude Code  
**Accountable Owner:** PMO / Architecture Lead  

---

## Inventory Summary

| Domain | Title | Evidence Status | Count |
|---|---|---|---|
| Domain 2 | Architecture Principles, Standards and Governance | VERIFIED / DRAFT | 6 |
| Domain 4 | System Context and Solution Architecture | PARTIAL / DRAFT | 2 |
| Domain 9 | Application Architecture | MISSING | 0 |
| Domain 10 | Module Architecture | MISSING | 0 |
| Domain 12 | API and Integration Architecture | PARTIAL | 1 |
| Domain 13 | Data Flow and Event Architecture | PARTIAL | 1 |
| **TOTAL** | | | **10** |

---

## Domain 2 — Architecture Principles, Standards and Governance

### D2-001: Technology Stack Standard

| Field | Value |
|---|---|
| **Document Name** | TECHNOLOGY_STACK_STANDARD.md |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md` |
| **Version** | 1.0 |
| **Status** | Approved Baseline |
| **Document Owner** | SMEsPlus Architecture Office / Claude Code / ChatGPT |
| **Document Date** | 2026-07-06 |
| **Evidence Status** | VERIFIED |
| **Key Sections** | Core Architecture Principles, Technology Stack (Frontend, Backend, Database, Infrastructure), API Standards, DevOps and CI/CD, Testing Stack, Security Stack, AI Collaboration Standard, Naming Standards, Terminology Standard (Open ERP), Mandatory Technology Decision Rules |
| **Authority** | Boss Approved |
| **Relevant to STEP0302** | ✓ Yes (Architecture Principles, Standards, Governance) |
| **Gate Impact** | Foundational governance document — directly supports Gate B |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | VERIFIED — Approved baseline |

**Content Coverage:**
- ✓ SaaS-first architecture principles
- ✓ Multi-tenant by design principles
- ✓ API-first principles
- ✓ Open ERP canonical terminology
- ✓ Technology stack baseline
- ✓ Naming standards
- ✓ Mandatory decision rules
- ✓ Coding standards requirements

---

### D2-002: Architecture Governance Standard

| Field | Value |
|---|---|
| **Document Name** | ARCHITECTURE_GOVERNANCE_STANDARD.md |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/ARCHITECTURE_GOVERNANCE_STANDARD.md` |
| **Version** | v1.0 |
| **Status** | Approved |
| **Document Owner** | SMEsPlus Architecture Office / Liza |
| **Document Date** | 2026-07-05 |
| **Evidence Status** | VERIFIED |
| **Key Sections** | Architecture Principles (8 principles), Review Scope, Authority, Gate Rule, Correction Record (S02-FINAL-001) |
| **Authority** | Boss Approved |
| **Relevant to STEP0302** | ✓ Yes (Architecture Governance) |
| **Gate Impact** | Governance control document — directly supports Gate B |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | VERIFIED — Approved with correction record |

**Architecture Principles:**
- ✓ SaaS First
- ✓ Multi-Tenant by Design
- ✓ API First
- ✓ Security by Design
- ✓ Audit by Design
- ✓ Configuration over Customization
- ✓ Evidence-driven design
- ✓ Gate-controlled delivery

---

### D2-003: Enterprise Standards v0.1

| Field | Value |
|---|---|
| **Document Name** | SMEPLUS-ENTERPRISE-STANDARDS-v0.1.md |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Enterprise_Standards/SMEPLUS-ENTERPRISE-STANDARDS-v0.1.md` |
| **Version** | 0.1 |
| **Status** | DRAFT |
| **Document Owner** | SMEsPlus Architecture Office |
| **Document Date** | Not specified |
| **Evidence Status** | DRAFT |
| **Key Sections** | Rules (No Evidence = No Final Claim, No Requirement ID = No Jira Task, etc.), Standard Flow |
| **Authority** | Guidance document (not yet approved) |
| **Relevant to STEP0302** | ✓ Yes (Enterprise Standards) |
| **Gate Impact** | Supports foundational control principles — Gate B reference |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | DRAFT — Requires review and approval |

---

### D2-004: Architecture Review Gate (ARG)

| Field | Value |
|---|---|
| **Document Name** | ARCHITECTURE_REVIEW_GATE.md |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/ARCHITECTURE_REVIEW_GATE.md` |
| **Version** | Unknown (detailed procedures) |
| **Status** | CONTROLLED DRAFT |
| **Document Owner** | Architecture Office |
| **Document Date** | Not specified |
| **Evidence Status** | DRAFT |
| **Key Sections** | Gate Overview, Phase 1 (Proposal & Submission), Phase 2 (Initial Review), Phase 3 (Technical Review), Phase 4 (Architecture Review), Phase 5 (Executive Approval), Phase 6+ (Implementation phases), Submission format, Review checklist, Approval criteria |
| **Authority** | Governance control (draft) |
| **Relevant to STEP0302** | ✓ Yes (Governance control process) |
| **Gate Impact** | Defines gate process for STEP0302 and subsequent work |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | DRAFT — Detailed but not yet formally approved |

---

### D2-005: Clean Room Engineering Directive v1.0

| Field | Value |
|---|---|
| **Document Name** | SMEsPlus_Clean_Room_Engineering_Directive_v1.0.md |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Governance/SMEsPlus_Clean_Room_Engineering_Directive_v1.0.md` |
| **Version** | 1.0 |
| **Status** | APPROVED |
| **Document Owner** | SMEsPlus Architecture Office |
| **Document Date** | Not specified |
| **Evidence Status** | VERIFIED |
| **Key Sections** | Clean Room engineering rules, Business Concept → Business Rule → SMEsPlus Design → New Implementation flow |
| **Authority** | Boss Approved (referenced in ADR framework) |
| **Relevant to STEP0302** | ✓ Yes (Architecture principles and governance) |
| **Gate Impact** | Foundational control for implementation governance |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | VERIFIED — Approved baseline |

---

### D2-006: Architecture ADR Framework

| Field | Value |
|---|---|
| **Document Name** | ADR (Architecture Decision Records) Framework |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/ADR/` |
| **Version** | Multiple ADRs (ADR-0002 through ADR-0006) |
| **Status** | CONTROLLED DRAFT |
| **Document Owner** | SMEsPlus Architecture Office |
| **Document Date** | Various (2026-07) |
| **Evidence Status** | DRAFT |
| **Key Sections** | ADR-0002: Evidence-Driven Functional Specification, ADR-0003: As-Is Before-To-Be Functional Design, ADR-0004: Accounting Thailand Localization Scope, ADR-0005: Clean Room Engineering Directive, ADR-0006: Clean Room Learning Directive v2 Policy A |
| **Authority** | Governance control (ADRs are active but not yet finalized) |
| **Relevant to STEP0302** | ✓ Yes (Architecture Decision Records framework) |
| **Gate Impact** | Defines ADR process and existing decisions |
| **Commit SHA** | Available in Git history per file |
| **Evidence Requirement** | DRAFT — Active framework, requires finalization |

---

## Domain 4 — System Context and Solution Architecture

### D4-001: Business Capability Model v0.1

| Field | Value |
|---|---|
| **Document Name** | SMEPLUS-BUSINESS-CAPABILITY-MODEL-v0.1.md |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_Architecture_Office/Reference_Architecture/SMEPLUS-BUSINESS-CAPABILITY-MODEL-v0.1.md` |
| **Version** | 0.1 |
| **Status** | DRAFT |
| **Document Owner** | SMEsPlus Architecture Office |
| **Document Date** | Not specified |
| **Evidence Status** | DRAFT |
| **Key Sections** | Capability Groups (12 groups: SaaS, IAM, CRM, Sales, Procurement, Inventory, Manufacturing, Accounting, HR, Services, Documents, Executive) |
| **Authority** | Reference architecture (not yet approved) |
| **Relevant to STEP0302** | ✓ Yes (System Context and Solution Architecture) |
| **Gate Impact** | Supports Gate B baseline architecture |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | DRAFT — Requires expansion and approval |

---

### D4-002: Architecture Scope V2

| Field | Value |
|---|---|
| **Document Name** | STATE03_ARCHITECTURE_SCOPE_V2.md |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/STATE03_ARCHITECTURE_SCOPE_V2.md` |
| **Version** | 2 |
| **Status** | CONTROLLED BASELINE DRAFT |
| **Document Owner** | SMEsPlus Architecture Office |
| **Document Date** | 2026-07-10 |
| **Evidence Status** | DRAFT |
| **Key Sections** | 24 Architecture Domains (Groups A-D), Immediate Work Authorized, Work Requiring Prior Gate Decision, Mandatory Working Conditions, GitHub Evidence Rule, Role Separation, Supersession Rule |
| **Authority** | Architecture control (approval pending) |
| **Relevant to STEP0302** | ✓ Yes (System Context and Solution Architecture scope) |
| **Gate Impact** | Defines scope for STATE03 work including Domain 4 |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | DRAFT — Requires independent review and Boss approval |

---

## Domain 9 — Application Architecture

| Field | Value |
|---|---|
| **Evidence Status** | MISSING |
| **Count** | 0 documents |
| **Description** | No authoritative source document exists for Application Architecture (application decomposition, bounded contexts, integration points) |
| **Gap Impact** | CRITICAL — Cannot baseline Domain 9 without authoritative source document |
| **Conflict** | None identified yet |
| **Action Required** | Application Architecture deliverable must be created and approved before Domain 9 can be verified |

---

## Domain 10 — Module Architecture

| Field | Value |
|---|---|
| **Evidence Status** | MISSING |
| **Count** | 0 documents |
| **Description** | No authoritative source document exists for Module Architecture (module boundaries, module dependencies, functional module structure) |
| **Gap Impact** | CRITICAL — Cannot baseline Domain 10 without authoritative source document |
| **Conflict** | None identified yet |
| **Action Required** | Module Architecture deliverable must be created and approved before Domain 10 can be verified |

---

## Domain 12 — API and Integration Architecture

### D12-001: Technology Stack Standard (API Section)

| Field | Value |
|---|---|
| **Document Name** | TECHNOLOGY_STACK_STANDARD.md (Section 5: API Standard) |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md` |
| **Version** | 1.0 |
| **Status** | Approved Baseline |
| **Document Owner** | SMEsPlus Architecture Office / Claude Code / ChatGPT |
| **Document Date** | 2026-07-06 |
| **Evidence Status** | VERIFIED (partial) |
| **Key Sections** | Backend API Stack (FastAPI, Python 3.12, REST API, OpenAPI/Swagger), API Standard (default REST, JSON, Bearer Token, standard response format, naming standards, API examples) |
| **Authority** | Boss Approved |
| **Relevant to STEP0302** | ✓ Yes (API and Integration Architecture) |
| **Gate Impact** | Foundational for API contracts — supports Gate B |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | VERIFIED for API standards portion — but missing detailed API contract definitions |

**Gap:** Detailed API contracts, integration patterns, and event-driven integration architecture are not yet documented.

---

## Domain 13 — Data Flow and Event Architecture

### D13-001: Technology Stack Standard (Event Processing Section)

| Field | Value |
|---|---|
| **Document Name** | TECHNOLOGY_STACK_STANDARD.md (Section 11: Messaging and Event Processing) |
| **Repository Path** | `99_SMEsPlus_Enterprise_Suite/00_PROJECT_STANDARD/TECHNOLOGY_STACK_STANDARD.md` |
| **Version** | 1.0 |
| **Status** | Approved Baseline |
| **Document Owner** | SMEsPlus Architecture Office / Claude Code / ChatGPT |
| **Document Date** | 2026-07-06 |
| **Evidence Status** | VERIFIED (partial) |
| **Key Sections** | Messaging and Event Processing (Redis Streams initial, RabbitMQ/Kafka future, immutable events, event publishing, critical events with retry and dead-letter handling) |
| **Authority** | Boss Approved |
| **Relevant to STEP0302** | ✓ Yes (Data Flow and Event Architecture) |
| **Gate Impact** | Foundational for event architecture — supports Gate B |
| **Commit SHA** | Available in Git history |
| **Evidence Requirement** | VERIFIED for event processing standards portion — but missing detailed data flow diagrams and event topic definitions |

**Gap:** Detailed data flow diagrams, event topic catalog, event contracts, and event-driven topology are not yet documented.

---

## Summary of Evidence Status

| Status | Count | Details |
|---|---|---|
| **VERIFIED** | 4 | Technology Stack Standard v1.0, Architecture Governance Standard v1.0, Clean Room Engineering Directive v1.0, and partial API/Event sections |
| **DRAFT** | 5 | Enterprise Standards v0.1, Architecture Review Gate, Business Capability Model v0.1, Architecture Scope V2, ADR Framework |
| **PARTIAL** | 2 | Domain 12 (API - partial sections), Domain 13 (Events - partial sections) |
| **MISSING** | 2 | Domain 9 (Application Architecture), Domain 10 (Module Architecture) |
| **TOTAL** | **10** | |

---

## Inventory Notes

1. **No Evidence = No Progress:** Domains 9 and 10 cannot be baselined without authoritative source documents.

2. **Partial Evidence Requires Expansion:** Domains 12 and 13 have foundational sections but require detailed specifications (API contracts, event topics, data flow diagrams).

3. **Clean Room Rule:** All architecture work follows the rule: Business Concept → Business Rule → SMEsPlus Design → New Implementation. This rule is documented in ADR-0005 and D2-005.

4. **Open ERP Terminology:** Technology Stack Standard (D2-001) explicitly mandates "Open ERP" as the canonical term for all SMEsPlus architecture and design documents.

5. **Gate Control:** All source documents support STATE03 Gate model (Gate A, B, C, D). No domain has passed a gate.

---

**Evidence Base:** GitHub repository commit history  
**Gate Status:** PARTIAL_EVIDENCE on Gate A, HOLD on Gates B, C, D  
**Next Step:** 16_STEP030204_SOURCE_TO_DOMAIN_TRACEABILITY_MATRIX.md

---

*No Evidence = No Progress*  
*ห้ามข้าม Gate*
