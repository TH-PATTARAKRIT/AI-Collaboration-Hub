> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV (Independent Verification)
> Formal Verification FV-006 | Phase 4 — State / Event Verification | Deliverable 04 of 16
> Session: SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006 | TEAM B Frozen Commit: b98a3b9fb435845dbd15fae79db63b0b73a82420

# 04 — STATE TRANSITION VERIFICATION MATRIX

## 0. Purpose, Method, and Boundary

This matrix independently verifies the state-transition semantics of TEAM B's canonical GROUP A design. It does
**not** redesign any object, state, or transition. Every row either (a) confirms a TEAM B statement is internally
consistent and traceable to TEAM A's approved evidence, or (b) records a Finding using the IBPV Finding Model and
the Charter's allowed status vocabulary (VERIFIED / VERIFIED WITH CONDITIONS / GAP FOUND / CONFLICT FOUND /
EVIDENCE MISSING / REWORK REQUIRED / NOT READY FOR DEVELOPMENT / READY FOR BOSS DECISION).

Object names below are TEAM B's own terminology (`08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`,
`05_INVENTORY_CORE_CANONICAL_DESIGN.md`, `06_SALES_CANONICAL_DESIGN.md`, `07_PURCHASE_CANONICAL_DESIGN.md`); no
new object or state name is introduced by this verification.

