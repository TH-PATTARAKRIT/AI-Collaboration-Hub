# 02_CLASSIFICATION_CODE_DICTIONARY.md

Order: /L99.99 — State 02, Step 08 — Classification Registers
Work Package: WP-08-02 — Classification Code Dictionary
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Working Branch: claude/state-02-classification-registers-7qwwcy
Prepared By: Claude Code (Preparer / Executor — Responsible role only)
Prepared At: 2026-07-14 (UTC)
Document Status: PREPARED FOR INDEPENDENT REVIEW
Gate Status: HOLD

Every code below is defined with: Code, Name, Definition, Entry Criteria, Exit Criteria,
Allowed Authority, Required Evidence, Gate Impact, Next Allowed Status, Invalid Usage.

---

## DOC — Document Classification

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| DOC-CANON | CANONICAL | Single controlling document for a governance topic | One-per-topic; Boss-confirmed | Superseded/archived | Boss confirms; DC executes | E1 path + Boss approval record | Controls execution | SUPERSEDED, ARCHIVED | Two CANONICAL for one topic (=CONFLICT) |
| DOC-SUP | SUPPORTING | Aids a canonical document; not controlling | Linked to a canonical topic | Reclassified | DC/CAI prepare | E1/E2 path | Input | CANONICAL (on approval), ARCHIVED | Used to control execution |
| DOC-WIP | WORKING DRAFT | In-progress, not controlling | Draft under preparation | Promoted/archived | CAI/DC | E1 path | None | SUPPORTING, CANONICAL, SUPERSEDED | Treated as approved/controlling |
| DOC-SUPD | SUPERSEDED | Replaced by a named newer version | Replacement named | Archived | Boss/DC | E1 path + Superseded By | Removed from control | ARCHIVED | Still controlling execution (=FAIL) |
| DOC-ARC | ARCHIVED | Retained, out of active control | Archive record exists | — (terminal) | DC | Archive record + SHA-256 pair | None | RETAINED AS EVIDENCE | Deleted |
| DOC-EVID | RETAINED AS EVIDENCE | Kept as historical evidence | Cited as evidence | — | DC/EV | E0–E2 reference | Input to audit | ARCHIVED | Modified or deleted |
| DOC-UNC | UNCLASSIFIED | Not yet classified | Newly discovered | Classified | CAI/DC | Path only | Cannot control execution | any DOC-* | Used for Gate/execution (=FROZEN) |

## EVD — Evidence Classification

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| EVD-E0 | System-generated | Independently inspectable system output (commit, hash, CI) | System artifact exists | Superseded | EV inspects | The artifact itself | Strong | E1 | Fabricated |
| EVD-E1 | Repository primary | Repository-controlled primary evidence | File at path + SHA | Superseded | CAI/EV | Path + commit/blob SHA | Strong | E0 | Claimed without path |
| EVD-E2 | Reviewed documentary | Reviewed document evidence | Reviewed record | Superseded | GR/EV | Reviewed record | Moderate | E1 | Unreviewed |
| EVD-E3 | Supporting | Secondary/contextual support | Linked support | Reclassified | CAI | Reference | Weak | E2 | Sole basis for PASS |
| EVD-E4 | Claim | Unverified status update / assertion | Stated claim | Verified/rejected | any | Statement only | None (not progress) | E0–E2 on verify | Counted as verified progress |
| EVD-E5 | Missing/inaccessible | Absent or unreachable evidence | Referenced but absent | Located | EV records | Absence note | HOLD/FAIL/FROZEN | E0–E2 on locate | Ignored silently |

## WRK — Work Item Classification

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| WRK-REQ | Requirement | Governance/step requirement | Stated requirement | Delivered | CAI/ES | Requirement text + path | Input | WRK-DELIV | Ownerless and active |
| WRK-WP | Work Package | Defined WP | Order defines WP | Delivered | CAI/ES | WP definition | Input | WRK-DELIV | Ownerless (=FROZEN) |
| WRK-DELIV | Deliverable | A produced artifact | Artifact exists | Verified | CAI | E1 path | Input | verified | Claimed absent artifact |
| WRK-ACT | Open Action | Correction/review/verify/decision action | Action opened | Closed w/ evidence | ES/CAI | Action record | Blocking if P0/P1 | closed | Closed without evidence |

