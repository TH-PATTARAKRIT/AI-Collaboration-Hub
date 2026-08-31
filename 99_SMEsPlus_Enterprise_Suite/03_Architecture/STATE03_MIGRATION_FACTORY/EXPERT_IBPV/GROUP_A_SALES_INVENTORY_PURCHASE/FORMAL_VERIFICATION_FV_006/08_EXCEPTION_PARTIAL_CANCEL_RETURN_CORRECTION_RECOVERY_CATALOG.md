# 08 — Exception / Partial / Cancel / Return / Correction / Recovery Catalog

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D08`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`
Control Level: `/L999.999`
Boss: Sole Final Approver
Status vocabulary used throughout: `VERIFIED` / `VERIFIED WITH CONDITIONS` / `GAP FOUND` / `CONFLICT FOUND` /
`EVIDENCE MISSING` / `REWORK REQUIRED` / `NOT READY FOR DEVELOPMENT` / `READY FOR BOSS DECISION`

## 1. Purpose and Method

This deliverable verifies whether TEAM B's canonical design (frozen package, files 01–21 under
`TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/`) treats partial delivery, partial receipt, backorder, shortage,
over/under-fulfillment, cancellation before vs. after partial activity, return/reversal, correction, duplicate/
retry, cross-warehouse effects, and audit continuity as **first-class, deliberate design decisions** rather than
afterthoughts — and independently re-classifies three items the governing charter flagged as priority review
points: Fit-Gap Candidate #7 (count-in-progress vs. settled on-hand), #10 (over-fulfillment/over-billing default
policy), and #12 (asymmetric Purchase/Sales cancellation gates).

Per the charter's IBPV boundary, this document **does not redesign**. Every finding below states what TEAM B's own
artifacts say, what TEAM A's approved evidence baseline says, and what IBPV independently concludes from comparing
the two — never a proposed fix. Where TEAM B's own reasoning is re-derived and found sound, that is stated as
plainly as where it is found incomplete.

Primary TEAM B sources: `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`,
`11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md`, `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`,
`17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md`, `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md`, with
supporting cross-checks against `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md`,
`05_INVENTORY_CORE_CANONICAL_DESIGN.md`, `07_PURCHASE_CANONICAL_DESIGN.md`, `06_SALES_CANONICAL_DESIGN.md`, and
`15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` — cross-checks were necessary because §00 of the
governing task explicitly warns that a claim of "resolved" must not be accepted at face value.

Primary TEAM A baseline sources: `TEAM_A/09_QUANTITY_SEMANTICS_REGISTER.md`,
`TEAM_A/10_EXCEPTION_PARTIAL_RETURN_CANCELLATION_MATRIX.md`, `TEAM_A/14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`,
`TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md`, with supporting cross-checks against `TEAM_A/03_SALES_CAPABILITY_MODEL.md`
and `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` for the exact source mechanics underlying the cancellation-gate
asymmetry (§6 below).

## 2. First-Class Treatment Catalog

"First-class" here means: a deliberate decision is recorded, with a stated evidence basis, an ADOPT/ADAPT/EXTEND/
REJECT/UNKNOWN disposition, and (where the disposition creates new behavior) a location where that behavior is
actually designed — not merely asserted in the disposition table itself. Rows are marked **Thin** where a
disposition exists but the corresponding design substance is minimal or absent, and **Missing** where evidence and
design are both silent.

