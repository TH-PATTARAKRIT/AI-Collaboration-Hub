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

Boss decisions are never inferred or manufactured. "Actual Decision = PENDING" means no
decision has been recorded. Only decisions with a real recorded evidence source are shown
as decided.

## 2. Register

Fields: Decision ID | Decision Required | Decision Authority | Available Options |
Recommended Option | Actual Decision | Decision Date | Evidence | Affected Documents |
Affected Work Packages | Expiry Date | Exception Conditions | Gate Impact

| Dec ID | Decision Required | Authority | Available Options | Recommended | Actual Decision | Date | Evidence | Affected Docs | Affected WPs | Expiry | Exception Conditions | Gate Impact |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| DEC-08-01 | Confirm Canonical RACI (DOC-S02-010) as controlling authority model | Boss | (a) Confirm (b) Confirm with conditions (c) Reject | (a) Confirm with conditions pending independent verify | PENDING | — | E1 DOC-S02-010; PR #24 S02-FINAL-002 | DOC-S02-010; doc 11 | WP-08-11 | n/a | n/a | Blocking |
| DEC-08-02 | Approve applying RC-001..010 authority corrections to sources | Boss | (a) Approve (b) Approve subset (c) Hold | (a) Approve pending independent verify | PENDING (PR #20 records "AUTHORIZED IN PRINCIPLE"; not independently verified) | — | E1 PR #20 body; DOC-S02-012 | DOC-S02-002/003/004/006 | WP-08-03/06 | n/a | n/a | Blocking |
| DEC-08-03 | Appoint and record named Independent Evidence Verifier (S02-FINAL-005) | Boss | (a) Appoint L99-for-system-evidence + separate human verifier (b) Appoint other | (a) | PENDING | — | E5 EV-08-21 | doc 11; all evidence | WP-08-11/05 | n/a | Verifier ≠ preparer | Blocking |
| DEC-08-04 | Accept branch reconciliation (deliver Step 08 on designated branch, new PR) | Boss / ChatGPT L99 | (a) Accept per PR #25 precedent (b) Require move to PR #24 branch | (a) Accept | PENDING | — | E1 doc 00; PR #25 precedent | doc 00; doc 13 | all | n/a | New PR is not a merge; no branch created to escape a block | Blocking (accept required) |
| DEC-08-05 | Sequencing of overlapping open PRs (#20/#23/#24/#25/this) | Boss | (a) Merge order defined (b) Consolidate (c) Hold all | Provide sequencing (doc 13 recommendation) | PENDING | — | E0 PR list | doc 13 | all | n/a | n/a | Blocking |
| DEC-08-06 | Boss closure decision for Step 08 | Boss | (a) Close (b) Close with conditions (c) Hold | Not recommended by preparer (independent review not done) | PENDING | — | E5 EV-08-22 | doc 17 | WP-08-17 | n/a | n/a | Gate decision |

## 3. Exceptions and Waivers

| Exc ID | Exception | Authority | Requested By | Actual Decision | Conditions | Expiry | Gate Impact |
|---|---|---|---|---|---|---|---|
| EXC-08-01 | Deliver Step 08 on `claude/state-02-classification-registers-7qwwcy` instead of PR #24 branch (harness branch-policy constraint) | Boss | Claude Code (preparer) | PENDING (disclosed, not self-approved) | Must be accepted by Boss/L99; reconciled in doc 13; no merge implied | Until Boss decision DEC-08-04 | Blocking |
| EXC-08-02 | Governance-controller Skill created new (no pre-existing package by that name in repo) | Boss / Executive Secretary | Claude Code (preparer) | PENDING | Skill is real files, not simulation; command discovery may need restart | On Boss acceptance | Input |

## 4. Rejected Proposals / Supersession Decisions

| Ref | Item | Decision | Evidence |
|---|---|---|---|
| SUP-08-01 | Authority Conflict Register v1.0 superseded by v1.1 | Supersession recorded for tracking (both retained) | E1 DOC-S02-031/032; register v1.1 header |

## 5. Control Statement

No Boss decision above is recorded as made. Every "Actual Decision = PENDING" is literal:
the preparer has not, and may not, decide these. Exceptions EXC-08-01/02 are disclosed for
Boss/independent acceptance and are not self-approved.
