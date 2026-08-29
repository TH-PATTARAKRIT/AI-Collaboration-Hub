# [SMEPLUS-26-08-29-MIG-B-D01-CORR3-001]
# DOMAIN_01 Team B Targeted Corrective Round 3 — Prior-Period Error / Restatement Compliance + Fiscal Close Reporting Semantics / L999.999

## 0. EXECUTION COMMAND

Continue in the **SAME Team B Claude session**.

This is a **TARGETED CORRECTIVE ROUND 3** only.

Do NOT restart B0–B19.
Do NOT restart Team A research.
Do NOT start DOMAIN_02.
Do NOT write production code.
Do NOT create physical DB/API implementation.
Do NOT perform PMO verification.
Do NOT self-approve Boss Final Gate.

Read the latest ChatGPT Independent Re-Audit Round 3 in full, correct only the affected accounting-design areas, run focused accounting-standard regression, commit/push/verify, then STOP for ChatGPT re-audit.

---

# 1. SOURCE OF TRUTH

Repository:

`TH-PATTARAKRIT/AI-Collaboration-Hub`

Branch:

`SMEsPlus`

Round-2 corrective content:

`06676d17e018397c262644d652fefc00639dab2a`

Round-2 closure/SHA update:

`5a07cab8272c12c90b817164aca1a1dd603071af`

Latest ChatGPT Independent Re-Audit Round 3:

`f6fb633fd141f45caf047bc94d75f84420e1cc6d`

Audit artifact:

`CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_O_TEAM_B_INDEPENDENT_REAUDIT_ROUND3.md`

Authoritative external accounting references to use for this corrective round:

- IFRS Foundation — IAS 8 Basis of Preparation of Financial Statements / prior-period errors.
- Thai Federation of Accounting Professions (TFAC) — TAS 8, Accounting Policies, Changes in Accounting Estimates and Errors.

Do not rely on blogs or model memory when primary/official accounting-standard evidence is available.

---

# 2. CURRENT GATE POSITION

```text
TEAM A DOMAIN_01: BOSS APPROVED WITH CONTROL
TEAM B ROUND 2: VERIFIED REMOTE
M-AUD-04 TEMPORAL MODEL: CLOSED AT REVIEWER LEVEL
M-AUD-05 ORDINARY-PERIOD DOUBLE COUNT: CORE CLOSED
M-AUD-06 PRIOR-PERIOD ERROR ACCOUNTING: FAIL / CRITICAL
M-AUD-07 FISCAL-CLOSE REPORTING SEMANTICS: FAIL / HIGH
PMO: HOLD
BOSS FINAL GATE: NOT OPEN
DEVELOPMENT: NOT AUTHORIZED
PRODUCTION: NOT AUTHORIZED
```

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.

---

# 3. CORR-B3-01 — DISTINGUISH ERROR FROM ESTIMATE

The design must stop treating all discoveries about prior periods as one generic correction case.

Define at conceptual/business-rule level at least:

```text
Current-Period Error
Prior-Period Error
Change in Accounting Estimate
Material Prior-Period Error
Immaterial Prior-Period Error
Retrospective Restatement
Impracticable Retrospective Determination
```

Mandatory distinctions:

1. **Prior-period error** arises from failure to use, or misuse of, reliable information that was available when prior financial statements were authorized.
2. **Change in accounting estimate** arises from new information/new developments and is not an error; IAS 8 treatment is prospective.
3. Material prior-period error is not allowed to default silently into current-period P&L.
4. Materiality requires judgment/policy; do NOT invent a numeric threshold.

Create explicit decision logic at conceptual level:

```text
DISCOVERY
  -> ERROR OR ESTIMATE?
  -> IF ERROR: CURRENT PERIOD OR PRIOR PERIOD?
  -> IF PRIOR PERIOD: MATERIAL?
  -> IF MATERIAL: RETROSPECTIVE RESTATEMENT UNLESS IMPRACTICABLE
  -> IF IMPRACTICABLE: EARLIEST PRACTICABLE RESTATEMENT PATH
```

Do not design SQL/workflow code.

---

# 4. CORR-B3-02 — TAS 8 / IAS 8 PRIOR-PERIOD ERROR TREATMENT

## Blocking defect

Round 2 stated that an error discovered after a fiscal year closes can normally be recognized through an ordinary current-dated Revenue/Expense Entry, while backdated Restatement is optional for comparative reporting.

That statement is not acceptable as a universal/default accounting treatment for a **material prior-period error**.

## Required correction

For material prior-period errors, blueprint behavior must support retrospective correction in accordance with IAS 8 / TAS 8, unless impracticable.

Conceptually cover:

- restating comparative amounts for prior period(s) presented in which the error occurred;
- if the error predates the earliest comparative period presented, restating opening balances of assets/liabilities/equity for the earliest comparative period presented;
- where retrospective determination is impracticable, applying the earliest practicable correction/restatement path;
- excluding material prior-period-error correction from current-period profit/loss merely because discovery occurred in the current period.

Do NOT hard-code a statutory threshold or accounting-policy choice not established by evidence.

Do NOT assume every prior-period error is material.

Do NOT assume every immaterial prior-period error has one universal treatment; preserve policy/judgment boundary.

---

# 5. CORR-B3-03 — PRESERVE BOTH ORIGINAL AND RESTATED HISTORY

Keep the Round-2 temporal architecture unless evidence proves it defective:

```text
Effective Date
Recorded At
Mode 1 — As Originally Known / Reported at T
Mode 2 — Current / Restated View
```

Use this model to guarantee both:

```text
ORIGINAL ISSUED REPORT
```

and

```text
FORMALLY RESTATED COMPARATIVE REPORT
```

remain independently reconstructable.

Mandatory properties:

1. Retrospective restatement does NOT erase the originally issued report.
2. A later restatement must have its own Recorded At timestamp and audit event.
3. Mode 1 for the original report remains immutable.
4. Mode 2 may show the corrected/restated comparative view.
5. Every report must state which reporting viewpoint/version it represents.
6. Restatement authorization must remain stricter than ordinary correction where appropriate.

Do not implement storage design.

---

# 6. CORR-B3-04 — RETAINED EARNINGS / OPENING COMPARATIVES

Design the conceptual treatment for a material prior-period error discovered after Fiscal-Year Close.

Must explicitly answer:

- When does retrospective restatement change a prior comparative P&L?
- When does it change retained earnings/equity?
- When must opening balances of the earliest comparative period be restated?
- How does current-period P&L avoid absorbing a material prior-period error?
- How is the current Balance Sheet reconciled to the restated prior-period truth?
- How do correction/restatement links remain additive and auditable?
- What happens if the period-specific effect is impracticable to determine?
- What happens if the cumulative effect is impracticable to determine?

Compare at least two conceptual approaches if there is a genuine design choice, but the final recommendation must remain compliant with the accounting-standard constraint.

No physical journal-schema design.

---

# 7. CORR-B3-05 — RESOLVE MP-11 / P&L CLOSING SEMANTIC CONTRADICTION

## Current inconsistency

Round-2 artifacts repeatedly state:

`Revenue/Expense are never reset by any posted action.`

But B08 MP-11 explicitly defines a Fiscal-Year Close Entry that:

- debits Revenue accounts;
- credits Expense accounts; and
- posts net Current Earnings to Equity / Retained Earnings.

These cannot both be stated as the same conceptual truth without clarification.

## Required work

Choose one coherent closing model.

### If MP-11 remains a real closing Entry

State precisely:

1. Prior Fiscal Year's P&L accounts are closed through MP-11.
2. New Fiscal Year's P&L begins at zero because the new Fiscal Year reporting horizon starts fresh; this is separate from the historical prior-year closing entry.
3. `Pre-Close FY P&L View` must remain reproducible after MP-11.
4. `Post-Close Ledger View` must be explicitly distinguished.
5. `New-FY P&L View` must be explicitly distinguished.
6. The closing Entry must not cause balance-sheet double counting.
7. Fiscal-year reports must not accidentally show zero Revenue/Expense merely because the closing Entry was included in the wrong report viewpoint.

### If Team B chooses a no-posted-close model

Remove MP-11 and prove how Current Earnings becomes formal Equity / Retained Earnings without violating double entry, historical reproducibility or reporting semantics.

Do NOT retain both conceptual models at once.

---

# 8. CORR-B3-06 — ACCOUNTING-STANDARD REGRESSION

Run a new focused Red-Team regression.

Personas at minimum:

```text
Senior Accountant
Thai CPA / Accounting Standards Reviewer
Financial Controller
External Auditor
Fiscal-Year Close Operator
Historical Reporting Reviewer
Migration Architect
SaaS Domain Architect
Clean-room Reviewer
```

Mandatory tests:

### Test 1 — Current-period error

Error occurs and is discovered before current-period financial statements are authorized.
Verify correction stays current-period and is fully auditable.

### Test 2 — Material prior-period error discovered next year

Verify:

- NOT defaulted into current-period P&L;
- comparative amounts restated retrospectively;
- original issued report still reproducible;
- restated report separately reproducible.

### Test 3 — Error before earliest comparative presented

Verify opening balances of assets/liabilities/equity for the earliest comparative period can be restated conceptually where required.

### Test 4 — Impracticable period-specific effect

Verify earliest practicable retrospective treatment is represented without fabricated precision.

