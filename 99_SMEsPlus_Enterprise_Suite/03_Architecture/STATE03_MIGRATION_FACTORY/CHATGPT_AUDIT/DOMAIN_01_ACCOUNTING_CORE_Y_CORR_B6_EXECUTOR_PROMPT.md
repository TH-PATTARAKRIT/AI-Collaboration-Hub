# [SMEPLUS-26-08-30-MIG-B-D01-CORR6-001]
# DOMAIN_01 Team B Targeted Corrective Round 6 — Fiscal Calendar Viewpoint, Membership Coherence & Retroactive-Change Semantics / L999.999

## 0. EXECUTION COMMAND

Continue in the **SAME Team B Claude session**.

This is **TARGETED CORRECTIVE ROUND 6 ONLY**.

Do NOT restart B0-B22.
Do NOT restart Team A research.
Do NOT start DOMAIN_02.
Do NOT write production code.
Do NOT create physical DB/API implementation.
Do NOT perform PMO verification.
Do NOT self-approve Boss Final Gate.

Read the latest ChatGPT Independent Re-Audit Round 6 in full. Correct only the Fiscal-Calendar viewpoint / membership / retroactive-change defects, run focused regression, commit/push/verify, then STOP for ChatGPT re-audit.

---

## 1. SOURCE OF TRUTH

Repository:

`TH-PATTARAKRIT/AI-Collaboration-Hub`

Branch:

`SMEsPlus`

Round-5 corrective content:

`406dfc128dac4f61b0a543e818b4b9605aa88264`

Round-5 closure/SHA update:

`275c446a89fca1f972e240844a451ed7f7ef1df9`

Latest ChatGPT Independent Re-Audit Round 6:

`b0ce666dad72909411a49690d0f642313d94dd13`

Audit artifact:

`CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_X_TEAM_B_INDEPENDENT_REAUDIT_ROUND6.md`

Jira control item:

`ERPPLUS-100`

Read the audit before editing any design artifact.

---

## 2. CURRENT GATE POSITION

```text
TEAM A DOMAIN_01: BOSS APPROVED WITH CONTROL
TEAM B ROUND 5: VERIFIED REMOTE
M-AUD-11 TRIAL BALANCE SEMANTICS: CLOSED
M-AUD-12 ORIGINAL SILENT CALENDAR EDIT: CORE CLOSED
M-AUD-13 ELAPSED VIEWPOINT CONTRADICTION: FAIL / CRITICAL
M-AUD-14 CALENDAR VERSION VS ENTRY MEMBERSHIP: FAIL / CRITICAL
CLEAN-ROOM: REVIEW PASS
PMO: HOLD
BOSS FINAL GATE: NOT OPEN
DEVELOPMENT: NOT AUTHORIZED
PRODUCTION: NOT AUTHORIZED
JIRA ASSIGNEE: UNASSIGNED
JIRA DUE DATE: TBD
```

Do not invent Jira owner or due date.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

---

# CORR-B6-01 — MAKE FISCAL CALENDAR SELECTION VIEWPOINT-AWARE

## Blocking contradiction

B07 §1g still says:

`The Elapsed test itself never takes a viewpoint parameter.`

But B07 §1h now defines Fiscal-Year Start/End boundaries as versioned facts with:

- Effective Date;
- Recorded At;
- Historical Known view;
- Current/restated view.

The old §1g statement is now stale and contradictory.

## Required design

Define explicit conceptual semantics equivalent to:

```text
FiscalYearDefinition_Known(C, date, T)
FiscalYearDefinition_Current(C, date)

Elapsed_Known(Y, D, T)
Elapsed_Current(Y, D)
```

or one generic viewpoint-parameterized formulation.

### Known viewpoint

A Known report at cutoff T must use:

- Entries knowable at T;
- Fiscal-Year boundary version knowable/authoritative at T;
- Fiscal-Year membership interpretation knowable/authoritative at T;
- Elapsed determination under that same version.

A later calendar change must not alter an already-issued Known report.

### Current/restated viewpoint

A Current report may reflect later authorized calendar changes only according to their explicit Effective-Date and reclassification/restatement semantics.

Do not mix a historical Entry subset with today's calendar boundary silently.

Update B07 §1e/§1g/§1h and B08 MP-09/MP-12 accordingly.

---

# CORR-B6-02 — CHOOSE ONE COHERENT POST-RELIANCE CALENDAR-CHANGE MODEL

Round 5 currently allows a post-reliance Version 2 boundary while existing Entry membership remains under Version 1.

That is under-specified for Current reporting.

Compare at least:

## Option A — Prospective-Only Change After Reliance

Once a Fiscal-Year boundary has governed COMMITTED facts or issued reports:

