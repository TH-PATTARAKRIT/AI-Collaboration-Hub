# 02 — Business Process Verification Map

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D02`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`
Control Level: `/L999.999`
Boss: Sole Final Approver
Status Vocabulary Used: charter §8 terms only (`VERIFIED`, `VERIFIED WITH CONDITIONS`, `GAP FOUND`, `CONFLICT FOUND`, `EVIDENCE MISSING`, `REWORK REQUIRED`, `NOT READY FOR DEVELOPMENT`, `READY FOR BOSS DECISION`)

## 0 — Method and Inputs

This deliverable independently verifies end-to-end business process completeness for Sales (order-to-cash),
Purchase (procure-to-pay), and Inventory (movement/valuation touchpoints) as one integrated commercial–supply–
inventory backbone, per charter §5 item 1 and §6.

For each process this file answers, with evidence: who initiates it, what it produces/changes, and how it hands
off to the next domain — then cross-checks TEAM B's canonical design (files `05`–`10` of the frozen TEAM B
package) against TEAM A's approved capability models and 12-scenario E2E lifecycle map (`TEAM_A/02`–`TEAM_A/07`),
looking specifically for a step evidenced in TEAM A but missing/altered in TEAM B without explanation, or vice
versa.

TEAM B files cited: `05_INVENTORY_CORE_CANONICAL_DESIGN.md`, `06_SALES_CANONICAL_DESIGN.md`,
`07_PURCHASE_CANONICAL_DESIGN.md`, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`,
`09_CANONICAL_BUSINESS_EVENT_CATALOG.md`, `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md`, with supporting
reference to `03`, `04`, `11`, `12`, `13`, `15`.

TEAM A files cited: `TEAM_A/02_INVENTORY_CAPABILITY_MODEL.md`, `TEAM_A/03_SALES_CAPABILITY_MODEL.md`,
`TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md`, `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` (12 scenarios),
`TEAM_A/06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md`, `TEAM_A/07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md`,
plus `TEAM_A/19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md` for the two items TEAM A itself closed after its original
12-scenario map was published (Scenario 2's `_run_buy()` body; Scenario 7/8's Purchase cancellation cascade).

`AUDIT_REVIEW/06_GROUP_A_REMAINING_GAP_GATE_IMPACT_REGISTER.md` was consulted for cross-reference only, per
charter §10 — not treated as an answer key.

## 1 — Process 1: Order-to-Cash (Sales)

| Question | Answer | Evidence |
|---|---|---|
| Who initiates? | A Sales-side actor creating a Quotation (`Draft`); becomes a Commercial Commitment on confirmation | TEAM B `06_SALES_CANONICAL_DESIGN.md` §01; TEAM A `TEAM_A/05` Scenario 1 (`sale.order confirmed`) |
| What does it produce/change? | State → `Committed`; for physically-fulfilled lines, a fulfillment request (not a direct physical write); Ordered quantity fixed as a Commitment fact | TEAM B `06` §01–§02, `09` §01 ("Commercial Commitment Confirmed", "Commercial Fulfillment Requested") |
| How does it hand off to the next domain? | Event-driven, indirect: Inventory resolves the actual Movement Instruction via its own routing rules, independent of how Sales asked | TEAM B `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §01; `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §02 row 1 (classified `Hard`) |

Full chain independently traced: Commercial Commitment Confirmed → Commercial Fulfillment Requested (`09` §01) →
Movement Instruction Confirmed → Stock Reserved (partial claim a valid outcome) → Movement Executed → Sales'
Delivered quantity re-derives (`05` §01–§04, `09` §03) → Billable-Now Recomputed → Billing Event Fired → Financial
Handoff record created → Accounting posts → Sales re-derives Invoiced quantity on the round-trip (`06` §04, `08`
§08, `09` §01/§04, `15` §01–§02).

**Finding FV006-BPV-001**
- Verification Area: Order-to-cash process completeness (commercial commitment → physical fulfillment → billing
  handoff)
- TEAM B Artifact(s): `06_SALES_CANONICAL_DESIGN.md` §01–§04, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §01
  and §08, `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §01
- Approved Evidence/Baseline: `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` Scenario 1 and Scenario 12;
  `TEAM_A/07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` §01/§03/§05
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: Every step TEAM A evidenced for the commercial-commitment-to-billing chain (confirm → fulfillment
  request → reservation → execution → delivered-quantity re-derivation → billable-now → billing event → posted
  record → invoiced-quantity round-trip) is present in TEAM B's design, independently renamed but not altered in
  substance, and no step is silently dropped.
