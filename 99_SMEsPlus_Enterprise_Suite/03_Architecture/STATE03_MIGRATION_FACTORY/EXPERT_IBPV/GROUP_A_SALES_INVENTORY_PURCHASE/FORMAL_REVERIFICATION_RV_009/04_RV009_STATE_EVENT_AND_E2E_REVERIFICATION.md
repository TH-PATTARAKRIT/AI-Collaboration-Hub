> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-009
> Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009` | Phase 5 lens — State / Event / E2E Re-Verification (Deliverable 04)
> Independent re-verification only. TEAM B's own closure register is treated as a claim to test, not as evidence.

# 04 — STATE TRANSITION, EVENT FLOW & E2E RE-VERIFICATION (RV9-01 — Denied-Approval Scope Only)

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009-D04`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009`
Re-Verification Target: TEAM B CORR-008 corrective package — `CORR8-01` state/event/E2E mechanics only
Baseline-correction commit: `e7eeba86d2693c5e15234d73f6722a9745038853`
Closure-package commit: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`
Control Level: `/L999.999`
Boss: Sole Final Approver
Charter: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/EXPERT_IBPV_CHARTER.md`
Status vocabulary used below: `VERIFIED`, `VERIFIED WITH CONDITIONS`, `GAP FOUND`, `CONFLICT FOUND`, `EVIDENCE MISSING`, `REWORK REQUIRED`, `NOT READY FOR DEVELOPMENT`, `READY FOR BOSS DECISION` — no other term is used.

## 00 — Scope Note

This deliverable independently re-verifies **only** the state-transition and event-catalog mechanics of `RV9-01` / `CORR8-01` (Denied-Approval Wind-Down Path) and the end-to-end sequencing consistency across the artifacts CORR-008 touched for it (`07` §01/§03, `08` §01/§05, `09` §02, `12` §07/§14, `18` §06).

Explicitly **out of scope for this deliverable**:

- The Approval-Control-coordination sub-claim of `RV9-01` (whether `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §03 coherently references the new `Rejected` state) — re-verified in **Deliverable 05, §03**, under the SoD/Approval lens where the primary artifact (`13`) lives. That result is summarized but not repeated in full here.
- Race-condition status — see the placeholder section at the end of this document.

## 01 — Original Findings Reproduced

**`FV006-STE-004`** (`FV_006/04_STATE_TRANSITION_VERIFICATION_MATRIX.md` §2.2/§3, `GAP FOUND`, Critical): the Supply Commitment's Canonical states enumerate `Pending Approval`, but no transition or terminal state is stated for a denied approval (`"Pending Approval | ? | Approval denied | *(not specified anywhere read)* | GAP"`).

**`FV006-EVT-003`** (`FV_006/05_EVENT_FLOW_VERIFICATION_MATRIX.md` §3, `GAP FOUND`, Critical): no event named "Supply Commitment Rejected" or equivalent exists in the pre-correction catalog, even though `12` §14 already establishes a generic rejection-event shape elsewhere. Named risk: "an orphaned Inventory fulfillment request with no instruction to stand down is a genuine audit/financial-integrity risk, not merely a UX gap," since Inventory's fulfillment request was already understood (pre-correction, ambiguously) to exist against the now-blocked commitment.

## 02 — Corrected Artifacts Independently Inspected

`07_PURCHASE_CANONICAL_DESIGN.md` §01 (full CORR-008 closure block) and §03; `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §01 (rewritten sequence) and §05 (cascade mechanism, referenced not re-edited); `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §02 (event rows); `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07 and §14; `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §06 (`N8`).

## 03 — Independent Verification: State Model

