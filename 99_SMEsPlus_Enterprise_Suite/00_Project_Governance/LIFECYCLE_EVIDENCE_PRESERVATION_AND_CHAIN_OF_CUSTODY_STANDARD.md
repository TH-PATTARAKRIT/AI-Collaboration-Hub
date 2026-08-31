# SMEsPlus Lifecycle Evidence Preservation & Chain-of-Custody Standard

Document ID: `SMEPLUS-GOV-LEP-001`  
Version: `1.0`  
Status: `BOSS APPROVED / EFFECTIVE`  
Effective Date: `2026-08-31`  
Owner: `SMEsPlus PMO / Project Governance`  
Final Approval Authority: `Boss`  
Applies To: `STATE03 onward / all controlled Groups, Domains, Workstreams, Steps, Gates and Lifecycle Promotions`  
Control Level: `/L99.99`

## 1. Boss Decision

Boss approved establishment of a hard evidence-preservation rule so that every material lifecycle transition has a verifiable origin, execution trail, independent review trail, Gate trail and downstream handoff trail.

The controlling principle is:

> **No Evidence Preservation = No Lifecycle Promotion.**

This standard supplements `PROJECT_CONSTITUTION.md` and the existing `No Evidence = No Progress` / `Never Skip Gate` controls. It does not replace any stricter evidence, clean-room, security, accounting, testing or production rule.

## 2. Purpose

The purpose is to prevent a situation where work was actually performed but later cannot be reconstructed or independently audited because the evidence remained only in a chat session, local machine, temporary branch, mutable branch tip, undocumented AI run or unlinked artifact.

A controlled work item must remain reconstructable from:

`WHY -> INPUT -> PROMPT / AUTHORITY -> EXECUTION -> OUTPUT -> REVIEW -> CORRECTION -> GATE -> BOSS DECISION -> HANDOFF -> NEXT FROZEN INPUT`

The project must be able to answer, years later:

- What was requested?
- Why was it authorized?
- What exact input baseline was used?
- Which AI / Team / Owner performed the work?
- What exact immutable output was produced?
- Which evidence supports each material claim?
- Who independently reviewed it?
- What findings or corrections occurred?
- What did Boss approve, reject, hold or override?
- What unresolved items were carried forward?
- What exact evidence package was handed to the next lifecycle stage?

## 3. Scope Boundary

This is a **governance and evidence-preservation control**.

It does NOT:

- create new Functional Scope;
- authorize Team B, Figma, IBPV, Team C, Team D, IDTM, IESA, Release or Production by itself;
- convert an Unknown into a Fact;
- convert a working-branch artifact into an approved canonical design merely by indexing it;
- allow PMO to override an Independent Reviewer or Boss;
- waive clean-room, security, legal, accounting, tax, SaaS or tenant-isolation requirements.

`Increasing evidence rigor != increasing product scope.`

## 4. Mandatory Lifecycle Evidence Chain

For each controlled Group / Domain / Workstream / Step, the canonical Evidence Chain Index must track at least the following lifecycle records when applicable:

1. Boss intent / authorization / approved baseline reference.
2. New Prompt / Session / Prompt Readiness Record.
3. Frozen input branch + immutable commit SHA.
4. Execution owner / team / function.
5. Execution output branch + immutable commit SHA.
6. Evidence Manifest and SHA-256 / integrity record where applicable.
7. Unknown / Conflict / Carry-Forward Register.
8. Independent Review input and output commit.
9. Review findings / correction directives.
10. Corrective execution commit(s).
11. Re-verification commit(s).
12. Gate recommendation.
13. Boss Gate decision / written exception / override where applicable.
14. Controlled handoff package.
15. Next-stage frozen input commit.
16. Jira / execution-control linkage when available.
17. Session archive / closure record where required by project constitution.

For every indexed item, record:

- Item / Task
- Owner
- Evidence Location / Direct Link
- Branch
- Immutable Commit SHA / Artifact Hash
- Timestamp
- Reviewer / Verifier
- Verification Status
- Gate Impact
- Preservation Status
- Notes / Open Unknowns

## 5. Preservation Status Vocabulary

Use only the following preservation statuses:

### `CANONICAL_COPY_VERIFIED`
The controlled evidence artifact exists on the canonical `SMEsPlus` branch and its exact path/commit is verified.

### `CANONICAL_REFERENCE_VERIFIED`
The evidence remains on an approved working / audit / verifier branch, but the canonical `SMEsPlus` branch contains a verified Evidence Chain Index entry with the exact immutable commit SHA, branch, path or commit link, owner, reviewer, timestamp, status and Gate impact.

### `ARCHIVE_REQUIRED`
Evidence exists, but its long-term preservation is not yet adequately controlled. Examples: temporary branch planned for deletion/rewrite, local-only evidence, mutable external location without immutable reference, missing manifest or missing canonical index.

### `EVIDENCE_MISSING`
Required evidence cannot be inspected or does not exist.

### `CONFLICTING_EVIDENCE`
Two or more evidence sources materially contradict each other and the contradiction has not been adjudicated.

## 6. Working Branch Rule

Working / Audit / IBPV / Corrective branches are permitted and are often required for independence.

However:

> **Working Branch Only + No Canonical Evidence Chain Index = HOLD.**

Before lifecycle promotion, every material working-branch output relied upon by the next stage must be represented in the canonical Evidence Chain Index by immutable SHA and verification metadata.

If a working branch is to be deleted, force-rewritten, rebased in a way that removes the frozen evidence commit, or otherwise made non-durable, the relied-upon evidence must first be preserved as `CANONICAL_COPY_VERIFIED` or another repository-controlled immutable archive approved by PMO / Boss.

