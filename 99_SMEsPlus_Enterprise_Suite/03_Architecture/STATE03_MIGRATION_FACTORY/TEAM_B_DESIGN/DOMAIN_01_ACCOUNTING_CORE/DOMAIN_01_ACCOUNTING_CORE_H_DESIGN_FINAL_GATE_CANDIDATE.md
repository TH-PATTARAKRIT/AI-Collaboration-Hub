# DOMAIN_01 ACCOUNTING CORE — DESIGN FINAL GATE CANDIDATE

| Field | Value |
|---|---|
| Project | SMEsPlus ENTERPRISE SUITE |
| STATE | STATE03 — Architecture |
| STEP | TBD / BASELINE LINKAGE REQUIRED (unchanged — no approved weighting exists) |
| Board | Board06 — Data & Canonical Model |
| Domain | DOMAIN_01 — Accounting Core |
| Team | Team B — Independent Clean-Room Design |
| **Corrective round** | **CORR-B01/B02/B03, session SMEPLUS-26-08-29-MIG-B-D01-CORR-001** — ChatGPT Independent Design Audit (`aa60c2d0497cefe804d37953bbfaa597c3476d79`) returned this design for targeted revision with three BLOCKING findings. All three corrected; full record in [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md) and [B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md](B18_CORR_B_FOCUSED_RED_TEAM_REGRESSION.md). This document now reflects the corrected state. |

## Boss Authorization Baseline

