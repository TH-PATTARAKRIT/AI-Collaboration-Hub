# SMEsPlus AI Skill RACI Matrix v0.1

Document ID: SMEPLUS-AIOS-RACI-001
Version: v0.1
Priority: P0
Status: AI PMO OFFICIALIZATION PREPARED / CHATGPT L99 REVIEW REQUIRED / NOT APPROVED / NOT AUTOMATED YET
Control Level: /L99.99
Prepared From: Claude AI draft `SMEsPlus_AI_SKILL_RACI_MATRIX_v0.1_DRAFT.md`
L99 Update By: ChatGPT L99 Gate Reviewer
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Path: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEsPlus_AI_SKILL_RACI_MATRIX_v0.1.md`
Generated: 2026-07-08 (Asia/Bangkok)

## Executive Summary

This document converts the Claude AI draft RACI matrix into an AI PMO-controlled v0.1 baseline for SMEsPlus AI collaboration.

This version is intended to make the workflow traceable in GitHub before Make Automation 100 percent is activated.

Current control result:

```text
GitHub Tracking: ENABLED
Operating Model Approval: NOT APPROVED
Make Automation Go-Live: HOLD
FDS / Build / DB / API / UAT / Figma Gates: HOLD
Next Required Review: AI PMO + ChatGPT L99 + Boss decision
```

## 1. AI Role Map

| # | Role / Skill | Category | Primary Function | Authority Limit |
|---|---|---|---|---|
| 1 | ai-pmo-owner-lock | Governance | Lock named owners, register evidence, control routing/status | No final approval |
| 2 | smesplus-expert-fds-designer | Drafting | Draft/revise Functional Specification artifacts | No self-approval, no gate closure |
| 3 | accounting-posting-review-prep | Review Prep | Prepare posting rule review packs | Cannot certify accounting correctness |
| 4 | thai-tax-review-prep | Review Prep | Prepare Thai VAT/WHT/tax review packs | Cannot claim legal/tax compliance |
| 5 | db-design-review-prep | Review Prep | Prepare data model/entity review packs | Cannot certify DB design |
| 6 | enterprise-api-review-prep | Review Prep | Prepare API/SaaS architecture review packs | Cannot certify architecture |
| 7 | qa-uat-package-generator | QA | Generate UAT case packages | Cannot declare UAT pass |
| 8 | make-automation-controller | Automation | Route, notify, log, collect evidence, escalate | Cannot approve, merge, release, deploy, or close gate |
| 9 | intelligently-designed-erp-reviewer | Domain Review | Review ERP/accounting logic correctness | Recommendation only |
| 10 | chatgpt-l99-gate-reviewer | Governance Review | Independent evidence/gate review | Cannot replace Boss final decision |
| 11 | Boss | Final Authority | Final decision, exception approval, owner nomination | Must log final/exception decisions |

## 2. Skill-to-Owner RACI Matrix

Legend: R = Responsible, A = Accountable, C = Consulted, I = Informed.

| Activity | AI PMO | FDS Designer | Posting Prep | Thai Tax Prep | DB Prep | API Prep | QA/UAT | Make | ERP Reviewer | ChatGPT L99 | Boss |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FDS Drafting | I | R/A | - | - | - | - | - | I | C | I | I |
| FDS Revision | I | R/A | - | - | - | - | - | I | C | C | I |
| Posting Rules Review Pack | I | C | R/A | - | - | - | - | I | C | I | I |
| Posting Rules Domain Check | I | I | C | - | - | - | - | I | R/A | I | I |
| Thai Tax Review Pack | I | C | - | R/A | - | - | - | I | C | I | I |
| Thai Tax Legal/Compliance Confirmation | I | I | - | R facilitator only | - | - | - | I | C | C | A named legal/accounting owner required |
| Data Entity Review Pack | I | C | - | - | R/A | - | - | I | C | I | I |
| API Contract Review Pack | I | C | - | - | C | R/A | - | I | C | I | I |
| UAT Case Formalization | I | C | - | - | - | - | R/A | I | C | I | I |
| Owner Naming / RACI Lock | R/A | C | C | C | C | C | C | I | C | I | C/A for human owner nomination |
| Evidence Registration | R/A | C | C | C | C | C | C | I | I | I | I |
| Gate Status Movement | C | I | I | I | I | I | I | I | I | R/A recommendation | C/A for final movement |
| Independent Governance Verdict | I | I | I | I | I | I | I | I | I | R/A | I |
| Automation Routing / Payload Dispatch | C | I | I | I | I | I | I | R/A | I | I | I |
| Overdue / Ownerless Escalation | R | I | I | I | I | I | I | R | I | I | A |
| Final Gate Approval | I | I | I | I | I | I | I | I | I | C | R/A |
| Exception Handling | C | I | I | I | I | I | I | I | I | C | R/A |

## 3. Execution Surface Rules

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

## 4. Canonical Handoff Payload v0.1

This reconciles the earlier 7-field and 12-field lists. This is the authoritative payload for Make and AI-to-AI routing.

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

## 5. Evidence Path Standard v0.1

| Evidence Type | Standard Path |
|---|---|
| Governance / RACI | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/` |
| Functional Design | `99_SMEsPlus_Enterprise_Suite/02_Functional_Design/` |
| AI output / review packs | `99_SMEsPlus_Enterprise_Suite/07_Output_From_AI/` |
| ACC batch output | `99_SMEsPlus_Enterprise_Suite/07_Output_From_AI/ACC-<module>_FDS_BATCH_<NNN>/` |
| Review gates | `99_SMEsPlus_Enterprise_Suite/04_Review_Gates/` |
| Testing / UAT evidence | `99_SMEsPlus_Enterprise_Suite/08_Testing_Evidence/` |
| Automation logs | `99_SMEsPlus_Enterprise_Suite/07_Output_From_AI/Automation_Log/` |
| SHA256 manifests | Same folder as artifact package |

