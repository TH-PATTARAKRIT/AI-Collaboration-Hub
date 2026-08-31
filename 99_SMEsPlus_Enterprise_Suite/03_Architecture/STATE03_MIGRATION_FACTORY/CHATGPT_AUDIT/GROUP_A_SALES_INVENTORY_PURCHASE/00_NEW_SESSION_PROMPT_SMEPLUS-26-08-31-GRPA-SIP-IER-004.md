# [SMEPLUS-26-08-31-GRPA-SIP-IER-004]
# GROUP A — Sales + Inventory + Purchase Independent Evidence Review & Evidence Gate Recommendation / L999.999

## SINGLE END-TO-END SELF-STARTING INDEPENDENT REVIEW PROMPT

Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Review Function: Independent Evidence Reviewer / CHATGPT_AUDIT-class independent review
Research Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Control Level: `/L999.999`
Boss: Sole Final Approver
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical Branch: `SMEsPlus`
Canonical Baseline at Prompt Creation: `7241c6e0195040a611d42a2597d8a48e103bff00`
Team A Evidence Branch: `claude/group-a-sales-inventory-purchase-dr002`
Frozen Team A Review Commit: `8b0993d824cf726fa52edd687272ff54b0977c42`
Team A Corrective Session: `SMEPLUS-26-08-31-MIG-A-GRPA-SIP-CORR-003`
Canonical NEW PROMPT Governance: `STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md` v1.1
Jira Governance Control: `ERPPLUS-135`
Learning Matrix Parent: `ERPPLUS-133`
Dedicated GROUP A Execution Jira: `TBD / DO NOT INVENT`
STEP Binding: `TBD / BASELINE LINKAGE REQUIRED`

This Prompt is the ONLY execution instruction for this independent-review session.

`ONE SESSION = ONE END-TO-END PROMPT.`

`DO NOT ask Boss for a separate START / CONTINUE / NEXT / PUSH instruction.`

Execute immediately after reading and reconciling the controlled baselines.

---

# 1. BOSS APPROVAL / INTENT

Boss has approved the Five-Unit Challenge conclusion for the post-CORR-003 stage.

Your mission is to independently review the Team A GROUP A evidence package at frozen commit:

`8b0993d824cf726fa52edd687272ff54b0977c42`

and produce an Evidence Gate recommendation to Boss.

You are NOT Team A.

You are NOT Team B.

You are NOT IBPV Formal Verification.

You are NOT Team D.

You are NOT IDTM Formal Test.

You are NOT IESA Formal Assurance.

You are an independent evidence reviewer whose job is to determine whether Team A's evidence package is sufficiently complete, traceable, internally consistent, clean-room safe and neutral enough to be presented to Boss for an Evidence Gate decision and, if Boss approves, later handed to Team B for independent canonical design.

You must independently re-perform material checks rather than trusting Team A's closure narrative.

`TEAM A CLAIM != INDEPENDENTLY VERIFIED FACT.`

---

# 2. PROMPT RISK CLASSIFICATION

Risk Class: `MEDIUM`

Reason:

- this review may determine whether Team A evidence is ready for Boss Evidence Gate decision;
- review conclusions can materially affect downstream Team B readiness;
- no target design, Development, Production or source-system write is authorized;
- evidence inspection is read-only;
- review artifacts may be committed only to a separate independent-review branch.

Required treatment:

- Five-Unit Pre-Prompt Challenge: `COMPLETE / BOSS APPROVED`
- Prompt Readiness Record: `REQUIRED / INCLUDED`
- Independent Reviewer separation: `MANDATORY`

---

# 3. FIVE-UNIT PRE-PROMPT CHALLENGE — BOSS-APPROVED REVIEW INPUT

The following are challenge questions and risk lenses only. They are NOT expected answers.

Mandatory interpretation:

`Ask until materially clear — not until everyone agrees.`

`No Answer Key Before Review.`

`Independent reviewer discovers the review conclusion from evidence.`

## 3.1 Audit VETO — Evidence / Governance Challenge

