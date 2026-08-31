# A7 — Inventory Adjustment / Physical Count / Cut-off Evidence

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Research inventory count facts, adjustment posting triggers, date/period/cutoff interaction, historical corrections, freeze/lock, audit trail | Claude (Team A, DR-002) | This artifact; `stock/models/stock_quant.py`, `stock_scrap.py` | 2026-08-31 | Independent Evidence Review (pending) | PARTIALLY VERIFIED | Directly feeds A16 Cross-Proof scenario 4 (Inventory Adjustment) |

## 1. Physical count mechanism

`stock.quant` carries the full count workflow on the same row as the theoretical on-hand quantity — there is no separate "count session"/"count document" model observed in the modules read this pass:

- `inventory_quantity` (stored) — the user-entered "Counted" quantity.
- `inventory_quantity_auto_apply` — computed/inverse pair; when set, automatically applies the counted quantity to `quantity`.
- `inventory_diff_quantity` — computed+stored, `@api.depends('inventory_quantity','inventory_quantity_set')` — the gap between theoretical and counted quantity. This is the field that would drive an adjustment posting (see A9 for the valuation-side consequence).
- This is the **only** path in this codebase to directly overwrite `stock.quant.quantity` outside the normal move-execution flow (confirmed by this pass's own reading; `product.product.qty_available`'s `inverse='_inverse_qty_available'` provides a product-level manual-edit shortcut, but it operates by creating an inventory-adjustment quant write under the hood, not a separate mechanism).

## 2. Count-in-progress vs. settled on-hand

Not independently traced this pass beyond the fields above — whether a "count in progress" state exists that freezes normal moves against a location during counting was **not evidenced** in the files read (`stock_quant.py`). GROUP A's own frozen evidence did not address this question either (their Inventory Capability Model scope was §02–§10, and count-freeze semantics do not appear in any of the reused sections). Registered `EVIDENCE_MISSING` in A14 (N-A7-01).

## 3. Adjustment posting trigger at the Inventory side

The mechanism is: counted quantity differs from theoretical → `inventory_diff_quantity` computed → applying the count creates/adjusts a `stock.move` (an "Inventory Adjustment" is itself represented as a stock move from/to the `inventory` (Inventory Loss) usage location, consistent with the same location semantics documented in A5 §2) → that move flows through the normal valuation pipeline (`_set_value()`, `_create_account_move()`) exactly like any other move once it reaches `done`. This was inferred from the consistent use of the `inventory` location-usage value across `stock_quant.py` and `stock_scrap.py`, not from directly reading an "apply inventory count" method body — **PARTIALLY VERIFIED**, not a full trace of a single method. Registered in A14 (N-A7-02) as a residual gap: the exact method that converts `inventory_diff_quantity` into a posted `stock.move` was not located and read line-by-line this pass.

## 4. Date/effective date behavior and period/cutoff interaction

Not directly evidenced this pass at the Inventory-model level (no `date`/`date_done`/period-lock field was read in `stock_quant.py`/`stock_move.py` during this specific research pass, though `stock.move` is known from A3/A4 reading to carry scheduling/date fields not enumerated here). This is a **material open item** given Lane C's Cross-Proof scenario 6 ("Period / Cut-off — Inventory physical date vs. Accounting effective/recorded date") explicitly requires this evidence. Registered `EVIDENCE_MISSING — HIGH MATERIALITY` in A14 (N-A7-03) — **not silently dropped**, explicitly flagged as blocking full confidence in Cross-Proof scenario 6 until closed.

## 5. Historical corrections

Confirmed via A4 §6: the only path to correct a `done` movement is a new Return (or, for pure quantity corrections without a commercial return, a new Inventory Adjustment move) — there is no "un-confirm/edit a done record" action anywhere in the source read this pass or by GROUP A. This is a genuine, well-evidenced fact: Inventory history in this codebase is append-only at the move level.

## 6. Stock freeze/lock concepts

Not evidenced this pass. `stock.picking.type.create_backorder` and `stock.location.usage` were read, but no field or method suggesting a period-lock or stock-freeze control was found in the files read. Registered `EVIDENCE_MISSING` in A14 (N-A7-04) — genuinely unknown, not assumed absent.

## 7. Audit trail implications

- `stock.move`'s `value_manual` inverse (`_inverse_value_manual`, in `stock_account`) writes a `product.value` audit record whenever a user manually overrides a move's valuation — a real, source-confirmed audit-trail mechanism, though scoped to valuation overrides specifically, not general count/adjustment audit.
- General field-level audit history (`mail.thread`/`tracking=True` fields) was observed on `product.template.is_storable` and `.type` (both `tracking=True`) but a full audit-trail sweep of `stock.quant`/`stock.move` was not performed this pass.

## Summary disposition

This deliverable is **PARTIALLY VERIFIED**, not fully exhausted — four residual gaps are registered honestly in A14 (count-freeze state, exact adjustment-posting method trace, date/cutoff fields, stock lock/freeze). This reflects DR-002's own instruction that a material unknown may not silently disappear merely to reach closure; A7 is reported at the depth this pass actually reached, with explicit next-action items rather than an inflated completeness claim.

No Evidence = No Progress. DELTA-FIRST.
