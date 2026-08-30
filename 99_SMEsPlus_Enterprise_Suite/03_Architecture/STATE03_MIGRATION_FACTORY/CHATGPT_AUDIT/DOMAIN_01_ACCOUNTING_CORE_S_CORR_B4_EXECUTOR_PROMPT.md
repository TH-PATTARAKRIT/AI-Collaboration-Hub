# [SMEPLUS-26-08-30-MIG-B-D01-CORR4-001]
# DOMAIN_01 Team B Targeted Corrective Round 4 — Reported Equity Mathematics, Fiscal-Boundary Continuity & Viewpoint-Safe Retained Earnings / L999.999

## 0. EXECUTION COMMAND

Continue in the **SAME Team B Claude session**.

This is **TARGETED CORRECTIVE ROUND 4 ONLY**.

Do NOT restart B0–B20.
Do NOT restart Team A research.
Do NOT start DOMAIN_02.
Do NOT write production code.
Do NOT create physical DB/API implementation.
Do NOT perform PMO verification.
Do NOT self-approve Boss Final Gate.

Read the latest ChatGPT Independent Re-Audit Round 4 in full. Correct only the affected reporting-equity / fiscal-boundary / temporal-viewpoint mathematics, run focused regression, commit/push/verify, then STOP for ChatGPT re-audit.

---

# 1. SOURCE OF TRUTH

Repository:

`TH-PATTARAKRIT/AI-Collaboration-Hub`

Branch:

`SMEsPlus`

Round-3 corrective content:

`478f94777397a83aaeef4f7cd6e3559f750634ba`

Round-3 closure/SHA update:

`19dd7cc906ac0b995ee1642a6f83b38943673996`

Latest ChatGPT Independent Re-Audit Round 4:

`9c0a3f2d179994a20f01db16d5713989a78c0b2a`

Audit artifact:

`CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_R_TEAM_B_INDEPENDENT_REAUDIT_ROUND4.md`

Jira control item:

`ERPPLUS-100`

Read the audit before editing any design artifact.

---

# 2. CURRENT GATE POSITION

```text
TEAM A DOMAIN_01: BOSS APPROVED WITH CONTROL
TEAM B ROUND 3: VERIFIED REMOTE
M-AUD-06 IAS 8 PRIOR-PERIOD ERROR: CLOSED AT DOMAIN-DESIGN LEVEL
M-AUD-07 POSTED-CLOSE CONTRADICTION: CORE CLOSED
M-AUD-08 REPORTED-EQUITY MATHEMATICS: FAIL / CRITICAL
M-AUD-09 FISCAL-BOUNDARY CLOSE-TIMING GAP: FAIL / CRITICAL
M-AUD-10 VIEWPOINT-AWARE REPORTED RE: FAIL / HIGH
CLEAN-ROOM: REVIEW PASS
PMO: HOLD
BOSS FINAL GATE: NOT OPEN
DEVELOPMENT: NOT AUTHORIZED
PRODUCTION: NOT AUTHORIZED
JIRA ASSIGNEE: UNASSIGNED
JIRA DUE DATE: TBD
```

Do not invent Jira owner or due date. Preserve them as governance red flags unless separately authorized by Boss/PMO.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

---

# 3. CORR-B4-01 — SEPARATE RAW LEDGER IDENTITY FROM REPORTED FINANCIAL-STATEMENT IDENTITY

## Blocking defect

The current MP-02 proof still reasons from every committed ledger line across all time, but the Round-3 reporting model uses mixed horizons:

- Asset / Liability / ledger Equity = all-time;
- Revenue / Expense = current Fiscal Year;
- Reported Retained Earnings = direct RE ledger balance + accumulated prior closed-FY earnings.

Those are not the same mathematical population used in the original proof.

## Required work

Define two separate conceptual identities.

### A. Raw Ledger Identity

One consistent horizon over all raw ledger account categories.

Example conceptual form:

```text
RawAssets + RawExpenses = RawLiabilities + RawEquity + RawRevenue
```

The exact notation may differ, but every term must use the same ledger horizon and same temporal viewpoint.

### B. Reported Financial-Statement Identity

Define the reporting transformation explicitly.

At minimum identify:

