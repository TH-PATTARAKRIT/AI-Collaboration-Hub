# [SMEPLUS-26-09-07-ACC-PHASE-S-REMEDIATION-002]
# CLAUDE NEW SESSION — PHASE S BOUNDED REMEDIATION BEFORE INDEPENDENT RC VERIFICATION
# /L99999.99999

## 0. PURPOSE

Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Boss: Sole Final Approver
Mode: NEW SESSION / CONTROLLED CONTINUATION / NO RESET / EVIDENCE-FIRST
Parent closeout branch: `audit/account-phase-s-final-closeout-2026-09-07-001`
Verified closeout state commit before this prompt: `09128a99550b1b92e4da09f181dad4799e2c9bd3`
Boss ruling to consume: `BOSS_DECISION_Q_BOSS_03_AND_INDEPENDENT_VERIFIER_APPOINTMENT_2026_09_07.md`

This is NOT a new research round.
This is NOT Phase SA.
This is NOT Functional Design.
This is NOT implementation.
This session exists only to prepare reproducible, frozen owner evidence so an independent verifier can run `RC-01` through `RC-06`.

Absolute rules:
- No Evidence = No Progress.
- Never Skip Gate.
- Do not restart L1.
- Do not mutate peer-owner evidence.
- Do not run or self-certify any `RC-*` challenge.
- Do not discharge Vetoes.
- Do not answer domain Boss decisions.
- Preserve superseded text and prior SHAs as lineage.

## 1. BOSS DECISIONS — BINDING

Consume without re-asking:
- `PHASE-S/Q-BOSS-01 = APPROVED` — bounded owner corrections authorized.
- `XRECON/Q-BOSS-01 (XRD-009) = NOT SATISFIED` — same-model verification does not satisfy structural independence.
- `PHASE-S/Q-BOSS-02 = APPROVED` — structural independence requires separate verifier, frozen evidence, read-only boundary, independent reproduction and independent publication.
- `Q-BOSS-03 = NO — DOCUMENTARY INSPECTION ALONE IS NOT SUFFICIENT FOR RC-05`.
- ChatGPT GPT-5.6 Sol is appointed independent verifier subject to per-repair eligibility.

## 2. PRE-FLIGHT — MUST VERIFY CURRENT REMOTE STATE

Before mutation:
1. Fetch `audit/account-phase-s-final-closeout-2026-09-07-001` and verify the current remote HEAD.
2. Read the final closeout artefacts at/after `09128a9` and the Boss ruling above.
3. Resolve the exact frozen correction refs created for P06 source, P06 IEV, P08 source, P08 IEV, P09 and P11. Do not infer names from memory; read the published closeout lineage.
4. Verify each frozen ref still points to the intended immutable commit.
5. Publish a pre-remediation freeze record before making any correction.

If any asserted SHA or ref is stale, classify the delta before proceeding. Do not silently substitute a newer head.

## 3. WORKSTREAM A — P11 `CO-F-01` PIN-HONOURING INSTRUMENT REPAIR

Known proven defect from closeout:
- P11 CORR3 intake/currentness instrument declares a pinned-SHA table but tree resolution uses floating `origin/<branch>` heads.
- The published floating-head run was reproduced exactly.
- A pin-honoured run produced a different member set.
- Prior re-pin work is behaviourally inert because the instrument does not consume its declared pins.

Required bounded correction:
1. Locate the exact instrument and every wrapper/runner that resolves peer trees.
2. Replace floating branch resolution with explicit immutable SHA resolution from the declared pin table.
3. Fail closed if a declared pin is missing, malformed, unresolved, or non-substantive where the governing control requires a substantive commit.
4. Publish the exact pin table used by the repaired run.
5. Execute the repaired instrument twice from clean state and prove byte-identical outputs for the same frozen inputs.
6. Add a failure control: intentionally alter one pin in a controlled copy and prove the output/input identity changes or the instrument fails closed.
7. Compare old floating-head output vs repaired pin-honoured output by member identity, not cardinality alone.
8. Re-state every P11 finding/conclusion whose truth depended on the old floating-head population. Do not widen beyond affected claim classes.
9. Preserve old instrument/output as superseded lineage; never rewrite the old evidence.