Independently challenge:

1. Do the exact source references actually support closure of Purchase cancellation and procurement→Purchase findings?
2. Does row-level dump evidence actually support the claimed ownership, installation and historical use of the three approval modules?
3. Does the evidence distinguish `module exists / installed / historically used` from `internal workflow verified`?
4. Is `to_check_level` treated only as an observed database state where source transition logic is unavailable?
5. Are SHA-256 claims reproducible and accurately scoped?
6. Does any stale statement in the Gate package contradict CORR-003 results?
7. Is any executor self-declaration being treated as independent verification?

## 3.2 TBRAC — Thailand Business Reality Challenge

Independently challenge:

1. Are customer-specific historical approval patterns clearly separated from Thailand-wide business reality?
2. Does any Fit-Gap or user-fitness statement generalize Thai SME behavior without authoritative evidence or real-user validation?
3. Are Thailand-specific claims kept at the correct TBRAC evidence status?
4. Are company-specific practices preserved as `COMPANY DEPENDENT / KNOWN-NOT-VERIFIED / REQUIRES REAL USER VALIDATION` where appropriate?

Do NOT launch a new Thailand research programme in this review.

## 3.3 EXPERT IBPV — Advisory Business Process / Design Challenge

Independently challenge:

1. Are lifecycle/event/handoff facts for Purchase cancellation and procurement→Purchase sufficiently evidenced for downstream design work?
2. For approval, are exact trigger/state/permission/SoD semantics still unknown because module source is absent?
3. Is the evidence handoff neutral enough that Team B can independently design rather than inherit Team A's preferred solution?
4. Are `ADAPT / EXTEND / REJECT / UNKNOWN` labels clearly non-authoritative candidates rather than target-design decisions?

Do NOT perform IBPV Formal Verification.

## 3.4 EXPERT IDTM — Advisory Deep-Test / Integrity Challenge

Independently challenge:

1. Are cancellation and procurement findings sufficiently precise to become future test-oracle inputs?
2. Is approval workflow still a future test-oracle evidence gap at button/transition/permission level?
3. Are observable facts separated from inferred expected behavior?
4. Are application-layer controls distinguished from DB constraints?

Do NOT create or execute Formal IDTM test cases.

## 3.5 EXPERT IESA — Advisory ERP & SaaS System-Level Challenge

Independently challenge:

1. Does the evidence adequately expose cross-domain risks without pretending to prove production readiness?
2. Is approval preserved as a system-level control dependency where exact workflow remains unverified?
3. Are multi-company, auditability, authorization and migration implications carried forward where material?
4. Does the package avoid converting source/reference behavior into target SaaS architecture?

Do NOT perform IESA Pre-Assurance or Final Assurance.

---

# 4. CONSOLIDATED PRE-PROMPT OUTPUT

## QUESTIONS TO CONSIDER

- Are R6/R7/R8 closures reproducible from primary evidence?
- What exactly is proven versus not proven for the three approval modules?
- Is the Fit-Gap Candidate Pack neutral enough for Team B independence?
- Are stale statements and hash claims fully reconciled?
- Are any remaining High/Medium/Low gaps material blockers to the Team A Evidence Gate, or controlled carry-forwards?

## RISKS / BLIND SPOTS

- Self-review contamination.
- Treating metadata/data proof as source-level workflow proof.
- Treating customer-specific practice as Thai-wide requirement.
- Treating Team A Fit-Gap recommendation as target design.
- Stale Gate-package wording after correction.
- Hash/manifest overstatement.
- Escalating non-blocking Unknowns into unnecessary repeat research.

## EVIDENCE / VALIDATION CONCERNS

- Primary evidence must be inspected at exact frozen commit/reference.
- Where practical, re-run/recompute selected source/dump/hash checks independently.
- Do not accept executor prose as sole evidence.
- Do not silently resolve genuine Unknowns.

## SCOPE / AUTHORITY CONCERNS

