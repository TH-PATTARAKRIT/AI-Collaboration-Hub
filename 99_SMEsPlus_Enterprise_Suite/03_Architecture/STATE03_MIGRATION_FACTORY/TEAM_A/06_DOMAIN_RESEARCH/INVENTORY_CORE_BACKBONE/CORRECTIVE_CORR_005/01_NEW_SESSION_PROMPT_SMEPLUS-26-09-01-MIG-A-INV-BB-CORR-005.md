# [SMEPLUS-26-09-01-MIG-A-INV-BB-CORR-005]
# Inventory Core DR-002 Register Reconciliation & Evidence-Gate Delta Preparation / TEAM A / L999.999

## SINGLE END-TO-END SELF-STARTING TEAM A CORRECTIVE PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Execution Team: `TEAM A — Source Learning / Business Evidence Extraction`  
Workstream: `Inventory Core Backbone — DR-002 Register Reconciliation`  
Mode: `READ ONLY PRIMARY EVIDENCE / DELTA-FIRST / GOVERNANCE-RECONCILIATION / CLEAN-ROOM`  
Control Level: `/L999.999`  
Boss: `Sole Final Approver`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Governance Branch: `SMEsPlus`  
Canonical Governance Baseline at Prompt Creation: `34bcc665a6c72972db5a18e737b3143f42b94ade`  
Frozen TEAM A DR-002 Commit: `b31597fafa318c2edd9047ad89c128e4ace2e7cb`  
Frozen TEAM A DR-002 Branch: `claude/inventory-core-backbone-dr002`  
Frozen Independent Review IER-003 Commit: `45c749eae826642872ccc2dc09f0f714932c5b8e`  
Independent Review Branch: `audit/inventory-core-dr002-independent-review-003`  
Boss Scope Ruling Commit: `997809d63d643bebdcdb825f0894975c781b4b18`  
CORR-004 Supersession Commit: `370b081768dbc157f4278300a2b8e1e18a997e1f`  
Five-Unit Readiness Commit: `34bcc665a6c72972db5a18e737b3143f42b94ade`  
Execution Branch: `claude/inventory-core-backbone-register-recon-corr005`  
Jira: `ERPPLUS-137` — preserve fields; comment only if connector is available.

This is the **only execution instruction for this session**.

**ONE SESSION = ONE END-TO-END PROMPT.**

Execution flags:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

Do not ask Boss for separate `START`, `CONTINUE`, `NEXT`, `COMMIT`, `PUSH`, or routine phase-by-phase confirmation.

---

## 1. Mission

Perform a narrow corrective reconciliation of TEAM A Inventory DR-002 after Independent Review IER-003 and two subsequent Boss scope rulings.

The purpose is **not further source research**.

The purpose is to make the TEAM A DR-002 package internally consistent with already-established evidence and governance so an Independent Delta Re-Review can determine whether the Inventory Evidence Gate is ready for Boss decision.

Required outcome:

1. reconcile all five High findings from IER-003 into TEAM A's own controlled registers;
2. remove H2/H3 from the set of open Inventory research blockers using the Boss-approved dispositions;
3. preserve valid migration / TBRAC / Accounting-Tax / implementation-test carry-forwards;
4. correct any stale, contradictory, or superseded wording in affected TEAM A files;
5. recompute residual counts from the reconciled package rather than copying `0 Critical / 5 High / 14 Medium / 7 Low` mechanically;
6. distinguish `OPEN INVENTORY RESEARCH BLOCKER` from `CONTROLLED CROSS-DOMAIN / MIGRATION / USER-VALIDATION / TEST CARRY-FORWARD`;
7. produce a reproducible corrected evidence package and SHA-256 manifest;
8. stop at `READY FOR INDEPENDENT DELTA RE-REVIEW` — do not self-approve the Inventory Evidence Gate.

---

## 2. Mandatory Preflight — Verify Before Editing

### 2.1 Repository / branch / commit verification

Fetch all required refs before acting.

Verify exactly:

- `origin/SMEsPlus` contains `34bcc665a6c72972db5a18e737b3143f42b94ade` or a descendant containing the same governance artifacts;
- `origin/claude/inventory-core-backbone-dr002` contains frozen DR-002 commit `b31597fafa318c2edd9047ad89c128e4ace2e7cb`;
- `origin/audit/inventory-core-dr002-independent-review-003` contains IER-003 commit `45c749eae826642872ccc2dc09f0f714932c5b8e`;
- working branch is `claude/inventory-core-backbone-register-recon-corr005` and its starting point is the frozen DR-002 commit unless an explicit verified descendant contains no unrelated modifications.

If a governance commit is not in the working branch ancestry, do **not** call it missing. Use explicit cross-branch inspection such as `git show origin/SMEsPlus:<path>` or equivalent after fetch.

Do not touch shared/contaminated worktrees owned by other sessions.

### 2.2 Confirm CORR-004 was never executed

Verify:

`claude/inventory-core-backbone-h2-h3-corr004 == b31597fafa318c2edd9047ad89c128e4ace2e7cb`

or otherwise prove no CORR-004 execution artifacts were published.

If CORR-004 was unexpectedly executed after the supersession record, STOP and report a true concurrency/governance conflict.

---

## 3. Mandatory Inputs — Read Fully Before Editing

### 3.1 Frozen TEAM A DR-002 package

Path:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/DEEP_RESEARCH_DR002/EXECUTION/`

Enumerate `A0-A20` yourself. Do not trust a remembered list without verifying it.

At minimum, re-read all files containing any of the following:

- five High findings;
- source/module scope;
- Warehouse / Location / Branch wording;
- SaaS / Tenant / Company / Branch wording;
- Thailand branch / regulatory wording;
- migration provenance;
- Unknown / Conflict / Evidence Gap counts;
- Material Unknown Exhaustion;
- Accounting x Inventory Cross-Proof input;
- clean-room classification;
- final recommendation / session closure / SHA manifest.

Expected affected files include, but are not limited to:

- `A1_INVENTORY_SOURCE_LANDSCAPE_AND_MODULE_SCOPE.md`
- `A5_WAREHOUSE_LOCATION_PRODUCT_UOM_TRACEABILITY.md`
- `A7_ADJUSTMENT_COUNT_CUTOFF_EVIDENCE.md`
- `A9_INVENTORY_ACCOUNTING_VALUATION_INTERFACE_EVIDENCE.md`
- `A10_SAAS_TENANT_COMPANY_WAREHOUSE_RISK_REGISTER.md`
- `A11_THAILAND_BUSINESS_REALITY_AND_REGULATORY_REGISTER.md`
- `A12_MIGRATION_PROVENANCE_AND_CONTINUITY_EVIDENCE.md`
- `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`
- `A15_MATERIAL_UNKNOWN_EXHAUSTION_REPORT.md`
- `A16_ACCOUNTING_X_INVENTORY_CROSS_PROOF_INPUT_PACK.md`
- `A17_CLEAN_ROOM_CLASSIFICATION_AND_QUARANTINE_REGISTER.md`
- `A18_TEAM_A_INVENTORY_DEEP_RESEARCH_FINAL_REPORT.md`
- `A19_INVENTORY_DEEP_RESEARCH_SHA256_MANIFEST.txt`
- `A20_SESSION_CLOSURE_SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002.md`

Do not modify a file merely because it is listed above; modify only where reconciliation is required.

### 3.2 Independent Review IER-003

Read the complete IER-003 execution package from:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/`

At minimum verify:

- package integrity / SHA reproduction;
- primary claim re-performance;
- each of the five High finding reviews;
- finding and Gate impact register;
- targeted TEAM A corrective recommendation;
- Boss Gate recommendation;
- independent session closure / manifest.

Do not summarize IER-003 from memory. Re-open the actual files.

### 3.3 Boss scope ruling

Read from `origin/SMEsPlus`:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/INVENTORY_CORE_BACKBONE/BOSS_INVENTORY_SCOPE_RULING_BH_EXCLUSION_AND_BRANCH_BASELINE_2026_09_01.md`

This ruling is binding.

### 3.4 CORR-004 supersession record

Read:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/CORRECTIVE_CORR_004/CORR004_SUPERSESSION_RECORD_2026_09_01.md`

### 3.5 Five-Unit readiness

