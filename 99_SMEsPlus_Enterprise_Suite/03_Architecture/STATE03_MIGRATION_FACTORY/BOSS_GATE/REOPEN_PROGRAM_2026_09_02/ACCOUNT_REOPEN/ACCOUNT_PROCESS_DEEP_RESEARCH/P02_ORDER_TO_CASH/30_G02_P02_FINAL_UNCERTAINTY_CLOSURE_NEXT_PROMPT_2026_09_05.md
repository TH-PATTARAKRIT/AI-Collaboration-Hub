# [SMEPLUS-26-09-05-G02-P02-O2C-FINAL-UNCERTAINTY-CLOSURE-003]
# G02-P02 Order-to-Cash — Final Uncertainty Closure: Evidence Identity, Population Denominator, C-04 Runtime Boundary & Clean Handoff / L99999.99999

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Parallel Group: **G02 — Sales / Revenue / Cash**
Process: **P02 — Order-to-Cash**
Execution Mode: **CONTINUE EXISTING OLD P02 SESSION**
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Working Branch: `research/account-p02-order-to-cash-2026-09-04-001`
Baseline Commit: `aca211e637bc72ff25bd7182c0eff9ab57061bfd`
Package Path: `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_PROCESS_DEEP_RESEARCH/P02_ORDER_TO_CASH/`
Boss: **Sole Final Approver**

## 2. MODEL / EFFORT — FIXED FOR THIS EXECUTION ENVELOPE

Use exactly:
- **Model: Claude Opus 5**
- **Effort: HIGH**

One Prompt = One fixed Model/Effort execution envelope.
Do not switch model or effort inside this run.

## 3. PURPOSE OF THIS ROUND

This is NOT another full Deep Research round.
This is NOT a reset.
This is NOT a re-run of all prior P02 work.

This round exists only to close the three remaining uncertainty classes that now bound P02:

1. **Evidence Identity Model**
   - `Artifact != Snapshot != Database UUID != Database Lineage != Deployment Instance`
   - eliminate the identity ambiguity exposed by C-44 / C-48 / C-49;
   - determine which identity statements are FACT VERIFIED, which are only lineage hypotheses, and which prior conclusions must be withdrawn or narrowed.

2. **Population Denominator Integrity**
   - rebuild the P02 evidence population with a format-complete, independently implemented discovery method;
   - explicitly include and distinguish PGDMP, Odoo ZIP/backup, plain SQL dumps, unpacked backup directories, mounted/local database artefacts, and other materially relevant archive shapes already evidenced in the estate;
   - do not treat multiple tools that share the same pattern/blind spot as independent corroboration;
   - publish the command/method, denominator unit, path set, pattern set, positive controls, and failure controls;
   - do not claim customer-estate completeness; bound the claim to the evidence estate actually searched.

3. **C-04 Runtime Authority Boundary**
   - determine whether C-04 can now be closed entirely from existing read-only evidence;
   - if not, identify the exact existing disposable sandbox, exact script, exact writes/mutations, exact rollback/reset procedure, and exact evidence output required;
   - if explicit Boss authorisation for this bounded sandbox execution already exists in the current session/evidence, execute only within that exact boundary;
   - if such authorisation does NOT exist, DO NOT write, install, restore, start a customer/production DB, or mutate any environment. Instead produce the precise Boss Authorisation Pack and continue all unaffected work.

The target outcome is not to force PASS. The target outcome is that every remaining P02 uncertainty is either:
- closed by evidence;
- narrowed to a named, bounded dependency;
- or routed cleanly to G02/P10, P07/P08/P09, P11, or Boss Decision without ambiguity.

## 4. COMMON EXECUTION CONSTITUTION — MANDATORY

No Evidence = No Progress.
Never Skip Gate.
Boss = Sole Final Approver.
Scope-aware Everywhere.
Old Session First.
No repeated work without Material Delta.
Peer Position != Boss Decision.
UNRESOLVED != ADOPTED.
Recommendation != Canonical Boundary.
Independent Review != Truth.

### Scope-aware rule
Every material object, operation, access path, configuration, reference, report and mutation must first determine its applicable scope:
- PLATFORM
- TENANT
- COMPANY

