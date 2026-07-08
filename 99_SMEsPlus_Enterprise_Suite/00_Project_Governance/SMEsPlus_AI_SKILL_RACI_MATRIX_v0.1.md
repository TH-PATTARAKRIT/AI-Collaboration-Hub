# SMEsPlus AI Skill RACI Matrix v0.1.1

Document ID: SMEPLUS-AIOS-RACI-001
Version: v0.1.1
Priority: P0
Status: CLAUDE SKILL ARCHITECT CONTROLLER ADDED / CHATGPT L99 REVIEW REQUIRED / NOT APPROVED / NOT AUTOMATED YET
Control Level: /L99.99
Prepared From: Claude AI draft `SMEsPlus_AI_SKILL_RACI_MATRIX_v0.1_DRAFT.md`
L99 Update By: ChatGPT L99 Gate Reviewer
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Path: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEsPlus_AI_SKILL_RACI_MATRIX_v0.1.md`
Generated: 2026-07-08 (Asia/Bangkok)
Latest Update: Added `claude-skill-architect-controller` as the mandatory first meta-skill before other Claude Skills are built.

## Executive Summary

This document is the AI PMO-controlled RACI baseline for SMEsPlus AI collaboration.

The key update in v0.1.1 is that `claude-skill-architect-controller` is now added as a mandatory P0 meta-skill. This skill must be designed first because it controls how all other Claude Skills are designed, reviewed, packaged, validated, and maintained.

Current control result:

```text
GitHub Tracking: ENABLED
Claude Skill Architect Controller: REQUIRED FIRST
Operating Model Approval: NOT APPROVED
Make Automation Go-Live: HOLD
FDS / Build / DB / API / UAT / Figma Gates: HOLD
Next Required Review: AI PMO + ChatGPT L99 + Boss decision
```

## 1. AI Role Map

| # | Role / Skill | Category | Primary Function | Authority Limit |
|---|---|---|---|---|
| 1 | claude-skill-architect-controller | Meta-Skill Governance | Design, validate, maintain, and standardize Claude Skills before operational use | Cannot approve operational gates or bypass Boss / AI PMO / ChatGPT L99 |
| 2 | ai-pmo-owner-lock | Governance | Lock named owners, register evidence, control routing/status | No final approval |
| 3 | smesplus-expert-fds-designer | Drafting | Draft/revise Functional Specification artifacts | No self-approval, no gate closure |
| 4 | accounting-posting-review-prep | Review Prep | Prepare posting rule review packs | Cannot certify accounting correctness |
| 5 | thai-tax-review-prep | Review Prep | Prepare Thai VAT/WHT/tax review packs | Cannot claim legal/tax compliance |
| 6 | db-design-review-prep | Review Prep | Prepare data model/entity review packs | Cannot certify DB design |
| 7 | enterprise-api-review-prep | Review Prep | Prepare API/SaaS architecture review packs | Cannot certify architecture |
| 8 | qa-uat-package-generator | QA | Generate UAT case packages | Cannot declare UAT pass |
| 9 | make-automation-controller | Automation | Route, notify, log, collect evidence, escalate | Cannot approve, merge, release, deploy, or close gate |
| 10 | intelligently-designed-erp-reviewer | Domain Review | Review ERP/accounting logic correctness | Recommendation only |
| 11 | chatgpt-l99-gate-reviewer | Governance Review | Independent evidence/gate review | Cannot replace Boss final decision |
| 12 | Boss | Final Authority | Final decision, exception approval, owner nomination | Must log final/exception decisions |

## 2. Skill Build Sequence Control

No operational Claude Skill should be created before `claude-skill-architect-controller` is defined and reviewed.

Required sequence:

```text
Step 1: Create Claude Skill Architect Controller design
Step 2: Review by AI PMO + ChatGPT L99
Step 3: Boss confirms Skill build standard
Step 4: Build first operational Skill batch
Step 5: Test with dry-run outputs only
Step 6: Activate through AI PMO-controlled workflow only
```

Recommended first build batch after the meta-skill is reviewed:

| Priority | Skill | Reason |
|---:|---|---|
| P0 | claude-skill-architect-controller | Controls all future Skill design quality and boundary |
| P1 | ai-pmo-owner-lock | Dispatches work and prevents ownerless execution |
| P1 | smesplus-expert-fds-designer | Handles FDS production/revision workload |
| P1 | qa-uat-package-generator | Converts FDS into testable UAT evidence |

Second batch:

```text
accounting-posting-review-prep
thai-tax-review-prep
db-design-review-prep
enterprise-api-review-prep
```

Third batch:

```text
make-automation-controller
intelligently-designed-erp-reviewer
chatgpt-l99-gate-reviewer
```

## 3. Skill-to-Owner RACI Matrix

Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed.

| Activity | Skill Architect | AI PMO | FDS Designer | Posting Prep | Thai Tax Prep | DB Prep | API Prep | QA/UAT | Make | ERP Reviewer | ChatGPT L99 | Boss |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Skill design standard | R/A | C | I | I | I | I | I | I | I | C | C | I |
| Skill package blueprint | R/A | C | C | C | C | C | C | C | C | C | C | I |
| Skill boundary review | R | C | C | C | C | C | C | C | C | C | A recommendation | I |
| Skill activation decision | C | C | I | I | I | I | I | I | I | I | C | R/A |
| FDS Drafting | I | I | R/A | - | - | - | - | - | I | C | I | I |
| FDS Revision | I | I | R/A | - | - | - | - | - | I | C | C | I |
| Posting Rules Review Pack | I | I | C | R/A | - | - | - | - | I | C | I | I |
| Posting Rules Domain Check | I | I | I | C | - | - | - | - | I | R/A | I | I |
| Thai Tax Review Pack | I | I | C | - | R/A | - | - | - | I | C | I | I |
| Thai Tax Legal/Compliance Confirmation | I | I | I | - | R facilitator only | - | - | - | I | C | C | A named legal/accounting owner required |
| Data Entity Review Pack | I | I | C | - | - | R/A | - | - | I | C | I | I |
| API Contract Review Pack | I | I | C | - | - | C | R/A | - | I | C | I | I |
| UAT Case Formalization | I | I | C | - | - | - | - | R/A | I | C | I | I |
| Owner Naming / RACI Lock | I | R/A | C | C | C | C | C | C | I | C | I | C/A for human owner nomination |
| Evidence Registration | I | R/A | C | C | C | C | C | C | I | I | I | I |
| Gate Status Movement | I | C | I | I | I | I | I | I | I | I | R/A recommendation | C/A for final movement |
| Independent Governance Verdict | I | I | I | I | I | I | I | I | I | I | R/A | I |
| Automation Routing / Payload Dispatch | C | C | I | I | I | I | I | I | R/A | I | I | I |
| Overdue / Ownerless Escalation | I | R | I | I | I | I | I | I | R | I | I | A |
| Final Gate Approval | I | I | I | I | I | I | I | I | I | I | C | R/A |
| Exception Handling | I | C | I | I | I | I | I | I | I | I | C | R/A |

## 4. Claude Skill Architect Controller Scope

`claude-skill-architect-controller` must produce a Skill Build Blueprint before any other Skill is built.

For every candidate Skill, it must define:

```text
skill_name
business_purpose
owner_work_replaced
trigger_conditions
expected_input
expected_output
required_evidence
allowed_actions
forbidden_actions
reviewer
verifier
github_path
make_payload_fields
gate_impact
sample_prompt
sample_output
activation_condition
```

It must reject any Skill design as `SKILL_DESIGN_HOLD` if missing:

```text
owner purpose
input evidence
output evidence
forbidden actions
reviewer
verifier
gate impact
GitHub path
Make routing rule
```

## 5. Execution Surface Rules

| Surface | Allowed | Forbidden |
|---|---|---|
| Claude Chat | Draft, analyze, export, prepare documents | Repository write, push, approve, close gate |
| Claude Code Web | GitHub execution only with explicit per-action authorization | Content decision, approval, gate closure |
| Claude Terminal | Local command, checksum, git verification only when authorized | Gate decision, implicit push, self-approval |
| AI PMO | Owner lock, evidence registration, routing control, status control | Author FDS content, issue governance verdict, final approval |
| Make | Route, notify, create draft payload, collect evidence, update non-gate status, escalate | Approve, close gate, mark PASS, merge, release, deploy |
| Intelligently Designed ERP AI | ERP/accounting/business logic review | Final approval or legal/tax certification |
| ChatGPT L99 | Independent governance/evidence review | Replace Boss decision |
| Boss | Final decision and exception approval | N/A |

Cross-surface rule: no AI may claim work done by another surface unless remote evidence is present and cited with commit, path, timestamp, and executor.

## 6. Canonical Handoff Payload v0.1.1

```yaml
event_type: ""
batch_id: ""
module: ""
repository: "TH-PATTARAKRIT/AI-Collaboration-Hub"
branch: "SMEsPlus"
commit_sha_or_source_ref: ""
source_path: ""
target_path: ""
owner_skill: ""
accountable_owner: ""
reviewer_skill: ""
verifier: ""
evidence_path: ""
evidence_required: true
current_gate_status: ""
forbidden_actions: []
required_output: ""
callback_channel: ""
due_at: ""
escalation_owner: "AI PMO / Boss"
```

Reject any handoff as `INCOMPLETE_HANDOFF` if one of these required fields is missing:

```text
event_type
batch_id or source artifact reference
module
repository
branch
owner_skill
accountable_owner
reviewer_skill
verifier
evidence_path
current_gate_status
forbidden_actions
required_output
```

The receiving AI must not infer or backfill missing fields. It must stop and report to AI PMO.

## 7. Evidence Path Standard v0.1.1

| Evidence Type | Standard Path |
|---|---|
| Governance / RACI | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/` |
| Skill design council output | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/Skill_Design/` |
| Claude Skill package blueprint | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/Skill_Design/Blueprints/` |
| Functional Design | `99_SMEsPlus_Enterprise_Suite/02_Functional_Design/` |
| AI output / review packs | `99_SMEsPlus_Enterprise_Suite/07_Output_From_AI/` |
| ACC batch output | `99_SMEsPlus_Enterprise_Suite/07_Output_From_AI/ACC-<module>_FDS_BATCH_<NNN>/` |
| Review gates | `99_SMEsPlus_Enterprise_Suite/04_Review_Gates/` |
| Testing / UAT evidence | `99_SMEsPlus_Enterprise_Suite/08_Testing_Evidence/` |
| Automation logs | `99_SMEsPlus_Enterprise_Suite/07_Output_From_AI/Automation_Log/` |
| SHA256 manifests | Same folder as artifact package |

