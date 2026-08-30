# [SMEPLUS-26-08-30-MIG-B-D01-CORR5-001]
# DOMAIN_01 Team B Targeted Corrective Round 5 — Trial Balance Horizon Integrity + Fiscal Calendar Historical Safety / L999.999

## 0. EXECUTION COMMAND

Continue in the **SAME Team B Claude session**.

This is **TARGETED CORRECTIVE ROUND 5 ONLY**.

Do NOT restart B0-B21.
Do NOT restart Team A research.
Do NOT start DOMAIN_02.
Do NOT write production code.
Do NOT create physical DB/API implementation.
Do NOT perform PMO verification.
Do NOT self-approve Boss Final Gate.

Read the latest ChatGPT Independent Re-Audit Round 5 in full. Correct only the Trial-Balance horizon contradiction and the Fiscal-Year-boundary historical-safety gap, run focused regression, commit/push/verify, then STOP for ChatGPT re-audit.

---

# 1. SOURCE OF TRUTH

Repository:

`TH-PATTARAKRIT/AI-Collaboration-Hub`

Branch:

`SMEsPlus`

Round-4 corrective content:

`b50dceb7fdd9f0d017ab7b13abf64ac404ee8598`

Round-4 closure/SHA update:

`404e769d8741142f1aa1f4482e8cd20e1f486cef`

Latest ChatGPT Independent Re-Audit Round 5:

`de7492afd0af0f58185f3f36940a77f2389aa8b8`

Audit artifact:

`CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_U_TEAM_B_INDEPENDENT_REAUDIT_ROUND5.md`

Jira control item:

`ERPPLUS-100`

Read the audit before editing any Team B design artifact.

---

# 2. CURRENT GATE POSITION

```text
TEAM A DOMAIN_01: BOSS APPROVED WITH CONTROL
TEAM B ROUND 4: VERIFIED REMOTE
M-AUD-08 REPORTED-EQUITY DOUBLE COUNT: CLOSED AT DOMAIN-DESIGN LEVEL
M-AUD-09 DELAYED FISCAL CLOSE REPORTING GAP: CORE CLOSED
M-AUD-10 CURRENT/KNOWN REPORTED RE: CORE CLOSED FOR FINANCIAL FACTS
M-AUD-11 TRIAL-BALANCE HORIZON CONTRADICTION: FAIL / CRITICAL
M-AUD-12 FISCAL-CALENDAR HISTORICAL MUTABILITY GAP: FAIL / HIGH
CLEAN-ROOM: REVIEW PASS
PMO: HOLD
BOSS FINAL GATE: NOT OPEN
DEVELOPMENT: NOT AUTHORIZED
PRODUCTION: NOT AUTHORIZED
JIRA ASSIGNEE: UNASSIGNED
JIRA DUE DATE: TBD / EMPTY
```

Do not invent Jira assignee or due date.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

---

# 3. CORR-B5-01 — SEPARATE RAW CUMULATIVE LEDGER FROM CATEGORY-BOUNDED REPORTING BALANCES

## Blocking contradiction

MP-09 currently defines category-bounded account balances:

```text
Asset / Liability / Equity:
  cumulative from inception through D

Revenue / Expense:
  lower-bounded by the start of the Fiscal Year containing D
```

MP-12 Proof A correctly uses one common cumulative horizon for every category to prove the raw ledger identity.

MP-12 Proof G then incorrectly says the Raw Trial Balance is MP-09's direct mixed-horizon output and still balances via Proof A.

These are different mathematical populations.

## Required conceptual separation

Define distinct outputs.

### Output A — Raw Cumulative Ledger Balance / Raw Cumulative Trial Balance

For query date D:

- include every authoritative Line with Effective Date <= D;
- use the SAME lower horizon for every Account Category;
- do not reset/bound Revenue or Expense by current Fiscal Year;
- Current view includes all legitimate facts currently known;
- Known view additionally filters `Recorded At <= T`;
- must balance directly because every included Entry is MP-01 balanced.

Use a precise name. Do not call a mixed-horizon report this output.

### Output B — Fiscal-Year-Bounded Account Activity / Reporting Balance

For reporting date D:

- Balance Sheet account balances may remain cumulative;
- Revenue/Expense activity is bounded to the Fiscal Year containing D;
- this is a mixed-horizon reporting view;
- it is NOT, by itself, a raw balanced Trial Balance after prior Fiscal Years have elapsed.