| # | Category | TEAM B Design Citation | TEAM A Baseline Citation | IBPV Assessment |
|---|---|---|---|---|
| 1 | Partial delivery | `12` §01 ("Partial Fulfillment (Delivery/Receipt)" — `ADOPT` unmodified: header status durable, line remaining always live); `08` §03 (Fulfillment Continuation splits unexecuted remainder) | `TEAM_A/10` #1 (PDEL-01/02, BO-04/08) | First-class |
| 2 | Partial receipt | `12` §01 (same disposition, explicitly symmetric to delivery); `07` §07 (Purchase cancellation "state-partitioned by how much has already been received") | `TEAM_A/10` #2 (POL-31) | First-class |
| 3 | Backorder | `12` §04 (`ADAPT`, self-continuation link, not a separate document type); `05` §05 (Fulfillment Continuation); `03` §03 (Fulfillment continuation classified as a Commitment fact) | `TEAM_A/10` #3 (BO-01..14) | First-class |
| 4 | Shortage (confirmation not gated by stock availability) | `13` §04 ("Sales-Side Confirmation Gate — An Open Business-Policy Decision" — requires a configurable gate per gate type, default not fixed) | `TEAM_A/10` #6 (advisory-only, non-blocking, GRPA-02/03/04) | Partial / correctly incomplete — see §3.4 |
| 5 | Over-fulfillment (over-delivery/over-receipt) | `12` §02 (`EXTEND` — configurable Over-Fulfillment Policy, default deferred); `11` §04 (cross-references the same decision) | `TEAM_A/10` #4; `TEAM_A/16` #10 | Shape first-class, default correctly open — see §5 (Fit-Gap #10) |
| 6 | Under-fulfillment | `12` §01 (subsumed under Partial Fulfillment / Backorder, §3/§4 above) | `TEAM_A/09` §05 item 1 (Remaining, `qty_to_deliver`) | First-class (treated as the mirror of partial delivery, not a separate mechanism) |
| 7 | Cancellation before confirmation | `12` §06 (`ADOPT` unmodified); `08` §05 | `TEAM_A/10` #10 (SO-22, PO-10) | First-class |
| 8 | Cancellation after confirmation (before vs. after partial activity) | `12` §07 (`ADOPT`, made symmetric; per-instruction correction to an evidenced batch defect); `08` §05; `07` §07 (Purchase, state-partitioned by receipt scenario); `06` §05 (Sales) | `TEAM_A/10` #11 (asymmetric evidence — origin of Fit-Gap #12) | First-class with an unresolved coherence question — see §6 (Fit-Gap #12) |
| 9 | Cancellation after reservation | `12` §08 (`ADOPT` unmodified) | `TEAM_A/10` #12 (MOV-22/31) | First-class |
| 10 | Return / reversal (customer and vendor) | `12` §05 (`ADAPT` in full — Reversal is Inventory-owned); `05` §05 (mandatory application-visible traceability link, elevated from a DB FK) | `TEAM_A/10` #8/#9 (fully-closed, negative-confirmed on both commercial sides) | First-class — strongest-evidenced pattern in the package (`17` §01 item 5) |
| 11 | Correction during physical movement | `12` §09; `08` §06; `05` §01 ("undo and redo in place," Inventory-internal, invisible to Sales/Purchase) | `TEAM_A/10` #13 | First-class |
| 12 | Correction after complete physical movement | `12` §10 (`ADOPT` as a hard invariant — no "un-execute" anywhere); `08` §06 | `TEAM_A/10` #14 (exhaustive negative claim) | First-class |
| 13 | Duplicate / retry behavior | `12` §11 (`REJECT` after-the-fact reconciliation; requires an enforced write-time invariant); `05` §02 | `TEAM_A/10` #15 (`_merge_quants()`, one concrete instance) | Thin — narrower than the evidence's own risk surface; see §3.5 |
| 14 | Cross-warehouse / cross-company effects | `12` §12 (`ADOPT` unmodified); `08` §07; `14` (referenced, not read in this deliverable's scope) | `TEAM_A/10` #16 | First-class |
| 15 | Audit continuity through all of the above | `03` §06 (traceability elevated to an application-visible fact, not merely a DB FK — an independent design requirement); `05` §05; `12` §15 (Line Deletion After Commitment — zeroed, never deleted, symmetric both sides); `12` §10 | Cross-cutting; no single TEAM A row, evidenced throughout `TEAM_A/10` | First-class — one of the strongest aspects of the package |

## 3. Narrative Notes on Specific Rows

### 3.1 Backorder / partial fulfillment (rows 1–3, 6)

TEAM B's decision to keep "remaining obligation" as a live, independently re-derived computation on the commercial
side rather than reading the Inventory-side continuation link (`08` §03: "an intentional non-coupling, adopted
from evidence as a genuine architectural choice, not a gap") is a defensible, evidence-grounded layering decision,
consistent with `03` §05's "Returned and Backordered are not independent commercial-line quantities" finding. No
gap found here.

### 3.2 Return / reversal (row 10)

TEAM B correctly separates two questions that TEAM A's evidence pack kept distinct: (a) the mechanism (Reversal,
`ADAPT`ed in full, Inventory-owned regardless of commercial origin — `05` §05), and (b) whether a Sales-initiated
RMA *affordance* should additionally exist, which TEAM B correctly leaves as `HYPOTHESIS / REQUIRES REAL USER
VALIDATION` rather than deciding it from Team A's unsourced "many SME businesses expect..." line (`12` §05; `17`
§04 item 15). This is the one case in the whole fit-gap register where TEAM B explicitly declines to treat a
plausible-sounding but unevidenced generalization as a finding — a correct, and notable, exercise of restraint.

### 3.3 Correction (rows 11–12)

The immutable-execution invariant ("no un-execute anywhere," `12` §10) is the load-bearing rule underneath audit
continuity (row 15) as well. It is consistently restated across `03` §03 (Movement Execution), `05` §01, and `08`
§06, and the floor-guard symmetry extension to Purchase (`12` §09, correcting a Sales-only evidenced asymmetry) is
a reasoned, evidence-anchored strengthening, not an invented rule. No gap found here.

