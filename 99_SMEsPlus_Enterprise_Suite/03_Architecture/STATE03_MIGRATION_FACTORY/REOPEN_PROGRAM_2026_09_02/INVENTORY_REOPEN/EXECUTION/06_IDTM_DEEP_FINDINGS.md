# Inventory Full Reopen — EXPERT IDTM Deep Findings (Track 04 Convergence)

| Field | Value |
|---|---|
| Session | `SMEPLUS-26-09-02-INV-REOPEN-001` |
| Jira | `ERPPLUS-139` |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical Branch | `SMEsPlus` (this track's evidence is **not yet merged** — see §3.10) |
| Reopen Execution Branch / Worktree | `audit/inventory-reopen-2026-09-02-inv-reopen-001` / `INVENTORY_REOPEN_2026_09_02_EXECUTION` |
| Underlying Evidence Branches Cited | `audit/inventory-core-corr007b-3high-closure-010` (tip `0eb78c68`, controlling round CORR-007B); `claude/inventory-core-backbone-dr002` (tip `b31597fa`, baseline round DR-002) |
| Control Level | `/L999.999` |
| Track | `04 — EXPERT IDTM` |
| Mandate | Data, Identity, Reconciliation & Integrity — identity, lineage, reconciliation, migration integrity, idempotency, deep testability |
| Deliverable | `06_IDTM_DEEP_FINDINGS.md` |
| Date | 2026-09-02 |
| Inputs Converged | Council (challenge) findings + Special Team (investigation) findings — produced independently, blind to each other, per the 9-Veto Council Charter's anti-groupthink rule |
| **Status** | `TRACK 04 OUTPUT — COUNCIL + SPECIAL TEAM CONVERGED — VERDICT: HOLD — CHALLENGE/INVESTIGATION EVIDENCE ONLY, NOT A GATE DECISION` |

This document does not declare a Gate PASS, does not authorize Team B design, Team C implementation, or Development on Inventory, and does not close, override, or supersede any standing governance ruling. It converges two independently-produced Track 04 (EXPERT IDTM) findings sets into one evidence record for Boss's eventual Gate decision on the Inventory Full Reopen. Where the two inputs disagree, that disagreement is stated explicitly below rather than resolved by picking a side — surfacing exactly this kind of divergence is the point of running Council and Special Team blind to one another in the first place.

---

## 1. Purpose, Scope, and Method

This is the Track 04 (EXPERT IDTM) deliverable for the Inventory Full Reopen. The mandate boundary is identity, lineage, reconciliation, migration integrity, idempotency, and deep testability, as scoped to Inventory ("Stock Truth") by the Full Reopen Program and the 9-Veto Council Charter.

Two inputs were converged to produce it:

- **Council (challenge)** — a Veto-track review of the existing Inventory Core Backbone evidence chain (the nine-branch lineage DR-002 → IER-003 → CORR-005 → IDR-007 → CORR-006 → CORR-007A → CORR-007B), read at each branch's actual git tip rather than from any summary layer, with several specific claims independently re-verified by targeted re-greps rather than trusted by citation alone.
- **Special Team (investigation)** — an independent investigation combining (a) the same prior-evidence chain and (b) fresh, largely blind primary-source re-reading of the Odoo reference implementation at `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/{stock,stock_account,uom}`, performed before comparing its own conclusions against prior documents.

Both were produced blind to each other. This document's job is to converge them honestly: merge genuine agreement, credit each input's distinct contributions, and explicitly surface — not silently paper over — any place they diverge in substance, severity, or framing.

This document is evidence for Boss's Gate decision. **It is not the Gate decision itself.** It does not declare Gate PASS. It does not authorize Team B design, Team C implementation, or Development. Where it recommends anything, it recommends conditions attached to the standing `HOLD`, not a path around it.

---

## 2. Verdict Reconciliation

### 2.1 Headline Verdicts

| Input | Verdict |
|---|---|
| Council (challenge) | `HOLD` |
| Special Team (investigation) | `HOLD` |
| **Reconciled Track 04 Verdict** | **`HOLD`** |

At the headline level, Council and Special Team converge without needing arbitration: both recommend `HOLD`, both explicitly decline to treat Team B or Team C as authorized, and both frame their own recommendation as reinforcing — not replacing — the standing `Account + Inventory Backbone Reference Baseline = HOLD` disposition already in force from CORR-007B.

Agreement at the headline level does not mean the two inputs agree on everything underneath it. Two places exist where the blind reviews genuinely diverge — not on the underlying facts, in either case, but on how those facts should be weighed and characterized. Both are surfaced explicitly here.

### 2.2 Surfaced Disagreement 1 — Severity and Ownership Framing of the Idempotency / Migration-Replay Gap

| | Council's Framing | Special Team's Framing |
|---|---|---|
| Item classification | `CONFLICTING / PARTIALLY SUPPORTED` — "primary material gap for this mandate" | `REFINED / NARROWED, not elevation-worthy` (concurrency/record-state); `MATERIAL GAP CONFIRMED... routed to Team A/Migration` (replayability) |
| Characterization | "The single weakest point in the whole chain," one of "the two headline technical questions this reopen was chartered to test," has received "ZERO additional scrutiny" across five corrective rounds | Performed fresh, independent re-tracing this cycle; narrows (does not overturn) the prior open scope; explicitly "a refinement... not a reason to reopen or elevate" |
| Recommended next step | Should become a named, first-class functional requirement for Team B from day one, given the Charter's Zero-Tolerance ruling on duplicate-posting-by-replay | Confirmed gap is a required Team A/Migration design input, but "not an Inventory Evidence Gate blocker on its own" |

Both reviews agree on every underlying fact: no unified idempotency-key mechanism exists in the reference system; no external-ID/provenance field exists on any source Inventory record; a genuine record-state guard exists (`_action_done()`'s already-done/cancel filter); a genuine but partial concurrency lock exists (`try_lock_for_update()`, quant-UPDATE path only, no equivalent on the quant-CREATE path). Where they diverge is severity and next-step ownership, not substance.

This document does not adjudicate which framing should govern — that is Boss's call. What can be said without taking a side: the specific complaint animating Council's framing — that this question has gone unscrutinized for five rounds — is, as of this very cycle, no longer fully true. Special Team's session is itself the fresh scrutiny Council's review (produced blind to it) correctly identified as absent from everything that came before. Whether that fresh scrutiny is enough to downgrade the item's severity, as Special Team concludes, or merely narrows its scope while leaving its severity intact, as Council's own framing would likely still hold had it seen Special Team's parallel work, is exactly the kind of judgment this reopen's governance structure reserves for Boss. Full technical detail is in §3.4–§3.5.

### 2.3 Surfaced Disagreement 2 — Characterizing This Cycle's Work Against the EXPERT IDTM Charter

Council's review states explicitly that nothing reviewed this cycle is, or should be mistaken for, the Charter-defined EXPERT IDTM 100%-AI Deep Test Matrix execution (Dimensions 2 and 6 of `EXPERT_IDTM_CHARTER.md`), because that execution requires a built Team C implementation to test against — which does not exist for Inventory, since Team B design is not even authorized yet.

Special Team's own narrative opens differently: it describes itself as "the first Special Team session under the new 9-Veto governance to close that loop" on DR-002's `A13_CROSS_DOMAIN_INVARIANT_CANDIDATE_REGISTER.md`, stating plainly, "this session is that pass." Read in isolation, that language risks being understood as a claim that formal EXPERT IDTM execution has now occurred for Inventory.

Section 3.9 examines this in full and concludes the tension is one of self-characterization only — Special Team's own described methodology (reference-code re-reading, no code changes, no database restore or live query, no built target system tested) is factually consistent with Council's more conservative framing, not in conflict with it. But the language difference is real, it is surfaced here rather than smoothed over, and this document adopts Council's framing as governing for its own status and closing language — precisely because this document's own charge is to avoid anything that could be misread as declaring readiness.

### 2.4 Where the Two Inputs Fully Agree

The two disagreements above should not overshadow the actual shape of the evidence. Full convergence — several points independently re-derived rather than merely cross-cited — exists on: the quantity-identity model; the UOM structural facts; the lot/serial/package source-identity facts; the concurrency row-lock finding; the fact that no native provenance field exists; the absence of DB CHECK constraints on negative quantity and duplicate bins; the standing `N-A12-01` disposition and its NOT PROVEN sub-items; the `GRPA-M15` closure; and the Clean-Room impact assessment. Section 3 covers all of this, not only the two points of divergence.

---

## 3. Detailed Findings

### 3.1 Quantity Identity Model ("Stock Truth")

Both reviews converge, independently, on the same foundational model. Stock Truth is a single `stock.quant` row keyed on the five-part tuple (product, location, lot, package, owner). Council's citation traces DR-002's A3 deliverable, which maps six derived-vs-stored quantity concepts — on-hand, reserved, available, demand, `product_qty`, done quantity — each to an exact field, compute dependency, mutation trigger, and correction path, independently re-derived (not merely re-cited) by IDR-007's own primary-source re-reads. Special Team, working from a fresh, largely blind read of `stock_quant.py` this session, arrived at the identical structure without first consulting DR-002's write-up: `quantity` (on-hand, stored) and `reserved_quantity` (stored) as the two ledger primitives, with `available_quantity` computed as `quantity - reserved_quantity` (`stock_quant.py:78-122`). This structure is now confirmed by at least three independent reading passes — DR-002's original research, IDR-007's re-derivation, and this cycle's Special Team re-derivation — with no daylight between any of them.

Special Team adds one mechanism-level detail neither Council's summary nor DR-002's citation set foregrounds as sharply: `_get_available_quantity()` (`stock_quant.py:793-832`) clamps the reported available figure to zero by default (`allow_negative=False`); a true negative persists silently in the underlying `quantity` field and surfaces only when a caller explicitly passes `allow_negative=True` (used, per Special Team's reading, for historical as-of-date valuation lookups). This sharpens rather than contradicts Council's own citation of the schema-level fact that no DB CHECK constraint blocks a negative `quantity` value (§3.6).

**Position:** `CLOSED_WITH_EVIDENCE`. No disagreement.

### 3.2 UOM Conversion, Rounding, and Historization

Both trackers converge on the same structural deviation from a textbook Odoo mental model: there is no `uom.category` model; convertibility between two units is determined by walking a self-referential `relative_uom_id` tree to a common ancestor, not by a stored category foreign key (Council: DR-002 A3 §3 / A5 §6; Special Team: independently traced `_has_common_reference()`, `uom_uom.py:218-230`). Both also confirm rounding precision is global rather than per-UoM — one shared "Product Unit" record system-wide (Council); Special Team's independent read (`uom_uom.py:62-67`) reaches the same conclusion.

Special Team's fresh source read surfaces two sub-findings that go beyond what Council's review captured this cycle:

- `_compute_quantity()`'s default `rounding_method` is `'UP'` (`uom_uom.py:152`) — ordinary cross-UOM conversion is not neutral-rounding by default, with direct bearing on any migration or reconciliation calculation crossing a UOM boundary.
- `_onchange_critical_fields()` (`uom_uom.py:79-93`) contains an explicit, source-authored warning that editing a UOM's `relative_factor` does **not** retroactively update existing data, and that changing core UOMs on a running database is "not recommended." Special Team frames this as a historical-continuity risk distinct from, and additive to, the already-standing `N-A12-01` finding: `N-A12-01` concerns whether opening/closing *stock value* is continuous across a period boundary; this new finding concerns whether a *quantity conversion* recorded in the past remains reproducible once today's conversion-factor table has moved on. Council's review neither tested nor contradicted this; it is new evidence this cycle contributes to the same continuity conversation Council's own `N-A12-01` discussion already flags as material.

**Position:** structural UOM facts — `CLOSED_WITH_EVIDENCE`, converged. UOM non-historization — `CARRY_FORWARD`: a genuine, newly-surfaced sub-risk belonging in the same Team B continuity conversation as `N-A12-01`, not yet evaluated by any design.

### 3.3 Lot / Serial / Package Traceability Identity

Both reviews agree, as source facts, on the `product.template.tracking` three-way gate, the absence of a `product.packaging` model (replaced by `uom_ids`/`product.uom` barcode records), and the distinction between `stock.package.history` (a separate, append-only immutable snapshot) and a reusable, live `stock.package` row.

Council flags a specific unresolved migration decision: whether SMEsPlus should carry forward live package state, the append-only history snapshot, or both — flagged since DR-002, never revisited by any of the five subsequent corrective rounds. Special Team's session did not take up this specific question this cycle; it is neither newly resolved nor newly contradicted here, and remains exactly where Council's review found it.

Special Team contributes new, independent depth on a related but distinct question: identity-constraint coverage. Direct field-level inspection of four models this session found `stock.picking` carries a genuine DB-level `unique(name, company_id)` constraint (`stock_picking.py:710-713`), while `stock.quant`, `stock.lot`, `stock.package`, and `stock.reference` carry no DB-level uniqueness equivalent anywhere in the models read. `stock.lot`'s own uniqueness (name + product + company) is enforced only by a post-write `@api.constrains` method (`_check_unique_lot()`, `stock_lot.py:103-126`) — an ORM-level, not database-level, guarantee. `stock.quant.sn_duplicated` (`stock_quant.py:217-223`) is a reactive, read-time detector for serials that have already collided, not a preventive gate. `stock.package.name` carries only a trigram search index (`stock_package.py:25`), no uniqueness constraint at all. Special Team characterizes this as a three-tier picture: the outward-facing transfer-document number is protected at the database layer; the underlying ledger, traceability, and grouping identities are not. This refines Council's own, more general schema-constraint finding (§3.6) into model-specific detail; nothing in Council's review contradicts it.

**Position:** source identity facts — `CLOSED_WITH_EVIDENCE`, converged. Constraint-coverage detail — `CLOSED_WITH_EVIDENCE` (Special-Team-original, consistent with and sharpening Council's general finding). Migration disposition (live/history/both) — `CARRY_FORWARD` (Council-flagged, outstanding, unaddressed either way this cycle).

### 3.4 Idempotency — What Actually Exists (Record-State and Concurrency)

Two genuine protective mechanisms were independently traced to source this cycle.

**Concurrency.** `_update_available_quantity()` (`stock_quant.py`, ~line 1082) calls `try_lock_for_update(...)` before mutating an *existing* quant row — a real pessimistic row lock. Special Team traced this directly and independently this session; Council's review cites the identical fact but attributes its original discovery to IDR-007's prior-round spot-check, treating Special Team's independent arrival at the same line as a further confirmation rather than a new discovery. Both agree the mechanism is real and both agree its coverage is partial: it protects the UPDATE-of-an-existing-bin path only. Neither review found an equivalent lock on the path that CREATEs a new bin-key row; both identify `_merge_quants()` as the already-known compensating cleanup for that narrower residual window. On this specific, narrow sub-question, Council and Special Team fully agree, and both credit it `CLOSED_WITH_EVIDENCE, strengthened`.

**Record-state idempotency.** Special Team traced `_action_done()` (`stock_move.py:2094-2158`) directly this session and found a genuine guard at line 2097 — the method filters its working set to moves whose state is `not in ('done', 'cancel')` before doing any quantity-affecting work, so re-invoking it on an already-done move is a safe no-op for that record. Special Team labels this explicitly **record-state idempotency**: real, source-verified, worth crediting. Council's parallel review does not dispute this specific mechanism — Council's own findings acknowledge "a full inventory of 7 quantity-remaining-based guards exists" — but Council's framing of the same underlying evidence, inherited verbatim from DR-002's original A13/A6 language and left unchanged across five subsequent corrective rounds, rates the guard set as a whole "PARTIALLY SUPPORTED, not VERIFIED," on the grounds that "no explicit already-processed-abort exception/guard was found anywhere." This is the first thread of the disagreement in §2.2: Special Team's fresh trace credits `_action_done()`'s state filter as exactly the kind of guard DR-002's original language said it could not find; Council's review carries forward the more skeptical original characterization without having re-traced `stock_move.py` line-by-line itself this cycle.

Both reviews independently draw the same crucial boundary around this credit: record-state idempotency protects only against re-processing an **existing** record a second time. It does nothing to stop a retried or replayed migration/import step from **creating** a second record for the same source transaction, because no natural or external key exists anywhere in the reference model to recognize the second record as a duplicate of the first. That absence — source-identity idempotency, distinct from record-state idempotency — is where both reviews agree the real, unresolved gap lives (§3.5).

**Position:** concurrency/row-locking — `CLOSED_WITH_EVIDENCE`, converged. Record-state guard credit — `CONFLICTING` in framing only: Special Team credits it as a genuine, verified mechanism; Council's inherited framing rates the broader guard bucket PARTIALLY SUPPORTED. The disagreement is about how much weight this mechanism should carry, not whether it exists.

### 3.5 Idempotency — What Does Not Exist (Source-Identity Provenance and Migration Replay)

Set against §3.4, both reviews are unambiguous that source-identity idempotency — a natural or external key letting a migration/import process recognize "I have already created a record for this source transaction" — does not exist anywhere in the reference Inventory data model. Council cites DR-002 A12 §10: no source Inventory record (`stock.move`, `stock.quant`, `stock.picking`) carries an external-reference or provenance field; the source uses plain internal integer IDs only, and DR-002 states outright that a migration "will need to introduce its own provenance/external-ID mapping layer — the source does not provide one natively." Special Team's independent contribution this cycle is a concrete, additional instance of the identical conclusion: a full read of `stock.reference` — the source's `procurement.group` substitute, and the natural place a grouping/dedup key might have lived — found zero uniqueness constraint on its `name` field and no external-system identifier field of any kind.

Where the two reviews part is not on this fact but on what it means for the reopen right now — the most consequential disagreement in this entire track's record (full framing in §2.2). Council treats the combined absence as "the single weakest point in the whole chain for this mandate," un-advanced across five corrective rounds, and argues it should become a named, first-class functional requirement for Team B given the Charter's Zero-Tolerance ruling on duplicate-posting-by-replay. Special Team, having performed the fresh re-scrutiny Council's review found missing, reaches the same factual floor but characterizes the residual item as "a material gap confirmed," routed onward to Team A/Migration design — not, in Special Team's own words, "an Inventory Evidence Gate blocker on its own."

Migration/import replayability specifically — can an extraction or load job be safely re-run without duplicating its effect — deserves its own note. Council's review states plainly this question "has never been raised as a research question anywhere in the nine-branch chain," distinct from and narrower than the operational retry-idempotency question, and poses it as genuinely open in Council's own material questions: is it even in scope for this track, or silently assumed to belong to a future Migration Factory phase? Special Team's item table answers exactly that open question, this cycle, for the first time in the chain: replayability was checked directly against `stock.move`, `stock.quant`, `stock.picking`, and `stock.reference`, and confirmed absent as a reference-system mechanism. Read together rather than in isolation, this is less a contradiction than the reopen process working as intended — Council (blind) asks whether the question has ever actually been asked; Special Team (blind, same cycle) turns out to be the answer. What remains genuinely unresolved, and is for Boss to weigh: whether that now-confirmed gap is severe enough to hold the Inventory Evidence Gate on its own, or is correctly scoped out to a later Migration/Team A design phase.

**Position:** `CONFLICTING`. The underlying fact — no native mechanism exists, and none has yet been designed — is fully converged and would be `CLOSED_WITH_EVIDENCE` in isolation. The open item is the severity/ownership judgment layered on top, which the two blind reviews resolve differently and which this document does not arbitrate.

### 3.6 Negative Stock, Over/Under-Fulfillment, and Schema-Level Integrity

Both reviews independently confirm, at the schema level, that no DB CHECK constraint prevents a negative `stock.quant.quantity`, no unique index prevents a duplicate (product, location, lot, package, owner) bin, and — per DR-002's A13 register, which both reviews treat as controlling — nothing prevents a delivered or received quantity from exceeding an ordered or demanded quantity. Special Team's independent read of `stock_quant.py:793-832` adds the specific clamp mechanism behind the on-screen "available" figure (`allow_negative=False` by default) without finding any DB-level guard behind it — corroborating, not contradicting, Council's citation of DR-002 A2/A13.

Where the two reviews part is the empirical question sitting behind these schema facts: has any of this actually happened in the real source data? Council's review carries forward `N-DB-01` — DR-002's own attempt to restore the actual source database, blocked by a sandbox permission control rather than data inaccessibility — as an unresolved item, open since DR-002, carried through IDR-007's own independent recount, never escalated as a request for the elevated permission that would close it. Special Team's session does not mention `N-DB-01`, the sandbox-permission blocker, or any attempt at empirical/data-level testing anywhere in its record. This is not a contradiction — Special Team does not claim the empirical question is resolved — but it is a coverage gap worth naming plainly: the one review that raised this question got no independent corroboration or challenge on it this cycle, and it should not be read as resolved simply because the second review was silent on it.

The over/under-fulfillment invariant specifically warrants separate treatment, because Council's review surfaces a distinct, procedural finding Special Team's review does not address at all: DR-002's own A13 register named the absence of any over/under-fulfillment guard as one of "the four strongest, most consequential invariant-gap candidates" in the entire evidence package — yet it was never assigned an identifier in the master Unknown/Conflict register (`A14`), and consequently has no owner and no disposition in any of CORR-005, CORR-006, CORR-007A, or CORR-007B's final tables. Council's own language is that it "fell through the seam" between the forward-looking invariant-candidate register and the actively-tracked gap register. This is a governance/process finding as much as a technical one, unique to Council's review; Special Team's session neither corroborates nor disputes it, not having examined the `A14` register's own completeness this cycle.

**Position:** schema-level constraint absence (negative quantity, duplicate bin, over/under-fulfillment) — `CLOSED_WITH_EVIDENCE`, converged as fact. Empirical incidence in real data — `UNKNOWN`, carried forward from Council's review, un-corroborated and un-contradicted by Special Team's silence. Over/under-fulfillment process-tracking gap — `REOPEN_ELIGIBLE`, a Council-original finding surfaced here because no subsequent round, including this cycle's Special Team pass, has given it a disposition.

### 3.7 Historical Continuity and Inventory-to-GL Reconciliation (N-A12-01)

This is the one item where both reviews explicitly decline to re-litigate and instead defer to the same standing, previously-escalated disposition: `N-A12-01 = HIGH FUNCTIONAL DESIGN GAP — REOPENED`, per Boss's own explicit ruling carried in the CORR-007B evidence. Sub-item E (Inventory-valuation-to-GL reconciliation) and sub-item F (opening-balance carry-forward across a migration or fiscal-year cutover) are both explicitly labeled **NOT PROVEN** in that controlling evidence. Both reviews independently confirm — rather than re-derive from scratch, consistent with the Council Charter's no-repeated-question rule — that this disposition is correct and should not be treated as closed by the substantial mechanism-proof work already done elsewhere around lock-dates, closing crons, and valuation-posting gates, which the evidence itself is careful to say it does not resolve.

Special Team's session adds one piece of new, firsthand evidence rather than contesting the item's status: a direct re-performance (not a citation) of `stock_valuation_report.py`'s `action_print_as_pdf()` and `action_print_as_xlsx()` methods (lines 140-144) confirms these are literally two-line stub methods that `return` with no body. The one purpose-built Inventory-to-GL reconciliation report in the reference system — covering Initial Balance, Ending Stock, Loss, and Variation — cannot produce an exportable, archivable audit artifact. This independently reconfirms, by direct re-performance, the finding CORR-007B's evidence chain already carried as item `G-7`; Council's review cites the same `G-7` finding by reference to CORR-007B rather than re-opening the file itself this cycle. No disagreement exists between the two reviews on this item.

**Position:** `REOPEN_ELIGIBLE` — both reviews affirm the standing REOPENED status; neither review is this track's authority to close it, and neither attempts to. This item is owned by the Boss/Accounting-Inventory cross-proof track, with Track 04's role limited to confirming it remains open from the IDTM/reconciliation-identity lens and reconfirming the `G-7` export-artifact defect.

### 3.8 Orphan / Migration-Invalid States and the Stockable-Consumable-Service Routing Edge Case

Council's review confirms a specific extraction-risk finding from DR-002 A12 §11: `stock_move_line.move_id`'s foreign key is `ON DELETE SET NULL`, not cascading or restricting, and no unique index protects the quant bin key — meaning a migration extraction performed via direct SQL (bypassing the ORM) could encounter orphaned lines, duplicate bins, or negative quantities the application layer would otherwise have blocked. No target extraction-defense design was found in any branch reviewed. Separately, `GRPA-M15`'s PO-line provenance-drift finding — a good model of rigor in this evidence chain — is treated identically by both reviews: closed via a fresh, independently re-run full-tree grep, with the disputed `purchase_request_id` column correctly classified as a legacy-orphan via FK-plus-relation-table-plus-module-family structural inference, explicitly labeled as inference rather than a located field, and an appropriately scoped data-content check carried forward to Team A's Migration Data Profiling work rather than silently closed. Special Team's session accepted this disposition as-is and did not re-litigate it, consistent with the Special Team Investigation Rule for items already closed with evidence.

Special Team's own original contribution here is narrower and self-labeled as speculative: a read of `product.write()` (stock module, lines 1131-1150) found that promoting a product to storable triggers an evidenced backfill/reconciliation (`_reset_inventory()`, whose own docstring cites valuation integrity as the reason), while no equivalent triggered cleanup was found in the code paths read this session for the reverse direction — demoting a product away from storable. Special Team is explicit this is a scoped, non-exhaustive observation (a full constraint search for a blocking guard on the reverse direction was not completed), offered as a concrete edge case for Team A/Team B attention on the still-open Stockable/Consumable/Service routing hypothesis (`INV-FP-13`), and explicitly not a verdict on the underlying business-reality question, which the project's own tracking reserves for Track 02/Track 03 plus a dedicated deliverable. Council's review does not mention this finding; it is new this cycle, and nothing in Council's review contradicts it.

**Position:** orphan/migration-invalid extraction risk — `CLOSED_WITH_EVIDENCE` (risk identified), defensive-handling design itself `CARRY_FORWARD` (no target design found by either review). `GRPA-M15` — `CLOSED_WITH_EVIDENCE`, with a named `CARRY_FORWARD` data-content check owned by Team A. Reclassification asymmetry (`is_storable`) — `CARRY_FORWARD`, Special-Team-original, non-exhaustive, feeds `INV-FP-13` rather than standing alone.

### 3.9 Scope Characterization Revisited: Is This EXPERT IDTM Deep Test Matrix Execution?

One further point belongs in the findings record, not only in §2.3, because it shapes how every other finding in this document should be read. The project maintains a formal, Boss-approved `EXPERT_IDTM_CHARTER.md` defining a 100%-AI-execution, 10-dimension Deep Test Matrix; Dimension 2 ("Inventory Conservation & State") and Dimension 6 ("Integration & Idempotency") map directly onto this track's mandate. Council's review is explicit and unambiguous that nothing reviewed this cycle is, or should be mistaken for, that formal execution: the Charter's own gate requires a built Team C implementation to test against, which does not exist yet for Inventory, and Team B design is not even authorized. Every finding Council's review discusses is source-code-reading evidence about the Odoo reference system, not executed-test evidence about SMEsPlus's own system; at this stage, "deep testability" can only mean "are the future test preconditions well identified," not "has deep testing occurred."

Special Team's own narrative opens with a related but differently-framed observation: DR-002's own A13 register was explicitly authored to feed "future EXPERT IDTM test-matrix design," stating "only EXPERT IDTM executes formal test matrices," and Special Team characterizes its own session as "the first Special Team session under the new 9-Veto governance to close that loop," stating plainly, "this session is that pass." Read on its own, this framing risks being understood as a claim that formal EXPERT IDTM execution has now occurred for Inventory.

It should not be read that way, and this document adopts Council's framing as governing for exactly this reason. Special Team's own described methodology, set out in its own words elsewhere in the same report, matches Council's characterization precisely rather than contradicting it: every finding is "Reference-Only, source-and-line cited against the Odoo reference snapshot... for business-and-technical-semantic learning purposes only"; the track "made no code changes, executed no database restore or live query"; nothing was tested against a built SMEsPlus/Team C system, because none exists. What Special Team's session genuinely accomplished — real, valuable, and credited plainly rather than inflated or discarded — is closing a previously five-rounds-stagnant scrutiny gap on DR-002's A13 invariant-candidate register through fresh, independent, primary-source re-verification of the reference system. That is pre-design evidence-gathering of real value to a future Team B design and a future, genuine EXPERT IDTM execution once Team C exists. **It is not that execution itself.** This document's status line and closing statement reflect Council's more conservative framing for exactly this reason: to prevent any reader — including Boss, at the moment of Gate decision — from mistaking thorough reference-system research for the formal, Charter-defined, post-implementation deep-testing pass the mandate's own name evokes.

**Position:** `CARRY_FORWARD`, with an explicit framing note. Nothing here changes any Gate posture; the formal EXPERT IDTM 100%-AI Deep Test Matrix execution against a built Team C implementation remains entirely future work, unstarted.

### 3.10 Evidence-Chain Currency

Both reviews independently flag the same systemic caveat, and it applies to this document by inheritance. Council's review states the finding directly: every claim in its review was read from unmerged branches, not canonical `origin/SMEsPlus`, consistent with Track 01 (Audit VETO)'s own F-01/F-02 findings — nothing in the Inventory Identity/Reconciliation domain is yet verified on canonical. Special Team's review reaches the identical conclusion independently: CORR-007B, the controlling evidence round both reviews ground their work in, remains entirely unmerged to canonical (tip `0eb78c68` on `audit/inventory-core-corr007b-3high-closure-010`), consistent with Track 01's F-01 finding. Every source-line citation in this document — including the new ones Special Team's fresh reference-code reads contribute this cycle — currently lives only on execution branches pending a Boss Gate decision.

**Position:** `CARRY_FORWARD`. Fully converged, no disagreement, and structurally not this track's to resolve alone — this is Track 01 (Audit VETO)'s primary finding, and this document defers to it rather than duplicating its authority.

---

## 4. Clean-Room Impact Statement

Both reviews independently assess Clean-Room impact as **LOW / well-contained**, and neither raises a violation, a near-violation, or a disagreement with the other on this point — this is one of the most solidly converged sections of the entire Track 04 record.

**What both reviews confirm.** Every migration-identity, provenance, quantity, UOM, lot/serial/package, and idempotency finding in both inputs is explicitly and repeatedly framed by its own source documents as reference-system business-semantic evidence, not SMEsPlus target design. Council cites DR-002's A12 deliverable stating outright, "No target Migration Factory implementation is designed here," and A4/A6 stating, "No vendor state machine is proposed here as SMEsPlus target design." Special Team's own report states plainly that every finding is "Reference-Only, source-and-line cited against the Odoo reference snapshot... for business-and-technical-semantic learning purposes only," and that the track "made no code changes, executed no database restore or live query." Neither review found source code, schema DDL, ORM class structure, or naming patterns copied into any SMEsPlus deliverable. The Boss `bh_*`/`bhpro_*` exclusion ruling is honored consistently everywhere both reviews checked; neither review touched or referenced that excluded source family, and IDR-007's own prior honest admission that it could not locate `bh_*` module source on the available machine — rather than reading it and withholding the result — is cited by Council as itself a clean, non-violating outcome.

**One nuance both reviews converge on, from different angles.** Because Odoo's own source has no idempotency-key mechanism and no external-ID/provenance layer for Inventory records at all (§3.5), there is, as Council puts it, "nothing here for a future Team B design to inadvertently clone" on this specific point — the absence itself removes a cloning risk, but correspondingly increases the burden on Team B to originate a wholly new, clean-room mechanism for both idempotent migration import and durable record provenance, since no reference pattern exists to responsibly adapt even at the level of business semantics. Special Team reaches the same place from its own angle and adds two specific framing guardrails worth carrying forward: first, the finding that `stock.picking` carries a real DB-level uniqueness constraint while `stock.quant`/`stock.lot`/`stock.package`/`stock.reference` do not (§3.3) is reported strictly as a fact about the reference system's own uneven constraint coverage, **not** a proposal to copy Odoo's constraint set into SMEsPlus — SMEsPlus's own schema, not yet authored, has full latitude to adopt a different, stronger, or differently-scoped strategy; second, the finding that no Inventory record carries a native external-reference/provenance field is a fact about the source's absence of a migration-replay key, **not** a specification for what SMEsPlus's own idempotency-key design should look like — that remains an original SMEsPlus/Team A decision this track does not make and does not imply.

**`GRPA-M15`'s inference-based closure** (§3.8) is likewise handled correctly by both reviews: the legacy-OCA-module-family classification is presented as inference from structural evidence (foreign key plus relation-table plus module-family match), not as copied code or a copied design pattern, and both reviews accept this distinction without qualification.

**Reconciled Clean-Room Impact: LOW / well-contained.** No violation or near-violation identified by either review. The one substantive nuance — an absent reference pattern shifts the burden onto Team B to *originate*, rather than *adapt*, a clean-room idempotency/provenance mechanism — is not a Clean-Room concern in itself, but a downstream design-scoping consequence worth carrying into whatever functional requirement eventually gets written for it.

---

## 5. Item Classification Table

Taxonomy per the Council Charter's 6-way classification: `CLOSED_WITH_EVIDENCE` / `CARRY_FORWARD` / `REOPEN_ELIGIBLE` / `CONFLICTING` / `UNKNOWN` / `SUPERSEDED`.

### 5.1 Identity & Traceability

| Item | Classification | Alignment | Evidence Basis |
|---|---|---|---|
| Quantity identity model — Stock Truth (`stock.quant` bin key; on-hand/reserved/available/demand/done qty) | `CLOSED_WITH_EVIDENCE` | Converged — 3 independent reads (DR-002, IDR-007, Special Team) | DR-002 A3; `stock_quant.py:78-122` |
| UOM conversion & rounding — structural facts (no `uom.category`; tree-based; global rounding precision) | `CLOSED_WITH_EVIDENCE` | Converged | DR-002 A3 §3/A5 §6; `uom_uom.py:218-230,62-67` |
| UOM conversion-factor historization risk (`relative_factor` not retroactive) | `CARRY_FORWARD` — no design yet | Special Team original; not contradicted | `uom_uom.py:79-93` |
| Lot/serial/package — source identity facts (tracking gate; no `product.packaging`; history vs. live package) | `CLOSED_WITH_EVIDENCE` | Converged | DR-002 A5 §7,9/A12 §3 |
| Lot/serial/package — migration disposition (live state vs. history snapshot vs. both) | `CARRY_FORWARD` — unaddressed since DR-002 | Council-flagged; not revisited this cycle | DR-002; open since first raised |
| Identity-constraint coverage across 4 core models (DB-level vs. ORM-level vs. reactive) | `CLOSED_WITH_EVIDENCE` | Special Team original; refines Council's general schema finding | `stock_picking.py:710-713`; `stock_lot.py:103-126`; `stock_quant.py:217-223`; `stock_package.py:25` |
| Traceability link fields (`returned_move_ids` / `produce_line_ids`, GRPA-M11/M12) | `CLOSED_WITH_EVIDENCE` | Council-sourced; not re-examined by Special Team, not contradicted | CORR-006 §5.1-5.2 |

### 5.2 Idempotency & Migration Integrity

| Item | Classification | Alignment | Evidence Basis |
|---|---|---|---|
| Concurrency / row-locking on quant UPDATE path | `CLOSED_WITH_EVIDENCE` — strengthened | Converged — independently re-traced by IDR-007 and Special Team | `stock_quant.py` ~line 1082, `try_lock_for_update()` |
| Native external-ID/provenance field absence on source Inventory records (fact) | `CLOSED_WITH_EVIDENCE` | Converged; reinforced by Special Team's `stock.reference` citation | DR-002 A12 §10; `stock_reference.py` |
| Operational duplicate/retry idempotency (7 guards + `_action_done` state guard) — severity of residual gap | `CONFLICTING` — see §2.2/§3.4 | Diverges: Council rates PARTIALLY SUPPORTED/weakest-point; Special Team credits `_action_done()` as genuine, rates REFINED/NARROWED | DR-002 A13 §3, A6 §5; `stock_move.py:2094-2158` line 2097 |
| Migration/import replayability (safe re-run without duplicating effect) — severity & ownership | `CONFLICTING` — see §2.2/§3.5 | Diverges: Council — UNKNOWN, never raised, headline risk; Special Team — MATERIAL GAP CONFIRMED, routed to Team A/Migration | Council: silence across 9 branches; Special Team: `stock.move/quant/picking/reference` checked directly |

### 5.3 Schema Integrity & Invariants

| Item | Classification | Alignment | Evidence Basis |
|---|---|---|---|
| Schema-level absence of DB CHECK constraints (negative qty, duplicate bin, over/under-fulfillment) — fact | `CLOSED_WITH_EVIDENCE` | Converged | DR-002 A2 §2, A13 §10; `stock_quant.py:793-832` |
| Empirical incidence of negative-qty/duplicate-bin in real source data | `UNKNOWN` — blocked by `N-DB-01` | Council-flagged; un-corroborated and un-contradicted by Special Team's silence | DR-002 DB-restore attempt blocked by sandbox permission; carried through IDR-007 |
| Over/under-fulfillment invariant — enforcement fact (not enforced anywhere) | `CLOSED_WITH_EVIDENCE` | Converged | DR-002 A13 §10 |
| Over/under-fulfillment invariant — process-tracking status (never assigned an `A14` ID) | `REOPEN_ELIGIBLE` — never registered | Council-original; unaddressed by Special Team this cycle | DR-002 A13 "four strongest gap candidates"; absent from `A14` and all 5 corrective rounds' tables |

### 5.4 Reconciliation & Continuity

| Item | Classification | Alignment | Evidence Basis |
|---|---|---|---|
| Historical opening/closing stock continuity across cutover (`N-A12-01` sub-item F) | `REOPEN_ELIGIBLE` — standing REOPENED | Converged; both defer to standing disposition | CORR-007B files 03/08/13; Boss standing ruling |
| Inventory-to-GL/valuation reconciliation (`N-A12-01` sub-item E; A13 §9 reconciliation-identity candidate; `G-7` export stub) | `REOPEN_ELIGIBLE` — standing REOPENED | Converged; Special Team adds firsthand `G-7` reconfirmation | CORR-007B file 13; `stock_valuation_report.py:140-144` |

### 5.5 Extraction, Routing & Process Governance

| Item | Classification | Alignment | Evidence Basis |
|---|---|---|---|
| Orphan/migration-invalid states from raw-SQL extraction (FK `ON DELETE SET NULL`, no unique index on bin key) | `CLOSED_WITH_EVIDENCE` (risk) / `CARRY_FORWARD` (defense design) | Converged on risk; neither review found a target design | DR-002 A12 §11 |
| `GRPA-M15` PO-line provenance drift (`purchase_request_id`) | `CLOSED_WITH_EVIDENCE`, with named `CARRY_FORWARD` sub-item | Converged; Special Team accepted as-is | CORR-007B file 01 |
| Stockable/Consumable/Service reclassification asymmetry (`is_storable` promote-backfill vs. demote-no-cleanup-found) | `CARRY_FORWARD` — scoped, non-exhaustive | Special Team original; feeds `INV-FP-13`; not addressed by Council | `product.py` (stock module) lines 1131-1150 |

### 5.6 Evidence Currency & Scope Characterization

| Item | Classification | Alignment | Evidence Basis |
|---|---|---|---|
| Evidence-chain currency (all findings on unmerged branches, not canonical) | `CARRY_FORWARD` — Track 01 authority | Converged; both defer to Track 01 (Audit VETO) F-01 | CORR-007B tip `0eb78c68`; DR-002 tip `b31597fa` |
| Characterization of this cycle's work vs. the formal EXPERT IDTM Deep Test Matrix (Charter Dimensions 2/6) | `CARRY_FORWARD` — framing note, see §2.3/§3.9 | Diverges in self-characterization only; described methodology is consistent | `EXPERT_IDTM_CHARTER.md`; `A13_CROSS_DOMAIN_INVARIANT_CANDIDATE_REGISTER.md` |

---

## 6. Consolidated Open Risks and Material Questions Carried to Boss

### 6.1 Open Risks / Holds

- `N-A12-01` = HIGH FUNCTIONAL DESIGN GAP — REOPENED (standing Boss ruling). Sub-items E (valuation-to-GL reconciliation) and F (opening-balance carry-forward) explicitly NOT PROVEN. No migration cutover should cross a fiscal-year boundary until a joint Accounting × Inventory cross-proof exists (`G-5`). *[Both inputs]*
- Duplicate/retry/idempotency for Inventory operations: record-state and concurrency mechanisms are real and evidenced; no unified idempotency-key mechanism and no source-identity "already-processed, abort" guard exists for migration-replay purposes. Severity/ownership framing is contested between Council and Special Team (§2.2) — Boss should treat this as unresolved rather than adopting either framing by default. *[Both, diverging]*
- Source-to-target provenance/external-ID mapping layer for Inventory records does not exist in the source system and does not yet exist as a SMEsPlus design — a precondition for any deterministic migration-reconciliation proof. *[Both]*
- Migration/import replayability is confirmed absent as a reference-system mechanism (Special Team, this cycle), but its ownership — Inventory Evidence Gate blocker vs. routed Team A/Migration input — is unresolved (§2.2). *[Both, diverging]*
- Empirical (data-level) verification of negative-quantity, over-fulfillment, and duplicate-bin incidence in the real source dataset remains blocked by sandbox/tooling permission (`N-DB-01`), unresolved since DR-002, and received no attention this cycle from either review. *[Council; uncontested]*
- Package traceability migration disposition (live `stock.package` vs. immutable `stock.package.history` vs. both) is undecided — flagged at DR-002, never revisited, including this cycle. *[Council; uncontested]*
- The over/under-fulfillment invariant-gap candidate is untracked in the master `A14` gap register, unowned, and has no disposition anywhere in the corrective chain or this cycle's review — a process gap in its own right. *[Council-original]*
- Identity-constraint coverage is uneven across Inventory's core models: `stock.picking` has a real DB-level unique constraint; `stock.quant`, `stock.lot`, `stock.package`, and `stock.reference` do not, relying only on ORM-level or reactive application-layer checks. *[Special-Team-original, consistent with Council's general schema finding]*
- The one-directional `is_storable` reclassification safety net (promote backfills; demote has no confirmed equivalent cleanup in the paths read) is a new, narrowly-scoped observation for Team A/Team B attention on the still-open Stockable/Consumable/Service routing hypothesis (`INV-FP-13`). *[Special-Team-original]*
- UOM conversion-factor changes are not retroactive to historical data — a second, distinct historical-continuity risk at the quantity-identity layer, compounding the already-standing `N-A12-01` value-continuity gap. *[Special-Team-original]*
- Evidence-chain currency: every finding in this document — including this cycle's newest Special Team source reads — lives only on unmerged execution branches, not canonical `origin/SMEsPlus`. *[Both]*

### 6.2 Material Questions for Boss's Consideration

- Given the EXPERT IDTM Charter's own Zero-Tolerance list names "duplicate financial posting caused by system failure or replay" and "critical inventory conservation/integrity violation" as Tolerance-zero categories: should Team B's eventual Inventory design mandate be required to name an explicit idempotency-key/dedupe mechanism as a first-class functional requirement from day one (Council's position), or is it correctly scoped as a Team A/Migration design input that need not independently block this Gate (Special Team's position)? **This is the central unresolved question in this document.**
- Should SMEsPlus's target design reproduce the reference system's running-ledger-boundary opening/closing model (no posted opening entry, per `N-A12-01`'s own mechanism proof), or adopt a more traditional posted-opening-balance model instead? *(Special Team, offered as evidence for Team B, not a recommendation.)*
- What deduplication key will SMEsPlus's own migration/import tooling use, given no Inventory record in the reference system carries a native external-reference/provenance/idempotency field? *(Special Team, named as a required design input.)*
- Has any session — including the Migration Factory's own Team A extraction-observation package — actually begun designing the provenance/external-ID mapping layer DR-002 itself said would be needed? No evidence of this was found in any branch reviewed by either input. *(Council.)*
- Has any session actually requested the elevated container/DB permission needed to close `N-DB-01`, or has it become a permanent gap by default inertia rather than active decision? *(Council.)*
- Does Track 06/Track 03's ownership of `N-A12-01` already encompass the full IDTM reconciliation-identity angle (A13 §9's "Inventory-to-Accounting reconciliation identity" candidate), or does that candidate need its own explicit tracked item distinct from `N-A12-01`'s accounting-close framing? *(Council.)*

---

## 7. Closing Statement

This document is a Track 04 (EXPERT IDTM) evidence record converging two independently-produced findings sets for Boss's eventual Gate decision on the Inventory Full Reopen. **It is a challenge/investigation finding, not a Gate decision.** Nothing in it declares Gate PASS, and nothing in it authorizes Team B design, Team C implementation, or Development to proceed on Inventory.

Council's own closing position: "Recommend HOLD, consistent with and reinforcing the existing 'Account + Inventory Backbone Reference Baseline = HOLD' disposition, with the specific additions in this review's Open Risks list... treated as first-class, named conditions of that hold rather than implicit background risk." Special Team's own closing position: "HOLD is recorded to concur with, not override, the existing... governance state, with this track's specific evidence folded in for Boss's eventual decision." Both positions point the same direction, and this document adopts both without needing to choose between them.

Where the two inputs diverge — on the severity and ownership of the idempotency/migration-replay gap (§2.2, §3.4–§3.5), and on how this cycle's own work should be characterized against the formal Charter-defined Deep Test Matrix (§2.3, §3.9) — this document surfaces both positions in full rather than resolving them. Neither divergence changes the headline verdict; both are conditions Boss should weigh explicitly rather than inherit by default from whichever input is read last.

**Terminal:** Track 04 (EXPERT IDTM) = `HOLD`. Council and Special Team converge on verdict and on the large majority of underlying findings; they diverge in severity/ownership framing on the idempotency and migration-replay gap, and in self-characterization of this cycle's own work against the formal EXPERT IDTM Deep Test Matrix — both surfaced explicitly above, neither resolved by this document. `Account + Inventory Backbone Reference Baseline = HOLD` (standing) is reinforced, not superseded. **No Gate PASS is declared anywhere in this document. Team B, Team C, and Development remain unauthorized for Inventory.** This is a Track 04 evidence record for Boss's Gate decision — not the decision itself.

---

## Sources

- **Council (challenge) findings**, Track 04 — EXPERT IDTM / Data, Identity, Reconciliation & Integrity, verdict `HOLD`, this session.
- **Special Team (investigation) findings**, Track 04 — EXPERT IDTM / Data, Identity, Reconciliation & Integrity, verdict `HOLD`, this session.
- Both inputs cite, and this document inherits by reference: DR-002 (`claude/inventory-core-backbone-dr002`, tip `b31597fa`), IER-003, CORR-005, IDR-007 (`audit/inventory-core-corr005-delta-rereview-007`), CORR-006, CORR-007A, CORR-007B (`audit/inventory-core-corr007b-3high-closure-010`, tip `0eb78c68`), and direct reads of the Odoo reference implementation at `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/{stock,stock_account,uom}`.
- Header conventions, branch topology, and the 6-way classification taxonomy cross-checked against `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` (this EXECUTION folder) for consistency with this reopen's established documentation format.