- Cross-domain impact: Sales ↔ Inventory ↔ Accounting-interface — the full chain is intact end to end.
- Gate impact: None — no blocking condition raised by this finding.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

**Finding FV006-BPV-002**
- Verification Area: Sales cancellation and reversal process completeness
- TEAM B Artifact(s): `06_SALES_CANONICAL_DESIGN.md` §05–§06, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §04
  and §05, `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §05–§08
- Approved Evidence/Baseline: `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` Scenarios 5, 7, 8
  ("Evidence status: VERIFIED FACT... single cleanest, most fully-closed scenario")
- Finding Status: `VERIFIED WITH CONDITIONS`
- Severity: Minor
- Why it matters: TEAM B correctly reproduces the evidenced facts that (a) Sales owns no Return/Reversal
  capability of its own — Inventory owns it exclusively — and (b) post-commitment cancellation cascades only to
  not-yet-executed fulfillment. The condition is that whether SMEsPlus should additionally offer a
  Sales-initiated RMA *affordance* (not a new Reversal mechanism) is explicitly and correctly left open by TEAM B
  as `HYPOTHESIS / REQUIRES REAL USER VALIDATION` (Boss Gate §4.3; TEAM B `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md`
  item 15). This is a properly disclosed open item, not a design defect, but it must not be silently resolved by
  Team C in either direction.
- Cross-domain impact: Sales ↔ Inventory. Building a Sales-initiated RMA screen without Boss/business
  confirmation would create a UI capability with no corresponding backend Reversal-initiation authority, which
  the canonical design (`05` §05) explicitly assigns to Inventory alone.
- Gate impact: Does not block the process-completeness verdict; the underlying open question is carried into the
  Pre-Development Gate as a named policy item.
- Required owner: Boss (business decision on whether to add a Sales-initiated RMA affordance)
- Blocks Development: No, provided Team C is explicitly instructed not to build a Sales-owned Return capability
  before this is decided
- Boss decision required: Yes

## 2 — Process 2: Procure-to-Pay (Purchase)

| Question | Answer | Evidence |
|---|---|---|
| Who initiates? | Three evidenced entry points, all preserved: (1) a buyer manually drafting a Supply Commitment; (2) an Internal Demand Request, approved then converted; (3) Inventory's Supply Need Signal (reorder-point-style), resolved by Purchase as a registered fulfiller | TEAM B `07_PURCHASE_CANONICAL_DESIGN.md` §01/§04; `08` §02; TEAM A `TEAM_A/05` Scenario 2 |
| What does it produce/change? | State → `Committed` or `Pending Approval` (amount-threshold gate); a receipt fulfillment request created directly/synchronously | TEAM B `07` §01/§03; `09` §02 |
| How does it hand off to the next domain? | Direct, synchronous: Purchase's demand converts directly into a Movement Instruction, unlike Sales' indirect path | TEAM B `07` §06; `08` §01 and §10 (explicit rationale for why this asymmetry is preserved, not normalized); `10` §02 row 2 (classified `Hard`) |

Full chain independently traced: Supply Commitment Confirmed → [`Pending Approval`, if amount-threshold gated] →
Committed → Movement Instruction created directly (receiving Location) → Movement Execution recorded → Stock
Position increments → Purchase's Received quantity re-derives → Billable-Now Recomputed → Billing Event Fired →
Financial Handoff → Accounting posts → Purchase re-derives Invoiced quantity (`07` §02–§03, `08` §01/§08, `09`
§02/§04, `15`).

**Finding FV006-BPV-003**
- Verification Area: Procure-to-pay process completeness across all three initiation paths
- TEAM B Artifact(s): `07_PURCHASE_CANONICAL_DESIGN.md` §01–§04, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`
  §01–§02, `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §02
- Approved Evidence/Baseline: `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` Scenarios 1 and 2;
  `TEAM_A/19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md` (closing the original `_run_buy()` `EVIDENCE_MISSING` item);
  `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` §05 (Purchase Request)
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: All three initiation paths TEAM A evidenced (manual RFQ, Internal Demand Request, and the
  reorder-point/Supply-Need trigger, including the per-product fork between a plain RFQ and a Purchase-Request
  route) converge correctly on the same Supply Commitment lifecycle in TEAM B's design, with no step invented or
  dropped. The originally-`EVIDENCE_MISSING` reorder-to-PO body (`_run_buy()`), later closed by TEAM A's own
  CORR-003 pass, is faithfully abstracted at the business-semantic level in TEAM B `08` §02 ("resolves the event
  into a new or reused draft Supply Commitment") — TEAM B did not need the implementation detail to correctly
  preserve the observed reuse-or-create business behavior.
- Cross-domain impact: Inventory → Purchase → Inventory (receipt) → Accounting-interface, fully connected.
- Gate impact: None.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

**Finding FV006-BPV-004**
- Verification Area: Purchase approval-gate placement within the procure-to-pay process
- TEAM B Artifact(s): `07_PURCHASE_CANONICAL_DESIGN.md` §01 and §03, `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`
  §02–§03 (APR-001, APR-002)
- Approved Evidence/Baseline: `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` §02 (PO-06/07/08, test-confirmed) and §03;
  `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` cross-scenario note ("the orphaned two-level approval schema... none
  of the 12 scenarios above required or found evidence of that mechanism actually gating any of these flows")
- Finding Status: `VERIFIED WITH CONDITIONS`
- Severity: Major
- Why it matters: TEAM B correctly distinguishes two genuinely separate control mechanisms — the amount-threshold
  gate (fully evidenced, placed correctly in the E2E lifecycle at confirmation) and the sequential level-based
  approval (real and historically used, but whose internal trigger logic is honestly carried forward as
  `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT` per Boss Gate §4.1, rather than invented). This is the
  correct verification posture — TEAM A itself found no evidence that the sequential mechanism gates order
  confirmation in any of the 12 canonical scenarios, and TEAM B does not claim otherwise. The condition is that
  this HOLD is the single highest-priority open item in the entire package (also flagged by TEAM B itself,
  `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 1) and directly affects financial/control integrity per
  charter §9.