If a target folder does not exist, the first authorized GitHub execution may create it. Creation must be reported with commit hash and file path.

## 8. SLA Thresholds v0.1.1

| SLA Item | Threshold | Escalation |
|---|---:|---|
| Skill Architect Controller design draft | 4 working hours | AI PMO -> Boss |
| Skill blueprint review after design draft | 4 working hours | AI PMO -> ChatGPT L99 |
| Owner assignment after new batch or gap | 4 working hours | AI PMO -> Boss |
| Reviewer assignment after review pack prepared | 4 working hours | AI PMO -> Boss |
| Review turnaround for ordinary review | 1 working day | AI PMO -> Boss |
| Critical path review: tax, posting, DB/API, QA/UAT | 8 working hours | AI PMO -> Boss |
| Incomplete handoff correction | 2 working hours | AI PMO -> sender owner |
| Ownerless Make routing event | immediate HOLD | Make -> AI PMO |
| Overdue unresolved blocker | 1 working day | AI PMO -> Boss exception list |

These SLA values are v0.1.1 defaults. Boss or AI PMO may revise before Make go-live.

## 9. Forbidden Actions by Role

Universal forbidden actions for all AI roles:

```text
No PASS
No READY as final status
No APPROVED
No COMPLETE
No DONE
No BUILD READY
No CODING READY
No JIRA READY
No PRODUCTION READY
No RELEASE READY
No MERGE READY
No CERTIFIED
No self-closing gap
No bypass of AI PMO / ChatGPT L99 / Boss
```

