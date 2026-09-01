# Inventory CORR-005 Pre-Prompt Five-Unit Challenge

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Target: `TEAM A Inventory DR-002 Register Reconciliation + Independent Delta Review Preparation`  
Risk: `HIGH`  
Readiness: `READY`  
Boss decision: `APPROVED TO PROCEED`  
Date: `2026-09-01`

## Governing Inputs

- TEAM A Inventory DR-002 frozen commit: `b31597fafa318c2edd9047ad89c128e4ace2e7cb`
- Independent Review IER-003 frozen commit: `45c749eae826642872ccc2dc09f0f714932c5b8e`
- Boss Scope Ruling: `BOSS_INVENTORY_SCOPE_RULING_BH_EXCLUSION_AND_BRANCH_BASELINE_2026_09_01.md`
- CORR-004: `SUPERSEDED BEFORE EXECUTION`

## 1. Audit VETO — Evidence / Governance Challenge

Verdict: `NO VETO — PROCEED`

Questions resolved before prompt issuance:

- Is further H2 source research required? **No.** `bh_*` / `bhpro_*` are Boss-excluded from source learning.
- Is further H3 Branch architecture research required? **No.** Multi-Company / Multi-Branch is an approved platform baseline and downstream Inventory does not redefine it.
- May the reconciliation silently delete legacy/migration/TBRAC dependencies? **No.** Valid carry-forwards must remain explicit.
- May Team A turn scope exclusion into implementation proof? **No.** H2 is closed as an Inventory research blocker by scope decision, not proven as target logic.
- May Team A self-approve the Evidence Gate? **No.** Independent Delta Re-Review and Boss decision remain mandatory.

Audit requirement: preserve chronology and additive traceability. The old DR-002 and IER-003 artifacts remain frozen audit evidence.

## 2. TBRAC — Thailand Business Reality Challenge

Verdict: `PROCEED WITH CONTROLLED CARRY-FORWARD`

- H3 must no longer be phrased as an open question about whether SMEsPlus needs a Branch model.
- Legacy `branch` versus `company_registry` remains a migration-data mapping question only.
- Real-user validation remains legitimate only for identifying which legacy value was operationally trusted by the customer.
- Thai tax-document branch semantics remain an Accounting / Tax concern and must not be converted into Inventory architecture.
- No customer-specific or vendor-specific representation may be generalized to Thailand-wide truth.

## 3. EXPERT IBPV — Business Process / Design Challenge

Verdict: `PROCEED — NO ARCHITECTURE REOPENING`

- Inventory must preserve the approved Tenant / Company / Branch context at Warehouse / Location / Stock Truth interfaces.
- Inventory does not own the platform Branch definition.
- H2 does not define an Inventory business process; excluded vendor-specific Party/CRM structure may only survive as migration provenance if needed.
- Reconciliation must clearly separate Stock Truth evidence from Partner/CRM, Migration, SaaS, Accounting/Tax and TBRAC carry-forwards.

## 4. EXPERT IDTM — Future Testability Challenge

Verdict: `ADVISORY ONLY — PROCEED`

No formal IDTM execution occurs now. The reconciliation must preserve future-testable invariants such as:

- no cross-tenant or cross-company stock leakage;
- Warehouse/Location operations carry correct organizational context;
- cross-branch visibility/transfer rules are tested against the approved platform contract rather than inferred from legacy Branch fields.

No test oracle may be invented from excluded `bh_*` / `bhpro_*` logic.

## 5. EXPERT IESA — System Assurance Challenge

Verdict: `ADVISORY ONLY — PROCEED`

- Repeated downstream re-definition of Tenant / Company / Branch is itself an assurance risk; use the approved platform baseline.
- Excluded legacy modules must not contaminate canonical architecture.
- Controlled carry-forwards must remain visible to Migration, Accounting/Tax, SaaS and Real-User Validation workstreams.
- Inventory Gate readiness must be based on Inventory evidence completeness, not on forcing unrelated cross-domain dependencies to disappear.

## Consolidated Five-Unit Result

`UNANIMOUS DIRECTION: ACCEPT WITH CONTROLS`

`Critical Blocking Unknown Before Start: NONE`

`Prompt Readiness: READY`

Authorized next action:

`TEAM A DR-002 REGISTER RECONCILIATION + DELTA REVIEW PREPARATION ONLY`

Prohibited in the next session:

- full Inventory Deep Research repeat;
- any `bh_*` / `bhpro_*` source learning;
- Branch architecture research/redesign;
- Team B design;
- development;
- Evidence Gate self-approval;
- merge to `SMEsPlus`.

`Ask until materially clear — not until everyone agrees.`  
`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