Boss Gate: `512da309b0bbe597a1343ce386302d8f870d1fcf` ("record Boss approval for DOMAIN_01
Team A and authorize controlled Team B handoff"). Team B Handoff: `2314a786d9a1918f4cf4de3da7c2f8b85d3c98fe`
("authorize controlled DOMAIN_01 handoff to Team B"). Both independently verified against the
live authoritative repository (`TH-PATTARAKRIT/AI-Collaboration-Hub`, branch `SMEsPlus`) this
session, after an initial stale-read HOLD — full verification trail in
[B00](B00_GOVERNANCE_AND_HANDOFF_VERIFICATION.md).

## Team A Evidence Baseline

ChatGPT Final Team-A Audit `22f5a603c3431af985ff5c9c49f90366e32c1dbd` (REVIEW PASS — FORWARD
TO PMO VERIFICATION) → PMO Verification `3d42b10f9cc2a29c2b60dc0260d53f99260f22b4` (VERIFIED
WITH CARRY-FORWARD). Six critical findings, six business invariants, thirteen generic rules,
eight mathematical models, twenty residual unknowns — all read in full this session before
design work began.

## Team B Scope

DOMAIN_01 Accounting Core, conceptual/domain design only. No code, physical schema, ORM,
migration implementation, or API — per directive §12, not authorized this phase.

## Design Evidence Summary

Eighteen phases (B0–B17) complete, plus one targeted corrective round (CORR-B01/B02/B03).
Nine capabilities, nine domain-boundary concepts, a four-state lifecycle with an original
Consumption Gate mechanism (corrected: Period Lock and Consumption now independently gate
Amendment, not conflated), **eleven** invariants (BINV-11 added), fifteen business rules,
eleven conceptual entities (Current Earnings added), ten mathematical design principles
(including a corrected, fully-proved accounting-equation derivation and a corrected,
time-consistent aggregation formula), thirteen control objectives, thirteen migration
requirements, eighteen exception scenarios (six newly resolved), nine advancement items with
measurable criteria, **seven** formally compared design-option decisions (DT-07 added). Full
index: [F — Design Evidence Pack](DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md).

## Clean-room Status

**Critical Vendor-Derived Design Risk = 0**, verified twice (B14 direct check, B15 §8
independent cross-check from the traceability angle). Three vendor-adjacent comparison terms
individually reviewed and confirmed never adopted into the design itself.

## Traceability Status

Zero orphan critical design decisions. One ID-space collision and one rule-interaction gap
found and resolved explicitly during traceability review (B15 §3) — recorded, not hidden.
Zero circular definitions. Zero confirmed regulatory overreach.

## Unknown Status

Team A's full 20-item residual register carries forward unchanged and unresolved by this
design phase (correctly — Class G unknowns are never converted into requirements). Six new
Team B design assumptions were introduced by this phase's own decisions and are separately
tracked (next section) — these are a different category from Team A's carried-forward
unknowns and must not be conflated with them.

## Advancement Status

Nine advancement items, each with a stated reference-system limitation, an independent
business requirement, a chosen design mechanism, and a measurement criterion — not merely
aspirational objectives. Summary table: [F §23](DOMAIN_01_ACCOUNTING_CORE_F_TEAM_B_DESIGN_EVIDENCE_PACK.md#23-measured-advancement-criteria-summary--full-detail-in-b12).

## Critical Findings

**Three BLOCKING findings from ChatGPT's independent audit, all corrected this round:**
`D01-B-AUD-01` (Consumption/period-reopen contradiction — B04/B05/B08/B13 corrected),
`D01-B-AUD-02` (incomplete accounting-equation proof — B07/B08 corrected, full proof, verified
numerically), `D01-B-AUD-03` (time-inconsistent historical as-of after VOID — B04/B08
corrected, new BINV-11). One further precision gap found during the focused regression and
fixed (BINV-11/MP-09 scope precision — Amendment vs. Correction/Void distinguished). None
remain open. Full record: [CORR_B01_B02_B03_CORRECTIVE_ROUND.md](CORR_B01_B02_B03_CORRECTIVE_ROUND.md).
Separately, the original internal red-team pass (B16) found and fixed six further,
non-blocking design gaps before this pack was first assembled.

## Critical Assumptions

Six Team B design assumptions require Boss/gate confirmation, none silently treated as
settled: (1) rounding method = round-half-up; (2) **revised at CORR-B01** — period close and
Consumption are now two independent, orthogonal gates on Amendment (the original "automatic,
blanket consumption trigger" framing was internally contradictory and is withdrawn, not
carried forward); the narrower residual question is whether an authorized reopen should carry
any additional restriction beyond CO-08's authorization tier; (3) chart-of-accounts
template/instance structure (Option B, itself building on Team A's still-open GAP-D01-05);
(4) audit-trail tamper-evidence scope extended beyond the narrowly evidenced Thai legal
requirement; (5) correction shape left flexible (both full-reversal and delta permitted;
Void, B13 DT-07, is now understood as the zero-net instance of this same flexibility);
(6) the CO-02/CO-06 configuration-coupling rule found during B15 traceability review. Full
detail: [B15 §6](B15_DESIGN_TRACEABILITY_MATRIX.md#6-unresolved-critical-assumptions-register-consolidated).

## Residual Gaps

The design's weakest points, stated in [G — Self-Review](DOMAIN_01_ACCOUNTING_CORE_G_TEAM_B_SELF_REVIEW.md)
§3: six unconfirmed assumptions (above); AD-05's thin single-source evidentiary base; no
validation yet against real workflow/usage (out of scope for this phase, but a real limit on
what "measurably better" can currently mean).

## Carry-forward Items

Team A's STEP binding (TBD), 12 CLASS-D quarantine items, A4 mapping review items, progress-
weighting baseline (all TBD per Boss Gate §4/Handoff §6, unchanged by this domain pass);
Team A's OQ-01 (Thai statutory scope beyond e-Tax/tax-invoice) and OQ-02 (whether reference
implements IAS 21 remeasurement at all) — both confirmed in B15 §6 as not blocking this
domain's design regardless of how they resolve.

## TEAM B Working Progress

```
18 / 18 mandatory phases evidence-backed (B0–B17)
```
Reported strictly as **TEAM B DOMAIN WORKING PROGRESS** — not converted to Project/STATE/STEP
percentage, per directive §14 (no approved project weighting exists).

## Project % / STATE % / STEP %

```
Project % : TBD / BASELINE REQUIRED
STATE %   : TBD / BASELINE REQUIRED
STEP %    : TBD / BASELINE LINKAGE REQUIRED
```

## ChatGPT Audit Required

**YES.**

## PMO Verification Required

**YES.**

## Boss Final Decision Required

**YES** — including specific confirmation or revision of the six Critical Assumptions above.

## Gate Status

```
DESIGN FINAL GATE CANDIDATE — CORRECTIVE ROUND APPLIED
PENDING: verified push of the corrective-round commit
```

Superseded pre-correction status (kept visible, not deleted): "READY FOR CHATGPT INDEPENDENT
DESIGN AUDIT," true as of commits `6c18dd32b34ae6428757892048a756c1f575245a` /
`727b53008d58d3be5750a310707a195834e86c00` — that audit is exactly what returned the three
findings this round corrects. This line will be updated again, in place, once the
corrective-round commit is pushed and independently verified against `origin/SMEsPlus` (same
two-step discipline as the original push), at which point the status becomes **READY FOR
CHATGPT RE-AUDIT**, not a repeat of the same "independent design audit" label — this is
specifically a re-audit of corrected material.

## Open Assumptions — Explicitly Not Resolved by This Report

The six items below are **ASSUMPTION / OPEN FOR FINAL GATE**. Per explicit instruction this
session, they are not escalated as a question here and not resolved by this executor —
Boss confirms or revises them at the Final Gate, not before:

1. Rounding method = round-half-up (B08 MP-04, B13 DT-01)
2. **Revised at CORR-B01** — Period Lock and Consumption are two independent, orthogonal
   gates on Amendment (three consumption triggers, not four; period close no longer one of
   them). Residual open question, narrower than before: should an authorized reopen carry any
   restriction beyond CO-08's authorization tier (e.g., a time window after close)? (B04 §4, B13 DT-02)
3. Chart-of-accounts template/instance structure (B07 §2, B13 DT-03)
4. Audit-trail tamper-evidence scope beyond evidenced legal requirement (B09 CO-07, B13 DT-04)
5. Correction shape left flexible — both reversal-repost and delta permitted; Void (B13 DT-07)
   is the zero-net instance of this same flexibility (B08 MP-08, B13 DT-05)
6. CO-02/CO-06 configuration-coupling rule (B15 §3 Issue 2)