Read:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/INVENTORY_CORE_BACKBONE/INVENTORY_CORR005_PRE_PROMPT_FIVE_UNIT_CHALLENGE.md`

---

## 4. Binding Finding Dispositions

Reconcile, do not re-research, the following.

### H1 — Fiscal Position / GRPA-H4

IER-003 verdict:

`VERIFIED CLOSED`

The model exists in authorized source; TEAM A's earlier search scope missed the bare `account` folder.

Required action:

- correct the DR-002 gap/register wording;
- preserve the exact IER-003 evidence citation;
- do not conduct a new fiscal-position research pass.

### H2 — Partner Brand/HQ / GRPA-H5

Boss disposition:

`CLOSED BY BOSS SCOPE EXCLUSION / LEGACY MIGRATION DATA CARRY-FORWARD ONLY`

Binding rules:

- `bh_*` and `bhpro_*` are OUT-OF-SCOPE for SMEsPlus source learning;
- do not search for, request, download, inspect, infer, or learn from `bh_parent_company`, `bh_brand`, `bh_store_type`, or any other `bh_*` / `bhpro_*` implementation source;
- do not derive target architecture/business semantics from their schema or source;
- legacy DB existence/provenance may be retained only so Migration does not silently lose data;
- exact vendor internal logic is not an Inventory research blocker because the source family itself is excluded by Boss.

Required action:

- remove H2 from `OPEN INVENTORY RESEARCH BLOCKER` classification;
- preserve a controlled `LEGACY MIGRATION DATA / CROSS-DOMAIN CARRY-FORWARD` entry if needed;
- explicitly label that closure is by scope exclusion, not by implementation proof.

### H3 — Thai Branch / GRPA-H8

Boss disposition:

`CLOSED AS AN INVENTORY ARCHITECTURE QUESTION`

Binding rules:

- SMEsPlus SaaS Multi-Tenant / Multi-Company / Multi-Branch architecture is an existing approved platform baseline;
- Inventory must not re-research or redefine the Branch architecture;
- legacy `branch` versus `company_registry` remains a Migration / TBRAC mapping question only;
- real-user validation may remain only to determine which legacy value was operationally trusted for migration;
- tax-document Branch semantics are Accounting / Tax owned;
- no child-company or vendor representation may be promoted to the canonical SMEsPlus Branch model from this research.

Required action:

- remove H3 from `OPEN INVENTORY RESEARCH BLOCKER` classification;
- correct any DR-002 wording that states or implies Branch architecture is still undecided by Inventory;
- correct any overstatement that the customer's actual branch is proven to be a child `res.company` if IER-003 showed the data did not prove that practice;
- retain only controlled Migration / TBRAC / Accounting-Tax carry-forwards.

### H4 — Cutoff / Timing / N-A7-03 + N-A9-02

IER-003 verdict:

`VERIFIED CLOSED`

Required action:

- reconcile DR-002 evidence with the exact lock-date / cutoff enforcement evidence found by IER-003;
- update Accounting x Inventory Cross-Proof input accordingly;
- do not repeat a broad cutoff research pass.

### H5 — Company ACL / N-A13-02

IER-003 verdict:

`VERIFIED WITH CONDITIONS — NOT AN INVENTORY GATE BLOCKER`

Required action:

- incorporate the independently verified company-scoped `ir.rule` evidence;
- preserve any limitation/condition exactly as IER-003 stated;
- carry future implementation/test verification forward where appropriate;
- do not claim SaaS runtime isolation is already implemented merely because reference-source ACL evidence exists.

---

## 5. Absolute Prohibitions

This session MUST NOT:

1. perform another full Inventory Deep Research;
2. perform new `bh_*` / `bhpro_*` source research;
3. seek BHPRO/vendor source;
4. study or redesign Branch architecture;
5. decide the target Tenant / Company / Branch data model;
6. create Team B Inventory design;
7. change Accounting-owned semantics;
8. perform Formal IBPV, IDTM or IESA lifecycle execution;
9. self-approve the Inventory Evidence Gate;
10. authorize Team B, Team C, Development, Release or Production;
11. merge to `SMEsPlus`;
12. delete historical DR-002 / IER-003 evidence to make counts look cleaner.

If existing text is wrong, correct it with explicit traceability to IER-003 / Boss ruling. Preserve Git history and a corrective audit trail.

---

## 6. Reconciliation Method

For every changed register row or narrative claim, record:

- old DR-002 classification;
- new classification;
- evidence/ruling that caused the change;
- whether it is:
  - `VERIFIED CLOSED`,
  - `CLOSED BY BOSS SCOPE EXCLUSION`,
  - `CLOSED AS INVENTORY ARCHITECTURE QUESTION`,
  - `VERIFIED WITH CONDITIONS`,
  - `CONTROLLED MIGRATION CARRY-FORWARD`,
  - `CONTROLLED TBRAC / REAL-USER-VALIDATION CARRY-FORWARD`,
  - `ACCOUNTING/TAX CARRY-FORWARD`,
  - `FUTURE IMPLEMENTATION/TEST CARRY-FORWARD`,
  - or still an actual `OPEN INVENTORY RESEARCH BLOCKER`.

Never convert a carry-forward into a Fact.

Never count a Boss scope exclusion as technical implementation proof.

---

## 7. Residual Count Reconciliation

The original DR-002 terminal count was:

`0 Critical / 5 High / 14 Medium / 7 Low`

Do not copy this number into the corrected package.

Recompute from the reconciled register.

Mandatory output must show at least two different count views:

### 7.1 Open Inventory Research Blockers

Counts only items still actionable by further authorized Inventory evidence research.

### 7.2 Controlled Carry-Forwards

Separately count/classify items that are no longer Inventory research blockers but remain relevant to:

- Migration;
- TBRAC / real-user validation;
- Accounting / Tax;
- SaaS implementation/test verification;
- other cross-domain design.

If all five former High items cease to be open Inventory research blockers after applying the verified evidence and Boss rulings, state that precisely. Do not automatically erase their audit history.

If another material High/Critical Inventory research blocker is discovered while reconciling contradictions, register it honestly and do not force a ready status.

---

## 8. Files to Reconcile

Modify only the minimum necessary TEAM A DR-002 files.

Likely affected files include:

- `A1_INVENTORY_SOURCE_LANDSCAPE_AND_MODULE_SCOPE.md`
- `A5_WAREHOUSE_LOCATION_PRODUCT_UOM_TRACEABILITY.md`
- `A7_ADJUSTMENT_COUNT_CUTOFF_EVIDENCE.md`
- `A9_INVENTORY_ACCOUNTING_VALUATION_INTERFACE_EVIDENCE.md`
- `A10_SAAS_TENANT_COMPANY_WAREHOUSE_RISK_REGISTER.md`
- `A11_THAILAND_BUSINESS_REALITY_AND_REGULATORY_REGISTER.md`
- `A12_MIGRATION_PROVENANCE_AND_CONTINUITY_EVIDENCE.md`
- `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`
- `A15_MATERIAL_UNKNOWN_EXHAUSTION_REPORT.md`
- `A16_ACCOUNTING_X_INVENTORY_CROSS_PROOF_INPUT_PACK.md`
- `A17_CLEAN_ROOM_CLASSIFICATION_AND_QUARANTINE_REGISTER.md`
- `A18_TEAM_A_INVENTORY_DEEP_RESEARCH_FINAL_REPORT.md`
- `A19_INVENTORY_DEEP_RESEARCH_SHA256_MANIFEST.txt`

`A20_SESSION_CLOSURE_SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002.md` is a historical closure artifact. Prefer leaving its historical statement intact and create a new CORR-005 closure record. If a current-package pointer is essential, add only an explicit supersession/addendum note without rewriting history.

---

## 9. Mandatory CORR-005 Deliverables

Create under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/CORRECTIVE_CORR_005/EXECUTION/`

