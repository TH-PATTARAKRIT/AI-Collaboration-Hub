# 07_DECISION_AND_EXCEPTION_REGISTER.md

Order: /L99.99 — State 02, Step 08 — Classification Registers
Work Package: WP-08-07 — Decision and Exception Register
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Working Branch: claude/state-02-classification-registers-7qwwcy
Prepared By: Claude Code (Preparer / Executor — Responsible role only)
Prepared At: 2026-07-14 (UTC)
Document Status: PREPARED FOR INDEPENDENT REVIEW
Gate Status: HOLD

## 1. Rule

Boss decisions are never inferred or manufactured. Final Decision Authority for every
decision below is **Boss (sole)**; ChatGPT L99 may only recommend / accept-for-review — L99
holds no final decision authority (P0-02 correction). Boss Decision Status, Application
Status, Independent Verification Status, Merge Status, and Effective Control Status are
recorded as **separate** fields (P0-03 correction): a Boss decision may exist while
application, verification, merge, and effective control are still PENDING/NOT — and an
incomplete verification never reverts a recorded Boss decision back to PENDING.

## 2. Register

Fields: Decision ID | Decision Required | Final Decision Authority | Reviewer Recommendation |
Boss Decision Status | Decision Evidence | Application Status | Independent Verification
Status | Merge Status | Effective Control Status | Affected WPs | Gate Impact.

Legend — Boss Decision Status: RECORDED (with evidence) / PENDING (none recorded).
"RECORDED (unmerged)" means a Boss decision is documented in an unmerged PR and is therefore
not yet effective in the merged base.

| Dec ID | Decision Required | Final Decision Authority | Reviewer Recommendation | Boss Decision Status | Decision Evidence | Application Status | Independent Verification Status | Merge Status | Effective Control Status | Affected WPs | Gate Impact |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DEC-08-01 | Confirm Canonical RACI (DOC-S02-010) as controlling authority model | Boss | ChatGPT L99: confirm with conditions | RECORDED (unmerged) — PR #24 records S02-FINAL-002 "APPROVED and applied" | E1 PR #24 body S02-FINAL-002; DOC-S02-010 | APPLIED on PR #24 branch (unmerged) | PENDING (no independent verifier) | NOT MERGED | NOT EFFECTIVE (unmerged; base 8570187 unchanged) | WP-08-11 | Blocking |
| DEC-08-02 | Approve applying RC-001..010 authority corrections to sources | Boss | ChatGPT L99: approve pending verify | RECORDED (unmerged) — PR #20 records Boss Decision 2 "AUTHORIZED → APPLIED" | E1 PR #20 body; DOC-S02-012 | APPLIED on PR #20 branch (unmerged) | PENDING (preparer-level only) | NOT MERGED | NOT EFFECTIVE (unmerged) | WP-08-03/06 | Blocking |
| DEC-08-03 | Appoint and record named Independent Evidence Verifier (S02-FINAL-005) | Boss | ChatGPT L99: appoint L99-for-E0 + separate non-preparer verifier | PENDING | E5 EV-08-21 (not recorded) | NOT STARTED | PENDING | n/a | NOT EFFECTIVE | WP-08-11/05 | Blocking |
| DEC-08-04 | Accept branch reconciliation (deliver Step 08 on designated branch, new PR #27) | Boss | ChatGPT L99: accept per PR #25 precedent | PENDING | E1 doc 00; PR #25 precedent | Delivered on designated branch (PR #27) | PENDING | NOT MERGED | NOT EFFECTIVE (accept required) | all | Blocking (accept required) |
| DEC-08-05 | Sequencing of overlapping open PRs (#20/#23/#24/#25/#27) | Boss | ChatGPT L99: sequencing per doc 13 | PENDING | E0 PR list | NOT STARTED | PENDING | NOT MERGED | NOT EFFECTIVE | all | Blocking |
| DEC-08-06 | Boss closure decision for Step 08 | Boss | Preparer makes no closure recommendation (independent verify not done) | PENDING | E5 EV-08-22 (not recorded) | NOT STARTED | PENDING | n/a | NOT EFFECTIVE | WP-08-17 | Gate decision |

Note on DEC-08-01 / DEC-08-02: the referenced Boss decisions exist only in unmerged PRs
(#24, #20). They are recorded as decisions, but their Effective Control Status is NOT
EFFECTIVE because those PRs are not merged into the base and independent verification is
still PENDING. This separation is the P0-03 correction: a recorded decision is not the same
as an effective, verified, merged control.

## 3. Exceptions and Waivers

Final approval authority for every exception is **Boss (sole)**. ChatGPT L99 recommends only.

| Exc ID | Exception | Final Approval Authority | Reviewer Recommendation | Requested By | Boss Decision Status | Conditions | Expiry | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| EXC-08-01 | Deliver Step 08 on `claude/state-02-classification-registers-7qwwcy` / new PR #27 instead of PR #24 branch (harness branch-policy constraint) | Boss | ChatGPT L99: accept (per PR #25 precedent) | Claude Code (preparer) | PENDING (disclosed, not self-approved) | Reconciled in doc 13; no merge implied | Until Boss decision DEC-08-04 | Blocking |
| EXC-08-02 | Governance-controller Skill created new (no pre-existing package by that name in repo) | Boss | ChatGPT L99: accept | Claude Code (preparer) | PENDING | Skill is real files, not simulation | On Boss acceptance | Input |

## 4. Rejected Proposals / Supersession Decisions

| Ref | Item | Decision | Evidence |
|---|---|---|---|
| SUP-08-01 | Authority Conflict Register v1.0 superseded by v1.1 | Supersession recorded for tracking (both retained) | E1 DOC-S02-031/032; register v1.1 header |

## 5. Control Statement

Final Decision Authority is Boss (sole) for every decision and exception; ChatGPT L99
recommends only and holds no final decision authority. Where a Boss decision is RECORDED it
is documented in an unmerged PR and is NOT EFFECTIVE until merged and independently verified.
DEC-08-03/04/05/06 remain PENDING — the preparer has not, and may not, decide these.
Exceptions EXC-08-01/02 are disclosed for Boss acceptance and are not self-approved. Decision
Status is recorded separately from Application, Independent Verification, Merge, and Effective
Control Status (P0-03).
