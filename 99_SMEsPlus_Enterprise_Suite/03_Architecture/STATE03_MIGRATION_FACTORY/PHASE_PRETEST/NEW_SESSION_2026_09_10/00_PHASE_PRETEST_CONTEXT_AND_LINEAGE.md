# [SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]
# SMEsPlus PHASE PRE-TEST — NEW SESSION CONTEXT AND LINEAGE

Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Execution branch: `architecture/account-phase-pretest-new-session-2026-09-10-001`
Session scope: **PHASE PRE-TEST ONLY**
Boss: **SOLE FINAL APPROVER**
Date: `2026-09-10`

## 1. Why this session exists

This is the controlled successor to Phase SA. Its purpose is to prove that the cross-module architecture learned and synthesized in Phase SA is complete, testable, traceable and safe enough to hand to Functional Design.

This session does NOT restart Phase S and does NOT repeat Phase SA research. It consumes the Phase SA result as controlled input and challenges whether the resulting requirements, contracts, routing and controls can be expressed as an executable Pre-Test Matrix without inventing missing design.

Core working model:

`INPUT -> PROCESS -> OUTPUT -> DOWNSTREAM ROUTING -> NEXT MODULE INPUT`

For every scenario, the Pre-Test Matrix must also expose:

- Accounting consequence for every business flow;
- Inventory consequence whenever stock is involved;
- Manufacturing routing when production is required;
- Purchase routing when procurement or dropship is required;
- Tenant and Company boundary;
- approval/control boundary;
- audit/event/reversal/idempotency requirements;
- negative, exception and recovery paths.

## 2. Boss authority entering this phase

Boss granted:

`PRE-TEST ENTRY AUTHORIZATION = GRANT`

Authority record:
`SC-60_BOSS_PRETEST_ENTRY_AUTHORIZATION_2026_09_10.md`

Parent Phase SA readiness commit:
`fd4fa6f37acac21a9fc7182e939144b8c1f08afa`

Boss entry authorization commit:
`d5ad78184a527d3c973e154efb07e2a85f0ef48e`

This authorization permits Phase Pre-Test work only. It is not authorization for Functional Design, physical schema lock, application implementation, merge, release or deployment.

## 3. Canonical authority carried forward

The following are binding inputs unless superseded by explicit Boss authority with traceable evidence:

- `SC-AUTH-02 = Reading C`.
- `8C-CLARIFICATION-01 = APPROVED`.
- Phase SA -> Pre-Test is an **internal verification transition**, not an 8-Criteria Exit Gate.
- Module and State 8-Criteria gates remain where the approved clarification places them.
- Phase S is not reopened; only retrospective integrity reconciliation already performed is carried forward.
- Boss remains the sole Final Approver.

## 4. Phase SA status at handoff

Phase SA produced a `READY FOR PRE-TEST — INTERNAL VERIFICATION TRANSITION ONLY` result.

Carry forward exactly:

- `EC-04 = 0/3` tolerance-zero runtime closures;
- `EC-07 = 0/2` clean structurally independent passes;
- `6` vetoes in force, `0` discharged;
- B-7 package ready but waiting for an eligible structurally independent executor;
- AAS+ concurrence and limb-2 re-wording outstanding;
- Manufacturing veto not lifted;
- `6` Boss elections ready and held;
- `POH-D-02` withheld for missing Thai statutory evidence;
- `E2E-04 = NOT TRAVERSABLE`;
- `0/22` scenarios runtime-verified;
- 22 cross-module scenarios = `10/12/0` in the Phase SA disposition model;
- 18 E2E scenarios = `9/9/0` in the Phase SA disposition model;
- `0` Phase SA specification gaps owned by SMEs Core at handoff.

None of these values may be silently upgraded by entering Pre-Test.

## 5. What Pre-Test means

Pre-Test is a **pre-design verification phase**. It is intended to answer:

