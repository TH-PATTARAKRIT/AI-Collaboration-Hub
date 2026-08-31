# [SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006]
# GROUP A — Sales + Inventory + Purchase Formal Independent Business Process & Design Verification / EXPERT IBPV / L999.999

## SINGLE END-TO-END SELF-STARTING FORMAL IBPV PROMPT

Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Control Level: `/L999.999`
Boss: Sole Final Approver
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical Branch: `SMEsPlus`
Canonical Baseline at Prompt Creation: `6b0e4729bc6cbecb4f1d4559f137927d3cbfa786`
Dedicated IBPV Working Branch: `ibpv/group-a-sip-formal-verification-006`
TEAM B Frozen Design Commit: `b98a3b9fb435845dbd15fae79db63b0b73a82420`
STEP Binding: `TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT`
Dedicated Jira Execution Issue: `TBD / DO NOT INVENT`

This Prompt is the ONLY execution instruction for this Formal IBPV session.

`ONE SESSION = ONE END-TO-END PROMPT.`

Do NOT ask Boss for a separate START / CONTINUE / NEXT / COMMIT / PUSH instruction.

Execute immediately after reading and reconciling the controlled baselines.

---

# 1. BOSS DIRECTIVE / AUTHORITY

Boss explicitly authorizes Formal IBPV Verification to proceed.

Boss clarification:

`Authorization to proceed does NOT mean the TEAM B design is Final.`

TEAM B current status remains only:

`TEAM B DESIGN CANDIDATE COMPLETE — READY FOR FORMAL IBPV VERIFICATION`

It is NOT:

- Final Design;
- Boss Approved Design;
- Development Ready;
- Team C Authorized.

Your role is to independently verify TEAM B's design and issue a Pre-Development Gate Recommendation to Boss.

You do NOT approve the design finally and you do NOT authorize Development.

---

# 2. GOVERNING CHARTER / GOVERNANCE

Mandatory charter:

`99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IBPV_CHARTER.md`

Charter authority:

`EXPERT IBPV verifies Team B designs before Development.`

`EXPERT IBPV is a verification body, not a design authoring body and not an implementation body.`

Mandatory pre-prompt readiness record:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/00_PRE_PROMPT_READINESS_SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006.md`

Prompt Risk:

`HIGH`

Five-Unit Pre-Prompt Challenge conclusion:

`READY — FORMAL IBPV MAY START`

Mandatory principles:

`No Evidence = No Progress.`

`Never Skip Gate.`

`Independent Reviewer must not review its own work.`

`No Cross-Team Execution.`

`Boss = Sole Final Approver.`

---

# 3. INDEPENDENCE / FROZEN INPUT RULE

You are NOT TEAM B.

You must review TEAM B as an independent verifier.

TEAM B frozen design input:

- Branch: `claude/team-b-group-a-sip-design-005`
- Frozen commit: `b98a3b9fb435845dbd15fae79db63b0b73a82420`
- Required TEAM B package: files `01`–`21` under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/`

Do NOT silently review a later mutable branch tip.

Do NOT modify any TEAM B artifact.

Do NOT repair TEAM B design in place.

Do NOT convert your verification findings into replacement design authored by IBPV.

If a design gap exists, record the gap precisely and state what must be reworked/clarified/evidenced by the proper owner.

---

# 4. APPROVED EVIDENCE BASELINE

## 4.1 TEAM A Approved Evidence

Frozen TEAM A evidence commit:

`8b0993d824cf726fa52edd687272ff54b0977c42`

Approved Evidence Gate:

`EVIDENCE GATE — PASS / BOSS APPROVED`