Exceptions: phrases such as `REQUIRES CHATGPT L99 REVIEW` or `REQUIRES BOSS DECISION` are allowed because they do not claim completion.

## 10. Gate Movement Rule

A gate may move only when all conditions are true:

1. responsible output exists;
2. evidence path and SHA256/commit/reference are registered;
3. accountable owner is named;
4. reviewer is named;
5. verifier is named;
6. AI PMO confirms owner lock and evidence registration;
7. ChatGPT L99 issues independent governance/evidence verdict for gate movement beyond review state;
8. Boss issues explicit final gate decision when final approval or exception is needed.

No gate may skip state.

Allowed state vocabulary:

```text
DRAFTED
PREPARED ONLY / NOT APPROVED
PUSHED TO GITHUB / NOT REVIEWED
REVIEWED WITH COMMENTS / GATE HOLD
REQUIRES OWNER REVIEW
REQUIRES CHATGPT L99 REVIEW
REQUIRES BOSS DECISION
SKILL_DESIGN_HOLD
```

## 11. Make Automation Readiness Checklist

Make Automation remains HOLD until all checks below are completed.

| Readiness Check | Status |
|---|---|
| RACI v0.1.1 exists in GitHub | PRESENT |
| Claude Skill Architect Controller added | PRESENT |
| AI PMO review of RACI v0.1.1 | NOT YET |
| ChatGPT L99 review of RACI v0.1.1 | NOT YET |
| Boss approval of RACI operating model | NOT YET |
| Named owners for all structural roles | NOT YET |
| Legal / Accounting owner named | NOT YET |
| Canonical payload schema confirmed by Make controller | NOT YET |
| Evidence path standard confirmed by AI PMO | NOT YET |
| Skill Architect Controller blueprint created | NOT YET |
| First Skill package build decision | NOT YET |
| Sandbox/dry-run Make scenario tested | NOT YET |
| Live Make automation go-live approval | NOT YET |

