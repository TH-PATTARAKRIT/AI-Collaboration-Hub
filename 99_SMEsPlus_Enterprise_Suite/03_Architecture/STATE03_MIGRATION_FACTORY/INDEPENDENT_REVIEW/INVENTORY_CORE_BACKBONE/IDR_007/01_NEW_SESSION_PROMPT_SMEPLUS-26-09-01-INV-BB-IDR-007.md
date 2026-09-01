# [SMEPLUS-26-09-01-INV-BB-IDR-007]
# Inventory Core CORR-005 Fresh Independent Delta Re-Review / INDEPENDENT REVIEW / L999.999

## SINGLE END-TO-END SELF-STARTING INDEPENDENT REVIEW PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Execution Function: `Independent Evidence Reviewer — Inventory Core Backbone`  
Mode: `READ ONLY PRIMARY EVIDENCE / DELTA-FIRST / INDEPENDENT RE-PERFORMANCE / CLEAN-ROOM`  
Control Level: `/L999.999`  
Boss: `Sole Final Approver`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Governance Branch: `SMEsPlus`  
Canonical Governance Baseline at Prompt Creation: `54025627d63eb4055ff89f602454d9122876dfb2`  
Frozen TEAM A DR-002 Commit: `b31597fafa318c2edd9047ad89c128e4ace2e7cb`  
Frozen IER-003 Commit: `45c749eae826642872ccc2dc09f0f714932c5b8e`  
Frozen TEAM A CORR-005 Commit: `d69da7900941bdae209eb33af20ac24e4893d536`  
IDR-006 Non-Execution Supersession Commit: `3e89b073302ff8d8bfad356275cdc6707a53b67f`  
Five-Unit Readiness Commit: `54025627d63eb4055ff89f602454d9122876dfb2`  
Execution Branch: `audit/inventory-core-corr005-delta-rereview-007`  
Jira: `ERPPLUS-137` — preserve all existing fields; evidence comment only if connector is available.

This is the **only instruction for this session**.

`ONE SESSION = ONE END-TO-END PROMPT.`

Execution flags:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

Do not ask Boss for a separate START / CONTINUE / NEXT / COMMIT / PUSH instruction.

---

## 1. Mission

Perform a fresh, genuinely independent **Delta Re-Review** of TEAM A Inventory CORR-005.

The prior prompt `IDR-006` existed but has no published execution result. It is superseded for execution by this fresh-session prompt. Do not reuse its execution branch.

This is **not** another full Inventory Deep Research pass.

The review question is:

> Is CORR-005's corrected Inventory evidence package sufficiently reconciled, internally consistent, and independently supportable to be presented to Boss for an Inventory Evidence Gate decision?

You must independently challenge CORR-005 rather than validate it by assumption.

Do **not** self-declare Inventory Evidence Gate PASS.

Do **not** authorize Team B Inventory Design.

---

## 2. Preflight — Mandatory Before Any Review Writing

### 2.1 Repository / branch verification

Fetch current remote state first.

Verify:

1. `SMEsPlus` contains the Five-Unit readiness commit `54025627d63eb4055ff89f602454d9122876dfb2`.
2. `claude/inventory-core-backbone-dr002` contains exact frozen commit `b31597fafa318c2edd9047ad89c128e4ace2e7cb`.
3. `audit/inventory-core-dr002-independent-review-003` contains exact frozen IER-003 commit `45c749eae826642872ccc2dc09f0f714932c5b8e`.
4. `claude/inventory-core-backbone-register-recon-corr005` contains exact frozen CORR-005 commit `d69da7900941bdae209eb33af20ac24e4893d536`.
5. `audit/inventory-core-corr005-delta-rereview-007` starts exactly from `d69da7900941bdae209eb33af20ac24e4893d536` and has no unexpected prior execution commit.
6. The IDR-006 supersession record exists on `SMEsPlus` and the old IDR-006 branch is not used for this run.

If governance files exist on `SMEsPlus` but are not ancestors of the frozen evidence branch, inspect them explicitly cross-branch. Do **not** misclassify cross-branch visibility as missing evidence.

### 2.2 Collision containment

Do not modify any unrelated worktree or branch.

If another writer is active on `audit/inventory-core-corr005-delta-rereview-007`, STOP and report `HOLD — CONCURRENT WRITER / BRANCH OWNERSHIP CONFLICT`.

---

## 3. Mandatory Inputs

Read from exact refs, not memory.

### 3.1 TEAM A DR-002

Ref:

`claude/inventory-core-backbone-dr002 @ b31597fafa318c2edd9047ad89c128e4ace2e7cb`