Boss Gate record:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/GROUP_A_SALES_INVENTORY_PURCHASE/GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md`

## 4.2 Independent TEAM A Evidence Review

Audit branch:

`audit/group-a-sip-evidence-review-004`

Frozen Independent Review commit:

`626873c3b924a0350dfd75cf52d276eff6414dd2`

## 4.3 Clean-room Usage Rule

For Formal IBPV, approved neutral business evidence and the TEAM B design are normal inputs.

Vendor-specific source code, ORM structures, proprietary implementation details and restricted/quarantined technical observations are NOT normal design-verification input.

Do not reopen raw vendor-source research merely to find an answer that TEAM B lacks.

If a material rule cannot be verified from approved neutral evidence / approved baselines, classify it `EVIDENCE MISSING` rather than importing restricted implementation knowledge.

---

# 5. FORMAL IBPV MISSION

Independently determine whether TEAM B's GROUP A design is:

- complete enough for Pre-Development decision;
- traceable to approved evidence / approved project baseline / explicit controlled design reasoning;
- internally consistent;
- cross-domain coherent;
- state/event coherent;
- ownership/handoff coherent;
- approval/SoD controllable;
- exception-safe;
- accounting-interface safe within scope;
- SaaS/multi-company coherent;
- explicit about assumptions, conflicts, Unknowns and Evidence Gaps;
- sufficiently precise for Boss to decide whether Team C may later begin implementation.

You must verify the design independently.

Do NOT treat TEAM B's own readiness report as proof.

---

# 6. ALLOWED FORMAL IBPV STATUS VOCABULARY

Use the charter vocabulary for findings and final recommendation:

- `VERIFIED`
- `VERIFIED WITH CONDITIONS`
- `GAP FOUND`
- `CONFLICT FOUND`
- `EVIDENCE MISSING`
- `REWORK REQUIRED`
- `NOT READY FOR DEVELOPMENT`
- `READY FOR BOSS DECISION`

Do NOT use:

- `FINAL APPROVED`
- `BOSS APPROVED`
- `PRODUCTION READY`
- `RELEASE APPROVED`

A `READY FOR BOSS DECISION` recommendation is still not Team C authorization.

---

# 7. HARD SCOPE BOUNDARY

## 7.1 In Scope

Formal verification of:

1. End-to-End Business Process Flow
2. Cross-Module / Cross-Domain Flow
3. State Transition Flow
4. Business Event Flow
5. Business Fact / Data Ownership / Lifecycle / Handoff
6. Approval / Permission / Segregation-of-Duties semantics
7. Reject / Cancel / Partial / Retry / Reversal / Correction / Recovery paths
8. Accounting / tax / WHT / compliance interface impact where GROUP A touches those boundaries
9. Multi-company / branch / warehouse / SaaS tenant semantics where applicable
10. Integration boundaries and failure/recovery semantics
11. Requirement/Evidence-to-Design Traceability
12. Assumption / Conflict / Unknown / Evidence-Gap management
13. Cross-domain scenarios that could fail even when each individual module appears locally correct

## 7.2 Out of Scope / Prohibited

Do NOT:

- author replacement TEAM B design;
- edit TEAM B files;
- write Node.js code;
- define physical production DDL/ORM/API implementation;
- perform Team C work;
- perform Team D work;
- perform Formal IDTM testing;
- perform Formal IESA assurance;
- merge any branch into `SMEsPlus`;
- release/deploy;
- write to production/customer systems;
- waive a gap;
- self-approve;
- authorize Team C.

---

# 8. MANDATORY FORMAL VERIFICATION QUESTIONS

For every material process, independently answer with evidence:

- Who initiates it?
- Who owns each fact/state?
- What event or rule changes the state?
- What data/fact is created, changed, referenced, locked or reversed?
- What cross-domain handoff occurs?
- What accounting/compliance consequence is triggered and when?
- What approval/permission/SoD requirement applies?
- What happens on rejection?
- What happens on cancellation before and after partial completion?
- What happens on partial delivery / partial receipt?
- What happens on retry / duplicate processing?
- What happens on return / reversal / correction?
- What happens when a downstream service/domain fails?
- How is audit history preserved?
- How does the process behave across company / branch / warehouse / tenant boundaries?
- Which TEAM B design artifact contains the rule?
- What approved evidence or approved baseline supports it?
- Which Unknowns remain unresolved?

Do not merely confirm that a section exists; verify that the semantics are coherent across artifacts.

---

# 9. PRIORITY CHALLENGE CLUSTERS FROM FIVE-UNIT PRE-PROMPT REVIEW

## 9.1 Cluster A — TEAM B Independence / Traceability

Verify that TEAM B's design decisions do not simply inherit Team A `ADAPT / EXTEND / REJECT / UNKNOWN` labels.

Re-perform a sample sufficient to establish independence, including all three items TEAM B explicitly says it resolved beyond Team A's prior UNKNOWN classification:

- Fit-Gap item #7 — physical count-in-progress vs. settled on-hand fact;
- Fit-Gap item #10 — explicit Over-Fulfillment Policy;
- Fit-Gap item #12 — asymmetric cancellation gates.

For each, classify whether the TEAM B conclusion is:

- evidence-supported design reasoning;
- a valid new target requirement;
- an unsupported assumption;
- a cross-domain conflict;
- or evidence missing.

Do NOT redesign the decision yourself.

## 9.2 Cluster B — Approval / SoD

Priority artifact:

`13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`

Focus on:

- `APR-001` Amount-Threshold Approval;
- `APR-002` Sequential Level-Based Approval;
- `APR-003` Sales Confirmation Gate;
- creator/requester vs. approver distinction;
- rejection/resubmission/cancel interactions;
- company/branch scoping;
- auditability.

The exact internal workflow of the three legacy approval modules remains unavailable.

Verify whether TEAM B has successfully separated:

`Target Business Requirement`

from

`Unverified Reference Workflow`

If a material target rule cannot be justified without the missing legacy workflow, classify that point `EVIDENCE MISSING` / `REWORK REQUIRED` as applicable.

Do not infer the missing workflow.

## 9.3 Cluster C — Policy Defaults Deferred to Boss / Business

TEAM B explicitly left these unresolved:

1. Canonical `Invoiced Quantity` definition;
2. Default Over-Fulfillment / Over-Billing policy;
3. Default Sales Confirmation Gate policy.

Formal IBPV must independently decide whether each:

- may safely remain an open Boss/business policy decision at Pre-Development Gate; or
- is sufficiently material that Development must remain `NOT READY FOR DEVELOPMENT` until decided.

Do NOT choose the business policy for Boss.

## 9.4 Cluster D — Cancellation / Accounting Boundary

TEAM B Fit-Gap item #12 concluded that Purchase may legitimately have a stricter cancellation gate than Sales due to vendor-financial exposure.

Independently verify whether this conclusion:

- is supported at business-semantic/interface level;
- remains inside GROUP A authority;
- avoids assuming unverified AP/AR/Accounting Core internals;
- remains coherent with partial receipt / vendor-bill / cancellation / reversal handling.

If the conclusion depends on Accounting Core behavior not verified in GROUP A, classify the dependency rather than silently accepting it.

## 9.5 Cluster E — SaaS / Tenant / Multi-Company

Priority artifact:

`14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md`

TEAM B introduced `Tenant` as a SaaS-native boundary not derived from Team A's single-customer evidence.

Independently verify whether the Tenant concept is traceable to an approved SMEsPlus project identity / SaaS baseline.

If yes, classify the project-baseline trace explicitly.

If no approved baseline supports it, classify the Team B claim as an untraceable design decision / gap rather than accepting Team B's own assertion.

Also verify:

- Legal Company isolation;
- Branch semantics where evidenced;
- Warehouse/location ownership;
- shared-master vs. company-owned facts;
- cross-company handoff Unknowns;
- no silent cross-tenant leakage semantics.

## 9.6 Cluster F — Thailand / User Reality

Priority artifact:

`16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md`

Verify that:

- no customer-specific observation becomes Thailand-wide truth without evidence;
- Thai tax-branch remains correctly classified;
- Sales-initiated RMA remains real-user validation territory unless evidence exists;
- district/sub-district delivery semantics remain controlled;
- business-policy defaults are not disguised as Thai standard practice.

Do not create Thai requirements without authoritative or real-user evidence.

## 9.7 Cluster G — Exceptions / Recovery / Integrity

Priority artifacts:

- `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`
- `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md`
- `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`

Verify first-class treatment of:

- partial delivery;
- partial receipt;
- backorder;
- shortage;
- over/under fulfillment;
- cancellation before/after partial activity;
- return/reversal;
- correction;
- duplicate/retry;
- cross-warehouse effects;
- failure/recovery and audit continuity.

Any missing material path must be a finding.

## 9.8 Cluster H — Accounting / External Handoff

Priority artifact:

`15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md`

Verify that GROUP A defines only financial/accounting handoff semantics and does not redesign:

- COA;
- GL Posting Engine;
- tax engine;
- WHT engine;
- fiscal-position internals;
- valuation-accounting internals;
- AR/AP internal posting logic.

Verify that correction/reversal identity and downstream traceability are sufficient at the interface boundary.

## 9.9 Cluster I — Future Testability (IDTM Lens Only)

Do NOT run Formal IDTM.

Check whether material rules are precise enough to later yield observable outcomes, particularly:

- quantity conservation;
- state/event outcomes;
- approval/SoD outcomes;
- duplicate/retry behavior;
- company/tenant isolation;
- reversal/correction integrity.

If a rule cannot be independently interpreted for future testing, record a design clarity gap.

`Testability informs verification; it does not provide the design answer.`

## 9.10 Cluster J — ERP / SaaS System Coherence (IESA Lens Only)

Do NOT perform Formal IESA Assurance.

Challenge:

- cross-domain fact integrity;
- failure and recovery boundaries;
- integration dependency coherence;
- migration/audit identity continuity;
- multi-company/tenant coherence;
- possibility that individual modules are locally valid but integrated flow fails.

Register system-level concerns without prescribing target architecture.

---

# 10. MANIFEST / COMPLETENESS RE-PERFORMANCE

TEAM B claims:

- 13/13 planned phases complete;
- 21/21 deliverables present;
- file `21_TEAM_B_FINAL_SHA256_MANIFEST.txt` hashes files 01–20.

Do not trust this self-claim.

Independently:

1. Enumerate files 01–21 at frozen TEAM B commit `b98a3b9...`.
2. Recompute SHA-256 for files 01–20.
3. Compare all hashes to file 21.
4. Record mismatch / missing / unexpected files.
5. Verify that key cross-references resolve to existing artifacts.

A hash PASS proves file integrity only; it does NOT prove design correctness.

---

# 11. FINDING MODEL

Every material finding must include:

- Finding ID;
- Verification Area;
- TEAM B Artifact(s);
- Approved Evidence / Baseline reference;
- Finding Status using IBPV vocabulary;
- Severity: Critical / Major / Moderate / Minor;
- Why it matters;
- Cross-domain impact;
- Gate impact;
- Required owner for response/rework/evidence;
- whether the finding is blocking Development;
- whether Boss decision is required.

Do NOT embed a replacement design as the "fix".

A valid finding may say:

`TEAM B must clarify/rework X because Y is untraceable or contradictory.`

A prohibited finding would rewrite X on TEAM B's behalf.

---

# 12. PRE-DEVELOPMENT BLOCKING RULE

Per IBPV Charter, Development remains HOLD when any applicable item remains unresolved unless Boss explicitly rules otherwise:

- Critical business-flow gap;
- Critical cross-domain conflict;
- missing evidence for a material business rule;
- unverified state/event transition affecting financial/control integrity;
- unresolved accounting/compliance impact;
- unresolved security/permission/SoD design issue;
- untraceable TEAM B design decision.

Formal IBPV must apply this rule independently.

Do NOT weaken a blocker merely because TEAM B declared itself ready.

---

# 13. EXECUTION PHASES — AUTO-CONTINUE

Execute all phases without routine Boss confirmation.

## PHASE 0 — Governance / Independence / Frozen Baseline

- Verify repo / branches / frozen commits.
- Verify IBPV Charter and Pre-Prompt Readiness Record.
- Confirm dedicated IBPV branch.
- Confirm TEAM B input is read-only.
- Create Deliverable 01.

## PHASE 1 — TEAM B Package / Manifest Re-Performance

- Verify 21/21 package.
- Reproduce SHA-256 manifest.
- Record integrity result in Deliverable 01 and later report.

## PHASE 2 — End-to-End Business Process Verification

- Verify business-process completeness.
- Create Deliverable 02.

## PHASE 3 — Cross-Domain / Integration Verification

- Verify Sales ↔ Inventory ↔ Purchase ↔ Accounting-handoff coherence.
- Create Deliverable 03.

## PHASE 4 — State / Event Verification

- Verify lifecycle/state model.
- Verify event model.
- Create Deliverables 04 and 05.

## PHASE 5 — Fact / Data Ownership / Handoff Verification

- Verify authoritative facts, owners, changes, handoffs, audit identity.
- Create Deliverable 06.

## PHASE 6 — Approval / Permission / SoD Verification

- Execute Cluster B and relevant Cluster C checks.
- Create Deliverable 07.

## PHASE 7 — Exception / Partial / Cancel / Return / Correction / Recovery

- Execute Clusters D/G.
- Create Deliverable 08.

## PHASE 8 — Accounting / Compliance Interface Verification

- Execute Cluster H.
- Create Deliverable 09.

## PHASE 9 — Integration Failure / Retry / System Boundary Verification

- Verify retries, duplicates, downstream failure, recoverability, identity.
- Create Deliverable 10.

## PHASE 10 — SaaS / Multi-Company / Thailand Reality Verification

- Execute Clusters E/F plus IDTM/IESA advisory lenses.
- Create Deliverable 11.

## PHASE 11 — Traceability / Conflict / Gap Consolidation

- Independently audit TEAM B evidence-to-design traceability.
- Re-perform all priority Fit-Gap challenges.
- Create Deliverables 12 and 13.

## PHASE 12 — Formal IBPV Conclusion / Gate Recommendation

- Consolidate full verification.
- Apply blocking rule.
- Create Deliverables 14 and 15.
- Create SHA-256 manifest Deliverable 16.
- Commit/push final evidence.
- STOP for Boss decision.

---

# 14. REQUIRED DELIVERABLES

Create only inside:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/EXPERT_IBPV/GROUP_A_SALES_INVENTORY_PURCHASE/FORMAL_VERIFICATION_FV_006/`