### 3.4 Shortage / Sales confirmation gate (row 4)

TEAM B's disposition here is a genuine partial resolution, not a full one, and TEAM B says so itself (`17` §04
item 14: "TEAM B resolves the **shape** of the decision... but explicitly defers the **default value** to Boss/
business"). This is the same pattern as Fit-Gap #10 (§5 below) and is treated with the same judgment: correctly
left open, not silently defaulted. See §5.3 for the shared observation about the absence of a stated interim
fail-safe default across all three deferred policy items TEAM B lists in `20` §05 item 2.

### 3.5 Duplicate / retry behavior (row 13) — Finding FV006-EXC-002

TEAM A's evidence for this category is exactly one concrete, sourced mechanism: concurrent writers to the same
Stock Position bin (`TEAM_A/10` #15, citing `_merge_quants()`). TEAM B's disposition (`12` §11) correctly
strengthens this single instance — requiring the bin's uniqueness to be an *enforced* write-time invariant rather
than an after-the-fact reconciliation convention is a real improvement over the evidenced behavior.

However, "duplicate/retry" as a catalog category is broader than the one instance evidence happened to surface.
Neither `12` §11 nor any other file in the package addresses: (a) a retried commercial-side confirmation action
(e.g., a double-submitted Sales/Purchase confirmation creating two Movement Instructions for one commitment), or
(b) idempotency of the Financial Handoff round-trip described in `08` §08 / `15` §01–§03 (what happens if a
Billable-Now write to Accounting is retried after a timeout with an ambiguous prior outcome). TEAM A's evidence is
silent on both of these because its own research never encountered them (there is no corresponding row in
`TEAM_A/10`), so this is not a case of TEAM B ignoring available evidence — but it means the "duplicate/retry"
catalog cell is narrower than its label suggests, and a reader of `12` §11 alone could mistake the one closed
instance for full category coverage.

**Finding FV006-EXC-002.** Verification Area: Duplicate/Retry Recovery Coverage. TEAM B Artifact: `12` §11.
Approved Evidence/Baseline: `TEAM_A/10` #15 (single instance); `TEAM_A/14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`
(no broader duplicate/retry item registered). Finding Status: `EVIDENCE MISSING`. Severity: Minor. Why it matters:
a catalog entry that reads as "resolved" for one narrow, evidenced instance could be mistaken by Team C for
category-wide coverage of retry/idempotency risk, including at the commercial-confirmation and Financial-Handoff
layers where no evidence was ever gathered either way. Cross-domain impact: potential double-Movement-Instruction
or double-financial-posting risk is not confined to Inventory; it touches Sales, Purchase, and the Accounting
interface boundary. Gate impact: does not block the current design package, since nothing here contradicts it —
it is an uncovered surface, not a wrong decision. Required owner: whoever scopes the next evidence-gathering or
design session for GROUP A (Team A for further evidence, or Team B if a design decision is wanted without further
evidence). Blocking Development: No, not for the currently-scoped mechanisms; Yes for any Development story that
implements confirmation-submission or Financial-Handoff retry handling before this is addressed. Boss decision
required: No — this is a scoping/evidence gap, not a business policy call.

## 4. Independent Classification — Fit-Gap #7 (Physical Count-in-Progress vs. Settled On-Hand)

### 4.1 TEAM A's original framing

`TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` §01 item 7 classified this `UNKNOWN`: "Physical count workflow fused into
the same ledger row as the on-hand quantity... Works in source, but conflates two concerns (ledger + count-in-
progress) in one row — a target design may reasonably prefer separation." The underlying evidence citation is
`TEAM_A/02_INVENTORY_CAPABILITY_MODEL.md` item QNT-08: "Physical-count fields (`inventory_quantity`,
`inventory_diff_quantity`) live on the same row as the ledger — count workflow is fused in, not a separate
document." Team A explicitly declined to resolve this further because its evidence-only mandate could observe the
fusion but had no basis to decide whether a target design should keep or separate it.

### 4.2 TEAM B's claimed resolution