### Test 5 — Impracticable cumulative effect

Verify the design does not falsely claim full retrospective precision.

### Test 6 — Change in accounting estimate

Verify prospective treatment; do not route through prior-period-error Restatement logic.

### Test 7 — Immaterial prior-period error

Do not invent a materiality threshold. Verify the blueprint routes to accounting-policy/judgment rather than silently treating it as material or immaterial.

### Test 8 — Original vs restated comparative

Same business date D, different reporting viewpoints. Both values must be reconstructable and explicitly labeled.

### Test 9 — Fiscal-Year Close pre-close P&L

Use worked numbers. Verify full FY Revenue, Expense and Current Earnings before close.

### Test 10 — Fiscal-Year Close post-close ledger

Use the same numbers. Verify closing mechanics exactly, including Equity/Retained Earnings.

### Test 11 — New Fiscal-Year P&L

Verify new FY starts with zero current-FY Revenue/Expense without destroying prior-year report reproducibility.

### Test 12 — Restatement after Fiscal-Year Close

Material prior-period error affects prior-year Expense by an illustrative amount. Show original prior-year report, restated comparative, retained earnings/equity effect and current-year P&L treatment.

### Test 13 — Migration opening balance

Verify migration opening balance remains a distinct migration event and is not confused with Fiscal-Year Close or retrospective restatement.

### Test 14 — Correction-of-restatement

Verify additive linkage and version history remain reconstructable.

### Test 15 — Multi-company isolation

A restatement in Company A must not affect Company B.

For every test record:

```text
Inputs
Accounting Classification
Materiality Status
Timeline
Effective Date
Recorded At
Original Report View
Restated Report View
Current-Period P&L Effect
Equity / Retained Earnings Effect
Standard Principle Tested
Expected Result
Actual Design Result
PASS / FAIL
Finding
Disposition
```

Any CRITICAL/HIGH defect = HOLD and correct before audit readiness.

---

# 9. CORR-B3-07 — PROPAGATE CORRECTIONS

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
B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md
DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md
DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md
DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md
TEAM_B_STATUS.md
```

Create:

```text
CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md
B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md
DOMAIN_01_ACCOUNTING_CORE_Q_CORR_B3_CLOSURE_EVIDENCE.md
SESSION_ARCHIVE/SESSION_SMEPLUS-26-08-29-MIG-B-D01-CORR3-001_CLOSURE.md
```

Preserve visible correction history.

Do not silently rewrite or delete the previous flawed reasoning.

---

# 10. SIX BOSS-LEVEL ASSUMPTIONS

Keep unresolved assumptions visible unless this corrective round necessarily narrows one.

Current controlled set remains:

1. Rounding method.
2. Period/Fiscal-Year close semantics — may be narrowed by this correction, but do not Boss-approve it.
3. COA template/instance.
4. Broad audit tamper-evidence scope.
5. Correction shape flexibility.
6. CO-02/CO-06 coupling.

Do NOT ask Boss to approve them during this executor round.

Do NOT resolve them merely to make the pack appear complete.

---

# 11. CLEAN-ROOM CONTROL

Do not use raw Vendor implementation as target-design authority.

Accounting-standard sources are allowed and preferred.

No Vendor ORM/table/field/class/method structure may enter the target design.

Required final check:

```text
Critical Vendor-Derived Design Risk = 0
```

Otherwise HOLD.

---

# 12. GITHUB CONTROL

Commit controlled Markdown design/evidence artifacts only.

Recommended commit message:

`docs(state03): correct DOMAIN_01 prior-period error and fiscal close semantics`

Push to:

```text
TH-PATTARAKRIT/AI-Collaboration-Hub
branch SMEsPlus
```

Verify independently:

1. `origin/SMEsPlus`
2. direct GitHub commit lookup

Record remote SHA.

---

# 13. FINAL EXECUTOR REPORT

Report exactly:

```text
CORR-B3-01 Error vs Estimate Classification:
CORR-B3-02 IAS8/TAS8 Prior-Period Error Treatment:
CORR-B3-03 Original vs Restated History:
CORR-B3-04 Retained Earnings / Opening Comparative Treatment:
CORR-B3-05 Fiscal Close / MP-11 Semantics:
CORR-B3-06 Accounting-Standard Regression:
CORR-B3-07 Artifact Propagation:
CORR-B3-08 Evidence / Push Verification:

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

STATUS:
READY FOR CHATGPT INDEPENDENT RE-AUDIT
or
HOLD — <exact blocker>
```

---

# 14. STOP CONDITION

After remote push verification:

STOP.

Do NOT:

- perform PMO verification;
- open Boss Final Gate;
- resolve Boss assumptions;
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