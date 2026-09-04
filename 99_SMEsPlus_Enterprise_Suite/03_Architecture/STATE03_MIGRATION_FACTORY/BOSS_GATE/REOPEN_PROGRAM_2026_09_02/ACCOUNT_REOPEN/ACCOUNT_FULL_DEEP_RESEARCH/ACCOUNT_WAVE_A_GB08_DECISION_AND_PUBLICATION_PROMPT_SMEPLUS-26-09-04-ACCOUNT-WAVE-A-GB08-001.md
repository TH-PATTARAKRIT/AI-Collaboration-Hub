# [SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001]
# ACCOUNT WAVE A — GB-08 Decision Package, Evidence Publication & Hold-State Cleanup / VERY DEEP / L99999.99999

Model: `Claude Opus 5 (Extra)`

Parent Session:
`[SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001] ACCOUNT WAVE A — Final Closure, Evidence Publication & Wave B Readiness / VERY DEEP / L99999.99999`

Program:
`[SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001]`

Boss has approved the `git push` permission path.

Boss still requires a clear, evidence-backed explanation and decision package for `GB-08` before any Wave A Final Gate decision or Wave B movement.

Boss = Sole Final Approver.
No Evidence = No Progress.
Never Skip Gate.
Do not start Wave B.
Do not implement.
Do not modify source code.
Do not merge.
Do not deploy.
Do not self-declare PASS.

## 1. Current Known State

From the latest Wave A Final Closure evidence:

- This is still `Wave A`, not Wave B.
- `Gate recommendation = RECOMMEND HOLD`.
- `CONDITIONAL PASS` is unavailable because tolerance-zero boundaries remain unresolved.
- `FAIL` is not recommended because the semantic model has not been substantively disproved.
- `MCU-04 = VERIFIED DEFECT`.
- `GB-08 = BOSS DECISION REQUIRED`.
- `% Board / % STATE / % STEP` is not calculable from a verified denominator.
- `Wave B = NOT READY — EXACT DEPENDENCIES`.
- The research package must not be treated as approved, closed, or canonical until Boss issues a Final Gate decision.

## 2. First Action — Evidence Publication

Because Boss has approved push permission, perform the authorized publication flow:

1. Execute the actual `git push` for the Wave A package branch.
2. Re-read the published branch from origin.
3. Verify that the branch, HEAD commit, manifest, and decision package are accessible from origin.
4. Only after origin verification, post one accurate Jira evidence comment to `ERPPLUS-138`.
5. Return:
   - repository
   - branch
   - origin URL
   - HEAD commit SHA
   - manifest digest
   - Jira key
   - Jira comment/link
   - publication status

If push or Jira posting still fails, report:
`EVIDENCE PUBLICATION NOT VERIFIED`

Do not fabricate a published link or Jira update.

## 3. GB-08 — Required Explanation

Create a Boss-readable explanation of `GB-08` using only verified evidence.

At minimum explain:

1. What `GB-08` is.
2. Why `GB-08` is a Boss decision rather than a purely technical finding.
3. Which source roots were searched.
4. Why root enumeration changed from earlier counts to the current bounded count.
5. What the 22-root enumeration proves and does not prove.
6. What `5/22 roots` means.
7. Why the root originally researched by Wave A did not show the behavior.
8. Why this creates downstream risk.
9. Which Accounting / SaaS / migration / reporting semantics are affected.
10. Why this blocks Wave A Final Gate and Wave B readiness.

Use this framing unless contradicted by evidence:

`GB-08 asks how SMEsPlus should define canonical FX-rate ownership and rate-selection precedence when reference source roots / versions show different branch/company rate behavior.`

## 4. GB-08 — Four Options

Locate and extract the four GB-08 options already stated in the Wave A package.

If the four options exist in a local package file, cite the file path and line/section.

If they do not exist as a formal register, create a new explicit `GB08_BOSS_DECISION_OPTIONS.md` from verified evidence only.

