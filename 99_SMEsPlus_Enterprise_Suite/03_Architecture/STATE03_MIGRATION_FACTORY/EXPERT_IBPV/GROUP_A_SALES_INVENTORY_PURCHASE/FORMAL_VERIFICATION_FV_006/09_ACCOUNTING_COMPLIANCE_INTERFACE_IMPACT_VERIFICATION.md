> GROUP A — Sales + Inventory + Purchase | EXPERT IBPV — Formal Independent Business Process & Design Verification
> Session: SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006 | Mandatory Deliverable — Accounting / Compliance Impact Verification
> Verifier boundary: classification only. IBPV does not redesign TEAM B work and does not design Accounting Core.

# 09 — ACCOUNTING / COMPLIANCE INTERFACE IMPACT VERIFICATION

## 00 — Scope and Method

This file independently verifies one Group A design surface: the boundary where Sales, Inventory, and Purchase
hand a financial consequence to Accounting Core. Per the EXPERT IBPV Charter §10 (clean-room boundary) and the
Formal IBPV Pre-Prompt Readiness Record §3.3 priority item 2, this verification does not use Accounting Core's
own (separately-approved, out-of-domain) design as an input — it only confirms that TEAM B's Group A artifacts
stopped where Group A's authority stops.

Three questions are answered, each against the allowed IBPV status vocabulary only:

1. Does `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` define only handoff/interface semantics, or
   does it redesign Chart of Accounts, GL posting, tax/WHT engine internals, fiscal-position internals,
   valuation-accounting internals, or AR/AP internal posting logic?
2. Is the correction/reversal identity defined at the boundary sufficient for a downstream accounting system to
   trace a correction/reversal back to its originating transaction, without Group A needing to know accounting
   internals?
3. Does Fit-Gap Register item #12 (stricter Purchase cancellation gate for "vendor-financial exposure") stay
   inside Group A's authority, or does it depend on Accounting Core behavior that Group A has not verified?

Artifacts examined: `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` (primary),
`12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07, `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md`
item 12, cross-checked against `07_PURCHASE_CANONICAL_DESIGN.md` §07, `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §04,
`08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §08, `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` §02–§04,
`03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §06, and the TEAM A evidence baseline
(`TEAM_A/13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` item 9, `TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` item 12).

---

## 01 — Verification Task 1: Does File 15 Stay Inside the Handoff/Interface Boundary?

**Finding FV006-ACC-001**

| Field | Content |
|---|---|
| Verification Area | Accounting/External Interface boundary discipline |
| TEAM B Artifact(s) | `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` §00–§08 (whole file) |
| Approved Evidence/Baseline | Governing prompt §10 (as restated in File 15 §00); `TEAM_A/13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` (Financial Handoff round-trip evidence); EXPERT_IBPV_CHARTER.md §10 (clean-room boundary) |
| Finding Status | **VERIFIED** |
| Severity | N/A (positive finding) |

**Analysis.** Read clause by clause, File 15 confines itself to the fact/event/identity that crosses the
boundary, not the internals on the far side:

- §01 (Financial Handoff Contract) states only *what* crosses (Billable-Now quantity + resolved identities),
  *who* writes it, and *what comes back* (a durable posted-record reference). It does not specify a chart of
  accounts, a journal structure, or a posting algorithm.
- §02 correctly identifies the Billing Event (not commitment confirmation, not physical execution) as the
  trigger — a business-semantic classification question, squarely inside Group A's authority to answer, not an
  accounting-internal one.
- §03 explicitly stops short of computing tax: "Accounting performs the actual substitution/computation —
  Sales/Purchase only supply candidacy, never compute the final tax amount themselves." This is the correct
  shape — Group A supplies an input, Accounting owns the computation.
- §06 (Fiscal/Tax Substitution) is explicitly carried forward as `CONTROLLED CARRY-FORWARD`, not designed —
  "the substitution algorithm itself... is not designed, guessed, or assumed here." This is the correct
  disposition for an item outside Group A's authority.
- §07 (WHT) is explicitly confirmed out of scope, with the reasoning traced to evidence (WHT attaches only to
  Accounting-internal concepts, never to Commercial/Supply Commitment documents).
- §08 restates the non-design list (COA, GL posting engine, journal numbering, WHT engine internals, tax engine
  internals, fiscal-position internals, valuation-accounting internals, AR/AP internal posting logic) and states
  that anything referenced above is referenced only as "Accounting owns this," never with an opinion on internal
  shape. Independent re-reading of §01–§07 confirms this claim holds — no clause states or implies an opinion on
  internal shape.