`17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md` §01 item 7 states: "TEAM B independently resolves this
to a decision: keep count-in-progress conceptually distinct from the settled on-hand ledger fact, even if a future
schema implementation stores them adjacently — a count-in-progress is a Commitment-type fact (a proposed
correction awaiting reconciliation), not yet a Physical fact," citing `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_
CATALOG.md` §00's fact-type taxonomy as the reasoning tool Team A's mandate did not have available. `20_TEAM_B_
FORMAL_IBPV_READINESS_REPORT.md` does not separately flag this item as a red flag or caveat in its §05 priority
review list, implying TEAM B considers it closed.

### 4.3 IBPV independent re-derivation

The reasoning tool itself is sound and correctly applied as far as it goes: the Commitment/Physical/Derived/
Control taxonomy in `03` §00 is genuinely established and consistently used elsewhere in the package (e.g.,
Movement Instruction = Commitment, Movement Execution = Physical, `03` §03). Classifying a proposed count
correction as "not yet a Physical fact until reconciled" is a coherent, defensible application of that taxonomy,
not an invented rule.

The problem is elsewhere: IBPV searched every TEAM B canonical design file for any actual modeling of "physical
count," "count-in-progress," "cycle count," "stocktake," or "inventory adjustment" beyond the one sentence in `17`
§01 item 7, specifically:

- `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §03 ("Physical Fulfillment (Inventory) Facts") lists nine
  facts (Movement instruction, Movement execution, Stock position, Reservation, Transfer operation, Fulfillment
  continuation, Reversal, Traceability unit, Handling unit, Supply need signal) — **no row for a Physical Count or
  count-in-progress fact appears anywhere in this table.**
- `05_INVENTORY_CORE_CANONICAL_DESIGN.md`, read in full (§00–§09), defines Movement Instruction/Execution,
  Stock Position, the six quantity views, Reservation, Transfer Operation/Continuation/Reversal, Traceability
  Unit/Handling Unit, and Supply Need Signaling — **no section addresses a physical count workflow, a
  count-in-progress entity, its lifecycle, its owner, or the mechanism by which it reconciles into Stock Position.**
- `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` (the E2E lifecycle catalog) contains no count-related scenario.
- `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` (the quantity register) contains no count-related row.

In short: TEAM B recorded a *classification label* for Fit-Gap #7, but never produced the Fact/State/Event/Owner/
Handoff design that its own acceptance criterion #5 (`20` §04 item 5) claims is "explicit for every material
flow." A physical inventory count is, by TEAM A's own evidence, a real, recurring operational activity (it exists
in the reference system as a live mechanism, not a hypothetical) — resolving *how it should be classified* without
also stating *what entity holds it, what states it passes through, what event fires on reconciliation, who owns
it, and how it hands off to a Stock Position adjustment (itself presumably a Movement Execution, per `05` §01)* is
not the same as designing it. This is exactly the pattern the governing task warned about: a claim of resolution
that should not be accepted at face value.

### 4.4 Classification

This finding does not fit cleanly into a single option of the five-way test in the governing task, because two
different things are being evaluated at once: the *classification reasoning* (sound) and the *design completeness*
(absent). Stated precisely: the classification is **evidence-supported design reasoning** as far as it goes, but
the material design artifact that classification was supposed to produce is **evidence missing / not authored**
anywhere in the frozen package. Net disposition:

**Finding FV006-EXC-003.** Verification Area: Fit-Gap Candidate #7 — Count-in-Progress vs. Settled On-Hand Fact.
TEAM B Artifact(s): `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md` §01 item 7 (the resolution claim);
absence confirmed against `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §00/§03 and
`05_INVENTORY_CORE_CANONICAL_DESIGN.md` §00–§09 (full file). Approved Evidence/Baseline:
`TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` §01 item 7; `TEAM_A/02_INVENTORY_CAPABILITY_MODEL.md` QNT-08. Finding
Status: `GAP FOUND`. Severity: Major. Why it matters: this was named a known priority item precisely because
count-in-progress vs. settled on-hand is a real source of operational and financial-reporting error (a count that
is merely proposed being read as if it were the settled quantity, or vice versa); a one-line classification without
an entity/state/event/owner design gives Team C nothing concrete to build against and risks the exact ambiguity
the classification was meant to prevent. Cross-domain impact: Stock Position (on-hand) is read by both Sales
(Available/Forecasted, `11` §01) and Purchase (Forecasted/Incoming, same); an unmodeled reconciliation path from
count-in-progress into Stock Position leaves both consuming domains exposed to the same fused-row ambiguity Team A
originally flagged, undiminished by the label change. Gate impact: undercuts the "PASS" self-assessment in `20`
§04 item 5 (Fact/State/Event/Owner/Handoff explicit for material flows) for this specific material flow; the
readiness report's §05 red-flag list does not surface this gap, so it would otherwise pass through undetected.
Required owner: the design function responsible for `05_INVENTORY_CORE_CANONICAL_DESIGN.md` and
`03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` (i.e., whoever next continues or supersedes TEAM B's design
work for GROUP A Inventory Core) must add the missing entity/state/event/owner/handoff design; this report does
not prescribe what that design should be. Blocking Development: Yes, for any Development story touching physical
count, cycle count, or inventory adjustment; No for Sales/Purchase commitment-and-fulfillment stories that do not
depend on a count-in-progress mechanism. Boss decision required: No — this is a design-completeness rework item,
not a business policy choice; Boss awareness is warranted only because Fit-Gap #7 was named a governing-prompt
priority item.

## 5. Independent Classification — Fit-Gap #10 (Over-Fulfillment / Over-Billing Default Policy)

### 5.1 TEAM A's original framing

`TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` §02 item 10: "Over-receipt/over-delivery is completely unguarded on both
Sale and Purchase lines... Whether exceeding ordered quantity should be blocked, warned, or silently allowed" —
classified `UNKNOWN`, with the rationale "a real design decision SMEsPlus must make deliberately — the source's
silence here is not evidence that silence is correct." `TEAM_A/10_EXCEPTION_PARTIAL_RETURN_CANCELLATION_MATRIX.md`
#4 independently confirms over-receipt is "never specially detected or blocked" as a genuinely unguarded condition,
not merely an unresearched one.

### 5.2 TEAM B's disposition

`12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §02–§03 and `17` §02 item 10: TEAM B does **not** leave
this `UNKNOWN`. It resolves the *existence* of a configurable Over-Fulfillment Policy (block / warn-and-allow /
allow-silently, symmetric across Delivered and Received) and a parallel Over-Billing Policy at the Billable-Now
computation, as a required design element — but explicitly refuses to fix a default value, stating this is
"flagged for Boss/business policy input." `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 2 independently
lists this as one of three business-policy decisions TEAM B deliberately deferred, and calls for Formal IBPV to
confirm it reaches Boss before implementation-level design proceeds.

### 5.3 IBPV independent judgment

This is not a case of TEAM B silently deciding a business question and calling it resolved. The distinction TEAM B
draws — deciding that a policy *must exist* is a design-shape question answerable from the operational-risk
argument alone (an unguarded quantity mismatch is a data-quality and fraud/error-masking exposure regardless of
which specific default a business later picks), while *which default* is a business-policy question requiring
owner input — is a coherent and defensible separation of concerns, correctly and visibly surfaced rather than
buried in a design-detail table. TEAM B's own `20` §05 explicitly asks Formal IBPV to confirm exactly this hand-off
to Boss, which IBPV does here.

Two independent observations qualify, but do not overturn, that conclusion:

1. **No interim fail-safe default is specified anywhere in the package.** `12` §02, §03, and `13` §04 all state
   "TEAM B does not fix a default" without also stating what a target implementation should do *if Development
   begins before Boss decides* — e.g., mandating a conservative default (such as `block`, or `warn-and-allow`) as
   the required starting state until Boss overrides it. Without that instruction, the practical effect of leaving
   this "open" is that whoever writes the first line of implementation code chooses the default by omission — which
   is exactly the silent-decision outcome TEAM B says it is trying to avoid.
2. All three of TEAM B's own deferred policy items (Invoiced-quantity definition, Over-Fulfillment/Over-Billing
   default, Sales Confirmation Gate default — `20` §05 item 2) share this same characteristic. The pattern is
   consistent, so it reads as a deliberate stance (leave the *value* open, do not prescribe an interim), not an
   oversight specific to this one item — but it is a stance with a real implementation-sequencing risk that Formal
   IBPV should surface explicitly rather than let pass silently.

On materiality: over-fulfillment/over-billing touches financial exposure and data-integrity risk on both the Sales
(AR) and Purchase (AP) sides symmetrically, and TEAM A's evidence confirms it is genuinely unguarded today with no
existing mitigating control. That is enough to make the *default value* decision material enough to gate the
specific feature area, without requiring that the entire GROUP A Development effort halt on it — the rest of the
Sales/Inventory/Purchase backbone (commitment, fulfillment, cancellation, return) does not functionally depend on
this one default.

### 5.4 Classification

**Finding FV006-EXC-004.** Verification Area: Fit-Gap Candidate #10 — Over-Fulfillment/Over-Billing Default
Policy. TEAM B Artifact(s): `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §02–§03;
`11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` §04; `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 2.
Approved Evidence/Baseline: `TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` §02 item 10;
`TEAM_A/10_EXCEPTION_PARTIAL_RETURN_CANCELLATION_MATRIX.md` #4. Finding Status: `VERIFIED WITH CONDITIONS`.
Severity: Major. Why it matters: the policy-shape decision is sound and correctly left open rather than
silently defaulted, but the absence of a mandated interim fail-safe default creates a real risk that Team C
resolves the open question by default-by-omission before Boss ever sees it, defeating the purpose of leaving it
open. Cross-domain impact: symmetric across Sales (AR/Billable-Now) and Purchase (AP/Billable-Now); an
unguarded default chosen by omission in one domain (e.g., `allow-silently`) would propagate the exact
data-quality/fraud-masking exposure TEAM B's own rationale in `12` §02 warns against. Gate impact: this specific
feature area (Over-Fulfillment/Over-Billing enforcement) should remain `NOT READY FOR DEVELOPMENT` until Boss
sets the default (or explicitly authorizes a stated interim default); it does not gate the rest of GROUP A.
Required owner: Boss (default value decision), with a condition that whoever authors the next-level design or
Development backlog item for this feature must be instructed to treat the absence of a Boss decision as a hard
block on that specific story, not as license to pick a default. Blocking Development: Yes, for the
Over-Fulfillment/Over-Billing feature specifically; No, for the rest of GROUP A. Boss decision required: Yes
— `READY FOR BOSS DECISION` on the default value (block / warn-and-allow / allow-silently, and its Over-Billing
counterpart).

## 6. Independent Classification — Fit-Gap #12 (Asymmetric Cancellation Gates: Purchase Stricter Than Sales)

### 6.1 TEAM A's original framing and underlying source mechanics

`TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` §02 item 12 classified this `UNKNOWN`: "Purchase's cancellation gate is dual
(locked OR open vendor bill); Sale's is single (locked only)... Could be intentional (AP exposure is a harder
blocker than AR) or accidental — not resolvable from source alone." The precise underlying mechanics, per
`TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` PO-10/PO-35: `button_cancel()` on Purchase has "two hard gates: `locked`
blocks the whole batch; any non-cancel/non-draft vendor bill also blocks the whole batch" — i.e., a vendor bill in
*any* state other than cancelled or draft (which in practice means a posted/open bill) independently blocks
cancellation. Per `TEAM_A/03_SALES_CAPABILITY_MODEL.md` CANC-04/05: Sale's `action_cancel()` "raises if `locked`"
and the base `_action_cancel()` "cancels only draft invoices... zero stock interaction" — it does not check
invoice state as a *blocking* condition at all; it simply auto-cancels the still-draft invoices as a side effect
and proceeds.

### 6.2 TEAM B's disposition

`12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07 and `07_PURCHASE_CANONICAL_DESIGN.md` §07: TEAM B
does not leave this `UNKNOWN`. It resolves it as `ADAPT` both gates as evidenced, reasoning that "an outstanding
vendor bill represents real financial exposure that an outstanding customer invoice on the Sales side does not
symmetrically create at cancellation time (a Sales cancellation only touches draft invoices, never posted ones, by
the same logic)." `17` §02 item 12 states this is "resolvable from the business-semantic difference alone, without
needing further evidence."