Each option must include:

- Option ID
- Description
- Evidence supporting it
- Evidence against it
- Business impact
- Accounting impact
- SaaS / tenant / company impact
- Migration impact
- Reporting impact
- Wave B impact
- AAS+ view
- PMO view
- Risk level
- What Boss is deciding
- What remains unknown

Do not choose on behalf of Boss.

## 5. Minimum Option Set If Not Already Formalized

If the prior package does not contain formal options, use this minimum evidence-safe option structure and refine it from the package evidence:

### Option 1 — Company-Specific Rate Authority
FX rate ownership is company-scoped. Company-specific rate wins. Global/null-company rate may be used only as explicitly allowed fallback and must never override company-specific rate.

### Option 2 — Branch/Operating-Unit Preference Within Company Boundary
Branch or operating-unit rate preference may exist only inside an owning company boundary. It must never cross tenant/company boundary. Branch hierarchy and inheritance rules must be explicit.

### Option 3 — Tenant-Standard Global Rate With Controlled Override
Tenant-level standard FX rate is canonical by default. Company/branch override is allowed only through explicit configuration, audit trail, and deterministic precedence.

### Option 4 — No Implicit Preference / Require Explicit Rate Resolution
System must not infer ambiguous rate precedence. Posting or revaluation requiring FX rate must block until the applicable rate context is explicit.

These are candidate decision options only. They must be reconciled against actual package evidence and corrected if inconsistent.

## 6. AAS+ / PMO Recommendation Framework

Prepare a recommendation, but keep it clearly separate from Boss decision.

AAS+ should evaluate:

- clean-room semantic correctness
- accounting event integrity
- source-of-truth stability
- event ownership
- FX valuation correctness
- future architecture risk

PMO should evaluate:

- evidence sufficiency
- gate impact
- implementation timing risk
- downstream Wave B risk
- Jira/GitHub traceability
- auditability
- whether the decision can safely move to Wave B

Recommendation must be one of:

- `RECOMMEND OPTION 1`
- `RECOMMEND OPTION 2`
- `RECOMMEND OPTION 3`
- `RECOMMEND OPTION 4`
- `RECOMMEND HOLD — EVIDENCE INSUFFICIENT`
- `RECOMMEND BOSS BUSINESS RULING BEFORE RESEARCH CAN CONTINUE`

## 7. Decision Boundary Rule

Do not freeze SMEsPlus design to any reference-version implementation.

Reference implementation behavior is evidence, not design authority.

The Boss decision must freeze the SMEsPlus business semantic and control boundary, not automatically adopt v18, v19, or any source-root behavior.

Any downstream design must be clean-room and independently justified from:

`Business Fact -> Accounting Semantic -> Control Requirement -> SaaS Boundary -> Source of Truth -> Event Ownership -> Failure/Correction Rule`

## 8. Output Required

Produce and publish at minimum:

1. `ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md`
2. `ACCOUNT_WAVE_A_GB08_OPTIONS_REGISTER.md`
3. `ACCOUNT_WAVE_A_GB08_AAS_PLUS_PMO_RECOMMENDATION.md`
4. `ACCOUNT_WAVE_A_GB08_EVIDENCE_TRACE.md`
5. `ACCOUNT_WAVE_A_GB08_DOWNSTREAM_DEPENDENCY_MAP.md`
6. Update Final Gate Report with GB-08 status.
7. Update Jira evidence comment only after origin publication verification.

## 9. Stop Condition

Stop at exactly one of:

`GB-08 DECISION PACKAGE READY FOR BOSS`

or

`GB-08 HOLD — EVIDENCE PACKAGE NOT PUBLISHED`

or

`GB-08 HOLD — OPTIONS NOT SUPPORTED BY EVIDENCE`

Do not start Wave B.
Do not implement.
Do not declare Wave A closed.
Do not declare PASS.

BEGIN NOW.