Use a precise name that cannot be confused with Output A.

### Output C — Balanced Reporting / Presentation Trial Balance

If SMEsPlus requires a balanced trial-balance-style presentation using current-FY Revenue/Expense under the no-posted-close model:

- add the required derived prior-FY accumulated-earnings / Reported Retained Earnings bridge as a **presentation-only derived component**;
- never persist/post it as a financial fact;
- prove it ties exactly to the Raw Cumulative Trial Balance and to Reported Financial Statements.

If Team B determines Output C is not a valid required concept at this domain layer, state that explicitly and remove every unsupported claim that MP-09's mixed-horizon output is a balanced Trial Balance.

Do not solve this by silently reintroducing posted closing Entries; the no-posted-close model remains the current controlled design unless independently disproven.

---

# 4. CORR-B5-02 — REPAIR MP-09 SEMANTICS AND NAMING

MP-09 currently carries the title:

`Aggregation (Account Balance / Trial Balance)`

That title now hides two different concepts.

Rework MP-09 so each formula has one exact semantic meaning.

At minimum define separately:

```text
CumulativeAccountBalance_Current(A,C,D)
CumulativeAccountBalance_Known(A,C,D,T)

FiscalYearActivity_Current(A,C,D)
FiscalYearActivity_Known(A,C,D,T)
```

Names may differ, but semantics must not.

For each formula specify:

- upper Effective-Date bound;
- lower Effective-Date bound;
- Recorded-At rule;
- Account Categories to which it applies;
- whether it is expected to balance as a multi-account set;
- whether it is a ledger fact, derived reporting value, or presentation value.

Do NOT use `all-time` ambiguously. Use language equivalent to:

`from ledger inception through Effective Date D`

so future-dated Entries are not accidentally implied to be included.

---

# 5. CORR-B5-03 — RE-PROVE RAW TRIAL BALANCE VS REPORTED/PRESENTATION TRIAL BALANCE

Rebuild MP-12 Proof G.

Mandatory structure:

## Proof G1 — Raw Cumulative Trial Balance

Use one common horizon across all categories.

Show:

```text
Σ raw cumulative debits through D
=
Σ raw cumulative credits through D
```

and derive the expanded Raw Ledger Identity.

## Proof G2 — Current-FY reporting transformation

Partition cumulative Revenue/Expense into:

```text
Prior elapsed Fiscal Years
+
Current Fiscal Year
```

Move prior elapsed net earnings into the derived reporting-equity representation exactly once.

Show how the Reported Financial-Statement equation follows.

## Proof G3 — Balanced presentation TB, if retained

If a balanced current-FY Trial Balance presentation exists, show the exact derived bridge line/component required to make the presentation balance.

It must be labeled:

```text
DERIVED PRESENTATION COMPONENT — NOT POSTED FINANCIAL FACT
```

The bridge must equal the mathematically required accumulated prior-FY earnings / Reported-equity transformation and must never create a second copy of the same value.

## Proof G4 — Current vs Known viewpoint

Repeat G1-G3 for the Known view using `Recorded At <= T`.

A later Restatement may change Current presentation but not the originally-known presentation for a fixed T.

---

# 6. CORR-B5-04 — DIRECTLY RE-TEST THE FAILURE CASE FROM THE AUDIT

Use the Round-5 audit's exact example.

```text
Query date: 05-Jan-2025
Direct RE entering FY2024: 1000
FY2024 Revenue: 400
FY2024 Expense: 150
FY2024 CE: 250
Cash / Assets: 1250
FY2025 Revenue/Expense: 0
```

Show all three outputs separately.

### Expected Raw Cumulative TB

```text
Debit:  Assets 1250 + cumulative Expense 150 = 1400
Credit: Direct RE 1000 + cumulative Revenue 400 = 1400
PASS
```

### Expected FY2025-bounded activity/reporting account view

```text
Revenue FY2025 = 0
Expense FY2025 = 0
Balance Sheet remains cumulative
```

Explicitly state that this mixed-horizon account set alone is not the Raw Cumulative TB.

### Expected Reported Financial Statement / balanced presentation

```text
Reported RE = 1000 + 250 = 1250
Reported Equity = 1250 in the no-other-equity case
Assets = Liabilities + Reported Equity = 1250
```

