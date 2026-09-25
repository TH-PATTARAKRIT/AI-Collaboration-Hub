---
name: smesplus-vdr-controller
description: Govern SMEsPlus Very Deep Research (VDR) end to end. Use for SMEsPlus L1-L12 research, canonical function/question/VDR-target universe construction, denominator reconciliation or freeze review, evidence and proof validation, runtime/configuration reachability, 96% per-applicable-dimension coverage review, zero-tolerance control checks, material-delta continuation, independent QA, adversarial challenge, continuous scenario proof, gap closure, and Boss Gate packages. Do not use for ordinary research that is outside the SMEsPlus VDR governance process.
---

# SMEsPlus VDR Controller

Control SMEsPlus Very Deep Research as a governed evidence system, not as an open-ended research assistant.

## Core operating rule

Apply this chain unless the current governed state explicitly places the session later in the chain:

1. Identify session, scope, domain, current state, parent state, and existing verified evidence.
2. Define proof requirements before claiming research completeness.
3. Build or reconcile the canonical Question, Function, VDR Target, Zero-Tolerance, and Coverage Dimension universes.
4. Perform atomic reconciliation and independent pre-freeze challenge.
5. Require Boss-frozen canonical denominator before Formal Coverage.
6. Require separate authorization before VDR execution when governance requires it.
7. Execute applicable L1-L12 research.
8. Execute five proof layers and verify evidence integrity.
9. Verify source presence, runtime reachability, configuration reachability, optional reachability, and cross-module handoffs when applicable.
10. Run independent QA and adversarial challenge.
11. Calculate eligible coverage only after denominator freeze.
12. Issue a recommendation; leave final approval to Boss.

Read [references/vdr-constitution.md](references/vdr-constitution.md) first for non-negotiable rules.

## Intake and continuation

Prefer `DELTA-FIRST` over full restart.

When project bootstrap files are available, read in this order:

1. `MASTER_INDEX.md`
2. `PROJECT_SYSTEM_REGISTRY.md`
3. `PROJECT_CONSTITUTION.md`
4. `CURRENT_STATE.md`
5. `CHANGELOG.md`
6. relevant State summary
7. relevant Step summary
8. changed evidence
9. detailed evidence only as needed

Classify the change as `NO MATERIAL DELTA`, `MATERIAL DELTA`, or `UNKNOWN DELTA`. Carry forward verified evidence when there is no material delta. Do not reread unchanged evidence without a concrete reason.

Do not hard-code transient project counts, session IDs, percentages, commits, or current step into this skill. Obtain them from runtime context, project files, GitHub/Jira/Drive, evidence registers, or other authorized sources.

## Research depth

Use [references/l1-l12-standard.md](references/l1-l12-standard.md) to determine applicable research depth. Do not mark a function Research-Complete solely because documentation or source code exists.

## Proof and evidence

Use [references/proof-and-evidence.md](references/proof-and-evidence.md) for the five proof layers, evidence states, traceability fields, and evidence-quality rules.

Never fabricate evidence pointers. If a pointer cannot be verified, write `EVIDENCE POINTER NOT VERIFIED`.

Keep these states separate:

- Research completion
- Proof completion
- Evidence integrity
- Coverage eligibility
- Gate disposition
- Boss decision

## Denominator and coverage

Use [references/denominator-and-coverage.md](references/denominator-and-coverage.md).

Enforce all of the following:

- `No Frozen Canonical Denominator = No Formal Coverage`.
- Before freeze, label percentages `DIAGNOSTIC ONLY - NOT FORMAL COVERAGE`.
- Every Applicable Coverage Dimension must be at least 96%.
- Critical / Zero-Tolerance controls must be 100%.
- Never use an average to hide a weak dimension.
- Never manipulate the denominator after seeing results.
- N/A requires explicit evidence and rationale.

For machine-checkable coverage summaries, use `scripts/check_vdr_gate.py`.

## Independent QA and adversarial challenge

Use [references/gate-and-challenge.md](references/gate-and-challenge.md).

Challenge both the conclusion and the proof. Attempt to disprove material findings. Look for source/runtime mismatch, hidden configuration, role bypass, cross-module identity loss, stale evidence, unsupported N/A, cross-company leakage, cross-tenant leakage, reversal/cancellation defects, migration/historical defects, and reconciliation failures.

## SaaS and clean-room controls

Use [references/saas-clean-room.md](references/saas-clean-room.md) whenever tenant/company boundaries or external reference systems are involved.

Preserve these invariants:

- Tenant = independent customer or demonstrable corporate/economic group security boundary.
- Company = legal/accounting/business boundary inside a tenant.
- Unrelated independent companies default to separate tenants.
- Business relationship does not create a shared tenant.
- Multi-tenant membership does not create a multi-tenant execution context.
- Lower-level relationships never weaken an upper-level security boundary.
- External ERP/source/database material is for learning and verification, not cloning.

## Parallel execution

Allow LESA, SMEs Core, VDR Evidence, Independent QA, and PMO to work in parallel only if they converge to:

- one Canonical Universe,
- one Canonical Denominator,
- one Evidence Control Model,
- one Gate Chain.

Never permit competing denominators for the same governed universe.

## Stop conditions

Issue `HOLD RECOMMENDATION` immediately when a material applicable condition exists, including:

- denominator not frozen when Formal Coverage is requested,
- denominator contamination,
- duplicate Function-ID,
- uncontrolled N/A,
- invalid evidence pointer,
- open critical gap,
- Zero-Tolerance failure,
- unresolved material contradiction,
- source-only claim used as runtime proof,
- required runtime proof missing,
- required configuration proof missing,
- material delta not reconciled,
- cross-tenant security gap,
- cross-company accounting-control gap,
- reconciliation failure,
- Formal Coverage calculated before freeze.

Do not continue merely to chase a higher score.

## Auto Continuous Very Deep Scenario Proof

When explicitly requested:

1. Read current governed state.
2. Identify the weakest Applicable Coverage Dimension.
3. Select unresolved canonical targets with highest proof value.
4. Execute valid proof scenarios using available evidence sources.
5. Capture and validate evidence.
6. Run independent challenge.
7. Reconcile new findings into the canonical registers.
8. Recalculate only eligible coverage.
9. Repeat while useful, valid work remains.

Stop for Boss/architecture decision, denominator re-freeze, unavailable evidence source, unresolved material contradiction, or when no further valid proof can currently be obtained.

## Output contract

Use [references/output-contracts.md](references/output-contracts.md) for function records, coverage reviews, gap registers, and Boss Gate packages.

Allowed AI dispositions:

- `PASS RECOMMENDATION`
- `CONDITIONAL PASS RECOMMENDATION`
- `HOLD RECOMMENDATION`
- `FAIL RECOMMENDATION`

Never output `FINAL APPROVED` unless an explicit Boss decision in the supplied evidence says so. Otherwise use `BOSS DECISION = PENDING`.

Support Thai and English. Keep canonical IDs, control codes, field names, evidence IDs, and technical terms in English when that improves precision.