- historical membership remains frozen;
- a new calendar version may only govern future dates/future Fiscal Years;
- no current/restated report reinterprets old Entries under the new boundary;
- any correction of historical Fiscal-Year membership requires a separate formal Restatement/reclassification path.

## Option B — Retroactive Change with Atomic Restatement/Reclassification

A new boundary version may become effective over already-recorded dates only if one controlled operation also defines the affected reclassification/restatement semantics.

Requirements:

- Known view preserves old boundary + old membership;
- Current/restated view uses new boundary + new membership;
- affected Entry memberships cannot remain half-old/half-new;
- all affected comparative reporting must be reproducible;
- audit event links old version, new version, reason, actor, Recorded At, Effective Date, scope, and affected reporting periods.

## Option C — another model

Allowed only if it is internally coherent and proves stronger or equivalent guarantees.

Select one model and state why.

Do NOT leave the current hybrid semantics in place.

---

# CORR-B6-03 — RECONCILE FISCAL-YEAR MEMBERSHIP

Current design says:

- exactly one Fiscal Year contains any date for a Company;
- boundary versions can change;
- an Entry's membership is fixed by the boundary version authoritative when Recorded;
- Current view uses latest authoritative boundary version from Effective Date forward.

These statements must be reconciled.

Define precisely:

```text
Fiscal-Year Membership of Entry
Calendar Version governing Membership
Membership_Known(E,T)
Membership_Current(E)
```

or equivalent neutral concepts.

Acceptance:

For any Company + Entry + reporting viewpoint, exactly one Fiscal-Year membership is authoritative.

No date/Entry may be interpreted simultaneously under incompatible versions.

If Current and Known memberships differ after a formal historical calendar Restatement, both must remain independently reconstructable and explicitly labeled.

---

# CORR-B6-04 — PROPAGATE INTO REPORTING FORMULAS

Reconcile at minimum:

```text
FiscalYearActivity_Known
FiscalYearActivity_Current
ReportedRetainedEarnings_Known
ReportedRetainedEarnings_Current
ReportedEquity_Known
ReportedEquity_Current
Elapsed_Known
Elapsed_Current
MP-12 Proof D
MP-12 Proof G4
```

Every formula must use one coherent reporting viewpoint end-to-end.

Forbidden hybrid example:

```text
Historical financial facts @ T
+
Current calendar version @ now
```

unless explicitly defined as a separate analytical view — never as an originally-issued report reconstruction.

---

# CORR-B6-05 — FISCAL CALENDAR IDENTITY / CARDINALITY

Update B07 Fiscal Year identity wording.

The old unconditional statement:

`exactly one Fiscal Year contains any given date for a Company`

is incomplete once versions exist.

Replace with a viewpoint/version-safe invariant equivalent to:

```text
For one Company and one authoritative calendar viewpoint/version,
exactly one Fiscal Year governs any eligible date.
```

Also define:

- no overlapping active Fiscal Years in one authoritative calendar version;
- no uncovered dates if the business policy requires continuous fiscal coverage;
- how transitions between calendar versions preserve this invariant;
- how future-dated version changes are validated before activation.

Do not invent implementation storage.

---

# CORR-B6-06 — TARGETED REGRESSION

Create:

`B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md`

Use at least these personas:

```text
Senior Accountant
Financial Controller
External Auditor
Historical Reporting Reviewer
Fiscal Calendar Administrator
Migration Architect
SaaS Domain Architect
Accounting Systems Architect
Clean-room Reviewer
```

Run at least 15 scenarios.

### Test 1 — Known report before later calendar change

Issue a report at T1 under Fiscal Calendar Version 1.

Later create Version 2.

Re-run Known(D,T1).

Expected: identical Fiscal-Year membership, Elapsed status, P&L, Reported RE and Reported Equity.

### Test 2 — Current report after prospective-only future calendar change

If selected model allows prospective change, verify past membership unchanged and future dates follow Version 2.

### Test 3 — Current report after retroactive boundary change

If selected model allows retroactive change, prove Current membership changes only through the required formal reclassification/restatement mechanism.

If selected model forbids it, prove the request is rejected/rerouted.

### Test 4 — Round-5 Test-12 scenario

FY2024 Version 1 = Jan1-Dec31.
Attempt Version 2 = Jan1-Nov30 after heavy reliance.

Explicitly show what happens to December Entries under Known and Current views.

No hybrid ambiguity allowed.

### Test 5 — December Entry exactly at affected boundary

Entry Effective Date Dec15/2024.
Show authoritative Fiscal-Year membership before and after the calendar-change process.

### Test 6 — Elapsed_Known vs Elapsed_Current

After later boundary versioning, compute both for the same historical D/T.

Expected: Known uses historical calendar version; Current uses authorized current semantics.