Required files:

1. `01_IBPV_SCOPE_INPUT_AND_INDEPENDENCE_REGISTER.md`
2. `02_BUSINESS_PROCESS_VERIFICATION_MAP.md`
3. `03_CROSS_MODULE_CROSS_DOMAIN_FLOW_VERIFICATION.md`
4. `04_STATE_TRANSITION_VERIFICATION_MATRIX.md`
5. `05_EVENT_FLOW_VERIFICATION_MATRIX.md`
6. `06_DATA_FACT_OWNERSHIP_AND_HANDOFF_VERIFICATION.md`
7. `07_CONTROL_APPROVAL_PERMISSION_SOD_VERIFICATION.md`
8. `08_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_RECOVERY_CATALOG.md`
9. `09_ACCOUNTING_COMPLIANCE_INTERFACE_IMPACT_VERIFICATION.md`
10. `10_INTEGRATION_FAILURE_RETRY_RECOVERY_VERIFICATION.md`
11. `11_SAAS_MULTI_COMPANY_THAILAND_REALITY_VERIFICATION.md`
12. `12_REQUIREMENT_EVIDENCE_TO_DESIGN_TRACEABILITY_AUDIT.md`
13. `13_DESIGN_CONFLICT_OPEN_GAP_EVIDENCE_MISSING_REGISTER.md`
14. `14_IBPV_INDEPENDENT_VERIFICATION_REPORT.md`
15. `15_PRE_DEVELOPMENT_GATE_RECOMMENDATION_TO_BOSS.md`
16. `16_IBPV_FINAL_SHA256_MANIFEST.txt`

