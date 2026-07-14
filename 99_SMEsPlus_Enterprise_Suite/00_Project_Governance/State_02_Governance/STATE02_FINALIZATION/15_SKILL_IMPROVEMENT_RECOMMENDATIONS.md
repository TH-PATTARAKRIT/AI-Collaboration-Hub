# 15 — SKILL IMPROVEMENT RECOMMENDATIONS

Document ID: S02-FINAL-DOC-15
Skill (simulated): `state-governance-evidence-controller`
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub | Evidence Commit `8570187…`
Prepared By: Claude AI | 2026-07-14 (UTC)

These recommendations are for a future **installed** Skill. They are advisory; adoption is a Boss
decision.

## 1. Recommended Enhancements

| ID | Recommendation | Rationale | Priority |
|---|---|---|---|
| SI-01 | Auto re-hash every cited source file (`git hash-object`) and diff against the last register's recorded SHA on every run | Detected value this run (EC-2); makes "unchanged since last register" a machine assertion | High |
| SI-02 | Require a named Reviewer and Verifier identity as a hard input; block VERIFIED transitions until both are recorded | The single biggest gap this run (R-1, S02-FINAL-005) | High |
| SI-03 | Maintain a controlled synonym/glossary map (e.g. PMO → {human PMO, AI PMO Support-Only, coordination office}) and flag any bare ambiguous term | Root cause of ACF-007/009/010 | High |
| SI-04 | Emit the Boss Approval Queue in a machine-parseable table (Decision ID keyed) so approvals can be recorded back per-ID | Improves SKT-06 usability and closes the loop | Medium |
| SI-05 | Enforce a "one Canonical per topic" invariant and fail if two Canonical candidates target the same topic | Strengthens SKT-05 / SK-AC-08 | Medium |
| SI-06 | Add a closure gate that mechanically blocks CLOSE (allows only CONDITIONAL/DO-NOT) while any P0 conflict lacks a recorded Boss decision | Hard-enforces SK-AC-06 | High |
| SI-07 | Capture GitHub Issue/PR corroboration by live fetch and tier it (E0/E1) rather than citing prior-session summaries | Removes R-3 | Medium |
| SI-08 | Distinguish "prepared 100%" from "verified 100%" as separate fields everywhere a percentage appears | Prevents percentage-as-progress (doc 07) | High |

## 2. Non-Goals (explicitly out of scope for the Skill)

- The Skill must never acquire authority to approve gates, publish canonical documents, merge,
  release, deploy, or approve production. These remain Boss-only (Ownerless Standard §7).
- The Skill must never appoint an Acting Owner on SLA expiry alone; appointment stays a Boss decision.

## 3. Adoption Note

Adopting SI-02 and SI-06 would let a future run reach `RECOMMEND CLOSE` (not merely CONDITIONAL) once
Boss records the Reviewer/Verifier identities and the P0 decisions — because the remaining gap this
run is precisely recorded independent verification, which SI-02 makes a first-class input.

Boss is the Sole Final Approver.