### Test 7 — Reported RE Known after later calendar change

Must remain identical to originally-issued result.

### Test 8 — Reported RE Current after legitimate historical calendar Restatement

If allowed, must reflect the approved reclassification consistently.

### Test 9 — Current-FY P&L after calendar version transition

Verify Revenue/Expense membership has one authoritative answer.

### Test 10 — Raw cumulative TB unaffected by calendar policy

`CumulativeAccountBalance` / Raw Cumulative TB must remain ledger-fact driven and balanced independent of Fiscal-Year version changes.

### Test 11 — Balanced Presentation TB after calendar Restatement

Derived bridge and Reported Equity must use the same Current calendar/membership viewpoint and balance.

### Test 12 — Future version with zero reliance

Change next Fiscal Year before any Entry/report relies on it; verify clean transition.

### Test 13 — overlapping proposed versions

Attempt a calendar version that creates overlapping Fiscal Years under one Current viewpoint.
Expected: reject before activation.

### Test 14 — gap between Fiscal Years

If continuous coverage is required, attempt a version creating an uncovered date interval.
Expected: reject; otherwise document why the business allows it.

### Test 15 — multi-company isolation

Company A calendar versioning must not alter Company B membership, Elapsed status, P&L, Reported RE or Reported Equity.

For every scenario record:

```text
Inputs
Timeline
Query Date D
Knowledge Cutoff T
Calendar Version(s)
Version Effective Date
Version Recorded At
Entry Effective Date
Entry Recorded At
Membership_Known
Membership_Current
Elapsed_Known
Elapsed_Current
Raw Cumulative TB
Fiscal-Year Activity
Reported RE
Reported Equity
Expected Result
Actual Result
PASS / FAIL
Finding
Disposition
```

Any CRITICAL/HIGH finding = HOLD and correct before claiming re-audit readiness.

---

# CORR-B6-07 — PROPAGATE CORRECTIONS

Inspect/update every materially affected artifact, at minimum:

```text
B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md
B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md
B05_ACCOUNTING_INVARIANT_BASELINE.md
B07_CONCEPTUAL_INFORMATION_MODEL.md
B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md
B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md
B10_CANONICAL_MIGRATION_REQUIREMENTS.md
B11_EXCEPTION_FAILURE_MODEL.md
B13_DESIGN_OPTION_TRADEOFF_REGISTER.md
B15_DESIGN_TRACEABILITY_MATRIX.md
B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md
B23_CORR_B6_FISCAL_CALENDAR_VIEWPOINT_AND_MEMBERSHIP_REGRESSION.md
DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md
DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md
DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md
TEAM_B_STATUS.md
```

Create:

`CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md`

and a Round-6 closure evidence artifact/session closure.

Preserve visible correction history. Do not silently erase prior defects.

---

# CORR-B6-08 — CLEAN-ROOM / GITHUB / STOP

Clean-room requirement:

`Critical Vendor-Derived Design Risk = 0`

Commit only controlled Markdown design/evidence artifacts.

Recommended commit message:

`docs(state03): correct DOMAIN_01 fiscal calendar viewpoint and membership semantics`

Push to:

```text
TH-PATTARAKRIT/AI-Collaboration-Hub
branch SMEsPlus
```

Verify independently:

1. `origin/SMEsPlus`
2. direct GitHub commit lookup

Record remote SHA.

Update Jira `ERPPLUS-100` with evidence only. Do not invent Assignee or Due Date.

---

# FINAL EXECUTOR REPORT

Report exactly:

```text
CORR-B6-01 Calendar Viewpoint:
CORR-B6-02 Change Model Selected:
CORR-B6-03 Membership Semantics:
CORR-B6-04 Reporting Formula Propagation:
CORR-B6-05 Cardinality/Identity:
CORR-B6-06 Regression:
CORR-B6-07 Artifact Propagation:
CORR-B6-08 Evidence/Push Verification:

Regression Tests Passed:
Regression Tests Failed:
New Critical Findings:
New High Findings:
Remaining Boss Assumptions:
Residual Team A Unknowns:
Clean-room Critical Risk:
Orphan Critical Decisions:
Git Commit:
Push Verified:
Jira Status:
Jira Assignee:
Jira Due Date:

STATUS:
READY FOR CHATGPT INDEPENDENT RE-AUDIT
or
HOLD — <exact evidence-backed blocker>
```

---

# STOP CONDITION

After verified push:

STOP.

Do NOT:

- perform PMO verification;
- open Boss Final Gate;
- resolve Boss assumptions;
- start coding;
- start DOMAIN_02;
- declare Final Pass.

Next authority:

`ChatGPT Independent Re-Audit -> PMO Verification -> Boss Final Gate`

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

# /L999.999 — EXECUTE NOW
