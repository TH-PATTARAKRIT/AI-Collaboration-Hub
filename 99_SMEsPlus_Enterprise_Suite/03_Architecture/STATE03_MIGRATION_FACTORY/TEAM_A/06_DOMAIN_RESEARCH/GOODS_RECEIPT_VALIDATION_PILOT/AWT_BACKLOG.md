> Domain: GOODS_RECEIPT_VALIDATION_PILOT | AWT Backlog (Boss Order 2026-09-28, §6) | Not executable in this container — prepared for later authorized environment

# AWT BACKLOG — Gx1 (Goods Receipt Validation)

Per Boss's order §6: for every function requiring later Atomic White-box Trace, prepare the hypothesis and runtime plan now, so no documentation research needs repeating once an authorized Odoo 19 Community environment exists (`BGQ-04` in `STATE03_BOSS_GATE_QUEUE.md`). Nothing below has been executed; every "current V" is unchanged from `25_TEAM_A_DOMAIN_STATUS.md`.

---

### GRV-F02 — Physical receipt execution

- **Criticality**: C2
- **Hypothesis to verify**: A draft/expected receipt has zero stock or financial effect; only a validated ("done") receipt moves quantity into a stock-owned location.
- **Required environment**: Odoo 19 Community, Inventory app installed, one warehouse, one-step routing.
- **Configuration prerequisite**: Multi-Step Routes disabled (baseline one-step case first).
- **Runtime action**: Create a Purchase Order for a stockable product; confirm; open the generated receipt; validate.
- **Expected observable result**: On-hand quantity increases only after Validate is clicked, not on PO confirmation.
- **Cross-module observation**: Purchase Order's "Received" quantity field updates in step with the receipt's validated quantity.
- **Accounting/stock effect**: Depends on GRV-F04's valuation mode (see below) — record whichever is observed, don't assume.
- **Reversal scenario**: None for this function alone (see GRV-F07/GRV-F03 for reversal/backorder AWT).
- **Evidence required**: Before/after stock-quantity snapshot; UI state transition screenshot or log.
- **Target V**: V4 (floor V3) | **Current V**: V2 | **Missing proof**: Runtime confirmation of the draft-vs-done boundary.

### GRV-F03 — Partial receipt / backorder handling

- **Hypothesis to verify**: Receiving less than ordered requires an explicit user action (edit quantity + validate, or explicit split) to create a backorder; it is not silent/automatic.
- **Required environment**: Same as GRV-F02.
- **Configuration prerequisite**: None beyond a PO with quantity > 1.
- **Runtime action**: Confirm a PO for qty 10; on the receipt, edit received quantity to 6; validate; observe prompt/behavior.
- **Expected observable result**: A backorder record for qty 4 is created, linked to the original PO, in draft/expected state.
- **Cross-module observation**: Original PO's received-quantity tracking reflects 6/10 until the backorder is itself processed.
- **Accounting/stock effect**: The 6 units follow GRV-F04's valuation path; the 4 units have no effect until their own backorder receipt is validated.
- **Reversal scenario**: Cancel the backorder before receiving — confirm this doesn't retroactively affect the already-received 6 units.
- **Evidence required**: Backorder record ID/link; state before/after the edit+validate action.
- **Target V**: V4 (floor V3) | **Current V**: V2 | **Missing proof**: Runtime confirmation that backorder creation is action-triggered, not silent.

### GRV-F04 — Inventory valuation at receipt

- **Criticality**: C1
- **Hypothesis to verify**: Under the default (manual/periodic) valuation, a receipt's validation creates **no** immediate journal entry; under automatic/perpetual valuation, it does. **Open sub-hypothesis (raised during Gx2/Sales Delivery research, cross-referenced here as a Material Delta)**: Odoo 19 may have changed perpetual valuation to post at *invoice* time rather than at *physical movement* time — this directly contradicts the simpler "perpetual = real-time-at-movement" assumption this pilot originally recorded, and must be resolved by the same AWT pass. See `SALES_DELIVERY_VALIDATION_PILOT/22_UNKNOWN_AND_GAPS.md` GAP-SDV-01 for the full contradiction record.
- **Required environment**: Same as GRV-F02, plus Accounting app installed, one Product Category with each of (Manual, FIFO), (Automatic/Perpetual, FIFO).
- **Configuration prerequisite**: Two product categories, each valuation/costing combination isolated per category to avoid cross-contamination.
- **Runtime action**: Receive the same product/quantity under each of the two category configurations; check Accounting → Journal Entries immediately after each Validate, and again only after posting a vendor bill for the perpetual case.
- **Expected observable result**: Manual case — no journal entry until a human posts one. Perpetual case — resolve whether the entry appears at receipt-validate time or only at bill-post time (this is the open contradiction).
- **Cross-module observation**: Which account is debited/credited (interim/clearing vs. stock valuation vs. price-difference) under each mode.
- **Accounting/stock effect**: This function's entire purpose is to observe the accounting effect — primary target of this AWT unit.
- **Reversal scenario**: Cancel/return the receipt after validation under perpetual mode; confirm whether a reversing entry is automatic or requires manual action.
- **Evidence required**: Journal entry list (or explicit absence) at each checkpoint, per configuration.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: The single most important open question in this pilot — full runtime resolution of the perpetual-valuation-timing contradiction.

