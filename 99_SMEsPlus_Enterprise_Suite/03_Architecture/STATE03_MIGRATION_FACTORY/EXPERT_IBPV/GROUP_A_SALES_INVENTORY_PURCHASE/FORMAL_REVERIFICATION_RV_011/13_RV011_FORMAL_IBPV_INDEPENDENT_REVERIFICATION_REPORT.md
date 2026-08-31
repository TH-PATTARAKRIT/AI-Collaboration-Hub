> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 13 — FORMAL IBPV INDEPENDENT RE-VERIFICATION REPORT

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D13`
Project: SMEsPlus ENTERPRISE SUITE · STATE03 — Architecture · GROUP A — Sales + Inventory + Purchase
Execution Function: EXPERT IBPV · Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011`

This report consolidates Deliverables 01–12. It does not restate their detail; it cross-references material
findings and states this team's overall independent conclusion. **This is a verification conclusion, not a Boss
decision and not a Team C authorization.**

## 1. What Was Verified and How

- The CORR-010 package's integrity is independently reproduced: 37/37 SHA-256 hashes match exactly (D02),
  ancestry from the RV-009 final commit is a clean, 21-file, scope-clean corrective delta with zero leakage into
  TEAM A, prior IBPV, or other domains (D01, D02).
- The one governance-evidence discrepancy CORR-010's own preflight reported ("NOT FOUND" for commit `36820bf...`
  and its Five-Unit readiness file) is independently reproduced as a real symptom, then independently root-caused
  using only git ancestry commands: the object exists on canonical `SMEsPlus`, is not reachable from the GROUP A
  working lineage because that lineage forked from canonical 22 commits earlier and was never re-synced, and the
  correct classification is `GOVERNANCE EVIDENCE EXISTS — CROSS-BRANCH TRACEABILITY / LINEAGE VISIBILITY ISSUE`,
  not `EVIDENCE DOES NOT EXIST` (D03).
- Both race-condition closures Formal IBPV RV-009 left open (`FV006-EVT-004`, `FV006-EVT-005`) are independently
  re-derived as closed by explicit counterexample/oracle trace, not accepted from CORR-010's own claim (D04, D05).
- `FV006-EVT-001` is independently confirmed genuinely still open and honestly registered as `CONTROLLED
  CARRY-FORWARD`, not fabricated as resolved (D06).
- All eight RV-009 B-item precision defects are independently re-checked against the current primary-source text,
  not against CORR-010's own closure register, and all eight are confirmed correctly dispositioned (D07).
- The Approval/Multi-Approve interface boundary and the Accounting HOLD boundary are both independently confirmed
  held — no engine internals, no rule DSL, no legacy-internal-logic inference, no AR/AP fact invention (D08, D09).
- A fresh, independent cross-file regression sweep across all eleven CORR-010-touched files and their material
  dependents finds no new contradiction beyond the two citation defects CORR-010 already self-reported and fixed
  (D10).
- No TEAM B, TEAM A, or prior-IBPV artifact was edited by this session (confirmed via `git status` at time of
  writing — only new files under `FORMAL_REVERIFICATION_RV_011/`).

## 2. Domain-Wide Picture

CORR-010 is, on independent re-performance rather than mere re-reading, a genuine and substantively sound
targeted closure — not a paper closure. Both race-condition findings independently survive the specific
counterexample/oracle tests the governing prompt required (D04 §02, D05 §02); this is a materially stronger
verification than a re-read of CORR-010's own claimed closure text, since a counterexample that succeeded would
have overturned CORR-010's own conclusion. None did.

What this session's independent method adds beyond re-reading CORR-010's own claims is: (1) a genuine, traced
root-cause for the governance-lineage discrepancy, rather than accepting either "not found" or a bare "it exists
somewhere" — the exact fork point and the 22 intervening canonical-only commits are independently reconstructed
from git ancestry alone (D03); (2) direct re-verification of B4, B7, and B8 against primary text this session
read itself, not merely against CORR-010's own precision-cleanup register (D07); (3) an independent SHA-256
reproduction computed from the live working tree rather than transcribed from CORR-010's manifest (D02).