If a balanced presentation TB is produced, show its derived bridge explicitly and tie it to 250 exactly once.

---

# 7. CORR-B5-05 — PROTECT FISCAL-YEAR BOUNDARIES FROM SILENT HISTORICAL RECLASSIFICATION

## Historical-safety gap

Round 4 makes `Elapsed` depend on Fiscal-Year Start/End boundaries and intentionally does not apply Entry `Recorded At` to those boundaries.

That is safe only if the calendar definition itself cannot be silently rewritten after it has governed historical accounting/reporting truth.

## Compare at least two models

### Option A — Boundary immutability after first authoritative use

A Fiscal-Year Start/End definition becomes immutable once any of the following occurs:

- a COMMITTED Entry belongs to that Fiscal Year;
- the Fiscal Year elapses;
- a report using that Fiscal Year is issued/consumed;
- a Period inside it is closed/consumed.

Future calendar changes create future Fiscal-Year definitions only.

### Option B — Versioned Fiscal Calendar

Fiscal-Year definitions are auditable/versioned conceptual facts.

Known-view reporting uses the calendar definition valid/known at T.
Current-view reporting uses the currently-authoritative calendar definition, subject to controlled change rules.

Historical re-partitioning must require explicit restatement/change-control semantics; never silent in-place mutation.

### Option C — another model

Allowed only if it proves equivalent or stronger historical reproducibility.

## Mandatory invariant

Create or revise an invariant equivalent to:

```text
A Fiscal-Year boundary that has governed authoritative accounting facts or an issued/consumed report cannot be changed in place in a way that silently changes historical classification or reporting.
```

If the chosen model permits a historical fiscal-calendar change, define:

- authority;
- audit evidence;
- effective time;
- historical Known view;
- current/restated view;
- impact on Fiscal-Year membership of existing Entries;
- whether the change is accounting-policy/configuration change or formal restatement;
- required Gate.

Do not invent Thai regulatory requirements if not evidenced.

---

# 8. CORR-B5-06 — TARGETED RED-TEAM REGRESSION

Create:

`B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md`

Personas at minimum:

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

### Test 1 — Mid first Fiscal Year cumulative Raw TB

Raw cumulative TB balances.

### Test 2 — Mid first Fiscal Year current-FY reporting activity

Raw cumulative TB and current-FY activity are numerically distinct but consistent.

### Test 3 — First day of second Fiscal Year

Use the exact 1000/400/150/250 example. Raw TB balances at 1400/1400; current-FY Revenue/Expense are zero; Reported Equity = 1250.

### Test 4 — Balanced presentation TB bridge

If supported, show the 250 derived bridge exactly once and prove the presentation balances.

### Test 5 — Delayed FiscalYearClosed declaration

All three outputs remain mathematically coherent before declaration.

### Test 6 — Declaration occurs with no financial facts

Raw TB and Reported Equity values do not change.

### Test 7 — Current-FY transaction after boundary

Raw cumulative TB, current-FY activity and Reported Financial Statements all reconcile.

### Test 8 — Later material Restatement of prior FY

Current Raw TB and Reported Equity change consistently; current-FY P&L remains unaffected when required by the prior IAS 8 design.

### Test 9 — Known view before Restatement

Original cumulative TB / Reported Equity remain exactly reproducible for fixed T.

### Test 10 — Multiple Equity accounts

No double count across Other Ledger Equity, Direct RE and accumulated elapsed-FY earnings.

### Test 11 — Migration opening balance

Migration opening facts do not double count with derived prior-FY accumulated earnings.

### Test 12 — Attempt to edit elapsed Fiscal-Year End Date

Chosen boundary-safety invariant must reject, version, or route the change through explicit controlled semantics. No silent historical rewrite.

### Test 13 — Attempt to edit Fiscal-Year boundary after a report was consumed

Original Known view remains reproducible.

### Test 14 — Authorized future Fiscal-Year calendar change

Future dates change as intended without reclassifying historical Entries.

### Test 15 — Multi-company calendar isolation

Changing Company A's future Fiscal Calendar cannot alter Company B's Fiscal-Year membership or reporting.

For every scenario record:

```text
Inputs
Timeline
Query Date D
Knowledge Cutoff T if applicable
Fiscal-Year Definition
Fiscal-Year Definition Status/Version
Raw Cumulative Ledger Components
Raw Cumulative TB Result
Current-FY Activity Components
Derived Presentation Components
Reported Equity Components
Reporting Viewpoint
Expected Equation
Actual Design Equation
Expected Result
Actual Result
PASS / FAIL
Finding
Disposition
```

Any CRITICAL/HIGH finding = HOLD and correct before claiming re-audit readiness.

---

# 9. CORR-B5-07 — PROPAGATE CORRECTIONS

Inspect and update every materially affected artifact, at minimum:

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
B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md
DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md
DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md
DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md
TEAM_B_STATUS.md
```

Create:

```text
CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md
B22_CORR_B5_TRIAL_BALANCE_AND_FISCAL_CALENDAR_REGRESSION.md
DOMAIN_01_ACCOUNTING_CORE_W_CORR_B5_CLOSURE_EVIDENCE.md
SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR5-001_CLOSURE.md
```

Preserve visible correction history.

Do not silently erase the Round-4 wording that caused M-AUD-11/12.

---

# 10. SIX TEAM B ASSUMPTIONS

Keep Boss-level assumptions visible unless this corrective round directly changes one.

Do NOT resolve them merely to make the Gate cleaner.

If Fiscal-Calendar governance creates a genuinely new Boss-level assumption, add it explicitly with evidence and Gate impact rather than hiding it inside prose.

---

# 11. CLEAN-ROOM CONTROL

Do not read raw Vendor implementation as target-design authority.

No Vendor ORM/table/field/class/method structure may enter the corrected design.

Required final result:

```text
Critical Vendor-Derived Design Risk = 0
```

Otherwise HOLD.

---

# 12. JIRA CONTROL

Jira item:

`ERPPLUS-100`

Current verified governance red flags:

```text
Assignee = UNASSIGNED
Due Date = TBD / EMPTY
Status = To Do
```

Do not invent or change assignee/due date without authority.

After successful Round-5 push, add a factual Jira comment containing:

- Round-5 findings addressed;
- Git content commit;
- closure commit;
- regression result;
- remaining assumptions/unknowns;
- `READY FOR CHATGPT INDEPENDENT RE-AUDIT` only if evidence supports it.

Do not self-transition to PMO/Final status.

---

# 13. GITHUB CONTROL

Commit controlled Markdown design/evidence artifacts only.

Recommended content commit:

`docs(state03): correct DOMAIN_01 trial balance and fiscal calendar semantics`

Push to branch:

`SMEsPlus`

Verify independently:

1. fresh `git fetch` + remote SHA comparison;
2. direct GitHub commit lookup.

If unrelated concurrent commits land on the shared branch:

- do not overwrite them;
- rebase/merge non-destructively only if safe;
- verify no Team-B evidence was lost;
- record the concurrent-commit situation in closure evidence.

---

# 14. FINAL EXECUTOR REPORT

Report exactly:

```text
CORR-B5-01 Raw Cumulative vs Category-Bounded Balance:
CORR-B5-02 MP-09 Semantic Repair:
CORR-B5-03 Trial Balance / Presentation Reconciliation:
CORR-B5-04 Direct Failure-Case Re-Test:
CORR-B5-05 Fiscal Calendar Historical Safety:
CORR-B5-06 Focused Regression:
CORR-B5-07 Artifact Propagation:
CORR-B5-08 Evidence/Push Verification:

Regression Tests Passed:
Regression Tests Failed:
New Critical Findings:
New High Findings:
Remaining Boss Assumptions:
Residual Team A Unknowns:
Clean-room Critical Risk:
Orphan Critical Decisions:
Jira Assignee:
Jira Due Date:
Git Content Commit:
Git Closure Commit:
Push Verified:

STATUS:
READY FOR CHATGPT INDEPENDENT RE-AUDIT
or
HOLD — <exact evidence-backed blocker>
```

---

# 15. STOP CONDITION

After verified remote push and Jira evidence comment:

STOP.

Do NOT:

- perform PMO verification;
- open Boss Final Gate;
- resolve Boss assumptions;
- start Development;
- start DOMAIN_02;
- declare Final Pass.

Next authority:

`ChatGPT Independent Re-Audit -> PMO Verification -> Boss Final Gate`

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

# /L999.999 — EXECUTE NOW
