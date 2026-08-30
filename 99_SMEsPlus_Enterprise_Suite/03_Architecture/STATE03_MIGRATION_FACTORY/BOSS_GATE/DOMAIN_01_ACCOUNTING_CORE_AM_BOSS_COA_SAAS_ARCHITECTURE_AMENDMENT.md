# DOMAIN_01 Accounting Core — Boss Architecture Amendment: COA + SaaS Architecture Mandatory Gate

Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 — Accounting Core
Workstream: Thailand COA Architecture Closure
Jira: ERPPLUS-132
Control Level: /L99.99
Final Approval Authority: Boss

## 1. Boss Decision

**APPROVED — ADD `COA-G04S — SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture` AS A MANDATORY COA CLOSURE GATE.**

Reason recorded by Boss: SMEsPlus is being designed as a SaaS platform; COA architecture must therefore explicitly define SaaS tenancy, provisioning, versioning, upgrade and customization behaviour before financial-statement mapping and final COA freeze.

This is an architecture amendment to the previously approved COA closure sequence. Historical records are preserved; they are not rewritten to imply that COA-G04S existed before this Boss approval.

## 2. Revised Gate Sequence

1. COA-G01 — Source Baseline Reconciliation
2. COA-G02 — Base COA Kernel Discovery
3. COA-G03 — AI Semantic Consolidation
4. COA-G04 — Account Type & Account Group Architecture
5. **COA-G04S — SaaS COA Tenancy, Provisioning, Versioning & Upgrade Architecture**
6. COA-G05 — Financial Statement Taxonomy
7. COA-G06 — Thailand Tax Accounting Controls
8. COA-G07 — Multi-company & Dimension Proof
9. COA-G08 — Independent Audit + PMO Verification + Boss Final COA Freeze

`COA-G04S` blocks COA-G05 and all later freeze activities.

## 3. Mandatory COA-G04S Scope

COA-G04S must define and evidence at least:

- Tenant isolation
- Company isolation
- Standard Thai COA Template vs Company COA Instance separation
- COA provisioning for new Tenant / Company
- Standard COA Template versioning
- Company/Tenant customization boundary
- Controlled template upgrade / delta handling
- Backward compatibility
- Canonical account identity independent from account code
- Company-maintainable Account Group behaviour
- Multi-company sharing / separation rules
- Role and permission boundary for COA maintenance
- Audit / change history
- Migration mapping compatibility
- Canonical reporting continuity after customization or upgrade

## 4. SaaS COA Architecture Principle

Target conceptual flow:

`SMEsPlus SaaS Platform`
` -> Thailand Localization Profile`
` -> Standard Thai COA Template`
` -> Template Version`
` -> Tenant`
` -> Company COA Instance`
` -> Company-maintainable Account Groups`
` -> Company Posting Accounts`
` -> Dimensions`
` -> Canonical Financial Statement Mapping`

The Standard Thai COA Template must not be treated as a single live record set whose direct modification silently changes every Tenant.

Required upgrade principle:

`Template Version Change -> Compatibility Assessment -> Tenant Delta Analysis -> Upgrade Preview -> Controlled Apply -> Audit Evidence`

No automatic destructive overwrite of Tenant/Company customizations is authorized by this amendment.

## 5. Change Classification Requirement

COA template changes shall be classifiable for downstream design as:

- MANDATORY — statutory / system-control driven
- RECOMMENDED — SMEsPlus standard improvement
- OPTIONAL — industry / business extension

Exact implementation fields or database schema remain outside this Gate unless separately authorized.

## 6. COA-G04S Exit Criteria

COA-G04S may be proposed for closure only when evidence supports:

- Standard COA Template Model = VERIFIED
- Tenant/Company Instance Model = VERIFIED
- Provisioning Model = VERIFIED
- Customization Boundary = VERIFIED
- Versioning Model = VERIFIED
- Upgrade/Delta Model = VERIFIED
- Tenant Isolation = VERIFIED
- Company Isolation = VERIFIED
- Multi-company Behaviour = VERIFIED
- Canonical Identity / Account Code Independence = VERIFIED
- Canonical Reporting Continuity = VERIFIED
- Migration Mapping Compatibility = VERIFIED
- Blocking SaaS COA Unknowns = 0

COA-G04S PASS does not self-authorize COA-G05; Gate movement still follows project governance.

## 7. Existing COA Rules Preserved

This amendment does not change these approved controls:

- SMEsPlus Local Thailand = 19 ACTIVE Account Types.
- Off-Balance Sheet remains excluded from ordinary Balance Sheet/P&L totals by default.
- Account Group may be maintainable by Company but must not silently redefine Account Type or canonical accounting meaning.
- `389 source rows != 389 SMEsPlus target accounts`.
- `~32 Base Kernel` remains a working expectation only; exact count = TBD / EVIDENCE REQUIRED.
- Account Code is not canonical identity.
- Dimension-over-Account-Proliferation remains the default where accounting treatment is materially equivalent.
- Clean-room boundary remains absolute.

## 8. Authority Boundary

This amendment authorizes COA + SaaS architecture work only.

Development Authorization = NOT GRANTED.
Production Authorization = NOT GRANTED.
Database implementation = NOT AUTHORIZED BY THIS AMENDMENT.
Downstream implementation from an unfrozen COA = NOT AUTHORIZED.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