Do not overwrite TEAM B or TEAM A files.

---

# 15. REQUIRED FINAL RECOMMENDATION LOGIC

After completing the whole review, issue one evidence-based recommendation to Boss.

Possible terminal recommendation shapes include:

### If materially verified with no blocking issue

`FORMAL IBPV COMPLETE — READY FOR BOSS DECISION`

with finding statuses `VERIFIED` / `VERIFIED WITH CONDITIONS` as applicable.

### If material rework is required

`FORMAL IBPV COMPLETE — REWORK REQUIRED / NOT READY FOR DEVELOPMENT`

### If material evidence is missing

`FORMAL IBPV COMPLETE — EVIDENCE MISSING / NOT READY FOR DEVELOPMENT`

Do not say:

`TEAM C AUTHORIZED`

or

`BOSS APPROVED`

Boss decides what happens after the report.

---

# 16. AUTONOMOUS EXECUTION AUTHORITY

Within this Prompt's scope you are authorized to:

- read GitHub/local approved project files;
- inspect frozen commits/branches;
- compute/reproduce hashes;
- create the IBPV-only verification artifacts;
- commit them to the dedicated IBPV branch;
- push the dedicated IBPV branch;
- continue through all phases automatically.

Execution flags:

`AUTO-CONTINUE`

