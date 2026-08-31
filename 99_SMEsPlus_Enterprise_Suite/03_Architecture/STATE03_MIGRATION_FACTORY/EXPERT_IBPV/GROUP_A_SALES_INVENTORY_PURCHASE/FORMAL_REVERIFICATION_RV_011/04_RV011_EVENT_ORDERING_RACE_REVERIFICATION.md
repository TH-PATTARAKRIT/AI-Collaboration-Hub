> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 04 — `FV006-EVT-004` EVENT ORDERING RACE RE-VERIFICATION (RV11-01)

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D04`

## 00 — Original Finding, Independently Re-Read

`FV006-EVT-004` (`FV_006/05_EVENT_FLOW_VERIFICATION_MATRIX.md` §4, Major, `GAP FOUND`, Blocking: Yes), reproduced
here from Formal IBPV RV-009 Deliverable 06 §04 and Deliverable 03 (not from CORR-010's own restatement): a user
confirming a Commercial Commitment and then immediately editing the line's Ordered quantity fires two
Sales-originated events — `Commercial Fulfillment Requested` and `Commercial Line Quantity Changed` — in quick
succession, with no stated ordering guarantee between them; out-of-order processing could leave a Movement
Instruction silently retaining the pre-edit quantity. RV-009 additionally found CORR-008's own ordering clause
(`09`§00A) self-contradictory for exactly this same-line/different-event-type case.

## 01 — Corrected Text, Independently Read

`09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §00A, current state (read directly, not via CORR-010's file 30
paraphrase): the ordering clause now states two rules — "no cross-line, no cross-document ordering guarantee"
(unchanged) and "same-line events, any event type: ordering-independent-by-design" — under which any event whose
consuming effect depends on a value-bearing field is a **trigger to reconcile**, never a **carrier of the value
to apply**; the consumer must read the line's then-current authoritative field values at the moment of
processing, never a value captured in the event's payload.

## 02 — Independent Counterexample Test

**Setup**: Commercial Commitment line, Ordered = 10, confirmed. Two same-line, different-typed events are
generated: `Commercial Fulfillment Requested` (F) and `Commercial Line Quantity Changed` to 15 (Q).

**Case A — F processed before Q**: F's handler creates the Movement Instruction; per §00A it must read the
line's *then-current* Ordered quantity at the moment of processing. If Q has not yet been applied to the line's
own authoritative record when F is processed, the line still reads 10 at that instant — planned quantity = 10.
When Q is subsequently processed, §00A requires the same reconciliation: re-read current Ordered (now 15) and
adjust the existing Movement Instruction accordingly — planned quantity becomes 15. **Final state: 15.**

**Case B — Q processed before F**: Q is a reconciling event with no Movement Instruction yet in existence. §00A's
own text states this is "a safe no-op, since the eventual instruction creation itself reads current state." When
F is subsequently processed, it creates the Movement Instruction by reading the line's then-current Ordered
quantity — which, at that point, already reflects Q's edit (15). **Final state: 15.**

**Result: both orderings converge on the same final state (15), independently confirmed by tracing the rule's
own text against both processing orders — no counterexample found.** This matches the CORR10-01 oracle stated in
CORR-010's own file 30 exactly ("Ordered=10 → Q to 15 processed strictly before F → resulting Movement
Instruction quantity is 15, not 10, regardless of order"), but this session derived the result independently by
tracing both orderings against the rule's text, not by taking the stated oracle on faith.

## 03 — Checklist (Governing Prompt §5, RV11-01)

| # | Question | Independent finding |
|---|---|---|
| 1 | Does the corrected rule remove the self-contradictory FIFO/no-ordering wording? | Yes — the old two-clause contradiction (line-scoped FIFO vs. no cross-type guarantee) is replaced by one rule that makes ordering immaterial rather than asserting a guarantee. Independently confirmed by direct re-read; zero occurrences of the old contradictory phrasing found anywhere in `09`. |
| 2 | Is correctness genuinely ordering-independent for same-line, different-event-type arrival? | Yes — proven by the counterexample trace in §02 above for both orderings. |
| 3 | Does the consumer re-read current authoritative state rather than apply stale event-carried values? | Yes — stated explicitly ("never a value captured in the event's own payload at emission time") and consistent with the same pattern already used for Movement Instruction actual-so-far quantity (`05`§01) and line-level remaining quantity (`06`§03). |
| 4 | What happens if quantity-change arrives before fulfillment-request? | Explicitly addressed — no-op, since the later-created instruction reads current state (§02 Case B). |
| 5 | What happens on replay/redelivery? | Composes with the idempotency invariant (`12`§11) without contradiction — independently checked: a repeat of the *same* specific event (same business identity) is a safe no-op per idempotency; a *different* same-line event still triggers its own (idempotent) reconciliation. These are orthogonal axes (identity-of-event vs. type-of-event) and the text does not conflate them. |
| 6 | Does idempotency still apply? | Yes — explicitly cross-referenced (`FV006-INT-001`), and independently confirmed not to conflict with the reconciliation rule (§05 above). |
| 7 | Does unresolved handoff remain separately observable, not masked? | Yes — §00A states explicitly that total non-delivery of the first handoff is caught by `Handoff Unresolved` (`FV006-INT-002`, §03A), "a distinct failure mode from mis-ordering, which this rule does not need to, and does not, address." |
| 8 | Is the design technology-neutral? | Yes — no lock, queue, compare-and-swap, or messaging mechanism named anywhere in the corrected text (independently confirmed by direct read). |
| 9 | Are all cross-references correct? | Independently checked: `09`§00A's self-citation of the nonexistent `§04A` is now `§03A` (correct — `09`§03A exists and is the Handoff Reconciliation Events section). `09`§00A/§03A's citation of `12`§13 for the handoff-failure section is now `12`§13A (correct — `12`§13 is the distinct, still-unrelated SLA-lateness section, confirmed by direct read of `12`§13 vs §13A). Zero stale cross-references found in a targeted grep-equivalent read of `09`, `08`§12, `12`§11/§13/§13A. |

## 04 — Registration Check

`18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §07 was read directly (not via CORR-010's paraphrase): item
`N10` records `FV006-EVT-004` as `CLOSED BY TEAM B CORRECTION (CORR-010)`, citing the exact corrected section
(`09`§00A) and the exact mechanism (trigger-to-reconcile, not carrier-of-value). Independently confirmed accurate
against the corrected text itself, not merely present as a register entry.

## 05 — Verdict

**`VERIFIED`.** The ordering-clause self-contradiction Formal IBPV RV-009 found is genuinely eliminated, and the
replacement rule independently survives an explicit two-ordering counterexample trace for the exact scenario
`FV006-EVT-004` describes. The design is technology-neutral, composes correctly with the idempotency and
handoff-unresolved mechanisms without overlap or contradiction, and is correctly registered in file 18 with
accurate cross-references. This is a design-level closure, appropriately scoped — it does not, and does not need
to, prescribe an implementation mechanism to satisfy the finding.

No residual unknown material to this finding's own scope was found on independent re-performance.

**Gate impact**: this finding no longer independently blocks Development. It was the one item Formal IBPV RV-009
(D11 item C1) classified as narrowly blocking Team C specifically because of the "actively mistracked" pattern —
that mistracking is independently confirmed corrected (§04 above), and the underlying design gap is independently
confirmed closed (§02–§03 above).