```text
Other Ledger Equity
Direct Retained-Earnings Ledger Balance
Closed-FY Accumulated Earnings
Completed-but-Unclosed FY Earnings, if applicable
Current Fiscal-Year Earnings
Reported Retained Earnings
Reported Equity
```

Then prove the reporting equation from the raw-ledger identity.

Do NOT claim the old MP-02 proof is unchanged.

Do NOT use implementation/database fields.

---

# 4. CORR-B4-02 — ELIMINATE DIRECT RETAINED-EARNINGS DOUBLE COUNTING

## Current contradiction

B07 §1e defines:

```text
Reported Retained Earnings =
  Direct RE ledger balance
  + accumulated closed-FY Current Earnings
```

B08 MP-02 currently describes:

```text
Reported Equity = Equity(ledger, all-time) + Reported Retained Earnings
```

But the direct Retained-Earnings ledger balance is already inside the Equity account category unless explicitly excluded.

## Mandatory proof case

Use B20's own numbers:

```text
Direct RE ledger balance entering FY2024 = 1000
FY2024 Current Earnings = 250
Expected Reported RE after FY2024 = 1250
Expected total Reported Equity in a no-other-equity scenario = 1250
NOT 2250
```

Define a non-overlapping decomposition.

A valid conceptual relationship may resemble:

```text
OtherLedgerEquity = RawLedgerEquity EXCLUDING the designated RE direct-balance component
ReportedEquity = OtherLedgerEquity + ReportedRetainedEarnings
```

or another independently proven model.

The sets must be mutually exclusive. No term may be counted twice.

---

# 5. CORR-B4-03 — FISCAL-BOUNDARY CONTINUITY MUST NOT DEPEND ON OPERATOR CLOSE TIMING

## Blocking scenario

A Fiscal Year can end before the operational `FiscalYearClosed` action is performed.

Using B20's example:

```text
Direct RE entering FY2024 = 1000
FY2024 Current Earnings = 250
Cash at 31-Dec-2024 = 1250
```

Assume FY2024 ends 31-Dec but operational close is executed 15-Jan-2025.

At 05-Jan-2025 the reporting equation must remain correct.

The design may NOT lose the FY2024 earnings merely because the operator has not yet executed the close declaration.

## Compare at least three conceptual options

### Option A — Boundary-driven accumulated earnings

Completed Fiscal-Year earnings enter reported accumulated earnings at the fiscal boundary automatically. `FiscalYearClosed` is governance/lock status only.

### Option B — Completed-but-Unclosed Earnings component

Until operational close occurs, completed prior-FY earnings remain a separate reported-equity component. On close declaration they reclassify conceptually into closed/retained earnings with **zero change to total Reported Equity**.

### Option C — Mandatory atomic close before next FY opens

Allowed only if independently justified as a hard domain invariant and tested for operational/reporting consequences. Do not select it only to preserve current wording.

## Mandatory invariant

If no new financial facts occur:

```text
Reported Equity immediately before close declaration
=
Reported Equity immediately after close declaration
```

Close declaration may change control status/classification, but must not create or destroy economic value.

Explicitly answer:

- Can the new FY accept postings before prior FY operational close?
- What does the Balance Sheet show during that interval?
- What does YTD P&L show?
- What equity component contains the prior completed year's earnings?
- Does the close action change a number or only status/classification?
- What audit event records the transition?

---

# 6. CORR-B4-04 — MAKE REPORTED RETAINED EARNINGS / EQUITY VIEWPOINT-AWARE

## Current gap

B07 §1e defines Reported Retained Earnings using MP-09 Mode 2 only.

But B20 Test 8 relies on an `as originally known` Reported RE value under Mode 1.

The formula must define this behavior, not leave it implicit in the regression.

## Required conceptual functions

Support at least the equivalent of:

```text
ReportedRE_Current(C, D)
ReportedRE_Known(C, D, T)
ReportedEquity_Current(C, D)
ReportedEquity_Known(C, D, T)
```

or one generic viewpoint-parameterized formula.

### Current / Restated view

- uses all currently-known legitimate facts;
- may reflect later Restatements;
- prior-year earnings use Mode 2 semantics.

### As Originally Known / Reported view

