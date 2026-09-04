# SMEsPlus Canonical Evidence Acquisition Flow Standard

Standard ID: `SMEPLUS-EVIDENCE-ACQ-001`
Status: `BOSS APPROVED / PROJECT-WIDE MANDATORY`
Effective Date: `2026-09-04`
Scope: All SMEsPlus modules, domains, Very Deep Research sessions, and State-level research/verification activities.
Authority: Boss — Sole Final Approver.

## 1. Constitutional Position

This standard governs how SMEsPlus obtains, validates, correlates, challenges, classifies, and preserves research evidence before any conclusion may be relied upon by AAS+, PMO, Architecture, Functional Design, Engineering, Testing, Migration, or downstream State work.

It operates together with:

- `No Evidence = No Progress`
- `Never Skip Gate`
- SMEsPlus Very Deep Research 8-Criteria Universal Exit Constitution
- SMEsPlus Deep Research Method Convergence Standard
- SMEsPlus Negative Claim Controls

Core principle:

> Reference source is evidence, not authority.
> Verified business semantic is the design authority.

## 2. Canonical Acquisition Flow

Every controlled Very Deep Research activity SHALL follow this flow:

`Discover Population`
→ `Bound Scope`
→ `Enumerate`
→ `Collect Evidence`
→ `Correlate Across Layers`
→ `Challenge Contradictions`
→ `Independent Reproduce`
→ `Classify Fact / Inference / Unknown`
→ `Preserve Evidence Lineage`
→ `Boss Decision where semantic choice remains`

No stage may be silently skipped.

## 3. Stage A — Discover Population

Before deep interpretation, identify the actual research universe where applicable:

- source roots / versions
- modules / manifests
- models / entities
- functions / material code paths
- database schemas / tables / constraints
- menus / screens / fields / actions
- configuration surfaces
- runtime paths
- reports
- security/access paths
- integrations
- scheduled jobs
- business events
- accounting/operational events
- tenant/company boundaries
- migration/historical paths
- failure/exception paths

Do not assume a single source root, version, module tree, or UI surface represents the complete system.

## 4. Stage B — Bound Scope

Every material claim SHALL declare its evidence boundary.

Where a verified denominator exists, record it.
Where no denominator can be verified, classify the population as:

`UNBOUNDED / NOT YET ENUMERABLE`

No percentage may be published without a verified denominator.

## 5. Stage C — Deterministic Enumeration

Research must move from ad-hoc browsing to repeatable enumeration.

For each material population define, where feasible:

- enumeration rule
- script/search rule
- denominator
- enumerated count
- evidence count
- gap count
- unknown count
- material delta

Independent reviewers must be able to reproduce the same population using the recorded method.

## 6. Stage D — Evidence Collection

Evidence may include, as applicable:

- Source Code observation
- Database observation
- UI observation
- Configuration observation
- Runtime/test behavior
- Approved SMEsPlus artifact
- Migration/historical evidence
- Authoritative statutory/accounting evidence
- Independent contradiction evidence

Every evidence item must retain source identity and provenance.

## 7. Stage E — Cross-Layer Correlation

Material facts should be correlated across the strongest applicable evidence layers:

`Source Code`
↔ `Database`
↔ `UI / Configuration`
↔ `Runtime Behavior`
↔ `Existing Approved SMEsPlus Evidence`

Agreement across layers increases confidence but does not remove the need for challenge.

If evidence layers disagree, open a Contradiction. Do not silently select the preferred layer.

## 8. Stage F — Contradiction Challenge

Every material contradiction must record:

- competing claims
- evidence for each claim
- scope of each evidence source
- whether the contradiction is semantic, implementation-specific, version-specific, data-specific, or control-specific
- current disposition
- downstream impact

Material contradictions cannot be hidden by averaging, majority opinion, or reviewer count.

## 9. Stage G — Independent Reproduction

Any finding that may affect:

- Architecture
- Accounting/Financial Integrity
- SaaS/Tenant Boundary
- Security
- Migration
- State/Gate movement
- Canonical Business Semantic

must be independently reproduced by a reviewer/team that did not author the primary finding.

Independent Review does not automatically become truth.
Reviewer findings themselves require evidence verification.

Canonical rule:

`Independent Review != Truth`
`Verified Evidence = Truth Basis`

## 10. Stage H — Claim Classification

Every material conclusion must be explicitly classified as one of:

- `VERIFIED FACT`
- `REFERENCE BEHAVIOR`
- `INFERENCE`
- `RECOMMENDATION`
- `UNKNOWN`
- `CONTRADICTED`

For negative claims, also apply:

- `VERIFIED ABSENCE`
- `NOT FOUND IN SEARCHED SCOPE`
- `NOT YET SEARCHED`

Mandatory rule:

`NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST`

## 11. Stage I — Evidence Lineage Preservation

Every material conclusion must be traceable to:

- Session/Prompt ID
- Evidence source
- Repository/path or external evidence reference
- Commit SHA / version / source root where applicable
- Reviewer/correction lineage
- Final disposition
- Gate consequence

Silent overwrite of contradicted or corrected findings is prohibited.

## 12. Stage J — Boss Decision Boundary

Research must stop trying to discover an answer when evidence has already established that the remaining choice is normative/business/architectural rather than factual.

Examples include:

- canonical ownership rule
- business recognition point
- control strictness
- tenant/company policy
- supported migration rule
- acceptable operational policy

At that point, produce a Boss Decision Package containing:

1. Decision question
2. Verified facts
3. Reference behavior(s)
4. Evidence limitations
5. Options
6. Risk/benefit per option
7. AAS+ recommendation
8. PMO recommendation
9. Downstream impact
10. What additional research can and cannot resolve

AI may recommend but may not decide for Boss.

## 13. Integration with Very Deep Research 8-Criteria Exit Gate

The acquisition flow is mandatory throughout Very Deep Research and directly supports:

1. Scope Bounded
2. Enumeration Converged
3. Unknown Exhausted
4. Tolerance-Zero Closed
5. Contradiction Resolution Complete
6. Negative Claim Controlled
7. Two Consecutive Clean Independent Passes
8. Final Knowledge Package Complete

A Module or State may not progress merely because evidence collection is voluminous. The acquisition method itself must be bounded, reproducible, and converged.

## 14. Project-Wide Applicability

This standard applies to all current and future SMEsPlus modules/domains including, but not limited to:

- Accounting
- Inventory
- Purchase
- Sales
- Manufacturing
- CRM
- Project
- HR
- Approval
- Document
- Payment/Banking
- Tax/Localization
- SaaS/Foundation
- Integration
- Infrastructure

Domain-specific additions are allowed. This canonical flow may not be weakened without Boss approval.

## 15. Time Principle

Very Deep Research is work-completeness driven, not deadline driven.

- Do not reduce scope merely to meet a date.
- Do not declare PASS because a scheduled review window ended.
- Do not bypass independent reproduction to save time.
- Do not reclassify a GATING UNKNOWN as non-gating for schedule reasons.

The project advances when the required evidence and exit criteria are satisfied.

## 16. Final Rule

`Discover -> Bound -> Enumerate -> Evidence -> Correlate -> Challenge -> Reproduce -> Classify -> Preserve -> Boss Decide`

This is the mandatory canonical evidence acquisition lifecycle for SMEsPlus Very Deep Research.