- Independent review only.
- No modification of Team A evidence.
- No Team B design.
- No Team C/D work.
- No Formal IBPV/IDTM/IESA.
- No merge into `SMEsPlus`.
- No Release/Production authority.

## OPTIONAL SCOPE-SAFE RECOMMENDATIONS

- If a stale Team A document is found, record an exact correction finding; do NOT edit Team A's file in this review.
- If an open High/Medium/Low item is not Gate-blocking, classify it as controlled carry-forward rather than reopening broad research.
- If missing approval-module source is required for a downstream design decision, record that requirement precisely without attempting to obtain restricted source unless separately authorized.

## BLOCKING UNKNOWNS BEFORE EXECUTION

`NONE.`

The purpose of this review is to determine the Gate impact of existing evidence and open items.

---

# 5. PROMPT READINESS RECORD

```text
PROMPT READINESS RECORD

Prompt / Session ID:
SMEPLUS-26-08-31-GRPA-SIP-IER-004

Current STATE / STEP / Domain:
STATE03 / STEP TBD / GROUP A Sales + Inventory + Purchase

Current Authorized Execution Function:
INDEPENDENT EVIDENCE REVIEWER ONLY

Risk Class:
MEDIUM

Boss Intent:
Independently review Team A GROUP A evidence after CORR-003 and recommend whether the package is ready for Boss Evidence Gate decision.

Expected Outcome:
Evidence-based independent review package with PASS/HOLD/FAIL-FROZEN recommendation, exact findings, carry-forwards and no downstream design contamination.

In Scope:
Frozen Team A evidence commit 8b0993d824cf726fa52edd687272ff54b0977c42; CORR-003 closure; R6/R7/R8 re-performance; approval evidence boundary; Fit-Gap neutrality; Thailand generalization check; manifest/hash re-verification; Gate-package consistency; remaining-gap Gate impact.

Out of Scope:
Editing Team A evidence; new full Deep Research; Team B target design; Figma; Team C; Team D; Formal IBPV; Formal IDTM; Formal IESA; merge/release/production.

Known / Verified Facts:
- Team A evidence branch exists at the frozen review commit.
- CORR-003 executor reports 3 Critical → 0 and created files 19/20.
- Final SHA manifest file exists.
- Exact approval module internal source was not part of the extraction used by Team A.

Unverified Assumptions:
- Whether all executor closure claims survive independent re-performance.
- Whether remaining open items are non-blocking to Evidence Gate.
- Whether Fit-Gap candidate wording is sufficiently neutral.

Critical Unknowns / Conflicts:
NONE blocking start of independent review.

Five-Unit Challenge Summary:
Audit VETO, TBRAC, IBPV, IDTM and IESA recommend independent evidence review before any Team B transition.

Resolved Before Execution:
- Five-Unit Challenge approved by Boss.
- Frozen Team A commit identified.
- Reviewer role separated from Team A.
- Single End-to-End Prompt rule applied.

Carry-Forward Unknowns:
Any evidence gap that cannot be independently closed without crossing scope/legal/clean-room boundaries remains explicit and receives a Gate-impact classification.

Execution Authority:
Read-only evidence inspection and independent re-performance; create independent audit artifacts on a separate audit branch; commit/push audit evidence.

Prohibited Actions:
No Team A file edits; no target design/code; no source/live system writes; no merge to SMEsPlus; no downstream formal assurance; no self-approval; no Boss-final decision claim.

Evidence Required:
Exact file/commit/source/table/query/hash references; reproducible review steps where practical; finding-by-finding verdict; conflict/unknown preservation.

Acceptance Criteria:
Defined in §13.

Gate Impact:
Produces an independent Evidence Gate recommendation to Boss only. Does not itself authorize Team B.

Readiness Status:
READY

Boss Exception / Override:
NONE
```

---

# 6. INDEPENDENCE / BRANCH CONTROL

The reviewer MUST remain independent from Team A execution.

1. Treat Team A branch `claude/group-a-sales-inventory-purchase-dr002` at commit `8b0993d824cf726fa52edd687272ff54b0977c42` as READ ONLY.
2. Do NOT edit, amend, squash, rewrite or append to Team A files.
3. Create a separate review branch from the current canonical `SMEsPlus` branch:

`audit/group-a-sip-evidence-review-004`

4. Write independent review artifacts only under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/CHATGPT_AUDIT/GROUP_A_SALES_INVENTORY_PURCHASE/`

5. If the branch already exists, verify its lineage and use it only if it belongs to this exact review; otherwise STOP as a branch-control conflict.
6. No merge into `SMEsPlus` is authorized.

`Independent Reviewer must not review its own work.`

`Independent Reviewer must not repair the evidence it is judging.`

---

# 7. READ BEFORE REVIEW — CONTROLLED BASELINE

Use DELTA-FIRST but read enough to independently understand the review target.

At minimum reconcile:

## Governance / Review Controls

1. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/PROJECT_CONSTITUTION.md`
2. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md`
3. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IBPV_CHARTER.md`
4. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IDTM_CHARTER.md`
5. `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IESA_CHARTER.md`
6. `99_SMEsPlus_Enterprise_Suite/03_Architecture/00_Architecture_Governance/THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md`

## Prompt / Corrective Baseline

7. `00_NEW_SESSION_PROMPT_SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002.md`
8. `00_NEW_SESSION_PROMPT_SMEPLUS-26-08-31-MIG-A-GRPA-SIP-CORR-003.md`

## Team A Evidence — frozen commit only

9. `02_INVENTORY_CAPABILITY_MODEL.md`
10. `04_PURCHASE_CAPABILITY_MODEL.md`
11. `05_INTEGRATED_E2E_LIFECYCLE_MAP.md`
12. `06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md`
13. `07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md`
14. `08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md`
15. `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md`
16. `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`
17. `16_FIT_GAP_CANDIDATE_PACK.md`
18. `17_GROUP_A_EVIDENCE_MANIFEST.md`
19. `18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`
20. `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md`
21. `20_GROUP_A_FINAL_SHA256_MANIFEST.txt`

Read other GROUP A evidence files when needed to verify a material claim. Do not re-read unrelated domains merely for completeness.

`Token Optimization Mode: DELTA-FIRST.`

---

# 8. REVIEW CLUSTER A — R7 PURCHASE CANCELLATION RE-PERFORMANCE

Independently verify the corrected Purchase cancellation finding.

Required checks:

1. Locate the cited Purchase cancellation override and inspect the exact source behavior.
2. Verify how linked pickings/moves are treated by state.
3. Verify the relationship with generic `stock.picking.action_cancel()` / `stock.move._action_cancel()` only as far as needed to judge the claimed cascade.
4. Challenge the claim concerning partial receipt/backorder separation; determine what is source-proven, test-proven, inferred or merely architectural expectation.
5. Verify whether completed physical facts are preserved.
6. Record any transaction-rollback statement separately as source-proven, framework-supported inference or unverified.
7. Issue an independent verdict:
   - `VERIFIED`
   - `VERIFIED WITH CONDITIONS`
   - `GAP FOUND`
   - `CONFLICT FOUND`
   - `EVIDENCE MISSING`

Do not assume symmetry with Sales.

---

# 9. REVIEW CLUSTER B — R8 PROCUREMENT → PURCHASE RE-PERFORMANCE

Independently verify:

- `_run_buy()` implementation/equivalent;
- `buy` action registration;
- MTO/chained-demand re-trigger call site;
- material payload and linkage into Purchase.

Required checks:

1. Verify exact source paths/anchors.
2. Verify the dispatch chain rather than relying on method names.
3. Verify which values are direct inputs, derived context, vendor resolution output or implementation artifacts.
4. Verify draft-PO reuse/creation behavior only to the extent directly supported.
5. Verify the claimed linkage back to stock demand/moves.
6. Distinguish business semantic from vendor implementation architecture.
7. Issue the same independent verdict vocabulary as Cluster A.

---

# 10. REVIEW CLUSTER C — R6 APPROVAL EVIDENCE BOUNDARY

This is the most important Evidence-Boundary review.

Independently determine what the existing dump/metadata/data proves and what it does NOT prove.

At minimum verify, where evidence is available:

- existence of the relevant fields on `sale.order`, `purchase.order`, `purchase.request`;
- field state (`base` vs `manual`) where claimed;
- module ownership from `ir_model_data`/metadata where claimed;
- installation state/version where claimed;
- historical row usage where claimed;
- observed `purchase_order.state = to_check_level` where claimed;
- separation of the small Studio/dynamic pilot from the three installed modules.

Then classify separately:

A. `MODULE EXISTENCE`
B. `MODULE INSTALLED STATE`
C. `FIELD OWNERSHIP`
D. `HISTORICAL USAGE`
E. `OBSERVED STATE VALUE`
F. `INTERNAL WORKFLOW LOGIC`
G. `APPROVAL PERMISSION / SoD LOGIC`
H. `CURRENT-LIVE BEHAVIOR`

Never collapse these into one status.

Because exact internal module source was absent from Team A's extraction, do NOT infer:

- exact button logic;
- exact transition graph;
- exact approval authority;
- exact rejection/cancel behavior;
- current-live behavior;

unless independent evidence actually proves them.

Determine Gate impact:

- Is missing internal workflow source a blocker to the **Team A Evidence Gate**?
- Or is it a controlled downstream Unknown that Team B must not assume and IBPV/IDTM must later challenge?
- Would obtaining the source create clean-room/license concerns that require separate Boss authorization?

Do not automatically require additional source simply because it exists somewhere.

---

# 11. REVIEW CLUSTER D — FIT-GAP NEUTRALITY / TBRAC CHECK

Review `16_FIT_GAP_CANDIDATE_PACK.md` as a Team A proposal, not as approved target design.

For each material `ADAPT / EXTEND / REJECT / UNKNOWN` candidate, determine whether the evidence supports:

1. the underlying observed business semantic;
2. the strength of the recommendation label;
3. neutrality for Team B independent design.

Special attention:

- Item 13 — approval capability;
- Item 15 — Sales-initiated RMA/return UX statement;
- any statement implying what "many SMEs" or Thai businesses expect without TBRAC evidence;
- any architecture pattern recommendation derived from vendor implementation.

Allowed reviewer outcomes per candidate:

- `NEUTRAL / SAFE AS CANDIDATE INPUT`
- `SAFE ONLY WITH QUALIFIER`
- `DOWNGRADE TO UNKNOWN / HYPOTHESIS`
- `DESIGN-CONTAMINATION RISK`
- `TBRAC VALIDATION REQUIRED`

Do NOT redesign the candidate yourself.

If the candidate pack risks contaminating Team B independence, recommend that Team B receive a neutral evidence subset plus the candidate pack as a clearly non-authoritative appendix; do not edit the Team A pack in this review.

---

# 12. REVIEW CLUSTER E — GATE PACKAGE / HASH / REMAINING GAP CONSISTENCY

Independently review:

1. `17_GROUP_A_EVIDENCE_MANIFEST.md`
2. `18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`
3. `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md`
4. `20_GROUP_A_FINAL_SHA256_MANIFEST.txt`
5. `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`

Required checks:

- recompute SHA-256 for files 01–19 where practical and compare to file 20;
- confirm file 20 correctly excludes itself;
- identify stale statements in file 18 that pre-date CORR-003;
- identify inconsistent counts/statuses across files 14/18/19;
- verify `0 Critical` is supported by the status definitions, not merely wording;
- classify each remaining High/Medium/Low gap as:
  - `GATE BLOCKING`
  - `CONTROLLED CARRY-FORWARD`
  - `OUT-OF-SCOPE / REGISTER ONLY`
  - `ALREADY RESOLVED / STALE ENTRY`
- do not reopen broad research solely because low-severity Unknowns remain.

A stale Team A statement is an audit finding. Do NOT edit it during independent review.

---

# 13. MANDATORY INDEPENDENT REVIEW DELIVERABLES / ACCEPTANCE CRITERIA

Create these independent artifacts under the authorized `CHATGPT_AUDIT/GROUP_A_SALES_INVENTORY_PURCHASE/` path on the separate audit branch:

1. `01_GROUP_A_INDEPENDENT_REVIEW_SCOPE_AND_BASELINE.md`
2. `02_GROUP_A_R7_R8_REPERFORMANCE_MATRIX.md`
3. `03_GROUP_A_APPROVAL_EVIDENCE_BOUNDARY_REVIEW.md`
4. `04_GROUP_A_FIT_GAP_NEUTRALITY_TBRAC_REVIEW.md`
5. `05_GROUP_A_GATE_PACKAGE_AND_HASH_RECONCILIATION.md`
6. `06_GROUP_A_REMAINING_GAP_GATE_IMPACT_REGISTER.md`
7. `07_GROUP_A_INDEPENDENT_EVIDENCE_REVIEW_REPORT.md`
8. `08_GROUP_A_EVIDENCE_GATE_RECOMMENDATION_TO_BOSS.md`
9. `09_GROUP_A_INDEPENDENT_REVIEW_SHA256_MANIFEST.txt`
10. `SESSION_SMEPLUS-26-08-31-GRPA-SIP-IER-004_CLOSURE.md`

Acceptance criteria:

- Team A frozen commit and branch verified;
- reviewer independence preserved;
- material R6/R7/R8 claims independently checked;
- approval evidence boundary explicitly separated by evidence type;
- Fit-Gap neutrality/TBRAC risks classified;
- hash/manifest checks independently reproduced where practical;
- stale/inconsistent Team A statements identified exactly;
- remaining open gaps receive Gate-impact classification;
- no Team A file is edited;
- no target design is created;
- evidence citations are inspectable;
- final recommendation is evidence-based and does not claim Boss authority.

---

# 14. EVIDENCE GATE RECOMMENDATION RULES

The reviewer may recommend only one terminal Evidence Gate status:

## `PASS / VERIFIED — READY FOR BOSS EVIDENCE GATE DECISION`

Use only when:

- no unresolved Critical evidence-integrity issue remains;
- material CORR-003 closures independently survive review;
- remaining gaps are controlled carry-forwards or outside Gate scope;
- clean-room / scope / evidence traceability are acceptable;
- Team B can receive the package without being forced to inherit unverified conclusions.

## `HOLD / EVIDENCE REQUIRED`

Use when:

- a material claim cannot be independently supported;
- missing evidence could materially change business semantics or downstream design;
- Gate package inconsistency is significant enough to impair reliable handoff;
- approval or other control semantics are represented more strongly than evidence permits.

## `FAIL / FROZEN`

Use only when:

- material evidence was fabricated/contradicted;
- clean-room or authority boundary was materially violated;
- the package cannot be safely corrected/carried forward without invalidating the research baseline.

The reviewer MUST NOT issue:

- `BOSS APPROVED`
- `TEAM B AUTHORIZED`
- `DEVELOPMENT READY`
- `PRODUCTION READY`

Those decisions belong to later controls/Boss.

---

# 15. AUTONOMOUS END-TO-END EXECUTION AUTHORITY

Execute this review autonomously from baseline verification through final audit commit/push.

You are authorized to:

- create the dedicated audit branch described in §6;
- inspect the frozen Team A evidence branch read-only;
- inspect authorized local source/dump evidence read-only if available to independently re-perform claims;
- run non-destructive local commands for source/dump/hash verification;
- create independent review artifacts;
- commit and push review artifacts to the dedicated audit branch;
- continue through all review clusters without routine Boss confirmation.

DO NOT stop or ask Boss merely for:

- proceeding to the next review cluster;
- reading another in-scope evidence file;
- re-running a read-only evidence/hash check;
- creating the next required audit artifact;
- committing/pushing to the dedicated audit branch;
- carrying forward a non-blocking Unknown.

Ask Boss ONLY if:

1. a true `STOP / HOLD / FAIL-FROZEN` situation requires Boss interpretation before safe continuation;
2. material Scope expansion/CR is required;
3. frozen baseline/commit identity is inconsistent or unavailable;
4. legal/license/quarantine controls would need to be crossed;
5. destructive/write access to source/live systems is required;
6. Team B/C/D or Formal IBPV/IDTM/IESA authority would be required;
7. branch/repository/access conflict prevents independent audit evidence from being safely preserved;
8. a material contradiction cannot safely remain a registered finding pending Boss decision.

`NO ROUTINE CONFIRMATION.`

`AUTO-CONTINUE.`

`AUTO-COMMIT/PUSH AUDIT EVIDENCE.`

---

# 16. PROGRESS REPORTING

Report only evidence-backed progress.

At minimum report:

- `% Board`
- `% STATE`
- `% STEP`

If no controlled denominator/binding exists, report:

`TBD / BASELINE REQUIRED`

Do not substitute review-file count for STATE/STEP completion.

Additionally report:

- Review Cluster complete/total;
- Deliverables complete/total;
- Findings by severity/status;
- Blocking issues;
- Current Evidence Gate recommendation status.

---

# 17. SESSION CLOSURE CONTROL

Before claiming review completion:

1. Verify all required independent-review artifacts exist.
2. Generate SHA-256 manifest for the finalized review artifacts, excluding the manifest's self-hash.
3. Commit and push all review evidence to the dedicated audit branch.
4. Record exact repository, branch, file path and commit SHA.
5. Create `SESSION_SMEPLUS-26-08-31-GRPA-SIP-IER-004_CLOSURE.md`.
6. Preserve unresolved findings/carry-forwards.
7. Do not merge.
8. Do not claim Boss decision.

Terminal statement must be exactly one of:

- `INDEPENDENT EVIDENCE REVIEW COMPLETE — PASS / VERIFIED — READY FOR BOSS EVIDENCE GATE DECISION`
- `INDEPENDENT EVIDENCE REVIEW COMPLETE — HOLD / EVIDENCE REQUIRED`
- `INDEPENDENT EVIDENCE REVIEW COMPLETE — FAIL / FROZEN`

---

# 18. SELF-STARTING EXECUTION ORDER

Immediately perform, without requiring another user message:

```text
VERIFY GOVERNANCE + FROZEN COMMITS
        ↓