- uses only facts with `Recorded At <= T`;
- must also evaluate any relevant close/declaration/classification state as known at T;
- later Restatements cannot change the result;
- must reproduce the originally-issued Balance Sheet and Equity figure exactly.

Do not blend these views.

Every report consuming Reported RE / Reported Equity must state its viewpoint.

---

# 7. CORR-B4-05 — RE-PROVE MP-02 / MP-09 / MP-11 INTERACTION

Rebuild the mathematical proof after the corrections.

At minimum prove:

## Proof A — Raw ledger

Every balanced Entry implies raw ledger debit/credit equality over a common horizon.

## Proof B — Reporting transformation

Partition prior completed Fiscal-Year Revenue/Expense from current-FY Revenue/Expense.

Show how prior completed net earnings move into the **reporting representation** of equity without a posted close Entry and without double counting.

## Proof C — Current FY

```text
Assets + CurrentFY Expenses
=
Liabilities + Reported Equity + CurrentFY Revenue
```

using non-overlapping definitions.

## Proof D — Historical Mode 1

Same equation must hold using facts and reporting classifications known at T.

## Proof E — Restated Mode 2

Same equation must hold after legitimate prior-period Restatement.

## Proof F — Fiscal close declaration

With no financial facts added:

```text
Total Reported Equity before declaration
=
Total Reported Equity after declaration
```

Only status/classification may change.

## Proof G — Trial Balance vs Financial Statements

Explicitly distinguish:

```text
Raw Ledger / Raw Trial Balance
```

from

```text
Reported / Adjusted Presentation View
```

If a synthetic/derived presentation line is conceptually required for Reported Retained Earnings, state it as a reporting concept — not a stored/posted financial fact.

The design must state how both views tie back to the same underlying balanced ledger.

---

# 8. CORR-B4-06 — TARGETED RED-TEAM REGRESSION

Create `B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md`.

Personas at minimum:

```text
Senior Accountant
Financial Controller
External Auditor
Fiscal-Year Close Operator
Historical Reporting Reviewer
Migration Architect
SaaS Domain Architect
Accounting Systems Architect
Clean-room Reviewer
```

Run at least these 15 scenarios.

### Test 1 — Direct RE + one completed FY

Direct RE = 1000, FY earnings = 250. Prove Reported Equity = 1250, not 2250.

### Test 2 — Multiple Equity accounts

Include Share Capital, Other Equity, direct RE and one closed-FY earnings term. Prove every component counted exactly once.

### Test 3 — Raw Trial Balance before fiscal boundary

Use full raw P&L and Equity account populations. Raw TB must balance.

### Test 4 — Reported Financial Statements before fiscal boundary

Use same facts. Reported equation must tie to Raw TB through the documented transformation.

### Test 5 — Fiscal year ends; close action delayed 15 days

At D = Jan 5, prior FY completed but not operationally closed. Reported equation must remain correct.

### Test 6 — Close declaration occurs Jan 15

No financial Entry. Total Reported Equity Jan 14 vs Jan 15 must be identical absent new financial facts.

### Test 7 — New-FY transaction before prior-FY operational close

If permitted by the selected model, post current-FY activity and prove both YTD P&L and Reported Equity remain correct. If prohibited, prove the invariant/operational consequence and justify it.

### Test 8 — Original issued Balance Sheet after later Restatement

Use `ReportedEquity_Known(C,D,T)` or equivalent. Later Restatement must not alter the original value.

### Test 9 — Current/restated Balance Sheet after Restatement

Same D, current viewpoint. Reported Equity must reflect the Restatement.

### Test 10 — Close declaration recorded after historical report T

Mode 1 must reconstruct what was actually knowable at T without importing a later operational status.

### Test 11 — Material prior-period error

Retain Round-3 IAS 8 treatment. Prove Reported Equity change and zero inappropriate current-period P&L effect.

### Test 12 — Impracticability adjustment

Verify opening-equity adjustment and counterpart remain balanced and viewpoint-safe.

### Test 13 — Migration opening balance

Migration opening must not double-count with derived accumulated earnings.

### Test 14 — Correction of Restatement

Mode 1 original remains fixed; Mode 2 updates; Reported Equity remains balanced.