Primary package:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/DEEP_RESEARCH_DR002/EXECUTION/`

Enumerate the directory. Do not trust remembered counts.

### 3.2 IER-003

Ref:

`audit/inventory-core-dr002-independent-review-003 @ 45c749eae826642872ccc2dc09f0f714932c5b8e`

Read all artifacts required to reproduce:
- five High dispositions,
- SHA/package integrity,
- residual-count reasoning,
- gate-impact reasoning,
- Boss recommendation,
- session closure.

### 3.3 CORR-005

Ref:

`claude/inventory-core-backbone-register-recon-corr005 @ d69da7900941bdae209eb33af20ac24e4893d536`

Read:
- all changed TEAM A DR-002 files,
- all seven CORR-005 execution deliverables,
- CORR-005 SHA manifest,
- final residual blocker / carry-forward register,
- readiness report and session closure.

### 3.4 Governance

Read from `SMEsPlus`:
- Boss Inventory Scope Ruling excluding `bh_*` / `bhpro_*` source learning,
- approved SaaS Multi-Tenant / Multi-Company / Multi-Branch baseline control,
- CORR-004 supersession record,
- IDR-006 non-execution supersession record,
- IDR-007 Five-Unit readiness record.

---

## 4. Hard Scope Rules

### 4.1 Excluded source families

`bh_*` and `bhpro_*` are **OUT OF SCOPE FOR SOURCE LEARNING**.

You may acknowledge their legacy database footprints only as migration provenance when already present in authorized evidence.

Do not acquire, inspect, infer, reconstruct, or use their source logic as SMEsPlus learning/design evidence.

### 4.2 Platform baseline must not be reopened

SMEsPlus already has approved SaaS:
- Multi-Tenant,
- Multi-Company,
- Multi-Branch.

Do not research Branch architecture again.

Only verify that Inventory evidence correctly carries Tenant / Company / Branch context and that legacy branch facts remain in the proper Migration/TBRAC/Accounting-Tax carry-forward boundary.

### 4.3 Cross-domain boundaries

Inventory owns Stock Truth and Inventory lifecycle evidence.

Accounting/Tax owns final accounting/tax semantics.

Migration owns legacy mapping/provenance.

Do not resolve those domains by invention.

---

## 5. Independent Delta Review Work

Perform all sections autonomously.

### 5.1 Reproduce package integrity

Independently recompute the CORR-005 manifest against the actual frozen package.

Verify claimed `27/27` coverage, missing paths, duplicates, changed-file list, and self-hash convention.

Do not trust TEAM A's manifest result without reproduction.

### 5.2 Re-perform all five former High findings

For each item, reopen exact primary evidence and decide independently:

1. `GRPA-H4` — Fiscal Position.
2. `GRPA-H5 / H2` — Partner Brand/HQ.
3. `GRPA-H8 / H3` — Thai Branch.
4. `N-A7-03 / N-A9-02` — Cutoff / Timing.
5. `N-A13-02` — Company ACL / Record Rules.

For every item record:
- original DR-002 status,
- IER-003 result,
- Boss ruling if applicable,
- CORR-005 status,
- independent IDR-007 verdict,
- exact evidence citation,
- whether status is technical proof, governance scope disposition, controlled carry-forward, or test-stage carry-forward,
- Gate impact.

### 5.3 Scope-exclusion challenge

Explicitly verify that H2 closure is not mislabeled as technical verification.

Acceptable semantics:

`CLOSED BY BOSS SCOPE EXCLUSION — CONTROLLED MIGRATION CARRY-FORWARD`

if and only if Inventory no longer depends on the excluded source logic.

### 5.4 Branch-baseline challenge

Explicitly verify that H3 closure does not claim the customer's legacy branch usage is fully understood.

Acceptable semantics:

`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION — CONTROLLED MIGRATION/TBRAC + ACCOUNTING-TAX CARRY-FORWARD`

if and only if no unresolved branch fact changes Inventory Stock Truth or the approved platform hierarchy.

### 5.5 Residual register recount

Independently recompute open Inventory research blockers from the corrected register.

Do not copy `0 Critical / 0 High / 14 Medium / 7 Low`.

Recount every open row and verify:
- severity,
- status,
- owner/domain,
- next action,
- Gate impact,
- carry-forward destination.

### 5.6 Severity challenge

Challenge all 14 Medium and 7 Low items.

The objective is **not** to close them artificially.

Determine whether any item is materially misclassified and should be elevated to Critical/High because it affects one or more of:
- Stock Truth,
- quantity conservation,
- reservation integrity,
- state lifecycle,
- cut-off,
- tenant/company isolation,
- migration continuity,
- accounting handoff integrity,
- material clean-room/compliance boundary.

If a real Critical/High item exists, classify it honestly and do not recommend Gate readiness.

### 5.7 Controlled carry-forward audit

Verify no carry-forward disappeared or was silently treated as resolved.

At minimum preserve correct visibility for:
- excluded legacy `bh_*`/`bhpro_*` data footprints → Migration only,
- customer-specific legacy branch mapping → Migration/TBRAC,
- Thai tax branch semantics → Accounting/Tax,
- ORM-vs-DB-layer tenant isolation residuals → future implementation/test/assurance as applicable.

### 5.8 Cross-file consistency

Check all CORR-005-modified DR-002 files for stale contradictions, especially old `5 High` / `HOLD` wording, unsupported branch claims, incorrect source-learning scope, stale next actions, or counts inconsistent with the corrected register.

Historical statements may remain if clearly dated/superseded. They must not masquerade as current status.

### 5.9 Clean-room check

Verify no excluded source learning entered CORR-005 and no vendor implementation was converted into target design.

---

## 6. Required Deliverables

Create only under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IDR_007/EXECUTION/`