Primary TEAM B sources: `06_SALES_CANONICAL_DESIGN.md`, `07_PURCHASE_CANONICAL_DESIGN.md`,
`05_INVENTORY_CORE_CANONICAL_DESIGN.md`, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`,
`09_CANONICAL_BUSINESS_EVENT_CATALOG.md`, `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md`,
`12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`.

Primary TEAM A baseline: `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` (12 canonical scenarios, including the
2026-08-31 Corrective Update), `TEAM_A/06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md`,
`TEAM_A/09_QUANTITY_SEMANTICS_REGISTER.md`.

## 1. Object Inventory

| # | TEAM B Object | Also known as (TEAM A term) | Governing TEAM B Section(s) |
|---|---|---|---|
| 1 | Commercial Commitment | Sales Order (`sale.order`) | `06` §01–§07, `08` §00–§05 |
| 2 | Supply Commitment | Purchase Order (`purchase.order`) | `07` §01–§07, `08` §00–§05 |
| 3 | Internal Demand Request | Purchase Request (`purchase.request`) | `07` §04 |
| 4 | Movement Instruction | Planned `stock.move` | `05` §01, §07; `09` §03 |
| 5 | Transfer Operation | `stock.picking` | `05` §05 |
| 6 | Reservation | `stock.quant.reserved_quantity` claim | `05` §04 |
| 7 | Movement Execution | Done `stock.move.line` | `05` §01 |
| 8 | Reversal | Return (`stock.return.picking`) | `05` §05 |

## 2. Per-Object State Verification

### 2.1 Commercial Commitment (Sales Order)

**States (per `06` §01):** `Draft` → (`Sent`, optional/non-behavioral) → `Committed` → `Cancelled`; `Draft`
reachable again only from `Cancelled` (itself reached from `Committed`) or from `Sent`. `Locked` is an
**independent boolean**, not a lifecycle state.

| From | To | Trigger (event/rule) | Source | Consistency vs. `09`/`11`/`12` |
|---|---|---|---|---|
| Draft | Sent | Manual, non-behavioral | `06` §01 | Consistent — `09` catalog does not list "Sent" as a triggering event, correctly reflecting that it has no downstream consumer |
| Draft/Sent | Committed | Confirmation gate passes (product presence on every real line; credit/availability gate per configurable policy) | `06` §01; `09` §01 "Commercial Commitment Confirmed" | Consistent with `09` §01 row 1 |
| Committed | Cancelled | `Commercial Commitment Cancelled` event, not fully executed elsewhere | `06` §05; `09` §01 row 5; `12` §07 | Consistent — cascade scoped to not-yet-executed fulfillment only |
| Draft/Sent | Cancelled | Unrestricted except by Lock | `12` §06 | Consistent |
| Cancelled / Sent | Draft | Manual reset | `06` §01 | Consistent with the *restricted* return-to-draft rule TEAM B requires uniformly (`08` §05); re-confirmation always creates **new** physical demand, never revives cancelled instructions (`06` §05) |
| (any) | Locked = true/false | Manual or auto-policy, independent of lifecycle state | `06` §01; `09` §01 row 4 | See Finding **FV006-STE-007** on duplicate-trigger idempotency |

**Verified:** the Draft/Sent/Committed/Cancelled chain, the Locked-as-orthogonal-boolean design, and the
restricted re-confirmation-creates-new-demand rule are all internally consistent and traceable to TEAM A evidence
(`TEAM_A/05` Scenario 7: Sale's cycle "VERIFIED FACT... test-confirmed", `TEAM_A/09` §01 rows Quoted/Ordered).

**Findings:** see **FV006-STE-002** (no approval sub-state despite a confirmed real approval mechanism).

### 2.2 Supply Commitment (Purchase Order)

**States (per `07` §01):** `Draft` → (`Sent`, non-behavioral) → [`Pending Approval`, conditional] → `Committed` →
`Cancelled`.

| From | To | Trigger (event/rule) | Source | Consistency vs. `09`/`11`/`12` |
|---|---|---|---|---|
| Draft/Sent | Committed | Confirmed, below amount-threshold or approval-manager role | `07` §01, §03; `09` §02 "Supply Commitment Confirmed" | Consistent |
| Draft/Sent | Pending Approval | Confirmed, above threshold or role absent | `07` §01, §03; `09` §02 row 1 | Consistent |
| Pending Approval | Committed | `Supply Commitment Approved`, authorized actor | `09` §02 row 2 | Consistent |
| Pending Approval | **?** | Approval denied | *(not specified anywhere read)* | **GAP — see FV006-STE-004** |
| Committed | Cancelled | Not locked AND no open vendor bill; not-yet-received portion cancels, received portion spared | `07` §07; `12` §07 | Consistent — TEAM B `ADAPT`s the dual gate as a legitimate, non-symmetric business condition |
| Cancelled | Draft | Manual reset | `07` §07 (as corrected) | See **FV006-STE-003** — the correction is stated in §07/`08` §05 but not reflected in §01's own "Canonical states" line |

**Verified:** the amount-threshold approval gate, the `Pending Approval` phase itself, and the cancellation
cascade (state-partitioned by receipt scenario, per-instruction rather than all-or-nothing) are all consistent
with `12` §02, §07 and with `TEAM_A/05`'s Corrective Update (Scenario 7/8 "now CLOSED... proven structurally
airtight").

**Findings:** **FV006-STE-003**, **FV006-STE-004**.

### 2.3 Internal Demand Request

**States (per `07` §04):** `Draft` → `Pending Approval` → `Approved` / `Rejected`.

| From | To | Trigger | Source | Consistency |
|---|---|---|---|---|
| Draft | Pending Approval | Submission | `07` §04 | Consistent |
| Pending Approval | Approved | Approver action | `07` §04; `09` §02 "Internal Demand Request Approved" | Consistent |
| Pending Approval | Rejected | Approver action | `07` §04 | No corresponding catalogued event in `09` — see **FV006-STE-005** |
| Rejected | **?** | *(none documented)* | — | **GAP — FV006-STE-005** |
| Approved | (converted) | `Internal Demand Converted`, hard-gated on Approved | `07` §04; `09` §02 | The resulting state is described only as "a read-model mirror," not a named value — see **FV006-STE-006** |

**Findings:** **FV006-STE-005**, **FV006-STE-006**.

### 2.4 Movement Instruction / Transfer Operation (Inventory Physical Layer)

TEAM B does **not** publish an explicit "Canonical states:" enumeration for this object family, unlike Commercial
and Supply Commitment. States must be reconstructed from narrative and event text:

| Implied state | Evidence it exists | Source |
|---|---|---|
| Draft | "Mutable until execution begins" | `05` §01 |
| Waiting/Confirmed | `Movement Instruction Confirmed` event | `09` §03 row 1 |
| Partially Reserved / Fully Reserved | "Partial reservation... is a valid outcome, not an error" | `05` §04 |
| Partially Executed / Fully Executed | `Movement Executed` event, "(fully or partially) actioned" | `09` §03 row 3 |
| Cancelled (not-yet-executed remainder only) | "cancellation cascades ONLY to not-yet-executed Movement Instructions" | `08` §05 |
| Closed / superseded by continuation | `Fulfillment Continuation Created` | `05` §05; `09` §03 row 4 |

A **Transfer Operation**'s own state is stated to be "entirely derived from constituent instruction states; it
carries no independent state machine" (`05` §05) — but because the constituent instruction states are themselves
never exhaustively enumerated, this derivation cannot be independently confirmed as complete. **See FV006-STE-001.**

**Verified:** the planned/actual (Instruction/Execution) split, the immutability of a recorded Movement Execution,
the "undo-and-redo-in-place" correction mechanic scoped to not-yet-fully-executed detail, and the hard "no
un-execute" invariant are all internally consistent (`05` §01, §05; `08` §06; `12` §09, §10) and match
`TEAM_A/05` Scenarios 9/10 ("VERIFIED FACT... as a negative claim").

### 2.5 Reservation

Not a named lifecycle state machine in its own right — a claim fact layered on the Movement Instruction's
reservation sub-state (`05` §04). Verified consistent: partial claim is a valid, distinctly-tracked outcome;
release-on-cancellation is unconditional for not-yet-executed instructions (`08` §05; `12` §08); Reservation is
never exposed to Sales/Purchase as a raw total, only via the derived Available/Forecasted views (`05` §04; `09`
§05, §06). Cross-domain concurrency behavior of the claim step itself is addressed in Deliverable 05
(**FV006-EVT-005**), not repeated here as a state-machine defect.

### 2.6 Movement Execution and Reversal

Movement Execution is a fact record, not a state machine: once written it is immutable (`05` §01), correctable
only by a Reversal (`05` §05; `12` §10). A Reversal is itself created only against a fully-executed Transfer
Operation, is Inventory-owned "regardless of commercial origin" (`05` §05), and is structurally the same
mechanism whether customer- or vendor-directed (`08` §04). **Verified** — this is the most exhaustively evidenced
finding in the whole TEAM A package (`TEAM_A/05` Scenarios 5/6: "the strongest, most fully-closed findings in this
entire phase") and TEAM B's design preserves it without alteration.

## 3. Cross-Cutting Exception-Path Verification (Charter §6 required questions)

| Exception scenario | Object(s) | TEAM B answer | Source | Verification result |
|---|---|---|---|---|
| Reject (approval denial) | Supply Commitment | Not specified | — | **GAP — FV006-STE-004** |
| Reject (approval denial) | Internal Demand Request | `Rejected` state exists; no successor transition given | `07` §04 | **GAP — FV006-STE-005** |
| Cancel before confirmation | Both Commitments | Unrestricted except by Lock | `12` §06 | VERIFIED |
| Cancel after confirmation, before any partial execution | Both Commitments | Full cancel of not-yet-executed fulfillment | `12` §07 | VERIFIED |
| Cancel after partial execution | Both Commitments | Executed portion isolated/spared; per-instruction evaluation (corrects an evidenced all-or-nothing defect) | `12` §07; `05` §08 item 3 | VERIFIED — traced to `TEAM_A/05` Corrective Update |
| Cancel after full execution | Both Commitments | Nothing physical touched; only Reversal available | `07` §07; `08` §05 | VERIFIED |
| Retry / duplicate — physical write | Stock Position bin | Enforced uniqueness / concurrency-safe upsert required (`REJECT`s after-the-fact reconciliation) | `12` §11 | VERIFIED (deliberate strengthening over an evidenced defect) |
| Retry / duplicate — commitment confirmation | Commercial/Supply Commitment | Not specified | — | **GAP — FV006-STE-007** |
| Return/Reversal-after-execution | Transfer Operation | Reversal only; Inventory-owned | `05` §05; `12` §05 | VERIFIED |
| Correction during open execution | Movement Instruction | Undo-and-redo-in-place, invisible to Sales/Purchase | `08` §06; `12` §09 | VERIFIED |
| Correction after full execution | Transfer Operation | No "un-execute"; Reversal only (hard invariant) | `08` §06; `12` §10 | VERIFIED |

## 4. TEAM A E2E Completeness Cross-Check

Verified against `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` Scenarios 1–12: no TEAM A-evidenced state or
transition is silently dropped or merged by TEAM B in a way that changes audit or financial meaning.

| TEAM A Scenario | TEAM B Coverage | Result |
|---|---|---|
| 1 — Buy→Receive→Stock→Sell→Reserve→Deliver | `08` §01 | VERIFIED — full chain preserved, including the deliberate asymmetry between Purchase's direct/synchronous and Sales' indirect/event-driven demand-to-instruction path (`08` §10) |
| 2 — Shortage→Supply Need→Purchase→Receipt | `08` §02 | VERIFIED — both the reordering-rule and Internal-Demand-Request forks preserved as distinct, per-product-configurable paths |
| 3/4 — Partial fulfillment | `08` §03; `12` §01 | VERIFIED — header-durable/line-live pattern preserved unmodified |
| 5/6 — Return/Reversal | `08` §04; `12` §05 | VERIFIED — Inventory-exclusive ownership preserved without modification |
| 7/8 — Cancellation before/after confirmation/reservation | `08` §05; `12` §06–§08 | VERIFIED — including the Purchase-side cascade TEAM A's Corrective Update closed as "structurally airtight" |
| 9/10 — Correction during/after movement | `08` §06; `12` §09–§10 | VERIFIED |
| 11 — Multi-warehouse/company | `08` §07 | VERIFIED |
| 12 — Financial handoff | `08` §08 | VERIFIED at the interface-boundary level (full posting mechanics correctly out of scope) |

No scenario state was found merged or dropped. The gaps recorded in Section 5 below are **omissions/ambiguities
within TEAM B's own state model**, not deviations from TEAM A's evidenced baseline — TEAM A's map does not
evidence the Supply Commitment's approval-rejection path either (its own approval-workflow observations are
explicitly carried as an unresolved Carry-Forward Unknown), so those specific findings are independently
identified by this verification, not inherited from TEAM A.

## 5. Findings Register

| Finding ID | Verification Area | TEAM B Artifact(s) | Evidence/Baseline Ref. | Status | Severity | Blocking Dev? | Boss Decision? | Owner |
|---|---|---|---|---|---|---|---|---|
| FV006-STE-001 | Movement Instruction / Transfer Operation state completeness | `05` §01, §05; `08`; `09` §03 | `TEAM_A/05` Scenario 1 (method-level evidence only, no explicit state enum either) | GAP FOUND | Major | Yes | No | TEAM B |
| FV006-STE-002 | Commercial Commitment approval sub-state | `06` §01 vs. §07 | `TEAM_A/05` cross-scenario notes ("orphaned...schema... none of the 12 scenarios found evidence of that mechanism gating any of these flows") | GAP FOUND | Major | Yes | No | TEAM B |
| FV006-STE-003 | Supply Commitment return-to-draft rule — internal document inconsistency | `07` §01 vs. §07; `08` §05 | `TEAM_A/05` Scenario 7 (PO-09 asymmetry) | CONFLICT FOUND | Moderate | No | No | TEAM B |
| FV006-STE-004 | Supply Commitment approval-rejection has no destination state | `07` §01, §03; `12` §14 | Not evidenced either way in `TEAM_A` files reviewed — approval internal logic is a confirmed Carry-Forward Unknown | GAP FOUND | Critical | Yes | Yes | TEAM B |
| FV006-STE-005 | Internal Demand Request `Rejected` has no successor transition | `07` §04 | EVIDENCE MISSING in TEAM A files reviewed (not contradicted, simply silent) | GAP FOUND | Major | No | No | TEAM B |
| FV006-STE-006 | Internal Demand Request post-conversion state value undefined | `09` §02 "Internal Demand Converted"; `07` §04 | — | GAP FOUND | Moderate | No | No | TEAM B |
| FV006-STE-007 | No idempotency rule for duplicate commitment-confirmation | `12` §11 (scoped to Stock Position bin only) | — | GAP FOUND | Moderate | No | No | TEAM B |

**Why FV006-STE-004 matters most:** it is the only Critical finding in this matrix, it is **not** one of TEAM B's
three self-declared Boss/business policy items (Invoiced Quantity definition, Over-Fulfillment/Over-Billing
default, Sales Confirmation Gate default — `06` §01/§02, `11` §04, `12` §02/§03), and it sits directly on the
Charter's Pre-Development Blocking Rule category "unverified state/event transition that affects
financial/control integrity." A Supply Commitment stalled in `Pending Approval` with no defined exit-on-rejection
path is an open vendor-facing commitment with no closure mechanism. See the paired event-catalog finding
**FV006-EVT-003** in Deliverable 05.

**Cross-domain impact summary:** FV006-STE-001 and FV006-STE-004 both propagate into Inventory (an
under-specified or orphaned fulfillment request); FV006-STE-002 propagates into the Approval/SoD verification
(Deliverable 07); FV006-STE-007 propagates into the event-duplication risk documented in Deliverable 05
(FV006-EVT-004).

## 6. Verification Status of This Deliverable

- 7 findings recorded: 1 Critical, 2 Major-blocking, 2 Major/Moderate non-blocking-but-tracked, 1 Moderate
  conflict, 1 Moderate gap.
- No state or transition evidenced by TEAM A was found silently dropped or merged in a way that would obscure
  audit or financial meaning.
- The base commitment lifecycles (Sales/Purchase), the cancellation cascade, the Reversal/Return model, and the
  correction/undo-redo mechanics are all **VERIFIED** as internally consistent and evidence-traceable.
- One finding (FV006-STE-004) independently meets the Charter's Pre-Development Blocking Rule and is not
  resolvable by IBPV; it requires TEAM B rework and, on the rejection-handling policy itself, likely Boss/business
  input.
- This deliverable's material is **NOT READY FOR DEVELOPMENT** on the specific points listed as blocking above;
  the remainder of the state model is **VERIFIED** or **VERIFIED WITH CONDITIONS**. This is a per-area
  classification only — the consolidated Pre-Development Gate Recommendation is issued in Deliverable 15, not
  here.