### Test 15 — Multi-company isolation

Company A fiscal-close/restatement status must not alter Company B's Reported Equity.

For every scenario record:

```text
Inputs
Timeline
Fiscal-Year State
Operational Close State
Effective Date
Recorded At
Raw Ledger Components
Raw TB Result
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

# 9. CORR-B4-07 — PROPAGATE CORRECTIONS

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
B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md
DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md
DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md
DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md
TEAM_B_STATUS.md
```

Create:

```text
CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md
B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md
DOMAIN_01_ACCOUNTING_CORE_T_CORR_B4_CLOSURE_EVIDENCE.md
SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-30-MIG-B-D01-CORR4-001_CLOSURE.md
```

Preserve visible correction history.

Do not silently rewrite prior flawed reasoning.

---

# 10. PRESERVE ROUND-3 IAS 8 CORRECTIONS

Do NOT regress `M-AUD-06` while fixing the math.

Keep explicit distinctions among:

```text
Current-Period Error
Change in Accounting Estimate
Material Prior-Period Error
Immaterial Prior-Period Error
Retrospective Restatement
Impracticability
```

Material prior-period errors must not default into current-period P&L.

Do not invent a materiality threshold.

Current TAS 8 primary-text provenance remains a separate evidence-confidence matter; do not fabricate Thai clauses.

---

# 11. SIX BOSS-LEVEL ASSUMPTIONS

Keep unresolved assumptions visible unless Round 4 necessarily narrows one.

Current set:

1. Rounding method.
2. Period/Fiscal-Year close semantics.
3. COA template/instance.
4. Broad audit tamper-evidence scope.
5. Correction shape flexibility.
6. CO-02/CO-06 coupling.

Do NOT ask Boss to resolve them during this executor round.

Do NOT resolve them only to make the evidence pack appear complete.

---

# 12. CLEAN-ROOM CONTROL

No raw Vendor implementation may become target-design authority.

No Vendor ORM/table/field/class/method structure may enter the design.

Accounting principles and official standards are allowed evidence.

Required final result:

```text
Critical Vendor-Derived Design Risk = 0
```

Otherwise HOLD.

---

# 13. JIRA / GOVERNANCE CONTROL

Jira:

`ERPPLUS-100`

Current verified governance facts:

```text
Status: To Do
Assignee: UNASSIGNED
Due Date: TBD / empty
```

Do not invent or assign a person/date without authorization.

At the end, add an evidence comment containing:

- Round-4 content commit SHA;
- closure SHA;
- corrected M-AUD-08/09/10 status;
- B21 regression result;
- remaining assumptions/unknowns;
- explicit STOP for ChatGPT re-audit.

Do not transition Jira status to PMO-ready or Done.

---

# 14. GITHUB CONTROL

Commit controlled Markdown design/evidence artifacts only.

Recommended commit message:

`docs(state03): correct DOMAIN_01 reported equity and fiscal-boundary mathematics`

Push to:

```text
TH-PATTARAKRIT/AI-Collaboration-Hub
branch SMEsPlus
```

Verify independently:

1. `origin/SMEsPlus`
2. direct GitHub commit lookup

Record exact remote SHA.

No raw source.
No DB dump.
No customer raw data.
No credentials.
No production code.

---

# 15. FINAL EXECUTOR REPORT

Report exactly:

```text
CORR-B4-01 Raw vs Reported Identity:
CORR-B4-02 Direct RE Double Count:
CORR-B4-03 Fiscal-Boundary Continuity:
CORR-B4-04 Viewpoint-Aware Reported RE:
CORR-B4-05 Mathematical Re-Proof:
CORR-B4-06 Regression:
CORR-B4-07 Propagation:
CORR-B4-08 Evidence/Push:

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

# 16. STOP CONDITION

After verified remote push and Jira evidence comment:

STOP.

Do NOT:

- perform PMO verification;
- open Boss Final Gate;
- approve Boss assumptions;
- invent Jira owner/due date;
- start development;
- start DOMAIN_02;
- declare Final Pass.

Next authority:

```text
ChatGPT Independent Re-Audit
→ PMO Verification
→ Boss Final Gate
```

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

# /L999.999 — EXECUTE NOW