Do NOT apply Tenant + Company context as a blanket requirement to every operation.

## 5. PRESERVE PRIOR LINEAGE

Preserve all existing files and prior findings, including wrong findings.
Do not silently overwrite them.

Mandatory lineage to preserve and reconcile:
- `RE-13` through latest RE entries;
- C-44 / C-48 / C-49;
- P02-F-28a withdrawal;
- prior population counts and why each was superseded;
- the plain-SQL dump omission;
- UUID over-count / under-count evidence;
- all C-04 status changes;
- all PMO exit-criteria movements.

Any new correction must be added to the revision/error log with:
Original Finding -> Source Used -> Why Wrong -> New Evidence -> Corrected Finding -> Architecture Impact -> Affected Decision/Prompt/Commit.

## 6. CANONICAL EVIDENCE IDENTITY MODEL — REQUIRED DELIVERABLE

Create a new controlled deliverable that defines and tests at least these levels:

### 6.1 Artifact
A physical file/directory/archive discovered on a storage path.
Identity may use path + hash + size + format + timestamps, but no single one is assumed sufficient without evidence.

### 6.2 Snapshot
A point-in-time backup/export/copy of a database lineage.
Multiple artifacts may represent the same snapshot.

### 6.3 Database UUID
A database-level identifier captured inside the database.
Treat it as an observed attribute, NOT automatically as lineage identity.
The current evidence already shows UUID can be changed after restore and shared across distinct live databases.

### 6.4 Database Lineage
A continuous ancestry of database state across backup/restore/copy/upgrade events.
Must be inferred only from evidence such as creation metadata, restore timing, company growth, sequence continuity, internal IDs, or other discriminators.
Do NOT assume name or UUID alone defines lineage.

### 6.5 Deployment Instance
A database lineage actually running with a particular code/module/configuration set in an environment.
A deployment instance must bind:
- database lineage;
- environment/host/container where evidence permits;
- installed module set;
- code/source identity if known;
- configuration scope;
- effective time/version.

### 6.6 Business Entity / Customer Identity
Keep separate from database identity.
One business name may map to multiple database lineages; one lineage may move across business/environment labels.

For every level, produce:
- definition;
- permitted keys;
- forbidden shortcuts;
- evidence required;
- known counterexamples from P02;
- confidence/classification.

## 7. POPULATION DENOMINATOR REBUILD — FORMAT-COMPLETE METHOD

Do NOT simply re-run the prior signature sweep.
The prior method is known blind to at least one material archive shape.

Build a discovery method whose PATTERN SET covers, at minimum, every archive/storage representation already evidenced in P02.

Required controls:

1. **Positive controls by format**
   For each supported archive shape, identify at least one known example and prove the discovery method finds it.

2. **Failure controls**
   Demonstrate that an intentionally unsupported/fake shape is not silently counted as valid.

3. **Independent implementation**
   At least one second implementation must differ materially in approach, not merely re-use the same signature/pattern library.
   Examples of genuine independence include:
   - content/signature-led discovery;
   - structure/manifest/filestore relationship discovery;
   - database-internal metadata discovery after archive extraction/read;
   - OS/file-type assisted discovery with independent validation.

4. **Path set declaration**
   Explicitly enumerate the roots searched.
   Record unreachable roots, cloud placeholders, blocked I/O, permission failures, and excluded roots separately.

5. **Unit declaration**
   Publish separate counts for:
   - artifacts;
   - snapshots;
   - database lineages;
   - deployment instances, if determinable.

Do NOT collapse these into one number.

6. **No premature total**
   Never publish a total while a background discovery task is still running.
   A partial is PARTIAL, never TOTAL.

7. **Background task terminality**
   Before declaring the round terminal, prove:
   - no load-bearing background task is still running;
   - each remaining task is either completed, terminated with evidence, or explicitly non-load-bearing and dispositioned.

## 8. DEPLOYED CODE IDENTITY — BOUND THE CLAIM

For material deployed findings, determine whether the code actually running is known.