1. Is every required business scenario represented?
2. Is every input complete enough to drive an unambiguous process?
3. Is every process obligation traceable to Phase S/SA evidence or Boss authority?
4. Is every output explicit and sufficient for its downstream consumer?
5. Does each downstream module receive the information it actually needs?
6. Are accounting, inventory, manufacturing, purchase, tax and payment effects correctly routed?
7. Are Tenant/Company boundaries explicit?
8. Are exception, reversal, retry, cancellation, correction and recovery cases represented?
9. Are controls testable, with a defined expected result and evidence requirement?
10. Can Functional Design begin without inventing missing business semantics?

Pre-Test does NOT convert an unimplemented SMEsPlus system into runtime proof. Where actual execution requires future implementation, the matrix must classify the obligation honestly as execution-dependent and preserve it for the lawful proof point.

## 6. SMEs Core doctrine

The following doctrine is binding:

`Truth over Pass.`
`Evidence over Assumption.`
`Falsify before Accept.`
`Correct before Escalate.`
`No deadline can convert uncertainty into truth.`

Do not search for evidence to pass. Search for evidence strong enough to survive falsification.

## 7. Single-writer / collision control

There shall be one active Phase Pre-Test execution branch and one controlling session.

- This session is the controlling execution session.
- Other historical Phase S/SA sessions and branches are read-only lineage.
- Read-only specialist analysis may be used, but it must not write competing canonical artifacts.
- Any structurally independent B-7 review must be read-only against a frozen baseline and publish through its own independent evidence channel; it must not mutate this branch while the challenge is running.
- If concurrent canonical writers are detected, stop publication, reconcile lineage, and re-freeze before continuing.

## 8. Clean-room boundary

Reference ERP systems may be used only as evidence, learning, experiment or benchmark inputs.

Do not inherit vendor schema, ORM, state model, menu structure, UI or workflow by default.

The Pre-Test Matrix tests SMEsPlus business semantics and control requirements, not vendor parity.

## 9. Mandatory cross-module routing doctrine

For every scenario:

- **Accounting** is a universal downstream/control concern for business events that have accounting consequence.
- **Inventory** must be included whenever stock, quantity-on-hand, reservation, movement, valuation or availability is affected.
- **Manufacturing** must be included whenever production, BOM consumption, WIP, output, scrap, rework or capacity routing is required.
- **Purchase** must be included whenever procurement, replenishment, subcontracting or dropship is required.
- Other modules must be included according to the business nature and actual dependency.

No module may be tested in isolation if its output is an input to another module.

## 10. Test evidence classes

Every Pre-Test row must be classified as exactly one primary evidence class:

- `PTE-1 STATIC/SEMANTIC PROOF` — can be proven from approved requirement/contract evidence;
- `PTE-2 REFERENCE/EXPERIMENT PROOF` — can be explored in a non-authoritative reference/test system without treating the reference behavior as SMEsPlus design authority;
- `PTE-3 EXECUTION-DESIGN READY` — test procedure is complete but real SMEsPlus runtime execution requires future implementation;
- `PTE-4 EXTERNAL AUTHORITY DEPENDENCY` — requires AAS+, statutory, Business SME or other external authority;
- `PTE-5 BOSS AUTHORITY DEPENDENCY` — genuine Boss decision remains.

No `PTE-3`, `PTE-4` or `PTE-5` row may be mislabelled PASS.

## 11. B-7 independence rule

The current Claude Opus 5 execution body authored Phase SA artifacts and is not structurally independent for B-7 against that baseline.

B-7 must be executed by an eligible independent verifier under the approved independence controls. Same-session subagents and self-challenge do not qualify as structural independence.

The main Pre-Test session may prepare and route the B-7 pack, consume the returned findings, correct the canonical package, re-freeze, and re-route as required. It may not certify its own independence.

## 12. Terminal target

The target of this session is:

`PHASE PRE-TEST MATRIX COMPLETE / EVIDENCE-RECONCILED / READY FOR BOSS FUNCTIONAL-DESIGN ENTRY GATE`

This is not a promise to reach PASS. If falsification finds a material requirement, control, routing or evidence defect, correct it and repeat the affected verification before presenting the Boss Gate.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.