### 6.3 IBPV independent analysis

**(a) Whether this stays inside GROUP A's own declared authority.** `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_
DEPENDENCY_MODEL.md` §00 is explicit and unambiguous: "AR/AP internal posting logic... are Accounting Core's own
domain and are not designed, redesigned, or second-guessed here," restated at §00's closing list ("AR/AP internal
posting logic. Any of these referenced above is referenced only as 'Accounting owns this,' never [designed]").
Fit-Gap #12's justification requires exactly the kind of judgment that sentence disclaims: it asserts that a
vendor bill's "non-cancel/non-draft" state constitutes "real financial exposure" as a matter of business substance
— which is a claim about what an AP posting state *means*, not merely an acknowledgment that Accounting owns the
posting mechanism. TEAM B's own Financial Handoff contract (`08` §08; `15` §01–§03) models the interface only as
"Sales/Purchase write Billable-Now, then read back Invoiced" — it does not model "Purchase's own cancellation gate
reads a vendor-bill state value to block itself" as part of that interface at all. The vendor-bill state check
inside `button_cancel()` is therefore a second, undocumented read path into Accounting-owned state that exists
alongside the one Financial Handoff channel TEAM B does formally design — and the business-semantic weight Fit-Gap
#12 places on that state value is asserted, not verified against any AP posting-lifecycle evidence (none was
gathered; `TEAM_A/14` has no row on AP posting-lifecycle semantics).

**(b) Whether the comparison used to justify the asymmetry is actually complete.** TEAM B's rationale compares
Purchase's gate (blocked by *any non-draft* vendor bill, i.e., a **posted** bill blocks) against "a merely-drafted
customer invoice" on the Sales side. But the source evidence shows Sales' gate does not check invoice state *at
all* as a blocking condition — the live, unanswered comparison is what happens when a Sales order already has a
**posted** customer invoice against it: does the source evidence show that case being blocked, symmetric to
Purchase's posted-vendor-bill check? Per CANC-04/05, no — Sales cancellation is gated only by `locked`, full stop.
TEAM B's justifying sentence answers a comparison ("draft vs. draft") that was never the point of contention, and
does not address the comparison ("posted vendor bill blocks" vs. "posted customer invoice does not block") that
would actually test whether the asymmetry is a deliberate business-semantic choice or simply left unbuilt on the
Sales side in the reference system. This does not mean the asymmetry is wrong — AP exposure genuinely can be a
harder blocking condition than AR exposure in many businesses — but it means TEAM B's claim to have resolved this
"from the business-semantic difference alone, without needing further evidence" is weaker than stated: the
specific evidence that would make the comparison airtight (whether a posted Sales invoice is, or should be, an
equivalent Sales-side blocker) was not examined.

**(c) Coherence with partial-receipt/vendor-bill/reversal elsewhere in the design.** `05_INVENTORY_CORE_
CANONICAL_DESIGN.md` §08 item 3 and `12` §07 record a deliberate TEAM B strengthening: cancellation guards over a
batch of Movement Instructions must be evaluated **per-instruction**, correcting an evidenced defect where "one
executed instruction anywhere in a batch blocks the whole batch's cancellation." This principle is applied to the
*physical* fulfillment gate. It is not applied to, or even discussed against, the *financial-exposure* gate
carried over unchanged from evidence: "any non-cancel/non-draft vendor bill... blocks the whole batch" remains an
order-level, all-or-nothing check in TEAM B's own design (`07` §07 restates it without qualification). Given that
partial receipt and partial billing are both first-class, deliberately designed scenarios elsewhere in this same
package (`12` §01; `11` §03), TEAM B does not address the resulting interaction: a Purchase Order with one fully
received-and-billed line and one entirely unexecuted line would, on the evidence as carried forward, have its
*unrelated, unexecuted line's* cancellation blocked by a vendor bill against the *other* line — the same
all-or-nothing shape TEAM B explicitly classified as a defect one section earlier, for the physical gate. TEAM B
does not state whether it considered and rejected extending the per-instruction principle to the financial gate,
or simply did not examine the interaction.

### 6.4 Classification

Two distinct findings follow from §6.3(a)/(b) and §6.3(c) respectively.

**Finding FV006-EXC-005.** Verification Area: Fit-Gap Candidate #12 — Cancellation Gate Asymmetry, Domain-Boundary
and Evidence-Completeness. TEAM B Artifact(s): `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07;
`07_PURCHASE_CANONICAL_DESIGN.md` §07; `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md` §02 item 12;
compared against `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` §00. Approved Evidence/Baseline:
`TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` §02 item 12; `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` PO-10/PO-35;
`TEAM_A/03_SALES_CAPABILITY_MODEL.md` CANC-04/05. Finding Status: `CONFLICT FOUND`. Severity: Major. Why it
matters: TEAM B's own package states, in one file, that it will not design or second-guess AR/AP internal posting
logic, and then, in another file, resolves a GROUP A design question by asserting a specific business-semantic
weight for an AP posting-state value — the two positions are not reconciled anywhere in the package. Separately,
the specific comparison used to justify the asymmetry (draft vs. draft) is not the comparison that would actually
test it (posted vendor bill vs. posted customer invoice), so the claim to have resolved this "without needing
further evidence" is not fully supported by the evidence cited. Cross-domain impact: this is precisely a
GROUP A ↔ Accounting Core boundary question — the correctness of Purchase's stricter gate depends on facts
(what "posted vendor bill" implies operationally, and whether an equivalent posted-Sales-invoice case should
symmetrically block) that belong to Accounting Core and to further Sales-side evidence, neither of which TEAM B
consulted before deciding. Gate impact: this specific design decision (the dual cancellation gate as currently
justified) should not be treated as closed; it does not by itself invalidate the underlying evidenced mechanism
(both gates, as literally observed, may still be `ADOPT`-worthy), only the *justification* offered for treating
the asymmetry as deliberately correct rather than an artifact of uneven build-out. Required owner: joint —
Accounting Core's design owner (to confirm what an open/posted vendor bill's financial-exposure meaning actually
is) and Team A or Team B (to close the missing posted-Sales-invoice comparison) before the asymmetry is
re-affirmed. Blocking Development: No for building the two gates as literally evidenced (they are real,
sourced behaviors); Yes for treating "Purchase's stricter gate is a deliberate, correct business asymmetry" as a
settled design principle that should be extended or relied upon elsewhere without the missing evidence. Boss
decision required: No at this stage — this is an evidence/justification gap, not yet a business policy choice;
it may become one once the missing comparison is closed and shows a genuine, not merely evidenced-by-omission,
divergence in how the business wants AR vs. AP exposure treated at cancellation.

