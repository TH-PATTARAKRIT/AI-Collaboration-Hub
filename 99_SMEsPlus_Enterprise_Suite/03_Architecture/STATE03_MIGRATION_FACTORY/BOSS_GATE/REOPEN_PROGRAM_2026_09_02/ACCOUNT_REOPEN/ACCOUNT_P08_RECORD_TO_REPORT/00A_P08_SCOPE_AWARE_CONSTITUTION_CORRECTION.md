# P08 — SCOPE-AWARE CONSTITUTION CORRECTION (ADOPTED IN-FLIGHT)

Correction ID: `SMEPLUS-26-09-04-ACC-REV2-CORR1`
Received: mid-execution of session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`
Applies to: current P01–P11 execution
Action taken: **adopted as a controlled correction.** No reset. No restart from L1. No evidence discarded. No completed work repeated without material delta.

## 1. What the correction supersedes

Any prior wording — in this session's bootstrap, in imported prior evidence, or in a governing ruling as previously read — implying that **Tenant Context + Company Context are mandatory for every operation**.

That blanket reading is withdrawn. The canonical rule is `SCOPE-AWARE EVERYWHERE`.

## 2. Canonical scope model now in force for P08

| Scope | Tenant context | Company context |
|---|---|---|
| `PLATFORM` | not required | not required |
| `TENANT` | **mandatory** | not required, unless the specific operation is company-scoped |
| `COMPANY` | **mandatory** | **mandatory** |

`MISSING REQUIRED SCOPE = DENY`
`REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`

Definitions adopted verbatim: Tenant = security/customer boundary. Company = legal/accounting/business boundary.
`OWNERSHIP ≠ AVAILABILITY`. `OWNERSHIP SCOPE ≠ OPERATIONAL SCOPE ≠ FINANCIAL SCOPE ≠ REFERENCE SCOPE`. `MULTI-TENANT MEMBERSHIP ≠ MULTI-TENANT EXECUTION CONTEXT`. Unrelated independent companies are separate tenants by default.

## 3. Effect on GB-08 (FX Boss ruling)

GB-08 states FX rate resolution "must execute under Current Tenant + Current Company context". Under the corrected model this is **not** withdrawn, because an FX accounting rate applied to a posting produces a financial effect and a financial effect is owned by a company. GB-08's rule is therefore re-expressed, not superseded:

> The **application of a rate to a posting** is `COMPANY` scope — tenant and company both mandatory.
> The **rate master record itself** is not automatically company scope. Its scope must be determined from business semantics, and P08 finds it is not one scope but three candidate scopes. See `01_P08_SCOPE_OWNERSHIP_MATRIX.md` rows `SC-FX-01`..`SC-FX-04`.

This distinction was previously collapsed by the "tenant+company everywhere" reading, and collapsing it is precisely what produced R8's finding that the benchmark resolves rates at an ancestor company while writing them at an operating company. Under scope-aware analysis that is not merely a defect — it is an **unstated scope choice**, and P08 now records it as one.

## 4. What was materially affected in work already completed

Findings produced before the correction were written against the benchmark's own company model, and classified the absence of a tenant dimension as a gap. That classification is over-constrained wherever the object in question is not company-scoped. Each materially affected finding is re-analysed in `01_P08_SCOPE_OWNERSHIP_MATRIX.md` §4 and recorded in `21_P08_REVISION_LOG.md` §2 with the required six columns: original finding → scope assumption used → why over-constrained → correct scope analysis → updated classification → architecture and cross-process impact.

Findings **not** materially affected — the posting-engine integrity findings, the entry-identity findings, the close-mechanism findings, the report-derivability findings — are unchanged and were **not** re-run. Their evidence, citations, checkpoints and commit lineage are preserved intact.

## 5. Cross-process posture

P08 does not stop for another process's scope determination. Every unresolved cross-process scope question is recorded as `PEER DEPENDENCY OPEN` in `18_P08_DEPENDENCY_REGISTER.md` and work continues.

Where scope cannot be resolved from business semantics, source evidence, runtime evidence, database evidence or the legal/accounting boundary, the item is recorded `HOLD — SCOPE EVIDENCE REQUIRED` and unaffected work continues.

## 6. Autonomy

Boss interaction is Final Gate only. This session asks no confirmation, pauses at no intermediate checkpoint, and presents no scope menu for selection. It resolves scope by evidence and records what it cannot resolve.

Terminal state remains the session's original objective — a handoff prepared for Core Accounting Reconciliation. **The session declares no readiness of any kind**: no `PASS`, no approval, no sign-off, no freeze, no merge and no implementation authority. *(The draft used a readiness label here, which this session's own governance prohibits; corrected after independent review.)*
