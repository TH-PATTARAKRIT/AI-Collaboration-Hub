# [SMEPLUS-26-09-01-COA-G02-CORR1-001]
# COA-G02 CORR1 — Targeted SaaS Invariant Evidence-Record & Gate-Report Reconciliation / L999.999

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical Branch: `SMEsPlus`
Domain: DOMAIN_01 Accounting Core / COA
Gate: `COA-G02 — Base COA Kernel Discovery`
Execution Role: Team B targeted correction
Boss: Sole Final Approver

Absolute rules:

- No Evidence = No Progress.
- Never Skip Gate.
- Do not convert UNKNOWN into FACT.
- Do not broaden a targeted correction into redesign.
- Do not self-approve G02.

## 2. AUTHORITY / INPUTS

Read and verify before editing:

1. Boss G02 authorization:
   `29eafce5bd9923d577167ecb8f9f1f63e88286df`
2. Team B G02 Gate Report:
   `051acf4fd3b375e977d4e65e99bf12388402a830`
3. Fresh Independent Audit Prompt:
   `f900b5b8d5587d4556f5d09b4b06f86faa109679`
4. Five-Unit audit readiness:
   `8314808d197077e1eb7e0ed160770b5aa729315c`
5. Independent Audit result:
   `d452ecc8fc826ed9d07b738ff5a5efc9028a633e`
6. CORR1 Five-Unit readiness:
   `519b59bacdebe031abdaa067abd1dea200b4a4f0`
7. Boss Cross-Gate SaaS Invariants ruling:
   `DOMAIN_01_ACCOUNTING_CORE_AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`

Authority order:

`Boss Ruling > ChatGPT Independent Audit > Primary Evidence > Executor Claim`

## 3. INDEPENDENT AUDIT RESULT TO PRESERVE

Independent Audit terminal disposition:

`COA-G02 = HOLD / CORRECTION REQUIRED`

Substantive result:

`36-CONCEPT BASE COA KERNEL CANDIDATE = INDEPENDENTLY SUPPORTED`

The Independent Audit verified:

- primary workbook integrity;
- ODOO18 = 389 rows;
- 14 observed source Account Type labels;
- reconcile True=33 / False=356;
- 39 explicit `account.1_*` anchors;
- missing anchors = 0;
- extra anchors = 0;
- row/name mismatches = 0;
- all nine Team B reductions = ACCEPT;
- all six mandatory additions = ACCEPT;
- K01..K36 semantic candidate set supported at G02 scope;
- no accounting-semantic defect requiring redesign of the 36-concept candidate.

Do not reopen those conclusions unless the correction process discovers a genuine contradictory primary fact.

## 4. BLOCKING FINDINGS — EXACT CORRECTION SCOPE

### G02-AUD-01 — MANDATORY SI EVIDENCE-RECORD FIELDS MISSING

Affected artifact:

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G02_EVIDENCE/COA_G02_SAAS_INVARIANT_COMPLIANCE.md`

Current defect:

The existing matrix does not contain all Boss-mandated evidence-record fields and uses status forms such as `PASS` / `PASS — classification scope`, which are outside the exact allowed vocabulary.

Required Boss fields for each SI-01..SI-10:

1. Applicability to the Gate
2. Evidence Location
3. Owner / Owner Role
4. Reviewer / Verifier
5. Verification Status
6. Conflict / Exception
7. Gate Impact

Allowed Verification Status vocabulary only:

- `PASS / VERIFIED`
- `HOLD / EVIDENCE REQUIRED`
- `FAIL / FROZEN`
- `N/A — JUSTIFICATION REQUIRED`

### G02-AUD-02 — G02 GATE REPORT MISSING EXPLICIT SI MATRIX

Affected artifact:

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G02_EVIDENCE/COA_G02_GATE_REPORT.md`

Current defect:

The report contains a summary assertion that SI-01..SI-10 pass at classification/discovery scope, but does not include the explicit Boss-required SI-01..SI-10 evidence matrix.

## 5. MANDATORY EXECUTION ORDER

### STEP 1 — BASELINE / DIFF CONTROL

Before editing:

- fetch canonical `SMEsPlus`;
- verify current HEAD;
- verify Independent Audit commit exists in history;
- inspect both affected files;
- inspect Boss SI ruling;
- inspect CORR1 Five-Unit readiness;
- record clean working state.

If unrelated concurrent changes exist in the same files, STOP and report conflict rather than silently overwriting them.

### STEP 2 — CORRECT `COA_G02_SAAS_INVARIANT_COMPLIANCE.md`

Republish the current SI-01..SI-10 matrix using a structure containing at minimum:

| SI | Requirement | Applicability to G02 | Evidence Location | Owner / Owner Role | Reviewer / Verifier | Verification Status | Conflict / Exception | Gate Impact |
|---|---|---|---|---|---|---|---|---|

Mandatory interpretation:

- Each SI remains a cross-Gate guardrail at G02.
- `PASS / VERIFIED` at G02 means the G02 classification/discovery result complies with the invariant at this Gate's authorized scope.
- It does NOT mean runtime implementation, provisioning, upgrade, isolation or multi-company execution proof is complete.
- Later-Gate ownership must remain explicit for G04/G04S/G05/G06/G07 as applicable.
- Do not mark an applicable invariant `N/A` merely because runtime proof is later.
- Do not use non-approved status variants.

For evidence locations, cite exact current controlled artifacts/sections/commits wherever available rather than generic prose.

For owner/reviewer fields, state the responsible role honestly. Do not invent a named human reviewer if none exists.