CREATE/VERIFY INDEPENDENT AUDIT BRANCH
        ↓
CLUSTER A — R7 PURCHASE CANCELLATION RE-PERFORMANCE
        ↓
CLUSTER B — R8 PROCUREMENT→PURCHASE RE-PERFORMANCE
        ↓
CLUSTER C — R6 APPROVAL EVIDENCE BOUNDARY
        ↓
CLUSTER D — FIT-GAP NEUTRALITY / TBRAC
        ↓
CLUSTER E — GATE PACKAGE / HASH / REMAINING-GAP CONSISTENCY
        ↓
CONSOLIDATE INDEPENDENT FINDINGS
        ↓
CLASSIFY GATE IMPACT
        ↓
ISSUE EVIDENCE GATE RECOMMENDATION TO BOSS
        ↓
GENERATE REVIEW SHA-256 MANIFEST
        ↓
COMMIT + PUSH AUDIT EVIDENCE
        ↓
CREATE SESSION CLOSURE RECORD
        ↓
STOP
```

No second START command is required.

---

# 19. GOVERNING PRINCIPLES

`ONE SESSION = ONE END-TO-END PROMPT.`

`Ask until materially clear — not until everyone agrees.`

`No Answer Key Before Review.`

`Independent Reviewer must not review its own work.`

`Independent Reviewer must not repair the evidence it judges.`

`Team A evidence != Team B target design.`

`Observed customer practice != Thailand-wide requirement.`

`Metadata/data proof != internal workflow source proof.`

`Unknown != failure; invented certainty = control failure.`

`No Evidence = No Progress.`

`Never Skip Gate.`

`Boss = Sole Final Approver.`