Minimum deliverables:

1. `01_CORR005_PREFLIGHT_AND_BASELINE_VERIFICATION.md`
2. `02_CORR005_FIVE_HIGH_RECONCILIATION_MATRIX.md`
3. `03_CORR005_RESIDUAL_BLOCKER_AND_CARRY_FORWARD_REGISTER.md`
4. `04_CORR005_DR002_CROSS_FILE_CONSISTENCY_REPORT.md`
5. `05_CORR005_INDEPENDENT_DELTA_REVIEW_READINESS_REPORT.md`
6. `06_CORR005_SESSION_CLOSURE.md`
7. `07_CORR005_FINAL_SHA256_MANIFEST.txt`

The manifest must hash the corrected current TEAM A evidence package and CORR-005 content artifacts as appropriate, excluding itself from self-hash. State scope precisely.

---

## 10. Cross-File Consistency Sweep

Before closure, search the corrected TEAM A package for stale statements including, at minimum:

- `5 High`
- `0 Critical / 5 High / 14 Medium / 7 Low`
- `fiscal.position` missing
- `owning module not found` where H2 now has a Boss exclusion disposition
- `bh_parent_company` as a future source-research task
- `BHPRO` source acquisition as an Inventory next action
- Branch architecture described as undecided by Inventory
- branch as proven child `res.company` customer practice
- cutoff/timing described as still evidence-missing
- company ACL described as wholly unread/unverified
- H2/H3 described as Inventory Gate research blockers