At minimum record for each relevant deployment lineage:
- generation/version;
- installed modules;
- custom modules materially affecting Sales / Inventory / Accounting / Payment / Tax;
- source availability status;
- source-to-deployment match status;
- confidence/classification.

Use these statuses only:
- MATCH VERIFIED
- PARTIAL MATCH
- SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED
- SOURCE MISSING
- DEPLOYED CODE IDENTITY UNRESOLVED

Do not convert benchmark source behavior into deployed behavior when code identity is unresolved.

## 9. C-04 — RUNTIME DECISION TREE

First ask:

### 9.1 Can C-04 be closed read-only?
Use all existing source, database, posted-history, configuration and prior test artefacts.
If YES, close it with exact evidence and do not mutate anything.

### 9.2 If NO, is there already explicit Boss authorisation for the exact bounded disposable sandbox execution?
If YES:
- verify sandbox identity and disposable/resettable status;
- verify script hash/path;
- snapshot/pre-state;
- execute exactly once;
- capture logs/results;
- capture intermediate state between Delivery and Invoice where the test is designed to do so;
- capture post-state;
- restore/reset sandbox;
- prove restoration;
- record every write;
- do not touch production/customer databases.

If NO:
- DO NOT execute;
- produce `P02_C04_BOSS_AUTHORISATION_PACK.md` containing:
  - exact sandbox;
  - exact script;
  - exact command;
  - exact database/container to be changed;
  - expected writes;
  - rollback/reset plan;
  - evidence to capture;
  - why read-only evidence is insufficient;
  - what exact questions the run will close;
  - maximum bounded duration/side effects if determinable;
  - stop conditions.

Then continue every unaffected closure task automatically.

## 10. BUSINESS / ACCOUNTING TRUTH — DO NOT REOPEN WITHOUT DELTA

Carry forward Boss-approved policy:

- Invoice Policy != COGS Recognition Policy.
- For normal SMEsPlus Perpetual + Storable flow, physical Delivery/Stock-out is the COGS recognition trigger.
- Revenue/AR recognition remains a separate event from Inventory/COGS recognition.
- Scope-aware Everywhere.

Do not reopen these as benchmark-dependent questions.
Only reopen if new evidence creates a direct contradiction to the Boss-approved SMEsPlus policy itself.

## 11. EIGHT BUSINESS SCENARIOS

Do not repeat scenario work already completed unless the new identity/population/deployed-code evidence changes a conclusion.

For each existing scenario:
- preserve prior status;
- apply only material deltas;
- state whether the new population/identity correction changes it;
- route unresolved statutory questions to P07;
- route core ledger/reporting questions to P08;
- route management-accounting implications to P09;
- route cross-process truth to P11.

## 12. FOUR AAS-03 INDEPENDENT CHALLENGES — MANDATORY

Run four fresh, independent challenge perspectives on the NEW uncertainty-closure material only:

1. Leader Functional Design
2. Leadership Database Design
3. Lead Integration & Localization
4. Lead Code & UI Architect

Each must state separately:
- what is supported;
- what is missing;
- what is risky;
- what is challenged;
- evidence needed next.

At least one challenge must actively attempt to disprove the new Evidence Identity Model.
At least one challenge must attack the population denominator method itself, not its findings.
At least one challenge must attack C-04 closure logic and mutation boundary.
At least one challenge must compare source/deployed-code identity claims against custom module reality.

No expert may self-declare PASS/FAIL for the whole process.

## 13. AAS+ CONSOLIDATION

AAS+ must reconcile:
- agreements;
- disagreements;
- contradictions;
- unresolved evidence;
- Boss decisions;
- cross-process handoffs.

Preserve dissent.
Do not force consensus.

## 14. PMO / EXIT CRITERIA — FRESH ASSESSMENT

Reassess all P02 exit criteria from the current evidence only.

For each criterion:
- previous status;
- current status;
- evidence delta;
- reason for movement/no movement.

Do not improve a criterion merely because more work was performed.
If evidence quality deteriorates a criterion, downgrade it.

## 15. REQUIRED NEW/UPDATED DELIVERABLES

Create/update as evidence requires, including at minimum:

- `30_P02_EVIDENCE_IDENTITY_MODEL.md`
- `31_P02_FORMAT_COMPLETE_POPULATION_REBUILD.md`
- `32_P02_DEPLOYMENT_CODE_IDENTITY_REGISTER.md`
- `33_P02_C04_RUNTIME_CLOSURE_OR_AUTHORISATION_PACK.md`
- `34_P02_FINAL_UNCERTAINTY_RECONCILIATION.md`
- updated Contradiction Register
- updated Revision/Error Log
- updated Source Link Register
- updated Evidence Manifest
- updated AAS-03 Challenge
- updated AAS+ Consolidation
- updated PMO assessment
- updated Core Reconciliation / P11 Handoff
- `P02_CHECKPOINT_REGISTER.md`
- `P02_AUTO_RESUME_STATE.md`

If numbering collides with files already created during execution, preserve existing files and use the next available number while keeping the mandated semantic filename visible.

## 16. CHECKPOINTS + AUTO-RESUME

Mandatory checkpoints:

CP-01 — Evidence identity model built and counterexample-tested
CP-02 — Format-complete population method built and controlled
CP-03 — Population execution completed/dispositioned
CP-04 — Deployment code identity bounded
CP-05 — C-04 read-only closure or exact authorisation pack completed
CP-06 — Business-scenario delta reconciliation
CP-07 — Four AAS-03 challenges completed
CP-08 — AAS+ consolidation completed
CP-09 — PMO exit assessment completed
CP-10 — P11/G02 handoff + terminality audit completed

At each checkpoint:
- write evidence;
- update register;
- commit if materially complete;
- update resume state;
- continue automatically to the next executable checkpoint.

Do not ask Boss for routine intermediate approval.

AUTO_RESUME_STATE must contain:
- last completed checkpoint;
- current blocker/dependency;
- exact next command/action;
- files affected;
- evidence still required;
- whether mutation authorisation is required;
- whether any background task is running;
- safe resume instruction.

## 17. TERMINALITY STANDARD

A P02 execution round is not terminal merely because the narrative says TERMINAL.

Before terminal reporting verify:
- all load-bearing background tasks are completed/dispositioned;
- remote branch contains the final evidence;
- remote HEAD equals intended final local commit;
- no required deliverable is only local/uncommitted;
- no unresolved task is hidden behind prose;
- every remaining HOLD has a named owner/dependency;
- no P10/P06 work was started automatically.

## 18. TERMINAL STATES — ONLY THESE

Choose exactly one:

### A. `G02-P02 READY FOR CONTROLLED HANDOFF TO P10 — OPEN HOLDS NAMED`
Use only if all currently obtainable P02 evidence work is complete, every remaining hold is external/peer/statutory/Boss-owned, and the evidence identity/population method is no longer itself an unresolved blocker.

### B. `G02-P02 MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR NAMED DEPENDENCY`
Use if one or more material P02 blockers remain and cannot be closed without new evidence/authorisation.
Name each one exactly.

### C. `G02-P02 EVIDENCE INTEGRITY FAILURE — CORRECTION REQUIRED`
Use if the population/identity method still produces material contradictions that prevent reliance on the package.

No PASS.
No freeze.
No merge.
No implementation authorisation.

## 19. FINAL REPORT TO BOSS

Report concisely:
- final branch;
- final commit SHA;
- direct GitHub link;
- terminal state;
- evidence identity result;
- population result by unit (artifact/snapshot/lineage/deployment where determinable);
- C-04 result;
- exact remaining holds;
- P11 handoff status;
- whether G02 may proceed to P10 as controlled handoff;
- PMO recommendation;
- background task count at terminal;
- whether any write/mutation occurred.

## 20. STOP RULE

When all currently executable work is exhausted:

COMMIT
-> PUSH
-> VERIFY REMOTE
-> UPDATE CHECKPOINT
-> UPDATE AUTO_RESUME_STATE
-> PRODUCE TERMINAL REPORT
-> STOP.

Do not wait idle.
Do not start P10 automatically.
Do not start P06.
Do not merge.
Do not implement.
Do not contact Boss during execution except where an explicit state-changing authorisation is genuinely required and absent.

Begin now.