- **New state `Rejected`**: `07` §01 states it is reachable only from `Pending Approval`, and is deliberately distinct from `Cancelled` — `Rejected` carries "one authorized approver's decision, with a mandatory reason," while `Cancelled` is "withdrawal for any reason, by any authorized actor, at any stage." This is a real, substantive distinction (different actor constraints, different mandatory-reason requirement, different triggering context), not a cosmetic rename of an existing state. **Verified.**
- **Resubmission path**: `Rejected → Draft` is permitted under the pre-existing "`Draft` reachable from any prior state" rule; TEAM B's stated default (absent a Boss ruling) is explicit manual resubmission rather than silent auto-reset, correctly registered as `N8` in `18` §06 and correctly classified `CONTROLLED CARRY-FORWARD` (a policy nuance, not a structural gap — the state/event/audit/wind-down shape is complete regardless of which way this is decided). **Verified.**
- **Defect independently found**: `07` §01's own top-line summary — *"Canonical states: `Draft` → (`Sent`...) → [`Pending Approval`, conditional] → `Committed` → `Cancelled`, with `Draft` reachable from any prior state"* — was **not** updated to include `Rejected`, even though the CORR-008 closure block immediately below it introduces `Rejected` as "a new named state distinct from `Cancelled`." A reader consulting only this enumeration line (the natural place to look for the authoritative state list) would not learn `Rejected` exists. This is not a new class of defect: the original Formal IBPV FV-006 Deliverable 04 (`FV006-STE-003`) already caught this exact pattern once, in this exact section of this exact file — a correction stated in prose/cross-reference but not reflected in §01's own "Canonical states" summary line. The CORR8-01 correction was written into the same section carrying that pre-existing defect class and repeats it for the newly-added state.
  - Cite: `07_PURCHASE_CANONICAL_DESIGN.md` §01 (summary line) vs. the CORR-008 closure block in the same section.

## 04 — Independent Verification: Event Model

- **New event `Supply Commitment Rejected`** (`09` §02): precondition (`Pending Approval`, authorized actor denies), fact/state change (`State → Rejected`), and two named consumers — Inventory (stands down the fulfillment request via the standard cascade) and Purchase (permanent audit history: actor, reason, timestamp). This directly closes `FV006-EVT-003`'s core concern for Inventory. **Verified.**
- **Accounting consumer check**: `FV006-EVT-003`'s original text named Accounting as a second party potentially left without notification ("no catalogued event to notify Inventory... or Accounting"). The corrected `Supply Commitment Rejected` row does not list Accounting as a consumer. Independently checked against `13` §02's Accounting Interface Impact row ("None") and the general Financial Handoff model (`08` §08, `09` §01/§04): a commitment sitting in `Pending Approval` has not reached `Committed` and therefore has no Financial Handoff record yet to reverse or notify against — omitting Accounting as a consumer is **consistent**, not a silent gap. Not raised as a finding.
- **Audit trail**: `07` §01 states the rejection event's "actor, timestamp, and reason are permanently retained," consistent with `12` §14's pre-existing generic rejection-event shape (actor + reason + timestamp). **Verified.**
- **Owner**: Purchase, stated identically in `07` §01 and `09` §02. **Verified.**

## 05 — Independent Verification: Downstream Wind-Down (No Orphaned Demand)

`07` §01 states the already-created, not-yet-executed fulfillment request is stood down "using the **same** not-yet-executed-instruction cascade already defined for Cancellation (`08` §05, `12` §07) — no separate stand-down mechanism is invented." This was independently traced, not taken on faith:

- `08` §01's rewritten sequence: on `Rejected`, "instruction is stood down via the SAME not-yet-executed cascade used for Cancellation (§05 below) — no separate stand-down mechanism, no orphaned fulfillment request."
- `08` §05 (unedited, the cascade being reused): "cancellation cascades ONLY to not-yet-executed Movement Instructions/Reservations; already-executed work is spared" — a general mechanism that pre-dates CORR-008 and is genuinely reusable here (both `Cancelled` and `Rejected` share the precondition "not-yet-executed").
- `09` §02's `Supply Commitment Rejected` row consumer text matches word-for-word in substance: "Inventory (stands down the already-created, not-yet-executed fulfillment request via the standard not-yet-executed cascade, `08` §05)."

No new stand-down mechanism was invented anywhere in the reviewed set — the CORR-008 discipline of reuse-over-invention (Boss Gate §4.1 / governing prompt §11) is honored. **Verified — this closes the specific orphaned-fulfillment-request risk `FV006-EVT-003` named as a genuine audit/financial-integrity risk.**

## 06 — E2E Consistency Check: WHEN Is the Fulfillment Request Created?

The task's specific concern: does the rewritten `08` §01 sequence match the edited `09` §02 rows exactly, with no contradiction about timing?

