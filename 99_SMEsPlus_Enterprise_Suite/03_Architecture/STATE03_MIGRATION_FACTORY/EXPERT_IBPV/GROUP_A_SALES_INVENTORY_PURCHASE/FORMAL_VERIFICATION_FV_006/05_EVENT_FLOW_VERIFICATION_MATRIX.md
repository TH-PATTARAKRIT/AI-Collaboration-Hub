> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV (Independent Verification)
> Formal Verification FV-006 | Phase 4 — State / Event Verification | Deliverable 05 of 16
> Session: SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006 | TEAM B Frozen Commit: b98a3b9fb435845dbd15fae79db63b0b73a82420

# 05 — EVENT FLOW VERIFICATION MATRIX

## 0. Purpose, Method, and Boundary

This matrix independently verifies every canonical business event in `09_CANONICAL_BUSINESS_EVENT_CATALOG.md`:
who/what emits it, what state change it causes (cross-checked against Deliverable 04's state matrix), which
cross-domain consumers react to it, and whether the catalog is internally coherent with itself and with
`TEAM_A/06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md`. Per the assignment, this verification specifically checks
for: (a) events with no consumer ("dead events"), (b) state changes with no corresponding catalogued event
("untracked mutations"), and (c) cross-domain event orderings that could produce a race. IBPV classifies only; it
does not redesign the catalog.

## 1. Event-by-Event Verification

Legend: **Emitter** = originating domain/object; **Effect** = state/fact change (cross-checked against
Deliverable 04); **Consumer(s)** = cross-domain reactors per `09`; **TEAM A parity** = corresponding row in
`TEAM_A/06`, if any.

### 1.1 Events Originating in Commercial Demand (Sales) — `09` §01

| Event | Emitter | Effect | Consumer(s) | TEAM A parity | Verification |
|---|---|---|---|---|---|
| Commercial Commitment Confirmed | Sales | State → Committed | Inventory (fulfillment request for physical lines); "(for gated-billing-policy lines, nothing further fires automatically)" | `TEAM_A/06` §01 row 1 | VERIFIED WITH CONDITIONS — the parenthetical's "gated-billing-policy lines" phrase is not a term defined anywhere in the read package (billing policy, per `06` §04/`11` §02, governs Billable-Now computation, not line-level fulfillment classification). It is presumably intended to mean non-physically-fulfilled (service) lines, but the catalog's own wording conflates two distinct concepts. **Minor clarity gap, not scored as a numbered finding** — flagged for TEAM B's terminology pass. |
| Commercial Fulfillment Requested | Sales | Emits a fulfillment request | Inventory (creates Movement Instruction) | `TEAM_A/06` §01 row 2 | VERIFIED |
| Commercial Line Quantity Changed (post-commitment) | Sales | Ordered quantity changes | Inventory (adjusts request, subject to floor guard) | `TEAM_A/06` §01 row 3 | VERIFIED — see race check §3 (**FV006-EVT-004**) |
| Commercial Commitment Locked | Sales | Locked = true | "Sales itself (freezes named fields)" | `TEAM_A/06` §01 row Order locked | **Dead-event candidate — FV006-EVT-001** |
| Commercial Commitment Cancelled (post-commitment) | Sales | Not-yet-executed fulfillment cancelled | Inventory (release/cancel) | `TEAM_A/06` §01 row Order cancelled | VERIFIED |
| Billable-Now Recomputed | Sales | Billable-Now recomputed | "(internal to Sales; feeds the next Billing Event)" | Not separately rowed in `TEAM_A/06` | Borderline — see **FV006-EVT-001** |
| Billing Event Fired | Sales | Financial Handoff record created | Accounting (posts); Sales (re-derives Invoiced) | `TEAM_A/06` §01 row Invoice created | VERIFIED |
| Subcontract/Dropship Fulfillment Line Confirmed | Sales | Draft Supply Commitment created/reused | Purchase | `TEAM_A/06` §01 row Subcontract-service line confirmed | VERIFIED — but see wording concern **FV006-EVT-006** re: the §05 dependency-table entry for this same mechanism |

### 1.2 Events Originating in Supply Commitment (Purchase) — `09` §02

| Event | Emitter | Effect | Consumer(s) | TEAM A parity | Verification |
|---|---|---|---|---|---|
| Supply Commitment Confirmed | Purchase | State → Committed or → Pending Approval | Inventory (receipt request, direct/synchronous); Shared Master (Vendor Price Reference) | `TEAM_A/06` §02 row RFQ confirmed | VERIFIED |
| Supply Commitment Approved | Purchase | State → Committed | Inventory (unblocks request) | `TEAM_A/06` §02 row Order approved | VERIFIED |
| Supply Commitment Line Quantity Changed | Purchase | Ordered quantity changes | Inventory (adjusts receipt expectation) | `TEAM_A/06` §02 row PO line quantity reduced | VERIFIED — parity gap on floor-guard wording, see **FV006-EVT-007** |
| Supply Commitment Cancelled | Purchase | Not-yet-received fulfillment cancelled; received portion spared | Inventory | `TEAM_A/06` §02 row Order cancelled | VERIFIED |
| **(no event: Supply Commitment approval rejected)** | — | — | — | — | **Untracked mutation — FV006-EVT-003**, cross-ref FV006-STE-004 |
| Internal Demand Request Approved | Purchase | State → Approved | Enables PR→Supply Commitment conversion | `TEAM_A/06` §02 row Purchase Request approved | VERIFIED |
| Internal Demand Converted | Purchase | Supply Commitment line created/reused; allocation link written | Supply Commitment; IDR state becomes read-model mirror | `TEAM_A/06` §02 row PR line converted to PO | VERIFIED — mirror-value ambiguity cross-ref FV006-STE-006 |
| Multi-Vendor Comparison Resolved | Purchase | Winner proceeds; losers cancelled | Supply Commitment (losers) | `TEAM_A/06` §02 row Tender confirmed | VERIFIED |
| Supply Need Fulfilled | Purchase | New/reused draft Supply Commitment created | Inventory (on this commitment's own confirmation) | `TEAM_A/06` §02 row Reordering rule fires | VERIFIED |
| Billable-Now Recomputed / Billing Event Fired (AP) | Purchase | Financial Handoff record created | Accounting; Purchase (re-derives Invoiced) | `TEAM_A/06` §02 row Vendor bill posted | VERIFIED |

### 1.3 Events Originating in Physical Fulfillment (Inventory) — `09` §03

| Event | Emitter | Effect | Consumer(s) | TEAM A parity | Verification |
|---|---|---|---|---|---|
| Movement Instruction Confirmed | Inventory | Draft → Waiting/Confirmed; may emit further upstream request | Chained upstream instruction | `TEAM_A/06` §03 row Move confirmed | VERIFIED |
| Stock Reserved | Inventory | Reservation created/updated | Sales/Purchase advisory Available reads (never raw) | `TEAM_A/06` §03 row Move reserved | VERIFIED, passive/pull-only reaction — see transport-semantics gap **FV006-EVT-002** and concurrency gap **FV006-EVT-005** |
| Movement Executed | Inventory | Stock Position changes; Movement Execution recorded | Sales' Delivered / Purchase's Received re-derivation | `TEAM_A/06` §03 row Move done | VERIFIED |
| Fulfillment Continuation Created | Inventory | New continuation-linked Transfer Operation | "(Inventory-internal; Sales/Purchase do not consume the link directly)" | `TEAM_A/06` §03 row Picking validated with shortfall | **Dead-event candidate — FV006-EVT-001** |
| Reversal Executed | Inventory | New opposing Movement Execution, linked to original | Sales/Purchase (traceability only) | `TEAM_A/06` §03 row Return created | VERIFIED |
| Supply Need Raised | Inventory | Supply Need Event emitted | Purchase (or another registered fulfiller) | `TEAM_A/06` §03 row Replenishment procurement raised | VERIFIED |
| Put-Away Resolved | Inventory | Destination sub-location assigned | "(Inventory-internal)" | `TEAM_A/06` §03 row Put-away resolved | **Dead-event candidate — FV006-EVT-001** |

### 1.4 Events Originating in the Financial Handoff Boundary — `09` §04

| Event | Emitter | Effect | Consumer(s) | TEAM A parity | Verification |
|---|---|---|---|---|---|
| Financial Record Posted | Accounting (interface) | Posted record exists | Sales/Purchase (backward Invoiced re-derivation) | `TEAM_A/06` §01/§02 invoice rows | VERIFIED |
| Financial Record Reversed/Corrected | Accounting (interface) | Reversal exists | Sales/Purchase (backward re-derivation "on next read") | Not separately rowed in `TEAM_A/06` (out of GROUP A scope) | VERIFIED at the interface boundary; correctly not decomposed further per `09` §04 |

## 2. Dead-Event Check — Catalog Self-Consistency

`09` §00 states its own inclusion rule: *"An event qualifies for this catalog only if at least one other domain
observes or reacts to it... purely internal recomputation is not catalogued as an event."*

Three catalogued rows list **no cross-domain consumer at all**, directly contradicting that rule as written:

| Event | Catalog's own consumer text | Rule violated? |
|---|---|---|
| Commercial Commitment Locked (`09` §01) | "Sales itself (freezes named fields)" | Yes — single-domain only |
| Fulfillment Continuation Created (`09` §03) | "(Inventory-internal; Sales/Purchase do not consume the link directly...)" | Yes — explicitly denies cross-domain consumption |
| Put-Away Resolved (`09` §03) | "(Inventory-internal)" | Yes — single-domain only |

A fourth row is borderline: **Billable-Now Recomputed** (`09` §01) lists its consumer as "internal to Sales; feeds
the next Billing Event" — defensible as inclusion-by-necessity (it is a documented intermediate step in a chain
that *does* end in a cross-domain event), unlike the three above, which have no stated forward chain to any
cross-domain effect at all.

**Finding FV006-EVT-001 (CONFLICT FOUND, Major):** the catalog's own §00 inclusion criterion is violated by at
least three of its ~25 rows. Either the rule is too strict (and should be revised to explain why
internally-consequential-but-not-cross-domain events like a field-freeze are still worth cataloguing), or these
three rows should not be presented as canonical cross-domain business events. As written, Team C cannot reliably
use this catalog to decide which state changes require real cross-domain event wiring (e.g., an outbox/message
bus) versus which are plain in-process method calls — a material ambiguity given the Charter's emphasis on
"Integration boundaries and failure-recovery behavior." **Owner:** TEAM B. **Blocking:** No (a categorization/
documentation defect, not a missing capability). **Boss decision:** No.

## 3. Untracked-Mutation Check — States That Change With No Catalogued Event

Cross-referencing Deliverable 04's state matrix against the full `09` catalog surfaces one confirmed case:

**Finding FV006-EVT-003 (GAP FOUND, Critical):** the Supply Commitment can enter `Pending Approval` (`07` §01,
§03) and — per Deliverable 04's Finding FV006-STE-004 — the design never states what happens when approval is
**denied**. No event named "Supply Commitment Rejected" or equivalent exists anywhere in `09` §01–§04, even
though `12` §14 establishes that a generic "rejection event with an actor, a reason, and a timestamp" is a
first-class exception concept elsewhere in the same package. This is a textbook untracked mutation: if a business
rule allows the state to change on rejection, that change has no catalogued event to notify Inventory (whose
fulfillment request was already created against the now-blocked commitment, per `09` §02 row 1 "Inventory...
receipt fulfillment request, direct/synchronous") or Accounting. **Cross-domain impact:** an orphaned Inventory
fulfillment request with no instruction to stand down is a genuine audit/financial-integrity risk, not merely a
UX gap. **Owner:** TEAM B, coordinated with the Approval/SoD design. **Blocking:** Yes — Critical. **Boss
decision:** Yes, to the extent the rejection-handling behavior (auto-cancel vs. return-to-draft) is itself a
business-policy fork rather than a mechanical default.

No other untracked mutation was found: every other state transition identified in Deliverable 04 (Draft↔Sent,
Committed↔Cancelled, Instruction confirm/reserve/execute, Reversal) has a corresponding catalogued event.

## 4. Cross-Domain Event Ordering / Race Check

**Finding FV006-EVT-002 (GAP FOUND, Critical) — no stated transport semantics.** `09` never states, for any event,
whether emission and consumption are synchronous/transactional, asynchronous with at-least-once delivery, or
polled on next read. The only transport characterization anywhere in the read package is `08` §10's contrast of
Purchase's "direct/synchronous" receipt path against Sales' "indirect/event-driven" fulfillment-request path —
stated only for that one pair, not as a catalog-wide rule. Without this, race and failure-recovery behavior
(explicit Charter responsibilities: "Integration boundaries and failure-recovery behavior," "What happens when
downstream services fail?") cannot be conclusively verified — only flagged as open risk. **Owner:** TEAM B.
**Blocking:** Yes. **Boss decision:** No (a design-completeness item TEAM B must supply; IBPV would re-verify
whatever policy TEAM B states).

Building on that gap, two concrete race scenarios are identified:

**Finding FV006-EVT-004 (GAP FOUND, Major) — Sales fulfillment-request vs. quantity-change ordering.** Because
Sales' physical-demand path is explicitly "indirect/event-driven" (`08` §10) rather than synchronous, a user who
confirms a Commercial Commitment and then immediately edits the line's Ordered quantity (a supported
post-commitment action per `06` §02) fires two Sales-originated events — `Commercial Fulfillment Requested` and
`Commercial Line Quantity Changed` — in quick succession. Neither `09` nor `08` states an ordering guarantee
between them. If Inventory processes them out of order, or the adjustment targets a Movement Instruction that has
not yet been created, the instruction could silently retain the pre-edit quantity — a quantity-conservation
failure the Charter's IDTM future-testability lens explicitly asks IBPV to check for. This is precisely the kind
of "cross-domain scenario that may fail even when individual modules appear correct" the Charter singles out for
IBPV attention (§9.10/Cluster J of the governing prompt). By contrast, Purchase's equivalent pairing is lower-risk
because its receipt-demand path is stated as direct/synchronous. **Owner:** TEAM B. **Blocking:** Yes — Major.
**Boss decision:** No.

**Finding FV006-EVT-005 (GAP FOUND, Moderate) — Reservation-claim concurrency not explicitly covered.** `12` §11
requires the Stock Position bin's uniqueness to be an *enforced* invariant at write time (correcting an evidenced
defect), but that fix is scoped to the bin/quant write itself. The Reservation **claim** step — reading Available
and claiming against it (`05` §04) — is a separate operation the design does not explicitly cover with the same
concurrency-safety language. Two simultaneous claims (e.g., two Sales lines, or a Sales line racing an Internal
Transfer) against the same Available quantity could each be evaluated against a stale Available figure if the
claim itself is not atomic/serialized, even though partial claiming is explicitly a valid, non-error outcome.
**Owner:** TEAM B. **Blocking:** No — Moderate, tracked pending TEAM B confirmation that `12` §11's invariant is
intended to extend to the claim step. **Boss decision:** No.

No instance was found of two domains reacting to the **same** event with genuinely conflicting effects — every
event in §01–§04 above has at most one primary cross-domain consumer domain per instance (the Financial Handoff
events are structurally symmetric across Sales/AR and Purchase/AP but never apply to the same record).

## 5. Secondary Wording Findings

**Finding FV006-EVT-006 (GAP FOUND, Minor) — ambiguous write-direction wording.** `09` §05's cross-cutting table
lists "Commercial Commitment line | Purchase (subcontract/dropship...) | **Write, scoped** | [08]§09" — read
literally, this suggests Purchase writes into Sales' own commitment-line record, which would conflict with
domain-ownership principles used throughout `05`–`09`. The paired event row (`09` §01, "Subcontract/Dropship
Fulfillment Line Confirmed") describes the actual effect as "a draft Supply Commitment is created/reused" — i.e.,
a **new**, Purchase-owned record — consistent with `TEAM_A/06` §04's equivalent finding ("Purchase... creates a PO
line and stamps `sale_line_id`," a back-reference stamp, not a mutation of the Sales line). The catalog's own
wording does not resolve this internally. **Owner:** TEAM B (wording clarification). **Blocking:** No. **Boss
decision:** No.

**Finding FV006-EVT-007 (GAP FOUND, Minor) — floor-guard parity omission.** The Sales-side event row
("Commercial Line Quantity Changed") explicitly notes the change is "subject to the floor guard," while the
structurally parallel Purchase-side row ("Supply Commitment Line Quantity Changed," `09` §02) does not, even
though `12` §09 states TEAM B made the floor guard symmetric across both domains. Documentation-parity issue only
— the substantive rule is established elsewhere. **Owner:** TEAM B. **Blocking:** No. **Boss decision:** No.

## 6. Findings Register

| Finding ID | Verification Area | TEAM B Artifact(s) | Evidence/Baseline Ref. | Status | Severity | Blocking Dev? | Boss Decision? | Owner |
|---|---|---|---|---|---|---|---|---|
| FV006-EVT-001 | Catalog self-consistency (dead/internal events) | `09` §00 vs. §01/§03 | `TEAM_A/06` (no equivalent rule stated, N/A) | CONFLICT FOUND | Major | No | No | TEAM B |
| FV006-EVT-002 | Event transport/delivery semantics | `09` (whole document); `08` §10 | `TEAM_A/06` (method-call level only, not prescriptive) | GAP FOUND | Critical | Yes | No | TEAM B |
| FV006-EVT-003 | Untracked mutation — Supply Commitment rejection | `09` §02; `12` §14 | Not evidenced in `TEAM_A` files reviewed (Carry-Forward Unknown) | GAP FOUND | Critical | Yes | Yes | TEAM B |
| FV006-EVT-004 | Race — Sales fulfillment-request vs. quantity-change ordering | `08` §01, §10; `09` §01 | `TEAM_A/06` §01 (method-call rows, no ordering statement) | GAP FOUND | Major | Yes | No | TEAM B |
| FV006-EVT-005 | Race — Reservation-claim concurrency | `05` §04; `12` §11 | — | GAP FOUND | Moderate | No | No | TEAM B |
| FV006-EVT-006 | Wording — subcontract/dropship write direction | `09` §01, §05 | `TEAM_A/06` §04 | GAP FOUND | Minor | No | No | TEAM B |
| FV006-EVT-007 | Wording — floor-guard parity | `09` §01 vs. §02; `12` §09 | — | GAP FOUND | Minor | No | No | TEAM B |

**Cross-references to Deliverable 04:** FV006-EVT-003 pairs with FV006-STE-004 (same underlying gap, viewed from
the event side); the "read-model mirror" ambiguity noted for Internal Demand Converted pairs with FV006-STE-006;
the duplicate-confirmation gap FV006-STE-007 is the commitment-layer analogue of the transport-semantics gap
FV006-EVT-002.

## 7. Verification Status of This Deliverable

- 7 findings recorded: 2 Critical-blocking, 1 Major-blocking, 1 Major non-blocking-but-tracked, 1 Moderate, 2
  Minor.
- Dead-event check: 3 confirmed violations of the catalog's own inclusion rule (FV006-EVT-001).
- Untracked-mutation check: 1 confirmed instance (FV006-EVT-003), directly tied to Deliverable 04's most severe
  finding.
- Race check: 2 concrete scenarios identified (FV006-EVT-004, FV006-EVT-005), both rooted in the same underlying
  transport-semantics gap (FV006-EVT-002); no same-event conflicting-consumer race was found.
- The bulk of the catalog — the Commit→Fulfillment-Request→Reserve→Execute→Re-derive chain for both Sales and
  Purchase, the Financial Handoff round-trip, and the Reversal/Return event — is **VERIFIED** and traces cleanly
  to `TEAM_A/06`.
- This deliverable's material is **NOT READY FOR DEVELOPMENT** on the two Critical points (FV006-EVT-002,
  FV006-EVT-003) and the one blocking Major point (FV006-EVT-004); the remainder is **VERIFIED** or **VERIFIED
  WITH CONDITIONS**. The consolidated Pre-Development Gate Recommendation is issued in Deliverable 15, not here.