- Cross-domain impact: Purchase and, by the shared Approval Control concept design (`13` §03), potentially Sales
  and the Internal Demand Request as well.
- Gate impact: This HOLD is charter §9's "unresolved accounting/compliance impact" / "unresolved security/
  permission/SoD design issue" category — a named Pre-Development blocking condition.
- Required owner: TEAM B / PMO (source-code acquisition for the three named modules is the stated resolution
  path, per `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §01 item 1); not a Boss business-policy decision
  by itself
- Blocks Development: Yes, specifically for any feature depending on the sequential level-based approval's exact
  transition/permission behavior; does not block Development of the amount-threshold gate, which is fully
  specified
- Boss decision required: Yes — Boss must decide whether to accept this as a scoped HOLD carried into Team C
  (with the internal logic resolved later) or to require closure before any Development proceeds

## 3 — Process 3: Inventory Movement and Valuation Touchpoints

| Question | Answer | Evidence |
|---|---|---|
| Who initiates? | Either commercial/supply domain (a fulfillment or receipt request), or Inventory itself (a chained replenishment instruction, or a Supply Need Signal it emits) | TEAM B `05_INVENTORY_CORE_CANONICAL_DESIGN.md` §01 and §07; `09` §03 |
| What does it produce/change? | Movement Instruction (Commitment fact, mutable) → Movement Execution (Physical fact, immutable once recorded) → Stock Position change | TEAM B `05` §01–§02; TEAM A `TEAM_A/02_INVENTORY_CAPABILITY_MODEL.md` |
| How does it hand off to the next domain? | Read-only compute back to Sales (Delivered) / Purchase (Received); the resulting quantity is an input to the next hard gate (billing) | TEAM B `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §02 row 3 |

**Finding FV006-BPV-005**
- Verification Area: Inventory movement lifecycle completeness (reservation, execution, backorder, reversal)
- TEAM B Artifact(s): `05_INVENTORY_CORE_CANONICAL_DESIGN.md` §01–§08, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`
  §03–§06, `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §01, §04, §08–§10
- Approved Evidence/Baseline: `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` Scenarios 3, 4, 5, 6, 9, 10;
  `TEAM_A/02_INVENTORY_CAPABILITY_MODEL.md`
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: The immutable-execution invariant, the planned/actual (Movement Instruction/Execution) split, the
  Fulfillment Continuation (backorder) self-link, and the Inventory-owned Reversal mechanism are all present, and
  TEAM B additionally *strengthens* two evidenced defects rather than merely preserving them: (1) per-instruction
  (not whole-batch) cancellation evaluation (`05` §08 item 3, `12` §07 — the reference system's all-or-nothing
  batch guard is explicitly corrected), and (2) an enforced, not merely eventually-consistent, uniqueness
  invariant on the Stock Position bin (`05` §02, `12` §11). Both corrections are explicitly labeled as TEAM B's
  own reasoned strengthening, not silently substituted for the evidenced behavior — satisfying the traceability
  requirement that every departure from evidence be explicitly labeled.
- Cross-domain impact: Inventory is correctly the sole owner throughout; Sales/Purchase participation is
  correctly limited to read-only derived-quantity consumption and traceability linkage.
- Gate impact: None.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

**Finding FV006-BPV-006**
- Verification Area: Inventory valuation — scope boundary correctness
- TEAM B Artifact(s): `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` §00 and §08
- Approved Evidence/Baseline: `TEAM_A/06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md` §05 (neither Sale nor Purchase
  performs GL posting; only the handoff points are confirmed); governing prompt §10/§19 (Accounting Core out of
  GROUP A scope)
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: "Valuation" (inventory-valuation-accounting internals) is correctly and explicitly excluded from
  this design package as Accounting Core's own domain (`15` §08), not silently omitted or invented. Movement
  (physical fact) is fully designed; valuation (financial fact derived from movement) is correctly deferred. This
  is the right verification outcome for a scope boundary, not a completeness gap — Team C must still be told,
  before implementation, that no inventory-valuation logic exists anywhere in this package and must be sourced
  from the Accounting Core domain design.
- Cross-domain impact: Inventory/Accounting boundary.
- Gate impact: None on this file's process-completeness verdict; flagged so Team C does not mistake the absence
  for an oversight.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

## 4 — Internal Coherence Check Across Files 05/06/07/08 (and 09/10)

Cross-read for contradiction between the four core process-design files plus the two files that index them:

- Quantity vocabulary (Ordered/Delivered-Received/Invoiced/Billable-Now) is used identically in `06`, `07`, `08`,
  and `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` — no competing term found for the same concept.
- The "Never-Assume-Equivalence" reminders stated in `08` §00 are restated verbatim, not contradicted, in `10` §03.
- The Handoff Points table in `10` §02 and the Cross-Cutting Dependency Table in `09` §05/§06 describe the same
  nine handoff relationships with consistent hard/advisory classification in both files — no divergence found.
- The asymmetry TEAM B deliberately preserves (Purchase's direct/synchronous receipt path vs. Sales' indirect/
  event-driven fulfillment path) is stated and justified in three places (`07` §06, `08` §01/§10, `10` §02) with
  the same rationale each time — not restated inconsistently.

**Finding FV006-BPV-007**
- Verification Area: Internal coherence of the process-design file set
- TEAM B Artifact(s): `06`, `07`, `08`, `09`, `10`, `11`
- Approved Evidence/Baseline: N/A (internal-consistency check, not an evidence-traceability check)
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: No contradictory restatement of the same business fact, state, or handoff was found across the
  six files most load-bearing for process completeness. This supports (but, per charter §12, does not by itself
  establish) internal design coherence — cross-domain boundary-level coherence is independently verified in
  Deliverable 03 of this package.
- Cross-domain impact: All three domains.
- Gate impact: None.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

## 5 — Summary

| Process | Verdict | Material open items |
|---|---|---|
| Order-to-Cash (Sales) | `VERIFIED`, one item `VERIFIED WITH CONDITIONS` | FV006-BPV-002 (Sales RMA affordance — Boss decision) |
| Procure-to-Pay (Purchase) | `VERIFIED`, one item `VERIFIED WITH CONDITIONS` | FV006-BPV-004 (sequential approval internal-logic HOLD — blocks that specific control) |
| Inventory movement/valuation touchpoints | `VERIFIED` | None material |
| Internal file-set coherence (05–10) | `VERIFIED` | None material |

No process step evidenced in TEAM A's approved capability models or 12-scenario E2E map was found missing or
silently altered in TEAM B's canonical design without an explicit, traceable rationale. Two items carry forward as
open — one a Boss business-policy decision (Sales RMA affordance), one a control-integrity HOLD requiring
source-code acquisition (sequential approval internal logic) — both already self-disclosed by TEAM B and
independently confirmed material by this review. This deliverable alone does not authorize Development; it feeds
the consolidated IBPV Independent Verification Report and Pre-Development Gate Recommendation elsewhere in this
package. This file does not constitute Boss approval, Development readiness, or Team C authorization.
