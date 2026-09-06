# [SMEPLUS-26-09-06-SAAS-CELL-001]
# BOSS DECISION — Core–Extension Boundary & Extensibility Architecture / L9999.9999

Project: SMEsPlus ENTERPRISE SUITE  
Date: 2026-09-06  
Boss: Sole Final Approver  
Jira: ERPPLUS-151  
Decision Status: APPROVED  
Mode: CONTINUATION / DELTA-FIRST / EVIDENCE-FIRST / CLEAN-ROOM / NO RESET

## 1. Decision

Boss APPROVES adding **Core–Extension Boundary & Extensibility Architecture** to the active `SAAS-CELL-001` architecture package.

This approval applies to the refined SMEsPlus-specific architecture, not to the source proposal verbatim.

## 2. Core Principle

SMEsPlus applies the Open-Closed Principle as follows:

> Core is open for extension through stable, published contracts, while extensions must not directly modify or weaken Core invariants.

This does NOT mean the Core can never evolve. Core evolution remains allowed through controlled product governance, material-delta review, compatibility control, migration control, evidence, and applicable gates.

## 3. Approved Layer Model

1. **SMEsPlus Core**
   - Domain logic
   - Standard business semantics
   - Core data models
   - State machines
   - Transaction integrity
   - Accounting/financial integrity
   - Tenant/company security boundaries
   - Authorization
   - Audit and reconciliation

2. **Stable Extension Contracts**
   - APIs
   - Domain events
   - Strategy interfaces
   - Controlled hooks/interceptors
   - Integration contracts

3. **Product Extension Layer**
   - Reusable, governed SMEsPlus extensions
   - Versioned and independently testable
   - No customer-specific Core fork

4. **Customer / External Extensions**
   - External integrations
   - Approved plugins where justified
   - BFF / sidecar / webhook consumers
   - Enterprise-specific controlled extensions where applicable

## 4. Non-Negotiable Extension Controls

Extensions MUST NOT weaken or bypass:

- Business Semantic Integrity
- Financial Integrity
- Transaction Integrity
- Tenant Isolation
- Company Boundary
- Authorization
- Audit Integrity
- Historical Integrity
- Reconciliation
- Upgrade / Compatibility Integrity

## 5. Event and Transaction Rules

Events do not replace Core transaction integrity.

Pattern:

`Request -> Controlled Policy/Validation Extension -> Core Transaction -> Commit -> Domain Event`

Rules:

- Before-processing extensions must be typed, deterministic, and controlled.
- Core owns material business invariants.
- Post-commit events represent facts that already occurred.
- Event subscribers must not rewrite finalized Core financial/stock/tax/audit facts.

## 6. Strategy / Dependency Injection Rules

Dependency Injection and Strategy patterns are approved only through explicit, whitelisted extension points.

They do NOT grant permission to replace arbitrary Core behavior.

Examples of more extensible areas may include:
- Pricing strategy
- Discount strategy
- Approval policy
- Numbering policy
- Integration provider
- Notification provider

Restricted/high-control areas include:
- Tax calculation
- Inventory valuation
- Posting
- COGS
- FX gain/loss
- Depreciation
- Reconciliation

Non-replaceable invariants include:
- Tenant isolation
- Double-entry integrity
- Audit trail
- Transaction atomicity
- Historical integrity
- Authorization boundary

## 7. Data Extension Rules

### 7.1 Extension Tables
Structured extension tables are allowed where justified, provided they preserve:
- tenant scope
- company scope where applicable
- Core object identity/reference
- extension version
- audit metadata
- lifecycle and referential integrity

### 7.2 JSONB / Metadata
JSONB or flexible metadata is permitted for non-critical extensible attributes.

It must NOT become the primary source of truth for material fields such as:
- Debit/Credit
- Financial amount
- Tax base
- Inventory quantity
- Cost
- Tenant identity
- Company identity
- Posting status
- Approval state
- Reconciliation keys

Material financial/transactional facts require typed, controlled schemas and integrity rules.

## 8. Standard vs Enterprise Extension Policy

### STANDARD
Preferred order:
`Configuration -> Policy -> Workflow -> Entitlement -> Master Data -> Reporting -> Approved Product Extension`

Standard must not become an arbitrary customer-plugin platform.

### ENTERPRISE
May support stronger controlled extension mechanisms, external services, and customer-specific integrations where justified by architecture, security, compatibility, SLA, and operational evidence.

No Enterprise extension may fork or directly mutate the shared Core product semantics.

## 9. Trust Classification

Extension trust generally increases in this direction:

`Configuration < Product Extension < Domain Event Consumer < Webhook/API < BFF < In-Process Plugin < Core Strategy Replacement`

Higher-trust mechanisms require stronger certification, testing, isolation, observability, rollback, and governance.

## 10. Contract Governance

Freeze the principle, not a single tool.

- Contract Testing = REQUIRED principle.
- Pact or equivalent tools = candidate mechanisms, not permanent constitutional mandates.
- No silent breaking change.
- Published contracts require compatibility management and controlled migration.
- Deprecation period is risk/consumer/SLA/release dependent; it is not fixed universally at 1–2 major releases.

Lifecycle:
`ACTIVE -> DEPRECATED -> MIGRATION AVAILABLE -> CONSUMER MIGRATED/VERIFIED -> END OF SUPPORT -> REMOVED`

## 11. Core Extension Constitution

CE-01  CORE MUST NOT CONTAIN CUSTOMER-SPECIFIC LOGIC.  
CE-02  EXTENSION MUST USE PUBLISHED CONTRACTS.  
CE-03  NO DIRECT CORE DATABASE PATCH.  
CE-04  EXTENSION MUST NOT BYPASS TENANT, COMPANY, SECURITY OR AUTHORIZATION BOUNDARIES.  
CE-05  EXTENSION MUST NOT BREAK FINANCIAL, TRANSACTION OR RECONCILIATION INVARIANTS.  
CE-06  FINALIZED BUSINESS FACTS CANNOT BE MUTATED BY EXTENSION.  
CE-07  CONTRACT CHANGES REQUIRE COMPATIBILITY + MIGRATION CONTROL.  
CE-08  STANDARD CUSTOMER VARIATION MUST PREFER CONFIGURATION OVER CODE.  
CE-09  IN-PROCESS EXTENSION = HIGH TRUST AND REQUIRES STRONGER CERTIFICATION.  
CE-10  CORE FORK PER CUSTOMER = PROHIBITED.  
CE-11  EXTENSION FAILURE MUST HAVE DEFINED FAILURE ISOLATION.  
CE-12  EVERY EXTENSION MUST BE VERSIONED, TESTABLE, AUDITABLE, OBSERVABLE AND REMOVABLE.

## 12. Technology Freeze Status

The following remain implementation candidates and are NOT frozen by this approval:

- Kafka
- RabbitMQ
- NATS
- specific DI container
- specific plugin framework
- Pact as the only contract-test tool
- JSONB as a universal extension mechanism
- 1:1 extension tables as a universal pattern
- Sidecar/BFF as mandatory architecture
- exact API versioning scheme
- microservices extraction strategy

## 13. Governance Effect

This Boss approval is now a controlled architecture input for `SAAS-CELL-001` and must be carried forward without reopening unless a material contradiction or new evidence is found.

No Team C / production authorization is created by this approval.  
No database topology is frozen by this approval.  
Boss remains sole Final Approver.