**Finding FV006-EXC-006.** Verification Area: Fit-Gap Candidate #12 — Cancellation Gate Granularity Coherence.
TEAM B Artifact(s): `05_INVENTORY_CORE_CANONICAL_DESIGN.md` §08 item 3; `12_EXCEPTION_PARTIAL_CANCEL_RETURN_
CORRECTION_MODEL.md` §07; `07_PURCHASE_CANONICAL_DESIGN.md` §07. Approved Evidence/Baseline:
`TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` PO-10/PO-35 (batch-level vendor-bill gate, as evidenced). Finding Status:
`GAP FOUND`. Severity: Moderate. Why it matters: TEAM B established, as a named deliberate strengthening, that an
all-or-nothing batch evaluation over Movement Instructions is a defect worth correcting; it carried forward an
equally all-or-nothing batch evaluation over vendor-bill financial exposure without applying, or discussing why it
declined to apply, the same principle — leaving an internal inconsistency in how "all-or-nothing gates" are
treated across two adjacent mechanisms in the same cancellation flow. Cross-domain impact: directly interacts with
partial-receipt and partial-billing, both first-class scenarios elsewhere in this design (`12` §01; `11` §03); an
order with independently-progressing lines could have an unrelated, unexecuted line's cancellation blocked solely
because a different line has an open vendor bill. Gate impact: does not block adoption of the vendor-bill gate as
evidenced, but the design package should not be read as having fully reconciled its own per-instruction principle
against this specific gate. Required owner: whoever owns `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`
§07 and `07_PURCHASE_CANONICAL_DESIGN.md` §07 for GROUP A. Blocking Development: No, for initial implementation of
the gate as evidenced (order-level, all-or-nothing, matching current source behavior); this should be noted as an
open design question before any Development story attempts to make the financial-exposure gate line-level or
per-instruction on the assumption that TEAM B already considered and endorsed that granularity — it did not
address it either way. Boss decision required: No — this is a design-coherence question for the responsible
design owner, not a business policy choice.

