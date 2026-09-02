# 16 — BOSS APPROVAL: BATCH A CONTROLLED RESEARCH ROUTING DIRECTIVE

| Field | Value |
|---|---|
| Project | `SMEsPlus ENTERPRISE SUITE` |
| Workstream | `ACCOUNT_REOPEN / BOSS_DECISION_LEGAL_TAX_ROUTING` |
| Jira | `ERPPLUS-138` |
| Source Routing Package Branch | `audit/account-boss-decision-legal-tax-routing-2026-09-02-001` |
| Source Routing Package Commit | `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6` |
| This Record Branch | `boss/account-batch-a-research-routing-approval-2026-09-02` |
| Boss Decision | Approve Batch A controlled research and routing execution |
| Final Authority | Boss is the sole Final Approver |
| Terminal Status | `BATCH A APPROVED FOR CONTROLLED RESEARCH ROUTING ONLY` |

`No Evidence = No Progress.` `Never Skip Gate.` `Boss is the sole Final Approver.`

## 1. Boss Operating Directive

Boss approved controlled continuation under this operating principle:

> Understand deeply.  
> Transfer accurately.  
> Preserve verifiably.

This directive is now treated as a working control standard for the Account continuation stream.

## 2. Approved Scope

Boss approves Batch A to proceed as controlled research and routing only:

| Priority | Decision ID | Approved Direction | Control Status |
|---|---|---|---|
| 1 | `ACC-DEC-018` | Proceed with `COA-G01` unblock routing | `HOLD UNTIL EVIDENCE VERIFIED` |
| 2 | `ACC-DEC-014` | Proceed with Legal-Tax Review routing for WHT / VAT / CIT / DBD-NPAE | `LEGAL_TAX_REVIEW_REQUIRED` |
| 3 | `ACC-DEC-003` | Treat WHT multi-rate baseline as mandatory research topic | `RESEARCH REQUIRED` |
| 4 | `ACC-DEC-019` | Proceed with Account x Inventory Joint Session 3 routing | `PENDING JOINT SESSION 3` |
| 5 | `ACC-DEC-004`–`ACC-DEC-013` | Include all 10 scope questions as research-required items | `RESEARCH REQUIRED / BOSS FINAL DECISION PENDING` |

## 3. Not Approved By This Decision

This record does not approve:

- Final Accounting Solution
- Functional Design
- UX/UI final design
- Development
- Production implementation
- Gate PASS
- Merge into `SMEsPlus`
- Pull request opening
- Any AI self-approval

## 4. Execution Instruction For Next AI Session

The next executor must use the routing package at:

- Repo: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- Branch: `audit/account-boss-decision-legal-tax-routing-2026-09-02-001`
- Commit: `1fbc64c20d2d2003f1ee0dbeb591bef9a4cd4ff6`
- Key file: `02_BOSS_DECISION_QUEUE.md`

Execution must produce evidence-backed outputs only. Every item must carry Owner, Evidence Location, Status, Gate Impact, and Next Action.

## 5. Required Next Outputs

At minimum, the next execution stream must produce:

1. `COA_G01_UNBLOCK_EXECUTION_RECORD.md`
2. `LEGAL_TAX_REVIEW_ROUTING_EXECUTION_RECORD.md`
3. `ACC_WHT_06_RESEARCH_EXECUTION_RECORD.md`
4. `ACCOUNT_INVENTORY_JOINT_SESSION_3_EXECUTION_RECORD.md`
5. `ACCOUNT_SCOPE_RESEARCH_REGISTER_SC01_SC10.md`
6. `BATCH_A_EVIDENCE_GATE_SUMMARY.md`
7. SHA-256 manifest
8. Session closure with Direct GitHub Links

## 6. PMO Control Notes

- Each stream may proceed in parallel only if evidence ownership is separated.
- COA-G01 remains blocked until source evidence, re-audit, PMO verification, and Boss decision exist.
- Legal-tax items remain `LEGAL_TAX_REVIEW_REQUIRED` until reviewed by qualified Thai legal-tax/accounting authority or supported by authoritative source evidence.
- Account x Inventory items cannot be closed from Account side alone.
- Scope items enter research as mandatory study topics, not as approved final scope.

## 7. Final Classification

# `BATCH A APPROVED FOR CONTROLLED RESEARCH ROUTING ONLY`

This is an approval to continue evidence-controlled research and routing. It is not a Final Solution approval.