## 3. Consolidated Material Findings, Cross-Referenced

### 3.1 The Race-Condition Closures Hold Under Independent Counterexample Testing (D04, D05)

Unlike the B1–B8 precision defects (which are documentation/citation corrections layered on already-sound
structural decisions, per RV-009's own characterization), `FV006-EVT-004` and `FV006-EVT-005` were the two items
RV-009 escalated to a genuinely new, narrowly-scoped blocking category. This session's independent counterexample
trace (D04 §02: both processing orders converge on 15, not 10; D05 §02: the stated invariant cannot produce a
committed total exceeding On-Hand) is the correct evidentiary bar for closing a *design-level* concurrency/race
finding — a bar this session applied by deriving the result itself, not by verifying that CORR-010's stated
oracle matches CORR-010's own claimed outcome.

### 3.2 The Governance-Lineage Discrepancy Is Resolved With a Traced Mechanism, Not a Guess

D03's root-cause trace (§02: fork point `8f5fa522...`, 22 intervening canonical-only commits, `36820bf...`
landing on canonical alongside unrelated Domain-01 governance work) satisfies the governing prompt §4's
instruction to distinguish branch ancestry, local fetch state, worktree visibility, or another evidenced reason
where provable, and to record only the narrow fact where it is not. The narrow, provable fact — object exists,
branch lineage does not include it, structural reason identified — is exactly what is recorded; no further,
unprovable claim about the CORR-010 executor's specific local environment is asserted.

### 3.3 Interaction: The B-Item Corrections and the Race-Condition Closures Share No Contested Ground

Independently confirmed (D07, D10): none of the eight B-item citation/wording fixes alters or depends on the
substance of the CORR10-01/CORR10-02 closures, and neither race-condition closure depends on any B-item fix
being correct. The two categories are cleanly separable, consistent with how CORR-010 itself organized them
(files 30 vs. 32) — independent re-verification confirms this separation holds, not just that it is claimed.

### 3.4 The Accounting and Approval Boundaries Hold Across Two Independently-Scoped Checks

D08 (Approval, from the `13`/`07` text side) and D09 (Accounting, from the `15`/`07`§07 text side) independently
reach the same class of conclusion from opposite directions — a `git diff` confirming the underlying boundary
file is either untouched (`15`) or touched only by a citation-scoped edit (`13`, `07`) — and neither reviewer
found the boundary crossed.

## 4. What This Means, Read Together

No single finding in this report, taken alone, would justify a different conclusion than CORR-010's own claim.
What independent re-performance adds is that the two findings capable of overturning CORR-010's claim — the
race-condition closures, tested by counterexample, and the governance-evidence discrepancy, tested by direct
repository inspection rather than accepted narrative — both independently survive. The Boss/Accounting-dependent
items (A1, A2) and the PMO-actionable lineage items (C4, C5) remain exactly where they were, narrowly scoped, and
not silently dropped (Deliverable 11).

## 5. Status Vocabulary Compliance

Every deliverable in this session (01–12) used only the charter's allowed status vocabulary. No deliverable used
`FINAL APPROVED`, `BOSS APPROVED`, `PRODUCTION READY`, `RELEASE APPROVED`, or `TEAM C AUTHORIZED` for its own
conclusion.

## 6. Terminal Classification

**`FORMAL IBPV CORR-010 RE-VERIFICATION COMPLETE — NON-ACCOUNTING CLOSURE VERIFIED — PRE-DEVELOPMENT GATE STILL
HOLD FOR ACCOUNTING/CONTROLLED DEPENDENCIES — READY FOR BOSS NEXT-STEP DECISION`**

This classification is scoped, not blanket — see Deliverable 14 for the precise, itemized breakdown. It does not
authorize Team C. It does not constitute Boss approval. It does not constitute a Pre-Development Gate PASS. It is
this team's independent verification conclusion for Boss to act on.