`AUTO-COMMIT/PUSH EVIDENCE`

`NO ROUTINE CONFIRMATION`

`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

Do not ask Boss to approve each file, phase, commit or push.

---

# 17. TRUE STOP CONDITIONS

Ask Boss only if one of these occurs and prevents safe continuation:

1. Frozen TEAM B commit / required evidence cannot be accessed.
2. Repository/branch conflict makes it impossible to preserve independent evidence without destructive action.
3. Verification would require restricted/quarantined vendor material outside current authority.
4. A material scope contradiction cannot safely be recorded as GAP/CONFLICT/EVIDENCE MISSING.
5. A destructive/irreversible/live-system write would be required.
6. Credentials/access authority is genuinely missing and blocks the verification.

A finding of `GAP FOUND`, `CONFLICT FOUND`, `EVIDENCE MISSING`, or even `NOT READY FOR DEVELOPMENT` is NOT by itself a reason to stop early.

Continue the review, capture the full independent finding set, then issue the terminal recommendation.

---

# 18. GITHUB / BRANCH CONTROL

Execution branch:

`ibpv/group-a-sip-formal-verification-006`

Use this branch for IBPV artifacts only.

Do NOT commit Formal IBPV artifacts to the TEAM B branch.

Do NOT merge into `SMEsPlus`.

Do NOT create or approve a release.

At completion report:

- repository;
- branch;
- final commit SHA;
- verification artifact path;
- final recommendation;
- count of findings by status/severity;
- any Development-blocking findings;
- explicit confirmation that TEAM B files were untouched;
- explicit confirmation that no merge/Team C/Development occurred.

---

# 19. PROGRESS REPORTING CONTROL

You may report session-internal phase completion such as:

`13 / 13 IBPV phases complete`

and deliverable completion such as:

`16 / 16 IBPV deliverables complete`

Do NOT invent official `% Board`, `% STATE`, or `% STEP` if no approved denominator / STEP binding exists.

Use:

`TBD / BASELINE REQUIRED`

where the approved denominator/linkage is not evidenced.

---

# 20. SINGLE-PROMPT INTEGRITY / START COMMAND

This is a self-starting prompt.

Begin immediately with PHASE 0.

Do not wait for:

- START;
- CONTINUE;
- NEXT;
- COMMIT;
- PUSH;
- routine Boss confirmation.

Continue End-to-End until all phases and required IBPV artifacts are complete, then STOP at the Formal IBPV recommendation for Boss.

`Independent experts verify the design; only Boss decides whether the lifecycle may advance.`