Minimum deliverables:

1. `01_IDR007_PREFLIGHT_AND_FROZEN_BASELINE_VERIFICATION.md`
2. `02_IDR007_CORR005_SHA256_REPRODUCTION.md`
3. `03_IDR007_FIVE_HIGH_INDEPENDENT_REPERFORMANCE.md`
4. `04_IDR007_H2_SCOPE_EXCLUSION_AUDIT.md`
5. `05_IDR007_H3_BRANCH_BASELINE_AND_CARRY_FORWARD_AUDIT.md`
6. `06_IDR007_RESIDUAL_COUNT_AND_SEVERITY_RECOMPUTATION.md`
7. `07_IDR007_CONTROLLED_CARRY_FORWARD_AUDIT.md`
8. `08_IDR007_CROSS_FILE_CONSISTENCY_AND_CLEAN_ROOM_REVIEW.md`
9. `09_IDR007_INDEPENDENT_DELTA_REVIEW_REPORT.md`
10. `10_IDR007_BOSS_INVENTORY_EVIDENCE_GATE_RECOMMENDATION.md`
11. `11_IDR007_SESSION_CLOSURE.md`
12. `12_IDR007_FINAL_SHA256_MANIFEST.txt`

Manifest must hash deliverables `01-11`; do not claim a self-hash for file `12`.

Do not modify TEAM A DR-002 / CORR-005 files or IER-003 files.

---

## 7. Independent Verdict Rules

Allowed overall outcomes:

### A. READY

Use only when:
- package integrity reproduces,
- all five former High dispositions are supported at the correct evidence/governance level,
- zero material Critical/High Inventory research blocker remains,
- residual Medium/Low rows are correctly classified and controlled,
- carry-forwards are explicit and owned,
- no clean-room or cross-domain boundary violation exists.

Terminal wording:

`INDEPENDENT DELTA RE-REVIEW COMPLETE — READY FOR BOSS INVENTORY EVIDENCE GATE DECISION`

This is **not** Gate PASS.

### B. HOLD / TARGETED CORRECTION REQUIRED

Use when a material evidence, classification, count, carry-forward, or consistency defect is correctable without invalidating the full package.

Terminal wording:

`INDEPENDENT DELTA RE-REVIEW COMPLETE — HOLD / TARGETED CORRECTION REQUIRED — INVENTORY EVIDENCE GATE NOT READY`

### C. FAIL-FROZEN

Use only for an applicable invariant breach, material evidence fabrication/tampering, unrecoverable clean-room violation, or frozen-baseline contradiction that invalidates the package.

---

## 8. Git / Publication Authority

You are authorized to:
- create review artifacts in `IDR_007/EXECUTION/`,
- commit them to `audit/inventory-core-corr005-delta-rereview-007`,
- push that dedicated branch,
- continue after each commit/push without asking Boss,
- post an evidence-only comment to `ERPPLUS-137` if Jira connector is available.

You are **not** authorized to:
- merge to `SMEsPlus`,
- edit TEAM A artifacts,
- open Team B Inventory design,
- start development,
- change Jira fields/status/assignee/due date,
- perform production/live writes.

---

## 9. True STOP Conditions

Ask Boss only if one of these occurs:
- concurrent writer / branch ownership conflict,
- required frozen commit cannot be resolved after fetch,
- material governance contradiction that cannot safely remain `CONFLICTING EVIDENCE`,
- destructive/irreversible/live write becomes necessary,
- clean-room/license boundary would be crossed,
- material scope expansion or Change Request is required.

Routine uncertainty is not a STOP condition. Register it with evidence and continue.

---

## 10. Final Report to Boss

At completion report:
- repository,
- audit branch,
- final commit SHA,
- SHA reproduction result,
- five former High verdicts,
- independently recomputed residual counts,
- any severity changes,
- carry-forward summary,
- clean-room result,
- final independent recommendation,
- confirmation that Inventory Evidence Gate was not self-approved,
- confirmation that Team B Inventory / Development were not authorized.

No Evidence = No Progress.  
Never Skip Gate.  
Boss is the sole Final Approver.  
Ask until materially clear — not until everyone agrees.  
Independent experts challenge the questions; the authorized Team discovers the answers.