## 7. Consolidated Findings Register

| Finding ID | Verification Area | Status | Severity | Blocking Development | Boss Decision Required |
|---|---|---|---|---|---|
| FV006-EXC-002 | Duplicate/Retry recovery coverage narrower than category label | `EVIDENCE MISSING` | Minor | No (Yes if confirmation/Financial-Handoff retry work is scheduled first) | No |
| FV006-EXC-003 | Fit-Gap #7 — count-in-progress classified but not designed | `GAP FOUND` | Major | Yes, for physical-count/cycle-count/adjustment stories only | No (Boss awareness only) |
| FV006-EXC-004 | Fit-Gap #10 — over-fulfillment/over-billing default left open, no interim fail-safe | `VERIFIED WITH CONDITIONS` | Major | Yes, for the Over-Fulfillment/Over-Billing feature only | Yes |
| FV006-EXC-005 | Fit-Gap #12 — asymmetric gate justification crosses into unverified AP internals; comparison incomplete | `CONFLICT FOUND` | Major | Yes, for relying on the asymmetry as a settled principle beyond its evidenced literal behavior | No (not yet — pending evidence closure) |
| FV006-EXC-006 | Fit-Gap #12 — financial-exposure gate granularity not reconciled with per-instruction principle | `GAP FOUND` | Moderate | No, for the gate as literally evidenced; Yes, if extended to line-level without this being addressed | No |

## 8. Gate Recommendation Summary

The exception/partial/cancel/return/correction/recovery domain is, on the whole, one of the more carefully treated
areas of TEAM B's package: 12 of 15 catalog rows in §2 are assessed First-Class, the immutable-execution and
audit-continuity invariants are consistently and deliberately reasoned rather than assumed, and TEAM B's
restraint in *not* elevating Team A's unsourced RMA generalization (§3.2) is a positive independent-reasoning
signal, not just a compliant one.

Against the three named priority items specifically: Fit-Gap #10 was correctly identified as requiring Boss input
and was not silently decided, but needs an explicit interim-default instruction before Development starts on that
feature (`READY FOR BOSS DECISION` on the default value). Fit-Gap #7's classification is sound reasoning but was
never turned into an actual design, leaving a real Fact/State/Event/Owner/Handoff gap for count-in-progress
specifically (`GAP FOUND`, blocking only that feature area). Fit-Gap #12's disposition is the least settled of the
three: it reaches into Accounting Core territory the package elsewhere declines to enter, rests on an incomplete
evidentiary comparison, and leaves an unexamined granularity inconsistency against TEAM B's own per-instruction
principle (`CONFLICT FOUND` / `GAP FOUND`) — this item should not be treated as closed for Formal IBPV purposes
even though TEAM B's readiness report does not list it as a red flag.

None of the six findings in this deliverable require the entire GROUP A package to be held `NOT READY FOR
DEVELOPMENT`; each names the specific feature area it constrains. The package as a whole, for this domain, is
assessed `VERIFIED WITH CONDITIONS` — the conditions being the closure of FV006-EXC-002 through -006 above.