| Artifact | Statement |
|---|---|
| `08` §01 | "Supply Commitment confirmed → emits a Movement Instruction directly/synchronously into the receiving Location, IMMEDIATELY, regardless of whether the commitment itself lands in Committed or Pending Approval" |
| `09` §02, `Supply Commitment Confirmed` row | "Inventory (receipt fulfillment request created directly/synchronously in **both** cases; held `Blocked` if the state lands in Pending Approval...)" |
| `07` §01 | "the Inventory-facing receipt fulfillment request is created directly/synchronously at Confirm time on **both** branches (`Committed` or `Pending Approval`), and held `Blocked`... for the `Pending Approval` branch specifically" |
| `07` §03 | Repeats the identical statement, explicitly noting it "removes a prior internal ambiguity between this file and `09` §02" |

All four independently-read statements agree on every material point: creation is synchronous, at Confirm time, on both branches, with `Blocked` (not absent, not `Cancelled`) as the intermediate status on the `Pending Approval` branch. **Verified — no remaining contradiction.** The pre-correction ambiguity `24` §2 self-reports (whether `08` §01 implied post-`Committed` creation while `09` §02 implied pre-existing-and-merely-unblocked creation) was independently re-derived from the corrected text itself, not accepted on `24`'s word alone — the resolution is real and consistently propagated to every artifact that states it.

## 07 — Residual Unknown (`N8`) — Independent Check

`18` §06, `N8`: "Whether `Rejected`... auto-transitions to `Draft` or requires an explicit manual resubmission action" — classified `CONTROLLED CARRY-FORWARD`, TEAM B recommends explicit manual resubmission, default deferred to Boss/business per `07` §01. **Verified as correctly classified**: the state/event/owner/audit/wind-down shape is structurally complete independent of how this specific policy question resolves, consistent with how every other similar policy default in this package (Over-Fulfillment Policy, Sales Confirmation Gate Policy) is carried forward rather than silently defaulted.

## 08 — Cross-Reference to Deliverable 05

The Approval-Control coordination sub-claim in `22`'s CORR8-01 entry ("coordinated with the Approval Control concept, `13` §03") was independently checked in Deliverable 05 §03 and found **not substantiated** — `13` was never edited as part of CORR8-01 (confirmed via `24` §3's own "Files Changed" table) and contains no reference anywhere to the new `Rejected` state or `Supply Commitment Rejected` event. That result is `GAP FOUND` (documentation-coherence only, non-blocking) and is tracked in full in Deliverable 05; it is not repeated here to avoid duplicate findings across deliverables.

## 09 — Verdict

**`VERIFIED WITH CONDITIONS`.**

- The substantive defect named by `FV006-STE-004`/`FV006-EVT-003` — an open vendor-facing commitment with no denial exit, and the resulting orphaned-fulfillment-request risk — is genuinely and completely closed: a real new state, a fully-specified new event with audit trail, and a reused (not invented) stand-down cascade, all stated with matching timing across every touched artifact (`07`, `08`, `09`, `12`).
- Condition: `07` §01's own "Canonical states:" summary line was not updated to list `Rejected`, repeating the exact defect class Formal IBPV FV-006 already caught once in this same section (`FV006-STE-003`). This should be corrected — add `Rejected` to the summary enumeration — before this finding is treated as fully, cleanly closed.
- Related but separately-tracked: see Deliverable 05 §03 for the `13` Approval-Control coordination gap (`GAP FOUND`, non-blocking).
- Gate impact: does **not** reopen Critical status — no orphaned-request risk remains, and no legacy approval-internal logic was invented to achieve this closure (`13` §00/§03's `HOLD` is unaffected, as `07` §01 itself correctly states). The enumeration-completeness condition is non-blocking but should be satisfied before unconditional closure of `CORR8-01`.

---

### Race-Condition Status — see Deliverable 06

Out of scope for this deliverable. `FV006-EVT-004` and `FV006-EVT-005` (the two named race-condition findings — Sales fulfillment-request vs. quantity-change ordering; the related Stock-Reservation race) and the `CORR8-06` event-transport-semantics closure (`09` §00A) that TEAM B claims addresses their contributing cause without resolving the findings themselves are re-verified separately by another reviewer under Formal Re-Verification RV-009 Deliverable 06. This document makes no claim, positive or negative, about race-condition status.
