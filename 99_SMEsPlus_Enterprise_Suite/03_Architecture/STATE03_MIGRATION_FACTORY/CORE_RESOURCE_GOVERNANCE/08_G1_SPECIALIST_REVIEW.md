# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G1 — Specialist Review of Terminology & Invariants

Status: SPECIALIST REVIEW COMPLETE — INDEPENDENT CHALLENGE REQUIRED
Input: `07_G1_TERMINOLOGY_AND_INVARIANT_DRAFT.md`
Owner: SaaS Team under SMEs Core

## 1. Review Scope

Eight AI Expert Specialist units reviewed the G1 draft only for vocabulary/invariant correctness. No numerical sizing, commercial price, topology or production mechanism was approved.

## 2. Specialist Findings

### Platform / Infrastructure Architecture

PASS WITH CONDITIONS.

- Correct separation: Package != Tenant != Cell != Server != DB Host.
- Correct distinction between Headroom, Protection Limit and Failure Boundary.
- Required clarification: ENTERPRISE dedicated environment must remain mechanism-neutral; dedicated boundary does not necessarily mean one physical server.
- Required clarification: `Commercial Limit < Protection Boundary < Failure Boundary` must be evaluated per material resource dimension/policy, not as one universal scalar.

### Database Engineering & Performance

PASS WITH CONDITIONS.

- CRG-05/06/18 are structurally sound.
- CRG-07 modification is preferable to an absolute prohibition because exceptional binary-in-DB cases may exist, but exception proof must include transactional impact, backup/restore amplification, WAL/replication impact and maintenance headroom.
- `Failure Boundary` must include correctness/recoverability risk, not only latency or capacity exhaustion.

### SRE / Performance & Load Testing

PASS WITH CONDITIONS.

- Burst vs Sustained Heavy Workload separation is necessary.
- Headroom and Operating Reserve definitions are useful but must not be treated as evidence of sufficient reserve size.
- Exact relationship between commercial, protection and failure boundaries remains HOLD pending benchmark/stress/soak evidence.
- CRG-17 is mandatory and testable later.

### Security / Tenant Isolation

PASS WITH REQUIRED CONTROL.

- Tenant is the security boundary; Company cannot weaken it.
- Usage attribution must require trusted Tenant execution context before a usage fact becomes chargeable/evidence-bearing.
- Raw telemetry without provable Tenant attribution must not be promoted into Chargeable Usage.
- ENTERPRISE dedicated resources must preserve the same canonical Tenant identity/security semantics.

### FinOps / SaaS Cost Economics

PASS WITH CONDITIONS.

- Customer Logical Usage and Internal Physical Consumption are correctly separated.
- Cost-to-Serve must include non-sellable protection overhead for economic validation, but this overhead must not be represented as customer logical usage without an explicit commercial unit contract.
- Approximate Standard base price remains hypothesis only.
- Capacity Class cannot be inferred from organization size alone.

### Billing / Wallet / Metering Architecture

PASS WITH REQUIRED TERMINOLOGY NORMALIZATION.

- `Overage` is potentially misleading under prepaid governance. Primary canonical term should be `Additional Chargeable Usage`; `Overage` may remain only as a customer-facing synonym where contractually defined.
- Usage Ledger must be explicitly separated from statutory/accounting ledger.
- Chargeable Usage requires: Tenant attribution + normalized evidence + published unit/rule + entitlement evaluation + financial authorization.
- Forecasted bill/cost is informational and does not create unsecured debt.

### Product Package / Commercial Governance

PASS WITH CONDITIONS.

- Commercial Package and Capacity Class are correctly separated from Deployment Tier.
- Organization size may be a sales/sizing signal only.
- STANDARD package mobility can exist without changing Tier.
- Package naming cannot imply guaranteed CPU/RAM/server identity unless contractually/evidentially proven.

### Independent Architecture Audit Preparation

READY FOR CHALLENGE, NOT YET GATE PASS.

Pre-challenge concerns:
1. Protected Mode vs Hard Cap could still be misread as tenant-wide shutdown.
2. Operating Reserve could be misread as guaranteed continuity beyond safety.
3. `Usage Ledger` terminology may collide with accounting ledger semantics.
4. ENTERPRISE dedicated environment could be misread as one physical machine.
5. Commercial/Protection/Failure boundary relation must remain multidimensional.
6. The chargeable-usage promotion rule needs an explicit trusted-attribution prerequisite.

## 3. Specialist Correction Requirements Before G1 Freeze

SR-01 — Make `Additional Chargeable Usage` primary; demote `Overage` to optional contract language.

SR-02 — Define `Usage Ledger` as a non-statutory operational evidence ledger unless/until a separate accounting posting is created.

SR-03 — Add trusted Tenant attribution as a prerequisite for Normalized Usage Event and Chargeable Usage.

SR-04 — Clarify Hard Cap is resource/action-specific by default and does not imply total ERP lockout.

SR-05 — Clarify Operating Reserve cannot override technical safety/failure controls.

SR-06 — Clarify ENTERPRISE dedicated environment means dedicated resource/security/operational boundary, not necessarily one physical server/DB.

SR-07 — State commercial/protection/failure boundaries are dimension-specific and evidence-driven.

## 4. Specialist Review Disposition

`PASS WITH CORRECTIONS REQUIRED BEFORE INDEPENDENT RE-CHALLENGE`

No G1 pass is claimed by this review.