No clause in File 15, read on its own, redesigns or second-guesses Accounting Core. This part of the interface
model is well-scoped and is **VERIFIED** as within Group A's authority.

A boundary-adjacent observation (not a finding against File 15 itself, carried into Finding FV006-ACC-003 below):
File 15 is disciplined in isolation, but Group A's other artifacts (Files 07, 12, 17) rely on a fact that File 15
never defines as crossing the boundary. File 15's own discipline is what makes that gap visible — see §03 below.

---

## 02 — Verification Task 2: Is Correction/Reversal Identity Sufficient at the Boundary?

**Finding FV006-ACC-002**

| Field | Content |
|---|---|
| Verification Area | Correction/Reversal traceability at the Financial Handoff |
| TEAM B Artifact(s) | `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` §04–§05; `09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §04; `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §06; `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` §02–§04 |
| Approved Evidence/Baseline | `TEAM_A` evidence on the PO-line↔SO-line FK traceability gap (cited in `03` §06); Financial Handoff round-trip evidence underlying File 15 §04 |
| Finding Status | **VERIFIED WITH CONDITIONS** |
| Severity | Minor–Moderate |

**Analysis.** The base identity model is sound: File 03 §06 establishes the general rule that every fact must
carry a durable reference plus a traceability link to what it was derived from or reverses, and File 15 §04
correctly restates this for the Financial Handoff specifically — "the posted record must carry a durable,
application-visible link back to the originating Commercial/Supply Commitment line... elevated from a
database-only FK." This is exactly the right level of abstraction: it tells Accounting Core *that* a durable
link must exist, not *how* to structure the record that carries it.

The gap is in scope, not in principle. File 09 §04 records the "Financial Record Reversed/Corrected" event as
producing a *new* fact — "Accounting-owned reversal **exists**" — rather than describing an in-place status
mutation of the original record. File 15 §05 then requires only that "the backward read... always reflect the
current state of Accounting's record" (singular). Read together, this is ambiguous on exactly the point Group A
is not allowed to assume: if Accounting Core represents a correction/reversal as a *new*, separate record (the
common and audit-preferred accounting pattern, and the same pattern TEAM B itself uses for Inventory's own
Reversal mechanism, per File 09 §03 "Reversal Executed... linked to the original"), File 15 does not explicitly
state that the §04 traceability requirement extends to that new record as well as to the original posting. As
written, §04's traceability requirement is scoped to "every value crossing the Financial Handoff" — most
naturally read as the original Billable-Now write, at Billing Event time. It is not explicitly restated for
whatever record(s) Accounting Core may produce afterward in response to a correction/reversal.

This is a wording gap Group A itself is authorized to close (it is a requirement on what crosses back, not a
statement about how Accounting implements reversal), not a redesign of AR/AP internal posting logic. Contrast
this with File 11 §04, where TEAM B correctly declines to assume whether Accounting's "Invoiced" figure should
be based on posted-only or any-non-cancelled postings, and explicitly defers that as an open Boss/business
decision rather than assuming an answer — the same discipline is not fully carried through to the
correction/reversal identity requirement in File 15 §04–§05.

**Why it matters.** If a target implementation reads File 15 §04 literally (traceability required only on the
original crossing), a downstream accounting reversal record that is not required to carry the same durable link
could exist without Sales/Purchase being able to associate it with the correct commitment line — breaking the
"backward read reflects current state" guarantee in §05 for exactly the case (correction/reversal) it exists to
cover.

