# [SMEPLUS-26-09-01-INV-BB-IDR-006]
# Inventory Core CORR-005 Independent Delta Re-Review / INDEPENDENT REVIEW / L999.999

## SINGLE END-TO-END SELF-STARTING INDEPENDENT REVIEW PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Execution Function: `Independent Evidence Reviewer — Inventory Core Backbone`  
Mode: `READ ONLY PRIMARY EVIDENCE / DELTA-FIRST / INDEPENDENT RE-PERFORMANCE / CLEAN-ROOM`  
Control Level: `/L999.999`  
Boss: `Sole Final Approver`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Governance Branch: `SMEsPlus`  
Canonical Governance Baseline for this prompt: `ea05ef6c3d880fbac27288ece08c97b817f6d599`  
Frozen TEAM A DR-002 Commit: `b31597fafa318c2edd9047ad89c128e4ace2e7cb`  
Frozen Independent Review IER-003 Commit: `45c749eae826642872ccc2dc09f0f714932c5b8e`  
Frozen TEAM A CORR-005 Commit: `d69da7900941bdae209eb33af20ac24e4893d536`  
Five-Unit Readiness Commit: `ea05ef6c3d880fbac27288ece08c97b817f6d599`  
Execution Branch: `audit/inventory-core-corr005-delta-rereview-006`  
Jira: `ERPPLUS-137` — preserve existing fields; evidence comment only if connector is available.

This is the **only execution instruction for this session**.

`ONE SESSION = ONE END-TO-END PROMPT.`

Execution flags:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

Do not ask Boss for a separate START / CONTINUE / NEXT / COMMIT / PUSH instruction.

---

## 1. Mission

Perform a genuinely independent **delta re-review** of TEAM A Inventory CORR-005.

This is **not** another full Inventory Deep Research pass.

The reviewer must determine whether CORR-005 correctly reconciled the five former High findings and the DR-002 controlled registers without introducing false closure, scope leakage, hidden evidence loss, or cross-domain contradictions.

The decision target is only:

`Is the corrected Inventory evidence package sufficiently reconciled to be presented to Boss for Inventory Evidence Gate decision?`

Do not self-approve the Inventory Evidence Gate.

Do not authorize Team B Inventory design.

---

## 2. Mandatory Frozen Inputs

Before writing any review result, independently verify repository state and read the following from their exact refs.

### 2.1 TEAM A DR-002

Branch / commit:

`claude/inventory-core-backbone-dr002 @ b31597fafa318c2edd9047ad89c128e4ace2e7cb`