Initial Make scope, when allowed, must start with non-gate actions only:

```text
notify
route to named owner
log evidence
update non-gate status
escalate ownerless/overdue items
```

## 12. Open Items Before Activation

| Open Item | Owner | Status | Gate Impact |
|---|---|---|---|
| Create Claude Skill Architect Controller blueprint | Claude Skill Architect + AI PMO | HOLD | Blocks all Skill package builds |
| Confirm Skill design council output | AI PMO | HOLD | Blocks Skill activation |
| Confirm RACI matrix v0.1.1 | AI PMO | HOLD | Blocks operating model |
| Name all structural role owners | AI PMO + Boss | HOLD | Blocks Make automation |
| Name Thai Tax Legal/Accounting reviewer | Boss / AI PMO | HOLD | Blocks tax/Figma/build gates |
| Confirm SLA thresholds | AI PMO | HOLD | Blocks escalation automation |
| Confirm evidence paths | AI PMO | HOLD | Blocks evidence automation |
| Confirm Make payload schema | Make Automation Controller + AI PMO | HOLD | Blocks Make automation |
| Run first sandbox Make scenario | Make Automation Controller | HOLD | Blocks go-live |
| ChatGPT L99 review | ChatGPT L99 | REQUIRED | Blocks Boss approval |
| Boss approval of operating model | Boss | REQUIRED | Blocks activation |

## 13. Next Required Actions

1. Claude prepares `claude-skill-architect-controller` design blueprint.
2. AI PMO reviews the blueprint and confirms missing fields.
3. ChatGPT L99 reviews the Skill boundary and gate logic.
4. Boss approves the Skill build sequence.
5. Only after that, build the first operational Skill package batch.
6. Live Make automation remains HOLD until Boss approval.

## Final Control Status

```text
RACI v0.1.1: PREPARED IN GITHUB
Claude Skill Architect Controller: ADDED AS P0 META-SKILL
Actual Skill Package Built: NO
AI PMO Review: REQUIRED
ChatGPT L99 Review: REQUIRED
Boss Approval: REQUIRED
Make Automation: HOLD
FDS / Build / DB / API / UAT / Figma: HOLD
```

PREPARED IN GITHUB / CLAUDE SKILL ARCHITECT CONTROLLER REQUIRED FIRST / NOT APPROVED / NOT AUTOMATED YET