**Cross-domain impact.** Low as currently scoped — this is a wording/completeness issue inside Group A's own
artifact, resolvable without Accounting Core's internal design being known, since the requirement can be phrased
generically ("any record Accounting Core produces in relation to a given Commercial/Supply Commitment line, at
any time, must carry the durable link") without assuming whether that is one mutable record or a linked set.

**Gate impact.** Does not block Development on its own; recommend closure before Team C begins on the
Financial-Handoff read-back path, since ambiguity here is exactly the kind of "unverified state/event transition
that affects financial/control integrity" the Charter's Pre-Development Blocking Rule (§9) is written to catch.

**Required owner.** TEAM B (interface-wording clarification within File 15, inside Group A's own authority — no
Accounting Core input required to fix the wording itself, though Accounting Core's confirmation that it can
honor the (now-explicit) requirement would remove residual doubt).

**Blocking Development.** No (Minor–Moderate, not Critical).
**Boss decision required.** No — this is a TEAM B clarification, not a policy question.

---

## 03 — Verification Task 3: Does Fit-Gap #12 Stay Inside Group A's Authority?

**Finding FV006-ACC-003**

| Field | Content |
|---|---|
| Verification Area | Cross-domain authority boundary — Purchase cancellation gate |
| TEAM B Artifact(s) | `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md` §02 item 12; `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07; `07_PURCHASE_CANONICAL_DESIGN.md` §07 (dual cancellation gate sub-bullet) |
| Approved Evidence/Baseline | `TEAM_A/13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` item 9 ("A Purchase order cannot be cancelled while `locked`, or while it has a non-cancel/non-draft vendor bill... ORM method guard"); `TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md` item 12 (Team A: `UNKNOWN` — "Could be intentional... or accidental — not resolvable from source alone") |
| Finding Status | **GAP FOUND** |
| Severity | **Critical** |

**Analysis.**

*What Team A evidenced.* The reference-system behavior itself is solid, test-confirmed evidence: Purchase's
cancellation guard blocks when the commitment is locked, **or** when a "non-cancel/non-draft vendor bill" exists
against it. Team A correctly left the *design intent* behind this dual gate as `UNKNOWN` — the evidence shows
only that the behavior exists, not why, and not whether it should carry forward.

*What TEAM B decided.* TEAM B resolved this UNKNOWN itself, in three places (File 07 §07, File 12 §07, File 17
item 12), using identical reasoning each time: "an outstanding vendor bill represents real financial exposure"
that "a merely-drafted customer invoice does not symmetrically represent," therefore `ADAPT` both gates as
evidenced. File 17 §05 explicitly lists item 12 as one of three cases where "TEAM B resolved beyond Team A's own
classification... using reasoning tools... not evidence" — TEAM B's own words confirm this was decided by
business-semantic reasoning alone, not by further evidence gathering.

*The boundary problem.* The phrase "open vendor bill" / "non-cancel/non-draft vendor bill" names a fact that
does not exist anywhere in Group A's own interface model. A targeted search of every Group A canonical artifact
(Files 08, 09, 15 — the E2E lifecycle model, the event catalog, and the accounting interface model, respectively)
turns up no definition of a "vendor bill status" fact crossing the boundary. The only two facts File 15 defines
as readable back from Accounting are (a) "a durable posted-record reference... to re-derive Invoiced quantity"
(§01) and (b) the Correction/Reversal Signal for the same backward Invoiced-quantity re-derivation (§05). Neither
is "does a non-cancel/non-draft vendor bill exist for this line" — that is a finer-grained fact about the
*internal lifecycle state* (draft / posted / cancelled) of an Accounting-owned document, which File 15 §00 and
§08 place explicitly outside Group A's authority ("AR/AP internal posting logic... not designed, redesigned, or
second-guessed here").

In the evidenced reference system, Purchase and the vendor Bill live in one application/database, so a direct
query across that boundary is structurally possible and was never a design decision at all — it was simply how a
monolith is built. TEAM B's `ADAPT`ed design carries that direct-query behavior forward as a Group A control
precondition without first asking whether Group A's own bounded interface (which it authored in File 15) can
actually supply that fact. It cannot, as File 15 currently stands. This is not a hypothetical concern: it is a
demonstrable inconsistency between what File 15 (interface model) defines as crossing the boundary and what
Files 07/12/17 (cancellation gate design) assume is available to read.

This also means the conclusion is not framed the way Group A's authority requires. A framing that would have
stayed inside authority is available and already implicit in Group A's own vocabulary — e.g., gating on "does an
un-reversed Financial Handoff posted-record reference exist for this line" (a fact File 15 §01/§05 already
defines). Instead, the adopted framing ("outstanding vendor financial exposure," "non-cancel/non-draft vendor
bill") describes and depends on a document-lifecycle distinction (draft vs. posted vs. cancelled) that belongs to
AR/AP internal posting logic — precisely the category File 15 §08 lists as not Group A's to assume.

*A discipline inconsistency worth naming.* Elsewhere in the same package (File 11 §04), TEAM B correctly declines
to assume how Accounting Core internally distinguishes posted from non-cancelled postings, and explicitly defers
that exact distinction to Boss/business as an open policy question rather than building a design on top of an
assumed answer. Fit-Gap #12 leans on the same underlying distinction (a bill's internal posted/draft/cancelled
state) but, unlike File 11 §04, does not defer it — it treats the distinction as safely assumable and closes the
question outright. The two are not reconcilable as written: either the posted/cancelled distinction is knowable
and usable by Group A (in which case File 11 §04's deferral is over-cautious) or it is not (in which case
Fit-Gap #12's `ADAPT` rests on an assumption Group A has no authority to make). TEAM B's package currently
contains both positions.

**Why it matters.** A cancellation gate is a control — exactly the category of design the Charter (§9) treats as
blocking when unresolved ("unresolved accounting/compliance impact," "unverified state/event transition that
affects financial/control integrity," "untraceable Team B design decision"). As currently specified, a Team C
implementer cannot build this gate from Group A's own artifacts without either (a) reaching directly into
Accounting Core's internal document state — which violates the domain boundary Group A itself established — or
(b) inventing an interface signal that no Group A artifact defines and that Accounting Core has not confirmed it
can supply. Either path means the gate is being implemented by guesswork, not by traceable design.

**Cross-domain impact.** High. Resolving this requires input from whoever owns the Accounting Core domain — Group
A cannot unilaterally decide whether an "obligation-open/outstanding" signal can be exposed at the boundary, in
what shape, or with what latency, because that decision is inseparable from Accounting Core's own posting-engine
design, which is expressly outside Group A's authority to assume or specify.

**Gate impact.** Blocks this specific control point at the Pre-Development Design Gate. Per Charter §9, this
qualifies independently under at least three blocking categories: unresolved accounting/compliance impact,
unverified financial/control-integrity transition, and untraceable design decision (the gate's precondition
traces to no defined interface fact).

**Required owner.** Two distinct actions, for two distinct owners, neither of which is IBPV's to perform:

- **TEAM B** — for the interface-completeness gap itself: File 15 does not currently define the fact this gate
  depends on, and that is a Group A authoring gap Group A must close (in-authority: deciding what Group A asks to
  cross the boundary is Group A's job; deciding what Accounting Core can supply is not).
- **Whoever owns the Accounting Core domain** — input is required on whether, and how, a vendor-obligation-open
  signal (however it is ultimately framed) can be exposed at the boundary without exposing AR/AP internal
  posting logic, since that determines what Group A is even able to design against.
- **Boss** — a policy decision is also required independently of the interface question: Team A left the
  underlying business intent as `UNKNOWN` ("could be intentional or accidental"), and TEAM B's resolution rests
  on a business-semantic assertion Group A's mandate does not have standing to finalize unilaterally once it
  depends on cross-domain facts. Whether Purchase should in fact carry a stricter cancellation gate than Sales is
  a business-policy question for Boss, informed by both teams, not a fact Group A's own reasoning alone can
  settle.

**Blocking Development.** **Yes**, for this specific control point (the Purchase cancellation gate's dual
precondition), pending the cross-domain input and Boss decision above. This does not by itself imply the entire
Group A package is blocked — that determination belongs to the consolidated IBPV verification report — but this
control point specifically is not implementable as currently specified.

**Boss decision required.** **Yes.**

---

## 04 — Summary Table

| Finding ID | Area | Status | Severity | Blocking Development | Boss Decision Required |
|---|---|---|---|---|---|
| FV006-ACC-001 | File 15 boundary discipline (COA/GL/tax/WHT/fiscal/valuation/AR-AP-internal non-design) | VERIFIED | N/A | No | No |
| FV006-ACC-002 | Correction/reversal identity sufficiency at the Financial Handoff | VERIFIED WITH CONDITIONS | Minor–Moderate | No | No |
| FV006-ACC-003 | Fit-Gap #12 — Purchase cancellation gate depends on an undefined, out-of-authority AP-internal fact | GAP FOUND | Critical | Yes (this control point) | Yes |

## 05 — Section Recommendation to the Consolidated IBPV Report

On the accounting/compliance interface surface specifically: the Financial Handoff contract in File 15 is, in
isolation, a well-scoped and authority-respecting design — **VERIFIED**. It requires one wording tightening on
correction/reversal traceability before Team C begins — **VERIFIED WITH CONDITIONS**. Fit-Gap #12's cancellation
gate resolution is **GAP FOUND**, Critical severity, and is not ready for Development as specified: it resolves a
Team-A-flagged `UNKNOWN` using a business-semantic assumption that silently depends on Accounting Core's internal
document-lifecycle state, a fact Group A's own interface model does not define and has no authority to assume.
This item should be carried into the consolidated report as a named blocking item requiring both Accounting-Core-
owner input and a Boss policy decision before this specific control point may proceed to Team C.