No AI may treat a mutable branch tip as a frozen evidence baseline.

## 7. Lifecycle Promotion Gates

### 7.1 Team A -> Team B

Team B may not begin controlled independent canonical design unless:

- Team A evidence package has a frozen commit;
- Independent Evidence Review exists where required;
- Boss Evidence Gate exists where required;
- material carry-forwards are registered;
- canonical Evidence Chain Index records the above;
- preservation status contains no unresolved `ARCHIVE_REQUIRED`, `EVIDENCE_MISSING` or `CONFLICTING_EVIDENCE` item that materially affects the Team B input.

### 7.2 Team B -> Figma / Formal IBPV

The next design-verification stage must receive a frozen Team B design commit and traceability from approved evidence to design.

A Team B self-declaration such as `READY FOR REVIEW` is not independent verification.

### 7.3 Pre-Development -> Team C — HARD GATE

Team C / Development remains blocked unless the domain/workstream Evidence Chain Index shows, at minimum:

- approved / controlled Team A evidence baseline;
- Team A Evidence Gate decision;
- frozen Team B design baseline;
- Formal IBPV findings;
- all blocking corrective cycles and re-verification outcomes;
- Pre-Development Gate recommendation;
- Boss Development decision / explicit written exception;
- carry-forward register;
- next-stage handoff package;
- all material evidence preserved as `CANONICAL_COPY_VERIFIED` or `CANONICAL_REFERENCE_VERIFIED`.

Therefore:

> **No Evidence Chain Seal = No Team C.**

### 7.4 Team C -> Team D / IDTM / IESA / Production

The same principle continues downstream. Code, test, security, performance, clean-room, IDTM, IESA, Release and Production evidence must remain traceable through immutable baselines and Gate records. A downstream PASS must not erase or obscure upstream evidence lineage.

## 8. Evidence Chain Seal

Before a lifecycle promotion, PMO / Governance must issue one of:

### `PASS / VERIFIED — EVIDENCE CHAIN SEALED`
All material required records are inspectable, immutable or durably referenced, reviewed, internally consistent and correctly linked to the promotion decision.

### `HOLD / EVIDENCE PRESERVATION REQUIRED`
Work may exist, but one or more required records are missing, unindexed, not durable, not reviewed, not linked or insufficiently preserved.

### `FAIL / FROZEN — TRACEABILITY CONTROL FAILURE`
Material evidence cannot be reconstructed, is contradictory without adjudication, was overwritten/lost, or a lifecycle stage was promoted without the required evidence/Gate controls.

`PASS` is a preservation / traceability result only. It does not by itself mean Functional PASS, Design PASS, Development Ready, Release Ready or Production Ready.

## 9. Mandatory Canonical Evidence Chain Index

Every material controlled Group / Domain / Workstream must maintain a canonical file named substantially as:

`<GROUP_OR_DOMAIN>_EVIDENCE_CHAIN_INDEX.md`

The file must live on the canonical `SMEsPlus` branch in an approved project governance / gate / evidence location.

It must be updated DELTA-FIRST whenever any of the following occurs:

- new frozen execution commit;
- independent review;
- correction / rework;
- re-verification;
- Boss Gate decision;
- handoff to the next team;
- evidence supersession;
- branch preservation risk;
- Jira control linkage;
- change in Gate impact.

Historical rows must not be deleted merely because later work supersedes them. Mark them `SUPERSEDED`, `HISTORICAL`, `REJECTED`, `HOLD`, or equivalent controlled status and preserve lineage.

## 10. Independent Review Rule

The Evidence Chain Index records reviewer conclusions but does not replace the underlying independent-review artifacts.

`Executor Claim != Independent Verification.`

An execution team must not change its own preservation status to `PASS / VERIFIED — EVIDENCE CHAIN SEALED` without PMO / independent verification appropriate to the Gate.

## 11. Boss Override / Exception

Boss remains Sole Final Approver.

If Boss explicitly chooses to promote despite an evidence-preservation gap, the canonical record must contain:

- Boss Override / Exception ID
- Date / Timestamp
- Missing or conflicting evidence
- Business reason for override
- Known risk
- Compensating control
- Owner for later closure
- Gate impact

A verbal or chat-only exception that is not archived in the project repository is not a durable lifecycle exception.

## 12. Enforcement

From the effective date of this standard:

- PMO must block lifecycle promotion when required evidence preservation is incomplete.
- New Prompts that request an unauthorized lifecycle jump must be classified `HOLD` or `FAIL / FROZEN` depending on severity.
- Team C prompts must cite the applicable Evidence Chain Index and Evidence Chain Seal.
- Production prompts must cite the full relevant upstream evidence lineage and final assurance / Boss decision.
- No completion percentage may be inferred from the existence of an Evidence Chain Index alone.

## 13. Group A Initial Application

The first controlled application is:

`GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone`

A canonical Group A Evidence Chain Index is created under the STATE03 Migration Factory Boss-Gate area and is the authoritative traceability map for the Group A lifecycle lineage.

Current control at issuance:

`TEAM C / DEVELOPMENT = NOT AUTHORIZED BY THIS STANDARD.`

Group A must complete the remaining verification / Gate path and receive an explicit Boss Development decision before Team C may begin.

## 14. Governance Principles

`Repository = Single Source of Truth.`  
`No Evidence = No Progress.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`No Evidence Chain Seal = No Team C.`  
`Never Skip Gate.`  
`Independent Reviewer must not review its own work.`  
`Boss = Sole Final Approver.`