### GRV-F05 — Landed cost allocation onto received goods

- **Criticality**: C1
- **Hypothesis to verify**: Landed cost application is gated by costing method (FIFO/AVCO required) regardless of valuation mode (manual or automatic both work).
- **Required environment**: Same as GRV-F04, plus a landed-cost-eligible product category (FIFO) and a Standard-costing category (control case expected to fail/be unavailable).
- **Configuration prerequisite**: A landed cost record type configured and linked to a completed receipt.
- **Runtime action**: Attempt to apply a landed cost to a receipt under (a) FIFO + Manual valuation, (b) FIFO + Automatic valuation, (c) Standard costing method.
- **Expected observable result**: (a) and (b) succeed; (c) is blocked or unavailable.
- **Cross-module observation**: Resulting valuation adjustment amount and account entries for (a) vs (b).
- **Accounting/stock effect**: Adjusted per-unit cost of the already-received stock.
- **Reversal scenario**: Reverse/cancel a landed cost entry; confirm valuation reverts.
- **Evidence required**: Screenshots/logs of the block on (c); valuation before/after for (a)/(b).
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Runtime confirmation of the gating condition and the exact allocation account behavior.

### GRV-F06 — Three-way match / bill control policy

- **Criticality**: C1
- **Hypothesis to verify**: Three-way matching is an informational flag (`Should Be Paid` / `Exception`) on the vendor bill, not a hard block on bill creation, editing, or payment execution.
- **Required environment**: Same as GRV-F02, plus Purchase app "received quantities" Bill Control Policy + 3-way matching enabled.
- **Configuration prerequisite**: A PO partially received (per GRV-F03), to test bill creation against a mismatched quantity.
- **Runtime action**: Attempt to create/edit a vendor bill for a quantity exceeding what's received; attempt to register a payment against it.
- **Expected observable result**: Bill creation/edit is not blocked; `Should Be Paid` moves to `Exception`; **payment-execution behavior is the open question** — confirm whether payment can proceed despite the `Exception` flag.
- **Cross-module observation**: Whether an approval workflow or role-based control intercepts an `Exception`-flagged bill before payment.
- **Accounting/stock effect**: None directly from the flag itself; payment posting effect if allowed.
- **Reversal scenario**: N/A for this function (control-verification only).
- **Evidence required**: Whether payment registration succeeds, is blocked, or requires an extra confirmation step, with an `Exception`-flagged bill.
- **Target V**: V5 (floor V4) | **Current V**: V2 | **Missing proof**: Whether the flag has any hard-block teeth anywhere downstream, per CQS-GRV-04.

### GRV-F07 — Reversal / return of received goods

- **Criticality**: C2 (now evidence-supported per `06_BUSINESS_RULE_REGISTER.md`, see GAP-GRV-06 update)
- **Hypothesis to verify**: A pre-bill vendor return uses Reverse Transfer alone; a post-bill vendor return additionally requires a Vendor Refund/Credit Note, symmetric with SDV-F06/F07's sales-side pattern.
- **Required environment**: Same as GRV-F02, plus a validated receipt with a subsequently validated vendor bill (post-bill test case) and one without (pre-bill test case).
- **Configuration prerequisite**: None beyond having both receipt states available.
- **Runtime action**: Attempt Reverse-Transfer-only return on each; for the post-bill case, additionally issue a Vendor Refund/Credit Note and observe whether the stock-only attempt was actually insufficient as documentation predicts.
- **Expected observable result**: Pre-bill case resolves fully via Reverse Transfer; post-bill case requires the Vendor Refund/Credit Note step.
- **Cross-module observation**: Compare directly against Gx2's SDV-F06/F07 AWT results — run in the same session for comparability; also check whether the Purchase Matching smart button surfaces the returned quantity against the original bill.
- **Accounting/stock effect**: Stock reversal (both cases) + financial reversal (post-bill case).
- **Reversal scenario**: This function *is* the reversal scenario for GRV-F02.
- **Evidence required**: Step-by-step record of both paths; whether refund amount auto-populates.
- **Target V**: V4 (floor V3) | **Current V**: V2 | **Missing proof**: Full runtime walkthrough of both paths, and the Purchase Matching interaction.

---

## Backlog status

```
FUNCTIONS WITH AWT PLAN PREPARED : 6 (GRV-F02, F03, F04, F05, F06, F07)
FUNCTIONS AWAITING DOCUMENTATION FIRST : 0
FUNCTIONS NOT REQUIRING AWT (C3, config-only) : 1 (GRV-F01 — configuration surface, no runtime ambiguity to resolve beyond what documentation already states)
```

No item in this backlog may be executed without the environment queued at `BGQ-04` in `STATE03_BOSS_GATE_QUEUE.md`.