For conflicts/exceptions:

- use `NONE` where there is no known conflict at G02 scope;
- explicitly state controlled downstream evidence dependency where runtime/deep-design proof belongs to a later Gate;
- do not label a normal later-Gate dependency as a G02 failure if the Boss ruling only requires G02-safe classification behavior.

### STEP 3 — CORRECT `COA_G02_GATE_REPORT.md`

Add a dedicated section titled exactly or equivalently:

`SAAS INVARIANT COMPLIANCE — SI-01..SI-10`

Include an explicit matrix with the same seven Boss-required evidence fields for every SI.

The Gate Report must make all of the following unambiguous:

1. substantive 36-concept candidate remains independently supported;
2. CORR1 addresses only G02-AUD-01 and G02-AUD-02;
3. no runtime G04S/G07 proof is being claimed;
4. Team B correction is complete only at evidence-production scope;
5. G02 remains `HOLD / CORRECTION REQUIRED — PENDING FRESH TARGETED INDEPENDENT RE-AUDIT` until that re-audit occurs;
6. `READY FOR PMO VERIFICATION = NO` before re-audit PASS;
7. `COA-G03 = NOT STARTED / NOT AUTHORIZED`.

### STEP 4 — CONSISTENCY CHECK

Mechanically verify:

- exactly 10 SI rows in each required SI matrix;
- every SI row has all seven required evidence-record fields;
- verification-status values use only the Boss-approved vocabulary;
- no `PASS — classification scope`, plain `PASS`, `DEFERRED`, or other status appears in the Verification Status column;
- both affected artifacts express the same current G02 Gate state;
- 36 candidate count unchanged;
- nine reductions unchanged;
- six additions unchanged;
- K01..K36 unchanged;
- Boss 19 ACTIVE Account Types unchanged;
- no G03 evidence created;
- no database/API/ORM/implementation content introduced.

If any semantic contradiction is discovered, STOP and report it as a new evidence conflict instead of silently modifying the candidate set.

### STEP 5 — PUBLICATION

Before commit:

- inspect `git diff`;
- confirm changed scope is limited to the two affected G02 artifacts plus necessary CORR1 closure/evidence records;
- ensure no unrelated changes;
- ensure historical audit evidence remains untouched.

Publish a targeted additive correction commit.

Do not rewrite or delete the Independent Audit commit.

### STEP 6 — CORR1 CLOSURE RECORD

Create a concise Team B CORR1 closure artifact recording:

- triggering audit commit;
- G02-AUD-01 disposition;
- G02-AUD-02 disposition;
- files changed;
- exact commit SHA;
- verification checks performed;
- semantic candidate unchanged confirmation;
- current Gate status;
- next required reviewer.

## 6. REQUIRED TERMINAL STATUS

Team B must stop with exactly:

`COA-G02 CORR1 TEAM B CORRECTION = COMPLETE`

`G02-AUD-01 = CORRECTED / PENDING INDEPENDENT RE-AUDIT`

`G02-AUD-02 = CORRECTED / PENDING INDEPENDENT RE-AUDIT`

`36-CONCEPT CANDIDATE = UNCHANGED / INDEPENDENTLY SUPPORTED BY PRIOR AUDIT`

`COA-G02 = HOLD / CORRECTION REQUIRED — PENDING FRESH TARGETED INDEPENDENT RE-AUDIT`

`READY FOR PMO VERIFICATION = NO`

`COA-G03 = NOT STARTED / NOT AUTHORIZED`

Do not use `PASS`, `CLOSED`, `READY FOR PMO`, or `BOSS APPROVED` in the Team B terminal disposition.

## 7. FRESH TARGETED RE-AUDIT REQUIREMENT

After publication, the next session must be a fresh independent reviewer context and must inspect only the CORR1 delta plus enough unchanged evidence to ensure no semantic regression.

Required re-audit questions:

1. Does `COA_G02_SAAS_INVARIANT_COMPLIANCE.md` now contain all seven mandatory fields for SI-01..SI-10?
2. Does each Verification Status use only the Boss-approved vocabulary?
3. Does `COA_G02_GATE_REPORT.md` now contain a complete explicit SI-01..SI-10 matrix?
4. Are later-Gate deferrals preserved without false runtime-proof claims?
5. Did CORR1 leave the independently supported 36-concept semantics unchanged?
6. Did CORR1 remain within G02-AUD-01/02 scope?

If all pass, the independent reviewer may return:

`PASS / VERIFIED — READY FOR PMO VERIFICATION`

Otherwise return:

`HOLD / CORRECTION REQUIRED`

or

`FAIL / FROZEN`

## 8. PROHIBITED ACTIONS

Do NOT:

- redesign the Base Kernel;
- optimize toward ~32;
- alter K01..K36 without newly discovered contradictory primary evidence;
- start G03;
- perform PMO Verification;
- issue Boss G02 closure;
- freeze final COA;
- design schema/API/ORM;
- code/build/deploy;
- claim runtime SaaS proof;
- erase the HOLD audit history.

## 9. PROGRESS REPORTING

Unless an approved evidence-weighted denominator exists, report exactly:

- `% Board = TBD / NO APPROVED BASELINE`
- `% STATE = TBD / NO APPROVED BASELINE`
- `% STEP = TBD / NO APPROVED BASELINE`

No guessed percentages.

## 10. EXECUTION COMMAND

Proceed autonomously with the targeted CORR1 correction only.

Do not ask Boss to reconfirm the already-established correction scope.

Stop immediately after publication and report the correction commit and evidence paths for fresh targeted Independent Re-audit.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