If a target folder does not exist, the first authorized GitHub execution may create it. Creation must be reported with commit hash and file path.

## 6. SLA Thresholds v0.1

| SLA Item | Threshold | Escalation |
|---|---:|---|
| Owner assignment after new batch or gap | 4 working hours | AI PMO -> Boss |
| Reviewer assignment after review pack prepared | 4 working hours | AI PMO -> Boss |
| Review turnaround for ordinary review | 1 working day | AI PMO -> Boss |
| Critical path review: tax, posting, DB/API, QA/UAT | 8 working hours | AI PMO -> Boss |
| Incomplete handoff correction | 2 working hours | AI PMO -> sender owner |
| Ownerless Make routing event | immediate HOLD | Make -> AI PMO |
| Overdue unresolved blocker | 1 working day | AI PMO -> Boss exception list |

These SLA values are v0.1 defaults. Boss or AI PMO may revise before Make go-live.

## 7. Forbidden Actions by Role

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

## 8. Gate Movement Rule

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
```

## 9. Make Automation Readiness Checklist

Make Automation remains HOLD until all checks below are completed.

| Readiness Check | Status |
|---|---|
| RACI v0.1 exists in GitHub | PRESENT |
| AI PMO review of RACI v0.1 | NOT YET |
| ChatGPT L99 review of RACI v0.1 | NOT YET |
| Boss approval of RACI operating model | NOT YET |
| Named owners for all 10 structural roles | NOT YET |
| Legal / Accounting owner named | NOT YET |
| Canonical payload schema confirmed by Make controller | NOT YET |
| Evidence path standard confirmed by AI PMO | NOT YET |
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

## 10. Open Items Before Activation

| Open Item | Owner | Status | Gate Impact |
|---|---|---|---|
| Confirm 17-activity RACI matrix | AI PMO | HOLD | Blocks operating model |
| Name all 10 structural role owners | AI PMO + Boss | HOLD | Blocks Make automation |
| Name Thai Tax Legal/Accounting reviewer | Boss / AI PMO | HOLD | Blocks tax/Figma/build gates |
| Confirm SLA thresholds | AI PMO | HOLD | Blocks escalation automation |
| Confirm evidence paths | AI PMO | HOLD | Blocks evidence automation |
| Confirm Make payload schema | Make Automation Controller + AI PMO | HOLD | Blocks Make automation |
| Run first sandbox Make scenario | Make Automation Controller | HOLD | Blocks go-live |
| ChatGPT L99 review | ChatGPT L99 | REQUIRED | Blocks Boss approval |
| Boss approval of operating model | Boss | REQUIRED | Blocks activation |

## 11. Next Required Actions

1. AI PMO reviews this file and issues `AI PMO OWNER LOCK REVIEW`.
2. AI PMO names owners or escalates missing names to Boss.
3. Make Automation Controller confirms payload schema and first sandbox scenario.
4. ChatGPT L99 reviews official v0.1.
5. Boss decides whether to activate as operating model.
6. Live Make automation remains HOLD until Boss approval.

## Final Control Status

```text
RACI v0.1: PREPARED IN GITHUB
AI PMO Review: REQUIRED
ChatGPT L99 Review: REQUIRED
Boss Approval: REQUIRED
Make Automation: HOLD
FDS / Build / DB / API / UAT / Figma: HOLD
```

PREPARED IN GITHUB / NOT APPROVED / NOT AUTOMATED YET