Required result: a new dedicated P11 remediation branch/ref and immutable correction SHA. Never push the repair back onto an old frozen evidence ref.

## 4. WORKSTREAM B — P11 `CO-F-02` STALE INBOUND NEGATIVES

Known defect:
- Two P11 inbound negative assertions are stale.
- P08's written notification existed before P11's first owner correction commit.

Required bounded correction:
1. Identify the two exact live assertions and their claim IDs/carriers.
2. Read the P08 notification at its immutable SHA.
3. Mark the stale negatives superseded/withdrawn in place on the new P11 remediation branch while preserving lineage.
4. Replace them only with statements supported by the actual notification and current P08 evidence.
5. Sweep the entire P11 package for equivalent wording/claim-class duplicates and report every occurrence.
6. Do not edit P08.

## 5. WORKSTREAM C — P08 REPRODUCIBILITY PACKAGE FOR `RC-05`

Boss ruling: documentary inspection alone is insufficient.

P08 must publish a verifier-consumable reproducibility package containing:
1. exact executable instrument or exact executable procedure used for the corrected balance/tolerance claims;
2. frozen reproducible input files or immutable evidence references that the independent verifier can access;
3. SHA-256 for each frozen input where files are used;
4. exact population, unit and denominator;
5. predicates for reporting-currency balance, stored balance and any related control measurement actually in RC-05 scope;
6. exact Decimal/tolerance semantics;
7. positive control;
8. negative control;
9. failure/discriminating control that proves the instrument can return a non-zero/contradictory outcome;
10. expected control behaviour documented before independent execution;
11. command line / invocation sequence and expected output schema;
12. immutable correction/evidence SHA.

Do NOT run `RC-05` as a challenge. This session may test that its own instrument executes, but such owner execution is preparation evidence only and cannot satisfy structural independence.

If primary database/extract evidence required for independent reproduction is absent from the repository/authorized evidence location, publish exactly:
`P08-RC05-PREP-C — MISSING REPRODUCIBLE PRIMARY INPUT`
and name the missing input. Do not substitute documentary inspection.

## 6. OTHER RC SURFACES

Do not redo already completed owner corrections without material delta.
Your duty for `RC-01`, `RC-02`, `RC-03`, `RC-04`, `RC-06` is only to verify that each challenge surface has:
- exact immutable SHA;
- exact bounded scope;
- required inputs accessible to the independent verifier;
- no moving-branch dependency;
- no missing notification/dependency that would make the challenge premature.

If missing, repair only the packaging/provenance defect required to make that RC executable. Do not run the challenge.

## 7. REQUIRED OUTPUTS

Publish on a NEW remediation branch, minimum:
- `00_PHASE_S_REMEDIATION_PRE_FREEZE.md`
- `01_P11_CO_F_01_PIN_INSTRUMENT_REPAIR.md`
- `02_P11_CO_F_02_STALE_INBOUND_REPAIR.md`
- `03_P08_RC05_REPRODUCIBILITY_PACKAGE.md`
- `04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md`
- `05_REMEDIATION_EVIDENCE_MANIFEST.md`
- `06_REMEDIATION_CHECKPOINT_REGISTER.md`
- `PHASE_S_REMEDIATION_AUTO_RESUME.md`

Each RC handoff row must include:
RC ID · owner · exact repair/correction SHA · exact files/surface · inputs · controls · expected challenge action · dependency · status.

## 8. STOP CONDITIONS

Stop only if:
- required evidence is genuinely inaccessible;
- a correction requires peer-owner mutation;
- a new material defect outside this bounded remit is proven;
- a Boss-only decision blocks all remaining lanes.

Otherwise continue autonomously until all verifier handoff surfaces are frozen.

## 9. PERMITTED TERMINAL STATES

- `REMEDIATION-A — ALL RC SURFACES FROZEN AND READY FOR INDEPENDENT VERIFIER`
- `REMEDIATION-B — BOUNDED MATERIAL DEFECT REMAINS`, exact item named
- `REMEDIATION-C — REQUIRED EVIDENCE UNAVAILABLE`, exact evidence named

None means Phase S PASS.
None means Veto discharged.
None means Boss closure.

At `REMEDIATION-A`, stop and return only the immutable verifier handoff matrix to the independent verification session.