## RAID — Risk, Assumption, Issue, Dependency

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| RAID-R | Risk | Potential future adverse event | Identified risk | Mitigated/closed | Owner | Mitigation + evidence | Blocking if P0 | monitored/closed | P0 without Owner (=FROZEN) |
| RAID-A | Assumption | Unconfirmed basis for work | Stated assumption | Confirmed/voided | Owner | Confirmation evidence | Input | confirmed | Treated as fact |
| RAID-I | Issue | Realized problem | Issue occurred | Resolved | Owner | Resolution evidence | Blocking if P0 | resolved | Unowned P0 |
| RAID-D | Dependency | Reliance on external item | Dependency exists | Satisfied | Owner | Link/evidence | Blocking if critical | satisfied | Unlinked critical dependency |

## DEC — Decision and Exception

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| DEC-BOSS | Boss Decision | Decision reserved to Boss | Decision required | Decision recorded | Boss only | Boss decision record | Gate decision | recorded | Inferred/manufactured |
| DEC-GOV | Governance Decision | Governance-level decision | Decision required | Recorded | Boss/ES per RACI | Decision record | Input | recorded | Self-decided by preparer |
| DEC-EXC | Exception/Waiver | Temporary approved deviation | Deviation exists | Expiry/closure | Boss | Exception record + expiry | Conditional | closed | Permanent/undated |
| DEC-REJ | Rejected Proposal | Proposal declined | Decision recorded | — | Boss | Decision record | None | — | Re-executed after rejection |

## PRI — Priority

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| PRI-P0 | Critical blocker | Blocks State/Gate | Critical impact | Resolved | Owner/ES | Escalation data | Blocking | resolved | P0 without escalation |
| PRI-P1 | High-impact blocker | Major impact, blocks step | High impact | Resolved | Owner/ES | Action + due date | Blocking | resolved | Ignored |
| PRI-P2 | Important non-blocking | Important, not blocking | Material | Resolved | Owner | Record | Input | resolved | Escalated as P0 |
| PRI-P3 | Administrative | Improvement/admin | Minor | Resolved | Owner | Record | None | resolved | Blocking a gate |

## SEV — Severity

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| SEV-S0 | State/Gate integrity failure | Breaks state/gate integrity | Integrity broken | Corrected | ES/Boss | Correction evidence | FAIL/FROZEN | corrected | Downgraded silently |
| SEV-S1 | Major governance failure | Major control failure | Major failure | Corrected | ES | Evidence | Blocking | corrected | Unrecorded |
| SEV-S2 | Material control weakness | Material weakness | Material | Corrected | Owner | Evidence | HOLD | corrected | Ignored |
| SEV-S3 | Minor control/doc issue | Minor issue | Minor | Corrected | Owner | Evidence | Input | corrected | Escalated as S0 |
| SEV-S4 | Observation | Improvement note | Observation | Noted | Owner | Note | None | noted | Blocking a gate |

## EXE — Execution Status

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| EXE-NS | NOT STARTED | Work not begun | Item exists | Started | CAI | — | None | DRAFT | Reported as progress |
| EXE-DR | DRAFT | Draft in progress | Draft exists | Advanced | CAI | E1 path | None | IN PROGRESS | Reported as complete |
| EXE-IP | IN PROGRESS | Actively worked | Work ongoing | Submitted | CAI | E1 path | None | IN REVIEW | =APPROVED |
| EXE-IR | IN REVIEW | Under review | Submitted | Reviewed | GR | Review record | Input | READY FOR VERIFICATION | =VERIFIED |
| EXE-RV | READY FOR VERIFICATION | Ready for verify | Review done | Verified | EV | Handoff record | Input | EXECUTION COMPLETE | =PASS |
| EXE-HD | HOLD | Paused pending decision | Blocker exists | Released | ES | Reason record | HOLD | any | Hidden |
| EXE-RW | REWORK REQUIRED | Rework needed | Defect found | Reworked | CAI | Defect record | HOLD | IN PROGRESS | Ignored |
| EXE-EC | EXECUTION COMPLETE | Preparation complete | All prep done | Retired | CAI | E1 evidence | Input (not approval) | — | =APPROVED / =CLOSED |
| EXE-RT | RETIRED | No longer active | Superseded | — | DC | Archive record | None | — | Deleted |