Primary package:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/DEEP_RESEARCH_DR002/EXECUTION/`

Enumerate the package. Do not trust remembered filenames or counts.

### 2.2 Independent Review IER-003

Branch / commit:

`audit/inventory-core-dr002-independent-review-003 @ 45c749eae826642872ccc2dc09f0f714932c5b8e`

Read the review artifacts needed to reproduce the five High dispositions, especially H1-H5, Unknown-count reconciliation, Gate impact register, targeted correction recommendation, Boss Gate recommendation, closure, and manifest.

### 2.3 TEAM A CORR-005

Branch / commit:

`claude/inventory-core-backbone-register-recon-corr005 @ d69da7900941bdae209eb33af20ac24e4893d536`

Read all CORR-005 execution artifacts under:

`.../INVENTORY_CORE_BACKBONE/CORRECTIVE_CORR_005/EXECUTION/`

and inspect every DR-002 file actually modified by CORR-005.

### 2.4 Governance / Boss scope rulings

Read the current canonical records from `SMEsPlus`, including:

- Boss Inventory Scope Ruling: `bh_*` and `bhpro_*` excluded from source learning.
- Approved SaaS Tenant / Company / Branch baseline: downstream Inventory research must not reopen Platform Architecture without material contradiction.
- CORR-004 supersession record.
- CORR-005 Five-Unit readiness.
- This IDR-006 Five-Unit readiness.

If governance records are outside the audit branch ancestry, read them explicitly cross-branch. Do **not** call them missing merely because they are not ancestors of the frozen evidence branch.

---

## 3. Independence Requirements

You are not TEAM A.

Do not accept `RESOLVED`, `CLOSED`, `27/27`, `0 High`, or any other CORR-005 assertion merely because TEAM A wrote it.

Re-perform enough source / evidence inspection to establish each verdict independently.

You may reuse a frozen primary citation only after reopening it or mechanically validating it yourself.

Do not modify TEAM A evidence as part of this review.

Do not merge anything into `SMEsPlus`.

---

## 4. Mandatory Review Clusters

### Cluster A — Package integrity

1. Verify branch / commit ancestry and frozen refs.
2. Enumerate CORR-005 artifacts and changed files independently.
3. Reproduce the CORR-005 SHA-256 claims. Do not trust TEAM A's reported `27/27` without mechanical reproduction.
4. Confirm no unrelated file or prior Independent Review artifact was modified.

### Cluster B — Five former High findings

Independently review each original High item:

#### B1 — GRPA-H4 / Fiscal Position

Verify that `account.fiscal.position` is in fact present in authorized source and the original Evidence Missing classification is legitimately resolved.

#### B2 — GRPA-H5 / H2 / Partner Brand-HQ

Required governance interpretation:

`bh_* / bhpro_* = EXCLUDED FROM SOURCE LEARNING.`

Verify that CORR-005 did not study excluded source and did not convert scope exclusion into implementation proof.

Expected review question:

`Is this correctly closed as an Inventory research blocker while retaining any necessary legacy-data / Migration provenance?`

Do not acquire, read, or recommend further `bh_*` / `bhpro_*` source learning.

#### B3 — GRPA-H8 / H3 / Thai Branch

Do not reopen Multi-Tenant / Multi-Company / Multi-Branch Architecture.

Verify that CORR-005 correctly narrowed the unresolved fact to Migration / TBRAC / Accounting-Tax carry-forward rather than treating Branch architecture as an Inventory research gap.

Do not claim customer field usage is verified unless there is direct evidence.

#### B4 — N-A7-03 / N-A9-02 / Cutoff-Timing

Re-open the exact source evidence relied on by IER-003 and verify whether the Inventory-side timing / Accounting lock-date mechanism actually closes the original research question.

#### B5 — N-A13-02 / Company ACL

Verify ORM-layer company-scoped rule evidence independently.

Keep any DB-layer / bypass / `sudo()` / future implementation-test issue separate. Do not equate ORM evidence with proof of every future SaaS isolation path.

### Cluster C — Residual count reconciliation

Independently derive the open Inventory research blocker counts from the corrected register.

Verify or reject TEAM A's claim:

`0 Critical / 0 High / 14 Medium / 7 Low = 21 open Inventory research blockers`

Also independently identify the controlled carry-forward rows and ensure they are not double-counted as open Inventory blockers and are not silently erased.

### Cluster D — Cross-file consistency

Inspect every CORR-005-modified DR-002 file for stale statements such as:

- five High remain open;
- `bh_*` source acquisition still required;
- Branch architecture still an Inventory research question;
- Cutoff / fiscal position / ACL still Evidence Missing where corrected evidence exists;
- material-unknown exhaustion statements inconsistent with the reconciled count.

Historical statements may remain if clearly dated / superseded. Do not require deletion of the audit trail.

### Cluster E — Governance / clean-room / cross-domain boundary

Verify all of the following:

- no `bh_*` / `bhpro_*` source learning occurred;
- no Branch Architecture redesign or re-research occurred;
- scope exclusion was not presented as implementation proof;
- Migration/TBRAC/Accounting-Tax carry-forwards remain visible;
- Inventory did not assume authority over Accounting, Tax, Partner/CRM, Migration or SaaS Platform design;
- no Team B / Development authorization is implied.

### Cluster F — Gate impact

For every surviving Medium / Low / controlled carry-forward item, determine whether any item is actually mis-severitised and should be Critical/High for the **Inventory Evidence Gate**.

Do not mechanically treat 14 Medium + 7 Low as non-blocking.

If a finding materially undermines Stock Truth, quantity conservation, ownership/traceability, tenant/company isolation, valuation handoff, migration integrity, or the ability of Team B to design without guessing, escalate it based on evidence.

---

## 5. Explicit Non-Goals

Do not:

- repeat full DR-002;
- study `bh_*` / `bhpro_*` source;
- redesign Branch;
- redesign SaaS Tenant / Company / Branch hierarchy;
- design Team B Inventory architecture;
- perform Accounting's work;
- start formal IBPV / IDTM / IESA lifecycle execution;
- write production code;
- merge into `SMEsPlus`;
- declare Boss approval.

---

## 6. Required Deliverables

Create a dedicated review directory under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IDR_006/EXECUTION/`

Create, at minimum:

1. `01_IDR006_PREFLIGHT_AND_FROZEN_BASELINE_VERIFICATION.md`
2. `02_IDR006_CORR005_SHA256_REPRODUCTION.md`
3. `03_IDR006_FIVE_HIGH_INDEPENDENT_REPERFORMANCE.md`
4. `04_IDR006_RESIDUAL_COUNT_RECONCILIATION.md`
5. `05_IDR006_CROSS_FILE_CONSISTENCY_AND_STALE_CLAIM_SWEEP.md`
6. `06_IDR006_SCOPE_EXCLUSION_AND_BRANCH_BASELINE_COMPLIANCE.md`
7. `07_IDR006_CARRY_FORWARD_AND_CROSS_DOMAIN_BOUNDARY_REGISTER.md`
8. `08_IDR006_MEDIUM_LOW_MATERIALITY_CHALLENGE.md`
9. `09_IDR006_FINDING_AND_GATE_IMPACT_REGISTER.md`
10. `10_IDR006_BOSS_INVENTORY_EVIDENCE_GATE_RECOMMENDATION.md`
11. `11_SESSION_SMEPLUS-26-09-01-INV-BB-IDR-006_CLOSURE.md`
12. `12_IDR006_FINAL_SHA256_MANIFEST.txt`

Additional files may be created only when necessary to preserve evidence clarity.

Every material finding must state:

- evidence location;
- independent verdict;
- severity;
- Gate impact;
- owner / next action where applicable;
- whether it is Inventory-owned or a controlled cross-domain carry-forward.

---

## 7. Verdict Vocabulary

Use disciplined classifications such as:

`VERIFIED CLOSED`  
`VERIFIED WITH CONDITIONS`  
`CLOSED BY BOSS SCOPE EXCLUSION — NOT IMPLEMENTATION PROOF`  
`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION`  
`CONTROLLED CARRY-FORWARD`  
`CONFLICTING EVIDENCE`  
`EVIDENCE MISSING`  
`REQUIRES REAL USER VALIDATION`  
`REGULATORY VERIFICATION REQUIRED`  
`TARGETED CORRECTION REQUIRED`

Unknown is not fact.

A Boss governance ruling is authoritative for scope / control, but it is not implementation proof.

---

## 8. Boss Gate Recommendation Rule

The reviewer may recommend **one**, and only one, of:

### A
`READY FOR BOSS INVENTORY EVIDENCE GATE DECISION`

Use only if no unresolved Critical/High Inventory research blocker remains after independent challenge and the remaining carry-forwards are explicitly bounded.

### B
`TARGETED CORRECTION REQUIRED — NOT READY FOR BOSS INVENTORY EVIDENCE GATE DECISION`

Use if a correctable evidence/register inconsistency remains.

### C
`HOLD — EVIDENCE REQUIRED`

Use if material evidence is genuinely unavailable or a Critical/High research blocker remains.

Do not declare `INVENTORY EVIDENCE GATE = PASS` yourself.

---

## 9. Commit / Push Authority

You are authorized to create and modify **only this IDR-006 review's own artifacts** on:

`audit/inventory-core-corr005-delta-rereview-006`

You are authorized to commit and push those review artifacts to that branch without routine confirmation.

Do not modify TEAM A DR-002 or CORR-005 files.

Do not merge into `SMEsPlus`.

If Jira / Atlassian connector is available, add an evidence-only comment to `ERPPLUS-137` without changing existing fields. Connector absence is administrative and must be disclosed, not treated as Evidence Gate failure.

---

## 10. True STOP Conditions

Ask Boss only if one of these occurs:

- the frozen CORR-005 commit cannot be verified;
- the dedicated audit branch contains unexpected independent work before execution;
- a material evidence contradiction cannot safely remain classified as `CONFLICTING EVIDENCE`;
- a requested action would cross legal / license / clean-room boundary;
- a destructive / irreversible / live-system write would be required;
- scope expansion outside this delta review becomes materially necessary.

Non-blocking unknowns are registered and carried forward. They are not reasons to stop.

---

## 11. Mandatory Terminal Status

End with exactly one of the following semantic outcomes:

`INDEPENDENT DELTA RE-REVIEW COMPLETE — READY FOR BOSS INVENTORY EVIDENCE GATE DECISION`

or

`INDEPENDENT DELTA RE-REVIEW COMPLETE — TARGETED CORRECTION REQUIRED — NOT READY FOR BOSS INVENTORY EVIDENCE GATE DECISION`

or

`INDEPENDENT DELTA RE-REVIEW COMPLETE — HOLD / EVIDENCE REQUIRED`

Also state explicitly:

`INVENTORY EVIDENCE GATE NOT SELF-APPROVED.`  
`TEAM B INVENTORY DESIGN NOT AUTHORIZED BY THIS REVIEW.`  
`NO MERGE TO SMEsPlus.`

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
