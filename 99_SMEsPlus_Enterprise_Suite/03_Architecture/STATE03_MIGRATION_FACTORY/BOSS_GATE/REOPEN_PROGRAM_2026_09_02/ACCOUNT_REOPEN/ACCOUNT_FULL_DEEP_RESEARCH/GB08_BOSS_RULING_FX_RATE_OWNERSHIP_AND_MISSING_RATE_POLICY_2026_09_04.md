# GB-08 Boss Ruling — FX Rate Ownership & Missing Rate Policy

Date: 2026-09-04
Project: SMEsPlus ENTERPRISE SUITE
Program: `[SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001] Accounting Domain Full-Spectrum Deep Research Program / L9999.9999`
Wave: `ACCOUNT WAVE A — CORE LEDGER & CLOSING`
Decision Ref: `GB-08`
Decision Authority: `Boss — Sole Final Approver`
Status: `BOSS APPROVED — CANONICAL BUSINESS SEMANTIC`

## 1. Decision Summary

Boss approves the AGPO recommendation and freezes the following Business Semantics for SMEsPlus.

### R1 — FX Rate Ownership / Scope

`FX accounting rate is governed within Tenant context and resolved at Company accounting scope.`

Canonical rules:

1. Tenant is the security/customer boundary.
2. Company is the legal/accounting boundary.
3. FX rate resolution for accounting must execute under `Current Tenant + Current Company` context.
4. Branch does not own an independent accounting FX rate by default.
5. Branch inherits the Company's approved FX policy and rate context.
6. Cross-tenant FX rate access/resolution is prohibited.
7. Implicit cross-company FX rate substitution is prohibited unless explicitly governed by a future Boss-approved policy.
8. Reference implementation/version behavior is evidence only and is not the SMEsPlus design authority.

### R2 — Missing FX Rate Policy

`NO VALID FX RATE = NO FINANCIAL POSTING`

Canonical rules:

1. A foreign-currency financial transaction may not be posted without a valid approved FX rate required by the applicable policy.
2. Silent `1.0` fallback is prohibited.
3. Silent future-rate substitution is prohibited.
4. Missing required rate must BLOCK posting and surface an explicit `FX RATE REQUIRED` control state.
5. Posting may proceed only after the applicable approved rate is available and the transaction is revalidated.
6. Migration/opening processes may use controlled historical rates only with explicit provenance and policy authority.
7. Any exceptional override, if permitted by a future policy, must be explicit, authorized, reason-required, traceable, and auditable.

## 2. Canonical FX Invariants

### FX-INV-01 — Cross-Tenant Isolation
`Cross-Tenant FX Rate Access = PROHIBITED`

### FX-INV-02 — Cross-Company Substitution
`Cross-Company Rate Substitution = PROHIBITED unless explicitly governed`

### FX-INV-03 — Silent Missing-Rate Fallback
`Missing Required Rate Silent Fallback = PROHIBITED`

### FX-INV-04 — Posted FX Provenance
Every posted foreign-currency financial fact must preserve, at minimum:

- FX Rate
- Rate Date
- Rate Source
- Tenant Context
- Company Context
- Currency Pair
- Applicable Rate Type/Policy
- Provenance / Approval lineage where applicable

### FX-INV-05 — Historical Immutability
Changing FX master data after posting must not silently rewrite historical posted financial facts.

## 3. Canonical Rate Resolution Principle

Default accounting resolution principle:

`Current Tenant`
→ `Current Company`
→ `Applicable Currency Pair`
→ `Applicable Rate Type / Policy`
→ `Valid Approved Rate for Required Date/Period`
→ `Posting`

If no valid approved rate exists:

`BLOCK POSTING`

Prohibited implicit fallbacks include:

- another Tenant's rate
- another Company's rate
- arbitrary global/null-company rate
- future rate without an explicit approved policy
- silent `1.0`

## 4. Architectural Consequence

This Boss ruling freezes Business Semantics only.

It does NOT authorize implementation.

AAS+ may now design/revalidate, from first principles:

- FX Data Model
- Rate Ownership Model
- Rate Resolver
- Posting Guard
- Historical FX Snapshot / Provenance
- Exception / Override Control
- Audit Trail
- Migration / Opening Rate handling

All such design remains subject to the current Very Deep Research / 8-Criteria Universal Exit Constitution and downstream Boss gates.

## 5. GB-08 Disposition

`GB-08 BUSINESS DECISION = RESOLVED BY BOSS RULING`

However this ruling does NOT automatically close Account Wave A.

Wave A must still satisfy all remaining Very Deep Research exit criteria, including scope boundedness, method convergence, unknown exhaustion, tolerance-zero closure, contradiction closure, negative-claim control, two consecutive clean independent passes, and final knowledge package completeness.

Wave B must not start until Wave A receives the applicable Boss Final Research Gate decision.

## 6. Governance

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss is the sole Final Approver.`

Reference systems remain `REFERENCE / LEARNING / BENCHMARK ONLY`.
SMEsPlus remains a NEW 100% Clean-room SaaS ERP.
