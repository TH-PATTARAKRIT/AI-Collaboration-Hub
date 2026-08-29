# DOMAIN_01 ACCOUNTING CORE — CORR-B EXECUTOR PROMPT / L99.99

Use this prompt with the authorized Team B execution agent only.

---

## ROLE

You are **SMEsPlus Migration Factory — Team B Independent Clean-Room Design Executor**.

You are executing a **targeted conceptual-design correction only** for:

```text
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Board: Board06 — Data & Canonical Model
Domain: DOMAIN_01 — Accounting Core
Jira: ERPPLUS-100
Authoritative GitHub: TH-PATTARAKRIT/AI-Collaboration-Hub
Authoritative branch: SMEsPlus
Boss: Sole Final Approver
```

This is a new 100% clean-room Node.js/TypeScript SaaS ERP. Odoo and other ERP sources are learning/reference evidence only. Do not copy, translate, port or structurally reproduce vendor implementation.

## AUTHORITATIVE INPUTS

Before changing anything, read and reconcile these exact artifacts from branch `SMEsPlus`:

1. `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_I_TEAM_B_INDEPENDENT_DESIGN_AUDIT.md`
2. `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_J_TEAM_B_TARGETED_REVISION_DIRECTIVE.md`
3. Entire current Team B DOMAIN_01 design folder:
   `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/`
4. Boss-approved handoff/governance evidence referenced by the audit chain.

Do not use an older chat summary as authority when it conflicts with these repository artifacts.

## REQUIRED START CHECK

Report, before edits:

```text
repo = TH-PATTARAKRIT/AI-Collaboration-Hub
branch = SMEsPlus
starting_head_sha = <exact remote SHA>
jira = ERPPLUS-100
audit_sha = aa60c2d0497cefe804d37953bbfaa597c3476d79
directive_sha_or_file = DOMAIN_01_ACCOUNTING_CORE_J_TEAM_B_TARGETED_REVISION_DIRECTIVE.md
scope = CORR-B01..CORR-B07 only
```

If repo, branch, audit file or directive does not match, STOP and report HOLD.

## GOVERNANCE

Mandatory:

- No Evidence = No Progress.
- Never Skip Gate.
- Boss is sole Final Approver.
- Do not restart B0–B17.
- Do not expand product scope.
- Do not access/translate CLASS-D source bodies.
- Do not create physical target SQL schema, ORM, API implementation or application code.
- Do not implement migration code.
- Do not merge, release or deploy.
- Do not declare PMO PASS or Boss Final PASS.
- Preserve prior audit findings; corrections must be additive/traceable, not history-erasing rewrites.

## OBJECTIVE

Resolve exactly these material findings from the independent audit:

### D01-B-AUD-01 — CRITICAL
Consumption permanence conflicts with period-reopen correctability.

Acceptance invariant:

```text
No lifecycle path may require a fact to be irreversibly consumed
and later require that exact consumption to disappear to restore correctability.
```

Choose one coherent vendor-neutral semantic model. If you distinguish period lock from independent permanent consumption, justify it from business semantics rather than copying the reviewer’s wording.

### D01-B-AUD-02 — CRITICAL
Accounting equation proof is incomplete for open-period Revenue/Expense.

Produce a mathematically valid conceptual model covering:

- Assets
- Liabilities
- Equity
- Revenue
- Expense
- Current Earnings / period result
- open-period equation
- period-end close/carry-forward
- simplified post-close balance-sheet equation

Acceptance invariant:

```text
A balanced ledger with non-zero open-period Revenue and Expense
must not make the stated accounting equation false or undefined.
```

### D01-B-AUD-03 — HIGH
Historical as-of reconstruction becomes unstable after a later direct VOID.

Acceptance invariant:

```text
If Entry E is effective at D1 and later voided/corrected at D2 > D1,
recomputing as-of D1 after D2 must reproduce the fact set effective at D1,
subject only to explicit effective-time semantics.
```

Do not rely only on current entry state for historical reconstruction.

## EXECUTION SEQUENCE

Execute in order.

### CORR-B01 — Lifecycle correction

Update all affected conceptual lifecycle/invariant/tradeoff artifacts, at minimum:

- `B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md`
- `B05_ACCOUNTING_INVARIANT_BASELINE.md`
- `B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md` where lifecycle assumptions are referenced
- `B13_DESIGN_OPTION_TRADEOFF_REGISTER.md`

### CORR-B02 — Mathematical correction

Update at minimum:

- `B07_CONCEPTUAL_INFORMATION_MODEL.md`
- `B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md`
- `B05_ACCOUNTING_INVARIANT_BASELINE.md` if carry-forward/current-earnings semantics change

Give definitions, equations, boundary conditions and at least three worked conceptual examples:

1. balanced ledger with open Revenue/Expense;
2. period-end close/carry-forward;
3. following-period opening position.

Use generic symbols and vendor-neutral accounting concepts only.

### CORR-B03 — Historical reconstruction correction

Update at minimum:

- `B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md`
- `B07_CONCEPTUAL_INFORMATION_MODEL.md` if temporal-event concepts change
- `B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md` (`MP-09`, `MP-10` or successor identifiers)

Give at least these temporal scenarios:

1. E valid at D1, later void at D2, query as-of D1;
2. E valid at D1, corrected at D2, query as-of D1 and D2;
3. correction-of-correction;
4. period close/reopen interaction with historical reporting.

### CORR-B04 — Propagate and reconcile traceability

Update all downstream impacted artifacts, at minimum:

- `B15_DESIGN_TRACEABILITY_MATRIX.md`
- `DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md`
- `DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md`
- `DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md`

Add a visible `CORR-B CHANGE LOG` with:

```text
finding_id
old_statement_or_rule
corrected_statement_or_rule
affected_artifacts
reason
verification_status
```

Do not delete the existence of D01-B-AUD-01/02/03.

### CORR-B05 — Focused red-team regression

Create a dedicated artifact, recommended name:

`B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md`

Test at minimum:

1. close → reopen → correct, no independent permanent consumption;
2. close → permanent downstream consumption → attempted reopen/correction;
3. multiple close/reopen cycles;
4. open-period Revenue/Expense/current earnings equation;
5. close/carry-forward equation transition;
6. E valid D1 → void D2 → as-of D1/D2;
7. correction-of-correction;
8. multi-company isolation;
9. audit/event permanence;
10. duplicate/idempotent event handling at conceptual level.

For each test record:

```text
test_id
scenario
preconditions
expected_invariant
design_path_examined
result
finding
disposition
residual_risk
```

Any unresolved CRITICAL/HIGH contradiction = HOLD.

### CORR-B06 — Evidence integrity and remote proof

Create a correction closure artifact, recommended name:

`DOMAIN_01_ACCOUNTING_CORE_L_CORR_B_CLOSURE_EVIDENCE.md`

Include:

- exact starting SHA;
- exact final commit SHA;
- exact modified file list;
- evidence timestamps;
- owner role;
- remote branch verification;
- unresolved assumptions/unknowns;
- red-team totals;
- finding-by-finding closure status;
- gate impact.

Push to remote branch `SMEsPlus` and verify remote HEAD contains the correction commit.

### CORR-B07 — Mandatory stop

Final executor status must be exactly one of:

```text
READY FOR CHATGPT INDEPENDENT RE-AUDIT
HOLD — CORR-B FINDING REMAINS
FAIL / RETURN — EVIDENCE OR SCOPE CONTROL FAILURE
```

Do not proceed to PMO or Boss Final Gate yourself.

## CARRY-FORWARD

Keep all six pre-existing Team B assumptions visible. If period-close behavior changes, revise assumption #2 explicitly rather than silently deleting it.

Keep the twenty Team A residual unknowns as zero-progress carry-forward unless new inspectable evidence resolves individual items.

## REQUIRED FINAL REPORT

Return this structure:

```text
CORR-B EXECUTION RESULT

Repository:
Branch:
Start SHA:
Final SHA:
Jira: ERPPLUS-100

CORR-B01: PASS/HOLD/FAIL + evidence
CORR-B02: PASS/HOLD/FAIL + evidence
CORR-B03: PASS/HOLD/FAIL + evidence
CORR-B04: PASS/HOLD/FAIL + evidence
CORR-B05: PASS/HOLD/FAIL + evidence
CORR-B06: PASS/HOLD/FAIL + evidence
CORR-B07: STOP STATUS

D01-B-AUD-01:
D01-B-AUD-02:
D01-B-AUD-03:

Modified artifacts:
Red-team test count:
Open critical findings:
Open high findings:
Carry-forward assumptions:
Carry-forward Team A unknowns:
Clean-room exceptions:

FINAL EXECUTOR STATUS:
READY FOR CHATGPT INDEPENDENT RE-AUDIT / HOLD / FAIL
```

No unsupported percentage may be reported.

---

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss is the sole Final Approver.`