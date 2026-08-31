> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV (Independent Verifier) | Formal Verification FV-006
> Session: SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006 | Phase 9 of 12 — Integration Failure / Retry / System Boundary Verification
> Independent of TEAM B. No target design authored here. Boss is sole Final Approver. Findings use the IBPV vocabulary only.

# 10 — INTEGRATION FAILURE / RETRY / RECOVERY VERIFICATION

## 00 — Method, Scope and Independence Note

This deliverable independently verifies TEAM B's design against five specific questions: (1) retry/duplicate-
submission idempotency, (2) downstream/cross-domain failure recovery, (3) cross-warehouse/cross-company effects
during exceptions, (4) migration/audit identity continuity under correction/reversal/retry, and (5) a testability
lens (advisory only) on quantity conservation, state/event outcomes, and duplicate/retry behavior.

Per the Clean-room Usage Rule (governing prompt §4.3), this review is confined to the TEAM B and TEAM A artifacts
listed in §01 below. Where a question depends on a TEAM B artifact outside that set (e.g. file 05 or file 19, which
were not provided to this verification pass), this report says so explicitly and records the point as `EVIDENCE
MISSING (scoped to this deliverable)` rather than inferring an answer or treating the absence as a TEAM B defect.
No Formal IDTM test execution was performed and none is implied by any finding below — §06 applies a testability
lens only, per governing prompt Cluster I, and classifies precision rather than answering the underlying question
itself. No git operations were performed; commit/branch identifiers below are restated from the governing session
prompt for context only and are not re-verified here (manifest/hash re-performance is Phase 1's subject, not this
deliverable's).

Context restated from the governing prompt (`01_NEW_SESSION_PROMPT_SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006.md`):
Session `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`; TEAM B frozen design commit `b98a3b9fb435845dbd15fae79db63b0b73a82420`;
IBPV working branch `ibpv/group-a-sip-formal-verification-006`.

## 01 — Sources Reviewed for This Deliverable

TEAM B (frozen design candidate):
- `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`
- `09_CANONICAL_BUSINESS_EVENT_CATALOG.md`
- `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md`
- `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md`
- `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`

TEAM A (approved evidence, read-only, no target design):
- `15_EXTERNAL_DEPENDENCY_AND_SYSTEM_RISK_OBSERVATION_REGISTER.md`
- `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md`

TEAM B files 01–07, 13–21 and TEAM A files other than 13/15 were **not** provided to this deliverable and are not
relied upon. Any cross-reference to them below is flagged as out-of-scope for this verification pass, not answered.

---

## 02 — Question 1: Retry / Duplicate-Submission Idempotency

**Question**: If a Sales Order, Purchase Order, or Inventory movement is submitted/processed twice (network retry,
double-click, message redelivery), does TEAM B's design define idempotency — a stable identity/reference that
prevents double-effect — or is this unaddressed?

**What the cited artifacts say**: `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §11 ("Duplicate / Retry
Behavior") is the only place in the cited TEAM B set that names this topic. It addresses exactly one concrete case
inherited from evidence: concurrent writers to the same logical Stock Position bin inserting a competing row
instead of updating one. TEAM B's decision there is a genuine strengthening — it `REJECT`s the reference system's
after-the-fact reconciliation pattern and requires Stock Position bin uniqueness to be an *enforced*, write-time
invariant (e.g. a concurrency-safe upsert or equivalent).

No equivalent statement exists anywhere in the cited files for the command/document layer: `08 §01`–`§05`
(confirm/commit lifecycle) and `09 §01`–`§03` (event preconditions) never include a de-duplication key, a
correlation/idempotency reference, or a stated rule for what happens if a Confirm action, a fulfillment-request
event, or a Movement Execution trigger is invoked twice for what is logically the same underlying user action or
network call. Specifically unanswered: does invoking Confirm a second time on an already-`Committed` Commercial or
Supply Commitment safely no-op, get rejected, or silently re-fire `Commercial Fulfillment Requested` /
`Supply Commitment Confirmed` and its downstream consequences (a second Movement Instruction, a second Reservation,
a second Financial Handoff write) a second time?

**Finding FV006-INT-001**
- Verification Area: Retry / duplicate-submission idempotency (Q1)
- TEAM B Artifact(s): `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §11; `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §01–§05; `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §01–§03
- Approved Evidence/Baseline: TEAM A `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` §02 item 3 (stock.quant row uniqueness not enforced in the reference system, reconciled after the fact by `_merge_quants()`)
- Finding Status: GAP FOUND
- Severity: Critical
- Why it matters: Double-click and network-retry are near-certain occurrences in any real web-based ERP usage pattern, not rare tail events. The only idempotency treatment in the cited design is scoped to one physical-layer concurrency case; the document/command layer — where a retried Confirm or a redelivered fulfillment-request message could double-create Movement Instructions, Reservations, or Financial Handoff writes — has no stated contract at all. This is exactly the category the governing prompt's blocking rule names: "unverified state/event transition affecting financial/control integrity."
- Cross-domain impact: A silently re-fired Confirm/fulfillment event would double-write across all three domains this design covers — a second instruction/reservation in Inventory and potentially a second Billable-Now write into the Financial Handoff.
- Gate impact: Blocks confident verification of charter scope item 7.1.7 ("Reject / Cancel / Partial / Retry / Reversal / Correction / Recovery paths") as it applies specifically to retry.
- Required owner: TEAM B (design clarification — this is a completeness question, not a business-policy choice).
- Blocking Development: Yes.
- Boss decision required: No — unlike the Invoiced-quantity or Over-Fulfillment-default items, this does not require a business policy choice, only a design statement TEAM B can supply independently.

---

## 03 — Question 2: Downstream / Cross-Domain Failure Recovery

**Question**: If Inventory fails to confirm a reservation after Sales has committed (or Purchase fails to record a
receipt after Inventory expects one), what does TEAM B's design say happens? Is recovery/compensation defined, or
silently assumed to never fail?

**What the cited artifacts say**: `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §02 classifies both
directions named in the question as "Hard" handoffs — "Commercial commitment → physical fulfillment request" and
"Supply commitment → physical receipt expectation." Both rows describe only the mechanism (event-driven/indirect
for Sales, direct/synchronous for Purchase) and the happy-path outcome. Neither row, nor any text in `08` or `09`,
states what happens if the second half of the handoff does not occur — e.g. Inventory cannot resolve a routing
rule and never creates the Movement Instruction, or the "direct, synchronous" receipt-expectation write fails
partway after the Supply Commitment has already moved to `Committed`.

`11 §01` notes that a negative `Forecasted` quantity is "a valid trigger condition for Supply Need, not an error
state," which covers the business-shortage case, but does not address a technical failure of the handoff write
itself. The closest explicit acknowledgment in the cited scope is `12 §13` ("Missing/Late Documents, Late Supply,
SLA Breach"), which TEAM B itself marks `NOT OBSERVED` / `UNKNOWN` — but that entry is framed around business
lateness (a shipment that is simply late), not around a technical failure of a hard handoff write. No compensating
step, timeout, alert, or reconciliation concept is named anywhere in the cited files for the latter case; it is not
even raised as an open item the way §13 raises lateness.

**Finding FV006-INT-002**
- Verification Area: Downstream/cross-domain failure recovery (Q2)
- TEAM B Artifact(s): `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §02; `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §00, §01; `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §01–§03; `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §13
- Approved Evidence/Baseline: TEAM B's own self-declared `UNKNOWN` at `12 §13` (adjacent but not identical scope — business lateness, not handoff-write failure)
- Finding Status: GAP FOUND
- Severity: Major
- Why it matters: Every "Hard" handoff in the design is documented only for its success path. Under this gap, a Commercial or Supply Commitment can sit `Committed` with no corresponding Inventory-side instruction (or vice versa) with no stated detection or repair path. This directly undercuts the design's own "Never-Assume-Equivalence" reminders (`08 §00`, restated at `10 §03`), which describe what the states mean when both sides of a handoff succeed but say nothing about what to do when one side doesn't.
- Cross-domain impact: Affects Sales↔Inventory and Purchase↔Inventory equally; any silent divergence here also feeds an incorrect input into the later Financial Handoff (Billable-Now is computed from Delivered/Received, which in turn depends on the handoff having actually completed).
- Gate impact: This is this deliverable's core subject (charter §7.1 item 10, "Integration boundaries and failure/recovery semantics") and is currently unresolved.
- Required owner: TEAM B, with an explicit statement of whether Commitment-confirm and Inventory-side instruction-creation are assumed atomic (a stated assumption is missing either way, not just a recovery path).
- Blocking Development: Yes.
- Boss decision required: No at this stage; if TEAM B's eventual answer accepts a period of eventual-consistency as a business risk, that acceptance should be made visible to Boss at the gate-recommendation stage.

---

## 04 — Question 3: Cross-Warehouse / Cross-Company Effects During Exceptions

**Question**: Cross-warehouse / cross-company effects during exceptions (partial receipt split across warehouses,
etc.) — is this addressed?

**What the cited artifacts say**: `08 §07` (Scenario 11) states that every fact in the design scopes primarily by
Company, with Warehouse as a "secondary, often-derived dimension," and separately confirms Company/Branch is
disjoint from the Thai Tax-Branch concept. `12 §12` adds that Sales and Purchase apply an identical
accessible-branch check on lines and that Stock Position scope is always derived from Location, never
independently set. Both of these are access-control/scoping rules, confirmed `ADOPT`ed unmodified.

Neither of these sections, nor the Fulfillment Continuation mechanism described at `08 §03` (the mechanism that
actually handles a partial delivery/receipt by splitting the unexecuted remainder onto a new, continuation-linked
Transfer Operation), states whether that continuation Transfer Operation may target a different
warehouse/Location than the original within the same Company, or what happens to the commercial/supply line's
re-derived Delivered/Received/Remaining quantities if it does. The design's stated non-coupling rule — the
commercial/supply side never reads the continuation link directly (`08 §03`) — suggests the answer "it shouldn't
matter to Sales/Purchase," but this is an inference drawn from a rule stated for a different purpose, not an
explicit design decision addressing the named scenario.

**Finding FV006-INT-003**
- Verification Area: Cross-warehouse effects during exceptions (Q3)
- TEAM B Artifact(s): `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §03, §07; `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §12
- Approved Evidence/Baseline: None cited for this specific split-across-warehouses scenario in either team's package; TEAM A's invariant register (`13`) carries no matching candidate.
- Finding Status: GAP FOUND
- Severity: Moderate
- Why it matters: The design states access-scoping and Location-derivation rules but does not explicitly confirm the fulfillment-mechanics question a partial-receipt-across-warehouses scenario actually raises: whether a Fulfillment Continuation may cross warehouses and, if so, whether that has any visible effect on the commercial/supply layer's quantities. An inferable answer exists from adjacent rules, but it is not a stated one.
- Cross-domain impact: Affects Inventory's Fulfillment Continuation mechanism and Sales/Purchase's quantity re-derivation in any operating pattern where one commitment line is fulfilled across more than one warehouse.
- Gate impact: Narrower than FV006-INT-001/002; still a named charter scope item (§7.1 item 9) left implicit for the exception case specifically rather than explicit.
- Required owner: TEAM B (a confirming statement, not a new mechanism).
- Blocking Development: No — the inferable answer from existing non-coupling rules is a reasonable basis to track this as a condition rather than a hard blocker.
- Boss decision required: No.

---

## 05 — Question 4: Migration / Audit Identity Continuity

**Question**: When a transaction is corrected, reversed, or retried, does the design preserve a stable identity so
audit history isn't broken?

**Reversal** — reasonably well specified. `08 §04` and `12 §10` describe a Reversal as creating a *new*, opposing
Movement Execution that links back to the specific original execution(s) reversed, never mutating or deleting the
original (consistent with the immutable-execution invariant at `12 §10`). `10 §02` classifies "Physical reversal →
traceability" as a read-only linkage available to Sales/Purchase. Taken together, this is coherent: audit
trace-back from a reversed transaction to its original is supported by a stated linkage mechanism, and the
original record is never overwritten.

**In-place correction** — less precise. `08 §06` and `12 §09` describe an in-progress execution's correction as
"undo and redo in place," stating that "an executed detail entry cannot be deleted." This implies immutability, but
does not state whether the "undo" and "redo" steps each produce their own new, separately-identified immutable
record (a full multi-row trail, consistent with how Reversal is specified) or whether "in place" means an existing
record's fields are mutated after the fact. Both readings are consistent with the text as written; an independent
reader cannot derive a single expected audit-trail shape from the cited wording.

**Retry** — not assessable from the cited files. Because no retry/idempotency contract exists at the command layer
(§02 above, FV006-INT-001), whether a retried Confirm or Movement Execution trigger reuses the original record's
identity or mints a second, competing one cannot be determined. This is not a separate root cause; it is the same
gap as FV006-INT-001 viewed from the audit-continuity angle.

**Migration-specific identity** (e.g. a legacy/external cross-reference preserved across a corrected or reversed
record) is not addressed in any of the five TEAM B files cited for this deliverable. If such a concept exists, it
would be expected in a different TEAM B artifact (e.g. the Evidence-to-Design Traceability Matrix, file 19) that
was not provided to this verification pass.

**Finding FV006-INT-004**
- Verification Area: Migration/audit identity continuity (Q4)
- TEAM B Artifact(s): `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §04, §06; `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §09, §10; `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §02
- Approved Evidence/Baseline: n/a (design-precision question, not an evidence-traceability question)
- Finding Status: VERIFIED WITH CONDITIONS (Reversal) / GAP FOUND (in-place correction wording) / EVIDENCE MISSING, scoped to this deliverable (migration-specific cross-reference identity; retry-linked identity is carried by FV006-INT-001 rather than re-scored here)
- Severity: Moderate
- Why it matters: Reversal's identity/linkage model is sound as stated. The correction-mechanic wording is ambiguous between two materially different audit outcomes (multi-row trail vs. in-place mutation), which matters directly for anyone who must later prove what physically happened to a corrected transaction. The migration-cross-reference question cannot be answered from the files in scope here and should not be assumed either present or absent based on this deliverable alone.
- Cross-domain impact: Affects Accounting's backward re-derivation (which depends on Sales/Purchase quantities that are themselves derived from Movement Execution history) and any future migration/reconciliation tooling that must correlate corrected or reversed records back to an originating transaction.
- Gate impact: Moderate for the correction-wording point; the retry-linked portion inherits FV006-INT-001's severity and blocking status by reference rather than adding a second blocking item.
- Required owner: TEAM B (clarify correction-mechanic wording); a later verification pass with file 19 in scope should close the migration-cross-reference question.
- Blocking Development: No, independently — the ambiguity is a clarity gap, not a confirmed defect; it inherits blocking status only through its link to FV006-INT-001.
- Boss decision required: No.

---

## 06 — Question 5: Testability Lens (Advisory Only — No Test Execution Performed)

Per governing prompt Cluster I, the following classifies whether each named area is precise enough that an
independent tester could later write an observable pass/fail test. This section does not answer the underlying
business question and does not run any test.

### 06.1 Quantity Conservation

`11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` §01–§03 gives closed-form, stored-vs-derived definitions
(`Available = On-Hand − Reserved`; `Forecasted = On-Hand + Incoming − Outgoing`; `Remaining-to-Deliver = Ordered −
Delivered`; `Remaining-to-Receive = Ordered − Received`) precise enough for a tester to define a pass/fail oracle
today — e.g. after a series of partial Movement Executions, assert `Delivered` equals the sum of executed
quantities and `Remaining-to-Deliver` recomputes accordingly. This portion is adequately precise for future
testing. `Invoiced` quantity, by contrast, is explicitly left open at `11 §04` (posted-only vs. any-non-cancelled,
with a stated TEAM B recommendation but no binding default) and `12 §02`/`§03` (Over-Fulfillment/Over-Billing
policy defaults not fixed). No single pass/fail oracle for "Invoiced/billing-layer quantities reconcile correctly"
can be written until those policy defaults are set. TEAM B has already surfaced both as open Boss/business items;
this is recorded here only because it directly blocks writing a quantity-conservation test for the billing layer
today, not as a new discovery.

**Finding FV006-INT-005** — Status: VERIFIED (physical and commitment layers) with a linked GAP (billing-layer
oracle blocked pending an already-flagged Boss policy decision). Severity: Minor for the verified portion; the
billing-layer blockage tracks the severity/status of TEAM B's own already-open Invoiced-quantity and
Over-Fulfillment/Over-Billing items rather than introducing a new one. Not independently blocking Development.
Boss decision required: Yes, but this restates an item TEAM B already raised, not a new requirement.

### 06.2 State/Event Outcomes

`09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §01–§03 gives, for most rows, a concrete precondition and a concrete
state change (e.g. "Commercial Commitment Confirmed": precondition = Draft/Sent + product presence on every real
line; outcome = State → Committed), sufficient for a tester to write a pass/fail case directly from the table. One
row is not self-contained as cited: "Movement Instruction Confirmed" states the outcome as "Draft → Waiting/
Confirmed" without stating, within file 09, the condition that selects `Waiting` versus `Confirmed`. That branch
condition may be defined in `05_INVENTORY_CORE_CANONICAL_DESIGN.md`, which was not provided to this verification
pass.

**Finding FV006-INT-006** — Status: VERIFIED WITH CONDITIONS. Severity: Minor. The missing branch condition is
recorded as `EVIDENCE MISSING (scoped to this deliverable)`, not as a TEAM B design gap, since it is plausibly
resolved in an artifact outside this review's cited set. Not blocking. A subsequent verification pass that
includes file 05 should confirm whether the condition is in fact stated there.

### 06.3 Duplicate/Retry Behavior

As established in §02, the Stock Position bin uniqueness rule (`12 §11`) is precise enough to test today (a
concurrency test asserting a single, consistent row/upsert result). No equivalent statement exists for a repeated
Confirm or Movement-Execution-trigger call, so no pass/fail oracle can be written for that broader retry scenario.

**Finding FV006-INT-007** — Status: GAP FOUND. This restates FV006-INT-001 from the testability angle rather than
adding an independent defect; its severity (Critical) and blocking status are inherited from FV006-INT-001, not
separately scored in the consolidated count below.

---

## 07 — Consolidated Finding Register (This Deliverable)

| Finding ID | Question | Status | Severity | Blocking Development | Boss Decision Required |
|---|---|---|---|---|---|
| FV006-INT-001 | Q1 — Command-layer retry/idempotency | GAP FOUND | Critical | Yes | No |
| FV006-INT-002 | Q2 — Downstream handoff failure/compensation | GAP FOUND | Major | Yes | No (visibility recommended if eventual-consistency is later accepted) |
| FV006-INT-003 | Q3 — Cross-warehouse split during exceptions | GAP FOUND | Moderate | No | No |
| FV006-INT-004 | Q4 — Audit identity continuity (correction wording; migration cross-reference) | VERIFIED WITH CONDITIONS / GAP FOUND / EVIDENCE MISSING (see §05) | Moderate | No (independently) | No |
| FV006-INT-005 | Q5a — Quantity-conservation testability | VERIFIED / linked GAP (billing layer) | Minor | No (tracks existing item) | Yes (restates existing item) |
| FV006-INT-006 | Q5b — State/event testability | VERIFIED WITH CONDITIONS | Minor | No | No |
| FV006-INT-007 | Q5c — Retry testability | GAP FOUND (restates FV006-INT-001) | Critical (inherited) | Yes (inherited) | No |

Independently-blocking findings introduced by this deliverable: **FV006-INT-001, FV006-INT-002** (FV006-INT-007 is
the same defect as FV006-INT-001 viewed through the testability lens and is not an additional blocker).

## 08 — Positive / Verified Observations (Not Findings, Recorded for Balance)

- The immutable-execution invariant (`12 §10`, `08 §06`: no "un-execute" action exists; correction after full
  execution is possible only via Reversal) is clearly stated and directly testable as written.
- The cancellation-cascade correction at `12 §07` — moving from an evidenced all-or-nothing batch guard to a
  required per-instruction evaluation — is a precisely stated strengthening with an explicit before/after
  description, and traces cleanly to TEAM A's corrective invariant-register update
  (`TEAM_A/13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md`, "CORRECTIVE UPDATE" section, item 1). This is a
  well-evidenced, independently traceable design decision.
- The Reservation-release rule on cancellation of a not-yet-executed instruction (`08 §05`) is stated plainly and
  is testable as written.

## 09 — Section-Level Note on Gate Impact

This deliverable identifies two independently-blocking gaps (FV006-INT-001, FV006-INT-002) under the governing
prompt's Pre-Development Blocking Rule (§12 of the governing prompt): both concern "unverified state/event
transition affecting financial/control integrity" and both remain open. This section does not itself issue the
Formal IBPV terminal recommendation — that consolidation is Phase 12's subject
(`14_IBPV_INDEPENDENT_VERIFICATION_REPORT.md` and `15_PRE_DEVELOPMENT_GATE_RECOMMENDATION_TO_BOSS.md`) — but this
deliverable's own findings, taken alone, would not support closing the "Integration boundaries and failure/recovery
semantics" scope item (charter §7.1 item 10) without further TEAM B clarification on FV006-INT-001 and
FV006-INT-002.