## VER — Verification Status

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| VER-NS | NOT SUBMITTED | Not submitted for verify | — | Submitted | CAI | — | None | PENDING REVIEW | =VERIFIED |
| VER-PR | PENDING REVIEW | Awaiting review | Submitted | Reviewed | GR | — | Input | PENDING VERIFICATION | Skipped |
| VER-PV | PENDING VERIFICATION | Awaiting verify | Reviewed | Verified | EV | — | Input | PARTIALLY VERIFIED/VERIFIED | =PASS |
| VER-PARV | PARTIALLY VERIFIED | Some evidence verified | Partial verify | Full verify | EV | Partial record | Conditional | VERIFIED | Reported as VERIFIED |
| VER-V | VERIFIED | Independently verified | Non-preparer verify done | — | EV (≠ preparer) | Verifier record | Strong | — | Self-verified by preparer |
| VER-REJ | REJECTED | Verification failed | Defect found | Reworked | EV | Rejection record | FAIL | REWORK REQUIRED | Suppressed |
| VER-INA | INACCESSIBLE | Evidence unreachable | E5 | Located | EV | Absence note | HOLD/FAIL | PENDING VERIFICATION | Ignored |

## GATE — Gate Status

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| GATE-PASS | PASS | Gate passed | Review+verify+Boss | — | Boss | Full evidence chain | Decision | — | Declared by preparer |
| GATE-PWC | PASS WITH CONTROL | Pass with conditions | Conditions defined | Conditions met | Boss | Evidence + conditions | Conditional | PASS | Unconditional use |
| GATE-HD | HOLD | Gate held | Open items | Cleared | GTR→Boss | Open-item list | Blocking | any | Treated as PASS |
| GATE-FAIL | FAIL | Gate failed | Control missing | Corrected | GTR→Boss | Failure record | Blocking | HOLD | Hidden |
| GATE-FRZ | FROZEN | Frozen (no owner/no classification) | Missing owner/class | Assigned | ES | Freeze record | Blocking | HOLD | Overridden silently |
| GATE-NA | NOT APPLICABLE | Gate not applicable | Justified | — | GTR | Justification | None | — | Used to skip control |

## CONF — Confidentiality

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| CONF-PUB | PUBLIC | Public information | Cleared for public | Reclassified | DC/Boss | Classification note | None | INTERNAL | Contains secrets |
| CONF-INT | INTERNAL | Internal-only | Internal use | Reclassified | DC | Note | None | CONFIDENTIAL | Published |
| CONF-CONF | CONFIDENTIAL | Restricted internal | Sensitive | Reclassified | DC/ES | Note | Input | RESTRICTED | Broad access |
| CONF-RES | RESTRICTED | Highly restricted | Highly sensitive | Reclassified | ES/Boss | Note | Input | SECRET-REF | Copied widely |
| CONF-SEC | SECRET/CREDENTIAL — REFERENCE ONLY | Secret; store reference only | Secret exists | — | Boss/secret owner | Reference to secret store only | Blocking if leaked | — | Secret copied into register |

## ACC — Access

| Code | Name | Definition | Entry Criteria | Exit Criteria | Allowed Authority | Required Evidence | Gate Impact | Next Allowed Status | Invalid Usage |
|---|---|---|---|---|---|---|---|---|---|
| ACC-V | View | May view only | Grant recorded | Revoked | DC/ES | Access record | None | EDIT | Edit under view grant |
| ACC-E | Edit | May edit | Grant recorded | Revoked | DC/ES | Access record | Input | APPROVE | Approve under edit grant |
| ACC-A | Approve | May approve (Boss for final) | Grant recorded | Revoked | Boss/ES | Access record | Decision | — | AI holding final-approve |
| ACC-N | No Access | No access | Default | Granted | DC/ES | — | None | VIEW | Silent access |

## Notes

- Codes are unique within their group. Cross-group combination (e.g., a document that is
  DOC-CANON, CONF-INT, EXE-EC, VER-PV) is expected; each dimension is recorded separately.
- No code in EXE, VER, or GATE implies APPROVAL. Approval is a separate DEC-BOSS decision.
