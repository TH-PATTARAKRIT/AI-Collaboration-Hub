---
name: smeplus-state02-governance-controller
description: >-
  SMEsPlus State 02 Governance & Classification controller. Use when working on
  State 02 governance classification registers (Step 08) in
  99_SMEsPlus_Enterprise_Suite/00_Project_Governance/State_02_Governance/. Provides
  Step 08 classification commands, the classification code model, and the read-only
  classification validation script. Boss remains Sole Final Approver; Claude Code is
  Preparer/Executor only.
---

# SMEsPlus State 02 Governance Controller

Control Level: /L99.99 · Repository: TH-PATTARAKRIT/AI-Collaboration-Hub ·
Final Approval Authority: Boss · Independent Governance Reviewer: ChatGPT L99.

This Skill supports **State 02 — Governance, Step 08 — Classification Registers**. It does
not execute Step 09–12. It never approves, verifies, passes a Gate, or closes a Step.

## Locked Controls

```text
No Evidence = No Progress
No Verification = No Pass
No Owner = FROZEN
No Classification = Not Authorized for Execution Control
No Boss Approval = Step Not Closed
```

## Role Model (enforced)

```text
Claude Code                   = Preparer / Executor only
ChatGPT L99                   = Independent Governance Reviewer
Independent Evidence Verifier = Non-preparer identity
Boss                          = Sole Final Approver
AI PMO                        = Support Only
Executive Secretary / Liza    = Coordination and escalation
```
No identity may be both Preparer and Verifier, Preparer and Final Approver, Claude Code and
Independent Reviewer, AI PMO and Accountable Owner, or AI and Final Approver.

## Step Definition

```text
Step 08 = Classification Registers
```

## Commands

| Command | Action |
|---|---|
| `/smeplus-state02-governance-controller step08` | Show Step 08 scope, WP-08-01..17, and current package status. |
| `/smeplus-state02-governance-controller classify-documents` | Prepare/refresh the Document Classification Register (doc 03). One CANONICAL per topic; no UNCLASSIFIED/SUPERSEDED controls execution. |
| `/smeplus-state02-governance-controller classify-evidence` | Prepare/refresh the Evidence Classification Register (doc 05) using E0–E5; E4≠progress, E5=HOLD/FAIL/FROZEN. |
| `/smeplus-state02-governance-controller reconcile-step08` | Reconcile Step 08 against PR #20/#23/#24/#25 and prior State 02 material (doc 13). No merge, no close. |
| `/smeplus-state02-governance-controller validate-step08` | Run `scripts/validate_state02_classification.py` read-only; emit STEP08_VALIDATION_REPORT.md; non-zero exit on critical. |
| `/smeplus-state02-governance-controller report-step08` | Produce the Boss Executive Classification Report (doc 16) with two separate progress figures. |

## Command Details

- **step08** — Read `references/step08-classification-registers.md`, then summarize WP status
  from the Step 08 package. Report Execution Preparation and Official Step Closure progress
  separately; never combine them.
- **classify-documents** — Inspect all State 02 governance documents; assign exactly one DOC
  classification each; flag competing CANONICAL as CONFLICT; require Superseded By on any
  SUPERSEDED; never delete historical evidence.
- **classify-evidence** — Assign E0–E5; record location, timestamp, and integrity method; do
  not count E4 claims as verified progress; classify E5 as HOLD/FAIL/FROZEN by criticality.
- **reconcile-step08** — Update the Reclassification and Reconciliation Log; cross-reference
  open PRs and unmerged Step 05/closure/finalization material; propose (not apply) sequencing.
- **validate-step08** — `python3 scripts/validate_state02_classification.py <pkg_dir>`; the
  script is read-only and never rewrites source registers.
- **report-step08** — Emit the Boss report; leave Review/Verification/Approval/Closure to the
  independent and Boss roles.

## Validation Script

`scripts/validate_state02_classification.py` — read-only; detects missing mandatory fields,
duplicate IDs, duplicate CANONICAL, missing Owner/Reviewer/Verifier, missing evidence
location/timestamp, unsupported PASS/APPROVED, unclassified/superseded documents controlling
execution, broken references, P0 without escalation, inline secrets, and stale/mismatched
manifests. Self-test covers mandatory tests T08-01..T08-10.

## Boundaries

Draft PR only. No merge, release, deploy, production change, Final Gate, or State/Step
closure. Do not prefill PASS or APPROVED. Boss remains the Sole Final Approver.

> If newly added commands are not discoverable, a Claude Code restart may be required for
> skill command discovery.
