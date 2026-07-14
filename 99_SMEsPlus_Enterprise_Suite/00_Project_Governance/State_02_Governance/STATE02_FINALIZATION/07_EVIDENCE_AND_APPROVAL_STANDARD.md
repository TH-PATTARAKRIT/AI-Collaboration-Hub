# 07 — EVIDENCE AND APPROVAL STANDARD

Document ID: S02-FINAL-DOC-07
State: 02 — Governance / Step 07 — Evidence & Approval Standard
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Evidence Commit Reviewed: `8570187bc0f13835be154d10cdc09bfa98e1dfe9`
Prepared By: Claude AI (Responsible / analysis only)
Prepared At: 2026-07-14 (UTC)

## 1. Core Rule

```text
A percentage without evidence is NOT verified progress.
No Evidence = No Progress.
Verified ≠ Prepared. Prepared by Claude AI is Responsible work only, never an approval.
Boss is the Sole Final Approver.
```

## 2. Mandatory Fields for Every Controlled Item

Every controlled work item MUST carry all of:

| # | Field | Rule |
|---|---|---|
| 1 | Work item | Named, uniquely identifiable |
| 2 | Owner | Exactly one Accountable owner (human where authority applies; AI PMO never Accountable) |
| 3 | Evidence location | Repo path + line/section, or commit SHA, or system record URL |
| 4 | Timestamp | UTC date/time of the evidence |
| 5 | Reviewer | Independent Governance Reviewer identity (≠ preparer) |
| 6 | Verifier | Independent Evidence Verifier identity (≠ preparer, ≠ reviewer where feasible) |
| 7 | Verification result | VERIFIED / NOT VERIFIED / HOLD — with the inspected evidence reference |
| 8 | Gate impact | Which gate the item blocks, informs, or decides |
| 9 | Boss decision | Where final State/Gate approval is required |

An item missing field 3, 4, or 7 is **NOT VERIFIED** and cannot count as progress.

## 3. Evidence Tiers

| Tier | Meaning | Example |
|---|---|---|
| E0 System evidence | Independently inspectable machine record | commit SHA, blob SHA, branch ref, CI record |
| E1 Repository evidence | File path + line/section at a known commit | `AI_ROLE_AND_RESPONSIBILITY.md:160 @ ed333098…` |
| E2 Register evidence | Controlled register entry with owner + timestamp | ACF-005 row in doc 02 |
| E3 Self-report | Claude AI narrative | **Never** sufficient alone; must be backed by E0/E1/E2 |

Claude AI self-report (E3) is never accepted as verification. This is enforced by SKT-02.

## 4. Approval Standard

| Approval Type | Who | Evidence of Approval |
|---|---|---|
| Gate approval | Boss only | Boss approval record (dated) |
| Canonical publication | Boss approves; DC publishes | Boss record + publication commit SHA |
| Merge / Release / Deploy / Production | Boss only (PROHIBITED this state) | Boss record — not exercised in State 02 |
| Review sign-off | Independent Reviewer (GR) | Traceable per-item review decision |
| Verification sign-off | Independent Verifier (EV) | Per-item verifier result with inspection trace |

No AI may issue any of the above approvals. No joint final approval is valid.

## 5. Application to This Finalization (worked example)

| Item | Evidence (E-tier) | Verifier | Result | Honest status |
|---|---|---|---|---|
| Source conflicts unchanged since v1.1 | E0 blob SHAs re-hashed at HEAD (doc 02 §2) | Not yet independent (CAI computed) | Consistent, awaiting EV | Prepared; independent verification PENDING |
| Step 01 CLOSED BY BOSS | E1/E2 STATE01_CLOSURE_CONFIRMATION.md | Boss (2026-07-13) | VERIFIED CLOSED | Verified fact |
| ACF-001..010 exist at cited lines | E1 line numbers confirmed at HEAD | Not yet independent | Consistent | Prepared; EV PENDING |
| Canonical RACI meets structural rules | E1 source §3/§4 | Not yet independent | Consistent | Prepared; GR/EV PENDING |

This table deliberately separates **verified facts** (Boss-recorded) from **prepared/consistent**
items awaiting independent review/verification. No percentage is asserted as verified progress.

## 6. Control Statement

Boss is the Sole Final Approver. Any item lacking evidence is HOLD or NOT VERIFIED, never "done".
Claude AI does not self-verify and does not self-approve.