Each stale occurrence must be either corrected or explicitly identified as historical/superseded text.

---

## 11. Evidence and Citation Discipline

Every substantive correction must cite one of:

- frozen TEAM A DR-002 evidence;
- IER-003 independent re-performance evidence;
- Boss Scope Ruling;
- Five-Unit readiness record.

Do not introduce new external-web evidence in this reconciliation session.

Do not use excluded `bh_*` / `bhpro_*` source as evidence even if it becomes discoverable during execution.

---

## 12. Git / Publication Rules

Authorized:

- edit TEAM A DR-002 files only on `claude/inventory-core-backbone-register-recon-corr005`;
- create CORR-005 execution artifacts on that branch;
- commit in logical batches;
- push only that dedicated branch;
- post an evidence comment to `ERPPLUS-137` if Jira connector is available, without changing existing issue fields/status unless explicitly authorized.

Not authorized:

- merge to `SMEsPlus`;
- modify IER-003 audit artifacts;
- modify Account workstream files;
- modify another Team/session branch;
- open Team B Inventory execution.

Before each push, fetch remote and confirm no unexpected same-branch concurrent writer. If the dedicated branch has an unexplained remote commit not produced by this session, STOP as a true concurrency conflict.

---

## 13. True STOP Conditions

Ask Boss only if one of these occurs:

1. CORR-004 was actually executed after being superseded;
2. a material Critical/High Inventory research contradiction appears that is not covered by existing evidence/rulings;
3. the Boss Scope Ruling conflicts with another later Boss-approved frozen baseline;
4. destructive/irreversible/live-system write would be required;
5. branch ownership/concurrency is ambiguous;
6. required frozen DR-002 or IER-003 evidence is genuinely inaccessible after explicit ref fetch;
7. clean-room/license boundary would be crossed.

Do not stop for a non-blocking Unknown; register and carry it forward.

---

## 14. Mandatory Final Status Logic

Use one of these terminal statuses only.

### If reconciliation succeeds and no open material Inventory research blocker remains

`TEAM A INVENTORY DR-002 REGISTER RECONCILIATION COMPLETE — READY FOR INDEPENDENT DELTA RE-REVIEW — INVENTORY EVIDENCE GATE NOT YET APPROVED`

### If material Inventory research blocker remains

`TEAM A INVENTORY DR-002 REGISTER RECONCILIATION COMPLETE — MATERIAL INVENTORY RESEARCH BLOCKER REMAINS — NOT READY FOR GATE`

### If evidence/governance cannot be verified

`EVIDENCE / GOVERNANCE VERIFICATION FAILED — HOLD`

Never output `INVENTORY EVIDENCE GATE PASS` from this Team A session.

Never authorize Team B.

---

## 15. Final Boss-Facing Report

At completion report:

- repository;
- branch;
- final commit SHA;
- files modified;
- files created;
- five High disposition table;
- old residual counts vs reconciled count views;
- open Inventory research blockers, if any;
- controlled carry-forwards by owner/domain;
- SHA-256 manifest status;
- Jira evidence-comment result if attempted;
- confirmation that no `bh_*` / `bhpro_*` source learning occurred;
- confirmation that Branch architecture was not reopened;
- confirmation that no merge to `SMEsPlus`, no Team B authorization, and no development occurred;
- exact terminal status.

Then stop.

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`  
`Approved architecture is verified downstream; it is not repeatedly redesigned downstream.`
