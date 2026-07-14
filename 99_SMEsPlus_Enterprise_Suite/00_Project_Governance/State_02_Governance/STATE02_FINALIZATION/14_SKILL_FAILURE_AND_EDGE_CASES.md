# 14 — SKILL FAILURE AND EDGE CASES

Document ID: S02-FINAL-DOC-14
Skill (simulated): `state-governance-evidence-controller`
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub | Evidence Commit `8570187…`
Prepared By: Claude AI | 2026-07-14 (UTC)

## 1. Remaining-Work Classification (SKT-04 — not all rework)

| Item | Category | Owner of next action |
|---|---|---|
| Correct ACF-001..006, 008 source wording | Defect correction | RO/CAI after S02-FINAL-001 |
| Publish canonical PMO glossary (ACF-010) | Deliverable creation | ES/CAI after S02-FINAL-003 |
| Relabel folder/matrix ownership (ACF-007/009) | Defect correction | DC after S02-FINAL-003 |
| Record independent review of ACF findings | Review | Governance Reviewer (S02-FINAL-005) |
| Record independent verification of ACF findings | Verification | Evidence Verifier (S02-FINAL-005) |
| Confirm Canonical RACI / Ownerless Standard | Boss decision | Boss (S02-FINAL-002/004) |
| Merge finalization branch to SMEsPlus | Merge / administrative closure | Boss-authorized RO (out of scope this state) |

None of the above is misclassified as "rework of Step 01". Step 01 remains CLOSED BY BOSS.

## 2. Edge Cases Handled

| Edge Case | Skill Behaviour | Result |
|---|---|---|
| EC-1: "100% COMPLETE" asserted without independent verification | Accept only where Boss-recorded (Step 01); otherwise mark prepared/HOLD | Handled (doc 07 §5) |
| EC-2: Source file changed since prior register | Re-hash blob at HEAD and compare | Handled — SHAs matched v1.1 (doc 02 §2) |
| EC-3: Reviewer/Verifier absent | Flag INCOMPLETE input; route to Boss; do not self-verify | Handled (doc 12, S02-FINAL-005) |
| EC-4: Duplicate governance docs | Pick one Canonical; classify rest Supporting; create no new duplicate | Handled (docs 03/04/05) |
| EC-5: Pressure to close the State | Return exactly one recommendation; refuse to close | Handled (doc 10, CONDITIONAL CLOSE) |
| EC-6: Joint "Boss / PMO" authority | Detect; recommend Boss-only correction; do not silently rewrite source | Handled (doc 02, doc 08) |
| EC-7: HOLD used as "stop all work" | Apply HOLD = Gate-not-passed ≠ stop permitted work | Handled (doc 04 §3) |
| EC-8: Ambiguous "PMO" term | Do not guess; route glossary to Boss (S02-FINAL-003) | Handled |

## 3. Failure Modes the Skill Must Avoid (self-audit)

| Failure Mode | Avoided? | Guard |
|---|---|---|
| Self-approval (PASS/APPROVED/CLOSED) | Yes | No such claim in package; SK-AC-05 |
| Reopening Step 01 without defect evidence | Yes | SKT-01; doc 01 §2 |
| Fabricating verification | Yes | E3 self-report never accepted (doc 07) |
| Creating a duplicate package | Yes | Reused existing v1.0/v1.1 registers, RACI, ownerless standard |
| Modifying production / merging | Yes | No merge/release/deploy; source unmodified |
| Percentage-as-progress | Yes | Doc 07 §1 |

## 4. Residual Risks (declared, not hidden)

- **R-1:** Independent Reviewer/Verifier identities unrecorded → all ACF findings remain HOLD until
  S02-FINAL-005. This caps the closure verdict at CONDITIONAL CLOSE.
- **R-2:** If Boss rejects S02-FINAL-001, P0 authority conflicts persist into State 03 gate wording.
- **R-3:** GitHub Issue corroboration (#5,#6,#9,#10) is cited from prior sessions; not re-fetched
  this run. Treated as Supporting, not primary, evidence.

Boss is the Sole Final Approver.
