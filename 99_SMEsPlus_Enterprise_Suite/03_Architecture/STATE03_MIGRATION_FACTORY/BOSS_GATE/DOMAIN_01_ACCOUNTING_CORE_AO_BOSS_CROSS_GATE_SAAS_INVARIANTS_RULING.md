# DOMAIN_01 Accounting Core — Boss Ruling: Cross-Gate SaaS Invariants for Thailand COA Closure

Date: 2026-08-30
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain: DOMAIN_01 — Accounting Core
Workstream: Thailand COA Architecture Closure
Jira: ERPPLUS-132
Control Level: /L99.99
Final Approval Authority: Boss

## 1. Boss Decision

**APPROVED — CROSS-GATE SAAS INVARIANTS SHALL APPLY TO EVERY COA CLOSURE GATE.**

Reason: SMEsPlus is being designed as a SaaS ERP platform. SaaS tenancy, isolation, canonical identity, template immutability, upgrade control and localization boundaries must therefore constrain the work from COA-G01 onward; they must not be deferred until COA-G04S.

COA-G04S remains the dedicated deep-design and verification Gate for SaaS COA architecture. This ruling does not mark COA-G04S as executed or passed.

## 2. Mandatory Cross-Gate SaaS Invariants

The following invariants are mandatory across COA-G01, G02, G03, G04, G04S, G05, G06, G07 and G08:

- **SI-01 — Tenant context is mandatory.**
- **SI-02 — Company context is mandatory where company-scoped.**
- **SI-03 — Standard Template is not tenant-owned mutable data.**
- **SI-04 — Tenant customization cannot modify the published Standard Template.**
- **SI-05 — Account Code / Name is not canonical identity.**
- **SI-06 — Published Template Version is immutable.**
- **SI-07 — Upgrade is explicit, previewable and auditable.**
- **SI-08 — No cross-tenant COA access.**
- **SI-09 — Company customization must preserve canonical reporting semantics.**
- **SI-10 — SaaS Core must not hard-code Thailand-specific source architecture.**

## 3. Cross-Gate Enforcement Rule

Every COA Gate artifact and Gate Report shall include an explicit `SAAS INVARIANT COMPLIANCE` section or matrix covering SI-01 through SI-10.

For each invariant, the Gate must record:

- applicability to the Gate;
- evidence location;
- owner / owner role;
- reviewer / verifier;
- verification status;
- conflict / exception if any;
- Gate impact.

Allowed verification status:

- `PASS / VERIFIED`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN`
- `N/A — JUSTIFICATION REQUIRED`

`N/A` is not automatic. It requires a documented reason showing why that invariant is not materially exercised by the specific Gate.

## 4. Audit Veto Rule

A Gate MUST NOT be declared PASS, FROZEN, READY FOR HANDOFF, or COMPLETE if an applicable SaaS Invariant is violated or lacks the evidence required for that Gate.

Mandatory effect:

`Applicable SI violation -> Gate = FAIL / FROZEN`

`Applicable SI evidence missing -> Gate = HOLD`

No downstream Gate may use a known invariant violation as accepted architecture debt unless Boss explicitly issues a separate controlled exception ruling.

## 5. Gate-Specific Minimum Interpretation

### COA-G01 — Source Baseline Reconciliation

Source evidence must be classified without turning source-system tenant/company assumptions or Thailand-specific vendor structure into SMEsPlus SaaS Core architecture. Account Code / Name must remain source-facing attributes, not canonical identity.

### COA-G02 — Base COA Kernel Discovery

Base Kernel candidates must be expressed as SaaS-safe canonical business/accounting concepts and must not depend on one Tenant's codes, names, groups or mutable company configuration as identity.

### COA-G03 — AI Semantic Consolidation

Consolidation decisions must preserve tenant/company boundaries, canonical identity and reporting semantics. Similar source names/codes across tenants must not be treated as shared identity by default.

### COA-G04 — Account Type & Account Group Architecture

Company-maintainable Account Groups and Posting Accounts must remain separate from platform-controlled canonical meaning and Account Type. Company customization must not rewrite the published Standard Template.

### COA-G04S — SaaS COA Architecture

This remains the dedicated Gate for full evidence of tenancy, isolation, provisioning, template/instance separation, versioning, customization boundaries, upgrade/delta handling, permissions, audit history, migration compatibility and reporting continuity.

### COA-G05 — Financial Statement Taxonomy

Company-specific customization must still map to canonical financial-statement semantics. Financial-statement classification must not depend solely on mutable Company Account Group or Account Code.

### COA-G06 — Thailand Tax Accounting Controls

Thailand localization rules may be implemented through a controlled localization layer/profile, but SaaS Core must not hard-code Thailand-specific source architecture. Tenant/company isolation remains mandatory for tax-related accounting data and configuration.

### COA-G07 — Multi-company & Dimension Proof

Evidence must explicitly test tenant isolation, company isolation, company customization, dimensions and canonical reporting continuity. Cross-tenant access is a hard failure.

### COA-G08 — Independent Audit + PMO + Boss Freeze

The final audit package must include a complete SI-01..SI-10 compliance matrix. Any unresolved applicable invariant prevents Final COA Freeze and downstream handoff.

## 6. Relationship to COA-G04S

Cross-Gate SaaS Invariants are **guardrails from G01 onward**.

COA-G04S is the **dedicated deep-design / verification Gate**.

Therefore:

`Cross-Gate Invariants != COA-G04S completion`

and

`COA-G04S authorization != COA-G04S PASS`.

## 7. Authority Boundaries

This ruling changes governance and architecture controls only.

Development Authorization = **NOT GRANTED**.
Production Authorization = **NOT GRANTED**.
Physical database implementation = **NOT AUTHORIZED BY THIS RULING**.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
